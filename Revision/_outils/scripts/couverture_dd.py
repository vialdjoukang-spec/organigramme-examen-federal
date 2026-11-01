#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""couverture_dd.py — Vérifie que CHAQUE DX de LISTE_DX_CANONIQUE est maîtrisé dans la banque d'un SSP.

Règle (CHARTE_REDACTION.md §3) : un DX est « couvert » s'il est DX CIBLE (1er DX.n du champ dx) d'au moins N questions EX
(défaut N = 2). AP / SPE / mentions croisées sont comptées à part (bonus, ne remplacent pas les EX).

Usage : python3 couverture_dd.py <dossier_SSP | G2> [--min 2] [--quiet]
Écrit COUVERTURE_DD.md dans le dossier SSP ; code retour 1 s'il reste des gaps.
"""
import sys, os, collections, datetime
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _commun import *

def analyse(s, nmin=2):
    J = ssp_json(s); dx = liste_dx(s)
    rows = {k: collections.Counter() for k, _ in dx}
    trans = 0
    if J:
        for b in J['questions']:
            ids = b.get('dx_cibles') or dx_ids(b['dx'])
            if not ids: trans += 1; continue
            niv = {'examen': 'ex', 'approfondissement': 'ap', 'specialiste': 'spe'}[b['niveau']]
            if ids[0] in rows: rows[ids[0]][niv] += 1
            for k in ids[1:]:
                if k in rows: rows[k]['croise'] += 1
    gaps = [k for k, _ in dx if rows[k]['ex'] < nmin]
    return J, dx, rows, gaps, trans

def main():
    a = sys.argv[1:]
    if not a: sys.exit(__doc__)
    nmin = int(a[a.index('--min') + 1]) if '--min' in a else 2
    tgt = a[0]
    s = entry_for_dir(tgt) if os.path.isdir(tgt) else ssp_entry(tgt)
    J, dx, rows, gaps, trans = analyse(s, nmin)
    n = J['n'] if J else 0
    cov = (len(dx) - len(gaps)) / len(dx) if dx else 0
    L = [f"# COUVERTURE_DD — {s['code']} {s['titre_fr']} ({s['lot']})", "",
         f"_Généré par `couverture_dd.py` le {datetime.datetime.now():%Y-%m-%d %H:%M} (Europe/Zurich) · seuil : ≥ {nmin} EX par DX cible_", "",
         f"**{n} questions** · DX couverts **{len(dx)-len(gaps)}/{len(dx)} ({cov:.0%})** · questions transversales (sans DX.n) : {trans}", "",
         "| DX | Diagnostic | EX cible | AP | SPE | croisé | État |", "|---|---|---:|---:|---:|---:|---|"]
    for k, nom in dx:
        r = rows[k]; ok = r['ex'] >= nmin
        L.append(f"| {k} | {nom} | {r['ex']} | {r['ap']} | {r['spe']} | {r['croise']} | {'✅' if ok else '❌ GAP'} |")
    L += ["", "## Gaps à combler", ""]
    L += [f"- {k} : {rows[k]['ex']} EX (manque {nmin-rows[k]['ex']})" for k in gaps] or ["- Aucun : tous les DX ont ≥ %d EX cibles." % nmin]
    sans_ap = [k for k, _ in dx if rows[k]['ap'] + rows[k]['spe'] == 0]
    L += ["", "## Pistes d'enrichissement (non bloquant)", "", f"- DX sans AP ni SPE : {', '.join(sans_ap) if sans_ap else 'aucun'}"]
    out = os.path.join(ssp_dir(s), 'COUVERTURE_DD.md')
    if os.path.isdir(ssp_dir(s)): open(out, 'w', encoding='utf-8').write('\n'.join(L) + '\n')
    if '--quiet' not in a: print('\n'.join(L))
    sys.exit(1 if gaps else 0)

if __name__ == '__main__':
    main()
