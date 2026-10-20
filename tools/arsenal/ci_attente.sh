#!/usr/bin/env bash
# Attend TOUS les contrôles de la PR de la branche courante (ou $1) ; une ligne : VERT|ROUGE <contrôles en échec>.
set -u
b=${1:-$(git rev-parse --abbrev-ref HEAD)}
sleep 15
gh pr checks "$b" --watch -i 20 >/dev/null 2>&1
f=$(gh pr checks "$b" 2>/dev/null | awk -F'\t' '$2=="fail"{print $1}' | paste -sd, -)
p=$(gh pr checks "$b" 2>/dev/null | awk -F'\t' '$2=="pending"{print $1}' | paste -sd, -)
[ -z "$f" ] && [ -z "$p" ] && { echo "VERT $b"; exit 0; }
echo "ROUGE $b : ${f:-} ${p:+en attente: $p}"; exit 1
