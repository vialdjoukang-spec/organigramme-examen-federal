#!/bin/bash
cd /home/user/wt/lot-044
python3 /tmp/claude-0/-home-user/15c9849e-78d1-5a00-9dcf-bd21b180736d/scratchpad/ref/outils/controle3.py Claude/LOT_044/LOT_044_Phase_B_V0_DX.10.html --paquet Claude/LOT_044/_travail/DX.10/paquet.json --ex 400 > /tmp/ctl.json
python3 - "$@" <<'P'
import json,sys
R=json.load(open('/tmp/ctl.json'))[0]
print({k:R[k] for k in ('verdict','octets','connecteur%','paragraphes_sans_connecteur')})
only=sys.argv[1:] 
for k,v in R['defauts'].items():
    if only and not any(k.startswith(o) for o in only): print(k,v['n']); continue
    print('==',k,v['n'])
    for e in v['ex']: print('  -',e)
P
