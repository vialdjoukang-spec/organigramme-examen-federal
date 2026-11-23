"""Pipeline DX -> jusqu'à 3 paramètres biostatistiques suisses contextualisés + contrôle croisé (référentiel MHT, cours).
Reprise : chaque DX traité est écrit dans SQLite (WAL) ; relancer = ne traite que les DX manquants (--refaire pour tout recalculer)."""
import json, re, sys, os, csv, subprocess, html
from concurrent.futures import ThreadPoolExecutor
sys.path.insert(0, os.path.dirname(__file__))
from noyau import db, journal, maintenant, RACINE
from regles import apparier, norm
from normaliseur import parse, concorde, nombres

# Entrées du contrôle croisé (facultatives : absentes = contrôle croisé sauté, statuts inchangés)
MHT = os.environ.get('EPI_MHT', '/workspace/Leona__Injection_MHT_20261115/out')
REPO = os.environ.get('EPI_DEPOT') or subprocess.run(['git', '-C', os.path.dirname(os.path.abspath(__file__)), 'rev-parse', '--show-toplevel'],
                                                      capture_output=True, text=True).stdout.strip() or '/workspace/grok/etude/repo'
_c = os.environ.get('EPI_CARTE', '/workspace/Leona__Brief_Redaction_LOTs_20261115/scripts/carte_lots.json')
CARTE = json.load(open(_c))['lecons'] if os.path.exists(_c) else {}
CRIT = ['population', 'definition', 'mesure', 'unite']           # dimensions critiques
CTX = CRIT + ['annee', 'territoire', 'type_source', 'url']
RANG = {'can': 1, 'obs': 1, 'idd': 2, 'ms': 3, 'cod': 4, 'mht': 5}

def elision(p):
    return re.sub(r"\bde ([aeiouyhéèêAEIOUYHÉ])", r"d’\1", p).replace('((', '(').replace('))', ')')

def indicateurs(c):
    cols = [d[0] for d in c.execute('SELECT * FROM indicateurs LIMIT 1').description]
    return {r[0]: dict(zip(cols, r)) for r in c.execute('SELECT * FROM indicateurs')}

def mht_par_dx():
    """Valeurs du référentiel MHT rattachées à chaque (lot, dx), avec statut de concordance et extraits primaires retrouvés."""
    if not os.path.exists(f'{MHT}/mapping.json'): return {}
    m = json.load(open(f'{MHT}/mapping.json'))
    conc = {r['n']: r for r in csv.DictReader(open(f'{MHT}/CONCORDANCE.csv'))}
    prim = {}
    p = f'{MHT}/urls_primaires/resultats.json'
    if os.path.exists(p):
        for x in json.load(open(p)):
            ex = [(cd['url'], e, cd.get('nature', '')) for cd in x.get('candidats', []) for e in cd.get('extraits', [])]
            if ex: prim[str(x['n'])] = ex
    out = {}
    for r in m:
        for cb in r.get('cibles', []):
            if cb.get('lot') and cb.get('dx_code'):
                out.setdefault((cb['lot'], cb['dx_code']), []).append(dict(r, conc=conc.get(str(r['n']), {}), prim=prim.get(str(r['n']), [])))
    return out

def type_mesure(s):
    s = norm(s)
    if 'incidence' in s or 'nouveaux cas' in s: return 'incidence'
    if 'prevalence' in s: return 'prevalence'
    if 'deces' in s or 'mortalit' in s: return 'mortalite'
    if 'cas' in s or 'hospitalis' in s: return 'cas'
    return 'autre'

_cours = {}
def texte_cours(lot, dx):
    k = f'{lot:03d}:DX{dx}'
    if k in _cours: return _cours[k]
    v = CARTE.get(k); t = ''
    if v:
        h = subprocess.run(['git', '-C', REPO, 'cat-file', 'blob', v['blob']], capture_output=True).stdout.decode('utf-8', 'ignore')
        t = re.sub(r'\s+', ' ', html.unescape(re.sub(r'<[^>]+>', ' ', re.sub(r'<(script|style)[^>]*>.*?</\1>', ' ', h, flags=re.S))))
    _cours[k] = (t, v['chemin'] if v else ''); return _cours[k]

def croise(p, refs, lot, dx):
    """Contrôle croisé dimensionnel. Concordant seulement si mesure + unité compatibles ET valeur à l'arrondi près."""
    notes = []
    pv = parse(f"{p['valeur_txt']} {('%' if p['unite'] == '%' else 'pour 100 000' if '100 000' in (p['unite'] or '') else '')}")
    for r in refs:
        if p['cle'] == f"mht:{r['n']}": continue
        rv = parse(r['valeur'])
        if not rv or not pv: continue
        tm_r = 'cas' if 'cas annuel' in norm(r['type_libelle']) else type_mesure(r['type_libelle'] + ' ' + r['valeur'])
        tm_p = 'hospitalisations' if p['cle'].startswith('ms:') else 'cas' if p['cle'].endswith(':n') else type_mesure(p['mesure'] + ' ' + p['unite'])
        if tm_r != tm_p or (rv.unite or '') != (pv.unite or ''):
            notes.append(f"MHT n°{r['n']} « {r['valeur']} » ({r['type_libelle']}) : autre indicateur"); continue
        popr = norm(r.get('population', '')); popp = norm(p.get('population', '') + ' ' + p.get('age_sexe', ''))
        generale = re.fullmatch(r'\s*(population (generale|suisse|adulte|residante)?|adultes?|suisse|)\s*(\(.*\))?\s*', popr) is not None
        sous_groupe = re.findall(r'\d+\s*ans|enfant|femme|homme|diabet|patient|hospital|urgence|medecine generale|consultation|cohorte|traite|personnes agees|\bage', popr)
        if sous_groupe and not all(g in popp for g in sous_groupe) and not generale:
            notes.append(f"MHT n°{r['n']} « {r['valeur']} » ({r.get('population','')}) : autre population"); continue
        ok = concorde(rv, pv); an_r = (re.search(r'\b(19|20)\d\d\b', r.get('population', '')) or [''])[0] or (r.get('annee') or '').strip()
        ratio = max(rv.haut, pv.haut) / max(1e-9, min(rv.bas, pv.bas)) if min(rv.bas, pv.bas) > 0 else 99
        if ok: verdict = 'concordant (à l’arrondi près)'
        elif ratio > 1.5: verdict = f"autre indicateur probable (définition/population différente ; source = {p['valeur_txt']} {'' if p['unite'] in p['valeur_txt'] else p['unite']})"
        elif an_r and p['annee'] and an_r not in p['annee']: verdict = f"autre année ({an_r} vs {p['annee']} : {p['valeur_txt']} {p['unite']})"
        elif not an_r: verdict = f"ÉCART, année MHT non précisée ; valeur source {p['annee']} = {p['valeur_txt']} {'' if p['unite'] in p['valeur_txt'] else p['unite']}"
        else: verdict = f"DISCORDANT, valeur juste ({p['annee']}) = {p['valeur_txt']} {p['unite']}"
        notes.append(f"MHT n°{r['n']} « {r['valeur']} » : {verdict}")
    t, chemin = texte_cours(lot, dx)
    if t and p['valeur'] is not None:
        hits = [i for v, i in nombres(t) if abs(v - p['valeur']) <= max(0.05, abs(p['valeur']) * 0.0005)]
        if hits: notes.append(f"cours ({chemin}) : même chiffre présent « …{t[max(0, hits[0]-80):hits[0]+40].strip()}… » (vérifier le contexte)")
    return ' | '.join(notes)

def param_mht(r):
    """Valeur MHT dont un extrait primaire contient le chiffre : paramètre candidat, contexte souvent incomplet → statut honnête."""
    rv = parse(r['valeur'])
    for url, ex, nat in r['prim']:
        ev = [v for v, _ in nombres(ex)]
        if rv and any(rv.bas - rv.tol() <= v <= rv.haut + rv.tol() for v in ev):
            an = re.search(r'\b(19|20)\d\d\b', ex)
            ch = re.search(r'suisse|switzerland|swiss|bern|zurich|geneva|geneve|lausanne|basel', norm(ex))
            return dict(cle=f"mht:{r['n']}", source=f"Référentiel MHT n°{r['n']} + source primaire retrouvée", libelle=r['entite'],
                valeur=rv.bas, valeur_txt=r['valeur'], unite=rv.unite or '', population=r['population'] or '', age_sexe='',
                definition=f"{r['entite']} – {r['type_libelle']}", mesure=r['type_libelle'], annee=an.group(0) if an else '',
                territoire=('Suisse' if ch else 'non précisé dans l’extrait (hors CH probable)'), type_source=nat or 'publication',
                url=url, preuve=ex[:400], sha256='', phrase='', hors_ch=0 if ch else 1)
    return None

def traiter(dxr, I, MH):
    lot, dx, nom = dxr['lot'], dxr['dx'], dxr['diagnostic']
    res = dict(lot=lot, dx=dx, code=dxr['code'], ssp=dxr['ssp'], diagnostic=nom, nom_source=dxr.get('nom_source', 'ssp_dx.json / annexe'), params=[])
    if not nom:
        res['statut_dx'] = 'DX non nommé (Phase A à faire) – aucune recherche possible'; return res
    cands = []
    for k, q in apparier(nom):
        if k in I and I[k]['valeur'] is not None: cands.append((0 if q == 'exact' else 1, RANG[k.split(':')[0]], k, q))
    cands.sort()
    refs = MH.get((lot, dx), [])
    choisis = [(dict(I[k]), q) for _, _, k, q in cands[:3]]
    # Consigne 19:54 : valeurs/liens Gemini non fiables -> le référentiel MHT ne sert QUE de cible de contrôle croisé, jamais de paramètre.
    for p, q in choisis:
        manque = [d for d in CTX if not (p.get(d) or '').strip()]
        crit = [d for d in manque if d in CRIT]
        if crit: st = 'contexte incomplet (' + ', '.join(crit) + ')'
        elif q == 'exact' and not manque: st = 'vérifié'
        elif q == 'groupe': st = f"partiel – indicateur de groupe « {p['libelle']} »"
        else: st = 'partiel – contexte à confirmer' + (f" ({', '.join(manque)})" if manque else '')
        if not p.get('phrase'):
            p['phrase'] = f"{p['valeur_txt']} {p['unite']} – {p['mesure']} ; {p['population']} ; {p['annee'] or 'année non précisée'} ; {p['territoire']}."
        p['phrase'] = elision(p['phrase'])
        p['statut'] = st; p['appariement'] = q
        p['croise'] = croise(p, refs, lot, dx)
        res['params'].append(p)
    res['statut_dx'] = ('≥1 vérifié' if any(x['statut'] == 'vérifié' for x in res['params']) else
                        'partiel' if res['params'] else 'non trouvé (aucune donnée structurée suisse appariée)')
    return res

def main(refaire=False):
    c = db(); I = indicateurs(c); MH = mht_par_dx()
    R = json.load(open(os.path.join(RACINE, 'data', 'dx_2480.json')))
    R.sort(key=lambda x: (x['lot'] > 32, x['lot'], x['dx']))         # priorité LOTs 001–032
    fait = set() if refaire else {(a, b) for a, b in c.execute('SELECT lot,dx FROM resultats')}
    todo = [x for x in R if (x['lot'], x['dx']) not in fait]
    journal(f'pipeline : {len(todo)} DX à traiter ({len(fait)} déjà faits)')
    with ThreadPoolExecutor(8) as ex:
        for i, res in enumerate(ex.map(lambda x: traiter(x, I, MH), todo)):
            c.execute('INSERT OR REPLACE INTO resultats VALUES(?,?,?,?,?)', (res['lot'], res['dx'], res['diagnostic'], json.dumps(res, ensure_ascii=False), maintenant()))
            if i % 50 == 0: c.commit()
    c.commit(); journal('pipeline : terminé'); c.close()
if __name__ == '__main__': main('--refaire' in sys.argv)
