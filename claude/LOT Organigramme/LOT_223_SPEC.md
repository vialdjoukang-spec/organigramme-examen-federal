# LOT_223 — SPEC commune (PROFILES 2023, SSP O7.1 « consultation before or after a trip to a foreign (tropical) country »)

## Identité
- LOT_223 = PROFILES 2023, SSP **O7.1 — Consultation avant ou après un voyage en pays tropical** (source : https://smifk-cims.ch/profiles-2023/ssps, consulté 2026-10-21).
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
- Conteneur `<div id="lot223-appel[A|B]-v5" style="font-family: sans-serif; line-height: 1.65; max-width: 980px; margin: auto;">`, h2 bleu #1a5276 bordure #2980b9, sous-titre gris.
- Chaque monographie = `<details open ...>` style du gabarit, `<summary>` « DX.n — Nom <span style="font-size:0.8em;color:#2e8b57;">badge</span> ».
- Grands titres `<p><strong>1. …</strong><br>` ; sous-titres en `<em>` ou `<strong><em>`.
- Fenêtres bio-mathématiques : `<details>` bordure gauche #2980b9 fond #ebf5fb, summary « 🔍 Fenêtre Interactive Bio-Mathématique N.k : … ».
- **CORRECTION** : ne PAS utiliser `<a href="#" title="…">` (inaccessible au toucher, saute en haut de page). Pour un terme interactif, utiliser un `<details>` en ligne :
  `<details class="t" style="display:inline;"><summary style="display:inline;cursor:pointer;color:#1f618d;text-decoration:underline dotted;">terme</summary><span style="display:block;margin:4px 0 8px;padding:8px;background:#f4f6f7;border-left:3px solid #1f618d;font-size:0.93em;">Définition / mécanisme. <em>Source : …</em></span></details>`
- Tableaux : `border="1" cellpadding="7" cellspacing="0" style="width:100%;border-collapse:collapse;..."` thead #d4e6f1 ; envelopper chaque tableau dans `<div style="overflow-x:auto;">` (lecture mobile).
- En fin de fichier : section « Sources » numérotée (titre, organisme, année, URL, date d'accès) et mention : « Contenu produit par IA à partir des sources citées ; non validé cliniquement par un médecin. »

## Fichiers du lot
1. LOT_223_Appel_A_V5_Ultra_Pedagogique_Plan_et_Liste.html — Bloc 1 monographie 14 points du SSP ; Bloc 2 liste DX.1–DX.10 ordonnée + badge + justification.
2. LOT_223_Appel_B_V5_Ultra_Pedagogique_Partie_1_DX.1_a_DX.2.html
3. LOT_223_Appel_B_V5_Ultra_Pedagogique_Partie_2_DX.3_a_DX.5.html
4. LOT_223_Appel_B_V5_Ultra_Pedagogique_Partie_3_DX.6_a_DX.7.html
5. LOT_223_Appel_B_V5_Ultra_Pedagogique_Partie_4_DX.8_a_DX.10.html

## Consigne de Vial (2026-10-21) — plan académique de repli et qualité des différentiels
11. **Plan de repli.** Quand le plan monographique en 14 points ne s'applique pas naturellement à une entité (SSP transversal, procédural, médico-légal, ou entité qui est une classe d'agents plutôt qu'une maladie), ne pas forcer : produire un **plan universitaire/académique** (I., II., III. ; A., B. ; 1., 2.) qui suit la logique propre du sujet, avec **de nombreuses fenêtres cliquables `<details>`** pour les détails (mécanismes, calculs, posologies, cadre légal, exemples). Annoncer en tête de la monographie, en une phrase, pourquoi ce plan est retenu. Les exigences de fond (sources, posologies suisses, bio-mathématique utile, guérison/recherche 2026, pièges d'examen) restent dues ; le lint accepte ce plan si la monographie contient la classe `plan-academique`.
12. **Différentiels de haut niveau.** Chaque DX doit dire ce qui le **distingue des autres DX** et des simulateurs non toxiques :
   - Appel A, Bloc 2 : outre la liste ordonnée, un **tableau comparatif des toxidromes/entités** (conscience, pupilles, FC/PA, FR, température, peau, péristaltisme, ECG, biologie clé, antidote) et un **algorithme discriminant** (quel signe ou examen fait basculer d'un DX à l'autre).
   - Chaque monographie Appel B : rubrique « Diagnostics différentiels discriminants » au point 4 (ou section équivalente), avec les 3–4 confusions les plus dangereuses, le signe ou examen qui tranche, et le piège d'examen associé ; inclure les causes non toxiques qui miment l'intoxication (hypoglycémie, AVC, méningo-encéphalite, état de mal non convulsif, sepsis, hypothermie, traumatisme crânien, troubles métaboliques).
   - Associations et co-ingestions (alcool + benzodiazépines + paracétamol) explicitement traitées : toujours doser paracétamol et éthanol dans l'ingestion volontaire inconnue si la source le soutient.
13. **Fenêtres des thèmes transversaux : très riches et très précises.** Pour tout thème transversal (cadre légal, éthique, communication, organisation des soins, prévention, santé publique, évaluation du risque suicidaire, capacité de discernement, déclaration, Tox Info Suisse, médecine légale), chaque fenêtre `<details>` contient : définition exacte ; base légale ou déontologique précise (article et alinéa via Fedlex, directive ASSM ou code FMH avec année) ; conditions d'application et exceptions ; procédure pas à pas ; exemple clinique concret avec la décision correcte ; erreur fréquente ou piège d'examen ; source datée. Une fenêtre transversale ne se limite jamais à une phrase.











## Spécificités LOT_223
Arbitrages contraignants fixés par l'agent de recherche (22.10.2026). Dossier de preuves : `evidence.json` (85 sources [S1]–[S85] ; textes intégraux suisses/européens + 23 IP suisses ; autres études = résumés, à marquer « résumé »). La SPEC commune parle de toxidromes (modèle hérité) : pour ce lot, lire « entités/situations du voyageur » ; le tableau comparatif de l'Appel A porte sur : délai après retour/incubation, signe clé, examen clé, mécanisme, conduite immédiate, prévention, déclaration.

### Plan
- **Appel A, Bloc 1 : plan académique** (classe `plan-academique`), annoncé en une phrase : SSP procédural à deux temps. I. Consultation pré-voyage (A. évaluation du risque individuel et de l'itinéraire ; B. vaccinations ; C. paludisme ABCDE ; D. autres conseils : diarrhée, rage, eau douce, voyageurs particuliers — grossesse, immunosupprimé, enfant, > 65 ans, VFR). II. Consultation post-voyage (A. fièvre ; B. diarrhée ; C. éosinophilie ; D. peau ; E. exposition à risque et voyageur asymptomatique). III. Cadre légal et organisationnel (LEp art. 12 et annexe 1 de l'ordonnance DFI RS 818.101.126 ; OEp art. 41–48 ; RSI annexe 7 ; OPAS art. 12a al. 3 ; healthytravel.ch/CEMV, Swiss TPH centre de référence). Bloc 2 : liste, tableau comparatif, algorithme.
- **Appel B** : plan monographique en 14 points pour DX.1–DX.3 et DX.6–DX.10 ; **plan académique de repli autorisé pour DX.4 et DX.5** (prévention procédurale), avec mêmes exigences (posologies IP, A-B-C-D, pièges).

### Les 10 DX (ordre contraignant : fréquence suisse/européenne sourcée × gravité)
1. **DX.1 Paludisme d'importation** — 1er rang ; 22 % des fièvres au retour [S29] ; ≈ 340 cas/an en Suisse 2014–2018 [S3].
2. **DX.2 Dengue et arboviroses (chikungunya, Zika)** — 429 cas de dengue en Suisse en 2024 [S7] ; 5 % des fièvres [S29].
3. **DX.3 Diarrhée du voyageur** (aiguë, dysenterie, persistante, BLSE) — 10–40 % des voyageurs [S14].
4. **DX.4 Pré-voyage : prophylaxie antipaludique, autotraitement d'urgence, protection antivectorielle** — rang, fréquence non quantifiée ; > 1 million de voyageurs/an [S4].
5. **DX.5 Pré-voyage : vaccinations** (fièvre jaune, hépatite A, typhoïde, encéphalite japonaise, MenACWY, Qdenga®, Vimkunya®, Dukoral®) — 40,5 % seulement des voyageurs malades avaient consulté avant [S32].
6. **DX.6 Exposition à la rage : PrEP/PEP** — rang, fréquence non quantifiée (Suisse).
7. **DX.7 Fièvre entérique** — 2 % des fièvres [S29] ; résistances (XDR).
8. **DX.8 Fièvre non paludéenne répondant à la doxycycline** (rickettsioses, leptospirose, fièvre Q) — 30,5 % des fièvres indifférenciées non paludéennes [S31].
9. **DX.9 Éosinophilie : schistosomiase (Katayama) et strongyloïdose** — 2 % EuroTravNet 2010 [S33].
10. **DX.10 Dermatoses du voyageur** (larva migrans, pyodermites, leishmaniose) — 18 % des patients GeoSentinel [S47].

### Conflits de sources et arbitrages (IP suisse d'abord pour la posologie ; recommandation officielle suisse la plus récente pour les schémas ; l'autre position en fenêtre)
- **Fièvre jaune** : IP Stamaril® + RSI = dose unique à vie (validité du certificat dès J10, à vie) ; **CEMV = rappel unique ≥ 10 ans (max. 2 doses)** chez l'immunocompétent → enseigner CEMV pour la clinique, RSI pour le certificat. > 60 ans : seulement si risque significatif et inévitable (IP). Seuls les médecins autorisés par l'OFSP vaccinent (OEp art. 41).
- **Rage** : retenir **OFSP/CFV 2021 et Plan 2026** — PrEP 2 doses J0/J28 (J7 si urgent ; immunosupprimé J0/7/21–28) ; PEP préalablement vacciné (≥ 2 doses) J0+J3 sans hRIG, sérologie J14 ; non vacciné J0/3/7/14 + hRIG ≤ 20 UI/kg (1 ampoule 300 UI suffit en règle), sérologie J21, seuil ≥ 0,5 UI/mL. IP Rabipur® (PrEP 3 doses ; PEP 5 doses ou 2-1-1) en fenêtre « divergence ». Lavage 15 min.
- **Méfloquine** : IP (≥ 1 semaine avant ; dose de charge citée) vs OFSP (10–14 jours avant ; doses de charge non recommandées ; 1,5 cp ≥ 90 kg, 2 cp ≥ 120 kg). Contre-indications IP : dépression, anxiété généralisée, psychose, convulsions, insuffisance hépatique sévère, fièvre bilieuse hémoglobinurique.
- **Doxycycline** : OFSP dès 8 ans vs IP Supracycline® > 12 ans ; 100 mg/j, J-1 à 4 semaines après.
- **Atovaquone/proguanil** : J-1/2 → 7 jours après ; CI prophylaxie si ClCr < 30 mL/min ; durée max. 3 mois (experts suisses, pas l'IP).
- **Lopéramide** : IP max 16 mg/j ; CEMV max 12 mg/j ; CI dysenterie, < 6 ans.
- **Paracétamol** : IP Dafalgan® max 4 g/j adulte, ≤ 75 mg/kg/j enfant ; OMS 60 mg/kg/j ; **AINS proscrits** dans les arboviroses (OMS, recommandation forte).
- **Qdenga®** : IP dès 4 ans ; CEMV dès 6 ans **uniquement après dengue documentée** + exposition à forte transmission.
- **Ixiaro®** : IP ≥ 18 ans, J0/J28 ; CEMV J7 possible, hors étiquette 12 mois–18 ans.
- **Vivotif®** : IP revaccination annuelle (voyageur de zone non endémique) vs page CEMV « 1 ou 3 ans » ; vaccin Vi injectable non enregistré en Suisse.
- **Non autorisés en Suisse (liste Swissmedic 30.09.2026)** : artésunate, primaquine, praziquantel, Ixchiq®, Eurartesim® → l'écrire ; base légale d'importation non lue.
- **Hors étiquette** : azithromycine (diarrhée du voyageur, fièvre entérique), ivermectine/albendazole (larva migrans).
- **IP Ciproxine®** « Typhus 2 × 500 mg 7 jours » = vraisemblablement fièvre typhoïde (terminologie germanophone) ; ne pas citer sans précaution ; résistance de S. Typhi à 90 % (Angleterre) → pas de ciprofloxacine empirique au retour d'Asie du Sud.

### Seuils clés
- Paludisme : fièvre > 37,5 °C ≥ 7 jours après l'arrivée en zone → test dans les 24 h (au plus tard 48 h) ; exclusion = 3 jours de tests négatifs ; gravité : parasitémie ≥ 2 % (non-immun), Hb < 50 g/L, glycémie < 2,2 mmol/L, pH < 7,35 ou HCO3⁻ < 15 mmol/L, lactate > 5 mmol/L, créatinine > 265 µmol/L + diurèse < 400 mL/24 h, bilirubine > 50 µmol/L, GCS < 11, PAS < 80 mmHg ; artésunate 2,4 mg/kg (H0, H12, H24 puis /24 h ; 12 mg/kg en 5 doses).
- Risque palustre CEMV : élevé > 10/100 000 voyageurs (P) ; faible > 1–10 (T*, si pas de soins en 48 h) ; minime ≤ 1 (M).
- Dengue : incubation 3–14 j ; signes d'alerte OMS 2025 ; pas de transfusion plaquettaire prophylactique < 50 000/µL sans saignement.
- Diarrhée : ≥ 3 selles/24 h ; SRO 40–50 mL/kg en 4–6 h (Normolytoral®).
- Schistosomiase : sérologie ≥ 2 mois après l'eau douce ; Katayama 4–8 semaines ; praziquantel 40 mg/kg après œufs (non autorisé) ; ivermectine 200 µg/kg (Subvectin®).
- Déclaration (annexe 1) : dengue, chikungunya, Zika, typhoïde/paratyphoïde, choléra = labo, 24 h ; paludisme = labo, 1 semaine ; rage et fièvre jaune = suspicion clinique, 24 h.
- LAMal : OPAS art. 12a al. 3 → vaccins et conseil pour voyage **non remboursés**.

### Lacunes connues (écrire « donnée non trouvée dans les sources consultées » ; à envoyer en HELP après audit)
Version PRO healthytravel.ch (tableaux par pays) non consultée ; chiffres suisses récents du paludisme (2020–2025) et de la typhoïde ; protocole suisse du paludisme grave et accès à l'artésunate ; doses d'azithromycine pour la diarrhée et la fièvre entérique (sources européennes) ; posologie larva migrans ; seuils sérologiques helminthes ; procédure d'exemption amarile ; exceptions PEP pour animaux domestiques ; textes intégraux BIA 2025, LeishMan 2014, ISTM 2017 ; statut de déclaration des rickettsioses/leptospirose.
