# Audit médical du texte : TC_RA.json (IMG-042 à IMG-104)

| Objet | Valeur |
|---|---|
| Fichier | `enrichi/TC_RA.json`, 191 665 octets, SHA-256 `993dc79846a3…`, dernier commit 136b90ccd. Le JSON est valide et contient 63 fiches. |
| Périmètre | Champs gold, premiere_intention, autres, syndrome, traitement et sources. Les images sont exclues du périmètre. |
| Méthode | J'ai lu 38 AIPS du corpus refdata par URL (`aips_fiche.py trouve` puis le texte HTML). J'ai fait 11 recherches web (ESO-ESMINT, EULAR, EHA-EMN, SVGO, AO Spine, ESC, EUGOGO, Chiari) et refait 6 calculs en Python. Un script a compté les « À vérifier », l'ordre et l'étiquetage des sources. |
| Relevé mécanique | 64 « À vérifier ». 13 fiches placent l'AIPS (source suisse) après les sources européennes. 9 sources sur 120 portent une étiquette. |
| Verdict | **Corrections requises.** Il y a 24 défauts critiques, 10 majeurs et 6 mineurs. |

## 1. Critiques (AIPS présente au corpus, puis « À vérifier » ou dose fausse)

| # | Emplacement | Extrait | PATCH exact (AIPS lue) |
|---|---|---|---|
| C1 | 042 TT[0] | « prolactinome : … cabergoline 0,5 mg par semaine … (AIPS Dostinex) » | Ajouter : « AIPS Dostinex n° 51756 (nov. 2025) : indication limitée aux **micro**prolactinomes ; macroprolactinome **hors AIPS** (Pituitary Society 2023). Contre-indications : valvulopathie, antécédent de fibrose pulmonaire, péricardique ou rétropéritonéale, insuffisance hépatique sévère, inhibiteurs du CYP3A4. Allaitement : ne pas allaiter. » |
| C2 | 042 TT[3] ; 043 TT[2] ; 045 TT[0] | « doses : À vérifier » | « hydrocortisone 10–20 mg/j en insuffisance surrénale chronique (AIPS Hydrocortisone Galepharm n° 57970, août 2025) ; lévothyroxine après les glucocorticoïdes, 25–50 µg/j au départ puis 100–200 µg/j (AIPS Euthyrox n° 54949, févr. 2023) ; desmopressine p.o. 0,1 mg 3×/j au départ, 0,2–1,2 mg/j (AIPS Minirin cp n° 49002, févr. 2024) » |
| C3 | 044 TT[0] | « dose : À vérifier (AIPS Solu-Cortef non relue …) » | « AIPS Solu-Cortef n° 23533 (oct. 2025) : indication choc par insuffisance corticosurrénalienne ; jusqu'à 100 mg i.v. en ≥ 30 s, puis toutes les 2 à 6 h. Le schéma de 100 mg puis 200 mg/24 h relève de la recommandation, pas de l'AIPS. » |
| C4 | 046 TT[2] ; 073 TT[1] ; 063 TT[1] ; 074 TT[2] | « co-amoxicilline ; dose AIPS : À vérifier » | « p.o. : 3 × 625 mg/j ou 2 × 1 g/j, 3 × 1 g/j au plus (AIPS Augmentin n° 45674, sept. 2026). i.v. : 1,2 g 3–4×/j, ou 2,2 g 3–4×/j si l'infection est grave (AIPS Co-Amoxi-Mepha i.v. n° 56758, sept. 2026) » |
| C5 | 053 TT[0] | « métronidazole … (dose : À vérifier) » | « métronidazole i.v. : 15 mg/kg, puis 7,5 mg/kg toutes les 6 h pendant 3 j, puis toutes les 12 h ; durée de 5 à 7 j, 10 j au plus ; l'abcès cérébral est indiqué (AIPS Metronidazol B. Braun n° 48018, févr. 2026) » |
| C6 | 054 TT[3] | « amphotéricine B liposomale (dose : À vérifier) » | « mucormycose : 5–10 mg/kg/j dès J1, 10 mg/kg/j en cas d'atteinte du SNC, sans paliers (AIPS AmBisome n° 53342, janv. 2025) » |
| C7 | 049 TT[1] | « sélénium 6 mois (EUGOGO 2021) ; dose : À vérifier » | « sélénite de sodium 100 µg 2×/j pendant 6 mois (EUGOGO 2021) ; **hors indication AIPS** : selenase n° 53770 vise la seule carence » |
| C8 | 050 TT[0] ; 100 TT[0] | « dose AIPS : À vérifier » | « AIPS Solu-Medrol n° 35112 (août 2025) : poussée de SEP 500–1000 mg/j i.v. en 30 min pendant 3–5 j ; névrite optique isolée, NMO et MOGAD **hors AIPS** » |
| C9 | 080 TT[1] | « méthylprednisolone i.v. à forte dose … dose : À vérifier » | « 0,25–1 g/j i.v. pendant 3 j au plus (EULAR) ; AIPS Solu-Medrol n° 35112 : traitement i.v. intermittent ≥ 250 mg/j, ≤ 5 j » |
| C10 | 062 TT[1] | « cisplatine ; dose AIPS : À vérifier » | « AIPS Cisplatine Sandoz n° 51077 (août 2023) : carcinome épidermoïde ORL, 50–100 mg/m² en dose unique, **intervalle de 4 semaines “absolument indispensable”** ; le schéma de 100 mg/m² toutes les 3 semaines avec la radiothérapie s'écarte de l'AIPS (EHNS-ESMO-ESTRO) » |
| C11 | 068 TT[0] ; 069 TT[1] | « bêtabloquant … molécule et dose : À vérifier » | « propranolol 10–40 mg 3–4×/j ; hyperthyroïdie indiquée (AIPS Inderal n° 31706, janv. 2023) » |
| C12 | 068 TT[1] | « carbimazole ou thiamazole … dose AIPS : À vérifier » | « carbimazole 20–60 mg/j en 2–3 prises pendant 15–30 j, puis entretien ; durée de 6 à 18 mois. Renoncer si possible au 1er trimestre. Contraception fiable. Allaitement déconseillé (AIPS Néo-Mercazole n° 21037, août 2020). Thiamazole absent du corpus. » |
| C13 | 069 TT[0] | « lévothyroxine ; dose adulte : À vérifier » | « 25–50 µg/j au départ, paliers de 25–50 µg toutes les 2–4 semaines, entretien 100–200 µg/j (AIPS Euthyrox n° 54949). La même AIPS est déjà citée en 075. » |
| C14 | 070 TT[1] | « cinacalcet ; dose AIPS : À vérifier » | « HPT primaire sans chirurgie possible : 30 mg 2×/j, puis paliers toutes les 2–4 semaines jusqu'à 90 mg 3–4×/j (AIPS Cinacalcet Spirig HC n° 69216, nov. 2020 ; Mimpara absent du corpus) » |
| C15 | 076 TT[1] | « acide acétylsalicylique 100 mg par jour (AIPS Aspirine Cardio) » | **Dose fausse pour l'indication.** « AIPS Aspirine Cardio n° 51795 (mars 2026) : après AIT, 300 mg 1×/j ou 100 mg 3×/j. La dose de 100 mg/j est la dose cardiovasculaire générale (écart signalé) » |
| C16 | 077 TT[1] ; 098 TT[1] | « dose AIPS Aspirine Cardio » | 077 : même PATCH que C15. 098 : « infarctus médullaire **hors indication AIPS** ; 100 mg/j selon la pratique, à signaler comme tel » |
| C17 | 087 TT[1] | « tériparatide, romosozumab … doses AIPS : À vérifier » | « tériparatide 20 µg/j s.c., 24 mois au plus (AIPS Forsteo n° 56007, avr. 2026) ; romosozumab 210 mg/mois s.c. pendant 12 mois, puis antirésorptif, **contre-indiqué après un infarctus du myocarde ou un AVC** (AIPS Evenity n° 67033, juil. 2024) » |
| C18 | 088 TT[0] | « dose AIPS Fortecortin pour cette indication : À vérifier » | « AIPS Fortecortin n° 48669/48670 (2022) : œdème cérébral et traitement palliatif des tumeurs malignes. La compression médullaire n'a **pas de posologie AIPS** ; les 16 mg/j viennent de NICE NG234. » |
| C19 | 089 TT[1] | « doses AIPS pour le myélome : À vérifier » | « acide zolédronique 4 mg i.v. en ≥ 15 min toutes les 3–4 semaines, avec calcium 500 mg et vitamine D 400 UI/j (AIPS Zometa n° 56257, mars 2026) ; dénosumab : le myélome n'est **pas** une indication AIPS (XGEVA n° 61865 : tumeurs solides) » |
| C20 | 092 TT[0] | « AINS à dose maximale tolérée … doses AIPS : À vérifier » | « naproxène 1000 mg/j en attaque, puis 500–1000 mg/j ; la spondylarthrite ankylosante est indiquée (AIPS Naproxen-Mepha n° 51480, sept. 2024) » |
| C21 | 096 TT[2] | « acide folique en périconceptionnel ; dose AIPS : À vérifier » | « 0,4 mg/j au moins 4 semaines avant la conception jusqu'à 12 SA (recommandation) ; **hors indication AIPS** : Acidum folicum 5 mg n° 55746 vise l'anémie mégaloblastique ; > 5 mg/j à éviter pendant la grossesse » |
| C22 | 064 TT[3] | « chimioprophylaxie des contacts (Hib) : À vérifier » | Ouvrir l'AIPS Rimactan n° 34279 (corpus) et l'OFSP. Écrire la dose lue, ou « hors indication AIPS ». |
| C23 | 093 TT[2] | « méthylprednisolone … (AO Spine 2017, faible) » | Ajouter : « AIPS Solu-Medrol n° 35112 : traumatisme médullaire aigu, traitement commencé dans les 8 h ; 30 mg/kg i.v. en ≥ 30 min » |
| C24 | 049 TT[3] | « téprotumumab … (AIPS TEPEZZA) » | Ajouter : « contraception efficace avant, pendant et 6 mois après le traitement (AIPS n° 69795, mars 2026) » |

## 2. Majeurs (recommandation périmée, source fausse ou américaine seule)

| # | Emplacement | Défaut | PATCH |
|---|---|---|---|
| M1 | 087 TT[1], sources | La SVGO 2020 est périmée. | « Ferrari S et al., SVGO 2026 revision, Swiss Med Wkly 2026;156:5700 (08.10.2026) » : stratégie anabolique d'abord en cas de risque très élevé ou imminent, puis consolidation |
| M2 | 080 sources, TT[0]/[3] | EULAR LVV 2018 est remplacée. | « Mukhtyar CB et al., EULAR 2025 PMR/LVV, Ann Rheum Dis 2026 » ; relire la dose de prednisone et l'aspirine dans ce texte |
| M3 | 089 TT[0], sources | EHA-ESMO 2021 est remplacée. | « Dimopoulos MA et al., EHA-EMN guidelines, Nat Rev Clin Oncol 2025;22:680–700 » |
| M4 | 079 TT[2] | ESO-ESMINT 2019 seul ; l'occlusion basilaire est citée au syndrome sans traitement. | Ajouter : « occlusion basilaire, NIHSS ≥ 10 : thrombectomie plus traitement médical (ESO-ESMINT 2024, Eur Stroke J, PMID 38752743) » |
| M5 | 093 TT[1] | AO Spine 2017 donne « suggère ». | « décompression dans les 24 h recommandée (AO Spine/Praxis 2024, Global Spine J 14(3 Suppl)) » |
| M6 | 103 sources | La source est fausse et marquée « À vérifier ». | « Ciaramitaro P et al., Diagnosis and treatment of Chiari malformation and syringomyelia in adults: international consensus, Neurol Sci 2022;43:1327–1342 » |
| M7 | 042, 048, 052, 061, 069, 083, 090 sources | Source américaine seule (Endocrine Society, ACR, AAO, AAOMS, ATA, NASS, IDSA). | Chercher la source suisse, puis européenne (ESE, ESR, EURETINA, ESCMID…), ou écrire « aucune recommandation européenne trouvée le JJ.MM.AAAA » |
| M8 | 076 TT[1] | Clopidogrel : l'AIPS couvre l'AVC récent (7 j à 6 mois), pas l'AIT. | Préciser « AVC ischémique récent ; AIT hors libellé AIPS » |
| M9 | 13 fiches (042, 046, 049, 053, 055, 075–077, 079, 080, 088, 098, 101) | L'AIPS (suisse) figure après les sources européennes ; 111 sources sur 120 n'ont pas d'étiquette. | Trier Suisse → Europe → autres → OMS ; étiqueter « (Suisse) », « (Europe) », « (international) » |
| M10 | 046, 053, 055, 064 TT | « associations et durée : À vérifier » ; l'interdiction d'allaiter de Rocephin n'est pas citée. | Ajouter « allaitement : ne pas utiliser ; si le traitement est indispensable, interrompre l'allaitement (AIPS Rocephin n° 44625) » ; sourcer la durée (EPOS 2020) |

## 3. Mineurs

| # | Emplacement | PATCH |
|---|---|---|
| m1 | 092 PI | Attribuer l'imagerie à EULAR 2015 (Mandl), pas à ASAS-EULAR 2022. |
| m2 | 047, 058 autres | La liste commence au rang 3 : renuméroter au rang 2. |
| m3 | 051 r3 ; 089 r4 | Le champ « quand » vaut « à éviter » ou « aucune indication » : écrire un cadre ou retirer l'entrée. |
| m4 | 064 sources | Remplacer « édition en vigueur : À vérifier » par « OFSP/CFV, plan de vaccination suisse 2026 ». |
| m5 | 049 TT[3] | Citer le consensus ATA/ETA 2022, qui place le téprotumumab en 1re ligne, à côté d'EUGOGO 2021. |
| m6 | 057 TT[0–1] ; 087 TT[0] ; 090 ; 091 | Rendre verbales les puces nominales (« appareiller », « poser un piston par stapédotomie », « calmer la douleur, mobiliser tôt »). |

## 4. Points conformes (contrôlés)

Les fiches suivantes sont conformes à l'AIPS lue (numéro et date) :
- Rocephin 1–2 g/24 h, jusqu'à 4 g ;
- Tepezza 10 puis 20 mg/kg × 7, toutes les 3 semaines ;
- Euthyrox chez le nouveau-né, 0–6 mois : 25–75 µg (10 µg/kg) ;
- Actilyse 0,9 mg/kg, 90 mg au plus, 10 % en bolus, 60 min ;
- Metalyse 25 mg au plus, 4,5 h ;
- Actemra ACG 162 mg toutes les 2 semaines (première manifestation) ou chaque semaine (récidive) ;
- XGEVA 120 mg toutes les 4 semaines avec calcium et vitamine D ;
- Vitarubine Dépôt.

Les éléments suivants sont exacts :
- seuils EU-TIRADS ;
- critères SLiM ;
- 5e atelier sur l'HPT ;
- ESGE 2016 (2 h / 6 h / 24 h) ;
- méthylprednisolone EUGOGO 4,5 g (6 × 0,5 + 6 × 0,25 g, recalculé) ;
- ESVS 2023 (14 j) ;
- NICE NG234 (16 mg) ;
- Bernard 2015.

Examens de référence et premières intentions : je n'ai trouvé aucune erreur bloquante.

**Question finale : non.** Avant `audit-ok`, il faut :
- appliquer C1–C24 (les AIPS sont au corpus) ;
- remplacer les 4 recommandations périmées et la source fausse (M1–M6) ;
- remplacer les 7 sources américaines seules ;
- trier et étiqueter les sources.
