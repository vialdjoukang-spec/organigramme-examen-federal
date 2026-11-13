import json,re,sys,importlib.util
spec=importlib.util.spec_from_file_location('c3','/home/user/organigramme-examen-federal/Claude/_outils/controle3.py'); C=importlib.util.module_from_spec(spec); spec.loader.exec_module(C)
p=json.load(open('Claude/LOT_052/_travail/DX.4/paquet.json'))
d={x['id']:x['texte'] for x in p['passages']}
h=open('Claude/LOT_052/LOT_052_Phase_B_V0_DX.4.html',encoding='utf-8').read()
ph=C.phrases_html(C.SOURCES.sub(' ',h))
mode=sys.argv[1] if len(sys.argv)>1 else 'A'
for tag,b,t in ph:
    cites=C.CIT.findall(b); nums=C.nombres(C.STRUCT.sub(' ',t))
    if mode=='A':
        if nums and not cites and tag!='td': print('NOCITE |',t[:200])
        if cites and nums:
            ns=C.nombres_source(' '.join(d.get(c,'') for c in cites)); m=sorted(n for n in nums if n not in ns)
            if m: print('MANQ',m,'|',t[:160],'|',cites)
        if C.DOSE.search(t) and not any(c.lower().startswith('aips') for c in cites): print('DOSE |',t[:100])
    elif mode=='L':
        n=len(t.split())
        if n>32 and tag!='td': print(n,'|',t[:150])
    elif mode=='N':
        if tag!='td' and not C.est_verbale(t): print('NOM |',t[:150])
