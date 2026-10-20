#!/usr/bin/env bash
# Attend TOUS les contrôles de la PR de la branche courante (ou $1) sur le commit HEAD poussé.
# Une ligne : VERT|ROUGE <détail>. VERT exige au moins un contrôle et aucun fail/pending/cancel.
set -u
b=${1:-$(git rev-parse --abbrev-ref HEAD)}
sha=$(git rev-parse --verify "refs/heads/$b" 2>/dev/null ||
      git rev-parse --verify "refs/remotes/origin/$b" 2>/dev/null) || {
  echo "ROUGE $b : branche Git introuvable"; exit 1;
}
for _ in $(seq 1 120); do
  j=$(gh pr view "$b" --json headRefOid,statusCheckRollup 2>/dev/null) || {
    echo "ROUGE $b : lecture GitHub impossible"; exit 1;
  }
  r=$(printf '%s' "$j" | python3 "$(dirname "$0")/ci_verdict.py" "$sha") ; rc=$?
  [ $rc -ne 2 ] && { echo "$r $b"; exit $rc; }
  sleep 20
done
echo "ROUGE $b : délai dépassé"; exit 1
