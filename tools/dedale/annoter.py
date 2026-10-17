#!/usr/bin/env python3
"""Dédale-A · composition des schémas annotés par PRÉRÉGLAGES (une image = une idée).

INSTRUCTIONS (automate, zéro jeton) ------------------------------------------------
    python3 tools/dedale/annoter.py nc07            # compose assets/nc/nc07-<préréglage>.svg et nc07-presets.json
    python3 tools/dedale/annoter.py nc07 --verifier # recompose en mémoire et compare à l'octet (CI)
    python3 tools/dedale/annoter.py nc07 --tour     # sprite WebP des 8 vues (local : Chromium requis)
Entrées : nc/presets/<nerf>.yml (préréglages : vue de base, cadrage, encart, couches visibles, 8 étiquettes
          au plus, légende courte), nc/annot/<nerf>.yml (annotations sourcées d'Ariane : chaque étiquette y
          renvoie par « ref »), nc/trait/<nerf>-<vue>.svg/.json (trait et ancres de freestyle.py),
          nc/trait/<nerf>-<vue>-masques.svg/.json (aplats de masques.py), nc/sources.yml (crédits).
Sortie  : assets/nc/<nerf>-<préréglage>.svg : les 7 couches (trait, territoires, nerf, noyaux, foramens,
          lesions, legendes) sont toujours présentes ; celles du préréglage sont visibles (data-couches),
          les autres masquées (display="none") ; Hermès bascule une couche par [data-couche="…"], ce qui
          agit aussi sur l'encart. assets/nc/<nerf>-presets.json décrit les préréglages pour l'application.
Mise en page : titre ; zone de dessin carrée de 800 px (au moins 60 % de l'image) recadrée sur les ancres
          du préréglage, trait d'épaisseur constante (vector-effect) ; encart de la tête entière si demandé ;
          étiquettes de 30 px (13,5 px à 360 px de large) posées à côté de leur structure par un placement
          glouton déterministe (aucun chevauchement, aucun trait de rappel croisé) ; légende et crédit
          courts : 4 lignes au plus. Le crédit complet reste dans <metadata> et assets/nc/credits.json.
Règles  : aucune position saisie à la main ; le nerf en vert foncé (#156534) ; aplats pâles seulement pour
          les territoires ; le rouge (#b91c1c) seulement pour un site lésionnel « urgence: true ».
"""
import json, math, os, random, re, shutil, subprocess, sys, tempfile
from xml.sax.saxutils import escape
import yaml

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
HERE = os.path.join(ROOT, 'tools', 'dedale')
OUT = os.path.join(ROOT, 'assets', 'nc')
RENDER = os.environ.get('DEDALE_RENDER', '/workspace/ssp/nc_src/render')
DATE = '2026-10-17'
VERT, ROUGE = '#156534', '#b91c1c'
W, HEAD, FS, FT, LH = 800, 64, 30, 32, 38
CAR = 0.60          # largeur moyenne d'un caractère en em (estimation prudente, contrôlée par verifier.py)
LBL_H = 36          # hauteur d'une boîte d'étiquette (30 px + interligne)
BASE = 26           # ligne de base dans la boîte
MAX_ETIQ, MAX_LEG = 8, 4
NOMS_VUES = {'plan': 'plan du nerf (d’après Gray 1918)', 'face': 'vue de face', 'profil': 'vue de profil droit',
             '34': 'vue de trois quarts droite'}
COUCHES = ('territoires', 'trait', 'nerf', 'noyaux', 'foramens', 'lesions', 'legendes')
STYLE = ('text{font-family:system-ui,-apple-system,"Segoe UI",Roboto,Arial,sans-serif;fill:#111}'
         '.tt{font-size:%dpx;font-weight:700}.lb,.lg{font-size:%dpx}'
         '.lb{paint-order:stroke;stroke:#fff;stroke-width:7px;stroke-linejoin:round}'
         '.lb.u{fill:%s;font-weight:700}'
         'path{fill:none;stroke-linecap:round;stroke-linejoin:round;vector-effect:non-scaling-stroke}'
         '.peau path{stroke:#2f2f2f;stroke-width:1.6}.crane path{stroke:#6b6b6b;stroke-width:.9;stroke-opacity:.55}'
         '.tronc path{stroke:#555;stroke-width:1;stroke-opacity:.75}.terr path{stroke:#9a9a9a;stroke-width:.8}'
         '.nerf path{stroke:%s;stroke-width:3.4}.pl{fill:#2f2f2f;stroke:none}.fl path{fill:inherit;stroke:none}'
         '.ld{stroke:#222;stroke-width:1.6}.ld.u{stroke:%s;stroke-width:2.4}'
         '.pt{fill:#111;stroke:#fff;stroke-width:2}.pt.u{fill:%s}'
         '.cad{fill:none;stroke:#555;stroke-width:2}.enc{fill:#fff;stroke:#555;stroke-width:2}') % (FT, FS, ROUGE, VERT, ROUGE, ROUGE)
STYLE_TOUR = ('text{font-family:system-ui,-apple-system,"Segoe UI",Roboto,Arial,sans-serif;fill:#111}'
         '.tt{font-size:30px;font-weight:700}.lg{font-size:%dpx}.cr{font-size:%dpx;fill:#333}.b{font-weight:700}'
         '.nb{font-size:21px;font-weight:700;text-anchor:middle;dominant-baseline:central}'
         'path{fill:none;stroke-linecap:round;stroke-linejoin:round}'
         '#trait .peau path{stroke:#2f2f2f;stroke-width:1.5}'
         '#trait .crane path{stroke:#6b6b6b;stroke-width:.8;stroke-opacity:.5}'
         '#trait .tronc path{stroke:#555;stroke-width:.9;stroke-opacity:.75}'
         '#territoires path{stroke:#9a9a9a;stroke-width:.7;stroke-opacity:.8}'
         '#nerf path{stroke:%s;stroke-width:2.8}'
         '.ld{stroke:#555;stroke-width:1}.bd{fill:#fff;stroke:#111;stroke-width:1.6}'
         '#trait .pl{fill:#2f2f2f;stroke:none}.pt{fill:#111;stroke:#fff;stroke-width:1.5}.pr{fill:#fff;stroke:#111;stroke-width:2}') % (22, 20, VERT)




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
    for r in (36, 56, 80, 110, 145, 185, 230):
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
        if par_dir.get(t[1], 0) < 2:
            par_dir[t[1]] = par_dir.get(t[1], 0) + 1; out.append(t)
    return out


def conflit(l1, c1, l2, c2):
    b1, q1, b2, q2 = c1[2], c1[3], c2[2], c2[3]
    p1, p2 = (l1['sx'], l1['sy']), (l2['sx'], l2['sy'])
    return (inter(b1, b2, 8) or seg_rect(p1, q1, b2) or seg_rect(p2, q2, b1) or seg_seg(p1, q1, p2, q2))


def placer(labels, zone, interdits, evite=()):
    """Placement déterministe : pour chaque étiquette, candidats autour de l'ancre (rayon court d'abord, vers
    l'extérieur du groupe) ; recherche en profondeur avec élagage du meilleur coût total, sans chevauchement de
    boîtes ni croisement de traits de rappel. Échec explicite si aucune combinaison ne convient."""
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
    def nconf(ch, i, ci):
        return sum(1 for j in range(n) if j != i and conflit(labels[i], C[i][ci], labels[j], C[j][ch[j]]))
    for depart in range(40):
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


def composer(nerf, nom, P, a):
    vue = P['vue']
    tdir = os.path.join(ROOT, 'nc', 'trait')
    G = groupes_trait(open(os.path.join(tdir, '%s-%s.svg' % (nerf, vue)), encoding='utf-8').read())
    meta = json.load(open(os.path.join(tdir, '%s-%s.json' % (nerf, vue)), encoding='utf-8'))
    anc = dict(meta.get('ancres', {}))
    fm = os.path.join(tdir, '%s-%s-masques' % (nerf, vue))
    M = {}
    if os.path.exists(fm + '.svg'):
        M = groupes_trait(open(fm + '.svg', encoding='utf-8').read())
        anc.update(json.load(open(fm + '.json', encoding='utf-8'))['ancres'])
    couches = list(P['couches'])
    # zone de dessin et transformation (base -> écran)
    if vue == 'plan':
        pw, ph = meta['taille']; k = W / pw; DH = round(ph * k); x0 = y0 = 0.0
    else:
        DH = W
        pts = [anc[n] for n in P['cadre']['ancres']]
        bx0, bx1 = min(p[0] for p in pts), max(p[0] for p in pts)
        by0, by1 = min(p[1] for p in pts), max(p[1] for p in pts)
        S = max(bx1 - bx0, by1 - by0, 40) * (1 + 2 * P['cadre'].get('marge', 0.2))
        S = min(S, W)
        x0, y0 = (bx0 + bx1) / 2 - S / 2, (by0 + by1) / 2 - S / 2
        k = W / S
    zone = (0, HEAD, W, DH)
    T = lambda x, y: (round((x - x0) * k, 1), round(HEAD + (y - y0) * k, 1))
    tr_main = 'matrix(%.6f 0 0 %.6f %.2f %.2f)' % (k, k, -x0 * k, HEAD - y0 * k)
    enc = P.get('encart')
    E = None
    if enc:
        t, pos = enc['taille'], enc.get('position', 'hg')
        ex = 12 if pos[1] == 'g' else W - 12 - t
        ey = HEAD + 12 if pos[0] == 'h' else HEAD + DH - 12 - t
        E = (ex, ey, t, t); ke = t / W
        TE = lambda x, y: (round(ex + x * ke, 1), round(ey + y * ke, 1))
    # étiquettes
    nerf_pts = points_nerf(G.get('nerf', ''))
    labels = []
    if len(P['etiquettes']) > MAX_ETIQ:
        sys.exit('ÉCHEC : préréglage %s : %d étiquettes, 8 au plus.' % (nom, len(P['etiquettes'])))
    for et in P['etiquettes']:
        couche_src, e = entree(a, et['ref'])
        an = et.get('ancre') or e.get('ancre')
        if an not in anc:
            sys.exit('ÉCHEC : ancre %r absente des données de la vue %s' % (an, vue))
        x, y = anc[an]
        if et.get('entre'):   # milieu d'un segment : entre deux repères, ramené sur le nerf
            (xa, ya), (xb, yb) = anc[et['entre'][0]], anc[et['entre'][1]]
            x, y = (xa + xb) / 2, (ya + yb) / 2
        if et.get('accroche') == 'nerf' or et.get('entre'):
            x, y = min(nerf_pts, key=lambda p: (p[0] - x) ** 2 + (p[1] - y) ** 2)
        sx, sy = TE(x, y) if et.get('espace') == 'encart' else T(x, y)
        couche = et.get('couche') or {'legendes': 'legendes', 'noyaux': 'noyaux', 'foramens': 'foramens', 'lesions': 'lesions',
                                       'territoires': 'territoires', 'nerf': 'legendes'}[couche_src]
        labels.append({'ref': et['ref'], 'texte': et['texte'], 'sx': sx, 'sy': sy, 'couche': couche,
                       'encart': et.get('espace') == 'encart',
                       'urgence': bool(couche == 'lesions' and e.get('urgence')), 'source': e.get('source', '')})
    evite = [T(x, y) for x, y in nerf_pts[::2]] if vue != 'plan' else []   # le texte évite de masquer le nerf
    placer(labels, zone, [E] if E else [], evite)
    # couches
    defs = ['<clipPath id="zone"><rect x="0" y="%d" width="%d" height="%d"/></clipPath>' % (HEAD, W, DH)]
    if vue == 'plan':
        defs.append('<g id="d-trait">%s</g>' % G.get('peau', '').replace('<path ', '<path class="pl" '))
    else:
        defs.append('<g id="d-trait">%s</g>' % ''.join('<g class="%s">%s</g>' % (c, G.get(c, '')) for c in ('crane', 'tronc', 'peau')))
        defs.append('<g id="d-terr"><g class="terr">%s</g>%s</g>' % (G.get('territoires', ''),
                    ''.join('<g class="fl" fill="%s">%s</g>' % (col, M.get('m-' + g, ''))
                            for g, col in (P.get('remplissages') or {}).items())))
        defs.append('<g id="d-nerf"><g class="nerf">%s</g></g>' % G.get('nerf', ''))
    src = {'trait': 'd-trait', 'territoires': 'd-terr', 'nerf': 'd-nerf'}
    corps = {c: [] for c in COUCHES}
    for c, ref in src.items():
        if vue == 'plan' and c != 'trait':
            continue
        corps[c].append('<use href="#%s" transform="%s"/>' % (ref, tr_main))
    for l in labels:
        b, q, u = l['box'], l['q'], ' u' if l['urgence'] else ''
        # texte calé du côté du trait de rappel : le trait touche toujours le texte, quelle que soit la police
        if q[0] >= b[0] + b[2] - 0.5:
            ta, tx = ' text-anchor="end"', b[0] + b[2] - 3
        elif q[0] <= b[0] + 0.5:
            ta, tx = '', b[0] + 3
        else:
            ta, tx = ' text-anchor="middle"', b[0] + b[2] / 2
        corps[l['couche']].append(
            '<g class="lbl" data-ref="%s"><path class="ld%s" d="M%.1f %.1fL%.1f %.1f"/><circle class="pt%s" cx="%.1f" cy="%.1f" r="%s"/>'
            '<text class="lb%s"%s x="%.1f" y="%.1f">%s</text></g>'
            % (l['ref'], u, l['sx'], l['sy'], q[0], q[1], u, l['sx'], l['sy'], '8' if l['urgence'] else '5.5',
               u, ta, tx, b[1] + BASE, ''.join('<tspan x="%.1f" dy="%d">%s</tspan>' % (tx, 0 if n == 0 else LBL_H, escape(t))
                                                 for n, t in enumerate(l['texte'].split(' | ')))))
    # encart (tête entière, cadre du zoom)
    encart = ''
    if E:
        ex, ey, t, _ = E
        inner = ''.join('<g data-couche="%s"%s><use href="#%s"/></g>' % (c, '' if c in couches else ' display="none"', ref)
                        for c, ref in src.items())
        cadre = '<rect class="cad" x="%.1f" y="%.1f" width="%.1f" height="%.1f"/>' % (x0, y0, W / k, W / k)
        encart = ('<g class="encart"><rect class="enc" x="%.1f" y="%.1f" width="%d" height="%d"/>'
                  '<svg x="%.1f" y="%.1f" width="%d" height="%d" viewBox="0 0 %d %d">%s%s</svg></g>'
                  % (ex, ey, t, t, ex, ey, t, t, W, W, inner, cadre))
    # légende + crédit (4 lignes au plus)
    leg = [ln for t in P.get('legende', []) for ln in envelopper(t, FS, W - 48)]
    cred = credit_lignes(vue)
    if len(leg) + len(cred) > MAX_LEG:
        sys.exit('ÉCHEC : préréglage %s : légende de %d lignes, %d au plus.' % (nom, len(leg) + len(cred), MAX_LEG))
    y = HEAD + DH + 40
    bas = []
    for ln in leg + cred:
        bas.append('<text class="lg" x="24" y="%d">%s</text>' % (y, escape(ln))); y += LH
    H = y - LH + 16
    titre = P['titre']
    desc = '%s, %s. %s' % (titre, NOMS_VUES[vue], ' '.join(l['texte'].replace(' | ', ' ') + '.' for l in labels))
    meta_txt = json.dumps({'licence': 'CC BY-SA 4.0', 'licence_url': 'https://creativecommons.org/licenses/by-sa/4.0/',
                           'mention': 'Œuvre dérivée', 'credit': credit_complet(vue),
                           'etiquettes': [{'ref': l['ref'], 'texte': l['texte'], 'source': l['source']} for l in labels],
                           'annotations': a.get('statut'), 'valide_par_vial': bool(a.get('valide_par_vial'))},
                          ensure_ascii=False, sort_keys=True)
    out = ['<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %d %d" role="img" aria-labelledby="t d" data-nerf="%s" '
           'data-preset="%s" data-vue="%s" data-couches="%s" data-zone="0 %d %d %d">' % (W, H, nerf, nom, vue, ' '.join(couches), HEAD, W, DH),
           '<title id="t">%s</title><desc id="d">%s</desc><metadata>%s</metadata>' % (escape(titre), escape(desc), escape(meta_txt)),
           '<style>%s</style><defs>%s</defs>' % (STYLE, ''.join(defs)),
           '<rect width="%d" height="%d" fill="#fff"/>' % (W, H),
           '<text class="tt" x="24" y="44">%s</text>' % escape(titre)]
    for c in COUCHES:
        if c == 'lesions' and encart:
            pass
        vis = '' if c in couches else ' display="none"'
        clip = ' clip-path="url(#zone)"' if c in src else ''
        out.append('<g id="%s" data-couche="%s"%s%s>%s</g>' % (c, c, vis, clip, ''.join(x for x in corps[c] if x.startswith('<use'))))
    out.append(encart)
    for c in COUCHES:   # étiquettes au-dessus de l'encart, rangées dans leur couche
        lab = ''.join(x for x in corps[c] if not x.startswith('<use'))
        if lab:
            vis = '' if c in couches else ' display="none"'
            out.append('<g class="etiquettes" data-couche="%s"%s>%s</g>' % (c, vis, lab))
    out.append('<g id="legende-bas">%s</g></svg>\n' % ''.join(bas))
    return ''.join(out), labels


def manifeste(nerf, p, res):
    m = {'nerf': nerf, 'note': 'Un préréglage = un fichier SVG et un jeu de couches visibles ; basculer une couche : [data-couche="…"].',
         'presets': {}}
    for nom, P in p['presets'].items():
        m['presets'][nom] = {'fichier': '%s-%s.svg' % (nerf, nom), 'titre': P['titre'], 'vue': P['vue'], 'couches': P['couches'],
                             'etiquettes': [{'ref': l['ref'], 'texte': l['texte']} for l in res[nom][1]]}
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
    for nom, P in p['presets'].items():
        txt, labels = composer(nerf, nom, P, a)
        res[nom] = (svgo(txt), labels)
    return a, s, p, res


def tour(nerf):
    """Sprite WebP des 8 vues (local seulement : Chromium de Playwright)."""
    from playwright.sync_api import sync_playwright
    from PIL import Image
    a, s = charger(nerf)
    fr, px = [], 300
    with tempfile.TemporaryDirectory() as d, sync_playwright() as p:
        b = p.chromium.launch(); pg = b.new_page(viewport={'width': px, 'height': px})
        for k in range(8):
            G = groupes_trait(open(os.path.join(RENDER, '%s-t%d.svg' % (nerf, k)), encoding='utf-8').read())
            svg = ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 800" width="%d" height="%d"><style>%s</style>'
                   '<rect width="800" height="800" fill="#fff"/><g id="trait">%s</g><g id="territoires">%s</g><g id="nerf">%s</g></svg>'
                   % (px, px, STYLE_TOUR.replace('stroke-width:2.8', 'stroke-width:4').replace('.peau path{stroke:#2f2f2f;stroke-width:1.5',
                      '.peau path{stroke:#2f2f2f;stroke-width:2.2'),
                      ''.join('<g class="%s">%s</g>' % (c, G.get(c, '')) for c in ('crane', 'tronc', 'peau')),
                      G.get('territoires', ''), G.get('nerf', '')))
            f = os.path.join(d, 'f%d.svg' % k); open(f, 'w').write(svg)
            pg.goto('file://' + f); png = os.path.join(d, 'f%d.png' % k); pg.screenshot(path=png)
            fr.append(Image.open(png).convert('RGB'))
        b.close()
    sp = Image.new('RGB', (px * 8, px), (255, 255, 255))
    for k, im in enumerate(fr):
        sp.paste(im, (k * px, 0))
    dst = os.path.join(OUT, '%s-tour.webp' % nerf)
    for q in (80, 70, 60, 50):
        sp.save(dst, 'WEBP', quality=q, method=6)
        if os.path.getsize(dst) <= 190 * 1024:
            break
    ko = round(os.path.getsize(dst) / 1024)
    e = credit_entree(nerf, 'tour', a, s, ko, fichier='%s-tour.webp' % nerf,
                      titre='%s · tour de 8 vues (45° chacune, plongée 15°)' % a['titre'],
                      mods='Huit rendus Freestyle (tools/dedale/freestyle.py --tour) rastérisés à %d px et assemblés en sprite WebP '
                           '(qualité %d) par tools/dedale/annoter.py --tour ; sans annotation.' % (px, q))
    ecrire_credits([e])
    print('tour : %s (%d Ko, qualité %d)' % (os.path.relpath(dst, ROOT), ko, q))



def main():
    args = sys.argv[1:]
    nerf = next((x for x in args if not x.startswith('--')), 'nc07')
    if '--tour' in args:
        return tour(nerf)
    a, s, p, res = construire(nerf)
    fichiers = {'%s-%s.svg' % (nerf, n): t for n, (t, _) in res.items()}
    fichiers['%s-presets.json' % nerf] = manifeste(nerf, p, res)
    if '--verifier' in args:
        bad = [f for f, t in fichiers.items()
               if not os.path.exists(os.path.join(OUT, f)) or open(os.path.join(OUT, f), encoding='utf-8').read() != t]
        for f in bad:
            print('ÉCHEC : assets/nc/%s diffère de sa recomposition.' % f)
        print('Recomposition à l’octet : %d/%d fichiers identiques.' % (len(fichiers) - len(bad), len(fichiers)))
        sys.exit(1 if bad else 0)
    os.makedirs(OUT, exist_ok=True)
    ent = []
    for f, t in fichiers.items():
        open(os.path.join(OUT, f), 'w', encoding='utf-8', newline='\n').write(t)
        print('assets/nc/%s : %d octets' % (f, len(t.encode())))
    for nom, (t, labels) in res.items():
        P = p['presets'][nom]
        ko = round(len(t.encode()) / 1024)
        if P['vue'] == 'plan':
            g = s['gray788']
            e = credit_entree(nerf, nom, a, s, ko, titre='%s · %s' % (a['titre'], P['titre'].split('· ', 1)[-1]),
                              mods='Planche agrandie ×2, filtre crayon (fondu « dodge » sur flou gaussien), retrait automatique des '
                                   'légendes anglaises, vectorisation potrace 1.16 (tools/dedale/trace.py), composition par '
                                   'tools/dedale/annoter.py (préréglage « plan ») ; svgo 4.0.0.')
            e.update({'auteur': g['auteur'], 'source': 'Wikimedia Commons', 'source_url': g['source_url'], 'url': g['source_url'],
                      'licences_amont': {'gray788': g['licence']}})
        else:
            e = credit_entree(nerf, nom, a, s, ko, titre='%s · %s' % (a['titre'], P['titre'].split('· ', 1)[-1]),
                              mods=('Rendu des contours par Freestyle (Blender 3.6.19, tools/dedale/freestyle.py) ; aplats des territoires par '
                                    'tools/dedale/masques.py ; préréglage « %s » (vue %s, %d étiquettes) composé par tools/dedale/annoter.py '
                                    'depuis nc/presets/%s.yml et nc/annot/%s.yml ; svgo 4.0.0.') % (nom, P['vue'], len(labels), nerf, nerf))
        e['preset'] = nom
        ent.append(e)
    # les anciennes vues (une vue = tout le contenu) sont remplacées par les préréglages
    vieux = [f for f in os.listdir(OUT) if re.match(r'%s-[\w-]+\.svg$' % nerf, f) and f not in fichiers]
    for f in vieux:
        os.remove(os.path.join(OUT, f)); print('retiré : assets/nc/%s' % f)
    ecrire_credits(ent, retirer=vieux)


if __name__ == '__main__':
    main()
