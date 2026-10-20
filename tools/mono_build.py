"""Monographies des diagnostics différentiels (Hygie, 17.10.2026).

data/ck/mono/<tranche>.json → assets/mono/mono-<tranche>.js (window.CK_MONO_<TRANCHE>), chargé à la demande
(patch 0026) ; budget propre assets/mono/ dans tools/budget.py (hors budget assets/ck).
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
DATA, OUT = os.path.join(ROOT, 'data/ck/mono'), os.path.join(ROOT, 'assets/mono')
NEW_EXP = ('exp_ref', 'exp_premier', 'exp_bio', 'exp_morph', 'exp_fonc')
REQ = ['def', 'epi', 'phy', 'cli', 'exp', 'dia', 'but', 'mes', 'pha', 'src', 'lu', 'n']
SSP_DATA = os.path.join(ROOT, 'data/ck/mono_ssp.json')
SSP_OUT = os.path.join(OUT, 'mono-ssp.js')


def mid(name):
    x = ''.join(c for c in unicodedata.normalize('NFKD', name.lower()) if not unicodedata.combining(c))
    return re.sub(r'[^a-z0-9]+', '-', x).strip('-')


def tranche(k):
    return k[0] if 'a' <= k[0] <= 'z' else '0'


def html(e):
    """Render six protocol rubrics; legacy diagnosis text stays within rubric 5."""
    lines = [
        f'<b>1. Généralité &amp; Définition :</b> {e["def"]}',
        f'<b>2. Épidémiologie et Sex Ratio :</b> {e["epi"]}',
        f'<b>3. Physiopathologie :</b> {str(e["phy"]).replace(chr(10), "<br>")}',
        f'<b>4. Sémiologie clinique :</b> {str(e["cli"]).replace(chr(10), "<br>")}',
        '<b>5. Sémiologie aux explorations</b>',
    ]
    labels = {
        'exp_ref': 'Examen de référence diagnostique', 'exp_premier': 'À faire en premier',
        'exp_bio': 'Biologie', 'exp_morph': 'Morphologie', 'exp_fonc': 'Explorations fonctionnelles',
    }
    if chronologie_ready(e):
        lines.append(f'<b>{labels["exp_ref"]} :</b> {e["exp_ref"]}')
        lines.append('<b>Bilan ordonné</b>')
        bilan = e['bilan_ordre']
        for index, step in enumerate(bilan, 1):
            title = 'À faire en premier' if index == 1 else step['titre']
            lines.append(f'<b>{index} — {title} :</b> {step["texte"]}')
        # The ordered timeline replaces the old unordered exploration fields.
        # Keep the full diagnostic criteria once, after the timeline.
        lines.append(f'<b>Critères diagnostiques :</b> {e["dia"]}')
    else:
        # Prototype-free legacy records retain their existing rendering.
        lines.extend(f'<b>{labels[k]} :</b> {e[k]}' for k in NEW_EXP if e.get(k))
        lines.append(f'<b>Explorations :</b> {e["exp"]}')
        lines.append(f'<b>Critères diagnostiques :</b> {e["dia"]}')
    lines.extend([
        '<b>6. Prise en charge</b>',
        f'<b>A- But :</b> {e["but"]}',
        '<b>B- Moyens</b>',
    ])
    if chronologie_ready(e):
        for index, phase in enumerate(e['pec_ordre'], 1):
            lines.append(f'<b>Phase {index} — {phase["titre"]}</b>')
            categories = (('mes', 'Mesures générales'), ('pha', 'Pharmacologie'), ('aut', 'Autres'))
            for key, label in categories:
                if phase.get(key):
                    lines.append(f'<b>{label} :</b> {phase[key]}')
    else:
        lines.extend([f'<b>Mesures générales :</b> {e["mes"]}', f'<b>Pharmacologie :</b> {e["pha"]}'])
        if e.get('aut'):
            lines.append(f'<b>Autres :</b> {e["aut"]}')
    return '<br>'.join(lines)


def chronologie_errors(e):
    """Validate the opt-in ordered diagnostic and care timelines; legacy is allowed."""
    fields = ('chronologie_version', 'bilan_ordre', 'pec_ordre')
    if not any(field in e for field in fields):
        return []
    errors = []
    if type(e.get('chronologie_version')) is not int or e.get('chronologie_version') != 1:
        errors.append('chronologie_version doit être le nombre 1')
    bilan = e.get('bilan_ordre')
    if not isinstance(bilan, list) or not 1 <= len(bilan) <= 6:
        errors.append('bilan_ordre doit contenir de 1 à 6 étapes')
    else:
        for index, step in enumerate(bilan, 1):
            if not isinstance(step, dict) or set(step) != {'titre', 'texte'}:
                errors.append(f'bilan_ordre[{index}] exige seulement titre et texte')
                continue
            if not isinstance(step.get('titre'), str) or not step['titre'].strip():
                errors.append(f'bilan_ordre[{index}].titre doit être non vide')
            if not isinstance(step.get('texte'), str) or not step['texte'].strip():
                errors.append(f'bilan_ordre[{index}].texte doit être non vide')
        if isinstance(bilan[0], dict):
            if bilan[0].get('titre') != 'À faire en premier':
                errors.append('bilan_ordre[0].titre doit être « À faire en premier »')
            if not isinstance(e.get('exp_premier'), str) or bilan[0].get('texte') != e.get('exp_premier'):
                errors.append('bilan_ordre[0].texte doit reprendre exp_premier à l’identique')
    pec = e.get('pec_ordre')
    if not isinstance(pec, list) or not 1 <= len(pec) <= 6:
        errors.append('pec_ordre doit contenir de 1 à 6 phases')
    else:
        couvert = set()
        for index, phase in enumerate(pec, 1):
            if not isinstance(phase, dict) or not {'titre'} <= phase.keys() or phase.keys() - {'titre', 'mes', 'pha', 'aut'}:
                errors.append(f'pec_ordre[{index}] exige titre et seulement mes, pha, aut facultatifs')
                continue
            if not isinstance(phase.get('titre'), str) or not phase['titre'].strip():
                errors.append(f'pec_ordre[{index}].titre doit être non vide')
            contenus = []
            for field in ('mes', 'pha', 'aut'):
                if field in phase:
                    if not isinstance(phase[field], str) or not phase[field].strip():
                        errors.append(f'pec_ordre[{index}].{field} doit être non vide si présent')
                    else:
                        couvert.add(field)
                        contenus.append(phase[field])
            if not contenus:
                errors.append(f'pec_ordre[{index}] doit contenir au moins un moyen')
        if not {'mes', 'pha'} <= couvert:
            errors.append('pec_ordre doit couvrir mesures générales (mes) et pharmacologie (pha)')
    return errors


def chronologie_ready(e):
    """True when both ordered timelines meet the schema and required coverage."""
    return bool(e.get('chronologie_version') == 1 and not chronologie_errors(e)
                and isinstance(e.get('bilan_ordre'), list) and isinstance(e.get('pec_ordre'), list))


def text_fields(value, path=''):
    """Yield every nested string and its JSON-like path for recursive guards."""
    if isinstance(value, str):
        yield path, value
    elif isinstance(value, dict):
        for key, item in value.items():
            child = f'{path}.{key}' if path else str(key)
            yield from text_fields(item, child)
    elif isinstance(value, list):
        for index, item in enumerate(value):
            yield from text_fields(item, f'{path}[{index}]')


def prototype_ready(e):
    """True when the opt-in record has the complete six-rubric structure; not a clinical review."""
    version = e.get('prototype_version')
    return (type(version) is int and version == 1
            and all(isinstance(e.get(k), str) and e[k].strip() for k in REQ + list(NEW_EXP))
            and chronologie_ready(e))


def load():
    M = {}
    for f in sorted(glob.glob(os.path.join(DATA, '*.json'))):
        for k, e in json.load(open(f, encoding='utf-8')).items():
            if k.startswith('_'):
                continue
            assert k not in M, 'clé en double : ' + k
            M[k] = (os.path.basename(f)[:-5], e)
    return M


def load_ssp(root=ROOT):
    path = os.path.join(root, 'data/ck/mono_ssp.json')
    return json.load(open(path, encoding='utf-8')) if os.path.exists(path) else None


def catalogue_ssp(root=ROOT):
    app = open(os.path.join(root, 'app_v2.html'), encoding='utf-8').read()
    a, b = _app.span(app, 'SSP')
    return {x[0]: x[1] for x in json.loads(app[a:b])}


def _field_errors(k, e, require_prototype=False):
    err = []
    for f in REQ:
        if not str(e.get(f, '')).strip(): err.append(f'{k} : champ {f} vide')
    if require_prototype and 'prototype_version' not in e:
        err.append(f'{k} : les monographies SSP doivent déclarer prototype_version: 1')
    if 'prototype_version' in e:
        version = e.get('prototype_version')
        if not (type(version) is int and version == 1):
            err.append(f'{k} : prototype_version doit être le nombre 1')
        else:
            for f in NEW_EXP:
                if not isinstance(e.get(f), str) or not e[f].strip():
                    err.append(f'{k} : champ prototype {f} doit être une chaîne non vide')
    for message in chronologie_errors(e):
        err.append(f'{k} : {message}')
    for path, value in text_fields(e):
        if re.search(r'<(b|strong)\b', value, re.I): err.append(f'{k}.{path} : gras réservé aux titres')
    if not re.search(r'\d{2}\.\d{2}\.\d{4}', e.get('lu', '')): err.append(f'{k} : date de lecture absente')
    pharmacology = [('pha', e.get('pha', ''))]
    if isinstance(e.get('pec_ordre'), list):
        pharmacology.extend((f'pec_ordre[{i}].pha', phase.get('pha', ''))
                            for i, phase in enumerate(e['pec_ordre']) if isinstance(phase, dict))
    for path, phrase in pharmacology:
        if (isinstance(phrase, str) and re.search(r'\d\s?(mg|µg|g|mmol|UI)\b', phrase)
                and 'AIPS' not in e.get('src', '') + phrase):
            err.append(f'{k}.{path} : dose sans AIPS lue (écrire « dose : à vérifier (AIPS) »)')
    return err


def errors(M, names):
    err = []
    for k, (t, e) in M.items():
        if mid(e.get('n', '')) != k: err.append(f'{k} : clé ≠ libellé normalisé')
        if t != tranche(k): err.append(f'{k} : mauvaise tranche {t}')
        if k not in names: err.append(f'{k} : aucun diagnostic de NOT ne porte ce libellé')
        err.extend(_field_errors(k, e))
    return err


def errors_ssp(M, names):
    """Validate SSP-keyed monographies against the app catalogue; all entries are opt-in prototypes."""
    err = []
    for code, e in M.items():
        if code not in names:
            err.append(f'{code} : code SSP absent du catalogue app')
        elif e.get('n') != names[code]:
            err.append(f'{code} : n ≠ libellé SSP du catalogue (« {names[code]} »)')
        err.extend(_field_errors(code, e, require_prototype=True))
    return err


def build(M):
    T = {}
    for k, (t, e) in M.items():
        T.setdefault(t, {})[k] = {'h': html(e), 's': e['src'] + ' · lu le ' + e['lu']}
    return {t: '/* Généré par tools/mono_build.py depuis data/ck/mono/ : ne pas modifier à la main. */\n'
            f'window.CK_MONO_{t.upper()}=' + json.dumps(dict(sorted(v.items())), ensure_ascii=False, separators=(',', ':')) + ';\n'
            for t, v in T.items()}


def build_ssp(M):
    """Build the dedicated SSP asset consumed by monoLoad('ssp')."""
    V = {code: {'h': html(e), 's': e['src'] + ' · lu le ' + e['lu']} for code, e in sorted(M.items())}
    return '/* Généré par tools/mono_build.py depuis data/ck/mono_ssp.json : ne pas modifier à la main. */\n' \
        + 'window.CK_MONO_SSP=' + json.dumps(V, ensure_ascii=False, separators=(',', ':')) + ';\n'


def main():
    s = _app.read()
    NOT = json.loads(s[slice(*_app.span(s, 'NOT'))])
    if '--draft' in sys.argv:
        c = sys.argv[sys.argv.index('--draft') + 1]
        from tip_data import load as load_tip
        TIP = load_tip(ROOT, s)
        M = load()
        for n, d in zip(NOT[c][0], TIP[c]['d']):
            print('##', mid(n), '(fait)' if mid(n) in M else '', '|', re.sub(r'\s+', ' ', d))
        return
    names = {mid(d) for v in NOT.values() for d in v[0] if d}
    M = load()
    err = errors(M, names)
    A = build(M)
    SSP = load_ssp()
    SSP_JS = None
    if SSP is not None:
        err.extend(errors_ssp(SSP, catalogue_ssp()))
        SSP_JS = build_ssp(SSP)
    if '--check' in sys.argv:
        for t, js in A.items():
            p = os.path.join(OUT, f'mono-{t}.js')
            if not os.path.exists(p) or open(p, encoding='utf-8').read() != js: err.append(f'{p} pas à jour')
        if SSP_JS is not None and (not os.path.exists(SSP_OUT) or open(SSP_OUT, encoding='utf-8').read() != SSP_JS):
            err.append(f'{SSP_OUT} pas à jour')
        print('\n'.join(err) or f'Monographies : {len(M)}/{len(names)} diagnostics, contrôle OK')
        sys.exit(1 if err else 0)
    if err: sys.exit('\n'.join(err))
    os.makedirs(OUT, exist_ok=True)
    for t, js in A.items():
        open(os.path.join(OUT, f'mono-{t}.js'), 'w', encoding='utf-8').write(js)
    if SSP_JS is not None:
        open(SSP_OUT, 'w', encoding='utf-8', newline='\n').write(SSP_JS)
    print(f'Monographies : {len(M)}/{len(names)} diagnostics')


if __name__ == '__main__':
    main()
