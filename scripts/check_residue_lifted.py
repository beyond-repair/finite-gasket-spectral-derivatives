"""Supporting computation for the README section
"Residue condition: lengths 2^j + m for small m (elimination over a fixed field)":
a faster, equivalent form of `check_residue_p_plus_m.py direct`.

Requires python-flint (tested with 0.9.0).  Exact arithmetic only.

Why it is equivalent (uses only the lemma already recorded in the README):
a chain with S_{p+m} in GF(2^p) has alpha_1 a root of R (computed over GF(2^e),
e = 2^ceil(log2(m+1))) lying in GF(2^p), and c = z_1(alpha_1^2+alpha_1) = z_{p-1} has
degree exactly p, so alpha_1 has degree exactly p/e over GF(2^e) and the chain condition
N^(p-1-m)(c) = z_m holds.  Hence alpha_1 is a root of an irreducible factor f of R over
GF(2^e) with deg f = p/e that passes the chain condition modulo f -- exactly the factors
that `filter` reports as surviving.  `direct` recomputes R over GF(2^(2p)) and scans all
of its roots in GF(2^p); here R is computed once over GF(2^e), only surviving factors are
kept, and those are mapped into GF(2^(2p)) by a field embedding GF(2^e) -> GF(2^(2p))
(a root of the defining polynomial of GF(2^e)).  The count of S = 0 is Galois-invariant,
so the choice of embedding does not matter.  The enumeration of chain tops and the tests
`S in GF(2^p)`, `S = 0` are the same code as `direct`.

Modes
  python check_residue_lifted.py prepare M OUT.json [workers]
      Orbit prefixes; R over GF(2^e); for every irreducible factor of degree 2^i passing
      the chain condition, store (prefix, factor, p).  Also prints the filter summary.
  python check_residue_lifted.py lift IN.json P [all|rep|verify]
      Embed every stored factor with that p into GF(2^(2P)) and enumerate as `direct ... orbit`
      (`all`, default: every root of every factor, chains deduplicated by c, same counts as direct).
      `rep`: one root per surviving factor.  Valid for the question "is S = 0 ever?" because
      sigma = Frobenius^e fixes GF(2^e) pointwise (so it fixes the prefix and f), permutes the
      roots of the irreducible f transitively, maps the chains attached to a root r bijectively
      onto those attached to sigma(r), and maps S to sigma(S); S = 0 and S in GF(2^p) are
      preserved.  `verify`: every root, no deduplication; asserts that the per-root counts
      agree within each factor (an exact check of that equivariance on the given data).

Nothing here selects W, takes a continuum limit, or constructs a force.
"""
import json
import os
import sys
import time
import multiprocessing

import flint

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from check_residue_p_plus_m import chains, eliminate, field_degree  # noqa: E402


_CTX = {}


def _ctx(m):
    """One context per process, kept alive: python-flint 0.9 can crash when a context is freed."""
    if m not in _CTX:
        e = field_degree(m)
        F = flint.fq_default_ctx(2, e); P = flint.fq_default_poly_ctx(F); X = P.gen()
        _CTX[m] = (e, F, P, X, chains(F, P, X, m, True))
    return _CTX[m]


def _work(args):
    m, idx = args
    e, F, P, X, chs = _ctx(m)
    ch = chs[idx]
    R = eliminate(P, X, ch)
    assert not R.is_zero(), 'R vanishes identically'
    cand, out = {}, []
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
            out.append(dict(p=p, f=[[int(b) for b in a.to_list()] for a in f.coeffs()]))
    return dict(idx=idx, degR=R.degree(), cand=cand,
                prefix=[[int(b) for b in z.to_list()] for z in ch], surv=out)


def prepare(m, out, workers):
    """Per-prefix results are cached in OUT.json.d/ so an interrupted run resumes."""
    e, F, P, X, chs = _ctx(m)
    n = len(chs)
    cache = out + '.d'; os.makedirs(cache, exist_ok=True)
    todo = [i for i in range(n) if not os.path.exists(os.path.join(cache, f'{i}.json'))]
    t0 = time.time()
    if todo:
        with multiprocessing.get_context('spawn').Pool(workers) as pool:  # fork deadlocks with flint
            for r in pool.imap_unordered(_work, [(m, i) for i in todo], chunksize=1):
                tmp = os.path.join(cache, f'{r["idx"]}.tmp')
                json.dump(r, open(tmp, 'w')); os.replace(tmp, os.path.join(cache, f'{r["idx"]}.json'))
    res = [json.load(open(os.path.join(cache, f'{i}.json'))) for i in range(n)]
    cand, surv = {}, {}
    for r in res:
        for p, k in r['cand'].items(): cand[int(p)] = cand.get(int(p), 0) + k
        for s in r['surv']: surv[s['p']] = surv.get(s['p'], 0) + 1
    json.dump(dict(m=m, e=e, modulus=[int(str(a)) for a in F.modulus().coeffs()], prefixes=res),
              open(out, 'w'))
    print(f'prepare m={m} e={e} prefixes={n} (computed this call: {len(todo)}) '
          f'degR={sorted({r["degR"] for r in res})} '
          f'power-of-two-degree factors (p: count)={dict(sorted(cand.items()))} '
          f'surviving chain condition (p: count)={dict(sorted(surv.items()))} '
          f'time={time.time()-t0:.1f}s', flush=True)


def lift(path, p, mode='all'):
    data = json.load(open(path)); m, e = data['m'], data['e']
    F = flint.fq_default_ctx(2, 2 * p); P = flint.fq_default_poly_ctx(F); X = P.gen()
    t0 = time.time()
    beta = P(data['modulus']).roots()[0][0]           # embedding GF(2^e) -> GF(2^(2p))
    pw = [F.one()]
    for _ in range(e - 1): pw.append(pw[-1] * beta)
    def emb(bits): return sum((pw[i] for i, b in enumerate(bits) if b), F.zero())

    def asroots(b):
        rs = [r for r, _ in (X**2 + X + b).roots()]
        assert len(rs) == 2
        return rs

    def in_p(y):
        t = y
        for _ in range(p):
            t = t * t
        return t == y

    nf = nc = nchain = nin = nzero = 0; seen = set(); per_factor = []

    def tops_counts(c, low_sum):
        n_ch = n_in = n_zero = 0
        for zp in asroots(c):
            tops = [[zp]]
            for _ in range(m):
                tops = [t + [rr] for t in tops for rr in asroots(t[-1])]
            for t in tops:
                n_ch += 1
                S = low_sum + sum((1 / y for y in t), F.zero())
                if in_p(S):
                    n_in += 1
                    n_zero += S.is_zero()
        return n_ch, n_in, n_zero

    for r in data['prefixes']:
        pre = [emb(z) for z in r['prefix']]
        for i in range(1, m + 1):                       # embedded prefix is a chain
            assert pre[i] ** 2 + pre[i] == pre[i - 1]
        w = pre[1]
        for s in r['surv']:
            if s['p'] != p:
                continue
            nf += 1
            f = P([emb(a) for a in s['f']])
            rts = f.roots()
            assert len(rts) == f.degree()                 # degree p/e factor splits in GF(2^p)
            if mode == 'rep':
                rts = rts[:1]
            counts = []
            for a1, _ in rts:
                assert in_p(a1)
                c = w * (a1 * a1 + a1)
                zs = [c]
                for _ in range(p - 1 - m):
                    zs.append(zs[-1] * zs[-1] + zs[-1])
                assert zs[-1] == pre[m]                    # chain condition, already true mod f
                if mode == 'all':
                    if str(c) in seen:
                        continue
                    seen.add(str(c))
                nc += 1
                low = pre[1:m + 1] + list(reversed(zs))[1:]
                assert len(low) == p - 1 and low[-1] == c
                Sl = sum((1 / y for y in low), F.zero())
                cnt = tops_counts(c, Sl)
                counts.append(cnt)
                nchain += cnt[0]; nin += cnt[1]; nzero += cnt[2]
            if mode == 'verify':
                assert len(set(counts)) == 1, counts
            per_factor.append(counts[0] if counts else None)
    extra = f' per-factor (chains, S in GF, S=0) for one root={per_factor}' if mode != 'all' else ''
    print(f'lift[{mode}] k={p+m} (p={p}, m={m}, orbit reps): surviving factors={nf}, '
          f'{"admissible c" if mode == "all" else "roots used"}={nc}, '
          f'chains examined={nchain}, with S in GF(2^p)={nin}, with S = 0: {nzero}, '
          f'time={time.time()-t0:.1f}s{extra}', flush=True)


if __name__ == '__main__':
    if sys.argv[1] == 'prepare':
        prepare(int(sys.argv[2]), sys.argv[3], int(sys.argv[4]) if len(sys.argv) > 4 else 4)
    else:
        lift(sys.argv[2], int(sys.argv[3]), sys.argv[4] if len(sys.argv) > 4 else 'all')
    sys.stdout.flush()
    os._exit(0)
