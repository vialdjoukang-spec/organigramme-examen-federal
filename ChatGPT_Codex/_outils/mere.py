#!/usr/bin/env python3
"""MÈRE — lève la légion : 1 fetch groupé, puis N soldats (processus clones de soldat.py) en vagues parallèles.
Zéro modèle. Sortie : rapports/*.json (1 par soldat) + DIGEST.md (seul fichier lu par le modèle).

Usage : python3 mere.py <depot> [--jours 10] [--soldats 16]
"""
import sys, os, json, subprocess, argparse, re, time
from concurrent.futures import ThreadPoolExecutor

ICI = os.path.dirname(os.path.abspath(__file__))


def git(depot, *a, t=900):
    return subprocess.run(['git', '-C', depot, *a], capture_output=True, text=True, errors='ignore', timeout=t).stdout


def soldat(args):
    p = subprocess.run([sys.executable, os.path.join(ICI, 'soldat.py'), *args], capture_output=True, text=True, timeout=300)
    try:
        return json.loads(p.stdout)
    except Exception:
        return {'erreur': ' '.join(args)[-120:], 'stderr': p.stderr[-200:]}


def vague(nom, missions, n, out):
    t = time.time()
    with ThreadPoolExecutor(n) as ex:
        res = list(ex.map(soldat, missions))
    with open(os.path.join(out, f'{nom}.json'), 'w') as fh:
        json.dump(res, fh, ensure_ascii=False, indent=0)
    print(f'vague {nom}: {len(missions)} soldats, {time.time()-t:.0f}s', file=sys.stderr)
    return res


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('depot')
    ap.add_argument('--jours', type=int, default=10)
    ap.add_argument('--soldats', type=int, default=16)
    a = ap.parse_args()
    D = os.path.abspath(a.depot)
    nom = os.path.basename(D)
    out = os.path.join(ICI, 'rapports', nom)
    os.makedirs(out, exist_ok=True)

    # Vague 0 — branches récentes, un seul fetch groupé (profondeur 1)
    refs = git(D, 'for-each-ref', '--sort=-committerdate', '--format=%(committerdate:unix) %(refname:short)', 'refs/remotes').split('\n')
    seuil = time.time() - a.jours * 86400
    actives = [r.split()[1] for r in refs if r and int(r.split()[0]) >= seuil and r.split()[1] not in ('origin', 'origin/HEAD')]
    specs = [f'+refs/heads/{b[7:]}:refs/remotes/{b}' for b in actives]
    for i in range(0, len(specs), 40):
        git(D, 'fetch', '-q', '--depth=1', 'origin', *specs[i:i + 40])

    # Vague 1 — un soldat par branche
    B = vague('1_branches', [['branche', D, b] for b in actives], a.soldats, out)

    # Vague 2 — un soldat par LOT (version la plus récente), par prompt, par fichier de liens
    lot_ref = {}
    for r in B:  # B est trié du plus récent au plus ancien
        for L in r.get('lots', []):
            lot_ref.setdefault(L, r['ref'])
    tree = git(D, 'ls-tree', '-r', '--name-only', 'origin/main').splitlines()
    chemins_main = {}
    for f in tree:
        m = re.search(r'^(.*LOT_(\d{3}))/', f)
        if m and not f.startswith(('audit', 'qa')):
            chemins_main.setdefault(int(m.group(2)), m.group(1))
    missions_lot = []
    for L, ref in lot_ref.items():
        cands = [f for f in git(D, 'ls-tree', '-r', '--name-only', ref).splitlines() if f'LOT_{L:03d}/' in f and f.endswith('.html')]
        if cands:
            missions_lot.append(['lot', D, ref, cands[0].rsplit('/', 1)[0]])
    for L, ch in chemins_main.items():
        if L not in lot_ref:
            missions_lot.append(['lot', D, 'origin/main', ch])
    LOTS = vague('2_lots', missions_lot, a.soldats, out)

    prompts = set()
    for r in B:
        for f in r.get('prompts', []):
            prompts.add((r['ref'], f))
    for f in tree:
        if re.search(r'(PROMPT|HARNAIS|SKILL|AGENTS|CLAUDE|LIRE|SPEC|REPRISE|TRANSITION)[^/]*\.md$', f, re.I) and not f.startswith(('audit', 'livraisons', 'qa')):
            prompts.add(('origin/main', f))
    P = vague('3_prompts', [['prompt', D, r, f] for r, f in sorted(prompts)], a.soldats, out)

    liens = [f for f in tree if re.search(r'(lien|link|source|ressource|refer|imag|biblio)[^/]*\.(md|txt|json)$', f, re.I)
             and not f.startswith(('audit', 'qa', 'livraisons', 'nosology'))][:120]
    LI = vague('4_liens', [['liens', D, 'origin/main', f] for f in liens], a.soldats, out)

    # Digest ultra-concis
    o = [f'# DIGEST {nom} — {len(actives)} branches actives ({a.jours} j), {len(missions_lot)} LOT/chap., {len(P)} prompts, {len(LI)} fichiers liens']
    o.append('## Branches (date sujet | LOTs | prompts/outils neufs)')
    for r in B[:30]:
        o.append(f"- {r.get('sujet','')[:90]} | {r.get('lots')} | {r.get('prompts')} {r.get('outils', [])[:4]}")
    o.append('## LOTs (n | dx | figs | img | src | verbe% | connect% | outils)')
    for r in sorted(LOTS, key=lambda x: x.get('lot', '')):
        if 'lot' in r:
            o.append(f"- {r['lot'].split('/')[-1]}@{r['ref'].split('/')[-1][:22]} | {r['dx']} | {r['figs']} | {r['img']} | {r['src']} | {r['verbe%']} | {r['connect%']} | {r['outils'][:5]}")
    gab = {}
    for r in LOTS:
        for t in r.get('titres', []):
            gab[t] = gab.get(t, 0) + 1
    o.append('## Gabarit dominant (titre ×LOTs)')
    o.append('; '.join(f'{t}×{n}' for t, n in sorted(gab.items(), key=lambda x: -x[1])[:30]))
    o.append('## Prompts (Ko | BLOQUANT | interdit | lignes dupliquées) — plan')
    for r in sorted(P, key=lambda x: -x.get('Ko', 0))[:25]:
        if 'f' in r:
            o.append(f"- {r['f']}@{r['ref'].split('/')[-1][:20]} ({r['Ko']}|{r['bloquant']}|{r['interdit']}|{r['doublons_lignes']}) :: " + ' | '.join(r['plan'][:18]))
    o.append('## Liens (urls/suisses/imagerie)')
    for r in sorted(LI, key=lambda x: -(x.get('swiss', 0) + x.get('img', 0)))[:20]:
        if 'f' in r and r['urls']:
            o.append(f"- {r['f']} {r['urls']}/{r['swiss']}/{r['img']} {list(r['dom'])[:6]}")
    err = [r for r in B + LOTS + P + LI if 'erreur' in r]
    o.append(f'## Erreurs soldats : {len(err)}')
    with open(os.path.join(out, 'DIGEST.md'), 'w') as fh:
        fh.write('\n'.join(o))
    print(os.path.join(out, 'DIGEST.md'))


if __name__ == '__main__':
    main()
