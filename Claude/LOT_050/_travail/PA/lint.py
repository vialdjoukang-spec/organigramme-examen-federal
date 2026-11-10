import re,sys,glob,html
sys.path.insert(0,'/home/user/organigramme-examen-federal/Claude/_outils')
import controle3 as C
out=[]
for f in sorted(glob.glob('fragments/p*.html')):
    h=open(f).read()
    for tag,b,t in C.phrases_html(h):
        if tag.lower()=='td': continue
        n=len(t.split())
        if not C.est_verbale(t) : out.append((f,'NOM',t))
        elif n>32: out.append((f,'LONG%d'%n,t))
    paras=re.findall(r'<(?:p|div class="p")(?:\s[^>]*)?>(.*?)</(?:p|div)>',h,re.S|re.I)
    for p in paras:
        t=C.texte(p)
        if len(t.split())>40 and not C.CONNECT.search(t): out.append((f,'NOCONN',t[:110]))
for o in out: print(o[0][-7:-5],o[1],'|',o[2][:int(sys.argv[1]) if len(sys.argv)>1 else 400])
print(len(out))
