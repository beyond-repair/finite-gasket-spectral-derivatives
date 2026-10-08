"""Supporting checks for the README section
"Residue condition: lengths 2^j + 2 (relative-trace argument)".

Finite exact computations in GF(2^64) (field model from check_coincidental_reduction).
The theorem itself is proved in the README; this script checks its ingredients:
  1. on every chain with p = 4, 8 (k = p + 2 = 6, 10; all chains) and p = 16
     (k = 18; one chain per Frobenius orbit, orbit lemma of the sixth run):
     z_{p+i} = alpha_i + z_i z_p with alpha_i in GF(2^p) (i = 1, 2),
     alpha_1^2 + alpha_1 = z_1^2 c, alpha_2^2 + alpha_2 = alpha_1 + z_2^2 c (c = z_{p-1}),
     Nm(z_{p+1}) = z_1^2 alpha_1, Nm(z_{p+2}) = alpha_1 + (1 + z_2) alpha_2,
     the z_p-coefficient C1 of S_{p+2} equals 1/c + z_1^2/alpha_1 + z_2/Nm(z_{p+2})
     and also z_1^2/(alpha_1 + 1) + z_2/Nm(z_{p+2}),
     and C1 = 0 <=> S_{p+2} in GF(2^p);
  2. for each of the four choices (z_1, z_2), the quadratic Q(a) obtained from
     C1 = 0 has constant term mu^2 + mu != 0 (so Q is not identically zero), the
     substitution identity holds at random points, and every chain with C1 = 0
     has Q(alpha_1) = 0 and alpha_1 in GF(2^4); the linear coefficient B is 0
     (also proved by hand in the README), and A != 0, so Q(a) = A a^2 + C has
     the single root a = sqrt(C/A) in GF(2^4);
  3. counts of chains with S_{p+2} in GF(2^p): 8 (k = 6), 0 (k = 10), 0 (k = 18).
Nothing here selects W, takes a continuum limit, or constructs a force.
"""
from __future__ import annotations

import os
import random
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from check_coincidental_reduction import ginv, gmul, solve_T  # noqa: E402


def frob(x, e):
    for _ in range(e):
        x = gmul(x, x)
    return x


def in_sub(x, e):  # x in GF(2^e)
    return frob(x, e) == x


def sq(x):
    return gmul(x, x)


def chains(k, reduced):
    """All chains (z_0..z_k), or one per Frobenius orbit (keep one child at power-of-two depths)."""
    out = []

    def walk(ch):
        if len(ch) == k + 1:
            out.append(tuple(ch))
            return
        j = len(ch)
        x = solve_T(ch[-1])
        assert x is not None and sq(x) ^ x == ch[-1]
        kids = (x,) if (reduced and j & (j - 1) == 0) else (x, x ^ 1)
        for y in kids:
            walk(ch + [y])

    walk([1])
    return out


def quad_coeffs(w, zeta):
    """Coefficients of Q(a) = A a^2 + B a + C from C1 = 0 (README derivation)."""
    w2 = sq(w)
    one_z = 1 ^ zeta
    lam = gmul(gmul(w, zeta ^ w2), ginv(one_z))
    mu = gmul(gmul(w, zeta), ginv(one_z))
    z2w = gmul(sq(zeta), w)
    A = sq(lam) ^ z2w
    B = lam ^ 1 ^ z2w
    C = sq(mu) ^ mu
    return lam, mu, A, B, C


def check_p(p, reduced, expected_inside):
    k = p + 2
    inside = 0
    roots_seen = set()
    for ch in chains(k, reduced):
        z = ch
        c, zp = z[p - 1], z[p]
        w, zeta = z[1], z[2]
        assert sq(w) ^ w == 1 and sq(zeta) ^ zeta == w
        a1 = z[p + 1] ^ gmul(w, zp)
        a2 = z[p + 2] ^ gmul(zeta, zp)
        assert in_sub(a1, p) and in_sub(a2, p) and in_sub(c, p)
        assert not in_sub(c, p // 2)  # c has degree exactly p
        assert sq(a1) ^ a1 == gmul(sq(w), c)
        assert sq(a2) ^ a2 == a1 ^ gmul(sq(zeta), c)
        # norms to GF(2^p): x * x^(2^p)
        nm1 = gmul(z[p + 1], frob(z[p + 1], p))
        nm2 = gmul(z[p + 2], frob(z[p + 2], p))
        assert nm1 == gmul(sq(w), a1)
        assert nm2 == a1 ^ gmul(1 ^ zeta, a2)
        assert gmul(zp, frob(zp, p)) == c
        C1 = ginv(c) ^ gmul(sq(w), ginv(a1)) ^ gmul(zeta, ginv(nm2))
        assert C1 == gmul(sq(w), ginv(a1 ^ 1)) ^ gmul(zeta, ginv(nm2))
        S = 0
        for i in range(1, k + 1):
            S ^= ginv(z[i])
        assert S != 0
        # S = S0 + C1 z_p with S0 in GF(2^p)
        S0 = S ^ gmul(C1, zp)
        assert in_sub(S0, p) and in_sub(C1, p)
        assert (C1 == 0) == in_sub(S, p)
        if C1 == 0:
            inside += 1
            lam, mu, A, B, Cc = quad_coeffs(w, zeta)
            assert a2 == gmul(lam, a1) ^ mu
            assert gmul(A, sq(a1)) ^ gmul(B, a1) ^ Cc == 0
            assert in_sub(a1, 4)
            roots_seen.add(a1)
    assert inside == expected_inside, (k, inside)
    tag = "one chain per Frobenius orbit" if reduced else "all chains"
    print(f"p = {p}, k = {k} ({tag}): identities OK, {inside} chains with S_k in GF(2^{p})")


def check_quadratics():
    # the four choices of (z_1, z_2)
    w0 = solve_T(1)
    rng = random.Random(1)
    for w in (w0, w0 ^ 1):
        z0 = solve_T(w)
        for zeta in (z0, z0 ^ 1):
            assert in_sub(w, 2) and in_sub(zeta, 4) and not in_sub(zeta, 2)
            lam, mu, A, B, C = quad_coeffs(w, zeta)
            assert C != 0, "Q identically zero"
            assert B == 0 and A != 0
            assert in_sub(A, 4) and in_sub(C, 4)
            for _ in range(20):
                a = rng.getrandbits(64)
                a2 = gmul(lam, a) ^ mu
                lhs = sq(a2) ^ a2
                rhs = a ^ gmul(gmul(sq(zeta), w), sq(a) ^ a)
                assert lhs ^ rhs == gmul(A, sq(a)) ^ gmul(B, a) ^ C
            print(f"(z_1, z_2) choice: Q = A a^2 + B a + C with A {'!=' if A else '=='} 0, "
                  f"B {'!=' if B else '=='} 0, C != 0 OK")


def main():
    check_quadratics()
    check_p(4, False, 8)
    check_p(8, False, 0)
    check_p(16, True, 0)
    print("all checks OK")


if __name__ == "__main__":
    main()
