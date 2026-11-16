import sys,json,glob
sys.path.insert(0,'/home/user/organigramme-examen-federal/Claude/_outils')
import controle3 as C
P=C.charger_paquet('Claude/LOT_052/_travail/PA/paquet.json')
tot=0
for f in sorted(glob.glob('Claude/LOT_052/_travail/PA/fragments/p*.html')):
    class A: points=0;min=0;max=10**9;ex=99;script_ok=False
    r=C.controler(f,P,A,{})
    tot+=r['octets']
    print(f[-8:],r['octets'],r['verdict'],r['connecteur%'],r['paragraphes_sans_connecteur'])
    for k,v in r['defauts'].items():
        if k.startswith('C_'): continue
        for e in v['ex']: print('  ',k,e[:230])
print('TOTAL',tot)
