#!/usr/bin/env python3
"""CONTROLE_MEDINA — contrat d'un chapitre MEDINA vérifié sans modèle (complète controle3.py).

Contrôles : classes de la liste fermée ; chaque data-k a son <template data-pop> ; nouvelles clés préfixées ;
Pareto data-cover → ids d'îlots existants ; ouverture <template id="ch-CODE"> et fermeture </div></template> ;
quatre panneaux pA/pE/pS/pP ; quiz ≥ 3 dans pE ; abréviations (MAJUSCULES ≥ 2 lettres) absentes du glossaire ;
figures : attribution + licence ; SVG anatomique sans source = MAJEUR ; métaphores signalées par lexique.

Usage : python3 controle_medina.py chapters/I50 --glossaire glossary [--reutilisables np,echo,irm]
"""
import os, re, sys, json, glob, argparse, importlib.util

CLASSES = set('ilot toc chap-body sci-body sci sci-bar key trap k alert two card t pareto-btn src pager prev next quiz fb '
              'status chap-head code n ui w ratio chap lab panel tabs'.split())
METAPHORES = re.compile(r"\b(tel(?:le)?s? (?:un|une) |comme (?:un|une) (?:chef|moteur|barrage|tsunami|bombe|cascade de dominos)|"
                        r"véritable|chef d'orchestre|clé de voûte|pierre angulaire|talon d'Achille|bombe à retardement)", re.I)
ANATOMIE = re.compile(r'(ventricule|oreillette|artère|veine|nerf|muscle|os |vertèbre|rein|néphron|foie|poumon|bronche|cerveau|cortex)', re.I)


def glossaire(d):
    """Lecture textuelle (sans exécuter les modules : rapide et sûr)."""
    G = set()
    for f in glob.glob(os.path.join(d or '', '*.py')):
        G |= set(re.findall(r"""\ba\(\s*['"]([^'"]+)['"]""", open(f, errors='ignore').read()))
    return G


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('dossier')
    ap.add_argument('--glossaire')
    ap.add_argument('--reutilisables', default='')
    a = ap.parse_args()
    code = os.path.basename(os.path.normpath(a.dossier))
    pre = code.lower()
    fichiers = sorted(glob.glob(os.path.join(a.dossier, f'{code}_*.html')))
    corps = ''.join(open(f, errors='ignore').read() for f in fichiers if '_pop' not in f)
    pops = ''.join(open(f, errors='ignore').read() for f in fichiers if '_pop' in f)
    tout = corps + pops
    d = {}
    cl = {c for v in re.findall(r'class="([^"]+)"', tout) for c in v.split()}
    d['classes_hors_liste'] = sorted(c for c in cl - CLASSES if not c.startswith('mc-'))
    cles = set(re.findall(r'data-k="([^"]+)"', tout))
    tpl = set(re.findall(r'<template data-pop="([^"]+)"', tout))
    reuse = set(filter(None, a.reutilisables.split(',')))
    d['cles_sans_template'] = sorted(cles - tpl - reuse)
    d['cles_non_prefixees'] = sorted(k for k in tpl if not k.startswith((pre + '-', 'pareto-' + pre)) and k not in reuse)
    ids = set(re.findall(r'<section class="ilot" id="([^"]+)"', tout))
    cov = {i for v in re.findall(r'data-cover="([^"]+)"', tout) for i in v.split(',')}
    d['pareto_ids_inconnus'] = sorted(cov - ids)
    d['ouverture'] = [] if f'<template id="ch-{code}">' in corps else [f'<template id="ch-{code}"> absent']
    d['fermeture'] = [] if re.search(r'</div>\s*</template>\s*$', open(fichiers[-1] if fichiers else os.devnull, errors='ignore').read() if fichiers else '') or any(
        re.search(r'</div>\s*</template>\s*$', open(f, errors='ignore').read()) for f in fichiers if f.endswith('_d.html')) else ['</div></template> final absent']
    d['panneaux_manquants'] = [p for p in ('pA', 'pE', 'pS', 'pP') if f'id="{p}"' not in corps and f"id='{p}'" not in corps]
    nq = len(re.findall(r'class="quiz', corps))
    d['quiz_insuffisants'] = [] if nq >= 3 else [f'{nq} quiz']
    G = glossaire(a.glossaire)
    if G:
        txt = re.sub(r'<[^>]+>', ' ', tout)
        ab = set(re.findall(r'\b[A-Z][A-Z0-9]{1,6}\b', txt)) - {'II', 'III', 'IV', 'VI', 'VII', 'VIII', 'IX', 'XI', 'XII', 'NB'}
        d['abreviations_hors_glossaire'] = sorted(ab - G)[:40]
    figs = re.findall(r'<figure\b.*?</figure>', tout, re.S)
    d['figures_sans_attribution'] = [f[:80] for f in figs if '<img' in f and not re.search(r'(CC[ -]BY|CC0|domaine public|public domain|licence)', f, re.I)]
    svgs = re.findall(r'<svg\b.*?</svg>', tout, re.S)
    d['svg_anatomique_sans_source'] = [s[:60] for s in svgs if ANATOMIE.search(s) and not re.search(r'source|licence|CC', s, re.I)]
    d['metaphores'] = list(dict.fromkeys(m.group(0) for m in METAPHORES.finditer(re.sub(r'<[^>]+>', ' ', tout))))[:10]
    d = {k: v for k, v in d.items() if v}
    majeur = {'cles_sans_template', 'ouverture', 'fermeture', 'panneaux_manquants', 'svg_anatomique_sans_source', 'pareto_ids_inconnus'}
    verdict = 'ROUGE' if majeur & set(d) else ('ORANGE' if d else 'VERT')
    print(json.dumps({'chapitre': code, 'fichiers': len(fichiers), 'octets': sum(os.path.getsize(f) for f in fichiers),
                      'verdict': verdict, 'defauts': d}, ensure_ascii=False, indent=1))
    sys.exit(1 if verdict == 'ROUGE' else 0)


if __name__ == '__main__':
    main()
