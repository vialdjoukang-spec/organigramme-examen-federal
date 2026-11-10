#!/usr/bin/env python3
"""LÉGION — collecteur gratuit, multi-processus, multi-escouades (stdlib seule).

Usage : python3 legion.py <depot1> [<depot2> ...] --out <dossier>
Sortie : legion_digest.json (complet) + legion_digest.md (ultra-concis, à lire par un modèle).
Coût modèle : 0. Réutilisable comme contrôleur qualité (escouade QUALITE).
"""
import os, re, sys, json, html, subprocess, collections, argparse
from concurrent.futures import ProcessPoolExecutor

SKIP_DIRS = {'.git', 'node_modules', '__pycache__', '.venv', 'dist'}
TXT_EXT = {'.md', '.txt', '.json', '.html', '.py', '.yml', '.yaml', '.js'}
URL_RE = re.compile(r'https?://[^\s)"\'<>\]]+')
LOT_RE = re.compile(r'LOT[_ ]?(\d{3})', re.I)
DX_RE = re.compile(r'DX\.(\d+)')
SWISS = ('compendium.ch', 'swissmedicinfo', 'bag.admin.ch', 'admin.ch', 'sgim', 'ssmi', 'swissmedic',
         'medix.ch', 'pharmavista', 'sginf', 'ssi', 'chuv.ch', 'hug.ch', 'unige', 'unil', 'iml', 'kssg',
         'usz.ch', 'insel', 'smw.ch', 'revmed.ch', 'aips', 'ssp', 'fmh.ch', 'swissnoso', 'infovac', 'sgk',
         'swisscardio', 'sggg', 'paediatrieschweiz', 'tox', 'svgo', 'sgp', 'suva')
IMG_DOM = ('radiopaedia', 'wikimedia', 'openi.nlm', 'dermnet', 'eyewiki', 'pathpedia', 'ecgwaves',
           'litfl', 'webpathology', 'ultrasoundcases', 'pocus')
# Connecteurs logiques français (contrôle "phrase verbale + connecteur")
CONNECT = re.compile(r"\b(car|donc|or|ainsi|puis|alors|parce que|puisque|lorsque|quand|si|tandis que|"
                     r"alors que|afin de|afin que|pour que|de sorte que|c'est pourquoi|en effet|cependant|"
                     r"toutefois|néanmoins|par conséquent|dès lors|ensuite|enfin|d'abord|aussi|"
                     r"en revanche|ce qui|ce qui explique|via|grâce à|à cause de|en raison de|"
                     r"conduisant à|entraînant|provoquant|signant|orientant)\b", re.I)
# Heuristique verbe conjugué (FR) : auxiliaires/verbes fréquents + terminaisons 3e pers.
VERB = re.compile(r"\b(est|sont|a|ont|fait|font|peut|peuvent|doit|doivent|reste|restent|devient|"
                  r"deviennent|signe|signent|oriente|orientent|impose|imposent|confirme|confirment|"
                  r"élimine|éliminent|traite|traitent|associe|associent|survient|surviennent|"
                  r"provoque|provoquent|entraîne|entraînent|exige|exigent|reçoit|reçoivent|"
                  r"\w+(?:e|ent|it|ient|ait|aient|era|eront|ra|ront))\b", re.I)
TAG_RE = re.compile(r'<(script|style)[^>]*>.*?</\1>', re.S | re.I)
STRIP_RE = re.compile(r'<[^>]+>')
HEAD_RE = re.compile(r'<h([1-4])[^>]*>(.*?)</h\1>', re.S | re.I)
MD_HEAD = re.compile(r'^(#{1,4})\s+(.+)$', re.M)


def walk(root):
    for d, ds, fs in os.walk(root):
        ds[:] = [x for x in ds if x not in SKIP_DIRS]
        for f in fs:
            yield os.path.join(d, f)


def read(p, cap=2_000_000):
    try:
        with open(p, 'rb') as fh:
            return fh.read(cap).decode('utf-8', 'ignore')
    except Exception:
        return ''


def html_text(s):
    s = TAG_RE.sub(' ', s)
    return html.unescape(re.sub(r'\s+', ' ', STRIP_RE.sub(' ', s))).strip()


def qualite(text):
    """Escouade QUALITÉ : phrases, % avec verbe conjugué, % avec connecteur, longueur moyenne."""
    sents = [x.strip() for x in re.split(r'(?<=[.!?;])\s+|\s•\s|\n', text) if len(x.strip()) > 25]
    if not sents:
        return {'n': 0}
    v = sum(1 for x in sents if VERB.search(x))
    c = sum(1 for x in sents if CONNECT.search(x))
    return {'n': len(sents), 'verbe%': round(100 * v / len(sents)), 'connect%': round(100 * c / len(sents)),
            'mots_moy': round(sum(len(x.split()) for x in sents) / len(sents), 1)}


def analyse_fichier(p):
    """Unité de travail d'un soldat : un fichier → fiche compacte."""
    ext = os.path.splitext(p)[1].lower()
    try:
        size = os.path.getsize(p)
    except OSError:
        size = 0
    r = {'p': p, 'ext': ext, 'o': size}
    if ext not in TXT_EXT or size > 3_000_000:
        return r
    s = read(p)
    urls = URL_RE.findall(s)
    if urls:
        doms = collections.Counter(re.sub(r'^https?://(www\.)?', '', u).split('/')[0].lower() for u in urls)
        r['urls'] = len(urls)
        r['dom'] = dict(doms.most_common(8))
        r['swiss'] = sum(n for d, n in doms.items() if any(k in d for k in SWISS))
        r['imgdom'] = sum(n for d, n in doms.items() if any(k in d for k in IMG_DOM))
    if ext == '.md' and re.search(r'PROMPT|SKILL|AGENTS|CLAUDE|HARNAIS|SPEC|CONTINU|REPRISE|PASSATION|LIRE|BRACELET', os.path.basename(p), re.I):
        r['plan'] = [('#' * len(h)) + ' ' + t.strip()[:90] for h, t in MD_HEAD.findall(s)][:80]
    if ext == '.html' and re.search(r'DX\.\d+|Phase_A|chap|cours', os.path.basename(p), re.I):
        r['h'] = [f'h{l} ' + html_text(t)[:70] for l, t in HEAD_RE.findall(s)][:40]
        r['img'] = len(re.findall(r'<img\b|<svg\b', s, re.I))
        r['modal'] = len(re.findall(r'modal|dialog', s, re.I))
        r['src'] = len(re.findall(r'<a\s[^>]*href=["\']https?://', s, re.I))
        t = html_text(s)
        r['txt_o'] = len(t.encode())
        r['q'] = qualite(t)
    return r


def escouade_git(root):
    """Branches actives (dates) + LOTs présents sur les branches sans checkout (git ls-tree)."""
    out = {}
    try:
        refs = subprocess.run(['git', '-C', root, 'for-each-ref', '--sort=-committerdate',
                               '--format=%(committerdate:short)|%(refname:short)|%(subject)', 'refs/remotes'],
                              capture_output=True, text=True, timeout=60).stdout.splitlines()
        out['branches_total'] = len(refs)
        out['branches_recentes'] = refs[:15]
        prod = collections.Counter(r.split('|')[1].split('/')[1] if '/' in r.split('|')[1] else '?' for r in refs)
        out['prefixes'] = dict(prod.most_common(10))
        lots_branches = collections.defaultdict(set)
        for r in refs:
            m = LOT_RE.search(r.split('|')[1].replace('-', '_'))
            if m:
                lots_branches[int(m.group(1))].add(r.split('|')[1])
        out['lots_en_branche'] = sorted(lots_branches)
    except Exception as e:
        out['err'] = str(e)
    return out


def synthese(root, fiches):
    S = {'depot': os.path.basename(root)}
    S['fichiers'] = len(fiches)
    S['octets'] = sum(f['o'] for f in fiches)
    S['ext'] = dict(collections.Counter(f['ext'] for f in fiches).most_common(10))
    top = collections.Counter()
    for f in fiches:
        top[os.path.relpath(f['p'], root).split(os.sep)[0]] += f['o']
    S['top_dirs_Mo'] = {k: round(v / 1e6, 1) for k, v in top.most_common(15)}
    # LOTs
    lots = collections.defaultdict(lambda: {'dx': set(), 'A': 0, 'o': 0, 'img': 0, 'fig': 0, 'lieu': set(), 'q': []})
    for f in fiches:
        rel = os.path.relpath(f['p'], root)
        m = LOT_RE.search(rel)
        if not m or 'audit' in rel.split(os.sep)[0]:
            continue
        L = lots[int(m.group(1))]
        L['lieu'].add(rel.split(os.sep)[0])
        if f['ext'] == '.html':
            dm = DX_RE.search(rel)
            if dm:
                L['dx'].add(int(dm.group(1)))
            if 'Phase_A' in rel:
                L['A'] = 1
            L['o'] += f['o']
            L['img'] += f.get('img', 0)
            if f.get('q', {}).get('n'):
                L['q'].append(f['q'])
        if f['ext'] in ('.png', '.jpg', '.jpeg', '.webp', '.svg', '.gif'):
            L['fig'] += 1
    S['lots'] = {}
    for k in sorted(lots):
        L = lots[k]
        q = L['q']
        S['lots'][k] = {'dx': len(L['dx']), 'A': L['A'], 'Ko': round(L['o'] / 1024), 'img_html': L['img'],
                        'fig': L['fig'], 'lieu': sorted(L['lieu']),
                        'verbe%': round(sum(x['verbe%'] for x in q) / len(q)) if q else None,
                        'connect%': round(sum(x['connect%'] for x in q) / len(q)) if q else None}
    # Prompts
    S['prompts'] = sorted(({'f': os.path.relpath(f['p'], root), 'Ko': round(f['o'] / 1024, 1),
                            'plan': f['plan'][:25]} for f in fiches if f.get('plan')),
                          key=lambda x: -x['Ko'])[:25]
    # Liens
    L = [f for f in fiches if f.get('urls')]
    S['fichiers_liens'] = sorted(({'f': os.path.relpath(f['p'], root), 'urls': f['urls'], 'swiss': f['swiss'],
                                   'img': f['imgdom'], 'dom': f['dom']} for f in L
                                  if not os.path.relpath(f['p'], root).startswith(('audit', 'audits'))),
                                 key=lambda x: (-x['swiss'], -x['urls']))[:20]
    dom = collections.Counter()
    for f in L:
        dom.update(f['dom'])
    S['domaines_top'] = dict(dom.most_common(25))
    # Gabarit HTML dominant (titres h2 les plus fréquents)
    h = collections.Counter()
    for f in fiches:
        for t in f.get('h', []):
            if t.startswith(('h2', 'h3')):
                h[re.sub(r'\d+', '#', t)] += 1
    S['gabarit_titres'] = h.most_common(30)
    qs = [f['q'] for f in fiches if f.get('q', {}).get('n')]
    if qs:
        S['qualite_globale'] = {'docs': len(qs), 'verbe%': round(sum(x['verbe%'] for x in qs) / len(qs)),
                                'connect%': round(sum(x['connect%'] for x in qs) / len(qs)),
                                'mots_moy': round(sum(x['mots_moy'] for x in qs) / len(qs), 1)}
    return S


def md(digests):
    o = ['# LÉGION — digest\n']
    for S in digests:
        o.append(f"## {S['depot']} — {S['fichiers']} fichiers, {round(S['octets']/1e6)} Mo")
        o.append('ext ' + json.dumps(S['ext'], ensure_ascii=False))
        o.append('dirs Mo ' + json.dumps(S['top_dirs_Mo'], ensure_ascii=False))
        g = S.get('git', {})
        o.append(f"git: {g.get('branches_total')} branches; préfixes {g.get('prefixes')}; LOTs en branche {g.get('lots_en_branche')}")
        o += ['  ' + b for b in g.get('branches_recentes', [])[:8]]
        if S['lots']:
            o.append('### LOTs (n: dx|A|Ko|img|fig|verbe%|connect%|lieu)')
            o.append('; '.join(f"{k}:{v['dx']}|{v['A']}|{v['Ko']}|{v['img_html']}|{v['fig']}|{v['verbe%']}|{v['connect%']}|{','.join(v['lieu'])[:18]}"
                               for k, v in S['lots'].items()))
        o.append('### Qualité globale ' + json.dumps(S.get('qualite_globale'), ensure_ascii=False))
        o.append('### Gabarit titres h2/h3 (fréq)')
        o.append('; '.join(f'{t}×{n}' for t, n in S['gabarit_titres'][:25]))
        o.append('### Prompts (Ko) + plan')
        for p in S['prompts'][:15]:
            o.append(f"- {p['f']} ({p['Ko']}) :: " + ' | '.join(p['plan'][:14]))
        o.append('### Fichiers de liens (urls/suisses/imagerie)')
        for f in S['fichiers_liens'][:12]:
            o.append(f"- {f['f']} {f['urls']}/{f['swiss']}/{f['img']} {list(f['dom'])[:5]}")
        o.append('domaines ' + json.dumps(S['domaines_top'], ensure_ascii=False))
        o.append('')
    return '\n'.join(o)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('roots', nargs='+')
    ap.add_argument('--out', default='.')
    ap.add_argument('--workers', type=int, default=os.cpu_count())
    a = ap.parse_args()
    digests = []
    with ProcessPoolExecutor(a.workers) as ex:
        for root in a.roots:
            files = list(walk(root))
            fiches = list(ex.map(analyse_fichier, files, chunksize=64))
            S = synthese(root, fiches)
            S['git'] = escouade_git(root)
            digests.append(S)
    os.makedirs(a.out, exist_ok=True)
    with open(os.path.join(a.out, 'legion_digest.json'), 'w') as fh:
        json.dump(digests, fh, ensure_ascii=False, indent=1, default=list)
    m = md(digests)
    with open(os.path.join(a.out, 'legion_digest.md'), 'w') as fh:
        fh.write(m)
    print(f'OK {len(m.encode())} octets digest')


if __name__ == '__main__':
    main()
