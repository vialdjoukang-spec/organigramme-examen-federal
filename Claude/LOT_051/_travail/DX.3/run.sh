#!/bin/bash
cd /home/user/wt/lot-051 && export PAQUET_CACHE=/tmp/claude_paquet_cache
python3 /home/user/organigramme-examen-federal/Claude/_outils/lecon.py finir --lot 051 --cible DX.3 --titre "DX.3 — Maladie coronarienne chronique (angor stable)" 2>&1 | cut -c1-1500
