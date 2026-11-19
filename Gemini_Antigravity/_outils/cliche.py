#!/usr/bin/env python3
"""CLICHE — images médicales sourcées, interprétées et juxtaposées au texte (µ6 v2). Une image n'est jamais une décoration :
elle montre ce que le point enseigne, et le lecteur apprend à la lire.
  chercher  "<requête anglaise>" [--n 8]          → candidats Wikimedia Commons (licence de CHAQUE fichier, auteur, URL)
  prendre   "<File:Titre.jpg>" --lot DIR [--largeur 1000]  → images/<nom>.webp + <nom>.json (métadonnées), cache, reprise sur 429
  figure    --meta images/<nom>.json --titre … --cliche … --reperes '[[x%,y%,"texte"],…]' --pieges '[…]' --decision "…"
            → bloc HTML : cliché brut (« cherchez d'abord ») puis copie annotée (repères numérotés en SVG) + lecture guidée
Licences admises : CC0, CC BY, CC BY-SA, domaine public. Refus : NC, ND, inconnue."""
import re, sys, json, time, html, argparse, os, io, urllib.request, urllib.parse
API = 'https://commons.wikimedia.org/w/api.php'
UA = {'User-Agent': 'MedCoursPedago/1.0 (cours medicaux suisses; https://github.com/vialdjoukang-spec/organigramme-examen-federal)'}
LIBRE = re.compile(r'^(cc0|cc[ -]by(?:[ -]sa)?(?:[ -][\d.]+)?|public domain|pd)', re.I)
REFUS = re.compile(r'\bnc\b|\bnd\b', re.I)


def get(url, binaire=False, essais=8):
    for k in range(essais):
        try:
            r = urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=60).read()
            return r if binaire else json.loads(r)
        except urllib.error.HTTPError as e:
            if e.code != 429 or k == essais - 1:
                raise
            time.sleep(min(60, 3 * 2 ** k))


def nettoie(s):
    return re.sub(r'\s+', ' ', html.unescape(re.sub(r'<[^>]+>', ' ', s or ''))).strip()


def infos(pages):
    out = []
    for p in pages:
        ii = (p.get('imageinfo') or [{}])[0]
        m = ii.get('extmetadata', {})
        lic = nettoie(m.get('LicenseShortName', {}).get('value'))
        out.append({'titre': p['title'], 'licence': lic, 'libre': bool(LIBRE.match(lic) and not REFUS.search(lic)),
                    'auteur': nettoie(m.get('Artist', {}).get('value'))[:160], 'url': ii.get('descriptionurl'),
                    'vignette': ii.get('thumburl'), 'description': nettoie(m.get('ImageDescription', {}).get('value'))[:300],
                    'largeur': ii.get('width'), 'hauteur': ii.get('height')})
    return out


def chercher(q, n, largeur=960):
    d = get(API + '?' + urllib.parse.urlencode({'action': 'query', 'generator': 'search', 'gsrsearch': f'filetype:bitmap {q}',
            'gsrnamespace': 6, 'gsrlimit': n, 'prop': 'imageinfo', 'iiprop': 'url|extmetadata|size', 'iiurlwidth': largeur, 'format': 'json'}))
    return infos(d.get('query', {}).get('pages', {}).values())


def prendre(titre, lot, largeur):
    from PIL import Image
    d = get(API + '?' + urllib.parse.urlencode({'action': 'query', 'titles': titre, 'prop': 'imageinfo',
            'iiprop': 'url|extmetadata|size', 'iiurlwidth': largeur, 'format': 'json'}))
    meta = infos(d['query']['pages'].values())[0]
    if not meta['libre']:
        sys.exit(f'REFUS licence : {meta["licence"]}')
    nom = re.sub(r'[^\w.-]+', '_', titre.split(':', 1)[1].rsplit('.', 1)[0])[:60]
    os.makedirs(f'{lot}/images', exist_ok=True)
    dest = f'{lot}/images/{nom}.webp'
    if not os.path.exists(dest):
        im = Image.open(io.BytesIO(get(meta['vignette'], binaire=True))).convert('RGB')
        im.thumbnail((largeur, largeur))
        im.save(dest, 'WEBP', quality=72)
    w, h = Image.open(dest).size
    meta.update({'fichier': f'images/{nom}.webp', 'w': w, 'h': h, 'consulte': time.strftime('%Y-%m-%d')})
    json.dump(meta, open(f'{lot}/images/{nom}.json', 'w'), ensure_ascii=False, indent=1)
    print(json.dumps(meta, ensure_ascii=False))


def figure(a):
    m = json.load(open(a.meta))
    rep = json.loads(a.reperes)
    pieges = json.loads(a.pieges or '[]')
    e = html.escape
    w, h = m['w'], m['h']
    marques = ''.join(f'<circle cx="{x * w / 100:.0f}" cy="{y * h / 100:.0f}" r="{max(w, h) * .035:.0f}" fill="none" stroke="#b00020" '
                      f'stroke-width="{max(w, h) * .006:.1f}" stroke-dasharray="{max(w, h) * .015:.0f}"/><text x="{x * w / 100 + max(w, h) * .04:.0f}" '
                      f'y="{y * h / 100:.0f}" font-size="{max(w, h) * .045:.0f}" font-weight="700" fill="#b00020" stroke="#fff" '
                      f'stroke-width="{max(w, h) * .004:.1f}">{i}</text>' for i, (x, y, _) in enumerate(rep, 1))
    lecture = ''.join(f'<li><b>{i}.</b> {e(t)}</li>' for i, (_, _, t) in enumerate(rep, 1))
    pg = ''.join(f'<li>{e(p)}</li>' for p in pieges)
    print(f'''<figure class="cliche-guide"><p class="p"><b>{e(a.titre)}.</b> {e(a.cliche)}</p>
<div class="paire"><div><img src="{m['fichier']}" width="{w}" height="{h}" alt="{e(a.titre)} — cliché brut" loading="lazy"><p class="p">Lisez d'abord seul ce cliché ({e(a.titre.lower())}) : cherchez vous-même le signe.</p></div>
<div><svg viewBox="0 0 {w} {h}" role="img" aria-label="{e(a.titre)} — copie annotée"><image href="{m['fichier']}" width="{w}" height="{h}"/>{marques}</svg><p class="p">La copie annotée ({e(a.titre.lower())}) numérote les repères décrits ci-dessous.</p></div></div>
<div class="p"><b>Lecture guidée.</b><ol>{lecture}</ol></div>{f'<div class="p"><b>Pièges.</b><ul>{pg}</ul></div>' if pg else ''}
<p class="p"><b>Ce que l'image décide.</b> {e(a.decision)}</p>
<figcaption>Image : {e(m['auteur'] or 'auteur non indiqué')}, {e(m['licence'])}, {e(m.get('source', 'Wikimedia Commons'))}, <a href="{e(m['url'])}">{e(m['titre'])}</a>, consultée le {m['consulte']}. Copie annotée : œuvre dérivée sous la même licence.</figcaption></figure>''')


EPMC = 'https://www.ebi.ac.uk/europepmc/webservices/rest/'


def chercher_pmc(q, n):
    """Articles en accès ouvert sous CC BY / CC0 (licence de l'article qui couvre ses figures) et légendes de leurs figures."""
    d = get(EPMC + 'search?' + urllib.parse.urlencode({'query': f'({q}) AND OPEN_ACCESS:y AND (LICENSE:"cc by" OR LICENSE:"cc0")',
            'format': 'json', 'pageSize': n, 'resultType': 'core'}))
    out = []
    for r in d['resultList']['result']:
        pmc = r.get('pmcid')
        if not pmc:
            continue
        x = urllib.request.urlopen(urllib.request.Request(EPMC + f'{pmc}/fullTextXML', headers=UA), timeout=60).read().decode('utf-8', 'ignore')
        for m in re.finditer(r'<fig\b.*?</fig>', x, re.S):
            g = re.search(r'xlink:href="([^"]+)"', m.group(0))
            if g:
                out.append({'pmcid': pmc, 'licence': r.get('license', '').upper(), 'fichier_source': g.group(1),
                            'titre_article': r['title'][:120], 'legende': nettoie(m.group(0))[:300]})
    return out


def prendre_pmc(pmc, nom_fig, lot, largeur):
    from PIL import Image
    d = get(EPMC + 'search?' + urllib.parse.urlencode({'query': f'PMCID:{pmc}', 'format': 'json', 'resultType': 'core'}))
    r = d['resultList']['result'][0]
    lic = (r.get('license') or '').upper()
    if not re.match(r'^CC(0| BY)(?!.*(NC|ND))', lic):
        sys.exit(f'REFUS licence : {lic}')
    num = pmc.replace('PMC', '')
    url = f'https://pmc.ncbi.nlm.nih.gov/articles/instance/{num}/bin/{nom_fig}'
    os.makedirs(f'{lot}/images', exist_ok=True)
    nom = re.sub(r'[^\w.-]+', '_', f'{pmc}_{nom_fig.rsplit(".", 1)[0]}')[:60]
    dest = f'{lot}/images/{nom}.webp'
    if not os.path.exists(dest):
        im = Image.open(io.BytesIO(get(url, binaire=True))).convert('RGB')
        im.thumbnail((largeur, largeur))
        im.save(dest, 'WEBP', quality=72)
    w, h = Image.open(dest).size
    auteurs = r.get('authorString', '')
    meta = {'titre': f'{r["title"]} — {nom_fig}', 'licence': lic, 'libre': True,
            'auteur': (auteurs[:120] + ('…' if len(auteurs) > 120 else '')) + f' — {r.get("journalTitle", "")} {r.get("pubYear", "")}',
            'url': f'https://doi.org/{r["doi"]}' if r.get('doi') else f'https://pmc.ncbi.nlm.nih.gov/articles/{pmc}/',
            'fichier': f'images/{nom}.webp', 'w': w, 'h': h, 'consulte': time.strftime('%Y-%m-%d'), 'source': 'Europe PMC'}
    json.dump(meta, open(f'{lot}/images/{nom}.json', 'w'), ensure_ascii=False, indent=1)
    print(json.dumps(meta, ensure_ascii=False))


if __name__ == '__main__':
    ap = argparse.ArgumentParser(); s = ap.add_subparsers(dest='c')
    c = s.add_parser('chercher'); c.add_argument('q'); c.add_argument('--n', type=int, default=8)
    p = s.add_parser('prendre'); p.add_argument('titre'); p.add_argument('--lot', required=True); p.add_argument('--largeur', type=int, default=960)
    cp = s.add_parser('chercher-pmc'); cp.add_argument('q'); cp.add_argument('--n', type=int, default=5)
    pp = s.add_parser('prendre-pmc'); pp.add_argument('pmcid'); pp.add_argument('fichier_figure'); pp.add_argument('--lot', required=True); pp.add_argument('--largeur', type=int, default=960)
    f = s.add_parser('figure')
    for k in ('meta', 'titre', 'cliche', 'reperes', 'decision'):
        f.add_argument('--' + k, required=True)
    f.add_argument('--pieges')
    a = ap.parse_args()
    if a.c == 'chercher':
        for r in chercher(a.q, a.n):
            print(json.dumps(r, ensure_ascii=False))
    elif a.c == 'chercher-pmc':
        for r in chercher_pmc(a.q, a.n):
            print(json.dumps(r, ensure_ascii=False))
    elif a.c == 'prendre-pmc':
        prendre_pmc(a.pmcid, a.fichier_figure, a.lot, a.largeur)
    elif a.c == 'prendre':
        prendre(a.titre, a.lot, a.largeur)
    else:
        figure(a)
