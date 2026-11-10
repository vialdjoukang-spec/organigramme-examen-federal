import sys,re,json
sys.path.insert(0,'/home/user/wt/lot-001/Claude/_outils')
import controle3 as C
f='/home/user/wt/lot-001/Claude/LOT_001/LOT_001_Phase_B_V0_DX.2.html'
h=open(f,encoding='utf-8').read()
P=C.charger_paquet('paquet.json')
class A: points=14;min=100000;max=200000;script_ok=False;ex=999
r=C.controler(f,P,A,{})
print(r['verdict'],r['octets'],'conn%',r['connecteur%'],'sans_conn',r['paragraphes_sans_connecteur'])
for k,v in r['defauts'].items():
    print(k,v['n'])
    for e in v['ex']: print('   ',e)
paras=re.findall(r'<(?:p|div class="p")(?:\s[^>]*)?>(.*?)</(?:p|div)>',h,re.S|re.I)
for p in paras:
    t=C.texte(p)
    if len(t.split())>40 and not C.CONNECT.search(t): print('SANSCONN:',t[:110])
