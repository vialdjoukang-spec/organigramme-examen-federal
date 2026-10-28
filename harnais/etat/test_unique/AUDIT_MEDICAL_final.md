# Audit médical (fond) — LOT_001_Phase_B_V0_DX.1.html — itération 8 (28.10.2026)

Auditeur : agent médical, sur ordre explicite de Vial. Points audités : 2, 3, 4, 7, 8, 9, 10, 11, 12 (extraction `controle_lot.py extraire`). Le cours n'a pas été modifié.

## 1. Vérifications faites

| Contrôle | Résultat |
|---|---|
| AIPS lus (`.cache/aips/`) : VEOZA 69232, LYNKUET 69917, ESTROFEM 40050, ESTRADOT 55976, OESTROGEL 46638, FEMOSTON 53128, UTROGESTAN 45351, LIVIAL 49504, OVESTIN 24122, VAGIFEM 49600, CIMIFEMINE 56933 | Doses, voies, rythmes, CI, seuils hépatiques (> 2 × LSN avant ; > 5 × ou > 3 × + bilirubine > 2 × pour l'arrêt), Child-Pugh, DFGe, fluvoxamine × 9,4, itraconazole × 6,32, grossesse/allaitement : **conformes**. Aucun numéro déduit. |
| Chiffres AIPS (SKYLIGHT −6,9/−4,4 ; WHI EP RR 2,13 ; TEV 3 et 8/1000 ; endomètre 5/1000 × 2–12 ; LIBERATE HR 1,40 ; AVC 1,31/1,39 ; arrêt 4–6 semaines avant chirurgie) | Conformes au texte lu. |
| PMID 29217652, 39660328, 32412940, 12904517, 11145492, 16139656, 12804462 (`pubmed.py verifier`) | Existent. Triade 28 % / 14 % confirmée (résumé Europe PMC). |
| Nappi, Maturitas 2023 (31–52 %, 11 452 / 5 178 / 2 035) | Confirmé (résumés secondaires). |
| NAMS 2023 (PDF lu) : refroidissement et déclencheurs « Level II », perte de poids II–III | Conforme. |
| SGGG avis d'experts n° 99 (PDF lu, p. 1–3) | Existe ; niveaux I (NK3, ISRS/ISRSN, gabapentine, TCC, hypnose), oxybutynine I–II, Ze 450 niveau II, clonidine/prégabaline non recommandées : conformes. |
| Graphe de l'arbre (point 10) : tous les liens relus | Un défaut de chaînage (G1). |

## 2. Score (§12.2)

| Point | Score | Raison |
|---|---|---|
| 2 Épidémiologie | 2 | Chiffres suisses puis européens, dénominateurs explicités. |
| 3 Physiopathologie | 1 | Contradiction interne sur la température cutanée de la panique (M1). |
| 4 Démarche | 2 | Drapeaux rouges complets, conduite immédiate claire. |
| 7 Syndromes | 1 | Sémiologie inexacte du lymphome, omissions SAOS et symptômes B (M2–M4). |
| 8 Diagnostic positif | 2 | NICE 1.3.1, STRAW+10, ESHRE 2024 exacts. |
| 9 Examens | 2 | Seuils AIPS exacts ; métanéphrines selon Lenders 2020. |
| 10 Arbre | 1 | Retours « puis poursuite » qui court-circuitent grossesse et saignement (G1). |
| 11 Prise en charge | 1 | Posologies suisses hors AIPS de la SGGG n° 99 non reprises (M5). |
| 12 Prévention | 2 | Trois niveaux, vaccination suisse, risque fracturaire SVGO. |
| **Total** | **14/18 = 77,7 %** | Sous le seuil de 90 %. |

## 3. Constats

| Classe | Emplacement | Extrait (≤ 200 car.) | Correction attendue | Source |
|---|---|---|---|---|
| **Grave G1** | Point 10, liens `f4→q7`, `f3→q7`, `f5→q7` (et `f10…f13→q7`) | « Resucrage, adaptation du traitement, puis poursuite » → q7 « Aménorrhée avant 40 ans ? » | Après une hypoglycémie, la patiente saute les nœuds qe8 (saignement post-ménopausique), q6 (test de grossesse), q1 (fièvre/lymphome), q2, q3, q5, q10–q13. Elle peut donc arriver au THM sans exclure grossesse ni saignement (contradiction avec les points 4 E7/E8 et 9.b). Corriger : `f4→qe8`, `f3→q5`, `f5→q10`, `f10→q11`, `f11→q12`, `f12→q13`, `f13→q7`. | AIPS ESTROFEM (saignement inexpliqué : CI) ; AIPS FEMOSTON (« une grossesse doit être exclue ») |
| Moyen M1 | Point 3, tableau de corrélation, ligne « Vasodilatation cutanée » | « les extrémités sont chaudes dans la ménopause, alors qu'elles sont froides et pâles dans le phéochromocytome et la panique » | Le point 4 (DX.2) et le nœud q11 écrivent l'inverse : la température cutanée ne discrimine pas la panique. Retirer « et la panique » ici et en 7.1 et 7.5, ou nuancer partout. | DSM-5 (critère « frissons ou bouffées de chaleur ») |
| Moyen M2 | Point 7.8, signe « Adénopathie » | « Une adénopathie dure, indolore et adhérente évoque un lymphome » | Le ganglion lymphomateux est typiquement ferme, élastique, indolore et mobile. L'adénopathie dure et adhérente évoque une métastase de carcinome. Corriger, car c'est un piège d'examen classique. | Sémiologie universelle (traités de sémiologie) |
| Moyen M3 | Point 7.8, symptômes fonctionnels | « Fièvre … Amaigrissement … elle appartient aux symptômes B » | Donner les seuils de la classification d'Ann Arbor/Lugano : fièvre > 38 °C inexpliquée, sueurs nocturnes profuses, perte > 10 % du poids en 6 mois. | Lugano 2014 (Cheson, J Clin Oncol) |
| Moyen M4 | Point 7.3, symptômes fonctionnels du SAOS | Liste : insomnie, ronflement, somnolence, irritabilité, concentration, humeur | Ajouter les **apnées constatées par l'entourage**, symptôme le plus spécifique, ainsi que la nycturie et les céphalées matinales. | ERS 2023 ; STOP-Bang |
| Moyen M5 | Point 11 B, « Médicaments employés hors indication AIPS » | « Aucune posologie pour les SVM n'est donnée ici … La gabapentine n'est efficace qu'à 900 mg/j » | La règle LOCAL exige la Suisse d'abord. Le tableau 1 de la SGGG n° 99 donne les doses : paroxétine/citalopram/escitalopram 10–20 mg ; venlafaxine 37,5–150 mg ; desvenlafaxine 100–150 mg ; gabapentine 900–2400 mg (début 100–300 mg le soir) ; oxybutynine 5–10 mg. Les reprendre avec l'étiquette « hors AIPS, à valider », avant les essais pivots. Préciser aussi que Loprinzi 2000 et Pandya 2005 portent sur des survivantes d'un cancer du sein. | SGGG n° 99, tableau 1 |
| Léger L1 | Point 11.C, ligne « Examen … des seins » | « L'auto-examen des seins n'a pas montré de bénéfice … » | Signaler que l'AIPS de FEMOSTON demande un auto-examen mensuel : la divergence doit être explicite. | AIPS 53128 |
| Léger L2 | Points 7.1 et 7.3 | « AAFP 2020 ; À vérifier dans une source européenne » | Il s'agit de sémiologie universelle : une source non suisse datée suffit. Retirer « À vérifier » ou citer une source européenne. | Règle de Vial (2) |
| Léger L3 | Point 10, nœud t1 / point 11 | « progestérone micronisée orale à 300 mg/j » | Rappeler la limite AIPS de 200 mg par prise (300 mg en 2 prises). | AIPS UTROGESTAN 45351 |
| Léger L4 | Point 12, en-tête | « une femme sur trois à une sur deux a des SVM modérés à sévères » | Restreindre aux femmes post-ménopausées éligibles de Nappi, comme le fait le point 2. | Nappi 2023 |

Non vérifié (hors temps) : dates d'autorisation Swissmedic (04.12.2023, 05.08.2025), catégories SVGO 2026, exigence SCORE2 attribuée à la SGGG n° 90. Hors périmètre médical : le fichier pèse 409 571 octets, au-dessus de la borne de 200 Ko.

## 4. Question finale

**Un médecin spécialiste universitaire du domaine valide-t-il cette leçon telle quelle ? — Non.**
Il manque : (1) un arbre décisionnel qui ne contourne pas le test de grossesse ni le saignement post-ménopausique (G1) ; (2) une sémiologie exacte du lymphome et du SAOS, avec les seuils des symptômes B (M2–M4) ; (3) la suppression de la contradiction sur la panique (M1) ; (4) les posologies suisses hors AIPS de la SGGG n° 99 (M5). Le contrôle AIPS ne relève aucune erreur de dose ni de contre-indication.

VERDICT: non · critiques 0 · graves 1 · moyens 5
