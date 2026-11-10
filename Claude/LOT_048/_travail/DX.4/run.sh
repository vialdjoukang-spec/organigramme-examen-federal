#!/bin/bash
cd /home/user/wt/lot-048
export PAQUET_CACHE=/tmp/claude_paquet_cache
python3 Claude/LOT_048/_travail/DX.4/build.py
python3 /home/user/organigramme-examen-federal/Claude/_outils/lecon.py finir --lot 048 --cible DX.4 --titre "DX.4 — Dysphagie oropharyngée de la maladie de Parkinson" >/dev/null 2>&1
python3 /home/user/organigramme-examen-federal/Claude/_outils/controle3.py Claude/LOT_048/LOT_048_Phase_B_V0_DX.4.html --paquet Claude/LOT_048/_travail/DX.4/paquet.json --ex ${1:-40} --points 14 | python3 -c "
import json,sys
r=json.load(sys.stdin)[0]
print(r['verdict'],r['octets'],'conn%',r['connecteur%'],'sansconn',r['paragraphes_sans_connecteur'])
for k,v in r['defauts'].items():
    print(k,v['n'])
    for e in v['ex']: print('   ',e[:260])
"
