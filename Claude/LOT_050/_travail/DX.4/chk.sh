cd /home/user/wt/lot-050
python3 /home/user/organigramme-examen-federal/Claude/_outils/controle3.py Claude/LOT_050/LOT_050_Phase_B_V0_DX.4.html --paquet Claude/LOT_050/_travail/DX.4/paquet.json --ex 40 | python3 -c "
import json,sys
r=json.load(sys.stdin)[0]
for k,v in r['defauts'].items():
    print('##',k,v['n'])
    for e in v['ex']: print('  ',e[:230])
print(r['verdict'],r['octets'],r['connecteur%'],r['paragraphes_sans_connecteur'])"
