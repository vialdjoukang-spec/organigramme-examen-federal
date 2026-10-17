#!/usr/bin/env python3
"""Dédale-S · schéma clé « voie motrice » d'un nerf crânien (pilote : VII, paralysie centrale ou périphérique).

INSTRUCTIONS (automate, zéro jeton) ------------------------------------------------
    python3 tools/dedale/voie.py nc07            # compose assets/nc/nc07-voie-motrice.svg et son crédit
    python3 tools/dedale/voie.py nc07 --verifier # recompose en mémoire et compare à l'octet (CI)
Entrée  : nc/presets/<nerf>-voie-motrice.yml (états, repères, notes de légende, couleurs des fibres).
Sortie  : un SVG au même contrat que les 3 vues (annoter.py) : couches nommées data-couche, états data-etats et
          data-etat, aucun texte sur le dessin sauf le titre, repères numérotés g.nc-num fléchés, légende numérotée
          en 2 colonnes (g#legende), crédit court (g#credit), métadonnées de licence.
Dessin  : schéma ORIGINAL en coupe frontale (pas un rendu du modèle 3D ; Blender inutile), tracé par ce programme
          depuis la géométrie ci-dessous : 2 hémisphères, capsules internes, tronc cérébral (pont), noyaux faciaux en
          2 parties (haute et basse), nerfs faciaux jusqu'aux 2 hémifaces d'un visage. Traits au crayon (graisse
          hiérarchisée, léger tremblé rejouable), fibres cortico-nucléaires en gris (hémisphère droit) et en bleu
          (hémisphère gauche), nerf facial seul en jaune. Vue de face : la droite du patient est à gauche de l'image.
Anatomie : StatPearls NBK526119 et NBK555891, Gray 1918 § 5g (voir credits.json) : partie haute (dorsale) du
          noyau innervée par les 2 hémisphères, partie basse (ventrale) par l'hémisphère opposé seulement.
"""
import json, math, os, random, sys
from xml.sax.saxutils import escape
import yaml
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import annoter as A  # noqa: E402

ROOT, OUT, W, HEAD = A.ROOT, A.OUT, A.W, A.HEAD
COUCHES = ('territoires', 'trait', 'voies', 'nerf', 'noyaux', 'foramens', 'lesions', 'legendes', 'legende')
STYLE_PLUS = ('.ks{fill:none;stroke:#1a1a1a;stroke-width:4.2px;stroke-linecap:round;stroke-linejoin:round}'
              '.kc{fill:none;stroke:#2b2b2b;stroke-width:2.2px;stroke-linecap:round;stroke-linejoin:round}'
              '.kd{fill:none;stroke:#8a8a8a;stroke-width:1.2px;stroke-linecap:round;stroke-linejoin:round}'
              '.vf{fill:none;stroke-width:2.8px;stroke-linecap:round;stroke-linejoin:round}'
              '.vf.d{stroke:%s}.vf.g{stroke:%s}'
              '.coupe{fill:none;stroke:#fff;stroke-width:4px;stroke-dasharray:5 6;stroke-linecap:butt}'
              '.lx{fill:none;stroke:#b91c1c;stroke-width:4px;stroke-linecap:round}'
              '.px{fill:none;stroke:#222;stroke-width:4px;stroke-linecap:round}')
SOURCES = [
    {'titre': 'Neuroanatomy, Cranial Nerve 7 (Facial)', 'auteur': 'StatPearls (NCBI Bookshelf)',
     'url': 'https://www.ncbi.nlm.nih.gov/books/NBK526119/', 'licence': 'CC BY-NC-ND 4.0 (texte lu, rien n’est copié)',
     'loc': 'Structure and Function ; Clinical Significance (paralysie centrale)', 'lu_le': A.DATE},
    {'titre': 'Neuroanatomy, Corticobulbar Tract', 'auteur': 'StatPearls (NCBI Bookshelf)',
     'url': 'https://www.ncbi.nlm.nih.gov/books/NBK555891/', 'licence': 'CC BY-NC-ND 4.0 (texte lu, rien n’est copié)',
     'loc': 'Structure and Function ; Clinical Significance', 'lu_le': A.DATE},
    {'titre': 'Gray H., Anatomy of the Human Body, 20e éd., 1918, § 5g « The Facial Nerve »', 'auteur': 'H. Gray, H. V. Carter',
     'url': 'https://commons.wikimedia.org/wiki/File:Gray788.png', 'licence': 'Domaine public', 'loc': '§ 5g', 'lu_le': A.DATE},
]
CREDIT_COURT = ['CC BY-SA 4.0 · schéma original (Dédale), d’après StatPearls', '(NBK526119, NBK555891) et Gray 1918, lus le 17.10.2026.']


# ---------------------------------------------------------------- géométrie (coordonnées de l'image, 800 px)
def miroir(pts):
    return [(round(W - x, 1), y) for x, y in pts]


def ellipse(cx, cy, rx, ry, n=72, a0=0.0, a1=2 * math.pi, onde=None):
    out = []
    for i in range(n + 1):
        t = a0 + (a1 - a0) * i / n
        k = 1 + (onde(t) if onde else 0)
        out.append((cx + rx * k * math.cos(t), cy + ry * k * math.sin(t)))
    return out


def lisser(pts, pas=4.0):
    """Catmull-Rom échantillonnée tous les « pas » px environ."""
    if len(pts) < 3:
        return list(pts)
    P = [pts[0]] + list(pts) + [pts[-1]]
    out = [pts[0]]
    for i in range(1, len(P) - 2):
        p0, p1, p2, p3 = P[i - 1], P[i], P[i + 1], P[i + 2]
        n = max(2, int(math.hypot(p2[0] - p1[0], p2[1] - p1[1]) / pas))
        for j in range(1, n + 1):
            t = j / n
            out.append(tuple(0.5 * ((2 * p1[c]) + (-p0[c] + p2[c]) * t + (2 * p0[c] - 5 * p1[c] + 4 * p2[c] - p3[c]) * t * t
                                    + (-p0[c] + 3 * p1[c] - 3 * p2[c] + p3[c]) * t ** 3) for c in (0, 1)))
    return out


def crayon(pts, graine, amp=0.7, ferme=False, lisse=True):
    """Chemin au crayon : courbe lissée, léger tremblé lent (graine fixe : rejouable à l'octet)."""
    q = lisser(pts) if lisse else list(pts)
    rnd = random.Random(graine)
    dx = dy = 0.0
    out = []
    for x, y in q:
        dx = 0.8 * dx + 0.2 * rnd.uniform(-amp, amp) * 3
        dy = 0.8 * dy + 0.2 * rnd.uniform(-amp, amp) * 3
        out.append((x + dx, y + dy))
    d = 'M' + 'L'.join('%.1f %.1f' % p for p in out)
    return d + ('Z' if ferme else '')


def droit(pts):
    return 'M' + 'L'.join('%.1f %.1f' % p for p in pts)


def geometrie():
    G = {'ks': [], 'kc': [], 'kd': [], 'fd': [], 'fg': [], 'nerf': [], 'noyaux': [], 'anc': {}}
    gy = lambda t: 0.022 * math.sin(15 * t) * (1 if math.cos(t) < 0.35 else 0.15)          # gyres (face latérale)
    # hémisphère droit du patient (gauche de l'image), puis miroir
    hem = ellipse(252, 238, 148, 140, n=120, onde=gy)
    sylvius = [(108, 286), (160, 292), (215, 298), (238, 288)]
    ventricule = [(392, 206), (368, 214), (356, 236), (372, 246), (394, 240)]
    thalamus = ellipse(347, 300, 22, 17, n=36)
    lenticulaire = [(262, 330), (292, 276), (306, 300), (304, 332), (262, 330)]
    for i, (pts, cls, ferme) in enumerate(((hem, 'ks', True), (sylvius, 'kc', False), (ventricule, 'kd', False),
                                           (thalamus, 'kd', True), (lenticulaire, 'kd', True))):
        G[cls].append(crayon(pts, 10 + i, ferme=ferme, lisse=cls != 'ks'))
        G[cls].append(crayon(miroir(pts), 20 + i, ferme=ferme, lisse=cls != 'ks'))
    # tronc cérébral : mésencéphale, pont (renflé), bulbe
    tronc = [(362, 348), (360, 390), (356, 440), (330, 462), (318, 500), (330, 538), (366, 552), (372, 600),
             (400, 604), (428, 600), (434, 552), (470, 538), (482, 500), (470, 462), (444, 440), (440, 390), (438, 348)]
    G['ks'].append(crayon(tronc, 31))
    G['kd'].append(crayon([(366, 552), (400, 556), (434, 552)], 32))            # sillon bulbo-pontique
    G['kd'].append(crayon([(356, 440), (400, 446), (444, 440)], 33))            # limite pont-mésencéphale
    # visage : 2 hémifaces de part et d'autre de la ligne médiane
    face = ellipse(400, 738, 112, 120, n=96)
    G['ks'].append(crayon(face, 41, ferme=True, lisse=False))
    oreille = [(290, 702), (276, 708), (274, 732), (288, 748)]
    sourcil = [(332, 676), (352, 668), (378, 674)]
    oeil = ellipse(356, 694, 18, 6, n=24)
    for i, (pts, cls, ferme) in enumerate(((oreille, 'kc', False), (sourcil, 'kc', False), (oeil, 'kc', True))):
        G[cls].append(crayon(pts, 50 + i, ferme=ferme))
        G[cls].append(crayon(miroir(pts), 60 + i, ferme=ferme))
    G['kc'].append(crayon([(400, 700), (392, 752), (404, 760)], 71))                       # nez
    G['kc'].append(crayon([(366, 800), (384, 808), (400, 809), (416, 808), (434, 800)], 72))  # bouche
    G['kd'].append(crayon([(312, 650), (350, 642), (400, 640), (450, 642), (488, 650)], 73))  # rides du front
    # fibres cortico-nucléaires (1er motoneurone) : hémisphère droit en gris, gauche en bleu (miroir)
    descente = [(120, 238), (200, 250), (284, 266), (314, 296), (330, 344), (352, 392), (370, 432), (382, 460)]
    ipsi = [(382, 460), (376, 470), (371, 476)]
    croise_haut = [(382, 460), (400, 466), (420, 474), (428, 477)]
    croise_bas = [(384, 462), (402, 478), (416, 494), (424, 499)]
    for pts_list, cle in (((descente, ipsi, croise_haut, croise_bas), 'fd'),):
        for j, pts in enumerate(pts_list):
            G['fd'].append(crayon(pts, 80 + j, amp=0.3))
            G['fg'].append(crayon(miroir(pts), 90 + j, amp=0.3))
    # noyaux faciaux : partie haute et partie basse, de chaque côté
    for cx in (370, 430):
        for cy in (484, 506):
            G['noyaux'].append(droit(ellipse(cx, cy, 12, 8, n=32)) + 'Z')
    # nerf facial (2e motoneurone) : du noyau au visage, branches haute (front) et basse (bouche)
    sortie = [(358, 484), (346, 498), (342, 506), (332, 522), (322, 530)]
    sortie_bas = [(358, 506), (346, 512), (334, 524)]
    tronc_n = [(322, 530), (292, 546), (268, 584), (262, 632), (266, 676), (276, 698), (284, 708)]
    haut = [(284, 708), (300, 682), (322, 658), (344, 646)]
    bas = [(284, 708), (294, 748), (318, 782), (352, 798)]
    nerf = (sortie, sortie_bas, tronc_n, haut, bas)
    for j, pts in enumerate(nerf):
        G['nerf'].append(crayon(pts, 100 + j, amp=0.25))
        G['nerf'].append(crayon(miroir(pts), 110 + j, amp=0.25))
    G['pts_fibres'] = [p for pts in (descente, ipsi, croise_haut, croise_bas) for p in lisser(pts, 2)]
    G['pts_fibres'] += [p for pts in (descente, ipsi, croise_haut, croise_bas) for p in lisser(miroir(pts), 2)]
    G['pts_nerf'] = [p for pts in nerf for q in (pts, miroir(pts)) for p in lisser(q, 1.5)]
    G['pts_noyaux'] = [p for cx in (370, 430) for cy in (484, 506) for p in ellipse(cx, cy, 12, 8, n=48)]
    # lésions : centrale (capsule interne droite) et périphérique (nerf facial droit), zones paralysées
    def quart(x_sens, haut_aussi):
        y0 = 738 - 120 if haut_aussi else 714
        pts = [(400, y0)]
        for i in range(61):
            t = -math.pi / 2 + math.pi * i / 60
            x, y = 400 + 112 * math.cos(t) * x_sens, 738 + 120 * math.sin(t)
            if y >= y0:
                pts.append((x, y))
        pts.append((400, 858))
        return 'M' + 'L'.join('%.1f %.1f' % p for p in pts) + 'Z'
    G['zone_centrale'] = quart(+1, False)       # bas du visage, côté gauche du patient (droite de l'image)
    G['zone_peripherique'] = quart(-1, True)    # hémiface droite entière (gauche de l'image)
    G['coupe_centrale'] = [droit(lisser(p, 2)) for p in ([(322, 318), (330, 344), (352, 392), (370, 432), (382, 460)], ipsi, croise_haut, croise_bas)]
    G['coupe_peripherique'] = [droit(lisser(p, 2)) for p in ([(263, 618), (262, 632), (266, 676), (276, 698), (284, 708)], haut, bas)]
    G['x_centrale'] = (322, 318)
    G['x_peripherique'] = (264, 606)
    G['anc'] = {'cortex': (120, 238), 'capsule_g': (W - 314, 296), 'croisement': (400, 468),
                'noyau_haut_g': (442, 482), 'noyau_bas_g': (442, 508), 'nerf_g': (W - 263, 640),
                'lesion_centrale': (322, 318), 'zone_centrale': (456, 790),
                'lesion_peripherique': (264, 606), 'zone_peripherique': (338, 738)}
    return G


def croix(c, cls, r=9):
    x, y = c
    return '<path class="%s" d="M%.1f %.1fL%.1f %.1fM%.1f %.1fL%.1f %.1f"/>' % (cls, x - r, y - r, x + r, y + r, x - r, y + r, x + r, y - r)


# ---------------------------------------------------------------- composition
def composer(nerf, P):
    G = geometrie()
    zone = (0, HEAD, W, W)
    # le dessin est en coordonnées de l'image : la zone (0, HEAD) ↔ y de 64 à 864
    grille = A.Grille(G['pts_nerf'] + G['pts_noyaux'] + G['pts_fibres'])
    defaut = P['etat_defaut']
    etats, groupes, legendes, toutes = {}, [], [], []
    fills = {}
    for nom, E in P['etats'].items():
        if len(E['etiquettes']) > A.MAX_ETIQ:
            sys.exit('ÉCHEC : état %s : %d repères, %d au plus.' % (nom, len(E['etiquettes']), A.MAX_ETIQ))
        reps = []
        for num, et in enumerate(E['etiquettes'], 1):
            sx, sy = G['anc'][et['ancre']]
            reps.append({'num': num, 'ref': et['ancre'], 'nom': et['nom'], 'glo': et.get('glo'), 'sx': sx, 'sy': sy,
                         'couche': et.get('couche', 'legendes'), 'urgence': bool(et.get('urgence')), 'source': 'StatPearls NBK526119'})
        try:
            A.placer(reps, zone, grille)
        except SystemExit as ex:
            sys.exit('%s (schéma voie motrice, état %s)' % (ex, nom))
        etats[nom] = list(E['couches'])
        cache = '' if nom == defaut else ' display="none"'
        par_couche = {}
        for m in reps:
            par_couche.setdefault(m['couche'], []).append(A.rendu_repere(m))
        for c in COUCHES:
            if c in par_couche:
                groupes.append('<g class="numeros" data-etat="%s" data-couche="%s"%s>%s</g>' % (nom, c, cache, ''.join(par_couche[c])))
        legendes.append((nom, A.lignes_legende(E, reps), cache))
        toutes.append((nom, E, reps))
        fills.update(E.get('remplissages') or {})
    # couche lesions : une sous-couche par état (zone paralysée pâle, interruption des fibres, croix)
    # zone paralysée (aplat pâle, couche territoires, sous le trait) ; interruption des fibres et croix (couche lesions)
    les, ter = [], []
    for nom in P['etats']:
        cache = '' if nom == defaut else ' display="none"'
        k = 'centrale' if nom == 'central' else 'peripherique'
        ter.append('<g class="zone" data-etat="%s"%s><path fill="%s" d="%s"/></g>' % (nom, cache, fills['paralysie'], G['zone_' + k]))
        corps = (''.join('<path class="coupe" d="%s"/>' % d for d in G['coupe_' + k]) +
                 croix(G['x_' + k], 'lx' if nom == 'central' else 'px'))
        les.append('<g class="lesion" data-etat="%s"%s>%s</g>' % (nom, cache, corps))
    y_leg = HEAD + W + 34
    nl = max(r for _, (_, r), _ in legendes)
    y_cred = y_leg + nl * A.LL + 12
    H = int(y_cred + A.LL + 12)
    leg = []
    for nom, (lignes, _), cache in legendes:
        leg.append('<g class="legende" data-etat="%s"%s>%s</g>' % (nom, cache, ''.join(
            ('<text class="lg" x="%d" y="%d"><tspan class="n">%d</tspan> · %s</text>' % (x, y_leg + r * A.LL, num, escape(t))) if num
            else '<text class="lg" x="%d" y="%d">%s</text>' % (x, y_leg + r * A.LL, escape(t)) for x, r, num, t in lignes)))
    cred = ''.join('<text class="lg" x="24" y="%d">%s</text>' % (y_cred + n * A.LL, escape(t)) for n, t in enumerate(CREDIT_COURT))
    vis = lambda c: '' if c in etats[defaut] else ' display="none"'
    couches = {
        'trait': '<g class="kd">%s</g><g class="kc">%s</g><g class="ks">%s</g>' % tuple(
            ''.join('<path d="%s"/>' % d for d in G[k]) for k in ('kd', 'kc', 'ks')),
        'voies': '<g class="vf d">%s</g><g class="vf g">%s</g>' % (''.join('<path d="%s"/>' % d for d in G['fd']),
                                                                   ''.join('<path d="%s"/>' % d for d in G['fg'])),
        'nerf': '<g class="nf"><g class="n1">%s</g><g class="n2">%s</g></g>' % ((''.join('<path d="%s"/>' % d for d in G['nerf']),) * 2),
        'noyaux': '<g class="nx">%s</g>' % ''.join('<path d="%s"/>' % d for d in G['noyaux']),
        'lesions': ''.join(les),
        'territoires': ''.join(ter),
    }
    titre = P['titre']
    desc = '%s : coupe frontale schématique. États : %s.' % (titre, ' ; '.join(
        '%s (%s)' % (E['nom'], ', '.join('%d %s' % (m['num'], m['nom']) for m in L)) for _, E, L in toutes))
    meta = json.dumps({'licence': 'CC BY-SA 4.0', 'licence_url': 'https://creativecommons.org/licenses/by-sa/4.0/',
                       'mention': 'Schéma original', 'credit': credit_complet(), 'sources': SOURCES,
                       'etats': {n: [{'num': m['num'], 'ancre': m['ref'], 'nom': m['nom']} for m in L] for n, _, L in toutes},
                       'valide_par_vial': False}, ensure_ascii=False, sort_keys=True)
    style = (A.STYLE.replace('{N1}', '%.1f' % (2 * A.D_NERF)).replace('{N2}', '6.5').replace('{NX}', '1')
             + STYLE_PLUS % (P['fibres']['droite'], P['fibres']['gauche']))
    out = ['<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %d %d" role="img" aria-labelledby="t d" data-nerf="%s" data-vue="voie-motrice" '
           'data-etat="%s" data-etats="%s" data-zone="0 %d %d %d">' % (W, H, nerf, defaut, escape(json.dumps(etats, separators=(',', ':')), {'"': '&quot;'}), HEAD, W, W),
           '<title id="t">%s</title><desc id="d">%s</desc><metadata>%s</metadata>' % (escape(titre), escape(desc), escape(meta)),
           '<style>%s</style>' % style,
           '<rect width="%d" height="%d" fill="#fff"/>' % (W, H),
           '<text class="tt" x="24" y="44">%s</text>' % escape(titre),
           '<svg x="0" y="%d" width="%d" height="%d" viewBox="0 %d %d %d" overflow="hidden">' % (HEAD, W, W, HEAD, W, W)]
    for c in COUCHES[:-1]:
        out.append('<g id="%s" data-couche="%s"%s>%s</g>' % (c, c, vis(c), couches.get(c, '')))
    out.append('</svg>')
    out += groupes
    out.append('<g id="legende" data-couche="legende"%s>%s</g>' % (vis('legende'), ''.join(leg)))
    out.append('<g id="credit">%s</g></svg>\n' % cred)
    return ''.join(out), toutes


def credit_complet():
    return ('Schéma original, CC BY-SA 4.0 : coupe frontale tracée par automate (Dédale, 17.10.2026, tools/dedale/voie.py), '
            'd’après StatPearls « Neuroanatomy, Cranial Nerve 7 (Facial) » (NBK526119) et « Neuroanatomy, Corticobulbar Tract » '
            '(NBK555891), et Gray 1918 § 5g (domaine public) ; aucune figure n’est copiée ni décalquée.')


def credit_entree(nerf, ko, toutes):
    f = '%s-voie-motrice.svg' % nerf
    return {
        'fichier': f, 'nerf': nerf, 'vue': 'voie-motrice',
        'titre': 'Nerf facial (VII) · voie motrice : paralysie centrale ou périphérique',
        'auteur': 'Dédale (automate tools/dedale/voie.py), projet Organigramme Examen fédéral',
        'source': 'Schéma original d’après références anatomiques (StatPearls NBK526119, NBK555891 ; Gray 1918 § 5g)',
        'source_url': SOURCES[0]['url'], 'url': SOURCES[0]['url'],
        'licence': 'CC BY-SA 4.0', 'licence_url': 'https://creativecommons.org/licenses/by-sa/4.0/',
        'derive': False, 'oeuvre_derivee': False, 'schema_original': True, 'mention': 'Schéma original',
        'references': SOURCES,
        'modifications': ('Coupe frontale schématique composée par tools/dedale/voie.py (géométrie codée, traits au crayon, '
                          'fibres cortico-nucléaires grises et bleues, nerf facial jaune) ; repères numérotés et légende par '
                          'tools/dedale/annoter.py ; états %s ; svgo 4.0.0.' % ', '.join(n for n, _, _ in toutes)),
        'a_verifier': ('Passage exact dans la capsule interne (genou ou bras postérieur, selon la source) ; part relative des '
                       'fibres directes pour la partie basse du noyau (« mainly contralateral »).'),
        'verifie_le': A.DATE, 'genere_par_ia': False, 'contenu_verifie_visuellement': True, 'valide_par_vial': False,
        'etats': [n for n, _, _ in toutes], 'ko': ko,
    }


def construire(nerf):
    P = yaml.safe_load(open(os.path.join(ROOT, 'nc', 'presets', nerf + '-voie-motrice.yml'), encoding='utf-8'))
    txt, toutes = composer(nerf, P)
    return A.svgo(txt), toutes


def main():
    args = sys.argv[1:]
    nerf = next((x for x in args if not x.startswith('--')), 'nc07')
    txt, toutes = construire(nerf)
    f = '%s-voie-motrice.svg' % nerf
    p = os.path.join(OUT, f)
    if '--verifier' in args:
        ok = os.path.exists(p) and open(p, encoding='utf-8').read() == txt
        print('Recomposition à l’octet : %s %s.' % (f, 'identique' if ok else 'DIFFÉRENTE'))
        sys.exit(0 if ok else 1)
    open(p, 'w', encoding='utf-8', newline='\n').write(txt)
    print('assets/nc/%s : %d octets' % (f, len(txt.encode())))
    A.ecrire_credits([credit_entree(nerf, round(len(txt.encode()) / 1024), toutes)])


if __name__ == '__main__':
    main()
