#!/bin/bash
# assemble hors MANIFESTE partagé puis contrôle
set -e
cd /home/user/wt/lot-047
export PAQUET_CACHE=/tmp/claude_paquet_cache
O=/home/user/organigramme-examen-federal/Claude/_outils
T=Claude/LOT_047/_travail/DX.7
S=/tmp/claude-0/-home-user/15c9849e-78d1-5a00-9dcf-bd21b180736d/scratchpad/dx7; mkdir -p $S
(cd $T && python3 mk.py)
python3 $O/assembler.py --fragments $T/fragments --paquet $T/paquet.json --contrat $T/contrat.json --titre "DX.7 — Œsophagite à éosinophiles" --sortie $S/LOT_047_Phase_B_V0_DX.7.html
python3 - <<P
import sys,os
sys.path.insert(0,'$O'); os.environ['OUTILS_REF']='$O'
import lecon
lecon.lignes('$S/LOT_047_Phase_B_V0_DX.7.html')
P
cp $S/LOT_047_Phase_B_V0_DX.7.html Claude/LOT_047/LOT_047_Phase_B_V0_DX.7.html
python3 $O/controle3.py Claude/LOT_047/LOT_047_Phase_B_V0_DX.7.html --paquet $T/paquet.json --ex ${1:-4} > $T/controle.json || true
python3 - <<P
import json
R=json.load(open('$T/controle.json'))[0]
print({k:R[k] for k in ('verdict','octets','connecteur%','paragraphes_sans_connecteur','phrases')})
for k,v in R['defauts'].items(): print(' ',k,v['n'],'||'.join(v['ex']))
P
