#!/usr/bin/env python3
"""Audit médical de niveau 1 · Janus et Galien · huit contrôles déterministes, zéro jeton (CI).

  python3 tools/audit/niveau1.py --only G2          # un contrôle (une étape de CI par contrôle)
  python3 tools/audit/niveau1.py --sortie qa/audit-flags.json   # tous, et l'artefact des signalements

G1 doses        chaque dose de data/ck renvoie (dose_ref) à une ligne de data/ck/doses_ch.json dont la dose
                la contient, sinon statut « À vérifier » ; TIP, NOT et GES : aucune dose nouvelle par rapport
                à qa/doses-baseline.json sans la mention « À vérifier » dans le même texte.
G2 sources      chaque affirmation porte src (lu_le ISO, au plus aujourd'hui) ou statut « À vérifier ».
G3 domaines     chaque URL appartient à qa/domaines.yml ; une source clinique a un éditeur suisse ou européen.
G4 termes       Lyncée : aucun terme nouveau non défini, renvois glo|id existants (tools/lyncee.py).
G5 chaîne       schémas JSON et renvois croisés : lésion, sémiologie, exploration, objectif, mesures, moyens.
G6 verbes       chaque phrase d'un champ rédigé contient une forme verbale conjuguée.
G7 rouge        le rouge n'apparaît que sur un élément bloquant (bloquant: true) ou de classe .urg.
G8 justification  chaque examen (exam.reference, exam.lignes) porte mecanisme, principe et pourquoi_ce_choix ;
                chaque moyen spécifique (pec.moyens_specifiques) porte en plus limites. Chaque champ est un texte
                d'au moins 20 caractères et 3 mots, distinct des autres champs du même élément ; une phrase
                « … À vérifier » est admise quand aucune source n'a été lue.
Le signalement (élément, contrôle, motif, fichier, ligne) s'écrit dans --sortie, même vide.
"""
import argparse, colorsys, gzip, json, os, re, subprocess, sys
from urllib.parse import urlparse
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(HERE))
from ck_common import ROOT, CHAMPS_PROSE, load_all, line_of, norm, strings, strip_tags, today  # noqa: E402

DOSE = re.compile(r'(?<![\w.,])(\d+(?:[.,]\d+)?(?:\s?(?:-|–|à)\s?\d+(?:[.,]\d+)?)?)\s?(mg|µg|mcg|g|UI|U|mmol|mL|ml)'
                  r'(?:\s?/\s?(kg|j|jour|h|m2|m²|dose|prise))?(?![\w/])(?!\s?/\s?(?:l|L|dL|dl|24|min|mol))')
STATUT_AV = 'À vérifier'
ROUGES = {'red', 'crimson', 'darkred', 'firebrick', 'tomato', 'orangered', 'indianred'}
VARS_ROUGES = ('--bad', '--c0', '--red', '--rouge', '--danger')


def flag(F, ctrl, elem, motif, fichier='', ligne=0):
    F.append({'controle': ctrl, 'element': elem, 'motif': motif, 'fichier': fichier, 'ligne': ligne})


def _elem(n, e):
    return f'{n}|{e.get("id", e.get("module", "?"))}'


def _where(root, n, e):
    return f'data/ck/{n}.json', line_of(root, n, e.get('id', e.get('module', '')))


def dose_norm(t):
    return re.sub(r'\s+', '', t.replace(',', '.').replace('–', '-').replace('mcg', 'µg').replace('ml', 'mL')).lower()


# ---------------------------------------------------------------- G1
def g1(root, data, F):
    table = {d['id']: d for d in data['doses_ch']}
    for d in data['doses_ch']:
        if not d.get('url', '').startswith(('https://www.swissmedicinfo.ch/', 'https://swissmedicinfo.ch/', 'https://swissmedicinfo-pro.ch/',
                                            'https://compendium.ch/', 'https://www.compendium.ch/', 'https://www.swissmedic.ch/')):
            flag(F, 'G1', _elem('doses_ch', d), 'la ligne ne renvoie pas à l’AIPS suisse (swissmedicinfo.ch ou compendium.ch)', *_where(root, 'doses_ch', d))

    def walk(n, top, obj):
        if isinstance(obj, list):
            for x in obj:
                walk(n, top, x)
            return
        if not isinstance(obj, dict):
            return
        own = [t for k, v in obj.items() if k not in ('src',) for t in ([v] if isinstance(v, str) else
               [x for x in v if isinstance(x, str)] if isinstance(v, list) else []) if k not in ('id', 'url', 'dose_ref')]
        doses = [m.group(0) for t in own for m in DOSE.finditer(strip_tags(t))]
        if doses and obj.get('statut') != STATUT_AV and top.get('statut') != STATUT_AV:
            ref = table.get(obj.get('dose_ref') or '')
            for d in doses:
                if not ref:
                    flag(F, 'G1', _elem(n, top), f'dose « {d} » sans dose_ref vers doses_ch.json ni statut « À vérifier »', *_where(root, n, top))
                elif not re.search(r'(?<![\d.])' + re.escape(dose_norm(d)) + r'(?![\d])', dose_norm(ref['dose'])):
                    flag(F, 'G1', _elem(n, top), f'dose « {d} » absente de la ligne {ref["id"]} (« {ref["dose"]} »)', *_where(root, n, top))
        for k, v in obj.items():
            if isinstance(v, (dict, list)) and k != 'src':
                walk(n, top, v)

    for n in ('glo', 'syn', 'hyp', 'nc'):
        for e in data[n]:
            walk(n, e, e)
    # Contenu hérité (TIP, NOT, GES) : aucune dose nouvelle sans « À vérifier ».
    bl_path = os.path.join(root, 'qa', 'doses-baseline.json')
    cur = doses_heritees(root)
    if cur is None:
        return
    if not os.path.exists(bl_path):
        flag(F, 'G1', 'qa/doses-baseline.json', 'référence des doses héritées absente (python3 tools/audit/niveau1.py --init-doses)')
        return
    bl = json.load(open(bl_path, encoding='utf-8'))['doses']
    for k, n in sorted(cur.items()):
        if n > bl.get(k, 0):
            flag(F, 'G1', k.split('|')[0], f'dose nouvelle « {k.split("|", 1)[1]} » dans le contenu hérité, sans source suisse ni « À vérifier »', 'app_v2.html', 0)


def doses_heritees(root):
    """{"<constante>.<clé>|<dose normalisée>": occurrences} pour TIP, NOT et GES, hors textes « À vérifier »."""
    app = os.path.join(root, 'app_v2.html')
    if not os.path.exists(app):
        return None
    s = open(app, encoding='utf-8').read()
    out = {}
    for name in ('TIP', 'NOT', 'GES'):
        k = '\nconst ' + name + '='
        if s.count(k) != 1:
            continue
        a = s.find(k) + len(k)
        v = json.JSONDecoder().raw_decode(s, a)[0]
        items = v.items() if isinstance(v, dict) else ((x.get('id', str(i)), x) for i, x in enumerate(v))
        for key, val in items:
            for t in _all_str(val):
                if STATUT_AV in t:
                    continue
                for m in DOSE.finditer(strip_tags(t)):
                    kk = f'{name}.{key}|{dose_norm(m.group(0))}'
                    out[kk] = out.get(kk, 0) + 1
    return out


def _all_str(v):
    if isinstance(v, str):
        yield v
    elif isinstance(v, list):
        for x in v:
            yield from _all_str(x)
    elif isinstance(v, dict):
        for x in v.values():
            yield from _all_str(x)


# ---------------------------------------------------------------- G2
def _src_ok(obj, auj):
    """'' si conforme, sinon le motif."""
    src = obj.get('src')
    if obj.get('statut') == STATUT_AV:
        return ''
    if not src:
        return 'ni src ni statut « À vérifier »'
    for r in src:
        if not r.get('lu_le'):
            return f'source {r.get("id")} sans date de lecture (lu_le)'
        if r['lu_le'] > auj:
            return f'source {r.get("id")} lue le {r["lu_le"]}, date future'
    return ''


def g2(root, data, F):
    auj = today()
    nested = {'hyp': [('exam.reference', lambda e: [e['exam']['reference']] if isinstance(e.get('exam', {}).get('reference'), dict) else []),
                      ('exam.lignes', lambda e: e.get('exam', {}).get('lignes') or []),
                      ('pec.moyens_specifiques', lambda e: e.get('pec', {}).get('moyens_specifiques', []))],
              'nc': [('lesions', lambda e: e.get('lesions', []))]}
    for n in ('glo', 'syn', 'hyp', 'nc'):
        for e in data[n]:
            m = _src_ok(e, auj)
            if m and n in ('glo', 'syn', 'hyp'):
                flag(F, 'G2', _elem(n, e), m, *_where(root, n, e))
            for champ, get in nested.get(n, []):
                for i, x in enumerate(get(e)):
                    mx = _src_ok(x, auj)
                    if mx:
                        flag(F, 'G2', _elem(n, e), f'{champ}[{i}] : {mx}', *_where(root, n, e))
            if e.get('statut') == 'sourcé' and not e.get('src'):
                flag(F, 'G2', _elem(n, e), 'statut « sourcé » sans src', *_where(root, n, e))
    for d in data['doses_ch']:
        if d.get('lu_le', '9') > auj:
            flag(F, 'G2', _elem('doses_ch', d), f'lu le {d.get("lu_le")}, date future', *_where(root, 'doses_ch', d))


# ---------------------------------------------------------------- G3
def domaines(root):
    import yaml
    return yaml.safe_load(open(os.path.join(root, 'qa', 'domaines.yml'), encoding='utf-8'))


def _match(url, liste):
    u = urlparse(url)
    host = (u.hostname or '').lower()
    host = host[4:] if host.startswith('www.') else host
    for d in liste:
        dh, _, dp = d.partition('/')
        if host == dh or host.endswith('.' + dh):
            if not dp or u.path.lstrip('/').startswith(dp):
                return d
    return None


def g3(root, data, F):
    D = domaines(root)
    clin = D['suisse'] + D['europe']
    pays = set(D['pays_admis'])
    for s in data['src']:
        anat = s.get('type') == 'anatomie'
        d = _match(s.get('url', ''), clin + (D['anatomie'] if anat else []))
        if not d:
            flag(F, 'G3', _elem('src', s), f'domaine hors liste blanche : {s.get("url")}', *_where(root, 'src', s))
        if not anat and s.get('pays') not in pays:
            flag(F, 'G3', _elem('src', s), f'éditeur hors Suisse et Europe (pays {s.get("pays")}, {s.get("org")})', *_where(root, 'src', s))
    for n in ('glo', 'syn', 'hyp', 'nc', 'loc'):
        for e in data[n]:
            for _, _, t in strings(e):
                for u in re.findall(r'https?://[^\s"<>)]+', t):
                    if not _match(u, clin + D['anatomie']):
                        flag(F, 'G3', _elem(n, e), f'URL hors liste blanche dans le texte : {u}', *_where(root, n, e))


# ---------------------------------------------------------------- G4, G5
def g4(root, data, F, diff=None):
    args = [sys.executable, os.path.join(os.path.dirname(HERE), 'lyncee.py'), '--racine', root]
    if diff:
        args += ['--diff', diff]
    p = subprocess.run(args, capture_output=True, text=True)
    for l in p.stdout.splitlines():
        if l.startswith('ÉCHEC'):
            flag(F, 'G4', 'lyncée', l[6:].strip())
    if p.returncode and not any(f['controle'] == 'G4' for f in F):
        flag(F, 'G4', 'lyncée', (p.stdout + p.stderr).strip()[-300:])


def g5(root, data, F):
    sys.path.insert(0, os.path.dirname(HERE))
    from ck_build import validate
    errs, _ = validate(root)
    for n, i, m in errs:
        e = {'id': i} if n != 'loc' else {'module': i}
        flag(F, 'G5', f'{n}|{i}', m, *_where(root, n, e))


# ---------------------------------------------------------------- G6
_VERBES = None


def verbes():
    global _VERBES
    if _VERBES is None:
        with gzip.open(os.path.join(HERE, 'verbes_conjugues.txt.gz'), 'rt', encoding='utf-8') as f:
            _VERBES = {l.strip() for l in f if l.strip() and not l.startswith('#')}
    return _VERBES


def phrases(t):
    t = re.sub(r'\([^()]*\)', ' ', strip_tags(t))  # une parenthèse ne compte pas comme phrase
    for p in re.split(r'(?<=[.!?;])\s+', t):
        mots = re.findall(r"[A-Za-zÀ-ÖØ-öø-ÿœŒ]+", p)
        if len(mots) >= 3:
            yield p.strip(), mots


def g6(root, data, F):
    V = verbes()
    for n in ('glo', 'syn', 'hyp', 'nc'):
        for e in data[n]:
            for path, champ, t in strings(e):
                if champ not in CHAMPS_PROSE:
                    continue
                for p, mots in phrases(t):
                    if not any(m.lower() in V for m in mots) and not _elision_verbe(p, V):
                        flag(F, 'G6', _elem(n, e), f'{path} : phrase sans verbe conjugué : « {p[:90]} »', *_where(root, n, e))


def _elision_verbe(p, V):
    """« s'observe », « n'est », « l'atteinte » : la forme après l'apostrophe compte si c'est un verbe."""
    return any(w.lower() in V for g in re.findall(r"\b(?:[nmlstcj]|qu)['’]([a-zà-ÿœ]+)", p, re.I) for w in [g])


# ---------------------------------------------------------------- G7
def _rouge(val):
    v = val.strip().lower()
    if any(w in v for w in VARS_ROUGES) or any(re.search(r'\b' + w + r'\b', v) for w in ROUGES):
        return True
    for h in re.findall(r'#([0-9a-f]{6}|[0-9a-f]{3})\b', v):
        h = ''.join(c * 2 for c in h) if len(h) == 3 else h
        r, g, b = (int(h[i:i + 2], 16) / 255 for i in (0, 2, 4))
        hh, l, s = colorsys.rgb_to_hls(r, g, b)
        if (hh * 360 <= 15 or hh * 360 >= 345) and s >= .45 and .2 <= l <= .75:
            return True
    for r, g, b in re.findall(r'rgba?\(\s*(\d+)[ ,]+(\d+)[ ,]+(\d+)', v):
        hh, l, s = colorsys.rgb_to_hls(int(r) / 255, int(g) / 255, int(b) / 255)
        if (hh * 360 <= 15 or hh * 360 >= 345) and s >= .45 and .2 <= l <= .75:
            return True
    return False


def g7(root, data, F):
    for n in ('glo', 'syn', 'hyp', 'nc', 'loc'):
        for e in data[n]:
            for path, _, t in strings(e):
                for st in re.findall(r'style\s*=\s*["\']([^"\']*)', t):
                    if re.search(r'color\s*:', st) and _rouge(st):
                        flag(F, 'G7', _elem(n, e), f'{path} : style rouge en ligne interdit (utilisez bloquant: true)', *_where(root, n, e))
                if 'class="urg"' in t and not e.get('bloquant'):
                    flag(F, 'G7', _elem(n, e), f'{path} : classe urg sur un élément non bloquant', *_where(root, n, e))
    # Feuilles de style de l'application : une règle .ck-… en rouge doit viser .urg ou [data-bloquant].
    app = os.path.join(root, 'app_v2.html')
    if os.path.exists(app):
        s = open(app, encoding='utf-8').read()
        for css in re.findall(r'<style[^>]*>(.*?)</style>', s, re.S):
            for sel, body in re.findall(r'([^{}]+)\{([^{}]*)\}', css):
                if '.ck-' not in sel:
                    continue
                for decl in body.split(';'):
                    k, _, v = decl.partition(':')
                    if k.strip() in ('color', 'background', 'background-color', 'border-color', 'border-left-color', 'border') and _rouge(v):
                        if not all(('.urg' in x or '[data-bloquant' in x) for x in sel.split(',') if '.ck-' in x):
                            flag(F, 'G7', 'app_v2.html', f'règle « {sel.strip()[:80]} » : rouge hors .urg ou [data-bloquant]', 'app_v2.html', 0)


# ---------------------------------------------------------------- G8
JUSTIF_EXAM = ('mecanisme', 'principe', 'pourquoi_ce_choix')
JUSTIF_MOYEN = JUSTIF_EXAM + ('limites',)
JUSTIF_MIN = 20


def _justif(item, champs, nom):
    """Rend les motifs d'échec d'un examen ou d'un moyen : champ absent, vide, trop court ou recopié."""
    if not isinstance(item, dict):
        return ['élément illisible (objet attendu)']
    motifs, vus = [], {}
    if 'pourquoi' in item:
        motifs.append('champ pourquoi : il est remplacé par pourquoi_ce_choix')
    for c in champs:
        v = item.get(c)
        if not isinstance(v, str) or not v.strip():
            motifs.append(f'{c} manquant ou vide')
            continue
        t = strip_tags(v).strip()
        if len(t) < JUSTIF_MIN or len(re.findall(r"[A-Za-zÀ-ÖØ-öø-ÿœŒ]+", t)) < 3:
            motifs.append(f'{c} trop court (au moins {JUSTIF_MIN} caractères et 3 mots) : « {t[:60]} »')
            continue
        k = norm(t)
        if k in vus:
            motifs.append(f'{c} recopie {vus[k]}')
        elif norm(strip_tags(str(item.get(nom, '')))) == k:
            motifs.append(f'{c} recopie {nom}')
        vus.setdefault(k, c)
    return motifs


def g8(root, data, F):
    for e in data['hyp']:
        ex, pec = e.get('exam') or {}, e.get('pec') or {}
        items = []
        if isinstance(ex.get('reference'), dict):
            items.append(('exam.reference', ex['reference'], JUSTIF_EXAM, 'nom'))
        for i, l in enumerate(ex.get('lignes') or []):
            items.append((f'exam.lignes[{i}]', l, JUSTIF_EXAM, 'nom'))
        for i, m in enumerate(pec.get('moyens_specifiques') or []):
            items.append((f'pec.moyens_specifiques[{i}]', m, JUSTIF_MOYEN, 'texte'))
        for path, it, champs, nom in items:
            for m in _justif(it, champs, nom):
                flag(F, 'G8', _elem('hyp', e), f'{path} : {m}', *_where(root, 'hyp', e))


GATES = {'G1': g1, 'G2': g2, 'G3': g3, 'G4': g4, 'G5': g5, 'G6': g6, 'G7': g7, 'G8': g8}


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument('--racine', default=ROOT)
    ap.add_argument('--only', default=','.join(GATES))
    ap.add_argument('--diff', default=None, help='branche de base pour G4 (la référence de Lyncée ne peut que baisser)')
    ap.add_argument('--sortie', default=None)
    ap.add_argument('--init-doses', action='store_true', help='crée qa/doses-baseline.json si elle manque')
    a = ap.parse_args(argv)
    root = a.racine
    if a.init_doses:
        p = os.path.join(root, 'qa', 'doses-baseline.json')
        if os.path.exists(p):
            print('La référence des doses existe déjà ; elle ne se régénère pas.')
            return 1
        cur = doses_heritees(root) or {}
        json.dump({'note': 'Doses du contenu hérité (TIP, NOT, GES) au 17.10.2026 ; toute dose nouvelle exige une source suisse ou « À vérifier ».',
                   'total': sum(cur.values()), 'doses': dict(sorted(cur.items()))}, open(p, 'w', encoding='utf-8'), ensure_ascii=False, indent=0)
        print(f'Référence des doses créée : {len(cur)} clés, {sum(cur.values())} mentions.')
        return 0
    data = load_all(root)
    sel = [g.strip().upper() for g in a.only.split(',') if g.strip()]
    F = []
    for g in sel:
        before = len(F)
        try:
            GATES[g](root, data, F, a.diff) if g == 'G4' else GATES[g](root, data, F)
        except Exception as ex:  # un contrôle qui plante échoue, il ne passe jamais en silence
            flag(F, g, 'outil', f'erreur interne : {type(ex).__name__}: {ex}')
        n = len(F) - before
        print(f'{g} : {"réussi" if not n else f"ÉCHEC, {n} signalement(s)"}')
    for f in F[:100]:
        loc = f' ({f["fichier"]}:{f["ligne"]})' if f['fichier'] else ''
        print(f'  ÉCHEC {f["controle"]} {f["element"]}{loc} : {f["motif"]}')
    if len(F) > 100:
        print(f'  … et {len(F) - 100} autres signalements (voir --sortie).')
    if a.sortie:
        os.makedirs(os.path.dirname(os.path.abspath(a.sortie)), exist_ok=True)
        json.dump(F, open(a.sortie, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
        print(f'Signalements écrits : {a.sortie} ({len(F)}).')
    return 1 if F else 0


if __name__ == '__main__':
    sys.exit(main())
