# LOT_217 — SPEC commune (PROFILES 2023, SSP O6.4 « harassment, bullying, mobbing »)

## Identité
- LOT_217 = PROFILES 2023, SSP **O6.4 — Harcèlement, mobbing** (source : https://smifk-cims.ch/profiles-2023/ssps, consulté 2026-10-21).
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
- Conteneur `<div id="lot217-appel[A|B]-v5" style="font-family: sans-serif; line-height: 1.65; max-width: 980px; margin: auto;">`, h2 bleu #1a5276 bordure #2980b9, sous-titre gris.
- Chaque monographie = `<details open ...>` style du gabarit, `<summary>` « DX.n — Nom <span style="font-size:0.8em;color:#2e8b57;">badge</span> ».
- Grands titres `<p><strong>1. …</strong><br>` ; sous-titres en `<em>` ou `<strong><em>`.
- Fenêtres bio-mathématiques : `<details>` bordure gauche #2980b9 fond #ebf5fb, summary « 🔍 Fenêtre Interactive Bio-Mathématique N.k : … ».
- **CORRECTION** : ne PAS utiliser `<a href="#" title="…">` (inaccessible au toucher, saute en haut de page). Pour un terme interactif, utiliser un `<details>` en ligne :
  `<details class="t" style="display:inline;"><summary style="display:inline;cursor:pointer;color:#1f618d;text-decoration:underline dotted;">terme</summary><span style="display:block;margin:4px 0 8px;padding:8px;background:#f4f6f7;border-left:3px solid #1f618d;font-size:0.93em;">Définition / mécanisme. <em>Source : …</em></span></details>`
- Tableaux : `border="1" cellpadding="7" cellspacing="0" style="width:100%;border-collapse:collapse;..."` thead #d4e6f1 ; envelopper chaque tableau dans `<div style="overflow-x:auto;">` (lecture mobile).
- En fin de fichier : section « Sources » numérotée (titre, organisme, année, URL, date d'accès) et mention : « Contenu produit par IA à partir des sources citées ; non validé cliniquement par un médecin. »

## Fichiers du lot
1. LOT_217_Appel_A_V5_Ultra_Pedagogique_Plan_et_Liste.html — Bloc 1 monographie 14 points du SSP ; Bloc 2 liste DX.1–DX.10 ordonnée + badge + justification.
2. LOT_217_Appel_B_V5_Ultra_Pedagogique_Partie_1_DX.1_a_DX.2.html
3. LOT_217_Appel_B_V5_Ultra_Pedagogique_Partie_2_DX.3_a_DX.5.html
4. LOT_217_Appel_B_V5_Ultra_Pedagogique_Partie_3_DX.6_a_DX.7.html
5. LOT_217_Appel_B_V5_Ultra_Pedagogique_Partie_4_DX.8_a_DX.10.html

## Consigne de Vial (2026-10-21) — plan académique de repli et qualité des différentiels
11. **Plan de repli.** Quand le plan monographique en 14 points ne s'applique pas naturellement à une entité (SSP transversal, procédural, médico-légal, ou entité qui est une classe d'agents plutôt qu'une maladie), ne pas forcer : produire un **plan universitaire/académique** (I., II., III. ; A., B. ; 1., 2.) qui suit la logique propre du sujet, avec **de nombreuses fenêtres cliquables `<details>`** pour les détails (mécanismes, calculs, posologies, cadre légal, exemples). Annoncer en tête de la monographie, en une phrase, pourquoi ce plan est retenu. Les exigences de fond (sources, posologies suisses, bio-mathématique utile, guérison/recherche 2026, pièges d'examen) restent dues ; le lint accepte ce plan si la monographie contient la classe `plan-academique`.
12. **Différentiels de haut niveau.** Chaque DX doit dire ce qui le **distingue des autres DX** et des simulateurs non toxiques :
   - Appel A, Bloc 2 : outre la liste ordonnée, un **tableau comparatif des toxidromes/entités** (conscience, pupilles, FC/PA, FR, température, peau, péristaltisme, ECG, biologie clé, antidote) et un **algorithme discriminant** (quel signe ou examen fait basculer d'un DX à l'autre).
   - Chaque monographie Appel B : rubrique « Diagnostics différentiels discriminants » au point 4 (ou section équivalente), avec les 3–4 confusions les plus dangereuses, le signe ou examen qui tranche, et le piège d'examen associé ; inclure les causes non toxiques qui miment l'intoxication (hypoglycémie, AVC, méningo-encéphalite, état de mal non convulsif, sepsis, hypothermie, traumatisme crânien, troubles métaboliques).
   - Associations et co-ingestions (alcool + benzodiazépines + paracétamol) explicitement traitées : toujours doser paracétamol et éthanol dans l'ingestion volontaire inconnue si la source le soutient.
13. **Fenêtres des thèmes transversaux : très riches et très précises.** Pour tout thème transversal (cadre légal, éthique, communication, organisation des soins, prévention, santé publique, évaluation du risque suicidaire, capacité de discernement, déclaration, Tox Info Suisse, médecine légale), chaque fenêtre `<details>` contient : définition exacte ; base légale ou déontologique précise (article et alinéa via Fedlex, directive ASSM ou code FMH avec année) ; conditions d'application et exceptions ; procédure pas à pas ; exemple clinique concret avec la décision correcte ; erreur fréquente ou piège d'examen ; source datée. Une fenêtre transversale ne se limite jamais à une phrase.











## Spécificités LOT_217
Arbitrages contraignants (agent de recherche, 22.10.2026 ; preuves dans `evidence.json`, sources S1–S59).

### A. Liste ordonnée des 10 DX (fréquence suisse sourcée pondérée par la gravité ; annoncer ce critère)
1. **DX.1 — Mobbing (harcèlement psychologique) au travail chez l'adulte, avec trouble de l'adaptation (CIM-11 6B43)** — badge « 6,8 % des femmes et 5,9 % des hommes actifs, 12 mois (ESS 2022) [S5] ».
2. **DX.2 — Harcèlement scolaire (brimades) de l'enfant et de l'adolescent, plaintes psychosomatiques ou refus scolaire** — « 5,8 à 8,8 % des 11–15 ans harcelés ≥ 2 fois/mois (HBSC 2022 CH) [S16] ».
3. **DX.3 — Épisode dépressif avec idées suicidaires consécutif au harcèlement** — rang avancé par la gravité ; « idées suicidaires OR 2,05 après mobbing [S42] ; 8,4 % de pensées suicidaires en Suisse [S39] ».
4. **DX.4 — Cyberharcèlement de l'adolescent (dont diffusion de contenus intimes, sextorsion)** — « 7,2 à 15,4 % au moins une fois (HBSC 2022 CH) [S16] ; 28 % des garçons insultés en ligne (JAMES 2024) [S19] ».
5. **DX.5 — Harcèlement sexuel au travail (y compris milieu médical)** — « 1,7 % des femmes, 4,1 % des 15–29 ans (ESS 2022) [S5] ; observé par 19,0 %/16,7 % en médecine romande [S22] ».
6. **DX.6 — Conflit de travail ou burn-out sans mobbing (diagnostic différentiel)** — « 25 % des femmes, 19 % des hommes épuisés émotionnellement (ESS 2022) [S5][S6] ».
7. **DX.7 — Violence et harcèlement envers les soignants par patients ou proches** — « 50 % du personnel hospitalier en 12 mois (Hahn 2012) [S24] ; 42 % en soins à domicile [S58] ».
8. **DX.8 — Harcèlement obsessionnel (stalking)** — « 15–18 % des femmes au cours de la vie (estimation internationale, aucune enquête suisse) [S14] ».
9. **DX.9 — TSPT et TSPT complexe après harcèlement grave** — « 9e rang — fréquence non quantifiée (Suisse) ».
10. **DX.10 — Allégation de harcèlement d'origine délirante ou paranoïaque** — « ≤ 10 % des stalkings liés à un délire/psychose/manie ; 5–10 % de fausses victimes (Allemagne) [S14] ».
Hors liste (renvoi d'une phrase, sans monographie) : violence domestique et abus sexuel (SSP O6.3), orientation sexuelle et identité de genre (O6.5), burn-out comme SSP (O6.9), absentéisme (O6.1).

### B. Plan
- **Appel A, Bloc 1 (monographie du SSP) : plan académique** (`class="plan-academique"`), annoncé en une phrase : le harcèlement est une situation psychosociale et juridique, non une maladie. Structure imposée : I. Définitions et cadre (TF, SECO, LEg, CP 181b, HBSC, FMH) ; II. Épidémiologie suisse ; III. Cadre légal (CO, LTr, LEg, CC, CP, LAVI, secret médical, OIT 190) ; IV. Évaluation clinique (drapeaux rouges, anamnèse, outils NAQ-R/PHQ-9, CIM-11) ; V. Conduite médico-légale (certificat, orientation, arbre) ; VI. Prise en charge A-B-C-D ; VII. Prévention ; VIII. Points clés et pièges. Les 14 contenus du § 5 bis restent couverts (clés p1–p14 de `ssp`).
- **Appel A, Bloc 2** : tableau comparatif des 10 DX (contexte/auteur, signe clé, critère discriminant, outil, risque vital, base légale, conduite immédiate) et algorithme discriminant. Le tableau de « toxidromes » de la SPEC commune ne s'applique PAS à ce lot.
- **Appel B** : plan monographique en 14 points pour chaque DX (entités cliniques), point 4 avec « Diagnostics différentiels discriminants » (3–4 confusions, signe qui tranche, piège). Physiopathologie limitée aux données lues (stress chronique, cortisol, CRP, risque cardiométabolique : associations observationnelles, jamais causales). Aucune fenêtre bio-mathématique forcée : seuls calculs admis = scores NAQ-R/PHQ-9, délais légaux, titration, proportions, tous marqués « calcul dérivé ».

### C. Conflits de sources et arbitrages (IP suisse d'abord, puis Europe)
1. **Antidépresseurs < 18 ans** : IP suisses (Fluctine®, Fluoxetin-Mepha, Cipralex®, Zoloft® pour la dépression) = non recommandés ; Remeron® = « ne doit pas être utilisé ». Swisspeddose (hors IP) : fluoxétine 8–13 ans 2,5–10 mg/j, 13–18 ans 5–10 mg/j ≥ 1 semaine, puis 10–20 mg/j, max. 40 mg/j ; sertraline 6–18 ans 12,5–25 mg/j 1 semaine puis 25–200 mg/j. Écrire : usage hors IP, décision spécialisée. Ne jamais présenter la fluoxétine comme autorisée en Suisse chez l'enfant.
2. **TSPT** : IP Zoloft® autorise la sertraline (formes chroniques) ; OMS 2013 : TCC centrée sur le trauma/EMDR d'abord, ISRS seulement si échec, indisponibilité ou dépression modérée à sévère ; antidépresseurs proscrits chez l'enfant pour le TSPT. Arbitrage : psychothérapie d'abord, sertraline selon l'IP ensuite.
3. **Benzodiazépines** : IP Temesta® (durée aussi brève que possible, en général ≤ 2–3 mois ; pas < 12 ans) ; SGAD 2024 (2, max. 4 semaines en suicidalité aiguë) ; OMS 2013 (aucune benzodiazépine ni antidépresseur pour les symptômes aigus ou l'insomnie du premier mois post-traumatique). Arbitrage : la durée la plus courte ; jamais en prévention du stress aigu.
4. **Sertraline dose maximale** : SGAD 2016 (50–150 mg) versus IP (200 mg/j) → l'IP prime.
5. **Prévalence du mobbing** : brochure SECO (6,8 % attribué à « ESS 2015 », note ESS 2012) versus OFS 2024 → citer l'ESS 2022 de l'OFS (5,9 % H / 6,8 % F) ; SECO 2002 (4,4 %) seulement en historique.
6. **Harcèlement et CP** : la page Jeunes et médias dit que le harcèlement n'est pas nommé dans le CP → obsolète depuis le 1.1.2026 (CP 181b). CP 55a au 1.10.2026 ne cite pas l'art. 181b (malgré la proposition CAJ-N) : ne pas l'affirmer.
7. **OIT 190** : non ratifiée (message du Conseil fédéral du 5.6.2026) ; ne pas l'invoquer comme droit suisse.
8. **TSPT après mobbing** : le SECO évoque des symptômes « comparables » aux troubles post-traumatiques ; la CIM-11 exige un événement extrêmement menaçant ou horrible → par défaut trouble de l'adaptation ou épisode dépressif.

### D. Seuils et chiffres clés obligatoires
- Définition TF du mobbing (4A_128/2007) citée textuellement ; « notion juridique » que le médecin ne certifie pas (ASSM/FMH 2020) ; FMH art. 34 (but, date, destinataire ; complaisance interdite).
- ESS 2022 : mobbing 5,9 % H / 6,8 % F ; harcèlement sexuel 0,4 % H / 1,7 % F (4,1 % F 15–29 ans) ; épuisement émotionnel 19 % H / 25 % F ; stress 23 %.
- HBSC 2022 CH : harcèlement ≥ 2×/mois 5,8–8,8 % ; cyber ≥ 1× 7,2–15,4 % ; OMS Europe : 11 % harcelés, 15–16 % cyberharcelés.
- CIM-11 : 6B43 (début ≤ 1 mois, résolution ≤ 6 mois après fin du stresseur) ; épisode dépressif ≥ 5 symptômes ≥ 2 semaines ; 6B40 événement extrême ; 6A24 délire ≥ 3 mois ; QD85 burn-out non trouble mental.
- Outils : NAQ-R 22 items, 6 mois, seuils 33–44 / ≥ 45 ; PHQ-9 ≥ 10 (Se 88 %, Sp 88 %), 5/10/15/20.
- Droit : CO 328, 336c (30/90/180 j), 336a et LEg 5 (≤ 6 mois de salaire), 324a (3 semaines la 1re année) ; LEg 10 (protection jusqu'à 6 mois après la procédure) ; LTr 6 et 3a, LTr 9 (45/50 h) ; CC 28b, 28c (6 mois renouvelables) ; CP 181b (≤ 3 ans, sur plainte, depuis 1.1.2026), 193 (≤ 5 ans), 197a, 198, 179ter ; délai de plainte 3 mois (CP 31) ; CC 314c (droit d'aviser du médecin) versus 314d (obligation des non-soumis au secret) ; LAVI 1, 2, 15.
- Médicaments (IP) : sertraline Zoloft® 50 mg/j (TSPT : 25 mg 1 semaine puis 50 mg), paliers ≤ 50 mg/semaine, max. 200 mg, Child-Pugh A–B ≥ ½ dose, C contre-indiquée ; escitalopram Cipralex® 10 mg (max. 20 ; > 65 ans 5–10 ; QT long contre-indiqué) ; mirtazapine Remeron® 15–45 mg le soir ; lorazépam Temesta® 1 mg 2–3×/j ou 1 mg au coucher.
- Ressources : 143 (adultes) et 147 (jeunes), 24 h sur 24 ; centres LAVI ; inspection cantonale du travail ; police 117 ; urgences 144.

### E. Lacunes connues (écrire « donnée non trouvée dans les sources consultées »)
- Prévalence suisse représentative du stalking ; prévalence du TSPT après harcèlement ; pronostic chiffré du trouble de l'adaptation après mobbing.
- Texte intégral HBSC national 2022 et recommandations SGAD 2024 ; commentaire SECO de l'OLT 3 ; DPMin et lois scolaires cantonales (ne citer aucun âge pénal).
- Seuil numérique GAD-7, seuils MBI/PCL-5/ITQ ; outil validé d'évaluation du risque en stalking ; posologies antipsychotiques (DX.10).
- Données chiffrées suisses sur le harcèlement entre médecins (ASMAC : affirmation qualitative seulement) ; incapacité de travail « limitée au poste » non sourcée.
- Résumés seulement : RMS 2026, Najjar 2022, Hahn 2012/2013, études observationnelles internationales (mentionner « résumé » dans les sources).
