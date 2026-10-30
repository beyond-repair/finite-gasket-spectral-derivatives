"""Checkpointed / resumable `lift` of scripts/check_residue_lifted.py (engineering change only).

Same mathematics, same counts and same output line as
    python check_residue_lifted.py lift IN.json P [all|rep|verify]
(see that file for why the computation is equivalent to `direct`).  Differences, none of
which changes what is counted:

* Chain tops are enumerated depth-first in a canonical order (the two roots of
  y^2 + y = b sorted by coefficient bits) instead of building the full list of 2^(m+1)
  tops in memory.  The counts are sums over the same set of tops, so they are unchanged;
  memory drops from O(2^m) field elements per root to O(m).
* Every --interval seconds (default 300) the cursor (factor number, root number, top
  number), the partial counts, the roots already found for the current factor and, for
  `all`, the set of c already seen are written to CKPT.tmp and renamed over CKPT (atomic).
  `--resume` continues from it; the stored roots are re-checked (f(r) = 0, r in GF(2^p))
  instead of being recomputed, so a resumed `rep` run uses the same root as before.  The
  checkpoint records sha256 of IN.json, P and the mode, and is refused if they differ.
* `time=` in the output line is wall time summed over all runs of this job.

Usage: python check_residue_lifted_ckpt.py IN.json P [all|rep|verify] [--ckpt F] [--resume]
                                           [--interval S] [--stop-after-tops N]  (test hook, exit 75)
Nothing here selects W, takes a continuum limit, or constructs a force.
"""
import hashlib
import json
import os
import sys
import time

import flint

FMT = 1


def bits(x):
    return [int(b) for b in x.to_list()]


def atomic_write(path, obj):
    tmp = path + '.tmp'
    with open(tmp, 'w') as fh:
        json.dump(obj, fh)
        fh.flush(); os.fsync(fh.fileno())
    os.replace(tmp, path)
    dfd = os.open(os.path.dirname(os.path.abspath(path)), os.O_RDONLY)
    try:
        os.fsync(dfd)
    finally:
        os.close(dfd)


def main(argv):
    path, p = argv[0], int(argv[1])
    mode = argv[2] if len(argv) > 2 and not argv[2].startswith('--') else 'all'
    opts = argv[2:] if mode == 'all' and (len(argv) <= 2 or argv[2].startswith('--')) else argv[3:]
    ck, resume, interval, stop_after = None, False, 300.0, -1
    i = 0
    while i < len(opts):
        o = opts[i]
        if o == '--ckpt': ck = opts[i + 1]; i += 2
        elif o == '--resume': resume = True; i += 1
        elif o == '--interval': interval = float(opts[i + 1]); i += 2
        elif o == '--stop-after-tops': stop_after = int(opts[i + 1]); i += 2
        else: sys.exit(f'unknown argument {o}')
    if resume and not ck: sys.exit('--resume needs --ckpt')
    raw = open(path, 'rb').read(); digest = hashlib.sha256(raw).hexdigest()
    data = json.loads(raw); m, e = data['m'], data['e']
    F = flint.fq_default_ctx(2, 2 * p); P = flint.fq_default_poly_ctx(F); X = P.gen()
    t0 = time.time()
    beta = P(data['modulus']).roots()[0][0]           # embedding GF(2^e) -> GF(2^(2p))
    pw = [F.one()]
    for _ in range(e - 1): pw.append(pw[-1] * beta)
    def emb(bs): return sum((pw[i] for i, b in enumerate(bs) if b), F.zero())

    def asroots(b):
        rs = [r for r, _ in (X**2 + X + b).roots()]
        assert len(rs) == 2
        return sorted(rs, key=bits)                    # canonical order (resume indexing)

    def in_p(y):
        t = y
        for _ in range(p):
            t = t * t
        return t == y

    # work items: (prefix number, surv number) with this p, in file order (as the original)
    items = [(ri, si) for ri, r in enumerate(data['prefixes']) for si, s in enumerate(r['surv']) if s['p'] == p]
    st = dict(fmt=FMT, sha256=digest, p=p, mode=mode, item=0, roots=None, root=0, top=0,
              nf=0, nc=0, nchain=0, nin=0, nzero=0, cur=[0, 0, 0], counts=[], per_factor=[],
              seen=[], elapsed=0.0)
    if resume and os.path.exists(ck):
        old = json.load(open(ck))
        if (old.get('fmt'), old.get('sha256'), old.get('p'), old.get('mode')) != (FMT, digest, p, mode):
            sys.exit(f'checkpoint {ck} does not match this job; refusing')
        st = old
        print(f'# resumed from {ck}: item {st["item"]}/{len(items)} root {st["root"]} top {st["top"]}',
              file=sys.stderr, flush=True)
    seen = set(st['seen'])
    elapsed0 = st['elapsed']; last = time.time(); done_tops = 0

    def save():
        st['seen'] = sorted(seen); st['elapsed'] = elapsed0 + time.time() - t0
        atomic_write(ck, st)

    pre_cache = {}
    while st['item'] < len(items):
        ri, si = items[st['item']]
        r = data['prefixes'][ri]; s = r['surv'][si]
        if ri not in pre_cache:
            pre = [emb(z) for z in r['prefix']]
            for i in range(1, m + 1):
                assert pre[i] ** 2 + pre[i] == pre[i - 1]
            pre_cache = {ri: pre}
        pre = pre_cache[ri]; w = pre[1]
        f = P([emb(a) for a in s['f']])
        if st['roots'] is None:                        # new factor
            st['nf'] += 1
            rts = [a for a, _ in f.roots()]
            assert len(rts) == f.degree()
            if mode == 'rep':
                rts = rts[:1]
            st['roots'] = [bits(a) for a in rts]; st['root'] = 0; st['top'] = 0
            st['counts'] = []; st['cur'] = [0, 0, 0]
            rts_el = rts
        else:                                          # resumed factor: re-check stored roots
            rts_el = [F(b) for b in st['roots']]
            for a in rts_el:
                assert f(a).is_zero()
        while st['root'] < len(rts_el):
            a1 = rts_el[st['root']]
            assert in_p(a1)
            c = w * (a1 * a1 + a1)
            zs = [c]
            for _ in range(p - 1 - m):
                zs.append(zs[-1] * zs[-1] + zs[-1])
            assert zs[-1] == pre[m]
            if mode == 'all' and st['top'] == 0 and str(c) in seen:
                st['root'] += 1; continue
            low = pre[1:m + 1] + list(reversed(zs))[1:]
            assert len(low) == p - 1 and low[-1] == c
            Sl = sum((1 / y for y in low), F.zero())
            ntops = 2 ** (m + 1)                       # zp choice, then m further choices
            t = st['top']
            while t < ntops:
                # top number t: bit (m - j) of t is the choice at level j (j = 0 is zp)
                b, S = c, Sl
                for j in range(m + 1):
                    y = asroots(b)[(t >> (m - j)) & 1]
                    S = S + 1 / y; b = y
                st['cur'][0] += 1
                if in_p(S):
                    st['cur'][1] += 1; st['cur'][2] += int(S.is_zero())
                t += 1; st['top'] = t; done_tops += 1
                if ck and (time.time() - last >= interval or done_tops == stop_after):
                    save(); last = time.time()
                    print(f'# checkpoint item {st["item"]} root {st["root"]} top {t}/{ntops}', file=sys.stderr, flush=True)
                if done_tops == stop_after:
                    print('# stopped by --stop-after-tops (test hook)', file=sys.stderr, flush=True)
                    sys.stdout.flush(); os._exit(75)
            if mode == 'all':
                seen.add(str(c))
            st['nc'] += 1
            cnt = st['cur']; st['counts'].append(list(cnt))
            st['nchain'] += cnt[0]; st['nin'] += cnt[1]; st['nzero'] += cnt[2]
            st['cur'] = [0, 0, 0]; st['root'] += 1; st['top'] = 0
        if mode == 'verify':
            assert len({tuple(x) for x in st['counts']}) == 1, st['counts']
        st['per_factor'].append(tuple(st['counts'][0]) if st['counts'] else None)
        st['item'] += 1; st['roots'] = None
        if ck:
            save(); last = time.time()
    if ck:
        save()
    pf = [tuple(x) if x is not None else None for x in st['per_factor']]
    extra = f' per-factor (chains, S in GF, S=0) for one root={pf}' if mode != 'all' else ''
    total = elapsed0 + time.time() - t0
    print(f'lift[{mode}] k={p+m} (p={p}, m={m}, orbit reps): surviving factors={st["nf"]}, '
          f'{"admissible c" if mode == "all" else "roots used"}={st["nc"]}, '
          f'chains examined={st["nchain"]}, with S in GF(2^p)={st["nin"]}, with S = 0: {st["nzero"]}, '
          f'time={total:.1f}s{extra}', flush=True)


if __name__ == '__main__':
    main(sys.argv[1:])
    sys.stdout.flush()
    os._exit(0)
