import sys,re
sys.path.insert(0,'/home/user/organigramme-examen-federal/Claude/_outils')
import controle3 as c
h=open('/home/user/wt/lot-050/Claude/LOT_050/LOT_050_Phase_B_V0_DX.5.html',encoding='utf-8').read()
S=c.SOURCES.sub(' ',h)
for tag,b,t in c.phrases_html(S):
    if tag=='td': continue
    n=len(t.split())
    if n>28 or not c.est_verbale(t): print(('L%d '%n if n>28 else 'N  ')+t)
