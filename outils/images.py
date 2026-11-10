#!/usr/bin/env python3
"""IMAGES — automate collecteur gratuit de clichés et figures sous licence libre (zéro modèle).

Fournisseurs (API publiques, sans clé) :
  commons   : Wikimedia Commons (namespace Fichier) — licence lue dans extmetadata de CHAQUE fichier
  europepmc : articles en accès ouvert (licence d'ARTICLE ; la figure reste « à relire »)
  catalogue : ressources académiques de Vial (Radiopaedia, Radiology Assistant, Ultrasound Cases, Eurorad…)
              → LIEN DE CAS uniquement, jamais de copie (droits non établis)
Règles : NC/ND/licence inconnue = refus ; une requête précise par figure ; cache disque ; budget journalier ;
aucune insertion automatique ; planche HTML de contrôle visuel (un seul coup d'œil pour tout le lot).

Usage :
  python3 images.py --lot LOT_166 --besoins besoins.json [--budget 60]
  besoins.json : [{"dx":"DX.1","point":9,"modalite":"échographie","requete":"ascites ultrasound Morison"}]
Sortie : LOT_166/images/CANDIDATS.json + LOT_166/images/PLANCHE.html + LOT_166/images/<sha>.<ext>
"""
import os, re, sys, json, hashlib, argparse, urllib.request, urllib.parse, datetime, html

UA = {'User-Agent': 'collecteur-images-pedagogique/1.0 (cours medicaux; contact via depot)'}
LIBRES = re.compile(r'^(cc0|cc[- ]by(?:[- ]sa)?(?:[- ]\d\.\d)?|public domain|pd|domaine public)', re.I)
REFUS = re.compile(r'\bnc\b|\bnd\b|non.?commercial|no.?deriv', re.I)
CATALOGUE = {
    'Radiopaedia': 'https://radiopaedia.org/search?q={q}&scope=cases',
    'Radiology Assistant': 'https://radiologyassistant.nl/search?q={q}',
    'Ultrasound Cases': 'https://www.ultrasoundcases.info/search/?q={q}',
    'Eurorad (ESR)': 'https://www.eurorad.org/advanced-search?search={q}',
    'Learning Radiology': 'https://www.learningradiology.com/',
    'Case Stacks': 'https://casestacks.com/',
    'Casimage (UNIGE)': 'https://www.casimage.com/',
    'RadioSurf (UniBE)': 'https://elearning.medizin.unibe.ch/',
}


def get(url, cache, budget):
    os.makedirs(cache, exist_ok=True)
    f = os.path.join(cache, hashlib.sha256(url.encode()).hexdigest()[:24])
    if os.path.exists(f):
        return open(f, 'rb').read()
    if budget['reste'] <= 0:
        raise RuntimeError('budget journalier épuisé')
    budget['reste'] -= 1
    with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=20) as r:
        b = r.read(15_000_000)
    open(f, 'wb').write(b)
    return b


def commons(q, cache, budget, n=6):
    p = {'action': 'query', 'format': 'json', 'generator': 'search', 'gsrnamespace': 6, 'gsrsearch': q,
         'gsrlimit': n, 'prop': 'imageinfo', 'iiprop': 'url|mime|size|extmetadata', 'iiurlwidth': 900}
    j = json.loads(get('https://commons.wikimedia.org/w/api.php?' + urllib.parse.urlencode(p), cache, budget))
    out = []
    for pg in (j.get('query', {}).get('pages', {}) or {}).values():
        ii = (pg.get('imageinfo') or [{}])[0]
        m = {k: re.sub('<[^>]+>', '', v.get('value', '')) for k, v in (ii.get('extmetadata') or {}).items()}
        lic = m.get('LicenseShortName', '')
        ok = bool(LIBRES.search(lic)) and not REFUS.search(lic)
        out.append({'fournisseur': 'commons', 'titre': pg.get('title'), 'page': ii.get('descriptionurl'),
                    'fichier': ii.get('thumburl') or ii.get('url'), 'mime': ii.get('mime'),
                    'auteur': m.get('Artist', '')[:200], 'licence': lic, 'licence_url': m.get('LicenseUrl', ''),
                    'description': m.get('ImageDescription', '')[:400],
                    'decision': 'admissible_a_inspecter' if ok else 'refuse_licence'})
    return out


def europepmc(q, cache, budget, n=5):
    url = 'https://www.ebi.ac.uk/europepmc/webservices/rest/search?' + urllib.parse.urlencode(
        {'query': f'({q}) AND OPEN_ACCESS:Y AND HAS_FT:Y', 'format': 'json', 'resultType': 'core', 'pageSize': n})
    j = json.loads(get(url, cache, budget))
    out = []
    for it in j.get('resultList', {}).get('result', []):
        lic = it.get('license') or ''
        ok = bool(LIBRES.search(lic.replace('-', ' '))) and not REFUS.search(lic)
        out.append({'fournisseur': 'europepmc', 'titre': it.get('title'), 'page': f"https://europepmc.org/article/PMC/{it.get('pmcid')}",
                    'fichier': None, 'auteur': (it.get('authorString') or '')[:200], 'licence': lic,
                    'decision': 'article_admissible_figure_a_relire' if ok else 'refuse_licence'})
    return out


def acquerir(c, dossier, cache, budget):
    """Rapatrie seulement les candidats Commons admissibles ; empreinte SHA-256 = identité de la figure."""
    if c['decision'] != 'admissible_a_inspecter' or not c.get('fichier'):
        return c
    b = get(c['fichier'], cache, budget)
    h = hashlib.sha256(b).hexdigest()
    ext = {'image/png': 'png', 'image/jpeg': 'jpg', 'image/svg+xml': 'svg', 'image/webp': 'webp'}.get(c.get('mime'), 'jpg')
    nom = f'{h[:16]}.{ext}'
    open(os.path.join(dossier, nom), 'wb').write(b)
    c.update(local=nom, sha256=h, acquis=datetime.datetime.now().isoformat(timespec='seconds'),
             inspection_visuelle=False, publication_ready=False)
    return c


def planche(cands, chemin):
    cases = []
    for c in cands:
        img = f'<img src="{c["local"]}" loading="lazy" style="max-width:100%;max-height:260px">' if c.get('local') else '<em>lien seul</em>'
        cases.append(f'<figure style="border:1px solid #889;padding:6px;margin:0"><b>{html.escape(c["besoin"])}</b><br>{img}'
                     f'<figcaption style="font-size:12px">{html.escape(c.get("titre") or "")}<br>{html.escape(c.get("licence") or "")} · '
                     f'{html.escape(c.get("auteur") or "")[:80]}<br><a href="{c.get("page")}">source</a> · {c["decision"]}</figcaption></figure>')
    open(chemin, 'w').write('<!doctype html><meta charset="utf-8"><title>Planche</title><body style="font:14px sans-serif;background:#eef1f3">'
                            '<div style="display:grid;grid-template-columns:repeat(auto-fill,minmax(260px,1fr));gap:8px">'
                            + ''.join(cases) + '</div>')


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('--lot', required=True)
    ap.add_argument('--besoins', required=True)
    ap.add_argument('--budget', type=int, default=60)
    ap.add_argument('--cache', default='.cache/images')
    a = ap.parse_args()
    d = os.path.join(a.lot, 'images')
    os.makedirs(d, exist_ok=True)
    budget, tout = {'reste': a.budget}, []
    for b in json.load(open(a.besoins)):
        tag = f"{b['dx']} · point {b['point']} · {b['modalite']}"
        for f in (commons, europepmc):
            try:
                for c in f(b['requete'], a.cache, budget):
                    c['besoin'] = tag
                    tout.append(acquerir(c, d, a.cache, budget))
            except Exception as e:  # échec déclaré, jamais contourné
                tout.append({'besoin': tag, 'fournisseur': f.__name__, 'decision': f'echec: {e}'})
        for nom, u in CATALOGUE.items():
            tout.append({'besoin': tag, 'fournisseur': 'catalogue_vial', 'titre': nom,
                         'page': u.format(q=urllib.parse.quote(b['requete'])), 'decision': 'lien_de_cas_uniquement'})
    json.dump(tout, open(os.path.join(d, 'CANDIDATS.json'), 'w'), ensure_ascii=False, indent=1)
    planche([c for c in tout if c.get('fournisseur') != 'catalogue_vial'], os.path.join(d, 'PLANCHE.html'))
    print(f"{d}: {sum(1 for c in tout if c.get('local'))} images acquises, {budget['reste']} requêtes restantes")
