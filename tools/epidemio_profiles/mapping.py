#!/usr/bin/env python3
"""Rattache chaque valeur du référentiel au LOT (code SSP) puis au DX (numéro + contrôle du nom).
Entrées : out/referentiel.json, Brief/scripts/ssp_dx.json, Brief/scripts/carte_lots.json, dépôt git (origin/main).
Sorties : out/mapping.json, out/NON_RATTACHEES.md"""
import json, re, subprocess, unicodedata, difflib, sys, os
from collections import defaultdict
ICI = os.path.dirname(os.path.abspath(__file__)); OUT = os.path.join(os.path.dirname(ICI), 'out')
BRIEF = '/workspace/Leona__Brief_Redaction_LOTs_20261115/scripts'
REPO = '/workspace/grok/etude/repo'
STOP = set("de du des la le les l d et a au aux en par sur avec sans ou un une chez pour non y compris type autre autres toutes tous causes cause".split())

def toks(s):
    s = unicodedata.normalize('NFD', s.lower()); s = ''.join(c for c in s if unicodedata.category(c) != 'Mn')
    return {w[:6] for w in re.findall(r'[a-z0-9]+', s) if w not in STOP and len(w) > 2}

def sim(a, b):
    ta, tb = toks(a), toks(b)
    if not ta or not tb: return 0.0
    j = len(ta & tb) / min(len(ta), len(tb))
    return max(j, difflib.SequenceMatcher(None, ' '.join(sorted(ta)), ' '.join(sorted(tb))).ratio() * 0.8)

def git(*a):
    return subprocess.run(['git', '-C', REPO, *a], capture_output=True).stdout

def titre_dx(blob, n):
    """Nom du DX n lu dans un titre h1–h4/title « DX.n — Nom » (gère les fichiers multi-DX)."""
    h = git('cat-file', 'blob', blob).decode('utf-8', 'ignore')
    for tag, b in re.findall(r'<(h[1-4]|title)\b[^>]*>(.*?)</\1>', h, re.S | re.I):
        t = re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', ' ', b)).strip()
        m = re.search(rf'DX\.?\s*0?{n}\b\s*[—–:-]?\s*(.{{3,140}})', t)
        if m and not re.match(r'\s*(à|et)\s+DX', m.group(1)):
            return re.split(r'\s+[—|]\s+', m.group(1))[0].strip()
    return ''

def main():
    rows = json.load(open(f'{OUT}/referentiel.json'))
    ssp = {x['code']: x for x in json.load(open(f'{BRIEF}/ssp_dx.json'))}
    carte = json.load(open(f'{BRIEF}/carte_lots.json'))['lecons']
    main_paths = set(git('ls-tree', '-r', '--name-only', 'origin/main').decode().split('\n'))
    cache = {}
    def nom_dx(lot, n):
        """Nom du DX : titre du cours de référence, sinon ssp_dx.json."""
        k = f'{lot:03d}:DX{n}'
        if k in cache: return cache[k]
        v = carte.get(k); t = ''
        if v and v['ref'] == 'origin/main': t = titre_dx(v['blob'], n)
        if not t:
            d = ssp_lot[lot]['dx'][n - 1] if lot in ssp_lot and n <= len(ssp_lot[lot]['dx']) else ''
            t = '' if 'nom à venir' in d else d
        cache[k] = t; return t
    ssp_lot = {x['lot']: x for x in ssp.values()}
    res, non = [], []
    for r in rows:
        code = r['code_ssp'].lstrip('↳ ').strip()
        r['code_ssp'] = code
        cibles = []
        for c in [x.strip() for x in code.split('/')]:
            parts = c.split('.')
            # G : G<n>.<dx> ; S/F/O : X<n>.<m>.<dx> ; code SSP seul => Phase A
            if c.startswith('G'):
                base, dx = (parts[0], parts[1]) if len(parts) == 2 else (c, None)
            else:
                base, dx = ('.'.join(parts[:2]), parts[2]) if len(parts) == 3 else ('.'.join(parts[:2]), None)
            if base not in ssp:
                cibles.append({'code': c, 'statut': 'code_SSP_inconnu'}); continue
            lot = ssp[base]['lot']
            if dx is None:
                cibles.append({'code': c, 'lot': lot, 'lecon': 'A', 'statut': 'phase_A'}); continue
            n = int(dx)
            nom = nom_dx(lot, n); s = sim(r['entite'], nom) if nom else None
            best = (n, s, nom)
            # Le code fait foi ; on ne renumérote que si le nom du DX codé diverge nettement
            # et qu'un autre DX du même LOT porte clairement le même nom.
            if s is not None and s < 0.3:
                for k in range(1, 11):
                    nk = nom_dx(lot, k); sk = sim(r['entite'], nk) if nk else 0
                    if k != n and sk >= 0.67 and sk > (best[1] or 0): best = (k, sk, nk)
            n2, s2, nom2 = best
            statut = ('dx_verifie' if s2 is not None and s2 >= 0.5 else
                      'dx_par_code_nom_inconnu' if s2 is None else 'dx_par_code_nom_a_verifier')
            if n2 != n: statut = 'dx_renumerote'
            cibles.append({'code': c, 'lot': lot, 'ssp': ssp[base]['nom'], 'lecon': f'DX{n2}', 'dx_code': n,
                           'nom_cours': nom2, 'sim': round(s2, 2) if s2 is not None else None, 'statut': statut})
        r['cibles'] = cibles
        res.append(r)
        if any(c['statut'] in ('code_SSP_inconnu', 'dx_par_code_nom_a_verifier', 'dx_renumerote') for c in cibles):
            non.append(r)
    json.dump(res, open(f'{OUT}/mapping.json', 'w'), ensure_ascii=False, indent=1)
    from collections import Counter
    cnt = Counter(c['statut'] for r in res for c in r['cibles'])
    L = ['# Valeurs non rattachées ou douteuses', '',
         f'Statuts des cibles : {dict(cnt)}.', '',
         '| # | Code | Entité | LOT | DX code → cours | Nom du cours | Statut |', '|---|---|---|---|---|---|---|']
    for r in non:
        for c in r['cibles']:
            if c['statut'] in ('code_SSP_inconnu', 'dx_par_code_nom_a_verifier', 'dx_renumerote'):
                L.append(f"| {r['n']} | {c['code']} | {r['entite']} | {c.get('lot','')} | {c.get('dx_code','')} → {c.get('lecon','')} | {c.get('nom_cours','')} | {c['statut']} |")
    open(f'{OUT}/NON_RATTACHEES.md', 'w').write('\n'.join(L) + '\n')
    print(dict(cnt), 'lignes avec cible douteuse :', len(non))

if __name__ == '__main__':
    main()
