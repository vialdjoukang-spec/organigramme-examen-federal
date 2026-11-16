import re,sys,json
sys.path.insert(0,'/home/user/organigramme-examen-federal/Claude/_outils')
import controle3 as C
h=open('/home/user/wt/lot-047/Claude/LOT_047/LOT_047_Phase_B_V0_DX.7.html').read()
h=C.SOURCES.sub(' ',h)
ph=C.phrases_html(h)
paras=re.findall(r'<(?:p|div class="p")(?:\s[^>]*)?>(.*?)</(?:p|div)>',h,re.S|re.I)
for p in paras:
    t=C.texte(p)
    if len(t.split())>40 and not C.CONNECT.search(t): print('SANS CONN:',t[:110])
tot=0;n=0
for tg,b,t in ph:
    if tg=='td': continue
    n+=1
    if C.CONNECT.search(t): tot+=1
print('conn',tot,n,round(100*tot/n))
