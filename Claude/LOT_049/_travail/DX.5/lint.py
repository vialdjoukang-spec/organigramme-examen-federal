import re,sys,glob,html
sys.path.insert(0,'/home/user/organigramme-examen-federal/Claude/_outils')
import controle3 as C
for f in sorted(glob.glob('src/p*.txt')):
    h=open(f).read()
    h=re.sub(r'\[\[[^\]]+\]\]','',h)
    ph=C.phrases_html(h)
    paras=re.findall(r'<(?:p|div class="p")(?:\s[^>]*)?>(.*?)</(?:p|div)>',h,re.S)
    for tag,b,t in ph:
        if tag=='td': continue
        n=len(t.split())
        if not C.est_verbale(t): print(f,'NOM |',t)
        elif n>28: print(f,'LONG',n,'|',t)
    for p in paras:
        tt=C.texte(p)
        if len(tt.split())>40 and not C.CONNECT.search(tt): print(f,'NOCONN |',tt[:140])
