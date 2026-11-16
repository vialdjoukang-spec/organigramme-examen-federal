import re,sys,glob
sys.path.insert(0,'/home/user/organigramme-examen-federal/Claude/_outils')
import controle3 as c
for f in sorted(glob.glob('fragments/p*.html')):
    h=open(f).read(); ph=[x for x in c.phrases_html(h) if x[0].lower()!='td']
    n=len(ph); k=sum(1 for x in ph if c.CONNECT.search(x[2]))
    print(f,n,k,round(100*k/max(n,1)))
