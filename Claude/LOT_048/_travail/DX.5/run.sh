#!/bin/bash
cd /home/user/wt/lot-048
export PAQUET_CACHE=/tmp/claude_paquet_cache
python3 Claude/LOT_048/_travail/DX.5/build.py
python3 /home/user/organigramme-examen-federal/Claude/_outils/lecon.py finir --lot 048 --cible DX.5 --titre "DX.5 — Anneau de Schatzki" >/dev/null 2>&1
python3 /home/user/organigramme-examen-federal/Claude/_outils/controle3.py Claude/LOT_048/LOT_048_Phase_B_V0_DX.5.html --paquet Claude/LOT_048/_travail/DX.5/paquet.json --ex ${1:-60} | python3 -c "
import json,sys
r=json.load(sys.stdin)[0]
print(r['verdict'],r['octets'],'conn%',r['connecteur%'],'sansconn',r['paragraphes_sans_connecteur'])
for k,v in r['defauts'].items():
    print(k,v['n'])
    for e in v['ex']: print('   ',e[:260])
"
