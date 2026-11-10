cd /home/user/wt/lot-052; export PAQUET_CACHE=/tmp/claude_paquet_cache
python3 /home/user/organigramme-examen-federal/Claude/_outils/controle3.py Claude/LOT_052/LOT_052_Phase_B_V0_DX.7.html --paquet Claude/LOT_052/_travail/DX.7/paquet.json --ex 300 > /tmp/claude-0/chk.json
python3 - <<'P'
import json
r=json.load(open('/tmp/claude-0/chk.json'))[0]
print(r['verdict'],r['octets'],r['connecteur%'],r['paragraphes_sans_connecteur'])
for k,v in r['defauts'].items():
    print('##',k,v['n'])
    for e in v['ex']: print('  -',e)
P
