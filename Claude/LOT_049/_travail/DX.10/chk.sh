#!/bin/bash
cd /home/user/wt/lot-049
export PAQUET_CACHE=/tmp/claude_paquet_cache
python3 Claude/LOT_049/_travail/DX.10/conv.py >/dev/null
python3 /home/user/organigramme-examen-federal/Claude/_outils/lecon.py finir --lot 049 --cible DX.10 --titre "DX.10 — Inhalation de corps étranger" >/dev/null 2>&1
python3 /home/user/organigramme-examen-federal/Claude/_outils/controle3.py Claude/LOT_049/LOT_049_Phase_B_V0_DX.10.html --paquet Claude/LOT_049/_travail/DX.10/paquet.json --ex 200 > /tmp/claude-0/ctl.json
python3 - <<'P'
import json
r=json.load(open('/tmp/claude-0/ctl.json'))[0]
print(r['verdict'],r['octets'],r['connecteur%'],r['paragraphes_sans_connecteur'])
for k,v in r['defauts'].items():
    print('##',k,v['n'])
    for e in v['ex']: print('  -',e)
P
