import sys,json,glob,os
sys.path.insert(0,'/home/user/organigramme-examen-federal/Claude/_outils')
import controle3 as C
D=os.path.dirname(os.path.abspath(__file__))
os.system(f'python3 {D}/build_frag.py')
P=C.charger_paquet(D+'/paquet.json')
tot=0
sel=sys.argv[1:]
for f in sorted(glob.glob(D+'/fragments/p*.html')):
    if sel and not any(s in f for s in sel): continue
    class A: points=0;min=0;max=10**9;ex=99;script_ok=False
    r=C.controler(f,P,A,{})
    tot+=r['octets']
    print(f[-8:],r['octets'],r['verdict'],r['connecteur%'],r['paragraphes_sans_connecteur'])
    for k,v in r['defauts'].items():
        if k.startswith('C_'): continue
        for e in v['ex']: print('  ',k,e[:260])
print('TOTAL',tot)
