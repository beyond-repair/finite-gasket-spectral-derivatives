"""Supporting checks for the README section
"Residue condition: Frobenius orbit reduction and exact check to k = 45".

Finite exact computations only (nothing here is a proof for all k):
  1. x^64 + x^4 + x^3 + x + 1 is irreducible over F_2 (reuses
     check_coincidental_reduction.check_modulus_irreducible);
  2. model-independent cross-check of the orbit lemma: for k <= PY_K, the number of
     chains with Tr_d(S_k) = 1 (d = 2^ceil(log2(k+1)), Tr_d the trace of GF(2^d) to
     F_2, a Galois invariant of the chain) is computed by full enumeration in two
     independent field models, GF(2^64) and GF(2^32) (pure Python), and compared with
     the C program's full count and with orbit_size * (count on the reduced tree);
  3. scripts/residue_orbits_gf2_64.c "validate" repeats 2 in C for k <= 22 (full tree
     vs reduced tree, node counts 2^k and 2^(k - ceil(log2(k+1))));
  4. the C program walks the Frobenius-reduced tree and confirms S_k != 0 for
     1 <= k <= KMAX (default 45).
The orbit lemma itself is proved in the README.  Nothing here selects W, takes a
continuum limit, or constructs a force.
"""
from __future__ import annotations

import os
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from check_coincidental_reduction import check_modulus_irreducible  # noqa: E402

PY_K = 11


class Field:
    def __init__(self, deg, low):
        self.deg, self.mod = deg, (1 << deg) | low
        self._solver()

    def mul(self, a, b):
        r, d, m = 0, self.deg, self.mod
        while b:
            if b & 1:
                r ^= a
            b >>= 1
            a <<= 1
            if a >> d:
                a ^= m
        return r

    def inv(self, a):  # a^(2^deg - 2)
        r = 1
        for _ in range(self.deg - 1):
            a = self.mul(a, a)
            r = self.mul(r, a)
        return r

    def N(self, x):
        return self.mul(x, x) ^ x

    def _solver(self):
        piv = {}
        for j in range(self.deg):
            v, c = self.N(1 << j), 1 << j
            while v:
                h = v.bit_length() - 1
                if h in piv:
                    v ^= piv[h][0]
                    c ^= piv[h][1]
                else:
                    piv[h] = (v, c)
                    break
        self.piv = piv

    def solve(self, z):  # one root of y^2 + y = z
        v, c = z, 0
        while v:
            h = v.bit_length() - 1
            v ^= self.piv[h][0]
            c ^= self.piv[h][1]
        assert self.N(c) == z
        return c

    def trd(self, x, k):
        d = 1
        while d < k + 1:
            d *= 2
        t = y = x
        for _ in range(d - 1):
            y = self.mul(y, y)
            t ^= y
        assert t in (0, 1)
        return t


def tr_counts(F, kmax):
    out = [0] * (kmax + 1)
    level = [(1, 0)]  # (z_i, S_i)
    for k in range(1, kmax + 1):
        nxt = []
        for z, S in level:
            y = F.solve(z)
            for w in (y, y ^ 1):
                S2 = S ^ F.inv(w)
                assert S2 != 0
                out[k] += F.trd(S2, k)
                nxt.append((w, S2))
        level = nxt
    return out


def main(kmax=45):
    check_modulus_irreducible()
    F64, F32 = Field(64, 0b11011), Field(32, 0x8D)
    c64, c32 = tr_counts(F64, PY_K), tr_counts(F32, PY_K)
    assert c64 == c32, (c64, c32)
    print("Tr_d(S_k)=1 counts, full enumeration, GF(2^64) and GF(2^32) agree:", c64[1:])
    exe = os.path.join(HERE, "residue_orbits_gf2_64")
    subprocess.run(["gcc", "-O3", "-march=native", "-fopenmp", "-o", exe,
                    os.path.join(HERE, "residue_orbits_gf2_64.c")], check=True)
    val = subprocess.run([exe, "22", "validate"], check=True, capture_output=True, text=True).stdout
    for line in val.splitlines():
        k = int(re.search(r"k=(\d+)", line).group(1))
        full = int(re.search(r"tr1_full=(\d+)", line).group(1))
        assert line.endswith(" ok"), line
        if k <= PY_K:
            assert full == c64[k], (k, full, c64[k])
    print("C validate k<=22: full = orbit_size * reduced for Tr_d counts and node counts; matches Python for k<=%d" % PY_K)
    res = subprocess.run([exe, str(kmax)], capture_output=True, text=True)
    print(res.stdout, end="")
    assert res.returncode == 0
    print("S_k != 0 on the Frobenius-reduced tree for all 1 <= k <= %d" % kmax)


if __name__ == "__main__":
    main(int(sys.argv[1]) if len(sys.argv) > 1 else 45)
