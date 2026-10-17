#!/usr/bin/env python3
"""Janus, avec Dédale · tests des contrôles des schémas de nerfs (tools/dedale/verifier.py).

Chaque critère d'acceptation de Dédale a son test : la vérification réussit sur le dépôt, puis échoue
quand la règle est violée (couche ou état mal masqué, texte sous 13 px à 360 px, plus de 8 étiquettes par
état, étiquettes chevauchées, légende de plus de 4 lignes, dessin sous 60 %, poids, crédit, couleur, nerf non
jaune, aplat vif, image intégrée, SVG modifié à la main, tour de 8 vues ou quatrième vue publiés).
"""
import json, os, re, shutil, subprocess, sys, tempfile
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


def muter_re(d, f, motif, rempl):
    p = os.path.join(d, 'assets', 'nc', f)
    s = open(p, encoding='utf-8').read()
    t = re.sub(motif, rempl, s, count=1, flags=re.S)
    assert t != s, (f, motif)
    open(p, 'w', encoding='utf-8').write(t)


def trop_d_etiquettes(d):
    p = os.path.join(d, 'nc', 'presets', 'nc07.yml')
    s = open(p, encoding='utf-8').read()
    a = '      - {ref: F3, texte: "Foramen stylo-mastoïdien", couche: foramens}\n'
    assert a in s
    open(p, 'w', encoding='utf-8').write(s.replace(a, a * 3, 1))


def chevauchement(d):
    # deux étiquettes de l'état par défaut au même endroit
    p = os.path.join(d, 'assets', 'nc', 'nc07-profil.svg')
    s = open(p, encoding='utf-8').read()
    t = re.findall(r'<text[^>]*class="lb[^"]*"[^>]*>', s)
    xy = lambda tag: (re.search(r' x="([-\d.]+)"', tag).group(1), re.search(r' y="([-\d.]+)"', tag).group(1))
    (x1, y1), (x2, y2) = xy(t[0]), xy(t[1])
    t2 = t[1].replace(' x="%s"' % x2, ' x="%s"' % x1).replace(' y="%s"' % y2, ' y="%s"' % y1)
    open(p, 'w', encoding='utf-8').write(s.replace(t[1], t2, 1))


def fichier_en_plus(nom, source=None):
    def f(d):
        dst = os.path.join(d, 'assets', 'nc', nom)
        if source:
            shutil.copy(os.path.join(d, 'assets', 'nc', source), dst)
        else:
            open(dst, 'wb').write(b'RIFF0000WEBP')
    return f


V = 'nc07-profil.svg'
CAS = {
    'couche_absente_echoue': lambda d: muter(d, V, 'id="foramens"', 'id="autre"'),
    'couche_mal_masquee_echoue': lambda d: muter(d, V, '<g id="lesions" data-couche="lesions" display="none"', '<g id="lesions" data-couche="lesions"'),
    'etat_mal_masque_echoue': lambda d: muter(d, V, '<g class="legende" data-etat="branches" display="none">', '<g class="legende" data-etat="branches">'),
    'texte_trop_petit_echoue': lambda d: muter(d, V, '.lb,.lg{font-size:30px', '.lb,.lg{font-size:28px'),
    'plus_de_8_etiquettes_echoue': trop_d_etiquettes,
    'etiquettes_chevauchees_echoue': chevauchement,
    'legende_de_5_lignes_echoue': lambda d: muter(d, V, '<g class="legende" data-etat="trajet">',
                                                  '<g class="legende" data-etat="trajet"><text class="lg" x="24" y="1">a</text><text class="lg" x="24" y="2">b</text>'),
    'dessin_sous_60_pourcent_echoue': lambda d: muter(d, V, 'data-zone="0 64 800 800"', 'data-zone="0 64 800 400"'),
    'poids_depasse_echoue': lambda d: muter(d, V, '</svg>', '<!--' + 'x' * 130000 + '--></svg>'),
    'couleur_interdite_echoue': lambda d: muter(d, V, '#8a8a8a', '#1d4ed8'),
    'nerf_vert_echoue': lambda d: muter(d, V, '.n2 path{stroke:#ffc400', '.n2 path{stroke:#156534'),
    'rouge_hors_lesions_echoue': lambda d: muter(d, V, 'class="pt"', 'class="pt u"'),
    'aplat_vif_echoue': lambda d: muter(d, V, 'fill="#f6d7b0"', 'fill="#1d4ed8"'),
    'image_integree_echoue': lambda d: muter(d, V, '</svg>', '<image href="data:image/png;base64,AA"/></svg>'),
    'svg_retouche_echoue': lambda d: muter(d, V, 'vue de profil droit', 'vue de profil  droit'),
    'tour_de_8_vues_echoue': fichier_en_plus('nc07-tour.webp'),
    'quatrieme_vue_echoue': fichier_en_plus('nc07-plan.svg', 'nc07-face.svg'),
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
