#!/usr/bin/env bash
# Automate Iris · adopte la référence visuelle proposée par la CI pour une demande de fusion (skill ssp-qualite-visuelle).
# Usage : tools/visuel_reference.sh <numéro de PR>
# Conditions : l’étiquette « visuel:nouvelle-reference » est posée, et une exécution « Visuel » est terminée sur la tête de la PR.
# Effet : un seul commit explicite, « visuel: nouvelle référence », sur la branche courante (qui doit être celle de la PR).
set -euo pipefail
pr=${1:?numéro de PR}
LABEL=visuel:nouvelle-reference
read -r br sha < <(gh pr view "$pr" --json headRefName,headRefOid -q '.headRefName+" "+.headRefOid')
gh pr view "$pr" --json labels -q '.labels[].name' | grep -qx "$LABEL" || { echo "ÉCHEC : étiquette $LABEL absente sur #$pr."; exit 1; }
[ "$(git rev-parse --abbrev-ref HEAD)" = "$br" ] || { echo "ÉCHEC : placez-vous sur la branche $br."; exit 1; }
[ "$(git rev-parse HEAD)" = "$sha" ] || { echo "ÉCHEC : la branche locale n'est pas à jour avec la PR ($sha)."; exit 1; }
run=$(gh run list --workflow visuel.yml --branch "$br" --commit "$sha" --status completed --limit 1 --json databaseId -q '.[0].databaseId')
[ -n "$run" ] || { echo "ÉCHEC : aucune exécution Visuel terminée sur $sha ; attendez la CI."; exit 1; }
tmp=$(mktemp -d); trap 'rm -rf "$tmp"' EXIT
gh run download "$run" -n visuel-reference-proposee -D "$tmp"
rm -rf qa/visuel/reference && cp -r "$tmp/reference" qa/visuel/reference && cp "$tmp/reference.json" qa/visuel/reference.json
git add -A qa/visuel/reference qa/visuel/reference.json
git commit -m "visuel: nouvelle référence (PR #$pr, exécution $run)"
echo "Référence adoptée : $(ls qa/visuel/reference | wc -l) captures. Poussez : la CI compare alors en mode bloquant contre cette référence. Laissez l'étiquette jusqu'à la fusion."
