/* Exhaustive finite check for the README section
   "Residue condition: power-of-two lemma and exhaustive check to k = 31".

   Statement checked (finite exact computation, not a proof for all k):
     for every chain z_0 = 1, z_i^2 + z_i = z_{i-1} (i = 1..k) over the algebraic
     closure of F_2, S_k = sum_{i=1}^k 1/z_i != 0, for 1 <= k <= KMAX <= 31.

   Field: GF(2^32) = F_2[x]/(x^32 + x^7 + x^3 + x^2 + 1).  Irreducibility of the
   modulus is checked in scripts/check_residue_extension.py.  N(x) = x^2 + x is
   F_2-linear and N^32 = F^32 + 1 = 0 on GF(2^32) (F = Frobenius), with kernel
   {0, 1}; hence every chain of length <= 31 lies in GF(2^32), and the two roots of
   y^2 + y = z_{i-1} are y and y + 1.

   S_k is carried as num/den with den = z_1...z_k != 0, so S_k = 0 iff num = 0.

   Usage:  residue_chains_gf2_32 KMAX            -> per-k chain and zero counts
           residue_chains_gf2_32 KMAX levels     -> histogram of the N-level of S_k
             (level(x) = min{m : N^m x = 0}; field-independent, used to cross-check
              against the independent GF(2^64) model in Python).
   Build:  gcc -O3 -march=native -fopenmp -o residue_chains_gf2_32 residue_chains_gf2_32.c
   Nothing here selects W, takes a continuum limit, or constructs a force. */
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>
#if defined(__PCLMUL__)
#include <wmmintrin.h>
#endif

#define POLY 0x8Du /* x^7 + x^3 + x^2 + 1 */

static inline uint32_t gmul(uint32_t a, uint32_t b) {
#if defined(__PCLMUL__)
  __m128i A = _mm_cvtsi32_si128((int)a), B = _mm_cvtsi32_si128((int)b);
  __m128i P = _mm_cvtsi32_si128((int)POLY);
  uint64_t p = (uint64_t)_mm_cvtsi128_si64(_mm_clmulepi64_si128(A, B, 0));
  uint64_t q = (uint64_t)_mm_cvtsi128_si64(
      _mm_clmulepi64_si128(_mm_cvtsi64_si128((long long)(p >> 32)), P, 0));
  uint64_t r = (p & 0xffffffffu) ^ q;
  uint64_t q2 = (uint64_t)_mm_cvtsi128_si64(
      _mm_clmulepi64_si128(_mm_cvtsi64_si128((long long)(r >> 32)), P, 0));
  return (uint32_t)((r & 0xffffffffu) ^ q2);
#else
  uint64_t r = 0, aa = a;
  while (b) { if (b & 1) r ^= aa; b >>= 1; aa <<= 1; if (aa >> 32) aa ^= ((uint64_t)1 << 32) | POLY; }
  return (uint32_t)r;
#endif
}

static uint32_t SOL[4][256];
static inline uint32_t Nlin(uint32_t x) { return gmul(x, x) ^ x; }
static inline uint32_t solveN(uint32_t z) {
  return SOL[0][z & 255] ^ SOL[1][(z >> 8) & 255] ^ SOL[2][(z >> 16) & 255] ^ SOL[3][z >> 24];
}
static uint32_t ginv(uint32_t a) { /* a^(2^32 - 2) */
  uint32_t r = 1;
  for (int i = 0; i < 31; i++) { a = gmul(a, a); r = gmul(r, a); }
  return r;
}
static int level(uint32_t x) { int m = 0; while (x) { x = Nlin(x); m++; } return m; }

static void build_solver(void) {
  uint32_t pv[32], pc[32];
  int have[32] = {0};
  for (int j = 0; j < 32; j++) {
    uint32_t v = Nlin(1u << j), c = 1u << j;
    while (v) {
      int h = 31 - __builtin_clz(v);
      if (have[h]) { v ^= pv[h]; c ^= pc[h]; } else { have[h] = 1; pv[h] = v; pc[h] = c; break; }
    }
  }
  for (int t = 0; t < 4; t++)
    for (int b = 0; b < 256; b++) {
      uint32_t v = ((uint32_t)b) << (8 * t), c = 0;
      while (v) {
        int h = 31 - __builtin_clz(v);
        if (!have[h]) { v ^= 1u << h; continue; }
        v ^= pv[h]; c ^= pc[h];
      }
      SOL[t][b] = c;
    }
  for (uint32_t s = 1; s < 200000; s++) { /* solver self-test on the image of N */
    uint32_t a = Nlin(s * 2654435761u);
    if (Nlin(solveN(a)) != a) { fprintf(stderr, "solver self-test failed\n"); exit(2); }
  }
}

static int KMAX;
typedef struct { unsigned long long nodes[33], zeros[33]; } Cnt;

static void rec(uint32_t z, int i, uint32_t num, uint32_t den, Cnt *c) {
  if (i == KMAX) return;
  uint32_t y = solveN(z);
  for (int b = 0; b < 2; b++, y ^= 1u) {
    uint32_t n2 = gmul(num, y) ^ den, d2 = gmul(den, y);
    c->nodes[i + 1]++;
    if (n2 == 0) c->zeros[i + 1]++;
    rec(y, i + 1, n2, d2, c);
  }
}

static unsigned long long H[33][34];
static void rec_levels(uint32_t z, int i, uint32_t S) {
  if (i == KMAX) return;
  uint32_t y = solveN(z);
  for (int b = 0; b < 2; b++, y ^= 1u) {
    uint32_t S2 = S ^ ginv(y);
    H[i + 1][level(S2)]++;
    rec_levels(y, i + 1, S2);
  }
}

int main(int argc, char **argv) {
  KMAX = argc > 1 ? atoi(argv[1]) : 20;
  if (KMAX < 1 || KMAX > 31) { fprintf(stderr, "KMAX must be in 1..31\n"); return 1; }
  build_solver();
  if (argc > 2 && strcmp(argv[2], "levels") == 0) {
    rec_levels(1, 0, 0);
    for (int k = 1; k <= KMAX; k++)
      for (int l = 0; l < 34; l++)
        if (H[k][l]) printf("%d %d %llu\n", k, l, H[k][l]);
    return 0;
  }
  int D = KMAX < 8 ? 0 : 6, cnt = 1;
  Cnt tot; memset(&tot, 0, sizeof tot);
  uint32_t *Z = malloc(4u << D), *NU = malloc(4u << D), *DE = malloc(4u << D);
  Z[0] = 1; NU[0] = 0; DE[0] = 1;
  for (int i = 0; i < D; i++) {
    uint32_t *Z2 = malloc(4u << D), *N2 = malloc(4u << D), *D2 = malloc(4u << D);
    int nc = 0;
    for (int q = 0; q < cnt; q++) {
      uint32_t y = solveN(Z[q]);
      for (int b = 0; b < 2; b++, y ^= 1u) {
        uint32_t n2 = gmul(NU[q], y) ^ DE[q], d2 = gmul(DE[q], y);
        tot.nodes[i + 1]++;
        if (n2 == 0) tot.zeros[i + 1]++;
        Z2[nc] = y; N2[nc] = n2; D2[nc] = d2; nc++;
      }
    }
    free(Z); free(NU); free(DE); Z = Z2; NU = N2; DE = D2; cnt = nc;
  }
#pragma omp parallel for schedule(dynamic, 1)
  for (int q = 0; q < cnt; q++) {
    Cnt c; memset(&c, 0, sizeof c);
    rec(Z[q], D, NU[q], DE[q], &c);
#pragma omp critical
    for (int k = 0; k <= 32; k++) { tot.nodes[k] += c.nodes[k]; tot.zeros[k] += c.zeros[k]; }
  }
  int bad = 0;
  for (int k = 1; k <= KMAX; k++) {
    printf("k=%d chains=%llu zeros=%llu\n", k, tot.nodes[k], tot.zeros[k]);
    if (tot.nodes[k] != (1ull << k) || tot.zeros[k]) bad = 1;
  }
  return bad;
}
