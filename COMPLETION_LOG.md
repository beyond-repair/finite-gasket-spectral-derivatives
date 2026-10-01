# Completion log — finite-gasket-spectral-derivatives

Dated 2026-10-01 (America/New_York).

## Proved this run

- Exact split of locked Gamma_loop and V'' into the lambda = 6 eigenspace of multiplicity m_6 and complementary eigenvalues mu_j in [0, 6).
- Identities: Gamma_loop = (m_6/2) ln(1-6W) + (1/2) sum_j ln(1-W mu_j); V''(W) = -18 m_6/(1-6W)^2 - (1/2) sum_j mu_j^2/(1-W mu_j)^2 for W < 1/6.
- Bound: on W in [0, 1/6), V''(W) <= -18 m_6/(1-6W)^2 < 0, with equality in <= iff every mu_j = 0.
- On free gasket levels n >= 2 recorded in sierpinski-geometry-045 SPECTRUM.md (eigenvalues in (0, 6)), the inequality is strict.
- With Tr L = 6*3^n from E(n) = 3^{n+1} and the SPECTRUM.md multiplicity formula m_6 = (3^n-3)/2 (n = 2..5), Tr L - 6 m_6 = 3^{n+1}+9 > 0.

## Classical

- Dirichlet multiplicity of the initial eigenvalue 6 on -Delta_m (Gamma_m, corners grounded): (3^m-3)/2 for m >= 2; Qiu arXiv:1206.1381 §2, after Fukushima–Shima / Shima. Not a free-graph statement.

## Abstract-only (not committed as gasket theorems)

- Two-point spectra supported on {0, 6} that saturate V''(W) = -18 m_6/(1-6W)^2. Those extremals use only Tr L, mult(6), and the box [0, 6]. They are not free gasket spectra.

## Numerical

- Free L = D - A: lambda_max = 6 for n >= 2; Tr L = 6*3^n; mult(6) = (3^n-3)/2 and eigenvalues 3, 5 present for n = 2..5 (SPECTRUM.md). E(n) = 3^{n+1} (gasket_graph.py).

## Still open

- Next open item: rigorous proof that free L = D - A on build_gasket(n) has mult(6) = (3^n-3)/2 for all n >= 2 (presently numerical for n = 2..5 in SPECTRUM.md; Dirichlet analogue is classical).
