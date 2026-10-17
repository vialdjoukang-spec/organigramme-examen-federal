#!/usr/bin/env python3
"""Lyncée · Janus · détecteur des termes médicaux non définis (contrôle G4, zéro jeton).

Corpus : TIP, NOT, GES et le HTML statique d'app_v2.html, puis tout le texte de data/ck et de data/cs,
y compris les définitions du glossaire (règle du glossaire imbriqué).
Un mot devient candidat s'il porte un affixe médical, s'il suit un motif éponyme
(« signe de Babinski ») ou s'il s'agit d'une abréviation. Il est défini s'il figure dans
data/ck/glo.json (libellé, alias, flexions) ou dans qa/termes_exclus.txt (avec un motif).

  python3 tools/lyncee.py                       # contrôle contre qa/termes-baseline.json
  python3 tools/lyncee.py --diff origin/main    # contrôle, et la référence ne peut que baisser
  python3 tools/lyncee.py --update              # resserre la référence (jamais d'ajout)
  python3 tools/lyncee.py --json .cache/lyncee.json   # liste complète pour le tri (Hippocrate)

Le gate est déterministe : aucune liste externe n'est téléchargée en CI. Les filtres MeSH
(CC BY-NC) et Lexique 3.83 (CC BY-SA) restent des aides au tri, en cache local seulement.
Code de sortie : 1 si un terme nouveau non défini, un renvoi glo|id inexistant, une
auto-référence ou une paire circulaire apparaît, ou si la référence grandit.
"""
import argparse, collections, hashlib, json, os, re, subprocess, sys
from html.parser import HTMLParser
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from ck_common import ROOT, load_all, norm, strings, strip_tags  # noqa: E402

VERSION = 'lyncee-2'  # lyncee-2 : corpus étendu aux monographies (data/ck/mono)
SUFFIXES = ('ite', 'ites', 'ose', 'oses', 'algie', 'algies', 'emie', 'emies', 'pathie', 'pathies', 'plegie',
            'plegies', 'paresie', 'ectomie', 'tomie', 'stomie', 'scopie', 'graphie', 'gramme', 'plastie',
            'urie', 'pnee', 'rragie', 'rrhee', 'cele', 'lyse', 'penie', 'cytose', 'ome', 'omes', 'oide',
            'oides', 'emique', 'pathique', 'plegique', 'algique', 'ectasie', 'trophie', 'esthesie', 'phasie',
            'praxie', 'gnosie', 'megalie', 'plasie', 'opie', 'cardie', 'ptose', 'sclerose', 'stenose', 'itis')
PREFIXES = ('hyper', 'hypo', 'dys', 'tachy', 'brady', 'hemi', 'hemat', 'hemo', 'cardio', 'neuro', 'gastro',
            'hepat', 'nephr', 'pneumo', 'osteo', 'arthr', 'myo', 'dermat', 'encephal', 'chole', 'angio',
            'thrombo', 'leuco', 'erythro', 'ophtalm', 'oto', 'rhino', 'laryng', 'pharyng', 'oesophag',
            'cysto', 'uro', 'pyelo', 'spondyl', 'myel', 'radicul', 'polyneur', 'hydro', 'lymph', 'adeno',
            'cholecyst', 'endo', 'peri', 'intra', 'sous-', 'sus-', 'extra')
EPONYME = re.compile(
    r"\b(signe|signes|maladie|syndrome|manoeuvre|manœuvre|test|reflexe|réflexe|triade|score|classification"
    r"|critères|criteres|échelle|echelle|phénomène|phenomene|tétrade|tetrade|épreuve|epreuve|point|loi"
    r"|paralysie|tumeur|ulcère|ulcere|nodule|nodules|anneau|cercle|fracture|luxation)"
    r"\s+(?:de\s+|d['’]\s?|du\s+)((?:[A-ZÉÈÀ][a-zà-ÿ'’-]+)(?:(?:\s+et\s+|-|\s+)[A-ZÉÈÀ][a-zà-ÿ'’-]+){0,2})")
MOT = re.compile(r"[A-Za-zÀ-ÖØ-öø-ÿŒœ][A-Za-zÀ-ÖØ-öø-ÿŒœ0-9-]*")
ABREV = re.compile(r'^(?=(?:[^A-Z]*[A-Z]){2})[A-Za-z0-9]{2,7}$')
ROMAIN = re.compile(r'^(?=[IVXLC]+$)M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$')
MAJ_COURANTS = {'ET', 'OU', 'LE', 'LA', 'LES', 'DE', 'DU', 'DES', 'UN', 'UNE', 'EN', 'NE', 'PAS', 'OUI', 'NON',
                'SI', 'AU', 'AUX', 'PAR', 'POUR', 'SUR', 'AVEC', 'SANS', 'EST', 'SONT', 'CE', 'QUI', 'QUE'}
REGLES = hashlib.sha256(repr((VERSION, SUFFIXES, PREFIXES, EPONYME.pattern, ABREV.pattern,
                              sorted(MAJ_COURANTS))).encode()).hexdigest()[:12]


class _Texte(HTMLParser):
    """Texte visible du HTML statique (hors script, style, code)."""
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.skip, self.out = 0, []

    def handle_starttag(self, tag, attrs):
        if tag in ('script', 'style', 'code', 'pre', 'template'):
            self.skip += 1

    def handle_endtag(self, tag):
        if tag in ('script', 'style', 'code', 'pre', 'template') and self.skip:
            self.skip -= 1

    def handle_data(self, d):
        if not self.skip and d.strip():
            self.out.append(d)


def _json_strings(v, path):
    if isinstance(v, str):
        yield path, v
    elif isinstance(v, list):
        for i, x in enumerate(v):
            yield from _json_strings(x, f'{path}[{i}]')
    elif isinstance(v, dict):
        for k, x in v.items():
            if k in ('s', 'fs', 'src', 'u', 'id', 'k'):  # sources, URL et identifiants
                continue
            yield from _json_strings(x, f'{path}.{k}')


MONO_NON_TEXTE = {'src', 'lu', 'id', 'ssp'}
CS_NON_TEXTE = {'ssp', 'format', 'ges', 'competences', 'dim', 'redige_par', 'session'}


def corpus(root):
    """Rend (origine, texte) pour tout le texte affiché, définitions du glossaire comprises."""
    app = os.path.join(root, 'app_v2.html')
    if os.path.exists(app):
        sys.path.insert(0, os.path.join(root, 'tools'))
        s = open(app, encoding='utf-8').read()
        for name in ('TIP', 'NOT', 'GES'):
            a, b = _span(s, name)
            if a is not None:
                for p, t in _json_strings(json.loads(s[a:b]), name):
                    yield p, strip_tags(t)
        p = _Texte()
        p.feed(s)
        for i, t in enumerate(p.out):
            yield f'html[{i}]', t
    for name, items in load_all(root).items():
        for p, _, t in strings(items, name):
            yield p, t
    # Monographies des différentiels (data/ck/mono) : tout le texte affiché, sauf source et date.
    mdir = os.path.join(root, 'data', 'ck', 'mono')
    if os.path.isdir(mdir):
        for fn in sorted(os.listdir(mdir)):
            if fn.endswith('.json'):
                for k, e in json.load(open(os.path.join(mdir, fn), encoding='utf-8')).items():
                    for champ, t in e.items():
                        if champ not in MONO_NON_TEXTE and isinstance(t, str):
                            yield f'mono.{k}.{champ}', strip_tags(t)
    # Stations CS (data/cs) : même texte affiché, sauf les codes propres aux stations.
    for name in ('format', 'stations'):
        f = os.path.join(root, 'data', 'cs', name + '.json')
        if os.path.exists(f):
            for p, champ, t in strings(json.load(open(f, encoding='utf-8')), 'cs.' + name):
                if champ not in CS_NON_TEXTE:
                    yield p, t


def _span(s, name):
    for k in ('\nconst ' + name + '=', '\nlet ' + name + '='):
        if s.count(k) == 1:
            a = s.find(k) + len(k)
            return a, json.JSONDecoder().raw_decode(s, a)[1]
    return None, None


def candidats(texts):
    """Rend {clé normalisée: [forme affichée, occurrences, première origine]}."""
    c = {}

    def add(key, form, where):
        e = c.get(key)
        if e:
            e[1] += 1
        else:
            c[key] = [form, 1, where]

    for where, t in texts:
        for m in EPONYME.finditer(t):
            form = f'{m.group(1)} de {m.group(2)}'
            add(norm(form), form, where)
        for w in MOT.findall(t):
            w = w.strip('-')
            if len(w) < 2:
                continue
            if ABREV.match(w) and not ROMAIN.match(w) and w not in MAJ_COURANTS and not w.isdigit():
                add(w, w, where)  # abréviation : casse exacte
                continue
            n = norm(w)
            if len(n) < 6 or not n.isascii() or any(ch.isdigit() for ch in n):
                continue
            if n.endswith(SUFFIXES) or (n.startswith(PREFIXES) and len(n) >= 8):
                add(n, w.lower(), where)
    # Pluriel : « cyanoses » rejoint « cyanose » quand les deux existent.
    for k in [k for k in c if k.endswith(('s', 'x')) and k[:-1] in c]:
        c[k[:-1]][1] += c.pop(k)[1]
    return c


def definis(root, data):
    d, abr = set(), set()
    for e in data['glo']:
        forms = [e.get('label', '')] + e.get('alias', []) + e.get('flexions', [])
        for f in forms:
            if not f:
                continue
            (abr.add(f) if e.get('type') == 'abreviation' else None)
            d.add(norm(f))
    excl = os.path.join(root, 'qa', 'termes_exclus.txt')
    bad = []
    if os.path.exists(excl):
        for i, l in enumerate(open(excl, encoding='utf-8'), 1):
            l = l.rstrip('\n')
            if not l.strip() or l.startswith('#'):
                continue
            term, _, motif = l.partition('\t')
            if not motif.strip():
                bad.append(f'qa/termes_exclus.txt:{i} « {term} » n’a pas de motif')
            d.add(norm(term)); abr.add(term.strip())
    return d, abr, bad


def est_defini(key, d, abr):
    if ABREV.match(key) and key == key.strip() and not key.islower():
        return key in abr or norm(key) in d
    return key in d or (key.endswith(('s', 'x')) and key[:-1] in d)


def graphe(data, d_forms):
    """Contrôles du glossaire : renvois, auto-références, paires circulaires, profondeur."""
    errs = []
    ids = {e['id'] for e in data['glo'] if 'id' in e}
    forms = {}
    for e in data['glo']:
        for f in [e.get('label', '')] + e.get('alias', []) + e.get('flexions', []):
            if f and len(norm(f)) > 2:
                forms[norm(f)] = e['id']
    pat = re.compile(r'\b(' + '|'.join(sorted(map(re.escape, forms), key=len, reverse=True)) + r')\b') if forms else None
    edges = collections.defaultdict(set)
    for e in data['glo']:
        own = {norm(f) for f in [e.get('label', '')] + e.get('alias', []) if f}
        txt = norm(' '.join(t for _, _, t in strings(e)))
        for r in e.get('composantes', []) + e.get('voir', []):
            if r not in ids:
                errs.append(f"glo|{e['id']} renvoie à glo|{r}, qui n’existe pas")
            elif r == e['id']:
                errs.append(f"glo|{e['id']} se cite lui-même dans ses renvois")
            edges[e['id']].add(r)
        for f in own:
            if f and re.search(r'\b' + re.escape(f) + r'\b', norm(e.get('def', ''))):
                errs.append(f"glo|{e['id']} : auto-référence, la définition emploie « {f} »")
        if pat:
            for m in pat.finditer(txt):
                t = forms[m.group(1)]
                if t != e['id']:
                    edges[e['id']].add(t)
    for a, refs in edges.items():
        for b in refs:
            if a < b and edges.get(b) == {a} and refs == {b}:
                errs.append(f'paire circulaire : glo|{a} et glo|{b} ne se définissent que l’un par l’autre')
    depth = {}

    def dfs(n, seen):
        if n in depth:
            return depth[n]
        if len(seen) > 6:
            return 0
        v = 1 + max((dfs(m, seen | {n}) for m in edges.get(n, ()) if m not in seen), default=0)
        depth[n] = v
        return v
    prof = max((dfs(n, frozenset()) for n in ids), default=0)
    return errs, prof, edges


def renvois_texte(root, data):
    """Chaque identifiant glo|… cité dans l'application ou les données doit exister."""
    ids = {e['id'] for e in data['glo']}
    errs = []
    app = os.path.join(root, 'app_v2.html')
    blobs = [open(app, encoding='utf-8').read()] if os.path.exists(app) else []
    blobs += [json.dumps(v, ensure_ascii=False) for v in data.values()]
    for b in blobs:
        for m in re.finditer(r'glo\|([a-z0-9][a-z0-9-]*)', b):
            if m.group(1) not in ids:
                errs.append(f'glo|{m.group(1)} est cité mais n’existe pas dans data/ck/glo.json')
    return sorted(set(errs))


def arbres_branches(root, motifs):
    """Extrait (git archive) le texte affiché de chaque branche distante qui suit un motif ; rend [(ref, dossier)]."""
    import fnmatch, tarfile, tempfile, io
    refs = subprocess.run(['git', 'for-each-ref', '--format=%(refname:short)', 'refs/remotes/origin'],
                          cwd=root, capture_output=True, text=True).stdout.split()
    out = []
    for r in refs:
        nom = r.split('/', 1)[-1]
        if nom in ('HEAD', 'main') or not any(fnmatch.fnmatch(nom, m) for m in motifs):
            continue
        d = tempfile.mkdtemp(prefix='lyncee-')
        p = subprocess.run(['git', 'archive', r, 'app_v2.html', 'data/ck', 'data/cs', 'qa/termes_exclus.txt'],
                           cwd=root, capture_output=True)
        if p.returncode != 0:  # chemin absent dans une vieille branche : on reprend sans data/cs
            p = subprocess.run(['git', 'archive', r, 'app_v2.html', 'data/ck'], cwd=root, capture_output=True)
        if p.returncode == 0:
            tarfile.open(fileobj=io.BytesIO(p.stdout)).extractall(d, filter='data')
            out.append((nom, d))
    return out


def recensement(root, motifs):
    """Termes non définis dans main ET dans les branches ouvertes, classés par fréquence décroissante.
    Un terme défini dans une branche (glossaire en attente de fusion) est marqué « en attente »."""
    arbres = [('main', root)] + arbres_branches(root, motifs)
    tous, d_all, abr_all = {}, set(), set()
    for nom, d in arbres:
        dd, aa, _ = definis(d, load_all(d))
        d_all |= dd; abr_all |= aa
    d0, a0, _ = definis(root, load_all(root))
    for nom, d in arbres:
        for k, (f, n, where) in candidats(corpus(d)).items():
            if est_defini(k, d0, a0):
                continue
            e = tous.setdefault(k, [f, 0, where, []])
            e[1] = max(e[1], n); e[3].append(nom)
    rows = sorted(([k] + v + [est_defini(k, d_all, abr_all)] for k, v in tous.items()), key=lambda x: (-x[2], x[0]))
    return rows, [n for n, _ in arbres]


def baseline_de(root, ref, path):
    """Référence lue dans la branche de base (git show), ou None."""
    rel = os.path.relpath(path, root)
    p = subprocess.run(['git', 'show', f'{ref}:{rel}'], cwd=root, capture_output=True, text=True)
    return json.loads(p.stdout) if p.returncode == 0 else None


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument('--racine', default=ROOT)
    ap.add_argument('--baseline', default=None)
    ap.add_argument('--diff', default=None, help='branche de base : la référence ne peut que baisser')
    ap.add_argument('--update', action='store_true', help='resserre la référence (jamais d’ajout)')
    ap.add_argument('--init', action='store_true', help='crée la référence si elle n’existe pas')
    ap.add_argument('--json', default=None)
    ap.add_argument('--branches', nargs='*', default=None, metavar='MOTIF',
                    help='recensement : main + branches origin/<motif> (défaut feat/*), classé par fréquence')
    ap.add_argument('--top', type=int, default=60)
    ap.add_argument('--inclure-branches', action='store_true',
                    help='avec --init : la référence couvre aussi les termes des branches ouvertes')
    a = ap.parse_args(argv)
    root = a.racine
    if a.branches is not None:
        rows, noms = recensement(root, a.branches or ['feat/*'])
        print(f'Lyncée · recensement ({len(noms)} arbres : {", ".join(noms)}) : {len(rows)} termes non définis '
              f'dans main, dont {sum(r[5] for r in rows)} en attente dans une branche.')
        for r in rows[:a.top]:
            print(f'{r[2]:6d}  {r[1]}{"  (en attente)" if r[5] else ""}  [{", ".join(r[4][:3])}]')
        if a.json:
            os.makedirs(os.path.dirname(os.path.abspath(a.json)), exist_ok=True)
            json.dump({'regles': REGLES, 'arbres': noms, 'non_definis': rows},
                      open(a.json, 'w', encoding='utf-8'), ensure_ascii=False, indent=0)
        return 0
    bl_path = a.baseline or os.path.join(root, 'qa', 'termes-baseline.json')
    data = load_all(root)
    c = candidats(corpus(root))
    d, abr, errs = definis(root, data)
    nd = {k: v for k, v in c.items() if not est_defini(k, d, abr)}
    g_errs, prof, _ = graphe(data, d)
    errs += g_errs + renvois_texte(root, data)
    print(f'Lyncée ({VERSION}, règles {REGLES}) : {len(c)} candidats, {len(c) - len(nd)} définis ou exclus, '
          f'{len(nd)} non définis ; glossaire {len(data["glo"])} entrées, profondeur maximale {prof}.')
    if a.json:
        os.makedirs(os.path.dirname(os.path.abspath(a.json)), exist_ok=True)
        json.dump({'regles': REGLES, 'non_definis': sorted(([k] + v for k, v in nd.items()), key=lambda x: -x[2])},
                  open(a.json, 'w', encoding='utf-8'), ensure_ascii=False, indent=0)
    if not os.path.exists(bl_path):
        if a.init:
            if a.inclure_branches:
                rows, _ = recensement(root, ['feat/*'])
                nd = dict(nd, **{r[0]: r[1:4] for r in rows if not r[5]})
            _write(bl_path, sorted(nd))
            print(f'Référence créée : {len(nd)} termes.')
            return 0
        print('ÉCHEC référence absente :', bl_path)
        return 1
    bl = json.load(open(bl_path, encoding='utf-8'))
    base = set(bl['termes'])
    nouveaux = sorted(set(nd) - base)
    resolus = sorted(base - set(nd))
    if a.update:
        if bl.get('regles') != REGLES:
            print('ÉCHEC --update refusé : les règles ont changé ; régénérez avec --init après revue de Janus.')
            return 1
        _write(bl_path, sorted(base & set(nd)))
        print(f'Référence resserrée : {len(base)} → {len(base & set(nd))} termes.')
        base = base & set(nd)
        resolus = []
    if a.diff:
        old = baseline_de(root, a.diff, bl_path)
        if old is not None:
            grew = sorted(base - set(old['termes']))
            if grew and old.get('regles') == bl.get('regles'):
                errs.append(f'la référence grandit de {len(grew)} termes (ex. {", ".join(grew[:5])}) : interdit')
            elif grew:
                print(f'AVERTISSEMENT règles modifiées ({old.get("regles")} → {bl.get("regles")}) : '
                      f'{len(grew)} termes nouveaux dans la référence, à revoir par Janus.')
    if bl.get('regles') != REGLES:
        errs.append(f'la référence a été produite avec les règles {bl.get("regles")}, pas {REGLES} : régénérez-la')
    for k in nouveaux:
        f, n, where = nd[k]
        errs.append(f'terme nouveau non défini : « {f} » ({n}×, ex. {where}) → data/ck/glo.json ou qa/termes_exclus.txt')
    if resolus:
        print(f'{len(resolus)} termes de la référence sont désormais définis : lancez --update pour la resserrer.')
    for e in errs[:200]:
        print('ÉCHEC', e)
    if len(errs) > 200:
        print(f'… et {len(errs) - 200} autres échecs.')
    print(f'Lyncée : {len(nouveaux)} terme(s) nouveau(x) non défini(s) ; référence {len(base)}.')
    return 1 if errs else 0


def _write(path, termes):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w', encoding='utf-8') as f:
        json.dump({'outil': VERSION, 'regles': REGLES, 'total': len(termes),
                   'note': 'Référence de Lyncée : elle ne peut que baisser (tools/lyncee.py --update).',
                   'termes': termes}, f, ensure_ascii=False, indent=0)
        f.write('\n')


if __name__ == '__main__':
    sys.exit(main())
