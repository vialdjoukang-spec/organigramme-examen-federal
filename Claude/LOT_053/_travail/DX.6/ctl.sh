#!/bin/bash
cd /home/user/wt/lot-053
export PAQUET_CACHE=/tmp/claude_paquet_cache
python3 Claude/LOT_053/_travail/DX.6/conv.py
python3 /home/user/organigramme-examen-federal/Claude/_outils/lecon.py finir --lot 053 --cible DX.6 --titre "DX.6 — Ascite de la cirrhose, dont la péritonite bactérienne spontanée" --ex 80 > /tmp/claude_dx6_out.txt 2>&1
python3 - <<'P'
import json
c=json.load(open('/home/user/wt/lot-053/Claude/LOT_053/_travail/DX.6/controle.json'))[0]
print(c['verdict'],c['octets'],c['connecteur%'],c['paragraphes_sans_connecteur'])
for k,v in c['defauts'].items(): print('##',k,v['n'])
import sys
json.dump(c['defauts'],open('/tmp/claude_dx6_def.json','w'),ensure_ascii=False)
P
