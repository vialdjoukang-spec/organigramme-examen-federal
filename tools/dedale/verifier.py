#!/usr/bin/env python3
"""Dédale-V · contrôle des schémas de nerfs crâniens (CI, zéro jeton).

INSTRUCTIONS ----------------------------------------------------------------------
    python3 tools/dedale/verifier.py nc07      # un nerf
    python3 tools/dedale/verifier.py --tous    # tous les nerfs présents dans assets/nc/
Contrôles (ÉCHEC = code de sortie 1) :
  V1 couches : trait, nerf, noyaux, foramens, territoires, lesions, legendes présentes (même vides) ;
  V2 lisibilité : tout texte mesure au moins 9 px une fois l'image réduite à 360 px de large ;
  V3 poids : au plus 120 Ko par vue SVG, au plus 200 Ko pour un sprite WebP (budget de la CI) ;
  V4 crédits : entrée complète dans assets/nc/credits.json (TASL, licence, « Œuvre dérivée »,
     modifications, date, genere_par_ia faux, valide_par_vial présent) et métadonnées dans le SVG ;
  V5 couleur : le vert du nerf (#156534) est la seule couleur ; le rouge (#b91c1c) n'apparaît que
     dans la couche lesions ; aucune image matricielle intégrée (pas de pixel généré) ;
  V6 annotations : chaque entrée de nc/annot/<nerf>.yml a un identifiant, un libellé et une source ;
  V7 rejouabilité : la recomposition par annoter.py redonne chaque SVG à l'octet près
     (sauf --sans-rejeu, quand svgo 4.0.0 n'est pas installé).
"""
import json, os, re, subprocess, sys
import yaml

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
NC = os.path.join(ROOT, 'assets', 'nc')
COUCHES = ('trait', 'nerf', 'noyaux', 'foramens', 'territoires', 'lesions', 'legendes')
CHAMPS = ('fichier', 'titre', 'auteur', 'source', 'source_url', 'url', 'licence', 'licence_url', 'licence_derivee', 'derive', 'mention',
          'modifications', 'verifie_le', 'valide_par_vial', 'genere_par_ia', 'oeuvre_derivee')
GRIS = re.compile(r'^#([0-9a-f])\1\1$|^#([0-9a-f]{2})\2\2$', re.I)
fails = []


def ko(p):
    return os.path.getsize(p) / 1024


def check(cond, msg):
    if not cond:
        fails.append(msg)
    return cond


def svg_vue(nerf, p, credits):
    rel = os.path.relpath(p, ROOT)
    s = open(p, encoding='utf-8').read()
    for c in COUCHES:
        check(re.search(r'<g[^>]*\bid="%s"' % c, s), '%s : couche « %s » absente (V1)' % (rel, c))
    vb = re.search(r'viewBox="0 0 ([\d.]+) ([\d.]+)"', s)
    if check(vb, '%s : viewBox absente' % rel):
        k = 360 / float(vb.group(1))
        tailles = [float(x) for x in re.findall(r'font-size:([\d.]+)px', s)]
        check(tailles and min(tailles) * k >= 9, '%s : texte de %.1f px à 360 px de large, minimum 9 (V2)'
              % (rel, (min(tailles) if tailles else 0) * k))
    check(ko(p) <= 120, '%s : %.0f Ko, plafond 120 (V3)' % (rel, ko(p)))
    check('<image' not in s and 'data:image' not in s, '%s : image matricielle intégrée interdite (V5)' % rel)
    for col in set(re.findall(r'#[0-9a-fA-F]{3,6}\b', s)):
        c = col.lower()
        if c in ('#156534',) or GRIS.match(c):
            continue
        if c == '#b91c1c':
            les = re.search(r'<g[^>]*id="lesions".*?</g>', s, re.S)
            check(les and c in les.group(0).lower() and s.lower().count(c) == les.group(0).lower().count(c),
                  '%s : rouge hors de la couche lesions (V5)' % rel)
            continue
        check(False, '%s : couleur %s non autorisée (V5)' % (rel, col))
    check('Œuvre dérivée' in s and 'CC BY-SA 4.0' in s, '%s : mention « Œuvre dérivée » ou licence absente du SVG (V4)' % rel)
    credit(rel, credits)


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
        vues = (a or {}).get('vues', [])
        for v in vues:
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
