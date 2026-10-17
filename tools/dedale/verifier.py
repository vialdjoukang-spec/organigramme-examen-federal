#!/usr/bin/env python3
"""Dédale-V · contrôle des schémas de nerfs crâniens (CI, zéro jeton).

INSTRUCTIONS ----------------------------------------------------------------------
    python3 tools/dedale/verifier.py nc07      # un nerf
    python3 tools/dedale/verifier.py --tous    # tous les nerfs présents dans assets/nc/
Contrôles (ÉCHEC = code de sortie 1) :
  V1 couches et états : trait, nerf, noyaux, foramens, territoires, lesions, legendes présentes (même vides) ;
     data-etats = états de nc/presets/<nerf>.yml ; couches visibles par défaut = celles de l'état par défaut ;
  V2 lisibilité : tout texte mesure au moins 13 px une fois l'image réduite à 360 px de large ;
  V3 poids : au plus 120 Ko par vue SVG ;
  V4 crédits : entrée complète dans assets/nc/credits.json (TASL, licence, « Œuvre dérivée »,
     modifications, date, genere_par_ia faux, valide_par_vial présent) et métadonnées dans le SVG ;
  V5 couleur : gris, nerf en jaune intense (#ffc400) cerné de #5a4500, aplats pâles déclarés dans les états
     (luminance ≥ 0,8) ; l'ancien vert du nerf (#156534) est refusé ; le rouge (#b91c1c) ne marque que la
     couche lesions ; aucune image matricielle intégrée ;
  V6 annotations : chaque entrée de nc/annot/<nerf>.yml a un identifiant, un libellé et une source ;
  V7 rejouabilité : la recomposition par annoter.py redonne chaque fichier à l'octet près
     (sauf --sans-rejeu, quand svgo 4.0.0 n'est pas installé) ;
  V8 une idée par état : au plus 8 étiquettes par état ;
  V9 aucun chevauchement dans un état : boîtes recalculées depuis le texte (0,60 em par caractère, au-dessus de
     la largeur mesurée dans Chromium), disjointes et dans l'image ;
  V10 dessin : la zone de dessin (data-zone) couvre au moins 60 % de l'image ;
  V11 légende : 4 lignes au plus par état (légende et crédit court compris) ;
  V12 trois vues : exactement face, profil et 34 publiées par nerf ; ni tour de 8 vues ni autre image.
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
JAUNE, CERNE = '#ffc400', '#5a4500'
VUES = ['face', 'profil', '34']


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


def svg_vue(nerf, p, credits, P=None):
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
    pales = {c.lower() for E in ((P or {}).get('etats') or {}).values() for c in (E.get('remplissages') or {}).values()}
    for col in set(re.findall(r'#[0-9a-fA-F]{3,6}\b', s)):
        c = col.lower()
        if c in (JAUNE, CERNE, '#b91c1c') or GRIS.match(c):
            continue
        check(c in pales and lum(c) >= 0.8, '%s : couleur %s non autorisée (V5)' % (rel, col))
    st = re.search(r'<style>(.*?)</style>', s, re.S)
    st = st.group(1).lower() if st else ''
    check(re.search(r'\.n2 path\{[^}]*stroke:%s' % JAUNE, st) and re.search(r'\.n1 path\{[^}]*stroke:%s' % CERNE, st),
          '%s : le nerf doit être jaune %s cerné de %s (V5)' % (rel, JAUNE, CERNE))
    try:
        racine = ET.fromstring(s)
    except ET.ParseError as e:
        check(False, '%s : SVG illisible (%s)' % (rel, e)); return
    def parcours(el, dans):
        dans = dans or el.get('data-couche') == 'lesions'
        rouge = 'u' in (el.get('class') or '').split() or any('#b91c1c' in (v or '').lower() for v in el.attrib.values())
        if rouge and not dans:
            fails.append('%s : rouge hors de la couche lesions (V5)' % rel)
            return False
        return all(parcours(c, dans) for c in el if not c.tag.endswith('style'))
    parcours(racine, False)
    check('Œuvre dérivée' in s and 'CC BY-SA 4.0' in s, '%s : mention « Œuvre dérivée » ou licence absente du SVG (V4)' % rel)
    if P is not None:
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
        fs = re.search(r'\.lb,\.lg\{font-size:([\d.]+)px', s)
        fs = float(fs.group(1)) if fs else 30
        for g in racine.iter():
            e = g.get('data-etat')
            if e is not None and g is not racine:
                check((g.get('display') == 'none') == (e != defaut), '%s : groupe %s de l’état %s mal masqué (V1)'
                      % (rel, g.get('class'), e))
        par_etat = {}
        for g in racine.iter():
            if 'etiquettes' in (g.get('class') or '').split():
                e = g.get('data-etat')
                check(e in attendu, '%s : étiquettes d’un état inconnu %r (V1)' % (rel, e))
                par_etat.setdefault(e, []).extend(boites(g, fs))
        for e, B in par_etat.items():
            check(len(B) <= MAX_ETIQ, '%s : état %s : %d étiquettes, %d au plus (V8)' % (rel, e, len(B), MAX_ETIQ))
            for n, b in enumerate(B):
                check(b[1] >= 0 and b[2] >= 0 and b[1] + b[3] <= W and b[2] + b[4] <= H, '%s : étiquette %s hors de l’image (V9)' % (rel, b[0]))
                for c in B[n + 1:]:
                    check(not inter(b[1:], c[1:]), '%s : état %s : étiquettes %s et %s se chevauchent (V9)' % (rel, e, b[0], c[0]))
        z = re.search(r'data-zone="([\d.]+) ([\d.]+) ([\d.]+) ([\d.]+)"', s)
        if check(z, '%s : data-zone absente (V10)' % rel):
            part = float(z.group(3)) * float(z.group(4)) / (W * H)
            check(part >= 0.6, '%s : dessin %.0f %% de l’image, 60 %% au moins (V10)' % (rel, 100 * part))
        lignes = {}
        for g in racine.iter():
            if (g.get('class') or '') in ('legende', 'credit'):
                lignes[g.get('data-etat')] = lignes.get(g.get('data-etat'), 0) + sum(1 for t in g.iter() if t.tag.endswith('text'))
        for e in attendu:
            check(lignes.get(e, 0) <= 4, '%s : état %s : légende de %d lignes, 4 au plus (V11)' % (rel, e, lignes.get(e, 0)))
    credit(rel, credits)


def boites(g, fs):
    out = []
    for lb in g:
        if 'lbl' not in (lb.get('class') or '').split():
            continue
        t = next((x for x in lb.iter() if x.tag.endswith('text')), None)
        if t is None:
            continue
        x, y = float(t.get('x')), float(t.get('y'))
        lignes = [ts.text or '' for ts in t if ts.tag.endswith('tspan')] or [t.text or '']
        w = max(len(l) for l in lignes) * CAR * fs
        ta = t.get('text-anchor')
        x0 = x - w if ta == 'end' else (x - w / 2 if ta == 'middle' else x)
        out.append((lb.get('data-ref'), x0, y - BASE, w, LBL_H * len(lignes)))
    return out


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
        P = yaml.safe_load(open(fp, encoding='utf-8')) if os.path.exists(fp) else None
        check(P is not None, 'nc/presets/%s.yml absent (V1)' % nerf)
        if P:
            check([str(v) for v in P.get('vues', [])] == VUES, 'nc/presets/%s.yml : vues %s, exactement %s (V12)' % (nerf, P.get('vues'), VUES))
            for nom, E in P['etats'].items():
                check(len(E.get('etiquettes') or []) <= MAX_ETIQ,
                      'nc/presets/%s.yml : état %s : %d étiquettes, %d au plus (V8)' % (nerf, nom, len(E.get('etiquettes') or []), MAX_ETIQ))
            check(os.path.exists(os.path.join(NC, nerf + '-presets.json')), 'assets/nc/%s-presets.json absent (V1)' % nerf)
        attendus = {'%s-%s.svg' % (nerf, v) for v in VUES} | {nerf + '-presets.json'}
        for f in sorted(os.listdir(NC)):
            if f.startswith(nerf + '-') and f not in attendus:
                check(False, 'assets/nc/%s : seules les 3 vues face, profil, 34 sont publiées (V12)' % f)
        for v in VUES:
            p = os.path.join(NC, '%s-%s.svg' % (nerf, v))
            if check(os.path.exists(p), 'assets/nc/%s-%s.svg absent (V12)' % (nerf, v)):
                svg_vue(nerf, p, credits, P)
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
