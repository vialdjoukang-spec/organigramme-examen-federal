# LOT_218 — SPEC commune (PROFILES 2023, SSP O6.5 « issues regarding diversity of affective and sexual orientation and gender identity »)

## Identité
- LOT_218 = PROFILES 2023, SSP **O6.5 — Diversité de l'orientation affective et sexuelle, identité de genre** (source : https://smifk-cims.ch/profiles-2023/ssps, consulté 2026-10-21).
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
- Conteneur `<div id="lot218-appel[A|B]-v5" style="font-family: sans-serif; line-height: 1.65; max-width: 980px; margin: auto;">`, h2 bleu #1a5276 bordure #2980b9, sous-titre gris.
- Chaque monographie = `<details open ...>` style du gabarit, `<summary>` « DX.n — Nom <span style="font-size:0.8em;color:#2e8b57;">badge</span> ».
- Grands titres `<p><strong>1. …</strong><br>` ; sous-titres en `<em>` ou `<strong><em>`.
- Fenêtres bio-mathématiques : `<details>` bordure gauche #2980b9 fond #ebf5fb, summary « 🔍 Fenêtre Interactive Bio-Mathématique N.k : … ».
- **CORRECTION** : ne PAS utiliser `<a href="#" title="…">` (inaccessible au toucher, saute en haut de page). Pour un terme interactif, utiliser un `<details>` en ligne :
  `<details class="t" style="display:inline;"><summary style="display:inline;cursor:pointer;color:#1f618d;text-decoration:underline dotted;">terme</summary><span style="display:block;margin:4px 0 8px;padding:8px;background:#f4f6f7;border-left:3px solid #1f618d;font-size:0.93em;">Définition / mécanisme. <em>Source : …</em></span></details>`
- Tableaux : `border="1" cellpadding="7" cellspacing="0" style="width:100%;border-collapse:collapse;..."` thead #d4e6f1 ; envelopper chaque tableau dans `<div style="overflow-x:auto;">` (lecture mobile).
- En fin de fichier : section « Sources » numérotée (titre, organisme, année, URL, date d'accès) et mention : « Contenu produit par IA à partir des sources citées ; non validé cliniquement par un médecin. »

## Fichiers du lot
1. LOT_218_Appel_A_V5_Ultra_Pedagogique_Plan_et_Liste.html — Bloc 1 monographie 14 points du SSP ; Bloc 2 liste DX.1–DX.10 ordonnée + badge + justification.
2. LOT_218_Appel_B_V5_Ultra_Pedagogique_Partie_1_DX.1_a_DX.2.html
3. LOT_218_Appel_B_V5_Ultra_Pedagogique_Partie_2_DX.3_a_DX.5.html
4. LOT_218_Appel_B_V5_Ultra_Pedagogique_Partie_3_DX.6_a_DX.7.html
5. LOT_218_Appel_B_V5_Ultra_Pedagogique_Partie_4_DX.8_a_DX.10.html

## Consigne de Vial (2026-10-21) — plan académique de repli et qualité des différentiels
11. **Plan de repli.** Quand le plan monographique en 14 points ne s'applique pas naturellement à une entité (SSP transversal, procédural, médico-légal, ou entité qui est une classe d'agents plutôt qu'une maladie), ne pas forcer : produire un **plan universitaire/académique** (I., II., III. ; A., B. ; 1., 2.) qui suit la logique propre du sujet, avec **de nombreuses fenêtres cliquables `<details>`** pour les détails (mécanismes, calculs, posologies, cadre légal, exemples). Annoncer en tête de la monographie, en une phrase, pourquoi ce plan est retenu. Les exigences de fond (sources, posologies suisses, bio-mathématique utile, guérison/recherche 2026, pièges d'examen) restent dues ; le lint accepte ce plan si la monographie contient la classe `plan-academique`.
12. **Différentiels de haut niveau.** Chaque DX doit dire ce qui le **distingue des autres DX** et des simulateurs non toxiques :
   - Appel A, Bloc 2 : outre la liste ordonnée, un **tableau comparatif des toxidromes/entités** (conscience, pupilles, FC/PA, FR, température, peau, péristaltisme, ECG, biologie clé, antidote) et un **algorithme discriminant** (quel signe ou examen fait basculer d'un DX à l'autre).
   - Chaque monographie Appel B : rubrique « Diagnostics différentiels discriminants » au point 4 (ou section équivalente), avec les 3–4 confusions les plus dangereuses, le signe ou examen qui tranche, et le piège d'examen associé ; inclure les causes non toxiques qui miment l'intoxication (hypoglycémie, AVC, méningo-encéphalite, état de mal non convulsif, sepsis, hypothermie, traumatisme crânien, troubles métaboliques).
   - Associations et co-ingestions (alcool + benzodiazépines + paracétamol) explicitement traitées : toujours doser paracétamol et éthanol dans l'ingestion volontaire inconnue si la source le soutient.
13. **Fenêtres des thèmes transversaux : très riches et très précises.** Pour tout thème transversal (cadre légal, éthique, communication, organisation des soins, prévention, santé publique, évaluation du risque suicidaire, capacité de discernement, déclaration, Tox Info Suisse, médecine légale), chaque fenêtre `<details>` contient : définition exacte ; base légale ou déontologique précise (article et alinéa via Fedlex, directive ASSM ou code FMH avec année) ; conditions d'application et exceptions ; procédure pas à pas ; exemple clinique concret avec la décision correcte ; erreur fréquente ou piège d'examen ; source datée. Une fenêtre transversale ne se limite jamais à une phrase.











## Spécificités LOT_218
Arbitrages contraignants (recherche du 22.10.2026 ; preuves : `evidence.json`, 56 sources S1–S56). Ils priment sur les consignes génériques de toxicologie de la tête de SPEC (lot transversal psychosocial : le « tableau comparatif des toxidromes » devient un tableau comparatif des 10 situations ; colonnes imposées : population, signe ou question clé, outil ou examen clé, cadre légal, conduite immédiate, piège).

**A. Plan.**
- Appel A, Bloc 1 : **plan académique** (classe `plan-academique`, annoncé en une phrase : sujet psychosocial, légal et préventif sans physiopathologie propre). Ossature imposée : I. Notions et terminologie (orientation ≠ identité ≠ caractéristiques sexuelles ; CIM-11 HA60/HA61 ; VDS) — II. Épidémiologie suisse (ESS 2022, HBSC 2022, Obsan, HSLU) — III. Déterminants : stress minoritaire et accès aux soins — IV. Cadre légal (Cst. 8, CP 261bis, CC 30b, CC 94/255a/264c, LPMA 3/4/15, LEg 3, CP 321, CC 314c, LPMéd 40) — V. Entretien inclusif et anamnèse sexuelle — VI. Situations cliniques (renvoi aux 10 DX) — VII. Prévention et santé publique — VIII. Points clés et pièges. Bloc 2 : liste, badges, justification, tableau comparatif, algorithme discriminant.
- Appel B : **14 points** par DX avec la transposition du PROMPT V6 § 5 bis (p3 = mécanisme ou cadre ; p8 = critères ou conditions légales). Plan académique toléré seulement pour DX.3 (violences) si le rédacteur l'annonce. Bio-mathématique uniquement : DX.8 (dose cumulée de cyprotérone, conversions pmol/L↔pg/mL, pressions d'Oestrogel®, ClCr < 30 mL/min), DX.9 (nmol/L↔ng/dL, hématocrite, équivalents de testostérone), DX.2 (NNT Doxy-PEP, schémas PrEP), DX.10 (dose de leuproréline par kg), DX.1/DX.3/DX.4 (rapports de fréquences, calculs dérivés). Aucun calcul plaqué ailleurs.

**B. Les 10 DX (ordre imposé, fréquence suisse pondérée par la gravité).**
1. DX.1 — Détresse psychique et suicidalité des personnes LGBT (stress minoritaire). Badge : pensées suicidaires 19,9 % (homo/bisexuels) et 28,9 % (trans/non binaires) contre 7,4 % et 8,1 % (ESS 2022) [S5].
2. DX.2 — Santé sexuelle des HSH et des femmes trans : VIH (PrEP, PEP), IST, hépatites, HPV, mpox. Badge : prévalence VIH 8 % chez les HSH ; 73,6 % des syphilis chez les HSH [S14].
3. DX.3 — Violences, discriminations, crimes de haine (dont couple de même sexe) et mesures de conversion. Badge : 67,6 % à vie ; 26,6 % dans les soins [S2].
4. DX.4 — Chemsex et usage de substances. Badge : 17,2 % des gbHSH suivis (SHCS + SwissPrEPared) [S19].
5. DX.5 — Adolescent en questionnement (coming-out, confidentialité, capacité de discernement). Badge : 4,2 % bisexuels, 1,6 % genre divers à 14–15 ans (HBSC 2022) [S4].
6. DX.6 — FSF, femmes lesbiennes et bisexuelles ; couples de même sexe : prévention gynécologique et projet parental. Badge : 69 % seulement des FSF romandes contrôlées en 3 ans [S2].
7. DX.7 — Adulte trans ou non binaire demandant une transition (HA60) : évaluation, état civil, fertilité, AOS. Badge : 0,6 % trans + 0,3 % genre divers (ESS 2022) [S4].
8. DX.8 — Hormonothérapie féminisante. Badge : « 8e rang — fréquence non quantifiée (Suisse) » ; méningiome sous cyprotérone 1–10/10 000 [S11].
9. DX.9 — Hormonothérapie masculinisante. Badge : érythrocytose ≈ 11 % [S8].
10. DX.10 — Adolescent avec incongruence/dysphorie de genre (suppression pubertaire, hormones, éthique). Badge : « 10e rang — fréquence non quantifiée (Suisse) ».
Les VDS (1:3000–1:5000 [S7]) ne sont pas un DX : elles figurent dans la monographie SSP (I.) et comme différentiel obligatoire des DX.7 et DX.10.

**C. Conflits de sources — décisions.**
- FI suisse > SSED 2026 pour chaque produit : Oestrogel® 1 pression = 1,25 g = 0,75 mg (3 mg/j = 4 pressions ; la mention SSED « 1–6 pressions » est fausse) ; Estradot® patchs 25–100 µg/24 h changés tous les 3–4 jours (la « 50–300 µg » SSED implique plusieurs patchs, off-label) ; Testoviron® Dépôt exclusivement i.m. (250 mg toutes les 2–3 semaines puis 3–4 semaines ; la SSED cite aussi une voie s.c.) ; Nebido®/Testone 1000 mg i.m. très lente toutes les 10–14 semaines (2e injection possible à 6 semaines) ; Testogel® 50–100 mg/j ; Tostran® 60 mg/j, max. 80 mg ; Aldactone® CI si ClCr < 30 mL/min, hyperkaliémie, hyponatrémie, Addison, éplérénone. Les doses SSED supérieures aux FI (spironolactone 100–300 mg/j, valérate d'estradiol 2–6 mg/j, cyprotérone ≈ 10 mg/j) se présentent comme recommandations d'experts suisses off-label.
- Off-label : aucune hormone n'est autorisée pour l'incongruence de genre ; les FI de testostérone listent « sexe féminin/femmes » en contre-indication ; Androcur® FI : indications masculines limitées (déviations sexuelles, cancer prostatique), déconseillé < 18 ans ; Lucrin Dépôt® autorisé seulement pour la puberté précoce centrale chez l'enfant ; Pamorelin® non recommandé < 18 ans ; Decapeptyl® seulement PMA ; Doxy-PEP off-label. Toujours écrire « hors indication (off-label), consentement documenté ».
- Cyprotérone : EMA/PRAC 2020 (≥ 10 mg/j réservé, risque surtout ≥ 25 mg/j, lié à la dose cumulée, méningiome → arrêt définitif) + SSED (≈ 10 mg/j, risque > 10 g cumulés). Présenter les deux.
- Mineurs : CNE 43/2024 (Suisse) prime sur l'AWMF 2025 pour le cadre éthico-juridique ; l'AWMF (D/A/CH) fixe les critères cliniques (pas avant Tanner 2, VII.K6) ; citer les votes séparés de la SGKJPP (diagnostic pédopsychiatrique complet indispensable, données à long terme manquantes, études nécessaires). Aucune ligne directrice exclusivement américaine ; WPATH SOC 8 et Endocrine Society seulement comme citées par la CNE/SSED.
- PrEP : FI Emtricitabin-Tenofovir-Mepha® = 1 comprimé/j, à la demande non recommandé ; SwissPrEPared 4.0 (approuvé CFIST) autorise 2-1-1 chez l'HSH cisgenre et impose 2-7 pour femmes trans et vaginal réceptif. Présenter FI puis SwissPrEPared.
- Droit pénal : CP 261bis = orientation sexuelle seulement (pas l'identité de genre) ; pas d'infraction fédérale de mesures de conversion dans le CP (état 1.10.2026) ; Neuchâtel = projet CPN art. 9 du 1.2.2023 (statut d'adoption non vérifié : l'écrire).

**D. Seuils et chiffres clés (à citer exactement).**
ESS 2022 : bisexuels 2,1 %, gays 1,4 %, lesbiennes 0,5 % ; trans 0,6 %, genre divers 0,3 % [S4] — pensées suicidaires 19,9/7,4 % et 28,9/8,1 % ; tentatives 11,9/3,4 % et 9,7/3,8 % [S5] — SGB : tentative ≈ 4 × (11 % contre 3 %), LGBT Health 18 %, trans 30 % [S3] — renoncement aux soins 16,2 % contre 6,9 % ; 35,6 % chez les trans [S2, S6] — CC 30b : seul dès 16 ans révolus, sans certificat ; avant 16 ans consentement du représentant légal [S26] — CC 94 mariage pour tous depuis le 1.7.2022 ; LPMA 3 al. 3 don de sperme seulement couple marié ; LPMA 4 don d'ovules et GPA interdits ; LPMA 15 conservation 5 + 5 ans [S26, S29] — Hormones (SSED) : suivi tous les 3 mois la 1re année puis 6–12 mois ; testostérone cible < 2 nmol/L et œstradiol 370–730 pmol/L (féminisation) ; testostérone 14–24 nmol/L à mi-cycle (énanthate), < 14 nmol/L en fin d'intervalle (undécanoate → raccourcir) ; hématocrite > 0,50–0,54 = érythrocytose (≈ 11 %) ; ≈ 10 % saignements persistants ; la testostérone n'est pas contraceptive ; dépistage du col 21–70 ans tous les 3 ans ou HPV dès 30 ans pour toute personne avec col [S8] — PrEP : CI si ClCr < 60 mL/min ou protéinurie [S12] — Doxy-PEP : 200 mg < 24 h (max. 72 h), ≤ 200 mg/24 h, recommandation conditionnelle si HSH/femme trans avec IST bactérienne dans les 12 mois [S13] — Chemsex : GHB/GBL + alcool/benzodiazépines/opioïdes = perte de conscience et dépression respiratoire [S21] ; GHB : GCS < 13 dans 56,1 % ; soins intensifs 55,3 % avec éthanol contre 22,4 % [S22] — PHQ-9 ≥ 10 : Se 88 %, Sp 88 % [S37] — plan de sécurité RR 0,570, NNT 16 [S36] ; ASSIP 8,3 % contre 26,7 % [S35] — Lucrin Dépôt® PPC : 0,3 mg/kg/4 semaines (min. 7,5 mg) [S45] — Nebido® LS : limitation hypogonadisme, garantie préalable de l'assureur [S54].

**E. Lacunes connues (écrire « donnée non trouvée dans les sources consultées » ; à envoyer au HELP après audit si elles restent).**
Code de déontologie FMH ; fréquence suisse des hormonothérapies et des suppressions pubertaires ; texte primaire SSGO du dépistage du col ; FI distincte d'Androcur®-10 ; statut d'adoption de l'art. 9 CPN (NE) et des lois cantonales sur les conversions ; jurisprudence du TF sur la prise en charge AOS ; texte intégral WPATH SOC 8, Endocrine Society, Cass Review ; violence de couple de même sexe chiffrée en Suisse ; critères de dépendance et dosages toxicologiques du chemsex ; don de sang des HSH ; LStup. Rappels de méthode : S14–S18, S22, S32–S37, S55 sont repris des dossiers des LOT_230/234/237/246/248 ; les études citées de seconde main (Wang, Béziane, Berrut, Pauli, Bustos, Wiepjes) se citent « cité par [S2]/[S6] ».
