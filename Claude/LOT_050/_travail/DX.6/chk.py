import sys,re,json
sys.path.insert(0,'/home/user/organigramme-examen-federal/Claude/_outils')
import controle3 as c
h=open('../../LOT_050_Phase_B_V0_DX.6.html',encoding='utf-8').read()
P=c.charger_paquet('paquet.json')
ph=c.phrases_html(c.SOURCES.sub(' ',h))
mode=sys.argv[1]
if mode=='num':
    for tag,b,t in ph:
        cites=c.CIT.findall(b); nums=c.nombres(c.STRUCT.sub(' ',t))
        if cites and nums:
            ns=c.nombres_source(' '.join(P.get(x,'') for x in cites))
            m={n for n in nums if n not in ns}
            if m: print('NUM',sorted(m),'|',t[:150],'|',cites)
        if nums and not cites and tag!='td': print('NOCITE',t[:120])
        if c.DOSE.search(t) and not any(x.startswith('aips') for x in cites): print('DOSE',t[:100])
elif mode=='long':
    for tag,b,t in ph:
        if tag=='td': continue
        n=len(t.split())
        if n>32: print(n,'|',t[:200])
elif mode=='nom':
    for tag,b,t in ph:
        if tag!='td' and not c.est_verbale(t): print('NOM|',t[:130])
elif mode=='conn':
    paras=re.findall(r'<(?:p|div class="p")(?:\s[^>]*)?>(.*?)</(?:p|div)>',h,re.S|re.I)
    for p in paras:
        t=c.texte(p)
        if len(t.split())>40 and not c.CONNECT.search(t): print(len(t.split()),'|',t[:110])
