import sys,re,json
sys.path.insert(0,'/home/user/organigramme-examen-federal/Claude/_outils')
import controle3 as C
h=open('Claude/LOT_048/LOT_048_Phase_B_V0_DX.7.html',encoding='utf-8').read()
ph=C.phrases_html(C.SOURCES.sub(' ',h))
for tag,b,t in ph:
    if tag.lower()=='td': continue
    n=len(t.split())
    if not C.est_verbale(t): print('NOM |',t)
    if n>28: print(f'LONG {n} |',t)
