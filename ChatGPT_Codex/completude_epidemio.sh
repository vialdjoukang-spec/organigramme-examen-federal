#!/usr/bin/env bash
# Complétude épidémiologique en arrière-plan : à lancer SEULEMENT après le « oui » de Vial (voir CONSIGNE_COMPLETUDE_EPIDEMIO.md).
set -euo pipefail
R="$(git -C "$(dirname "$0")" rev-parse --show-toplevel)"; OUT="$R/ChatGPT_Codex/ChatGPT_Codex__Completude_Epidemio"; mkdir -p "$OUT"
EPI_AGENT=ChatGPT_Codex EPI_SORTIE="$OUT" nohup bash "$R/tools/epidemio_reseau/completude.sh" >> "$OUT/completude.log" 2>&1 &
echo "Lancé (PID $!). Journal : $OUT/completude.log · Plan : $OUT/PLAN_COMPLETUDE_EPIDEMIO.html"
