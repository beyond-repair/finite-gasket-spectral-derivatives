#!/usr/bin/env bash
# Supervisor for long residue computations (engineering only; no mathematical content).
# Idempotent: safe to call from an hourly routine, at login, or by hand.
#
# For every JOBS_DIR/*.job (default /workspace/scratch-res/jobs) it sources the shell
# variables  NAME  DIR  CMD  LOG  MATCH  MIN_AVAIL_MB  [ENABLED=1]  and then:
#   * finished : LOG has an "EXIT:" line after the last "started"/"restart" line -> skip;
#   * alive    : a process whose command line contains MATCH exists           -> skip;
#   * dead     : MemAvailable >= MIN_AVAIL_MB  -> append "restart <date> by ensure_jobs
#                (no live process, no EXIT line)" to LOG and relaunch
#                  setsid nohup bash -c 'cd DIR; CMD >> LOG 2>&1; echo EXIT:$? >> LOG; date >> LOG'
#                otherwise report "deferred (low memory)".
# Jobs are launched one per call at most when memory is tight (MemAvailable re-read after
# each launch, with a short pause).  A checkpointed CMD (residue_orbits_ckpt ... --resume,
# check_residue_lifted_ckpt.py ... --resume) continues from its checkpoint; a plain CMD
# starts over.  Use  --dry-run  to only report.
set -u
JOBS_DIR=${JOBS_DIR:-/workspace/scratch-res/jobs}
DRY=0; [ "${1:-}" = "--dry-run" ] && DRY=1
exec 9>"$JOBS_DIR/.ensure_v2.lock" || exit 1
# (v2 lock name: the pre-2026-10-30 version leaked fd 9 into launched jobs, so the old
#  .ensure.lock stays held by the running walk51_ckpt wrapper; children now get 9>&-.)
flock -n 9 || { echo "ensure_jobs: another instance is running"; exit 0; }
avail() { awk '/MemAvailable/ {print int($2/1024)}' /proc/meminfo; }
rc=0
for jf in "$JOBS_DIR"/*.job; do
  [ -e "$jf" ] || continue
  NAME= DIR= CMD= LOG= MATCH= MIN_AVAIL_MB=0 ENABLED=1
  # shellcheck disable=SC1090
  . "$jf"
  [ "$ENABLED" = 1 ] || { echo "$NAME: disabled"; continue; }
  last=$(grep -nE '(started|restart)' "$LOG" 2>/dev/null | tail -1 | cut -d: -f1); last=${last:-0}
  if tail -n +"$((last + 1))" "$LOG" 2>/dev/null | grep -q '^EXIT:'; then
    echo "$NAME: finished ($(tail -n +"$((last + 1))" "$LOG" | grep '^EXIT:' | tail -1))"; continue
  fi
  if pgrep -f -- "$MATCH" > /dev/null; then
    echo "$NAME: alive (pid $(pgrep -f -- "$MATCH" | grep -v "^$$\$" | tr '\n' ' '))"; continue
  fi
  a=$(avail)
  if [ "$a" -lt "$MIN_AVAIL_MB" ]; then
    echo "$NAME: DEAD, deferred (MemAvailable ${a} MB < ${MIN_AVAIL_MB} MB)"; rc=2; continue
  fi
  if [ $DRY = 1 ]; then echo "$NAME: DEAD, would relaunch: $CMD"; continue; fi
  echo "restart $(date) by ensure_jobs (no live process, no EXIT line since line $last)" >> "$LOG"
  echo "$NAME started $(date) by ensure_jobs: $CMD" >> "$LOG"
  setsid nohup bash -c "cd '$DIR' && $CMD >> '$LOG' 2>&1; echo EXIT:\$? >> '$LOG'; date >> '$LOG'" \
    > /dev/null 2>&1 < /dev/null 9>&- &
  echo "$NAME: relaunched (MemAvailable was ${a} MB)"
  sleep 20
done
exit $rc
