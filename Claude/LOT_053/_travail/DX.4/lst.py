import re,sys
sys.path.insert(0,'/home/user/organigramme-examen-federal/Claude/_outils')
import controle3 as c
h=open('/tmp/claude-0/test.html').read()
ph=c.phrases_html(c.SOURCES.sub(' ',h))
for tag,b,t in ph:
    if tag=='td': continue
    n=len(t.split())
    if n>32: print('L',n,t[:300])
    elif not c.est_verbale(t): print('N',t[:300])
paras=re.findall(r'<(?:p|div class="p")(?:\s[^>]*)?>(.*?)</(?:p|div)>',h,re.S|re.I)
for p in paras:
    t=c.texte(re.sub(r'<sup class="r">.*?</sup>','',p))
    if len(t.split())>40 and not c.CONNECT.search(t): print('P',len(t.split()),t[:140])
