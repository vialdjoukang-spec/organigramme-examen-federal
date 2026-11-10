import sys,re
sys.path.insert(0,'/tmp/claude-0/-home-user/15c9849e-78d1-5a00-9dcf-bd21b180736d/scratchpad/ref/outils')
import controle3 as C
h=open('Claude/LOT_043/LOT_043_Phase_B_V0_DX.8.html',encoding='utf8').read()
for tag,b,t in C.phrases_html(C.SOURCES.sub(' ',h)):
    if tag.lower()=='td': continue
    n=len(t.split())
    if not C.est_verbale(t): print('NOM |',t)
    elif n>32: print(f'LONG{n} |',t)
