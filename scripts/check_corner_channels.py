"""Supporting checks for the README section "Corner channels and coincidental hits".

For free L_n = D - A on build_gasket(n), the Schur complement of L_n - lam onto
the three corners V_0 is S_n(lam) = t_n I + ((s_n - t_n)/3) J. With
R(z) = z(5 - z), Delta = (2 - lam)(5 - lam), the README proves
    s_n = ((6 - lam) s_{n-1}(R) + 2R) / Delta,   t_n likewise,
    s_0 = -lam, t_0 = 3 - lam,
and the reduced forms s_n = Q_n / P_n, t_n = Qt_n / Pt_n with
    P_n  = 2 - R^{n-1}(lam)                 (n >= 1),
    Pt_n = prod_{k=0}^{n-1} (5 - R^k(lam))  (n >= 1),
deg Q_n = 2^{n-1} + 1, deg Qt_n = 2^n, leading coefficients +-1.

This script
  1. builds Q_n, Qt_n with exact integer arithmetic (n <= EXACT_MAX), asserting
     that the divisions by (lam - 5) and (lam - 2) leave remainder 0;
  2. checks the Schur identity and the channel counts against eigh (n <= 6);
  3. for 3 <= n <= NMAX, computes over F_p (p = 2^61 - 1) the degree of
     gcd(Q_n, H_{n-1}(R(lam))) and gcd(Qt_n, H_{n-1}(R(lam))), where
     H_{n-1} = Q_{n-1} Qt_{n-1} prod_{j=0}^{n-3} prod_{a in {2,5,6}} (R^j - a)
     has every eigenvalue of L_{n-1} among its roots (README).
Because every polynomial involved has leading coefficient +-1, the F_p gcd
degree bounds the gcd degree over Q from above. A sym gcd of degree 1 (the
factor lam) and a std gcd of degree 0 certify: no corner-visible eigenvalue
other than 0 is a decimation hit at that level.

Steps 1 and 3 are finite exact computations; step 2 is numerical support.
Nothing here selects W, takes a continuum limit, or constructs a force.
"""
from __future__ import annotations

import sys
import time
from fractions import Fraction

P61 = 2**61 - 1
EXACT_MAX = 8


def trim(a):
    while len(a) > 1 and a[-1] == 0:
        a = a[:-1]
    return a


def add(a, b, p=None):
    n = max(len(a), len(b))
    r = [(a[i] if i < len(a) else 0) + (b[i] if i < len(b) else 0) for i in range(n)]
    return trim([x % p for x in r] if p else r)


def mul(a, b, p=None):
    r = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        if x:
            for j, y in enumerate(b):
                r[i + j] += x * y
            if p:
                r = [v % p for v in r] if i % 64 == 63 else r
    return trim([x % p for x in r] if p else r)


def scal(c, a, p=None):
    return trim([(c * x) % p if p else c * x for x in a])


def comp_R(a, p=None):
    """a(R(lam)) by Horner, R = 5 lam - lam^2."""
    Rp = [0, 5, -1] if p is None else [0, 5, p - 1]
    r = [0]
    for c in reversed(a):
        r = add(mul(r, Rp, p), [c], p)
    return r


def div_lin(a, root, p=None):
    """Quotient of a by (lam - root); asserts zero remainder."""
    n = len(a) - 1
    q = [0] * n
    acc = a[n]
    for i in range(n - 1, -1, -1):
        q[i] = acc
        acc = a[i] + acc * root
        if p:
            acc %= p
    assert acc == 0, "nonzero remainder: cancellation theorem violated"
    return trim(q)


def channels(nmax, p=None):
    """Lists Q[n], P[n], Qt[n], Pt[n] for n = 0..nmax (coefficients low->high)."""
    m1 = -1 if p is None else p - 1
    Q, P, Qt, Pt = [[0, m1]], [[1]], [[3, m1]], [[1]]
    six, tenR = [6, m1], [0, 10, -2 if p is None else p - 2]
    for n in range(1, nmax + 1):
        num = add(mul(six, comp_R(Q[-1], p), p), mul(tenR, comp_R(P[-1], p), p), p)
        num = div_lin(num, 5, p)            # divide by (lam - 5)
        if n >= 2:
            num = div_lin(num, 2, p)        # and by (lam - 2): total Delta
            den = comp_R(P[-1], p)
        else:
            num = scal(-1, num, p)          # (lam - 5) = -(5 - lam)
            den = [2, m1]
        Q.append(num); P.append(den)
        num = add(mul(six, comp_R(Qt[-1], p), p), mul(tenR, comp_R(Pt[-1], p), p), p)
        num = scal(-1, div_lin(num, 2, p), p)   # divide by (2 - lam)
        Qt.append(num); Pt.append(mul([5, m1], comp_R(Pt[-1], p), p))
    return Q, P, Qt, Pt


def pmod(a, b, p):
    a = a[:]
    inv = pow(b[-1], p - 2, p)
    db = len(b) - 1
    while len(a) - 1 >= db and not (len(a) == 1 and a[0] == 0):
        c = a[-1] * inv % p
        sh = len(a) - 1 - db
        for i in range(len(b)):
            a[sh + i] = (a[sh + i] - c * b[i]) % p
        a = trim(a)
    return a


def pgcd(a, b, p):
    while not (len(b) == 1 and b[0] == 0):
        a, b = b, pmod(a, b, p)
    return a


def peval(a, x, p=None):
    r = 0
    for c in reversed(a):
        r = r * x + c
        if p:
            r %= p
    return r


def certificate(nmax, p=P61):
    Q, P, Qt, Pt = channels(nmax, p)
    rows = []
    for n in range(3, nmax + 1):
        H = mul(Q[n - 1], Qt[n - 1], p)
        Rj = [0, 1]
        for j in range(n - 2):
            for a in (2, 5, 6):
                f = Rj[:]
                f[0] = (f[0] - a) % p
                H = mul(H, f, p)
            Rj = comp_R(Rj, p)
        HR = comp_R(H, p)
        gs, gt = pgcd(Q[n], HR, p), pgcd(Qt[n], HR, p)
        rows.append((n, len(gs) - 1, peval(gs, 0, p) == 0, len(gt) - 1))
    return rows


def numerical_support(nmax=6):
    import numpy as np
    sys.path.insert(0, __file__.rsplit("/", 1)[0])
    from check_decimation_hits import build_gasket, laplacian, eigenspaces
    Q, P, Qt, Pt = channels(nmax)
    for n in range(0, nmax + 1):
        X, E, C, _, _ = build_gasket(n)
        L = laplacian(len(X), E)
        N = len(L)
        I = np.setdiff1d(np.arange(N), C)
        x = 0.37
        A = L - x * np.eye(N)
        S = A[np.ix_(C, C)] - A[np.ix_(C, I)] @ np.linalg.solve(A[np.ix_(I, I)], A[np.ix_(I, C)])
        xf = Fraction(37, 100)                 # exact rational evaluation of Q/P
        es = S[0, 0] + 2 * S[0, 1] - float(Fraction(peval(Q[n], xf)) / peval(P[n], xf))
        et = S[0, 0] - S[0, 1] - float(Fraction(peval(Qt[n], xf)) / peval(Pt[n], xf))
        one = np.ones(3) / np.sqrt(3)
        sym = std = r3 = 0
        for lam, V in eigenspaces(L):
            W = V[C, :]
            a = np.linalg.norm(one @ W) > 1e-7
            b = np.linalg.norm(W - np.outer(one, one @ W)) > 1e-7
            sym += a; std += b
            if abs(lam - 3) < 1e-8:
                r3 = int(a) + 2 * int(b)
        print(f"n={n} schur_resid sym={es:.1e} std={et:.1e}  sigma={sym} "
              f"(2^(n-1)+1={2 ** (n - 1) + 1 if n else '-'}) tau={std} (2^n={2 ** n}) "
              f"c_n={sym + 2 * std} r_n(3)={r3}")


def main(nmax=11):
    t0 = time.time()
    Q, P, Qt, Pt = channels(EXACT_MAX)          # exact over Z, asserts divisibility
    for n in range(EXACT_MAX + 1):
        assert len(Q[n]) - 1 == (2 ** (n - 1) + 1 if n else 1)
        assert len(Qt[n]) - 1 == 2 ** n
        assert abs(Q[n][-1]) == 1 and abs(Qt[n][-1]) == 1
        if n >= 3:
            assert peval(Q[n], 3) != 0 and peval(Qt[n], 3) != 0
    print(f"exact Z recursion n<=8: divisibility, degrees, leading +-1, Q_n(3),Qt_n(3)!=0 (n>=3) OK "
          f"({time.time() - t0:.1f}s)")
    numerical_support()
    for n, ds, zero, dt in certificate(nmax):
        print(f"F_p certificate n={n}: deg gcd(Q_n, H(R))={ds} (lam | gcd: {zero}), "
              f"deg gcd(Qt_n, H(R))={dt}")
    print(f"total {time.time() - t0:.1f}s")


if __name__ == "__main__":
    main(int(sys.argv[1]) if len(sys.argv) > 1 else 11)
