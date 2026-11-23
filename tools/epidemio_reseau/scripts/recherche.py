"""Complétude bispatiale (consigne de Vial, 15.11.2026 21:51) : pour chaque DX nommé, deux recherches lancées en même temps,
niveau EUROPE (général, objectif : au moins une valeur vérifiée par DX) et niveau SUISSE (spécifique). Deux colonnes séparées,
chacune avec son contexte complet (8 colonnes) et son territoire. Hors Europe : on s'arrête. Sources branchées automatiquement : Orphanet/Orphadata (CC BY 4.0),
Europe PMC (PubMed inclus), Wikidata (traduction FR→EN du nom). Reprise idempotente : table `taches` (SQLite WAL), cache disque.
Rien n'est inventé : un candidat Europe PMC reste « candidats à lire » tant qu'un humain/une IA n'a pas lu la source."""
import os, re, sys, json, sqlite3, urllib.parse, xml.etree.ElementTree as ET, collections
from concurrent.futures import ThreadPoolExecutor
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from noyau import db, fetch, maintenant, journal, RACINE, CACHE
from regles import norm

CTX = ['population', 'age_sexe', 'definition', 'mesure', 'unite', 'annee', 'territoire', 'type_source']
FINI = ('vérifié',)   # 100 % = une valeur européenne vérifiée par DX nommé (consigne de Vial, 15.11.2026 21:51)
EPMC = 'https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=lite&pageSize=5&query='
ORPHA = {'prev': 'https://www.orphadata.com/data/xml/fr_product9_prev.xml', 'noms': 'https://www.orphadata.com/data/xml/fr_product1.xml'}
CH_Q = '(Switzerland OR Swiss OR CoLaus OR SAPALDIA OR "Swiss HIV Cohort")'
# Règle de Vial (15.11.2026, 21:49) : Suisse d'abord, sinon Europe ; hors Europe on s'arrête.
PAYS_EU = ['Europe', 'Union européenne', 'Suisse', 'Allemagne', 'Autriche', 'Belgique', 'Bulgarie', 'Chypre', 'Croatie', 'Danemark', 'Espagne',
           'Estonie', 'Finlande', 'France', 'Grèce', 'Hongrie', 'Irlande', 'Islande', 'Italie', 'Lettonie', 'Liechtenstein', 'Lituanie', 'Luxembourg',
           'Malte', 'Norvège', 'Pays-Bas', 'Pologne', 'Portugal', 'Roumanie', 'Royaume-Uni', 'Slovaquie', 'Slovénie', 'Suède', 'Tchéquie',
           'République tchèque', 'Serbie', 'Albanie', 'Macédoine du Nord', 'Monténégro', 'Bosnie-Herzégovine', 'Ukraine', 'Moldavie']
def _champ(mots): return '(' + ' OR '.join(f'TITLE:{m} OR ABSTRACT:{m}' for m in mots) + ')'
CH_Q = _champ(['Switzerland', 'Swiss', 'CoLaus', 'SAPALDIA', '"Swiss HIV Cohort"'])
EU_Q = _champ(['Europe', 'European', '"European Union"', 'ECDC', 'Eurostat', 'France', 'Germany', 'Italy', 'Austria', 'Spain', 'Netherlands', 'Belgium',
               'Denmark', 'Sweden', 'Norway', 'Finland', '"United Kingdom"', 'England', 'Scotland', 'Ireland', 'Portugal', 'Poland', 'Greece', 'Iceland'])
_EU_Q_ANCIEN = ('(Europe OR European OR "European Union" OR ECDC OR Eurostat OR France OR Germany OR Italy OR Austria OR Spain OR Netherlands OR Belgium '
        'OR Denmark OR Sweden OR Norway OR Finland OR "United Kingdom" OR England OR Scotland OR Ireland OR Portugal OR Poland OR Greece OR Iceland)')

def schema(c):
    c.execute('''CREATE TABLE IF NOT EXISTS taches(lot INT, dx INT, diagnostic TEXT, classe TEXT, entite TEXT, source_cible TEXT,
      priorite INT, statut TEXT, params TEXT, sources TEXT, candidats TEXT, date TEXT, agent TEXT, PRIMARY KEY(lot, dx))''')

def nom_court(n):
    n = re.sub(r'\s*\[S\d+\]|\s*donnée non trouvée.*$', '', n or '')
    return re.sub(r'\s*\(.*?\)', '', n).strip(' :;,.') or n

# ---------------------------------------------------------------- Orphanet
def orphanet():
    noms = {}
    t, *_ = fetch(ORPHA['noms'], binaire=True)
    if t:
        for d in ET.fromstring(t).iter('Disorder'):
            code = d.findtext('OrphaCode'); n = d.findtext('Name')
            for s in [n] + [x.text for x in d.iter('Synonym')]:
                if s: noms.setdefault(norm(s).strip(), code)
    prev, meta = {}, {}
    t, sha, date, _ = fetch(ORPHA['prev'], binaire=True)
    if t:
        root = ET.fromstring(t); meta = dict(date=root.get('date', '')[:10], sha=sha)
        for d in root.iter('Disorder'):
            code = d.findtext('OrphaCode'); L = []
            for p in d.iter('Prevalence'):
                L.append(dict(id=p.get('id'), source=p.findtext('Source') or '', type=p.findtext('PrevalenceType/Name') or '',
                              qualif=p.findtext('PrevalenceQualification/Name') or '', classe=p.findtext('PrevalenceClass/Name') or '',
                              valmoy=p.findtext('ValMoy') or '', geo=p.findtext('PrevalenceGeographic/Name') or '',
                              valid=p.findtext('PrevalenceValidationStatus/Name') or ''))
            prev[code] = (d.findtext('Name'), L)
            noms.setdefault(norm(d.findtext('Name')).strip(), code)
    return noms, prev, meta

def annees_pmid(pmids):
    """Année et titre des PMID cités (Europe PMC, par lots de 40)."""
    out = {}
    pmids = sorted(set(pmids))
    for i in range(0, len(pmids), 40):
        q = 'SRC:MED AND (' + ' OR '.join(f'EXT_ID:{p}' for p in pmids[i:i + 40]) + ')'
        t, *_ = fetch(EPMC.replace('pageSize=5', 'pageSize=40') + urllib.parse.quote(q))
        if t:
            for r in json.loads(t).get('resultList', {}).get('result', []):
                out[r.get('pmid')] = (r.get('pubYear', ''), r.get('title', ''))
    return out

ORDRE_GEO = {'Suisse': 0, 'Europe': 1}
def params_orphanet(code, prev, meta, ans):
    nom, L = prev.get(code, ('', []))
    P = []
    for p in sorted(L, key=lambda p: ORDRE_GEO.get(p['geo'], 2)):
        if p['geo'] not in PAYS_EU: continue          # hors Europe : on s'arrête
        if p['valid'] != 'Validé' or p['type'].startswith('Cas') or not (p['classe'] or float(p['valmoy'] or 0) > 0): continue
        pm = re.findall(r'(\d+)\[PMID\]', p['source']); yrs = [ans[x][0] for x in pm if x in ans and ans[x][0]]
        val = p['classe'] if p['qualif'] == 'Rang' or not float(p['valmoy'] or 0) else f"{p['valmoy'].replace('.', ',')} / 100 000 (valeur moyenne)"
        nais = 'naissance' in p['type'].lower()
        x = dict(cle=f"orpha:{code}:{p['id']}", source='Orphanet / Orphadata (CC BY 4.0)', valeur_txt=val,
                 unite='pour 100 000 naissances' if nais else 'pour 100 000 personnes',
                 population=('naissances vivantes' if nais else 'population générale') + f" – {p['geo']}",
                 age_sexe='non stratifié (tous âges, deux sexes)', definition=f"ORPHA:{code} « {nom} » (nomenclature Orphanet)",
                 mesure=f"{p['type']} ({p['qualif'].lower()})", annee=('publication ' + '–'.join(sorted(set(yrs)))) if yrs else '',
                 territoire=p['geo'], type_source='base curée Orphanet ; source primaire citée : ' + (', '.join(f'PMID {x}' for x in pm) or p['source']),
                 url=f'https://www.orpha.net/fr/disease/detail/{code}', preuve=f"fr_product9_prev.xml (Orphadata {meta.get('date')}) Prevalence id={p['id']} : {p['type']} | {p['classe'] or p['valmoy']} | {p['geo']}",
                 sha256=meta.get('sha', ''), hors_ch=int(p['geo'] != 'Suisse'))
        x['phrase'] = f"{x['mesure'].split(' (')[0]} de {nom} : {val} ({x['territoire']}, {x['annee'] or 'année non précisée'} ; Orphanet)."
        x['statut'] = 'vérifié' if all(x[k] for k in CTX) else 'contexte incomplet'
        P.append(x)
    return P[:3]

# ---------------------------------------------------------------- Wikidata (traduction) et Europe PMC
def anglais(fr):
    """Nom anglais via Wikidata : premier des 5 résultats qui a un libellé anglais."""
    u = 'https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json&language=fr&uselang=en&limit=5&search=' + urllib.parse.quote(fr)
    t, *_ = fetch(u)
    try:
        for r in json.loads(t)['search']:
            if r.get('match', {}).get('language') == 'fr' and r.get('label') and r['label'] != r['match'].get('text'):
                return r['label'], r['id']
    except Exception:
        pass
    return None, None

CHIFFRE = re.compile(r'[^.]*\b(prevalen|incidence|per 100[ ,.]?000|per 1000|%|‰)[^.]*\d[^.]*\.', re.I)
def extraits(cands):
    """Phrases chiffrées des résumés (aide à la lecture, jamais une valeur vérifiée)."""
    ids = [x['pmid'] for x in cands if x.get('pmid')][:5]
    if not ids: return
    t, *_ = fetch(EPMC.replace('resultType=lite', 'resultType=core').replace('pageSize=5', 'pageSize=10') + urllib.parse.quote('SRC:MED AND (' + ' OR '.join(f'EXT_ID:{i}' for i in ids) + ')'))
    if not t: return
    ab = {r.get('pmid'): re.sub('<[^>]+>', ' ', r.get('abstractText', '')) for r in json.loads(t).get('resultList', {}).get('result', [])}
    for x in cands:
        if x.get('pmid') in ab:
            x['extraits'] = [m.group(0).strip()[:400] for m in CHIFFRE.finditer(ab[x['pmid']])][:3]

def epmc(q):
    t, sha, date, _ = fetch(EPMC + urllib.parse.quote(q))
    if not t: return None, []
    j = json.loads(t)
    return j.get('hitCount', 0), [dict(pmid=r.get('pmid'), id=r.get('id'), annee=r.get('pubYear'), titre=r.get('title'), revue=r.get('journalTitle'),
                                       oa=r.get('isOpenAccess')) for r in j.get('resultList', {}).get('result', [])]

def niveau(lib, nom, T, O, d):
    """Une recherche (lib = 'Europe' ou 'Suisse') : Orphanet + Europe PMC. Retourne statut, params, sources, candidats."""
    noms, prev, meta, ans = O
    src, cand, P = [], [], []
    code = noms.get(norm(nom).strip()) or noms.get(norm(nom_court(nom)).strip())
    if code:
        P = [p for p in params_orphanet(code, prev, meta, ans) if (p['territoire'] == 'Suisse') == (lib == 'Suisse')]
    src.append(f"Orphanet/Orphadata {meta.get('date')} : " + (f"ORPHA:{code}, {len(P)} valeur(s) {lib}" if code else 'aucune entrée au nom exact') + f' ({d})')
    reg = CH_Q if lib == 'Suisse' else EU_Q
    hits = 0
    for niv, champ in (('titre épidémio', 'TITLE'), ('résumé', 'ABSTRACT')):
        termes = ' OR '.join(f'{champ}:"{x}"' for x in T)
        epi = '(TITLE:prevalence OR TITLE:incidence OR TITLE:epidemiology OR TITLE:burden OR TITLE:frequency)' if champ == 'TITLE' else '(prevalence OR incidence OR epidemiology)'
        n, L = epmc(f'({termes}) AND {epi} AND {reg}')
        src.append(f'Europe PMC {lib} ({niv}) : {n if n is not None else "erreur"} résultat(s) ({d})')
        if n is None: hits = None; break
        hits += n; cand += [dict(x, requete=f'{lib} – {niv}') for x in L]
        if n: break
    extraits(cand)
    ok = [p for p in P if p['statut'] == 'vérifié']
    st = 'vérifié' if ok else 'candidats à lire' if (hits or P) else 'à faire' if hits is None else 'à revoir (0 résultat automatique)'
    return st, P[:3], src, cand

def chercher(nom, O):
    d = maintenant()[:10]
    court = nom_court(nom); en, qid = anglais(court)
    if not en:   # variantes : sans préfixe générique, puis dernier groupe de mots
        for v in (re.sub(r"^(infection|maladie|syndrome|trouble|atteinte)s?\s+(par le |par la |par l'|à |a |de |du |des )?", '', court, flags=re.I),
                  court.split(',')[0], ' '.join(court.split()[-2:]), court.split()[-1]):
            if v and v != court and len(v) > 2:
                en, qid = anglais(v)
                if en: break
    sous = [x.strip() for x in re.split(r',|/| et |\(|\)|;', nom or '') if len(x.strip()) > 3]
    T = list(dict.fromkeys([court] + ([en] if en else []) + sous))[:6]
    tr = f"Wikidata (traduction) : {qid or 'aucune'} {('« ' + en + ' »') if en else ''} ({d})"
    with ThreadPoolExecutor(2) as ex:             # Europe et Suisse en même temps, sans attendre l'échec de l'un
        fe, fc = ex.submit(niveau, 'Europe', nom, T, O, d), ex.submit(niveau, 'Suisse', nom, T, O, d)
        E, C = fe.result(), fc.result()
    return (E[0], E[1], [tr] + E[2], E[3]), (C[0], C[1], [tr] + C[2], C[3])

# valeurs européennes vérifiées à la main (PR #743), contexte complet relu sur le résumé PubMed 21896369
MANUELS_EU = {(4, 8): [dict(cle='pmid:21896369', source='Wittchen et al., Eur Neuropsychopharmacol 2011', valeur_txt='14,0', unite='% de la population',
    population='population de l’UE-27, de la Suisse, de l’Islande et de la Norvège', age_sexe='tous âges couverts (enfance à grand âge selon les troubles) ; deux sexes',
    definition='trouble anxieux (critères DSM-IV), toutes formes réunies', mesure='prévalence sur 12 mois (2010)', annee='2010 (publication 2011)',
    territoire='Europe (UE-27 + CH, IS, NO)', type_source='revues systématiques, réanalyses et enquêtes nationales', url='https://pubmed.ncbi.nlm.nih.gov/21896369/',
    preuve='Résumé : « Studies and data from all member states of the European Union (EU-27) plus Switzerland, Iceland and Norway were included »',
    sha256='', hors_ch=1, statut='vérifié', phrase='En 2010, 14,0 % de la population européenne présentait un trouble anxieux sur douze mois.')]}
A_VERIFIER_EU = {(30, 7): 'EPOS 2020 : 5,5–28 % (âge/sexe des études à relire)', (32, 8): 'Allemagne 2005–2021 : 5,4 → 11,0/100 000 (âge/sexe à relire, PMC10657388)',
                 (32, 1): 'GBD 2017 mondial : hors Europe, ne compte pas'}

COLS = ['lot', 'dx', 'diagnostic', 'classe', 'entite', 'priorite', 'statut_eu', 'params_eu', 'sources_eu', 'candidats_eu',
        'statut_ch', 'params_ch', 'sources_ch', 'candidats_ch', 'date', 'agent']

def schema(c):
    cols = [r[1] for r in c.execute('PRAGMA table_info(taches)')]
    if cols and 'statut_eu' not in cols: c.execute('DROP TABLE taches')
    c.execute('''CREATE TABLE IF NOT EXISTS taches(lot INT, dx INT, diagnostic TEXT, classe TEXT, entite TEXT, priorite INT,
      statut_eu TEXT, params_eu TEXT, sources_eu TEXT, candidats_eu TEXT, statut_ch TEXT, params_ch TEXT, sources_ch TEXT, candidats_ch TEXT,
      date TEXT, agent TEXT, PRIMARY KEY(lot, dx))''')

def initialiser(c):
    schema(c)
    deja = {(a, b) for a, b in c.execute('SELECT lot,dx FROM taches')}
    res = {(r[0], r[1]): json.loads(r[2]) for r in c.execute('SELECT lot,dx,json FROM resultats')}
    for lot, dx, dg, k in c.execute('SELECT lot,dx,diagnostic,classe FROM applicabilite').fetchall():
        if k == 'N':
            c.execute('DELETE FROM taches WHERE lot=? AND dx=?', (lot, dx)); continue
        prio = {'A': 1, 'B': 2, 'C': 3}[k]
        pch = [p for p in res.get((lot, dx), {}).get('params', []) if p['statut'] == 'vérifié' and not p.get('hors_ch')]
        peu = MANUELS_EU.get((lot, dx), [])
        if (lot, dx) not in deja:
            c.execute(f'INSERT INTO taches VALUES({",".join("?" * 16)})', (lot, dx, dg, k, norm(nom_court(dg)).strip(), prio,
                'vérifié' if peu else 'à faire', json.dumps(peu, ensure_ascii=False), json.dumps([A_VERIFIER_EU[(lot, dx)]] if (lot, dx) in A_VERIFIER_EU else [], ensure_ascii=False), '[]',
                'vérifié' if pch else 'à faire', json.dumps(pch, ensure_ascii=False), json.dumps(['réseau suisse (OFS, OFSP-IDD, ONEC, Obsan)'] if pch else [], ensure_ascii=False), '[]',
                maintenant(), ''))
        else:
            c.execute('UPDATE taches SET classe=?, priorite=?, diagnostic=? WHERE lot=? AND dx=?', (k, prio, dg, lot, dx))
            if pch: c.execute("UPDATE taches SET statut_ch='vérifié', params_ch=? WHERE lot=? AND dx=? AND statut_ch!='vérifié'", (json.dumps(pch, ensure_ascii=False), lot, dx))
    c.commit()

def conforme(p, niv):
    """Une valeur compte seulement si les 8 colonnes de contexte, la valeur, la source et l'URL sont remplies, et le territoire européen."""
    manque = [k for k in CTX + ['valeur_txt', 'url', 'source'] if not str(p.get(k, '')).strip()]
    terr = norm(p.get('territoire', ''))
    if niv == 'ch' and 'suisse' not in terr: manque.append('territoire suisse')
    if niv == 'eu' and not any(norm(x) in terr for x in PAYS_EU + ['UE', 'EU', 'europ']): manque.append('territoire européen')
    if any(m in terr for m in ('monde', 'mondial', 'global', 'etats-unis', 'usa', 'chine', 'japon', 'canada', 'australie', 'inde', 'bresil')): manque.append('hors Europe')
    return manque

def importer_autres(c, racine_depot=None):
    """Fusionne (lecture seule) les niveaux déjà vérifiés par les autres IA : <Dossier>/<IA>__Completude_Epidemio/taches.jsonl."""
    r = racine_depot or os.environ.get('EPI_DEPOT')
    if not r or not os.path.isdir(r): return 0
    n = 0
    fichiers = [('etat partagé', os.path.join(r, 'tools', 'epidemio_reseau', 'etat', 'taches.jsonl'))]
    for d in os.listdir(r):
        if d.startswith('psychotherapie') or not os.path.isdir(os.path.join(r, d)): continue     # dossier privé : jamais lu
        for s in os.listdir(os.path.join(r, d)):
            if s.endswith('__Completude_Epidemio'): fichiers.append((s, os.path.join(r, d, s, 'taches.jsonl')))
    for s, f in fichiers:
            if not os.path.exists(f) or os.path.abspath(os.path.dirname(f)) == os.path.abspath(os.environ.get('EPI_SORTIE', '')): continue
            for l in open(f, encoding='utf-8'):
                t = json.loads(l)
                for niv in ('eu', 'ch'):
                    if t.get(f'statut_{niv}') == 'vérifié' and t[f'params_{niv}'] and not any(conforme(p, niv) for p in t[f'params_{niv}']):
                        cur = c.execute(f'UPDATE taches SET statut_{niv}=?, params_{niv}=?, sources_{niv}=? WHERE lot=? AND dx=? AND statut_{niv}!=?',
                                        ('vérifié', json.dumps(t[f'params_{niv}'], ensure_ascii=False), json.dumps(t[f'sources_{niv}'] + [f'importé de {s}'], ensure_ascii=False),
                                         t['lot'], t['dx'], 'vérifié'))
                        n += cur.rowcount
    c.commit(); return n

def exporter_jsonl(c, chemin):
    with open(chemin + '.tmp', 'w', encoding='utf-8') as f:
        for r in c.execute('SELECT * FROM taches ORDER BY priorite, lot, dx'):
            d = dict(zip(COLS, r))
            for k in COLS:
                if k.startswith(('params', 'sources', 'candidats')): d[k] = json.loads(d[k])
            f.write(json.dumps(d, ensure_ascii=False) + '\n')
    os.replace(chemin + '.tmp', chemin)

def executer(limite=None, agent=os.environ.get('EPI_AGENT', 'Grokbot'), plan=None):
    c = db(); initialiser(c); journal(f'recherche : {importer_autres(c)} niveaux importés des autres IA')
    todo = c.execute("SELECT entite, MIN(priorite), MIN(lot) FROM taches WHERE statut_eu='à faire' OR statut_ch='à faire' "
                     "GROUP BY entite ORDER BY MIN(priorite), MIN(lot)").fetchall()
    if limite: todo = todo[:limite]
    if not todo: return c
    noms, prev, meta = orphanet()
    codes = {noms.get(e) for e, *_ in todo}
    pm = [x for k in codes if k in prev for p in prev[k][1] for x in re.findall(r'(\d+)\[PMID\]', p['source'])]
    O = (noms, prev, meta, annees_pmid(pm))
    def un(e):
        dg = c.execute('SELECT diagnostic FROM taches WHERE entite=? ORDER BY lot LIMIT 1', (e,)).fetchone()[0]
        return e, chercher(dg, O)
    with ThreadPoolExecutor(3) as ex:
        for i, (e, (E, C)) in enumerate(ex.map(un, [t[0] for t in todo])):
            for niv, (st, P, src, cand) in (('eu', E), ('ch', C)):
                c.execute(f"UPDATE taches SET statut_{niv}=?, params_{niv}=?, sources_{niv}=?, candidats_{niv}=?, date=?, agent=? WHERE entite=? AND statut_{niv}!='vérifié'",
                          (st, json.dumps(P, ensure_ascii=False), json.dumps(src, ensure_ascii=False), json.dumps(cand, ensure_ascii=False), maintenant(), agent, e))
            c.execute("INSERT OR REPLACE INTO checkpoint VALUES('recherche', ?, ?)", (f'{i + 1}/{len(todo)} entités', maintenant())); c.commit()
            if plan and i % 25 == 0: plan()
    c.commit(); journal(f'recherche : {len(todo)} entités traitées'); return c

if __name__ == '__main__':
    lim = int(sys.argv[1]) if len(sys.argv) > 1 else int(os.environ.get('EPI_LIMITE', 0)) or None
    import plan as PL
    executer(lim, plan=PL.generer)
    PL.generer()
