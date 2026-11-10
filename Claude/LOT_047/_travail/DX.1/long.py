import sys
sys.path.insert(0,'/home/user/organigramme-examen-federal/Claude/_outils')
import controle3 as C,re
h=open('/tmp/w47/test.html').read()
n=0
for tag,b,t in C.phrases_html(C.SOURCES.sub(' ',h)):
    if tag.lower()=='td': continue
    w=len(t.split())
    if w>28: n+=1; print(w,t[:150])
print(n)
