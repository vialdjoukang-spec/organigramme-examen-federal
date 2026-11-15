#!/usr/bin/env python3
"""Légion de concordance : chaque valeur du référentiel est confrontée, en parallèle,
(1) au cours de référence du DX (carte_lots.json : main ou branche qui fait foi) et
(2) à la source que ce cours cite pour le même chiffre (page téléchargée, chiffre recherché dans le texte).
Statuts : concordant (même chiffre dans une phrase citée du cours, URL de la source) ; discordant (chiffre du même
genre pour la même population, différent) ; non_verifiable (aucun cours, chiffre absent, source sans URL).
preuve_web : trouve / absent / inaccessible / sans_url. Sorties : out/CONCORDANCE.csv, out/CONCORDANCE.md, out/concordance.json"""
import json, re, os, sys, csv, subprocess, html as H, collections, tempfile
from multiprocessing import Pool
from concurrent.futures import ThreadPoolExecutor
ICI = os.path.dirname(os.path.abspath(__file__)); OUT = os.path.join(os.path.dirname(ICI), 'out')
sys.path.insert(0, ICI)
import inject as I
REPO = I.REPO; BRIEF = I.BRIEF
OFFICIELS = re.compile(r'admin\.ch|bfs\.|bag\.|obsan|nicer\.org|swisstransplant|toxinfo|swissnoso|suva\.ch|sentinella|ofsp|ofs\b|onec|kinderkrebsregister|swisscancer|krebsliga|liguecancer|statistique', re.I)

def git_show(ref, chemin):
    return subprocess.run(['git', '-C', REPO, 'show', f'{ref}:{chemin}'], capture_output=True).stdout.decode('utf-8', 'ignore')

SEP = '[ \u00a0\u202f\u2009’\']?'

def motifs(valeur):
    """Expressions exigées dans la même phrase : chaque nombre clé ; le dernier suivi de % si la valeur est en %, « 100 000 » si taux."""
    ks = sorted(I.cles(valeur), key=lambda x: valeur.find(x.replace('.', ',')) if x.replace('.', ',') in valeur else 99)
    g = I.genre(valeur); out = []
    for k in ks:
        ent, _, dec = k.partition('.')
        e = re.sub(r'(\d)(?=(\d{3})+$)', lambda m: m.group(1) + SEP, ent) if len(ent) > 4 or (len(ent) == 4 and g == 'nombre') else ent
        out.append(e + (r'[.,]' + dec if dec else r'(?![.,]\d)'))
    return [rf'(?<![\d.,]){p}' for p in out], g

def phrases(h):
    corps = re.sub(r'<(script|style)\b.*?</\1>', ' ', h, flags=re.S | re.I)
    blocs = re.findall(r'<(p|li|td|dd|div)\b[^>]*>(.*?)</\1>', corps, re.S | re.I)
    for _, b in blocs:
        for brut in re.split(r'(?<=[.;!?])\s+(?=[A-ZÀ-Ý«(])', b):
            yield brut, I.txt(brut)

def url_de(h, brut):
    urls = []
    for ident in re.findall(r'href="#([^"]+)"', brut):
        m = re.search(rf'id="{re.escape(ident)}"', h)
        if m:
            u = re.search(r'https?://[^"\'<>\s]+', h[m.end():m.end() + 2500])
            if u: urls.append(H.unescape(u.group(0)).rstrip('.,;)'))
    for s in re.findall(r'\[(S\d+)\]', I.txt(brut)):
        m = re.search(rf'id="[\w-]*{s}"', h)
        if m:
            u = re.search(r'https?://[^"\'<>\s]+', h[m.end():m.end() + 2500])
            if u: urls.append(H.unescape(u.group(0)).rstrip('.,;)'))
    return list(dict.fromkeys(urls))

def confronter(tache):
    r, c, ref, chemin = tache
    base = {'n': r['n'], 'code': r['code_ssp'], 'entite': r['entite'], 'type': r['type_libelle'], 'valeur': r['valeur'],
            'population': r['population'], 'source_ref': r['source'], 'classe': r['classe_source'],
            'lot': c.get('lot', ''), 'lecon': c.get('lecon', ''), 'statut_dx': c.get('statut', ''), 'fichier': chemin or '', 'ref': ref or ''}
    if not chemin:
        return {**base, 'statut': 'non_verifiable', 'motif': 'aucun cours pour ce DX', 'preuve': '', 'urls': []}
    h = git_show(ref, chemin)
    pats, g = motifs(r['valeur'])
    if not pats:
        return {**base, 'statut': 'non_verifiable', 'motif': 'valeur sans nombre', 'preuve': '', 'urls': []}
    n_dx = int(c['lecon'][2:]) if c.get('lecon', '').startswith('DX') else None
    if n_dx:
        d, f, _ = I.portee_dx(h, n_dx)
        if d is not None: h_dx = h[d:f]
        else: h_dx = h
    else: h_dx = h
    trouve = None
    for brut, t in phrases(h_dx):
        if all(re.search(p, t) for p in pats) and (g != 'pct' or re.search(pats[-1] + r'\s?%', t)) and \
           (g != 'taux' or re.search(r'100[  \u202f]?000|pour 100', t)) and \
           (len(pats) > 1 or I.comparable(r, t)):  # un chiffre isolé exige aussi la même population ou unité
            u = url_de(h, brut)
            if trouve is None or (u and not trouve[2]): trouve = (brut, t, u)
            if u: break
    if trouve:
        _, t, u = trouve
        if u:
            return {**base, 'statut': 'concordant', 'motif': 'même chiffre dans une phrase citée du cours', 'preuve': t[:300], 'urls': u}
        return {**base, 'statut': 'non_verifiable', 'motif': 'chiffre présent dans le cours, source citée sans URL', 'preuve': t[:300], 'urls': []}
    hs = re.sub(r'<!-- EPI_PROFILES:DEBUT.*?EPI_PROFILES:FIN DX\d+ -->', '', h, flags=re.S)
    loc, _ = I.localiser(hs, n_dx) if n_dx else (None, '')
    sect = I.txt(hs[loc[0]:loc[1]]) if loc else ''
    conf = [x for x in I.present_genre(sect, I.genre(r['valeur'])) if I.comparable(r, x)]
    if conf:
        return {**base, 'statut': 'discordant', 'motif': 'le cours donne un autre chiffre du même genre pour la même population', 'preuve': conf[0].strip()[:300], 'urls': []}
    return {**base, 'statut': 'non_verifiable', 'motif': 'chiffre absent du cours ; aucune source primaire liée', 'preuve': '', 'urls': []}

CACHE = os.path.join(OUT, 'pages_cache')

def page_texte(u):
    """Texte d'une page source ; cache disque, trois essais (les sites officiels répondent parfois lentement)."""
    import hashlib
    os.makedirs(CACHE, exist_ok=True); fc = os.path.join(CACHE, hashlib.sha1(u.encode()).hexdigest() + '.txt')
    if os.path.exists(fc) and os.path.getsize(fc) > 200: return open(fc, encoding='utf-8').read()
    for _ in range(3):
        t = _page(u)
        if t and len(t) > 200:
            open(fc, 'w', encoding='utf-8').write(t); return t
    return t

def _page(u):
    try:
        r = subprocess.run(['curl', '-sL', '--max-time', '40', '--max-filesize', '15000000', '-A', 'Mozilla/5.0', '-o', '-', u], capture_output=True)
        b = r.stdout
        if not b: return None
        if b[:4] == b'%PDF':
            with tempfile.NamedTemporaryFile(suffix='.pdf', delete=False) as f: f.write(b); p = f.name
            t = subprocess.run(['pdftotext', '-q', p, '-'], capture_output=True).stdout.decode('utf-8', 'ignore'); os.unlink(p); return t
        return I.txt(b.decode('utf-8', 'ignore'))
    except Exception:
        return None

# Revue humaine des concordances « trouve » (15.11.2026) : même chiffre mais autre mesure ou autre population.
REVUE_REJET = {6: 'le cours donne 5 à 10 % pour la ménopause anticipée, pas pour les formes sévères',
               25: 'le cours cite une enquête allemande (10 % des hommes, 20 % des femmes), pas l\'ESS 2022',
               41: 'le cours donne 7 % pour le prurit chronique en général, pas pour le prurit psychogène',
               63: 'le cours écrit « jusqu\'à 3 % », la borne 2 % manque',
               68: 'le cours donne 50 à 70 % (part idiopathique), pas une incidence de 50 / 100 000',
               75: 'le cours donne environ 1 et 1,07 à 2,2 / 100 000 : approximation, pas identité',
               82: 'le cours vise l\'enfant, le référentiel le nourrisson de moins d\'un an',
               87: 'le cours donne 27 % en population générale, le référentiel une part parmi les rhinites chroniques',
               89: 'le cours donne 18 % pour la rhinite non allergique, pas pour la rhinite médicamenteuse',
               91: 'le cours parle de prévalence, le référentiel d\'incidence',
               127: 'le cours donne 20 % pour la douleur neuropathique, pas pour la polyneuropathie'}

def main():
    mp = json.load(open(f'{OUT}/mapping.json')); carte = json.load(open(f'{BRIEF}/carte_lots.json'))['lecons']
    taches = []
    for r in mp:
        for c in r['cibles']:
            v = carte.get(f"{c['lot']:03d}:{c['lecon']}") if 'lot' in c else None
            taches.append((r, c, v['ref'] if v else None, v['chemin'] if v else None))
    with Pool(min(16, os.cpu_count() or 4)) as p:
        res = p.map(confronter, taches)
    urls = sorted({u for x in res for u in x['urls']})
    with ThreadPoolExecutor(24) as ex:
        pages = dict(zip(urls, ex.map(page_texte, urls)))
    for x in res:
        x['officielle'] = any(OFFICIELS.search(u) for u in x['urls'])
        if not x['urls']: x['preuve_web'] = 'sans_url'; continue
        pats, _ = motifs(x['valeur'])
        etats = []
        for u in x['urls']:
            t = pages.get(u)
            if t is None: etats.append('inaccessible'); continue
            t = re.sub(r'\s+', ' ', t)
            ok = all(re.search(p, t) for p in pats) and (I.genre(x['valeur']) != 'pct' or re.search(pats[-1] + r'\s?%', t))
            etats.append('trouve' if ok else 'absent')
        x['preuve_web'] = 'trouve' if 'trouve' in etats else ('absent' if 'absent' in etats else 'inaccessible')
        x['url_preuve'] = next((u for u, e in zip(x['urls'], etats) if e == 'trouve'), x['urls'][0])
    # une valeur est concordante si au moins une de ses cibles l'est
    par = collections.defaultdict(list)
    for x in res: par[x['n']].append(x)
    final = []
    for n, xs in sorted(par.items()):
        best = sorted(xs, key=lambda x: ({'concordant': 0, 'discordant': 1, 'non_verifiable': 2}[x['statut']],
                                          {'trouve': 0, 'absent': 1, 'inaccessible': 2, 'sans_url': 3}[x['preuve_web']]))[0]
        final.append(best)
    for x in final:
        x['revue'] = ''
        if x['statut'] == 'concordant' and x['n'] in REVUE_REJET:
            x['statut'], x['motif'], x['revue'] = 'discordant', 'revue : ' + REVUE_REJET[x['n']], 'rejet'
        elif x['statut'] == 'concordant' and x['preuve_web'] != 'trouve':
            x['statut'], x['motif'] = 'non_verifiable', f"chiffre présent dans le cours, mais la page source ne le montre pas ({x['preuve_web']})"
        elif x['statut'] == 'concordant':
            x['revue'] = 'validé'
    json.dump(final, open(f'{OUT}/concordance.json', 'w'), ensure_ascii=False, indent=1)
    champs = ['revue', 'n', 'code', 'entite', 'type', 'valeur', 'population', 'source_ref', 'classe', 'lot', 'lecon', 'statut', 'preuve_web',
              'officielle', 'motif', 'preuve', 'url_preuve', 'fichier', 'ref']
    with open(f'{OUT}/CONCORDANCE.csv', 'w', newline='', encoding='utf-8') as f:
        w = csv.DictWriter(f, fieldnames=champs, extrasaction='ignore'); w.writeheader()
        for x in final: w.writerow({**x, 'url_preuve': x.get('url_preuve', '')})
    cnt = collections.Counter(x['statut'] for x in final)
    cw = collections.Counter((x['statut'], x['preuve_web']) for x in final)
    L = ['# Concordance du référentiel épidémiologique PROFILES 2023', '',
         f'{len(final)} valeurs confrontées en parallèle ({len(taches)} cibles, {len(urls)} pages sources téléchargées).',
         f'Statuts : {dict(cnt)}.', f'Détail statut × preuve web : { {f"{a}/{b}": v for (a, b), v in sorted(cw.items())} }.', '',
         'Une valeur concordante (véridique et prouvée) remplit trois conditions : le même chiffre figure dans une phrase du cours qui cite une source avec URL ; la page de cette source, téléchargée, contient ce chiffre ; la revue humaine confirme la même mesure et la même population.',
         '']
    for st in ('concordant', 'discordant', 'non_verifiable'):
        L += [f'## {st} ({cnt[st]})', '']
        for x in final:
            if x['statut'] != st: continue
            u = x.get('url_preuve', '')
            L.append(f"- #{x['n']} LOT {x['lot'] if x['lot']=='' else format(x['lot'],'03d')} {x['lecon']} · **{x['entite']}** : {x['valeur']} ({x['source_ref']}) · web : {x['preuve_web']}"
                     + (f" · [source]({u})" if u else '') + f" · {x['motif']}" + (f" · « {x['preuve'][:160]} »" if x['preuve'] else ''))
        L.append('')
    open(f'{OUT}/CONCORDANCE.md', 'w').write('\n'.join(L) + '\n')
    N = ['# Valeurs non injectées et motif', '', f"{sum(x['statut'] != 'concordant' for x in final)} valeurs restent hors injection : discordantes ou non vérifiables.", '']
    for st in ('discordant', 'non_verifiable'):
        N += [f'## {st} ({cnt[st]})', '']
        for x in final:
            if x['statut'] == st:
                N.append(f"- #{x['n']} {x['code']} · **{x['entite']}** : {x['valeur']} ({x['source_ref']}) · {x['motif']}" + (f" · [source]({x['url_preuve']})" if x.get('url_preuve') else ''))
        N.append('')
    open(f'{OUT}/NON_INJECTE.md', 'w').write('\n'.join(N) + '\n')
    print(dict(cnt)); print(dict(cw))

if __name__ == '__main__':
    main()
