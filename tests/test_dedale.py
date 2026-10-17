#!/usr/bin/env python3
"""Janus, avec Dédale · tests des contrôles des schémas de nerfs (tools/dedale/verifier.py).

Chaque critère d'acceptation de Dédale a son test : la vérification réussit sur le dépôt, puis échoue
quand la règle est violée (couche ou état mal masqué, texte trop petit à 360 px, repère trop petit, plus de
8 repères par état, texte sur le dessin, repères chevauchés, repère sur le nerf, data-nom absent, data-glo
inconnu, légende incomplète ou trop de notes, numérotation incohérente entre vues, dessin sous 60 %, poids,
crédit, couleur, nerf non jaune, aplat vif, image intégrée, SVG modifié à la main, tour de 8 vues ou
quatrième vue publiés).
"""
import json, os, re, shutil, subprocess, sys, tempfile
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def copie(d):
    for rel in ('tools/dedale', 'nc', 'assets/nc'):
        shutil.copytree(os.path.join(ROOT, rel), os.path.join(d, rel))
    os.makedirs(os.path.join(d, 'data', 'ck'))
    shutil.copy(os.path.join(ROOT, 'data', 'ck', 'glo.json'), os.path.join(d, 'data', 'ck', 'glo.json'))


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


def trop_de_reperes(d):
    p = os.path.join(d, 'nc', 'presets', 'nc07.yml')
    s = open(p, encoding='utf-8').read()
    a = '      - {ref: F3, nom: "Foramen stylo-mastoïdien", couche: foramens}\n'
    assert a in s
    open(p, 'w', encoding='utf-8').write(s.replace(a, a * 3, 1))


def cercles(s, etat='trajet'):
    """Cercles des repères d'un état : [(balise, cx, cy)]."""
    out = []
    for g in re.findall(r'<g class="numeros"[^>]* data-etat="%s"[^>]*>(.*?)</g></g>' % etat, s, re.S):
        for c in re.findall(r'<circle[^>]*>', g):
            out.append((c, re.search(r' cx="([-\d.]+)"', c).group(1), re.search(r' cy="([-\d.]+)"', c).group(1)))
    return out


def deplacer(c, x, y):
    t = re.sub(r' cx="[-\d.]+"', ' cx="%s"' % x, c[0])
    return re.sub(r' cy="[-\d.]+"', ' cy="%s"' % y, t)


def chevauchement(d):
    # deux repères de l'état par défaut au même endroit
    p = os.path.join(d, 'assets', 'nc', V)
    s = open(p, encoding='utf-8').read()
    c = cercles(s)
    open(p, 'w', encoding='utf-8').write(s.replace(c[1][0], deplacer(c[1], c[0][1], float(c[0][2]) + 4), 1))


def sur_le_nerf(d):
    # un repère posé sur le premier point du nerf
    p = os.path.join(d, 'assets', 'nc', V)
    s = open(p, encoding='utf-8').read()
    m = re.search(r'class="n1"><path[^>]* d="[mM](-?\d+(?:\.\d+)?)[ ,]?(-?\d+(?:\.\d+)?)', s)
    c = cercles(s)
    open(p, 'w', encoding='utf-8').write(s.replace(c[0][0], deplacer(c[0], m.group(1), m.group(2)), 1))


def numerotation_incoherente(d):
    # le repère 2 du trajet désigne une autre structure dans la vue de face
    p = os.path.join(d, 'assets', 'nc', 'nc07-face.svg')
    s = open(p, encoding='utf-8').read()
    a = 'data-nom="Segment cisternal"'
    assert a in s and 'aria-label="2 · Segment cisternal"' in s
    s = s.replace(a, 'data-nom="Ganglion trigéminal"', 1).replace('aria-label="2 · Segment cisternal"', 'aria-label="2 · Ganglion trigéminal"', 1)
    open(p, 'w', encoding='utf-8').write(s)


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
    'couche_legende_absente_echoue': lambda d: muter(d, V, 'id="legende"', 'id="autre"'),
    'couche_mal_masquee_echoue': lambda d: muter(d, V, '<g id="lesions" data-couche="lesions" display="none"', '<g id="lesions" data-couche="lesions"'),
    'etat_mal_masque_echoue': lambda d: muter(d, V, '<g class="legende" data-etat="branches" display="none">', '<g class="legende" data-etat="branches">'),
    'legende_trop_petite_echoue': lambda d: muter(d, V, '.lg{font-size:22px', '.lg{font-size:18px'),
    'numero_trop_petit_echoue': lambda d: muter(d, V, '.nm{font-size:18px', '.nm{font-size:16px'),
    'repere_trop_petit_echoue': lambda d: muter_re(d, V, r'(<circle[^>]*) r="14"', r'\1 r="11"'),
    'plus_de_8_reperes_echoue': trop_de_reperes,
    'texte_sur_le_dessin_echoue': lambda d: muter(d, V, '<g id="legende"', '<text x="300" y="400" class="lg">Pore</text><g id="legende"'),
    'reperes_chevauches_echoue': chevauchement,
    'repere_sur_le_nerf_echoue': sur_le_nerf,
    'data_nom_absent_echoue': lambda d: muter_re(d, V, r' data-nom="[^"]*"', ''),
    'data_glo_inconnu_echoue': lambda d: muter(d, V, 'data-glo="hyperacousie"', 'data-glo="terme-inconnu"'),
    'repere_sans_fleche_echoue': lambda d: muter_re(d, V, r'<path d="[^"]*" class="ah"/>', ''),
    'legende_incomplete_echoue': lambda d: muter_re(d, V, r'(<g class="legende" data-etat="trajet">)<text[^>]*><tspan class="n">1</tspan>[^<]*</text>', r'\1'),
    'notes_trop_longues_echoue': lambda d: muter(d, V, '<g class="legende" data-etat="trajet">',
                                                 '<g class="legende" data-etat="trajet">' + '<text x="24" y="1" class="lg">a</text>' * 3),
    'numerotation_incoherente_echoue': numerotation_incoherente,
    'dessin_sous_60_pourcent_echoue': lambda d: muter(d, V, 'data-zone="0 64 800 800"', 'data-zone="0 64 800 400"'),
    'poids_depasse_echoue': lambda d: muter(d, V, '</svg>', '<!--' + 'x' * 130000 + '--></svg>'),
    'couleur_interdite_echoue': lambda d: muter(d, V, '#8a8a8a', '#1d4ed8'),
    'nerf_vert_echoue': lambda d: muter(d, V, '.n2 path{stroke:#ffc400', '.n2 path{stroke:#156534'),
    'rouge_hors_lesions_echoue': lambda d: muter(d, V, 'class="cr"', 'class="cr u"'),
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
