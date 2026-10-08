"""Supporting checks for the README section
"Residue condition: power-of-two lemma and exhaustive check to k = 31".

Finite exact computations only (nothing here is a proof for all k):
  1. x^32 + x^7 + x^3 + x^2 + 1 is irreducible over F_2 (so GF(2^32) is a field);
  2. two independent field models agree: the N-level histogram of S_k over all
     chains, k <= LEVEL_K, computed in GF(2^64) (Python, check_coincidental_reduction)
     and in GF(2^32) (C, residue_chains_gf2_32.c);
  3. the C program enumerates all 2^k chains in GF(2^32) and confirms S_k != 0 for
     1 <= k <= KMAX (default 31).
The power-of-two lemma (S_k != 0 for every k = 2^j) is proved in the README and is
not a computation.  Nothing here selects W, takes a continuum limit, or constructs
a force.
"""
from __future__ import annotations

import os
import subprocess
import sys
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from check_coincidental_reduction import ginv, gmul, solve_T  # noqa: E402

F32 = (1 << 32) | 0x8D
LEVEL_K = 10


def check_modulus32():
    def mulmod(a, b):
        r = 0
        while b:
            if b & 1:
                r ^= a
            b >>= 1
            a <<= 1
            if a >> 32:
                a ^= F32
        return r

    def pmod(a, b):
        db = b.bit_length()
        while a and a.bit_length() >= db:
            a ^= b << (a.bit_length() - db)
        return a

    y = 2
    for i in range(32):
        y = mulmod(y, y)
        if i == 15:
            y16 = y
    assert y == 2  # x^(2^32) = x
    a, b = F32, y16 ^ 2
    while b:
        a, b = b, pmod(a, b)
    assert a == 1  # gcd(x^(2^16) - x, f) = 1, the only maximal proper subfield
    print("GF(2^32) modulus x^32+x^7+x^3+x^2+1 irreducible OK")


def level64(x):
    m = 0
    while x:
        x = gmul(x, x) ^ x
        m += 1
    return m


def py_level_hist(K):
    H = Counter()
    layer = [(1, 0)]
    for k in range(1, K + 1):
        new = []
        for z, S in layer:
            x = solve_T(z)
            for y in (x, x ^ 1):
                S2 = S ^ ginv(y)
                H[(k, level64(S2))] += 1
                new.append((y, S2))
        layer = new
    return H


def build():
    exe = os.path.join(HERE, "residue_chains_gf2_32")
    src = exe + ".c"
    subprocess.run(["gcc", "-O3", "-march=native", "-fopenmp", "-o", exe, src], check=True)
    return exe


def main(kmax=31):
    check_modulus32()
    exe = build()
    out = subprocess.run([exe, str(LEVEL_K), "levels"], check=True, capture_output=True, text=True).stdout
    Hc = Counter()
    for line in out.split("\n"):
        if line.strip():
            k, lv, c = map(int, line.split())
            Hc[(k, lv)] = c
    assert Hc == py_level_hist(LEVEL_K)
    print(f"N-level histograms of S_k agree between GF(2^64) and GF(2^32) for k <= {LEVEL_K} OK")
    r = subprocess.run([exe, str(kmax)], capture_output=True, text=True)
    print(r.stdout, end="")
    assert r.returncode == 0, "a chain with S_k = 0 was found or a count was wrong"
    print(f"residue sums: all 2^k chains have S_k != 0 for 1 <= k <= {kmax} OK")


if __name__ == "__main__":
    main(int(sys.argv[1]) if len(sys.argv) > 1 else 31)
