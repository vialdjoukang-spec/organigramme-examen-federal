import re,sys,json,html
sys.path.insert(0,'/home/user/organigramme-examen-federal/Claude/_outils')
import controle3 as C
h=open('/home/user/wt/lot-052/Claude/LOT_052/LOT_052_Phase_B_V0_DX.6.html',encoding='utf8').read()
h2=C.SOURCES.sub(' ',h)
paras=re.findall(r'<(?:p|div class="p")(?:\s[^>]*)?>(.*?)</(?:p|div)>',h2,re.S|re.I)
print('PARAS SANS CONNECTEUR')
for p in paras:
    t=C.texte(p)
    if len(t.split())>40 and not C.CONNECT.search(t): print(' -',len(t.split()),t[:110])
print('PHRASES')
for tag,b,t in C.phrases_html(h2):
    if tag.lower()=='td': continue
    n=len(t.split()); 
    if n>32 or not C.est_verbale(t): print(' *',n,'N' if not C.est_verbale(t) else 'L',t[:150])
