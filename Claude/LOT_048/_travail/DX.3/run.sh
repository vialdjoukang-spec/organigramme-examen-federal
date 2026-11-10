#!/bin/bash
cd /home/user/wt/lot-048
export PAQUET_CACHE=/tmp/claude_paquet_cache
python3 Claude/LOT_048/_travail/DX.3/build.py || exit 1
python3 /home/user/organigramme-examen-federal/Claude/_outils/lecon.py finir --lot 048 --cible DX.3 --titre "DX.3 — Œsophagite à éosinophiles" --ex ${2:-4} 2>&1 | tail -${1:-40}
