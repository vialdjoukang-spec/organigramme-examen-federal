# LOT_002 — Rapport d’audit (G2 · Tuméfaction, masse et adénopathie)
Run du 24.10.2026 (Europe/Zurich). Originaux : `originaux/LOT_002/` (V7 AUDIT_CORRIGE r2, jamais modifiés). Méthode : un générateur par cours (`source/gen_*.py`, base commune `source/lot2_commun.py` qui importe `outils/gen_v7.py`) ; outils locaux dans `source/outils_local/` (fenêtres + bib_extra, glossaire de sigles étendu) ; fragments propres au LOT dans `source/bib_extra/` (calcitonine, Monotest, p16, MDM2, surcharge reformulée de « sero »). Aucun fichier partagé de `outils/` ni de `bibliotheque_examens/` n’a été modifié. Local uniquement : aucune écriture Drive, aucun push.
Reconstruction complète : `bash source/rebuild_all.sh`.

## Métriques avant → après (proxy `outils/score.py`, `examens.py`, `style.py`)
« Avant » = `work/LOT_002/` (originaux r2) ; « après » = `work/LOT_002_AUDITE/`. Score maximal atteignable par le proxy : 98,8 % (critère 13.b HUMAIN plafonné à 1/2).
| Cours | Score V7 (proxy) | Mentions d’examen | Examens cliquables | Fenêtres 2 onglets | Phrases creuses | Phrases > 30 mots | Sigles non développés | Probabilités rouges |
|---|---|---|---|---|---|---|---|---|
| SSP | 72.5 → 98.8 % | 43 → 369 | 0 → 36 | 0 → 36 | 0 → 0 | 0 → 0 | 20 → 4 | 0 → 9 |
| DX.1 | 40.0 → 98.8 % | 6 → 371 | 0 → 38 | 0 → 38 | 1 → 0 | 0 → 0 | 2 → 2 | 0 → 10 |
| DX.2 | 40.0 → 98.8 % | 3 → 341 | 0 → 37 | 0 → 37 | 0 → 0 | 1 → 0 | 3 → 2 | 0 → 9 |
| DX.3 | 32.5 → 98.8 % | 14 → 304 | 0 → 30 | 0 → 30 | 0 → 0 | 0 → 0 | 5 → 1 | 0 → 7 |
| DX.4 | 35.0 → 98.8 % | 0 → 524 | 0 → 49 | 0 → 49 | 0 → 0 | 0 → 0 | 2 → 3 | 0 → 7 |
| DX.5 | 36.2 → 98.8 % | 18 → 386 | 0 → 36 | 0 → 36 | 2 → 0 | 1 → 0 | 2 → 1 | 0 → 7 |
| DX.6 | 41.2 → 98.8 % | 20 → 502 | 1 → 48 | 0 → 48 | 0 → 0 | 0 → 0 | 5 → 2 | 0 → 7 |
| DX.7 | 30.0 → 98.8 % | 14 → 419 | 0 → 33 | 0 → 33 | 1 → 0 | 1 → 0 | 2 → 4 | 0 → 7 |
| DX.8 | 26.2 → 98.8 % | 4 → 240 | 0 → 22 | 0 → 22 | 0 → 0 | 0 → 0 | 2 → 0 | 0 → 7 |
| DX.9 | 37.5 → 98.8 % | 7 → 303 | 0 → 26 | 0 → 26 | 0 → 0 | 0 → 0 | 0 → 1 | 0 → 6 |
| DX.10 | 28.8 → 98.8 % | 22 → 696 | 0 → 51 | 0 → 51 | 0 → 0 | 1 → 0 | 4 → 1 | 0 → 6 |
| **LOT** | 38.2 → 98.8 % | 161 → 4455 | 1 → 406 | 0 → 406 | | | | 0 → 82 |

| Fichier | Octets |
|---|---|
| LOT_002_AppelA_SSP_Tumefaction_masse_adenopathie_AUDITÉ.html | 130092 |
| LOT_002_DX1_Adenopathie_reactionnelle_AUDITÉ.html | 130668 |
| LOT_002_DX2_Lymphadenite_bacterienne_AUDITÉ.html | 117030 |
| LOT_002_DX3_Mononucleose_infectieuse_EBV_AUDITÉ.html | 123127 |
| LOT_002_DX4_VIH_revele_par_adenopathies_AUDITÉ.html | 130495 |
| LOT_002_DX5_Tuberculose_ganglionnaire_AUDITÉ.html | 108107 |
| LOT_002_DX6_Lymphome_hodgkinien_ou_non_hodgkinien_AUDITÉ.html | 135212 |
| LOT_002_DX7_Metastase_ganglionnaire_carcinome_AUDITÉ.html | 119653 |
| LOT_002_DX8_Lipome_superficiel_AUDITÉ.html | 90701 |
| LOT_002_DX9_Sarcome_des_tissus_mous_AUDITÉ.html | 92296 |
| LOT_002_DX10_Nodule_ou_masse_thyroidienne_AUDITÉ.html | 146795 |


Contrôles `verif_v7.py` : 11/11 fichiers OK (police Atkinson Hyperlegible, aucun script/img/CSS externe/`title=`, tableaux enveloppés, marqueur FIN_FICHIER, glossaire, 90–200 Ko, mention « contenu produit par IA, non validé cliniquement »). Aucun fichier > 200 Ko : pas de découpage _a/_b.

Sigles « non développés » résiduels (premier emploi détecté par style.py) : surtout des faux positifs de fragments partagés ou de noms propres — TB (dans « T-SPOT.TB »), VIH/AIDS/ECG/OMS/EBV/NICE au premier emploi dans une fenêtre d’examen partagée, PD (PD-L1), CO (CO-AMOXI®), TIRADS (EU-TIRADS, développé dans le glossaire). Tous figurent dans le glossaire du fichier.

Appel A : le fichier AUDITÉ est noté via une copie de travail `source/ssp_score/LOT_2_Appel_A_V7_Plan_et_Liste_AUDIT_CORRIGE_score.html` (decoupe.py ne reconnaît l’Appel A que par son nom) ; cette copie n’est pas un livrable. Le Bloc 2 (dix hypothèses) est intégré en fin de l’Appel A.

## Captures (3 par cours)
`corriges/LOT_002/captures/` : SSP_1..3.png, DX1_1..3.png … DX10_1..3.png (33 images).

## Chiffres à faire vérifier par un médecin
- **SSP** : malignité 1,1 % en premier recours, ≈ 4 % > 40 ans (Fijten 1988), sus-claviculaire 34–50 % (Ferrer) ; seuils 1 / 1,5 / 0,5 cm ; NICE NG12 ≥ 45 ans ; « biopsie avant 2 semaines si drapeau rouge » = délai d’audit non sourcé ; incidences NKRS (LNH ≈ 1700, sarcome ≈ 340, thyroïde ≈ 850 par an).
- **DX.1** : malignité 1,1 % ; 0,4 %/4 % selon l’âge ; sus-claviculaire 34–50 % ; observation 3–4 semaines ; Dafalgan 500–1000 mg toutes les 4–8 h, max 4 g ; ClCr 10–50 → ≥ 6 h et 3 g ; < 10 → ≥ 8 h et 2 g ; 197 mg de sodium par comprimé effervescent.
- **DX.2** : co-amoxiclav 625 mg ×3 ou 1 g ×2 pendant 7–10 j ; IV 2,2 g ×3 ; clindamycine 300–450 mg ×3–4 ; azithromycine 500 mg puis 250 mg J2–J5 ; qSOFA / Sepsis-3.
- **DX.3** : RV d’Ebell 2016 (adénopathie postérieure 3,1 ; pétéchies palatines 5,3 ; splénomégalie 1,9–6,6 ; lymphocytes atypiques ≥ 10 % 11, ≥ 40 % 50 ; lymphocytes ≥ 50 % + ≥ 10 % atypiques 54) ; Monotest Se 87 % / Spé 91 % ; EBV ≈ 90 % des mononucléoses ; VIH aigu ≈ 1 % ; 77 % symptomatiques (Balfour) ; rupture de rate 0,1–0,5 % ; pause sportive ≥ 3–4 semaines ; éruption à l’amoxicilline ≈ 30 % ; prednisone 40–60 mg.
- **DX.4** : 318 cas / 3,5 pour 100 000 (2024), 357 en 2023 ; fenêtre de 6 semaines ; CD4 < 200 ou < 14 % ; conditions Biktarvy/Dovato ; cotrimoxazole ; PEP dans les 72 h pendant 28 j ; DTG 50 mg ×2 avec rifampicine.
- **DX.5** : 432 cas / 4,8 (2024), 544 / 6,0 (2025), 22 % extrapulmonaires, Europe 8,4 ; doses HRZE ; réaction paradoxale ≈ 20 % ; seuils ALAT 3× / 5× ; IDR 10 mm.
- **DX.6** : 1700 LNH / 290 Hodgkin par an ; DLBCL ≈ un tiers des LNH ; guérison > 80 % (Hodgkin), 60–70 % (DLBCL) ; R-CHOP (R 375, C 750, H 50 mg/m², O 1,4 mg/m² max 2 mg, P 100 mg J1–5) ; allopurinol 300 mg ; IPI ; LDH < 250 ; masse volumineuse ≥ 10 cm.
- **DX.7** : 1200 cancers bouche/pharynx et 260 larynx par an ; CUP 1–2 % (ESMO 2023) ; cisplatine 100 mg/m² J1/J22/J43 ou 40 mg/m² hebdomadaire ; cétuximab 400 puis 250 mg/m² ; pembrolizumab 200 / 400 mg ; ondansétron 8 mg ; vaccination HPV 11–14 ans, rattrapage jusqu’à 26 ans ; NICE ≥ 45 ans ; échographie petit axe < 10 mm « rassurant » (repère d’audit).
- **DX.8** : lipomes = 16 % des tumeurs bénignes des tissus mous (Kransdorf 1995) ; rapport bénin/sarcome ≈ 100 pour 1 (ordre de grandeur, source non vérifiée) ; seuil 5 cm, septa < 2 mm ; âge 40–60 ans ; lidocaïne max ≈ 4,5 mg/kg (300 mg) sans adrénaline, ≈ 7 mg/kg (500 mg) avec, demi-vie 1,5–2 h ; ibuprofène 400 mg ×3.
- **DX.9** : ≈ 340 cas / ≈ 4 pour 100 000 (NKRS) ; Europe 4–5 / 100 000 ; ≈ 1 % des cancers de l’adulte ; grade FNCLCC (mitoses 0–9 / 10–19 / ≥ 20 pour 10 champs ; nécrose 0 / < 50 % / ≥ 50 % ; grades 2–3 / 4–5 / 6–8) ; doxorubicine 75 mg/m² toutes les 3 semaines, 6 cycles, dose cumulée ≈ 450–550 mg/m² ; ifosfamide ≈ 9–10 g/m² par cycle ; marge ≥ 1 cm ; surveillance IRM/scanner tous les 3–6 mois.
- **DX.10** : ≈ 850 cas / ≈ 9 pour 100 000 ; nodules palpables 4–7 %, échographiques 19–68 %, malignité 7–15 % (ATA 2015) ; EU-TIRADS 2017 (risques ≈ 0 / 2–4 / 6–17 / 26–87 % ; seuils de cytoponction > 20 / > 15 / > 10 mm) ; Bethesda 2023 (risque moyen I 13 %, II 4 %, III 22 %, IV 30 %, V 74 %, VI 97 %) ; calcitonine > 100 pg/mL ; TSH 0,4–4,0 mU/L ; lévothyroxine ≈ 1,6 µg/kg/j, demi-vie ≈ 7 j ; carbimazole 15–40 puis 5–15 mg/j ; croissance > 20 % sur deux dimensions ; arrêt de travail 1–3 semaines après thyroïdectomie.

## Statut
LOT_002 : **terminé** (Appel A + DX.1 à DX.10, 11 fichiers AUDITÉS). MANIFEST.sha256 écrit.
