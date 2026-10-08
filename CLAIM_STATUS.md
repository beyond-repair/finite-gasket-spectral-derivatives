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
| Residue sums `S_k ≠ 0` for every chain when k = 2^j (all j) | CLAIMED | prose argument in README "Residue condition: power-of-two lemma and exhaustive check to k = 31" |
| Residue sums `S_k ≠ 0` for every chain, 1 ≤ k ≤ 31; exact `h_n` formula for 3 ≤ n ≤ 34 | CLAIMED (theorem + finite exact computation) | `scripts/check_residue_extension.py` + `scripts/residue_chains_gf2_32.c` (exhaustive in GF(2^32); not a test) |
| Residue sums `S_k ≠ 0` for every chain when k = 2^j + 1 (all j ≥ 1); exact `h_n` formula for 3 ≤ n ≤ 35 | CLAIMED (theorem + finite exact computation) | prose argument in README "Residue condition: lengths 2^j + 1 and the limits of the subfield test"; supporting `scripts/check_residue_p_plus_one.py` (not a test) |
| Frobenius orbit reduction of the residue test (one child at power-of-two depths gives one chain per orbit); residue sums `S_k ≠ 0` for every chain, 1 ≤ k ≤ 45; exact `h_n` formula for 3 ≤ n ≤ 47 | CLAIMED (theorem + finite exact computation) | prose lemma in README "Residue condition: Frobenius orbit reduction and exact check to k = 45"; `scripts/check_residue_orbits.py` + `scripts/residue_orbits_gf2_64.c` (reduced tree in GF(2^64); not a test) |
| Logarithmic-derivative form `S_k = Π_k′(z_k)/Π_k(z_k)`; residue condition at length k ⇔ `gcd(N^k + 1, Π_k′) = 1` in F_2[t]; certificate for 1 ≤ k ≤ 21 | CLAIMED (theorem + finite exact computation) | prose lemma in README "Residue condition: logarithmic-derivative form and a polynomial gcd certificate"; `scripts/check_residue_logderiv.py` (not a test). Does not extend the k ≤ 45 range |
| Residue sums `S_k ≠ 0` for every chain, 1 ≤ k ≤ 46; exact `h_n` formula for 3 ≤ n ≤ 48 | CLAIMED (theorem + finite exact computation) | unchanged `scripts/residue_orbits_gf2_64.c` run with KMAX = 46 (2^40 reduced chains in GF(2^64)); README "Residue condition: exact check to k = 46 and no monomial trace certificate" (not a test) |
| Uniform monomial trace certificate `Tr_d(z_k^a z_{k−1}^b S_k) = 1` | NOT CLAIMED (negative search) | none valid for all 2 ≤ k ≤ 8 with \|a\| ≤ 6, \|b\| ≤ 4 (either sibling); `scripts/check_residue_trace_monomials.py` |
| Residue sums `S_k ≠ 0` (indeed `S_k ∉ GF(2^{2^j})`) for every chain when k = 2^j + 2, j ≥ 3; with k = 4, 6, every k = 2^j + 2 | CLAIMED | prose lemma in README "Residue condition: lengths 2^j + 2 (relative-trace argument)"; supporting `scripts/check_residue_p_plus_two.py` (k = 6, 10, 18; not a test). Does not change the exact `h_n` range (3 ≤ n ≤ 48) |
| Residue sums `S_k ≠ 0` for every chain when k − 2^⌊log2 k⌋ ∈ {3, 4, 5, 6}, for excess 7 except possibly k = 263, excess 8 except k = 520, excess 9 except k = 265 (elimination certificate: iterated relative norm R ∈ GF(2^e)[x] ≠ 0 and finitely many surviving p) | CLAIMED (theorem + finite exact computation) | prose lemma in README "Residue condition: lengths 2^j + m for 3 ≤ m ≤ 7 (elimination over a fixed field)"; `scripts/check_residue_p_plus_m.py` (filter m ≤ 10, direct counts incl. k = 71–73, 136, 137, 264; not a test). Does not change the exact `h_n` range (3 ≤ n ≤ 48) |
| Exact `h_n` formula for all n | NOT CLAIMED | open; the residue conjecture `Σ_{i≤k} 1/z_i ≠ 0` for all k ≥ 47 with k − 2^⌊log2 k⌋ ≥ 10 (and pending 263, 265, 520) would suffice (not known to be necessary); equivalently `gcd(N^k + 1, Π_k′) = 1` for those k |
| SPECTRUM.md informal "0.4–0.7" string | NOT CLAIMED | numerical observation of an unspecified quantity |
| Continuum limit, selected W, force, thrust | NOT CLAIMED | forbidden by README scope |

No LICENSE file in the tree. License choice is operator-only.

Parent research index: `coherence-drive`. Geometry dependency: `sierpinski-geometry-045`.
