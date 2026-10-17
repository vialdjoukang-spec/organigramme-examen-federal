"""Monographies des diagnostics différentiels (Hygie, 17.10.2026).

data/ck/mono/<tranche>.json → assets/ck/mono-<tranche>.js (window.CK_MONO_<TRANCHE>).
Clé = libellé du diagnostic normalisé (minuscules, sans accents, tirets) ; une monographie
sert tous les SSP où le diagnostic apparaît.  Tranche = première lettre de la clé.
  python3 tools/mono_build.py            reconstruit les assets
  python3 tools/mono_build.py --check    contrôle (CI) : structure, clés, gras, doses, assets à jour
  python3 tools/mono_build.py --draft G1 imprime l'existant TIP.d d'un SSP (aide de rédaction)
"""
import json, os, re, sys, glob, unicodedata
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import _app
ROOT = _app.ROOT
DATA, OUT = os.path.join(ROOT, 'data/ck/mono'), os.path.join(ROOT, 'assets/ck')
CH = [('def', '1. Définition'), ('epi', '2. Épidémiologie'), ('phy', '3. Physiopathologie'),
      ('cli', '4. Syndrome clinique'), ('exp', '5. Syndrome aux explorations'), ('dia', '6. Diagnostic')]
PEC = [('but', 'But'), ('mes', 'Mesures générales'), ('pha', 'Pharmacologie'), ('aut', 'Autre')]
REQ = [k for k, _ in CH] + ['but', 'mes', 'pha', 'src', 'lu', 'n']


def mid(name):
    x = ''.join(c for c in unicodedata.normalize('NFKD', name.lower()) if not unicodedata.combining(c))
    return re.sub(r'[^a-z0-9]+', '-', x).strip('-')


def tranche(k):
    return k[0] if 'a' <= k[0] <= 'z' else '0'


def html(e):
    L = [f'<b>{t} :</b> {e[k]}' for k, t in CH]
    L.append('<b>7. Prise en charge :</b>')
    L += [f'• <b>{t} :</b> {e[k]}' for k, t in PEC if e.get(k)]
    return '<br>'.join(L)


def load():
    M = {}
    for f in sorted(glob.glob(os.path.join(DATA, '*.json'))):
        for k, e in json.load(open(f, encoding='utf-8')).items():
            if k.startswith('_'):
                continue
            assert k not in M, 'clé en double : ' + k
            M[k] = (os.path.basename(f)[:-5], e)
    return M


def errors(M, names):
    err = []
    for k, (t, e) in M.items():
        if mid(e.get('n', '')) != k: err.append(f'{k} : clé ≠ libellé normalisé')
        if t != tranche(k): err.append(f'{k} : mauvaise tranche {t}')
        if k not in names: err.append(f'{k} : aucun diagnostic de NOT ne porte ce libellé')
        for f in REQ:
            if not str(e.get(f, '')).strip(): err.append(f'{k} : champ {f} vide')
        for f, v in e.items():
            if isinstance(v, str) and re.search(r'<(b|strong)\b', v): err.append(f'{k}.{f} : gras réservé aux titres')
        if not re.search(r'\d{2}\.\d{2}\.\d{4}', e.get('lu', '')): err.append(f'{k} : date de lecture absente')
        for f in ('pha', 'aut'):  # Hérophile : « à vérifier (AIPS) » n'autorise pas un chiffre ; seule une AIPS lue le permet
            p = e.get(f, '')
            if re.search(r'\d\s?(mg|µg|mcg|g|mmol|UI|mL|ml)\b|/kg\b', p) and 'AIPS lue' not in p:
                err.append(f'{k}.{f} : dose chiffrée sans AIPS lue (écrire « dose : à vérifier (AIPS) » ou citer « AIPS lue le … »)')
    return err


def build(M):
    T = {}
    for k, (t, e) in M.items():
        T.setdefault(t, {})[k] = {'h': html(e), 's': e['src'] + ' · lu le ' + e['lu']}
    return {t: '/* Généré par tools/mono_build.py depuis data/ck/mono/ : ne pas modifier à la main. */\n'
            f'window.CK_MONO_{t.upper()}=' + json.dumps(dict(sorted(v.items())), ensure_ascii=False, separators=(',', ':')) + ';\n'
            for t, v in T.items()}


def main():
    s = _app.read()
    NOT = json.loads(s[slice(*_app.span(s, 'NOT'))])
    if '--draft' in sys.argv:
        c = sys.argv[sys.argv.index('--draft') + 1]
        TIP = json.loads(s[slice(*_app.span(s, 'TIP'))])
        M = load()
        V = TIP[c].get('v') or {}
        S = {x['id']: x for x in V.get('S', [])}
        for i, (n, d) in enumerate(zip(NOT[c][0], TIP[c]['d'])):
            print('##', mid(n), '(fait)' if mid(n) in M else '', '|', re.sub(r'\s+', ' ', d))
            for j in (V['d'][i][1] if i < len(V.get('d') or []) else []):
                print('   src :', S[j]['t'], '·', S[j].get('u', ''))  # sources vérifiées du DD : à reprendre dans « src »
        return
    names = {mid(d) for v in NOT.values() for d in v[0] if d}
    M = load()
    err = errors(M, names)
    A = build(M)
    if '--check' in sys.argv:
        for t, js in A.items():
            p = os.path.join(OUT, f'mono-{t}.js')
            if not os.path.exists(p) or open(p, encoding='utf-8').read() != js: err.append(f'{p} pas à jour')
        print('\n'.join(err) or f'Monographies : {len(M)}/{len(names)} diagnostics, contrôle OK')
        sys.exit(1 if err else 0)
    if err: sys.exit('\n'.join(err))
    for t, js in A.items():
        open(os.path.join(OUT, f'mono-{t}.js'), 'w', encoding='utf-8').write(js)
    print(f'Monographies : {len(M)}/{len(names)} diagnostics')


if __name__ == '__main__':
    main()
