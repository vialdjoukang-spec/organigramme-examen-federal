import re,html,sys,glob
sys.path.insert(0,'/tmp/claude-0/-home-user/15c9849e-78d1-5a00-9dcf-bd21b180736d/scratchpad/ref/outils')
import controle3 as C
for f in sorted(glob.glob('fragments/p*.html')):
    h=open(f).read()
    for p in re.findall(r'<div class="p">(.*?)</div>',h,re.S):
        t=C.texte(re.sub(r'<sup class="r">.*?</sup>','',p))
        if len(t.split())>40 and not C.CONNECT.search(t): print('SANSCONN',f[-8:-5],len(t.split()),t[:150])
    for tag,b,t in C.phrases_html(h):
        if tag!='td' and len(t.split())>28: print('LONG',f[-8:-5],len(t.split()),t[:110])
