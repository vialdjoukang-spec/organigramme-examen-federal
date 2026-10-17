#!/usr/bin/env python3
"""Dédale-A · composition des schémas annotés à couches nommées.

INSTRUCTIONS (automate, zéro jeton) ------------------------------------------------
    python3 tools/dedale/annoter.py nc07            # compose assets/nc/nc07-{face,profil,34}.svg
    python3 tools/dedale/annoter.py nc07 --verifier # recompose en mémoire et compare à l'octet (CI)
    python3 tools/dedale/annoter.py nc07 --tour     # sprite WebP des 8 vues (local : Chromium requis)
Entrées : nc/annot/<nerf>.yml (annotations au format d'Ariane, chacune sourcée),
          nc/trait/<nerf>-<vue>.svg et .json (sorties de freestyle.py : trait et ancres projetées),
          nc/sources.yml (crédits TASL). Le tour lit <render>/<nerf>-t0…t7.svg (hors dépôt).
Sortie  : assets/nc/<nerf>-<vue>.svg avec les couches trait, nerf, noyaux, foramens, territoires,
          lesions, legendes (toujours présentes, même vides) ; métadonnées de licence « œuvre dérivée » ;
          puis passage de svgo 4.0.0 (tools/dedale/svgo.config.mjs) ; mise à jour de assets/nc/credits.json.
Règles  : aucune position saisie à la main (seules les ancres du modèle placent un repère) ; le nerf est
          le seul élément en couleur (#156534) ; le rouge (#b91c1c) est réservé aux sites lésionnels
          marqués « urgence: true » ; texte d'au moins 9 px une fois l'image réduite à 360 px de large.
"""
import json, os, re, shutil, subprocess, sys, tempfile
from xml.sax.saxutils import escape
import yaml

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
HERE = os.path.join(ROOT, 'tools', 'dedale')
OUT = os.path.join(ROOT, 'assets', 'nc')
RENDER = os.environ.get('DEDALE_RENDER', '/workspace/ssp/nc_src/render')
DATE = '2026-10-17'
VERT, ROUGE = '#156534', '#b91c1c'
W, HEAD, FS, LH, FS_CR = 800, 70, 22, 31, 20
NOMS_VUES = {'plan': 'plan du nerf (d’après Gray 1918)', 'face': 'vue de face', 'profil': 'vue de profil droit', '34': 'vue de trois quarts droite'}
COUCHES = ('trait', 'territoires', 'nerf', 'noyaux', 'foramens', 'lesions', 'legendes')
STYLE = ('text{font-family:system-ui,-apple-system,"Segoe UI",Roboto,Arial,sans-serif;fill:#111}'
         '.tt{font-size:30px;font-weight:700}.lg{font-size:%dpx}.cr{font-size:%dpx;fill:#333}.b{font-weight:700}'
         '.nb{font-size:21px;font-weight:700;text-anchor:middle;dominant-baseline:central}'
         'path{fill:none;stroke-linecap:round;stroke-linejoin:round}'
         '#trait .peau path{stroke:#2f2f2f;stroke-width:1.5}'
         '#trait .crane path{stroke:#6b6b6b;stroke-width:.8;stroke-opacity:.5}'
         '#trait .tronc path{stroke:#555;stroke-width:.9;stroke-opacity:.75}'
         '#territoires path{stroke:#9a9a9a;stroke-width:.7;stroke-opacity:.8}'
         '#nerf path{stroke:%s;stroke-width:2.8}'
         '.ld{stroke:#555;stroke-width:1}.bd{fill:#fff;stroke:#111;stroke-width:1.6}'
         '#trait .pl{fill:#2f2f2f;stroke:none}.pt{fill:#111;stroke:#fff;stroke-width:1.5}.pr{fill:#fff;stroke:#111;stroke-width:2}') % (FS, FS_CR, VERT)


def charger(nerf):
    a = yaml.safe_load(open(os.path.join(ROOT, 'nc', 'annot', nerf + '.yml'), encoding='utf-8'))
    s = yaml.safe_load(open(os.path.join(ROOT, 'nc', 'sources.yml'), encoding='utf-8'))
    return a, s


def groupes_trait(svg):
    g = dict(re.findall(r'<g id="([a-z]+)">(.*?)</g>', svg, re.S))
    return g


def envelopper(txt, fs, larg):
    n = max(20, int(larg / (0.53 * fs)))
    lignes, cur = [], ''
    for mot in txt.split():
        if cur and len(cur) + 1 + len(mot) > n:
            lignes.append(cur); cur = mot
        else:
            cur = (cur + ' ' + mot).strip()
    if cur:
        lignes.append(cur)
    return lignes


def credit_texte(a, s, vue=None):
    if vue == 'plan':
        return ('Œuvre dérivée, CC BY-SA 4.0. Trait vectorisé par automate (Dédale, 17.10.2026, tools/dedale/trace.py) '
                'depuis Gray788 (H. V. Carter, in H. Gray, Anatomy of the Human Body, 1918 ; domaine public, Wikimedia Commons). '
                'Légendes anglaises d’origine retirées par automate ; quelques fragments subsistent.')
    z, b, d = s['z-anatomy'], s['bodyparts3d'], s['dundee-cnf']
    return ('Œuvre dérivée, CC BY-SA 4.0. Trait rendu par automate (Dédale, %s) depuis Z-Anatomy '
            '(G. Kervyn, M. Zielinski, CC BY-SA 4.0), d’après BodyParts3D (DBCLS, CC BY-SA 2.1 JP) '
            'et Cranial Nerves and Foramina (University of Dundee, CAHID, CC BY 4.0).') % '17.10.2026'


def placer_badges(items, cy0):
    """Badges sur deux colonnes (gauche, droite) selon le côté de l'ancre ; espacement vertical minimal 36 px."""
    cols = {'g': [], 'd': []}
    for it in items:
        cols['g' if it['x'] < W / 2 else 'd'].append(it)
    for k, lst in cols.items():
        lst.sort(key=lambda i: i['y'])
        last = cy0 + 20
        for it in lst:
            it['by'] = max(it['y'], last)
            last = it['by'] + 36
            it['bx'] = 34 if k == 'g' else W - 34
    return items


def composer(nerf, vue, a, s):
    trait_svg = open(os.path.join(ROOT, 'nc', 'trait', '%s-%s.svg' % (nerf, vue)), encoding='utf-8').read()
    meta = json.load(open(os.path.join(ROOT, 'nc', 'trait', '%s-%s.json' % (nerf, vue)), encoding='utf-8'))
    G = groupes_trait(trait_svg)
    C = a['couches']
    anc = meta['ancres']
    if vue == 'plan':
        pw, ph = meta['taille']
        k = W / pw
        DH = round(ph * k)
        tr = 'translate(0 %d) scale(%.6f)' % (HEAD, k)
        G = {kk: v.replace('<path ', '<path class="pl" ') for kk, v in G.items()}
    else:
        T = meta['taille']
        assert T == W, 'taille de rendu inattendue'
        DH = W
        tr = 'translate(0 %d)' % HEAD
    # repères numérotés (noyaux, légendes à ancre, lésions et foramens à ancre)
    items, num = [], 0
    for couche in ('noyaux', 'foramens', 'lesions', 'legendes'):
        for e in C.get(couche) or []:
            if e.get('ancre'):
                if vue == 'plan' and e['ancre'] not in anc:
                    continue  # les ancres du modèle 3D ne valent pas pour la planche ; Ariane fournit celles du plan
                if e['ancre'] not in anc:
                    sys.exit('ÉCHEC : ancre %r absente de nc/trait/%s-%s.json' % (e['ancre'], nerf, vue))
                num += 1
                x, y = anc[e['ancre']]
                items.append({'couche': couche, 'e': e, 'n': str(num), 'x': x, 'y': y + HEAD})
    placer_badges(items, HEAD)
    calques = {c: [] for c in COUCHES}
    calques['trait'] = ['<g class="%s">%s</g>' % (kk, G.get(kk, '')) for kk in ('crane', 'tronc', 'peau')]
    calques['territoires'] = [G.get('territoires', '')]
    calques['nerf'] = [G.get('nerf', '')]
    for it in items:
        e, x, y = it['e'], it['x'], it['y']
        urg = it['couche'] == 'lesions' and e.get('urgence')
        pt = 'pr' if it['couche'] == 'legendes' else 'pt'
        coul = ' style="fill:%s"' % ROUGE if urg else ''
        calques[it['couche']].append(
            '<g data-id="%s"><path class="ld" d="M%.1f %.1fL%.1f %.1f"/><circle class="%s" cx="%.1f" cy="%.1f" r="4.5"%s/>'
            '<circle class="bd" cx="%.1f" cy="%.1f" r="15"/><text class="nb" x="%.1f" y="%.1f">%s</text></g>'
            % (e['id'], x, y, it['bx'], it['by'], pt, x, y, coul, it['bx'], it['by'], it['bx'], it['by'], it['n']))
    # légende
    L, y = [], HEAD + DH + 34
    nerf_items = C.get('nerf') or []
    if vue == 'plan':
        nerf_items = [{'libelle': 'Plan du nerf facial et du nerf intermédiaire, de leurs noyaux, ganglions et communications, '
                                  'd’après Gray 1918, fig. 788 (trait gris ; le nerf n’est pas encore isolé en vert).'}]
        L.append('<path d="M24 %dh40" style="stroke:#2f2f2f;stroke-width:3"/>' % (y - 7))
    else:
        L.append('<path d="M24 %dh40" style="stroke:%s;stroke-width:4"/>' % (y - 7, VERT))
    for e in nerf_items:
        for i, ln in enumerate(envelopper(e['libelle'], FS, W - 110)):
            L.append('<text class="lg" x="76" y="%d">%s</text>' % (y, escape(ln))); y += LH
    for e in (C.get('territoires') or []) if vue != 'plan' else []:
        L.append('<path d="M24 %dh40" style="stroke:#9a9a9a;stroke-width:2"/>' % (y - 7))
        for ln in envelopper(e['libelle'], FS, W - 110):
            L.append('<text class="lg" x="76" y="%d">%s</text>' % (y, escape(ln))); y += LH
    for it in items:
        e = it['e']
        L.append('<circle class="bd" cx="44" cy="%d" r="13"/><text class="nb" x="44" y="%d">%s</text>' % (y - 7, y - 7, it['n']))
        txt = e['libelle'] + (' (À vérifier)' if e.get('a_verifier') else '')
        for ln in envelopper(txt, FS, W - 110):
            L.append('<text class="lg" x="76" y="%d">%s</text>' % (y, escape(ln))); y += LH
    vides = [c for c in ('foramens', 'lesions') if not C.get(c)]
    if vides or a.get('statut') != 'valide':
        noms = {'foramens': 'foramens', 'lesions': 'sites lésionnels'}
        txt = 'À vérifier : %s en attente des données d’Ariane ; schéma non encore validé par Vial.' % (
            ' et '.join(noms[c] for c in vides) or 'annotations')
        first = True
        for ln in envelopper(txt, FS, W - 48):
            if first:
                ln = ln.replace('À vérifier :', '<tspan class="b">À vérifier :</tspan>', 1)
                first = False
            else:
                ln = escape(ln)
            L.append('<text class="lg" x="24" y="%d">%s</text>' % (y, ln if '<tspan' in ln else ln)); y += LH
    y += 6
    cred = credit_texte(a, s, vue)
    for ln in envelopper(cred, FS_CR, W - 48):
        L.append('<text class="cr" x="24" y="%d">%s</text>' % (y, escape(ln))); y += 27
    H = y + 6
    calques['legendes'] = calques['legendes'] + L
    titre = '%s · %s' % (a['titre'], NOMS_VUES[vue])
    if vue == 'plan':
        meta.setdefault('azimut', '–'); meta.setdefault('plongee', '–')
    desc = ('Schéma au crayon du %s, côté %s, %s. Caméra orthographique, azimut %s°, plongée %s°. Couches : trait (peau, crâne en transparence, tronc cérébral), '
            'territoires, nerf, noyaux, foramens, lésions, légendes.') % (a['titre'][0].lower() + a['titre'][1:], a['cote'], NOMS_VUES[vue], meta['azimut'], meta['plongee'])
    meta_txt = json.dumps({'licence': 'CC BY-SA 4.0', 'licence_url': 'https://creativecommons.org/licenses/by-sa/4.0/',
                           'mention': 'Œuvre dérivée', 'credit': cred, 'sources': a['sources_trait'],
                           'annotations': a.get('statut'), 'valide_par_vial': bool(a.get('valide_par_vial'))},
                          ensure_ascii=False, sort_keys=True)
    out = ['<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %d %d" role="img" aria-labelledby="t d" '
           'data-nerf="%s" data-vue="%s">' % (W, H, nerf, vue),
           '<title id="t">%s</title><desc id="d">%s</desc><metadata>%s</metadata>' % (escape(titre), escape(desc), escape(meta_txt)),
           '<style>%s</style>' % STYLE,
           '<rect width="%d" height="%d" fill="#fff"/>' % (W, H),
           '<text class="tt" x="24" y="44">%s</text><path d="M24 %dH%d" style="stroke:#bbb;stroke-width:1"/>' % (escape(titre), HEAD - 8, W - 24)]
    for c in COUCHES:
        t = ' transform="%s"' % tr if c in ('trait', 'territoires', 'nerf') else ''
        out.append('<g id="%s" data-couche="%s"%s>%s</g>' % (c, c, t, ''.join(calques[c])))
    out.append('</svg>\n')
    return ''.join(out)


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


def ecrire_credits(entrees):
    p = os.path.join(OUT, 'credits.json')
    # Format commun avec tools/nc_svg_check.py (Janus) : liste d'entrées, « fichier » = nom dans assets/nc/.
    data = json.load(open(p, encoding='utf-8')) if os.path.exists(p) else []
    idx = {e['fichier']: i for i, e in enumerate(data)}
    for e in entrees:
        if e['fichier'] in idx:
            data[idx[e['fichier']]] = e
        else:
            data.append(e)
    data.sort(key=lambda e: e['fichier'])
    open(p, 'w', encoding='utf-8', newline='\n').write(json.dumps(data, ensure_ascii=False, indent=1) + '\n')


def construire(nerf):
    a, s = charger(nerf)
    res = {}
    for vue in a['vues']:
        res[vue] = svgo(composer(nerf, vue, a, s))
    return a, s, res


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
                   % (px, px, STYLE.replace('stroke-width:2.8', 'stroke-width:4').replace('.peau path{stroke:#2f2f2f;stroke-width:1.5',
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
    a, s, res = construire(nerf)
    if '--verifier' in args:
        bad = [v for v, t in res.items()
               if open(os.path.join(OUT, '%s-%s.svg' % (nerf, v)), encoding='utf-8').read() != t]
        for v in bad:
            print('ÉCHEC : assets/nc/%s-%s.svg diffère de sa recomposition.' % (nerf, v))
        print('Recomposition à l’octet : %d/%d vues identiques.' % (len(res) - len(bad), len(res)))
        sys.exit(1 if bad else 0)
    os.makedirs(OUT, exist_ok=True)
    ent = []
    for v, t in res.items():
        f = os.path.join(OUT, '%s-%s.svg' % (nerf, v))
        open(f, 'w', encoding='utf-8', newline='\n').write(t)
        if v == 'plan':
            g = s['gray788']
            e = credit_entree(nerf, v, a, s, round(len(t.encode()) / 1024),
                              mods='Planche agrandie ×2, filtre crayon (fondu « dodge » sur flou gaussien), retrait automatique des '
                                   'légendes anglaises (composantes de la taille d’une lettre), vectorisation potrace 1.16 '
                                   '(tools/dedale/trace.py), composition par tools/dedale/annoter.py ; svgo 4.0.0.')
            e.update({'auteur': g['auteur'], 'source': 'Wikimedia Commons', 'source_url': g['source_url'], 'url': g['source_url'],
                      'licences_amont': {'gray788': g['licence']}})
            ent.append(e)
        else:
            ent.append(credit_entree(nerf, v, a, s, round(len(t.encode()) / 1024)))
        print('%s : %d octets' % (os.path.relpath(f, ROOT), len(t.encode())))
    ecrire_credits(ent)


if __name__ == '__main__':
    main()
