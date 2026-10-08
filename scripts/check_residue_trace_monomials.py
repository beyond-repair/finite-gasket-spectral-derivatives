"""Supporting search for the README section
"Residue condition: exact check to k = 46 and no monomial trace certificate".

Finite exact computation only (nothing here is a proof for any k beyond those enumerated).
Question: is there a uniform "trace certificate" of the shape
    Tr_d( z_k^a * z_{k-1}^b * S_k ) = 1   for every chain of length k,
or the same with z_k replaced by its sibling z_k + 1, where d = 2^ceil(log2(k+1)) and Tr_d is the
trace from GF(2^d) (which contains the chain and S_k) to F_2?  Such an identity, if it held for all k,
would prove S_k != 0.  This script enumerates all 2^k chains in GF(2^64) for k <= KMAX and lists, for
each k, every (a, b, sibling) with -6 <= a <= 6, -4 <= b <= 4 for which the identity holds.
Nothing here selects W, takes a continuum limit, or constructs a force.
"""
from __future__ import annotations

import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from check_residue_orbits import Field  # noqa: E402

KMAX = 8
F = Field(64, 0b11011)
_cache = {}


def pw(x, m):
    key = (x, m)
    if key not in _cache:
        y, e = (F.inv(x), -m) if m < 0 else (x, m)
        r = 1
        for _ in range(e):
            r = F.mul(r, y)
        _cache[key] = r
    return _cache[key]


def chains(kmax):
    level = [[1]]
    for k in range(1, kmax + 1):
        nxt = []
        for c in level:
            y = F.solve(c[-1])
            nxt.append(c + [y])
            nxt.append(c + [y ^ 1])
        level = nxt
        yield k, level


def main(kmax=KMAX):
    hits = {}
    for k, level in chains(kmax):
        data = []
        for c in level:
            s = 0
            for z in c[1:]:
                s ^= F.inv(z)
            assert s != 0
            data.append((c, s))
        good = []
        for a in range(-6, 7):
            for b in range(-4, 5):
                if k < 2 and b:
                    continue
                for sib in (0, 1):
                    ok = True
                    for c, s in data:
                        f = F.mul(pw(c[-1] ^ sib, a), pw(c[-2], b))
                        if F.trd(F.mul(f, s), k) != 1:
                            ok = False
                            break
                    if ok:
                        good.append((a, b, sib))
        hits[k] = set(good)
        print(f"k={k}: {len(good)} certificates" + (f", e.g. {sorted(good)[:6]}" if good else ""))
    common = set.intersection(*(hits[k] for k in range(2, kmax + 1)))
    print("common to all 2 <= k <=", kmax, ":", sorted(common) if common else "none")
    assert not hits[6] and not hits[7] and not common
    return hits


if __name__ == "__main__":
    main(int(sys.argv[1]) if len(sys.argv) > 1 else KMAX)
