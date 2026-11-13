#!/usr/bin/env python3
"""CONTRÔLE — partie 8 du cahier d'architecture v2, zéro modèle. Code 1 en cas d'échec ; sortie ≤ 20 lignes.

Vérifie sur Claude/_progression/donnees/ :
 1. identifiants uniques, conformes à la nomenclature, égaux au nom du fichier ;
 2. chaque champ du gabarit présent (structure de la fiche ⊇ gabarit) ;
 3. aucune case vide sans « — » (chaîne vide, null, liste ou objet vides) ;
 4. passerelles valides : type autorisé (partie 5.2 et interfaces de la partie 2), cible existante, pas d'auto-renvoi ;
 5. aucun terme vague sans chiffre dans une posologie remplie ;
 6. systèmes S1 et S11 séparés : système de l'identifiant = système de la fiche ; une molécule commune a deux fiches distinctes.
Usage : python3 Claude/_progression/controle.py [dossier]
"""
import glob, json, os, re, sys

ICI = os.path.dirname(os.path.abspath(__file__))
DON = sys.argv[1] if len(sys.argv) > 1 else os.path.join(ICI, 'donnees')
V = '—'
SYS = r'(S1[0-2]|S[1-9]|T)'
NOMEN = {'examens': re.compile(rf'^EX-[1-9]-{SYS}-[a-z0-9]+(-[a-z0-9]+)*$'),
         'pharmaco': re.compile(rf'^PH-{SYS}-[a-z0-9]+(-[a-z0-9]+)*$'),
         'psychiatrie': re.compile(r'^PS-(F\d\d(\.\d+)?(-F\d\d)?|F51-G47|CADRE-CH)$'),
         'fondamentales': re.compile(rf'^SF-{SYS}-[a-z0-9]+(-[a-z0-9]+)*$')}
TYPES_P = {'Prélèvement', 'Test compagnon', 'Confirmation', 'In vivo ↔ in vitro', 'Sommeil', 'Suivi thérapeutique',
           'Diagnostic psychiatrique', 'Fondement', 'Interface S1 ↔ S11', 'Traitement'}
VAGUE = re.compile(r'\b(faible dose|dose (habituelle|usuelle|faible|élevée)|à adapter|adapter|selon (la )?(réponse|tolérance|clinique)|progressive(ment)?|'
                   r'quelques|usuel(le)?|variable|individuel(le)?|si besoin|à titrer)\b', re.I)

err = []


def e(m):
    err.append(m)


def vides(x, chemin):
    if x is None or (isinstance(x, str) and not x.strip()) or (isinstance(x, (list, dict)) and not x):
        e(f'case vide sans « — » : {chemin}')
    elif isinstance(x, dict):
        for k, v in x.items():
            vides(v, f'{chemin}.{k}')
    elif isinstance(x, list):
        for i, v in enumerate(x):
            vides(v, f'{chemin}[{i}]')


def couvre(g, f, chemin):
    """Tout champ du gabarit existe dans la fiche (les lignes de tableau suivent la ligne type)."""
    if isinstance(g, dict):
        if not isinstance(f, dict):
            return e(f'gabarit : {chemin} devrait être un objet')
        for k, v in g.items():
            if k not in f:
                e(f'gabarit : champ absent {chemin}.{k}')
            else:
                couvre(v, f[k], f'{chemin}.{k}')
    elif isinstance(g, list) and g and isinstance(g[0], dict):
        if not isinstance(f, list):
            return e(f'gabarit : {chemin} devrait être une liste')
        for i, ligne in enumerate(f):
            couvre(g[0], ligne, f'{chemin}[{i}]')


def posologies(x, chemin):
    if isinstance(x, dict):
        for k, v in x.items():
            posologies(v, f'{chemin}.{k}')
    elif isinstance(x, list):
        for i, v in enumerate(x):
            posologies(v, f'{chemin}[{i}]')
    elif isinstance(x, str) and x != V and VAGUE.search(x) and not re.search(r'\d', x):
        e(f'posologie vague sans chiffre : {chemin} « {x[:40]} »')


def main():
    gab = json.load(open(os.path.join(DON, 'gabarits.json'), encoding='utf-8'))
    fiches = {}
    for p in sorted(glob.glob(os.path.join(DON, '*', '*.json'))):
        mod = os.path.basename(os.path.dirname(p))
        try:
            f = json.load(open(p, encoding='utf-8'))
        except ValueError as x:
            e(f'JSON illisible : {p} ({x})'); continue
        i = f.get('id', '')
        if i in fiches:
            e(f'identifiant en double : {i}')
        fiches[i] = f
        if os.path.basename(p) != i + '.json':
            e(f'nom de fichier ≠ identifiant : {p}')
        if mod not in NOMEN or not NOMEN[mod].match(i):
            e(f'nomenclature : {i} ({mod})')
        if f.get('module') != mod:
            e(f'module : {i}')
        m = re.match(rf'^(?:EX-\d-|PH-|SF-){SYS}-', i)
        if m and m.group(1) != f.get('systeme'):
            e(f'S1/S11 : système de l\'identifiant ≠ système de la fiche : {i}')
        if i.startswith('PS-') and f.get('systeme') != 'S11':
            e(f'S1/S11 : pathologie psychiatrique hors S11 : {i}')
        if f.get('type') in gab:
            couvre(gab[f['type']], f, i)
        vides({k: v for k, v in f.items() if k not in ('passerelles', 'etiquettes')}, i)
        for k in ('posologie', 'posologie_par_age'):
            if k in f:
                posologies(f[k], f'{i}.{k}')
        for t in f.get('barre_traitement', {}).get('hors_psychiatrie', []) + [x for p_ in f.get('pathologies', []) if isinstance(p_, dict)
                                                                             for x in p_.get('traitement', {}).get('hors_systeme', [])]:
            posologies(t.get('posologie_complete', V), f'{i}.posologie_complete')
    for i, f in fiches.items():
        for p in f.get('passerelles', []):
            if p.get('type') not in TYPES_P:
                e(f'passerelle de type inconnu : {i} → {p.get("type")}')
            if p.get('cible') not in fiches:
                e(f'passerelle vers un identifiant absent : {i} → {p.get("cible")}')
            elif p['cible'] == i:
                e(f'passerelle vers soi : {i}')
            elif {f['systeme'], fiches[p['cible']]['systeme']} == {'S1', 'S11'} and p['type'] not in ('Interface S1 ↔ S11', 'Sommeil', 'Fondement'):
                e(f'S1/S11 : passerelle hors interface : {i} → {p["cible"]}')
            if not p.get('pourquoi'):
                e(f'passerelle sans « pourquoi » (« — » attendu) : {i}')
        for c in [c for b in f.get('bandes', []) for c in b.get('chefs_de_file', []) if c != V] + [c for c in f.get('pathologies', []) if isinstance(c, str) and c != V]:
            if c not in fiches:
                e(f'renvoi vers un identifiant absent : {i} → {c}')
    dci = {}
    for i, f in fiches.items():
        if f.get('type', '').startswith('molecule'):
            dci.setdefault(f['titre'], set()).add(f['systeme'])
    s = json.load(open(os.path.join(DON, 'structure.json'), encoding='utf-8'))
    for so in s['examens']:
        for sy in so['systemes']:
            for i in sy['fiches']:
                if i not in fiches:
                    e(f'structure : emplacement sans fiche : {i}')
    n_p = sum(len(f.get('passerelles', [])) for f in fiches.values())
    communes = sorted(d for d, ss in dci.items() if {'S1', 'S11'} <= ss)
    print(f'CONTRÔLE partie 8 · {len(fiches)} fiches · {n_p} passerelles · molécules S1+S11 en fiches distinctes : {", ".join(communes) or "aucune"}')
    for m in err[:18]:
        print('  ✗', m)
    if len(err) > 18:
        print(f'  … {len(err) - 18} autres échecs')
    print('VERT' if not err else f'ROUGE : {len(err)} échec(s)')
    return 1 if err else 0


if __name__ == '__main__':
    sys.exit(main())
