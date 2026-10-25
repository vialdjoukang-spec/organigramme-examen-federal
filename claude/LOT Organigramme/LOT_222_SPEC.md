# LOT_222 — SPEC commune (PROFILES 2023, SSP O6.9 « problems related to work conditions, burnout, unemployment, financial problems »)

## Identité
- LOT_222 = PROFILES 2023, SSP **O6.9 — Conditions de travail, burnout, chômage, difficultés financières** (source : https://smifk-cims.ch/profiles-2023/ssps, consulté 2026-10-21).
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
- Conteneur `<div id="lot222-appel[A|B]-v5" style="font-family: sans-serif; line-height: 1.65; max-width: 980px; margin: auto;">`, h2 bleu #1a5276 bordure #2980b9, sous-titre gris.
- Chaque monographie = `<details open ...>` style du gabarit, `<summary>` « DX.n — Nom <span style="font-size:0.8em;color:#2e8b57;">badge</span> ».
- Grands titres `<p><strong>1. …</strong><br>` ; sous-titres en `<em>` ou `<strong><em>`.
- Fenêtres bio-mathématiques : `<details>` bordure gauche #2980b9 fond #ebf5fb, summary « 🔍 Fenêtre Interactive Bio-Mathématique N.k : … ».
- **CORRECTION** : ne PAS utiliser `<a href="#" title="…">` (inaccessible au toucher, saute en haut de page). Pour un terme interactif, utiliser un `<details>` en ligne :
  `<details class="t" style="display:inline;"><summary style="display:inline;cursor:pointer;color:#1f618d;text-decoration:underline dotted;">terme</summary><span style="display:block;margin:4px 0 8px;padding:8px;background:#f4f6f7;border-left:3px solid #1f618d;font-size:0.93em;">Définition / mécanisme. <em>Source : …</em></span></details>`
- Tableaux : `border="1" cellpadding="7" cellspacing="0" style="width:100%;border-collapse:collapse;..."` thead #d4e6f1 ; envelopper chaque tableau dans `<div style="overflow-x:auto;">` (lecture mobile).
- En fin de fichier : section « Sources » numérotée (titre, organisme, année, URL, date d'accès) et mention : « Contenu produit par IA à partir des sources citées ; non validé cliniquement par un médecin. »

## Fichiers du lot
1. LOT_222_Appel_A_V5_Ultra_Pedagogique_Plan_et_Liste.html — Bloc 1 monographie 14 points du SSP ; Bloc 2 liste DX.1–DX.10 ordonnée + badge + justification.
2. LOT_222_Appel_B_V5_Ultra_Pedagogique_Partie_1_DX.1_a_DX.2.html
3. LOT_222_Appel_B_V5_Ultra_Pedagogique_Partie_2_DX.3_a_DX.5.html
4. LOT_222_Appel_B_V5_Ultra_Pedagogique_Partie_3_DX.6_a_DX.7.html
5. LOT_222_Appel_B_V5_Ultra_Pedagogique_Partie_4_DX.8_a_DX.10.html

## Consigne de Vial (2026-10-21) — plan académique de repli et qualité des différentiels
11. **Plan de repli.** Quand le plan monographique en 14 points ne s'applique pas naturellement à une entité (SSP transversal, procédural, médico-légal, ou entité qui est une classe d'agents plutôt qu'une maladie), ne pas forcer : produire un **plan universitaire/académique** (I., II., III. ; A., B. ; 1., 2.) qui suit la logique propre du sujet, avec **de nombreuses fenêtres cliquables `<details>`** pour les détails (mécanismes, calculs, posologies, cadre légal, exemples). Annoncer en tête de la monographie, en une phrase, pourquoi ce plan est retenu. Les exigences de fond (sources, posologies suisses, bio-mathématique utile, guérison/recherche 2026, pièges d'examen) restent dues ; le lint accepte ce plan si la monographie contient la classe `plan-academique`.
12. **Différentiels de haut niveau.** Chaque DX doit dire ce qui le **distingue des autres DX** et des simulateurs non toxiques :
   - Appel A, Bloc 2 : outre la liste ordonnée, un **tableau comparatif des toxidromes/entités** (conscience, pupilles, FC/PA, FR, température, peau, péristaltisme, ECG, biologie clé, antidote) et un **algorithme discriminant** (quel signe ou examen fait basculer d'un DX à l'autre).
   - Chaque monographie Appel B : rubrique « Diagnostics différentiels discriminants » au point 4 (ou section équivalente), avec les 3–4 confusions les plus dangereuses, le signe ou examen qui tranche, et le piège d'examen associé ; inclure les causes non toxiques qui miment l'intoxication (hypoglycémie, AVC, méningo-encéphalite, état de mal non convulsif, sepsis, hypothermie, traumatisme crânien, troubles métaboliques).
   - Associations et co-ingestions (alcool + benzodiazépines + paracétamol) explicitement traitées : toujours doser paracétamol et éthanol dans l'ingestion volontaire inconnue si la source le soutient.
13. **Fenêtres des thèmes transversaux : très riches et très précises.** Pour tout thème transversal (cadre légal, éthique, communication, organisation des soins, prévention, santé publique, évaluation du risque suicidaire, capacité de discernement, déclaration, Tox Info Suisse, médecine légale), chaque fenêtre `<details>` contient : définition exacte ; base légale ou déontologique précise (article et alinéa via Fedlex, directive ASSM ou code FMH avec année) ; conditions d'application et exceptions ; procédure pas à pas ; exemple clinique concret avec la décision correcte ; erreur fréquente ou piège d'examen ; source datée. Une fenêtre transversale ne se limite jamais à une phrase.











## Spécificités LOT_222
- **Plan (contraignant).** Appel A, Bloc 1 : SSP transversal psychosocial et médico-légal → **plan académique** (I./A./1., classe `plan-academique`), annoncé en une phrase ; il couvre définitions (OMS 2019, CIM-10-GM Z73/Z56/Z59, F43.2), épidémiologie suisse, cadre légal (CO 324a/328/336c, LTr 6/9/15a/17c, OLT 1 43-45, OLT 3 2, LACI 8/15/22/27/28, LAI 3a bis-3c/7d/28, RAI 1quater, LPGA 6-8, LAA 9, LAMal 64a/65, Cst. 12, LP 93, CP 321), évaluation, outils, arbre, protocole A-B-C-D. DX.1–DX.8 : plan monographique en 14 points. DX.9–DX.10 : plan académique autorisé (classe `plan-academique`), exigences de fond inchangées. La SPEC générique (toxidromes, antidotes, co-ingestions) ne s'applique pas : le tableau comparatif de l'Appel A porte sur plainte clé, sphère touchée, durée, outil de dépistage, examen qui tranche, conduite et base légale.
- **10 DX ordonnés (fréquence suisse sourcée pondérée par la gravité).** 1 Épisode dépressif lié au travail, au chômage ou aux dettes (9,8 % de symptômes modérés à sévères, Obsan 2024) ; 2 Burnout sans trouble psychiatrique caractérisé (épuisement émotionnel 25 % F / 19 % H, ESS 2022) ; 3 Trouble de l'adaptation F43.2 (non quantifié) ; 4 Troubles anxieux TAG/panique (6,3 %) ; 5 Crise suicidaire du chômeur ou de la personne endettée (pensées suicidaires 14,4 % / 17,1 % ; avancée par la gravité) ; 6 Trouble lié à l'usage de l'alcool et des calmants (chronique à risque 4,4 % H / 3,4 % F) ; 7 Insomnie chronique et travail de nuit ou posté (non quantifié) ; 8 Simulateurs somatiques : carence martiale, hypothyroïdie, SAOS (IAH ≥ 15/h : 49,7 % H, 23,4 % F à Lausanne) ; 9 Précarité financière et renoncement aux soins (pauvreté 8,4 % ; renoncement 25,8 % à Genève 2025) ; 10 Incapacité prolongée, chômage et réinsertion (LACI, détection précoce AI, maladie professionnelle LAA < 3000 cas/an). La lombalgie chronique est écartée (aucune source lue).
- **Conflits arbitrés (FI suisse d'abord, puis source primaire la plus récente).** Campral® : FI 2023 = 2 cp de 333 mg 3×/j (1998 mg/j), CI si créatinine > 120 µmol/L ; le schéma HUG 2017 selon le poids (2×/j si < 60 kg) n'est PAS repris. Oxazépam dans le sevrage : FI Seresta® 2026 = 15-30 mg 3-4×/j ; le protocole HUG (60-200 mg/j, CIWA ≥ 8 → 15 mg, ≥ 15 → 30 mg, pas si alcoolémie > 2,5 ‰) est présenté comme pratique hospitalière, en fenêtre. Alcool chronique à risque : OFSP 2026 (≥ 2 verres/j F, ≥ 4 H ; repères CFAL 2018 caducs) prime sur HUG 2017 (> 20 g F, > 30 g H). Burnout : CIM-11 = phénomène professionnel, non maladie ; en Suisse, codage CIM-10-GM Z73 (pas de Z73.0 en GM) ou F43.2. Prazépam/alprazolam retard cités par les diapositives HUG : ne pas reprendre (aucune FI lue).
- **Seuils et chiffres clés.** PHQ-9 ≥ 10 (Se 88 %, Sp 88 %) ; PHQ-2 ≥ 3 (Se 83 %, Sp 92 %) ; GAD-7 Se 89 %/Sp 82 % (seuil non lu) ; AUDIT < 7 faible risque, > 7 F / > 8 H excessif, > 13 dépendance ; verre standard 10 g ; ponctuelle à risque ≥ 4 F / ≥ 5 H ; ferritine < 70 µg/L si inflammation (OMS), essai de fer si fatigue et ferritine < 50 µg/L (Vaucher) ; TSH > 10 mU/L traitement < 65-70 ans (ETA 2013) ; Ganzoni = poids × (15 − Hb) × 2,4 + 500 ; escitalopram 10-20 mg (≥ 6 mois ; 5 mg > 65 ans) ; sertraline 50-200 mg ; daridorexant 50 mg (réévaluer à 3 mois) ; zolpidem ≤ 10 mg ≤ 4 semaines, CI SAOS ; TCC-I en première ligne ; hypnotique/anxiolytique ≤ 3-4 semaines dans le burnout ; pas d'antidépresseur sans dépression ; reprise progressive d'abord à 50 % ; CO 336c 30/90/180 jours ; LACI 28 : 30 jours / 44 indemnités ; LACI 22 : 80 %/70 % ; LAI 28 : 40 % sur 1 an ; RAI 1quater : 30 jours ; plan de sécurité NNT 16 ; ASSIP 8,3 % vs 26,7 % ; 143 / 147 ; SECO sept. 2026 : 3,0 % ; seuil de pauvreté 2388 CHF/mois.
- **Lacunes connues (écrire « donnée non trouvée dans les sources consultées »).** Job-Stress-Index (CAPTCHA) ; Hochstrasser 2016 non lu directement ; SGAD 2016 partie 2 ; exigences diagnostiques CIM-11 QD85/6B43 ; seuil de ferritine du sujet sain ; forfait CSIAS 2026 ; recommandations suisses SAOS ; reconnaissance LAA des troubles psychiques ; seuil GAD-7 ; remboursement LS des spécialités ; points vides de evidence.json pour DX.3, DX.4, DX.7–DX.10 (notamment p5-p6 et p10) : rédiger sans inventer, ou signaler la lacune.
