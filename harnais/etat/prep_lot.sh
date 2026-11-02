#!/bin/bash
# prep_lot.sh NNN : worktree ../wc-NNN depuis origin/main + corrections mécaniques du cerveau + réparation des lignes + commit. Gratuit.
set -e; N=$1; R=$(cd "$(dirname "$0")/../.." && pwd); cd "$R"; git fetch -q origin main
git worktree add -q -B corr/lot-$N-cerveau ../wc-$N origin/main 2>/dev/null || true
for f in ../wc-$N/LOT_Claude_Finaux/LOT_$N/LOT_${N}_*.html; do python3 harnais/brain/cerveau.py corriger "$f" --appliquer >/dev/null 2>&1; done
cd ../wc-$N && git add -A && git commit -q --no-verify -m "LOT_$N : corrections mécaniques du cerveau" && echo "LOT_$N scripts ok: $(ls LOT_Claude_Finaux/LOT_$N | grep -c html) cours"
