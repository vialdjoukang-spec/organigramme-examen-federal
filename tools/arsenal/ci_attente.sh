#!/usr/bin/env bash
# Attend la CI de la branche courante (ou $1) et n'affiche qu'une ligne : VERT|ROUGE <job en échec>.
set -u
b=${1:-$(git rev-parse --abbrev-ref HEAD)}
for i in $(seq 1 30); do id=$(gh run list -b "$b" -w CI -L1 --json databaseId -q '.[0].databaseId' 2>/dev/null); [ -n "$id" ] && break; sleep 10; done
[ -z "${id:-}" ] && { echo "AUCUNE CI pour $b"; exit 2; }
if gh run watch "$id" --exit-status -i 20 >/dev/null 2>&1; then echo "VERT $b run $id"
else echo "ROUGE $b run $id : $(gh run view "$id" --json jobs -q '[.jobs[]|select(.conclusion=="failure")|.name]|join(",")')"; exit 1; fi
