#!/usr/bin/env python3
"""Galien · audit G2 prévalence (S2.7 dyspnée), 17.10.2026. Rejouable : extract NOT/TIP, ce script, inject NOT/TIP, prev_build.
Les 4 chiffres EURODEM (tableau 1, colonne EURODEM, n = 2525) sont exacts. Faute majeure : le syndrome coronarien aigu,
dont la dyspnée peut être le seul symptôme (équivalent angineux), manquait aux différentiels ; il est ajouté (index 10,
« % à vérifier » : EURODEM le range dans « autres », 33,7 %), au rang clinique 2 des diagnostics non chiffrés, après l'embolie.
"""
import json
C, NOM = 'S2.7', 'Syndrome coronarien aigu (dyspnée comme équivalent angineux)'
D = ('<b style="color:var(--bad)">À ne pas manquer.</b><br>'
     "• <b>Terrain et contexte</b> : Âge, diabète, femme, insuffisance rénale, antécédent coronarien, facteurs de risque cardiovasculaire<br>"
     "• <b>Chronologie et sémiologie</b> : Dyspnée d'apparition récente, au repos ou à l'effort minime, parfois sans aucune douleur thoracique<br>"
     "• <b>Signes associés</b> : Sueurs, nausées, fatigue intense, palpitations ou syncope ; parfois râles crépitants d'une insuffisance ventriculaire gauche<br>"
     "• <b>Examen décisif</b> : ECG dans les 10 minutes, puis troponine hypersensible selon l'algorithme 0/1 h<br>"
     "• <b>Piège à éviter</b> : Attribuer une dyspnée isolée du sujet âgé ou diabétique à une cause pulmonaire sans avoir fait l'ECG<br>")
N = json.load(open('data/NOT.json')); T = json.load(open('data/TIP.json')); P = json.load(open('data/ck/prev.json'))
if NOM not in N[C][0]:
    N[C][0].append(NOM); T[C]['d'].append(D)
i = N[C][0].index(NOM); assert len(T[C]['d']) == len(N[C][0])
if 'ESC 2023 — Guidelines for the management of acute coronary' not in T[C]['s']:
    T[C]['s'] += ' · ESC 2023 — Guidelines for the management of acute coronary syndromes'
it = P[C]['items']
if not any(e['i'] == i for e in it):
    for e in it:
        if e['rang'] >= 6: e['rang'] += 1          # EP garde le rang 5 ; le SCA prend le 6
    it.append({'i': i, 'nom': NOM, 'prev_pct': None, 'type': 'consultation', 'rang': 6, 'statut': 'À vérifier',
               'note': "EURODEM range ce diagnostic dans le groupe « autres » (33,7 %) sans le chiffrer ; aucune fréquence n'est "
                       "encore sourcée. La ligne directrice ESC 2023 compte la dyspnée parmi les symptômes de présentation du syndrome coronarien aigu."})
json.dump(N, open('data/NOT.json', 'w'), ensure_ascii=False, separators=(',', ':'))
json.dump(T, open('data/TIP.json', 'w'), ensure_ascii=False, separators=(',', ':'))
json.dump(P, open('data/ck/prev.json', 'w'), ensure_ascii=False, indent=1)
print('G2 corrigé')
