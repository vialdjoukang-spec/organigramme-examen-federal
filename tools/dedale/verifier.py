#!/usr/bin/env python3
"""Dédale-V · contrôle des schémas de nerfs crâniens (CI, zéro jeton).

INSTRUCTIONS ----------------------------------------------------------------------
    python3 tools/dedale/verifier.py nc07      # un nerf
    python3 tools/dedale/verifier.py --tous    # tous les nerfs présents dans assets/nc/
Contrôles (ÉCHEC = code de sortie 1) :
  V1 couches et états : trait, nerf, noyaux, foramens, territoires, lesions, legendes et legende présentes (même
     vides) ; data-etats = états de nc/presets/<nerf>.yml ; couches visibles par défaut = celles de l'état par
     défaut ; chaque groupe [data-etat] masqué hors de l'état par défaut ;
  V2 lisibilité (image réduite à 360 px de large) : titre ≥ 13 px ; repère numéroté ≥ 13 px de diamètre hors
     tout, numéro ≥ 8 px ; légende et crédit (petits caractères) ≥ 9 px ;
  V3 poids : au plus 120 Ko par vue SVG ;
  V4 crédits : entrée complète dans assets/nc/credits.json (TASL, licence, « Œuvre dérivée »,
     modifications, date, genere_par_ia faux, valide_par_vial présent) et métadonnées dans le SVG ;
  V5 couleur : gris, nerf en jaune intense (#ffc400) cerné de #5a4500, aplats pâles déclarés dans les états
     (luminance ≥ 0,8) ; l'ancien vert du nerf (#156534) est refusé ; le rouge (#b91c1c) ne marque que la
     couche lesions ; aucune image matricielle intégrée ;
  V6 annotations : chaque entrée de nc/annot/<nerf>.yml a un identifiant, un libellé et une source ;
  V7 rejouabilité : la recomposition par annoter.py redonne chaque fichier à l'octet près
     (sauf --sans-rejeu, quand svgo 4.0.0 n'est pas installé) ;
  V8 une idée par état : au plus 8 repères par état ;
  V9 repères aérés : dans un état, cercles disjoints, aucun repère sur le nerf ni sur un noyau (chemins du SVG
     échantillonnés, demi-épaisseur du nerf comprise), tous dans la zone de dessin ;
  V10 dessin : la zone de dessin (data-zone) couvre au moins 60 % de l'image ;
  V11 légende : dans g#legende, une entrée numérotée par repère de l'état, mêmes numéros, aucune ligne qui
     déborde de sa colonne ; 2 lignes de note au plus ;
  V12 trois vues : exactement face, profil et 34 publiées par nerf ; ni tour de 8 vues ni autre image ;
  V13 aucun texte sur le dessin : dans la zone de dessin, seuls les numéros des repères ;
  V14 contrat des repères : <g class="nc-num" data-num data-nom data-glo? tabindex="0" role="button"
     aria-label="n · nom">, trait de rappel et pointe de flèche ; data-nom non vide ; data-glo, s'il est
     présent, existe dans data/ck/glo.json ;
  V15 numérotation : dans un état, un même numéro désigne la même structure dans les 3 vues.
"""
import json, os, re, subprocess, sys
import xml.etree.ElementTree as ET
import yaml

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
NC = os.path.join(ROOT, 'assets', 'nc')
COUCHES = ('trait', 'nerf', 'noyaux', 'foramens', 'territoires', 'lesions', 'legendes', 'legende')
CHAMPS = ('fichier', 'titre', 'auteur', 'source', 'source_url', 'url', 'licence', 'licence_url', 'licence_derivee', 'derive', 'mention',
          'modifications', 'verifie_le', 'valide_par_vial', 'genere_par_ia', 'oeuvre_derivee')
GRIS = re.compile(r'^#([0-9a-f])\1\1$|^#([0-9a-f]{2})\2\2$', re.I)
fails = []
CAR_LEG, MAX_ETIQ = 0.56, 8
MIN_TT, MIN_NUM_D, MIN_NM, MIN_LG = 13, 13, 8, 9     # px, image réduite à 360 px
JAUNE, CERNE = '#ffc400', '#5a4500'
VUES = ['face', 'profil', '34']
COL2 = 412          # abscisse de la 2e colonne de la légende
NUM = re.compile(r'-?(?:\d+\.?\d*|\.\d+)(?:[eE][-+]?\d+)?|[MmLlHhVvCcSsQqTtAaZz]')


def echantillons(d, pas=1.5):
    """Points d'un chemin SVG (toutes commandes ; courbes échantillonnées, arcs pris en corde)."""
    tok = NUM.findall(d)
    pts, i, cmd = [], 0, None
    x = y = sx = sy = 0.0
    lx = ly = None
    def ligne(x0, y0, x1, y1):
        n = max(1, int(((x1 - x0) ** 2 + (y1 - y0) ** 2) ** 0.5 / pas))
        pts.extend((x0 + (x1 - x0) * t / n, y0 + (y1 - y0) * t / n) for t in range(1, n + 1))
    def courbe(P):
        for t in range(1, 13):
            u = t / 12
            if len(P) == 4:
                bx = sum(c * q[0] for c, q in zip(((1 - u) ** 3, 3 * u * (1 - u) ** 2, 3 * u * u * (1 - u), u ** 3), P))
                by = sum(c * q[1] for c, q in zip(((1 - u) ** 3, 3 * u * (1 - u) ** 2, 3 * u * u * (1 - u), u ** 3), P))
            else:
                bx = sum(c * q[0] for c, q in zip(((1 - u) ** 2, 2 * u * (1 - u), u * u), P))
                by = sum(c * q[1] for c, q in zip(((1 - u) ** 2, 2 * u * (1 - u), u * u), P))
            pts.append((bx, by))
    n_arg = {'M': 2, 'L': 2, 'H': 1, 'V': 1, 'C': 6, 'S': 4, 'Q': 4, 'T': 2, 'A': 7, 'Z': 0}
    while i < len(tok):
        if tok[i].isalpha():
            cmd = tok[i]; i += 1
            if cmd in 'Zz':
                ligne(x, y, sx, sy); x, y = sx, sy; lx = ly = None
                continue
        if cmd is None:
            break
        k = n_arg[cmd.upper()]
        v = [float(t) for t in tok[i:i + k]]
        if len(v) < k:
            break
        i += k
        rel = cmd.islower()
        ox, oy = (x, y) if rel else (0.0, 0.0)
        C = cmd.upper()
        if C == 'M':
            x, y = ox + v[0], oy + v[1]; sx, sy = x, y; pts.append((x, y)); lx = ly = None
            cmd = 'l' if rel else 'L'
        elif C == 'L':
            nx, ny = ox + v[0], oy + v[1]; ligne(x, y, nx, ny); x, y = nx, ny; lx = ly = None
        elif C == 'H':
            nx = (x + v[0]) if rel else v[0]; ligne(x, y, nx, y); x = nx; lx = ly = None
        elif C == 'V':
            ny = (y + v[0]) if rel else v[0]; ligne(x, y, x, ny); y = ny; lx = ly = None
        elif C == 'C':
            P = [(x, y), (ox + v[0], oy + v[1]), (ox + v[2], oy + v[3]), (ox + v[4], oy + v[5])]
            courbe(P); x, y = P[3]; lx, ly = P[2]
        elif C == 'S':
            c1 = (2 * x - lx, 2 * y - ly) if lx is not None else (x, y)
            P = [(x, y), c1, (ox + v[0], oy + v[1]), (ox + v[2], oy + v[3])]
            courbe(P); x, y = P[3]; lx, ly = P[2]
        elif C == 'Q':
            P = [(x, y), (ox + v[0], oy + v[1]), (ox + v[2], oy + v[3])]
            courbe(P); x, y = P[2]; lx, ly = P[1]
        elif C == 'T':
            c1 = (2 * x - lx, 2 * y - ly) if lx is not None else (x, y)
            P = [(x, y), c1, (ox + v[0], oy + v[1])]
            courbe(P); x, y = P[2]; lx, ly = c1
        elif C == 'A':
            nx, ny = ox + v[5], oy + v[6]; ligne(x, y, nx, ny); x, y = nx, ny; lx = ly = None
    return pts


def classes(el):
    return (el.get('class') or '').split()


def ko(p):
    return os.path.getsize(p) / 1024


def check(cond, msg):
    if not cond:
        fails.append(msg)
    return cond


def lum(c):
    c = c.lstrip('#')
    if len(c) == 3:
        c = ''.join(x * 2 for x in c)
    r, g, b = (int(c[k:k + 2], 16) / 255 for k in (0, 2, 4))
    return 0.2126 * r + 0.7152 * g + 0.0722 * b


def taille(st, cls):
    m = re.search(r'\.%s\{[^}]*font-size:([\d.]+)px' % re.escape(cls), st)
    return float(m.group(1)) if m else None


def svg_vue(nerf, p, credits, P=None, glo=None):
    """Contrôle une vue ; renvoie {état: {numéro: nom}} pour la cohérence entre vues (V15)."""
    rel = os.path.relpath(p, ROOT)
    s = open(p, encoding='utf-8').read()
    for c in COUCHES:
        check(re.search(r'<g[^>]*\bid="%s"' % c, s), '%s : couche « %s » absente (V1)' % (rel, c))
    vb = re.search(r'viewBox="0 0 ([\d.]+) ([\d.]+)"', s)
    if not check(vb, '%s : viewBox absente' % rel):
        return {}
    W, H = float(vb.group(1)), float(vb.group(2))
    k = 360 / W
    st = re.search(r'<style>(.*?)</style>', s, re.S)
    st = st.group(1).lower() if st else ''
    # V2 : tailles par rôle
    for cls, mini, quoi in (('tt', MIN_TT, 'titre'), ('lg', MIN_LG, 'légende'), ('nm', MIN_NM, 'numéro de repère')):
        t = taille(st, cls)
        check(t is not None and t * k >= mini, '%s : %s de %.1f px à 360 px de large, minimum %d (V2)' % (rel, quoi, (t or 0) * k, mini))
    autres = [float(x) for x in re.findall(r'font-size="([\d.]+)', s)]
    check(not autres or min(autres) * k >= MIN_LG, '%s : texte de %.1f px à 360 px de large (V2)' % (rel, min(autres or [0]) * k))
    check(ko(p) <= 120, '%s : %.0f Ko, plafond 120 (V3)' % (rel, ko(p)))
    check('<image' not in s and 'data:image' not in s, '%s : image matricielle intégrée interdite (V5)' % rel)
    pales = {c.lower() for E in ((P or {}).get('etats') or {}).values() for c in (E.get('remplissages') or {}).values()}
    for col in set(re.findall(r'#[0-9a-fA-F]{3,6}\b', s)):
        c = col.lower()
        if c in (JAUNE, CERNE, '#b91c1c') or GRIS.match(c):
            continue
        check(c in pales and lum(c) >= 0.8, '%s : couleur %s non autorisée (V5)' % (rel, col))
    check(re.search(r'\.n2 path\{[^}]*stroke:%s' % JAUNE, st) and re.search(r'\.n1 path\{[^}]*stroke:%s' % CERNE, st),
          '%s : le nerf doit être jaune %s cerné de %s (V5)' % (rel, JAUNE, CERNE))
    try:
        racine = ET.fromstring(s)
    except ET.ParseError as e:
        check(False, '%s : SVG illisible (%s)' % (rel, e)); return {}
    def parcours(el, dans):
        dans = dans or el.get('data-couche') == 'lesions'
        rouge = 'u' in classes(el) or any('#b91c1c' in (v or '').lower() for v in el.attrib.values())
        if rouge and not dans:
            fails.append('%s : rouge hors de la couche lesions (V5)' % rel)
            return False
        return all(parcours(c, dans) for c in el if not c.tag.endswith('style'))
    parcours(racine, False)
    check('Œuvre dérivée' in s and 'CC BY-SA 4.0' in s, '%s : mention « Œuvre dérivée » ou licence absente du SVG (V4)' % rel)
    z = re.search(r'data-zone="([\d.]+) ([\d.]+) ([\d.]+) ([\d.]+)"', s)
    if not check(z, '%s : data-zone absente (V10)' % rel):
        return {}
    zone = [float(z.group(i)) for i in range(1, 5)]
    check(zone[2] * zone[3] / (W * H) >= 0.6, '%s : dessin %.0f %% de l’image, 60 %% au moins (V10)' % (rel, 100 * zone[2] * zone[3] / (W * H)))
    dans_zone = lambda x, y: zone[0] <= x <= zone[0] + zone[2] and zone[1] <= y <= zone[1] + zone[3]
    # V13 : aucun texte sur le dessin, hors numéros des repères
    def textes(el, num):
        num = num or 'nc-num' in classes(el)
        if el.tag.endswith('}text') or el.tag == 'text':
            try:
                x, y = float(el.get('x', '0')), float(el.get('y', '0'))
            except ValueError:
                x = y = 0
            if not num and dans_zone(x, y):
                fails.append('%s : texte « %s » sur le dessin ; seuls les repères numérotés y sont permis (V13)'
                             % (rel, ''.join(el.itertext()).strip()[:40]))
        for c in el:
            textes(c, num)
    textes(racine, False)
    # nerf et noyaux : points échantillonnés (coordonnées de l'image : le dessin est posé à l'identique)
    nerf_pts, demi = [], 4.25
    for gid in ('nerf', 'noyaux'):
        g = next((e for e in racine.iter() if e.get('id') == gid), None)
        for pth in (g.iter() if g is not None else ()):
            if pth.tag.endswith('path') and pth.get('d'):
                nerf_pts += echantillons(pth.get('d'))
    sw = re.search(r'\.n1 path\{[^}]*stroke-width:([\d.]+)', st)
    g1 = next((e for e in racine.iter() if 'n1' in classes(e)), None)
    p1 = next((e for e in g1.iter() if e.tag.endswith('path')), None) if g1 is not None else None
    if sw:                                            # la feuille de style l'emporte sur l'attribut
        demi = float(sw.group(1)) / 2
    elif p1 is not None and p1.get('stroke-width'):
        demi = float(re.sub(r'[^\d.]', '', p1.get('stroke-width'))) / 2
    grille = {}
    for x, y in nerf_pts:
        grille.setdefault((int(x // 32), int(y // 32)), []).append((x, y))
    def d_nerf(x, y):
        best = float('inf')
        for i in range(int(x // 32) - 1, int(x // 32) + 2):
            for j in range(int(y // 32) - 1, int(y // 32) + 2):
                for q in grille.get((i, j), ()):
                    best = min(best, ((q[0] - x) ** 2 + (q[1] - y) ** 2) ** 0.5)
        return best
    vus = {}
    if P is None:
        credit(rel, credits); return vus
    try:
        etats = json.loads(racine.get('data-etats') or '{}')
    except ValueError:
        etats = {}
    attendu = {n: list(E['couches']) for n, E in P['etats'].items()}
    check(etats == attendu, '%s : data-etats ≠ états de nc/presets (V1)' % rel)
    defaut = racine.get('data-etat')
    check(defaut == P.get('etat_defaut'), '%s : état par défaut %r (V1)' % (rel, defaut))
    for c in COUCHES:
        g = re.search(r'<g[^>]*\bid="%s"[^>]*>' % c, s)
        if g and defaut in etats:
            cache = 'display="none"' in g.group(0)
            check(cache == (c not in etats[defaut]), '%s : couche %s %s à tort (V1)' % (rel, c, 'masquée' if cache else 'visible'))
    for g in racine.iter():
        e = g.get('data-etat')
        if e is not None and g is not racine:
            check((g.get('display') == 'none') == (e != defaut), '%s : groupe %s de l’état %s mal masqué (V1)' % (rel, g.get('class'), e))
    st_cr = re.search(r'\.cr\{[^}]*stroke-width:([\d.]+)', st)
    e_cr = float(st_cr.group(1)) if st_cr else 0
    par_etat = {}
    for g in racine.iter():
        if 'numeros' not in classes(g):
            continue
        e = g.get('data-etat')
        check(e in attendu, '%s : repères d’un état inconnu %r (V1)' % (rel, e))
        for m in g:
            if 'nc-num' not in classes(m):
                continue
            num, nom = m.get('data-num'), (m.get('data-nom') or '').strip()
            ok = check(num and num.isdigit(), '%s : repère sans data-num (V14)' % rel)
            check(nom, '%s : état %s : repère %s sans data-nom (V14)' % (rel, e, num))
            check(m.get('tabindex') == '0' and m.get('role') == 'button', '%s : repère %s sans tabindex="0" role="button" (V14)' % (rel, num))
            check(m.get('aria-label') == '%s · %s' % (num, nom), '%s : repère %s : aria-label ≠ « n · nom » (V14)' % (rel, num))
            if m.get('data-glo') is not None and glo is not None:
                check(m.get('data-glo') in glo, '%s : repère %s : data-glo %r absent de data/ck/glo.json (V14)' % (rel, num, m.get('data-glo')))
            kids = list(m)
            check(any(c.tag.endswith('path') and 'ld' in classes(c) for c in kids) and
                  any(c.tag.endswith('path') and 'ah' in classes(c) for c in kids), '%s : repère %s sans flèche (V14)' % (rel, num))
            cr = next((c for c in kids if c.tag.endswith('circle')), None)
            if not check(cr is not None, '%s : repère %s sans cercle (V14)' % (rel, num)) or not ok:
                continue
            try:
                cx, cy, r = float(cr.get('cx')), float(cr.get('cy')), float(cr.get('r')) + e_cr / 2
            except (TypeError, ValueError):
                check(False, '%s : repère %s : cercle illisible (V14)' % (rel, num)); continue
            par_etat.setdefault(e, []).append((int(num), nom, cx, cy, r))
    for e, L in par_etat.items():
        check(len(L) <= MAX_ETIQ, '%s : état %s : %d repères, %d au plus (V8)' % (rel, e, len(L), MAX_ETIQ))
        vus[e] = {n: nom for n, nom, *_ in L}
        check(len(vus[e]) == len(L), '%s : état %s : numéro de repère en double (V14)' % (rel, e))
        for i, (n, nom, cx, cy, r) in enumerate(L):
            check(2 * r * k >= MIN_NUM_D, '%s : repère %d de %.1f px à 360 px, %d au moins (V2)' % (rel, n, 2 * r * k, MIN_NUM_D))
            check(dans_zone(cx - r, cy - r) and dans_zone(cx + r, cy + r), '%s : état %s : repère %d hors du dessin (V9)' % (rel, e, n))
            dn = d_nerf(cx, cy)
            check(dn >= r + demi, '%s : état %s : repère %d sur le nerf (%.1f px du tracé) (V9)' % (rel, e, n, dn))
            for m2 in L[i + 1:]:
                d = ((cx - m2[2]) ** 2 + (cy - m2[3]) ** 2) ** 0.5
                check(d >= r + m2[4], '%s : état %s : repères %d et %d se chevauchent (V9)' % (rel, e, n, m2[0]))
    # V11 : légende
    legende = next((g for g in racine.iter() if g.get('id') == 'legende'), None)
    if check(legende is not None and legende.get('data-couche') == 'legende', '%s : couche g#legende absente (V11)' % rel):
        fs = taille(st, 'lg') or 22
        for g in legende:
            e = g.get('data-etat')
            nums, notes = [], 0
            for t in g:
                if not t.tag.endswith('text'):
                    continue
                n = next((x for x in t if 'n' in classes(x)), None)
                txt = ''.join(t.itertext())
                if n is not None:
                    nums.append(int(n.text))
                elif float(t.get('x')) < 30:
                    notes += 1
                x = float(t.get('x'))
                fin = x + len(txt) * CAR_LEG * fs
                note = n is None and x < 30          # note pleine largeur sous les 2 colonnes
                check(fin <= (COL2 - 4 if x < COL2 and not note else W - 4), '%s : état %s : ligne de légende « %s » déborde (V11)' % (rel, e, txt[:30]))
            check(notes <= 2, '%s : état %s : %d lignes de note, 2 au plus (V11)' % (rel, e, notes))
            check(sorted(nums) == sorted(vus.get(e, {})), '%s : état %s : légende %s ≠ repères %s (V11)' % (rel, e, sorted(nums), sorted(vus.get(e, {}))))
    credit(rel, credits)
    return vus


def credit(rel, credits):
    e = credits.get(os.path.basename(rel))
    if not check(e, '%s : aucune entrée dans assets/nc/credits.json (V4)' % rel):
        return
    for c in CHAMPS:
        check(c in e and e[c] not in ('', None), '%s : champ de crédit « %s » manquant (V4)' % (rel, c))
    check(e.get('genere_par_ia') is False, '%s : genere_par_ia doit être faux (V4)' % rel)
    check(e.get('oeuvre_derivee') is True and e.get('mention') == 'Œuvre dérivée', '%s : mention « Œuvre dérivée » (V4)' % rel)
    check(e.get('licence') == 'CC BY-SA 4.0' and e.get('licence_derivee') == 'CC BY-SA 4.0' and e.get('derive') is True,
          '%s : une vue dérivée reste sous CC BY-SA 4.0 (licence, licence_derivee, derive) (V4)' % rel)


def annot(nerf):
    p = os.path.join(ROOT, 'nc', 'annot', nerf + '.yml')
    if not check(os.path.exists(p), 'nc/annot/%s.yml absent (V6)' % nerf):
        return None
    a = yaml.safe_load(open(p, encoding='utf-8'))
    for couche, lst in (a.get('couches') or {}).items():
        for e in lst or []:
            for c in ('id', 'libelle', 'source'):
                check(e.get(c), 'nc/annot/%s.yml : %s/%s sans « %s » (V6)' % (nerf, couche, e.get('id', '?'), c))
            if couche == 'lesions' and e.get('urgence'):
                check(e.get('source'), 'nc/annot/%s.yml : lésion d’urgence sans source (V6)' % nerf)
    return a


def main():
    args = sys.argv[1:]
    nerfs = sorted({f.split('-')[0] for f in os.listdir(NC) if re.match(r'nc\d\d-', f)}) if '--tous' in args \
        else [x for x in args if not x.startswith('--')] or ['nc07']
    data = json.load(open(os.path.join(NC, 'credits.json'), encoding='utf-8'))
    if not isinstance(data, list):
        sys.exit('ÉCHEC assets/nc/credits.json doit être une liste d’entrées (format de tools/nc_svg_check.py)')
    credits = {e['fichier']: e for e in data}
    gp = os.path.join(ROOT, 'data', 'ck', 'glo.json')
    glo = {e['id'] for e in json.load(open(gp, encoding='utf-8'))} if os.path.exists(gp) else None
    for nerf in nerfs:
        a = annot(nerf)
        fp = os.path.join(ROOT, 'nc', 'presets', nerf + '.yml')
        P = yaml.safe_load(open(fp, encoding='utf-8')) if os.path.exists(fp) else None
        check(P is not None, 'nc/presets/%s.yml absent (V1)' % nerf)
        if P:
            check([str(v) for v in P.get('vues', [])] == VUES, 'nc/presets/%s.yml : vues %s, exactement %s (V12)' % (nerf, P.get('vues'), VUES))
            for nom, E in P['etats'].items():
                check(len(E.get('etiquettes') or []) <= MAX_ETIQ,
                      'nc/presets/%s.yml : état %s : %d repères, %d au plus (V8)' % (nerf, nom, len(E.get('etiquettes') or []), MAX_ETIQ))
            check(os.path.exists(os.path.join(NC, nerf + '-presets.json')), 'assets/nc/%s-presets.json absent (V1)' % nerf)
        attendus = {'%s-%s.svg' % (nerf, v) for v in VUES} | {nerf + '-presets.json'}
        for f in sorted(os.listdir(NC)):
            if f.startswith(nerf + '-') and f not in attendus:
                check(False, 'assets/nc/%s : seules les 3 vues face, profil, 34 sont publiées (V12)' % f)
        numeros = {}
        for v in VUES:
            p = os.path.join(NC, '%s-%s.svg' % (nerf, v))
            if check(os.path.exists(p), 'assets/nc/%s-%s.svg absent (V12)' % (nerf, v)):
                for e, M in svg_vue(nerf, p, credits, P, glo).items():
                    for n, nom in M.items():
                        prec = numeros.setdefault(e, {}).setdefault(n, (nom, v))
                        check(prec[0] == nom, '%s : état %s : repère %d « %s » (%s) ≠ « %s » (%s) (V15)' % (nerf, e, n, nom, v, prec[0], prec[1]))
        if '--sans-rejeu' not in args:
            r = subprocess.run([sys.executable, os.path.join(ROOT, 'tools', 'dedale', 'annoter.py'), nerf, '--verifier'],
                               capture_output=True, text=True)
            check(r.returncode == 0, '%s : recomposition non identique à l’octet (V7) %s' % (nerf, (r.stdout + r.stderr).strip()[-300:]))
    for f in fails:
        print('ÉCHEC', f)
    print('Dédale-V : %d nerf(s) contrôlé(s), %d échec(s).' % (len(nerfs), len(fails)))
    sys.exit(1 if fails else 0)


if __name__ == '__main__':
    main()
