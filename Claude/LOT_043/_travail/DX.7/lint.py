import sys,re,glob,importlib.util
sys.path.insert(0,'/tmp/claude-0/-home-user/15c9849e-78d1-5a00-9dcf-bd21b180736d/scratchpad/ref/outils')
import controle3 as C
mode=sys.argv[1] if len(sys.argv)>1 else 'all'
for f in sorted(glob.glob('fragments/p*.html')):
    h=open(f).read()
    for tag,b,t in C.phrases_html(h):
        if tag.lower()=='td': continue
        n=len(t.split())
        bad=[]
        if not C.est_verbale(t): bad.append('NOM')
        if n>32: bad.append(f'LONG{n}')
        if bad and mode in ('all','bad'): print(f[10:13],bad,t)
    paras=re.findall(r'<(?:p|div class="p")(?:\s[^>]*)?>(.*?)</(?:p|div)>',h,re.S)
    if mode in ('all','conn'):
        for p in paras:
            tt=C.texte(p)
            if len(tt.split())>40 and not C.CONNECT.search(tt): print(f[10:13],'SANSCONN',tt[:100])
