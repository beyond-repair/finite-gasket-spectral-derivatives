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

Whether a corner-visible eigenvalue λ (DN_n(λ) = 0, λ ≠ 0) can be a coincidental hit, i.e. R(λ) ∈ Spec(L_{n−1}) without decimation. If none occurs, the non-hit count is exactly 5·2^{n−1} and h_n = 1 − μ_exc(n) − 5·2^n/(3^{n+1}+3) exactly. This is a numerical observation for n = 3..6 only, not proved.

#### Numerical observation

scripts/check_decimation_hits.py (eigh on the same constructor, tolerances 1e−8 / 1e−7): for n = 1..6, c_n = 6, 11, 21, 41, 81, 161 = 5·2^{n−1}+1; dim DN_n(2) = 0; non-hit counts 5, 9, 20, 40, 80, 160 (n = 2 has 9 because its 5-space has one corner-visible direction); hit counts 1, 1, 3, 19, 87, 331, so h_n ≈ 0.167, 0.067, 0.071, 0.154, 0.238, 0.302, increasing toward 4/9 ≈ 0.444 from below; the decimation identity with corner defect has residual ≤ 2.2e−15. The fraction (hits + exceptional)/N is 0.40, 0.52, 0.67, 0.78, 0.85 for n = 2..6, which is compatible with SPECTRUM.md’s “0.4–0.7” for n = 2..4; that is a guess about how the old string was produced, not an identification, and that quantity tends to 1, not to 4/9.

#### Not a consequence

This subsection does not select W, does not state a continuum limit, a force, a stress, or a momentum, and does not claim the hit predicate or the corner defect formula is new.


---

<div align="center">

**REWRITE · BUILD · TRANSCEND**

**William (Brian) Ware** · [Atomic Dream Labs](https://github.com/beyond-repair)  
Governing source: [ADL-Governance](https://github.com/beyond-repair/ADL-Governance) · [Claim levels 0–5](https://github.com/beyond-repair/ADL-Governance/blob/main/docs/CLAIM_VALIDATION.md)

</div>
