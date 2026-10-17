#!/usr/bin/env python3
"""Dédale-A · composition des 3 vues annotées d'un nerf crânien (face, profil, trois quarts).

INSTRUCTIONS (automate, zéro jeton) ------------------------------------------------
    python3 tools/dedale/annoter.py nc07            # compose assets/nc/nc07-{face,profil,34}.svg et nc07-presets.json
    python3 tools/dedale/annoter.py nc07 --verifier # recompose en mémoire et compare à l'octet (CI)
Entrées : nc/presets/<nerf>.yml (états : couches visibles, 8 étiquettes au plus, légende courte ; retraits par vue),
          nc/annot/<nerf>.yml (annotations sourcées d'Ariane, citées par « ref »),
          nc/trait/<nerf>-<vue>-crane.svg/.json (crâne au crayon et cadre, crane.py),
          nc/trait/<nerf>-<vue>.svg/.json (courbes du nerf et ancres, freestyle.py),
          nc/trait/<nerf>-<vue>-masques.svg/.json (aplats des territoires, masques.py), nc/sources.yml.
Sortie  : une image par vue. Les 7 couches (trait, territoires, nerf, noyaux, foramens, lesions, legendes) et
          TOUS les états y figurent : data-etats (JSON état -> couches visibles), data-etat (état affiché par
          défaut) ; chaque groupe d'étiquettes porte data-etat et data-couche. Hermès change d'état en
          affichant [data-etat="X"] et les couches de data-etats[X], et en masquant le reste.
Rendu   : crâne en traits pleins à graisse hiérarchisée (silhouette épaisse, contours moyens, détails légers) ;
          nerf en jaune intense (#FFC400) cerné d'un trait sombre de 1 px (#5a4500), tout son trajet, au-dessus
          de tout ; noyaux pleins en jaune ; rouge (#b91c1c) seulement pour le site lésionnel « urgence: true ».
Étiquettes : 30 px (13,5 px à 360 px), posées à côté de leur structure par un placement rejouable, sans
          chevauchement ni trait de rappel croisé à l'intérieur d'un état ; légende ≤ 4 lignes crédit compris.
"""
import json, math, os, random, re, shutil, subprocess, sys, tempfile
from xml.sax.saxutils import escape
import yaml

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
HERE = os.path.join(ROOT, 'tools', 'dedale')
OUT = os.path.join(ROOT, 'assets', 'nc')
DATE = '2026-10-17'
JAUNE, CERNE, ROUGE = '#ffc400', '#5a4500', '#b91c1c'
W, HEAD, FS, FT, LH = 800, 64, 30, 32, 38
CAR = 0.60          # largeur moyenne d'un caractère en em (estimation prudente, contrôlée par verifier.py)
LBL_H = 36          # hauteur d'une boîte d'étiquette (30 px + interligne)
BASE = 26           # ligne de base dans la boîte
MAX_ETIQ, MAX_LEG = 8, 4
NOMS_VUES = {'face': 'vue de face', 'profil': 'vue de profil droit', '34': 'vue de trois quarts droite'}
COUCHES = ('territoires', 'trait', 'nerf', 'noyaux', 'foramens', 'lesions', 'legendes')
STYLE = ('text{font-family:system-ui,-apple-system,"Segoe UI",Roboto,Arial,sans-serif;fill:#111}'
         '.tt{font-size:%dpx;font-weight:700}.lb,.lg{font-size:%dpx}'
         '.lb{paint-order:stroke;stroke:#fff;stroke-width:7px;stroke-linejoin:round}'
         '.lb.u{fill:%s;font-weight:700}'
         '.cs path{fill:#222}.cc path{fill:#2b2b2b}.cd path{fill:#8a8a8a}.ct path{fill:#6b6b6b}.fl path{fill:inherit}'
         '.nf path{fill:none;stroke-linecap:round;stroke-linejoin:round}'
         '.n1 path{stroke:%s;stroke-width:{N1}px}.n2 path{stroke:%s;stroke-width:{N2}px}'
         '.nx path{fill:%s;stroke:%s;stroke-width:{NX}px}'
         '.ld{fill:none;stroke:#222;stroke-width:1.6}.ld.u{stroke:%s;stroke-width:2.4}'
         '.pt{fill:#111;stroke:#fff;stroke-width:2}.pt.u{fill:%s}') % (FT, FS, ROUGE, CERNE, JAUNE, JAUNE, CERNE, ROUGE, ROUGE)


def charger(nerf):
    a = yaml.safe_load(open(os.path.join(ROOT, 'nc', 'annot', nerf + '.yml'), encoding='utf-8'))
    s = yaml.safe_load(open(os.path.join(ROOT, 'nc', 'sources.yml'), encoding='utf-8'))
    p = yaml.safe_load(open(os.path.join(ROOT, 'nc', 'presets', nerf + '.yml'), encoding='utf-8'))
    return a, s, p


def groupes_trait(svg):
    return dict(re.findall(r'<g id="([a-z-]+)">(.*?)</g>', svg, re.S))


def larg(txt, fs=FS):
    return len(txt) * CAR * fs


def envelopper(txt, fs, w):
    n = max(10, int(w / (CAR * fs)))
    out, cur = [], ''
    for mot in txt.split():
        if cur and len(cur) + 1 + len(mot) > n:
            out.append(cur); cur = mot
        else:
            cur = (cur + ' ' + mot).strip()
    return out + ([cur] if cur else [])


def points_nerf(d_all):
    """Points (coordonnées de base) des chemins du nerf écrits par freestyle.py (M x y puis l dx dy relatifs)."""
    pts = []
    for d in re.findall(r' d="([^"]+)"', d_all):
        x = y = 0.0
        for cmd, nums in re.findall(r'([Ml])([^Ml]*)', d):
            v = [float(t) for t in re.findall(r'-?\d+(?:\.\d+)?', nums)]
            for k in range(0, len(v) - 1, 2):
                if cmd == 'M' and k == 0:
                    x, y = v[0], v[1]
                else:
                    x, y = x + v[k], y + v[k + 1]
                pts.append((x, y))
    return pts


def credit_lignes(vue):
    if vue == 'plan':
        return ['CC BY-SA 4.0, œuvre dérivée de Gray 1918', '(H. V. Carter, domaine public).']
    return ['CC BY-SA 4.0 · œuvre dérivée de Z-Anatomy,', 'BodyParts3D (DBCLS) et Univ. Dundee (CAHID).']


def credit_complet(vue):
    if vue == 'plan':
        return ('Œuvre dérivée, CC BY-SA 4.0. Trait vectorisé par automate (Dédale, 17.10.2026, tools/dedale/trace.py) '
                'depuis Gray788 (H. V. Carter, in H. Gray, Anatomy of the Human Body, 1918 ; domaine public, Wikimedia Commons).')
    return ('Œuvre dérivée, CC BY-SA 4.0. Trait rendu par automate (Dédale, 17.10.2026) depuis Z-Anatomy '
            '(G. Kervyn, M. Zielinski, CC BY-SA 4.0), d’après BodyParts3D (DBCLS, CC BY-SA 2.1 JP) '
            'et Cranial Nerves and Foramina (University of Dundee, CAHID, CC BY 4.0).')


# ---------------------------------------------------------------- placement des étiquettes
def inter(r1, r2, gap=0):
    return not (r1[0] + r1[2] + gap <= r2[0] or r2[0] + r2[2] + gap <= r1[0] or
                r1[1] + r1[3] + gap <= r2[1] or r2[1] + r2[3] + gap <= r1[1])


def proche(box, x, y):
    return (min(max(x, box[0]), box[0] + box[2]), min(max(y, box[1]), box[1] + box[3]))


def seg_rect(p, q, r):
    """Le segment pq traverse-t-il le rectangle r (échantillonnage fin, suffisant à cette échelle) ?"""
    for t in [i / 24 for i in range(1, 24)]:
        x, y = p[0] + (q[0] - p[0]) * t, p[1] + (q[1] - p[1]) * t
        if r[0] < x < r[0] + r[2] and r[1] < y < r[1] + r[3]:
            return True
    return False


def seg_seg(a, b, c, d):
    def o(p, q, r):
        return (q[0] - p[0]) * (r[1] - p[1]) - (q[1] - p[1]) * (r[0] - p[0])
    return o(a, b, c) * o(a, b, d) < 0 and o(c, d, a) * o(c, d, b) < 0


def candidats(l, labels, zone, interdits, cx, cy, evite=()):
    lignes = l['texte'].split(' | ')
    w, h = max(larg(t) for t in lignes) + 6, LBL_H * len(lignes)
    out_a = math.atan2(l['sy'] - cy, l['sx'] - cx)
    res = []
    for r in (36, 56, 80, 110, 145, 185, 230, 290, 360, 440):
        for k in range(32):
            ang = k * math.pi / 16
            ex, ey = l['sx'] + r * math.cos(ang), l['sy'] + r * math.sin(ang)
            c, sn = math.cos(ang), math.sin(ang)
            bx = ex + 6 if c > 0.35 else (ex - 6 - w if c < -0.35 else ex - w / 2)
            by = ey if sn > 0.35 else (ey - h if sn < -0.35 else ey - h / 2)
            box = (round(bx, 1), round(by, 1), round(w, 1), h)
            if bx < zone[0] + 6 or by < zone[1] + 6 or bx + w > zone[0] + zone[2] - 6 or by + h > zone[1] + zone[3] - 6:
                continue
            if any(inter(box, z, 6) for z in interdits):
                continue
            if any(box[0] - 10 < m['sx'] < box[0] + w + 10 and box[1] - 10 < m['sy'] < box[1] + h + 10 for m in labels):
                continue
            q = proche(box, l['sx'], l['sy'])
            if not l.get('encart') and any(seg_rect((l['sx'], l['sy']), q, z) for z in interdits):
                continue
            d_ang = abs((ang - out_a + math.pi) % (2 * math.pi) - math.pi)
            couvre = sum(1 for x, y in evite if box[0] < x < box[0] + w and box[1] < y < box[1] + h)
            res.append((round(r + 90 * d_ang / math.pi + 10 * abs(sn) + 3 * couvre, 3), k, box, q))
    res.sort(key=lambda t: (t[0], t[1]))
    par_dir, out = {}, []
    for t in res:               # au plus deux rayons par direction : couverture de tous les côtés
        if par_dir.get(t[1], 0) < 4:
            par_dir[t[1]] = par_dir.get(t[1], 0) + 1; out.append(t)
    return out


def conflit(l1, c1, l2, c2):
    b1, q1, b2, q2 = c1[2], c1[3], c2[2], c2[3]
    p1, p2 = (l1['sx'], l1['sy']), (l2['sx'], l2['sy'])
    return (inter(b1, b2, 8) or seg_rect(p1, q1, b2) or seg_rect(p2, q2, b1) or seg_seg(p1, q1, p2, q2))


def placer(labels, zone, interdits, evite=()):
    """Placement rejouable : pour chaque étiquette, candidats autour de l'ancre (rayon court d'abord, vers
    l'extérieur du groupe, en évitant de masquer le nerf) ; recherche locale à graine fixe sur une table de conflits
    (boîtes disjointes, aucun trait de rappel croisé ni traversant une boîte). Échec explicite sinon."""
    n = len(labels)
    if not n:
        return
    cx = sum(l['sx'] for l in labels) / n; cy = sum(l['sy'] for l in labels) / n
    C = [candidats(l, labels, zone, interdits, cx, cy, evite) for l in labels]
    for i, c in enumerate(C):
        if not c:
            sys.exit('ÉCHEC : aucune place pour l’étiquette « %s » (préréglage trop chargé).' % labels[i]['texte'])
    # recherche locale « conflits minimaux » à graine fixe (rejouable à l'octet) : plusieurs départs, on garde la
    # disposition valide de coût total minimal.
    rnd = random.Random(0)
    gagnant, cout_min = None, float('inf')
    # table des conflits entre candidats, calculée une fois (préfiltre : enveloppes boîte + trait de rappel disjointes)
    def env(l, c):
        b, q = c[2], c[3]
        return (min(b[0], l['sx']) - 8, min(b[1], l['sy']) - 8, max(b[0] + b[2], l['sx']) + 8, max(b[1] + b[3], l['sy']) + 8)
    EV = [[env(labels[i], c) for c in C[i]] for i in range(n)]
    X = {}
    for i in range(n):
        for j in range(i + 1, n):
            for ci, ei in enumerate(EV[i]):
                for cj, ej in enumerate(EV[j]):
                    if ei[0] < ej[2] and ej[0] < ei[2] and ei[1] < ej[3] and ej[1] < ei[3] \
                            and conflit(labels[i], C[i][ci], labels[j], C[j][cj]):
                        X[(i, ci, j, cj)] = X[(j, cj, i, ci)] = True
    def nconf(ch, i, ci):
        return sum(1 for j in range(n) if j != i and (i, ci, j, ch[j]) in X)
    for depart in range(300):
        ch = [0 if depart == 0 else rnd.randrange(min(len(C[i]), 6)) for i in range(n)]
        for it in range(1500):
            conf = [i for i in range(n) if nconf(ch, i, ch[i])]
            if not conf:
                break
            i = rnd.choice(conf)
            if rnd.random() < 0.1:
                ch[i] = rnd.randrange(len(C[i]))
            else:
                ch[i] = min(range(len(C[i])), key=lambda ci: (nconf(ch, i, ci), C[i][ci][0] + rnd.random()))
        else:
            continue
        cout = sum(C[i][ch[i]][0] for i in range(n))
        if cout < cout_min:
            gagnant, cout_min = list(ch), cout
    if gagnant is None:
        sys.exit('ÉCHEC : aucune disposition sans chevauchement (préréglage trop chargé).')
    # amélioration : chaque étiquette tente un candidat moins coûteux compatible
    for _ in range(3):
        for i in range(n):
            for ci in range(len(C[i])):
                if C[i][ci][0] >= C[i][gagnant[i]][0]:
                    break
                if not nconf(gagnant, i, ci):
                    gagnant[i] = ci; break
    best = [dict((i, C[i][gagnant[i]]) for i in range(n))]
    for i, c in best[0].items():
        labels[i]['box'], labels[i]['q'] = c[2], c[3]


# ---------------------------------------------------------------- composition d'un préréglage
def entree(a, ref):
    for couche, lst in (a.get('couches') or {}).items():
        for e in lst or []:
            if e.get('id') == ref:
                return couche, e
    sys.exit('ÉCHEC : référence %r absente de nc/annot (préréglage)' % ref)


def etiquettes(nerf, vue, nom_etat, E, a, anc, T, nerf_pts, retirer):
    labels = []
    for et in E['etiquettes']:
        if et['ref'] in retirer:
            continue
        couche_src, e = entree(a, et['ref'])
        an = et.get('ancre') or e.get('ancre')
        if an not in anc:
            sys.exit('ÉCHEC : ancre %r absente des données de la vue %s' % (an, vue))
        x, y = anc[an]
        if et.get('entre'):
            (xa, ya), (xb, yb) = anc[et['entre'][0]], anc[et['entre'][1]]
            x, y = (xa + xb) / 2, (ya + yb) / 2
        if et.get('accroche') == 'nerf' or et.get('entre'):
            x, y = min(nerf_pts, key=lambda p: (p[0] - x) ** 2 + (p[1] - y) ** 2)
        sx, sy = T(x, y)
        couche = et.get('couche') or {'legendes': 'legendes', 'noyaux': 'noyaux', 'foramens': 'foramens', 'lesions': 'lesions',
                                       'territoires': 'territoires', 'nerf': 'legendes'}[couche_src]
        labels.append({'ref': et['ref'], 'texte': et['texte'], 'sx': sx, 'sy': sy, 'couche': couche,
                       'urgence': bool(couche == 'lesions' and e.get('urgence')), 'source': e.get('source', '')})
    if len(labels) > MAX_ETIQ:
        sys.exit('ÉCHEC : état %s : %d étiquettes, %d au plus.' % (nom_etat, len(labels), MAX_ETIQ))
    return labels


def rendu_etiquette(l):
    b, q, u = l['box'], l['q'], ' u' if l['urgence'] else ''
    if q[0] >= b[0] + b[2] - 0.5:
        ta, tx = ' text-anchor="end"', b[0] + b[2] - 3
    elif q[0] <= b[0] + 0.5:
        ta, tx = '', b[0] + 3
    else:
        ta, tx = ' text-anchor="middle"', b[0] + b[2] / 2
    return ('<g class="lbl" data-ref="%s"><path class="ld%s" d="M%.1f %.1fL%.1f %.1f"/><circle class="pt%s" cx="%.1f" cy="%.1f" r="%s"/>'
            '<text class="lb%s"%s x="%.1f" y="%.1f">%s</text></g>'
            % (l['ref'], u, l['sx'], l['sy'], q[0], q[1], u, l['sx'], l['sy'], '8' if l['urgence'] else '5.5',
               u, ta, tx, b[1] + BASE, ''.join('<tspan x="%.1f" dy="%d">%s</tspan>' % (tx, 0 if n == 0 else LBL_H, escape(t))
                                              for n, t in enumerate(l['texte'].split(' | ')))))


def composer(nerf, vue, p, a):
    tdir = os.path.join(ROOT, 'nc', 'trait')
    G = groupes_trait(open(os.path.join(tdir, '%s-%s.svg' % (nerf, vue)), encoding='utf-8').read())
    meta = json.load(open(os.path.join(tdir, '%s-%s.json' % (nerf, vue)), encoding='utf-8'))
    anc = dict(meta['ancres'])
    M = groupes_trait(open(os.path.join(tdir, '%s-%s-masques.svg' % (nerf, vue)), encoding='utf-8').read())
    anc.update(json.load(open(os.path.join(tdir, '%s-%s-masques.json' % (nerf, vue)), encoding='utf-8'))['ancres'])
    CR = groupes_trait(open(os.path.join(tdir, '%s-%s-crane.svg' % (nerf, vue)), encoding='utf-8').read())
    x0, y0, S, _ = json.load(open(os.path.join(tdir, '%s-%s-crane.json' % (nerf, vue)), encoding='utf-8'))['cadre']
    k = W / S
    T = lambda x, y: (round((x - x0) * k, 1), round(HEAD + (y - y0) * k, 1))
    tr = 'matrix(%.6f 0 0 %.6f %.2f %.2f)' % (k, k, -x0 * k, HEAD - y0 * k)
    zone = (0, HEAD, W, W)
    nerf_pts = points_nerf(G.get('nerf', ''))
    evite = [T(x, y) for x, y in nerf_pts[::2]]
    retraits = (p.get('par_vue') or {}).get(vue, {}).get('retirer', {}) if p.get('par_vue') else {}
    defaut = p['etat_defaut']
    etats, groupes_lbl, legendes, toutes = {}, [], [], []
    fills = {}
    for nom, E in p['etats'].items():
        labels = etiquettes(nerf, vue, nom, E, a, anc, T, nerf_pts, retraits.get(nom, []))
        try:
            placer(labels, zone, [], evite)
        except SystemExit as ex:
            sys.exit('%s (vue %s, état %s)' % (ex, vue, nom))
        etats[nom] = list(E['couches'])
        cache = '' if nom == defaut else ' display="none"'
        par_couche = {}
        for l in labels:
            par_couche.setdefault(l['couche'], []).append(rendu_etiquette(l))
        for c in COUCHES:
            if c in par_couche:
                groupes_lbl.append('<g class="etiquettes" data-etat="%s" data-couche="%s"%s>%s</g>' % (nom, c, cache, ''.join(par_couche[c])))
        leg = [ln for t in E.get('legende', []) for ln in envelopper(t, FS, W - 48)]
        if len(leg) + 2 > MAX_LEG:
            sys.exit('ÉCHEC : état %s : légende de %d lignes, %d au plus.' % (nom, len(leg) + 2, MAX_LEG))
        legendes.append((nom, leg, cache))
        toutes.append((nom, E, labels))
        fills.update(E.get('remplissages') or {})
    nl = max(len(l) for _, l, _ in legendes) + 2
    y_leg = HEAD + W + 40
    H = y_leg + (nl - 1) * LH + 16
    bas = []
    for nom, leg, cache in legendes:
        bas.append('<g class="legende" data-etat="%s"%s>%s</g>' % (nom, cache, ''.join(
            '<text class="lg" x="24" y="%d">%s</text>' % (y_leg + n * LH, escape(t)) for n, t in enumerate(leg))))
    nleg = {nom: len(leg) for nom, leg, _ in legendes}
    # crédit court : sous la légende de l'état affiché ; une copie par état (position selon la longueur)
    for nom, leg, cache in legendes:
        bas.append('<g class="credit" data-etat="%s"%s>%s</g>' % (nom, cache, ''.join(
            '<text class="lg" x="24" y="%d">%s</text>' % (y_leg + (len(leg) + n) * LH, escape(t)) for n, t in enumerate(credit_lignes(vue)))))
    vis = lambda c: '' if c in etats[defaut] else ' display="none"'
    couches = {
        'territoires': '<g transform="%s">%s</g>' % (tr, ''.join('<g class="fl" fill="%s">%s</g>' % (col, M.get('m-' + g, ''))
                                                            for g, col in fills.items())),
        'trait': '<g transform="%s"><g class="cd">%s</g><g class="ct">%s</g><g class="cc">%s</g><g class="cs">%s</g></g>'
                 % (tr, CR.get('c-details', ''), CR.get('c-dents', ''), CR.get('c-contours', ''), CR.get('c-silhouette', '')),
        'nerf': '<g transform="%s" class="nf"><g class="n1">%s</g><g class="n2">%s</g></g>' % (tr, G.get('nerf', ''), G.get('nerf', '')),
        'noyaux': '<g transform="%s" class="nx">%s</g>' % (tr, CR.get('c-noyaux', '')),
    }
    titre = '%s · %s' % (p['titre'], NOMS_VUES[vue])
    desc = '%s. États : %s.' % (titre, ' ; '.join('%s (%s)' % (E['nom'], ', '.join(l['texte'].replace(' | ', ' ') for l in L))
                                                   for _, E, L in toutes))
    meta_txt = json.dumps({'licence': 'CC BY-SA 4.0', 'licence_url': 'https://creativecommons.org/licenses/by-sa/4.0/',
                           'mention': 'Œuvre dérivée', 'credit': credit_complet(vue),
                           'etats': {nom: [{'ref': l['ref'], 'texte': l['texte'], 'source': l['source']} for l in L] for nom, _, L in toutes},
                           'annotations': a.get('statut'), 'valide_par_vial': bool(a.get('valide_par_vial'))},
                          ensure_ascii=False, sort_keys=True)
    out = ['<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %d %d" role="img" aria-labelledby="t d" data-nerf="%s" data-vue="%s" '
           'data-etat="%s" data-etats="%s" data-zone="0 %d %d %d">' % (W, H, nerf, vue, defaut, escape(json.dumps(etats, separators=(',', ':')), {'"': '&quot;'}), HEAD, W, W),
           '<title id="t">%s</title><desc id="d">%s</desc><metadata>%s</metadata>' % (escape(titre), escape(desc), escape(meta_txt)),
           # épaisseurs du nerf en unités du dessin : 6,5 px de jaune et 1 px de cerne sur l'image de 800 px,
           # proportionnelles ensuite à la taille d'affichage
           '<style>%s</style>' % STYLE.replace('{N1}', '%.2f' % (8.5 / k)).replace('{N2}', '%.2f' % (6.5 / k)).replace('{NX}', '%.2f' % (1 / k)),
           '<rect width="%d" height="%d" fill="#fff"/>' % (W, H),
           '<text class="tt" x="24" y="44">%s</text>' % escape(titre),
           '<svg x="0" y="%d" width="%d" height="%d" viewBox="0 %d %d %d" overflow="hidden">' % (HEAD, W, W, HEAD, W, W)]
    for c in COUCHES:
        out.append('<g id="%s" data-couche="%s"%s>%s</g>' % (c, c, vis(c), couches.get(c, '')))
    out.append('</svg>')
    out += groupes_lbl
    out.append('<g id="legende-bas">%s</g></svg>\n' % ''.join(bas))
    return ''.join(out), toutes


def manifeste(nerf, p, res):
    m = {'nerf': nerf, 'note': ('Trois images (une par vue) ; chacune contient tous les états. Changer d’état : afficher '
                                '[data-etat="X"] et les couches data-etats[X] ([data-couche]), masquer le reste.'),
         'etat_defaut': p['etat_defaut'], 'vues': {}}
    for vue, (t, toutes) in res.items():
        m['vues'][vue] = {'fichier': '%s-%s.svg' % (nerf, vue),
                          'etats': {nom: {'nom': E['nom'], 'couches': E['couches'],
                                          'etiquettes': [{'ref': l['ref'], 'texte': l['texte']} for l in L]} for nom, E, L in toutes}}
    return json.dumps(m, ensure_ascii=False, indent=1) + '\n'


def svgo(txt):
    exe = shutil.which('svgo')
    if not exe:
        sys.exit('ÉCHEC : svgo 4.0.0 introuvable (npm i -g svgo@4.0.0).')
    v = subprocess.run([exe, '--version'], capture_output=True, text=True).stdout.strip()
    if v != '4.0.0':
        sys.exit('ÉCHEC : svgo %s au lieu de 4.0.0 (la sortie doit être rejouable à l’octet).' % v)
    with tempfile.TemporaryDirectory() as d:
        f = os.path.join(d, 'x.svg'); open(f, 'w', encoding='utf-8').write(txt)
        subprocess.run([exe, '--config', os.path.join(HERE, 'svgo.config.mjs'), '-q', '-i', f, '-o', f], check=True)
        return open(f, encoding='utf-8').read()


def credit_entree(nerf, vue, a, s, ko, fichier=None, titre=None, mods=None):
    z = s['z-anatomy']
    return {
        'fichier': fichier or '%s-%s.svg' % (nerf, vue),
        'nerf': nerf, 'vue': vue,
        'titre': titre or '%s · %s' % (a['titre'], NOMS_VUES.get(vue, vue)),
        'auteur': '%s ; d’après %s (%s) et %s (%s)' % (z['auteur'], s['bodyparts3d']['titre'], s['bodyparts3d']['auteur'],
                                                     s['dundee-cnf']['titre'], s['dundee-cnf']['auteur']),
        'source': 'Z-Anatomy (modèle 3D Blender)',
        'source_url': z['source_url'],
        'url': z['source_url'],
        'licence': 'CC BY-SA 4.0',
        'licence_derivee': 'CC BY-SA 4.0',
        'derive': True,
        'licence_url': z['licence_url'],
        'licences_amont': {'z-anatomy': z['licence'], 'bodyparts3d': s['bodyparts3d']['licence'], 'dundee-cnf': s['dundee-cnf']['licence']},
        'mention': 'Œuvre dérivée',
        'oeuvre_derivee': True,
        'modifications': mods or ('Rendu des contours par Freestyle (Blender 3.6.19, tools/dedale/freestyle.py) : peau en contour seul, '
                                  'crâne en transparence, tronc cérébral, muscles rattachés au nerf ; nerf projeté depuis les courbes du modèle ; '
                                  'annotations composées par tools/dedale/annoter.py depuis nc/annot/%s.yml ; svgo 4.0.0.' % nerf),
        'annotations': 'nc/annot/%s.yml (%s)' % (nerf, a.get('statut')),
        'verifie_le': DATE,
        'genere_par_ia': False,
        'contenu_verifie_visuellement': True,
        'valide_par_vial': bool(a.get('valide_par_vial')),
        'ko': ko,
    }


def ecrire_credits(entrees, retirer=()):
    p = os.path.join(OUT, 'credits.json')
    # Format commun avec tools/nc_svg_check.py (Janus) : liste d'entrées, « fichier » = nom dans assets/nc/.
    data = json.load(open(p, encoding='utf-8')) if os.path.exists(p) else []
    data = [e for e in data if e['fichier'] not in retirer]
    idx = {e['fichier']: i for i, e in enumerate(data)}
    for e in entrees:
        if e['fichier'] in idx:
            data[idx[e['fichier']]] = e
        else:
            data.append(e)
    data.sort(key=lambda e: e['fichier'])
    open(p, 'w', encoding='utf-8', newline='\n').write(json.dumps(data, ensure_ascii=False, indent=1) + '\n')



def construire(nerf):
    a, s, p = charger(nerf)
    res = {}
    for vue in p['vues']:
        txt, toutes = composer(nerf, vue, p, a)
        res[vue] = (svgo(txt), toutes)
    return a, s, p, res


def main():
    args = sys.argv[1:]
    nerf = next((x for x in args if not x.startswith('--')), 'nc07')
    a, s, p, res = construire(nerf)
    fichiers = {'%s-%s.svg' % (nerf, v): t for v, (t, _) in res.items()}
    fichiers['%s-presets.json' % nerf] = manifeste(nerf, p, res)
    if '--verifier' in args:
        bad = [f for f, t in fichiers.items()
               if not os.path.exists(os.path.join(OUT, f)) or open(os.path.join(OUT, f), encoding='utf-8').read() != t]
        for f in bad:
            print('ÉCHEC : assets/nc/%s diffère de sa recomposition.' % f)
        print('Recomposition à l’octet : %d/%d fichiers identiques.' % (len(fichiers) - len(bad), len(fichiers)))
        sys.exit(1 if bad else 0)
    os.makedirs(OUT, exist_ok=True)
    for f, t in fichiers.items():
        open(os.path.join(OUT, f), 'w', encoding='utf-8', newline='\n').write(t)
        print('assets/nc/%s : %d octets' % (f, len(t.encode())))
    ent = []
    for vue, (t, toutes) in res.items():
        ko = round(len(t.encode()) / 1024)
        e = credit_entree(nerf, vue, a, s, ko, titre='%s · %s' % (a['titre'], NOMS_VUES[vue]),
                          mods=('Crâne au crayon par Freestyle sur les os seuls, décimés (Blender 3.6.19, tools/dedale/crane.py : '
                                'silhouette épaisse, contours moyens, détails légers ; vectorisation potrace) ; nerf projeté depuis les '
                                'courbes du modèle (tools/dedale/freestyle.py), en jaune ; aplats des territoires (tools/dedale/masques.py) ; '
                                'états %s composés par tools/dedale/annoter.py depuis nc/presets/%s.yml et nc/annot/%s.yml ; svgo 4.0.0.')
                               % (', '.join(n for n, _, _ in toutes), nerf, nerf))
        e['etats'] = [n for n, _, _ in toutes]
        ent.append(e)
    # tout autre fichier publié de ce nerf (anciens préréglages, plan, tour) est retiré
    vieux = [f for f in os.listdir(OUT) if re.match(r'%s-[\w-]+\.(svg|webp|png)$' % nerf, f) and f not in fichiers]
    for f in vieux:
        os.remove(os.path.join(OUT, f)); print('retiré : assets/nc/%s' % f)
    ecrire_credits(ent, retirer=vieux)


if __name__ == '__main__':
    main()
