# Claim status — finite-gasket-spectral-derivatives

**Classification:** RESEARCH
**Claim cap:** ≤ 1 (finite discrete kernel identities)
**Sweep:** 283 / re-audit of PASS-2026-10-01-167
**Head recorded:** 7e2ca1b06239ca6a34fef357185ebdc3aab300b0 (kernel commit). This file update follows that commit.
**Prior claim head:** 9aa404950322594069bf91547ea2cb34c253eaae

| Capability | State | Evidence |
|---|---|---|
| `gamma_loop`, `dgamma_dw`, `v_second` on a supplied eigenvalue list | IMPLEMENTED + locally TESTED | `scripts/spectral_derivatives.py`; `tests/test_spectral_derivatives.py`; local unittest 5 passed (Sweep-283) |
| Positive-definiteness guard `omega^2 - W lambda > 0`, including `omega2 != 1` | IMPLEMENTED + locally TESTED | `test_omega2_scales_the_positive_wall` |
| `gasket-spectral` CLI (`kernel` on `build_gasket(level)` or a supplied list, `decimation`), installable via `pyproject.toml` | IMPLEMENTED + locally TESTED | `scripts/cli.py`; `tests/test_cli.py` (11 tests). W is a required input. Numerical checks only; not a proof and no claim raise |
| Actions `spectral-kernel` on kernel commit `7e2ca1b` | OBSERVED success | run 37671378075, conclusion success, 2026-10-07. Prior success run 37069941476 on `19a1264e`. Not a gasket proof. |
| Power-series remainder / hypergeometric identities | CLAIMED (prose derivation in README) | not executed as a test in this repository |
| Free `mult(6) = (3^n - 3)/2` on `build_gasket(n)` | CLAIMED | prose argument in README / COMPLETION_LOG.md; graph constructor lives in `sierpinski-geometry-045`, not in this tree |
| Free `mult(5) = (3^{n-1} - 1)/2` (n ≥ 3) on `build_gasket(n)` | CLAIMED | prose argument in README / COMPLETION_LOG.md |
| Free `mult(3) = (3^{n-1} - 3)/2` (n ≥ 2) on `build_gasket(n)` | CLAIMED | prose argument in README / COMPLETION_LOG.md |
| Exceptional mass `M_exc = (5·3^{n-1}-7)/2`, `μ_exc → 5/9` (n ≥ 3) | CLAIMED | corollary of the three free mult theorems + `|V_n|` from gasket_graph.py; README / COMPLETION_LOG.md |
| Dirichlet `λ_min(n)=φ_-^{(n-1)}(2)`, ratio `→ 1/5` | CLAIMED | Qiu §2 structure (opened) + branch comparison; README / COMPLETION_LOG.md |
| Hit mass `h_n → 4/9`, bound `1 − μ_exc − 5·2^n/(3^{n+1}+3) ≤ h_n ≤ 1 − μ_exc` (n ≥ 3), for the README-defined hit predicate | CLAIMED | prose argument in README / COMPLETION_LOG.md; supporting numerics `scripts/check_decimation_hits.py` (not a test) |
| Corner channels: `s_n = Q_n/(2 − R^{n−1})`, `t_n = Qt_n/Π(5 − R^k)`, `c_n = 5·2^{n−1}+1` (n ≥ 1), `dim DN_n(2) = 0` (n ≥ 3) | CLAIMED | prose argument in README "Corner channels and coincidental hits"; exact checks in `scripts/check_corner_channels.py` (not a test) |
| Exact `h_n = 1 − μ_exc − 5·2^n/(3^{n+1}+3)` (no coincidental hits) for 3 ≤ n ≤ 11 | CLAIMED (finite exact computation) | F_p gcd certificate, `scripts/check_corner_channels.py` |
| Two-adic reduction: coincidental hits only in the symmetric channel with `R^k(λ)=5`, `n−k` even, and residue sum `Σ 1/z_i = 0` in char 2; none in the standard channel; `λ=2` not corner-visible (n ≥ 3) | CLAIMED | prose argument in README "Two-adic reduction of coincidental hits"; exact checks in `scripts/check_coincidental_reduction.py` (not a test) |
| Exact `h_n = 1 − μ_exc − 5·2^n/(3^{n+1}+3)` for 3 ≤ n ≤ 18 | CLAIMED (theorem + finite exact computation) | residue sums nonzero for all chains with k ≤ 16 in GF(2^64) |
| Exact `h_n` formula for all n | NOT CLAIMED | open; the residue conjecture `Σ_{i≤k} 1/z_i ≠ 0` for all k would suffice (not known to be necessary) |
| SPECTRUM.md informal "0.4–0.7" string | NOT CLAIMED | numerical observation of an unspecified quantity |
| Continuum limit, selected W, force, thrust | NOT CLAIMED | forbidden by README scope |

No LICENSE file in the tree. License choice is operator-only.

Parent research index: `coherence-drive`. Geometry dependency: `sierpinski-geometry-045`.
