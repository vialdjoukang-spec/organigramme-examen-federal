#!/bin/bash
cd /home/user/wt/lot-048
export PAQUET_CACHE=/tmp/claude_paquet_cache
python3 Claude/LOT_048/_travail/DX.1/build_wrap.py 2>&1 | tail -3
python3 /home/user/organigramme-examen-federal/Claude/_outils/lecon.py finir --lot 048 --cible DX.1 --titre "DX.1 — Reflux gastro-œsophagien (œsophagite peptique et sténose peptique)" 2>&1 | tail -${1:-40}
