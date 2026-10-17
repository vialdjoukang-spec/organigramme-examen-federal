#!/usr/bin/env python3
"""Galien · audit G1 prévalence (S2.4, S2.5), 17.10.2026. Rejouable : extract NOT/TIP, ce script, inject NOT/TIP, prev_build.
1. Majeure : l'angor stable (syndrome coronarien chronique), 2e cause de douleur thoracique en médecine de famille
   romande (Verdon 2008, tableau 1 : 75/672 = 11,2 %), manquait aux différentiels de S2.4 et S2.5 ; il est ajouté en fin
   de liste (index 10 : la progression enregistrée 'd0'…'d9' ne bouge pas).
2. Mineure : la note « Douleur pariétale » (S2.4) taisait que le groupe musculo-squelettique compte 26 traumatismes et
   7 métastases costales.
3. Mineure : le cadre de S2.4 affirmait que la gêne thoracique était comprise dans l'étude ; la source dit seulement que
   la douleur thoracique, symptôme principal ou accessoire, était appréciée selon la pratique de chaque médecin.
"""
import json
NOM = 'Angor stable (syndrome coronarien chronique)'
D24 = ("• <b>Ce que c'est</b> : ischémie myocardique d'effort sur coronaropathie chronique (syndrome coronarien chronique)\n"
       "• <b>Distinction</b> : gêne rétrosternale déclenchée par l'effort ou l'émotion, qui cède en quelques minutes au repos ou sous trinitrine\n"
       "• <b>Délai</b> : bilan programmé, sauf si l'angor apparaît au repos, est récent ou s'aggrave\n"
       "• <b>Conduite</b> : ECG de repos et échocardiographie, puis estimation de la vraisemblance clinique ; coroscanner si elle est faible ou modérée (> 5 à 50 %), imagerie de stress si elle est modérée ou élevée (> 15 à 85 %)\n"
       "• <b>Piège</b> : traiter comme stable un angor de repos, de novo ou crescendo, qui est un syndrome coronarien aigu")
D25 = ("• <b>Terrain et contexte</b> : Âge, tabac, diabète, hypertension, dyslipidémie, hérédité coronarienne<br>"
       "• <b>Caractères de la douleur</b> : Gêne rétrosternale que l'effort ou l'émotion déclenche, et qui cède en quelques minutes au repos ou sous trinitrine<br>"
       "• <b>Signes associés</b> : Dyspnée d'effort ; l'examen est souvent normal, et un souffle d'éjection fait rechercher une sténose aortique<br>"
       "• <b>Examen décisif</b> : ECG de repos et échocardiographie, puis vraisemblance clinique ; coroscanner si elle est faible ou modérée (> 5 à 50 %), imagerie de stress si elle est modérée ou élevée (> 15 à 85 %)<br>"
       "• <b>Piège à éviter</b> : Traiter comme stable un angor de repos, de novo ou crescendo : c'est un syndrome coronarien aigu<br>")
NOTE = ("L'angor (« acute angina » du tableau 1) compte 75 patients sur 672 ; le texte de l'article les désigne comme "
        "coronaropathies stables, distinctes des 10 syndromes coronariens aigus.")
N = json.load(open('data/NOT.json')); T = json.load(open('data/TIP.json')); P = json.load(open('data/ck/prev.json'))
for c, d in (('S2.4', D24), ('S2.5', D25)):
    if NOM not in N[c][0]:
        N[c][0].append(NOM); T[c]['d'].append(d)
        if 'v' in T[c]: T[c]['v']['d'].append(['complété', [8, 3]])
    i = N[c][0].index(NOM); assert len(T[c]['d']) == len(N[c][0])
    it = P[c]['items']
    if not any(e['i'] == i for e in it):
        it.append({'i': i, 'nom': NOM, 'prev_pct': 11.2, 'type': 'consultation', 'src': 'R-VERDON-SMW-2008',
                   'loc': 'Tableau 1 (Ischaemic Heart Disease, Acute angina 75/672) et Résultats', 'date_lu': '2026-10-17',
                   'rang': max(e['rang'] for e in it) + 1, 'note': NOTE})  # chiffré : le rang ne sert qu'aux « à vérifier »
for e in P['S2.4']['items']:
    if e['nom'] == 'Douleur pariétale':
        e['note'] = ("Les causes musculo-squelettiques comptent 327 patients sur 672 : 287 syndromes de la paroi thoracique (42,7 %), "
                     "26 traumatismes (3,9 %, dont 7 fractures de côte), 7 douleurs projetées d'origine rachidienne et 7 métastases costales (1,0 %).")
P['S2.4']['cadre'] = ("Médecine de famille en Suisse romande : 672 patients de plus de 16 ans venus avec une douleur thoracique, symptôme "
                      "principal ou accessoire, chez 59 médecins de famille, diagnostic retenu après 12 mois de suivi ; l'étude ne distingue "
                      "pas la gêne de la douleur thoracique")
S25 = ' · ESC 2024 — Guidelines for the management of chronic coronary syndromes'
if 'chronic coronary' not in T['S2.5']['s']: T['S2.5']['s'] += S25
json.dump(N, open('data/NOT.json', 'w'), ensure_ascii=False, separators=(',', ':'))
json.dump(T, open('data/TIP.json', 'w'), ensure_ascii=False, separators=(',', ':'))
json.dump(P, open('data/ck/prev.json', 'w'), ensure_ascii=False, indent=1)
print('G1 corrigé')
