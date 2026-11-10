#!/usr/bin/env python3
"""CONSOLIDER — exécute, pour UNE IA, la carte produite par detecteur_lots.py : chaque leçon qui lui est attribuée
est écrite à sa destination unique <IA>/LOT_XXX/… (avec ses images et annexes relatives), puis toutes les copies
périmées de son ressort sont supprimées de l'arbre de travail. Zéro modèle. Aucun conflit possible entre IA :
le ressort d'une IA = les LOTs dont ATTRIBUTIONS.json la déclare propriétaire (ordre de Vial du 10.11.2026), où
que se trouvent leurs copies ; chaque leçon va dans le dossier de son propriétaire, jamais de son auteur.

Usage (depuis la racine du dépôt, sur une branche créée depuis main) :
  python3 outils/consolider.py --carte carte.json --ia Grokbot [--lots 100-120] [--max 60] [--appliquer]
Sans --appliquer : simulation (liste ce qui serait écrit et supprimé). Avec --appliquer : écrit, `git rm`, prêt à committer.
--max limite le nombre de leçons par passage (PR légères, poussées sans erreur 413).
"""
import os, re, sys, json, argparse, subprocess, posixpath

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from detecteur_lots import attribuer, lecons_du_chemin

RELATIF = re.compile(r'''(?:src|href)=["'](?!https?:|data:|#|mailto:|/)([^"'#?]+)''', re.I)


def git(*a, binaire=False):
    p = subprocess.run(['git', *a], capture_output=True)
    if p.returncode and not binaire:
        raise RuntimeError(p.stderr.decode()[:300])
    return p.stdout if binaire else p.stdout.decode('utf-8', 'ignore')


def plage(s):
    if not s:
        return range(1, 249)
    a, _, b = s.partition('-')
    a, b = int(a), int(b or a)
    return range(min(a, b), max(a, b) + 1)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--carte', required=True)
    ap.add_argument('--ia', required=True, choices=['Claude', 'ChatGPT_Codex', 'Grokbot'])
    ap.add_argument('--lots')
    ap.add_argument('--max', type=int, default=60)
    ap.add_argument('--appliquer', action='store_true')
    a = ap.parse_args()
    C = json.load(open(a.carte))
    lots = set(plage(a.lots))
    faites, ecrits, assets = 0, [], []
    for k, v in C['lecons'].items():
        lot = int(k[:3])
        if v['ia'] != a.ia or lot not in lots or v['main'] and v['chemin'] == v['destination']:
            continue
        if v['chemin'] == v['destination']:
            continue
        if faites >= a.max:
            break
        faites += 1
        ecrits.append((v['blob'], v['destination']))
        contenu = git('cat-file', 'blob', v['blob'], binaire=True).decode('utf-8', 'ignore')
        base = posixpath.dirname(v['chemin'])
        for rel in set(RELATIF.findall(contenu)):
            src = posixpath.normpath(posixpath.join(base, rel))
            if src.startswith('..') or not rel.strip():
                continue
            assets.append((v['ref'], src, posixpath.normpath(posixpath.join(posixpath.dirname(v['destination']), rel))))
    # Copies périmées de son ressort : chemins de main attribués à cette IA, hors destinations
    dest = {v['destination'] for v in C['lecons'].values()}
    ressort = []
    for p in C['obsoletes_main']:
        L = lecons_du_chemin(p)
        if L and L[0] in lots and attribuer(p, 'origin/main', '')[0] == a.ia and p not in dest:
            ressort.append(p)
    print(f'{a.ia} : {len(ecrits)} leçons à écrire, {len(assets)} annexes relatives, {len(ressort)} copies périmées à supprimer')
    if not a.appliquer:
        for b, d in ecrits[:10]:
            print('  écrire', d)
        for p in ressort[:10]:
            print('  supprimer', p)
        return
    for blob, d in ecrits:
        os.makedirs(os.path.dirname(d), exist_ok=True)
        open(d, 'wb').write(git('cat-file', 'blob', blob, binaire=True))
    for ref, src, d in assets:
        brut = subprocess.run(['git', 'show', f'{ref}:{src}'], capture_output=True).stdout
        if brut and not os.path.exists(d):
            os.makedirs(os.path.dirname(d) or '.', exist_ok=True)
            open(d, 'wb').write(brut)
    for p in ressort:
        if os.path.exists(p):
            git('rm', '-q', '--', p)
    git('add', '--', a.ia)
    print('appliqué : vérifier `git status`, puis committer, pousser et ouvrir la PR')


if __name__ == '__main__':
    main()
