# RAPPORT D’AUDIT · LOT_003 (24.10.2026)

Périmètre : 10 DX + Appel A (SSP G3 « Soif excessive et polydipsie » et liste du bloc 2). Grille V7 à 14 points ; le point 13.b est HUMAIN, d’où un plafond automatique de 98,8 %.
Avant = rapports/LOT_003_diagnostic.md (phase 0, originaux) ; après = source/eval.sh (decoupe_l → examens → style → score → verif_v7).

| Cours | Score avant | Score après | Examens cliquables / fenêtres à 2 onglets (avant → après) | Phrases > 30 mots (avant → après) | Sigles non développés (avant → après) | Phrases creuses (avant → après) | Probas rouges (après) | Fichier(s) (octets) | Captures |
|---|---|---|---|---|---|---|---|---|---|
| SSP + bloc 2 | 68,8 % | 98,8 % | 6 / 0 → 43 / 43 | 1 → 0 | 14 (+3) → 0 | 0 → 0 | 24 | LOT_003_Appel_A_SSP_G3_Soif_excessive_polydipsie_AUDITÉ_a.html (128 455)<br>…_AUDITÉ_b.html (144 564) | SSP_a_1..3, SSP_b_3 |
| DX.1 | 37,5 % | 98,8 % | 0 / 0 → 52 / 50 | 10 → 0 | 26 → 0 | 2 → 0 | 17 | LOT_003_DX1_Diabete_decompense_AUDITÉ_a.html (104 694)<br>LOT_003_DX1_Diabete_decompense_AUDITÉ_b.html (139 931) | DX1_a_1..3, DX1_b_3 |
| DX.2 | 27,5 % | 98,8 % | 0 / 0 → 24 / 23 | 7 → 0 | 3 → 0 | 0 → 0 | 16 | LOT_003_DX2_Deshydratation_hypernatremique_AUDITÉ.html (148 932) | DX2_1..3 |
| DX.3 | 27,5 % | 98,8 % | 0 / 0 → 20 / 20 | 8 → 0 | 22 → 0 | 0 → 0 | 13 | LOT_003_DX3_Xerostomie_Sjogren_AUDITÉ.html (144 909) | DX3_1..3 |
| DX.4 | 31,2 % | 98,8 % | 0 / 0 → 21 / 21 | 15 → 0 | 12 → 0 | 0 → 0 | 14 | LOT_003_DX4_Polydipsie_primaire_AUDITÉ.html (139 604) | DX4_1..3 |
| DX.5 | 35,0 % | 98,8 % | 0 / 0 → 32 / 32 | 12 → 0 | 7 → 0 | 0 → 0 | 14 | LOT_003_DX5_Polyurie_iatrogene_AUDITÉ.html (162 137) | DX5_1..3 |
| DX.6 | 26,2 % | 98,8 % | 0 / 0 → 36 / 35 | 12 → 0 | 24 → 0 | 0 → 0 | 14 | LOT_003_DX6_Insuffisance_cardiaque_cirrhose_AUDITÉ.html (154 609) | DX6_1..3 |
| DX.7 | 27,5 % | 98,8 % | 0 / 0 → 37 / 36 | 10 → 0 | 22 → 0 | 0 → 0 | 15 | LOT_003_DX7_Hypercalcemie_hypokaliemie_AUDITÉ.html (165 124) | DX7_1..3 |
| DX.8 | 28,8 % | 98,8 % | 0 / 0 → 28 / 28 | 8 → 0 | 21 → 0 | 0 → 0 | 14 | LOT_003_DX8_MRC_polykystose_levee_obstacle_AUDITÉ.html (141 766) | DX8_1..3 |
| DX.9 | 36,2 % | 98,8 % | 0 / 0 → 38 / 37 | 15 → 0 | 18 → 0 | 0 → 0 | 14 | LOT_003_DX9_Deficit_vasopressine_AVP_D_AUDITÉ.html (160 779) | DX9_1..3 |
| DX.10 | 35,0 % | 98,8 % | 0 / 0 → 25 / 25 | 16 → 0 | 9 → 0 | 0 → 0 | 14 | LOT_003_DX10_Resistance_vasopressine_AVP_R_AUDITÉ.html (147 321) | DX10_1..3 |
| **LOT** | **34,7 %** | **98,8 %** | 6 / 0 → 356 / 350 | | | | | 13 fichiers | 35 PNG |

Probabilités dans l’original : aucune balise `proba` ni couleur rouge (0 dans les 7 fichiers originaux).

verif_v7 : OK sur les 13 fichiers (pas de script, img, CSS externe ni `title=` ; FIN_FICHIER ; glossaire des sigles ; mention IA). Toutes les tailles sont entre 90 et 200 Ko ; DX1 et SSP sont découpés en _a/_b (> 198 Ko d’un seul tenant).
Contraste (outils/contraste.py, `.proba` incluse) : 0 élément sur les 13 fichiers. `.proba{color:#C8102E;font-weight:700}`, sans #FF2400 ni halo ; fond bleu ciel pâle appliqué par outils/charte_v7plus.py (pipeline).

Les fenêtres à un seul onglet (DX1 : 2 ; DX2, DX6, DX7, DX9 : 1 chacun) viennent d’un examen de bibliothèque sans texte d’interprétation. L’écart est cosmétique (même situation que LOT_001).

Captures : outils/captures3.py (lecture seule), vues bureau 900 px, dans corriges/LOT_003/captures/ : 1 = « Chaîne logique », 2 = « Diagnostic différentiel » (probabilités rouges), 3 = première fenêtre d’examen du point 9, onglet Interprétation. Pour DX1_b et SSP_b, seule la vue 3 existe (ancres 1 et 2 dans _a).

## Règles appliquées
- Ordre anatomie → physiologie → physiopathologie → clinique → examens → traitement, le pourquoi d’abord ; phrases verbales ≤ 30 mots ; langage courant + terme exact (glossaire).
- Chiffres sourcés, jamais inventés ; prévalences comparables (même unité, même population) ; une répartition d’un autre dénominateur est séparée et nommée comme telle.
- Exposant rouge `sup.proba` sur chaque diagnostic, toujours sourcé ; « non publiée en population générale » quand aucune prévalence fiable n’existe.
- Police Atkinson Hyperlegible ; examens cliquables à 2 onglets (Principe / Interprétation).

## Corrections de fond notables
- **Fenske 2018 (NEJM, PubMed 30067922)** : 144 patients, 11 centres en Suisse, Allemagne et Brésil ; polydipsie primaire 57 % (82), AVP-D 41 % (59), AVP-R 2 % (3) ; précision de la copeptine stimulée 96,5 % contre 76,6 % pour la restriction hydrique. DX9 et DX10 inversaient AVP-D et polydipsie primaire ; DX4 omettait le Brésil. Corrigé dans les trois fichiers et dans la SSP.
- Bloc 2 de l’Appel A aligné sur les 10 monographies de l’Appel B ; l’AVP-D gestationnelle passe en situation particulière.
- DX2, DX3, DX7, DX8, DX9 : point 8 (diagnostic positif) quasi vide dans l’original → critères datés et sourcés ; titres concurrents des points 7 et 11 (DX7, DX8, DX9) résolus.

## Outils (aucune écriture dans outils/ ni bibliotheque_examens/)
- Copies locales dans source/outils_local/ (gen_v7l.py, inserer_l.py, sigles_l.py, sigles_extra.py, decoupe_l.py) ; fragments d’examens supplémentaires dans source/bib_extra/.
- decoupe_l.py : un résumé « SSP G3 · … » est reconnu comme SSP.

## Remarques
- LOT_3_Appel_A_PREAUDIT_MEDICAL_LINGUISTIQUE_r1.html et INDEX_LOT_3.html sont des méta-documents : ils n’ont pas été audités comme cours (le pré-audit a servi de liste de contrôle).
- Les originaux n’ont pas été modifiés.

## Chiffres et doses à vérifier (détail par DX dans PROGRESS.md)
- **SSP** : Minirin® Melt 60–120 µg au coucher puis 2–3 prises/j, comprimés 0,1–0,2 mg 2–3×/j (AIPS) ; amiloride 5–10 mg 1–2×/j (hors AIPS), demi-vie 6–9 h ; NaCl 3 % 150 mL/20 min (ESE 2014) ; Actrapid® 0,1 U/kg/h (JBDS) ; prévalences /100 000 (diabète ≈ 6200, MRC ≈ 10 400, IC 1000–2000, bouche sèche ≈ 22 000, Sjögren ≈ 61, HPT primaire 85–233, AVP-D ≈ 4).
- **DX.1** : seuils du consensus 2024 ACD/EHH ; liquides, insuline 0,1 U/kg/h, potassium ; doses du traitement de fond (metformine, gliflozines, sémaglutide, tirzépatide) ; statut suisse du zimislécel et de l’icodec.
- **DX.2** : données de Berne (Arampatzis 2012) ; Lindner 2007/2009 ; bornes 146–150/151–160/> 160 (repères non consensuels) ; furosémide 20–40 mg IV.
- **DX.3** : Qin 2015 (61/100 000) ; Zintzaras 2005 (RR ≈ 19) ; pilocarpine 5 mg ×3–4 (max 30 mg/j) ; HCQ ≤ 5 mg/kg ; OPAS art. 18 ; NEPTUNUS (sources de congrès 2026).
- **DX.4** : protocole NaCl 3 % (250 mL/15 min puis 0,15 mL/kg/min) ; seuil de poids +2–3 kg (empirique) ; clozapine 200–450 mg/j ; natrémie de grossesse −4–5 mmol/L.
- **DX.5** : EMPA-REG (6,4 % vs 1,8 % ; acidocétose ≈ 0,1 %) ; Carvounis FEUrée < 35 % (Se 90 %, Sp 96 %) ; demi-vies torasémide et tolvaptan ; surveillance hépatique Jinarc®.
- **DX.6** : seuils NT-proBNP ; demi-vies sacubitril/valsartan/bisoprolol ; article OPAS de la réadaptation cardiaque ; autorisation suisse finérénone (FEVG préservée).
- **DX.7** : Zometa® 4 mg, Xgeva® 120 mg, disponibilité de Miacalcic® ; NaCl 200–300 mL/h ; seuil de l’os affamé < 2,1 mmol/L.
- **DX.8** : Jinarc® 45/15 → 90/30 mg ; Pradif® T 0,4 mg ; formulation SSED sur l’albuminurie annuelle.
- **DX.9** : Se/Sp au seuil 4,9 pmol/L (≈ 93 % / 100 %) ; réduction de desmopressine si DFGe < 50 ; hydrocortisone 15–25 mg/j ; essais d’ocytocine 2026.
- **DX.10** : amiloride 5–10 mg 1–2×/j, indométacine 1,5–2 mg/kg/j, HCTZ 25 mg 1–2×/j (hors AIPS) ; lithiémie +25–40 % sous thiazide ; réduction empirique du lithium ; rythme NICE CG185.
