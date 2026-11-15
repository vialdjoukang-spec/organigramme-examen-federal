#!/usr/bin/env python3
"""Injecte les seules valeurs CONCORDANTES (concordance.json) dans Claude/FedMed_Progression.html :
chaque cours y est embarqué en gzip+base64 (bloc JSON id="cours-embarques", clé « G1-DX2 », « S1_16-DX3 »…).
L'encadré se place à la fin du point 2 Épidémiologie, entre marqueurs EPI_PROFILES (idempotent : relance = 0 diff).
Garde-fous : clé présente, balises inchangées, cours source (main) + encadré < 150 000 octets.
Usage : inject_progression.py ENTREE.html SORTIE.html"""
import json, re, sys, os, gzip, base64, collections, html as H, subprocess
ICI = os.path.dirname(os.path.abspath(__file__)); OUT = os.path.join(os.path.dirname(ICI), 'out'); sys.path.insert(0, ICI)
import inject as I
ent, sortie = sys.argv[1], sys.argv[2]
s = open(ent, encoding='utf-8').read()
i = s.index('<script type="application/json" id="cours-embarques">'); a = s.index('>', i) + 1; b = s.index('</script>', a)
cours = json.loads(s[a:b])
ssp = {x['lot']: x['code'] for x in json.load(open(f'{I.BRIEF}/ssp_dx.json'))}
carte = json.load(open(f'{I.BRIEF}/carte_lots.json'))['lecons']
ref = {x['n']: x for x in json.load(open(f'{OUT}/referentiel.json'))}
conc = [x for x in json.load(open(f'{OUT}/concordance.json')) if x['statut'] == 'concordant']
par = collections.defaultdict(list)
for x in conc: par[(x['lot'], x['lecon'])].append(x)

def bloc(n, xs):
    e = lambda t: H.escape(t, quote=False)
    ps, srcs = [], []
    for x in xs:
        r = ref[x['n']]; sup = f'<sup class="r"><a href="#sb-epi-dx{n}">EPI</a></sup>'
        ps.append(f'<p>Pour « {e(r["entite"])} », la source « {e(r["source"])} » indique {I.MESURE.get(r["type_libelle"], "une valeur de")} '
                  f'{e(r["valeur"])}{sup}. Cette valeur concerne : {e(I.minus(r["population"]))}{sup}.</p>')
        u = x.get('url_preuve', '')
        srcs.append(f'{e(r["source"])}, chiffre retrouvé dans <a href="{e(u)}">{e(u)}</a>')
    return (I.DEB.format(n=n) + '\n<div class="epi-profiles" style="background:#F3FAFD;border:1px solid #87CEEB;border-radius:6px;'
            'padding:6px 10px;margin:8px 0">\n<div><strong>Repère suisse vérifié : référentiel PROFILES 2023</strong></div>\n'
            + '\n'.join(ps) + f'\n<div id="sb-epi-dx{n}" style="font-size:.85em">Sources : ' + ' ; '.join(dict.fromkeys(srcs))
            + '. Concordance vérifiée le 15.11.2026 entre le référentiel, le cours et la source.</div>\n</div>\n' + I.FIN.format(n=n))

journal = []
for (lot, le), xs in sorted(par.items()):
    cle = f"{ssp[lot].replace('.', '_')}-{le}"; n = int(le[2:])
    base = {'lot': lot, 'dx': le, 'cle': cle, 'valeurs': [x['n'] for x in xs]}
    if cle not in cours: journal.append({**base, 'statut': 'absent_de_la_plateforme'}); continue
    h0 = gzip.decompress(base64.b64decode(cours[cle])).decode('utf-8')
    nouveau = bloc(n, sorted(xs, key=lambda x: x['n']))
    deb, fin = I.DEB.format(n=n), I.FIN.format(n=n)
    if deb in h0:
        h = h0[:h0.index(deb)] + nouveau + h0[h0.index(fin) + len(fin):]
    else:
        loc, mode = I.localiser(h0, n)
        if not loc: journal.append({**base, 'statut': 'rubrique_introuvable', 'detail': mode}); continue
        h = h0[:loc[1]] + nouveau + '\n' + h0[loc[1]:]
    hsrc = re.sub(r'<!-- EPI_PROFILES:DEBUT.*?EPI_PROFILES:FIN DX\d+ -->\n?', '', h0, flags=re.S)
    v = carte.get(f'{lot:03d}:{le}')
    src_oct = len(subprocess.run(['git', '-C', I.REPO, 'cat-file', 'blob', v['blob']], capture_output=True).stdout) if v else 0
    taille = src_oct + len((nouveau + '\n').encode())
    if taille >= I.MAX: journal.append({**base, 'statut': 'refuse_taille', 'detail': f'{src_oct} + encadré = {taille} ≥ {I.MAX}'}); continue
    if I.equilibre(h) != I.equilibre(h0) and I.equilibre(h): journal.append({**base, 'statut': 'refuse_balises'}); continue
    if h != h0: cours[cle] = base64.b64encode(gzip.compress(h.encode('utf-8'), 9, mtime=0)).decode()
    journal.append({**base, 'statut': 'injecte' if deb not in h0 else 'regenere', 'octets_cours_source_apres': taille})
s2 = s[:a] + json.dumps(cours, separators=(',', ':')) + s[b:]
open(sortie, 'w', encoding='utf-8').write(s2)
json.dump(journal, open(f'{OUT}/inject_progression_journal.json', 'w'), ensure_ascii=False, indent=1)
c = collections.Counter(j['statut'] for j in journal)
print(dict(c), 'valeurs injectées :', sum(len(j['valeurs']) for j in journal if j['statut'] in ('injecte', 'regenere')))
for j in journal: print(j)
