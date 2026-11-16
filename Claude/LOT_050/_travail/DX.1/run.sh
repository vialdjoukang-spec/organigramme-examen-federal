#!/bin/bash
cd /home/user/wt/lot-050/Claude/LOT_050/_travail/DX.1 && python3 build.py && cd /home/user/wt/lot-050 && export PAQUET_CACHE=/tmp/claude_paquet_cache && python3 /home/user/organigramme-examen-federal/Claude/_outils/lecon.py finir --lot 050 --cible DX.1 --titre "DX.1 — Extrasystoles atriales et ventriculaires idiopathiques" --ex 3 | head -12
