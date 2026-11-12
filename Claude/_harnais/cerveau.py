#!/usr/bin/env python3
"""CERVEAU — second cerveau local (zéro modèle) : une question → les 8 passages les plus pertinents, avec leur chemin.
Remplace « relire pour retrouver » par une recherche BM25 (principe Chonkie + FlagEmbedding du Bracelet, sans
dépendance) sur : MEMOIRE*.md, carnets memoire/*.md, CONSIGNES_VIAL.md, HELP.md, CORRECTIONS_AUDIT.md,
LISTE_DX_CANONIQUE.md, rapports d'audit, textes de sources en cache (~/.cache/medina_sources).

  cherche "<question>" [--racine /home/user/wt/r-024] [--n 8]   → passages ≤ 400 car. + chemin
  index [--racine …]                                            → reconstruit l'index (la veille le fait toutes les 10 min)
"""
import re, os, sys, glob, json, math, pickle, collections, unicodedata

IDX = os.path.expanduser('~/.cache/medina_cerveau.pkl')
MOTIFS = ['Claude/MEMOIRE*.md', 'Claude/CONSIGNES_VIAL.md', 'Claude/LOT_0*/MEMOIRE.md', 'Claude/LOT_0*/memoire/*.md',
          'Claude/LOT_0*/HELP.md', 'Claude/LOT_0*/CORRECTIONS_AUDIT.md', 'Claude/LOT_0*/LISTE_DX_CANONIQUE.md',
          'Claude/LOT_0*/audits/*.md', 'Claude/LOT_0*/audits/*.json', 'Claude/_harnais/*.md']
VIDE = set('le la les de des du un une et ou en à au aux pour par sur dans avec que qui est sont ne pas se sa son ses ce'
           ' cette il elle on the of and to in is'.split())


def mots(t):
    t = unicodedata.normalize('NFKD', t.lower()); t = ''.join(c for c in t if not unicodedata.combining(c))
    return [w for w in re.findall(r'[a-z0-9]{2,}', t) if w not in VIDE]


def morceaux(chemin, t, taille=700):
    p = re.split(r'\n\s*\n|(?<=\.)\s+(?=[A-ZÉ])', t); buf = ''
    for x in p:
        if len(buf) + len(x) > taille and buf: yield chemin, buf.strip(); buf = ''
        buf += x + ' '
    if buf.strip(): yield chemin, buf.strip()


def construire(racines):
    docs = []; vus = set()
    for r in sorted(racines, reverse=True):  # le worktree le plus récent prime ; un chemin relatif n'est indexé qu'une fois
        for m in MOTIFS:
            for f in glob.glob(os.path.join(r, m)):
                if os.path.relpath(f, r) in vus: continue
                vus.add(os.path.relpath(f, r))
                docs += morceaux(os.path.relpath(f, r) + f' @{os.path.basename(r)}', open(f, encoding='utf-8', errors='ignore').read())
    for f in glob.glob(os.path.expanduser('~/.cache/medina_sources/*.txt')):
        docs += morceaux('source:' + os.path.basename(f), open(f, encoding='utf-8', errors='ignore').read()[:400000], 900)
    tf = [collections.Counter(mots(t)) for _, t in docs]; df = collections.Counter()
    for c in tf: df.update(c.keys())
    pickle.dump(dict(docs=docs, tf=tf, df=df, lm=sum(sum(c.values()) for c in tf) / max(1, len(tf))), open(IDX, 'wb'))
    return len(docs)


def cherche(q, n=8):
    I = pickle.load(open(IDX, 'rb')); N = len(I['docs']); sc = []
    for i, c in enumerate(I['tf']):
        L = sum(c.values()) or 1; s = 0
        for w in set(mots(q)):
            if w in c:
                idf = math.log(1 + (N - I['df'][w] + .5) / (I['df'][w] + .5))
                s += idf * c[w] * 2.2 / (c[w] + 1.2 * (.25 + .75 * L / I['lm']))
        if s: sc.append((s, i))
    for s, i in sorted(sc, reverse=True)[:n]:
        ch, t = I['docs'][i]; print(f'[{s:.1f}] {ch}\n    {t[:400]}')


if __name__ == '__main__':
    a = sys.argv[1:] or ['-h']
    rac = [a[a.index('--racine') + 1]] if '--racine' in a else sorted(glob.glob('/home/user/wt/r-0*')) or ['.']
    if a[0] == 'index': print(construire(rac), 'passages indexés')
    elif a[0] == 'cherche':
        if not os.path.exists(IDX): construire(rac)
        cherche(a[1], int(a[a.index('--n') + 1]) if '--n' in a else 8)
    else: print(__doc__)
