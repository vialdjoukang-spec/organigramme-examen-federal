#!/bin/bash
cd /home/user/wt/lot-048
export PAQUET_CACHE=/tmp/claude_paquet_cache
python3 Claude/LOT_048/_travail/DX.6/build.py 2>&1 | tail -3
python3 /home/user/organigramme-examen-federal/Claude/_outils/lecon.py finir --lot 048 --cible DX.6 --titre "DX.6 — Cancer de la cavité buccale et du pharynx" 2>&1 | tail -${1:-40}
