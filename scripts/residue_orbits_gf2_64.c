/* Frobenius-orbit-reduced exact check for the README section
   "Residue condition: Frobenius orbit reduction and exact check to k = KMAX".

   Statement checked (finite exact computation, not a proof for all k):
     for every chain z_0 = 1, z_i^2 + z_i = z_{i-1} (i = 1..k) over the algebraic
     closure of F_2, S_k = sum_{i=1}^k 1/z_i != 0, for 1 <= k <= KMAX <= 63.

   Field: GF(2^64) = F_2[x]/(x^64 + x^4 + x^3 + x + 1).  Irreducibility of the
   modulus is checked in scripts/check_residue_orbits.py.  N(x) = x^2 + x is
   F_2-linear and N^64 = F^64 + 1 = 0 on GF(2^64), with kernel {0, 1}; so every
   chain of length <= 63 lies in GF(2^64), and the roots of y^2 + y = z_{i-1}
   are y and y + 1.

   Orbit reduction (proved in the README): Frobenius F permutes the chains of
   length j, S_j(F chain) = S_j(chain)^2, and every F-orbit of length-j chains
   meets exactly once the set obtained by following ONE (arbitrary) child at every
   depth that is a power of two and BOTH children at every other depth.  So the
   reduced tree is enough for "S_j != 0 for every chain".

   S_k is carried as num/den with den = z_1...z_k != 0, so S_k = 0 iff num = 0.

   Usage:  residue_orbits_gf2_64 KMAX            -> reduced tree, per-k node and zero counts
           residue_orbits_gf2_64 KMAX validate   -> KMAX <= 24: for each k, full and reduced
              counts of chains with Tr_d(S_k) = 1, where d = 2^ceil(log2(k+1)) and
              Tr_d is the trace of GF(2^d) (which contains S_k) to F_2; it is Galois invariant; the
              orbit lemma predicts full = 2^ceil(log2(k+1)) * reduced, and node counts
              full = 2^k, reduced = 2^(k - ceil(log2(k+1))).
   Build:  gcc -O3 -march=native -fopenmp -o residue_orbits_gf2_64 residue_orbits_gf2_64.c
   Nothing here selects W, takes a continuum limit, or constructs a force. */
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>
#include <wmmintrin.h>
#include <smmintrin.h>

static inline uint64_t gmul(uint64_t a, uint64_t b) {
  __m128i A = _mm_cvtsi64_si128((long long)a), B = _mm_cvtsi64_si128((long long)b);
  __m128i P = _mm_cvtsi64_si128(0x1B); /* x^4 + x^3 + x + 1 */
  __m128i C = _mm_clmulepi64_si128(A, B, 0x00);
  uint64_t lo = (uint64_t)_mm_cvtsi128_si64(C), hi = (uint64_t)_mm_extract_epi64(C, 1);
  __m128i H = _mm_clmulepi64_si128(_mm_cvtsi64_si128((long long)hi), P, 0x00);
  uint64_t l2 = (uint64_t)_mm_cvtsi128_si64(H), h2 = (uint64_t)_mm_extract_epi64(H, 1);
  /* h2 has at most 4 bits */
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
static uint64_t ginv(uint64_t a) { /* a^(2^64 - 2) */
  uint64_t r = 1;
  for (int i = 0; i < 63; i++) { a = gmul(a, a); r = gmul(r, a); }
  return r;
}
static uint64_t SOL[8][256];
static inline uint64_t solveN(uint64_t z) {
  uint64_t r = 0;
  for (int t = 0; t < 8; t++) r ^= SOL[t][(z >> (8 * t)) & 255];
  return r;
}
static void build(void) {
  for (int s = 0; s < 100000; s++) { /* clmul vs schoolbook */
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
static int clog2(int m) { int b = 0; while ((1 << b) < m) b++; return b; } /* ceil(log2 m) */
/* Tr_{GF(2^d)/F_2}(x) for x in GF(2^d), d = 2^ceil(log2(k+1)) (the field of a length-k chain) */
static int trd(uint64_t x, int k) {
  int d = 1 << clog2(k + 1); uint64_t t = x, y = x;
  for (int i = 1; i < d; i++) { y = gmul(y, y); t ^= y; }
  if (t > 1) { fprintf(stderr, "relative trace not in F_2\n"); exit(2); }
  return (int)t;
}
static inline int ispow2(int j) { return j > 0 && (j & (j - 1)) == 0; }
static int KMAX;
typedef struct { unsigned long long nodes[64], zeros[64], tr1[64]; } Cnt;

static void rec(uint64_t z, int i, uint64_t num, uint64_t den, int reduced, int wanttr, Cnt *c) {
  if (i == KMAX) return;
  uint64_t y = solveN(z);
  int nb = (reduced && ispow2(i + 1)) ? 1 : 2;
  for (int b = 0; b < nb; b++, y ^= 1u) {
    uint64_t n2 = gmul(num, y) ^ den, d2 = gmul(den, y);
    c->nodes[i + 1]++;
    if (n2 == 0) c->zeros[i + 1]++;
    else if (wanttr) c->tr1[i + 1] += trd(gmul(n2, ginv(d2)), i + 1);
    rec(y, i + 1, n2, d2, reduced, wanttr, c);
  }
}
static void run(int reduced, int wanttr, Cnt *tot) {
  memset(tot, 0, sizeof *tot);
  int D = KMAX < 16 ? 0 : 12, cnt = 1;
  size_t cap = (size_t)1 << (D + 1);
  uint64_t *Z = malloc(8 * cap), *NU = malloc(8 * cap), *DE = malloc(8 * cap);
  Z[0] = 1; NU[0] = 0; DE[0] = 1;
  for (int i = 0; i < D; i++) {
    uint64_t *Z2 = malloc(8 * cap), *N2 = malloc(8 * cap), *D2 = malloc(8 * cap);
    int nc = 0, nb = (reduced && ispow2(i + 1)) ? 1 : 2;
    for (int q = 0; q < cnt; q++) {
      uint64_t y = solveN(Z[q]);
      for (int b = 0; b < nb; b++, y ^= 1u) {
        uint64_t n2 = gmul(NU[q], y) ^ DE[q], d2 = gmul(DE[q], y);
        tot->nodes[i + 1]++;
        if (n2 == 0) tot->zeros[i + 1]++;
        else if (wanttr) tot->tr1[i + 1] += trd(gmul(n2, ginv(d2)), i + 1);
        Z2[nc] = y; N2[nc] = n2; D2[nc] = d2; nc++;
      }
    }
    free(Z); free(NU); free(DE); Z = Z2; NU = N2; DE = D2; cnt = nc;
  }
#pragma omp parallel for schedule(dynamic, 1)
  for (int q = 0; q < cnt; q++) {
    Cnt c; memset(&c, 0, sizeof c);
    rec(Z[q], D, NU[q], DE[q], reduced, wanttr, &c);
#pragma omp critical
    for (int k = 0; k < 64; k++) { tot->nodes[k] += c.nodes[k]; tot->zeros[k] += c.zeros[k]; tot->tr1[k] += c.tr1[k]; }
  }
  free(Z); free(NU); free(DE);
}
int main(int argc, char **argv) {
  KMAX = argc > 1 ? atoi(argv[1]) : 20;
  if (KMAX < 1 || KMAX > 63) { fprintf(stderr, "KMAX must be in 1..63\n"); return 1; }
  build();
  int bad = 0;
  if (argc > 2 && strcmp(argv[2], "validate") == 0) {
    if (KMAX > 24) { fprintf(stderr, "validate needs KMAX <= 24\n"); return 1; }
    Cnt F, R; run(0, 1, &F); run(1, 1, &R);
    for (int k = 1; k <= KMAX; k++) {
      int B = clog2(k + 1);
      int ok = F.nodes[k] == (1ull << k) && R.nodes[k] == (1ull << (k - B)) &&
               F.tr1[k] == (R.tr1[k] << B) && F.zeros[k] == 0 && R.zeros[k] == 0;
      printf("k=%d full=%llu reduced=%llu d=%d tr1_full=%llu tr1_reduced=%llu zeros=%llu/%llu %s\n",
             k, F.nodes[k], R.nodes[k], 1 << B, F.tr1[k], R.tr1[k], F.zeros[k], R.zeros[k], ok ? "ok" : "MISMATCH");
      if (!ok) bad = 1;
    }
    return bad;
  }
  Cnt R; run(1, 0, &R);
  for (int k = 1; k <= KMAX; k++) {
    int B = clog2(k + 1);
    int ok = R.nodes[k] == (1ull << (k - B)) && R.zeros[k] == 0;
    printf("k=%d reduced_chains=%llu orbit_size=%d chains_covered=2^%d zeros=%llu %s\n",
           k, R.nodes[k], 1 << B, k, R.zeros[k], ok ? "ok" : "FAIL");
    if (!ok) bad = 1;
  }
  return bad;
}
