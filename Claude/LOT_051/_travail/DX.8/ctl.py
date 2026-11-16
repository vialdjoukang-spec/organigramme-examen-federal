import sys,json,types,collections
sys.path.insert(0,'/home/user/organigramme-examen-federal/Claude/_outils')
import controle3 as C
P=json.load(open('Claude/LOT_051/_travail/DX.8/paquet.json'))
paq=C.charger_paquet('Claude/LOT_051/_travail/DX.8/paquet.json')
a=types.SimpleNamespace(points=14,min=100000,max=200000,script_ok=False)
# reproduire controler en recueillant tout
import re,html,hashlib
chemin='Claude/LOT_051/LOT_051_Phase_B_V0_DX.8.html'
h=open(chemin,encoding='utf-8').read()
ph=C.phrases_html(C.SOURCES.sub(' ',h))
out=collections.defaultdict(list)
for tag,b,t in ph:
    cites=C.CIT.findall(b); nums=C.nombres(C.STRUCT.sub(' ',t))
    if nums and not cites and tag!='td': out['A_sans_cit'].append(t)
    if cites and nums:
        ns=C.nombres_source(' '.join(paq.get(c,'') for c in cites)); m=sorted(n for n in nums if n not in ns)
        if m: out['A_absent'].append(f'{m} :: {t[:150]}')
    if C.DOSE.search(t) and not any(c.lower().startswith('aips') for c in cites): out['A_dose'].append(t)
    if tag!='td':
        n=len(t.split())
        if not C.est_verbale(t): out['B_nominale'].append(t)
        if n>32: out['B_longue'].append(f'{n} :: {t}')
paras=re.findall(r'<(?:p|div class="p")(?:\s[^>]*)?>(.*?)</(?:p|div)>',h,re.S|re.I)
for p in paras:
    t=C.texte(p)
    if len(t.split())>40 and not C.CONNECT.search(t): out['B_sans_conn'].append(t[:160])
skip=set(sys.argv[1:])
for k,v in out.items():
    if k in skip: continue
    print('##',k,len(v))
    for x in v: print('  -',x[:330])
