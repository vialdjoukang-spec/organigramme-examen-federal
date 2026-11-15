#!/usr/bin/env python3
"""Injecte, de façon idempotente, un encadré « Repère suisse PROFILES 2023 » à la fin de la rubrique
épidémiologie (point 2 du gabarit 14 points) de chaque DX rattaché.

Usage :
  inject.py --dry-run            rapport out/DRYRUN.md, aucune écriture de cours
  inject.py --apply              écrit les cours modifiés dans out/stage/<chemin du dépôt>
  inject.py --apply --base out/stage   relance sur les fichiers déjà injectés (test d'idempotence)
Règles : version de référence = carte_lots.json (detecteur_lots.py) et seulement si elle vit sur origin/main
avec le même blob ; aucun chiffre existant remplacé ; conflit probable => pas d'injection, ligne dans CONFLITS.md ;
taille finale 90 000 ≤ octets < 150 000 (fichier déjà < 90 000 : injection permise, signalée) ; balises équilibrées."""
import json, re, os, sys, html as H, subprocess, argparse, collections
ICI = os.path.dirname(os.path.abspath(__file__)); RACINE = os.path.dirname(ICI); OUT = f'{RACINE}/out'
BRIEF = '/workspace/Leona__Brief_Redaction_LOTs_20261115/scripts'; REPO = '/workspace/grok/etude/repo'
MIN, MAX = 90_000, 150_000
EN_PRODUCTION = set(range(125, 133))  # LOTs repris par les agents A/B et l'executor (13.11–15.11.2026) : on n'y touche pas
DEB = '<!-- EPI_PROFILES:DEBUT DX{n} -->'; FIN = '<!-- EPI_PROFILES:FIN DX{n} -->'
MESURE = {'Prévalence': 'une prévalence de', 'Incidence': 'une incidence de', 'Cas annuels': 'un volume de',
          'Effectif total': 'un effectif de', 'Fréq. cohorte': 'une fréquence de', 'Part du motif': 'une part de'}
VIDES = {'br', 'hr', 'img', 'meta', 'link', 'input', 'source', 'col', 'wbr', 'area', 'base', 'embed', 'track', 'param'}
NUM = re.compile(r'(?<![\w])(\d{1,3}(?:[ \u202f\u00a0’\']\d{3})+|\d+(?:[.,]\d+)?)(?![\w])')

def git(*a): return subprocess.run(['git', '-C', REPO, *a], capture_output=True).stdout

def equilibre(h):
    pile = []
    h = re.sub(r'<(script|style)\b[^>]*>.*?</\1>', '', h, flags=re.S | re.I); h = re.sub(r'<!--.*?-->', '', h, flags=re.S)
    for ferme, nom in re.findall(r'<(/?)([a-zA-Z][\w-]*)\b[^>]*?(?<!/)>', h):
        nom = nom.lower()
        if nom in VIDES: continue
        if not ferme: pile.append(nom)
        elif pile and pile[-1] == nom: pile.pop()
        elif nom in pile: return f'fermeture </{nom}> mal placée'
    return None if not pile else f'non fermées: {pile[-5:]}'

def txt(f): return re.sub(r'\s+', ' ', H.unescape(re.sub(r'<[^>]+>', ' ', f))).strip()

def nums(s):
    out = set()
    for n in NUM.findall(s):
        n = re.sub(r'[ \u202f\u00a0’\']', '', n).replace(',', '.')
        out.add(n.lstrip('0') or '0')
    return out

def cles(valeur):
    """Nombres significatifs d'une valeur (sans les dénominateurs 100 000, 10 000, 1 000)."""
    v = re.sub(r'/\s*(100|10|1)[ \u202f\u00a0]?000\b', ' ', valeur)
    return nums(v)

def genre(valeur):
    if '%' in valeur: return 'pct'
    if re.search(r'/\s*100[ \u202f\u00a0]?000|pour 100', valeur): return 'taux'
    return 'nombre'

def present_genre(t, g):
    if g == 'pct': return re.findall(r'[^.]*\d\s?%[^.]*', t)
    if g == 'taux': return re.findall(r'[^.]*100[ \u202f\u00a0]?000[^.]*', t)
    return re.findall(r'[^.]*\d{1,3}(?:[ \u202f\u00a0’]\d{3})+[^.]*', t)

GENERIQUES = set('suisse suisses population generale personnes habitants hab annee annees an ans par cas pour plus total totale adultes adulte nombre selon chaque'.split())
UNITES = set('cas deces morts personnes consultations hospitalisations appels admissions accidents naissances interventions patients dons greffes'.split())

def mots(s):
    import unicodedata
    s = unicodedata.normalize('NFD', s.lower()); s = ''.join(c for c in s if unicodedata.category(c) != 'Mn')
    return set(re.findall(r'[a-z]{4,}|\d+', s))

def comparable(r, phrase):
    """Conflit probable : même genre de chiffre ET même population (mot spécifique commun) ou, pour un effectif, même unité."""
    ph = mots(phrase); ent = mots(r['entite'])
    pop = mots(r['population']) - GENERIQUES - ent
    if pop & ph: return True
    if genre(r['valeur']) == 'nombre' and (mots(r['valeur']) & UNITES & ph): return True
    return False

def minus(s): return s[0].lower() + s[1:] if len(s) > 1 and s[1].islower() else s

def bloc(n, rows):
    ps, srcs = [], []
    for r in rows:
        a = f'<sup class="r"><a href="#sb-epi-dx{n}">EPI</a></sup>'
        e = lambda x: H.escape(x, quote=False)
        ps.append(f'<p>Pour « {e(r["entite"])} », la source « {e(r["source"])} » indique {MESURE.get(r["type_libelle"], "une valeur de")} '
                  f'{e(r["valeur"])}{a}. Cette valeur concerne : {e(minus(r["population"]))}{a}.</p>')
        s = e(r['source']) + (f' ({r["annee"]})' if r['annee'] and r['annee'] not in r['source'] else '')
        if r['classe_source'] == 'non_primaire': s += ' : source non primaire, à vérifier'
        if not r['annee']: s += ' ; année non précisée'
        if s not in srcs: srcs.append(s)
    return (DEB.format(n=n) + '\n<div class="epi-profiles" style="background:#F3FAFD;border:1px solid #87CEEB;'
            'border-radius:6px;padding:6px 10px;margin:8px 0">\n<div><strong>Repère suisse : référentiel PROFILES 2023'
            '</strong></div>\n' + '\n'.join(ps) + f'\n<div id="sb-epi-dx{n}" style="font-size:.85em">Sources : '
            + ' ; '.join(srcs) + '. Relevé : audit épidémiologique PROFILES 2023 (248 SSP), 15.11.2026.</div>\n</div>\n'
            + FIN.format(n=n))

RE_H = re.compile(r'<(h[1-5])\b[^>]*>(.*?)</\1>', re.S | re.I)

RE_DXM = re.compile(r'<(h[1-5]|p|div|summary)\b[^>]*>\s*(?:<(?:strong|b|span)[^>]*>\s*)*((?:[^<\s]+\s+)?DX\.?\s*0?(\d+)\s*[—–:-])', re.I)

def portee_dx(h, n):
    """Bornes du DX n dans un fichier multi-DX (titres ou pseudo-titres « DX.k — … ») ; sinon tout le fichier."""
    marques = [(m.start(), int(m.group(3))) for m in RE_DXM.finditer(h)]
    # garder le premier repère de chaque série consécutive du même DX
    serie = [x for i, x in enumerate(marques) if i == 0 or marques[i - 1][1] != x[1]]
    if len({k for _, k in serie}) <= 1: return 0, len(h), 'mono'
    deb = [p for p, k in serie if k == n]
    if len(deb) != 1: return None, None, f'DX.{n} absent ou répété dans le fichier multi-DX'
    d = deb[0]; f = next((p for p, k in serie if p > d and k != n), len(h))
    return d, f, 'multi'

RE_PSEUDO = re.compile(r'<(p|div)\b[^>]*>\s*(?:<p>\s*)?<(strong|b)>\s*(\d{1,2})\s*\.\s*([^<]{0,80})</\2>', re.I)

def localiser(h, n):
    """Rubrique épidémiologie du DX n : vrai titre h2–h5, sinon pseudo-titre <p|div><strong>2. Épidémiologie</strong>."""
    d, f, mode = portee_dx(h, n)
    if d is None: return None, mode
    zone = [m for m in RE_H.finditer(h, d, f) if re.search(r'pid[ée]miolog', txt(m.group(2)), re.I)]
    if zone:
        m = next((z for z in zone if re.match(r'\s*2\s*[.)]', txt(z.group(2)))), zone[0])
        lvl = int(m.group(1)[1])
        nxt = re.compile(rf'<h[1-{lvl}]\b', re.I).search(h, m.end(), f)
        stop = nxt.start() if nxt else f
        seg = h[m.end():stop]
        i = seg.find('</section>')
        if i >= 0: return (m.start(), m.end() + i), mode
        pos = stop
        pre = re.search(r'(?:<(?:section|div|article|details)\b[^>]*>\s*)+$', h[m.end():stop])
        if pre: pos = m.end() + pre.start()
        return (m.start(), pos), mode
    ps = [m for m in RE_PSEUDO.finditer(h, d, f) if m.group(3) == '2' and re.search(r'pid[ée]miolog', m.group(4), re.I)]
    if len(ps) != 1: return None, f'rubrique épidémiologie introuvable ou ambiguë ({mode}, {len(ps)} pseudo-titres)'
    m = ps[0]
    nxt = next((x for x in RE_PSEUDO.finditer(h, m.end(), f) if x.group(3) == '3'), None)
    if not nxt: return None, f'fin de rubrique introuvable ({mode})'
    return (m.start(), nxt.start()), mode + '-pseudo'

def appliquer(h, n, rows):
    """Retourne (html, statut, détails) ; idempotent : un bloc existant pour DX n est régénéré à l'identique."""
    deb, fin = DEB.format(n=n), FIN.format(n=n)
    nouveau = bloc(n, rows)
    if deb in h:
        i, j = h.index(deb), h.index(fin) + len(fin)
        return h[:i] + nouveau + h[j:], 'regenere', ''
    loc, mode = localiser(h, n)
    if not loc: return h, 'non_localise', mode
    a, pos = loc
    return h[:pos] + nouveau + '\n' + h[pos:], 'injecte', mode

def main():
    ap = argparse.ArgumentParser(); ap.add_argument('--dry-run', action='store_true'); ap.add_argument('--apply', action='store_true')
    ap.add_argument('--base', default=None, help='lire les cours dans ce dossier (idempotence)'); a = ap.parse_args()
    mp = json.load(open(f'{OUT}/mapping.json')); carte = json.load(open(f'{BRIEF}/carte_lots.json'))['lecons']
    arbre = {}
    for l in git('ls-tree', '-r', 'origin/main').decode().splitlines():
        meta, p = l.split('\t', 1); arbre[p] = meta.split()[2]
    cibles = collections.defaultdict(list); nonverif = []
    for r in mp:
        for c in r['cibles']:
            if 'lot' not in c: continue
            # LOT 001–032 : numérotation du code = numérotation des cours validés ; au-delà, nom du DX vérifié exigé
            if c['lot'] > 32 and c['statut'] not in ('dx_verifie', 'dx_renumerote'):
                nonverif.append({'lot': c['lot'], 'lecon': c['lecon'], 'valeurs': [r['n']], 'statut': 'dx_non_verifie_par_le_nom',
                                 'detail': f"{r['entite']} ≠ « {c.get('nom_cours','')} »"}); continue
            cibles[(c['lot'], c['lecon'])].append(r)
    parfichier = collections.defaultdict(list); journal = list(nonverif)
    for (lot, le), rows in sorted(cibles.items()):
        k = f'{lot:03d}:{le}'; v = carte.get(k)
        base = dict(lot=lot, lecon=le, valeurs=[r['n'] for r in rows])
        if lot in EN_PRODUCTION: journal.append({**base, 'statut': 'lot_en_production'}); continue
        if not v: journal.append({**base, 'statut': 'pas_de_cours'}); continue
        if v['ref'] != 'origin/main':
            journal.append({**base, 'statut': 'reference_hors_main', 'ref': v['ref'], 'chemin': v['chemin']}); continue
        if arbre.get(v['chemin']) != v['blob']:
            journal.append({**base, 'statut': 'blob_main_different', 'chemin': v['chemin']}); continue
        if le == 'A': journal.append({**base, 'statut': 'phase_A_non_traitee', 'chemin': v['chemin']}); continue
        parfichier[v['chemin']].append((int(le[2:]), rows, base))
    conflits = []; voisins = []; modifs = {}
    for chemin, items in sorted(parfichier.items()):
        src = (open(f'{a.base}/{chemin}', encoding='utf-8').read() if a.base and os.path.exists(f'{a.base}/{chemin}')
               else git('cat-file', 'blob', arbre[chemin]).decode('utf-8'))
        h0 = src; h = src; av = len(h0.encode())
        for n, rows, base in sorted(items, key=lambda x: x[0]):
            # rubrique existante (hors bloc injecté) pour présence/conflit
            hs = re.sub(r'<!-- EPI_PROFILES:DEBUT.*?EPI_PROFILES:FIN DX\d+ -->', '', h, flags=re.S)
            loc, mode = localiser(hs, n)
            sect = txt(hs[loc[0]:loc[1]]) if loc else ''
            debuts = collections.Counter(' '.join(ph.split()[:3]) for ph in re.split(r'(?<=[.!?])\s+', sect) if len(ph.split()) > 5)
            if debuts and debuts.most_common(1)[0][1] >= 5:
                journal.append({**base, 'statut': 'cours_de_remplissage', 'chemin': chemin,
                                'detail': f'phrase-type répétée {debuts.most_common(1)[0][1]} fois : « {debuts.most_common(1)[0][0]} … »'}); continue
            garder, ignores = [], []
            for r in rows:
                kc = cles(r['valeur'])
                if loc and kc and any(kc <= nums(ph) for ph in re.split(r'(?<=[.;!?])\s+', sect)):
                    ignores.append((r['n'], 'deja_present')); continue
                g0 = present_genre(sect, genre(r['valeur']))
                g = [x for x in g0 if comparable(r, x)]
                if g0 and not g:
                    voisins.append(dict(chemin=chemin, lot=base['lot'], dx=n, n=r['n'], entite=r['entite'], valeur=r['valeur'],
                                        population=r['population'], source=r['source'], existant=[x.strip()[:220] for x in g0[:2]]))
                if loc and g:
                    conflits.append(dict(chemin=chemin, lot=base['lot'], dx=n, n=r['n'], entite=r['entite'], valeur=r['valeur'],
                                         population=r['population'], source=r['source'], existant=[x.strip()[:220] for x in g[:3]]))
                    ignores.append((r['n'], 'conflit_probable')); continue
                garder.append(r)
            if not garder:
                journal.append({**base, 'statut': 'rien_a_injecter', 'chemin': chemin, 'ignores': ignores}); continue
            h2, st, det = appliquer(h, n, garder)
            journal.append({**base, 'statut': st, 'detail': det, 'chemin': chemin, 'injectees': [r['n'] for r in garder],
                            'ignores': ignores})
            h = h2
        ap_ = len(h.encode()); e0, e1 = equilibre(h0), equilibre(h)
        ok = True; motif = ''
        if h != h0:
            if ap_ >= MAX: ok, motif = False, f'taille {ap_} ≥ {MAX}'
            elif e1 != e0 and e1: ok, motif = False, f'balises : {e1}'
        for j in journal:
            if j.get('chemin') == chemin and j['statut'] in ('injecte', 'regenere'):
                j.update(octets_avant=av, octets_apres=ap_, bande=('basse' if ap_ < MIN else 'ok'))
                if not ok: j['statut'], j['detail'] = 'refuse', motif
        if ok and h != h0: modifs[chemin] = h
        elif ok and a.base and os.path.exists(f'{a.base}/{chemin}'): modifs[chemin] = h
    if a.apply:
        for chemin, h in modifs.items():
            p = f'{OUT}/stage/{chemin}'; os.makedirs(os.path.dirname(p), exist_ok=True)
            open(p, 'w', encoding='utf-8').write(h)
    json.dump(journal, open(f'{OUT}/inject_journal.json', 'w'), ensure_ascii=False, indent=1)
    rapport(journal, conflits, modifs, a, voisins)

def rapport(journal, conflits, modifs, a, voisins):
    c = collections.Counter(j['statut'] for j in journal)
    L = [f'# {"Dry-run" if not a.apply else "Injection"} : épidémiologie PROFILES 2023', '',
         f'Cibles (LOT, leçon) : {len(journal)} ; statuts : {dict(c)}.',
         f'Fichiers modifiés : {len(modifs)} ; LOTs : {len({j["lot"] for j in journal if j["statut"] in ("injecte","regenere")})}.', '',
         '| LOT | DX | Statut | Valeurs | Octets avant → après | Détail |', '|---|---|---|---|---|---|']
    for j in journal:
        L.append(f"| {j['lot']:03d} | {j['lecon']} | {j['statut']} | {','.join(map(str, j.get('injectees', j['valeurs'])))} | "
                 f"{j.get('octets_avant','')}→{j.get('octets_apres','')} | {j.get('detail') or j.get('ref','')} {j.get('ignores','') or ''} |")
    open(f'{OUT}/{"DRYRUN" if not a.apply else "INJECTION"}.md', 'w').write('\n'.join(L) + '\n')
    C = ['# Conflits probables (aucune valeur remplacée, aucune injection)', '',
         'Le cours contient déjà un chiffre du même genre (%, taux pour 100 000 ou effectif) différent de la valeur du référentiel. Un humain arbitre.', '']
    for x in conflits:
        C += [f"## LOT {x['lot']:03d} · DX.{x['dx']} · #{x['n']} {x['entite']}",
              f"- Référentiel : **{x['valeur']}** ; {x['population']} ; {x['source']}.", f"- Fichier : `{x['chemin']}`."]
        C += [f"- Existant : « {e} »" for e in x['existant']] + ['']
    C += ['# Voisinages (valeur injectée à côté d\'un chiffre du même genre, population ou unité différente)', '',
          'Ces valeurs complètent le cours ; un humain vérifie qu\'elles ne se contredisent pas.', '']
    for x in voisins:
        C += [f"- LOT {x['lot']:03d} · DX.{x['dx']} · #{x['n']} {x['entite']} : **{x['valeur']}** ({x['population']} ; {x['source']}). Existant : « {x['existant'][0]} »"]
    open(f'{OUT}/CONFLITS.md', 'w').write('\n'.join(C) + '\n')
    print(dict(c), 'fichiers', len(modifs), 'conflits', len(conflits))

if __name__ == '__main__':
    main()
