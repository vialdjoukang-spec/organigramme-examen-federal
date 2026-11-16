#!/bin/bash
cd /home/user/wt/lot-048
export PAQUET_CACHE=/tmp/claude_paquet_cache
python3 Claude/LOT_048/_travail/DX.7/build.py 2>&1 | tail -3
python3 /home/user/organigramme-examen-federal/Claude/_outils/lecon.py finir --lot 048 --cible DX.7 --titre "DX.7 — Cancer de l'œsophage (carcinome épidermoïde et adénocarcinome)" 2>&1 | tail -${1:-40}
