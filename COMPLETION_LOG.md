# Completion log — finite-gasket-spectral-derivatives

## Proved this run (2026-10-02, free mult(5))

Dated 2026-10-02 (America/New_York).

- Theorem: for every integer n ≥ 3, the free combinatorial Laplacian L = D − A on build_gasket(n) has
  mult(5) = (3^{n−1} − 1)/2.
- Proof structure (recorded in README, section “Free mult(5)”):
  1. Assumptions: same free gasket graph as Free mult(6); n ≥ 3; L_D = Dirichlet principal submatrix on I_n = V_n \ V_0.
  2. Classical: Dir mult(5) = (3^{n−1}+3)/2 (Qiu arXiv:1206.1381 §2; Fukushima–Shima). Neumann map ρ on Dir_5 has rank 2 (loop / battery split; Ambrose–Bannon–Iyer–Roark Neumann REU 2025 and Morris–Patel–Regan–Wick Dirichlet REU 2025, both opened). Hence DN_5 := ker(ρ) has dim (3^{n−1}−1)/2.
  3. DN ⊆ free: extend DN modes by 0 on V_0; free corner identity matches ρ = 0.
  4. Free ∩ {u|_{V_0}=0} = DN_5.
  5. Corner obstruction: nonzero free corner values must be equal (solvability ⇒ c ∈ span{(1,1,1)}); the equal-corner inhomogeneous problem (L_D−5I)u = L_D 1 forces Σ = 6−(5/2)(3^{n−1}+3), which equals the free target Σ = −9 iff n = 2. For n ≥ 3 one gets c = 0.
  6. Resolvent input: ⟨(L_D−5I)^+ 1, 1⟩ = −3^{n−1} (elementary for n = 1 via L_D = 5I−J; recurrence G_n = 3 G_{n−1} from self-similarity, giving ⟨u,1⟩ = −mult_D(5)).
- Exception: n = 2 has free mult(5) = 2 = DN_dim + 1 (SPECTRUM.md); formula stated only for n ≥ 3.
- Hence mult(5) = (3^{n−1}−1)/2 for all n ≥ 3. Upgrades the n = 3..5 numerical line in sierpinski-geometry-045 SPECTRUM.md to a theorem for the free operator of gasket_graph.py.

## Proved previously (2026-10-01, free mult(6))

- Theorem: for every integer n ≥ 2, the free combinatorial Laplacian L = D − A on build_gasket(n) (gasket_graph.py) has
  mult(6) = (3^n − 3)/2 = |V_{n−1} \ V_0|.
- Proof structure (recorded in README, section “Free mult(6)”):
  1. Assumptions: vertex set V_n of the level-n upward-triangle gasket; edges only the finest upward edges; corners deg 2, all other vertices deg 4; L = D − A.
  2. Construction: for each x ∈ V_{n−1} \ V_0, a localized mode u_x supported on the two (n−1)-cells containing x, with u_x(x) = 2, value −1 on the four midpoints adjacent to x, and value +1 on the two opposite midpoints of those cells (0 elsewhere). Local verification gives L u_x = 6 u_x.
  3. Independence: the |V_{n−1} \ V_0| modes are linearly independent because u_x(y) = 2 δ_{xy} on V_{n−1} \ V_0.
  4. Upper bound: the restriction map ker(L − 6I) → ℝ^{V_{n−1}\V_0} is injective. If L v = 6v and v vanishes on V_{n−1} \ V_0, the eigenvalue equations on each (n−1)-cell force v = 0 at the three corners and at all finest midpoints (explicit 3×3 midpoint system, and a separate corner-cell calculation).
- Hence mult(6) = (3^n − 3)/2 for all n ≥ 2. This upgrades the n = 2..5 numerical line in sierpinski-geometry-045 SPECTRUM.md to a theorem for the free operator of gasket_graph.py.

## Proved previously (7f66ef4)

- Exact split of locked Gamma_loop and V'' into the lambda = 6 eigenspace of multiplicity m_6 and complementary eigenvalues mu_j in [0, 6).
- Identities: Gamma_loop = (m_6/2) ln(1-6W) + (1/2) sum_j ln(1-W mu_j); V''(W) = -18 m_6/(1-6W)^2 - (1/2) sum_j mu_j^2/(1-W mu_j)^2 for W < 1/6.
- Bound: on W in [0, 1/6), V''(W) ≤ -18 m_6/(1-6W)^2 < 0, with equality in ≤ iff every mu_j = 0.
- On free gasket levels n ≥ 2 recorded in sierpinski-geometry-045 SPECTRUM.md (eigenvalues in (0, 6)), the inequality is strict.
- With Tr L = 6*3^n from E(n) = 3^{n+1} and the multiplicity formula m_6 = (3^n-3)/2 (now a theorem for all n ≥ 2), Tr L - 6 m_6 = 3^{n+1}+9 > 0.

## Classical

- Dirichlet multiplicity of the initial eigenvalue 6 on -Delta_m (Gamma_m, corners grounded): (3^m-3)/2 for m ≥ 2; Qiu arXiv:1206.1381 §2, after Fukushima–Shima / Shima. Same numerical formula as the free mult(6) theorem, but a different operator (principal submatrix on V_m \ V_0).
- The same localized basis (modes indexed by V_{m−1} \ V_0) appears in Qiu §2 for Dirichlet and in Okoudjou–Strichartz–Tuley arXiv:1110.1554 for the Dirichlet graph Laplacian multiplicities. Those sources were opened for the mult(6) run; they do not by themselves prove the free D−A statement.
- Literature Neumann (even reflection at corners, treating boundary vertices as degree 4) is a third operator. UConn REU “Neumann Boundary Conditions on SG” / “Neumann Eigenfunctions on SG” (Ambrose–Bannon–Iyer–Roark, 2025; opened) counts Neumann mult(6) = |V_{m−1}| = (3^m + 3)/2, larger than free mult(6) by 3, and Neumann mult(5) = (3^{m−1} − 1)/2 (loop modes around holes of Γ_{m−1}). Free L = D − A is not the reflected Neumann Laplacian in general; for λ = 5 and n ≥ 3 the free 5-space coincides with the DN / Neumann loop space (proved this run via corner obstruction).
- Dirichlet mult(5) = (3^{m−1}+3)/2 (Qiu §2; Morris–Patel–Regan–Wick Dirichlet REU 2025, opened this run: loops plus two battery chains). Localized DN mult(5) = (3^{m−1}−1)/2 (Qiu §2).

## Abstract-only (not committed as gasket theorems)

- Two-point spectra supported on {0, 6} that saturate V''(W) = -18 m_6/(1-6W)^2. Those extremals use only Tr L, mult(6), and the box [0, 6]. They are not free gasket spectra.

## Numerical

- Free L = D − A: lambda_max = 6 for n ≥ 2; Tr L = 6*3^n; eigenvalues 3 and 5 present for n = 2..5 (SPECTRUM.md). E(n) = 3^{n+1} (gasket_graph.py).
- Free mult(6) for n = 2..5 matches (3^n − 3)/2 (theorem). Explicit u_x construction checked with residual 0 and full span for n = 2..5 against gasket_graph.py (supporting, not a substitute for injectivity).
- Free mult(5) for n = 3..5 matches (3^{n−1} − 1)/2 (theorem); n = 2 has mult(5) = 2. Corner evaluation rank 0 on free 5-space for n = 3..5; DN residual 0; ⟨(L_D−5I)^+ 1, 1⟩ = −3^{n−1} checked for n = 1..5.

## Still open

- Next open item: rigorous proof that free L = D − A on build_gasket(n) has mult(3) = (3^{n−1} − 3)/2 for all n ≥ 3 (SPECTRUM.md numerical: n = 3,4,5 give 3,12,39; n = 2 has mult(3) = 0). Eigenvalue 3 is the spectral-decimation child of 6 (φ-branch), not an initial forbidden value; the free mult(5)/mult(6) arguments do not apply unchanged.
