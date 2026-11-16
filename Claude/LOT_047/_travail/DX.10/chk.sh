#!/bin/bash
export PAQUET_CACHE=/tmp/claude_paquet_cache
cd /home/user/wt/lot-047
python3 /home/user/organigramme-examen-federal/Claude/_outils/controle3.py Claude/LOT_047/LOT_047_Phase_B_V0_DX.10.html --paquet Claude/LOT_047/_travail/DX.10/paquet.json --ex 300 > Claude/LOT_047/_travail/DX.10/ctl.json
python3 - <<'P'
import json
c=json.load(open('/home/user/wt/lot-047/Claude/LOT_047/_travail/DX.10/ctl.json'))
c=c[0] if isinstance(c,list) else c
print(c['verdict'],c['octets'],c['connecteur%'],c['paragraphes_sans_connecteur'])
for k,v in c['defauts'].items():
    print('##',k,v['n'])
    if k not in sys.argv if False else True:
        for x in v['ex']: print('  -',x)
P
