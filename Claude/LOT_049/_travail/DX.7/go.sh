#!/bin/bash
cd /home/user/wt/lot-049
export PAQUET_CACHE=/tmp/claude_paquet_cache
python3 Claude/LOT_049/_travail/DX.7/ecrire.py | tr '\n' ' '; echo
python3 /home/user/organigramme-examen-federal/Claude/_outils/lecon.py finir --lot 049 --cible DX.7 --titre "DX.7 — Embolie pulmonaire" --ex ${1:-6}
