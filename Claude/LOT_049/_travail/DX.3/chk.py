#!/usr/bin/env python3
import re,glob,sys
sys.path.insert(0,'/home/user/organigramme-examen-federal/Claude/_outils')
import controle3 as C
tot=0;con=0
for f in sorted(glob.glob('fragments/p*.html')):
    if len(sys.argv)>1 and sys.argv[1] not in f: continue
    h=open(f,encoding='utf-8').read()
    for tag,b in re.findall(r'<(p|div class="p")(?:\s[^>]*)?>(.*?)</(?:p|div)>',h,re.S):
        t=C.texte(b)
        if len(t.split())>40 and not C.CONNECT.search(t): print('PARA SANS CONN',f,t[:90])
    ph=C.phrases_html(h)
    for tg,b,t in ph:
        if tg=='td': continue
        tot+=1
        if C.CONNECT.search(t): con+=1
        if not C.est_verbale(t): print('NOMINALE',f,t[:80])
print('conn%',round(100*con/max(1,tot)),tot)
