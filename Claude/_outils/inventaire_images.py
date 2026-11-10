#!/usr/bin/env python3
"""INVENTAIRE_IMAGES — compte rendu des images, imageries et clichés d'UN LOT (zéro modèle), sur la version la plus avancée
de chaque leçon (carte de detecteur_lots.py). Un clone par LOT tourne en parallèle ; agréger avec --agreger.
Pour chaque figure : type (img fichier, img data:, svg), modalité devinée, légende, interprétation guidée (verbes de lecture,
repères, flèches), source et licence, point d'insertion (n° du point µ3).
Usage : inventaire_images.py --carte carte.json --lot 133 --sortie dir/   |   --agreger dir/ --html rapport.html"""
import re, sys, json, html, argparse, subprocess, os, glob, collections

MOD = [('ECG', r'\bECG|électrocardiogramme'), ('radiographie', r'radiograph|cliché|thorax de face|ASP\b|rx\b'),
       ('scanner', r'scanner|tomodensitom|\bTDM\b|\bCT\b|angio-?CT'), ('IRM', r'\bIRM\b|IRM|résonance magnétique|\bMRI\b'),
       ('échographie', r'échograph|ultrason|doppler|\bPOCUS\b|ETT\b|ETO\b'), ('endoscopie', r'endoscop|coloscop|gastroscop|bronchoscop'),
       ('histologie', r'histolog|biopsie|microscop|frottis|coloration'), ('photo clinique', r'photograph|lésion cutanée|aspect clinique|dermatos'),
       ('schéma', r'schéma|diagramme|algorithme|mécanisme|anatomie')]
INTERP = re.compile(r'\b(on (?:voit|observe|note|distingue)|montre|flèche|repère|noter|remarquer|signe (?:de|du)|à comparer|'
                    r'aspect (?:typique|en)|la lecture|interprét|met en évidence|visible|opacité|hyper|hypo(?:échog|dens|signal))', re.I)
LIC = re.compile(r'CC[- ]?BY(?:[- ]SA)?(?:[- ]\d\.\d)?|CC0|domaine public|public domain', re.I)


def point_de(h, pos):
    m = None
    for m in re.finditer(r'<h[23][^>]*>\s*(?:<[^>]+>\s*)*(\d{1,2})[.\s]', h[:pos]):
        pass
    return int(m.group(1)) if m else None


def analyser(h):
    figs = []
    for m in re.finditer(r'<figure\b.*?</figure>|<img\b[^>]*>|<svg\b.*?</svg>', h, re.S | re.I):
        b = m.group(0)
        if b.lower().startswith('<img') and any(f['debut'] <= m.start() < f['fin'] for f in figs):
            continue
        cap = re.search(r'<figcaption[^>]*>(.*?)</figcaption>', b, re.S)
        alt = re.search(r'alt="([^"]*)"', b)
        leg = re.sub(r'\s+', ' ', html.unescape(re.sub(r'<[^>]+>', ' ', (cap.group(1) if cap else '') or (alt.group(1) if alt else '')))).strip()
        src = re.search(r'src="([^"]{0,120})', b)
        typ = 'svg' if '<svg' in b[:5].lower() or b.lower().startswith('<svg') else ('data:' if src and src.group(1).startswith('data:') else 'fichier' if src else '?')
        ctx = re.sub(r'<[^>]+>', ' ', h[max(0, m.start() - 600):m.end() + 600])
        mods = [k for k, r in MOD if re.search(r, leg + ' ' + (ctx if not leg else ''), re.I)]
        figs.append({'debut': m.start(), 'fin': m.end(), 'type': typ, 'modalites': mods, 'legende': leg[:300],
                     'interpretation_guidee': bool(INTERP.search(leg)), 'licence': (LIC.search(b) or LIC.search(ctx) or [None])[0],
                     'source': bool(re.search(r'https?://|Wikimedia|Europe PMC|PMC\d|Radiopaedia|auteur', b, re.I)),
                     'point': point_de(h, m.start()), 'octets': len(b)})
    liens_cas = len(re.findall(r'radiopaedia\.org|eurorad\.org|radiologyassistant|ultrasoundcases', h, re.I))
    for f in figs:
        del f['debut'], f['fin']
    return figs, liens_cas


def lot(carte, n, sortie):
    C = json.load(open(carte))['lecons']
    res = {'lot': n, 'lecons': {}}
    for k, v in sorted(C.items()):
        if int(k[:3]) != n:
            continue
        h = subprocess.run(['git', 'cat-file', 'blob', v['blob']], capture_output=True).stdout.decode('utf-8', 'ignore')
        figs, liens = analyser(h)
        res['lecons'][k[4:]] = {'ia': v.get('auteur_ia', v['ia']), 'chemin': v['chemin'], 'ref': v['ref'], 'figures': figs, 'liens_cas': liens}
    os.makedirs(sortie, exist_ok=True)
    json.dump(res, open(f'{sortie}/LOT_{n:03d}.json', 'w'), ensure_ascii=False, indent=1)


def agreger(d, out):
    L = [json.load(open(f)) for f in sorted(glob.glob(f'{d}/LOT_*.json'))]
    tot = collections.Counter(); mods = collections.Counter(); ia = collections.Counter(); ex = []
    for r in L:
        for c, le in r['lecons'].items():
            tot['lecons'] += 1
            tot['lecons_avec_figure'] += bool(le['figures'])
            tot['liens_cas'] += le['liens_cas']
            for f in le['figures']:
                tot['figures'] += 1; tot[f'type_{f["type"]}'] += 1
                tot['avec_interpretation'] += f['interpretation_guidee']; tot['avec_licence'] += bool(f['licence'])
                tot['avec_source'] += f['source']; tot['avec_legende'] += bool(f['legende'])
                ia[le['ia']] += 1
                for m in f['modalites'] or ['non déterminée']:
                    mods[m] += 1
                if f['interpretation_guidee'] and f['type'] != 'svg' and len(ex) < 25:
                    ex.append((r['lot'], c, f['legende']))
    rows = ''.join(f'<tr><td>{k}</td><td>{v}</td></tr>' for k, v in tot.items())
    rm = ''.join(f'<tr><td>{k}</td><td>{v}</td></tr>' for k, v in mods.most_common())
    ri = ''.join(f'<tr><td>{k}</td><td>{v}</td></tr>' for k, v in ia.most_common())
    re_ = ''.join(f'<li><b>LOT_{a:03d} {c}</b> — {html.escape(l)}</li>' for a, c, l in ex)
    open(out, 'w').write(f'<!DOCTYPE html><html lang="fr"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Inventaire images</title>'
                         '<style>body{font:15px/1.5 Georgia,serif;max-width:900px;margin:auto;padding:16px;background:#f6f7f9;color:#2e3440}table{border-collapse:collapse}td{border:1px solid #ddd;padding:3px 8px}</style></head><body>'
                         f'<h1>Inventaire des images — LOTs {L[0]["lot"]:03d} à {L[-1]["lot"]:03d}</h1><h2>Totaux</h2><table>{rows}</table><h2>Modalités</h2><table>{rm}</table>'
                         f'<h2>Figures par IA auteur</h2><table>{ri}</table><h2>Exemples d’interprétation guidée</h2><ul>{re_}</ul></body></html>')
    json.dump({'totaux': tot, 'modalites': mods, 'par_ia': ia, 'exemples': ex}, open(out.replace('.html', '.json'), 'w'), ensure_ascii=False, indent=1)
    print(dict(tot)); print(mods.most_common()); print(ia.most_common())


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('--carte'); ap.add_argument('--lot', type=int); ap.add_argument('--sortie')
    ap.add_argument('--agreger'); ap.add_argument('--html')
    a = ap.parse_args()
    agreger(a.agreger, a.html) if a.agreger else lot(a.carte, a.lot, a.sortie)
