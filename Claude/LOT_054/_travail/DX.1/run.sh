#!/bin/bash
export PAQUET_CACHE=/tmp/claude_paquet_cache
cd /home/user/wt/lot-054
(cd Claude/LOT_054/_travail/DX.1 && python3 build.py)
python3 /home/user/organigramme-examen-federal/Claude/_outils/lecon.py finir --lot 054 --cible DX.1 --ex 200 --titre "DX.1 — Hernie de la paroi abdominale (inguinale, ombilicale, incisionnelle)" > /tmp/claude-0/-home-user/15c9849e-78d1-5a00-9dcf-bd21b180736d/scratchpad/fin.txt 2>&1
(cd Claude/LOT_054/_travail/DX.1 && python3 rep.py)
