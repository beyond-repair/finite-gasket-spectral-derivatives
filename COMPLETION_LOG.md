# Completion log — finite-gasket-spectral-derivatives

## Proved this run (2026-10-02, exceptional spectral mass)

Dated 2026-10-02 (America/New_York).

- Theorem: for every integer n ≥ 3, free L = D − A on build_gasket(n) has
  M_exc(n) := mult(3)+mult(5)+mult(6) = (5·3^{n−1} − 7)/2,
  and with N(n) = |V_n| = (3^{n+1}+3)/2 (assumption from gasket_graph.py / SPECTRUM.md N column; verified n = 2..5),
  μ_exc(n) := M_exc(n)/N(n) = (5·3^{n−1}−7)/(3^{n+1}+3),
  which increases to 5/9 as n → ∞; consequently 1 − μ_exc(n) decreases to 4/9.
- Proof structure (recorded in README, section “Exceptional spectral mass”):
  1. Assumptions: free gasket as in Free mult(6); |V_n| formula from the constructor; free mult(3), mult(5), mult(6) theorems already proved.
  2. Algebra: sum the three multiplicity formulas to get M_exc; divide by N(n).
  3. Limit: divide by 3^{n−1} → 5/9; complement → 4/9.
  4. Monotonicity: μ_exc(n+1) − μ_exc(n) has the same sign as 156 · 3^{n−1} > 0.
- Case n = 2 recorded separately: mult(3)=0, mult(5)=2, mult(6)=3 ⇒ M_exc=5, N=15, mass 1/3 (formula for n ≥ 3 only, because of the mult(5) exception).
- Clarification (not a theorem upgrade):
  - This counts total multiplicity of the exceptional values {3,5,6}. It does **not** prove that every remaining eigenvalue is an R-preimage of an eigenvalue of L_{n−1}, nor that any hit-rate algorithm equals 1 − μ_exc.
  - SPECTRUM.md “hit rates … roughly 0.4–0.7” stays a **numerical observation**; consistent with complement → 4/9 ≈ 0.444, not upgraded here.
  - Dirichlet λ_min(n)/λ_min(n−1) → 1/5 remains open / numerical in SPECTRUM.md (not proved this run; Qiu / classical sources not reopened for that claim).
- Supporting numerics (not a substitute for the algebra): eigvalsh on gasket_graph.py for n = 3,4,5 matches M_exc = 19, 64, 199.

## Proved previously (2026-10-02, free mult(3))

Dated 2026-10-02 (America/New_York).

- Theorem: for every integer n ≥ 2, the free combinatorial Laplacian L = D − A on build_gasket(n) has
  mult(3) = (3^{n−1} − 3)/2.
  The claim asked for n ≥ 3. That range is included. At n = 2 both sides are 0, so there is no mult(5)-style exception.
- Proof structure (recorded in README, section “Free mult(3)”):
  1. Assumptions: same free gasket as Free mult(6); edges partition into the finest upward triangles and into three level-1 cells, each isomorphic to the previous gasket; free mult(6) already proved for levels ≥ 2.
  2. Corner response: for every m ≥ 1 and every corner vector c there is w with w|V_0 = c, interior defect L w − 6 w = 0, and corner defect −3 c_q. Base m = 1 is the explicit 6-vertex function (corner 1, adjacent midpoints −1/2, opposite midpoint +1/2). Induction glues the response of one level-(m−1) cell and sets the other two cells to 0.
  3. Pairing with the response: every free 6-eigenfunction vanishes on V_0; every Dirichlet 6-mode has corner neighbor-sum 0, hence extends to a free 6-eigenfunction; the response itself has neighbor-sum −c_q. Therefore an interior 6-eigenfunction whose corner neighbor-sums vanish must have corner values 0, and is a free 6-eigenfunction. Also ker(L_1 − 6 I) = {0}.
  4. Lower bound, n ≥ 3: extend each free 6-eigenfunction of G_{n−1} by the midpoint formula u(y_i) = −(2 φ(x_i)+φ(x_{i+1})+φ(x_{i−1}))/2, which is Qiu's extension at λ = 3. Cell arithmetic gives L_n u = 3 u. The map is injective, so mult_n(3) ≥ mult_{n−1}(6) = (3^{n−1}−3)/2.
  5. Upper bound: a free 3-eigenfunction is determined by its restriction to V_{n−1} (midpoint system invertible). That restriction satisfies the interior equation of eigenvalue 6 and has corner neighbor-sum 0, hence is a free 6-eigenfunction. Restriction is injective.
- Hence mult(3) = (3^{n−1}−3)/2 for all n ≥ 2, and in particular for all n ≥ 3. Upgrades the n = 3..5 numerical line in sierpinski-geometry-045 SPECTRUM.md to a theorem for the free operator of gasket_graph.py.

## Proved previously (2026-10-02, free mult(5))

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
- Dirichlet graph mult(3) = (3^{m−1}−3)/2 is stated by Okoudjou–Strichartz–Tuley, arXiv:1110.1554 (ar5iv HTML opened this run), as the decimation child of Dirichlet mult(6). Same integer as the free theorem; not an input to it. Qiu arXiv:1206.1381 PDF opened this run for the decimation formula (Prop. 2.1, (2.3)–(2.5)): φ_+(6) = 3, φ_−(6) = 2 forbidden. Fukushima–Shima 1992 was not opened.
- Neumann (even reflection) mult(3) is larger than free mult(3) by 3. Ambrose–Bannon–Dunham–Iyer–Roark, Neumann Eigenfunctions on SG (PDF opened): Neumann mult_1(3) = 2, mult_2(3) = 3, and each 6-eigenfunction continues along one branch to eigenvalue 3, so Neumann mult_m(3) = (3^{m−1}+3)/2. The Neumann corner law is not the free corner law.

## Abstract-only (not committed as gasket theorems)

- Two-point spectra supported on {0, 6} that saturate V''(W) = -18 m_6/(1-6W)^2. Those extremals use only Tr L, mult(6), and the box [0, 6]. They are not free gasket spectra.

## Numerical

- Free L = D − A: lambda_max = 6 for n ≥ 2; Tr L = 6*3^n; eigenvalues 3 and 5 present for n = 2..5 (SPECTRUM.md). E(n) = 3^{n+1} (gasket_graph.py).
- Free mult(6) for n = 2..5 matches (3^n − 3)/2 (theorem). Explicit u_x construction checked with residual 0 and full span for n = 2..5 against gasket_graph.py (supporting, not a substitute for injectivity).
- Free mult(5) for n = 3..5 matches (3^{n−1} − 1)/2 (theorem); n = 2 has mult(5) = 2. Corner evaluation rank 0 on free 5-space for n = 3..5; DN residual 0; ⟨(L_D−5I)^+ 1, 1⟩ = −3^{n−1} checked for n = 1..5.
- Free mult(3) for n = 2..5 matches (3^{n−1} − 3)/2 (theorem): 0, 3, 12, 39. Extension residual of the midpoint formula on a 6-eigenbasis is below 10^{−14} for n = 3..5; restriction rank equals mult(6) of the previous level. Supporting only.
- Exceptional mass for n = 3,4,5 matches M_exc = 19, 64, 199 and μ_exc = 19/42, 64/123, 199/366 (theorem algebra; eigvalsh supporting). n = 2 has mass 5/15 = 1/3.

## Still open

- No further exceptional multiplicity columns remain in sierpinski-geometry-045 SPECTRUM.md. Free mult(3), mult(5), mult(6) are theorems, and their total exceptional mass μ_exc → 5/9 is now a theorem for n ≥ 3.
- Decimation hit rates: SPECTRUM.md’s “hit rates … roughly 0.4–0.7” remains a **numerical observation**. The exceptional-mass theorem does not define or prove a hit predicate; 1 − μ_exc → 4/9 is only a complementary mass fraction, not a proved hit rate.
- Dirichlet bottom: λ_min(n)/λ_min(n−1) → 1/5 stays open / numerical in SPECTRUM.md. Not proved this run (would need a real proof from Qiu arXiv:1206.1381 or equivalent, which was not written here).
