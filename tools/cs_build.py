#!/usr/bin/env python3
"""Chiron · compilateur des stations CS : data/cs/*.json → assets/st/*.js.

  python3 tools/cs_build.py           # valide, puis écrit assets/st/
  python3 tools/cs_build.py --check   # valide, et échoue si assets/st/ n'est pas à jour

Validation : schémas (data/cs/schema/, Draft 2020-12), identifiants uniques, renvois croisés
(SSP et GES de app_v2.html, hyp et src de data/ck/), date de lecture de chaque source,
aucune posologie chiffrée (« À vérifier » à la place), un verbe conjugué par phrase (G6).
Sortie, chargée à la demande par <script src> (compatible file://) :
  index.js      window.CS_ST_INDEX = {format, ssp: {SSP: [[id, titre, format], …]}}
  <id>.js       window.CS_ST_<ID> = la station
Aucune donnée CS n'entre dans app_v2.html.
"""
import argparse, json, os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(HERE, 'audit'))
ENTETE = '/* Généré par tools/cs_build.py depuis data/cs/ : ne pas modifier à la main. */\n'
PROSE = {'porte', 'taches', 'recit', 'emotions', 'jeu', 'texte', 't', 'pourquoi', 'attendu', 'pieges', 'a_verifier'}  # résultats et répliques du PS : style oral, hors G6
# Une dose (mg, µg, UI, éventuellement /kg) ; une concentration (mg/l, mmol/l) reste permise.
DOSE = re.compile(r'\d+(?:[.,]\d+)?\s*(?:mg|µg|mcg|UI|ml)(?:/kg)?(?![/\w])')


def var_name(ident):
    return 'CS_ST_' + re.sub(r'[^A-Z0-9]', '_', ident.upper())


def const(root, nom):
    s = open(os.path.join(root, 'app_v2.html'), encoding='utf-8').read()
    k = '\nconst ' + nom + '='
    if s.count(k) != 1:
        return None
    return json.JSONDecoder().raw_decode(s, s.find(k) + len(k))[0]


def load(root):
    d = os.path.join(root, 'data', 'cs')
    return (json.load(open(os.path.join(d, 'format.json'), encoding='utf-8')),
            json.load(open(os.path.join(d, 'stations.json'), encoding='utf-8')))


def strings(o, path=''):
    if isinstance(o, dict):
        for k, v in o.items():
            if isinstance(v, str):
                yield f'{path}/{k}', k, v
            else:
                for x in strings(v, f'{path}/{k}'):
                    yield x[0], (k if isinstance(v, list) and isinstance(x[2], str) and x[1] is None else x[1]), x[2]
    elif isinstance(o, list):
        for i, v in enumerate(o):
            if isinstance(v, str):
                yield f'{path}/{i}', None, v
            else:
                yield from strings(v, f'{path}/{i}')


def srcs(o):
    if isinstance(o, dict):
        for k, v in o.items():
            if k == 'src' and isinstance(v, list):
                yield from v
            else:
                yield from srcs(v)
    elif isinstance(o, list):
        for v in o:
            yield from srcs(v)


def validate(root):
    from jsonschema import Draft202012Validator
    from referencing import Registry, Resource
    sd = os.path.join(root, 'data', 'cs', 'schema')
    res = {n: json.load(open(os.path.join(sd, n), encoding='utf-8')) for n in os.listdir(sd) if n.endswith('.schema.json')}
    reg = Registry().with_resources((k, Resource.from_contents(v)) for k, v in res.items())
    fmt, st = load(root)
    errs = []
    for nom, doc in (('format', fmt), ('station', st)):
        v = Draft202012Validator(res[nom + '.schema.json'], registry=reg)
        for e in v.iter_errors(doc):
            p = list(e.absolute_path)
            ident = st[p[0]].get('id', p[0]) if nom == 'station' and p and isinstance(p[0], int) else nom
            errs.append((ident, f'schéma : {"/".join(map(str, p[1:]))} : {e.message[:200]}'))
    if errs:
        return errs, fmt, st
    ck = os.path.join(root, 'data', 'ck')
    src_ids = {e['id'] for e in json.load(open(os.path.join(ck, 'src.json'), encoding='utf-8'))}
    hyp_ids = {e['id'] for e in json.load(open(os.path.join(ck, 'hyp.json'), encoding='utf-8'))}
    ssp = {r[0] for r in (const(root, 'SSP') or [])}
    ges = {x.get('k') for g in (const(root, 'GES') or []) for x in g['items']}  # clé stable k, comme ckGes()
    fids = {f['id'] for f in fmt['formats']}
    try:
        from niveau1 import verbes, phrases, _elision_verbe
        V = verbes()
    except Exception:  # pragma: no cover
        V = None
    for r in srcs(fmt):
        if r['id'] not in src_ids:
            errs.append(('format', f'source {r["id"]} absente de data/ck/src.json'))
    vus = set()
    for s in st:
        i = s['id']
        if i in vus:
            errs.append((i, 'identifiant en double'))
        vus.add(i)
        if ssp and s['ssp'] not in ssp:
            errs.append((i, f'SSP {s["ssp"]} absente de const SSP'))
        if s['format'] not in fids:
            errs.append((i, f'format {s["format"]} absent de format.json'))
        for h in s.get('hyp', []):
            if h not in hyp_ids:
                errs.append((i, f'hyp {h} absente de data/ck/hyp.json'))
        for part, items in s['grille'].items():
            for n, it in enumerate(items):
                for g in it.get('ges', []):
                    if ges and g not in ges:
                        errs.append((i, f'grille/{part}/{n} : clé GES {g} inconnue'))
                for h in it.get('hyp', []):
                    if h not in hyp_ids:
                        errs.append((i, f'grille/{part}/{n} : hyp {h} absente'))
        for r in srcs(s):
            if r['id'] not in src_ids:
                errs.append((i, f'source {r["id"]} absente de data/ck/src.json'))
        for path, champ, t in strings(s):
            if DOSE.search(t):
                errs.append((i, f'{path} : posologie chiffrée interdite, écrire « À vérifier » : « {t[:80]} »'))
            if V is not None and not path.startswith('/resultats') and (champ in PROSE or path.split('/')[1] in ('pieges', 'a_verifier', 'taches')):
                for p, mots in phrases(t):
                    if not any(m.lower() in V for m in mots) and not _elision_verbe(p, V):
                        errs.append((i, f'{path} : phrase sans verbe conjugué : « {p[:90]} »'))
    return errs, fmt, st


def sortie(fmt, st):
    js = lambda o: json.dumps(o, ensure_ascii=False, separators=(',', ':'), sort_keys=False)
    idx = {}
    for s in sorted(st, key=lambda s: s['id']):
        idx.setdefault(s['ssp'], []).append([s['id'], s['titre'], s['format']])
    out = {'index.js': ENTETE + 'window.CS_ST_INDEX=' + js({'format': fmt, 'ssp': idx}) + ';\n'}
    for s in st:
        out[s['id'] + '.js'] = ENTETE + f'window.{var_name(s["id"])}=' + js(s) + ';\n'
    return out


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument('--check', action='store_true')
    ap.add_argument('--racine', default=os.path.dirname(HERE))
    a = ap.parse_args(argv)
    errs, fmt, st = validate(a.racine)
    for i, m in errs:
        print(f'cs_build : {i} : {m}', file=sys.stderr)
    if errs:
        return 1
    d = os.path.join(a.racine, 'assets', 'st')
    out = sortie(fmt, st)
    if a.check:
        bad = [n for n, c in out.items() if not os.path.exists(os.path.join(d, n)) or open(os.path.join(d, n), encoding='utf-8').read() != c]
        extra = [n for n in (os.listdir(d) if os.path.isdir(d) else []) if n not in out]
        for n in bad + extra:
            print(f'cs_build : assets/st/{n} pas à jour : lancez python3 tools/cs_build.py', file=sys.stderr)
        if bad or extra:
            return 1
        print(f'cs_build : {len(st)} stations valides, assets/st/ à jour.')
        return 0
    os.makedirs(d, exist_ok=True)
    for n in os.listdir(d):
        if n not in out:
            os.remove(os.path.join(d, n))
    for n, c in out.items():
        open(os.path.join(d, n), 'w', encoding='utf-8').write(c)
    print(f'cs_build : {len(st)} stations écrites dans assets/st/.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
