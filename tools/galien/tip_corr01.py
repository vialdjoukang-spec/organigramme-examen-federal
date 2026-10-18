"""Galien · corrections de niveau 2 du champ 5 de TIP (PR #33, d253d06), 17.10.2026.
Rejouable : python3 tools/json_inject.py extract TIP && python3 tools/galien/tip_corr01.py && python3 tools/json_inject.py inject TIP
Chaque correction remplace une phrase exacte ; une phrase absente fait échouer le script (pas de correction silencieuse)."""
import json, sys
LU = 'lu le 17.10.2026'
ERC_FA = {'t': 'Zideman et al. European Resuscitation Council Guidelines 2025 First Aid (obstruction des voies aériennes par un corps étranger, fig. 5), Resuscitation 2025, ' + LU,
          'o': 'European Resuscitation Council (ERC)', 'u': 'https://doi.org/10.1016/j.resuscitation.2025.110752', 'n': 'EU', 'a': '2025'}
ESC_PERI = {'t': '2025 ESC Guidelines for the management of myocarditis and pericarditis (§ 3.3.2, critères diagnostiques de la péricardite), ' + LU,
            'o': 'European Society of Cardiology (ESC)', 'u': 'https://doi.org/10.1093/eurheartj/ehaf192', 'n': 'EU', 'a': '2025'}
GLIM = {'t': 'Cederholm et al. GLIM criteria for the diagnosis of malnutrition (tableau 3, critères phénotypiques et étiologiques), Clinical Nutrition 2019 (ESPEN), ' + LU,
        'o': 'European Society for Clinical Nutrition and Metabolism (ESPEN), consensus GLIM', 'u': 'https://doi.org/10.1016/j.clnu.2018.08.002', 'n': 'EU', 'a': '2019'}
GLIM_PH = 'est un critère phénotypique de dénutrition selon GLIM, qui exige en plus un critère étiologique (apports réduits ou maladie inflammatoire)'
# (SSP, ancien texte exact, nouveau texte, source ajoutée ou None)
C = [
 ('S8.6', 'si la toux reste inefficace, penche-le en avant et donne 5 tapes dans le dos entre les omoplates, puis 5 compressions abdominales ; s’il perd connaissance, commence la réanimation (ERC 2021).',
  'si la toux devient inefficace, penche-le en avant et donne jusqu’à 5 tapes dans le dos entre les omoplates, puis jusqu’à 5 compressions abdominales, et alterne ensuite 5 tapes et 5 compressions jusqu’à la levée de l’obstruction ; ne cherche jamais le corps étranger à l’aveugle avec un doigt ; s’il perd connaissance et ne respire plus normalement, commence les compressions thoraciques (ERC 2025, premiers secours).', ERC_FA),
 ('S8.7', 'un score de Glasgow de 14 ou moins, une perte de connaissance, au moins 2 vomissements, un traitement anticoagulant ou un trouble de la coagulation, une crise post-traumatique, des signes de fracture ou un déficit focal imposent la TDM cérébrale (lignes directrices scandinaves 2013).',
  'un score de Glasgow de 14 ou moins, une perte de connaissance, au moins 2 vomissements, un traitement anticoagulant ou un trouble de la coagulation, une crise post-traumatique, des signes de fracture ou un déficit focal imposent la TDM cérébrale (lignes directrices scandinaves 2013, recommandation 1.1). Une exception existe : avec un score de 14 sans autre facteur de risque, ou de 15 avec une perte de connaissance ou au moins 2 vomissements comme seuls facteurs, un dosage de la protéine S100B fait dans les 6 heures après le choc permet de renoncer à la TDM s’il reste sous 0,10 microgramme par litre (recommandation 1.2).', None),
 ('S8.9', 'teste chaque tendon contre résistance, le fléchisseur profond par la flexion de l’articulation interphalangienne distale et le fléchisseur superficiel par celle de l’interphalangienne proximale, les autres doigts tenus en extension ;',
  'teste chaque tendon contre résistance : pour le fléchisseur profond, bloque l’interphalangienne proximale en extension et demande de fléchir la distale ; pour le fléchisseur superficiel, tiens les autres doigts en extension et demande de fléchir l’interphalangienne proximale (à vérifier : technique non détaillée par la source lue) ;', None),
 ('S8.12', 'car l’ischémie et la lésion nerveuse associée en donnent tous deux.', 'car l’ischémie et la lésion nerveuse associée en donnent toutes deux.', None),
 ('S1.1', 'fais fixer le regard vers le haut pendant une minute ; un ptosis qui s’aggrave et une brève secousse de la paupière vers le haut quand le regard revient droit devant orientent vers une myasthénie.',
  'fais fixer le regard vers le haut pendant une minute ; un ptosis qui s’aggrave oriente vers une myasthénie. Fais ensuite regarder vers le bas quelques secondes, puis droit devant : une brève secousse de la paupière vers le haut va dans le même sens. À vérifier : cette technique n’est pas citée par une source lue.', None),
 ('S2.2', 'ne corrige pas cette respiration par l’oxygène ou la sédation, car elle compense l’acidose.', 'ne freine pas cette respiration par une sédation, car elle compense l’acidose.', None),
 ('S2.5', 'des sueurs profuses, une angoisse et une position penchée en avant pour soulager la douleur orientent vers une cause thoracique grave (infarctus, péricardite).',
  'des sueurs profuses et une angoisse orientent vers une cause thoracique grave comme l’infarctus ; une douleur que le patient soulage en s’asseyant penché en avant, et qui augmente couché ou à l’inspiration, oriente vers une péricardite (ESC 2025, § 3.3.2).', ESC_PERI),
 ('F1.8', 'une perte d’au moins 5 % en 1 mois ou d’au moins 10 % en 6 mois est significative.',
  'une perte involontaire de plus de 5 % en 6 mois, ou de plus de 10 % au-delà de 6 mois, ' + GLIM_PH + '.', GLIM),
 ('F1.8', 'un indice inférieur à 18,5 kg/m² avant 70 ans, ou à 22 kg/m² après 70 ans, signe une dénutrition.',
  'un indice inférieur à 20 kg/m² avant 70 ans, ou à 22 kg/m² dès 70 ans, ' + GLIM_PH + ' (GLIM, tableau 3).', None),
 ('F2.23', 'une fonte musculaire et adipeuse signe une dénutrition.', 'une masse musculaire réduite ' + GLIM_PH + '.', GLIM),
 ('O3.3', 'un creusement bilatéral et symétrique des tempes et des épaules signe une dénutrition.', 'un creusement bilatéral et symétrique des tempes et des épaules traduit une masse musculaire réduite, qui ' + GLIM_PH + '.', GLIM),
 ('O3.1', 'une perte de 5 % en un mois ou de 10 % en six mois et une fonte temporale signent une dénutrition.', 'une perte de poids involontaire de plus de 5 % en 6 mois ou une fonte temporale sont des critères phénotypiques de dénutrition selon GLIM, qui exige en plus un critère étiologique.', GLIM),
 ('O3.4', 'un antiémétique dopaminergique un parkinsonisme', 'un antiémétique antidopaminergique (métoclopramide) un parkinsonisme', None),
 ('O4.4', 'un potassium ou un calcium isolément élevé fait suspecter un échantillon hémolysé.', 'un potassium isolément élevé fait suspecter un échantillon hémolysé.', None),
 ('O7.22', 'associé au tramadol ou à un triptan l’expose.', 'associé au tramadol ou à un triptan y expose.', None),
 ('O1.2', 'palpe l’utérus pendant 10 minutes ; moins de 3 contractions ou l’absence de relâchement entre elles sont anormales.',
  'palpe l’utérus pendant 10 minutes ; en phase active, moins de 3 contractions font suspecter une dynamique insuffisante, et plus de 5 contractions (tachysystolie) ou l’absence de relâchement entre elles menacent l’oxygénation du fœtus. À vérifier : seuils à relire dans une ligne directrice suisse ou européenne.', None),
 ('S4.3', 'sans fièvre ni douleur lombaire a une cystite simple.', 'sans fièvre ni douleur lombaire oriente vers une cystite simple.', None),
]
T = json.load(open('data/TIP.json'))
for sid, old, new, src in C:
    c = T[sid]['c']
    if old not in c[5]:
        sys.exit(f'{sid} : phrase introuvable (déjà corrigée ?) : {old[:70]}')
    c[5] = c[5].replace(old, new, 1)
    if src:
        v = T[sid].setdefault('v', {'S': [], 'c': [None] * len(c), 'd': [None] * len(T[sid].get('d', []))})
        i = next((x['id'] for x in v['S'] if x['u'] == src['u']), None)
        if i is None:
            i = max([x['id'] for x in v['S']] + [0]) + 1; v['S'].append({'id': i, **src})
        cur = v['c'][5] or ['corrigé', []]
        if i not in cur[1]: cur[1].append(i)
        v['c'][5] = cur
json.dump(T, open('data/TIP.json', 'w'), ensure_ascii=False, separators=(',', ':'))
print(f'{len(C)} corrections appliquées')
