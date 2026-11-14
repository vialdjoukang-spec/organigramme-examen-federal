# Corrections après audit : anamnèse A-TRAME, A-SPE-1a à 1g, A-MOT-1 à 25

Ces corrections répondent à AUDIT_ANAMNESE_01_25.md et datent du 14.11.2026. J'ai appliqué les 22 patchs aux 33 JSON de `anamnese/`, puis j'ai rechargé chaque fichier avec json.load. Chaque champ « lettre » commence désormais par une lettre VITE DIT CAFé, seule ou combinée (A-TRAME excepté, car sa lettre décrit la méthode).

## Patchs graves et moyens (n° 1 à 10)

| # | Fiche | Correction appliquée |
|---|---|---|
| 1 | A-SPE-1f | Le délai de la PEP VIH passe à 48 h, avec un début idéal dans les 4 h. La source CFIST/OFSP du 7.11.2025 remplace la mention « déduction 72 h ». |
| 2 | A-SPE-1d | La conduite après un AES est maintenant détaillée : laver la plaie, tester la personne source, débuter la PEP dans les 4 h (au plus tard à 48 h), déclarer à l'assureur LAA. La source CFIST 2025 a été ajoutée. |
| 3 | A-SPE-1f, A-MOT-22 | Contraception d'urgence : stérilet au cuivre jusqu'à 120 h (premier choix au-delà de 70 kg ou d'un IMC > 26), ulipristal jusqu'à 120 h, lévonorgestrel jusqu'à 72 h, doses selon AIPS. Source : IENK 2026. |
| 4 | A-SPE-1b | Les drapeaux rouges reprennent les items des check-lists de la Société suisse de pédiatrie : marche seul et au moins 10 mots à 18 mois, 20 à 50 mots à 24 mois. La mention « déduction » et le piège « à vérifier » ont été supprimés. |
| 5 | A-MOT-23 | Contraception en périménopause : 12 mois d'aménorrhée après 50 ans, 24 mois avant 50 ans. Ce seuil reste « à vérifier » : on n'a lu que le résumé de l'article de la RMS 2015, et le texte s'appuie aussi sur la HAS (source européenne). |
| 6 | A-MOT-22 | La référence OMS passe à la 6e éd. du MEC (3.11.2025), citée en dernier recours et non lue. IENK 2026 est cité avant elle. |
| 7 | A-SPE-1c | La question discriminante devient « recherche un trouble bipolaire : une réponse négative ne l'exclut pas ». |
| 8 | MOT-4, 8, 9, 11, 13, 14, 16, 17, 18, 19, 20, 22, 23, 24 | Chaque groupe porte maintenant une lettre VITE DIT CAFé : obstruction en Tr/D, D/T ou T/D ; grossesse en V ; préhépatique en F/C ; neurologique en V/D/A, V/T/D ou V/T/I. |
| 9 | 1c, MOT-8, 9, 13, 15, 17 | Les hypothèses sont reclassées par gravité puis par fréquence : causes organiques en tête (1c) ; GEU en 2e (MOT-8) ; V en tête (MOT-9, MOT-15) ; angiocholite avant hémolyse (MOT-13) ; queue de cheval en tête (MOT-17). |
| 10 | A-SPE-1a | Deux groupes ont été ajoutés : A (Kawasaki, arthrite juvénile systémique) et T (leucémie aiguë, neuroblastome, tumeur de Wilms). Ils sont classés juste après les causes infectieuses et traumatiques et sont marqués « déduction ». |

## Patchs légers (n° 11 à 22)

- **n° 11** : A-SPE-1b reçoit le groupe « Ia — Toxique prénatal » (syndrome d'alcoolisation fœtale, saturnisme).
- **n° 12** : A-MOT-1 reçoit la rupture œsophagienne et un groupe I/Tr sous-diaphragmatique (ulcère perforé, pancréatite, cholécystite).
- **n° 13** : A-MOT-2 reçoit un groupe Ia (bêtabloquant et AINS chez l'asthmatique, amiodarone, méthotrexate).
- **n° 14** : A-MOT-4 renomme le groupe en « Ia/F — Hypotension orthostatique ».
- **n° 15** : trois seuils portent maintenant l'étiquette « source européenne, non lu » : Baveno VII (MOT-12), EAU (MOT-18) et ESHRE 2024 (MOT-23).
- **n° 16** : A-MOT-24 complète la règle de Naegele par « ≈ DDR + 280 j », soit le 15.12.2026, et rappelle que l'échographie du 1er trimestre fixe le terme.
- **n° 17** : A-MOT-25 retire la limite d'âge de 30 ans ; la triple évaluation s'applique à tout âge.
- **n° 18** : A-TRAME retire « environ dix minutes » et fixe les âges des événements cardiovasculaires familiaux à 55 ans chez l'homme et 65 ans chez la femme.
- **n° 19** : SSP 192 et 195 ajoutées à A-SPE-1a et SSP 182 à A-MOT-24, toutes vérifiées dans PROFILES 2017 ; S-17 et S-26 ajoutés aux liens de A-SPE-1g.
- **n° 20** : A-SPE-1c remplace la question « confus ? » par l'orientation dans le temps et l'espace.
- **n° 21** : MOT-22 et MOT-24 précisent « Orfiril® solution buvable ». **Reste ouvert** : verser l'extrait AIPS dans le cache local, ce qui sort du périmètre des fiches.
- **n° 22** : les conduites nominales de MOT-1, MOT-4 et MOT-6 sont réécrites en phrases verbales.

## Honnêteté

L'auditeur a lu les sources CFIST 2025, IENK 2026 et les check-lists de la SSP ; je ne les ai pas relues. Elles portent donc la mention « lu (audit du 14.11.2026) ». Les fichiers sources de génération du scratchpad (p1.py à p9.py) ne contiennent pas ces patchs : les JSON font foi.

## Tour 2 (AUDIT_ANAMNESE_01_25_V2.md, 14.11.2026)

- **V2-1 (moyen)** : dans A-SPE-1b, les drapeaux rouges [1] et [2] posaient la question à l'envers. Je les ai remplacés mot pour mot par le texte de l'audit : « ne marche-t-il toujours pas seul ? » et « dit-il moins de 10 mots ou ne réagit-il pas à son nom ? ». La réponse « oui » déclenche maintenant bien la conduite.
- **V2-2** : la question de A-SPE-1c devient « Se trompe-t-il sur le jour ou le lieu ? (…) ».
- **V2-3** : dans A-MOT-24, la ponctuation « 17.12.2026, soit » est corrigée.
- **V2-4** : dans A-MOT-8, le groupe Tr/D ne mentionne plus que la « torsion testiculaire », car la torsion d'annexe figure déjà dans le groupe V.
- **V2-5** : dans A-MOT-24, le drapeau rouge du valproate cite maintenant mot pour mot la contre-indication pendant la grossesse (AIPS Orfiril n° 43225, sept. 2025).
- **V2-6** : les conduites nominales restantes de A-MOT-4 (haut risque, pointe de l'iceberg, cardiopathie, mort subite familiale, méléna) et de A-MOT-6 (red flags HUG 2025) sont réécrites en phrases verbales.
- **Patch 21** : l'audit V2 le déclare clos.
- **Validation** : les 33 JSON se rechargent avec json.load.
