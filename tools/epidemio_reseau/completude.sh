#!/usr/bin/env bash
# Complétude épidémiologique bispatiale (Europe + Suisse, en parallèle) des DX nommés. Idempotent : reprise sur checkpoint
# (SQLite WAL, table taches, cache disque). Usage : EPI_AGENT=<IA> EPI_SORTIE=<IA>/<IA>__Completude_Epidemio bash tools/epidemio_reseau/completude.sh
set -euo pipefail
ICI="$(cd "$(dirname "$0")" && pwd)"
export EPI_DEPOT="$(git -C "$ICI" rev-parse --show-toplevel)"
export EPI_SORTIE="$(cd "${EPI_SORTIE:?EPI_SORTIE = dossier propre de l IA}" && pwd)" EPI_PLAN="${EPI_SORTIE}"
mkdir -p "$EPI_SORTIE/out"; cd "$ICI"
python3 -c "import requests, openpyxl" 2>/dev/null || python3 -m pip install -q --user requests openpyxl
for t in tests/test_*.py; do python3 "$t" >/dev/null; done                  # règles et garde-fous
python3 scripts/connecteurs.py                                               # sources suisses (OFS, OFSP-IDD, ONEC, Obsan)
python3 scripts/pipeline.py                                                  # valeurs suisses du réseau (reprise : DX déjà faits sautés)
python3 scripts/applicabilite.py >/dev/null                                  # classes A/B/C/N
python3 scripts/eurostat_cod.py                                              # Eurostat causes de décès : UE-27 (Europe) et Suisse, même définition CIM-10
python3 scripts/eurostat_ehis.py                                             # Eurostat EHIS 2019 : prévalence déclarée UE-27 (Europe)
python3 scripts/recherche.py                                                 # Europe + Suisse en parallèle, tâches « à faire » seulement
python3 scripts/plan.py                                                      # PLAN_COMPLETUDE_EPIDEMIO.{html,md} + taches.jsonl
echo "Plan : $EPI_SORTIE/PLAN_COMPLETUDE_EPIDEMIO.html"
echo "Suite : lire les « candidats à lire » et enregistrer chaque valeur avec scripts/valider.py (contexte complet obligatoire)."
