"""Supporting numerics for the README section "Free decimation hit predicate".

Rebuilds the finest-only gasket graph exactly as sierpinski-geometry-045
gasket_graph.build_gasket does, and for free L = D - A reports, per level n:
  N, exceptional mass (eigenvalues 3, 5, 6), hit mass under predicate H_n,
  non-hit mass, the corner-visible dimension c_n, dim DN_n(2), and the
  decimation-identity residual (midpoint extension + corner defect 2*lam/(2-lam)).
It also computes c_2 and c_3 exactly as rational Krylov ranks.

Numerical observation only (except the exact Krylov ranks, which are finite
exact computations). It does not select W, construct a force, or take a
continuum limit.
"""
from __future__ import annotations

import math
from fractions import Fraction

import numpy as np


def build_gasket(level):
    c0, c1, c2 = np.array([0.0, 0.0]), np.array([1.0, 0.0]), np.array([0.5, math.sqrt(3) / 2])
    pos, pts, edges = {}, [], set()

    def key(p):
        return (round(float(p[0]), 10), round(float(p[1]), 10))

    def vid(p):
        k = key(p)
        if k not in pos:
            pos[k] = len(pts)
            pts.append(p.copy())
        return pos[k]

    def rec(a, b, c, d):
        if d == 0:
            ia, ib, ic = vid(a), vid(b), vid(c)
            for i, j in ((ia, ib), (ib, ic), (ic, ia)):
                edges.add((min(i, j), max(i, j)))
            return
        rec(a, 0.5 * (a + b), 0.5 * (c + a), d - 1)
        rec(0.5 * (a + b), b, 0.5 * (b + c), d - 1)
        rec(0.5 * (c + a), 0.5 * (b + c), c, d - 1)

    rec(c0, c1, c2, level)
    corners = [pos[key(c0)], pos[key(c1)], pos[key(c2)]]
    return np.vstack(pts), sorted(edges), corners, pos, key


def laplacian(n, edges):
    L = np.zeros((n, n))
    for i, j in edges:
        L[i, i] += 1; L[j, j] += 1; L[i, j] -= 1; L[j, i] -= 1
    return L


def eigenspaces(L, tol=1e-8):
    w, V = np.linalg.eigh(L)
    out, i = [], 0
    while i < len(w):
        j = i
        while j + 1 < len(w) and abs(w[j + 1] - w[i]) < tol:
            j += 1
        out.append((float(w[i:j + 1].mean()), V[:, i:j + 1]))
        i = j + 1
    return out


def R(z):
    return z * (5 - z)


def exact_krylov_dim(level):
    _, E, C, _, _ = build_gasket(level)
    N = 1 + max(max(e) for e in E)
    adj = [[] for _ in range(N)]
    for i, j in E:
        adj[i].append(j); adj[j].append(i)
    basis = {}
    for c in C:
        v = [0] * N; v[c] = 1
        for _ in range(N):
            w = [Fraction(x) for x in v]
            for p, b in basis.items():
                if w[p] != 0:
                    f = w[p] / b[p]
                    w = [a - f * q for a, q in zip(w, b)]
            piv = next((i for i, x in enumerate(w) if x != 0), None)
            if piv is None:
                break
            basis[piv] = w
            v = [len(adj[i]) * v[i] - sum(v[j] for j in adj[i]) for i in range(N)]
    return len(basis)


def main(nmax=6):
    prev = None
    for n in range(1, nmax + 1):
        P, E, C, pos, key = build_gasket(n)
        N = len(P)
        L = laplacian(N, E)
        Pp, Ep, Cp, _, _ = build_gasket(n - 1)
        Lp = laplacian(len(Pp), Ep)
        spec_prev = np.linalg.eigvalsh(Lp)
        exc = hit = nonhit = c = dn2 = 0
        for lam, V in eigenspaces(L):
            m = V.shape[1]
            r = np.linalg.matrix_rank(V[C, :], tol=1e-8)
            c += r
            if abs(lam - 2) < 1e-8:
                dn2 += m - r
            if min(abs(lam - 3), abs(lam - 5), abs(lam - 6)) < 1e-8:
                exc += m
            elif np.min(np.abs(spec_prev - R(lam))) < 1e-7:
                hit += m
            else:
                nonhit += m
        # decimation identity with corner defect, random v on V_{n-1}, lam = 0.73
        emb = np.array([pos[key(p)] for p in Pp])
        mid = np.setdiff1d(np.arange(N), emb)
        lam = 0.73
        v = np.random.default_rng(0).standard_normal(len(Pp))
        u = np.zeros(N); u[emb] = v
        A = L - lam * np.eye(N)
        u[mid] = np.linalg.solve(A[np.ix_(mid, mid)], -A[np.ix_(mid, emb)] @ v)
        rhs = (6 - lam) / ((2 - lam) * (5 - lam)) * ((Lp - R(lam) * np.eye(len(Pp))) @ v)
        rhs[Cp] += 2 * lam / (2 - lam) * v[Cp]
        resid = float(np.max(np.abs((A @ u)[emb] - rhs)))
        print(f"n={n} N={N} exc={exc} hit={hit} nonhit={nonhit} c_n={c} "
              f"5*2^(n-1)+1={5 * 2 ** (n - 1) + 1} dimDN(2)={dn2} "
              f"h_n={hit / N:.4f} 1-mu_exc={1 - exc / N:.4f} identity_resid={resid:.1e}")
    for n in (2, 3):
        print(f"exact rational Krylov dim c_{n} = {exact_krylov_dim(n)}")


if __name__ == "__main__":
    main()
