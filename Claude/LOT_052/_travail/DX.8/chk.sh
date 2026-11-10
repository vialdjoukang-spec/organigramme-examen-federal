#!/bin/bash
cd /home/user/wt/lot-052
export PAQUET_CACHE=/tmp/claude_paquet_cache
python3 Claude/LOT_052/_travail/DX.8/build_frag.py
python3 /home/user/organigramme-examen-federal/Claude/_outils/lecon.py finir --lot 052 --cible DX.8 --titre "DX.8 — Grossesse extra-utérine" 2>&1 | head -3
python3 /home/user/organigramme-examen-federal/Claude/_outils/controle3.py Claude/LOT_052/LOT_052_Phase_B_V0_DX.8.html --paquet Claude/LOT_052/_travail/DX.8/paquet.json --ex ${1:-40} > /tmp/claude-0/-home-user/15c9849e-78d1-5a00-9dcf-bd21b180736d/scratchpad/ctl.json
