#!/bin/bash
# Évaluation déterministe du LOT corrigé (outils partagés en lecture ; découpe locale qui reconnaît la SSP des fichiers AUDITÉS)
L=${1:-LOT_003}; cd /workspace/audit_1_10; PY=venv/bin/python
$PY corriges/$L/source/outils_local/decoupe_l.py ${L}_AUDITE >/dev/null && $PY outils/examens.py ${L}_AUDITE >/dev/null && $PY outils/style.py ${L}_AUDITE >/dev/null && $PY outils/score.py ${L}_AUDITE | tail -30
$PY outils/verif_v7.py corriges/$L/*AUDITÉ*.html | tail -15
