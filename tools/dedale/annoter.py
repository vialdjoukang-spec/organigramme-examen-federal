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
W, HEAD, FT = 800, 64, 32
FL, LL = 22, 28     # légende et crédit : petits caractères (22 px sur 800 px, soit 9,9 px à 360 px), interligne
CAR_LEG = 0.56      # largeur moyenne d'un caractère de la légende (mesurée dans Chromium : 0,53 au plus)
CAR = 0.60          # largeur moyenne d'un caractère en em (estimation prudente, contrôlée par verifier.py)
R_NUM, E_NUM, FN = 14, 2.2, 18   # repère numéroté : cercle de 14 px de rayon + trait de 2,2 px (30 px de diamètre hors
                                 # tout, 13,5 px à 360 px), numéro gras de 18 px
D_NERF = 8.5 / 2    # demi-épaisseur du nerf (cerne compris) sur l'image de 800 px
MARGE_NERF = 3      # jeu minimal entre un repère et le nerf
ECART = 14          # jeu minimal entre deux repères (aération)
MAX_ETIQ, MAX_NOTE = 8, 2
COL = (24, 412)     # abscisses des 2 colonnes de la légende
NOMS_VUES = {'face': 'vue de face', 'profil': 'vue de profil droit', '34': 'vue de trois quarts droite'}
COUCHES = ('territoires', 'trait', 'nerf', 'noyaux', 'foramens', 'lesions', 'legendes', 'legende')
STYLE = ('text{font-family:system-ui,-apple-system,"Segoe UI",Roboto,Arial,sans-serif;fill:#111}'
         '.tt{font-size:%dpx;font-weight:700}.lg{font-size:%dpx}.lg .n{font-weight:700}'
         '.cs path{fill:#222}.cc path{fill:#2b2b2b}.cd path{fill:#8a8a8a}.ct path{fill:#6b6b6b}.fl path{fill:inherit}'
         '.nf path{fill:none;stroke-linecap:round;stroke-linejoin:round}'
         '.n1 path{stroke:%s;stroke-width:{N1}px}.n2 path{stroke:%s;stroke-width:{N2}px}'
         '.nx path{fill:%s;stroke:%s;stroke-width:{NX}px}'
         '.nc-num{cursor:pointer}.nc-num:focus{outline:none}.nc-num:focus .cr,.nc-num:hover .cr{stroke-width:3.4px}'
         '.ld{fill:none;stroke:#222;stroke-width:1.4px}.ah{fill:#222}'
         '.cr{fill:#fff;stroke:#222;stroke-width:%.1fpx}.nm{font-size:%dpx;font-weight:700;text-anchor:middle}'
         '.ld.u{stroke:%s;stroke-width:2px}.ah.u{fill:%s}.cr.u{stroke:%s}.nm.u{fill:%s}'
         ) % (FT, FL, CERNE, JAUNE, JAUNE, CERNE, E_NUM, FN, ROUGE, ROUGE, ROUGE, ROUGE)


def charger(nerf):
    a = yaml.safe_load(open(os.path.join(ROOT, 'nc', 'annot', nerf + '.yml'), encoding='utf-8'))
    s = yaml.safe_load(open(os.path.join(ROOT, 'nc', 'sources.yml'), encoding='utf-8'))
    p = yaml.safe_load(open(os.path.join(ROOT, 'nc', 'presets', nerf + '.yml'), encoding='utf-8'))
    return a, s, p


def groupes_trait(svg):
    return dict(re.findall(r'<g id="([a-z-]+)">(.*?)</g>', svg, re.S))


def larg(txt, fs=FL):
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


def points_nerf(d_all, pas=None):
    """Points (coordonnées de base) des chemins du nerf écrits par freestyle.py (M x y puis l dx dy relatifs) ;
    avec « pas », chaque segment est densifié (un point tous les « pas » au plus)."""
    pts = []
    for d in re.findall(r' d="([^"]+)"', d_all):
        x = y = 0.0
        for cmd, nums in re.findall(r'([Ml])([^Ml]*)', d):
            v = [float(t) for t in re.findall(r'-?\d+(?:\.\d+)?', nums)]
            for k in range(0, len(v) - 1, 2):
                if cmd == 'M' and k == 0:
                    x, y = v[0], v[1]
                else:
                    nx, ny = x + v[k], y + v[k + 1]
                    if pas:
                        n = int(math.hypot(nx - x, ny - y) / pas)
                        pts += [(x + (nx - x) * i / (n + 1), y + (ny - y) * i / (n + 1)) for i in range(1, n + 1)]
                    x, y = nx, ny
                pts.append((x, y))
    return pts


def points_contours(svg_g, T):
    """Sommets (coordonnées de l'image) des chemins potrace d'un groupe (noyaux) : transform matrix(), puis M/L/C
    absolus ou relatifs ; T ramène les coordonnées de base à celles de l'image."""
    pts = []
    for att, d in re.findall(r'<path([^>]*?) d="([^"]+)"', svg_g):
        m = re.search(r'matrix\(([^)]+)\)', att)
        a_, b_, c_, d_, e_, f_ = [float(t) for t in m.group(1).split()] if m else (1, 0, 0, 1, 0, 0)
        x = y = 0.0
        for cmd, nums in re.findall(r'([MmLlCcZz])([^MmLlCcZz]*)', d):
            v = [float(t) for t in re.findall(r'-?\d+(?:\.\d+)?', nums)]
            st = 6 if cmd in 'Cc' else 2
            for k in range(0, len(v) - st + 1, st):
                ex, ey = v[k + st - 2], v[k + st - 1]
                x, y = (x + ex, y + ey) if (cmd.islower() and not (cmd == 'm' and k == 0 and not pts)) else (ex, ey)
                pts.append(T(a_ * x + c_ * y + e_, b_ * x + d_ * y + f_))
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


# ---------------------------------------------------------------- placement des repères numérotés
R_OUT = R_NUM + E_NUM / 2        # rayon hors tout d'un repère


def seg_seg(a, b, c, d):
    def o(p, q, r):
        return (q[0] - p[0]) * (r[1] - p[1]) - (q[1] - p[1]) * (r[0] - p[0])
    return o(a, b, c) * o(a, b, d) < 0 and o(c, d, a) * o(c, d, b) < 0


def d_seg(p, a, b):
    """Distance du point p au segment ab."""
    dx, dy = b[0] - a[0], b[1] - a[1]
    L = dx * dx + dy * dy
    t = 0 if not L else max(0, min(1, ((p[0] - a[0]) * dx + (p[1] - a[1]) * dy) / L))
    return math.hypot(p[0] - a[0] - t * dx, p[1] - a[1] - t * dy)


class Grille:
    """Index spatial des points à éviter (nerf densifié, contours des noyaux)."""
    def __init__(self, pts, pas=24):
        self.pas, self.g = pas, {}
        for x, y in pts:
            self.g.setdefault((int(x // pas), int(y // pas)), []).append((x, y))

    def proches(self, x, y, r):
        p = self.pas
        for i in range(int((x - r) // p), int((x + r) // p) + 1):
            for j in range(int((y - r) // p), int((y + r) // p) + 1):
                for q in self.g.get((i, j), ()):
                    if (q[0] - x) ** 2 + (q[1] - y) ** 2 < r * r:
                        yield q


def fleche(m, c):
    """Trait de rappel du bord du cercle vers la structure, pointe de flèche à 2 px de l'ancre."""
    ax, ay = m['sx'], m['sy']
    L = math.hypot(ax - c[0], ay - c[1])
    ux, uy = (ax - c[0]) / L, (ay - c[1]) / L
    p0 = (c[0] + ux * R_OUT, c[1] + uy * R_OUT)
    tip = (ax - ux * 2, ay - uy * 2)
    return p0, tip, (ux, uy)


def candidats(m, reperes, zone, G, cx, cy):
    out_a = math.atan2(m['sy'] - cy, m['sx'] - cx)
    res = []
    for r in (40, 50, 62, 76, 92, 112, 136, 165, 200):
        for k in range(36):
            ang = k * math.pi / 18
            c = (round(m['sx'] + r * math.cos(ang), 1), round(m['sy'] + r * math.sin(ang), 1))
            if not (zone[0] + R_OUT + 6 <= c[0] <= zone[0] + zone[2] - R_OUT - 6 and
                    zone[1] + R_OUT + 6 <= c[1] <= zone[1] + zone[3] - R_OUT - 6):
                continue
            if next(G.proches(c[0], c[1], R_OUT + D_NERF + MARGE_NERF + 1), None):
                continue                           # le repère ne couvre jamais le nerf ni un noyau
            if any(math.hypot(o['sx'] - c[0], o['sy'] - c[1]) < R_OUT + 8 for o in reperes):
                continue                           # ni la pointe d'une autre flèche
            p0, tip, _ = fleche(m, c)
            # le trait de rappel croise le nerf : permis (structure voisine du nerf), mais coûteux
            mx, my, rr = (p0[0] + tip[0]) / 2, (p0[1] + tip[1]) / 2, math.hypot(tip[0] - p0[0], tip[1] - p0[1]) / 2 + 4
            croise = sum(1 for q in G.proches(mx, my, rr) if d_seg(q, p0, tip) < 4 and math.hypot(q[0] - tip[0], q[1] - tip[1]) > 12)
            d_ang = abs((ang - out_a + math.pi) % (2 * math.pi) - math.pi)
            res.append((round(0.6 * r + 40 * d_ang / math.pi + 1.5 * croise, 3), k, c, p0, tip))
    res.sort(key=lambda t: (t[0], t[1]))
    par_dir, out = {}, []
    for t in res:                    # au plus 3 rayons par direction : couverture de tous les côtés
        if par_dir.get(t[1], 0) < 3:
            par_dir[t[1]] = par_dir.get(t[1], 0) + 1; out.append(t)
    return out


def conflit(c1, c2):
    a, b = c1[2], c2[2]
    if math.hypot(a[0] - b[0], a[1] - b[1]) < 2 * R_OUT + ECART:
        return True                                        # cercles trop proches
    if seg_seg(c1[3], c1[4], c2[3], c2[4]):
        return True                                        # flèches croisées
    return d_seg(b, c1[3], c1[4]) < R_OUT + 3 or d_seg(a, c2[3], c2[4]) < R_OUT + 3   # flèche sous un cercle


def repulsion(a, b):
    d = math.hypot(a[0] - b[0], a[1] - b[1])
    return max(0.0, 180 - d) * 1.4


def placer(reperes, zone, G):
    """Placement rejouable : candidats autour de l'ancre (court d'abord, vers l'extérieur du groupe, jamais sur le
    nerf) ; recherche locale à graine fixe sur une table de conflits (cercles disjoints et aérés, flèches non
    croisées, aucune flèche sous un cercle), puis aération : chaque repère s'éloigne des autres si cela ne crée
    aucun conflit. Échec explicite sinon."""
    n = len(reperes)
    if not n:
        return
    cx = sum(m['sx'] for m in reperes) / n; cy = sum(m['sy'] for m in reperes) / n
    C = [candidats(m, reperes, zone, G, cx, cy) for m in reperes]
    for i, c in enumerate(C):
        if not c:
            sys.exit('ÉCHEC : aucune place pour le repère %d « %s » (état trop chargé).' % (reperes[i]['num'], reperes[i]['nom']))
    def env(c):
        xs = (c[2][0], c[4][0]); ys = (c[2][1], c[4][1])
        g = R_OUT + ECART / 2 + 4
        return (min(xs) - g, min(ys) - g, max(xs) + g, max(ys) + g)
    EV = [[env(c) for c in C[i]] for i in range(n)]
    X = set()
    for i in range(n):
        for j in range(i + 1, n):
            for ci, ei in enumerate(EV[i]):
                for cj, ej in enumerate(EV[j]):
                    if ei[0] < ej[2] and ej[0] < ei[2] and ei[1] < ej[3] and ej[1] < ei[3] and conflit(C[i][ci], C[j][cj]):
                        X.add((i, ci, j, cj)); X.add((j, cj, i, ci))
    def nconf(ch, i, ci):
        return sum(1 for j in range(n) if j != i and (i, ci, j, ch[j]) in X)
    def cout_total(ch):
        return sum(C[i][ch[i]][0] for i in range(n)) + sum(repulsion(C[i][ch[i]][2], C[j][ch[j]][2])
                                                           for i in range(n) for j in range(i + 1, n))
    rnd = random.Random(0)
    gagnant, cout_min = None, float('inf')
    for depart in range(200):
        ch = [0 if depart == 0 else rnd.randrange(min(len(C[i]), 8)) for i in range(n)]
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
        # aération : descente sur coût propre + répulsion, sans jamais créer de conflit
        for _ in range(6):
            bouge = False
            for i in range(n):
                def local(ci):
                    return C[i][ci][0] + sum(repulsion(C[i][ci][2], C[j][ch[j]][2]) for j in range(n) if j != i)
                best = min((ci for ci in range(len(C[i])) if not nconf(ch, i, ci)), key=lambda ci: (local(ci), ci))
                if local(best) < local(ch[i]) - 1e-9:
                    ch[i] = best; bouge = True
            if not bouge:
                break
        cout = cout_total(ch)
        if cout < cout_min - 1e-9:
            gagnant, cout_min = list(ch), cout
    if gagnant is None:
        sys.exit('ÉCHEC : aucune disposition sans chevauchement (état trop chargé).')
    for i in range(n):
        c = C[i][gagnant[i]]
        reperes[i]['c'], reperes[i]['p0'], reperes[i]['tip'] = c[2], c[3], c[4]


# ---------------------------------------------------------------- composition d'un préréglage
def entree(a, ref):
    for couche, lst in (a.get('couches') or {}).items():
        for e in lst or []:
            if e.get('id') == ref:
                return couche, e
    sys.exit('ÉCHEC : référence %r absente de nc/annot (préréglage)' % ref)


def reperes_etat(nerf, vue, nom_etat, E, a, anc, T, nerf_pts, retirer):
    """Repères d'un état : numéro = rang dans la liste de l'état (identique dans les 3 vues)."""
    if len(E['etiquettes']) > MAX_ETIQ:
        sys.exit('ÉCHEC : état %s : %d repères, %d au plus.' % (nom_etat, len(E['etiquettes']), MAX_ETIQ))
    out = []
    for num, et in enumerate(E['etiquettes'], 1):
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
        out.append({'num': num, 'ref': et['ref'], 'nom': et['nom'], 'glo': et.get('glo'), 'sx': sx, 'sy': sy, 'couche': couche,
                    'urgence': bool(couche == 'lesions' and e.get('urgence')), 'source': e.get('source', '')})
    return out


def rendu_repere(m):
    u = ' u' if m['urgence'] else ''
    (cx, cy), p0, tip = m['c'], m['p0'], m['tip']
    ux, uy = (tip[0] - p0[0]), (tip[1] - p0[1])
    L = math.hypot(ux, uy) or 1
    ux, uy = ux / L, uy / L
    bx, by = tip[0] - ux * 8, tip[1] - uy * 8              # base de la pointe (8 px de long, 7 px de large)
    glo = ' data-glo="%s"' % escape(m['glo']) if m.get('glo') else ''
    return ('<g class="nc-num" data-num="%d" data-nom="%s"%s data-ref="%s" tabindex="0" role="button" aria-label="%d · %s">'
            '<path class="ld%s" d="M%.1f %.1fL%.1f %.1f"/>'
            '<path class="ah%s" d="M%.1f %.1fL%.1f %.1fL%.1f %.1fz"/>'
            '<circle class="cr%s" cx="%.1f" cy="%.1f" r="%d"/><text class="nm%s" x="%.1f" y="%.1f">%d</text></g>'
            % (m['num'], escape(m['nom'], {'"': '&quot;'}), glo, m['ref'], m['num'], escape(m['nom'], {'"': '&quot;'}),
               u, p0[0], p0[1], bx, by,
               u, tip[0], tip[1], bx - uy * 3.5, by + ux * 3.5, bx + uy * 3.5, by - ux * 3.5,
               u, cx, cy, R_NUM, u, cx, cy + 6.3, m['num']))


def lignes_legende(E, reperes):
    """Légende numérotée en 2 colonnes (ordre des numéros, colonne de gauche d'abord), puis notes pleine largeur.
    Renvoie [(x, rang, num ou None, texte)] et le nombre de rangs."""
    n_col = int((COL[1] - COL[0] - 12) / (CAR_LEG * FL))
    ent = []
    for m in reperes:
        lig = envelopper(m['nom'], FL, (n_col - 4) * CAR * FL)
        ent.append((m['num'], lig))
    moitie = (len(ent) + 1) // 2
    out, rangs = [], [0, 0]
    for k, (num, lig) in enumerate(ent):
        c = 0 if k < moitie else 1
        for j, t in enumerate(lig):
            out.append((COL[c] + (0 if j == 0 else 22), rangs[c], num if j == 0 else None, t))
            rangs[c] += 1
    r = max(rangs)
    notes = [ln for t in E.get('legende', []) for ln in envelopper(t, FL, (W - 48) * CAR / CAR_LEG)]
    if len(notes) > MAX_NOTE:
        sys.exit('ÉCHEC : note de légende de %d lignes, %d au plus.' % (len(notes), MAX_NOTE))
    for t in notes:
        out.append((COL[0], r, None, t)); r += 1
    return out, r


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
    obst = [T(x, y) for x, y in points_nerf(G.get('nerf', ''), pas=1.5 / k)] + points_contours(CR.get('c-noyaux', ''), T)
    grille = Grille(obst)
    retraits = (p.get('par_vue') or {}).get(vue, {}).get('retirer', {}) if p.get('par_vue') else {}
    defaut = p['etat_defaut']
    etats, groupes_num, legendes, toutes = {}, [], [], []
    fills = {}
    for nom, E in p['etats'].items():
        reperes = reperes_etat(nerf, vue, nom, E, a, anc, T, nerf_pts, retraits.get(nom, []))
        try:
            placer(reperes, zone, grille)
        except SystemExit as ex:
            sys.exit('%s (vue %s, état %s)' % (ex, vue, nom))
        etats[nom] = list(E['couches'])
        cache = '' if nom == defaut else ' display="none"'
        par_couche = {}
        for m in reperes:
            par_couche.setdefault(m['couche'], []).append(rendu_repere(m))
        for c in COUCHES:
            if c in par_couche:
                groupes_num.append('<g class="numeros" data-etat="%s" data-couche="%s"%s>%s</g>' % (nom, c, cache, ''.join(par_couche[c])))
        legendes.append((nom, lignes_legende(E, reperes), cache))
        toutes.append((nom, E, reperes))
        fills.update(E.get('remplissages') or {})
    y_leg = HEAD + W + 34
    nl = max(r for _, (_, r), _ in legendes)
    y_cred = y_leg + nl * LL + 12
    H = int(y_cred + LL + 12)
    leg = []
    for nom, (lignes, _), cache in legendes:
        leg.append('<g class="legende" data-etat="%s"%s>%s</g>' % (nom, cache, ''.join(
            ('<text class="lg" x="%d" y="%d"><tspan class="n">%d</tspan> · %s</text>' % (x, y_leg + r * LL, num, escape(t))) if num
            else '<text class="lg" x="%d" y="%d">%s</text>' % (x, y_leg + r * LL, escape(t)) for x, r, num, t in lignes)))
    cred = ''.join('<text class="lg" x="24" y="%d">%s</text>' % (y_cred + n * LL, escape(t))
                   for n, t in enumerate(credit_lignes(vue)))
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
    desc = '%s. États : %s.' % (titre, ' ; '.join('%s (%s)' % (E['nom'], ', '.join('%d %s' % (m['num'], m['nom']) for m in L))
                                                   for _, E, L in toutes))
    meta_txt = json.dumps({'licence': 'CC BY-SA 4.0', 'licence_url': 'https://creativecommons.org/licenses/by-sa/4.0/',
                           'mention': 'Œuvre dérivée', 'credit': credit_complet(vue),
                           'etats': {nom: [{'num': m['num'], 'ref': m['ref'], 'nom': m['nom'], 'source': m['source']} for m in L]
                                     for nom, _, L in toutes},
                           'annotations': a.get('statut'), 'valide_par_vial': bool(a.get('valide_par_vial'))},
                          ensure_ascii=False, sort_keys=True)
    out = ['<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %d %d" role="img" aria-labelledby="t d" data-nerf="%s" data-vue="%s" '
           'data-etat="%s" data-etats="%s" data-zone="0 %d %d %d">' % (W, H, nerf, vue, defaut, escape(json.dumps(etats, separators=(',', ':')), {'"': '&quot;'}), HEAD, W, W),
           '<title id="t">%s</title><desc id="d">%s</desc><metadata>%s</metadata>' % (escape(titre), escape(desc), escape(meta_txt)),
           # épaisseurs du nerf en px de l'image de 800 px (6,5 px de jaune, 1 px de cerne de chaque côté) : svgo
           # applique les transformations aux chemins du nerf et des noyaux (contrôlé dans svgo()), et la feuille de
           # style l'emporte sur l'attribut stroke-width qu'il ajoute ; proportionnelles ensuite à l'affichage
           '<style>%s</style>' % STYLE.replace('{N1}', '%.1f' % (2 * D_NERF)).replace('{N2}', '6.5').replace('{NX}', '1'),
           '<rect width="%d" height="%d" fill="#fff"/>' % (W, H),
           '<text class="tt" x="24" y="44">%s</text>' % escape(titre),
           '<svg x="0" y="%d" width="%d" height="%d" viewBox="0 %d %d %d" overflow="hidden">' % (HEAD, W, W, HEAD, W, W)]
    for c in COUCHES[:-1]:
        out.append('<g id="%s" data-couche="%s"%s>%s</g>' % (c, c, vis(c), couches.get(c, '')))
    out.append('</svg>')
    out += groupes_num
    out.append('<g id="legende" data-couche="legende"%s>%s</g>' % (vis('legende'), ''.join(leg)))
    out.append('<g id="credit">%s</g></svg>\n' % cred)
    return ''.join(out), toutes


def manifeste(nerf, p, res):
    m = {'nerf': nerf, 'note': ('Trois images (une par vue) ; chacune contient tous les états. Changer d’état : afficher '
                                '[data-etat="X"] et les couches data-etats[X] ([data-couche]), masquer le reste. Repères : '
                                'g.nc-num (data-num, data-nom, data-glo) ; légende : g#legende, masquable.'),
         'etat_defaut': p['etat_defaut'], 'vues': {}}
    for vue, (t, toutes) in res.items():
        m['vues'][vue] = {'fichier': '%s-%s.svg' % (nerf, vue),
                          'etats': {nom: {'nom': E['nom'], 'couches': E['couches'],
                                          'reperes': [dict({'num': m['num'], 'ref': m['ref'], 'nom': m['nom']},
                                                           **({'glo': m['glo']} if m.get('glo') else {})) for m in L]}
                                    for nom, E, L in toutes}}
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
        out = open(f, encoding='utf-8').read()
    for gid in ('nerf', 'noyaux'):
        i = out.find('id="%s"' % gid)
        if 'transform=' in out[i:out.find('</g></g>', i)]:
            sys.exit('ÉCHEC : svgo n’a pas appliqué la transformation au groupe %s (épaisseurs fausses).' % gid)
    return out


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
                                'états %s (repères numérotés fléchés, légende en 2 colonnes) composés par tools/dedale/annoter.py depuis nc/presets/%s.yml et nc/annot/%s.yml ; svgo 4.0.0.')
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
