#!/bin/bash
export OUTILS_REF=/tmp/claude-0/-home-user/15c9849e-78d1-5a00-9dcf-bd21b180736d/scratchpad/ref/outils PAQUET_CACHE=/tmp/claude_paquet_cache
(cd /home/user/wt/lot-043/Claude/LOT_043/_travail/DX.7 && python3 build.py)
cd /home/user/wt/lot-043
python3 /home/user/organigramme-examen-federal/Claude/_outils/lecon.py finir --lot 043 --cible DX.7 --titre "DX.7 — Pneumonie et pleuropneumonie" --ex ${1:-30} > /dev/null 2>&1
python3 - <<'P'
import json,sys
r=json.load(open('/home/user/wt/lot-043/Claude/LOT_043/_travail/DX.7/controle.json'))[0]
print(r['verdict'],r['octets'],'conn%',r['connecteur%'],'sans_conn',r['paragraphes_sans_connecteur'])
for k,v in r['defauts'].items():
    print('##',k,v['n'])
    for e in v['ex']: print('  -',e[:230])
P
