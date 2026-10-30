/* Checkpointed / resumable version of residue_orbits_gf2_64.c (engineering change only).

   Same statement, same field GF(2^64) = F_2[x]/(x^64 + x^4 + x^3 + x + 1), same
   Frobenius-orbit-reduced tree (one child at power-of-two depths, both elsewhere), same
   per-k stdout lines as `residue_orbits_gf2_64 KMAX` (no `validate` mode here: use the
   original binary for that).  Diagnostics go to stderr, prefixed with '#'.

   Differences (none changes what is counted):
   * Work units.  The reduced tree is expanded breadth-first to depth D (D = 24 for
     KMAX >= 30, else KMAX/2); its nodes, in blocks of W (below), are the independent units.  Node and zero
     counts are sums over units, so the order and the interruption points do not matter.
   * Checkpoint.  Every --interval seconds (default 300) the done-bitmap and the summed
     counts of finished units are written to CKPT.tmp, fsync'ed, renamed over CKPT, and
     the directory is fsync'ed (atomic: a crash leaves the old or the new file).  The file
     carries KMAX, D, the unit count, a format version and an FNV-1a checksum; --resume
     refuses a file that does not match.  Units unfinished at the crash are redone.
   * Lockstep lanes.  A unit is a block of W = 8 consecutive depth-D nodes (the last block
     may be shorter); the reduced tree below depth D has the same shape for every node, so
     the 8 subtrees are walked in lockstep (recW) and their multiplications overlap.
   * Sibling sharing.  The two children y, y+1 of a node satisfy, in characteristic 2,
     num*(y+1)+den = (num*y+den) + num and den*(y+1) = den*y + den, so each sibling pair
     costs 2 field multiplications instead of 4, and leaves (depth KMAX) need only
     num*y (no den, no solve).  Exact identities; same num/den as the original.

   Usage: residue_orbits_ckpt KMAX [--ckpt FILE] [--resume] [--interval SEC]
                                   [--stop-after-units N]   (test hook: exit 75 after
                                                             N units + checkpoint)
   Build: gcc -O3 -march=native -fopenmp -o residue_orbits_ckpt residue_orbits_ckpt.c */
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>
#include <time.h>
#include <fcntl.h>
#include <unistd.h>
#include <libgen.h>
#include <wmmintrin.h>
#include <smmintrin.h>
#include <omp.h>

static inline uint64_t gmul(uint64_t a, uint64_t b) {
  __m128i A = _mm_cvtsi64_si128((long long)a), B = _mm_cvtsi64_si128((long long)b);
  __m128i P = _mm_cvtsi64_si128(0x1B);
  __m128i C = _mm_clmulepi64_si128(A, B, 0x00);
  uint64_t lo = (uint64_t)_mm_cvtsi128_si64(C), hi = (uint64_t)_mm_extract_epi64(C, 1);
  __m128i H = _mm_clmulepi64_si128(_mm_cvtsi64_si128((long long)hi), P, 0x00);
  uint64_t l2 = (uint64_t)_mm_cvtsi128_si64(H), h2 = (uint64_t)_mm_extract_epi64(H, 1);
  uint64_t l3 = (uint64_t)_mm_cvtsi128_si64(
      _mm_clmulepi64_si128(_mm_cvtsi64_si128((long long)h2), P, 0x00));
  return lo ^ l2 ^ l3;
}
static uint64_t gmul_slow(uint64_t a, uint64_t b) {
  uint64_t r = 0;
  for (int i = 0; i < 64; i++) {
    if ((b >> i) & 1) r ^= a;
    uint64_t c = a >> 63; a <<= 1; if (c) a ^= 0x1B;
  }
  return r;
}
static inline uint64_t Nlin(uint64_t x) { return gmul(x, x) ^ x; }
static uint64_t SOL[8][256];
static inline uint64_t solveN(uint64_t z) {
  uint64_t r = 0;
  for (int t = 0; t < 8; t++) r ^= SOL[t][(z >> (8 * t)) & 255];
  return r;
}
static void build(void) { /* identical to residue_orbits_gf2_64.c, incl. self-tests */
  for (int s = 0; s < 100000; s++) {
    uint64_t a = 0x9E3779B97F4A7C15ull * (s + 1), b = 0xD1B54A32D192ED03ull * (s + 7);
    if (gmul(a, b) != gmul_slow(a, b)) { fprintf(stderr, "mul self-test failed\n"); exit(2); }
  }
  uint64_t pv[64], pc[64]; int have[64] = {0};
  for (int j = 0; j < 64; j++) {
    uint64_t v = Nlin(1ull << j), c = 1ull << j;
    while (v) {
      int h = 63 - __builtin_clzll(v);
      if (have[h]) { v ^= pv[h]; c ^= pc[h]; } else { have[h] = 1; pv[h] = v; pc[h] = c; break; }
    }
  }
  for (int t = 0; t < 8; t++)
    for (int b = 0; b < 256; b++) {
      uint64_t v = ((uint64_t)b) << (8 * t), c = 0;
      while (v) {
        int h = 63 - __builtin_clzll(v);
        if (!have[h]) { v ^= 1ull << h; continue; }
        v ^= pv[h]; c ^= pc[h];
      }
      SOL[t][b] = c;
    }
  for (uint64_t s = 1; s < 200000; s++) {
    uint64_t a = Nlin(s * 0x9E3779B97F4A7C15ull);
    if (Nlin(solveN(a)) != a) { fprintf(stderr, "solver self-test failed\n"); exit(2); }
  }
}
static int clog2(int m) { int b = 0; while ((1 << b) < m) b++; return b; }
static inline int ispow2(int j) { return j > 0 && (j & (j - 1)) == 0; }
static int KMAX;
typedef struct { unsigned long long nodes[64], zeros[64]; } Cnt;

/* node at depth i with value z and S_i = num/den; adds its descendants to c */
static void rec(uint64_t z, int i, uint64_t num, uint64_t den, Cnt *c) {
  if (i == KMAX) return;
  uint64_t y = solveN(z);
  int both = !ispow2(i + 1);
  uint64_t n0 = gmul(num, y) ^ den;               /* child y   */
  c->nodes[i + 1] += 1 + both;
  c->zeros[i + 1] += (n0 == 0);
  if (both) c->zeros[i + 1] += ((n0 ^ num) == 0); /* child y+1 */
  if (i + 1 == KMAX) return;
  uint64_t d0 = gmul(den, y);
  rec(y, i + 1, n0, d0, c);
  if (both) rec(y ^ 1u, i + 1, n0 ^ num, d0 ^ den, c);
}

/* W independent nodes at the same depth, walked in lockstep (the reduced tree's shape
   depends only on depth), so the field multiplications of different lanes overlap. */
#define W 8
static void recW(const uint64_t *z, int i, const uint64_t *num, const uint64_t *den, Cnt *c) {
  if (i == KMAX) return;
  uint64_t y[W], n0[W], n1[W], d0[W], d1[W], y1[W];
  int both = !ispow2(i + 1);
  for (int l = 0; l < W; l++) { y[l] = solveN(z[l]); n0[l] = gmul(num[l], y[l]) ^ den[l]; }
  c->nodes[i + 1] += (unsigned long long)W * (1 + both);
  for (int l = 0; l < W; l++) {
    c->zeros[i + 1] += (n0[l] == 0);
    if (both) c->zeros[i + 1] += ((n0[l] ^ num[l]) == 0);
  }
  if (i + 1 == KMAX) return;
  for (int l = 0; l < W; l++) { d0[l] = gmul(den[l], y[l]); n1[l] = n0[l] ^ num[l]; d1[l] = d0[l] ^ den[l]; y1[l] = y[l] ^ 1u; }
  recW(y, i + 1, n0, d0, c);
  if (both) recW(y1, i + 1, n1, d1, c);
}

#define MAGIC 0x52455349444b5054ull /* "RESIDKPT" */
#define FMTVER 2u
typedef struct { uint64_t magic; uint32_t ver, kmax, D, pad; uint64_t units, ndone; Cnt c; } Hdr;
static uint64_t fnv(const void *p, size_t n, uint64_t h) {
  const unsigned char *s = p; for (size_t i = 0; i < n; i++) { h ^= s[i]; h *= 0x100000001b3ull; } return h;
}
static int write_ckpt(const char *path, const Hdr *h, const unsigned char *done, size_t nb) {
  char tmp[4096]; snprintf(tmp, sizeof tmp, "%s.tmp", path);
  FILE *f = fopen(tmp, "wb"); if (!f) return -1;
  uint64_t ck = fnv(done, nb, fnv(h, sizeof *h, 0xcbf29ce484222325ull));
  if (fwrite(h, sizeof *h, 1, f) != 1 || fwrite(done, 1, nb, f) != nb || fwrite(&ck, 8, 1, f) != 1) { fclose(f); return -1; }
  fflush(f); fsync(fileno(f)); fclose(f);
  if (rename(tmp, path)) return -1;
  char dcopy[4096]; snprintf(dcopy, sizeof dcopy, "%s", path);
  int dfd = open(dirname(dcopy), O_RDONLY); if (dfd >= 0) { fsync(dfd); close(dfd); }
  return 0;
}
static int read_ckpt(const char *path, Hdr *h, unsigned char *done, size_t nb) {
  FILE *f = fopen(path, "rb"); if (!f) return -1;
  uint64_t ck; int ok = fread(h, sizeof *h, 1, f) == 1 && fread(done, 1, nb, f) == nb && fread(&ck, 8, 1, f) == 1;
  fclose(f);
  if (!ok) return -2;
  if (ck != fnv(done, nb, fnv(h, sizeof *h, 0xcbf29ce484222325ull))) return -3;
  return 0;
}

int main(int argc, char **argv) {
  if (argc < 2) { fprintf(stderr, "usage: %s KMAX [--ckpt F] [--resume] [--interval S] [--stop-after-units N]\n", argv[0]); return 1; }
  KMAX = atoi(argv[1]);
  if (KMAX < 1 || KMAX > 63) { fprintf(stderr, "KMAX must be in 1..63\n"); return 1; }
  const char *ck = NULL; int resume = 0; double interval = 300; long long stop_after = -1;
  for (int a = 2; a < argc; a++) {
    if (!strcmp(argv[a], "--ckpt") && a + 1 < argc) ck = argv[++a];
    else if (!strcmp(argv[a], "--resume")) resume = 1;
    else if (!strcmp(argv[a], "--interval") && a + 1 < argc) interval = atof(argv[++a]);
    else if (!strcmp(argv[a], "--stop-after-units") && a + 1 < argc) stop_after = atoll(argv[++a]);
    else { fprintf(stderr, "unknown argument %s\n", argv[a]); return 1; }
  }
  if (resume && !ck) { fprintf(stderr, "--resume needs --ckpt\n"); return 1; }
  build();
  int D = KMAX >= 30 ? 24 : KMAX / 2;
  Cnt pre; memset(&pre, 0, sizeof pre);
  size_t cap = (size_t)1 << (D + 1); int cnt = 1;
  uint64_t *Z = malloc(8 * cap), *NU = malloc(8 * cap), *DE = malloc(8 * cap);
  Z[0] = 1; NU[0] = 0; DE[0] = 1;
  for (int i = 0; i < D; i++) { /* same BFS as the original, counted outside the units */
    uint64_t *Z2 = malloc(8 * cap), *N2 = malloc(8 * cap), *D2 = malloc(8 * cap);
    int nc = 0, nb = ispow2(i + 1) ? 1 : 2;
    for (int q = 0; q < cnt; q++) {
      uint64_t y = solveN(Z[q]);
      for (int b = 0; b < nb; b++, y ^= 1u) {
        uint64_t n2 = gmul(NU[q], y) ^ DE[q], d2 = gmul(DE[q], y);
        pre.nodes[i + 1]++; if (n2 == 0) pre.zeros[i + 1]++;
        Z2[nc] = y; N2[nc] = n2; D2[nc] = d2; nc++;
      }
    }
    free(Z); free(NU); free(DE); Z = Z2; NU = N2; DE = D2; cnt = nc;
  }
  size_t NP = (size_t)cnt, U = (NP + W - 1) / W, nbytes = (U + 7) / 8;
  unsigned char *done = calloc(nbytes, 1);
  Hdr H; memset(&H, 0, sizeof H); H.magic = MAGIC; H.ver = FMTVER; H.kmax = KMAX; H.D = D; H.units = U;
  if (resume) {
    Hdr R; int r = read_ckpt(ck, &R, done, nbytes);
    if (r == -1) fprintf(stderr, "# no checkpoint at %s; starting fresh\n", ck);
    else if (r < 0) { fprintf(stderr, "checkpoint %s unreadable/corrupt (%d); refusing\n", ck, r); return 4; }
    else {
      if (R.magic != MAGIC || R.ver != FMTVER || R.kmax != (uint32_t)KMAX || R.D != (uint32_t)D || R.units != U) {
        fprintf(stderr, "checkpoint %s does not match this run (KMAX/D/units/version); refusing\n", ck); return 4;
      }
      uint64_t pc = 0; for (size_t i = 0; i < nbytes; i++) pc += __builtin_popcount(done[i]);
      if (pc != R.ndone) { fprintf(stderr, "checkpoint popcount mismatch; refusing\n"); return 4; }
      H = R; fprintf(stderr, "# resumed from %s: %llu/%zu units done\n", ck, (unsigned long long)R.ndone, U);
    }
  }
  fprintf(stderr, "# KMAX=%d D=%d prefixes=%zu units=%zu (blocks of %d) threads=%d\n", KMAX, D, NP, U, W, omp_get_max_threads());
  double t0 = omp_get_wtime(), last = t0; int stop = 0; long long thisrun = 0;
#pragma omp parallel for schedule(dynamic, 1)
  for (size_t q = 0; q < U; q++) {
    if (stop || (done[q >> 3] >> (q & 7) & 1)) continue;
    Cnt c; memset(&c, 0, sizeof c);
    size_t q0 = q * W;
    if (q0 + W <= NP) recW(Z + q0, D, NU + q0, DE + q0, &c);
    else for (size_t r = q0; r < NP; r++) rec(Z[r], D, NU[r], DE[r], &c);
#pragma omp critical
    {
      if (!stop) {
        for (int k = 0; k < 64; k++) { H.c.nodes[k] += c.nodes[k]; H.c.zeros[k] += c.zeros[k]; }
        done[q >> 3] |= (unsigned char)(1u << (q & 7)); H.ndone++; thisrun++;
        double now = omp_get_wtime();
        int hit = stop_after >= 0 && thisrun >= stop_after;
        if (ck && (now - last >= interval || hit)) {
          if (write_ckpt(ck, &H, done, nbytes)) fprintf(stderr, "# WARNING checkpoint write failed\n");
          else fprintf(stderr, "# checkpoint %llu/%zu units, %.0fs this run\n", (unsigned long long)H.ndone, U, now - t0);
          last = now;
        }
        if (hit) stop = 1;
      }
    }
  }
  if (stop) { fprintf(stderr, "# stopped by --stop-after-units (test hook)\n"); return 75; }
  if (H.ndone != U) { fprintf(stderr, "internal: %llu/%zu units\n", (unsigned long long)H.ndone, U); return 5; }
  if (ck) write_ckpt(ck, &H, done, nbytes);
  int bad = 0;
  for (int k = 1; k <= KMAX; k++) {
    int B = clog2(k + 1);
    unsigned long long n = pre.nodes[k] + H.c.nodes[k], zz = pre.zeros[k] + H.c.zeros[k];
    int ok = n == (1ull << (k - B)) && zz == 0;
    printf("k=%d reduced_chains=%llu orbit_size=%d chains_covered=2^%d zeros=%llu %s\n",
           k, n, 1 << B, k, zz, ok ? "ok" : "FAIL");
    if (!ok) bad = 1;
  }
  fprintf(stderr, "# done, %.1fs this run\n", omp_get_wtime() - t0);
  return bad;
}
