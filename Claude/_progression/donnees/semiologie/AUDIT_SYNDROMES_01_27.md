# Audit médical agressif — Syndromes SY-1 à SY-27 (14.11.2026)

Objet : `syndromes/SY-1.json` à `SY-27.json` (≈ 170 Ko), lus en entier. Contrôles faits : 38 AIPS ouvertes par `aips_fiche.py fiche <URL refdata>` et chaque citation confrontée au texte en cache (toutes retrouvées, aux coupures de mise en page près) ; `trouve` lancé sur chaque molécule déclarée « absente » ou « non lisible » ; 9 images lues (Read) ; licences vérifiées par l'API Commons (8/9 ; SY-18 non vérifiée, limite de débit) ; renvois S-xx et SY-xx tous présents. Calculs refaits : Nasonex 4 × 2 × 50 µg = 400 µg/j ✓ ; Brown-Séquard T10 → T8–T9 ✓ ; asymétrie de PA 170/135 = 35 mmHg > 20 ✓.

## Verdict : **corrections requises** (6 critiques). Question finale : **non**. Il faut corriger les 6 critiques et les 7 défauts graves.

## Score (grille 2/1/0)

| Axe | Pts | Raison |
|---|---|---|
| Définition, symptômes, physiopathologie, différentiels, drapeaux rouges, phrases verbales | 2 × 6 | Justes, verbales et utiles en CS |
| Signes et valeurs | 1 | Valeurs reprises surtout de sources américaines ; plusieurs « À vérifier » |
| Étiologies VITE DIT CAFé | 1 | Erreurs de catégorie (L4) |
| Examens clés | 1 | Seuils absents : NT-proBNP, critères de Light, pH pleural |
| Management et doses AIPS | 0 | 6 critiques (C1–C6) |
| Écarts AIPS/recommandation signalés | 1 | Signalés pour SY-5 et SY-25 ; non signalés en G2, G4 et M1–M2 |
| Synthèse orale CS | 1 | Contradiction en SY-14 ; Wells ambigu en SY-23 |
| Sources | 1 | Recommandations suisses et ESC presque toutes « non relues » ; SY-7 et SY-11 sans source |
| Images | 1 | Licences conformes ; légende SY-1 fausse ; SY-27 peu lisible |
| **Total** | **19/28 = 67,9 %** | Refusé (< 90 % et critiques présentes) |

## Critiques — PATCH exact

| # | Emplacement | Extrait | PATCH | Source lue |
|---|---|---|---|---|
| C1 | SY-19 management[2] | « bolus 80 U.I./kg PC … 18 U.I./kg PC par heure » | Remplacer par : « angor instable ou NSTEMI : « 60-70 U.I./kg PC (dose maximale : 5 000 U.I.) » puis « 12 - 15 U.I./kg PC par heure (maximum 1 000 U.I. par heure) » ; STEMI avec fibrinolyse : « 60 U.I./kg PC (maximum 4 000 U.I.) » puis « 12 U.I./kg PC par heure » ». La fiche citait la ligne générale des maladies thromboemboliques, soit une surdose d'environ 30 %. | AIPS Heparin-Na B. Braun n° 46613, juin 2026 |
| C2 | SY-25 management[1] | « labétalol : AIPS non lisible par l'outil, À vérifier » | « labétalol (« Urgences de l'hypertension artérielle sévère ») : « administrer 50 mg de Trandate en injection intraveineuse lente (1 minute au minimum) … toutes les 5 minutes … sans dépasser une dose globale de 200 mg » (AIPS Trandate® n° 41529, refdata 08.05.2026) » | AIPS Trandate, lue |
| C3 | SY-6 management[2] | « sérum salé hypertonique : molécule absente du corpus consulté » | Affirmation fausse. Écrire : « NaCl 10 % : HTIC hors AIPS (indications : « Hyponatrémie. Hypochlorémie. Intoxications par l'eau… ») (AIPS NaCl 10% B. Braun n° 29555, avril 2022) ; schéma décidé aux soins intensifs ». | AIPS lue |
| C4 | SY-13 management[1] | « apraclonidine : AIPS non lisible par l'outil, À vérifier » | Supprimer. L'AIPS d'Iopidine 0,5 % (n° 52813) est lisible ; elle limite le produit au traitement d'appoint du glaucome chronique (1 goutte 3 ×/j, au maximum 3 mois), ce qui exclut la crise aiguë. | AIPS lue |
| C5 | SY-4 management[1] | « dimenhydrinate : AIPS de la forme hospitalière non lue, À vérifier » | Le dimenhydrinate figure au corpus (Trawell® n° 43194), mais pour les seuls « maux de voyage ». Remplacer par : « méclozine : « Nausées et vomissements de toutes origines » ; « 1–2 supp. adultes … ou 1–4 gélules » par 24 h (AIPS Itinerol® B6 n° 18383, juin 2025) ». | AIPS lues |
| C6 | SY-24 management[1] | « (ceftriaxone, amoxicilline, flucloxacilline, vancomycine, gentamicine) ; non détaillé ici, À vérifier » | Supprimer la liste. Écrire : « antibiothérapie IV probabiliste décidée avec l'infectiologue après les 3 paires d'hémocultures ». Toute molécule nommée exige sa dose AIPS. | Règle §23 |

## Graves

| # | Emplacement | Défaut | PATCH (source) |
|---|---|---|---|
| G1 | SY-23 management[0] | La fiche propose rivaroxaban et apixaban, cite la grossesse comme contexte et ne donne aucune contre-indication. | Ajouter : « Grossesse : « Le rivaroxaban est contre-indiqué pendant la grossesse » (AIPS Xarelto n° 58728) ; utiliser l'énoxaparine. » |
| G2 | SY-19 management[2] | Ticagrélor donné d'emblée à tous | Ajouter : « pas de prétraitement si coronarographie < 24 h dans un SCA sans sus-décalage (ESC 2023, classe III) ; ticagrélor à discuter avant l'angioplastie primaire (IIb) » (source européenne, résumé ESC lu). |
| G3 | SY-14 a_dire_cs[1] | « prednisolone … selon l'AIPS », alors que le management la dit hors AIPS. Aucun schéma n'est donné. | « Je prescris de la prednisolone hors AIPS dans les 72 h, selon la recommandation » ; lire puis citer le schéma de Sullivan 2007 (non relu par l'audit). |
| G4 | SY-5 management[2] | La dose adulte de ceftriaxone dans la méningite n'est pas précisée. | « Méningite de l'adulte : 4 g/j, dose maximale AIPS en une prise ; l'ESCMID donne 2 g toutes les 12 h : écart à signaler, À vérifier ». |
| G5 | SY-13 management[1] | Timolol : la crise aiguë ne figure pas dans les indications AIPS ; contre-indications absentes. Pilocarpine : l'AIPS liste le « glaucome par blocage pupillaire » en contre-indication, contre sa propre indication. | Écrire « timolol hors indication aiguë ; contre-indiqué si « asthme bronchique … BPCO sévère ; bradycardie sinusale » » (AIPS Timoptic n° 41634) ; signaler la contradiction de l'AIPS Spersacarpine n° 26073 et laisser la décision à l'ophtalmologue. |
| G6 | SY-15 management | Angio-œdème bradykinique cité en étiologie, mais le management ne propose que l'adrénaline (inefficace dans ce cas) | Ajouter : « angio-œdème héréditaire : icatibant, « une injection unique de Firazyr 30 mg en sous-cutanée », répétable 6 h plus tard, au plus 3 injections par 24 h (AIPS Firazyr n° 58178, février 2026) ». Corps étranger chez le nourrisson : compressions thoraciques, pas abdominales (ERC, À vérifier). |
| G7 | SY-25 management[1] | Esmolol : l'AIPS précise que « l'utilisation de Brevibloc est réservé au traitement per- et postopératoire immédiat ». Aucune cible n'est donnée. | Citer cette phrase (hors AIPS) et ajouter la cible : « FC ≈ 60/min puis PA systolique basse (ESC 2024, valeurs exactes à lire) ». |

## Moyens

| # | Emplacement | PATCH |
|---|---|---|
| M1 | SY-3 management[1] | L'AIPS Benerva limite la dose à 200 mg/j ; la recommandation européenne sur l'encéphalopathie de Wernicke prévoit des doses plus fortes (EFNS 2010, non relue). Signaler l'écart. |
| M2 | SY-6 management[2] | Le mannitol AIPS (« 1–2 g/kg … en 30–60 min ») dépasse les doses usuelles en neuroréanimation. Signaler l'écart après lecture d'une recommandation. Ajouter le mannitol en SY-13 : l'AIPS couvre l'hypertension « intraoculaire ». |
| M3 | SY-21 | Ajouter la cible de PAM ≥ 65 mmHg et le volume de remplissage (Surviving Sepsis 2021, à lire), ainsi que l'hydrocortisone si l'insuffisance surrénalienne est l'étiologie retenue. |
| M4 | SY-27 | Préciser les critères de Light (protéines pleurales/sériques > 0,5 ; LDH pleurale/sérique > 0,6 ; LDH pleurale > 2/3 de la limite supérieure), le seuil de pH < 7,2 pour le drainage et le volume maximal par ponction (BTS, à lire). |
| M5 | SY-17 examens[0] | Donner les seuils d'exclusion du NT-proBNP et du BNP (ESC 2021, à lire). |
| M6 | SY-1 a_dire_cs[0] | Formulation actuelle : « médullaire si elle est épargnée ». Écrire : « médullaire ou corticale limitée si la face est épargnée ». |
| M7 | SY-26 management[1] | Préciser la dose retenue pour une pneumonie (borne haute AIPS : 3 g/j) et la recommandation SSI. |
| M8 | SY-7, SY-11 | Seule source : « déduction ». Citer un manuel ou une faculté suisse. SY-10 ne cite qu'une source américaine. |
| M9 | SY-5 | Déclaration de la méningococcie : lire les délais OFSP avant de les écrire. SY-12 : ajouter le seuil de PA avant thrombolyse, tiré de l'AIPS Actilyse. |

## Légers

L1 : la légende de SY-1 annonce un « écartement des autres orteils », alors que l'image montre des orteils fléchis. Corriger la légende.
L2 : renvois en double (SY-2 : IMG-023 pour l'IRM et le DaTSCAN ; SY-20 : EXP-065 pour l'ECG et l'écho).
L3 : SY-9, « milieu des mollets ». Le seuil classique est plutôt le genou ; à sourcer.
L4 : catégories VITE DIT CAFé mal placées : simulateurs en F (SY-12) ; infarctus du VD et constriction en F (SY-18) ; Libman-Sacks en A (SY-24) ; anaphylaxie classée deux fois (SY-21) ; botulisme en F (SY-10).
L5 : SY-23, le cas cumule 2 points de Wells, soit une probabilité intermédiaire à 3 niveaux. La phrase « élevé » demande la version à 2 niveaux : la préciser.
L6 : l'image de SY-27 est une capture de vidéo floue, sans repère ; l'annoter.
L7 : le visage de SY-14 reste en partie identifiable (autoportrait probable de l'autrice, non vérifié).
