# Corrections après audit : A-MOT-26 à A-MOT-60

J'ai appliqué l'audit `AUDIT_ANAMNESE_26_60.md` le 14.11.2026. Les 35 JSON sont réécrits dans `anamnese/` et chacun passe json.load. Je n'ai ni commité ni poussé.

## Défauts graves

| # | Fiche | Correction appliquée |
|---|---|---|
| G-1 | 26 | J'ai ajouté les 4 drapeaux du PATCH (néoplasie ou immunodépression ; céphalée positionnelle ou déclenchée par la toux ou l'effort ; céphalée récente ou progressive avec œdème papillaire ; œil douloureux avec signes autonomes). J'en ai ajouté un 5e : surconsommation d'antalgiques ou nouveau médicament. Les 11 drapeaux couvrent ainsi les 15 critères SNNOOP10 du tableau 2 HUG 2022, et un piège les énumère tous. |
| G-2 | 27 | J'ai ajouté le drapeau « chute » (hématome sous-dural sous anticoagulant, fracture, rhabdomyolyse, évaluation multifactorielle). J'ai aussi ajouté un axe « Chutes » avec les trois questions de repérage HUG, et cité la source HUG Personnes âgées 2026, § 4.3. |
| G-3 | 31 | J'ai placé en tête le drapeau « déficit sensitif brutal unilatéral », qui renvoie à l'AVC ou l'AIT, au 144 et à la filière AVC. J'ai mis « AVC ou AIT » en tête des hypothèses V et ajouté SY-12 et IMG-001 aux liens. |

## Défauts moyens

| # | Fiche | Correction appliquée |
|---|---|---|
| M-1 | 26 | Conduite devant une suspicion d'hémorragie sous-arachnoïdienne : une angio-TDM faite dans les 6 heures est très sensible ; au-delà de 6 heures et avec une imagerie normale, la ponction lombaire est indiquée. J'ai relu ce passage dans HUG 2022, tableau d'imagerie et § 5.3. |
| M-2 | 28 | Drapeau [0] : « Le déficit a-t-il commencé brutalement ? », AVC quel que soit le délai, avec les délais Swiss Stroke Society marqués « À vérifier ». Drapeau [3] : glycémie capillaire chez tout patient, sans retarder la filière AVC. |
| M-3 | 32 | L'AIT rétinien devient une urgence neurovasculaire le jour même, par la filière AVC. |
| M-4 | 33 | J'ai ajouté le drapeau « cellulite orbitaire », qui renvoie à IMG-046, et mis ce diagnostic en tête des hypothèses I. |
| M-5 | 36 | J'ai ajouté une hypothèse V (syndrome coronarien aigu avec douleur projetée à la gorge) et le syndrome de Lemierre. Le piège Centor est réécrit en phrases verbales. |
| M-6 | 55 | Seuil d'alcool à faible risque selon Addiction Suisse, repris par HUG 2021 (§ 2.1, tableau 1, relu) : au plus 2 verres standard par jour chez l'homme, 1 chez la femme, et 2 jours sans alcool par semaine. Seuil à risque (HUG 2021, § 2.4, relu) : plus de 30 g chez l'homme, plus de 20 g chez la femme. L'ancien seuil de l'ASSM 2022 (4 et 2 verres) est signalé comme dépassé. |
| M-7 | 38 | On ponctionne avant de donner l'antibiotique, sauf en cas de sepsis. |
| M-8 | 51 | Le RUD est désormais gradé (faible, moyen, élevé) selon le tableau 4b de HUG 2022. |
| M-9 | 52 | Les axes sont renommés selon R, U, D. J'ai ajouté « En cas de danger immédiat, appeler le 144. » |
| M-10 | 21 fiches (27, 29, 31-35, 38, 40-44, 46-50, 53, 56) | Le triplet générique est remplacé par trois questions ICE propres au motif. |
| M-11 | Toutes | Chaque conduite de drapeau rouge sans source porte désormais l'étiquette « déduction, non vérifié CH ». Cela concerne 131 conduites, fondues dans la parenthèse existante quand il y en avait une. |

## Défauts légers

| # | Correction appliquée |
|---|---|
| L-1 | Fiche 26 : j'ai ajouté le syndrome de vasoconstriction cérébrale réversible et l'apoplexie hypophysaire aux hypothèses V. La lettre devient « I (iatrogène, toxique) », avec l'intoxication au monoxyde de carbone. |
| L-2 | Fiche 39 : la synthèse précise le critère d'Ottawa (bord postérieur et pointe de la malléole latérale, sur 6 cm). |
| L-3 | Fiches 28 et 39 : j'ai ajouté l'axe « Facteurs d'influence ». |
| L-4 | J'ai ajouté les liens SY-11 (fiche 40), SY-12 (fiche 54) et S-35 (fiche 58). |
| L-5 | Fiche 57 : la malrotation (volvulus) passe en premier dans l'hypothèse C. |
| L-6 | Fiche 29 : « épilepsie focale structurelle » est remplacée par « malformation du développement cortical ». |
| L-7 | Fiche 42 : le qSOFA porte l'étiquette « source internationale, Sepsis-3 ; non vérifié CH ». |
| L-8 | Fiche 49 : la source devient « lu partiellement : points à retenir ». Fiche 59 : j'ai ajouté le DOI 10.53738/REVMED.2026.22.976.49183, vérifié dans le PDF. |
| L-9 | Fiche 54 : le piège sur la SMC est reformulé (SMC 2024, figure 1). |
| L-10 | Fiche 55 : la question d'ivresse ponctuelle suit HUG 2021, § 2.4 (plus de 4 verres chez la femme, plus de 5 chez l'homme). |

## Les 7 sources que l'auditeur n'a pas vérifiées

J'ai lu ces 7 sources moi-même pendant la rédaction, dans des PDF téléchargés de hug.ch ou des copies locales. J'ai gardé l'étiquette « lu » seulement pour la partie réellement lue, et je l'ai précisée :

- protocole HUG « Vertige isolé aigu » 2020 : algorithme lu en entier (1 page) ;
- HUG Anémie 2022 : points à retenir ;
- HUG Carences vitaminiques 2025 : lu partiellement (tableau B12) ;
- HUG Urticaire et angioedème 2023 : points à retenir ;
- HUG Vaccination 2025 : points à retenir ;
- Swiss Memory Clinics 2024 : sections 2 et 3, figure 1 ;
- Gardier, RMS 2018 : lu partiellement.

Les sources de la Swiss Stroke Society, de la Ligue contre l'épilepsie, de Pédiatrie Suisse et du CEMV restent marquées « non lu » ou « À vérifier ».
