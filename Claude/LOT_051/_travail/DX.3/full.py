import sys,json,types,collections
sys.path.insert(0,'/home/user/organigramme-examen-federal/Claude/_outils')
import controle3 as C
a=types.SimpleNamespace(min=100000,max=200000,ex=200,points=14,script_ok=False)
p='/home/user/wt/lot-051/Claude/LOT_051/_travail/DX.3/paquet.json'
pq=C.charger_paquet(p) if hasattr(C,'charger_paquet') else None
r=C.controler('/home/user/wt/lot-051/Claude/LOT_051/LOT_051_Phase_B_V0_DX.3.html',pq,a,collections.defaultdict(set))
print(r['verdict'],r['octets'],r['connecteur%'],r['paragraphes_sans_connecteur'])
for k,v in r['defauts'].items():
    print(k,v['n'])
    if k.startswith(('A_','C_','B_phrase_n','B_phrase_l')) or len(sys.argv)>1:
        for e in v['ex']: print('   ',e[:230])
