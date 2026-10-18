#!/usr/bin/env python3
"""Moteur partagé des quatre automates, sans dépendance Python externe.

Collecte des pistes CH/Europe, extraits chiffrés et provenance. Ne modifie jamais
prev.json ni les sources cliniques. Un résultat bibliographique n'est pas une
prévalence vérifiée. Reprise par empreinte SSP + libellé, ordre du catalogue.
"""
import argparse
from concurrent.futures import ThreadPoolExecutor
from collections import deque
from datetime import datetime, timedelta, timezone
import hashlib
from html import unescape
from html.parser import HTMLParser
import json
from pathlib import Path
import re
import subprocess
import sys
import threading
import time
import unicodedata
from urllib.parse import urlencode, urljoin, urlparse
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parents[2]
CONFIG = json.loads(Path(__file__).with_name('config.json').read_text())
DEFAULT_STATE = ROOT / '.etat_local' / 'prevalences'
PERCENT_NUMBER = r'(?:100|\d{1,2})(?:[.,]\s*\d+)?'
PERCENT = re.compile(r'(?<![\w.])(?:[<>≤≥]\s*)?' + PERCENT_NUMBER + r'(?:\s*(?:[-–]|à|to)\s*' + PERCENT_NUMBER + r')?\s*(?:%|per\s+cent|percent\b|pour\s+cent)', re.I)
STOP = {'par', 'des', 'les', 'une', 'sur', 'sous', 'entre', 'chez', 'dont', 'aux', 'and', 'the', 'for', 'from', 'with', 'avec', 'sans', 'dans', 'pour', 'type', 'types', 'tous', 'autre', 'autres', 'cause', 'causes', 'maladie', 'syndrome', 'suspicion', 'aigue', 'aigu', 'chronique', 'primaire', 'secondaire', 'trouble', 'troubles'}


def now():
    return datetime.now(timezone.utc).isoformat(timespec='seconds')


def norm(s):
    s = ''.join(c for c in unicodedata.normalize('NFKD', s.lower().replace('œ', 'oe')) if not unicodedata.combining(c))
    return re.sub(r'[^a-z0-9]+', ' ', s).strip()


def atomic_json(path, obj):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    temp = path.with_name(path.name + '.tmp')
    temp.write_text(json.dumps(obj, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    temp.replace(path)


def catalog(root=ROOT):
    sys.path.insert(0, str(root / 'tools'))
    from _app import span
    app = (root / 'app_v2.html').read_text(encoding='utf-8')
    a, b = span(app, 'SSP'); ssps = json.loads(app[a:b])
    a, b = span(app, 'NOT'); notions = json.loads(app[a:b])
    out = []
    for code, title, sector in ssps:
        for i, diagnostic in enumerate(notions.get(code, [[]])[0]):
            signature = json.dumps([code, i, diagnostic, title], ensure_ascii=False)
            out.append({'key': f'{code}#{i}', 'ssp': code, 'title_ssp': title,
                        'secteur': sector, 'categorie': code[0], 'i': i,
                        'diagnostic': diagnostic, 'fingerprint': hashlib.sha256(signature.encode()).hexdigest()})
    return ssps, out


def terms(text):
    # Le libellé français reste toujours présent ; les alias anglais élargissent
    # la découverte sans prétendre à l'équivalence clinique de toutes ses formes.
    found = [text]
    n = norm(text)
    for alias, translations in CONFIG['aliases'].items():
        if f' {alias} ' in f' {n} ':
            found.extend(translations)
    return list(dict.fromkeys(found))


def quoted(s):
    return '"' + re.sub(r'["\\\r\n]', ' ', s).strip() + '"'


def queries(task):
    diagnostic = ' OR '.join(quoted(t) for t in terms(task['diagnostic']))
    complaint = ' OR '.join(quoted(t) for t in terms(task['title_ssp']))
    out = []
    for geo, scope in CONFIG['geographies'].items():
        for kind in ('consultation', 'population'):
            target = f'({diagnostic})'
            if kind == 'consultation':
                target += f' AND ({complaint}) AND (patients OR consultation OR emergency OR primary care OR cohort)'
            target += ' AND (prevalence OR frequency OR proportion OR epidemiology OR prévalence OR fréquence) AND ' + scope
            out.append({'id': f'{geo}:{kind}', 'geographie_recherchee': geo,
                        'type_recherche': kind, 'query': target})
    return out


class Text(HTMLParser):
    def __init__(self):
        super().__init__(); self.parts = []; self.skip = 0; self.links = []
    def handle_starttag(self, tag, attrs):
        if tag in ('script', 'style'): self.skip += 1
        if tag == 'a':
            href = dict(attrs).get('href')
            if href: self.links.append(href)
    def handle_endtag(self, tag):
        if tag in ('script', 'style'): self.skip = max(0, self.skip - 1)
    def handle_data(self, data):
        if not self.skip: self.parts.append(data)
    @property
    def text(self): return re.sub(r'\s+', ' ', unescape(' '.join(self.parts))).strip()


def text_html(raw):
    p = Text(); p.feed(raw); return p.text


class Client:
    def __init__(self, cache, timeout=15, interval=.4, budget_seconds=600):
        self.cache = Path(cache); self.cache.mkdir(parents=True, exist_ok=True)
        self.timeout = timeout; self.interval = interval
        self.deadline = time.monotonic() + budget_seconds
        self.lock = threading.Lock(); self.last = {}
    def fetch(self, url, ttl_days=7):
        if urlparse(url).scheme != 'https': raise ValueError('HTTPS requis')
        key = hashlib.sha256(url.encode()).hexdigest(); p = self.cache / key
        if p.exists() and time.time() - p.stat().st_mtime < ttl_days * 86400:
            return p.read_bytes()
        with self.lock:
            if time.monotonic() >= self.deadline: raise TimeoutError('Budget de recherche atteint')
            host = urlparse(url).hostname
            delay = self.interval - (time.monotonic() - self.last.get(host, 0))
            if delay > 0: time.sleep(delay)
            self.last[host] = time.monotonic()
        req = Request(url, headers={'User-Agent': CONFIG['user_agent'], 'Accept': 'application/json, text/html, application/pdf;q=0.9'})
        with urlopen(req, timeout=min(self.timeout, max(1, self.deadline-time.monotonic()))) as r:
            raw = r.read(CONFIG['max_response_bytes'] + 1)
        if len(raw) > CONFIG['max_response_bytes']: raise ValueError('Document trop volumineux')
        tmp = p.with_suffix('.' + str(threading.get_ident()) + '.tmp')
        tmp.write_bytes(raw); tmp.replace(p)
        return raw
    def get_json(self, url):
        # Une coquille HTML, un captcha ou un HTTP 200 non JSON reste un échec.
        raw = self.fetch(url)
        value = json.loads(raw)
        if not isinstance(value, dict): raise ValueError('Réponse JSON inattendue')
        return value


def europepmc(client, q):
    url = 'https://www.ebi.ac.uk/europepmc/webservices/rest/search?' + urlencode({
        'query': q['query'], 'format': 'json', 'resultType': 'core',
        'pageSize': CONFIG['max_results_per_query'], 'sort': 'RELEVANCE'})
    d = client.get_json(url)
    if not isinstance(d.get('resultList', {}).get('result'), list) or 'hitCount' not in d:
        raise ValueError('Schéma Europe PMC inattendu')
    docs = []
    for r in d['resultList']['result']:
        doi = r.get('doi'); pmid = r.get('id'); source = r.get('source', 'MED')
        link = 'https://doi.org/' + doi if doi else f'https://europepmc.org/article/{source}/{pmid}'
        docs.append({'url': link, 'title': r.get('title', ''),
                     'text': text_html(r.get('abstractText', '')), 'provenance': 'europepmc',
                     'doi': doi, 'pmid': pmid, 'annee': r.get('pubYear'),
                     'population_verifiee': False})
    return url, docs


def crossref(client, q):
    url = 'https://api.crossref.org/works?' + urlencode({'query.bibliographic': q['query'].replace('"', '').replace(' OR ', ' ').replace(' AND ', ' '),
        'rows': CONFIG['max_results_per_query'], 'filter': 'type:journal-article',
        'select': 'DOI,title,abstract,URL,published'})
    d = client.get_json(url)
    if not isinstance(d.get('message', {}).get('items'), list): raise ValueError('Schéma Crossref inattendu')
    return url, [{'url': 'https://doi.org/' + r['DOI'], 'title': ' '.join(r.get('title', [])),
                  'text': text_html(r.get('abstract', '')), 'provenance': 'crossref',
                  'doi': r['DOI'], 'population_verifiee': False}
                 for r in d['message']['items'] if r.get('DOI')]


class Hug:
    INDEX = 'https://www.hug.ch/medecine-premier-recours/strategies-par-systemes'
    def __init__(self, client): self.client = client; self.links = None; self.error = None
    def prepare(self):
        try:
            raw = self.client.fetch(self.INDEX); p = Text(); p.feed(raw.decode('utf-8'))
            self.links = sorted({urljoin(self.INDEX, u) for u in p.links if '.pdf' in u.lower()
                                 and urlparse(urljoin(self.INDEX, u)).hostname == 'www.hug.ch'})
            if not self.links: raise ValueError('Aucun document trouvé dans l’index HUG')
        except Exception as e: self.error = str(e)[:240]; self.links = []
    def search(self, task):
        if self.links is None: self.prepare()
        if self.error: raise ValueError(self.error)
        wanted = {w for w in norm(task['diagnostic'] + ' ' + task['title_ssp']).split() if len(w) > 4 and w not in STOP}
        ranked = sorted(self.links, key=lambda u: (-sum(w in norm(u.rsplit('/', 1)[-1]) for w in wanted), u))
        chosen = [u for u in ranked if any(w in norm(u.rsplit('/', 1)[-1]) for w in wanted)][:3]
        docs = []
        for u in chosen:
            raw = self.client.fetch(u)
            if not raw.startswith(b'%PDF'): raise ValueError('Document HUG non PDF')
            p = subprocess.run(['pdftotext', '-layout', '-', '-'], input=raw, capture_output=True, timeout=25)
            if p.returncode: raise ValueError('Extraction PDF échouée')
            # Les pages sont conservées pour l'emplacement de chaque extrait.
            for page, text in enumerate(p.stdout.decode('utf-8').split('\f'), 1):
                docs.append({'url': u, 'title': u.rsplit('/', 1)[-1], 'text': text,
                             'loc': f'Page {page}', 'provenance': 'hug', 'document_sha256': hashlib.sha256(raw).hexdigest(),
                             'population_verifiee': False})
        return self.INDEX, docs


def snippets(doc, task, query_id):
    body = re.sub(r'\s+', ' ', doc.get('text', '')).strip()
    # Correspondance lexicale = piste, jamais confirmation d'un diagnostic exact.
    # Les sigles médicaux courts (VIH, BPCO, SIDA...) restent recherchables.
    keys = {w for term in terms(task['diagnostic']) for w in norm(term).split() if len(w) >= 3 and w not in STOP}
    out = []
    for m in PERCENT.finditer(body):
        excerpt = body[max(0, m.start()-180):min(len(body), m.end()+220)]
        excerpt_tokens = set(norm(excerpt).split())
        matched = sorted(keys & excerpt_tokens)
        if not matched: continue
        token = doc['url'] + '|' + doc.get('loc', '') + '|' + excerpt
        out.append({k: v for k, v in doc.items() if k != 'text'} | {
            'id': hashlib.sha256(token.encode()).hexdigest()[:24], 'extrait': excerpt,
            'sha256': hashlib.sha256(body.encode()).hexdigest(), 'date_recherche': now(),
            'requete': query_id, 'statut': 'candidat_a_relire', 'termes_reperes': matched,
            'valeur_reperee': m.group(0), 'type': 'À vérifier', 'geographie': 'À vérifier',
            'denominateur': 'À vérifier', 'diagnostic_exact': 'À vérifier'})
    return out


def due(task, old, refresh_days, retry_hours):
    if old.get('fingerprint') != task['fingerprint']: return True
    when = old.get('date_recherche')
    if not when: return True
    try: age = datetime.now(timezone.utc) - datetime.fromisoformat(when)
    except (ValueError, TypeError): return True
    hours = refresh_days * 24 if old.get('statut') == 'recherchee' else retry_hours
    return age >= timedelta(hours=hours)


def search_task(task, client, hug, providers):
    row = dict(task, date_recherche=now(), queries=[], candidates=[], statut='erreur')
    for provider in providers:
        plan = [{'id': 'CH:documents_hug'}] if provider == 'hug' else queries(task)
        for q in plan:
            if time.monotonic() >= client.deadline:
                row['queries'].append({'provider': provider, 'id': q['id'], 'ok': False, 'erreur': 'Budget atteint, recherche à reprendre'}); continue
            try:
                url, docs = hug.search(task) if provider == 'hug' else globals()[provider](client, q)
                row['queries'].append({'provider': provider, **q, 'url_recherche': url,
                                       'ok': True, 'documents': len(docs)})
                for doc in docs: row['candidates'].extend(snippets(doc, task, q['id']))
            except Exception as e:
                # Erreur tracée, non transformée en « zéro résultat ».
                row['queries'].append({'provider': provider, **q, 'ok': False, 'erreur': str(e)[:300]})
    dedup = {c['id']: c for c in row['candidates']}
    row['candidates'] = list(dedup.values())
    oks = sum(q['ok'] for q in row['queries'])
    row['statut'] = 'recherchee' if row['queries'] and oks == len(row['queries']) else 'partielle' if oks else 'erreur'
    return row



def merge_candidates(previous, discovered, limit):
    """Preserve readings and arithmetic history; retain discovery diversity.

    A bibliographic refresh must not erase an enriched candidate. Only the same
    URL/excerpt/id can inherit previous annotations; source drift is flagged.
    Automatic audit presence alone does not make a candidate a human reading.
    """
    all_candidates = {c['id']: dict(c) for c in previous}
    for fresh in discovered:
        old = all_candidates.get(fresh['id'])
        same_source = old and all(old.get(k) == fresh.get(k) for k in ('extrait', 'url', 'sha256', 'document_sha256'))
        if same_source:
            merged = dict(fresh)
            merged.update(old)
            merged['date_recherche'] = fresh.get('date_recherche', old.get('date_recherche'))
            discoveries = old.get('decouvert_par', []) + fresh.get('decouvert_par', [])
            discoveries += [{'provenance': c.get('provenance'), 'requete': c.get('requete')} for c in (old, fresh)]
            merged['decouvert_par'] = list({(d.get('provenance'), d.get('requete')): d for d in discoveries}.values())
            all_candidates[fresh['id']] = merged
        elif old:
            # An id with modified content cannot inherit arithmetic proofs.
            fresh = dict(fresh, source_modifiee=True)
            all_candidates[fresh['id']] = fresh
        else:
            all_candidates[fresh['id']] = dict(fresh)
    def enriched(c):
        audit = c.get('audit', {})
        return bool(c.get('statistique') or c.get('relecture_humaine') or c.get('relecture_agent') or
                    (isinstance(audit, dict) and (audit.get('corrections') or audit.get('calcul_verifie'))))
    curated = [c for c in all_candidates.values() if enriched(c)]
    groups = {}
    for c in all_candidates.values():
        if not enriched(c):
            groups.setdefault((c.get('provenance'), c.get('requete')), deque()).append(c)
    selected = curated[:limit]
    while len(selected) < limit and any(groups.values()):
        for queue in groups.values():
            if queue and len(selected) < limit:
                selected.append(queue.popleft())
    return selected, {'candidats_total_avant_limite': len(all_candidates),
                      'candidats_omis': len(all_candidates) - len(selected),
                      'candidats_enrichis_omis': max(0, len(curated)-limit)}


def run_category(category, args):
    _, tasks = catalog(); tasks = [t for t in tasks if t['categorie'] == category]
    path = Path(args.state_dir) / f'{category}.json'
    state = json.loads(path.read_text()) if path.exists() else {'version': 1, 'category': category, 'tasks': {}}
    if state.get('version') != 1 or state.get('category') != category: raise ValueError('État incompatible')
    queued = [t for t in tasks if due(t, state['tasks'].get(t['key'], {}), args.refresh_days, args.retry_hours)]
    # Jamais cherchés d'abord ; ensuite tentatives les plus anciennes. L'ordre G1→G16
    # et l'ordre officiel des autres secteurs sont stables à priorité égale.
    order = {t['key']: i for i, t in enumerate(tasks)}
    queued.sort(key=lambda t: (bool(state['tasks'].get(t['key'], {}).get('date_recherche')),
                              state['tasks'].get(t['key'], {}).get('date_recherche', ''), order[t['key']]))
    selected = queued[:args.limit] if args.limit else queued
    if args.plan:
        print(json.dumps({'category': category, 'due': len(queued), 'tasks': selected}, ensure_ascii=False, indent=1)); return state
    client = Client(args.cache_dir, args.timeout, CONFIG['interval_seconds'], args.budget_seconds)
    hug = Hug(client)
    if 'hug' in args.providers: hug.prepare()
    done = 0
    with ThreadPoolExecutor(max_workers=args.workers) as pool:
        # Petites vagues : ne pas marquer cherchée une tâche restée en file à la fin du budget.
        for start in range(0, len(selected), args.workers):
            if time.monotonic() >= client.deadline: break
            batch = selected[start:start+args.workers]
            for row in pool.map(lambda t: search_task(t, client, hug, args.providers), batch):
                previous = state['tasks'].get(row['key'], {})
                # Une panne temporaire ne supprime jamais des pistes antérieures.
                previous_candidates = previous.get('candidates', []) if previous.get('fingerprint') == row['fingerprint'] else []
                row['candidates'], selection = merge_candidates(previous_candidates, row['candidates'], CONFIG['max_candidates_per_task'])
                row.update(selection)
                state['tasks'][row['key']] = row; done += 1
                state.update(maj=now(), providers=args.providers, total_catalogue=len(tasks))
                atomic_json(path, state)
                print(f"{category} · {done}/{len(selected)} · {row['key']} · {row['statut']} · {len(row['candidates'])} piste(s)", flush=True)
    state.update(maj=now(), dernier_lot={'selectionnes': len(selected), 'traites': done, 'restants_a_rechercher': len(queued)-done})
    from tools.prevalences.auditeur import audit_state
    state, report = audit_state(state)
    atomic_json(path, state); atomic_json(Path(args.state_dir) / f'audit-{category}.json', report)
    return state


def main(category=None, argv=None):
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--categorie', choices=CONFIG['categories'], default=category, required=category is None)
    p.add_argument('--state-dir', default=str(DEFAULT_STATE)); p.add_argument('--cache-dir', default=str(ROOT / '.etat_local' / 'prevalences-cache'))
    p.add_argument('--limit', type=int, default=20, help='diagnostics par lancement ; 0 = tous, budget toujours appliqué')
    p.add_argument('--workers', type=int, default=2); p.add_argument('--budget-seconds', type=int, default=600)
    p.add_argument('--timeout', type=int, default=CONFIG['timeout_seconds'])
    p.add_argument('--refresh-days', type=int, default=CONFIG['refresh_days']); p.add_argument('--retry-hours', type=int, default=CONFIG['retry_hours'])
    p.add_argument('--providers', nargs='+', choices=CONFIG['providers'], default=CONFIG['providers']); p.add_argument('--plan', action='store_true')
    args = p.parse_args(argv)
    if args.limit < 0 or not 1 <= args.workers <= 4 or args.budget_seconds < 1 or args.timeout < 1 or args.refresh_days < 1 or args.retry_hours < 1:
        p.error('Limites invalides : lot ≥ 0, workers 1–4, délais positifs')
    run_category(args.categorie, args)
    return 0


if __name__ == '__main__':
    sys.path.insert(0, str(ROOT))
    raise SystemExit(main())
