import re,sys,json
sys.path.insert(0,'/home/user/organigramme-examen-federal/Claude/_outils')
import controle3 as C
h=open('../../LOT_047_Phase_B_V0_DX.9.html',encoding='utf-8').read()
paquet=C.charger_paquet('paquet.json')
body=C.SOURCES.sub(' ',h)
ph=C.phrases_html(body)
for tag,b,t in ph:
    cites=C.CIT.findall(b); nums=C.nombres(C.STRUCT.sub(' ',t))
    if nums and not cites and tag!='td': print('NOCITE',t[:120])
    if cites and nums:
        ns=C.nombres_source(' '.join(paquet.get(c,'') for c in cites)); m={n for n in nums if n not in ns}
        if m: print('NUM',sorted(m),'|',t[:110],'|',cites)
    if tag!='td':
        n=len(t.split())
        if not C.est_verbale(t): print("NOMINALE",t)
        if n>28: print("LONG",n,t)
paras=re.findall(r'<(?:p|div class="p")(?:\s[^>]*)?>(.*?)</(?:p|div)>',body,re.S|re.I)
for p in paras:
    t=C.texte(p)
    if len(t.split())>40 and not C.CONNECT.search(t): print("SANSCONN",t)
