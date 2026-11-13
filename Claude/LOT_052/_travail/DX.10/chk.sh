#!/bin/bash
O=/home/user/wt/lot-052/Claude/_outils
cd /home/user/wt/lot-052/Claude/LOT_052/_travail/DX.10
python3 $O/assembler.py --fragments fragments --paquet paquet.json --contrat contrat.json --titre "DX.10 — Rupture d'anévrisme de l'aorte abdominale" --sortie scratch/test.html >/dev/null
python3 $O/controle3.py scratch/test.html --paquet paquet.json --ex ${1:-40} > scratch/c.json
python3 - <<'E'
import json
R=json.load(open('scratch/c.json'))[0]
print({k:R[k] for k in ('verdict','octets','connecteur%','paragraphes_sans_connecteur')})
for k,v in R['defauts'].items():
    print(k,v['n'])
    for e in v['ex']: print('   ',e)
E
