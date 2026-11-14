# Corrections : EXP_c.json (EXP-103 à EXP-153), 14.11.2026

Réponse à `AUDIT_EXP_103_153.md`. J'ai relu chaque citation AIPS dans le texte en cache (`aips_fiche.py`, appel par URL refdata) avant de la reporter. Le JSON passe `json.load` (51 entrées).

## Défauts critiques
| # | id | Correction |
|---|---|---|
| 1 | 109 | Gynipral, tocolyse d'urgence : « Administrer le contenu d'une ampoule en injection i.v. lente (c.-à-d. sur une période de 5 à 10 minutes) », puis perfusion ; 48 h au maximum (n° 44438, novembre 2024). |
| 2 | 113 | Gonal-f PEN n° 56689 (août 2026) : « 75 à 150 UI de Gonal-f par jour », paliers de 37,5 UI tous les 7 ou 14 jours, anovulation du groupe II de l'OMS. Clomifène : À vérifier, absent du corpus. |
| 3 | 143 | Lucrin Dépôt n° 51903 (mai 2025) : « 0,3 mg/kg pour 4 semaines (minimum 7,5 mg) », avec le tableau de doses par poids. |
| 4 | 153 | Haldol n° 26891 : dose du sujet âgé (la moitié de la dose adulte, maximum compris) ; contre-indications : syndrome parkinsonien, démence à corps de Lewy, allongement connu du QTc ; ECG préalable. |

## Défauts graves
| # | id | Correction |
|---|---|---|
| 5 | 136 | Gold : Synacthen 0,25 mg, cortisol à 0 et 30 min (60 min facultatif). Seuil : > 500 nmol/l ou hausse ≥ 200 nmol/l (AIPS Synacthen n° 31723, juin 2023, lu). Lecture et source mises à jour. |
| 6 | 122 | Remplacé « pression d'orteil > 30 » par « index orteil/bras ≥ 0,70 ; pression d'orteil < 30 mmHg = ischémie menaçante ». TcPO2 patchée. |
| 7 | 135 | Source « ERS 2022 » remplacée par ATS 2020 (Jacobs, AJRCCM 2020;202:e121, source américaine, dernier recours). Traitement reformulé. |
| 8 | 114 | Contre-indication aux dérivés nitrés et aux donneurs de NO ajoutée (AIPS Viagra n° 54642). |

## Défauts moyens
| # | id | Correction |
|---|---|---|
| 9 | 113 | Utrogestan en FIV : « 2 capsules […] à 200 mg par jour à partir du jour de l'injection d'HCG jusqu'à la 12e semaine ». |
| 10 | 144 | Zometa : ajouté « hors AIPS si l'hypercalcémie n'est pas maligne ». |
| 11 | 147 | Mise en garde Prolia citée : « après l'arrêt du traitement par Prolia, des fractures vertébrales multiples ». Relais : À vérifier (SVGO). |
| 12 | 136 | Crise : l'AIPS ne donne pas de dose. Ajouté hors AIPS : 100 mg i.v. puis 200 mg/24 h (Endocrine Society 2016, non lu). |
| 13 | 142 | Bolus hors AIPS : 150 ml de NaCl 3 % en 20 min, 2 fois au maximum (Spasovski 2014, non lu), avec la limite AIPS de 10 mmol/l par jour. |
| 14 | 111, 112 | Bétaméthasone, sulfate de magnésium (neuroprotection) et progestérone vaginale passés en « hors AIPS », sans dose ; schéma : À vérifier (avis d'experts SGGG à identifier, ou FIGO 2021). |
| 15 | 128, 134 | Directive 2014/85/UE retirée et remplacée par l'OAC, annexe 1 (RS 741.51), À vérifier sur fedlex. |
| 16 | 138 | Auteurs corrigés (Gastaldi, Lucchini, Thalmann et al.). Ajouté : association précoce de la metformine avec un iSGLT2 ou un AR GLP-1 selon le risque cardio-rénal. |
| 17 | 131 | Source RLS remplacée : EFNS/ERS/ESRS, Garcia-Borreguero, Eur J Neurol 2012 (non lu). |
| 18 | 105 | Ajouté la source « AIPS Vesicare n° 57203 ». |
| 19 | 120, 136, 141, 144, 150 | Les cinq traces sont maintenant chiffrées. |

## Défauts légers
| # | Correction |
|---|---|
| 20 | 165 puces nominales de `autres.quand` et `autres.pourquoi_pas_gold` réécrites en phrases verbales. |
| 21 | 153 : le 4AT de rang 2 est remplacé par la CAM. |
| 22 | 109 : la ligne SSGO sans numéro est supprimée. |

## Valeurs « À vérifier » patchées
106 (normes HR-ARM, IAPWG), 107 (≤ 60 s), 114 (PSV > 30 / < 25 ; EDV > 5), 116 (source EULAR SG Microcirculation), 117 (Allen, Barbeau), 122 (TcPO2), 124 (TUG < 15 s), 135 (T90, INOX), 141 (pic de GH ≈ 7 µg/l, seuil du laboratoire, toujours « À vérifier »).

## Ce qui reste ouvert
- Le clomifène, l'oxybate, la métyrapone, le kétoconazole et l'urée sont absents du corpus AIPS.
- Les schémas obstétricaux dépendent d'un avis d'experts SGGG non encore identifié.
- L'OAC n'a pas été lue.
- Ni commit ni push.

## Tour 2 (réponse à AUDIT_EXP_103_153_V2.md)
J'ai appliqué P1 à P5 mot pour mot, puis les recommandations P6 à P9. Le JSON passe `json.load`.
- P1 (137) : « il exige une ponction lombaire » devient « il exige un cathétérisme veineux fémoral bilatéral jusqu'aux sinus pétreux ». L'erreur venait de la réécriture automatique de « invasif » ; la formulation reste juste en 130 (hypocrétine du LCR).
- P2 (113) : ajouté la source « AIPS Gonal-f PEN n° 56689, août 2026, refdata (lu) ».
- P3 (136) : valeur « hausse ≥ 200 (70 µg/l), c.-à-d. > 500 (180 µg/l) à 30 min » ; trace pathologique « Courbe plate : cortisol à 30 min ≤ 500 nmol/l ».
- P4 (122) : trace normale « TcPO2 ≥ 60 mmHg au dos du pied (pas d'ischémie) ».
- P5 (114) : trace normale « Doppler pénien après injection : pic systolique > 30 cm/s, télédiastolique ≤ 5 cm/s ».
- P6 (141) : trace normale alignée sur le seuil du laboratoire (≈ 7 µg/l, IS 98/574).
- P7 (114) : ajouté la contre-indication au riociguat (stimulateur de la guanylate cyclase).
- P8 (135) : ajouté l'essai INOX aux sources.
- P9 (122) : source de la TcPO2 précisée par seuil.
Ni commit ni push.
