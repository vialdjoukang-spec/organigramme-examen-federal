#!/usr/bin/env python3
"""Janus, avec Dédale · tests des contrôles des schémas de nerfs (tools/dedale/verifier.py).

Chaque critère d'acceptation de Dédale a son test : la vérification réussit sur le dépôt, puis échoue
quand la règle est violée (couche absente, texte trop petit, poids, crédit, couleur, image intégrée,
SVG modifié à la main, tour hors des paires autorisées).
"""
import json, os, shutil, subprocess, sys, tempfile
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def copie(d):
    for rel in ('tools/dedale', 'nc', 'assets/nc'):
        shutil.copytree(os.path.join(ROOT, rel), os.path.join(d, rel))


def verif(d, *extra):
    return subprocess.run([sys.executable, os.path.join(d, 'tools', 'dedale', 'verifier.py'), '--tous', *extra],
                          capture_output=True, text=True).returncode


def muter(d, f, a, b):
    p = os.path.join(d, 'assets', 'nc', f)
    s = open(p, encoding='utf-8').read()
    assert a in s, (f, a)
    open(p, 'w', encoding='utf-8').write(s.replace(a, b, 1))


CAS = {
    'couche_absente_echoue': lambda d: muter(d, 'nc07-face.svg', 'id="foramens"', 'id="autre"'),
    'texte_trop_petit_echoue': lambda d: muter(d, 'nc07-face.svg', '.cr{font-size:20px', '.cr{font-size:12px'),
    'poids_depasse_echoue': lambda d: muter(d, 'nc07-face.svg', '</svg>', '<!--' + 'x' * 130000 + '--></svg>'),
    'couleur_interdite_echoue': lambda d: muter(d, 'nc07-face.svg', 'stroke:#9a9a9a', 'stroke:#1d4ed8'),
    'rouge_hors_lesions_echoue': lambda d: muter(d, 'nc07-face.svg', 'stroke:#9a9a9a', 'stroke:#b91c1c'),
    'image_integree_echoue': lambda d: muter(d, 'nc07-face.svg', '</svg>', '<image href="data:image/png;base64,AA"/></svg>'),
    'svg_retouche_echoue': lambda d: muter(d, 'nc07-34.svg', 'Nerf facial (VII)', 'Nerf facial (VII) '),
}


def credit_sans(champ):
    def f(d):
        p = os.path.join(d, 'assets', 'nc', 'credits.json')
        data = json.load(open(p, encoding='utf-8'))
        data[0].pop(champ)
        json.dump(data, open(p, 'w', encoding='utf-8'), ensure_ascii=False)
    return f


CAS['credit_sans_licence_echoue'] = credit_sans('licence')
CAS['credit_sans_mention_derivee_echoue'] = credit_sans('mention')


def tour_interdit(d):
    shutil.copy(os.path.join(d, 'assets', 'nc', 'nc07-tour.webp'), os.path.join(d, 'assets', 'nc', 'nc01-tour.webp'))
    shutil.copy(os.path.join(d, 'nc', 'annot', 'nc07.yml'), os.path.join(d, 'nc', 'annot', 'nc01.yml'))
    p = os.path.join(d, 'nc', 'annot', 'nc01.yml')
    s = open(p, encoding='utf-8').read().replace('vues: [face, profil, "34", plan]', 'vues: []')
    open(p, 'w', encoding='utf-8').write(s)


CAS['tour_hors_V_VII_oculomoteurs_echoue'] = tour_interdit

res = {}
rejeu = shutil.which('svgo') is not None
opt = () if rejeu else ('--sans-rejeu',)
with tempfile.TemporaryDirectory() as d:
    copie(d)
    res['depot_conforme_reussit'] = verif(d, *opt) == 0
for nom, f in CAS.items():
    if nom == 'svg_retouche_echoue' and not rejeu:
        continue
    with tempfile.TemporaryDirectory() as d:
        copie(d); f(d)
        # Chaque cas teste sa propre règle : le rejeu (V7) n'est actif que pour le cas « retouché ».
        res[nom] = verif(d, *(opt if nom == 'svg_retouche_echoue' else ('--sans-rejeu',))) != 0
for k, v in res.items():
    print(('ok    ' if v else 'ÉCHEC ') + k)
print('Dédale : %d/%d%s.' % (sum(res.values()), len(res), '' if rejeu else ' (svgo absent : rejeu non testé)'))
sys.exit(0 if all(res.values()) else 1)
