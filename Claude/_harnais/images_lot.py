#!/usr/bin/env python3
"""IMAGES_LOT — quête d'images automatisée et gratuite (zéro modèle) pour tout un LOT.

Pour chaque requête (une par DX ou par structure), interroge Wikimedia Commons via cliche.py (licences libres seules),
télécharge la vignette, mesure la saturation des couleurs (consigne 8 bis : couleurs d'abord), classe les candidats
(Blausen, OpenStax, PMC en tête ; noir et blanc en dernier), met tout en cache et produit UNE planche HTML :
l'humain ou l'agent choisit d'un coup d'œil, puis `cliche.py prendre` + `cliche.py figure` (repères).

Usage : python3 Claude/_harnais/images_lot.py --lot 25 --requetes "Blausen salivary glands" "OpenStax pharynx" …
        python3 Claude/_harnais/images_lot.py --lot 25 --fichier requetes.txt     (une requête par ligne : « DX.n | requête »)
Sortie : Claude/LOT_0NN/images/_candidats/planche.html (+ candidats.json) ; cache ~/.cache/medina_images.
"""
import sys, os, json, re, io, html, hashlib, argparse, urllib.request
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '_outils'))
import cliche  # noqa: E402

CACHE = os.environ.get('IMAGES_CACHE', os.path.expanduser('~/.cache/medina_images'))
PRIO = re.compile(r'Blausen|OpenStax|^File:\d{4} |PMC|Anatomy & Physiology', re.I)


def saturation(url):
    os.makedirs(CACHE, exist_ok=True)
    f = os.path.join(CACHE, hashlib.sha1(url.encode()).hexdigest() + '.jpg')
    try:
        if not os.path.exists(f):
            u = re.sub(r'/\d+px-', '/120px-', url)
            req = urllib.request.Request(u, headers={'User-Agent': 'medina-images/1.0 (cours pedagogiques)'})
            open(f, 'wb').write(urllib.request.urlopen(req, timeout=15).read())
        from PIL import Image
        im = Image.open(f).convert('HSV').resize((64, 64))
        s = [p[1] for p in im.getdata()]
        return round(sum(s) / len(s) / 255, 3), f
    except Exception:
        return 0.0, None


def requete(q, n=8):
    cle = os.path.join(CACHE, 'q_' + hashlib.sha1(q.encode()).hexdigest() + '.json')
    if os.path.exists(cle):
        return json.load(open(cle))
    R = [r for r in cliche.chercher(q, n) if r.get('libre')]
    for r in R:
        r['saturation'], r['local'] = saturation(r['vignette']) if r.get('vignette') else (0, None)
        r['prioritaire'] = bool(PRIO.search(r['titre'] + ' ' + (r.get('auteur') or '')))
        r['couleur'] = (r['saturation'] >= 0.12) if r['local'] else None   # None : vignette non lue (débit limité)
        r['score'] = round(r['saturation'] + (0.5 if r['prioritaire'] else 0) + {True: 0.2, False: -0.5, None: 0}[r['couleur']], 3)
    R.sort(key=lambda r: -r['score'])
    os.makedirs(CACHE, exist_ok=True); json.dump(R, open(cle, 'w'), ensure_ascii=False)
    return R


if __name__ == '__main__':
    ap = argparse.ArgumentParser(); ap.add_argument('--lot', type=int, required=True)
    ap.add_argument('--requetes', nargs='*', default=[]); ap.add_argument('--fichier'); ap.add_argument('-n', type=int, default=8)
    a = ap.parse_args()
    Q = [('', q) for q in a.requetes]
    if a.fichier:
        Q += [tuple(x.strip() for x in l.split('|', 1)) if '|' in l else ('', l.strip()) for l in open(a.fichier) if l.strip()]
    out = f'Claude/LOT_{a.lot:03d}/images/_candidats'; os.makedirs(out, exist_ok=True)
    tout = []; blocs = []
    for etiq, q in Q:
        R = requete(q, a.n); tout.append(dict(dx=etiq, requete=q, candidats=R))
        cases = ''.join(f'<figure style="width:180px;margin:6px;display:inline-block;vertical-align:top">'
                        f'<img src="{html.escape(r["vignette"] or "")}" style="width:180px;height:140px;object-fit:contain;background:#fff">'
                        f'<figcaption style="font-size:11px">{ {True: "🎨", False: "⚫", None: "❔"}[r["couleur"]] } {html.escape(r["titre"][5:60])}<br>{html.escape(r["licence"])} · score {r["score"]}</figcaption></figure>'
                        for r in R)
        blocs.append(f'<h2>{html.escape(etiq)} {html.escape(q)}</h2>{cases or "<p>aucun candidat libre</p>"}')
    json.dump(tout, open(out + '/candidats.json', 'w'), ensure_ascii=False, indent=1)
    open(out + '/planche.html', 'w').write('<!doctype html><meta charset="utf-8"><title>Candidats images</title>'
                                           '<body style="font:14px system-ui;background:#f6fbff;margin:16px">' + ''.join(blocs))
    print(out + '/planche.html', sum(len(t['candidats']) for t in tout), 'candidats')
