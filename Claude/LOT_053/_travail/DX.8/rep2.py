import sys,re
sys.path.insert(0,'/home/user/organigramme-examen-federal/Claude/_outils')
import controle3 as c
h=open('/home/user/wt/lot-053/Claude/LOT_053/LOT_053_Phase_B_V0_DX.8.html',encoding='utf-8').read()
ph=c.phrases_html(c.SOURCES.sub(' ',h))
print('--LONG')
for tag,b,t in ph:
    if tag.lower()=='td': continue
    if len(t.split())>32: print(len(t.split()),t)
print('--NOM')
for tag,b,t in ph:
    if tag.lower()=='td': continue
    if not c.est_verbale(t): print(t)
print('--NOCONN')
paras=re.findall(r'<(?:p|div class="p")(?:\s[^>]*)?>(.*?)</(?:p|div)>',h,re.S|re.I)
for p in paras:
    tx=c.texte(p)
    if len(tx.split())>40 and not c.CONNECT.search(tx): print(len(tx.split()),tx[:300])
