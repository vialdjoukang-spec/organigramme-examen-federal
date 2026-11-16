import sys,json,argparse
sys.path.insert(0,'/home/user/organigramme-examen-federal/Claude/_outils')
import controle3 as C
a=argparse.Namespace(points=14,min=100000,max=200000,ex=999,script_ok=False)
P=C.charger_paquet('paquet.json')
f='../../LOT_049_Phase_B_V0_DX.4.html'
r=C.controler(f,P,a,{})
print(r['verdict'],r['octets'],r['connecteur%'],r['paragraphes_sans_connecteur'])
only=sys.argv[1:] 
for k,v in r['defauts'].items():
    if only and not any(k.startswith(o) for o in only): continue
    print('##',k,v['n'])
    for x in v['ex']: print('   ',x[:260])
