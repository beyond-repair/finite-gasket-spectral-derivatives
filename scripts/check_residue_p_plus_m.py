"""Supporting computation for the README section
"Residue condition: lengths 2^j + m for small m (elimination over a fixed field)".

Requires python-flint (pip install python-flint; tested with 0.9.0).  Exact arithmetic only.

Modes
  python check_residue_p_plus_m.py filter M [orbit]
      For every chain prefix z_1..z_M (all prefixes, or one per Frobenius orbit), build
      R(x) = full relative norm of G (see eliminate) in GF(2^e)[x], e = 2^ceil(log2(M+1)),
      assert R != 0, factor it over GF(2^e), and for every irreducible factor f of degree
      d = 2^i with p = e*d > M test the chain condition N^(p-1-M)(c) = z_M in GF(2^e)[x]/(f),
      c = z_1 (x^2 + x).  Prints the candidate and surviving values of p.
  python check_residue_p_plus_m.py direct M P [orbit]
      In GF(2^(2P)), enumerate every chain of length P+M whose alpha_1 = z_{P+1} + z_1 z_P is a root
      of R lying in GF(2^P) and whose c satisfies the chain condition; this contains every chain
      with S_{P+M} in GF(2^P).  Prints how many have S in GF(2^P) and how many have S = 0.

Nothing here selects W, takes a continuum limit, or constructs a force.
"""
import os
import sys
import time

import flint


def make_ring(P, X, z):
    """Nested ring GF(q)[x][alpha_2..alpha_m]/(alpha_i^2+alpha_i = alpha_{i-1} + c z_i^2), alpha_1 = x."""
    m = len(z) - 1
    c = z[1] * (X**2 + X)                    # c = omega (x^2 + x), omega = z_1
    kappa = {i: c * (z[i]**2) for i in range(2, m + 1)}
    ZERO = P.zero()
    def zero(l): return ZERO if l == 1 else (zero(l-1), zero(l-1))
    def add(u, v, l):
        if l == 1: return u + v
        return (add(u[0], v[0], l-1), add(u[1], v[1], l-1))
    def smul(u, s, l):  # times a polynomial in x
        if l == 1: return u * s
        return (smul(u[0], s, l-1), smul(u[1], s, l-1))
    def mul_alpha(u, i, l):  # u * alpha_i, level l >= i
        if i == 1: return smul(u, X, l)
        if l > i: return (mul_alpha(u[0], i, l-1), mul_alpha(u[1], i, l-1))
        a, b = u  # l == i: (a + b al) al = b beta_i + (a+b) al, beta_i = alpha_{i-1} + kappa_i
        bb = add(mul_alpha(b, i-1, i-1), smul(b, kappa[i], i-1), i-1)
        return (bb, add(a, b, i-1))
    def mul_beta(u, l):  # u * beta_l with u at level l-1
        return add(mul_alpha(u, l-1, l-1), smul(u, kappa[l], l-1), l-1)
    def mul(u, v, l):
        if l == 1: return u * v
        a, b = u; a2, b2 = v
        aa = mul(a, a2, l-1); bb = mul(b, b2, l-1)
        mid = mul(add(a, b, l-1), add(a2, b2, l-1), l-1)
        return (add(aa, mul_beta(bb, l), l-1), add(mid, aa, l-1))   # (a+b)(a'+b') + aa' = ab'+a'b+bb'
    def sq(u, l):
        if l == 1: return u * u
        a, b = u
        a2 = sq(a, l-1); b2 = sq(b, l-1)
        return (add(a2, mul_beta(b2, l), l-1), b2)
    def norm(u, l):  # level l -> l-1: a^2 + ab + b^2 beta_l
        a, b = u
        return add(add(sq(a, l-1), mul(a, b, l-1), l-1), mul_beta(sq(b, l-1), l), l-1)
    def const(s, l):
        return s if l == 1 else (const(s, l-1), zero(l-1))
    def alpha(i, l):
        if i == 1: return const(X, l)
        if l == i: return (zero(i-1), const(P.one(), i-1))
        return (alpha(i, l-1), zero(l-1))
    return dict(add=add, smul=smul, mul_alpha=mul_alpha, norm=norm, const=const, alpha=alpha, c=c)

def eliminate(P, X, z):
    """R(x) = norm of G, where G = w^2 prod_{i>=2} Nm_i + (x+1) sum_i z_i prod_{l != i} Nm_l,
    Nm_i = (1 + z_i) alpha_i + alpha_{i-1}; C_1 = G / ((x+1) prod Nm_i)."""
    m = len(z) - 1; L = m
    r = make_ring(P, X, z)
    add, smul, mul_alpha, const = r['add'], r['smul'], r['mul_alpha'], r['const']
    def times_Nm(u, i):  # u * Nm_i at level L
        return add(smul(mul_alpha(u, i, L), P(1 + z[i]), L), mul_alpha(u, i-1, L), L)
    w = z[1]
    if m == 1:
        return P(w**2)  # C_1 = w^2/(x+1): never zero
    G = const(P(w**2), L)
    for i in range(2, m + 1): G = times_Nm(G, i)
    for i in range(2, m + 1):
        t = const(P(z[i]) * (X + 1), L)
        for l2 in range(2, m + 1):
            if l2 != i: t = times_Nm(t, l2)
        G = add(G, t, L)
    R = G
    for l in range(L, 1, -1): R = r['norm'](R, l)
    return R

def chains(F, P, X, m, orbit):
    chs = [[F.one()]]
    for i in range(1, m + 1):
        new = []
        for ch in chs:
            rs = [rr for rr, _ in (X**2 + X + ch[-1]).roots()]
            assert len(rs) == 2
            if orbit and (i & (i - 1)) == 0: rs = rs[:1]
            for rr in rs: new.append(ch + [rr])
        chs = new
    return chs


def field_degree(m):
    e = 1
    while e < m + 1:
        e *= 2
    return e


def run_filter(m, orbit):
    e = field_degree(m)
    F = flint.fq_default_ctx(2, e); P = flint.fq_default_poly_ctx(F); X = P.gen()
    t0 = time.time(); cand = {}; surv = {}; degR = None
    chs = chains(F, P, X, m, orbit)
    for ch in chs:
        R = eliminate(P, X, ch)
        assert not R.is_zero(), 'R vanishes identically'
        degR = R.degree()
        for f, _ in R.factor()[1]:
            d = f.degree()
            if d & (d - 1):
                continue
            p = e * d
            if p <= m:
                continue
            cand[p] = cand.get(p, 0) + 1
            c = (P(ch[1]) * (X**2 + X)) % f
            for _ in range(p - 1 - m):
                c = (c * c + c) % f
            if c == P(ch[m]) % f:
                surv[p] = surv.get(p, 0) + 1
    print(f'filter m={m} e={e} prefixes={len(chs)} degR={degR} '
          f'power-of-two-degree factors (p: count)={dict(sorted(cand.items()))} '
          f'surviving chain condition (p: count)={dict(sorted(surv.items()))} time={time.time()-t0:.1f}s', flush=True)


def run_direct(m, p, orbit):
    F = flint.fq_default_ctx(2, 2 * p); P = flint.fq_default_poly_ctx(F); X = P.gen()

    def asroots(b):
        rs = [r for r, _ in (X**2 + X + b).roots()]
        assert len(rs) == 2
        return rs

    def in_p(y):
        t = y
        for _ in range(p):
            t = t * t
        return t == y

    t0 = time.time(); seen = set(); nc = nchain = nin = nzero = 0
    for pre in chains(F, P, X, m, orbit):
        R = eliminate(P, X, pre)
        assert not R.is_zero()
        w = pre[1]
        g = R.gcd(X.pow_mod(2**p, R) - X)  # the roots of R that lie in GF(2^p)
        for a1, _ in (g.roots() if g.degree() > 0 else []):
            if not in_p(a1):
                continue
            c = w * (a1 * a1 + a1)
            zs = [c]
            for _ in range(p - 1 - m):
                zs.append(zs[-1] * zs[-1] + zs[-1])
            if zs[-1] != pre[m] or str(c) in seen:
                continue
            seen.add(str(c)); nc += 1
            low = pre[1:m + 1] + list(reversed(zs))[1:]      # z_1 .. z_{p-1}
            assert len(low) == p - 1 and low[-1] == c
            Sl = sum((1 / y for y in low), F.zero())
            for zp in asroots(c):
                tops = [[zp]]
                for _ in range(m):
                    tops = [t + [r] for t in tops for r in asroots(t[-1])]
                for t in tops:
                    nchain += 1
                    S = Sl + sum((1 / y for y in t), F.zero())
                    if in_p(S):
                        nin += 1
                        nzero += S.is_zero()
    print(f'direct k={p+m} (p={p}, m={m}, {"orbit reps" if orbit else "all prefixes"}): '
          f'admissible c={nc}, chains examined={nchain}, with S in GF(2^p)={nin}, with S = 0: {nzero}, '
          f'time={time.time()-t0:.1f}s', flush=True)


if __name__ == '__main__':
    mode = sys.argv[1]; orbit = 'orbit' in sys.argv[2:]
    if mode == 'filter':
        run_filter(int(sys.argv[2]), orbit)
    else:
        run_direct(int(sys.argv[2]), int(sys.argv[3]), orbit)
    sys.stdout.flush()
    os._exit(0)  # python-flint 0.9 can crash in context teardown; results are already printed
