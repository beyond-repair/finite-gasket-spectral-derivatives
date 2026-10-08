# Completion log — finite-gasket-spectral-derivatives

## Proved this run (2026-10-08, fourth run: residue condition to k = 32 and all powers of two)

Dated 2026-10-08 (America/New_York).

- Lemma (README "Residue condition: power-of-two lemma and exhaustive check to k = 31"): for every j ≥ 0 and every chain z_0 = 1, z_i² + z_i = z_{i−1} over the algebraic closure of F_2, S_{2^j} = Σ_{i=1}^{2^j} 1/z_i ≠ 0.
- Proof structure: N = x² + x = F + 1 gives N^{2^j} = F^{2^j} + 1, so ker N^{2^j} = GF(2^{2^j}) is a field; z_i lies in it iff i + 1 ≤ 2^j; so S_{2^j − 1} is in the field and 1/z_{2^j} is not.
- Finite exact computation (scripts/check_residue_extension.py driving scripts/residue_chains_gf2_32.c): modulus x^32 + x^7 + x^3 + x^2 + 1 irreducible; all 2^k chains in GF(2^32) have S_k ≠ 0 for 1 ≤ k ≤ 31; the N-level histogram of S_k for k ≤ 10 agrees with the independent GF(2^64) model.
- Corollary: S_k ≠ 0 for all k ≤ 32 and all powers of two, so a coincidental hit needs n ≥ 35, and h_n = 1 − μ_exc(n) − 5·2^n/(3^{n+1}+3) exactly for 3 ≤ n ≤ 34 (previously n ≤ 18).
- Negative results recorded: Galois conjugation by F^{2^{j−1}} gave no contradiction at k = 2^{j−1} + 1; the trace of S_k and the N-level of S_k are not chain-invariant (k ≤ 13, k ≤ 12), so neither proves the conjecture.
- Still open: the residue conjecture for k ≥ 33 that are not powers of two, hence the exact h_n formula for n ≥ 35.
- No literature opened; no novelty claimed. Not a consequence: no W selected, no continuum limit, force, stress, or momentum.

## Proved previously (2026-10-08, third run: two-adic reduction of coincidental hits)

Dated 2026-10-08 (America/New_York).

- Theorem (two-adic reduction; README "Two-adic reduction of coincidental hits"): for every n ≥ 3, a coincidental hit at level n, if any, is seen only by the symmetric channel, has R^k(λ) = 5 with 1 ≤ k ≤ n − 2 and n − k even, and its residue chain z_i = R^{k−i}(λ) mod 𝔭 (𝔭 above 2) satisfies Σ_{i=1}^k 1/z_i = 0 in characteristic 2. The standard channel has no coincidental hits for any n, and λ = 2 is not corner-visible for n ≥ 3.
- Proof structure: (1) mod 2, Qt_n ≡ T^n(x) + 1 and Q_n ≡ x·T^{n−1}(x) with T(x) = x² + x; (2) same-channel exclusion from the reduced numerator (6 − λ)q(R) + 2R p(R); (3) cross-channel and standard-DN cases contradict the mod-2 forms; (4) s_n(2) = (s_{n−2}(−6) − 6)/3 > 0 by a Herglotz bound; (5) symmetric DN chains: v_2(y_i) = −1 for chains ending at 6, v_2(y_i) = 0 for chains ending at 5 with m odd, using s_m(5) = 5(3^{m−2} − 1)/2; for m even the residue of y_k/2 telescopes to z_k·Σ 1/z_i.
- Finite exact computation (scripts/check_coincidental_reduction.py): all 2^k residue chains in GF(2^64) have Σ 1/z_i ≠ 0 for 1 ≤ k ≤ 16, and the mod-2 congruences and channel values were checked exactly for n, m ≤ 8. Corollary: no coincidental hits and h_n = 1 − μ_exc(n) − 5·2^n/(3^{n+1}+3) exactly for 3 ≤ n ≤ 18 (previously n ≤ 11).
- Still open: the residue conjecture Σ_{i=1}^k 1/z_i ≠ 0 for all k and all chains z_0 = 1, z_i² + z_i = z_{i−1} over F̄_2. If true, the exact h_n formula holds for all n ≥ 3. Not proved; no counterexample known.
- No literature opened; no novelty claimed. Not a consequence: no W selected, no continuum limit, force, stress, or momentum.

## Proved previously (2026-10-08, second run: corner channels and coincidental hits)

Dated 2026-10-08 (America/New_York).

- Theorem (corner channels): for n ≥ 1 the corner Schur complement of L_n − λ is t_n I + ((s_n − t_n)/3) J with s_0 = −λ, t_0 = 3 − λ and s_n = [(6 − λ)s_{n−1}(R) + 2R]/Δ (same for t_n). In reduced form s_n = Q_n/(2 − R^{n−1}(λ)) and t_n = Qt_n/Π_{k<n}(5 − R^k(λ)), with integer Q_n, Qt_n of leading coefficient ±1 and degrees 2^{n−1}+1 and 2^n. The symmetric channel sees 2^{n−1}+1 distinct eigenvalues, the standard channel 2^n (corner rank 2 each), so c_n = 5·2^{n−1} + 1 for all n ≥ 1.
- Proof structure (README, "Corner channels and coincidental hits"): S_3 symmetry splits S_n; Schur complements compose through the hit subsection's corner-defect identity; the channel functions are Herglotz-type, so reduced numerator degree counts distinct visible eigenvalues; exact cancellations at λ = 5 (symmetric only, s(0) = 0) and λ = 2 (s_m(6) = t_m(6) = −3), and none elsewhere.
- Corollary: dim DN_n(2) = 0 for n ≥ 3 by an elementary argument (no Qiu §2), and c_2 = 11 is now a theorem rather than a Krylov computation. Closes the second open item of the previous run.
- Reduction: coincidental hits at level n are among the nonzero roots of gcd(Q_n Qt_n, H_{n−1}∘R), with H_{n−1} = Q_{n−1}Qt_{n−1}Π_{j≤n−3}Π_{a∈{2,5,6}}(R^j − a) (its roots contain Spec(L_{n−1}); DN eigenvalues iterate into {2,5,6} because DN_1 = 0).
- Finite exact certificate (scripts/check_corner_channels.py, F_p with p = 2^61 − 1; exact Z recursion to n = 8): for 3 ≤ n ≤ 11 the gcds have degree 1 (= λ) and 0. Hence for 3 ≤ n ≤ 11 there are no coincidental hits and h_n = 1 − μ_exc(n) − 5·2^n/(3^{n+1}+3) exactly. Upgrades the n = 3..6 floating-point observation.
- Still open: no coincidental hits for all n (general proof). Mod 23 gave minimal gcd degrees in both channels for n = 3..9, but no induction mod a fixed prime was found.
- No literature opened this run; the Schur-complement form of spectral decimation is standard and no novelty is claimed. Not a consequence: no W selected, no continuum limit, force, stress, or momentum.

## Proved previously (2026-10-08, free decimation hit predicate)

Dated 2026-10-08 (America/New_York).

- Definition: for λ ∈ Spec(L_n) \ {3,5,6}, λ is a hit iff R(λ) = λ(5−λ) ∈ Spec(L_{n−1}); h_n = hit mass / N(n). Defined here; SPECTRUM.md's "0.4–0.7" string is not identified with it.
- Theorem: for every n ≥ 3, 1 − μ_exc(n) − 5·2^n/(3^{n+1}+3) ≤ h_n ≤ 1 − μ_exc(n); hence h_n → 4/9. Non-decimating mass is O((2/3)^n).
- Proof structure (README, section "Free decimation hit predicate"):
  1. Midpoint extension for λ ∉ {2,5}; restriction to V_{n−1} injective.
  2. Decimation identity re-derived, with the free-corner defect: ((L_n−λ)u)(c) = ((6−λ)/Δ)((L_{n−1}−R)v)(c) + (2λ/(2−λ)) v(c), Δ = (2−λ)(5−λ). Interior rows have no defect.
  3. DN_n(λ) ≅ DN_{n−1}(R(λ)) for λ ∉ {2,5,6} (DN = eigenfunctions vanishing on V_0).
  4. Counting with free mult(5), mult(6) theorems and N(n): c_n = 2c_{n−1} − 1 − dim DN_n(2) for n ≥ 3, where c_n = N(n) − Σ dim DN_n(λ) is the corner-visible dimension.
  5. Exact base c_2 = 11 (rational Krylov rank, finite exact computation); so c_n ≤ 5·2^{n−1}+1.
  6. Every DN mode off {3,5,6} is a hit (n ≥ 3); λ = 0 is a corner-visible hit; so non-hits ≤ c_n − 1.
- Corollary resting on classical Qiu §2 Dirichlet structure (as used in the bottom-ratio theorem; not reopened this run): 2 ∉ Spec(L_D) for m ≥ 2, so DN_n(2) = 0 and c_n = 5·2^{n−1}+1 exactly for n ≥ 2.
- Numerical (scripts/check_decimation_hits.py, n = 1..6): c_n = 6, 11, 21, 41, 81, 161; non-hits 5, 9, 20, 40, 80, 160; h_n ≈ 0.167, 0.067, 0.071, 0.154, 0.238, 0.302; identity residual ≤ 2.2e−15. (hits+exceptional)/N = 0.40, 0.52, 0.67 for n = 2..4 is compatible with the old "0.4–0.7" string; that is a guess, not an identification.
- Still open: whether a corner-visible eigenvalue can be a coincidental hit. If never, non-hits = 5·2^{n−1} exactly (observed n = 3..6 only).
- Not a consequence: no W selected, no continuum limit, force, stress, or momentum; no novelty claim.

## Proved previously (2026-10-02, Dirichlet bottom ratio)

Dated 2026-10-02 (America/New_York).

- Theorem: for every integer n ≥ 1, Dirichlet L_D^{(n)} on I_n = V_n \ V_0 of build_gasket(n) has
  λ_min(n) = φ_−^{(n−1)}(2) with φ_−(x) = (5 − √(25 − 4x))/2;
  for n ≥ 2, λ_min(n)/λ_min(n−1) = 2/(5 + √(25 − 4 λ_min(n−1))) → 1/5 as n → ∞.
- Proof structure (recorded in README, section “Dirichlet bottom ratio”):
  1. Assumptions: free gasket as before; L_D = Dirichlet principal submatrix; classical Dirichlet spectral decimation from Qiu arXiv:1206.1381 §2 / Prop. 2.1 and (2.3)–(2.6) (ar5iv HTML opened this run): f(x)=x(5−x), φ_±, forbidden {2,5,6}, D_1={2,5,5}, initial 5 and 6 for m≥2, continued via φ_±. Fukushima–Shima 1992 not opened.
  2. Branch comparison: φ_+([0,6])=[3,5]; φ_− increasing with image [0,2]; hence λ_min(n)=φ_−(λ_min(n−1)) by induction from λ_min(1)=2.
  3. Rationalization: φ_−(x)/x = 2/(5+√(25−4x)) → 1/5 as x→0; λ_min(n)→0.
- Upgrades SPECTRUM.md Dirichlet ratio table / “→ 1/5” line from numerical observation to a theorem for L_D of gasket_graph.py.
- Clarification: free λ_min is 0; this is Dirichlet only. Free hit-rate string “0.4–0.7” stays numerical.

## Proved previously (2026-10-02, exceptional spectral mass)

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
- Dirichlet bottom / 2-series: Qiu arXiv:1206.1381 §2 (ar5iv opened this run) records D_1 = {2,5}, initial 5 and 6 for m≥2, and φ_−(x)=x/5+O(x²) as x→0. The identification λ_min(n)=φ_−^{(n−1)}(2) and the ratio limit 1/5 proved this run use that classical structure plus elementary branch comparison; they are not a new discovery of spectral decimation.

## Abstract-only (not committed as gasket theorems)

- Two-point spectra supported on {0, 6} that saturate V''(W) = -18 m_6/(1-6W)^2. Those extremals use only Tr L, mult(6), and the box [0, 6]. They are not free gasket spectra.

## Numerical

- Free L = D − A: lambda_max = 6 for n ≥ 2; Tr L = 6*3^n; eigenvalues 3 and 5 present for n = 2..5 (SPECTRUM.md). E(n) = 3^{n+1} (gasket_graph.py).
- Free mult(6) for n = 2..5 matches (3^n − 3)/2 (theorem). Explicit u_x construction checked with residual 0 and full span for n = 2..5 against gasket_graph.py (supporting, not a substitute for injectivity).
- Free mult(5) for n = 3..5 matches (3^{n−1} − 1)/2 (theorem); n = 2 has mult(5) = 2. Corner evaluation rank 0 on free 5-space for n = 3..5; DN residual 0; ⟨(L_D−5I)^+ 1, 1⟩ = −3^{n−1} checked for n = 1..5.
- Free mult(3) for n = 2..5 matches (3^{n−1} − 3)/2 (theorem): 0, 3, 12, 39. Extension residual of the midpoint formula on a 6-eigenbasis is below 10^{−14} for n = 3..5; restriction rank equals mult(6) of the previous level. Supporting only.
- Exceptional mass for n = 3,4,5 matches M_exc = 19, 64, 199 and μ_exc = 19/42, 64/123, 199/366 (theorem algebra; eigvalsh supporting). n = 2 has mass 5/15 = 1/3.
- Dirichlet λ_min(n) for n = 1..5 matches φ_−^{(n−1)}(2) and the ratio identity 2/(5+√(25−4 λ_min(n−1))) on gasket_graph.py eigvalsh (supporting).

## Still open

- No further exceptional multiplicity columns remain in sierpinski-geometry-045 SPECTRUM.md. Free mult(3), mult(5), mult(6) are theorems, and their total exceptional mass μ_exc → 5/9 is a theorem for n ≥ 3.
- Dirichlet bottom ratio λ_min(n)/λ_min(n−1) → 1/5 is a theorem for L_D (2026-10-02).
- Decimation hit rates: with the hit predicate defined in README ("Free decimation hit predicate"), h_n → 4/9 is now a theorem (2026-10-08), with 1 − μ_exc − 5·2^n/(3^{n+1}+3) ≤ h_n ≤ 1 − μ_exc for n ≥ 3. SPECTRUM.md's informal "0.4–0.7" string remains a numerical observation of an unspecified quantity.
- Coincidental hits among corner-visible eigenvalues: excluded for 3 ≤ n ≤ 11 by an exact finite certificate (2026-10-08, corner channels), and for 3 ≤ n ≤ 18 by the two-adic reduction plus a residue check for k ≤ 16 (2026-10-08, third run); for general n this is reduced to the residue conjecture Σ 1/z_i ≠ 0 in characteristic 2, which is open. Fourth run: the residue condition holds for all k ≤ 32 and every power of two k, so exact h_n now holds for 3 ≤ n ≤ 34; open for k ≥ 33 not a power of two.
- Elementary proof of DN_n(2) = 0 (n ≥ 3) without Qiu §2: done (2026-10-08, from c_n = 5·2^{n−1}+1 via corner channels).
