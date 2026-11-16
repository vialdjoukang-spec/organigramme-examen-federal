import sys,re
sys.path.insert(0,'/home/user/organigramme-examen-federal/Claude/_outils')
import controle3 as C
h=open('/home/user/wt/lot-051/Claude/LOT_051/LOT_051_Phase_B_V0_DX.3.html').read()
ph=C.phrases_html(C.SOURCES.sub(' ',h))
mode=sys.argv[1]
for tag,b,t in ph:
    if tag.lower()=='td': continue
    n=len(t.split())
    if mode=='nom' and not C.est_verbale(t): print('NOM|',t)
    if mode=='long' and n>32: print('LONG',n,'|',t)
    if mode=='conn' and not C.CONNECT.search(t): print('NC|',t)
