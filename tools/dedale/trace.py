#!/usr/bin/env python3
"""Dédale-T · plan du nerf au crayon à partir d'une planche de Gray (domaine public), par automate.

INSTRUCTIONS (automate, zéro jeton) ------------------------------------------------
    python3 tools/dedale/trace.py /workspace/ssp/nc_src/gray/Gray788.png nc07 --sans-texte
    python3 tools/dedale/trace.py Gray790.png nc07 --masque jaune      # planche colorée : nerf isolé
Entrée  : une planche de Gray téléchargée hors dépôt (licence vérifiée par l'API Commons, nc/sources.yml).
Sortie  : nc/trait/<nerf>-plan.svg (groupes peau = trait de la planche, nerf = masque de couleur s'il y a lieu)
          et nc/trait/<nerf>-plan.json (taille, source, empreinte de la planche).
Méthode : 1. agrandissement ×2 (Lanczos) ; 2. crayon par densité : fondu « dodge » de l'image sur son
          négatif flouté (flou gaussien, rayon 2 px), puis seuil à 225 ; 3. --sans-texte retire les composantes
          connexes isolées de la taille d'une lettre (légendes anglaises de 1918), en gardant les tirets et
          les points ; 4. --masque <couleur> isole le nerf d'une planche colorée (teinte HSV) ;
          5. vectorisation potrace (-t 6 -a 1 -O 0.4), coordonnées au dixième de pixel.
          Le résultat est déterministe (aucun aléa) ; annoter.py compose ensuite la vue « plan ».
Interdits : aucune retouche à la main ; aucune planche sans licence compatible.
"""
import hashlib, json, os, re, subprocess, sys, tempfile
from collections import deque
from PIL import Image, ImageFilter, ImageChops
import numpy as np

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
TEINTES = {'jaune': (35, 70), 'rouge': (-15, 15), 'bleu': (190, 250), 'vert': (80, 160)}


def crayon(g, rayon=2, seuil=225):
    a = np.asarray(g, dtype=np.float32)
    inv = Image.fromarray((255 - a).astype(np.uint8)).filter(ImageFilter.GaussianBlur(rayon))
    b = np.asarray(inv, dtype=np.float32)
    dodge = np.clip(a * 255.0 / np.maximum(1.0, 255.0 - b), 0, 255)
    return dodge < seuil


def composantes(m):
    h, w = m.shape
    lab = np.zeros((h, w), dtype=np.int32)
    out, n = [], 0
    ys, xs = np.nonzero(m)
    for y0, x0 in zip(ys, xs):
        if lab[y0, x0]:
            continue
        n += 1; q = deque([(y0, x0)]); lab[y0, x0] = n; px = []
        while q:
            y, x = q.popleft(); px.append((y, x))
            for dy in (-1, 0, 1):
                for dx in (-1, 0, 1):
                    yy, xx = y + dy, x + dx
                    if 0 <= yy < h and 0 <= xx < w and m[yy, xx] and not lab[yy, xx]:
                        lab[yy, xx] = n; q.append((yy, xx))
        py = [p[0] for p in px]; pxx = [p[1] for p in px]
        out.append((min(py), max(py), min(pxx), max(pxx), px))
    return out


def sans_texte(g, m, k):
    """Retire les composantes isolées de la taille d'une lettre ou d'un point (légendes anglaises de 1918).

    Les composantes sont cherchées sur la planche seuillée (avant le crayon, qui fragmente les lettres) ;
    une composante est du texte si sa hauteur va de 2,5 à 15 px et sa largeur au plus 22 px (échelle 1),
    ou si c'est un point isolé (au plus 4 px de côté). Les tirets plus longs (nerfs en pointillés) restent.
    Limite connue : un mot cursif lié ou une lettre collée à un trait reste (ex. « Small », « Petro » sur Gray788) ;
    on ne l'efface pas, car une règle plus large retirait aussi des ganglions (essai du 17.10.2026).
    """
    m0 = np.asarray(g, dtype=np.uint8) < 170
    txt = np.zeros_like(m0); n = 0
    for y0, y1, x0, x1, px in composantes(m0):
        hh, ww = (y1 - y0 + 1) / k, (x1 - x0 + 1) / k
        if (2.5 < hh <= 15 and ww <= 22) or (hh <= 4 and ww <= 4):
            for y, x in px:
                txt[y, x] = True
            n += 1
    txt = np.asarray(Image.fromarray(txt.astype(np.uint8) * 255).filter(ImageFilter.MaxFilter(5))) > 0
    return m & ~txt, n


def masque(rgb, nom):
    hsv = np.asarray(rgb.convert('HSV'), dtype=np.float32)
    h = hsv[..., 0] * 360 / 255; s = hsv[..., 1]; v = hsv[..., 2]
    lo, hi = TEINTES[nom]
    hh = np.where(h > 300, h - 360, h) if lo < 0 else h
    return (hh >= lo) & (hh <= hi) & (s > 70) & (v > 60)


def potrace(m):
    with tempfile.TemporaryDirectory() as d:
        pbm = os.path.join(d, 'a.pbm'); svg = os.path.join(d, 'a.svg')
        Image.fromarray(np.where(m, 0, 255).astype(np.uint8)).convert('1').save(pbm)
        subprocess.run(['potrace', pbm, '-s', '--flat', '-t', '6', '-a', '1', '-O', '0.4', '-u', '10', '-o', svg], check=True)
        s = open(svg).read()
    tr = re.search(r'transform="([^"]+)"', s).group(1)
    ds = re.findall(r' d="([^"]+)"', s)
    return tr, ' '.join(d.replace('\n', ' ') for d in ds)


def main():
    args = sys.argv[1:]
    src, nerf = args[0], args[1]
    k = 2
    im = Image.open(src)
    rgb = im.convert('RGB')
    rgb2 = rgb.resize((rgb.width * k, rgb.height * k), Image.LANCZOS)
    g = rgb2.convert('L')
    m = crayon(g)
    nerf_m = None
    if '--masque' in args:
        nerf_m = masque(rgb2, args[args.index('--masque') + 1])
        m = m & ~nerf_m
    retire = 0
    if '--sans-texte' in args:
        m, retire = sans_texte(g, m, k)
    W, H = g.size
    tr, d = potrace(m)
    grp = '<g id="peau"><path transform="%s" d="%s"/></g>' % (tr, d)
    if nerf_m is not None:
        tr2, d2 = potrace(nerf_m)
        grp += '<g id="nerf"><path transform="%s" d="%s"/></g>' % (tr2, d2)
    else:
        grp += '<g id="nerf"></g>'
    out = os.path.join(ROOT, 'nc', 'trait', '%s-plan' % nerf)
    open(out + '.svg', 'w', encoding='utf-8', newline='\n').write(
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %d %d" data-nerf="%s" data-vue="plan">%s</svg>\n' % (W, H, nerf, grp))
    json.dump({'nerf': nerf, 'vue': 'plan', 'taille': [W, H], 'echelle': k, 'source': os.path.basename(src),
               'sha256_source': hashlib.sha256(open(src, 'rb').read()).hexdigest(),
               'composantes_texte_retirees': retire, 'masque': args[args.index('--masque') + 1] if '--masque' in args else None,
               'ancres': {}}, open(out + '.json', 'w', encoding='utf-8', newline='\n'), ensure_ascii=False, indent=1, sort_keys=True)
    print('Dédale-T : %s-plan.svg (%d octets), %d composantes de texte retirées' % (nerf, os.path.getsize(out + '.svg'), retire))


if __name__ == '__main__':
    main()
