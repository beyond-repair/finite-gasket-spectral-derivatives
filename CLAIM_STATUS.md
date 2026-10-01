# Claim status — finite-gasket-spectral-derivatives

**Classification:** RESEARCH
**Claim cap:** ≤ 1 (finite discrete kernel identities)
**Sweep:** 167 / PASS-2026-10-01-167
**Head audited:** 393c59aa4f521187ba3d5b7f809dfdf4ce494f77

| Capability | State | Evidence |
|---|---|---|
| `gamma_loop`, `dgamma_dw`, `v_second` on a supplied eigenvalue list | IMPLEMENTED + locally TESTED | `scripts/spectral_derivatives.py`; `tests/test_spectral_derivatives.py` |
| Positive-definiteness guard `omega^2 - W lambda > 0` | IMPLEMENTED + locally TESTED | same |
| Power-series remainder / hypergeometric identities | CLAIMED (prose derivation in README) | not executed as a test in this repository |
| Free `mult(6) = (3^n - 3)/2` on `build_gasket(n)` | CLAIMED | prose argument in README / COMPLETION_LOG.md; graph constructor lives in `sierpinski-geometry-045`, not in this tree |
| Continuum limit, selected W, force, thrust | NOT CLAIMED | forbidden by README scope |

CI workflow added this pass. Actions conclusion is not yet observed; do not treat the workflow file as verification.

Parent research index: `coherence-drive`. Geometry dependency: `sierpinski-geometry-045`.
