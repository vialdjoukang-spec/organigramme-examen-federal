#!/usr/bin/env python3
import sys, os, re, json
sys.path.insert(0, '/home/user/organigramme-examen-federal/Claude/_outils')
import controle3 as C
D = os.path.dirname(os.path.abspath(__file__))
P = {p['id']: p['texte'] for p in json.load(open(D + '/paquet.json'))['passages']}
pts = [int(a) for a in sys.argv[1:]] or range(1, 15)
tot = {'long': 0, 'nom': 0, 'num': 0, 'nocit': 0, 'conn': 0, 'n': 0}
for n in pts:
    f = f'{D}/fragments/p{n:02d}.html'
    if not os.path.exists(f): continue
    h = open(f).read()
    for tag, b, t in C.phrases_html(h):
        if tag == 'td': continue
        tot['n'] += 1
        w = len(t.split())
        cites = C.CIT.findall(b)
        nums = C.nombres(C.STRUCT.sub(' ', t))
        if C.CONNECT.search(t): tot['conn'] += 1
        if w > 28: tot['long'] += 1; print(f'p{n} LONG {w}: {t}')
        if not C.est_verbale(t): tot['nom'] += 1; print(f'p{n} NOM: {t}')
        if nums and not cites: tot['nocit'] += 1; print(f'p{n} NOCIT: {t}')
        if cites:
            for c in cites:
                if c not in P: print(f'p{n} INCONNU {c}')
            src = ' '.join(P.get(c, '') for c in cites)
            ns = C.nombres_source(src)
            manq = {x for x in nums if x not in ns}
            if manq: tot['num'] += 1; print(f'p{n} NUM {sorted(manq)}: {t}')
        if C.DOSE.search(t) and not any(c.lower().startswith('aips') for c in cites): print(f'p{n} DOSE: {t}')
print(tot, 'conn%', round(100*tot['conn']/max(1,tot['n'])))
