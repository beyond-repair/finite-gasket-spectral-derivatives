"""Supporting checks for the README section
"Residue condition: logarithmic-derivative form and a polynomial gcd certificate".

Finite exact computations only (nothing here is a proof for all k).  Polynomials over
F_2 are Python ints (bit i = coefficient of t^i).  Notation as in the README:
  N(t) = t^2 + t,  N^j(t) = sum_{i subset of j} t^(2^i)  (Lucas),
  Pi_k(t) = prod_{j<k} N^j(t),  A_k(t) = N^k(t) + 1.
Checks:
  1. N^j has derivative 1, deg Pi_k = 2^k - 1, deg Pi_k' = 2^k - 2;
  2. at every chain endpoint z_k in GF(2^64) (k <= EVAL_K): Pi_k(z_k) * S_k = Pi_k'(z_k),
     and the product of Pi_k(z_k) over all 2^k endpoints is 1;
  3. square decomposition Pi_k = a_k^2 + t b_k^2 and the recursion
     a_k = t b_{k-1}(N), b_k = a_{k-1}(N) + t b_{k-1}(N)  (k <= REC_K);
  4. positive control: deg gcd(A_k, Pi_k' + c Pi_k) equals the number of chains with
     S_k = c(z_k), counted by enumeration in GF(2^64), for c in {t^m, t^m + 1} (k <= EVAL_K2);
  5. N^(2^B - 1)(t) = sum_{i < 2^B} t^(2^i) (the trace polynomial), B <= 5;
  6. certificate: gcd(A_k, Pi_k') = 1 in F_2[t] for 1 <= k <= KMAX (default 20).
Nothing here selects W, takes a continuum limit, or constructs a force.
"""
from __future__ import annotations

import os
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from check_residue_orbits import Field  # noqa: E402

EVAL_K, EVAL_K2, REC_K = 8, 10, 10


def submasks(j):
    s = j
    while True:
        yield s
        if s == 0:
            return
        s = (s - 1) & j


def npow(j):
    p = 0
    for i in submasks(j):
        p ^= 1 << (1 << i)
    return p


def deg(p):
    return p.bit_length() - 1


def mul(p, q):
    r, e = 0, 0
    while q:
        if q & 1:
            r ^= p << e
        q >>= 1
        e += 1
    return r


def deriv(p):
    odd = int("10" * (p.bit_length() // 2 + 1), 2)
    return (p & odd) >> 1


def pmod(a, b):
    db = b.bit_length()
    while a.bit_length() >= db:
        a ^= b << (a.bit_length() - db)
    return a


def gcd(a, b):
    while b:
        a, b = b, pmod(a, b)
    return a


def compose_N(p):  # p(t^2 + t)
    r, pw, e = 0, 1, 0
    n = 0b110
    while p >> e:
        if (p >> e) & 1:
            r ^= pw
        pw = mul(pw, n)
        e += 1
    return r


def unsquare(p):  # q with q^2 = p (p has only even exponents)
    q, i = 0, 0
    while p >> (2 * i):
        if (p >> (2 * i)) & 1:
            q |= 1 << i
        i += 1
    return q


def split(p):  # p = a^2 + t b^2
    ev = int("01" * (p.bit_length() // 2 + 1), 2)
    a2, tb2 = p & ev, p & ~ev
    assert (tb2 & 1) == 0
    return unsquare(a2), unsquare(tb2 >> 1)


def pi(k):
    p = 1
    for j in range(k):
        p = mul(p, npow(j))
    return p


def ev(F, p, x):
    r = 0
    for i in range(deg(p), -1, -1):
        r = F.mul(r, x) ^ ((p >> i) & 1)
    return r


def chains(F, kmax):
    level = [(1, 0)]
    for k in range(1, kmax + 1):
        nxt = []
        for z, s in level:
            y = F.solve(z)
            for w in (y, y ^ 1):
                nxt.append((w, s ^ F.inv(w)))
        level = nxt
        yield k, level


def main(kmax=20):
    F = Field(64, 0b11011)
    for j in range(12):
        assert deriv(npow(j)) == 1
    for k in range(1, 13):
        p = pi(k)
        assert deg(p) == 2 ** k - 1 and deg(deriv(p)) == 2 ** k - 2
    print("1. (N^j)' = 1 (j < 12); deg Pi_k = 2^k - 1, deg Pi_k' = 2^k - 2 (k <= 12)")
    cnt = []
    for k, level in chains(F, EVAL_K2):
        p = pi(k)
        a = npow(k) ^ 1
        if k <= EVAL_K:
            dp, prod = deriv(p), 1
            for z, s in level:
                pz = ev(F, p, z)
                assert F.mul(pz, s) == ev(F, dp, z)
                prod = F.mul(prod, pz)
            assert prod == 1
        for c in [1 << m for m in range(16)] + [(1 << m) | 1 for m in range(1, 16)]:
            hits = sum(1 for z, s in level if s == ev(F, c, z))
            g = gcd(a, deriv(p) ^ mul(p, c))
            assert deg(g) == hits, (k, c, deg(g), hits)
            if hits:
                cnt.append((k, c, hits))
    print("4. positive control: deg gcd(A_k, Pi_k' + c Pi_k) = #{chains with S_k = c(z_k)} for k <= %d and "
          "c in {t^m, t^m + 1 : m < 16}; nonzero cases (k, c as bitmask, count): %s" % (EVAL_K2, cnt))
    print("2. Pi_k(z) S_k = Pi_k'(z) at all chains and prod Pi_k(z) = 1 (k <= %d)" % EVAL_K)
    a, b = split(pi(0))
    for k in range(1, REC_K + 1):
        ak, bk = split(pi(k))
        assert mul(ak, ak) ^ (mul(mul(bk, bk), 2)) == pi(k)
        nb = compose_N(b)
        assert ak == mul(nb, 2) and bk == compose_N(a) ^ mul(nb, 2)
        assert deg(bk) == 2 ** (k - 1) - 1
        a, b = ak, bk
    print("3. Pi_k = a_k^2 + t b_k^2 with the stated recursion, deg b_k = 2^(k-1) - 1 (k <= %d)" % REC_K)
    for B in range(6):
        assert npow(2 ** B - 1) == sum(1 << (1 << i) for i in range(2 ** B))
    print("5. N^(2^B - 1) = trace polynomial for B <= 5")
    for k in range(1, kmax + 1):
        t0 = time.time()
        g = gcd(npow(k) ^ 1, deriv(pi(k)))
        assert g == 1, k
        print("6. k=%d gcd(N^k + 1, Pi_k') = 1  (%.1fs)" % (k, time.time() - t0), flush=True)
    print("certificate: S_k != 0 on all chains for 1 <= k <= %d (independent of chain enumeration)" % kmax)


if __name__ == "__main__":
    main(int(sys.argv[1]) if len(sys.argv) > 1 else 20)
