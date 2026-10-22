# LOT_225 — SPEC commune (PROFILES 2023, SSP O7.3 « dietary counselling including a healthy and sustainable nutrition »)

## Identité
- LOT_225 = PROFILES 2023, SSP **O7.3 — Conseil diététique, alimentation saine et durable** (source : https://smifk-cims.ch/profiles-2023/ssps, consulté 2026-10-21).
- Public : candidats à l'examen fédéral suisse de médecine humaine (MEBEKO/OFSP). Niveau : futur médecin assistant.

## Règles de fond (non négociables)
1. Aucune affirmation de mémoire : chaque chiffre, seuil, posologie, critère vient du dossier de preuves `evidence.json` (ou d'une source lue et ajoutée avec URL + date d'accès). Sinon écrire « donnée suisse non trouvée » — ne jamais inventer.
2. Hiérarchie : Suisse (Tox Info Suisse, Swissmedic/AIPS information professionnelle, compendium.ch, OFSP, OFS, sociétés suisses, ASSM, Fedlex) → Europe (ERC, EAPCCT, ESC, EASL, KDIGO, EMA) → international accepté en Suisse. Pas de recommandation exclusivement américaine (une position conjointe EAPCCT/AACT est acceptable).
3. Médicaments : DCI + spécialité suisse ® réellement autorisée (vérifier AIPS/compendium) + posologie selon l'information professionnelle suisse ou protocole Tox Info Suisse. Si non commercialisé en Suisse : le dire (importation, pharmacie hospitalière, dépôt d'antidotes).
4. Badges de fréquence : % seulement si sourcé (ex. rapport annuel Tox Info Suisse) ; sinon rang ordinal + « fréquence non quantifiée (Suisse) ».
5. Chaque phrase du corps comporte un verbe conjugué. Français professionnel, élégant, sans métaphores ni remplissage. Normal avant pathologique. Exemples chiffrés.
6. Toute abréviation développée à sa première apparition dans chaque fichier.
7. Bio-mathématique uniquement quand la clinique l'exige (trou anionique, trou osmolaire, nomogramme paracétamol, COHb, QTc, etc.) : fenêtre <details> avec variables + unités SI, équation, exemple résolu pas à pas, tableau d'interprétation (Normal / Seuil / Signification / Conduite). Les calculs doivent être exacts.
8. 14 points obligatoires par monographie ; point 11 en A-But / B-Moyens (non médicamenteux ; pharmacologiques : classe, DCI + mécanisme, spécialité suisse ®, posologie/voie/rythme + adaptation rénale/hépatique, durée) / C-Surveillance (clinique, biologique avec calendrier et seuils, radiologique) / D-Pronostic, critères de guérison ou recherche 2026.
9. Point 7 : syndromes numérotés 7.1, 7.2… ; chaque titre de syndrome ouvre une fenêtre reliant chaque signe à son mécanisme.
10. Point 9 : Gold standard (Se/Sp, seuil) → 1re intention (+ alternatives grossesse, DFGe < 30 mL/min, allergie au contraste, enfant) → 2e intention.

## Gabarit HTML (fidèle au méta-prompt, avec une correction)
- Fichier HTML5 complet autonome (<!DOCTYPE html>, <meta charset="UTF-8">, <meta name="viewport" content="width=device-width,initial-scale=1">).
- Conteneur `<div id="lot225-appel[A|B]-v5" style="font-family: sans-serif; line-height: 1.65; max-width: 980px; margin: auto;">`, h2 bleu #1a5276 bordure #2980b9, sous-titre gris.
- Chaque monographie = `<details open ...>` style du gabarit, `<summary>` « DX.n — Nom <span style="font-size:0.8em;color:#2e8b57;">badge</span> ».
- Grands titres `<p><strong>1. …</strong><br>` ; sous-titres en `<em>` ou `<strong><em>`.
- Fenêtres bio-mathématiques : `<details>` bordure gauche #2980b9 fond #ebf5fb, summary « 🔍 Fenêtre Interactive Bio-Mathématique N.k : … ».
- **CORRECTION** : ne PAS utiliser `<a href="#" title="…">` (inaccessible au toucher, saute en haut de page). Pour un terme interactif, utiliser un `<details>` en ligne :
  `<details class="t" style="display:inline;"><summary style="display:inline;cursor:pointer;color:#1f618d;text-decoration:underline dotted;">terme</summary><span style="display:block;margin:4px 0 8px;padding:8px;background:#f4f6f7;border-left:3px solid #1f618d;font-size:0.93em;">Définition / mécanisme. <em>Source : …</em></span></details>`
- Tableaux : `border="1" cellpadding="7" cellspacing="0" style="width:100%;border-collapse:collapse;..."` thead #d4e6f1 ; envelopper chaque tableau dans `<div style="overflow-x:auto;">` (lecture mobile).
- En fin de fichier : section « Sources » numérotée (titre, organisme, année, URL, date d'accès) et mention : « Contenu produit par IA à partir des sources citées ; non validé cliniquement par un médecin. »

## Fichiers du lot
1. LOT_225_Appel_A_V5_Ultra_Pedagogique_Plan_et_Liste.html — Bloc 1 monographie 14 points du SSP ; Bloc 2 liste DX.1–DX.10 ordonnée + badge + justification.
2. LOT_225_Appel_B_V5_Ultra_Pedagogique_Partie_1_DX.1_a_DX.2.html
3. LOT_225_Appel_B_V5_Ultra_Pedagogique_Partie_2_DX.3_a_DX.5.html
4. LOT_225_Appel_B_V5_Ultra_Pedagogique_Partie_3_DX.6_a_DX.7.html
5. LOT_225_Appel_B_V5_Ultra_Pedagogique_Partie_4_DX.8_a_DX.10.html

## Consigne de Vial (2026-10-21) — plan académique de repli et qualité des différentiels
11. **Plan de repli.** Quand le plan monographique en 14 points ne s'applique pas naturellement à une entité (SSP transversal, procédural, médico-légal, ou entité qui est une classe d'agents plutôt qu'une maladie), ne pas forcer : produire un **plan universitaire/académique** (I., II., III. ; A., B. ; 1., 2.) qui suit la logique propre du sujet, avec **de nombreuses fenêtres cliquables `<details>`** pour les détails (mécanismes, calculs, posologies, cadre légal, exemples). Annoncer en tête de la monographie, en une phrase, pourquoi ce plan est retenu. Les exigences de fond (sources, posologies suisses, bio-mathématique utile, guérison/recherche 2026, pièges d'examen) restent dues ; le lint accepte ce plan si la monographie contient la classe `plan-academique`.
12. **Différentiels de haut niveau.** Chaque DX doit dire ce qui le **distingue des autres DX** et des simulateurs non toxiques :
   - Appel A, Bloc 2 : outre la liste ordonnée, un **tableau comparatif des toxidromes/entités** (conscience, pupilles, FC/PA, FR, température, peau, péristaltisme, ECG, biologie clé, antidote) et un **algorithme discriminant** (quel signe ou examen fait basculer d'un DX à l'autre).
   - Chaque monographie Appel B : rubrique « Diagnostics différentiels discriminants » au point 4 (ou section équivalente), avec les 3–4 confusions les plus dangereuses, le signe ou examen qui tranche, et le piège d'examen associé ; inclure les causes non toxiques qui miment l'intoxication (hypoglycémie, AVC, méningo-encéphalite, état de mal non convulsif, sepsis, hypothermie, traumatisme crânien, troubles métaboliques).
   - Associations et co-ingestions (alcool + benzodiazépines + paracétamol) explicitement traitées : toujours doser paracétamol et éthanol dans l'ingestion volontaire inconnue si la source le soutient.
13. **Fenêtres des thèmes transversaux : très riches et très précises.** Pour tout thème transversal (cadre légal, éthique, communication, organisation des soins, prévention, santé publique, évaluation du risque suicidaire, capacité de discernement, déclaration, Tox Info Suisse, médecine légale), chaque fenêtre `<details>` contient : définition exacte ; base légale ou déontologique précise (article et alinéa via Fedlex, directive ASSM ou code FMH avec année) ; conditions d'application et exceptions ; procédure pas à pas ; exemple clinique concret avec la décision correcte ; erreur fréquente ou piège d'examen ; source datée. Une fenêtre transversale ne se limite jamais à une phrase.











## Spécificités LOT_225
*Arbitrages contraignants (agent de recherche, 22.10.2026 ; preuves dans `evidence.json`, 75 sources S1–S75).*

**A. Plan.** SSP transversal et préventif : la monographie SSP de l'Appel A suit un **plan académique** (I./A./1., classe `plan-academique`), annoncé en une phrase (la transposition CanMEDS « cadre légal en point 3, posologies » sonne faux pour un conseil nutritionnel). Plan suggéré : I. Définir l'alimentation saine et durable (pyramide 2024, assiette) ; II. Situation suisse (ESS 2022, menuCH, sel 2022–2023, OFEV) ; III. Cadre légal et assurance (OPAS 9b/9c, LS des GLP-1, CC 16/426/434) ; IV. Démarche de conseil (évaluation, IMC/tour de taille, NRS 2002/GLIM, groupes à besoins particuliers, compléments) ; V. Durabilité ; VI. Points clés et pièges. Les 10 DX sont des **situations cliniques** et reçoivent le **plan clinique en 14 points** (11.A–D complets) ; pas de physiopathologie plaquée au-delà de ce qu'apporte `evidence.json`.

**B. Les 10 DX (ordre = fréquence suisse sourcée pondérée par la gravité) :**
1. DX.1 Surpoids et obésité de l'adulte — badge 43,0 % (30,9 % + 12,1 %), ESS 2022 [S6].
2. DX.2 HTA et apport sodé excessif — 19,5 % d'HTA déclarée [S8] ; 24 % mesurée, sel 8,7 g/j [S11].
3. DX.3 Dénutrition hospitalière et gériatrique (NRS 2002, GLIM, renutrition) — 18,2 % NRS ≥ 3 à l'admission [S47] ; avancée par la gravité (EFFORT : décès à 30 j 7 % vs 10 %) [S49].
4. DX.4 Prédiabète et diabète de type 2 (prévention, rémission) — 6,2 % [S9].
5. DX.5 Dyslipidémie et prévention cardiovasculaire — « 5e rang — fréquence non quantifiée (Suisse) ».
6. DX.6 MASLD/MASH — « 6e rang — fréquence non quantifiée (Suisse) ».
7. DX.7 Périconception, grossesse, allaitement — rang, apport en iode insuffisant [S15].
8. DX.8 Nourrisson et jeune enfant (diversification, vitamines D/K, obésité infantile) — 16,7 % (source secondaire, le signaler) [S73].
9. DX.9 Alimentation végétarienne/végétalienne et carence en B12 — ≈ 1 sur 20 [S26].
10. DX.10 TCA, surtout anorexie mentale — 1,2 % des femmes vie entière [S56] ; SMR 5,86 [S57].
Non retenus (citer en différentiel/fenêtre) : maladie rénale chronique, goutte, maladie cœliaque et allergies (LOT_229), ostéoporose, carence martiale.

**C. Tableau comparatif et algorithme (Appel A, Bloc 2).** Colonnes adaptées au sujet (pas de toxidromes) : groupe/âge, signe d'appel, mesure clé (IMC, tour de taille, PA, natriurèse, HbA1c, LDL-C, FIB-4/élastographie, NRS 2002/GLIM, iodurie, holoTC/AMM, IMC < 15), mécanisme, conseil immédiat, remboursement (OPAS 9b/9c, LS). Algorithme : perte de poids involontaire → DX.3/DX.10 avant tout régime ; IMC bas + peur de grossir → DX.10 ; grossesse/projet → DX.7 ; < 3 ans → DX.8 ; régime d'exclusion → DX.9 ; sinon facteurs cardiométaboliques → DX.1/2/4/5/6.

**D. Conflits de sources et règles de citation (IP suisse d'abord, puis Europe).**
- Sel : cible OMS < 5 g/j reprise par l'OSAV ; ESC 2024 : sodium ≈ 2 g/j ou moins (≈ 5 g de sel, *calcul dérivé*) ; potassium +0,5–1 g/j seulement si sodium > 5 g/j et sans IRC modérée à avancée ; pyramide 2024 : « limiter le sel, sel iodé ».
- Vitamine D du senior : 800 UI dès 60 ans (CFN 2012 [S18], OSAV [S19]) vs « dès 65 ans » (page seniors [S20]) → fenêtre avec les deux.
- Konakion® : IP [S43] (naissance, J4–7, S4–6 si allaité) en premier ; schéma H4/J4/S4 (Laubscher 2026 [S75]) en fenêtre.
- Grossesse : 3–4 portions de produits laitiers (OSAV 2018 [S16]) ≠ 2–3 (pyramide adulte) ; Elevit® Pronatal **sans iode** [S42] ; AndreaFol® 0,4 mg = prévention primaire, 4–5 mg (Acidum folicum Streuli® 5 mg) = prévention secondaire [S40, S41].
- Prise de poids gravidique : repères IOM repris par la CFN (présenter comme position CFN, non comme recommandation américaine).
- GLP-1 : indication Swissmedic (IMC ≥ 30, ou ≥ 27 + comorbidité) ≠ remboursement LS (IMC ≥ 35, ou ≥ 28 + prédiabète/DT2, HTA, dyslipidémie ; déficit 500 kcal/j documenté ; arrêt si < 5 %/< 7 % à 16 semaines, < 10 %/< 12 % à 10 mois ; prescription en centre ; max 3 ans) [S31–S35].
- B12 du nourrisson végétalien : COFA 2018 (0,4 puis 0,8 µg/j) vs guide 2020 (2 × 1 µg ou 5 µg/j, absence de consensus) → fenêtre.
- PREDIMED : citer exclusivement la version republiée 2018 (HR 0,69 et 0,72).

**E. Seuils clés à reprendre exactement.** IMC 25/30/35 ; tour de taille 94/80 et 102/88 cm ; HTA ≥ 140/90, PA élevée 120–139/70–89, cible PAS 120–129 ; sel 8,7 g/j (F 7,4 ; H 9,9), < 5 g chez 14 % ; diabète HbA1c ≥ 6,5 % (48 mmol/mol), GAJ ≥ 7,0, HGPO 2 h ≥ 11,1 ; prédiabète OMS 6,0–6,4 % / 6,1–6,9 mmol/L ; LDL-C < 1,4/1,8/2,6/3,0 mmol/L ; graisses saturées < 10 % (< 7 % si hypercholestérolémie), fibres 25–40 g, phytostérols 2 g (−7 à −10 %) ; MASLD perte ≥ 5/7–10/≥ 10 % ; NRS 2002 ≥ 3 ; GLIM perte > 5 % (6 mois)/> 10 %, IMC < 20 (< 70 ans)/< 22 (≥ 70 ans) ; sujet âgé 30 kcal/kg, protéines ≥ 1,0 g/kg (brochure suisse 1,0–1,2), CNO ≥ 400 kcal et ≥ 30 g de protéines, boissons ≥ 1,6 L (F)/≥ 2,0 L (H) ; acide folique 400 µg dès le projet jusqu'à ≥ 12 SA ; iode 250 µg/j pendant l'allaitement, sel iodé 25 mg/kg ; vitamine D 400 UI (0–12 mois), 600 UI (1–59 ans, grossesse), 800 UI (≥ 60 ans) ; Vi-De 3® 1 goutte = 100 UI ; Vitarubine® Oral 1000 µg 1–2 cp/j ; EFFORT 23 % vs 27 % (OR 0,79), décès 7 % vs 10 % (OR 0,65) ; DiRECT rémission 46 % (86 % si ≥ 15 kg) ; anorexie : hospitalisation si IMC < 15 ou perte > 20 %/6 mois, reprise 0,5–1 kg/semaine (hospitalier), 0,2–0,5 (ambulatoire). OPAS 9b : 6 séances par prescription, médecin-conseil après 12 ; OPAS 9c : 10 séances.

**F. Lacunes connues (écrire « donnée non trouvée dans les sources consultées » ; envoyer dans HELP après audit).** Prévalence suisse de la dyslipidémie et de la MASLD ; seuils FIB-4 (figure EASL non lue) ; tableau 8 de l'ESC 2021 (valeurs alimentaires chiffrées) ; classes/niveaux ESC 2024 du mode de vie ; monitorage IMC 2025 primaire (captcha) ; algorithme chiffré de Friedli 2018 (résumé seul) ; OPAS annexe 1 (bariatrique : seuils via CHUV seulement) ; article OLT 1 sur l'allaitement ; seuils adultes holoTC/AMM ; textes EAT-Lancet 2019/2025 ; guides de poche GSLA. Résumés seulement : EFFORT, NRS 2002, DiRECT, DPS, PREDIMED, He 2013, Rees 2013, DNSG 2023, SSED 2023, Mohler-Kuo, Arcelus — à marquer « (résumé) » dans les sources.
