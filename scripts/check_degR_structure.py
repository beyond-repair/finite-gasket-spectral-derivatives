"""Supporting computation for the README section
"Residue condition: degree of the elimination polynomial R" (structural checks).

Requires python-flint (tested with 0.9.0).  Exact arithmetic only.

Runs the repo's own `check_residue_p_plus_m.eliminate` unchanged on every prefix (all 2^m
prefixes for m <= 6, one per Frobenius orbit for m >= 7, the same `chains` as `filter`).
The only change is that `make_ring` is wrapped so that each relative norm N_l is
instrumented: before N_m it records d_0 = max degree over GF(2^e) of the A_1-coefficients
of G (monomial alpha-basis of A_m), and after each N_l (l = m, ..., 2) it records
d_r = max coefficient degree of the result (r = m - l + 1).  The final level-1 element is R.

Per prefix it checks:
  d_0 == m - 1;  d_r == 2 d_{r-1} - (m - r - 1) for r = 1..m-1;  d_{m-1} == deg R == 2^m - 2;
  R != 0;  every odd-index coefficient of R is zero (R in GF(2^e)[x^2]).
Mismatches are counted, not asserted, so a counterexample would be reported.

Usage:  python check_degR_structure.py M [workers [cache_dir]]

Nothing here selects W, takes a continuum limit, or constructs a force.
"""
import json
import os
import sys
import time
import multiprocessing

import flint

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import check_residue_p_plus_m as cr  # noqa: E402

_ORIG_MAKE_RING = cr.make_ring
_REC = []


def _maxdeg(u, l):
    if l == 1:
        return -1 if u.is_zero() else u.degree()
    return max(_maxdeg(u[0], l - 1), _maxdeg(u[1], l - 1))


def _instrumented_make_ring(P, X, z):
    r = dict(_ORIG_MAKE_RING(P, X, z))
    L = len(z) - 1
    orig_norm = r['norm']

    def norm(u, l):
        if l == L:
            _REC.append(_maxdeg(u, l))
        v = orig_norm(u, l)
        _REC.append(_maxdeg(v, l - 1))
        return v
    r['norm'] = norm
    return r


cr.make_ring = _instrumented_make_ring  # eliminate looks make_ring up in its module globals

_CTX = {}


def _ctx(m):
    if m not in _CTX:
        e = cr.field_degree(m)
        F = flint.fq_default_ctx(2, e); P = flint.fq_default_poly_ctx(F); X = P.gen()
        _CTX[m] = (e, F, P, X, cr.chains(F, P, X, m, m >= 7))
    return _CTX[m]


def _work(args):
    m, idx = args
    e, F, P, X, chs = _ctx(m)
    _REC.clear()
    t0 = time.time()
    R = cr.eliminate(P, X, chs[idx])
    seq = list(_REC)
    cs = R.coeffs()
    odd = sum(1 for i in range(1, len(cs), 2) if not cs[i].is_zero())
    return dict(idx=idx, seq=seq, degR=(-1 if R.is_zero() else R.degree()),
                Rzero=R.is_zero(), odd=odd, t=time.time() - t0)


def check(m, res):
    bad = dict(d0=0, rec=0, closed=0, degR=0, Rzero=0, odd=0, len=0)
    seqs = {}
    for r in res:
        s = r['seq']
        seqs[tuple(s)] = seqs.get(tuple(s), 0) + 1
        if len(s) != m:
            bad['len'] += 1; continue
        if s[0] != m - 1: bad['d0'] += 1
        if any(s[k] != 2 * s[k - 1] - (m - k - 1) for k in range(1, m)): bad['rec'] += 1
        if s[-1] != 2**m - 2: bad['closed'] += 1
        if r['degR'] != 2**m - 2 or r['degR'] != s[-1]: bad['degR'] += 1
        if r['Rzero']: bad['Rzero'] += 1
        if r['odd']: bad['odd'] += 1
    return bad, seqs


def main():
    m = int(sys.argv[1]); workers = int(sys.argv[2]) if len(sys.argv) > 2 else 1
    cache = sys.argv[3] if len(sys.argv) > 3 else None
    e, F, P, X, chs = _ctx(m)
    n = len(chs); t0 = time.time()
    done = {}
    if cache:
        os.makedirs(cache, exist_ok=True)
        for i in range(n):
            fp = os.path.join(cache, f'{i}.json')
            if os.path.exists(fp): done[i] = json.load(open(fp))
    todo = [(m, i) for i in range(n) if i not in done]
    def store(r):
        done[r['idx']] = r
        if cache:
            tmp = os.path.join(cache, f'{r["idx"]}.tmp')
            json.dump(r, open(tmp, 'w')); os.replace(tmp, os.path.join(cache, f'{r["idx"]}.json'))
    if workers <= 1:
        for a in todo: store(_work(a))
    elif todo:
        with multiprocessing.get_context('spawn').Pool(workers) as pool:  # fork deadlocks with flint
            for r in pool.imap_unordered(_work, todo, chunksize=1): store(r)
    res = [done[i] for i in range(n)]
    bad, seqs = check(m, res)
    expect = [m - 1]
    for k in range(1, m): expect.append(2 * expect[-1] - (m - k - 1))
    print(f'degR-structure m={m} e={e} orbit={m >= 7} prefixes={n} (computed this call: {len(todo)}) '
          f'expected_seq={expect} observed_seqs={{{", ".join(f"{list(k)}: {v}" for k, v in seqs.items())}}} '
          f'degR={sorted({r["degR"] for r in res})} mismatches={bad} '
          f'sum_prefix_time={sum(r["t"] for r in res):.1f}s wall={time.time() - t0:.1f}s', flush=True)
    return 0 if not any(bad.values()) else 1


if __name__ == '__main__':
    sys.exit(main())
