# HELP_DX2 — LOT_016 — DX.2 Épisode dépressif

Lacunes du fichier `LOT_016_Phase_B_V0_DX.2.html` (30.10.2026). Format Prompt V0 §18. Chaque question demande : la recommandation suisse en vigueur (organisme, titre, année, URL), la version la plus récente comparée à celle du cours, les doses AIPS avec numéro Swissmedic, à défaut la source européenne la plus récente, un extrait mot pour mot daté.

## H16-DX2-01 — Mise à jour 2025 des recommandations suisses sur le traitement aigu de la dépression unipolaire
- Identifiant : LOT_016, Phase B, DX.2, points 8, 11.B, 11.C (fenêtres `dx2-p8-severite`, `dx2-p11-ordre`).
- Contexte : le fichier s'appuie sur SGAD/SGBP/SGPP 2016 (Swiss Med Forum 2016;16(35):716–724) et sur le compte rendu ARS MEDICI 2024 de la mise à jour.
- Question : que disent « Die somatische Behandlung der unipolaren depressiven Störungen: Update Teil 1 (2025) » (version courte et longue) sur la sévérité, l'ordre du traitement, les benzodiazépines, la capacité de travail et les interventions nutritionnelles ?
- Déjà cherché : https://www.psychiatrie.ch/sgpp/fachleute-und-kommissionen/behandlungsempfehlungen/ (30.10.2026) : document listé, téléchargement réservé aux membres (« Anmeldung erforderlich »), aucun contournement ; medicalforum.ch inaccessible (erreur 502 du mandataire).
- Emplacement : points 8 et 11 ; source [S4].

## H16-DX2-02 — Seuil de positivité de la GDS (forme courte)
- Identifiant : DX.2, point 4, fenêtre `dx2-p4-outils`.
- Contexte : la SGAP 2018 et la cohorte de Barcelone citent la GDS sans seuil.
- Question : quel seuil de la GDS-15 retient une source suisse (SGAP, Société professionnelle suisse de gériatrie, HUG, CHUV) ou européenne ?
- Déjà cherché : SGAP 2018 (texte intégral) ; fiche du SPF Santé publique belge (HTTP 404, 30.10.2026).
- Emplacement : point 4, fenêtre `dx2-p4-outils`.

## H16-DX2-03 — Sensibilité et spécificité du PHQ-9 et des deux questions de repérage
- Identifiant : DX.2, points 4 et 9.a.
- Contexte : le fichier écrit « donnée non trouvée dans les sources consultées ».
- Question : quelle validation européenne ou suisse (médecine de premier recours) chiffre la sensibilité et la spécificité du PHQ-9 (seuil 10) et du PHQ-2 ?
- Déjà cherché : Obsan (indicateur _065), NICE NG222, SGAD 2016 (30.10.2026).
- Emplacement : point 9.a, fenêtre `dx2-p9-gold`.

## H16-DX2-04 — Coût de la dépression en Suisse
- Identifiant : DX.2, point 2, fenêtre `dx2-p2-histoire`.
- Question : quel coût annuel (CHF) de la dépression publient l'OFSP, l'Obsan ou une étude suisse récente ?
- Déjà cherché : indicateur Obsan « Symptômes de dépression » (texte qualitatif seulement, 30.10.2026).
- Emplacement : point 2.

## H16-DX2-05 — Incapacité de travail dans l'épisode dépressif
- Identifiant : DX.2, point 11.B, fenêtre `dx2-p11-social`.
- Question : quelles règles suisses (SGPP 2025, Swiss Insurance Medicine, assurance-invalidité) guident la durée et la reprise du travail ?
- Déjà cherché : ARS MEDICI 2024 (titre du chapitre seulement) ; LAI art. 3abis–3c (état 1.1.2026).
- Emplacement : point 11.B.

## H16-DX2-06 — Choix de l'antidépresseur chez le patient déprimé dénutri
- Identifiant : DX.2, point 11.B, fenêtre `dx2-p11-pharma`.
- Contexte : le choix (mirtazapine ou sertraline plutôt que fluoxétine, bupropion, venlafaxine) découle des profils AIPS ; aucune recommandation dédiée n'a été trouvée.
- Question : une recommandation suisse ou européenne (SGAP, ESPEN, WFSBP) recommande-t-elle un antidépresseur particulier en cas de perte de poids ou de dénutrition ?
- Déjà cherché : SGAD 2016, SGAP 2018, ESPEN 2022 (R50, R51), NICE NG222 (30.10.2026).
- Emplacement : point 11.B.

## H16-DX2-07 — Imagerie et allergie aux produits de contraste iodés
- Identifiant : DX.2, point 9.c, fenêtre `dx2-p9-alt`.
- Question : quelle conduite d'imagerie cérébrale recommande une source suisse ou européenne en cas d'allergie aux produits de contraste iodés et de contre-indication à l'IRM ?
- Déjà cherché : SGAP 2018 (IRM, sinon scanner).
- Emplacement : point 9.c.

## Réponse proposée pour H16-09 (HELP.md, à reporter par la session principale)
- Valeur 2022 lue dans l'API JSON de l'indicateur Obsan _065 (https://ind.obsan.admin.ch/api/_065/kg/json, mise à jour du 17.01.2025, lue le 30.10.2026) : PHQ-9 ≥ 10 chez 9,8 % (IC 95 % 9,2–10,4 ; n = 18 447) ; femmes 11,7 %, hommes 7,9 % ; 15–34 ans 15,6 % ; 65 ans et plus 4,0 % ; 2017 : 8,6 % ; 2012 : 6,5 %. Extrait : `evidence/DX2_Obsan_OFS_depression_suicide_Suisse.txt`.
