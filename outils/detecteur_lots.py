#!/usr/bin/env python3
"""DETECTEUR_LOTS — trouve, pour chacune des 248 × 11 leçons, la version la plus avancée qui existe
dans tout le dépôt (main + TOUTES les branches), l'attribue à une IA et liste tout ce qui est périmé. Zéro modèle.

Leçon : Phase A (LOT_XXX_Phase_A_V*.html, Appel_A…Plan_et_Liste) ou DX.i (LOT_XXX_Phase_B_V*_DX.i.html, Appel_B_V*_DX.i).
Ancien format multi-DX (« Partie_n_DX.a_a_DX.b ») : couverture partielle, score plafonné, jamais préféré.
Score (0–100) : existe 40 · 14 points 20 · bande 100–200 Ko 20 · aucun défaut bloquant 10 · verdict vert 10.
Choix : score le plus élevé, puis le plus récent (date du commit de la branche), puis main.
Propriétaire (dossier cible) : lu dans ATTRIBUTIONS.json (ordre de Vial du 10.11.2026), jamais l'auteur ni le dossier.
La signature d'auteur (dossier, branche, auteur) reste notée à titre informatif dans le champ « auteur_ia ».

Usage : python3 detecteur_lots.py <depot> [--rafraichir] [--sortie carte_lots.json]
Sortie : carte_lots.json = {lecons:{"018:DX3":{ia,ref,chemin,blob,score,date,...}}, obsoletes_main:[…], branches_supplantees:[…]}
"""
import os, re, sys, json, time, argparse, subprocess, collections, tempfile
from concurrent.futures import ProcessPoolExecutor

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import controle3
from attributions import proprietaire

IAS = ('Claude', 'ChatGPT_Codex', 'Grokbot')
RE_LOT = re.compile(r'LOT[_\- ]?0*(\d{1,3})(?!\d)', re.I)
RE_A = re.compile(r'(?:Phase_A_V\d+|Appel_A_V?\d*_?(?:Ultra_Pedagogique_)?Plan_et_Liste)(?:__export_GoogleDoc)?\.html$', re.I)
RE_DX = re.compile(r'(?:Phase_B_V\d+|Appel_B_V\d+)_DX\.(\d{1,2})\.html$', re.I)
RE_PARTIE = re.compile(r'DX?\.?(\d{1,2})_a_DX?\.?(\d{1,2})', re.I)
EXCLUS = re.compile(r'(^|/)(audit|audits|AUDIT|qa|_OBSOLETES|orig|prototypes_format|essai_[^/]*|tests)(/|$)|\.rapport\.html$|_OBSOLETE|/p\d+\.html$', re.I)
BLOQUANTS = ('C_points_manquants', 'C_FIN_FICHIER_absent', 'C_balises', 'B_phrase_partagee_entre_fichiers')
SIGNES = [  # (motif sur chemin+branche+auteur, IA) — ordre = priorité
    (r'(^|/)(Claude|LOT_Claude_Finaux|claude)(/|$)', 'Claude'),
    (r'(^|/)(Grokbot|grok-LOTS-html|LOT_Tunder|LOT_Bitunder|Leona[^/]*|[^/]*[Tt]under[^/]*)(/|$)', 'Grokbot'),
    (r'(^|/)(ChatGPT_Codex|codex-LOTS-html|[^/]*[Cc]odex[^/]*|[^/]*GPT[^/]*)(/|$)', 'ChatGPT_Codex'),
    (r'^origin/(claude|corr2/.*opus)', 'Claude'),
    (r'^origin/(grok|tunder|bitunder|leona|alpha)/', 'Grokbot'),
    (r'^origin/(codex|gpt|chatgpt)', 'ChatGPT_Codex'),
    (r'(?i)\bclaude\b|anthropic', 'Claude'),
    (r'(?i)grok|tunder|leona', 'Grokbot'),
    (r'(?i)codex|chatgpt|gpt|openai|cursor', 'ChatGPT_Codex'),
]


def git(d, *a, t=1800, binaire=False):
    p = subprocess.run(['git', '-C', d, *a], capture_output=True, timeout=t)
    return p.stdout if binaire else p.stdout.decode('utf-8', 'ignore')


def rafraichir(d):
    git(d, 'fetch', '-q', '--depth=1', '--filter=tree:0', 'origin', '+refs/heads/*:refs/remotes/origin/*')
    refs = [r for r in git(d, 'for-each-ref', '--format=%(refname:short)', 'refs/remotes').split() if r.startswith('origin/') and r != 'origin/HEAD']
    specs = [f'+refs/heads/{r[7:]}:refs/remotes/{r}' for r in refs]
    for i in range(0, len(specs), 30):
        git(d, 'fetch', '-q', '--depth=1', 'origin', *specs[i:i + 30])


def auteur_ia(chemin, ref, auteur):
    """Signature de l'auteur (information seulement) : ne décide jamais du propriétaire."""
    for motif, ia in SIGNES:
        cible = chemin if motif.startswith('(^|/)') else (ref if motif.startswith('^origin') else f'{ref} {auteur}')
        if re.search(motif, cible):
            return ia, False
    return 'inconnu', True


def attribuer(chemin, ref, auteur):
    """Propriétaire exclusif du LOT de ce chemin, selon ATTRIBUTIONS.json ; None si aucun LOT reconnu."""
    L = lecons_du_chemin(chemin)
    return (proprietaire(L[0]), False) if L else (None, True)


def lecons_du_chemin(f):
    if not f.endswith('.html') or EXCLUS.search(f):
        return None
    m = RE_LOT.search(f.split('/')[-1]) or RE_LOT.search(f)
    if not m or not 1 <= int(m.group(1)) <= 248:
        return None
    lot, nom = int(m.group(1)), f.split('/')[-1]
    if RE_A.search(nom):
        return lot, ['A'], False
    dx = RE_DX.search(nom)
    if dx and 1 <= int(dx.group(1)) <= 10:
        return lot, [f'DX{int(dx.group(1))}'], False
    p = RE_PARTIE.search(nom)
    if p and 'Appel_B' in nom or (p and 'Partie' in nom):
        a, b = sorted((int(p.group(1)), int(p.group(2))))
        return lot, [f'DX{i}' for i in range(max(a, 1), min(b, 10) + 1)], True
    return None


def mesurer(blob_et_depot):
    blob, d = blob_et_depot
    brut = git(d, 'cat-file', 'blob', blob, binaire=True)
    with tempfile.NamedTemporaryFile(suffix='.html', delete=False) as fh:
        fh.write(brut)
        tmp = fh.name

    class A:
        points, min, max, ex, script_ok = 14, 100_000, 200_000, 1, False
    try:
        r = controle3.controler(tmp, {}, A, {})
    finally:
        os.unlink(tmp)
    defs = set(r['defauts'])
    s = 40 + (0 if 'C_points_manquants' in defs else 20) + (0 if 'C_taille_hors_bande' in defs else 20)
    bloq = bool(defs & set(BLOQUANTS))
    s += (0 if bloq else 10) + (10 if not defs else 0)
    return blob, {'score': s, 'bloquant': bloq, 'octets': len(brut), 'connect': r['connecteur%'], 'defauts': sorted(defs)}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('depot')
    ap.add_argument('--rafraichir', action='store_true')
    ap.add_argument('--sortie', default='carte_lots.json')
    a = ap.parse_args()
    d = os.path.abspath(a.depot)
    if a.rafraichir:
        rafraichir(d)
    refs = []
    for l in git(d, 'for-each-ref', '--format=%(committerdate:unix)|%(refname:short)|%(authorname) %(authoremail)', 'refs/remotes').splitlines():
        ts, ref, aut = l.split('|', 2)
        if ref not in ('origin/HEAD', 'origin'):
            refs.append((int(ts), ref, aut))
    occur = []  # (lot, lecons, ancien, ref, chemin, blob, date, ia, defaut)
    for ts, ref, aut in refs:
        for ligne in git(d, 'ls-tree', '-r', ref).splitlines():
            meta, chemin = ligne.split('\t', 1)
            _, typ, blob = meta.split()
            if typ != 'blob':
                continue
            L = lecons_du_chemin(chemin)
            if L:
                ia = proprietaire(L[0])
                occur.append((L[0], L[1], L[2], ref, chemin, blob, ts, ia, auteur_ia(chemin, ref, aut)[0]))
    blobs = sorted({o[5] for o in occur if not o[2]})
    with ProcessPoolExecutor() as ex:
        mesures = dict(ex.map(mesurer, [(b, d) for b in blobs], chunksize=16))
    best = {}
    for lot, lecs, ancien, ref, chemin, blob, ts, ia, auteur in occur:
        m = mesures.get(blob) or {'score': 30, 'bloquant': False, 'octets': 0, 'connect': None, 'defauts': ['ancien_format_multi_DX']}
        if ancien:
            m = dict(m, score=min(m['score'], 30))
        for lec in lecs:
            cand = {'ia': ia, 'auteur_ia': auteur, 'ref': ref, 'chemin': chemin, 'blob': blob, 'date': ts,
                    'main': ref == 'origin/main', 'ancien_format': ancien, **m}
            k = f'{lot:03d}:{lec}'
            if k not in best:
                best[k] = cand
            elif cand['blob'] == best[k]['blob']:  # contenu identique : la copie de main prime
                if cand['main'] and not best[k]['main']:
                    best[k] = cand
            elif (cand['score'], cand['date']) > (best[k]['score'], best[k]['date']):
                best[k] = cand
    # Destination unique de chaque leçon : <IA>/LOT_XXX/LOT_XXX_Phase_A_V0.html | LOT_XXX_Phase_B_V0_DX.i.html
    for k, v in best.items():
        lot, lec = int(k[:3]), k[4:]
        nom = f'LOT_{lot:03d}_Phase_A_V0.html' if lec == 'A' else f'LOT_{lot:03d}_Phase_B_V0_DX.{lec[2:]}.html'
        v['destination'] = f"{v['ia']}/LOT_{lot:03d}/{nom}"
    dest = {v['destination'] for v in best.values()}
    retenus = {v['blob'] for v in best.values()}
    # Périmés sur main : toute copie de leçon (format actuel ou ancien) qui n'est pas à sa destination unique
    obs_main = sorted({o[4] for o in occur if o[3] == 'origin/main' and o[4] not in dest})
    # Branches supplantées : aucune de leurs leçons n'est la version retenue
    par_ref = collections.defaultdict(set)
    for o in occur:
        par_ref[o[3]].add(o[5])
    branches = sorted(r for r, bs in par_ref.items() if r != 'origin/main' and not (bs & retenus))
    carte = {'genere': time.strftime('%Y-%m-%dT%H:%M:%S%z'), 'branches_scannees': len(refs), 'occurrences': len(occur),
             'versions_uniques_mesurees': len(blobs), 'lecons': dict(sorted(best.items())),
             'obsoletes_main': obs_main, 'branches_supplantees': branches}
    json.dump(carte, open(a.sortie, 'w'), ensure_ascii=False, indent=0)
    par_ia = collections.Counter(v['ia'] for v in best.values())
    print(f"{a.sortie} : {len(refs)} branches, {len(occur)} occurrences, {len(blobs)} versions uniques, "
          f"{len(best)} leçons trouvées / 2728, {len(obs_main)} copies périmées sur main, {len(branches)} branches supplantées, {dict(par_ia)}")


if __name__ == '__main__':
    main()
