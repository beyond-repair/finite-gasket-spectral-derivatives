<div align="center">

```
╔══════════════════════════════════════════════════════════════╗
║   ATOMIC DREAM LABS  ·  BEYOND-REPAIR                        ║
╚══════════════════════════════════════════════════════════════╝
```

# Finite Gasket Spectral Derivatives

### W-derivatives of (1/2) Tr ln K on the finite gasket. No continuum. No thrust.

[![Lifecycle](https://img.shields.io/badge/●_RESEARCH-a855f7?style=for-the-badge&labelColor=0f0f23)](https://github.com/beyond-repair/ADL-Governance)
[![Claim](https://img.shields.io/badge/Claim_≤1-22c55e?style=for-the-badge&labelColor=0f0f23)](https://github.com/beyond-repair/ADL-Governance/blob/main/docs/CLAIM_VALIDATION.md)
[![Governance](https://img.shields.io/badge/ADL--Governance-7c3aed?style=for-the-badge&labelColor=0f0f23)](https://github.com/beyond-repair/ADL-Governance)

```
LIFECYCLE   RESEARCH
CLAIM       ≤ 1   finite discrete kernel
NOT CLAIMED continuum · selected W · force
```

</div>

---
## ▌ STATUS

Classification follows [ADL-Governance](https://github.com/beyond-repair/ADL-Governance). A README facelift does not raise claim level. Physics and pharmacology stay at the evidenced cap. CI green is not experimental validation.

---

## ▌ RUN IT

Needs Python 3.10+ and NumPy. From a fresh clone:

```bash
git clone https://github.com/beyond-repair/finite-gasket-spectral-derivatives
cd finite-gasket-spectral-derivatives
python3 -m venv .venv && . .venv/bin/activate
pip install -e ".[test]"

gasket-spectral kernel --level 3 --w 0.1          # Gamma_loop, dGamma/dW, V'' at a prescribed W
gasket-spectral kernel --level 3 --w 0.1 --json
gasket-spectral kernel --eigenvalues 0,2,6,6 --w 0.1
gasket-spectral decimation --nmax 6               # supporting numerics for the hit-predicate section
python -m pytest                                  # 16 tests
```

`kernel` builds the free Laplacian L = D − A on `build_gasket(level)` (levels 0–7, default 3; the same constructor as `scripts/check_decimation_hits.py`) or takes `--eigenvalues`, then evaluates the three formulas below at the W you pass. `--w` is required and never defaulted, because this repository does not select W. `--omega2` defaults to 1. If K = ω²I − W L is not positive definite (W at or past the spectral wall ω²/λ_max, which is 1/6 for ω² = 1 and level ≥ 2), it prints the wall and exits 2. Bad input also exits 2.

Without installing, the same commands run from the repository root as `python3 -m scripts kernel ...` and `python3 -m scripts decimation`, and the tests as `python3 -m unittest discover -s tests` (NumPy still required). CI runs `python -m unittest tests/test_spectral_derivatives.py`.

The CLI and its tests are numerical checks of the kernel and the constructor. They are not proofs of the theorems below and do not raise the claim cap.

---

## ▌ PRESERVED BODY

# Finite gasket spectral derivatives

Locked scope. This repository does not select W, does not take a continuum limit, and does not predict a force.

Parent: the discrete kernel K = omega^2 I - W L. On the finite gasket at omega = 1, lambda_max = 6, so K is positive definite if and only if W < 1/6.

Eigenvalues of K are kappa_k = 1 - W lambda_k.

    det K = product_k (1 - W lambda_k)

    Gamma_loop = (1/2) sum_k ln(1 - W lambda_k)

    d Gamma_loop / dW = (1/2) sum_k (-lambda_k) / (1 - W lambda_k)

    V''(W) = - (1/2) sum_k lambda_k^2 / (1 - W lambda_k)^2

V'' is negative wherever K is positive definite and some lambda_k is nonzero. That is concavity of the one-loop piece. It is not a vacuum and not a thrust.

## Power series

For |W| lambda_max < 1, that is |W| < 1/6,

    Gamma_loop = - (1/2) sum_{n=1}^{infty} (W^n / n) Tr(L^n).

The radius is exactly 1/lambda_max = 1/6. The series diverges at the spectral wall W = 1/lambda_max. It does not select a value of W. The half-line W < 1/6 is the positive-definiteness interval, which is larger than the disk of convergence; the truncation identity is in the next section.

S_W is not in this repository. Stationarity is not defined here.

scripts/spectral_derivatives.py evaluates the eigenvalue sums from a list of eigenvalues. It does not build W(x) and it does not emit a force.

## Truncation remainder

### Assumptions

- omega = 1 and K = I - W L, with W a prescribed scalar.
- The spectrum {lambda_k} is real and lies in [0, lambda_max] with lambda_max = 6 attained, so K is positive definite if and only if W < 1/6.
- Tr(L^n) = sum_k lambda_k^n (algebraic multiplicities). The gasket is finite, so there are finitely many eigenvalues.
- Gamma_loop(W) = (1/2) sum_k ln(1 - W lambda_k) for W < 1/6.

S_W is not an input to this identity. No value of W is selected.

### Derivation

Fix an integer N >= 0 and a real number x < 1. Define

    r_N(x) = ln(1 - x) + sum_{n=1}^{N} (x^n / n) + int_0^x t^N / (1 - t) dt.

The empty sum (N = 0) is 0. Then r_N(0) = 0. On (-infty, 1) the integrand is continuous along the segment from 0 to x, and

    r_N'(x) = -1/(1 - x) + sum_{n=0}^{N-1} x^n + x^N / (1 - x)
            = -1/(1 - x) + (1 - x^N)/(1 - x) + x^N / (1 - x)
            = 0.

Hence r_N(x) = 0 for every x < 1.

If W < 1/6, then each x_k = W lambda_k satisfies x_k < 1. Summing (1/2) r_N(x_k) = 0 is the identity in the theorem.

For the inequality, take 0 <= x < 1 and t in [0, x]. Then t^N >= 0 and

    1 <= 1/(1 - t) <= 1/(1 - x).

Integrate over [0, x]:

    x^{N+1} / (N + 1) <= int_0^x t^N / (1 - t) dt <= x^{N+1} / ((N + 1) (1 - x)).

If 0 <= W < 1/6, then 0 <= W lambda_k <= 6W < 1, so 1/(1 - W lambda_k) <= 1/(1 - 6W). Summing the resulting bounds against (1/2) and using Tr(L^{N+1}) = sum_k lambda_k^{N+1} gives the inequality below.

Radius. For lambda_k >= 0 not all zero, (sum_k lambda_k^n)^{1/n} tends to lambda_max, and n^{1/n} tends to 1, so

    limsup_{n -> infty} |Tr(L^n) / n|^{1/n} = lambda_max = 6.

The radius of sum_{n>=1} (W^n / n) Tr(L^n) is therefore exactly 1/6. For |W| > 1/6 the terms do not tend to 0. At W = 1/6 the terms are asymptotic to mult(lambda_max) / n with mult(lambda_max) >= 1, so the series diverges. At W = -1/6 the same leading piece is the alternating harmonic series, and every lambda_k < 6 contributes a series dominated by |lambda_k / 6|^n, so the series converges at that single boundary point.

### Theorem

Identity. For every integer N >= 0 and every real W < 1/6,

    Gamma_loop(W) + (1/2) sum_{n=1}^{N} (W^n / n) Tr(L^n)
        = - (1/2) sum_k int_0^{W lambda_k} t^N / (1 - t) dt.

Inequality. For every integer N >= 0 and every W in [0, 1/6),

    - W^{N+1} Tr(L^{N+1}) / (2 (N + 1) (1 - 6W))
        <= Gamma_loop(W) + (1/2) sum_{n=1}^{N} (W^n / n) Tr(L^n)
        <= - W^{N+1} Tr(L^{N+1}) / (2 (N + 1)).

The right-hand side of the identity is the exact remainder of the truncated power-trace series. The infinite series equals Gamma_loop throughout the open disk |W| < 1/6, and also at W = -1/6. It diverges for every |W| > 1/6 and at the spectral wall W = 1/6. Neither the remainder nor the radius selects W.

### Not a consequence

This section does not identify L with D - A, does not evaluate Tr(L) by a degree sum, and does not state a continuum limit, a force, or a selected W.

## Hypergeometric form of the remainder

### Assumptions

The assumptions of the truncation section stand: omega = 1, K = I - W L, W a prescribed scalar, spectrum real in [0, 6] with lambda_max = 6 attained, finitely many eigenvalues, and Gamma_loop(W) = (1/2) sum_k ln(1 - W lambda_k) for W < 1/6.

N is an integer, N >= 0. Write x_k = W lambda_k. The Gauss series and the Lerch series are

    2F1(1, N+1; N+2; z) = sum_{m=0}^{infty} (N+1)/(N+1+m) z^m,

    Phi(z, 1, N+1) = sum_{m=0}^{infty} z^m / (m + N + 1),

absolutely convergent for |z| < 1. Off the cut [1, infty) they mean the analytic continuation of those series. S_W is not an input. No value of W is selected.

The strict concavity of Gamma_loop on (-infty, 1/6), and the sign of d Gamma_loop/dW, are already recorded above from V''(W) and the first derivative. They are not restated as a theorem here.

### Derivation

Scalar series identity, classical. Let N >= 0 be an integer and let |x| < 1. On the segment from 0 to x the geometric series 1/(1-t) = sum_{m>=0} t^m converges uniformly, so

    int_0^x t^N / (1-t) dt = sum_{m=0}^{infty} int_0^x t^{N+m} dt
        = sum_{m=0}^{infty} x^{N+m+1} / (N+m+1).

The Pochhammer ratio (1)_m / m! = 1 and

    (N+1)_m / (N+2)_m = (N+1)/(N+m+1),

because (N+1)_m = (N+1)(N+2)...(N+m) and (N+2)_m = (N+2)...(N+m+1). Therefore

    2F1(1, N+1; N+2; x) = sum_{m=0}^{infty} (N+1)/(N+1+m) x^m,

and

    x^{N+1}/(N+1) * 2F1(1, N+1; N+2; x)
        = sum_{m=0}^{infty} x^{N+m+1}/(N+m+1).

The same series is x^{N+1} Phi(x, 1, N+1). Hence, for |x| < 1,

    int_0^x t^N/(1-t) dt
        = x^{N+1}/(N+1) * 2F1(1, N+1; N+2; x)
        = x^{N+1} Phi(x, 1, N+1).

The sign is positive: both sides equal -ln(1-x) when N = 0. A minus in front of the hypergeometric term would contradict the geometric series.

Endpoint x = -1. The series sum_{m>=0} (-1)^m (N+1)/(N+1+m) converges by the alternating series test. Abel's theorem gives continuity from inside the disk along the radius, and the integral is continuous on (-infty, 1), so the identity holds at x = -1.

Continuation. For z in the complex plane cut along [1, infty), the straight segment from 0 to z does not meet the cut, and

    I_N(z) = int_0^z t^N/(1-t) dt

is holomorphic there (integer N, so no branch from the power). It agrees with the hypergeometric expression on |z| < 1. By the identity theorem,

    I_N(z) = z^{N+1}/(N+1) * 2F1(1, N+1; N+2; z)
           = z^{N+1} Phi(z, 1, N+1)

on the cut plane, with 2F1 and Phi the continuations. Restricting to real x < 1 gives the integral identity on the whole positive-definiteness half-line of each eigenvalue, not only on the disk. On that half-line the continuation is also the elementary tail already proved in the truncation section,

    I_N(x) = -ln(1-x) - sum_{n=1}^{N} x^n/n
           (x < 1),

so the name 2F1 does not add a second independent formula outside the disk of the series.

Spectral step. If |W| < 1/6, then |x_k| <= 6|W| < 1 for every k, and the series form applies termwise. If W = -1/6, then x_k is in [-1, 0], the lambda_max terms sit at the convergent endpoint x = -1, and every smaller eigenvalue is inside the open disk. If W < 1/6 in general, each x_k is real and strictly less than 1, so the continued form applies; the raw power series of 2F1 at x_k need not converge when W < -1/6. Substitute the truncation identity.

### Theorem

Scalar identity, classical, applied to this spectrum. For every integer N >= 0 and every real x < 1,

    int_0^x t^N/(1-t) dt
        = x^{N+1}/(N+1) * 2F1(1, N+1; N+2; x)
        = x^{N+1} Phi(x, 1, N+1),

where the special functions are their series when |x| < 1 and at x = -1, and their analytic continuations off [1, infty) in general.

Spectral identity. For every integer N >= 0 and every real W < 1/6, with x_k = W lambda_k,

    Gamma_loop(W) + (1/2) sum_{n=1}^{N} (W^n / n) Tr(L^n)
        = - (1/2) sum_k x_k^{N+1}/(N+1) * 2F1(1, N+1; N+2; x_k)
        = - (1/2) sum_k x_k^{N+1} Phi(x_k, 1, N+1).

On |W| < 1/6 and at W = -1/6 the series may be substituted for 2F1 and Phi. For W < -1/6 the same formula uses the continuation, which equals the integral remainder already recorded. The radius of the trace series remains 1/6. Neither formula selects W.

### Numerical observation

Scalar check only, not a spectral evaluation and not a fit. For N = 0 and x = 1/2,

    int_0^{1/2} dt/(1-t) = -ln(1/2) = ln 2,

and 2F1(1, 1; 2; 1/2) = sum_{m>=0} (1/2)^m / (m+1) = -ln(1/2) / (1/2) = 2 ln 2, so (1/2) * 2F1(1, 1; 2; 1/2) = ln 2. The two sides agree exactly.

### Not a consequence

This section does not identify L with D - A, does not select W, and does not state a continuum limit, a force, a stress, or a momentum. The scalar hypergeometric identity is classical; what is recorded here is its application to the finite-gasket remainder. No claim is made that the scalar identity was previously unknown.


## Lambda = 6 eigenspace split

### Assumptions

- omega = 1 and K = I - W L, with W a prescribed scalar.
- The spectrum {lambda_k} is real and lies in [0, 6] with lambda_max = 6 attained, so K is positive definite if and only if W < 1/6.
- The gasket is finite: finitely many eigenvalues, counted with algebraic multiplicity.
- Write m_6 = mult(6) >= 1 for the multiplicity of the eigenvalue 6, and write {mu_j} for the complementary eigenvalues (those not equal to 6). Then each mu_j lies in [0, 6).
- Gamma_loop(W) = (1/2) sum_k ln(1 - W lambda_k) and
  V''(W) = - (1/2) sum_k lambda_k^2 / (1 - W lambda_k)^2
  for W < 1/6, as recorded above.

S_W is not an input. No value of W is selected.

### Derivation

Split the locked sums into the m_6 copies of lambda = 6 and the complementary terms. For each copy of 6,

    ln(1 - W * 6) = ln(1 - 6W),
    (1/2) * 6^2 / (1 - 6W)^2 = 18 / (1 - 6W)^2.

Hence

    Gamma_loop(W) = (m_6 / 2) ln(1 - 6W) + (1/2) sum_j ln(1 - W mu_j),

    V''(W) = - 18 m_6 / (1 - 6W)^2 - (1/2) sum_j mu_j^2 / (1 - W mu_j)^2.

On W in [0, 1/6), each factor 1 - 6W is in (0, 1] and each 1 - W mu_j is in (0, 1]. Every complementary summand mu_j^2 / (1 - W mu_j)^2 is nonnegative, and vanishes if and only if mu_j = 0. Therefore

    V''(W) <= - 18 m_6 / (1 - 6W)^2 < 0,

with equality in the first comparison if and only if every mu_j = 0.

The free finite gasket L = D - A of sierpinski-geometry-045 has E(n) = 3^{n+1} from gasket_graph.py, so Tr L = 2E = 6 * 3^n for every n. SPECTRUM.md records, for n = 2..5, that lambda_max = 6, that mult(6) equals (3^n - 3)/2, and that eigenvalues 3 and 5 occur. Inserting the free multiplicity theorem mult(6) = (3^n - 3)/2 (proved below for all n >= 2) gives

    Tr L - 6 m_6 = 6 * 3^n - 3(3^n - 3) = 3^{n+1} + 9 > 0,

so the complementary eigenvalues cannot all vanish on those free graphs. The presence of eigenvalues in (0, 6) already forces the complementary sum in V'' to be strictly positive, hence a strict inequality V''(W) < - 18 m_6 / (1 - 6W)^2 on those levels.

Dirichlet multiplicity of the initial eigenvalue 6 on the discrete Laplacian -Delta_m of Gamma_m with corners grounded (V_m without V_0), equal to (3^m - 3)/2 for m >= 2, is classical: Qiu, arXiv:1206.1381, Section 2, attributing Fukushima–Shima / Shima. That is a different operator from the free whole-graph L = D - A. The free multiplicity is proved combinatorially in the next subsection from the build_gasket graph; it is not identified with Qiu's Dirichlet theorem.

### Theorem

Identities. Under the assumptions above, for every real W < 1/6,

    Gamma_loop(W) = (m_6 / 2) ln(1 - 6W) + (1/2) sum_j ln(1 - W mu_j),

    V''(W) = - 18 m_6 / (1 - 6W)^2 - (1/2) sum_j mu_j^2 / (1 - W mu_j)^2.

Bound. For every W in [0, 1/6),

    V''(W) <= - 18 m_6 / (1 - 6W)^2 < 0,

with equality in <= if and only if every complementary eigenvalue mu_j equals 0.

On the free gasket graphs of SPECTRUM.md with n >= 2, eigenvalues lie in (0, 6), so the inequality is strict. Neither the split nor the bound selects W.

### Negative result (abstract, not a gasket theorem)

The upper bound -18 m_6 / (1 - 6W)^2 is saturated precisely when the spectrum is supported on {0, 6}. That two-point support, together with the numerical constraints Tr L and mult(6) and the box [0, 6], defines an abstract extremal problem on finite spectra. It is not the spectrum of free L = D - A on build_gasket(n): those graphs carry eigenvalues in (0, 6). Do not commit two-point {0, 6} extremals as gasket theorems. The bound above remains valid as an inequality for every spectrum in the assumed box; saturation is off the gasket.

### Free mult(6) on build_gasket(n)

#### Assumptions

- G_n is the graph returned by build_gasket(n) in sierpinski-geometry-045/gasket_graph.py: vertex set V_n of the level-n Sierpinski pre-gasket, edges exactly the sides of the upward triangles of level n (finest edges only).
- |V_n| = (3^{n+1} + 3)/2, |V_{n-1} \ V_0| = (3^n - 3)/2, and E(n) = 3^{n+1}, so Tr L = 2E = 6 * 3^n.
- The three corners V_0 have degree 2; every other vertex has degree 4.
- L = D - A is the free combinatorial Laplacian on all of V_n (no grounding, no even reflection at corners).
- Integer n >= 2.

S_W is not an input. No value of W is selected.

#### Derivation

Lower bound (construction). Index the (n-1)-cells of G_n by the standard self-similar subdivision (three upward subcopies at each step). For each x in V_{n-1} \ V_0 there are exactly two (n-1)-cells containing x. Define u_x : V_n -> R by

- u_x(x) = 2;
- on each of those two cells, with corners (x, p, q) and finest midpoints m_{xp}, m_{xq}, m_{pq}: set u_x(m_{xp}) = u_x(m_{xq}) = -1 and u_x(m_{pq}) = +1;
- u_x = 0 at every other vertex.

Support of u_x is the union of the two (n-1)-cells. Direct checking of (L u_x)(v) = 6 u_x(v) at v = x (four neighbors, each -1), at each midpoint adjacent to x (neighbors include x with value 2 and the opposite midpoints), at each opposite midpoint (neighbors the two side midpoints), and at all vertices outside the support (identically zero), yields L u_x = 6 u_x. The family {u_x} is linearly independent because u_x(y) = 2 delta_{xy} for y in V_{n-1} \ V_0. Hence

    mult(6) >= |V_{n-1} \ V_0| = (3^n - 3)/2.

Upper bound (injective restriction). Let v satisfy L v = 6 v. The restriction map

    ker(L - 6 I) -> R^{V_{n-1} \ V_0},    v |-> v|_{V_{n-1} \ V_0}

is injective. Indeed, if v vanishes on V_{n-1} \ V_0, the eigenvalue equation at every finest midpoint reads: sum of the four neighbors equals -2 v(m). On an (n-1)-cell whose three corners all lie in V_{n-1} \ V_0 (hence have v = 0), writing (x, y, z) for the three midpoint values gives the system

    y + z = -2x,    z + x = -2y,    x + y = -2z,

which forces x = y = z = 0. On each of the three corner (n-1)-cells, one corner q is in V_0 and the other two corners are in V_{n-1} \ V_0. The corner equation at q is v(a) + v(b) = -4 v(q) for the two incident midpoints a, b; substituting into the three midpoint equations on that cell yields v(q) = 0 and vanishing of all three midpoints. Therefore v = 0 on V_0 and on V_n \ V_{n-1}, so v = 0. Combined with the lower bound,

    mult(6) = (3^n - 3)/2.

#### Theorem

For every integer n >= 2, the free combinatorial Laplacian L = D - A on build_gasket(n) satisfies

    mult(6) = (3^n - 3)/2.

Equivalently, dim ker(L - 6 I) equals the number of non-boundary vertices of V_{n-1}. The identity uses only the combinatorial graph of gasket_graph.py. It does not select W.

#### Classical comparison (opened sources)

- Qiu, arXiv:1206.1381, Section 2: Dirichlet -Delta_m on V_m \ V_0 has initial eigenvalue 6 of multiplicity (3^m - 3)/2, with localized modes indexed by V_{m-1} \ V_0 (after Fukushima–Shima / Shima). Same count and same index set as the free theorem; different operator (corners grounded).
- Okoudjou–Strichartz–Tuley, arXiv:1110.1554: records Dirichlet graph-Laplacian mult(6) = (3^m - 3)/2 in the spectral-decimation accounting used for Green-function traces.
- Ambrose–Bannon–Dunham–Iyer–Roark, UConn REU talk “Neumann Eigenfunctions on SG” (2025): Neumann (even reflection) mult(6) = |V_{m-1}| = (3^m + 3)/2. That count is larger than free mult(6) by 3; free L = D - A is not the reflected Neumann Laplacian.

The free theorem is not a citation of those Dirichlet or Neumann statements; it is a self-contained combinatorial argument for D - A on build_gasket(n).

#### Numerical observation

For n = 2..5 the formula matches SPECTRUM.md, and an explicit matrix check of the u_x family against eigvalsh(L) gives residual 0 and full span. That check is supporting evidence for the construction, not a substitute for the injectivity argument above.

#### Not a consequence

This subsection does not identify free L with Qiu's Dirichlet operator or with reflected Neumann, does not select W, and does not state a continuum limit, a force, a stress, or a momentum. The split of Gamma_loop and V'' remains elementary from the locked definitions once lambda = 6 is factored out. Free mult(5) is proved in the next subsection.

### Free mult(5) on build_gasket(n)

#### Assumptions

- G_n is the graph returned by build_gasket(n) in sierpinski-geometry-045/gasket_graph.py, as in the Free mult(6) subsection: finest upward edges only, corners deg 2, all other vertices deg 4, L = D − A free on all of V_n.
- Integer n ≥ 3.
- Write I_n = V_n \ V_0 for the non-corner vertices and L_D for the Dirichlet principal submatrix of L on I_n (corners grounded).
- For each corner q ∈ V_0 write n_1(q), n_2(q) for its two neighbors in G_n.

S_W is not an input. No value of W is selected.

#### Classical ingredients (opened sources)

- Dirichlet mult(5) = (3^{n−1} + 3)/2 for n ≥ 2 on L_D: Qiu, arXiv:1206.1381, §2 (after Fukushima–Shima / Shima). Same formula appears in the UConn REU writeup “Counting Dirichlet Eigenfunctions” (Morris–Patel–Regan–Wick, 2025; opened this run), which splits the Dirichlet 5-space into loop modes and two battery-chain modes.
- Localized / simultaneous Dirichlet–Neumann 5-modes, indexed by holes of Γ_{n−1}, have multiplicity ρ_n(5) = (3^{n−1} − 1)/2: Qiu §2; equivalently Ambrose–Bannon–Iyer–Roark, UConn REU “Neumann Boundary Conditions on SG” (2025; opened this run), which records Neumann mult(5) = (3^{n−1} − 1)/2 with one loop mode per hole of Γ_{n−1}.
- Number of holes in Γ_{n−1} is H_{n−1} = (3^{n−1} − 1)/2 (recurrence H_m = 3 H_{m−1} + 1, H_0 = 0).

These classical counts are for Dirichlet or Neumann operators. The free theorem below uses them only through the DN subspace of L_D and a free-specific corner obstruction.

#### Derivation

Write Dir_5 = ker(L_D − 5 I) and define the Neumann evaluation map

    ρ : Dir_5 → R^{V_0},    u ↦ ( u(n_1(q)) + u(n_2(q)) )_{q ∈ V_0}.

The classical battery / loop splitting gives rank(ρ) = 2 and

    DN_5 := ker(ρ)    has    dim DN_5 = (3^{n−1} + 3)/2 − 2 = (3^{n−1} − 1)/2.

(The same dimension is the localized count ρ_n(5) in Qiu and the Neumann mult(5) in Ambrose et al.)

DN ⊆ free. If u ∈ DN_5, extend u by 0 on V_0. On I_n one has L u = L_D u = 5 u. At a corner q, the free equation gives
(L u)(q) = − u(n_1(q)) − u(n_2(q)) = 0 = 5 u(q). So L u = 5 u on all of V_n, i.e. DN_5 ⊆ ker(L − 5 I).

Free modes that vanish on V_0 lie in DN_5. If L u = 5 u and u|_{V_0} = 0, then u|_{I_n} ∈ Dir_5, and the free corner identity
u(n_1(q)) + u(n_2(q)) = −3 u(q) = 0
puts u in ker(ρ). Hence

    ker(L − 5 I) ∩ {u : u|_{V_0} = 0} = DN_5.

Corner obstruction for n ≥ 3. It remains to show that every free 5-eigenfunction vanishes on V_0 when n ≥ 3. Let L u = 5 u and write c = u|_{V_0}, u_I = u|_{I_n}. Interior rows of L u = 5 u rearrange as

    (L_D − 5 I) u_I = A c,

where (A c)(v) = ∑_{q ∼ v, q ∈ V_0} c_q (only the six near-corner vertices are affected). Free corner rows give
u_I(n_1(q)) + u_I(n_2(q)) = −3 c_q for each q.

Solvability of (L_D − 5 I) u_I = A c against Dir_5 requires ⟨v, A c⟩ = 0 for every v ∈ Dir_5, i.e. c · ρ(v) = 0 for all v. Since im(ρ) = (1,1,1)^⊥ (rank 2, with ker(ρ^*) = span{(1,1,1)}), this forces c ∈ span{(1,1,1)}.

Thus either c = 0 (done) or, after scaling, c = (1,1,1). In that case A c = L_D 1_{I_n}, because (L_D 1)(v) equals the number of corner neighbors of v. So one solves

    (L_D − 5 I) u_I = L_D 1.

Every Dir_5 mode is orthogonal to 1: for v ∈ Dir_5 one has 5 ⟨v, 1⟩ = ⟨v, L_D 1⟩ = ∑_q (v(n_1)+v(n_2)) = ⟨ρ(v), (1,1,1)⟩ = 0, since ρ(v) ∈ (1,1,1)^⊥. Hence 1 ⊥ Dir_5, the reduced resolvent (L_D − 5 I)^+ is well-defined on 1, and every solution is
u_I = 1 + 5 (L_D − 5 I)^+ 1 + v with v ∈ Dir_5. The scalar ⟨u_I, 1⟩ is therefore independent of v.

Summing the equation (L_D − 5 I) u_I = L_D 1 against 1 yields
Σ − 5 ⟨u_I, 1⟩ = 6,
where Σ := ∑_{q ∈ V_0} (u_I(n_1(q)) + u_I(n_2(q))) is likewise independent of v (battery directions lie in (1,1,1)^⊥ and do not change Σ). The free corner target with c = (1,1,1) is Σ = −9.

Resolvent identity. Let G_n(5) := ⟨(L_D^{(n)} − 5 I)^+ 1, 1⟩. On I_1 (three midpoints) one has L_D = 5 I − J, so (L_D − 5 I)^+ 1 = −(1/3) 1 and G_1(5) = −1 = −3^{0}. Because 1 ⊥ Dir_5 for every n, the Stieltjes transform z ↦ ⟨(L_D − z I)^{-1} 1, 1⟩ is holomorphic at z = 5 on the orthogonal complement of Dir_5 and agrees with G_n near that point. Self-similarity of the Dirichlet gasket (three level-(n−1) cells glued at V_1 \ V_0) gives the recurrence G_n(5) = 3 G_{n−1}(5) for the D_3-symmetric quadratic form at this regular value of the reduced resolvent. Hence G_n(5) = −3^{n−1} for all n ≥ 1.

Combined with u_I = 1 + 5 (L_D − 5 I)^+ 1 + v (v ∈ Dir_5) and |I_n| + mult_D(5) = 5 · 3^{n−1},
⟨u_I, 1⟩ = |I_n| + 5 G_n(5) = |I_n| − 5 · 3^{n−1} = − mult_D(5) = −(3^{n−1} + 3)/2.
Therefore Σ = 6 + 5 ⟨u_I, 1⟩ = 6 − (5/2)(3^{n−1} + 3). This equals −9 if and only if (3^{n−1} + 3)/2 = 3, i.e. iff n = 2. For n ≥ 3 one has Σ ≠ −9, so c = (1,1,1) is impossible. Hence c = 0, and ker(L − 5 I) = DN_5.

#### Theorem

For every integer n ≥ 3, the free combinatorial Laplacian L = D − A on build_gasket(n) satisfies

    mult(5) = (3^{n−1} − 1)/2.

Equivalently, dim ker(L − 5 I) equals the number of holes in Γ_{n−1}. The identity uses the combinatorial graph of gasket_graph.py together with the classical DN dimension; it does not select W.

#### Exception n = 2

For n = 2 the same obstruction permits Σ = −9. SPECTRUM.md records free mult(5) = 2 = DN_dim + 1: one loop mode (the unique hole of Γ_1) and one D_3-symmetric mode with equal nonzero corner values. The formula (3^{n−1} − 1)/2 is therefore stated only for n ≥ 3.

#### Numerical observation

For n = 3,4,5 the formula matches SPECTRUM.md (mult(5) = 4,13,40). Explicit checks: DN_5 ⊆ free with residual 0; corner evaluation on ker(L − 5 I) has rank 0; three-edge ±1 loop modes on the finest holes of Γ_{n−1} span a subspace of the free 5-space. These checks support the identification, not a substitute for the obstruction argument.

#### Not a consequence

This subsection does not identify free L with the full Neumann Laplacian (for λ = 6 the free and Neumann multiplicities differ by 3), does not select W, and does not state a continuum limit, a force, a stress, or a momentum.

### Free mult(3) on build_gasket(n)

#### Assumptions

- G_n is the graph returned by build_gasket(n) in sierpinski-geometry-045/gasket_graph.py, as in the Free mult(6) subsection: finest upward edges only, corners degree 2, every other vertex degree 4, L = D − A free on all of V_n.
- The edge set of G_n is the disjoint union of the 3^n finest upward triangles, and equally the edge-disjoint union of the three level-1 cells. Each level-1 cell, with its induced edges, is combinatorially isomorphic to G_{n−1}.
- V_{n−1} ⊂ V_n is the vertex set of build_gasket(n−1). Each edge of G_{n−1} contributes exactly one midpoint in V_n \ V_{n−1}.
- Already proved, for every integer m ≥ 2: dim ker(L_m − 6 I) = (3^m − 3)/2.
- The count below is stated for every integer n ≥ 2. The range n ≥ 3 is the one in which the right-hand side is positive. At n = 2 both sides are zero.

S_W is not an input. No value of W is selected.

#### Classical ingredients (opened sources)

- Spectral decimation for the Dirichlet and Neumann graph Laplacians: λ_m = λ_{m+1}(5 − λ_{m+1}), extension formula (2.5), forbidden values {2, 5, 6}. Qiu, arXiv:1206.1381, Proposition 2.1 and (2.3)–(2.5) (PDF opened), after Fukushima–Shima. The only preimage of 6 that is not itself forbidden is φ_+(6) = 3; φ_−(6) = 2 is forbidden. Fukushima–Shima, Potential Analysis 1992, was not opened (Springer paywall); the formulas quoted as background are Qiu's.
- Okoudjou–Strichartz–Tuley, arXiv:1110.1554 (ar5iv HTML opened): in the Dirichlet graph-Laplacian accounting (Δ_m on V_m \ V_0) used for the Green trace, multiplicity of 6 is (3^m − 3)/2, of 5 is (3^{m−1} + 3)/2, and of 3 is (3^{m−1} − 3)/2. The 3-line is the decimation child of Dirichlet mult(6). Same integer as the free theorem; different boundary condition. It is not an input below.
- Ambrose–Bannon–Dunham–Iyer–Roark, UConn REU “Neumann Eigenfunctions on SG” (PDF opened): the Neumann law is (4 − λ) u(q) = 2 u(n_1) + 2 u(n_2), not the free law (2 − λ) u(q) = u(n_1) + u(n_2). They record the Neumann spectrum of Δ_1 as {0, 3, 6} with multiplicities (1, 2, 3), and mult(3) = 3 on Δ_2. Each Neumann 6-eigenfunction continues along one branch, to eigenvalue 3, so Neumann mult_m(3) = (3^{m−1} + 3)/2, larger than the free count by 3.

#### Derivation

Corner response at eigenvalue 6. For every integer m ≥ 1 and every c ∈ ℝ^{V_0} there exists w : V_m → ℝ with w|_{V_0} = c,
(L w − 6 w)(x) = 0 for x ∉ V_0, and (L w − 6 w)(q) = −3 c_q for q ∈ V_0.

Base m = 1. Corners q_0, q_1, q_2; opposite midpoints x = m_{q_1 q_2}, y = m_{q_0 q_2}, z = m_{q_0 q_1}. For c = (1, 0, 0) set w(q_0) = 1, w(q_1) = w(q_2) = 0, w(y) = w(z) = −1/2, w(x) = 1/2. Each midpoint has degree 4. The three midpoint defects L w − 6 w vanish because (a, b, c) = (−1/2, −1/2, 1/2) solves
2a + b + c = −1, a + 2b + c = −1, a + b + 2c = 0.
At q_0 the neighbors are y and z, so (L w)(q_0) = 2 − (−1) = 3 and (L − 6) w(q_0) = −3. At q_1 and q_2 the neighbor sums are zero, so the defects vanish. The other corners follow by symmetry of the level-1 graph.

Inductive step. G_m is the edge-disjoint union of three copies H_0, H_1, H_2 of G_{m−1}, with q_i the outer corner of H_i and with H_i meeting H_j at one glue vertex g_{ij} ∈ V_1 \ V_0. At a glue vertex the incident edges split between the two copies and the degrees add, so L_{G_m} = L_{H_i} + L_{H_j} there. Elsewhere the copy Laplacian agrees with L_{G_m}. Apply the inductive hypothesis inside H_0 to the corner values (c_0, 0, 0) on (q_0, g_{01}, g_{02}), and extend that function by 0 off H_0. Defects vanish on copy interiors and at both glue corners of H_0; the two copies therefore contribute defect 0 at each glue vertex; the defect at q_0 is −3 c_0; H_1 and H_2 are identically zero, so the defects at q_1 and q_2 vanish. Superposition gives a general c.

Consequences of the response ψ_q associated with c = e_q. L is symmetric.

1. Every free 6-eigenfunction vanishes on V_0. If L φ = 6 φ, then ⟨ψ_q, (L − 6) φ⟩ = ⟨(L − 6) ψ_q, φ⟩ = −3 φ(q), so φ(q) = 0. In particular ker(L_1 − 6 I) = {0}: corners vanish, and on the three midpoints the Dirichlet matrix is L_D = 5 I − J, so (−I − J) v = 0. Then v = −J v, hence J v = −3 J v, so J v = 0 and v = 0.
2. A Dirichlet 6-mode has zero corner flux. If (L_D − 6 I) v = 0 on I_m = V_m \ V_0 and u is v extended by 0, then (L − 6) u is supported on V_0 with value −(u(n_1)+u(n_2)) at q. Pairing with ψ_q gives u(n_1)+u(n_2) = 0, so (L u)(q) = 0 and u is a free 6-eigenfunction.
3. The response itself has neighbor sum −c_q. Indeed (L w)(q) = 6 c_q − 3 c_q = 3 c_q and also (L w)(q) = 2 c_q − (n_1+n_2).
4. Corner obstruction. Suppose (L v)(x) = 6 v(x) for every x ∉ V_0, and write c = v|_{V_0}. Let w be the response with the same corner values. Then v − w vanishes on V_0 and satisfies the interior equation, so its neighbor sums vanish by (2). Neighbor sums of v equal those of w, hence equal −c. If in addition n_1(q)+n_2(q) = 0 at every corner, then c = 0 and v is a free 6-eigenfunction.

Extension, lower bound, n ≥ 3. Let φ ∈ ker(L_{n−1} − 6 I). By (1), φ vanishes on V_0, so its two coarse neighbors at each corner sum to 0. Define u on V_n by u|_{V_{n−1}} = φ and, on each upward (n−1)-cell with corners x_0, x_1, x_2,
u(y_i) = −(2 φ(x_i) + φ(x_{i+1}) + φ(x_{i−1}))/2,
where y_i is the midpoint of the opposite side. This is Qiu's extension (2.5) at λ = 3, where the denominator (2−3)(5−3) equals −2. Each new vertex has its four neighbors inside its cell, and substitution shows that those four neighbors sum to u(y_i), so (L_n u)(y_i) = 3 u(y_i).

At an old non-corner x, two (n−1)-cells contain x. In a cell (x, a, b) the two new neighbors of x sum to −φ(x) − (3/2)(φ(a)+φ(b)). The four coarse neighbors sum to S = −2 φ(x), because L_{n−1} φ = 6 φ and the degree is 4. The four new neighbors therefore sum to −2 φ(x) − (3/2) S = φ(x), which is the degree-4 equation for eigenvalue 3. At a corner the same one-cell sum collapses to 0 because φ(q) = 0 and the coarse neighbor sum is 0, matching −u(q). Thus L_n u = 3 u. The map φ ↦ u is injective, so
mult_n(3) ≥ mult_{n−1}(6) = (3^{n−1} − 3)/2.

Restriction, upper bound. Let L_n u = 3 u. The midpoint equations on each (n−1)-cell are the same invertible 3×3 system (determinant 4), so u is the extension of φ = u|_{V_{n−1}} and the restriction map is injective. Reversing the cell arithmetic: at each non-corner of V_{n−1} the degree-4 equation for λ = 3 is equivalent to (L_{n−1} φ)(x) = 6 φ(x); at each corner the degree-2 equation is equivalent to the coarse neighbor sum being 0 (the corner value cancels). Consequence (4) at level n−1 ≥ 2 gives L_{n−1} φ = 6 φ. Therefore
mult_n(3) ≤ mult_{n−1}(6).

Level n = 2. The same restriction lands in ker(L_1 − 6 I) = {0}, so mult_2(3) = 0 = (3^1 − 3)/2.

#### Theorem

For every integer n ≥ 2, the free combinatorial Laplacian L = D − A on build_gasket(n) satisfies

    mult(3) = (3^{n−1} − 3)/2.

In particular the identity holds for every integer n ≥ 3. Equivalently, dim ker(L_n − 3 I) = dim ker(L_{n−1} − 6 I), by the φ_+ branch on this free operator: extension of free 6-eigenfunctions, and injective restriction onto that eigenspace. The n = 2 case is the zero identity, not an exception of the mult(5) type. The identity does not select W.

#### Numerical observation

For n = 3, 4, 5 the formula matches SPECTRUM.md (mult(3) = 3, 12, 39), and n = 2 has mult(3) = 0. Extension of an eigenbasis of ker(L_{n−1} − 6 I) by the midpoint formula has max residual below 10^{−14} for n = 3, 4, 5; restriction of ker(L_n − 3 I) lands in that 6-space with full rank. These checks support the identification. They are not a proof.

#### Not a consequence

This subsection does not identify free L with the reflected Neumann Laplacian, nor with the Dirichlet Laplacian, even though the Dirichlet multiplicity of 3 recorded by Okoudjou–Strichartz–Tuley is the same integer. It does not select W, and it does not state a continuum limit, a force, a stress, or a momentum.

### Exceptional spectral mass on build_gasket(n)

#### Assumptions

- G_n and L = D − A are as in the Free mult(6) subsection: finest upward edges only, corners degree 2, every other vertex degree 4, free Laplacian on all of V_n.
- Vertex count |V_n| = N(n) = (3^{n+1} + 3)/2, taken from gasket_graph.py / SPECTRUM.md (N column). Verified against build_gasket(n) for n = 2..5 (N = 15, 42, 123, 366). Not re-proved here as an independent counting theorem; used as an assumption from the constructor.
- Free multiplicity theorems already recorded in this README:
  - mult(6) = (3^n − 3)/2 for every integer n ≥ 2,
  - mult(5) = (3^{n−1} − 1)/2 for every integer n ≥ 3,
  - mult(3) = (3^{n−1} − 3)/2 for every integer n ≥ 2.
- Write M_exc(n) := mult(3) + mult(5) + mult(6) for the total multiplicity of the exceptional values {3, 5, 6} identified in SPECTRUM.md / classical SG literature, and μ_exc(n) := M_exc(n) / N(n).

S_W is not an input. No value of W is selected.

#### Derivation

For every integer n ≥ 3, add the three free multiplicity formulas:

    M_exc(n) = (3^{n−1} − 3)/2 + (3^{n−1} − 1)/2 + (3^n − 3)/2
             = (2 · 3^{n−1} + 3^n − 7)/2
             = (5 · 3^{n−1} − 7)/2.

Divide by N(n) = (3^{n+1} + 3)/2:

    μ_exc(n) = (5 · 3^{n−1} − 7) / (3^{n+1} + 3).

Limit. Divide numerator and denominator by 3^{n−1}:

    μ_exc(n) = (5 − 7 · 3^{1−n}) / (9 + 3^{2−n}) → 5/9 as n → ∞.

Hence 1 − μ_exc(n) → 4/9.

Monotone increase. Write a = 3^{n−1} ≥ 3. Then

    μ_exc(n+1) − μ_exc(n) has the same sign as
    (15a − 7)(9a + 3) − (5a − 7)(27a + 3) = 156 a > 0,

so μ_exc(n+1) > μ_exc(n) for every n ≥ 3. The sequence increases to 5/9.

#### Theorem (exceptional spectral mass)

For every integer n ≥ 3, the free combinatorial Laplacian L = D − A on build_gasket(n) satisfies

    M_exc(n) := mult(3) + mult(5) + mult(6) = (5 · 3^{n−1} − 7)/2,

and with N(n) = |V_n| = (3^{n+1} + 3)/2 (assumption from gasket_graph.py),

    μ_exc(n) := M_exc(n)/N(n) = (5 · 3^{n−1} − 7)/(3^{n+1} + 3),

which increases to 5/9 as n → ∞. Consequently the complementary fraction 1 − μ_exc(n) decreases to 4/9.

#### Case n = 2 (separate)

At n = 2 the free multiplicities are mult(3) = 0, mult(5) = 2 (outside the n ≥ 3 formula), mult(6) = 3, so M_exc(2) = 5, N(2) = 15, and μ_exc(2) = 5/15 = 1/3. This is smaller than μ_exc(3) = 19/42, consistent with the increase for n ≥ 3, but the closed formula (5 · 3^{n−1} − 7)/2 is stated only for n ≥ 3 because mult(5) is.

#### What this theorem does and does not say

- It counts the total multiplicity of the already-identified exceptional values {3, 5, 6}. The proof is only addition of the three free multiplicity theorems plus the |V_n| formula.
- It does **not** by itself prove that every remaining eigenvalue is a preimage under R(z) = z(5 − z) of an eigenvalue of L_{n−1}, nor that any particular hit-rate algorithm equals 1 − μ_exc(n).
- The SPECTRUM.md phrase “hit rates … roughly 0.4–0.7” remains a **numerical observation** about whatever closed-form check that file used. It is consistent with an exceptional mass approaching 5/9 (complement → 4/9 ≈ 0.444) but is not upgraded to a theorem here.
- Dirichlet λ_min(n)/λ_min(n−1) → 1/5 is proved in the next subsection (Dirichlet bottom ratio), not here.

#### Numerical observation

For n = 3, 4, 5, eigvalsh of L from gasket_graph.py matches M_exc = 19, 64, 199 and μ_exc = 19/42, 64/123, 199/366 against the closed formulas. For n = 2, M_exc = 5 and μ_exc = 1/3 as above. No hit-rate predicate is recorded as a theorem; a naive check “R(λ) lies in the spectrum of L_{n−1}” on non-exceptional eigenvalues is unstable relative to the SPECTRUM.md 0.4–0.7 band and is not claimed.

#### Not a consequence

This subsection does not select W, does not state a continuum limit, a force, a stress, or a momentum, and does not identify 1 − μ_exc with a proved decimation hit rate.


### Dirichlet bottom ratio on L_D of build_gasket(n)

#### Assumptions

- Same free gasket graph build_gasket(n) as Free mult(6). Write I_n = V_n \ V_0 and L_D^{(n)} for the Dirichlet principal submatrix of free L = D − A on I_n (corners grounded). This is the same discrete Dirichlet operator as Qiu's −Δ_n on Γ_n \ V_0.
- Classical spectral decimation for that Dirichlet graph Laplacian (Qiu, arXiv:1206.1381, §2 / Proposition 2.1 and (2.3)–(2.6); ar5iv HTML opened this run), after Fukushima–Shima:
  - f(x) = x(5 − x), inverse branches φ_±(x) = (5 ± √(25 − 4x))/2;
  - forbidden values {2, 5, 6};
  - D_1 = {2 (mult 1), 5 (mult 2)};
  - for m ≥ 2 the only initial Dirichlet eigenvalues are 5 and 6; every other Dirichlet eigenvalue at level m is a continued φ_±-preimage of a Dirichlet eigenvalue at level m − 1 (with the usual rule that 6 continues only to 3, since φ_−(6) = 2 is forbidden).
- Fukushima–Shima, Potential Analysis 1992, was not opened (Springer paywall); formulas used below are those stated in Qiu.

S_W is not an input. No value of W is selected. This subsection is about L_D, not about free L (whose bottom eigenvalue is 0).

#### Derivation

Branch geometry on [0, 6]. The map φ_+ is decreasing and φ_+([0, 6]) = [3, 5]. The map φ_− is increasing and φ_−([0, 6]) = [0, 2], with φ_−(x) < 2 for every x ∈ [0, 6).

Claim. For every integer n ≥ 1,
    λ_min(n) := λ_min(L_D^{(n)}) = φ_−^{(n−1)}(2).
In particular λ_min(n) = φ_−(λ_min(n−1)) for n ≥ 2.

Proof by induction. At n = 1, L_D^{(1)} = 5I − J on the three midpoints (same matrix as in Free mult(5)), so Spec = {2, 5, 5} and λ_min(1) = 2 = φ_−^{(0)}(2).

Assume λ_min(n−1) = φ_−^{(n−2)}(2). Every Dirichlet eigenvalue at level n is either initial (5 or 6, for n ≥ 2) or of the form φ_+(μ) or φ_−(μ) for some Dirichlet eigenvalue μ at level n − 1 (with 6 contributing only φ_+(6) = 3). Then:

- every initial value is ≥ 5;
- every φ_+-image lies in [3, 5];
- every φ_−-image satisfies φ_−(μ) ≥ φ_−(λ_min(n−1)), because φ_− is increasing and μ ≥ λ_min(n−1).

Hence the global minimum at level n is exactly φ_−(λ_min(n−1)) = φ_−^{(n−1)}(2).

Ratio identity. For x ∈ (0, 6],
    φ_−(x)/x = (5 − √(25 − 4x))/(2x) = 2 / (5 + √(25 − 4x)),
by rationalizing the numerator. Therefore
    λ_min(n)/λ_min(n−1) = 2 / (5 + √(25 − 4 λ_min(n−1)))
for every n ≥ 2.

Limit. The recurrence λ_min(n) = φ_−(λ_min(n−1)) with λ_min(1) = 2 forces λ_min(n) → 0 (since φ_−(x) ≤ x/2 on a neighborhood of 0, or simply φ_−(x)/x → 1/5 < 1). Sending λ_min(n−1) → 0 in the ratio identity gives
    λ_min(n)/λ_min(n−1) → 2/(5+5) = 1/5.

#### Theorem (Dirichlet bottom ratio)

For every integer n ≥ 1, the Dirichlet combinatorial Laplacian L_D^{(n)} on I_n = V_n \ V_0 of build_gasket(n) satisfies
    λ_min(n) = φ_−^{(n−1)}(2),
where φ_−(x) = (5 − √(25 − 4x))/2. For every n ≥ 2,
    λ_min(n)/λ_min(n−1) = 2 / (5 + √(25 − 4 λ_min(n−1))),
and therefore
    λ_min(n)/λ_min(n−1) → 1/5 as n → ∞.

This upgrades the Dirichlet ratio table and the “→ 1/5” line in sierpinski-geometry-045 SPECTRUM.md from a numerical observation to a theorem for L_D of gasket_graph.py, using classical spectral decimation structure from Qiu (opened) plus the elementary branch comparison and rationalization above.

#### What this theorem does and does not say

- It is a statement about Dirichlet L_D, not about free L (free λ_min = 0 for all n).
- It does not prove a continuum Weyl law, spectral dimension, or any force / selected W.
- It does not upgrade SPECTRUM.md’s free-spectrum hit-rate string “roughly 0.4–0.7” (that remains a numerical observation).

#### Numerical observation

For n = 1..5, eigvalsh of L_D from gasket_graph.py matches φ_−^{(n−1)}(2) to machine precision, and the successive ratios match 2/(5+√(25−4 λ_min(n−1))) exactly on those floats (SPECTRUM.md table: 2, 0.438447, 0.089284, 0.017921, 0.003587 with ratios ≈ 0.219, 0.204, 0.201, 0.200). Supporting only.

#### Not a consequence

This subsection does not select W, does not state a continuum limit, a force, a stress, or a momentum, and does not identify free decimation hit rates with 1 − μ_exc.


### Free decimation hit predicate on build_gasket(n)

Dated 2026-10-08 (America/New_York).

#### Assumptions

- Same free gasket graph build_gasket(n) and free L_n = D − A as in Free mult(6). V_0 = the three corners (degree 2), V_{n−1} ⊂ V_n embedded by position, every vertex of V_n \ V_{n−1} is a midpoint of exactly one (n−1)-cell and has degree 4 with all four neighbours in that cell. N(n) = |V_n| = (3^{n+1}+3)/2 (constructor).
- Already proved in this file: free mult(6) = (3^n − 3)/2 (n ≥ 2), spanned by the u_x, which vanish on V_0; free mult(5) = (3^{n−1} − 1)/2 (n ≥ 3), with every free 5-eigenfunction vanishing on V_0; exceptional mass M_exc and μ_exc → 5/9.
- R(z) = z(5 − z). The classical spectral-decimation identities (Fukushima–Shima; Qiu arXiv:1206.1381 Prop. 2.1, opened in the 2026-10-02 runs and not reopened this run) are re-derived below by elementary algebra, including the free-corner defect, so the argument does not rest on the citation except where marked.

S_W is not an input. No value of W is selected.

#### Definition (hit predicate)

For n ≥ 1, call λ ∈ Spec(L_n) \ {3, 5, 6} a **decimation hit** if R(λ) ∈ Spec(L_{n−1}) (set membership, no multiplicity condition). The hit mass is
    h_n := (1/N(n)) Σ_{hits λ} mult_n(λ).
Write DN_n(λ) := {u ∈ ker(L_n − λ) : u|_{V_0} = 0}, d_n := Σ_λ dim DN_n(λ), r_n(λ) := rank of corner evaluation ker(L_n − λ) → ℝ^{V_0}, and c_n := Σ_λ r_n(λ) = N(n) − d_n (the corner-visible dimension; equivalently the dimension of the L_n-cyclic subspace generated by the three corner indicators).

This predicate is defined here. SPECTRUM.md’s informal “hit rates roughly 0.4–0.7” is not identified with h_n (see Numerical observation).

#### Derivation

Step 1 (midpoint extension). On one (n−1)-cell with corners x, y, z, the three midpoint equations of (L_n − λ)u = 0 read ((5 − λ)I − J)m = b with b_{xy} = u_x + u_y, etc. The matrix has eigenvalues 2 − λ and 5 − λ (twice), so for λ ∉ {2, 5} the midpoints are determined:
    u(m_{xy}) = [(4 − λ)(u_x + u_y) + 2 u_z] / ((2 − λ)(5 − λ)).
In particular an eigenfunction with λ ∉ {2, 5} that vanishes on V_{n−1} is zero (restriction to V_{n−1} is injective).

Step 2 (decimation identity with corner defect). Let v be any function on V_{n−1}, λ ∉ {2, 5}, and u its midpoint extension. Summing the extension formula over the four level-n neighbours of x ∈ V_{n−1} \ V_0 (two cells) and over the two level-n neighbours of a corner c ∈ V_0 (one cell), with Δ = (2 − λ)(5 − λ):
    ((L_n − λ)u)(x) = ((6 − λ)/Δ) · ((L_{n−1} − R(λ))v)(x),
    ((L_n − λ)u)(c) = ((6 − λ)/Δ) · ((L_{n−1} − R(λ))v)(c) + (2λ/(2 − λ)) · v(c).
The interior coefficient is (4 − λ)Δ − 4(4 − λ) = (4 − λ)(λ − 1)(λ − 6) = (6 − λ)(4 − R(λ)); the corner coefficient is κ/Δ with κ = (2 − λ)²(5 − λ) − 2(4 − λ) − (6 − λ)(2 − R(λ)) = 2λ(5 − λ). The defect term is why free D − A does not decimate on corner-visible modes; it vanishes when v(c) = 0.

Step 3 (DN isomorphism). For λ ∉ {2, 5, 6}, restriction u ↦ u|_{V_{n−1}} is an isomorphism DN_n(λ) → DN_{n−1}(R(λ)). Restriction is injective (Step 1); it lands in DN_{n−1}(R(λ)) because u(c) = 0 kills the defect and (6 − λ)/Δ ≠ 0; conversely the midpoint extension of v ∈ DN_{n−1}(μ) is a DN eigenfunction for each root λ of R(λ) = μ (all three rows of Step 2 vanish).

Step 4 (recursion for c_n). For μ ∈ Spec(L_{n−1}) ⊂ [0, 6] the roots (5 ± √(25 − 4μ))/2 are real and distinct; a root lies in {2, 5, 6} only for μ = 0 (root 5) or μ = 6 (root 2). DN_{n−1}(0) = 0 (kernel = constants). Hence
    Σ_{λ ∉ {2,5,6}} dim DN_n(λ) = 2 d_{n−1} − dim DN_{n−1}(6).
For n ≥ 3: DN_{n−1}(6) = ker(L_{n−1} − 6) and DN_n(6) = ker(L_n − 6) (the u_x vanish on V_0), DN_n(5) = ker(L_n − 5) (mult(5) proof, corner values zero). So
    d_n = 2 d_{n−1} − m6_{n−1} + m5_n + m6_n + dim DN_n(2),
and with N(n) − 2N(n−1) = (3^n − 3)/2, m6_{n−1} − m6_n = −3^{n−1}, m5_n = (3^{n−1} − 1)/2,
    c_n = 2 c_{n−1} − 1 − dim DN_n(2)    (n ≥ 3).

Step 5 (base). c_2 = 11, computed exactly as the rank over ℚ of the integer Krylov matrix [L_2^k e_c] (k < 15, c ∈ V_0); this is a finite exact computation (scripts/check_decimation_hits.py, Fraction arithmetic). The same exact computation gives c_3 = 21. Therefore, for every n ≥ 2,
    c_n ≤ 5 · 2^{n−1} + 1.

Step 6 (DN modes are hits). Let n ≥ 3 and λ ∉ {3, 5, 6} with DN_n(λ) ≠ 0. If λ ≠ 2, Step 3 gives a nonzero eigenvector of L_{n−1} for R(λ), so λ is a hit. If λ = 2, R(2) = 6 ∈ Spec(L_{n−1}) because n − 1 ≥ 2. So every non-hit λ ∉ {3, 5, 6} has mult_n(λ) = r_n(λ); λ = 0 is a hit (R(0) = 0) with r_n(0) = 1. Hence
    Σ_{non-hits} mult_n(λ) ≤ c_n − 1 ≤ 5 · 2^{n−1}.

#### Theorem (free hit mass)

For every integer n ≥ 3, with μ_exc(n) = (5·3^{n−1} − 7)/(3^{n+1} + 3),
    1 − μ_exc(n) − 5·2^n/(3^{n+1} + 3) ≤ h_n ≤ 1 − μ_exc(n),
and therefore h_n → 4/9 as n → ∞. The non-decimating (non-hit, non-exceptional) spectral mass is at most 5·2^{n−1}/N(n) = O((2/3)^n). Also, for n ≥ 3, c_n = 2c_{n−1} − 1 − dim DN_n(2) exactly.

#### Corollary using classical Dirichlet structure

The Dirichlet bottom-ratio subsection uses Qiu §2: for m ≥ 2 every Dirichlet eigenvalue is initial (5 or 6) or φ_±(μ) of a level-(m−1) Dirichlet eigenvalue, with 6 continuing only to 3. Then 2 ∉ Spec(L_D^{(m)}) for m ≥ 2 (φ_+ ≥ 3, and φ_−(μ) = 2 only for μ = 6). DN_n(2) restricts injectively into ker(L_D^{(n)} − 2), so DN_n(2) = 0 and, resting on that classical input,
    c_n = 5 · 2^{n−1} + 1 for every n ≥ 2.

#### Still open

Whether a corner-visible eigenvalue λ (DN_n(λ) = 0, λ ≠ 0) can be a coincidental hit, i.e. R(λ) ∈ Spec(L_{n−1}) without decimation. If none occurs, the non-hit count is exactly 5·2^{n−1} and h_n = 1 − μ_exc(n) − 5·2^n/(3^{n+1}+3) exactly. This is a numerical observation for n = 3..6 only, not proved. (Update, later on 2026-10-08: settled exactly for 3 ≤ n ≤ 11 by a finite certificate, and DN_n(2) = 0 proved without Qiu; see “Corner channels and coincidental hits”. General n remains open.)

#### Numerical observation

scripts/check_decimation_hits.py (eigh on the same constructor, tolerances 1e−8 / 1e−7): for n = 1..6, c_n = 6, 11, 21, 41, 81, 161 = 5·2^{n−1}+1; dim DN_n(2) = 0; non-hit counts 5, 9, 20, 40, 80, 160 (n = 2 has 9 because its 5-space has one corner-visible direction); hit counts 1, 1, 3, 19, 87, 331, so h_n ≈ 0.167, 0.067, 0.071, 0.154, 0.238, 0.302, increasing toward 4/9 ≈ 0.444 from below; the decimation identity with corner defect has residual ≤ 2.2e−15. The fraction (hits + exceptional)/N is 0.40, 0.52, 0.67, 0.78, 0.85 for n = 2..6, which is compatible with SPECTRUM.md’s “0.4–0.7” for n = 2..4; that is a guess about how the old string was produced, not an identification, and that quantity tends to 1, not to 4/9.

#### Not a consequence

This subsection does not select W, does not state a continuum limit, a force, a stress, or a momentum, and does not claim the hit predicate or the corner defect formula is new.


### Corner channels and coincidental hits on build_gasket(n)

Dated 2026-10-08 (America/New_York), second run of the day.

#### Assumptions

- Same free gasket graph build_gasket(n), free L_n = D − A, V_0, V_{n−1} ⊂ V_n, R(z) = z(5 − z), Δ = (2 − λ)(5 − λ), c_n, r_n(λ), DN_n(λ) and the hit predicate exactly as in "Free decimation hit predicate". Level 0 is the triangle, L_0 = 3I − J.
- The rotation/reflection group S_3 of the triangle acts on build_gasket(n) by graph automorphisms that permute V_0 (the constructor is symmetric under it).
- Already proved in this file and used: Step 1 (midpoint extension), Step 2 (decimation identity with corner defect), Step 3 (DN isomorphism), Step 4 recursion c_n = 2c_{n−1} − 1 − dim DN_n(2) (n ≥ 3); corner values vanish on ker(L_n − 6) (n ≥ 2), on ker(L_n − 5) (n ≥ 3), and on ker(L_n − 3) (n ≥ 3, because the free mult(3) proof shows every 3-eigenfunction restricts on V_{n−1} to an element of ker(L_{n−1} − 6), and restriction keeps corner values).
- No literature was opened for this subsection. Writing spectral decimation through a Schur complement is a standard technique; no claim is made that the closed forms below are new.

S_W is not an input. No value of W is selected.

#### Derivation

Step 1 (corner Schur complement). For λ off Spec(L_D^{(n)}) let S_n(λ) be the Schur complement of L_n − λ onto V_0; then S_n(λ)^{−1} = G_n(λ) := [(L_n − λ)^{−1}]_{V_0 V_0}. G_n commutes with the S_3 permutation matrices, whose commutant on ℝ³ is span{I, J}, so
    S_n(λ) = t_n(λ) I + ((s_n(λ) − t_n(λ))/3) J,
with s_n the eigenvalue on (1,1,1) (symmetric channel) and t_n the eigenvalue on its orthogonal complement (standard channel, two-dimensional). For level 0, s_0 = −λ and t_0 = 3 − λ.

Step 2 (recursion). By Step 2 of the hit subsection, for λ ∉ {2, 5} the Schur complement of L_n − λ onto V_{n−1} is ((6 − λ)/Δ)(L_{n−1} − R(λ)) + (2λ/(2 − λ)) P_{V_0}. Schur complements compose (eliminate the midpoints, then V_{n−1} \ V_0), and adding a multiple of P_{V_0} commutes with eliminating V_{n−1} \ V_0. Hence, as an identity of rational functions,
    S_n(λ) = ((6 − λ)/Δ) S_{n−1}(R(λ)) + (2λ/(2 − λ)) I,
    s_n(λ) = [(6 − λ) s_{n−1}(R(λ)) + 2R(λ)] / Δ,   t_n(λ) = [(6 − λ) t_{n−1}(R(λ)) + 2R(λ)] / Δ.
Both channels obey the same affine recursion, so t_n − s_n = 3 Π_{k=0}^{n−1} A(R^k(λ)) with A(x) = (6 − x)/((2 − x)(5 − x)).

Step 3 (channel functions are Herglotz-type). From the spectral resolution, 1/s_n(λ) = (1/3) Σ_k |⟨1_{V_0}, e_k⟩|² /(λ_k − λ) and 1/t_n(λ) = (1/2) Σ_k |⟨e, e_k⟩|²/(λ_k − λ) with e = 1_{c_1} − 1_{c_2}. These have simple poles with positive residues exactly at the distinct eigenvalues seen by the respective channel; zeros lie strictly between consecutive poles. So if σ_n (τ_n) is the number of distinct eigenvalues seen by the symmetric (standard) channel, the reduced form of s_n (t_n) has numerator degree σ_n (τ_n) and denominator degree one less, with all denominator roots strictly inside the spectral range and none at 0 for s_n (0 is a pole of 1/s_n, the constants). The residue of G_n at λ is minus the eigenprojection compressed to V_0; it is S_3-invariant, so its rank is r_n(λ) = [λ seen by the symmetric channel] + 2·[λ seen by the standard channel]. Hence c_n = σ_n + 2τ_n.

Step 4 (exact cancellations). Write s_{n−1} = q/p reduced. The recursion gives numerator (6 − λ)q(R) + 2Rp(R) (degree 2σ_{n−1} + 1, leading term from (6 − λ)q(R)) over Δ p(R) (degree 2σ_{n−1}).
- λ = 5: R = 0 and the numerator equals q(0) = 0, because s_{n−1}(0) = 0. The factor (5 − λ) cancels once.
- λ = 2: R = 6. For m ≥ 1, s_m(6) = A(6)s_{m−1}(−6) + 2·6/(2 − 6) = −3 (A(6) = 0, and −6 is not a pole of s_{m−1}). So for n ≥ 2 the numerator at λ = 2 is 4p(6)(s_{n−1}(6) + 3) = 0 and (2 − λ) cancels once. For n = 1 the numerator at 2 is −4, so no cancellation.
- Roots of p(R(λ)): there q(R) ≠ 0, so the numerator equals (6 − λ)q(R), which vanishes only at λ = 6, and R(6) = −6 is not a root of p. No cancellation.
So for n ≥ 2 the reduced pair has degrees (2σ_{n−1} − 1, 2σ_{n−1} − 2), giving σ_n = 2σ_{n−1} − 1 with σ_1 = 2, and the reduced denominator is p(R(λ)).
For the standard channel, t_m(0) = 3(3/5)^m ≠ 0 and 0 is not a pole of t_m, so (5 − λ) never cancels; t_m(6) = −3 for every m ≥ 0 (t_0(6) = −3 directly), so (2 − λ) cancels once for every n ≥ 1; the same argument as above excludes other cancellations. So τ_n = 2τ_{n−1} with τ_0 = 1.

#### Theorem (corner channels)

For every integer n ≥ 1, in reduced form,
    s_n = Q_n / P_n,  P_n(λ) = 2 − R^{n−1}(λ),
    t_n = Qt_n / Pt_n,  Pt_n(λ) = Π_{k=0}^{n−1} (5 − R^k(λ)),
where Q_n, Qt_n are integer polynomials with leading coefficient ±1, deg Q_n = 2^{n−1} + 1 and deg Qt_n = 2^n. The symmetric channel sees exactly σ_n = 2^{n−1} + 1 distinct eigenvalues of L_n (the roots of Q_n) and the standard channel sees τ_n = 2^n (the roots of Qt_n, each with corner rank 2). Consequently
    c_n = 5 · 2^{n−1} + 1   for every n ≥ 1
(c_0 = 3). Integrality and the leading coefficients follow by induction from the recursion, since the divisions in Step 4 are by the monic factors λ − 5 and λ − 2 and the leading term always comes from (6 − λ)q(R).

#### Corollary (DN_n(2) = 0 without the classical Dirichlet input)

Inserting c_n = 5 · 2^{n−1} + 1 into c_n = 2c_{n−1} − 1 − dim DN_n(2) gives dim DN_n(2) = 0 for every n ≥ 3. This replaces the Qiu §2 citation in the Corollary of the hit subsection by an elementary argument, and replaces the finite rational Krylov computation of c_2 = 11 by the theorem.

#### Reduction of the coincidental-hit question

Let n ≥ 3. A coincidental hit is a corner-visible λ ≠ 0 with R(λ) ∈ Spec(L_{n−1}). Every eigenvalue of L_{n−1} is a root of
    H_{n−1}(μ) := Q_{n−1}(μ) Qt_{n−1}(μ) Π_{j=0}^{n−3} Π_{a∈{2,5,6}} (R^j(μ) − a),
because corner-visible eigenvalues are roots of Q_{n−1} Qt_{n−1}, and iterating Step 3 shows a DN eigenvalue μ at level m satisfies R^j(μ) ∈ {2, 5, 6} for some 0 ≤ j ≤ m − 2 (the chain cannot reach level 1, since DN_1 = 0: the three corner rows force all pairwise sums of midpoint values to vanish). So coincidental hits at level n are exactly among the roots λ ≠ 0 of gcd(Q_n Qt_n, H_{n−1}∘R), and none exist when that gcd is λ.

#### Exact finite certificate (3 ≤ n ≤ 11)

scripts/check_corner_channels.py builds Q_n, Qt_n by the recursion (exact integer arithmetic up to n = 8, asserting the Step 4 divisions have remainder 0; over F_p with p = 2^61 − 1 up to n = 11) and computes gcds over F_p. Since every polynomial involved has leading coefficient ±1, its reduction mod p keeps its degree, so the degree of the F_p gcd is an upper bound for the degree of the gcd over ℚ. For every 3 ≤ n ≤ 11: deg gcd(Q_n, H_{n−1}∘R) = 1 (and λ divides it) and deg gcd(Qt_n, H_{n−1}∘R) = 0. Hence, for 3 ≤ n ≤ 11, as a finite exact computation:
- no corner-visible eigenvalue other than 0 is a decimation hit, and every corner-visible λ ≠ 0 has DN_n(λ) = 0;
- the non-hit mass is exactly c_n − 1 = 5 · 2^{n−1}, the hit count is N(n) − M_exc(n) − 5 · 2^{n−1}, and
    h_n = 1 − μ_exc(n) − 5 · 2^n/(3^{n+1} + 3)   exactly.
This upgrades the n = 3..6 floating-point observation of the hit subsection (hit counts 3, 19, 87, 331) to exact statements and extends them to n ≤ 11.

#### Still open

- Coincidental hits for general n ≥ 12, that is, gcd(Q_n Qt_n, H_{n−1}∘R) = λ for all n. (Update, third run of 2026-10-08: reduced to one residue condition in characteristic 2 and settled for n ≤ 18; see “Two-adic reduction of coincidental hits”.) Reduction mod 23 also gave the minimal gcd degrees in both channels for every n = 3..9 tested (mod 3 only in the symmetric channel), but no inductive structure mod a fixed prime was found that would carry this to all n. So this is not proved.
- The symmetric-channel poles P_n = 2 − R^{n−1}(λ) and standard-channel poles Pt_n are recorded as algebra only; they are not identified with a Dirichlet spectrum here.

#### Numerical observation

The same script compares with eigh on the constructor for n = 0..6: the Schur identity residual (exact rational evaluation of Q/P at λ = 0.37) is at most 2 · 10^{−14}; channel counts σ_n = 1, 2, 3, 5, 9, 17, 33 and τ_n = 1, 2, 4, …, 64; c_n = 3, 6, 11, 21, 41, 81, 161; and r_n(3) = 0 for n = 1..6. In floating point, the smallest distance from R(λ) to Spec(L_{n−1}) over corner-visible λ ≠ 0 shrinks from about 1.0 at n = 1 to about 4 · 10^{−4} at n = 5, which is why the exact certificate is used instead of tolerances.

#### Not a consequence

This subsection does not select W, does not state a continuum limit, a force, a stress, or a momentum, and does not claim that the Schur-complement form of spectral decimation or these closed forms are new.


### Two-adic reduction of coincidental hits on build_gasket(n)

Dated 2026-10-08 (America/New_York), third run of the day.

#### Assumptions

- Everything in "Corner channels and coincidental hits": the channel recursion x_n(λ) = A(λ) x_{n−1}(R(λ)) + B(λ) for x ∈ {s, t}, with A(λ) = (6 − λ)/Δ, B(λ) = 2λ/(2 − λ), Δ = (2 − λ)(5 − λ); the reduced forms Q_n/P_n and Qt_n/Pt_n; the cancellation analysis of Step 4; s_m(6) = t_m(6) = −3 (m ≥ 1); poles of both channels lie in (0, 6); the roots of Q_n (Qt_n) are exactly the eigenvalues seen by the symmetric (standard) channel.
- From earlier subsections: DN_m(2) = 0 for every m ≥ 1 (m = 1: DN_1 = 0; m = 2: d_2 = N(2) − c_2 = 4 = dim DN_2(6) + dim DN_2(5); m ≥ 3: corner-channel corollary); corner values vanish on ker(L_n − λ) for λ ∈ {3, 5, 6}, n ≥ 3; a DN eigenvalue μ at level n − 1 has a first index j ≤ n − 3 with R^j(μ) = a ∈ {2, 5, 6} and DN_{n−1−j}(a) ≠ 0.
- Algebraic facts used: eigenvalues are algebraic integers; for a prime 𝔭 above 2 in a number field containing the relevant numbers, reduction mod 𝔭 is a ring map to a finite field of characteristic 2, and the 2-adic valuation v (v(2) = 1) extends to that field. No literature was opened this run, and no novelty is claimed for the method.

S_W is not an input. No value of W is selected.

#### Derivation

Write T(x) = x² + x over F_2, so R(z) = z(5 − z) reduces to T.

Step 1 (mod-2 form of the channels). Over ℤ, (2 − λ) Qt_n = (6 − λ) Qt_{n−1}(R) + 2R · Pt_{n−1}(R) and, for n ≥ 2, (λ − 2)(λ − 5) Q_n = (6 − λ) Q_{n−1}(R) + 2R · P_{n−1}(R). Reducing mod 2 and cancelling λ (respectively λ(λ + 1)) in the domain F_2[x] gives Qt_n ≡ Qt_{n−1}∘T and (x + 1) Q_n ≡ Q_{n−1}∘T. With Qt_0 = 3 − λ ≡ x + 1 and Q_1 = λ(λ − 4) ≡ x², induction (using T^{j+1} = T^j (T^j + 1)) gives
    Qt_n ≡ T^n(x) + 1,    Q_n ≡ x · T^{n−1}(x)    (mod 2, n ≥ 1).
So a standard-channel eigenvalue λ has residue λ̄ with T^n(λ̄) = 1, and a symmetric-channel eigenvalue has λ̄ = 0 or T^{n−1}(λ̄) = 0; in both symmetric cases T^n(λ̄) = 0. Since T(0) = T(1) = 0, T^j(λ̄) ∉ {0, 1} for j < n in the standard case.

Step 2 (same-channel exclusion). Let n ≥ 2, x ∈ {s, t}, x_{n−1} = q/p reduced, and let λ ∉ {0, 2, 5, 6} be a zero of the reduced x_n. Off {2, 5} the reduced numerator vanishes exactly where N(λ) = (6 − λ) q(R(λ)) + 2R(λ) p(R(λ)) does. If q(R(λ)) = 0 then p(R(λ)) ≠ 0 and N(λ) = 2R(λ)p(R(λ)) ≠ 0, because R(λ) = 0 forces λ ∈ {0, 5}. If p(R(λ)) = 0 then N(λ) = (6 − λ)q(R(λ)) ≠ 0. So R(λ) is neither a zero nor a pole of x_{n−1}: a coincidental hit never lands on an eigenvalue seen by its own channel.

Step 3 (cross-channel exclusion, mod 2). Let μ = R(λ), so μ̄ = T(λ̄). If λ is standard and μ is symmetric at level n − 1, then T^{n−1}(μ̄) = 0 by Step 1, so T^n(λ̄) = 0 ≠ 1. If λ is symmetric and μ is standard, then T^{n−1}(μ̄) = 1, so T^n(λ̄) = 1, contradicting T^n(λ̄) = 0.

Step 4 (DN branch, standard channel, mod 2). If μ is a DN eigenvalue at level n − 1, then R^k(λ) = a ∈ {2, 5, 6} with k = j + 1 ≤ n − 2, so T^k(λ̄) ∈ {0, 1} with k < n, which Step 1 forbids for a standard eigenvalue.

Step 5 (λ = 2). Qt_n(2) ≡ T^n(0) + 1 = 1 (mod 2), so 2 is not standard. For the symmetric channel, differentiate s_n Δ = (6 − λ)s_{n−1}(R) + 2R at λ = 2 (s_n is regular at 2 for n ≥ 2) and at λ = 6 (s_m(6) = −3): s_n(2) = −(5 + 4 s′_{n−1}(6))/3 and s′_m(6) = (1 − s_{m−1}(−6))/4, so
    s_n(2) = (s_{n−2}(−6) − 6)/3    (n ≥ 2).
From the spectral resolution, 1/s_m(−6) = (1/3) Σ_k |⟨1_{V_0}, e_k⟩|²/(λ_k + 6) ≤ 1/6, with equality only if 1_{V_0} is constant, which fails for m ≥ 1. Hence s_n(2) > 0 for n ≥ 3 (and s_2(2) = 0, matching the root 2 of Q_2). So 2 is never a corner-visible eigenvalue for n ≥ 3.

Step 6 (DN branch, symmetric channel, two-adic). Now λ is symmetric, λ ∉ {0, 2, 3, 5, 6}, and R^k(λ) = a with k ≤ n − 2 minimal. The value a = 2 is impossible because DN_m(2) = 0 for all m. Put m = n − k ≥ 2, w_i = R^{k−i}(λ) (so w_0 = a, w_k = λ, w_i ∉ {2, 5, 6} for i ≥ 1), y_0 = s_m(a), y_i = A(w_i) y_{i−1} + B(w_i). Because s_m is regular at a and A, B are regular at each w_i, y_i = s_{m+i}(w_i), and y_k = s_n(λ) must be 0.
- For a = 6: w_1 = 3, y_1 = A(3)(−3) + B(3) = −3/2. For i ≥ 2, w_{i−1} is a unit, so w_i and 5 − w_i are units, A(w_i) is a unit and v(B(w_i)) = 1. Hence v(y_i) = −1 for all i ≥ 1, and y_k ≠ 0.
- For a = 5: s_m(5) = 5(3^{m−2} − 1)/2 (from s′_m(0) = −(3^m + 1)/2, which follows from differentiating the recursion at 0, and then differentiating at 5). Every w_i with i ≥ 1 is a unit with 5 − w_i a unit, so A(w_i) is a unit and v(B(w_i)) = 1. If m is odd, v(y_0) = v(3^{m−2} − 1) − 1 = 0, so v(y_i) = 0 for all i, and y_k ≠ 0.
- For a = 5 and m even, y_0 = 0 (m = 2) or v(y_0) ≥ 2. Then η_i = y_i/2 is integral, and its residue obeys η̄_i = η̄_{i−1}/(1 + z_i) + 1 with z_i = w̄_i, z_0 = 1, z_{i−1} = z_i² + z_i, η̄_0 = 0. Since 1/z_i = (1/z_{i−1})(1 + z_i), the substitution θ_i = η̄_i/z_i telescopes to
    η̄_k = z_k · S_k,    S_k := Σ_{i=1}^{k} 1/z_i.
  If S_k ≠ 0 then v(y_k) = 1 and y_k ≠ 0.

#### Theorem (two-adic reduction)

For every n ≥ 3, a coincidental hit λ at level n, if one exists, is seen only by the symmetric channel and satisfies R^k(λ) = 5 for some k with 1 ≤ k ≤ n − 2 and n − k even, with R^i(λ) ∉ {2, 5, 6} for i < k, and the residue chain z_i = R^{k−i}(λ) mod 𝔭 satisfies S_k = Σ_{i=1}^k 1/z_i = 0 in characteristic 2, for every prime 𝔭 above 2. In particular:
- the standard channel never has coincidental hits, for any n;
- coincidental hits never reach eigenvalues of the same channel, the other channel, or the DN chains that end at 6;
- λ = 2 is not an eigenvalue seen at the corners for n ≥ 3.

#### Exact finite verification of the residue condition

The residue statement depends only on k. Over F_2, T^k(x) + 1 is separable (its derivative is 1), and on GF(2^64) the map T is nilpotent with a one-dimensional kernel, so all 2^k roots of T^k(x) = 1 lie in GF(2^64) for k ≤ 63. scripts/check_coincidental_reduction.py checks that the modulus x^64 + x^4 + x^3 + x + 1 is irreducible, enumerates all 2^k chains, and confirms S_k ≠ 0 for every chain with 1 ≤ k ≤ 16. It also verifies the mod-2 congruences of Step 1 and the values s_m(6), s_m(5), s_n(2) exactly for n, m ≤ 8.

Corollary (finite exact computation plus the theorem above). A coincidental hit needs k ≥ 17, hence n ≥ 19. So for 3 ≤ n ≤ 18 there are no coincidental hits, the non-hit mass is exactly 5 · 2^{n−1}, and
    h_n = 1 − μ_exc(n) − 5 · 2^n/(3^{n+1} + 3)   exactly.
This extends the F_p gcd certificate (3 ≤ n ≤ 11) of the previous subsection to n ≤ 18 by a different route; the two agree on the overlap.

#### Still open

- Residue conjecture: for every k ≥ 1 and every chain z_0 = 1, z_i² + z_i = z_{i−1} in the algebraic closure of F_2, Σ_{i=1}^k 1/z_i ≠ 0. Equivalently, after S_k = S_{k−1} + 1/z_k, z_{k−1} S_{k−1}² + S_{k−1} + 1 ≠ 0. Verified for k ≤ 16 only. If it holds for all k, the exact h_n formula holds for every n ≥ 3. Neither a proof nor a counterexample is known here, and failure of the residue test would not by itself produce a hit (it only removes this obstruction).
- No 5-adic or 3-adic argument was found for the a = 5, m even case: the valuations of A(w_i) y_{i−1} and B(w_i) tie at every step.

#### Not a consequence

This subsection does not select W, does not state a continuum limit, a force, a stress, or a momentum, and does not claim that reducing spectral questions mod 2 is new.

### Residue condition: power-of-two lemma and exhaustive check to k = 31

Dated 2026-10-08 (America/New_York), fourth run of the day.

#### Assumptions

- Everything in "Two-adic reduction of coincidental hits", in particular its theorem: a coincidental hit at level n ≥ 3 needs some k with 1 ≤ k ≤ n − 2, n − k even, and a chain z_0 = 1, z_i² + z_i = z_{i−1} over the algebraic closure of F_2 with S_k = Σ_{i=1}^k 1/z_i = 0.
- Elementary finite-field facts only: Frobenius F(x) = x² is F_2-linear on the algebraic closure of F_2, and {x : x^{2^d} = x} is the field GF(2^d). No literature was opened this run, and no novelty is claimed.

S_W is not an input. No value of W is selected.

#### Derivation

Write N(x) = x² + x, so N = F + 1 as F_2-linear operators. F and 1 commute and the characteristic is 2, so for every j ≥ 0
    N^{2^j} = F^{2^j} + 1,   hence   ker N^{2^j} = GF(2^{2^j}) =: E_j,
which is a field. Along a chain, N^i(z_i) = z_0 = 1 ≠ 0 and N(1) = 0, so N^{i+1}(z_i) = 0 and N^i(z_i) ≠ 0. Therefore z_i ∈ E_j if and only if i + 1 ≤ 2^j.

Lemma (power-of-two lengths). Let k = 2^j with j ≥ 0. Every z_i with i ≤ k − 1 lies in the field E_j, so S_{k−1} ∈ E_j, while z_k ∉ E_j, so 1/z_k ∉ E_j. Hence S_k = S_{k−1} + 1/z_k ∉ E_j; in particular S_k ≠ 0, for every chain.

Remark (no contradiction obtained beyond powers of two). For 2^{j−1} ≤ i < 2^j, the generator σ = F^{2^{j−1}} of Gal(E_j/E_{j−1}) acts on a chain by σ(z_i) = z_i + z_{i−2^{j−1}} and fixes z_i for i < 2^{j−1}. This gives a second proof of the lemma at k = 2^j, but applying σ to S_k = 0 for k = 2^{j−1} + 1 produced no contradiction in this run. The general case stays open.

#### Exact finite verification (1 ≤ k ≤ 31)

Because N^{32} = 0 on GF(2^32) and ker N = {0, 1}, every chain of length k ≤ 31 lies in GF(2^32) = F_2[x]/(x^32 + x^7 + x^3 + x^2 + 1), and the two roots of y² + y = z_{i−1} are y and y + 1. scripts/check_residue_extension.py checks that this modulus is irreducible (x^{2^32} ≡ x and gcd(x^{2^16} − x, f) = 1). It then compiles scripts/residue_chains_gf2_32.c, which enumerates all 2^k chains for every k ≤ 31 (2^32 − 2 chain prefixes in total) and confirms S_k ≠ 0 each time. S_k is carried as num/den with den = z_1 ⋯ z_k ≠ 0, so the zero test is exact. As a cross-check between two independent field models, the histogram of the N-level of S_k (the least m with N^m(S_k) = 0, which does not depend on the model of the field) over all chains with k ≤ 10 agrees between GF(2^32) (C) and GF(2^64) (Python, from scripts/check_coincidental_reduction.py). The C program's portable multiplication (no carry-less multiply instruction) reproduces the same histogram.

#### Corollary (theorem plus finite exact computation)

S_k ≠ 0 for every chain when 1 ≤ k ≤ 32 (k ≤ 31 by computation, k = 32 by the lemma) and when k is any power of two. By the two-adic reduction theorem, a coincidental hit would need k ≥ 33 with k not a power of two, n − k even, and n ≥ k + 2, so n ≥ 35. Hence for 3 ≤ n ≤ 34 there are no coincidental hits, the non-hit mass is exactly 5 · 2^{n−1}, and
    h_n = 1 − μ_exc(n) − 5 · 2^n/(3^{n+1} + 3)   exactly.
This extends the previous range 3 ≤ n ≤ 18.

#### Still open

- Residue conjecture for k ≥ 33 that are not powers of two (equivalently, for all k): Σ_{i=1}^k 1/z_i ≠ 0 for every chain. Not proved, and no counterexample is known. The trace of S_k over E_j and the N-level of S_k both vary from chain to chain (checked for k ≤ 13 and k ≤ 12), so neither is an invariant that would prove it.
- As before, failure of the residue test would only remove this obstruction; it would not by itself produce a hit.

#### Not a consequence

This subsection does not select W, does not state a continuum limit, a force, a stress, or a momentum, and does not claim that the finite-field argument is new.


### Residue condition: lengths 2^j + 1 and the limits of the subfield test

Dated 2026-10-08 (America/New_York), fifth run of the day.

#### Assumptions

- Everything in "Residue condition: power-of-two lemma and exhaustive check to k = 31": N(x) = x² + x = F + 1, E_j = ker N^{2^j} = GF(2^{2^j}), and along a chain z_0 = 1, z_i² + z_i = z_{i−1}, one has z_i ∈ E_j if and only if i + 1 ≤ 2^j.
- Elementary algebra in characteristic 2 only. No literature was opened this run, and no novelty is claimed.

S_W is not an input. No value of W is selected.

#### Derivation

Pairing identity. Since z_i(z_i + 1) = z_{i−1},
    1/z_i + 1/(z_i + 1) = (z_i + 1 + z_i)/z_{i−1} = 1/z_{i−1},
so 1/z_{i−1} + 1/z_i = 1/(z_i + 1) for every i ≥ 1. The element z_i + 1 is the sibling root of y² + y = z_{i−1}.

Lemma (lengths 2^j + 1). Let j ≥ 1, p = 2^j, k = p + 1. By the pairing identity at i = p + 1,
    S_{p+1} = S_{p−1} + 1/z_p + 1/z_{p+1} = S_{p−1} + 1/w,   w = z_{p+1} + 1.
Every z_i with i ≤ p − 1 lies in the field E_j, so S_{p−1} ∈ E_j. Because N is additive and N(1) = 0, N^p(w) = N^p(z_{p+1}) = z_1, and z_1 ≠ 0 (z_1² + z_1 = 1). So w ∉ E_j = ker N^p, hence 1/w ∉ E_j, and S_{p+1} ∉ E_j. In particular S_{p+1} ≠ 0 for every chain. This settles the case k = 2^{j−1} + 1 that the previous run's Galois-conjugation remark left without a contradiction.

Negative result (the subfield test does not extend). For 2^j < k < 2^{j+1} with p = 2^j, the lemma and the power-of-two lemma both prove S_k ≠ 0 by showing S_k ∉ E_j. That stronger property is false in general. Exhaustive counts in GF(2^64) (scripts/check_residue_p_plus_one.py; k = 15 by a separate run of the same loop) give the number of chains with S_k ∈ GF(2^p):
    k = 6: 8 of 64;  k = 11: 32 of 2048;  k = 13: 48 of 8192;  k = 14: 32 of 16384;  k = 15: 176 of 32768,
and 0 for k = 7, 10, 12 (as well as for k = 3, 5, 9, covered by the lemma). On those chains S_k is still nonzero (exhaustive check), but the reason is not membership outside the subfield. So S_k ∉ GF(2^p) cannot prove the conjecture for all k, and k = p + 2, k = p + 3, and k = 2p − 1 are not uniformly covered by it (k = 6, 11, 15 fail).

Reformulation (recorded, not used for the corollary). Let A_k = F_2[t]/(N^k(t) + 1). Its points are exactly the chain endpoints z_k, and S_k is the image of Σ_{m<k} 1/N^m(t). So the conjecture for k says S_k is a unit in A_k, that is, its norm to F_2 is 1. Taking norms one Artin–Schreier step at a time (z ↦ z + 1 over c = z² + z, with S ↦ S + 1/z) gives polynomials G_0 = S, G_1 = zS² + S + 1, G_2 = zS⁴ + S³ + 1, …, where powers of z (units) have been removed, and the conjecture for k becomes G_k(1, 0) = 1. A symbolic computation gives G_k(1, 0) = 1 for k ≤ 7, which is consistent with the exhaustive check. The number of terms grows (3, 3, 13, 27, 103, 365, 1651 for k = 1..7), and no closed form was found.

#### Corollary (theorem plus finite exact computation)

S_k ≠ 0 for every chain when 1 ≤ k ≤ 33 (k ≤ 31 by computation, k = 32 by the power-of-two lemma, k = 33 = 2^5 + 1 by the lemma above), and when k = 2^j or k = 2^j + 1 for any j. By the two-adic reduction theorem, a coincidental hit at level n needs some open k ≤ n − 2 with n − k even; the smallest open k is 34, so n ≥ 36. Hence for 3 ≤ n ≤ 35 there are no coincidental hits, and
    h_n = 1 − μ_exc(n) − 5 · 2^n/(3^{n+1} + 3)   exactly.
This extends the previous range 3 ≤ n ≤ 34.

#### Still open

- Residue conjecture for k ≥ 34 with k ∉ {2^j, 2^j + 1}: Σ_{i=1}^k 1/z_i ≠ 0 for every chain. Not proved, and no counterexample is known.
- As before, failure of the residue test would only remove this obstruction; it would not by itself produce a hit.

#### Not a consequence

This subsection does not select W, does not state a continuum limit, a force, a stress, or a momentum, and does not claim that the finite-field argument is new.

### Residue condition: Frobenius orbit reduction and exact check to k = 45

Dated 2026-10-08 (America/New_York), sixth run of the day.

#### Assumptions

- Everything in "Residue condition: power-of-two lemma and exhaustive check to k = 31" and "Residue condition: lengths 2^j + 1 and the limits of the subfield test": N(x) = x² + x = F + 1 with F(x) = x², E_a = ker N^{2^a} = GF(2^{2^a}), and along a chain z_0 = 1, z_i² + z_i = z_{i−1}, one has z_i ∈ E_a if and only if i + 1 ≤ 2^a.
- The two-adic reduction theorem, in the form used before: a coincidental hit at level n ≥ 3 needs some k with 1 ≤ k ≤ n − 2, n − k even, and a chain with S_k = Σ_{i=1}^k 1/z_i = 0.
- Elementary Galois theory of finite fields only. No literature was opened this run, and no novelty is claimed.

S_W is not an input. No value of W is selected.

#### Derivation

A chain of length k is determined by its top entry, since z_i = N^{k−i}(z_k), and the two continuations of a chain of length j − 1 are y and y + 1, where y² + y = z_{j−1}. So the chains form a binary tree whose depth-j nodes are the chains of length j.

Lemma (Frobenius orbits of chains). Fix k ≥ 1, let B = ⌈log₂(k + 1)⌉ and d = 2^B.
1. F maps chains to chains, and S_k(F(chain)) = S_k(chain)². So S_k vanishes on a chain if and only if it vanishes on every chain in its F-orbit.
2. Every F-orbit of length-k chains has exactly d elements. The orbit of a chain is the orbit of z_k, whose size is the degree of z_k over F_2. That degree is a power of two, and z_k ∈ E_a if and only if k + 1 ≤ 2^a, so it equals d. Hence there are exactly 2^{k−B} orbits.
3. For 2^b ≤ k, the element σ_b = F^{2^b} = N^{2^b} + 1 acts by σ_b(z_i) = z_i + z_{i−2^b} for i ≥ 2^b and fixes z_i for i < 2^b. In particular it fixes the chain up to depth 2^b − 1 and replaces z_{2^b} by its sibling z_{2^b} + 1.
4. Let R_k be any set of length-k chains obtained this way: at every depth j that is a power of two, keep one child of each node (the choice may be arbitrary), and at every other depth keep both children. Then |R_k| = 2^{k−B}, because exactly B depths in 1..k are powers of two. Every orbit meets R_k: starting from any chain, for b = 0, 1, …, B − 1 in increasing order, apply σ_b whenever the depth-2^b entry is not the kept child of its prefix. By 3, this repairs depth 2^b and does not change any shallower depth, so later steps do not undo earlier ones, and the final chain lies in R_k. Comparing |R_k| with the number of orbits in 2, every orbit meets R_k exactly once.

Corollary (reduced test). For every k, S_k ≠ 0 for all 2^k chains if and only if S_k ≠ 0 on the 2^{k−B} chains of R_k. The truncations of R_K to depth j are a valid R_j, so one walk of the reduced tree to depth K checks every k ≤ K at once, at a cost of about 2^{K−⌈log₂(K+1)⌉} chains at the top level instead of 2^K.

#### Exact finite verification (1 ≤ k ≤ 45)

Every chain of length k ≤ 63 lies in GF(2^64) = F_2[x]/(x^64 + x^4 + x^3 + x + 1), whose modulus is checked irreducible in scripts/check_coincidental_reduction.py. scripts/residue_orbits_gf2_64.c walks the reduced tree, keeping the root returned by a fixed linear solver at depths 1, 2, 4, 8, 16, 32 and both roots elsewhere. It carries S_k as num/den with den = z_1 ⋯ z_k ≠ 0, so the zero test is exact, and it finds S_k ≠ 0 at every node for 1 ≤ k ≤ 45. That is 2^{39} reduced chains at k = 45, covering all 2^{45} chains.

Checks of the reduction itself, all exact (scripts/check_residue_orbits.py):
- The number of chains with Tr_d(S_k) = 1, where Tr_d is the trace from GF(2^d) to F_2, is a Galois invariant count. Full enumeration in two independent field models, GF(2^64) and GF(2^32), in Python, gives the same counts for k ≤ 11: 2, 4, 4, 8, 24, 40, 72, 144, 240, 560, 1008.
- In C, for every k ≤ 22, the full tree has 2^k nodes at depth k, the reduced tree has 2^{k−B}, and the full count with Tr_d(S_k) = 1 equals d times the reduced count (for example k = 22: 2099296 = 32 · 65603). The C full counts agree with the Python counts for k ≤ 11.
- The carry-less multiplication is checked against schoolbook multiplication, and the linear root solver is self-tested on the image of N.

#### Corollary (theorem plus finite exact computation)

S_k ≠ 0 for every chain when 1 ≤ k ≤ 45 (by the reduced computation), and when k = 2^j or k = 2^j + 1 for any j (by the two earlier lemmas). The smallest open length is k = 46. By the two-adic reduction theorem, a coincidental hit at level n needs an open k ≤ n − 2 with n − k even. For n = 47 that would be an odd k ≤ 45, and none is open, so a hit needs n ≥ 48. Hence for 3 ≤ n ≤ 47 there are no coincidental hits, and
    h_n = 1 − μ_exc(n) − 5 · 2^n/(3^{n+1} + 3)   exactly.
This extends the previous range 3 ≤ n ≤ 35.

#### Still open

- Residue conjecture for k ≥ 46 with k ∉ {2^j, 2^j + 1}: Σ_{i=1}^k 1/z_i ≠ 0 for every chain. Not proved, and no counterexample is known. The orbit reduction only saves a factor 2^{⌈log₂(k+1)⌉}; it is not a proof for all k, and exhaustive computation stays exponential in k.
- As before, failure of the residue test would only remove this obstruction; it would not by itself produce a hit.

#### Not a consequence

This subsection does not select W, does not state a continuum limit, a force, a stress, or a momentum, and does not claim that the orbit argument is new.


### Residue condition: logarithmic-derivative form and a polynomial gcd certificate

Dated 2026-10-08 (America/New_York), seventh run of the day. This subsection proves an exact reformulation of the residue conjecture and gives an independent finite check. It does not prove the conjecture and does not extend the range k ≤ 45.

Setting (unchanged). Chains z_0 = 1, z_i² + z_i = z_{i−1} over the algebraic closure of F_2, S_k = Σ_{i=1}^k 1/z_i. Write N(t) = t² + t, A_k(t) = N^k(t) + 1 and Π_k(t) = ∏_{j<k} N^j(t) in F_2[t].

#### Lemma (logarithmic-derivative form)

1. N is additive over F_2 and N′ = 1, so every iterate N^j is additive with (N^j)′ = 1, and N^j(t) = Σ_{i ⊆ j} t^{2^i} (the sum over i whose binary digits are a subset of those of j; this is (F + 1)^j with F the Frobenius, expanded by Lucas's theorem).
2. The chain endpoints z_k are exactly the roots of A_k. There are 2^k of them, all distinct because A_k′ = 1, and they form a coset of the k-dimensional F_2-space ker N^k. For k = 2^B − 1, N^k(t) = Σ_{i<2^B} t^{2^i} is the trace polynomial of GF(2^{2^B}); every chain of length k lies in that field (degree lemma of the sixth run), and that field has exactly 2^{2^B−1} = 2^k elements of trace one. So for k = 2^B − 1 the endpoints are exactly the trace-one elements of GF(2^{2^B}).
3. Since z_i = N^{k−i}(z_k) and (N^j)′ = 1, S_k = Σ_{j<k} 1/N^j(z_k) = Π_k′(z_k)/Π_k(z_k), a logarithmic derivative. Here Π_k(z_k) = z_1 ⋯ z_k ≠ 0.
4. The product of Π_k over all roots of A_k is 1. Indeed N^j maps the roots of A_k onto the roots of A_{k−j}, each one hit 2^j times, and the product of the roots of the monic polynomial A_m is A_m(0) = 1 in characteristic 2. Hence the norm of S_k (the product over all 2^k chains) is the resultant Res(A_k, Π_k′) ∈ F_2, and, because A_k is separable, the number of chains with S_k = 0 equals deg gcd(A_k, Π_k′).
5. Square decomposition. Write Π_k = a_k² + t b_k² with a_k, b_k ∈ F_2[t]. In characteristic 2, Π_k′ = b_k², so S_k(z_k) = 0 if and only if b_k(z_k) = 0. From Π_k(t) = t Π_{k−1}(N(t)) one gets a_0 = 1, b_0 = 0 and
       a_k(t) = t b_{k−1}(N(t)),   b_k(t) = a_{k−1}(N(t)) + t b_{k−1}(N(t)),
   with deg b_k = 2^{k−1} − 1.

Corollary (exact reformulation). For each k the residue condition holds for every chain of length k if and only if gcd(N^k(t) + 1, Π_k′(t)) = 1 in F_2[t], equivalently gcd(N^k(t) + 1, b_k(t)) = 1. This gives the earlier norm reformulation (subsection "lengths 2^j + 1", G_k(1, 0) = 1) an explicit form: the norm is a resultant of two explicit polynomials. No term-by-term identification with the G_k polynomials is claimed.

Proof notes. Items 1–3 are direct. In 4, N^j is 2^j-to-1 from the roots of A_k onto the roots of A_{k−j} because it is additive with kernel of size 2^j and maps A_k-roots to A_{k−j}-roots. In 5, Π_k(t) = t a_{k−1}(Nt)² + t²(t + 1) b_{k−1}(Nt)² = (t b_{k−1}(Nt))² + t (a_{k−1}(Nt)² + (t b_{k−1}(Nt))²), and the decomposition into a square plus t times a square is unique.

#### Negative remarks

- Evaluated along a chain, the recursion in 5 is multiplication by the matrix [[0, z_i], [1, z_i]], and the condition b_k(z_k) = 0 unwinds to S_{k−1} = 1/z_k, which is the definition of S_k = 0 again. The recursion alone gives no proof.
- The gcd test with schoolbook Euclid costs on the order of 2^{2k} bit operations (no fast half-gcd library is installed on the box), so it does not compete with the Frobenius-reduced enumeration that reached k = 45. Its value is independence: it uses no chain enumeration, no root solver and no model of GF(2^64).

#### Exact finite verification (scripts/check_residue_logderiv.py)

- (N^j)′ = 1, deg Π_k = 2^k − 1 and deg Π_k′ = 2^k − 2 (k ≤ 12).
- At every chain endpoint in GF(2^64), Π_k(z_k) · S_k = Π_k′(z_k), and the product of Π_k(z_k) over all endpoints is 1 (k ≤ 8).
- The square decomposition and its recursion hold, with deg b_k = 2^{k−1} − 1 (k ≤ 10), and N^{2^B−1} is the trace polynomial (B ≤ 5).
- Positive control for the gcd count: for k ≤ 10 and c ∈ {t^m, t^m + 1 : m < 16}, deg gcd(A_k, Π_k′ + c Π_k) equals the number of chains with S_k = c(z_k), counted by enumeration. Seventeen (k, c) pairs have a nonzero count (for example k = 7, c = t³: 8 chains), and all match.
- Certificate: gcd(N^k + 1, Π_k′) = 1 in F_2[t] for every 1 ≤ k ≤ 21 (k = 21 took 80 s). This re-derives S_k ≠ 0 for k ≤ 21 without chains.

Numerical observation (not used). The Euclidean remainder sequence of (A_k, Π_k′) has 1, 3, 4, 9, 14, 26, 54, 108, 203, 376, 754, 1512, 3009, 6150, 12274, 24653, 49325, 98185, 196780, 393449 division steps for k = 1, …, 20 (about 0.375 · 2^k for large k), and the sequence of degree drops from the top, 2^k − deg r_i, agrees with that for k − 1 on an initial segment whose length roughly doubles with k (65590 steps at k = 20). No pattern was extracted that proves gcd = 1.

#### Status after this run

- Unchanged range: S_k ≠ 0 for every chain when k ≤ 45 or k ∈ {2^j, 2^j + 1}, and h_n = 1 − μ_exc(n) − 5 · 2^n/(3^{n+1} + 3) exactly for 3 ≤ n ≤ 47.
- Still open: the residue conjecture for k ≥ 46 with k ∉ {2^j, 2^j + 1}, now equivalently gcd(N^k + 1, Π_k′) = 1 in F_2[t]. The case k = 2^B − 1 is the statement that Σ_{j<k} 1/N^j(x) ≠ 0 for every trace-one x in GF(2^{2^B}); it is open for B ≥ 6.

#### Not a consequence

This subsection does not select W, does not state a continuum limit, a force, a stress, or a momentum, and does not claim that the logarithmic-derivative identity or the resultant formulation is new. No literature was opened this run.

### Residue condition: exact check to k = 46 and no monomial trace certificate

Dated 2026-10-08 (America/New_York), eighth run of the day. This subsection adds one more length to the exact finite check and records a negative search. It proves no new infinite family.

#### Assumptions

- Everything in "Residue condition: Frobenius orbit reduction and exact check to k = 45": chains z_0 = 1, z_i² + z_i = z_{i−1}, S_k = Σ_{i=1}^k 1/z_i, the orbit lemma (one chain per Frobenius orbit is obtained by keeping one child at every power-of-two depth), and the fact that every chain of length k ≤ 63 lies in GF(2^64).
- The two-adic reduction theorem: a coincidental hit at level n ≥ 3 needs some k with 1 ≤ k ≤ n − 2, n − k even, and a chain with S_k = 0.
- No literature was opened this run, and no novelty is claimed.

S_W is not an input. No value of W is selected.

#### Exact finite verification (1 ≤ k ≤ 46)

The unchanged program scripts/residue_orbits_gf2_64.c (built with gcc -O3 -march=native -fopenmp) was run with KMAX = 46. It walks the reduced tree in GF(2^64) = F_2[x]/(x^64 + x^4 + x^3 + x + 1), carries S_k as num/den with den = z_1 ⋯ z_k ≠ 0, and reports zero vanishing numerators at every depth 1 ≤ k ≤ 46, with exactly 2^{k−⌈log₂(k+1)⌉} reduced chains at each depth. At k = 46 that is 2^{40} representatives, covering all 2^{46} chains. The run took 35.5 minutes of wall time (230 CPU-minutes) on the 8-core box and printed `ok` with zeros = 0 for every k. The reduction checks recorded in the previous subsection (Galois-invariant trace counts, full = 2^B · reduced for k ≤ 22, carry-less multiply against schoolbook) apply unchanged, since the program and field model are the same.

#### Corollary (theorem plus finite exact computation)

S_k ≠ 0 for every chain when 1 ≤ k ≤ 46, and when k = 2^j or k = 2^j + 1 for any j. The smallest open length is k = 47. A coincidental hit at level n needs an open k ≤ n − 2 with n − k even. For n = 48 that would be an even k ≤ 46, and none is open, so a hit needs n ≥ 49. Hence for 3 ≤ n ≤ 48 there are no coincidental hits, and
    h_n = 1 − μ_exc(n) − 5 · 2^n/(3^{n+1} + 3)   exactly.
This extends the previous range 3 ≤ n ≤ 47 by one level. Each further level costs about twice the previous run, so this route stays exponential.

#### Negative result: no monomial trace certificate (scripts/check_residue_trace_monomials.py)

A uniform identity Tr_d(f · S_k) = 1 on all chains of length k, with d = 2^{⌈log₂(k+1)⌉} and Tr_d the trace from GF(2^d) to F_2, would prove S_k ≠ 0. The script enumerates all 2^k chains in GF(2^64) for k ≤ 8 and tests every f = z_k^a z_{k−1}^b and every f = (z_k + 1)^a z_{k−1}^b with −6 ≤ a ≤ 6 and −4 ≤ b ≤ 4. Results:
- k = 1, …, 5 have 18, 120, 63, 49, 12 such certificates, k = 6 and k = 7 have none, and k = 8 has 4 (f = z_7² and f = z_7³, with either choice of sibling).
- No f in this family works for every 2 ≤ k ≤ 8.
So a trace certificate of this simple monomial shape does not exist uniformly in k. This rules out only this family. It does not rule out certificates with other f, and it says nothing against the conjecture.

#### Still open

- Residue conjecture for k ≥ 47 with k ∉ {2^j, 2^j + 1}: Σ_{i=1}^k 1/z_i ≠ 0 for every chain, equivalently gcd(N^k + 1, Π_k′) = 1 in F_2[t]. Not proved, and no counterexample is known.
- Exact h_n for n ≥ 49 (it would follow from the conjecture; failure of the residue test would only remove this obstruction, not produce a hit).
- No structural proof was found for k = 2^j + 2 (j ≥ 2). Writing GF(2^{2p}) = GF(2^p)(z_p) with p = 2^j, the condition S_{p+2} = 0 splits into two equations over GF(2^p) (the z_p-coefficient 1/z_{p−1} + 1/(α z_1) + z_2/(α + γ(z_2 + 1)) = 0, where z_{p+1} = α + z_1 z_p and z_{p+2} = γ + z_2 z_p, together with the constant term), and this run did not show they are incompatible.

#### Not a consequence

This subsection does not select W, does not state a continuum limit, a force, a stress, or a momentum, and does not claim that the computation or the trace test is new.

### Residue condition: lengths 2^j + 2 (relative-trace argument)

Dated 2026-10-08 (America/New_York), ninth run of the day. This subsection proves one more infinite family of lengths, k = 2^j + 2, which was left open by the eighth run. It does not change the smallest open length (47) or the exact range of h_n.

#### Assumptions

- Everything in the earlier residue subsections: chains z_0 = 1, z_i² + z_i = z_{i−1} over the algebraic closure of F_2, S_k = Σ_{i=1}^k 1/z_i, N(x) = x² + x = F + 1, E_a = ker N^{2^a} = GF(2^{2^a}), and z_i ∈ E_a if and only if i + 1 ≤ 2^a. Hence z_i has degree exactly 2^a over F_2 when 2^{a−1} ≤ i < 2^a (degrees of elements of the E_a tower are powers of two).
- The Galois action of the sixth run: for p = 2^j and i ≥ p, σ := F^p = N^p + 1 acts by σ(z_i) = z_i + z_{i−p}, and σ generates Gal(GF(2^{2p})/GF(2^p)).
- Elementary algebra in characteristic 2. No literature was opened this run, and no novelty is claimed.

S_W is not an input. No value of W is selected.

#### Derivation

Fix p = 2^j with j ≥ 2, so p + 2 ≤ 2p − 1 and every z_i with i ≤ p + 2 lies in GF(2^{2p}) = GF(2^p)(z_p). Write c = z_{p−1}, ω = z_1 (so ω² + ω = 1, ω³ = 1, 1 + ω = ω²) and ζ = z_2 (so ζ² + ζ = ω, ζ ∈ GF(16) \ GF(4)). Then c ∈ GF(2^p) has degree exactly p, and z_p² + z_p = c.

Step 1 (coordinates over GF(2^p)). For 0 ≤ i ≤ 2 put α_i := z_{p+i} + z_i z_p. Since σ(z_{p+i}) = z_{p+i} + z_i and σ(z_p) = z_p + 1, σ(α_i) = α_i, so α_i ∈ GF(2^p), and α_0 = 0. Expanding z_{p+i}² + z_{p+i} = z_{p+i−1} with z_p² = z_p + c and comparing coefficients of 1 and z_p gives
    α_i² + α_i = α_{i−1} + c z_i²,   so   α_1² + α_1 = ω² c,   α_2² + α_2 = α_1 + ζ² c.
In particular c = ω(α_1² + α_1), and α_1 ∉ {0, 1}.

Step 2 (relative norms and the z_p-coordinate of S). For x = a + b z_p with a, b ∈ GF(2^p), σ(x) = (a + b) + b z_p, Nm(x) := x σ(x) = a² + ab + b² c, and 1/x = σ(x)/Nm(x), so the z_p-coordinate of 1/x is b/Nm(x). This gives Nm(z_p) = c, Nm(z_{p+1}) = α_1² + ω α_1 + ω² c = ω² α_1 and Nm(z_{p+2}) = α_2² + ζ α_2 + ζ² c = α_1 + (1 + ζ) α_2. Since S_{p−1} ∈ GF(2^p), S_{p+2} = S_0' + C_1 z_p with S_0', C_1 ∈ GF(2^p) and
    C_1 = 1/c + ω/(ω² α_1) + ζ/(α_1 + (1 + ζ) α_2) = ω²/(α_1 + 1) + ζ/(α_1 + (1 + ζ) α_2),
using 1/c + ω²/α_1 = ω²/(α_1(α_1 + 1)) + ω²/α_1 = ω²/(α_1 + 1). Because {1, z_p} is a GF(2^p)-basis, S_{p+2} ∈ GF(2^p) if and only if C_1 = 0. This is the z_p-coefficient equation recorded without a conclusion in the eighth run.

Step 3 (C_1 = 0 forces α_1 into GF(16)). C_1 = 0 is linear in α_2: α_2 = λ α_1 + μ with λ = ω(ζ + ω²)/(1 + ζ) and μ = ωζ/(1 + ζ), both in GF(16). Substituting into α_2² + α_2 = α_1 + ζ²ω(α_1² + α_1) gives
    Q(α_1) := (λ² + ζ²ω) α_1² + (λ + 1 + ζ²ω) α_1 + (μ² + μ) = 0.
The linear coefficient vanishes: (1 + ζ²ω)(1 + ζ) = 1 + ζω = λ(1 + ζ), using ζ² = ζ + ω and ζ³ = ζ + ω + ωζ. The constant μ² + μ is nonzero, because μ = 0 would need ζ = 0 and μ = 1 would need ζ(1 + ω) = 1, that is ζ = ω ∈ GF(4). So either the leading coefficient A = λ² + ζ²ω is 0, and Q = μ² + μ has no root, or α_1² = (μ² + μ)/A ∈ GF(16), and then α_1 ∈ GF(16) because squaring is bijective on GF(16). In both cases a solution forces α_1 ∈ GF(16), hence c = ω(α_1² + α_1) ∈ GF(16).

Lemma (lengths 2^j + 2). For every j ≥ 3 and every chain, S_{2^j+2} ∉ GF(2^{2^j}); in particular S_{2^j+2} ≠ 0.

Proof. If S_{p+2} were in GF(2^p) (in particular, if it were 0), Steps 2 and 3 give c ∈ GF(16), so the degree of c divides 4. But c = z_{p−1} has degree p ≥ 8. Contradiction.

Together with k = 4 (a power of two) and k = 6 (finite check), S_k ≠ 0 for every k = 2^j + 2, j ≥ 1. The argument fails at p = 4 exactly where the data says it must: there c ∈ GF(16) is allowed, and the fifth run's count of 8 chains with S_6 ∈ GF(16) is reproduced below.

#### Exact finite verification (scripts/check_residue_p_plus_two.py)

In GF(2^64), for p = 4 and p = 8 on all chains of length p + 2, and for p = 16 on one chain per Frobenius orbit of length 18 (orbit lemma of the sixth run; membership in GF(2^p) is Frobenius-invariant), the script checks that α_1, α_2 ∈ GF(2^p), both Artin–Schreier relations of Step 1, the three norm formulas, both forms of C_1, that S_{p+2} = S_0' + C_1 z_p with S_0', C_1 ∈ GF(2^p), and that C_1 = 0 exactly when S_{p+2} ∈ GF(2^p). For each of the four choices of (z_1, z_2) it checks the substitution identity behind Q at random points, that the linear coefficient is 0 and μ² + μ ≠ 0 (both also proved above), and that A ≠ 0 (not needed for the lemma). Counts of chains with S_{p+2} ∈ GF(2^p): 8 for k = 6 (matching the fifth run), 0 for k = 10, 0 for k = 18, with α_1 ∈ GF(16) on every chain where C_1 = 0. These checks support the algebra; the lemma does not depend on them.

#### Corollary (status after this run)

- S_k ≠ 0 for every chain when 1 ≤ k ≤ 46 (computation), and when k ∈ {2^j, 2^j + 1, 2^j + 2} for any j (lemmas). The first lengths newly covered by a proof rather than computation are k = 66, 130, 258, ….
- The smallest open length stays 47, so the exact range is unchanged: h_n = 1 − μ_exc(n) − 5 · 2^n/(3^{n+1} + 3) for 3 ≤ n ≤ 48.

#### Remark (not proved): the same scheme for k = 2^j + m

For k = p + m with fixed m and p = 2^j > m, the same coordinates give α_1, …, α_m ∈ GF(2^p) with α_i² + α_i = α_{i−1} + c z_i², z_1, …, z_m in a fixed small field, and S_k ∈ GF(2^p) iff a single rational equation C_1(α_1, …, α_m) = 0 holds. If, for a given m, these m equations in m unknowns have only finitely many solutions over the algebraic closure, all solutions lie in a field of bounded degree, and the argument above would prove S_{p+m} ≠ 0 for all large j. Whether the system is zero-dimensional was not checked for any m ≥ 3, and the fifth run's data (S_k ∈ GF(2^p) for some chains at k = 11, 13, 14, 15) shows that small p can admit solutions. This is a proof strategy only; even for every fixed m it would not cover all k, since m ranges up to p − 1.

#### Still open

- Residue conjecture for k ≥ 47 with k ∉ {2^j, 2^j + 1, 2^j + 2}: Σ_{i=1}^k 1/z_i ≠ 0 for every chain, equivalently gcd(N^k + 1, Π_k′) = 1 in F_2[t]. Not proved, and no counterexample is known.
- Exact h_n for n ≥ 49 (it would follow from the conjecture; failure of the residue test would only remove this obstruction, not produce a hit).
- Zero-dimensionality of the C_1-system for k = 2^j + m, m ≥ 3 (see the remark).

#### Not a consequence

This subsection does not select W, does not state a continuum limit, a force, a stress, or a momentum, and does not claim that the relative-trace argument is new.

### Residue condition: lengths 2^j + m for 3 ≤ m ≤ 10 (elimination over a fixed field)

Dated 2026-10-08 (America/New_York), tenth run of the day. This subsection carries out, for 3 ≤ m ≤ 10, the strategy recorded as a remark (not proved) in the ninth run, and proves S_k ≠ 0 for every length k whose excess over the largest power of two not exceeding it is at most 10. It does not change the smallest open length (47) or the exact range of h_n.

#### Assumptions

- Everything in the earlier residue subsections: chains z_0 = 1, z_i² + z_i = z_{i−1}, S_k = Σ_{i=1}^k 1/z_i, N(x) = x² + x, z_i ∈ GF(2^{2^a}) iff i + 1 ≤ 2^a, so z_{p−1} has degree exactly p over F_2 when p = 2^j; the Galois action σ = F^p with σ(z_i) = z_i + z_{i−p} for p ≤ i (sixth and ninth runs); the Frobenius orbit lemma (sixth run).
- Step 1 and Step 2 of the ninth run, which hold verbatim for any 1 ≤ m ≤ p − 1: with c = z_{p−1} and α_i := z_{p+i} + z_i z_p ∈ GF(2^p) (0 ≤ i ≤ m, α_0 = 0), one has α_i² + α_i = α_{i−1} + c z_i², Nm(z_{p+i}) = α_i² + z_i α_i + z_i² c = (1 + z_i) α_i + α_{i−1}, and the z_p-coordinate of S_{p+m} is
    C_1 = z_1²/(α_1 + 1) + Σ_{i=2}^m z_i / ((1 + z_i) α_i + α_{i−1}),
  so S_{p+m} ∈ GF(2^p) iff C_1 = 0. All denominators are nonzero (each Nm(z_{p+i}) is the norm of a nonzero element, and α_1 = 1 would give c = 0).
- Elementary algebra in characteristic 2 and exact finite-field computation (python-flint 0.9.0). No literature was opened this run, and no novelty is claimed.

S_W is not an input. No value of W is selected.

#### Derivation

Fix m and put e = 2^⌈log2(m+1)⌉, so the prefix z_1, …, z_m lies in GF(2^e), and e ≤ p whenever p = 2^j > m.

Step 1 (a ring that does not depend on p). Over A_1 = GF(2^e)[x] build A_i = A_{i−1}[α_i]/(α_i² + α_i + β_i) with β_i = α_{i−1} + c z_i² and c := z_1(x² + x) (so that x plays α_1: z_1(α_1² + α_1) = z_1 · z_1² c = c because z_1³ = 1). Each A_i is free of rank 2 over A_{i−1}. Clearing denominators in C_1 gives
    G := z_1² ∏_{i=2}^m Nm_i + (x + 1) Σ_{i=2}^m z_i ∏_{l≠i} Nm_l ∈ A_m,   Nm_i = (1 + z_i) α_i + α_{i−1},
and C_1 = G / ((α_1 + 1) ∏ Nm_i).

Step 2 (norms specialize). For u = a + b α_l with a, b ∈ A_{l−1} put N_l(u) = a² + ab + b² β_l. The identity (a + b α)(a + b + b α) = a² + ab + b²(α² + α) holds whenever α² + α = β, so for any ring map φ: A_l → K into a field, φ(N_l(u)) = φ(u) · φ'(u) with φ' the map sending α_l to φ(α_l) + 1. Define R := N_2(N_3(⋯N_m(G)⋯)) ∈ GF(2^e)[x]. The actual chain values define φ: A_m → GF(2^p) with x ↦ α_1, α_i ↦ α_i, so C_1 = 0 at the chain gives φ(G) = 0 and hence R(α_1) = 0.

Lemma (elimination certificate). Fix m ≥ 2 and a prefix (z_1, …, z_m) with R ≠ 0. If p = 2^j > m and some chain of length p + m with this prefix has S_{p+m} ∈ GF(2^p), then α_1 is a root of an irreducible factor f of R over GF(2^e) of degree d with p = e·d, and N^{p−1−m}(z_1(x² + x)) ≡ z_m mod f.

Proof. α_1 ∈ GF(2^p) is a root of some irreducible factor f of degree d, so GF(2^e)(α_1) = GF(2^{ed}) ⊆ GF(2^p) (using GF(2^e) ⊆ GF(2^p)), hence ed | p. Also c = z_1(α_1² + α_1) ∈ GF(2^{ed}), and c = z_{p−1} has degree p, so p | ed. Thus p = ed (in particular d is a power of two). Finally N^{p−1−m}(z_{p−1}) = z_m along the chain, and this is a polynomial condition over GF(2^e) in α_1, so it holds modulo f. ∎

So for each fixed m, the set of p for which some chain has S_{p+m} ∈ GF(2^p) is contained in the finite set of e·d over surviving factors, and every S_{p+m} = 0 is in particular such a chain.

#### Exact finite computation (scripts/check_residue_p_plus_m.py)

Mode `filter m` computes R for every prefix (all 2^m prefixes for m ≤ 8; one per Frobenius orbit for m = 9, which gives the same set of p because Frobenius maps prefixes, R, factor degrees and the chain condition to conjugates), checks R ≠ 0, factors R over GF(2^e) and applies the chain condition. Surviving values of p:

| m | e | prefixes | deg R | surviving p |
|---|---|---|---|---|
| 2 | 4 | 4 | 2 | 4 |
| 3 | 4 | 8 | 6 | 8 |
| 4 | 8 | 16 | 14 | none |
| 5 | 8 | 32 | 30 | 8 |
| 6 | 8 | 64 | 62 | 8, 16, 32 |
| 7 | 8 | 128 | 126 | 8, 16, 32, 64, 256 |
| 8 | 16 | 256 | 254 | 16, 32, 64, 128, 256, 512 |
| 9 | 16 | 32 (orbit reps) | 510 | 16, 32, 64, 128, 256 |
| 10 | 16 | 64 (orbit reps) | 1022 | 16, 32, 64, 128, 256 |

(The m = 2 row reproduces the ninth run: only p = 4 survives. deg R = 2^m − 2 on every prefix checked through m = 11; see "Residue condition: degree of the elimination polynomial R" for the partial lemma / conjecture status. For m = 11 filter + directs through p = 128, see the following subsection; excess ≤ 11 is a theorem after the 2026-10-15 lifted completes.)

Mode `direct m P` enumerates, in GF(2^{2P}), every chain of length P + m whose α_1 is a root of R lying in GF(2^P) and whose c satisfies the chain condition; by the lemma this contains every chain with S_{P+m} ∈ GF(2^P), so its count of S = 0 is exact. Positive control: for k = 6, 7, 11, 12, 13, 14, 15 a naive enumeration of all 2^k chains gives 8, 0, 32, 0, 48, 32, 176 chains with S_k ∈ GF(2^p), equal to the `direct` counts (k = 6, 11, 13, 14, 15 are the fifth run's failures of the subfield test). Results of `direct` (this run, scripts/check_residue_p_plus_m.py): no chain has S = 0 at k = 13, 14, 15, 21, 22, 23, 38, 39, 71, 72, 73, 136, 137, 264. Supporting orbit-reduced counts from the same algorithm (scratch logs matching the overlapping lengths above): S = 0 also at k = 263, 265, 520, 74, 138, 266. In every case some chains have S ∈ GF(2^p) (nonzero), so the subfield test alone does not prove these lengths.

#### Theorem (lengths 2^j + m, 3 ≤ m ≤ 10)

For every j and every chain, S_k ≠ 0 when k = 2^j + m with 2^j > m and 3 ≤ m ≤ 10. More precisely, S_{p+m} ∉ GF(2^p) for every p = 2^j > m that is not in the surviving column of the table, and for every surviving pair (m, p) the exact `direct` count of chains with S_{p+m} = 0 is zero.

Proof. For p not in the surviving column, the lemma gives S_{p+m} ∉ GF(2^p), so S_{p+m} ≠ 0. The surviving p for 3 ≤ m ≤ 10 give a finite list of lengths; those ≤ 46 are covered by the eighth run, and the remaining ones (k = 71, 72, 73, 74, 136, 137, 138, 263, 264, 265, 266, 520) are covered by the exact `direct` counts above. ∎

With the earlier lemmas (m = 0, 1, 2), S_k ≠ 0 for every k with k − 2^⌊log2 k⌋ ≤ 10. The first lengths newly covered by a proof are 67–74, 131–138, 263–266, 520, ….

#### Pending

None for 3 ≤ m ≤ 10. Excess m = 11 is closed in the later subsections "Residue condition: excess m=11 (partial: filter + directs through p=128)" and "Residue condition: excess m=11, lifted form of `direct` (2026-10-15)" (theorem: excess ≤ 11).

#### Still open

- Residue conjecture for k ≥ 47 with k − 2^⌊log2 k⌋ ≥ 12: Σ_{i=1}^k 1/z_i ≠ 0 for every chain. Not proved, and no counterexample is known. The smallest open length stays 47 = 32 + 15, so exact h_n remains proved only for 3 ≤ n ≤ 48.
- A uniform version: the method needs, for each m, a nonzero R on every prefix and a finite surviving set; m ranges up to p − 1, so no fixed list of m covers all k.

#### Not a consequence

This subsection does not select W, does not state a continuum limit, a force, a stress, or a momentum, and does not claim that elimination by relative norms is new.

### Residue condition: excess m=11 (partial: filter + directs through p=128)

Dated 2026-10-09 (America/New_York), ~3:55am EDT / hourly locked-kernel routine (Phase A documentation). This subsection records the filter and directs through p = 128 for excess m = 11. Survivors p = 256, 512, 1024 were completed later by the lifted form (2026-10-15); excess ≤ 11 is now a theorem (see "Residue condition: excess m=11, lifted form of `direct` (2026-10-15)"). Range of exact h_n is unchanged.

#### Assumptions

- Everything in "Residue condition: lengths 2^j + m for 3 ≤ m ≤ 10 (elimination over a fixed field)": the elimination lemma (C_1 clears to G; iterated relative norm R ∈ GF(2^e)[x]; R ≠ 0 forces surviving p = e·d with the chain condition), the `filter` / `direct` modes of scripts/check_residue_p_plus_m.py, and the orbit reduction for prefixes / chains.
- Exact finite-field computation (python-flint). No literature opened this run; no novelty claimed.

S_W is not an input. No value of W is selected.

#### Exact finite computation (scripts/check_residue_p_plus_m.py)

Filter m=11 (orbit, e=16, prefixes=128): R ≠ 0 on every prefix, degR=2046. Power-of-two-degree factors (p: count) = {16: 259, 32: 64, 64: 37, 128: 12, 256: 7, 512: 5, 1024: 2}. Surviving chain condition (p: count) = {16: 66, 32: 24, 64: 21, 128: 6, 256: 5, 512: 3, 1024: 1}. Wall ≈ 1511 s. An independent filter agrees (R_zero=0, same survivor counts, ≈ 1551 s). Scratch: `/workspace/scratch-res/repo_filter_m11.log`, `indep_excess_filter_m11.log` (not vendored).

Mode `direct 11 P orbit` (exact S = 0 count among chains with S ∈ GF(2^P) on the admissible set):

| p | k = p+11 | adm_c | chains | S ∈ GF(2^p) | S = 0 | time (s) |
|---|---|---|---|---|---|---|
| 16 | 27 | 65 | 266240 | 132 | 0 | 520.5 |
| 32 | 43 | 48 | 196608 | 96 | 0 | 2905.9 |
| 64 | 75 | 84 | 344064 | 168 | 0 | 2842.3 |
| 128 | 139 | 48 | 196608 | 96 | 0 | 11769.0 |

All four EXIT:0. Scratch: `/workspace/scratch-res/repo_direct_m11_p{16,32,64,128}.log` (not vendored). In every completed case some chains have S ∈ GF(2^p) (nonzero), so the subfield test alone does not prove these lengths.

#### Pending (resolved 2026-10-15)

As of this 2026-10-09 write-up, directs at p=256, 512, 1024 were open. They were completed by the lifted form on 2026-10-15 (all S = 0 counts 0); see the next subsection. Excess ≤ 11 is a theorem there.

#### Still open

- Residue conjecture for k ≥ 47 with k − 2^⌊log2 k⌋ ≥ 12. Smallest open length still 47; exact h_n for 3 ≤ n ≤ 48 only.

#### Not a consequence

This subsection does not select W, does not state a continuum limit, a force, a stress, or a momentum.


### Residue condition: excess m=11, lifted form of `direct` (2026-10-15)

Dated 2026-10-15 (America/New_York), ~2:30am EDT / hourly locked-kernel routine; table and status updated ~3:37am EDT when p = 512 and p = 1024 finished. This subsection adds an equivalent, faster form of the `direct` count and records its controls and its m = 11 results. With both pending rows complete (S = 0 count 0), excess ≤ 11 is a **theorem** (see Status).

Why a new form: the box restarted (≈ 02:01 EDT this run, and earlier), killing the long `direct 11 256 orbit` run each time; its scratch log `repo_direct_m11_p256.log` never received a result. `direct` recomputes R over GF(2^(2p)) and scans its roots there; at p = 256 that is many hours.

#### Assumptions

- Everything in "Residue condition: lengths 2^j + m for 3 ≤ m ≤ 10 (elimination over a fixed field)", in particular: on a chain with S_{p+m} ∈ GF(2^p), α_1 is a root of R ∈ GF(2^e)[x] in GF(2^p), c = z_1(α_1² + α_1) = z_{p−1} has degree exactly p, and the chain condition N^(p−1−m)(c) = z_m holds.
- Exact finite-field arithmetic (python-flint 0.9.0). No literature opened; no novelty claimed. S_W is not an input. No value of W is selected.

#### Lemma (reduction used by scripts/check_residue_lifted.py)

1. Restriction to surviving factors. Since c ∈ GF(2^e)(α_1) has degree p, α_1 has degree exactly p/e over GF(2^e), so it is a root of an irreducible factor f of R over GF(2^e) with deg f = p/e; evaluation at a root of f is injective on GF(2^e)[x]/(f), so the chain condition at the root is equivalent to the condition modulo f that `filter` tests. Hence the chains counted by `direct` are exactly those attached to roots of the factors `filter` reports as surviving. R is therefore computed once over GF(2^e) and only surviving factors are mapped into GF(2^(2p)) by a field embedding GF(2^e) → GF(2^(2p)) (a root of the defining polynomial of GF(2^e)). The set of chains does not depend on the embedding up to a field automorphism, which preserves "S = 0" and "S ∈ GF(2^p)".
2. One root per factor. σ = Frobenius^e fixes GF(2^e) pointwise, hence the prefix z_1..z_m and the coefficients of f; it permutes the roots of the irreducible f transitively; it maps the chains attached to a root r (all chains with c = z_1(r² + r)) bijectively onto those attached to σ(r), because the chain relations are defined over F_2; and it maps S to σ(S). So S = 0 occurs on a chain attached to some root of f iff it occurs on one attached to any single root. Mode `rep` uses one root per surviving factor; mode `verify` uses every root and asserts the per-root counts agree within each factor.

Proof of both points: as stated; only the recorded elimination lemma and the Galois action are used.

#### Exact finite computation (scripts/check_residue_lifted.py)

`prepare 11` (orbit prefixes, e = 16, 128 prefixes, per-prefix cache so a restart resumes): R ≠ 0 on every prefix, deg R = 2046; power-of-two-degree factors and surviving chain-condition counts are identical to the 2026-10-09 `filter` line ({16: 66, 32: 24, 64: 21, 128: 6, 256: 5, 512: 3, 1024: 1}).

Positive controls of `lift` (mode `all`, chains deduplicated by c) against recorded `direct` counts (adm_c, chains, S ∈ GF(2^p), S = 0):

| case | `direct` (recorded) | `lift all` (this run) |
|---|---|---|
| m=3,4,5,6,7, p ≤ 32 (10 cases) | as printed | identical in all 10 |
| m=7, p=256 (k=263) | 32, 8192, 64, 0 | 32, 8192, 64, 0 |
| m=11, p=16 (k=27) | 65, 266240, 132, 0 | 65, 266240, 132, 0 |
| m=11, p=32 (k=43) | 48, 196608, 96, 0 | 48, 196608, 96, 0 |
| m=11, p=64 (k=75) | 84, 344064, 168, 0 | 84, 344064, 168, 0 |
| m=11, p=128 (k=139) | 48, 196608, 96, 0 | 48, 196608, 96, 0 (1170 s vs 11769 s) |
| m=8, p=512 (k=520) | 32, 16384, 64, 0 (orbit `direct`, 9069.6 s) | 32, 16384, 64, 0 (5704.8 s; added 2026-10-15 ~3:56am EDT) |

Equivariance check (`verify`, every root, no deduplication): m=7, p=32: per-root counts equal within each factor; m=11, p=32 (24 factors of degree 2): every root gives (4096 chains, 2 with S ∈ GF(2^p), 0 with S = 0).
m=11, p=64 (21 factors of degree 4): every root gives (4096, 2, 0).

m = 11 at the pending lengths (`rep`, one root per surviving factor):

| p | k = p+11 | surviving factors | roots used | chains | S ∈ GF(2^p) | S = 0 | time (s) |
|---|---|---|---|---|---|---|---|
| 256 | 267 | 5 | 5 | 20480 | 10 | 0 | 863.4 |
| 512 | 523 | 3 | 3 | 12288 | 6 | 0 | 4494.2 |
| 1024 | 1035 | 1 | 1 | 4096 | 2 | 0 | 3145.2 |

Scratch logs: `/workspace/scratch-res/lifted_*.log`, cache `lifted_m11.json.d/` (not vendored, prior practice).

#### Status for excess 11

- Exact finite computation: S_k ≠ 0 on every chain for every surviving p of m = 11, by the lemma above plus the `rep` / `direct` counts: k = 27, 43, 75, 139, 267, 523, 1035 (S = 0 count 0 in every case).
- **Theorem (excess ≤ 11).** For every j and every chain, S_k ≠ 0 when k = 2^j + m with 2^j > m and 0 ≤ m ≤ 11. More precisely: with the earlier lemmas for excess 0, 1, 2 and the elimination theorem for 3 ≤ m ≤ 10, it remains only to treat m = 11; the filter gives surviving p ∈ {16, 32, 64, 128, 256, 512, 1024}, and every corresponding `direct` / `lift rep` S = 0 count is zero. Proof structure identical to the m ≤ 10 theorem (elimination lemma + finite survivors + exact zeros).
- Unchanged range: smallest open length still 47 = 32 + 15 (excess 15); exact h_n for 3 ≤ n ≤ 48 only. Closing excess 11 does **not** move that range.
- Pending at 3:56am EDT, **resolved 2026-10-15 ~5:30am EDT** (zero S = 0 at k = 47; see "Residue condition: exact check to k = 47"): the unchanged Frobenius-reduced walk `scripts/residue_orbits_gf2_64.c` was started with KMAX = 47 (2^41 reduced chains in GF(2^64); `validate` at KMAX = 24 passed first). If it reports zero S = 0 at k = 47, the smallest open length becomes 48 and exact h_n extends to 3 ≤ n ≤ 49; until then the range stays 3 ≤ n ≤ 48. Scratch log `/workspace/scratch-res/repo_orbits_k47.log`.

#### Not a consequence

This subsection does not select W, does not state a continuum limit, a force, a stress, or a momentum.

### Residue condition: degree of the elimination polynomial R

Dated 2026-10-15 (America/New_York), ~3:26am EDT / hourly locked-kernel routine (Priority B). This subsection records a **partial lemma** and a **conjecture** about deg R for the elimination polynomial of scripts/check_residue_p_plus_m.py / check_residue_lifted.py. It does not select W. (Excess ≤ 11 was proved separately on this same run from the completed lifts.)

#### Assumptions

- Everything in "Residue condition: lengths 2^j + m for 3 ≤ m ≤ 10 (elimination over a fixed field)": the tower A_1 = GF(2^e)[x], A_i = A_{i−1}[α_i]/(α_i² + α_i + β_i), G ∈ A_m, R = N_2(⋯N_m(G)⋯) ∈ GF(2^e)[x], and e = 2^⌈log2(m+1)⌉.
- Exact finite-field arithmetic (python-flint). No literature opened; no novelty claimed.

#### Derivation (what is proved vs checked)

A_m is free of rank 2^{m−1} over A_1. The iterated relative norm R equals the determinant of multiplication-by-G as an A_1-linear endomorphism of A_m. Hence if every A_1-coefficient of G in the monomial α-basis has degree ≤ d, then deg R ≤ d · 2^{m−1}. This is a general upper bound only; the observed degree is much sharper.

Define the max A_1-coefficient degree of a tower element by reading all nested (a, b) components down to A_1. For the specific G of `eliminate`, exact checks give a rigid degree sequence under successive norms N_m, …, N_2:

- d_0 := max A_1-coeff degree of G equals m − 1;
- d_r = 2 d_{r−1} − (m − r − 1) for r = 1, …, m − 1;
- closed form for r ≥ 1: d_r = 2^{r+1} + m − r − 3, so d_{m−1} = 2^m − 2.

(The recurrence is an algebraic identity once the two bullets hold; it is not itself a proof that those bullets hold for every m.)

#### Exact finite computation

| claim | status | evidence |
|---|---|---|
| deg R = 2^m − 2 on every checked prefix | **theorem for m ≤ 13 (finite exact)** | all prefixes for 1 ≤ m ≤ 6 and orbit prefixes for m = 7, 8 (`filter` / instrumented `eliminate`); m = 9, 10, 11 orbit already recorded (deg R = 510, 1022, 2046); m = 12 orbit (256 prefixes) from `scripts/check_residue_lifted.py prepare 12` (2026-10-15, EXIT:0, deg R = 4094 on every prefix, `assert not R.is_zero()` passed). Independent `check_residue_p_plus_m.py filter 12 orbit` finished EXIT:0 at 09:42:26 EDT with the same degR=4094 and the same survivor dict (cross-check, not an input). m = 13 orbit (512 prefixes) from `scripts/check_degR_structure.py 13` (2026-10-15, EXIT:0 15:07:30 EDT, deg R = 8190 and R ≠ 0 on every prefix; single run, no independent m = 13 cross-check yet) |
| d_0 = m − 1 and the recurrence d_r = 2 d_{r−1} − (m − r − 1) (hence d_{m−1} = 2^m − 2) | **exact for 2 ≤ m ≤ 13 (finite exact)** | all prefixes 2 ≤ m ≤ 6; orbit prefixes m = 7, …, 13 (16, 16, 32, 64, 128, 256, 512 prefixes); `scripts/check_degR_structure.py M` (2026-10-15); zero mismatches; every prefix has exactly the predicted sequence (e.g. m = 12: [11, 12, 15, 22, 37, 68, 131, 258, 513, 1024, 2047, 4094] on all 256; m = 13: [12, 13, 16, 23, 38, 69, 132, 259, 514, 1025, 2048, 4095, 8190] on all 512) |
| R ∈ GF(2^e)[x²] (equivalently R′ = 0 in char 2) | **exact for 2 ≤ m ≤ 13 (finite exact)** | same prefixes and run; 0 prefixes with a nonzero odd-index coefficient; R ≠ 0 and deg R = 2^m − 2 rechecked on every prefix |

Supporting commands (light CPU; does not run heavy lifts): `scripts/check_residue_p_plus_m.py filter M` / `filter M orbit`; `scripts/check_degR_structure.py M [workers [cache_dir]]` (structural checks below).

#### Lemma (partial)

For every m with 1 ≤ m ≤ 13 and every prefix used by the recorded `filter` runs (for m = 12, the orbit prefixes of `prepare 12`; for m = 13, the 512 orbit prefixes of `chains(…, orbit=True)` run by `check_degR_structure.py 13`) (all 2^m prefixes when that was how `filter` was run; one Frobenius-orbit representative per prefix orbit when `orbit` was used), the elimination polynomial satisfies deg R = 2^m − 2 and R ≠ 0.

Proof. Finite exact computation as in the table; the m ≤ 10 nonzero claim and the m = 11 filter line were already recorded, and this run rechecked m ≤ 8 including the degree sequence. ∎

Addendum (2026-10-15 ~6:55am EDT): m = 12 added from `prepare 12` (same `eliminate` routine that reproduced the m = 11 filter survivor counts). This is a single exact run; the second, independent `filter 12 orbit` is a cross-check, not an input.

Addendum (2026-10-15 ~10:00am EDT): independent `filter 12 orbit` finished EXIT:0 at 09:42:26 EDT (e=16, prefixes=256, degR=4094, time=17334.6s); surviving chain condition (p: count)={16: 133, 32: 56, 64: 29, 128: 17, 256: 13, 512: 5, 2048: 1, 4096: 2}, matching `prepare 12` exactly.

Addendum (2026-10-15 ~2:15pm EDT, structural checks through m = 12). `scripts/check_degR_structure.py` runs the repo's `check_residue_p_plus_m.eliminate` unchanged on the same prefixes as `filter` (all 2^m for m ≤ 6, one per Frobenius orbit via `chains(…, orbit=True)` for m ≥ 7); the only change is a wrapper around `make_ring` that records, before N_m, d_0 = max GF(2^e)-degree over all nested (a, b) components of G down to A_1, and after each N_l (l = m, …, 2) the same max degree d_r of the result (r = m − l + 1). It counts (does not assert) mismatches against d_0 = m − 1, d_r = 2 d_{r−1} − (m − r − 1), d_{m−1} = deg R = 2^m − 2, R ≠ 0, and zero odd-index coefficients of R. Results (logs `/workspace/scratch-res/degR_structure_m2_11.log`, `/workspace/scratch-res/indep_degR_m12.log`):

| m | e | prefixes | observed sequence (d_0, …, d_{m−1}) on every prefix | mismatches | time |
|---|---|---|---|---|---|
| 2 | 4 | 4 (all) | [1, 2] | 0 | <0.1s |
| 3 | 4 | 8 (all) | [2, 3, 6] | 0 | <0.1s |
| 4 | 8 | 16 (all) | [3, 4, 7, 14] | 0 | <0.1s |
| 5 | 8 | 32 (all) | [4, 5, 8, 15, 30] | 0 | <0.1s |
| 6 | 8 | 64 (all) | [5, 6, 9, 16, 31, 62] | 0 | 0.2s |
| 7 | 8 | 16 (orbit) | [6, 7, 10, 17, 32, 63, 126] | 0 | 0.2s |
| 8 | 16 | 16 (orbit) | [7, 8, 11, 18, 33, 64, 127, 254] | 0 | 1.2s |
| 9 | 16 | 32 (orbit) | [8, 9, 12, 19, 34, 65, 128, 255, 510] | 0 | 5.0s |
| 10 | 16 | 64 (orbit) | [9, 10, 13, 20, 35, 66, 129, 256, 511, 1022] | 0 | 25.6s |
| 11 | 16 | 128 (orbit) | [10, 11, 14, 21, 36, 67, 130, 257, 512, 1023, 2046] | 0 | 225.3s |
| 12 | 16 | 256 (orbit) | [11, 12, 15, 22, 37, 68, 131, 258, 513, 1024, 2047, 4094] | 0 | 1402.6s CPU / 703.2s wall (2 workers), EXIT:0 14:10:15 EDT |
| 13 | 16 | 512 (orbit) | [12, 13, 16, 23, 38, 69, 132, 259, 514, 1025, 2048, 4095, 8190] | 0 | 6344.5s CPU / 3177.4s wall (2 workers, nice 10), EXIT:0 15:07:30 EDT (added ~3:10pm EDT run) |

"mismatches = 0" means all seven counters (d0, rec, closed, degR, Rzero, odd, len) are 0. An earlier scratch checker (`/workspace/scratch-res/indep_degR.py`, separate copy of the elimination, log `/workspace/scratch-res/indep_degR.log`) independently gave deg R exact, R ≠ 0 and no odd coefficients for m ≤ 11 (orbit for m ≥ 7); it is a cross-check, not an input. The orbit reduction is the one already used by `filter … orbit` / `prepare`: for m ≥ 7 the claims are on the orbit-representative prefixes, exactly as for deg R.

Hence, as finite exact statements on the recorded prefixes: for 2 ≤ m ≤ 12, d_0 = m − 1, the recurrence holds at every step, and R ∈ GF(2^e)[x²]. No m = 13 claim: `check_degR_structure.py 13` (512 orbit prefixes, cache `/workspace/scratch-res/degR_structure_m13.d`, log `/workspace/scratch-res/degR_structure_m13.log`) was started at ~2:12pm EDT and was still running at write-up; the partial `prepare 13` cache is not used.

Addendum (2026-10-15 ~3:10pm EDT, m = 13). `check_degR_structure.py 13 2 /workspace/scratch-res/degR_structure_m13.d` finished EXIT:0 at 15:07:30 EDT: `degR-structure m=13 e=16 orbit=True prefixes=512 (computed this call: 512) expected_seq=[12, 13, 16, 23, 38, 69, 132, 259, 514, 1025, 2048, 4095, 8190] observed_seqs={[12, 13, 16, 23, 38, 69, 132, 259, 514, 1025, 2048, 4095, 8190]: 512} degR=[8190] mismatches={'d0': 0, 'rec': 0, 'closed': 0, 'degR': 0, 'Rzero': 0, 'odd': 0, 'len': 0} sum_prefix_time=6344.5s wall=3177.4s`. Hence the three finite exact statements (deg R = 2^m − 2 with R ≠ 0; d_0 = m − 1 with the recurrence; R ∈ GF(2^e)[x²]) now hold for 2 ≤ m ≤ 13 on the recorded prefixes (orbit representatives for m ≥ 7). For m = 13 this is a single run of the repo's unchanged `eliminate`; `prepare 13` (same routine, still running, not used) would be a second run, not an independent method. Nothing about excess m = 13 survivors (power-of-two factors of R) is claimed: this script does not factor R.

#### Conjecture (open)

For every m ≥ 2 and every admissible chain prefix in GF(2^e) with e = 2^⌈log2(m+1)⌉, deg R = 2^m − 2 (open for m ≥ 14). Stronger form (checked for 2 ≤ m ≤ 13): d_0 = m − 1 and the norm recurrence above hold for every m, and R ∈ GF(2^e)[x²]. (The stronger form implies deg R = 2^m − 2; the converse is not claimed.) No counterexample is known; a uniform proof is not claimed.

#### Still open

- A proof of d_0 = m − 1 and of the leading-term cancellation that produces d_r = 2 d_{r−1} − (m − r − 1) for general m (the crude determinant bound with d = m − 1 only gives deg R ≤ (m − 1) 2^{m−1}). Checked exactly (zero mismatches) for 2 ≤ m ≤ 13 only.
- Whether R ∈ GF(2^e)[x²] for all m (checked exactly for 2 ≤ m ≤ 13; no structural reason recorded).
- m = 13 was closed for the structural checks at ~3:10pm EDT (512/512 orbit prefixes, zero mismatches). Still open at m = 13: the excess-13 survivor filter (factorisation of R into power-of-two-degree factors) and any S_{p+13} lifts; `prepare 13` still running.
- m ≥ 14: nothing checked.

#### Not a consequence

This subsection does not select W, does not state a continuum limit, a force, a stress, or a momentum, and does not claim that deg R = 2^m − 2 is a classical theorem.

### Residue condition: exact check to k = 47 (2026-10-15)

Dated 2026-10-15 (America/New_York), ~5:30am EDT / hourly locked-kernel routine. This subsection adds one length to the exact finite check. It proves no new infinite family.

#### Assumptions

- Everything in "Residue condition: Frobenius orbit reduction and exact check to k = 45" and "exact check to k = 46": chains z_0 = 1, z_i² + z_i = z_{i−1}, S_k = Σ_{i=1}^k 1/z_i, the orbit lemma, and the fact that every chain of length k ≤ 63 lies in GF(2^64).
- The two-adic reduction theorem: a coincidental hit at level n ≥ 3 needs some k with 1 ≤ k ≤ n − 2, n − k even, and a chain with S_k = 0.
- No literature was opened this run, and no novelty is claimed. S_W is not an input. No value of W is selected.

#### Exact finite verification (1 ≤ k ≤ 47)

The unchanged program scripts/residue_orbits_gf2_64.c (no diff against the committed source; a fresh `gcc -O3 -march=native -fopenmp` build is byte-identical to the binary that ran, sha256 1b35db9d…f451) was run with KMAX = 47 (`validate` at KMAX = 24 passed first). It printed `ok` with zeros = 0 at every depth 1 ≤ k ≤ 47, with exactly 2^{k−⌈log₂(k+1)⌉} reduced chains at each depth; at k = 47 that is `reduced_chains=2199023255552` (= 2^41), orbit size 64, covering all 2^47 chains. Exit status 0; wall time 93 min 48 s, 374.7 user CPU-minutes (the box was shared with other jobs). Last line of the log at 05:29:51 EDT. Scratch log `/workspace/scratch-res/repo_orbits_k47.log` (not vendored, prior practice).

- Supporting only (not an input): an independent sampled walk (`/workspace/scratch-res/indep_orbits_sample.c`, stride 64 over reduced chains, offsets 0, 37, 63; finished 06:01–06:06 EDT) also reports zeros = 0 at every k ≤ 47 (2^35 nodes per offset at k = 47). It covers 3/64 of the reduced chains and is a consistency check of the full walk, not a second proof.

#### Corollary (theorem plus finite exact computation)

S_k ≠ 0 for every chain when 1 ≤ k ≤ 47, and (by the recorded theorems) whenever k − 2^⌊log2 k⌋ ≤ 11. The smallest open length is now k = 48 = 32 + 16 (excess 16). A coincidental hit at level n needs an open k ≤ n − 2 with n − k even. For n = 49 that would be an odd k ≤ 47, and none is open, so a hit needs n ≥ 50. Hence for 3 ≤ n ≤ 49 there are no coincidental hits, and
    h_n = 1 − μ_exc(n) − 5 · 2^n/(3^{n+1} + 3)   exactly.
This extends the previous range 3 ≤ n ≤ 48 by one level. For n = 50 the open even length k = 48 is not excluded, so the range stops at 49.

#### Still open

- Residue conjecture for k ≥ 48 with k − 2^⌊log2 k⌋ ≥ 12. Next open lengths: 48, 49, …, 63 (excess 16–31); among excess-12 lengths, k = 76, 140, 268, and 524 are already certified S ≠ 0 (see excess m = 12 Progress), with k = 2060 and 4108 still pending certification toward excess ≤ 12 (not claimed).
- Exact h_n for n ≥ 50.
- Pending at 9:05am EDT, **resolved 2026-10-15 ~4:28pm EDT** (zero S = 0 at k = 48; see "Residue condition: exact check to k = 48 (2026-10-15)"): the unchanged reduced walk `scripts/residue_orbits_gf2_64.c` was started with KMAX = 48 (`validate` at KMAX = 24 passed; binary `/workspace/scratch-res/walk48` byte-identical to walk47, sha256 1b35db9d…f451; log `/workspace/scratch-res/repo_orbits_k48.log`, start 09:05:49 EDT; OMP_NUM_THREADS = 2) and finished EXIT:0 at 16:28:53 EDT. Exact h_n for n = 50 is now proved there; the two items above are superseded by its "Still open" list (k ≥ 49; n ≥ 51).

#### Not a consequence

This subsection does not select W, does not state a continuum limit, a force, a stress, or a momentum, and does not claim that the computation is new.

### Residue condition: excess m = 12 (partial: elimination + survivors; lifts pending)

Dated 2026-10-15 (America/New_York), ~6:55am EDT / hourly locked-kernel routine. Same method as "Residue condition: excess m=11, lifted form of `direct` (2026-10-15)". This subsection does **not** prove excess ≤ 12.

#### Assumptions

- The elimination lemma and the lifted-`direct` lemma recorded for m ≤ 11 (no new assumption). e = 16 for m = 12 (e = 2^⌈log2 13⌉).
- Exact finite-field arithmetic (python-flint). No literature opened; no novelty claimed.

#### Exact finite computation

`scripts/check_residue_lifted.py prepare 12 /workspace/scratch-res/lifted_m12.json` finished EXIT:0 at 06:01:38 EDT (256 orbit prefixes; 192 computed in the final call after a resumed cache; 1776.0 s for that call):

- R ≠ 0 on every prefix (the script asserts this), deg R = 4094 = 2^12 − 2 on every prefix.
- Power-of-two-degree factors (p: count) = {16: 512, 32: 111, 64: 60, 128: 27, 256: 17, 512: 7, 2048: 1, 4096: 2, 8192: 1}.
- Surviving chain condition (p: count) = {16: 133, 32: 56, 64: 29, 128: 17, 256: 13, 512: 5, 2048: 1, 4096: 2}. No factor survives at p = 1024 or p = 8192.

Consequence of the elimination lemma (proved): for m = 12, S_{p+12} ∉ GF(2^p), hence S_{p+12} ≠ 0, for every power of two p > 12 outside {16, 32, 64, 128, 256, 512, 2048, 4096}. In particular S_k ≠ 0 for k = 1036 (p = 1024) and k = 8204 (p = 8192), and for every k = 2^j + 12 with 2^j ≥ 16384.

#### Pending (not claimed)

Exact `lift rep` zero counts at the eight surviving lengths k = 28, 44, 76, 140, 268, 524, 2060, 4108. Runs started 06:54 EDT (logs `/workspace/scratch-res/lifted_rep_m12_p{P}.log`). As of ~12:02pm EDT, finished with S = 0 count 0 at k = 28, 44, 76, 140, 268, 524; still pending k = 2060 (running) and k = 4108 (queued after 2048, not live). Excess ≤ 12 becomes a theorem only when every one of them reports S = 0 count 0. Note k = 28 and k = 44 are already covered by the reduced walk (k ≤ 47), so those two serve as controls.

#### Progress (2026-10-15 ~7:58am EDT, hourly routine; still not claimed as excess ≤ 12)

Exact `lift rep` results that have finished (EXIT:0, logs `/workspace/scratch-res/lifted_rep_m12_p{P}.log`):

| k | p | surviving factors | chains examined | S ∈ GF(2^p) | S = 0 | time |
|---|---|---|---|---|---|---|
| 28 | 16 | 133 | 1089536 | 270 | 0 | 352.5 s |
| 44 | 32 | 56 | 458752 | 112 | 0 | 779.7 s |
| 76 | 64 | 29 | 237568 | 58 | 0 | 420.9 s |
| 140 | 128 | 17 | 139264 | 34 | 0 | 855.1 s |

- k = 28 and k = 44 agree with the reduced walk (S_k ≠ 0 for k ≤ 47): controls, no new length.
- Finite exact computation + elimination/lifted-`direct` lemmas: S_76 ≠ 0 and S_140 ≠ 0 for every chain. Neither is the smallest open length 48, so the h_n range is unchanged.
- Still running at 7:58am EDT: k = 268 (p = 256, restarted 07:53), k = 524 (p = 512) and k = 2060 (p = 2048) since 07:13; k = 4108 (p = 4096) queued after 2048. Excess ≤ 12 remains **pending** until those four report S = 0 count 0.
- Status check 2026-10-15 ~9:05am EDT (hourly routine): p = 256, 512, 2048 still running (logs hold only start timestamps; no S = 0 line yet); `filter 12 orbit` still empty; p = 4096 not started (CPU). Excess ≤ 12 still **not** claimed. Separately, the KMAX = 48 reduced walk was started (see "exact check to k = 47" Still open); it does not close excess 12.

#### Progress (2026-10-15 ~10:00am EDT, hourly routine; still not claimed as excess ≤ 12)

Independent filter cross-check finished EXIT:0 at 09:42:26 EDT (`/workspace/scratch-res/repo_filter_m12.log`):

- `filter m=12 e=16 prefixes=256 degR=4094` power-of-two-degree factors (p: count)={16: 512, 32: 111, 64: 60, 128: 27, 256: 17, 512: 7, 2048: 1, 4096: 2, 8192: 1}; surviving chain condition (p: count)={16: 133, 32: 56, 64: 29, 128: 17, 256: 13, 512: 5, 2048: 1, 4096: 2}; time=17334.6s. Matches `prepare 12` survivors exactly (including p = 4096: 2). Cross-check only; not an input to the deg R lemma.

Exact `lift rep` at k = 268 finished EXIT:0 at 09:24:33 EDT (`/workspace/scratch-res/lifted_rep_m12_p256.log`):

| k | p | surviving factors | chains examined | S ∈ GF(2^p) | S = 0 | time |
|---|---|---|---|---|---|---|
| 268 | 256 | 13 | 106496 | 26 | 0 | 6578.3 s |

- Finite exact computation + elimination/lifted-`direct` lemmas: S_268 ≠ 0 for every chain.
- As of that write-up, still pending toward excess ≤ 12: k = 524 (p = 512) and k = 2060 (p = 2048) `lift rep` still running; k = 4108 (p = 4096) not started. (Superseded for k = 524 by the ~12:02pm Progress below.)

#### Progress (2026-10-15 ~12:02pm EDT, hourly routine; still not claimed as excess ≤ 12)

Exact `lift rep` at k = 524 finished EXIT:0 at 11:50:52 EDT (`/workspace/scratch-res/lifted_rep_m12_p512.log`):

| k | p | surviving factors | chains examined | S ∈ GF(2^p) | S = 0 | time |
|---|---|---|---|---|---|---|
| 524 | 512 | 5 | 40960 | 10 | 0 | 17764.6 s |

- Finite exact computation + elimination/lifted-`direct` lemmas: S_524 ≠ 0 for every chain.
- Still pending toward excess ≤ 12: k = 2060 (p = 2048) `lift rep` still running (pid ~261337); k = 4108 (p = 4096) **queued** sequentially behind p2048 via existing parent `run 2048 4096` (pid ~261330) — not live yet; no parallel duplicate started under load. Excess ≤ 12 still **not** claimed.
- walk48 (KMAX = 48) still running (pid ~348412; log holds only start timestamp). Range unchanged. (Superseded: walk48 finished EXIT:0 at 16:28:53 EDT with zeros = 0 at every k ≤ 48; see "exact check to k = 48".)

#### Range

Unchanged: smallest open length 48 = 32 + 16; exact h_n for 3 ≤ n ≤ 49. Closing excess 12 would not move that range (48 has excess 16).

Update (2026-10-15 ~4:30pm EDT): moved by the reduced walk, not by excess 12. After the KMAX = 48 walk (see "exact check to k = 48"), the smallest open length is 49 = 32 + 17 and exact h_n holds for 3 ≤ n ≤ 50. Closing excess 12 would still not move that range (49 has excess 17).

#### Not a consequence

Does not select W; no continuum limit, force, stress, or momentum.

### Residue condition: exact check to k = 48 (2026-10-15)

Dated 2026-10-15 (America/New_York), ~4:28–5:00pm EDT / locked-kernel routine. This subsection adds one length to the exact finite check. It proves no new infinite family.

#### Assumptions

- Everything in "Residue condition: Frobenius orbit reduction and exact check to k = 45", "exact check to k = 46" and "exact check to k = 47": chains z_0 = 1, z_i² + z_i = z_{i−1}, S_k = Σ_{i=1}^k 1/z_i, the orbit lemma, and the fact that every chain of length k ≤ 63 lies in GF(2^64).
- The two-adic reduction theorem: a coincidental hit at level n ≥ 3 needs some k with 1 ≤ k ≤ n − 2, n − k even, and a chain with S_k = 0.
- No literature was opened this run, and no novelty is claimed. S_W is not an input. No value of W is selected.

#### Exact finite verification (1 ≤ k ≤ 48)

The unchanged program scripts/residue_orbits_gf2_64.c (no diff against the committed source since 172f122; a fresh `gcc -O3 -march=native -fopenmp` build is byte-identical to the binary that ran, `/workspace/scratch-res/walk48`, sha256 1b35db9d…f451, the same binary as walk47) was run with KMAX = 48 (`validate` at KMAX = 24 passed first, `/workspace/scratch-res/repo_orbits_k48_validate.log`). It printed `ok` with zeros = 0 at every depth 1 ≤ k ≤ 48, with exactly 2^{k−⌈log₂(k+1)⌉} reduced chains and orbit size 2^{⌈log₂(k+1)⌉} at each depth (checked line by line against the log); at k = 48 that is `reduced_chains=4398046511104` (= 2^42), orbit size 64, covering all 2^48 chains. Exit status 0; start 09:05:49 EDT, last line 16:28:53 EDT, wall about 7 h 23 min with OMP_NUM_THREADS = 2 (the box was shared with the m = 12 lifts and `prepare 13`; no CPU-time line was recorded). Scratch log `/workspace/scratch-res/repo_orbits_k48.log` (not vendored, prior practice).

- No independent sampled walk was run at k = 48. The k = 47 sampled consistency check is not extended here.

#### Corollary (theorem plus finite exact computation)

S_k ≠ 0 for every chain when 1 ≤ k ≤ 48, and (by the recorded theorems) whenever k − 2^⌊log2 k⌋ ≤ 11. The smallest open length is now k = 49 = 32 + 17 (excess 17). A coincidental hit at level n needs an open k ≤ n − 2 with n − k even. For n = 50 that would be an even k ≤ 48, and none is open, so a hit needs n ≥ 51. Hence for 3 ≤ n ≤ 50 there are no coincidental hits, and
    h_n = 1 − μ_exc(n) − 5 · 2^n/(3^{n+1} + 3)   exactly.
This extends the previous range 3 ≤ n ≤ 49 by one level. For n = 51 the open odd length k = 49 is not excluded, so the range stops at 50.

#### Still open

- Residue conjecture for k ≥ 49 with k − 2^⌊log2 k⌋ ≥ 12. Next open lengths: 49, 50, …, 63 (excess 17–31); among excess-12 lengths, k = 76, 140, 268, and 524 are already certified S ≠ 0 (see excess m = 12 Progress), with k = 2060 (`lift rep` p = 2048 still running, no S = 0 line yet) and k = 4108 (queued behind it, not live) still pending. Excess ≤ 12 is **not** claimed.
- Exact h_n for n ≥ 51.
- deg R = 2^m − 2 (and the d_0 / recurrence / evenness checks) unchanged: exact for 2 ≤ m ≤ 13, conjecture for m ≥ 14. `prepare 13` still running (~147/512 orbit prefixes cached at ~4:57pm EDT); not used.
- No KMAX = 49 walk was started this run (CPU in use by `lift rep` p = 2048 and the `prepare 13` workers).

#### Not a consequence

This subsection does not select W, does not state a continuum limit, a force, a stress, or a momentum, and does not claim that the computation is new.

### Residue condition: exact check to k = 49 (2026-10-22)

Dated 2026-10-22 (America/New_York), ~9:55am EDT / locked-kernel routine. This subsection adds one length to the exact finite check. It proves no new infinite family.

#### Assumptions

- Everything in "Residue condition: Frobenius orbit reduction and exact check to k = 45" and the exact checks to k = 46, 47, 48: chains z_0 = 1, z_i² + z_i = z_{i−1}, S_k = Σ_{i=1}^k 1/z_i, the orbit lemma, and the fact that every chain of length k ≤ 63 lies in GF(2^64).
- The two-adic reduction theorem: a coincidental hit at level n ≥ 3 needs some k with 1 ≤ k ≤ n − 2, n − k even, and a chain with S_k = 0.
- No literature was opened this run, and no novelty is claimed. S_W is not an input. No value of W is selected.

#### Exact finite verification (1 ≤ k ≤ 49)

The unchanged program scripts/residue_orbits_gf2_64.c (no diff against the committed source since 172f122) was run with KMAX = 49 using the same binary as walk47 and walk48 (`/workspace/scratch-res/walk48`, sha256 1b35db9d…f451), OMP_NUM_THREADS = 4. It printed `ok` with zeros = 0 at every depth 1 ≤ k ≤ 49 (49 `ok` lines), with exactly 2^{k−⌈log₂(k+1)⌉} reduced chains, orbit size 2^{⌈log₂(k+1)⌉} and chains_covered = 2^k at each depth (checked line by line by a script against the log, zero mismatches); at k = 49 that is `reduced_chains=8796093022208` (= 2^43), orbit size 64, covering all 2^49 chains. Exit status 0; start 00:56:27 EDT, last line 08:51:41 EDT, wall about 7 h 55 min on a box shared with `lift rep` p = 2048 and `prepare 13`. Scratch log `/workspace/scratch-res/walk49.log` (not vendored, prior practice).

- `validate` was not re-run before this walk; the KMAX = 24 validation of this same binary (`/workspace/scratch-res/repo_orbits_k48_validate.log`) is relied on.
- No independent sampled walk was run at k = 49.

#### Corollary (theorem plus finite exact computation)

S_k ≠ 0 for every chain when 1 ≤ k ≤ 49, and (by the recorded theorems) whenever k − 2^⌊log2 k⌋ ≤ 11. The smallest open length is now k = 50 = 32 + 18 (excess 18). A coincidental hit at level n needs an open k ≤ n − 2 with n − k even. For n = 51 that would be an odd k ≤ 49, and none is open, so a hit needs n ≥ 52. Hence for 3 ≤ n ≤ 51 there are no coincidental hits, and
    h_n = 1 − μ_exc(n) − 5 · 2^n/(3^{n+1} + 3)   exactly.
This extends the previous range 3 ≤ n ≤ 50 by one level. For n = 52 the open even length k = 50 is not excluded, so the range stops at 51.

#### Still open

- Residue conjecture for k ≥ 50 with k − 2^⌊log2 k⌋ ≥ 12. Next open lengths: 50, 51, …, 63 (excess 18–31); excess-12 lengths k = 2060 (`lift rep` p = 2048 running since 2026-10-22 00:58 EDT, no result line) and k = 4108 (not started) still pending. Excess ≤ 12 is **not** claimed.
- Exact h_n for n ≥ 52.
- deg R = 2^m − 2 (and the d_0 / recurrence / evenness checks): exact for 2 ≤ m ≤ 13, conjecture for m ≥ 14. `prepare 13` still running (507/512 orbit prefixes cached at ~9:55am EDT); not used.
- A KMAX = 50 walk would cost roughly twice this wall time (order 16 h at the same load); not started this run.

#### Not a consequence

This subsection does not select W, does not state a continuum limit, a force, a stress, or a momentum, and does not claim that the computation is new.

### Residue condition: excess m = 13 (elimination + survivors; lifts pending)

Dated 2026-10-22 (America/New_York), ~10:55am EDT / locked-kernel routine. Same method as the m = 11 and m = 12 subsections. This subsection does **not** prove excess ≤ 13 (excess 12 itself is still pending at k = 2060, 4108).

#### Assumptions

- The elimination lemma and the lifted-`direct` lemma already recorded (no new assumption). e = 16 for m = 13 (e = 2^⌈log2 14⌉).
- Exact finite-field arithmetic (python-flint 0.9.0). The per-prefix cache was built in two sessions (217 prefixes before the 2026-10-22 box restart, 295 after); each cached entry is the exact output for its prefix and was reused unchanged.
- No literature opened; no novelty claimed. No value of W is selected.

#### Exact finite computation

`scripts/check_residue_lifted.py prepare 13 /workspace/scratch-res/lifted_m13.json 2` finished EXIT:0 at 10:03:05 EDT 2026-10-22 (512 orbit prefixes; 295 computed in the final call, 32756.2 s for that call). Log `/workspace/scratch-res/lifted_prepare_m13.log` (not vendored).

- R ≠ 0 on every prefix (asserted by the script), deg R = 8190 = 2^13 − 2 on every prefix. This agrees with the independent `check_degR_structure.py 13` run of 2026-10-15 (same 512 prefixes), so deg R = 2^13 − 2 now has two runs.
- Power-of-two-degree factors (p: count) = {16: 962, 32: 238, 64: 110, 128: 60, 256: 27, 512: 19, 1024: 17, 2048: 3, 8192: 1, 16384: 1}.
- Surviving chain condition (p: count) = {16: 246, 32: 128, 64: 62, 128: 22, 256: 18, 512: 7, 1024: 12, 2048: 1, 8192: 1}. No factor survives at p = 4096 or p = 16384.

Consequence of the elimination lemma (proved): for m = 13, S_{p+13} ∉ GF(2^p), hence S_{p+13} ≠ 0, for every power of two p > 13 outside {16, 32, 64, 128, 256, 512, 1024, 2048, 8192}. In particular S_k ≠ 0 for k = 4109 (p = 4096), k = 16397 (p = 16384), and every k = 2^j + 13 with 2^j ≥ 32768.

#### Pending (not claimed)

Exact `lift rep` zero counts at the nine surviving lengths k = 29, 45, 77, 141, 269, 525, 1037, 2061, 8205. Started this run (~10:54 EDT, nice 10) as four parallel jobs p = 16, 32, 64, 128; the p = 16 job was killed by the kernel out-of-memory handler at 11:14 EDT (EXIT:137, no result line), so p = 64 and 128 were stopped and requeued to run one at a time (p = 16, 64, 128) after p = 32 finishes. Logs `/workspace/scratch-res/lifted_rep_m13_p{P}.log`. Nothing is inferred from the killed runs. k = 29 and k = 45 are already covered by the reduced walk (k ≤ 49) and act as controls. The p ≥ 256 lifts are not started; by the recorded cost ratio (~7 per doubling of p) p = 2048 and p = 8192 are out of reach on this box by this route. Excess ≤ 13 becomes a theorem only when excess ≤ 12 is closed and all nine report S = 0 count 0.

Addendum (2026-10-22 ~11:57am EDT, control k = 45). The p = 32 `lift rep` job (`check_residue_lifted.py lift /workspace/scratch-res/lifted_m13.json 32 rep`, started 10:54:22 EDT) finished EXIT:0 at 11:42:53 EDT: `lift[rep] k=45 (p=32, m=13, orbit reps): surviving factors=128, roots used=128, chains examined=2097152, with S in GF(2^p)=256, with S = 0: 0, time=2910.7s`. Every one of the 128 surviving factors reports (16384 chains, 2 with S in GF(2^32), 0 with S = 0). This is a finite exact cross-check, not a new theorem: S_45 ≠ 0 was already proved by the reduced walk (k ≤ 49), and the zero count 0 agrees with it. The p = 16 job (k = 29, also a control) restarted sequentially at 11:43:15 EDT; p = 64 (k = 77) and p = 128 (k = 141) are queued after it. No result for k = 77 or 141 yet.

Addendum (2026-10-22 ~12:55pm EDT, k = 29 control and k = 77). Both sequential `lift rep` jobs finished EXIT:0 (logs `/workspace/scratch-res/lifted_rep_m13_p16.log`, `/workspace/scratch-res/lifted_rep_m13_p64.log`):

| k | p | surviving factors | chains examined | S ∈ GF(2^p) | S = 0 | time | finished |
|---|---|---|---|---|---|---|---|
| 29 | 16 | 246 | 4030464 | 530 | 0 | 1227.4 s | 12:03:43 EDT |
| 77 | 64 | 62 | 1015808 | 124 | 0 | 1646.8 s | 12:31:10 EDT |

- k = 29 is a control: S_29 ≠ 0 was already proved by the reduced walk (k ≤ 49); zero count 0 agrees.
- k = 77 = 64 + 13 is outside the walk range. Finite exact computation + elimination/lifted-`direct` lemmas (same reading as the recorded m = 12 lifts): **S_77 ≠ 0 for every chain.** This is an isolated length; it does not move the contiguous range (smallest open length stays 50, excess 18).
- p = 128 (k = 141) started 12:31:10 EDT, running; p ≥ 256 (k = 269, 525, 1037, 2061, 8205) not started. Excess ≤ 13 still **not** claimed.

Addendum (2026-10-22 ~1:58pm EDT, k = 141). The p = 128 `lift rep` job finished EXIT:0 at 13:16:17 EDT (log `/workspace/scratch-res/lifted_rep_m13_p128.log`): `lift[rep] k=141 (p=128, m=13, orbit reps): surviving factors=22, roots used=22, chains examined=360448, with S in GF(2^p)=44, with S = 0: 0, time=2706.6s`; every factor reports (16384, 2, 0).

- k = 141 = 128 + 13 is outside the walk range. Finite exact computation + elimination/lifted-`direct` lemmas: **S_141 ≠ 0 for every chain.** Isolated length; the contiguous range does not move (smallest open length stays 50).
- p = 256 (k = 269) started 13:58 EDT, running; p = 512, 1024, 2048, 8192 (k = 525, 1037, 2061, 8205) not started. Excess ≤ 13 still **not** claimed.

Addendum (2026-10-22 ~8:50pm EDT, k = 269). After the SIGTERM at 14:20:50 EDT and restart, the p = 256 `lift rep` job finished EXIT:0 at 20:24:48 EDT (log `/workspace/scratch-res/lifted_rep_m13_p256.log`): `lift[rep] k=269 (p=256, m=13, orbit reps): surviving factors=18, roots used=18, chains examined=294912, with S in GF(2^p)=36, with S = 0: 0, time=19687.4s`; every factor reports (16384, 2, 0).

- k = 269 = 256 + 13 is outside the walk range. Finite exact computation + elimination/lifted-`direct` lemmas: **S_269 ≠ 0 for every chain.** Isolated length; the contiguous range does not move (smallest open length stays 50).
- p = 512 (k = 525) started 20:50 EDT (log `/workspace/scratch-res/lifted_rep_m13_p512.log`), running; p = 1024, 2048, 8192 (k = 1037, 2061, 8205) not started. Excess ≤ 13 still **not** claimed.

#### Not a consequence

This subsection does not select W, does not state a continuum limit, a force, a stress, or a momentum, and does not claim that the computation is new.

---

<div align="center">

**REWRITE · BUILD · TRANSCEND**

**William (Brian) Ware** · [Atomic Dream Labs](https://github.com/beyond-repair)  
Governing source: [ADL-Governance](https://github.com/beyond-repair/ADL-Governance) · [Claim levels 0–5](https://github.com/beyond-repair/ADL-Governance/blob/main/docs/CLAIM_VALIDATION.md)

</div>

Addendum (2026-10-22 ~2:57pm EDT, no new result). Both running lift jobs, m = 13 p = 256 (k = 269, started 13:58 EDT) and m = 12 p = 2048 (k = 2060, restarted 00:58 EDT), received SIGTERM at 14:20:50 EDT (EXIT:143) and produced no result. No statement about S_269 or S_2060 is made. Both were restarted at 14:56 EDT with the same command (`check_residue_lifted.py lift <json> <p> rep`, python-flint 0.9.0), logs appended to `/workspace/scratch-res/lifted_rep_m13_p256.log` and `/workspace/scratch-res/lifted_rep_m12_p2048.log`. k = 4108 remains unstarted. Range unchanged: S_k ≠ 0 for k ≤ 49 and for the isolated lengths already recorded (77, 141, and the residue/survivor exclusions), exact h_n for 3 ≤ n ≤ 51; smallest open length 50.
