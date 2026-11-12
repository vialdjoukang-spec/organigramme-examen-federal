#!/usr/bin/env python3
"""SOURCES_CACHE — mémoire des sources partagée par tous les agents (zéro modèle).
Une page lue une fois n'est jamais rapatriée ni relue en entier : texte brut gardé en cache disque, index en clair.

  lire <url>            → rapatrie une fois (curl ; PMC/Europe PMC en texte), stocke le texte, affiche 1 500 caractères
  cherche <url> <mot…>  → renvoie seulement les phrases contenant les mots (≤ 12 phrases) : citation verbatim prête
  disjoncteur          → domaines coupés (≥ 2 échecs en 24 h, principe PyBreaker du Bracelet) : ne pas relancer
  index [motif]         → liste des sources en cache (date, octets, titre) : à consulter AVANT toute recherche web
Cache : $SOURCES_CACHE (défaut ~/.cache/medina_sources) ; index : Claude/_harnais/donnees/sources_index.jsonl
(URL, date, sha, titre ; aucun texte d'auteur dans le dépôt public).
"""
import re, os, sys, json, html, hashlib, subprocess, datetime

CACHE = os.environ.get('SOURCES_CACHE', os.path.expanduser('~/.cache/medina_sources'))
INDEX = 'Claude/_harnais/donnees/sources_index.jsonl'

DISJ = os.path.join(CACHE, '_disjoncteur.json')


def _dom(url):
    return re.sub(r'^https?://([^/:?#]+).*', r'\1', url)


def disj(url=None, echec=None):
    """Disjoncteur par domaine : 2 échecs en 24 h coupent le domaine 24 h (évite les 403 relancés en boucle)."""
    try: d = json.load(open(DISJ))
    except Exception: d = {}
    now = datetime.datetime.now().timestamp()
    if url is None: return {k: v for k, v in d.items() if v['n'] >= 2 and now - v['t'] < 86400}
    k = _dom(url); v = d.get(k, {'n': 0, 't': 0})
    if echec is None: return v['n'] >= 2 and now - v['t'] < 86400
    v = {'n': (v['n'] + 1 if now - v['t'] < 86400 else 1) if echec else 0, 't': now}; d[k] = v
    os.makedirs(CACHE, exist_ok=True); json.dump(d, open(DISJ, 'w'))


def brut(url):
    os.makedirs(CACHE, exist_ok=True)
    k = hashlib.sha256(url.encode()).hexdigest()[:16]
    ft = os.path.join(CACHE, k + '.txt')
    if os.path.exists(ft):
        return open(ft, encoding='utf-8').read(), False
    fb = os.path.join(CACHE, k + '.bin')
    if disj(url):
        print(f'[DISJONCTEUR] {_dom(url)} coupé (échecs répétés) : autre source', file=sys.stderr); return '', False
    m = re.match(r'https://ssi\.guidelines\.ch/guideline/(\d+)/(\w+)', url)
    if m:  # application JavaScript : l'API publique renvoie le texte de la recommandation
        subprocess.run(['curl', '-sS', '-m', '60', '-X', 'POST', '-H', 'Content-Type: application/json', '-o', fb,
                        '-d', json.dumps({'id': m.group(1), 'language': m.group(2)}),
                        'https://ssi.guidelines.ch/api/reader/query/guideline'], check=False)
    else:
        subprocess.run(['curl', '-sSL', '--retry', '2', '-m', '90', '-A', 'Mozilla/5.0', '-o', fb, url], check=False)
    data = open(fb, 'rb').read() if os.path.exists(fb) else b''
    if data[:4] == b'%PDF':
        t = subprocess.run(['pdftotext', '-layout', fb, '-'], capture_output=True, text=True).stdout
    else:
        h = data.decode('utf-8', 'ignore')
        h = re.sub(r'<(script|style|nav|header|footer)\b.*?</\1>', ' ', h, flags=re.S | re.I)
        t = html.unescape(re.sub(r'<[^>]+>', ' ', h))
    t = re.sub(r'[ \t]+', ' ', t); t = re.sub(r'\n\s*\n+', '\n', t).strip()
    if len(t) < 200:
        disj(url, True)
        print(f'[ALERTE] texte trop court ({len(t)} car.) : page dynamique ou refus ; ne pas citer sans autre lecture', file=sys.stderr)
        return t, True
    disj(url, False); open(ft, 'w', encoding='utf-8').write(t)
    titre = (re.search(r'<title>(.*?)</title>', data.decode('utf-8', 'ignore'), re.S | re.I) or [None, t[:90]])[1]
    os.makedirs(os.path.dirname(INDEX), exist_ok=True)
    with open(INDEX, 'a', encoding='utf-8') as f:
        f.write(json.dumps(dict(url=url, date=datetime.date.today().isoformat(), sha=k, octets=len(t),
                                titre=re.sub(r'\s+', ' ', html.unescape(titre or ''))[:120]), ensure_ascii=False) + '\n')
    return t, True


def cherche(url, mots):
    t, _ = brut(url)
    ph = re.split(r'(?<=[.!?])\s+', t.replace('\n', ' '))
    out = [p.strip() for p in ph if all(re.search(m, p, re.I) for m in mots)]
    return out[:12]


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print(__doc__); sys.exit(0)
    act = sys.argv[1]
    if act == 'lire':
        t, neuf = brut(sys.argv[2]); print(('[NOUVEAU] ' if neuf else '[CACHE] ') + f'{len(t)} car.\n' + t[:1500])
    elif act == 'cherche':
        for p in cherche(sys.argv[2], sys.argv[3:]): print('« ' + p[:500] + ' »')
    elif act == 'disjoncteur':
        print(json.dumps(disj(), indent=0) if disj() else 'aucun domaine coupé')
    elif act == 'index':
        motif = sys.argv[2] if len(sys.argv) > 2 else ''
        if os.path.exists(INDEX):
            for l in open(INDEX, encoding='utf-8'):
                if motif.lower() in l.lower(): print(l.strip())
