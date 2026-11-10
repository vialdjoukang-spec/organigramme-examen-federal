cd /home/user/wt/lot-047
export PAQUET_CACHE=/tmp/claude_paquet_cache
D=Claude/LOT_047/_travail/DX.5
python3 $D/build.py
mkdir -p /tmp/w47
python3 /home/user/organigramme-examen-federal/Claude/_outils/assembler.py --fragments $D/fragments --paquet $D/paquet.json --contrat $D/contrat.json --titre "DX.5 — Cardiopathie ischémique (angor stable ou syndrome coronarien aigu)" --sortie /tmp/w47/dx5.html | tail -2
python3 /home/user/organigramme-examen-federal/Claude/_outils/controle3.py /tmp/w47/dx5.html --paquet $D/paquet.json --ex ${1:-6} | python3 -c "
import json,sys
R=json.load(sys.stdin)[0]
print({k:R[k] for k in ('verdict','octets','connecteur%','paragraphes_sans_connecteur')})
for k,v in R['defauts'].items():
    if k.startswith('C_points'): continue
    print(k,v['n']); [print('   ',e) for e in v['ex']]
"
