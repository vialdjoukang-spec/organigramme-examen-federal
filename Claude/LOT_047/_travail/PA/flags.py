import re,sys
sys.path.insert(0,'/home/user/organigramme-examen-federal/Claude/_outils')
import controle3 as C
h=open('../../LOT_047_Phase_A_V0.html',encoding='utf-8').read()
body=C.SOURCES.sub(' ',h)
lim=int(sys.argv[1]) if len(sys.argv)>1 else 28
for tag,b,t in C.phrases_html(body):
    if tag.lower()=='td': continue
    n=len(t.split())
    nom=not C.est_verbale(t)
    nocite = bool(C.nombres(C.STRUCT.sub(' ',t))) and 'class="r"' not in b
    if nom or n>lim or nocite:
        print(('NOM ' if nom else '')+('NOCITE ' if nocite else '')+str(n),t)
