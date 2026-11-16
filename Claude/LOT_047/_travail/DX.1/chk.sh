cd /home/user/wt/lot-047
export PAQUET_CACHE=/tmp/claude_paquet_cache
python3 Claude/LOT_047/_travail/DX.1/build.py >/dev/null
python3 /home/user/organigramme-examen-federal/Claude/_outils/assembler.py --fragments Claude/LOT_047/_travail/DX.1/fragments --paquet Claude/LOT_047/_travail/DX.1/paquet.json --contrat Claude/LOT_047/_travail/DX.1/contrat.json --titre "DX.1 — Reflux gastro-œsophagien (maladie de reflux érosive ou non érosive)" --sortie /tmp/w47/test.html | tail -2
python3 /home/user/organigramme-examen-federal/Claude/_outils/controle3.py /tmp/w47/test.html --paquet Claude/LOT_047/_travail/DX.1/paquet.json --ex ${1:-6} | python3 -c "
import json,sys
R=json.load(sys.stdin)[0]
print({k:R[k] for k in ('verdict','octets','connecteur%','paragraphes_sans_connecteur')})
for k,v in R['defauts'].items():
    if k.startswith('C_points'): continue
    print(k,v['n']); [print('   ',e) for e in v['ex']]
"
