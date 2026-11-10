#!/usr/bin/env python3
"""SOLDAT — un clone, une mission, zéro modèle. Lit un dépôt git SANS checkout (git show), écrit ≤ 3 Ko JSON.

Missions :
  branche  <depot> <ref>            : fichiers ajoutés/modifiés vs main (hors gros HTML), prompts/outils neufs, LOTs touchés
  lot      <depot> <ref> <chemin>   : structure + qualité d'un LOT (titres, images, sources, % verbe, % connecteur)
  prompt   <depot> <ref> <fichier>  : plan Macro→Micro (titres), taille, règles BLOQUANT/INTERDIT comptées
  liens    <depot> <ref> <fichier>  : domaines, suisses, imagerie
"""
import sys, re, json, subprocess, html, collections, os

sys.path.insert(0, os.path.dirname(__file__))
from legion import qualite, html_text, HEAD_RE, MD_HEAD, URL_RE, SWISS, IMG_DOM  # réutilise les règles


def git(depot, *a):
    return subprocess.run(['git', '-C', depot, *a], capture_output=True, text=True, errors='ignore', timeout=120).stdout


def m_branche(depot, ref):
    base = git(depot, 'merge-base', 'origin/main', ref).strip() or 'origin/main'
    lignes = git(depot, 'diff', '--name-status', '--no-renames', 'origin/main', ref).splitlines()
    fichiers = [l.split('\t', 1) for l in lignes if '\t' in l and not l.startswith('D')]  # suppressions exclues
    lots = sorted({int(m) for _, f in fichiers for m in re.findall(r'LOT_(\d{3})', f)})
    neufs = [f for s, f in fichiers if not re.search(r'LOT_\d{3}/.*\.html$|^audit/|\.(png|jpe?g|webp|pdf)$', f)]
    return {'ref': ref, 'n': len(fichiers), 'lots': lots,
            'hors_lot': neufs[:25], 'prompts': [f for f in neufs if re.search(r'PROMPT|HARNAIS|SKILL|AGENTS|CLAUDE|LIRE', f, re.I)][:10],
            'outils': [f for f in neufs if f.endswith('.py')][:15],
            'sujet': git(depot, 'log', '-1', '--format=%cs %s', ref).strip()[:120]}


def m_lot(depot, ref, chemin):
    noms = git(depot, 'ls-tree', '-r', '--name-only', ref, '--', chemin).splitlines()
    dx = [n for n in noms if re.search(r'DX\.\d+\.html$', n)]
    figs = [n for n in noms if re.search(r'\.(png|jpe?g|webp|svg)$', n)]
    q, h, img, src = [], collections.Counter(), 0, 0
    for n in [x for x in noms if x.endswith('.html')][:12]:
        s = git(depot, 'show', f'{ref}:{n}')
        img += len(re.findall(r'<img\b|<svg\b', s, re.I))
        src += len(re.findall(r'href=["\']https?://', s))
        h.update(re.sub(r'\d+', '#', html_text(t))[:50] for l, t in HEAD_RE.findall(s) if l in '23')
        q.append(qualite(html_text(s)))
    q = [x for x in q if x.get('n')]
    moy = lambda k: round(sum(x[k] for x in q) / len(q)) if q else None
    return {'ref': ref, 'lot': chemin, 'dx': len(dx), 'figs': len(figs), 'img': img, 'src': src,
            'verbe%': moy('verbe%'), 'connect%': moy('connect%'), 'titres': [t for t, _ in h.most_common(16)],
            'annexes': [n.split('/')[-1] for n in noms if n.endswith('.md')][:8],
            'outils': [n.split('/')[-1] for n in noms if n.endswith('.py')][:12]}


def m_prompt(depot, ref, f):
    s = git(depot, 'show', f'{ref}:{f}')
    return {'ref': ref, 'f': f, 'Ko': round(len(s.encode()) / 1024, 1),
            'plan': [('#' * len(a)) + ' ' + b[:80] for a, b in MD_HEAD.findall(s)][:60],
            'bloquant': len(re.findall(r'BLOQUAN', s)), 'interdit': len(re.findall(r'(?i)interdit', s)),
            'doublons_lignes': sum(n - 1 for n in collections.Counter(l.strip() for l in s.splitlines() if len(l.strip()) > 40).values() if n > 1)}


def m_liens(depot, ref, f):
    s = git(depot, 'show', f'{ref}:{f}')
    u = URL_RE.findall(s)
    d = collections.Counter(re.sub(r'^https?://(www\.)?', '', x).split('/')[0].lower() for x in u)
    return {'ref': ref, 'f': f, 'urls': len(u), 'swiss': sum(n for k, n in d.items() if any(z in k for z in SWISS)),
            'img': sum(n for k, n in d.items() if any(z in k for z in IMG_DOM)), 'dom': dict(d.most_common(12))}


if __name__ == '__main__':
    mission, *args = sys.argv[1:]
    r = {'branche': m_branche, 'lot': m_lot, 'prompt': m_prompt, 'liens': m_liens}[mission](*args)
    print(json.dumps(r, ensure_ascii=False, separators=(',', ':')))
