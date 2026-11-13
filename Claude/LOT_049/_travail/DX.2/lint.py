import sys,re,glob,os
sys.path.insert(0,'/home/user/organigramme-examen-federal/Claude/_outils')
import controle3 as C
d=os.path.dirname(os.path.abspath(__file__))
tot=0;conn=0
for f in sorted(glob.glob(d+'/fragments/p*.html')):
    h=open(f,encoding='utf-8').read()
    ph=C.phrases_html(h)
    for tag,b,t in ph:
        if tag.lower()=='td': continue
        tot+=1
        if C.CONNECT.search(t): conn+=1
        n=len(t.split())
        if n>28: print(os.path.basename(f),'LONG',n,t[:80])
        if not C.est_verbale(t): print(os.path.basename(f),'NOM',t[:90])
    for p in re.findall(r'<(?:p|div class="p")(?:\s[^>]*)?>(.*?)</(?:p|div)>',h,re.S):
        t=C.texte(p)
        if len(t.split())>40 and not C.CONNECT.search(t): print(os.path.basename(f),'NOCONN',t[:70])
print('connecteur %',round(100*conn/max(1,tot)),'phrases',tot)
