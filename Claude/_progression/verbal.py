#!/usr/bin/env python3
"""VERBAL — porte des phrases verbales (ordre de Vial du 13.11.2026 : « je déteste profondément les phrases nominales »).
Toute phrase de ≥ 4 mots d'un champ rédigé d'une fiche JSON doit contenir un verbe conjugué (détecteur de
Claude/_outils/controle3.py). Champs exemptés : identifiants, titres, noms, synonymes, sources, valeurs (paramètre, normal).
Usage : python3 Claude/_progression/verbal.py [fichiers.json …]   (défaut : toutes les fiches ; code 1 si une phrase nominale)
        --liste : affiche chaque phrase fautive (fiche · champ · phrase)."""
import json, re, sys, glob, os, importlib.util
ici = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location('c3', os.path.join(ici, '..', '_outils', 'controle3.py'))
c3 = importlib.util.module_from_spec(spec); sys.argv, _a = [sys.argv[0]], sys.argv; spec.loader.exec_module(c3); sys.argv = _a
EXEMPTS = {'id', 'module', 'type', 'titre', 'fonction', 'mecanisme_nom', 'nom', 'sous_onglet', 'systeme', 'etiquettes', 'entree_primaire', 'axe_secondaire',
           'nom_exact', 'synonymes', 'sources', 'parametre', 'normal', 'seuil_alerte', 'cible', 'type_passerelle', 'code', 'cim10'}
def phrases(v, chemin):
    if isinstance(v, dict):
        for k, x in v.items():
            if k not in EXEMPTS: yield from phrases(x, chemin + [k])
    elif isinstance(v, list):
        for i, x in enumerate(v): yield from phrases(x, chemin + [str(i)])
    elif isinstance(v, str) and v.strip() not in ('', '—'):
        for ph in re.split(r'(?<=[.!?])\s+(?=[A-ZÀ-Ý«(])|\n', v):
            if len(re.findall(r"[A-Za-zÀ-ÿ]{2,}", ph)) >= 4: yield '.'.join(chemin), ph.strip()
args = [a for a in sys.argv[1:] if not a.startswith('--')]
fichiers = args or sorted(glob.glob(os.path.join(ici, 'donnees', '*', '*.json')))
fautes = 0; tot = 0
for f in fichiers:
    try: d = json.load(open(f, encoding='utf-8'))
    except Exception: continue
    for champ, ph in phrases(d, []):
        tot += 1
        if not c3.est_verbale(ph):
            fautes += 1
            if '--liste' in sys.argv:
                try: print(f'{os.path.basename(f)} · {champ} · {ph[:140]}')
                except BrokenPipeError: sys.exit(1)
print(f'VERBAL : {fautes} phrase(s) nominale(s) sur {tot} ({len(fichiers)} fiches)')
sys.exit(1 if fautes else 0)
