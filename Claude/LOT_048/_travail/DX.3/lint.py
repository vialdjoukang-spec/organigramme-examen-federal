import sys,re
sys.path.insert(0,'/home/user/organigramme-examen-federal/Claude/_outils')
import controle3 as c
h=open('/home/user/wt/lot-048/Claude/LOT_048/LOT_048_Phase_B_V0_DX.3.html',encoding='utf-8').read()
h=c.SOURCES.sub(' ',h)
n=0
for tag,b,t in c.phrases_html(h):
    if tag.lower()=='td': continue
    w=len(t.split())
    if w>28: print(w,t[:110]); n+=1
print('>28 mots:',n)
