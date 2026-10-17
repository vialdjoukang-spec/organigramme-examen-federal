#!/usr/bin/env python3
"""Dédale-V · contrôle des schémas de nerfs crâniens (CI, zéro jeton).

INSTRUCTIONS ----------------------------------------------------------------------
    python3 tools/dedale/verifier.py nc07      # un nerf
    python3 tools/dedale/verifier.py --tous    # tous les nerfs présents dans assets/nc/
Contrôles (ÉCHEC = code de sortie 1) :
  V1 couches : trait, nerf, noyaux, foramens, territoires, lesions, legendes présentes (même vides) ;
     data-couches = couches du préréglage (nc/presets/<nerf>.yml) ; les autres couches masquées ;
  V2 lisibilité : tout texte mesure au moins 13 px une fois l'image réduite à 360 px de large ;
  V3 poids : au plus 120 Ko par vue SVG, au plus 200 Ko pour un sprite WebP (budget de la CI) ;
  V4 crédits : entrée complète dans assets/nc/credits.json (TASL, licence, « Œuvre dérivée »,
     modifications, date, genere_par_ia faux, valide_par_vial présent) et métadonnées dans le SVG ;
  V5 couleur : gris, vert du nerf (#156534) et aplats pâles déclarés dans le préréglage (luminance ≥ 0,8) ;
     le rouge (#b91c1c) ne marque que la couche lesions ; aucune image matricielle intégrée ;
  V6 annotations : chaque entrée de nc/annot/<nerf>.yml a un identifiant, un libellé et une source ;
  V7 rejouabilité : la recomposition par annoter.py redonne chaque SVG à l'octet près
     (sauf --sans-rejeu, quand svgo 4.0.0 n'est pas installé) ;
  V8 une idée par image : au plus 8 étiquettes par préréglage ;
  V9 aucun chevauchement : boîtes d'étiquettes recalculées depuis le texte (largeur estimée à 0,60 em par
     caractère, au-dessus de la largeur mesurée dans Chromium), disjointes, dans l'image, hors de l'encart ;
  V10 dessin : la zone de dessin (data-zone) couvre au moins 60 % de l'image ;
  V11 légende : 4 lignes au plus sous le dessin (légende et crédit court compris), pas de colonne numérotée.
"""
import json, os, re, subprocess, sys
import xml.etree.ElementTree as ET
import yaml

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
NC = os.path.join(ROOT, 'assets', 'nc')
COUCHES = ('trait', 'nerf', 'noyaux', 'foramens', 'territoires', 'lesions', 'legendes')
CHAMPS = ('fichier', 'titre', 'auteur', 'source', 'source_url', 'url', 'licence', 'licence_url', 'licence_derivee', 'derive', 'mention',
          'modifications', 'verifie_le', 'valide_par_vial', 'genere_par_ia', 'oeuvre_derivee')
GRIS = re.compile(r'^#([0-9a-f])\1\1$|^#([0-9a-f]{2})\2\2$', re.I)
fails = []
CAR, LBL_H, BASE, MAX_ETIQ, MIN_PX = 0.60, 36, 26, 8, 13


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


def boites(s, fs):
    """Boîtes des étiquettes, recalculées depuis le SVG : (ref, x, y, w, h)."""
    out = []
    for ref, corps in re.findall(r'<g class="lbl" data-ref="([^"]+)">(.*?)</g>', s, re.S):
        t = re.search(r'<text([^>]*)>(.*?)</text>', corps, re.S)
        if not t:
            continue
        att = t.group(1)
        x = float(re.search(r'\bx="([-\d.]+)"', att).group(1)); y = float(re.search(r'\by="([-\d.]+)"', att).group(1))
        lignes = [re.sub(r'<[^>]+>', '', l) for l in re.findall(r'<tspan[^>]*>(.*?)</tspan>', t.group(2))] or [re.sub(r'<[^>]+>', '', t.group(2))]
        lignes = [l.replace('&amp;', '&').replace('&lt;', '<').replace('&gt;', '>') for l in lignes]
        w = max(len(l) for l in lignes) * CAR * fs
        ta = re.search(r'text-anchor="(\w+)"', att)
        x0 = x - w if ta and ta.group(1) == 'end' else (x - w / 2 if ta and ta.group(1) == 'middle' else x)
        out.append((ref, x0, y - BASE, w, LBL_H * len(lignes)))
    return out


def svg_vue(nerf, p, credits, preset=None, P=None):
    rel = os.path.relpath(p, ROOT)
    s = open(p, encoding='utf-8').read()
    for c in COUCHES:
        check(re.search(r'<g[^>]*\bid="%s"' % c, s), '%s : couche « %s » absente (V1)' % (rel, c))
    vb = re.search(r'viewBox="0 0 ([\d.]+) ([\d.]+)"', s)
    if not check(vb, '%s : viewBox absente' % rel):
        return
    W, H = float(vb.group(1)), float(vb.group(2))
    k = 360 / W
    tailles = [float(x) for x in re.findall(r'font-size:([\d.]+)px', s) + re.findall(r'font-size="([\d.]+)', s)]
    check(tailles and min(tailles) * k >= MIN_PX, '%s : texte de %.1f px à 360 px de large, minimum %d (V2)'
          % (rel, (min(tailles) if tailles else 0) * k, MIN_PX))
    check(ko(p) <= 120, '%s : %.0f Ko, plafond 120 (V3)' % (rel, ko(p)))
    check('<image' not in s and 'data:image' not in s, '%s : image matricielle intégrée interdite (V5)' % rel)
    pales = {c.lower() for c in ((P or {}).get('remplissages') or {}).values()}
    for col in set(re.findall(r'#[0-9a-fA-F]{3,6}\b', s)):
        c = col.lower()
        if c in ('#156534', '#b91c1c') or GRIS.match(c):
            continue
        check(c in pales and lum(c) >= 0.8, '%s : couleur %s non autorisée (V5)' % (rel, col))
    # rouge : seulement des éléments situés dans une couche lesions (classe « u » ou couleur #b91c1c en attribut)
    try:
        racine = ET.fromstring(s)
    except ET.ParseError as e:
        check(False, '%s : SVG illisible (%s)' % (rel, e)); racine = None
    def parcours(el, dans):
        dans = dans or el.get('data-couche') == 'lesions'
        rouge = 'u' in (el.get('class') or '').split() or any('#b91c1c' in (v or '').lower() for k, v in el.attrib.items())
        if rouge and not dans:
            fails.append('%s : rouge hors de la couche lesions (V5)' % rel)
            return False
        return all(parcours(c, dans) for c in el if not c.tag.endswith('style'))
    if racine is not None:
        parcours(racine, False)
    check('Œuvre dérivée' in s and 'CC BY-SA 4.0' in s, '%s : mention « Œuvre dérivée » ou licence absente du SVG (V4)' % rel)
    if preset is not None:
        m = re.search(r'data-couches="([^"]*)"', s)
        check(m and m.group(1).split() == list(P['couches']), '%s : data-couches ≠ couches du préréglage %s (V1)' % (rel, preset))
        for c in COUCHES:
            g = re.search(r'<g[^>]*\bid="%s"[^>]*>' % c, s)
            if g:
                cache = 'display="none"' in g.group(0)
                check(cache == (c not in P['couches']), '%s : couche %s %s à tort (V1)' % (rel, c, 'masquée' if cache else 'visible'))
        fs = re.search(r'\.lb[^{]*\{[^}]*font-size:([\d.]+)px', s) or re.search(r'\.lb,\.lg\{font-size:([\d.]+)px', s)
        fs = float(fs.group(1)) if fs else 30
        B = boites(s, fs)
        check(len(B) <= MAX_ETIQ, '%s : %d étiquettes, %d au plus par préréglage (V8)' % (rel, len(B), MAX_ETIQ))
        enc = re.search(r'<rect[^>]*class="enc"[^>]*>', s)
        E = None
        if enc:
            g = lambda a: float(re.search(r'\b%s="([-\d.]+)"' % a, enc.group(0)).group(1))
            E = (g('x'), g('y'), g('width'), g('height'))
        for n, b in enumerate(B):
            check(b[1] >= 0 and b[2] >= 0 and b[1] + b[3] <= W and b[2] + b[4] <= H, '%s : étiquette %s hors de l’image (V9)' % (rel, b[0]))
            if E:
                check(not inter(b[1:], E), '%s : étiquette %s sur l’encart (V9)' % (rel, b[0]))
            for c in B[n + 1:]:
                check(not inter(b[1:], c[1:]), '%s : étiquettes %s et %s se chevauchent (V9)' % (rel, b[0], c[0]))
        z = re.search(r'data-zone="([\d.]+) ([\d.]+) ([\d.]+) ([\d.]+)"', s)
        if check(z, '%s : data-zone absente (V10)' % rel):
            part = float(z.group(3)) * float(z.group(4)) / (W * H)
            check(part >= 0.6, '%s : dessin %.0f %% de l’image, 60 %% au moins (V10)' % (rel, 100 * part))
        bas = re.search(r'<g id="legende-bas">(.*?)</g>', s, re.S)
        n_l = len(re.findall(r'<text', bas.group(1))) if bas else 0
        check(bas and n_l <= 4, '%s : légende de %d lignes, 4 au plus (V11)' % (rel, n_l))
    credit(rel, credits)


def inter(a, b):
    return not (a[0] + a[2] <= b[0] or b[0] + b[2] <= a[0] or a[1] + a[3] <= b[1] or b[1] + b[3] <= a[1])


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
    for nerf in nerfs:
        a = annot(nerf)
        fp = os.path.join(ROOT, 'nc', 'presets', nerf + '.yml')
        if os.path.exists(fp):
            presets = yaml.safe_load(open(fp, encoding='utf-8'))['presets']
            check(os.path.exists(os.path.join(NC, nerf + '-presets.json')), 'assets/nc/%s-presets.json absent (V1)' % nerf)
            for nom, P in presets.items():
                check(len(P.get('etiquettes') or []) <= MAX_ETIQ,
                      'nc/presets/%s.yml : %s a %d étiquettes, %d au plus (V8)' % (nerf, nom, len(P.get('etiquettes') or []), MAX_ETIQ))
                p = os.path.join(NC, '%s-%s.svg' % (nerf, nom))
                if check(os.path.exists(p), 'assets/nc/%s-%s.svg absent' % (nerf, nom)):
                    svg_vue(nerf, p, credits, nom, P)
        else:
            for v in (a or {}).get('vues', []):
                p = os.path.join(NC, '%s-%s.svg' % (nerf, v))
                if check(os.path.exists(p), 'assets/nc/%s-%s.svg absent' % (nerf, v)):
                    svg_vue(nerf, p, credits)
        tour = os.path.join(NC, nerf + '-tour.webp')
        if os.path.exists(tour):
            rel = os.path.relpath(tour, ROOT)
            check(ko(tour) <= 200, '%s : %.0f Ko, plafond 200 (V3)' % (rel, ko(tour)))
            credit(rel, credits)
            check(nerf in ('nc03', 'nc04', 'nc05', 'nc06', 'nc07'),
                  '%s : tour de 8 vues réservé à V, VII et III-IV-VI (décision du 17.10.2026)' % rel)
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
