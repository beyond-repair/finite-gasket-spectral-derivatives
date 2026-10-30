# Completion log — finite-gasket-spectral-derivatives

## Progress this run (2026-10-23 ~3:55pm EDT / locked-kernel routine: m = 13 lift k = 525)

Dated 2026-10-23 (America/New_York).

- Record current before this run: head 474f93f (pushed); S_k ≠ 0 for 1 ≤ k ≤ 50; exact h_n for 3 ≤ n ≤ 52.
- **Assumptions**: locked K = ω²I − WL (ω = 1, λ_max = 6, K > 0 iff W < 1/6); the recorded elimination lemma and lifted-`direct` lemma; e = 16 for m = 13. No continuum, force, stress, momentum, or selected W.
- **Exact finite computation (new length)**: m = 13 `lift rep` p = 512 (k = 525) EXIT:0 15:04:57 EDT: 7 factors, 114,688 chains, 14 with S in GF(2^512), **0 with S = 0** (65,695.6 s). Hence S_525 ≠ 0 (finite exact + recorded lemmas). Isolated length; range unchanged.
- Started: m = 13 p = 1024 (k = 1037) at 15:54 EDT (log `/workspace/scratch-res/lifted_rep_m13_p1024.log`). Still running, no result: walk KMAX = 51 (started 07:52 EDT), m = 12 k = 2060. Not started: k = 2061, 4108, 8205.
- Range unchanged: exact h_n for 3 ≤ n ≤ 52; smallest open length 51. Still open: residue conjecture for k ≥ 51 apart from the isolated lengths recorded (77, 141, 269, 525 and the survivor exclusions); excess ≤ 12 and ≤ 13; deg R for m ≥ 14.
- README "Residue condition: excess m = 13" addendum; CLAIM_STATUS row updated. No literature opened; no novelty claimed.

## Progress this run (2026-10-23 ~6:55am EDT / locked-kernel routine: reduced walk k = 50)

Dated 2026-10-23 (America/New_York).

- Record current before this run: head 865b888 (pushed); S_k ≠ 0 for k ≤ 49; exact h_n for 3 ≤ n ≤ 51.
- **Assumptions**: locked K = ω²I − WL (ω = 1, λ_max = 6, K > 0 iff W < 1/6); orbit lemma; two-adic reduction theorem. No continuum, force, stress, momentum, or selected W.
- **Exact finite computation**: unchanged reduced walk KMAX = 50 EXIT:0 at 06:08:30 EDT (started 2026-10-22 15:53:13 EDT): zeros = 0 at every k ≤ 50, 2^44 reduced chains at k = 50 covering all 2^50 chains; counts checked line by line. Hence S_k ≠ 0 for 1 ≤ k ≤ 50.
- **Corollary**: smallest open length 51; exact h_n = 1 − μ_exc(n) − 5·2^n/(3^{n+1}+3) for 3 ≤ n ≤ 52 (was ≤ 51).
- Running / not claimed: m = 13 p = 512 (k = 525), m = 12 p = 2048 (k = 2060); k = 4108, 1037, 2061, 8205 not started; KMAX = 51 walk not started.
- Still open: residue conjecture for k ≥ 51 with excess ≥ 12 (apart from isolated lengths 77, 141, 269 and survivor exclusions); excess ≤ 12 and ≤ 13; exact h_n for n ≥ 53; deg R for m ≥ 14.
- README "Residue condition: exact check to k = 50 (2026-10-23)"; CLAIM_STATUS row added. No literature opened; no novelty claimed.

## Progress this run (2026-10-22 ~8:50pm EDT / locked-kernel routine: m = 13 lift k = 269)

Dated 2026-10-22 (America/New_York).

- Record current before this run: head 6ebada6 (pushed); S_k ≠ 0 for k ≤ 49; exact h_n for 3 ≤ n ≤ 51.
- **Assumptions**: locked K = ω²I − WL (ω = 1, λ_max = 6, K > 0 iff W < 1/6); the recorded elimination lemma and lifted-`direct` lemma; e = 16 for m = 13. No continuum, force, stress, momentum, or selected W.
- **Exact finite computation (new length)**: m = 13 `lift rep` p = 256 (k = 269) EXIT:0 20:24:48 EDT: 18 factors, 294,912 chains, 36 with S in GF(2^256), **0 with S = 0** (19,687.4 s). Hence S_269 ≠ 0 (finite exact + recorded lemmas). Isolated length; range unchanged.
- Running / not claimed: m = 13 p = 512 (k = 525) started 20:50 EDT (log `/workspace/scratch-res/lifted_rep_m13_p512.log`); p = 1024, 2048, 8192 not started; m = 12 k = 2060 still running (current process started 17:08 EDT per the process table; no EXIT line), k = 4108 not started; walk KMAX = 50 still running (started 15:53 EDT, no result).
- Range unchanged: exact h_n for 3 ≤ n ≤ 51; smallest open length 50. Still open: residue conjecture for k ≥ 50 with excess ≥ 12 (apart from the isolated lengths recorded: 77, 141, 269 and the survivor exclusions); excess ≤ 12 and ≤ 13; deg R for m ≥ 14.
- README "Residue condition: excess m = 13" addendum; CLAIM_STATUS row updated. No literature opened; no novelty claimed.

## Progress this run (2026-10-22 ~1:58pm EDT / locked-kernel routine: m = 13 lift k = 141)

Dated 2026-10-22 (America/New_York).

- Record current before this run: head 0c652e5 (pushed); S_k ≠ 0 for k ≤ 49; exact h_n for 3 ≤ n ≤ 51.
- **Assumptions**: locked K = ω²I − WL (ω = 1, λ_max = 6, K > 0 iff W < 1/6); the recorded elimination lemma and lifted-`direct` lemma; e = 16 for m = 13. No continuum, force, stress, momentum, or selected W.
- **Exact finite computation (new length)**: m = 13 `lift rep` p = 128 (k = 141) EXIT:0 13:16:17 EDT: 22 factors, 360,448 chains, 44 with S in GF(2^128), **0 with S = 0** (2706.6 s). Hence S_141 ≠ 0 (finite exact + recorded lemmas). Isolated length; range unchanged.
- Running / not claimed: m = 13 p = 256 (k = 269) started 13:58 EDT (log `/workspace/scratch-res/lifted_rep_m13_p256.log`); p = 512, 1024, 2048, 8192 not started; m = 12 k = 2060 still running, k = 4108 not started.
- Range unchanged: exact h_n for 3 ≤ n ≤ 51; smallest open length 50. Still open: residue conjecture for k ≥ 50 with excess ≥ 12 (apart from the isolated lengths recorded); excess ≤ 12 and ≤ 13; deg R for m ≥ 14.
- README "Residue condition: excess m = 13" addendum; CLAIM_STATUS row updated. No literature opened; no novelty claimed.

## Progress this run (2026-10-22 ~12:55pm EDT / locked-kernel routine: m = 13 lifts k = 29, 77)

Dated 2026-10-22 (America/New_York).

- Record current before this run: head bdb70c9 (pushed); S_k ≠ 0 for k ≤ 49; exact h_n for 3 ≤ n ≤ 51.
- **Assumptions**: locked K = ω²I − WL (ω = 1, λ_max = 6, K > 0 iff W < 1/6); the recorded elimination lemma and lifted-`direct` lemma; e = 16 for m = 13. No continuum, force, stress, momentum, or selected W.
- **Exact finite computation (control)**: m = 13 `lift rep` p = 16 (k = 29) EXIT:0 12:03:43 EDT: 246 factors, 4,030,464 chains, 530 with S in GF(2^16), **0 with S = 0**. Agrees with the walk.
- **Exact finite computation (new length)**: m = 13 `lift rep` p = 64 (k = 77) EXIT:0 12:31:10 EDT: 62 factors, 1,015,808 chains, 124 with S in GF(2^64), **0 with S = 0** (1646.8 s). Hence S_77 ≠ 0 (finite exact + recorded lemmas). Isolated length; range unchanged.
- Running / not claimed: m = 13 p = 128 (k = 141) since 12:31 EDT; p ≥ 256 not started; m = 12 k = 2060 still running, k = 4108 not started.
- Range unchanged: exact h_n for 3 ≤ n ≤ 51; smallest open length 50. Still open: residue conjecture for k ≥ 50 with excess ≥ 12 (apart from the isolated lengths recorded); excess ≤ 12 and ≤ 13; deg R for m ≥ 14.
- README "Residue condition: excess m = 13" addendum; CLAIM_STATUS row updated. No literature opened; no novelty claimed.

## Progress this run (2026-10-22 ~11:57am EDT / locked-kernel routine: m = 13 control lift k = 45)

Dated 2026-10-22 (America/New_York).

- Record current before this run: head c265878 (pushed); S_k ≠ 0 for k ≤ 49; exact h_n for 3 ≤ n ≤ 51; m = 13 survivors recorded; lifts pending.
- **Exact finite computation (cross-check, not a new theorem)**: m = 13 `lift rep` at p = 32 (k = 45) finished EXIT:0 at 11:42:53 EDT: 128 surviving factors, 2,097,152 chains examined, 256 with S in GF(2^32), **0 with S = 0** (2910.7 s). Agrees with the reduced walk, which already proved S_45 ≠ 0. Log `/workspace/scratch-res/lifted_rep_m13_p32.log`. README "Residue condition: excess m = 13" addendum; CLAIM_STATUS row updated.
- Running / queued, not claimed: m = 13 p = 16 (k = 29, control) restarted 11:43:15 EDT; p = 64 (k = 77) and p = 128 (k = 141) queued sequentially; p ≥ 256 not started. m = 12 `lift rep` k = 2060 still running; k = 4108 not started.
- Range unchanged: S_k ≠ 0 for k ≤ 49; exact h_n for 3 ≤ n ≤ 51. Still open: residue conjecture for k ≥ 50 with excess ≥ 12; excess ≤ 12 and ≤ 13; deg R for m ≥ 14.
- No literature opened; no novelty claimed. Not a consequence: no W selected, no continuum limit, force, stress, or momentum.

## Progress this run (2026-10-22 ~10:53–11:25am EDT / locked-kernel routine: excess m = 13 survivors)

Dated 2026-10-22 (America/New_York).

- Record current before this run: head 4758275 (pushed); S_k ≠ 0 for k ≤ 49; exact h_n for 3 ≤ n ≤ 51; smallest open length 50; `lift rep` k = 2060 running, k = 4108 not started, `prepare 13` 507/512.
- **Assumptions**: locked K = ω²I − WL (ω = 1, λ_max = 6, K > 0 iff W < 1/6); the recorded elimination lemma and lifted-`direct` lemma; e = 16 for m = 13. No continuum, force, stress, momentum, or selected W.
- **Exact finite computation**: `prepare 13` finished EXIT:0 at 10:03:05 EDT (512 orbit prefixes; 295 computed in the final call, 32756.2 s). R ≠ 0 and deg R = 8190 = 2^13 − 2 on every prefix (second, independent run of that degree statement). Surviving chain condition (p: count) = {16: 246, 32: 128, 64: 62, 128: 22, 256: 18, 512: 7, 1024: 12, 2048: 1, 8192: 1}; none at p = 4096 or 16384.
- **Consequence (elimination lemma + computation)**: S_{p+13} ≠ 0 for every power of two p > 13 outside {16, …, 2048, 8192}; in particular k = 4109, 16397, and every 2^j + 13 with 2^j ≥ 32768. README "Residue condition: excess m = 13"; CLAIM_STATUS row added.
- **Negative / operational result**: four parallel m = 13 `lift rep` jobs (p = 16, 32, 64, 128) exhausted memory; p = 16 was OOM-killed at 11:14 EDT (EXIT:137, no result). p = 64, 128 were stopped; p = 32 continues; p = 16, 64, 128 are queued to run one at a time after it, with raised OOM scores so the 8-hour k = 2060 lift is not the one killed. Nothing inferred from the killed runs.
- Pending, not claimed: m = 13 lift S = 0 counts at k = 29, 45 (controls), 77, 141, 269, 525, 1037, 2061, 8205; m = 12 at k = 2060 (running since 03:15 EDT per process start), 4108 (not started).
- Range unchanged: S_k ≠ 0 for k ≤ 49; exact h_n for 3 ≤ n ≤ 51. Still open: residue conjecture for k ≥ 50 with excess ≥ 12; excess ≤ 12 and ≤ 13; deg R for m ≥ 14.
- No literature opened; no novelty claimed. Not a consequence: no W selected, no continuum limit, force, stress, or momentum.

## Proved this run (2026-10-22 ~9:55am EDT / locked-kernel routine: k = 49 walk closed)

Dated 2026-10-22 (America/New_York).

- Record current before this run: head aacc635 (pushed); S_k ≠ 0 for k ≤ 48; exact h_n for 3 ≤ n ≤ 50; smallest open length 49; walk KMAX = 49, `lift rep` k = 2060 and `prepare 13` running.
- **Exact finite computation**: the reduced walk KMAX = 49 (unchanged source since 172f122, same binary as walk47/walk48, sha256 1b35db9d…f451) finished EXIT:0 at 08:51:41 EDT (started 00:56:27 EDT): `k=49 reduced_chains=8796093022208 orbit_size=64 chains_covered=2^49 zeros=0 ok`, zeros = 0 at every k ≤ 49; reduced-chain, orbit and coverage counts match 2^{k−⌈log₂(k+1)⌉} / 2^{⌈log₂(k+1)⌉} / 2^k at all 49 depths. Log `/workspace/scratch-res/walk49.log`.
- **Corollary (theorem + computation)**: S_k ≠ 0 for k ≤ 49; smallest open length 50 = 32 + 18; exact h_n = 1 − μ_exc(n) − 5 · 2^n/(3^{n+1} + 3) for 3 ≤ n ≤ 51 (README "exact check to k = 49"; CLAIM_STATUS row added).
- Pending, not claimed: `lift rep` k = 2060 (no result line); k = 4108 not started; `prepare 13` 507/512 prefixes cached.
- Still open: residue conjecture for k ≥ 50 with excess ≥ 12; excess ≤ 12 (k = 2060, 4108); exact h_n for n ≥ 52; deg R for m ≥ 14.
- No literature opened; no novelty claimed. Not a consequence: no W selected, no continuum limit, force, stress, or momentum.

## Status this run (2026-10-22 ~12:55–1:05am EDT / locked-kernel routine: interrupted jobs restarted, no new theorem)

Dated 2026-10-22 (America/New_York).

- Record current before this run: head 236e2d1 (pushed); excess ≤ 11 theorem; deg R = 2^m − 2, d_0 / recurrence and R ∈ GF(2^e)[x²] exact for 2 ≤ m ≤ 13; S_k ≠ 0 for k ≤ 48; exact h_n for 3 ≤ n ≤ 50; smallest open length 49; excess m = 12 lift rep S = 0 count 0 at k = 28, 44, 76, 140, 268, 524; k = 2060, 4108 uncertified.
- **Negative / operational result**: the compute box was restarted (~00:16 EDT 2026-10-22). Every pending job from the 2026-10-15 entries ended **without a result line**: `lift rep` k = 2060 (p = 2048; log `/workspace/scratch-res/lifted_rep_m12_p2048.log` held only its start timestamp), the queued k = 4108 (never started), and `prepare 13` (217 of 512 orbit prefixes cached in `/workspace/scratch-res/lifted_m13.json.d`). Nothing is inferred from the interrupted runs. The python-flint package was also missing after the restart and was reinstalled (0.9.0); cached prefix results are exact data and are reused unchanged.
- **Restarted (pending, not claimed)**, all with unchanged code:
  - reduced walk KMAX = 49 with the same binary as walk48 (sha256 1b35db9d…f451), OMP_NUM_THREADS = 4, log `/workspace/scratch-res/walk49.log`, started 00:56 EDT. If it reports zeros = 0 at k = 49 then S_k ≠ 0 for k ≤ 49 and the two-adic reduction extends exact h_n to n = 51; not claimed until EXIT:0.
  - `prepare 13` resumed from the 217-prefix cache, 2 workers, log `/workspace/scratch-res/lifted_prepare_m13.log`.
  - `lift rep` k = 2060 (p = 2048) from scratch (not resumable), log `/workspace/scratch-res/lifted_rep_m12_p2048.log`, started 00:58 EDT.
- **Cost estimate (numerical observation, not a bound)**: recorded lift timings per surviving factor are ~506 s at p = 256 (13 factors, 6578 s) and ~3553 s at p = 512 (5 factors, 17765 s), a ratio of ~7 per doubling of p. Extrapolating that ratio gives order 2 days for k = 2060 (1 factor) and order weeks for k = 4108 (2 factors, p = 4096). k = 4108 is therefore **not restarted**; excess ≤ 12 cannot close by this route on this box without either a faster method for the p = 4096 survivors or a structural argument that removes them.
- Range unchanged: S_k ≠ 0 for k ≤ 48; exact h_n for 3 ≤ n ≤ 50. Still open: residue conjecture for k ≥ 49 with excess ≥ 12; excess ≤ 12 (k = 2060, 4108); deg R recurrence / evenness for general m (exact only for m ≤ 13); excess-13 filter.
- No literature opened; no novelty claimed. Not a consequence: no W selected, no continuum limit, force, stress, or momentum.

## Proved this run (2026-10-15 ~4:28–5:00pm EDT / locked-kernel routine: k = 48 walk closed)

Dated 2026-10-15 (America/New_York).

- Record current before this run: head adab35f; excess ≤ 11 theorem; deg R = 2^m − 2, d_0 = m − 1 / recurrence and R ∈ GF(2^e)[x²] exact for 2 ≤ m ≤ 13; S_k ≠ 0 for k ≤ 47; exact h_n for 3 ≤ n ≤ 49; smallest open length 48; excess m = 12 lift rep S = 0 count 0 at k = 28, 44, 76, 140, 268, 524; k = 2060 running, k = 4108 queued; walk48 and `prepare 13` running.
- **Assumptions**: locked K = ω²I − WL (ω = 1, λ_max = 6, K > 0 iff W < 1/6); two-adic reduction theorem and Frobenius orbit lemma as already recorded. No continuum, force, stress, momentum, or selected W.
- **Exact finite computation**: the unchanged reduced walk `scripts/residue_orbits_gf2_64.c` with KMAX = 48 finished EXIT:0 at 16:28:53 EDT (started 09:05:49 EDT; ~7 h 23 min wall, OMP_NUM_THREADS = 2, box shared with lifts): `k=48 reduced_chains=4398046511104 orbit_size=64 chains_covered=2^48 zeros=0 ok`, and zeros = 0 at every k ≤ 48 (48 `ok` lines; reduced-chain and orbit counts match 2^{k−⌈log₂(k+1)⌉} / 2^{⌈log₂(k+1)⌉} at every k). `validate` KMAX = 24 passed first (`/workspace/scratch-res/repo_orbits_k48_validate.log`). Source has no diff since 172f122; a fresh `gcc -O3 -march=native -fopenmp` build is byte-identical to the binary that ran (`walk48`, sha256 1b35db9d…f451, same as walk47). Scratch `/workspace/scratch-res/repo_orbits_k48.log`.
- **Corollary (theorem + finite computation)**: S_k ≠ 0 for every chain when 1 ≤ k ≤ 48. Smallest open length is now 49 = 32 + 17. By the two-adic reduction theorem (for n = 50 only even k ≤ 48 could give a hit, and none is open), exact h_n = 1 − μ_exc(n) − 5 · 2^n/(3^{n+1} + 3) for **3 ≤ n ≤ 50** (was 3 ≤ n ≤ 49). For n = 51 the open odd length 49 is not excluded. README "Residue condition: exact check to k = 48 (2026-10-15)".
- No independent sampled walk at k = 48 (the k = 47 sampled consistency check is not extended). No KMAX = 49 walk started (CPU in use).
- **Pending, not claimed**: excess m = 12 `lift rep` at k = 2060 (p = 2048, pid ~261337) still running, log holds only the start timestamp; k = 4108 (p = 4096) still queued behind it (parent pid ~261330). Excess ≤ 12 is **not** a theorem. `prepare 13` (pid ~517804) still running, ~147/512 orbit prefixes cached; not used.
- Unchanged: deg R claims (exact for 2 ≤ m ≤ 13; conjecture for m ≥ 14). Still open: residue conjecture for k ≥ 49 with excess ≥ 12 (excess 12 partially closed); exact h_n for n ≥ 51; excess ≤ 12; excess-13 filter.
- No literature opened; no novelty claimed. Not a consequence: no W selected, no continuum limit, force, stress, or momentum.

## Progress this run (2026-10-15 ~2:55–3:10pm EDT / hourly routine: deg-R structural checks at m = 13)

Dated 2026-10-15 (America/New_York).

- Record current before this run: head 742ddcc; excess ≤ 11 theorem; deg R = 2^m − 2, d_0 = m − 1 / recurrence and R ∈ GF(2^e)[x²] exact for m ≤ 12; S_k ≠ 0 for k ≤ 47; exact h_n for 3 ≤ n ≤ 49; excess m = 12 lift rep S = 0 count 0 at k = 28, 44, 76, 140, 268, 524; k = 2060 running, k = 4108 queued; walk48, prepare 13 and `check_degR_structure.py 13` running.
- **Assumptions**: unchanged from the previous entry (locked K = ω²I − WL, the repo's elimination tower, Frobenius orbit reduction for m ≥ 7). No continuum, force, stress, momentum, or selected W.
- **Exact finite computation**: `check_degR_structure.py 13 2 /workspace/scratch-res/degR_structure_m13.d` finished EXIT:0 at 15:07:30 EDT (started 14:14:32): `prefixes=512 observed_seqs={[12, 13, 16, 23, 38, 69, 132, 259, 514, 1025, 2048, 4095, 8190]: 512} degR=[8190] mismatches={all 7 counters 0} sum_prefix_time=6344.5s wall=3177.4s`. Log `/workspace/scratch-res/degR_structure_m13.log` (not vendored).
- **Lemma status**: finite exact statements on the recorded prefixes (orbit representatives for m ≥ 7) now hold for 2 ≤ m ≤ 13: deg R = 2^m − 2 with R ≠ 0; d_0 = m − 1 and d_r = 2 d_{r−1} − (m − r − 1); R ∈ GF(2^e)[x²]. Extension from m ≤ 12 to m ≤ 13 for all three. Single run at m = 13 (no independent cross-check). Not a uniform proof.
- **Not claimed**: anything about excess m = 13 (R was not factored here); excess ≤ 12 (k = 2060 still running, k = 4108 queued); walk48 still running (log holds only the start timestamp); `prepare 13` still running (not used).
- Range unchanged: exact h_n for 3 ≤ n ≤ 49; S_k ≠ 0 for k ≤ 47. Still open: proof of the deg-R recurrence / evenness for general m; deg R conjecture for m ≥ 14; excess ≤ 12; excess-13 filter; residue conjecture for k ≥ 48.
- No literature opened; no novelty claimed. Not a consequence: no W selected, no continuum limit, force, stress, or momentum.

## Progress this run (2026-10-15 ~1:55–2:30pm EDT / hourly routine: deg-R structural checks through m = 12)

Dated 2026-10-15 (America/New_York).

- Record current before this run: head 87ae4e6; excess ≤ 11 theorem; deg R = 2^m − 2 for m ≤ 12 (finite exact); d_0 = m − 1 / recurrence and R ∈ GF(2^e)[x²] exact only for m ≤ 8; S_k ≠ 0 for k ≤ 47; exact h_n for 3 ≤ n ≤ 49; excess m = 12 lift rep S = 0 count 0 at k = 28, 44, 76, 140, 268, 524; k = 2060 running, k = 4108 queued; walk48 and prepare 13 running.
- **Assumptions**: locked K = ω²I − WL (ω = 1, λ_max = 6, K > 0 iff W < 1/6); the elimination tower A_1 = GF(2^e)[x], A_i = A_{i−1}[α_i]/(α_i² + α_i + β_i), G and R = N_2(⋯N_m(G)⋯) exactly as in `scripts/check_residue_p_plus_m.py eliminate`; Frobenius orbit reduction of prefixes for m ≥ 7 as already used by `filter … orbit` / `prepare`. No continuum, force, stress, momentum, or selected W.
- **Exact finite computation**: new `scripts/check_degR_structure.py M [workers [cache]]` runs the repo's `eliminate` unchanged, wrapping only `make_ring` so each relative norm records the max GF(2^e)-degree over all nested (a, b) components (d_0 before N_m; d_r after N_{m−r+1}). Mismatches are counted, not asserted. Results, all with zero mismatches on every counter (d0, rec, closed, degR, Rzero, odd, len):
  - m = 2…6 all prefixes (4, 8, 16, 32, 64); m = 7…11 orbit prefixes (16, 16, 32, 64, 128): log `/workspace/scratch-res/degR_structure_m2_11.log` (13:58–14:02:50 EDT, EXIT:0; m = 11 225.3s).
  - m = 12 orbit prefixes (256), 2 workers: `degR-structure m=12 e=16 orbit=True prefixes=256 … observed_seqs={[11, 12, 15, 22, 37, 68, 131, 258, 513, 1024, 2047, 4094]: 256} degR=[4094] mismatches={all 0} sum_prefix_time=1402.6s wall=703.2s`, EXIT:0 at 14:10:15 EDT. Log `/workspace/scratch-res/indep_degR_m12.log`; per-prefix cache `/workspace/scratch-res/degR_structure_m12.d/`.
  - Cross-check (not an input): the earlier separate scratch checker `/workspace/scratch-res/indep_degR.py` (log `/workspace/scratch-res/indep_degR.log`) already gave deg R exact, R ≠ 0, no odd coefficients for m ≤ 11.
- **Lemma status**: finite exact statements on the recorded prefixes — for 2 ≤ m ≤ 12, d_0 = m − 1, d_r = 2 d_{r−1} − (m − r − 1) at every step (so d_{m−1} = deg R = 2^m − 2), and R ∈ GF(2^e)[x²]. Strict extension of the written record from m ≤ 8 to m ≤ 12 for both structural claims. deg R = 2^m − 2 range unchanged (already m ≤ 12). Not a uniform proof; no structural explanation of evenness or of the leading-term cancellation is claimed.
- **Pending, not claimed**: `check_degR_structure.py 13` (512 orbit prefixes, 2 workers, nice 10, cache `/workspace/scratch-res/degR_structure_m13.d`, log `/workspace/scratch-res/degR_structure_m13.log`) started ~2:12pm EDT; at ~2:15pm EDT 10/512 prefixes done, every one with the predicted sequence ending 8190 and no odd coefficients — **partial, no m = 13 claim**. `prepare 13` (pid ~517804) still running, 49/512 prefixes cached; not used. walk48 KMAX = 48 (pid ~348412) still running, log holds only the start timestamp. `lift rep` p = 2048 (k = 2060, pid ~261337) still running, log holds only the start timestamp; k = 4108 still queued behind it. Excess ≤ 12 **not** claimed.
- Range unchanged: exact h_n for 3 ≤ n ≤ 49; S_k ≠ 0 for k ≤ 47. Still open: proof of d_0 = m − 1 / the recurrence / evenness for general m; deg R conjecture for m ≥ 13; excess ≤ 12 (pending k = 2060, 4108); residue conjecture for k ≥ 48.
- No literature opened; no novelty claimed. Not a consequence: no W selected, no continuum limit, force, stress, or momentum.

## Progress this run (2026-10-15 ~12:02pm EDT / hourly routine: excess m=12 lift k=524)

Dated 2026-10-15 (America/New_York).

- Record current before this run: head 1484af6; excess ≤ 11 theorem; deg R = 2^m − 2 for m ≤ 12 (finite exact); S_k ≠ 0 for k ≤ 47; exact h_n for 3 ≤ n ≤ 49; smallest open length 48; excess m = 12 filter EXIT:0; lift rep S = 0 count 0 at k = 28, 44, 76, 140, 268; k = 524 / 2060 / 4108 pending; walk48 and p2048 still running.
- **Assumptions**: locked K = ω²I − WL (ω = 1, λ_max = 6, K > 0 iff W < 1/6); elimination lemma and lifted-`direct` lemma as already recorded. No continuum, force, stress, momentum, or selected W.
- **Exact finite computation**: `scripts/check_residue_lifted.py lift … 512 rep` at m = 12 finished EXIT:0 between 06:54:46 and 11:50:52 EDT: `lift[rep] k=524 (p=512, m=12, orbit reps): surviving factors=5, roots used=5, chains examined=40960, with S in GF(2^p)=10, with S = 0: 0, time=17764.6s per-factor (chains, S in GF, S=0) for one root=[(8192, 2, 0), (8192, 2, 0), (8192, 2, 0), (8192, 2, 0), (8192, 2, 0)]`. Scratch `/workspace/scratch-res/lifted_rep_m12_p512.log`.
- **Consequence (finite computation + recorded lemmas)**: S_524 ≠ 0 for every chain. Together with elimination + prior lifts this leaves only k = 2060 and k = 4108 as excess-12 lengths not yet certified.
- **Pending, not claimed**: `lift rep` at k = 2060 (p = 2048) still running (pid ~261337 since 07:22 EDT; log `/workspace/scratch-res/lifted_rep_m12_p2048.log` holds only the start timestamp). k = 4108 (p = 4096) is **queued** sequentially behind p2048 via the existing parent `bash -c 'run 2048 4096'` (pid ~261330); not live yet; no parallel duplicate started (load already high: walk48 + p2048). Excess ≤ 12 is **not** a theorem yet. Separately, the KMAX = 48 reduced walk is still running (pid ~348412; log `/workspace/scratch-res/repo_orbits_k48.log` still holds only the start timestamp; prints only at end).
- Range unchanged: exact h_n for 3 ≤ n ≤ 49; smallest open length 48 = 32 + 16. Still open: residue conjecture for k ≥ 48 with excess ≥ 12 (excess 12 partially closed); deg R conjecture for m ≥ 13.
- No literature opened; no novelty claimed. Not a consequence: no W selected, no continuum limit, force, stress, or momentum.

## Progress this run (2026-10-15 ~10:00am EDT / hourly routine: excess m = 12 filter done + lift k = 268)

Dated 2026-10-15 (America/New_York).

- Record current before this run: head 3da6173; excess ≤ 11 theorem; deg R = 2^m − 2 for m ≤ 12 (finite exact); S_k ≠ 0 for k ≤ 47; exact h_n for 3 ≤ n ≤ 49; smallest open length 48; excess m = 12 lift rep S = 0 count 0 at k = 28, 44, 76, 140; k = 268, 524, 2060 pending; k = 4108 not started; `filter 12 orbit` was still empty at the prior write-up.
- **Exact finite computation (A)**: independent `scripts/check_residue_p_plus_m.py filter 12 orbit` finished EXIT:0 at 09:42:26 EDT: `filter m=12 e=16 prefixes=256 degR=4094` power-of-two-degree factors (p: count)={16: 512, 32: 111, 64: 60, 128: 27, 256: 17, 512: 7, 2048: 1, 4096: 2, 8192: 1}; surviving chain condition (p: count)={16: 133, 32: 56, 64: 29, 128: 17, 256: 13, 512: 5, 2048: 1, 4096: 2}; time=17334.6s. Matches `prepare 12` survivors exactly (including p = 4096: 2). Scratch `/workspace/scratch-res/repo_filter_m12.log`.
- **Exact finite computation (B)**: `scripts/check_residue_lifted.py lift … 256 rep` at m = 12 finished EXIT:0 at 09:24:33 EDT: `lift[rep] k=268 (p=256, m=12, orbit reps): surviving factors=13, roots used=13, chains examined=106496, with S in GF(2^p)=26, with S = 0: 0, time=6578.3s`. Scratch `/workspace/scratch-res/lifted_rep_m12_p256.log`.
- **Consequence (finite computation + recorded lemmas)**: S_268 ≠ 0 for every chain. Together with elimination + prior lifts this leaves only k = 524, 2060, 4108 as excess-12 lengths not yet certified.
- **Pending, not claimed**: `lift rep` still running at k = 524 (p = 512) and k = 2060 (p = 2048); k = 4108 (p = 4096) not started this run (CPU already has walk48 + two lifts). Excess ≤ 12 is **not** a theorem yet. Separately, the KMAX = 48 reduced walk is still running (no result yet); range unchanged.
- Range unchanged: exact h_n for 3 ≤ n ≤ 49; smallest open length 48 = 32 + 16. Still open: residue conjecture for k ≥ 48 with excess ≥ 12 (excess 12 partially closed); deg R conjecture for m ≥ 13.
- No literature opened; no novelty claimed. Not a consequence: no W selected, no continuum limit, force, stress, or momentum.

## Progress this run (2026-10-15 ~9:03am EDT / hourly routine: reduced walk KMAX = 48 started)

Dated 2026-10-15 (America/New_York).

- Record current before this run: head 2be0828; excess ≤ 11 theorem; deg R = 2^m − 2 for m ≤ 12 (finite exact); S_k ≠ 0 for k ≤ 47; exact h_n for 3 ≤ n ≤ 49; smallest open length 48; excess m = 12 lift rep S = 0 count 0 at k = 28, 44, 76, 140; k = 268, 524, 2060, 4108 pending.
- **Status check (Priority A / B blocked)**: the three pending m = 12 `lift rep` jobs are still running with no result lines yet — p = 256 (k = 268, pid ~290555, since 07:34 EDT), p = 512 (k = 524, pid ~261335, since 07:14 EDT), p = 2048 (k = 2060, pid ~261337, since 07:14 EDT). Logs `/workspace/scratch-res/lifted_rep_m12_p{256,512,2048}.log` still hold only the start timestamp. The independent `filter 12 orbit` cross-check (pid ~162924, since 05:33 EDT) still has an empty log. p = 4096 (k = 4108) was not started (CPU slots occupied; prefer not starving the three lifts). Excess ≤ 12 remains **not** claimed.
- **Pending, not claimed (Priority C)**: started the unchanged reduced walk `scripts/residue_orbits_gf2_64.c` with KMAX = 48 (smallest open length 48 = 32 + 16). `validate` at KMAX = 24 passed EXIT:0 first. Fresh build is byte-identical to walk47 (sha256 1b35db9d…f451). Binary `/workspace/scratch-res/walk48`, log `/workspace/scratch-res/repo_orbits_k48.log` (start 09:05:49 EDT). OMP_NUM_THREADS = 2 so the three lifts keep CPU. Expect ~2× the k = 47 wall (~3 h); the program prints per-k lines only after the full tree finishes. **Not** claimed: no S = 0 count at k = 48 yet; range unchanged.
- Range unchanged: exact h_n for 3 ≤ n ≤ 49; smallest open length 48 = 32 + 16. Still open: residue conjecture for k ≥ 48 with excess ≥ 12 (excess 12 partially closed); deg R conjecture for m ≥ 13.
- No literature opened; no novelty claimed. Not a consequence: no W selected, no continuum limit, force, stress, or momentum.

## Progress this run (2026-10-15 ~7:58am EDT / hourly routine: excess m = 12 lifts, first four lengths)

Dated 2026-10-15 (America/New_York).

- Record current before this run: head 6b19128; excess ≤ 11 theorem; deg R = 2^m − 2 for m ≤ 12 (finite exact); S_k ≠ 0 for k ≤ 47; exact h_n for 3 ≤ n ≤ 49; smallest open length 48.
- **Exact finite computation**: `scripts/check_residue_lifted.py lift … rep` at m = 12 finished EXIT:0 with S = 0 count 0 at k = 28 (p = 16; 133 factors, 1089536 chains), k = 44 (p = 32; 56 factors, 458752 chains), k = 76 (p = 64; 29 factors, 237568 chains), k = 140 (p = 128; 17 factors, 139264 chains). k = 28 and 44 agree with the k ≤ 47 walk (controls).
- **Consequence (finite computation + recorded lemmas)**: S_76 ≠ 0 and S_140 ≠ 0 for every chain. Together with the elimination result this leaves k = 268, 524, 2060, 4108 as the only excess-12 lengths not yet certified.
- **Pending, not claimed**: `lift rep` at k = 268 (restarted 07:53 EDT), 524 and 2060 (since 07:13 EDT), and 4108 (queued). The independent `filter 12 orbit` cross-check (since 05:32 EDT) has no output yet. Excess ≤ 12 is **not** a theorem yet.
- Range unchanged: exact h_n for 3 ≤ n ≤ 49; smallest open length 48 = 32 + 16. Still open: residue conjecture for k ≥ 48 with excess ≥ 12 (excess 12 partially closed); deg R conjecture for m ≥ 13.
- No literature opened; no novelty claimed. Not a consequence: no W selected, no continuum limit, force, stress, or momentum.

## Progress this run (2026-10-15 ~6:55am EDT / hourly routine: excess m = 12 elimination; deg R lemma to m ≤ 12)

Dated 2026-10-15 (America/New_York).

- Record current before this run: head 759170d; excess ≤ 11 theorem; deg R = 2^m − 2 theorem for m ≤ 11; S_k ≠ 0 for k ≤ 47; exact h_n for 3 ≤ n ≤ 49; smallest open length 48.
- **Exact finite computation**: `scripts/check_residue_lifted.py prepare 12` finished EXIT:0 at 06:01:38 EDT (256 orbit prefixes, e = 16). R ≠ 0 on every prefix (asserted), deg R = 4094 = 2^12 − 2 on every prefix. Surviving chain condition (p: count) = {16: 133, 32: 56, 64: 29, 128: 17, 256: 13, 512: 5, 2048: 1, 4096: 2}; none at p = 1024 or 8192. Scratch `/workspace/scratch-res/lifted_m12.json`, `/workspace/scratch-res/lifted_prepare_m12.log`.
- **Lemma extended (finite exact)**: deg R = 2^m − 2 and R ≠ 0 on every checked prefix for m ≤ 12 (was m ≤ 11). Conjecture for m ≥ 13 unchanged. The independent `filter 12 orbit` run (since 05:13 EDT) is a pending cross-check, not an input. README "degree of the elimination polynomial R".
- **Proved consequence (elimination lemma)**: S_{p+12} ≠ 0 for every power of two p > 12 outside {16, 32, 64, 128, 256, 512, 2048, 4096}, e.g. k = 1036 and k = 8204. README "excess m = 12 (partial …)".
- **Pending, not claimed**: `lift rep` S = 0 counts at k = 28, 44, 76, 140, 268, 524, 2060, 4108, started 06:54 EDT (logs `/workspace/scratch-res/lifted_rep_m12_p{P}.log`). Excess ≤ 12 is **not** proved until all eight report 0. k = 28 and 44 are already covered by the k ≤ 47 walk and act as controls.
- Supporting only: three independent sampled walks (stride 64, offsets 0, 37, 63) report zeros = 0 for every k ≤ 47; recorded in README "exact check to k = 47" as a consistency check.
- Range unchanged: exact h_n for 3 ≤ n ≤ 49; smallest open length 48 = 32 + 16. Still open: residue conjecture for k ≥ 48 with excess ≥ 12; deg R conjecture for m ≥ 13.
- No literature opened; no novelty claimed. Not a consequence: no W selected, no continuum limit, force, stress, or momentum.

## Proved this run (2026-10-15 ~4:51am EDT / hourly routine: k = 47 walk closed; excess m = 12 filter started)

Dated 2026-10-15 (America/New_York).

- Record current before this run: head 35b3b90; excess ≤ 11 theorem; deg R = 2^m − 2 theorem for m ≤ 11; smallest open length 47; exact h_n for 3 ≤ n ≤ 48; reduced walk KMAX = 47 running.
- **Exact finite computation**: the unchanged reduced walk `scripts/residue_orbits_gf2_64.c` with KMAX = 47 finished EXIT:0 at 05:29:51 EDT (93 min 48 s wall, 374.7 user CPU-min): `k=47 reduced_chains=2199023255552 orbit_size=64 chains_covered=2^47 zeros=0 ok`, and zeros = 0 at every k ≤ 47. Source has no diff against the commit; a fresh build is byte-identical to the binary that ran. Scratch `/workspace/scratch-res/repo_orbits_k47.log`.
- **Corollary (theorem + finite computation)**: S_k ≠ 0 for every chain when 1 ≤ k ≤ 47. Smallest open length is now 48 = 32 + 16. By the two-adic reduction theorem, exact h_n = 1 − μ_exc(n) − 5 · 2^n/(3^{n+1} + 3) for **3 ≤ n ≤ 49** (was 3 ≤ n ≤ 48). README "Residue condition: exact check to k = 47 (2026-10-15)".
- Excess m = 12 (pending, not claimed): `scripts/check_residue_p_plus_m.py filter 12 orbit` running since 04:53 EDT (log `/workspace/scratch-res/repo_filter_m12.log`, no output yet at 05:51 EDT) and `scripts/check_residue_lifted.py prepare 12` running since 05:31 EDT (per-prefix cache `/workspace/scratch-res/lifted_m12.json.d`, 181 entries at 05:51 EDT). No m = 12 survivor list or S = 0 count exists yet, so excess ≤ 12 is **not** proved and deg R = 2^m − 2 remains a conjecture for m ≥ 12.
- Status check 2026-10-15 ~5:50am EDT (hourly routine): record current; no new theorem this run. Still open: residue conjecture for k ≥ 48 with excess ≥ 12 (smallest open length 48 = 32 + 16); exact h_n for n ≥ 50.
- No literature opened; no novelty claimed. Not a consequence: no W selected, no continuum limit, force, stress, or momentum.

## Progress this run (2026-10-15 ~3:56am EDT / hourly routine: k=520 lift control; k=47 walk started)

Dated 2026-10-15 (America/New_York).

- Record current before this run: head ffda804; excess ≤ 11 theorem; deg R = 2^m − 2 theorem for m ≤ 11, conjecture in general; smallest open length 47; exact h_n for 3 ≤ n ≤ 48.
- **Numerical control (exact finite computation, supporting only)**: `scripts/check_residue_lifted.py lift … 512` (mode `all`) at m = 8 (k = 520) reproduces the recorded orbit `direct` count exactly: adm_c = 32, chains = 16384, S ∈ GF(2^p) = 64, S = 0 count 0 (lift 5704.8 s vs direct 9069.6 s). This is the largest p at which `lift` has been checked against an independent `direct` run; it adds no new length to any theorem (k = 520 was already covered by excess ≤ 10). Scratch `/workspace/scratch-res/lifted_ctrl.log`, `/workspace/scratch-res/big_8_512.log`. README control table updated.
- **Pending, not claimed**: unchanged reduced walk `residue_orbits_gf2_64.c` started with KMAX = 47 at 03:56 EDT (`validate` at KMAX = 24 passed). k = 47 = 32 + 15 is the smallest open length, so a zero count there would move exact h_n to 3 ≤ n ≤ 49. Log `/workspace/scratch-res/repo_orbits_k47.log`.
- Range unchanged this run: exact h_n for 3 ≤ n ≤ 48. Still open: residue conjecture for k ≥ 47 with excess ≥ 12; deg R conjecture for m ≥ 12.
- No literature opened; no novelty claimed. Not a consequence: no W selected, no continuum limit, force, stress, or momentum.

## Proved previously (2026-10-15 ~3:37am EDT / hourly routine: excess ≤ 11 theorem + deg R partial)

Dated 2026-10-15 (America/New_York).

- Record current before this run: head e821373; excess ≤ 10 theorem; excess 11 had filter + lifts through p = 256 (S=0 count 0); p = 512 and p = 1024 `rep` lifts were already running (left alone).
- **Exact finite computation (Priority A)**: both pending `lift rep` runs finished EXIT:0 with S = 0 count 0.
  - p=512 (k=523): `lift[rep] k=523 (p=512, m=11, orbit reps): surviving factors=3, roots used=3, chains examined=12288, with S in GF(2^p)=6, with S = 0: 0, time=4494.2s per-factor (chains, S in GF, S=0) for one root=[(4096, 2, 0), (4096, 2, 0), (4096, 2, 0)]` — scratch `/workspace/scratch-res/lifted_rep_m11_p512.log`.
  - p=1024 (k=1035): `lift[rep] k=1035 (p=1024, m=11, orbit reps): surviving factors=1, roots used=1, chains examined=4096, with S in GF(2^p)=2, with S = 0: 0, time=3145.2s per-factor (chains, S in GF, S=0) for one root=[(4096, 2, 0)]` — scratch `/workspace/scratch-res/lifted_rep_m11_p1024.log`.
- **Theorem**: S_k ≠ 0 for every chain whenever k − 2^⌊log2 k⌋ ≤ 11. Proof structure as for excess ≤ 10: elimination lemma (R ≠ 0, finite surviving p) + exact zero counts at every surviving (m, p) with m ≤ 11 (prior directs / lifts for m ≤ 10 and for m = 11 at p ∈ {16,32,64,128,256}; this run for p ∈ {512,1024}). First lengths newly covered by a proof include 523 and 1035 (among others already listed for m ≤ 10).
- **Partial lemma (Priority B, deg R)**: README "Residue condition: degree of the elimination polynomial R". deg R = 2^m − 2 is a theorem for m ≤ 11 by finite exact check; the same identity for all m ≥ 2 remains a conjecture. Structural exact checks (m ≤ 8): d_0 = m − 1, d_r = 2 d_{r−1} − (m − r − 1), R ∈ GF(2^e)[x²]. No counterexample found.
- Range unchanged: smallest open length still 47 = 32 + 15 (excess 15); exact h_n for 3 ≤ n ≤ 48. Closing excess 11 does **not** move that range.
- No literature opened; no novelty claimed. Not a consequence: no W selected, no continuum limit, force, stress, or momentum.


## Progress this run (2026-10-15 ~2:30am EDT / hourly routine: lifted `direct`, excess m=11 at p=256)

Dated 2026-10-15 (America/New_York).

- Record current before this run: head 92ad7bd; excess ≤ 10 is a theorem; excess 11 had filter + directs through p = 128; directs at p = 256, 512, 1024 pending. The `direct 11 256 orbit` run had been killed by box restarts (one at ≈ 02:01 EDT during this run); its log was empty.
- **Lemma (recorded in README "Residue condition: excess m=11, lifted form of `direct` (2026-10-15)")**: the chains counted by `direct` are exactly those attached to roots of the factors that `filter` reports as surviving (uses only the recorded elimination lemma), and by the action of Frobenius^e one root per surviving factor decides whether S = 0 occurs. New script scripts/check_residue_lifted.py (`prepare`, `lift all|rep|verify`; resumable per-prefix cache).
- **Controls (exact)**: `prepare 11` reproduces the 2026-10-09 filter survivor counts; `lift all` reproduces the recorded `direct` counts in 10 small cases (m = 3..7, p ≤ 32), at m=7 p=256 (k=263), and at m=11 p = 16, 32, 64, 128 (p=128: 1170 s vs 11769 s); `verify` at m=11 p = 32, 64 finds equal per-root counts (4096, 2, 0) within every factor.
- **Exact finite computation**: m=11, p=256 (k=267), `rep`: 5 factors, 20480 chains, 10 with S ∈ GF(2^p), **0 with S = 0**. So S_267 ≠ 0 on every chain.
- **Pending (do not claim excess ≤ 11)**: p=512 (k=523) and p=1024 (k=1035) `rep` runs in progress at write-up.
- Range unchanged: smallest open length 47; exact h_n for 3 ≤ n ≤ 48.
- No literature opened; no novelty claimed. Not a consequence: no W selected, no continuum limit, force, stress, or momentum.

## Progress this run (2026-10-09 ~3:55am EDT / hourly routine: excess m=11 filter + directs through p=128)

Dated 2026-10-09 (America/New_York), first run of the day (hourly locked-kernel routine, Phase A documentation only).

- **Progress / exact finite computation** (not a theorem covering all excess 11): scripts/check_residue_p_plus_m.py (python-flint), filter and direct modes, orbit-reduced where noted. Scratch logs under `/workspace/scratch-res/` (repo_filter_m11.log, indep_excess_filter_m11.log, repo_direct_m11_p{16,32,64,128}.log). Not vendored into the tree (prior practice).
- Filter m=11 (orbit, e=16, prefixes=128): R ≠ 0 on every prefix, degR=2046. Power-of-two-degree factors (p: count) = {16: 259, 32: 64, 64: 37, 128: 12, 256: 7, 512: 5, 1024: 2}. Surviving chain condition (p: count) = {16: 66, 32: 24, 64: 21, 128: 6, 256: 5, 512: 3, 1024: 1}. Wall time ≈ 1511 s (independent filter agrees: R_zero=0, same survivor counts, ≈ 1551 s).
- Exact direct zeros (orbit mode, S = 0 count = 0, EXIT:0) at:
  - p=16 → k=27: adm_c=65, chains=266240, S_in_GF=132, S=0=0, t=520.5s
  - p=32 → k=43: adm_c=48, chains=196608, S_in_GF=96, S=0=0, t=2905.9s
  - p=64 → k=75: adm_c=84, chains=344064, S_in_GF=168, S=0=0, t=2842.3s
  - p=128 → k=139: adm_c=48, chains=196608, S_in_GF=96, S=0=0, t=11769.0s
- **Pending (do not claim excess ≤ 11 yet):** directs at p=256 (k=267), p=512 (k=523), p=1024 (k=1035). Until those S=0 counts are 0, excess ≤ 11 is **not** proved. At documentation time, `direct 11 256 orbit` was still running; p=512 and p=1024 not started.
- Range unchanged: smallest open length still 47 = 32 + 15; exact h_n for 3 ≤ n ≤ 48.
- Assumptions / theorems / numerical checks kept separate. No novelty claim. Not a consequence: no W selected, no continuum limit, force, stress, or momentum.

## Proved this run (2026-10-08, tenth run: residue lengths 2^j + m, 3 ≤ m ≤ 10)

Dated 2026-10-08 (America/New_York).

- Lemma (README "Residue condition: lengths 2^j + m for 3 ≤ m ≤ 10 (elimination over a fixed field)"): for fixed m, with e = 2^⌈log2(m+1)⌉, the z_p-coordinate equation C_1 = 0 of the ninth run clears to an element G of a rank-2^{m−1} tower ring over GF(2^e)[x] that does not depend on p; its iterated relative norm R ∈ GF(2^e)[x] satisfies R(α_1) = 0 on any chain with S_{p+m} ∈ GF(2^p). If R ≠ 0 for the prefix, such a chain forces α_1 into an irreducible factor of degree d with p = e·d (because c = z_1(α_1² + α_1) = z_{p−1} has degree exactly p) and the chain condition N^{p−1−m}(c) = z_m modulo that factor.
- Finite exact computation (scripts/check_residue_p_plus_m.py, python-flint 0.9.0): R ≠ 0 on every prefix for m ≤ 10; surviving p as in the README table. Exact `direct` counts of S = 0 among chains with S ∈ GF(2^p) are 0 at k = 13–15, 21–23, 38, 39, 71–74, 136–138, 263–266, 520 (this-run script for the mid-range lengths; matching orbit-reduced scratch logs for 263, 265, 520, 74, 138, 266). Positive control against naive enumeration for k = 6, 7, 11–15 (counts 8, 0, 32, 0, 48, 32, 176 match).
- Theorem: S_k ≠ 0 for every chain whenever k − 2^⌊log2 k⌋ ≤ 10. With the earlier lemmas (excess 0, 1, 2), every such k is proved. First lengths newly covered by a proof: 67–74, 131–138, 263–266, 520, ….
- Pending: none for excess ≤ 10. Observation only: m = 11 filter has finite survivors including p = 1024; not closed this run.
- Range unchanged: the smallest open length is still 47 = 32 + 15, so exact h_n holds for 3 ≤ n ≤ 48.
- Observation only: deg R = 2^m − 2 on every prefix checked (m ≤ 9).
- No literature opened; no novelty claimed. Not a consequence: no W selected, no continuum limit, force, stress, or momentum.

## Proved previously (2026-10-08, ninth run: residue lengths 2^j + 2)

Dated 2026-10-08 (America/New_York).

- Lemma (README "Residue condition: lengths 2^j + 2 (relative-trace argument)"): for every j ≥ 3 and every chain, S_{2^j+2} ∉ GF(2^{2^j}); in particular S_{2^j+2} ≠ 0. With k = 4 (power of two) and k = 6 (finite check), S_k ≠ 0 for every k = 2^j + 2, j ≥ 1.
- Proof structure: with p = 2^j, c = z_{p−1} (degree exactly p), α_i = z_{p+i} + z_i z_p ∈ GF(2^p) (fixed by σ = F^p), the relations α_i² + α_i = α_{i−1} + c z_i² and the relative norms Nm(z_{p+1}) = z_1² α_1, Nm(z_{p+2}) = α_1 + (1 + z_2) α_2 make the z_p-coordinate of S_{p+2} equal to C_1 = z_1²/(α_1 + 1) + z_2/(α_1 + (1 + z_2) α_2). C_1 = 0 is linear in α_2; substituting into the α_2 relation gives a quadratic in α_1 over GF(16) whose linear coefficient is 0 and whose constant μ² + μ is nonzero, so α_1 ∈ GF(16), hence c ∈ GF(16), contradicting deg c = p ≥ 8.
- This resolves the case left without a conclusion in the eighth run (the two equations over GF(2^p) for k = 2^j + 2): the z_p-coefficient equation alone is already incompatible for j ≥ 3.
- Supporting exact checks (scripts/check_residue_p_plus_two.py, GF(2^64)): all identities on every chain for k = 6, 10 and on one chain per Frobenius orbit for k = 18; counts of S_{p+2} ∈ GF(2^p) are 8, 0, 0 (k = 6 reproduces the fifth run); α_1 ∈ GF(16) wherever C_1 = 0. Not a substitute for the proof.
- Range unchanged: the smallest open length is still 47, so exact h_n holds for 3 ≤ n ≤ 48. New proved lengths beyond computation: k = 66, 130, 258, ….
- Recorded as a strategy only (not proved): for k = 2^j + m the same coordinates give m equations in α_1, …, α_m; if that system is zero-dimensional for a fixed m, the argument would cover all large j. Not checked for any m ≥ 3, and it could not cover all k.
- Still open: the residue conjecture for k ≥ 47 with k ∉ {2^j, 2^j + 1, 2^j + 2}, hence exact h_n for n ≥ 49.
- No literature opened; no novelty claimed. Not a consequence: no W selected, no continuum limit, force, stress, or momentum.

## Proved previously (2026-10-08, eighth run: residue check to k = 46, no monomial trace certificate)

Dated 2026-10-08 (America/New_York).

- Finite exact computation (README "Residue condition: exact check to k = 46 and no monomial trace certificate"): the unchanged Frobenius-reduced walk scripts/residue_orbits_gf2_64.c, run with KMAX = 46 in GF(2^64), finds S_k ≠ 0 at every reduced chain for 1 ≤ k ≤ 46 (2^40 representatives at k = 46, covering all 2^46 chains; 35.5 min wall, 230 CPU-min).
- Corollary (two-adic reduction theorem + orbit lemma + this computation): the smallest open length is 47, so a coincidental hit needs n ≥ 49, and h_n = 1 − μ_exc(n) − 5·2^n/(3^{n+1}+3) exactly for 3 ≤ n ≤ 48 (previously n ≤ 47).
- Negative result (scripts/check_residue_trace_monomials.py, exhaustive for k ≤ 8): no certificate Tr_d(f·S_k) = 1 with f = z_k^a z_{k−1}^b or (z_k+1)^a z_{k−1}^b, |a| ≤ 6, |b| ≤ 4, holds for all 2 ≤ k ≤ 8; k = 6 and 7 admit none at all. Only this family is ruled out.
- Recorded without a conclusion: for k = 2^j + 2 (j ≥ 2) the condition S_k = 0 splits into two equations over GF(2^{2^j}); their incompatibility was not shown.
- Still open: the residue conjecture for k ≥ 47 with k ∉ {2^j, 2^j + 1} (equivalently gcd(N^k + 1, Π_k′) = 1), hence exact h_n for n ≥ 49.
- No literature opened; no novelty claimed. Not a consequence: no W selected, no continuum limit, force, stress, or momentum.

## Proved previously (2026-10-08, seventh run: logarithmic-derivative form, F_2[t] gcd certificate)

Dated 2026-10-08 (America/New_York).

- Lemma (README "Residue condition: logarithmic-derivative form and a polynomial gcd certificate"): with A_k = N^k(t) + 1 and Π_k = ∏_{j<k} N^j(t), S_k = Π_k′(z_k)/Π_k(z_k) because every N^j is additive with derivative 1; the product of Π_k over all chain endpoints is 1, so the norm of S_k is Res(A_k, Π_k′) and the number of chains with S_k = 0 is deg gcd(A_k, Π_k′). Also Π_k = a_k² + t b_k² with an explicit recursion, and Π_k′ = b_k².
- Corollary (exact reformulation): the residue condition at length k ⇔ gcd(N^k + 1, Π_k′) = 1 in F_2[t]. For k = 2^B − 1 the chain endpoints are exactly the trace-one elements of GF(2^{2^B}).
- Finite exact computation (scripts/check_residue_logderiv.py): the identities checked at all chains (k ≤ 8) and as polynomials (k ≤ 12); positive control of the gcd count against enumeration for 31 shifted targets, k ≤ 10 (17 nonzero cases, all match); gcd = 1 for k ≤ 21, an independent re-derivation of S_k ≠ 0 there with no chain enumeration.
- Negative results recorded: the (a_k, b_k) recursion evaluated along a chain is tautological (it unwinds to S_{k−1} = 1/z_k); schoolbook gcd is ~2^{2k}, so it does not extend the k ≤ 45 range. Euclid step counts and stable top segments of the remainder sequence recorded as a numerical observation only.
- Range unchanged: exact h_n for 3 ≤ n ≤ 47. Still open: the residue conjecture for k ≥ 46 with k ∉ {2^j, 2^j + 1}, equivalently gcd(N^k + 1, Π_k′) = 1.
- No literature opened; no novelty claimed. Not a consequence: no W selected, no continuum limit, force, stress, or momentum.

## Proved previously (2026-10-08, sixth run: Frobenius orbit reduction, residue check to k = 45)

Dated 2026-10-08 (America/New_York).

- Lemma (README "Residue condition: Frobenius orbit reduction and exact check to k = 45"): for each k, with B = ⌈log₂(k+1)⌉, every Frobenius orbit of length-k chains has exactly 2^B elements, S_k(F chain) = S_k(chain)², and keeping one arbitrary child at every power-of-two depth (both children elsewhere) gives exactly one chain per orbit. So S_k ≠ 0 for all chains iff it holds on these 2^{k−B} representatives, and one reduced tree walk checks all k ≤ K.
- Proof structure: a chain is fixed by z_k, whose degree over F_2 is 2^B because z_k ∈ GF(2^{2^a}) = ker N^{2^a} iff k + 1 ≤ 2^a; σ_b = F^{2^b} = N^{2^b} + 1 fixes the chain below depth 2^b and swaps the depth-2^b entry with its sibling; apply σ_b for b increasing; count orbits.
- Finite exact computation (scripts/check_residue_orbits.py driving scripts/residue_orbits_gf2_64.c, GF(2^64)): S_k ≠ 0 on every reduced chain for 1 ≤ k ≤ 45 (2^39 representatives at k = 45). The reduction was checked exactly: Galois-invariant Tr_d(S_k) = 1 counts agree between full enumeration in GF(2^64) and GF(2^32) (Python, k ≤ 11) and satisfy full = 2^B · reduced in C for k ≤ 22.
- Corollary: S_k ≠ 0 for all k ≤ 45 and all k = 2^j, 2^j + 1; the smallest open length is 46, so a coincidental hit needs n ≥ 48, and h_n = 1 − μ_exc(n) − 5·2^n/(3^{n+1}+3) exactly for 3 ≤ n ≤ 47 (previously n ≤ 35).
- Negative remark: the reduction saves only the factor 2^{⌈log₂(k+1)⌉}; it does not prove the conjecture, and the exhaustive cost stays exponential in k.
- Still open: the residue conjecture for k ≥ 46 with k not of the form 2^j or 2^j + 1, hence the exact h_n formula for n ≥ 48.
- No literature opened; no novelty claimed. Not a consequence: no W selected, no continuum limit, force, stress, or momentum.

## Proved previously (2026-10-08, fifth run: residue lengths 2^j + 1)

Dated 2026-10-08 (America/New_York).

- Lemma (README "Residue condition: lengths 2^j + 1 and the limits of the subfield test"): for every j ≥ 1 and every chain z_0 = 1, z_i² + z_i = z_{i−1} over the algebraic closure of F_2, S_{2^j+1} = Σ_{i=1}^{2^j+1} 1/z_i ≠ 0.
- Proof structure: the pairing identity 1/z_{i−1} + 1/z_i = 1/(z_i + 1) gives S_{p+1} = S_{p−1} + 1/(z_{p+1} + 1) with p = 2^j; S_{p−1} lies in GF(2^p) = ker N^p, while N^p(z_{p+1} + 1) = z_1 ≠ 0, so S_{p+1} ∉ GF(2^p).
- Corollary: S_k ≠ 0 for all k ≤ 33 (k = 33 = 2^5 + 1 is new) and for all k = 2^j, 2^j + 1; a coincidental hit needs n ≥ 36, so h_n = 1 − μ_exc(n) − 5·2^n/(3^{n+1}+3) exactly for 3 ≤ n ≤ 35 (previously n ≤ 34).
- Negative result recorded: the stronger property S_k ∉ GF(2^p) fails for k = 6, 11, 13, 14, 15 (8, 32, 48, 32, 176 chains), so that test cannot prove the conjecture in general. Reformulation as a norm condition G_k(1, 0) = 1 recorded and checked for k ≤ 7; no closed form found.
- Supporting check: scripts/check_residue_p_plus_one.py (GF(2^64), exhaustive, k ≤ 14; not a test).
- Still open: the residue conjecture for k ≥ 34 with k not of the form 2^j or 2^j + 1, hence the exact h_n formula for n ≥ 36.
- No literature opened; no novelty claimed. Not a consequence: no W selected, no continuum limit, force, stress, or momentum.

## Proved previously (2026-10-08, fourth run: residue condition to k = 32 and all powers of two)

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
- Coincidental hits among corner-visible eigenvalues (updated tenth run: S_k ≠ 0 proved whenever k − 2^⌊log2 k⌋ ≤ 10 by elimination over a fixed field; range unchanged, open for k ≥ 47 with excess ≥ 11; ninth run: S_k ≠ 0 proved for every k = 2^j + 2, range unchanged, open for k ≥ 47 not of the form 2^j, 2^j + 1, 2^j + 2; eighth run: S_k ≠ 0 for all k ≤ 46 by the reduced walk, exact h_n for 3 ≤ n ≤ 48, open for k ≥ 47 not of the form 2^j or 2^j + 1; no monomial trace certificate for k ≤ 8; seventh run: exact reformulation as gcd(N^k + 1, Π_k′) = 1 in F_2[t], independent gcd certificate for k ≤ 21, range unchanged; sixth run: Frobenius orbit reduction, S_k ≠ 0 for all k ≤ 45, exact h_n for 3 ≤ n ≤ 47, open for k ≥ 46 not of the form 2^j or 2^j + 1; fifth run: lengths 2^j + 1 proved, exact h_n for 3 ≤ n ≤ 35): excluded for 3 ≤ n ≤ 11 by an exact finite certificate (2026-10-08, corner channels), and for 3 ≤ n ≤ 18 by the two-adic reduction plus a residue check for k ≤ 16 (2026-10-08, third run); for general n this is reduced to the residue conjecture Σ 1/z_i ≠ 0 in characteristic 2, which is open. Fourth run: the residue condition holds for all k ≤ 32 and every power of two k, so exact h_n now holds for 3 ≤ n ≤ 34; open for k ≥ 33 not a power of two.
- Elementary proof of DN_n(2) = 0 (n ≥ 3) without Qiu §2: done (2026-10-08, from c_n = 5·2^{n−1}+1 via corner channels).

Addendum (2026-10-22 ~2:57pm EDT, no new result). Both running lift jobs, m = 13 p = 256 (k = 269, started 13:58 EDT) and m = 12 p = 2048 (k = 2060, restarted 00:58 EDT), received SIGTERM at 14:20:50 EDT (EXIT:143) and produced no result. No statement about S_269 or S_2060 is made. Both were restarted at 14:56 EDT with the same command (`check_residue_lifted.py lift <json> <p> rep`, python-flint 0.9.0), logs appended to `/workspace/scratch-res/lifted_rep_m13_p256.log` and `/workspace/scratch-res/lifted_rep_m12_p2048.log`. k = 4108 remains unstarted. Range unchanged: S_k ≠ 0 for k ≤ 49 and for the isolated lengths already recorded (77, 141, and the residue/survivor exclusions), exact h_n for 3 ≤ n ≤ 51; smallest open length 50.

Addendum (2026-10-22 ~3:53pm EDT, no new result). The lifts m = 13 p = 256 (k = 269) and m = 12 p = 2048 (k = 2060) are running with no result yet; the process table shows both started at 15:23 EDT (the 14:56 EDT launches are no longer present and left no EXIT line, so the current runs are counted from 15:23). No statement about S_269 or S_2060 is made. To attack the smallest open length directly, the Frobenius-orbit-reduced walk `scripts/residue_orbits_gf2_64 50` (OMP_NUM_THREADS=6) was started at 15:53 EDT, log `/workspace/scratch-res/walk50.log`; at KMAX = 49 it took about 8 h on 8 threads, so roughly a day is expected. If it exits 0 with zeros = 0 at k = 50, that is an exact finite check giving S_50 ≠ 0 and exact h_n for 3 ≤ n ≤ 52; until then nothing is claimed. k = 4108 remains unstarted. Range unchanged: S_k ≠ 0 for k ≤ 49 and the isolated lengths already recorded, exact h_n for 3 ≤ n ≤ 51; smallest open length 50.

Addendum (2026-10-23 ~7:53am EDT, no new result). The lifts m = 13 p = 512 (k = 525, running since 00:55 EDT) and m = 12 p = 2048 (k = 2060) are still running with no result or EXIT line; no statement about S_525 or S_2060 is made. To attack the smallest open length, the Frobenius-orbit-reduced walk `scripts/residue_orbits_gf2_64 51` (OMP_NUM_THREADS=6) was started at 07:52 EDT, log `/workspace/scratch-res/walk51.log`. KMAX = 50 took about 14 h, so roughly a day or more is expected. If it exits 0 with zeros = 0 at k = 51, that is an exact finite check giving S_51 ≠ 0 and exact h_n for 3 ≤ n ≤ 53; until then nothing is claimed. k = 4108 remains unstarted. Range unchanged: S_k ≠ 0 for 1 ≤ k ≤ 50 and the isolated lengths already recorded, exact h_n for 3 ≤ n ≤ 52; smallest open length 51.

Addendum (2026-10-29 ~12:53am EDT, no new result). The box restarted (uptime shows boot about 6:47pm EDT 2026-10-28), and all three running jobs were lost without a result or EXIT line: the reduced walk `scripts/residue_orbits_gf2_64 51` (started 2026-10-23 07:52 EDT), the lift m = 13 p = 1024 (k = 1037, started 2026-10-23 15:54 EDT), and the lift m = 12 p = 2048 (k = 2060). No statement about S_51, S_1037 or S_2060 is made. All three were restarted at 00:52 EDT 2026-10-29 with the same commands (walk with OMP_NUM_THREADS=6; lifts via `check_residue_lifted.py lift <json> <p> rep`, python-flint 0.9.0), logs appended to `/workspace/scratch-res/walk51.log`, `/workspace/scratch-res/lifted_rep_m13_p1024.log`, `/workspace/scratch-res/lifted_rep_m12_p2048.log`. The walk at KMAX = 50 took about 14 h, so KMAX = 51 is expected to need a day or more. k = 2061, 4108, 8205 remain unstarted. Range unchanged: S_k ≠ 0 for 1 ≤ k ≤ 50 and the isolated lengths already recorded (77, 141, 269, 525, and the residue/survivor exclusions), exact h_n for 3 ≤ n ≤ 52; smallest open length 51.

Addendum (2026-10-29 ~6:00pm EDT, no new result). The box restarted again (uptime shows boot about 5:39pm EDT 2026-10-29), and the three jobs restarted at 00:52 EDT were lost without a result or EXIT line: the reduced walk `scripts/residue_orbits_gf2_64 51`, the lift m = 13 p = 1024 (k = 1037), and the lift m = 12 p = 2048 (k = 2060). No statement about S_51, S_1037 or S_2060 is made. All three were restarted at about 18:00 EDT 2026-10-29 with the same commands and the same log files under `/workspace/scratch-res/`. Because repeated restarts have now cost the KMAX = 51 walk several partial runs, it would benefit from checkpointing before the next attempt; that is an engineering note, not a mathematical claim. k = 2061, 4108, 8205 remain unstarted. Range unchanged: S_k ≠ 0 for 1 ≤ k ≤ 50 and the isolated lengths already recorded, exact h_n for 3 ≤ n ≤ 52; smallest open length 51.

Addendum (2026-10-30 ~12:30am EDT, engineering change only; no mathematical claim, range unchanged). Because box restarts (2026-10-22, 2026-10-28 ~6:47pm, 2026-10-29 ~5:39pm EDT) repeatedly killed multi-day runs, checkpoint/resume tooling was added; the running jobs and the original scripts are untouched (walk binary sha256 1b35db9d…f451 unchanged). New: `scripts/residue_orbits_ckpt.c` (same reduced tree and same stdout as `residue_orbits_gf2_64`; independent units = blocks of 8 depth-24 nodes; atomic checksummed checkpoint every 300 s; `--resume`; sibling sharing num·(y+1)+den = (num·y+den)+num and 8-lane lockstep walk, about 2.8× less CPU per node in a single-thread benchmark at KMAX = 36), `scripts/check_residue_lifted_ckpt.py` (same counts and output line as `check_residue_lifted.py lift`; depth-first canonical top order, O(m) memory, chain-level checkpoint), `scripts/ensure_jobs.sh` (idempotent supervisor: relaunches a job with no live process and no EXIT line, memory-gated; job specs in `scripts/jobs/`), and `scripts/test_residue_ckpt.sh`. The test passed: stdout identical to the original binary for KMAX = 1..12, 17, 20, 29, 33, 38, with KMAX = 38 killed by SIGKILL mid-run and resumed, a stop/resume, corrupt and mismatched checkpoints refused, the m = 8 p = 32 `verify` lift identical after SIGKILL + resume, and a supervisor relaunch-and-resume. These are software tests on controls already covered by the walk; they add no new length. The box has no cron and no systemd (PID 1 is tini), so `@reboot` is not available; `ensure_jobs.sh` must be called by the hourly routine. The record walk KMAX = 51 and the lifts k = 1037, 2060 continue under the original code; nothing is claimed about S_51, S_1037 or S_2060. Range unchanged: S_k ≠ 0 for 1 ≤ k ≤ 50 and the isolated lengths already recorded, exact h_n for 3 ≤ n ≤ 52; smallest open length 51.
