#!/usr/bin/env python3
"""Atlas · compilateur des données CK : data/ck/*.json → assets/ck/*.js (contrôle G5).

  python3 tools/ck_build.py           # valide, puis écrit assets/ck/
  python3 tools/ck_build.py --check   # valide, et échoue si assets/ck/ n'est pas à jour

Validation : schémas JSON (data/ck/schema/, Draft 2020-12), identifiants uniques, renvois
croisés (glo, syn, hyp, nc, loc, doses_ch, src, modules de GES), chaîne complète (G5).
Sortie : une affectation « window.CK_<NOM>=… ; » compacte par fichier, triée par identifiant,
chargée à la demande par <script src> (compatible file://, contrairement à fetch) :
  glo-index.js  index du glossaire, chargé à l'inactivité : [id, type, libellé, formes, tranche]
  glo-<x>.js    définitions par tranche (première lettre de l'identifiant), au premier besoin
  syn.js, hyp.js, nc.js, loc.js, src.js, doses_ch.js : objets indexés par identifiant (loc : module)
Aucune donnée CK n'entre dans app_v2.html.
"""
import argparse, json, os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from ck_common import ROOT, FICHIERS, data_dir, load_all  # noqa: E402

ENTETE = '/* Généré par tools/ck_build.py depuis data/ck/ : ne pas modifier à la main. */\n'


def var_name(fichier):
    """glo-index → CK_GLO_INDEX ; même règle que ckLoad() dans app_v2.html."""
    return 'CK_' + re.sub(r'[^A-Z0-9]', '_', fichier.upper())


def schemas(root):
    from referencing import Registry, Resource
    d = os.path.join(data_dir(root), 'schema')
    res = {}
    for n in os.listdir(d):
        if n.endswith('.schema.json'):
            res[n] = json.load(open(os.path.join(d, n), encoding='utf-8'))
    reg = Registry().with_resources((k, Resource.from_contents(v)) for k, v in res.items())
    return res, reg


def ges(root):
    """Régions de GES (liste) lues dans app_v2.html, ou None si la constante manque."""
    app = os.path.join(root, 'app_v2.html')
    if not os.path.exists(app):
        return None
    s = open(app, encoding='utf-8').read()
    k = '\nconst GES='
    if s.count(k) != 1:
        return None
    return json.JSONDecoder().raw_decode(s, s.find(k) + len(k))[0]


def modules_ges(root):
    app = os.path.join(root, 'app_v2.html')
    if not os.path.exists(app):
        return None
    s = open(app, encoding='utf-8').read()
    k = '\nconst GES='
    if s.count(k) != 1:
        return None
    a = s.find(k) + len(k)
    return {g['id'] for g in json.JSONDecoder().raw_decode(s, a)[0]}


def validate(root):
    """Rend la liste des erreurs (fichier, élément, motif) ; vide si tout est conforme."""
    from jsonschema import Draft202012Validator
    res, reg = schemas(root)
    data = load_all(root)
    errs = []
    for n in FICHIERS:
        v = Draft202012Validator(res[n + '.schema.json'], registry=reg)
        for e in sorted(v.iter_errors(data[n]), key=lambda e: list(e.absolute_path)):
            p = list(e.absolute_path)
            ident = data[n][p[0]].get('id', data[n][p[0]].get('module', p[0])) if p and isinstance(p[0], int) and isinstance(data[n][p[0]], dict) else '-'
            errs.append((n, ident, f'schéma : {"/".join(map(str, p[1:])) or "racine"} : {e.message[:240]}'))
    sig = Draft202012Validator(res['sig.schema.json'], registry=reg)
    for e in data['glo']:
        if isinstance(e, dict) and e.get('type') == 'signe':
            for x in sig.iter_errors(e):
                errs.append(('glo', e.get('id'), f'signe : {x.message[:200]}'))
    if errs:
        return errs, data  # renvois croisés seulement sur des données bien formées
    ids = {}
    for n in FICHIERS:
        key = 'module' if n == 'loc' else 'id'
        seen = set()
        for e in data[n]:
            if e[key] in seen:
                errs.append((n, e[key], 'identifiant en double'))
            seen.add(e[key])
        ids[n] = seen

    def need(n, ident, champ, cible, refs):
        for r in refs:
            if r not in ids[cible]:
                errs.append((n, ident, f'{champ} renvoie à {cible}|{r}, qui n’existe pas'))

    def srcs(n, ident, obj):
        if isinstance(obj, dict):
            for r in obj.get('src', []) if isinstance(obj.get('src'), list) else []:
                if r['id'] not in ids['src']:
                    errs.append((n, ident, f'source {r["id"]} absente de data/ck/src.json'))
            for k, v in obj.items():
                if k != 'src':
                    srcs(n, ident, v)
        elif isinstance(obj, list):
            for v in obj:
                srcs(n, ident, v)

    mods = modules_ges(root)
    for e in data['glo']:
        need('glo', e['id'], 'composantes', 'glo', e.get('composantes', []))
        need('glo', e['id'], 'voir', 'glo', e.get('voir', []))
    for e in data['syn']:
        need('syn', e['id'], 'signes', 'glo', e['signes'])
        need('syn', e['id'], 'hyp', 'hyp', e['hyp'])
    for e in data['hyp']:
        need('hyp', e['id'], 'syn', 'syn', e['syn'])
        for m in e['pec']['moyens_specifiques']:
            if m.get('dose_ref'):
                need('hyp', e['id'], 'dose_ref', 'doses_ch', [m['dose_ref']])
    for e in data['nc']:
        for l in e['lesions']:
            need('nc', e['id'], f'lesions[{l["site"]}].syn', 'syn', [l['syn']])
            need('nc', e['id'], f'lesions[{l["site"]}].hyp', 'hyp', l['hyp'])
        for vue, p in e['vues'].items():
            if not os.path.exists(os.path.join(root, p)):
                errs.append(('nc', e['id'], f'vue {vue} : {p} introuvable'))
    ncs = {e['id']: e for e in data['nc']}
    for e in data['syn']:
        for lien in e.get('vues', []):
            _, nid, vue = lien.split('|')
            if nid not in ncs:
                errs.append(('syn', e['id'], f'vues renvoie à {nid}, absent de data/ck/nc.json'))
            elif not (ncs[nid].get('vues') or {}).get(vue):
                print(f'avertissement : syn {e["id"]} renvoie à la vue {nid}|{vue}, pas encore livrée ; '
                      f'l’affichage retombe sur la première vue disponible.', file=sys.stderr)
    for e in data['loc']:
        need('loc', e['module'], 'A', 'syn', e['A'])
        need('loc', e['module'], 'B', 'hyp', e['B'])
    G = ges(root)
    if G is not None:
        cles = {i['k'] for r in G for i in r['items']}
        for e in data['syn']:
            for k in e.get('gestes', []):
                if k not in cles:
                    errs.append(('syn', e['id'], f'gestes renvoie à la clé {k}, absente de GES'))
    if mods is not None:
        for n, key in (('syn', 'module'), ('loc', 'module')):
            for e in data[n]:
                if e[key] not in mods:
                    errs.append((n, e.get('id', e[key]), f'module {e[key]} absent de GES'))
    for n in FICHIERS:
        if n != 'src':
            for e in data[n]:
                srcs(n, e.get('id', e.get('module')), e)
    return errs, data


def js(name, value):
    return ENTETE + 'window.' + var_name(name) + '=' + json.dumps(value, ensure_ascii=False, separators=(',', ':'), sort_keys=True) + ';\n'


def tranche(ident):
    c = ident[0]
    return c if 'a' <= c <= 'z' else '0'


def build(data):
    """Rend {nom de fichier: contenu}, déterministe (tri stable par identifiant)."""
    out = {}
    glo = sorted(data['glo'], key=lambda e: e['id'])
    idx = [[e['id'], e['type'], e['label'], sorted(set([e['label']] + e.get('alias', []) + e.get('flexions', []))),
            tranche(e['id'])] for e in glo]
    out['glo-index.js'] = js('glo-index', {'v': 1, 'n': len(idx), 'e': idx})
    parts = {}
    for e in glo:
        parts.setdefault(tranche(e['id']), {})[e['id']] = e
    for t, d in sorted(parts.items()):
        out[f'glo-{t}.js'] = js(f'glo-{t}', d)
    for n in ('syn', 'hyp', 'nc', 'src', 'doses_ch'):
        out[n + '.js'] = js(n, {e['id']: e for e in sorted(data[n], key=lambda e: e['id'])})
    out['loc.js'] = js('loc', {e['module']: e for e in sorted(data['loc'], key=lambda e: e['module'])})
    return out


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument('--racine', default=ROOT)
    ap.add_argument('--check', action='store_true')
    a = ap.parse_args(argv)
    errs, data = validate(a.racine)
    for n, i, m in errs:
        print(f'ÉCHEC G5 {n}|{i} : {m}')
    if errs:
        print(f'ck_build : {len(errs)} erreur(s) ; rien n’est écrit.')
        return 1
    out = build(data)
    from prev_build import prev_js  # fréquences des diagnostics différentiels (data/ck/prev.json)
    out['prev.js'] = prev_js(a.racine)
    d = os.path.join(a.racine, 'assets', 'ck')
    present = {n for n in os.listdir(d) if n.endswith('.js') and not n.startswith('mono-')} if os.path.isdir(d) else set()  # mono-* : tools/mono_build.py
    if a.check:
        bad = [n for n, c in out.items() if not os.path.exists(os.path.join(d, n))
               or open(os.path.join(d, n), encoding='utf-8').read() != c]
        bad += [f'{n} (périmé)' for n in sorted(present - set(out))]
        for n in bad:
            print(f'ÉCHEC assets/ck/{n} n’est pas à jour : lancez python3 tools/ck_build.py')
        if bad:
            return 1
    else:
        os.makedirs(d, exist_ok=True)
        for n in present - set(out):
            os.remove(os.path.join(d, n))
        for n, c in out.items():
            with open(os.path.join(d, n), 'w', encoding='utf-8', newline='\n') as f:
                f.write(c)
    total = sum(len(c.encode('utf-8')) for c in out.values())
    print(f'ck_build : {sum(len(v) for v in data.values())} entrées valides ; {len(out)} fichiers, '
          f'{total} octets dans assets/ck/ ({"à jour" if a.check else "écrits"}).')
    return 0


if __name__ == '__main__':
    sys.exit(main())
