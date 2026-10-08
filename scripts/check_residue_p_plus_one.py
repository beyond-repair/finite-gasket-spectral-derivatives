"""Supporting checks for the README section
"Residue condition: lengths 2^j + 1 and the limits of the subfield test".

Finite exact computations in GF(2^64) (field model from check_coincidental_reduction).
Nothing here is a proof for all k:
  1. the pairing identity 1/z_{i-1} + 1/z_i = 1/(z_i + 1) on every chain, k <= KMAX;
  2. for k = 2^j + 1 (j = 1, 2, 3) every chain has S_k outside GF(2^(2^j)),
     i.e. S_k^(2^(2^j)) != S_k (the lemma proves this for every j);
  3. the negative result: for k = 6, 11, 13, 14 some chains have S_k inside
     GF(2^p), p = largest power of two below k, so "S_k is not in the subfield"
     is not a general proof route (counts printed; k = 15 gives 176 and is
     omitted here for runtime).
Nothing here selects W, takes a continuum limit, or constructs a force.
"""
from __future__ import annotations

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from check_coincidental_reduction import ginv, gmul, solve_T  # noqa: E402

KMAX = 14
EXPECTED_SUBFIELD_ZEROS = {6: 8, 11: 32, 13: 48, 14: 32}


def frob(x, p):
    for _ in range(p):
        x = gmul(x, x)
    return x


def main():
    layer = [(1, 0)]  # (z_k, S_k), z_0 = 1, S_0 = 0
    for k in range(1, KMAX + 1):
        new = []
        for z, S in layer:
            x = solve_T(z)
            for y in (x, x ^ 1):
                assert gmul(y, y) ^ y == z
                if k >= 1:
                    # 1/z_{k-1} = 1/z_k + 1/(z_k + 1)
                    assert ginv(z) == ginv(y) ^ ginv(y ^ 1)
                S2 = S ^ ginv(y)
                assert S2 != 0
                new.append((y, S2))
        layer = new
        if k & (k - 1) == 0:
            continue
        p = 1 << (k.bit_length() - 1)
        inside = sum(1 for _, S in layer if frob(S, p) == S)
        if k == p + 1:
            assert inside == 0, (k, inside)
            print(f"k = {k} = {p}+1: all {len(layer)} chains have S_k outside GF(2^{p}) OK")
        else:
            print(f"k = {k}, p = {p}: {inside} of {len(layer)} chains have S_k inside GF(2^{p})")
            if k in EXPECTED_SUBFIELD_ZEROS:
                assert inside == EXPECTED_SUBFIELD_ZEROS[k], (k, inside)
    print(f"pairing identity and S_k != 0 on all chains for k <= {KMAX} OK")


if __name__ == "__main__":
    main()
