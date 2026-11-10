#!/bin/bash
# itération locale : génère, assemble en scratch, contrôle
cd /home/user/wt/lot-054/Claude/LOT_054/_travail/DX.8
python3 gen.py >/dev/null || exit 1
mkdir -p tmp
O=/home/user/organigramme-examen-federal/Claude/_outils
python3 $O/assembler.py --fragments fragments --paquet paquet.json --contrat contrat.json --titre "DX.8 — Cancer du rein (carcinome à cellules rénales)" --sortie tmp/t.html
python3 $O/controle3.py tmp/t.html --paquet paquet.json --ex ${1:-6} > tmp/c.json
python3 - <<'P'
import json
R=json.load(open('tmp/c.json'))[0]
print({k:R[k] for k in('verdict','octets','connecteur%','paragraphes_sans_connecteur','phrases')})
for k,v in R['defauts'].items(): print(' ',k,v['n'],' || '.join(v['ex']))
P
