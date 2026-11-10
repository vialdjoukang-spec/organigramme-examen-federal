import sys,re,json
sys.path.insert(0,'/home/user/organigramme-examen-federal/Claude/_outils')
import controle3 as C
h=open('/home/user/wt/lot-049/Claude/LOT_049/LOT_049_Phase_B_V0_DX.10.html').read()
ph=C.phrases_html(C.SOURCES.sub(' ',h))
mode=sys.argv[1]
for tag,b,t in ph:
    if tag.lower()=='td': continue
    n=len(t.split())
    if mode=='long' and n>28: print(f'[{n}]',t)
    if mode=='nom' and not C.est_verbale(t): print('[NOM]',t)
if mode=='para':
    paras=re.findall(r'<(?:p|div class="p")(?:\s[^>]*)?>(.*?)</(?:p|div)>',h,re.S|re.I)
    for p in paras:
        tx=C.texte(p)
        if len(tx.split())>40 and not C.CONNECT.search(tx): print(len(tx.split()),'|',tx[:200])
