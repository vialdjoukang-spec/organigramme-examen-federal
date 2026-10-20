#!/usr/bin/env bash
# Attend TOUS les contrôles de la PR de la branche courante (ou $1) sur le commit HEAD poussé.
# Une ligne : VERT|ROUGE <détail>. VERT exige au moins un contrôle et aucun fail/pending/cancel.
set -u
b=${1:-$(git rev-parse --abbrev-ref HEAD)}
sha=$(git rev-parse "origin/$b" 2>/dev/null || git rev-parse HEAD)
for _ in $(seq 1 90); do
  [ "$(gh pr view "$b" --json headRefOid -q .headRefOid 2>/dev/null)" = "$sha" ] && break; sleep 10; done
sleep 20
for _ in $(seq 1 120); do
  j=$(gh pr checks "$b" --json name,bucket 2>/dev/null) || j=''
  r=$(printf '%s' "$j" | python3 "$(dirname "$0")/ci_verdict.py") ; rc=$?
  [ $rc -ne 2 ] && { echo "$r $b"; exit $rc; }
  sleep 20
done
echo "ROUGE $b : délai dépassé"; exit 1
