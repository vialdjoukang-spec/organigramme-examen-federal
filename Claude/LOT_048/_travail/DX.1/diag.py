import sys,re
sys.path.insert(0,'/home/user/organigramme-examen-federal/Claude/_outils')
import controle3 as c
h=open('/home/user/wt/lot-048/Claude/LOT_048/LOT_048_Phase_B_V0_DX.1.html').read()
paras=re.findall(r'<(?:p|div class="p")(?:\s[^>]*)?>(.*?)</(?:p|div)>',h,re.S|re.I)
for p in paras:
    t=c.texte(p)
    if len(t.split())>40 and not c.CONNECT.search(t): print('SANS CONN:',t[:150])
ph=c.phrases_html(c.SOURCES.sub(' ',h))
for tg,b,t in ph:
    if tg=='td': continue
    n=len(t.split())
    if n>26: print('LONG',n,t[:100])
