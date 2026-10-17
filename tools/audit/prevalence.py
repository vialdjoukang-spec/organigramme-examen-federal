#!/usr/bin/env python3
"""Contrôle mécanique des fréquences des diagnostics différentiels (data/ck/prev.json) · Asclépios, 17.10.2026.

  python3 tools/audit/prevalence.py            # contrôle seul (étape de CI « prévalence »)
  python3 tools/prev_build.py [--check]        # contrôle, puis écrit (ou vérifie) PRV dans app_v2.html et assets/ck/prev.js

Format : { "<SSP>": { "cadre": texte, "items": [ { "i", "nom", "prev_pct", "op"?, "type"?, "cadre"?, "src"?, "loc"?,
"date_lu"?, "statut"?, "rang", "note"? } ] } }.
Règles : P1 chaque diagnostic du SSP (NOT[SSP][0]) figure une fois, avec son nom exact ; P2 un chiffre est un nombre
dans ]0 ; 100] ; P3 un chiffre exige src (présent dans data/ck/src.json), loc (tableau, page ou paragraphe) et date_lu
(ISO, au plus aujourd'hui) ; P4 sans chiffre, statut « À vérifier » ; P5 type ∈ {consultation, population} ;
P6 l'ordre d'affichage est décroissant pour les chiffres, puis « à vérifier » par rang clinique (calculé, jamais saisi) ;
P7 un cadre (celui du SSP ou celui de l'élément) accompagne chaque chiffre.
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


def ordre(items):
    """Chiffres en ordre décroissant (égalité : rang), puis « à vérifier » par rang clinique."""
    av = [e for e in items if e.get('prev_pct') is None]
    ch = [e for e in items if e.get('prev_pct') is not None]
    return sorted(ch, key=lambda e: (-e['prev_pct'], e.get('rang', 99))) + sorted(av, key=lambda e: e.get('rang', 99))


def controler(root=ROOT, D=None, NOT=None):
    D = charger(root) if D is None else D
    NOT = notions(root) if NOT is None else NOT
    src = {e['id'] for e in json.load(open(os.path.join(root, 'data', 'ck', 'src.json'), encoding='utf-8'))}
    auj = datetime.date.today().isoformat()
    err = []
    for c, E in sorted(D.items()):
        if c not in NOT:
            err.append((c, '-', 'P1', 'SSP inconnu')); continue
        noms = NOT[c][0]
        items = E.get('items', [])
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


def prv(D):
    """Constante PRV : {SSP: [[i, %, op, population]]} dans l'ordre d'affichage (champs vides retirés)."""
    out = {}
    for c, E in sorted(D.items()):
        L = []
        for e in ordre(E['items']):
            r = [e['i'], e.get('prev_pct')]
            pop = e.get('type') == 'population'
            if e.get('op') or pop:
                r.append(e.get('op') or '')
            if pop:
                r.append(1)
            L.append(r)
        out[c] = L
    return out


def detail(D):
    """assets/ck/prev.js : {SSP: {i: {cadre, type, src, loc, date_lu, statut, note}}}."""
    out = {}
    for c, E in sorted(D.items()):
        out[c] = {}
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
