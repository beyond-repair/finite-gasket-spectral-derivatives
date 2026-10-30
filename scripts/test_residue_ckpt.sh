#!/usr/bin/env bash
# Test of checkpoint/resume and of the supervisor (engineering only).
#   1. residue_orbits_ckpt vs the original residue_orbits_gf2_64: identical stdout for
#      KMAX = 1..12, 17, 20, 29, 33 and K (default 38), with K run killed by SIGKILL
#      mid-run and resumed, plus a --stop-after-units stop/resume.
#   2. corrupt or mismatched checkpoints are refused.
#   3. check_residue_lifted_ckpt.py vs check_residue_lifted.py lift (time= stripped) on
#      lifted_m8.json p=32 verify, with SIGKILL mid-run and --resume.
#   4. ensure_jobs.sh relaunches a killed checkpointed walk, which resumes and matches.
# Usage: scripts/test_residue_ckpt.sh [K] [THREADS]      (exit 0 = all passed)
set -u
cd "$(dirname "$0")/.."
K=${1:-38}; TH=${2:-2}; S=/workspace/scratch-res
T=$(mktemp -d /tmp/ckpt-test.XXXX); fail=0
pass() { echo "PASS $*"; }; bad() { echo "FAIL $*"; fail=1; }
gcc -O3 -march=native -fopenmp -o "$T/orig" scripts/residue_orbits_gf2_64.c
gcc -O3 -march=native -fopenmp -o "$T/ck" scripts/residue_orbits_ckpt.c
for k in 1 2 3 4 5 6 7 8 9 10 11 12 17 20 29 33; do
  "$T/orig" $k > "$T/o" ; "$T/ck" $k > "$T/n" 2>/dev/null
  cmp -s "$T/o" "$T/n" || bad "KMAX=$k differs"
done; [ $fail = 0 ] && pass "KMAX 1..12,17,20,29,33 identical to original"
OMP_NUM_THREADS=$TH "$T/orig" $K > "$T/oK"
OMP_NUM_THREADS=$TH "$T/ck" $K --ckpt "$T/c.bin" --interval 1 > "$T/killed" 2>"$T/e1" & P=$!
sleep $(( K >= 38 ? 6 : 1 )); kill -9 $P 2>/dev/null; wait $P 2>/dev/null
grep -q checkpoint "$T/e1" && [ ! -s "$T/killed" ] && pass "SIGKILL mid-run after $(grep checkpoint "$T/e1" | tail -1 | sed 's/# //')" || bad "kill step (no checkpoint before kill or run finished)"
OMP_NUM_THREADS=$TH "$T/ck" $K --ckpt "$T/c.bin" --resume > "$T/r" 2>"$T/e2"
cmp -s "$T/oK" "$T/r" && pass "KMAX=$K killed+resumed identical to original ($(head -1 "$T/e2" | sed 's/# //'))" || bad "KMAX=$K resume differs"
rm -f "$T/c.bin"
OMP_NUM_THREADS=$TH "$T/ck" $K --ckpt "$T/c.bin" --stop-after-units 2000 > /dev/null 2>&1; s=$?
OMP_NUM_THREADS=$TH "$T/ck" $K --ckpt "$T/c.bin" --resume > "$T/r2" 2>/dev/null
[ $s = 75 ] && cmp -s "$T/oK" "$T/r2" && pass "KMAX=$K stop-after-units + resume identical" || bad "stop/resume"
cp "$T/c.bin" "$T/x.bin"; printf 'X' | dd of="$T/x.bin" bs=1 seek=200 conv=notrunc 2>/dev/null
"$T/ck" $K --ckpt "$T/x.bin" --resume > /dev/null 2>&1; [ $? = 4 ] && pass "corrupt checkpoint refused" || bad "corrupt accepted"
"$T/ck" $((K-1)) --ckpt "$T/c.bin" --resume > /dev/null 2>&1; [ $? = 4 ] && pass "mismatched checkpoint refused" || bad "mismatch accepted"
# 3. lift
L="$S/lifted_m8.json 32 verify"
if [ -e $S/lifted_m8.json ]; then
  o=$(python3 scripts/check_residue_lifted.py lift $L | sed 's/time=[0-9.]*s//')
  python3 scripts/check_residue_lifted_ckpt.py $L --ckpt "$T/l.ck" --interval 0.5 > /dev/null 2>&1 & P=$!
  sleep 6; kill -9 $P 2>/dev/null; wait $P 2>/dev/null
  n=$(python3 scripts/check_residue_lifted_ckpt.py $L --ckpt "$T/l.ck" --resume 2>"$T/le" | sed 's/time=[0-9.]*s//')
  grep -q resumed "$T/le" && [ "$o" = "$n" ] && pass "lift m=8 p=32 verify killed+resumed identical ($(sed 's/# //' "$T/le"))" || bad "lift resume: '$o' vs '$n'"
else echo "SKIP lift test ($S/lifted_m8.json missing)"; fi
# 4. supervisor
mkdir -p "$T/jobs"; cat > "$T/jobs/t.job" <<J
NAME=tjob
DIR=$PWD
CMD='OMP_NUM_THREADS=$TH $T/ck $K --ckpt $T/s.bin --resume --interval 1'
LOG=$T/s.log
MATCH='$T/ck $K --ckpt $T/s.bin'
MIN_AVAIL_MB=50
J
echo "tjob started $(date)" > "$T/s.log"
JOBS_DIR="$T/jobs" scripts/ensure_jobs.sh > "$T/sup1"; sleep 6; pkill -9 -f "$T/ck $K --ckpt $T/s.bin"; sleep 1
JOBS_DIR="$T/jobs" scripts/ensure_jobs.sh > "$T/sup2"
while pgrep -f "$T/ck $K --ckpt $T/s.bin" > /dev/null; do sleep 2; done
JOBS_DIR="$T/jobs" scripts/ensure_jobs.sh > "$T/sup3"
grep '^k=' "$T/s.log" > "$T/sk"
grep -q relaunched "$T/sup1" && grep -q relaunched "$T/sup2" && grep -q finished "$T/sup3" && grep -q resumed "$T/s.log" && cmp -s "$T/oK" "$T/sk" \
  && pass "ensure_jobs: dead job relaunched, resumed after SIGKILL, finished detected, output identical" || { bad "supervisor"; cat "$T"/sup*; }
echo "workdir $T"; [ $fail = 0 ] && echo "ALL PASSED" || echo "SOME FAILED"; exit $fail
