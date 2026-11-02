#!/bin/bash
# prep_lot2.sh NNN : worktree ../wd-NNN depuis origin/main (branche corr2/lot-NNN-opus) pour le passage correcteur Opus. Gratuit.
set -e; N=$1; R=$(cd "$(dirname "$0")/../.." && pwd); cd "$R"; git fetch -q origin main
git worktree add -q -B corr2/lot-$N-opus ../wd-$N origin/main 2>/dev/null || true
echo "wd-$N prêt"
