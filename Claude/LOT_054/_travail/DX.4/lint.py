import re,sys,html
sys.path.insert(0,'/home/user/organigramme-examen-federal/Claude/_outils')
import controle3 as c
for n in range(1,15):
    try: h=open(f'fragments/p{n:02d}.html').read()
    except: continue
    for tag,b,t in c.phrases_html(h):
        if tag=='td': continue
        w=len(t.split())
        if w>29 or not c.est_verbale(t): print(n,w,'|',t[:230])
