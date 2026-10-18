#!/usr/bin/env python3
"""Contrôle mécanique des fréquences des diagnostics différentiels (data/ck/prev.json) · Asclépios, 17.10.2026.

  python3 tools/audit/prevalence.py            # contrôle seul (étape de CI « prévalence »)
  python3 tools/prev_build.py [--check]        # contrôle, puis écrit (ou vérifie) PRV dans app_v2.html et assets/ck/prev.js

Format : { "<SSP>": { "cadre": texte, "items": [ { "i", "nom", "prev_pct", "op"?, "type"?, "cadre"?, "src"?, "loc"?,
"date_lu"?, "statut"?, "rang", "note"? } ] } }.
Règles : P1 chaque diagnostic du SSP (NOT[SSP][0]) figure une fois, avec son nom exact ; P2 un chiffre est un nombre
dans ]0 ; 100] ; P3 un chiffre exige src (présent dans data/ck/src.json), loc (tableau, page ou paragraphe) et date_lu
(ISO, au plus aujourd'hui) ; P4 sans chiffre, statut « À vérifier » ; P5 type ∈ {consultation, population} ;
P6 les chiffres sont décroissants ; les inconnues suivent leur ordre historique `rang`, mais ce rang n'est pas une
fréquence ni une classification clinique prouvée. Un classement qualitatif exige une source et un cadre complets ;
sans preuve valide, son état reste « indéterminé » ; P7 un cadre accompagne chaque chiffre.
"""
import datetime, json, os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(HERE))
from _app import ROOT, read, span  # noqa: E402

STATUT_AV = 'À vérifier'
TYPES = ('consultation', 'population')


def charger(root=ROOT):
    p = os.path.join(root, 'data', 'ck', 'prev.json')
    d = json.load(open(p, encoding='utf-8')) if os.path.exists(p) else {}
    return {k: v for k, v in d.items() if not k.startswith('_')}


def notions(root=ROOT):
    s = read(os.path.join(root, 'app_v2.html'))
    a, b = span(s, 'NOT')
    return json.loads(s[a:b])


def _source_ids(sources):
    if isinstance(sources, dict):
        return set(sources)
    return {e.get('id') for e in sources or [] if isinstance(e, dict)}


def classification_status(section, sources, today=None):
    """Valide le classement qualitatif documenté d'un SSP, sans déduire d'ordre clinique.

    Renvoie `{'etat': 'indetermine'|'valide'|'invalide', 'raisons': [...]}`.
    `sources` accepte la liste des entrées de src.json ou un dictionnaire indexé par identifiant.
    """
    c = section.get('classement')
    if c is None:
        return {'etat': 'indetermine', 'raisons': ['classement qualitatif non documenté']}
    reasons = []
    if not isinstance(c, dict):
        return {'etat': 'invalide', 'raisons': ['classement doit être un objet']}
    if c.get('type') != 'qualitatif_source':
        reasons.append('type de classement doit être qualitatif_source')
    if c.get('src') not in _source_ids(sources):
        reasons.append(f"source {c.get('src')!r} absente de data/ck/src.json")
    d = c.get('date_lu') or ''
    try:
        parsed = datetime.date.fromisoformat(d)
        today_date = datetime.date.fromisoformat(today) if isinstance(today, str) else (today or datetime.date.today())
        if parsed.isoformat() != d or parsed > today_date:
            reasons.append(f'date de lecture {d!r} invalide ou future')
    except (TypeError, ValueError):
        reasons.append(f'date de lecture {d!r} invalide ou future')
    if not isinstance(c.get('loc'), str) or not c.get('loc', '').strip():
        reasons.append('emplacement (tableau, page, paragraphe) manquant')
    if not isinstance(c.get('cadre'), str) or not c.get('cadre', '').strip():
        reasons.append('cadre du classement manquant')
    items = section.get('items', [])
    expected = [e.get('i') for e in items]
    order = c.get('ordre')
    if (not isinstance(order, list) or any(not isinstance(i, int) or isinstance(i, bool) for i in order)
            or len(order) != len(expected) or len(set(order)) != len(order) or set(order) != set(expected)):
        reasons.append('ordre doit être une permutation complète et univoque des indices DD')
    if reasons:
        return {'etat': 'invalide', 'raisons': reasons}

    # Les fréquences ne peuvent être contredites que lorsqu'elles décrivent le même type et le même cadre.
    by_i = {e['i']: e for e in items}
    positions = {i: pos for pos, i in enumerate(order)}
    for a in items:
        x = a.get('prev_pct')
        if isinstance(x, bool) or not isinstance(x, (int, float)):
            continue
        frame_a = a.get('cadre') or section.get('cadre')
        for b in items:
            y = b.get('prev_pct')
            if isinstance(y, bool) or not isinstance(y, (int, float)) or a['i'] == b['i']:
                continue
            frame_b = b.get('cadre') or section.get('cadre')
            if a.get('type', 'consultation') != b.get('type', 'consultation') or frame_a != frame_b:
                continue
            if x > y and positions[a['i']] > positions[b['i']]:
                reasons.append(f"ordre qualitatif contredit les chiffres comparables ({a['i']} avant {b['i']})")
                return {'etat': 'invalide', 'raisons': reasons}
    return {'etat': 'valide', 'raisons': []}


def ordre(items, classement=None, classification=None):
    """Ordre d'affichage ; un rang legacy ne prouve pas l'ordre clinique des inconnues."""
    if classification and classification.get('etat') == 'valide':
        by_i = {e['i']: e for e in items}
        return [by_i[i] for i in classement['ordre']]
    av = [e for e in items if e.get('prev_pct') is None]
    ch = [e for e in items if e.get('prev_pct') is not None]
    return sorted(ch, key=lambda e: (-e['prev_pct'], e.get('rang', 99))) + sorted(av, key=lambda e: e.get('rang', 99))


def _sources(root=ROOT):
    p = os.path.join(root, 'data', 'ck', 'src.json')
    return json.load(open(p, encoding='utf-8'))


def controler(root=ROOT, D=None, NOT=None):
    D = charger(root) if D is None else D
    NOT = notions(root) if NOT is None else NOT
    src_entries = _sources(root)
    src = _source_ids(src_entries)
    auj = datetime.date.today().isoformat()
    err = []
    for c, E in sorted(D.items()):
        if c not in NOT:
            err.append((c, '-', 'P1', 'SSP inconnu')); continue
        noms = NOT[c][0]
        items = E.get('items', [])
        cl = classification_status(E, src_entries)
        if cl['etat'] == 'invalide':
            err.extend((c, '-', 'P6', f"classement qualitatif invalide : {r}") for r in cl['raisons'])
        vus = [e.get('i') for e in items]
        if sorted(vus) != list(range(len(noms))):
            err.append((c, '-', 'P1', f'index {sorted(vus)} ≠ 0…{len(noms) - 1}'))
        for e in items:
            i, x = e.get('i'), e.get('prev_pct')
            if isinstance(i, int) and 0 <= i < len(noms) and e.get('nom') != noms[i]:
                err.append((c, i, 'P1', f'nom « {e.get("nom")} » ≠ « {noms[i]} »'))
            if not isinstance(e.get('rang'), int):
                err.append((c, i, 'P6', 'rang clinique entier manquant'))
            if e.get('type', 'consultation') not in TYPES:
                err.append((c, i, 'P5', f'type {e.get("type")}'))
            if x is None:
                if e.get('statut') != STATUT_AV:
                    err.append((c, i, 'P4', 'sans chiffre : statut « À vérifier » requis'))
                continue
            if isinstance(x, bool) or not isinstance(x, (int, float)) or not 0 < x <= 100:
                err.append((c, i, 'P2', f'chiffre {x!r} hors de ]0 ; 100]'))
            if e.get('src') not in src:
                err.append((c, i, 'P3', f'source {e.get("src")!r} absente de data/ck/src.json'))
            if not (e.get('loc') or '').strip():
                err.append((c, i, 'P3', 'emplacement (tableau, page) manquant'))
            d = e.get('date_lu') or ''
            if not re.fullmatch(r'\d{4}-\d\d-\d\d', d) or d > auj:
                err.append((c, i, 'P3', f'date de lecture {d!r} invalide'))
            if not (e.get('cadre') or E.get('cadre')):
                err.append((c, i, 'P7', 'cadre manquant'))
            if e.get('op') not in (None, '<', '≤', '≈'):
                err.append((c, i, 'P2', f'opérateur {e.get("op")!r}'))
        if E.get('items') and sum(e['prev_pct'] for e in items if isinstance(e.get('prev_pct'), (int, float))
                                  and e.get('type', 'consultation') == 'consultation') > 100.5:
            err.append((c, '-', 'P2', 'la somme des fréquences par consultation dépasse 100 %'))
    return err


def prv(D, sources=None, today=None):
    """Constante PRV : {SSP: [[i, %, op, population]]} dans l'ordre d'affichage (champs vides retirés)."""
    out = {}
    for c, E in sorted(D.items()):
        L = []
        sources = _sources() if sources is None else sources
        cl = classification_status(E, sources, today=today)
        for e in ordre(E['items'], E.get('classement'), cl):
            r = [e['i'], e.get('prev_pct')]
            pop = e.get('type') == 'population'
            if e.get('op') or pop:
                r.append(e.get('op') or '')
            if pop:
                r.append(1)
            L.append(r)
        out[c] = L
    return out


def detail(D, sources=None, today=None):
    """assets/ck/prev.js : métadonnées par DD, avec `classement` au niveau SSP.

    Le statut `indetermine` interdit d'interpréter les rangs legacy comme preuve clinique.
    """
    sources = _sources() if sources is None else sources
    out = {}
    for c, E in sorted(D.items()):
        out[c] = {}
        cl = classification_status(E, sources, today=today)
        out[c]['classement'] = dict(E.get('classement') or {}, etat=cl['etat'], raisons=cl['raisons'])
        for e in E['items']:
            x = {k: e[k] for k in ('type', 'src', 'loc', 'date_lu', 'statut', 'note') if e.get(k)}
            x['cadre'] = e.get('cadre') or E.get('cadre', '')
            out[c][str(e['i'])] = x
    return out


def main():
    err = controler()
    for c, i, r, m in err:
        print(f'ÉCHEC {r} {c}|{i} : {m}')
    D = charger()
    n = sum(len(E['items']) for E in D.values())
    k = sum(1 for E in D.values() for e in E['items'] if e.get('prev_pct') is not None)
    print(f'prévalence : {len(D)} SSP, {n} diagnostics, {k} chiffres sourcés, {n - k} « à vérifier », {len(err)} erreur(s).')
    return 1 if err else 0


if __name__ == '__main__':
    sys.exit(main())
