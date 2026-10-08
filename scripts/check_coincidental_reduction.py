"""Supporting checks for the README section "Two-adic reduction of coincidental hits".

Finite exact computations only (nothing here is a proof for all n):
  1. mod-2 congruences Q_n = x * T^{n-1}(x) and Qt_n = T^n(x) + 1 in F_2[x],
     T(x) = x^2 + x, for 1 <= n <= EXACT_MAX (exact integer Q_n, Qt_n);
  2. channel values s_m(6) = t_m(6) = -3, s_m(5) = 5(3^{m-2}-1)/2 (m >= 1),
     s_n(2) = (s_{n-2}(-6) - 6)/3 > 0 (n >= 3), as exact rationals;
  3. the residue-field statement used for the last open case: for every chain
     z_0 = 1, z_i^2 + z_i = z_{i-1} in GF(2^64) (which contains every such chain
     of length <= 63), S_k = sum_{i=1}^k 1/z_i != 0, for 1 <= k <= KMAX.
Nothing here selects W, takes a continuum limit, or constructs a force.
"""
from __future__ import annotations

import sys
import time
from fractions import Fraction

sys.path.insert(0, __file__.rsplit("/", 1)[0])
from check_corner_channels import channels, peval  # noqa: E402

EXACT_MAX = 8

# ---------- 1. mod-2 congruences ----------

def f2_mul(a, b):
    r = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        if x:
            for j, y in enumerate(b):
                r[i + j] ^= y
    while len(r) > 1 and r[-1] == 0:
        r.pop()
    return r


def f2_add(a, b):
    n = max(len(a), len(b))
    r = [(a[i] if i < len(a) else 0) ^ (b[i] if i < len(b) else 0) for i in range(n)]
    while len(r) > 1 and r[-1] == 0:
        r.pop()
    return r


def f2_T_iter(n):
    t = [0, 1]
    for _ in range(n):
        t = f2_add(f2_mul(t, t), t)
    return t


def check_mod2(Q, Qt):
    for n in range(1, EXACT_MAX + 1):
        q2 = [c % 2 for c in Q[n]]
        qt2 = [c % 2 for c in Qt[n]]
        assert q2 == f2_mul([0, 1], f2_T_iter(n - 1)), n
        assert qt2 == f2_add(f2_T_iter(n), [1]), n
    print(f"mod 2: Q_n = x*T^(n-1)(x), Qt_n = T^n(x)+1 for 1<=n<={EXACT_MAX} OK")


# ---------- 2. channel values ----------

def check_values(Q, P, Qt, Pt):
    ev = lambda N, D, x: Fraction(peval(N, x), peval(D, x))
    for m in range(1, EXACT_MAX + 1):
        assert ev(Q[m], P[m], 6) == -3 and ev(Qt[m], Pt[m], 6) == -3
        assert ev(Q[m], P[m], 5) == Fraction(5 * (3 ** (m - 1) - 3), 6)
    for n in range(2, EXACT_MAX + 1):
        s2 = ev(Q[n], P[n], 2)
        sm6 = ev(Q[n - 2], P[n - 2], -6)
        assert s2 == (sm6 - 6) / 3
        assert (s2 > 0) == (n >= 3) and (s2 == 0) == (n == 2)
    print(f"values: s_m(6)=t_m(6)=-3, s_m(5)=5(3^(m-2)-1)/2, s_n(2)=(s_(n-2)(-6)-6)/3>0 (n>=3) "
          f"for n,m<={EXACT_MAX} OK")


# ---------- 3. residue sums in GF(2^64) ----------

MOD = (1 << 64) | 0b11011  # x^64 + x^4 + x^3 + x + 1


def gmul(a, b):
    r = 0
    while b:
        if b & 1:
            r ^= a
        b >>= 1
        a <<= 1
        if a >> 64:
            a ^= MOD
    return r


def ginv(a):
    r, e = 1, (1 << 64) - 2
    while e:
        if e & 1:
            r = gmul(r, a)
        a = gmul(a, a)
        e >>= 1
    return r


def check_modulus_irreducible():
    # x^(2^64) = x mod MOD and gcd(x^(2^32) - x, MOD) = 1  =>  MOD irreducible of degree 64
    x = 2
    y = x
    for i in range(64):
        y = gmul(y, y)
        if i == 31:
            y32 = y
    assert y == x
    # gcd over F_2[x] of MOD and (y32 ^ x) as polynomials
    a, b = MOD, y32 ^ x
    def pmod(a, b):
        db = b.bit_length()
        while a and a.bit_length() >= db:
            a ^= b << (a.bit_length() - db)
        return a
    while b:
        a, b = b, pmod(a, b)
    assert a == 1
    print("GF(2^64) modulus x^64+x^4+x^3+x+1 irreducible OK")


_basis = None


def solve_T(c):
    """A solution x of x^2 + x = c in GF(2^64), or None."""
    global _basis
    if _basis is None:
        _basis = {}
        for i in range(64):
            v, comb = gmul(1 << i, 1 << i) ^ (1 << i), 1 << i
            while v:
                p = v.bit_length() - 1
                if p in _basis:
                    bv, bc = _basis[p]
                    v ^= bv
                    comb ^= bc
                else:
                    _basis[p] = (v, comb)
                    break
    comb = 0
    while c:
        p = c.bit_length() - 1
        if p not in _basis:
            return None
        bv, bc = _basis[p]
        c ^= bv
        comb ^= bc
    return comb


def check_residue_sums(kmax):
    t0 = time.time()
    level = [(1, 0)]
    for k in range(1, kmax + 1):
        new = []
        for z, S in level:
            x = solve_T(z)
            assert x is not None
            for zz in (x, x ^ 1):
                SS = S ^ ginv(zz)
                assert SS != 0, f"S_k = 0 at k={k}"
                new.append((zz, SS))
        level = new
        assert len(level) == 2 ** k
        print(f"residue sums: k={k}: all {2 ** k} chains have S_k != 0 ({time.time() - t0:.0f}s)",
              flush=True)


def main(kmax=13):
    Q, P, Qt, Pt = channels(EXACT_MAX)
    check_mod2(Q, Qt)
    check_values(Q, P, Qt, Pt)
    check_modulus_irreducible()
    check_residue_sums(kmax)


if __name__ == "__main__":
    main(int(sys.argv[1]) if len(sys.argv) > 1 else 13)
