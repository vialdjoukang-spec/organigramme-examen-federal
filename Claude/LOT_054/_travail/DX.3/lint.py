import sys,re,json
sys.path.insert(0,'/home/user/organigramme-examen-federal/Claude/_outils')
import controle3 as C
h=open('/home/user/wt/lot-054/Claude/LOT_054/LOT_054_Phase_B_V0_DX.3.html').read()
ph=C.phrases_html(C.SOURCES.sub(' ',h))
paras=re.findall(r'<(?:p|div class="p")(?:\s[^>]*)?>(.*?)</(?:p|div)>',h,re.S|re.I)
mode=sys.argv[1] if len(sys.argv)>1 else 'p'
if mode=='p':
    for p in paras:
        t=C.texte(p)
        if len(t.split())>40 and not C.CONNECT.search(t): print('SANS-CONN:',t[:110].replace('\n',' '))
elif mode=='s':
    for tg,b,t in ph:
        if tg.lower()=='td': continue
        n=len(t.split())
        if n>28 or not C.est_verbale(t): print(n,'|',t[:140])
elif mode=='c':
    # sentences without connector
    sans=[t for tg,b,t in ph if tg.lower()!='td' and not C.CONNECT.search(t)]
    tot=len([1 for tg,_,_ in ph if tg.lower()!='td'])
    print(len(sans),tot)
