import re,sys,glob
sys.path.insert(0,'/tmp/claude-0/-home-user/15c9849e-78d1-5a00-9dcf-bd21b180736d/scratchpad/ref/outils')
import controle3 as C
for f in sorted(glob.glob('fragments/p*.html')):
    h=open(f).read()
    for tag,b,t in C.phrases_html(h):
        if tag=='td': continue
        n=len(t.split())
        if n>28: print(f[-8:-5],'LONG',n,'::',t)
        elif not C.est_verbale(t): print(f[-8:-5],'NOM ::',t)
