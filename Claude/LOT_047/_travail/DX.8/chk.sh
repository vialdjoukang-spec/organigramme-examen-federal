cd /home/user/wt/lot-047
export PAQUET_CACHE=/tmp/claude_paquet_cache
python3 Claude/LOT_047/_travail/DX.8/build.py
mkdir -p /tmp/w47x8
python3 /home/user/organigramme-examen-federal/Claude/_outils/assembler.py --fragments Claude/LOT_047/_travail/DX.8/fragments --paquet Claude/LOT_047/_travail/DX.8/paquet.json --contrat Claude/LOT_047/_travail/DX.8/contrat.json --titre "DX.8 — Cancer de l'œsophage (adénocarcinome et carcinome épidermoïde)" --sortie /tmp/w47x8/test.html | tail -2
python3 /home/user/organigramme-examen-federal/Claude/_outils/controle3.py /tmp/w47x8/test.html --paquet Claude/LOT_047/_travail/DX.8/paquet.json --ex ${1:-6} | python3 -c "
import json,sys
R=json.load(sys.stdin)[0]
print({k:R[k] for k in ('verdict','octets','connecteur%','paragraphes_sans_connecteur')})
for k,v in R['defauts'].items():
    if k.startswith('C_points'): continue
    print(k,v['n']); [print('   ',e) for e in v['ex']]
"
