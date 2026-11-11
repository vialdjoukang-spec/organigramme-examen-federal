# LOT_224 — SPEC commune (PROFILES 2023, SSP O7.2 « determination of incapacity to work or to attend class/educational lessons »)

## Identité
- LOT_224 = PROFILES 2023, SSP **O7.2 — Détermination d'une incapacité de travail ou scolaire** (source : https://smifk-cims.ch/profiles-2023/ssps, consulté 2026-10-21).
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
- Conteneur `<div id="lot224-appel[A|B]-v5" style="font-family: sans-serif; line-height: 1.65; max-width: 980px; margin: auto;">`, h2 bleu #1a5276 bordure #2980b9, sous-titre gris.
- Chaque monographie = `<details open ...>` style du gabarit, `<summary>` « DX.n — Nom <span style="font-size:0.8em;color:#2e8b57;">badge</span> ».
- Grands titres `<p><strong>1. …</strong><br>` ; sous-titres en `<em>` ou `<strong><em>`.
- Fenêtres bio-mathématiques : `<details>` bordure gauche #2980b9 fond #ebf5fb, summary « 🔍 Fenêtre Interactive Bio-Mathématique N.k : … ».
- **CORRECTION** : ne PAS utiliser `<a href="#" title="…">` (inaccessible au toucher, saute en haut de page). Pour un terme interactif, utiliser un `<details>` en ligne :
  `<details class="t" style="display:inline;"><summary style="display:inline;cursor:pointer;color:#1f618d;text-decoration:underline dotted;">terme</summary><span style="display:block;margin:4px 0 8px;padding:8px;background:#f4f6f7;border-left:3px solid #1f618d;font-size:0.93em;">Définition / mécanisme. <em>Source : …</em></span></details>`
- Tableaux : `border="1" cellpadding="7" cellspacing="0" style="width:100%;border-collapse:collapse;..."` thead #d4e6f1 ; envelopper chaque tableau dans `<div style="overflow-x:auto;">` (lecture mobile).
- En fin de fichier : section « Sources » numérotée (titre, organisme, année, URL, date d'accès) et mention : « Contenu produit par IA à partir des sources citées ; non validé cliniquement par un médecin. »

## Fichiers du lot
1. LOT_224_Appel_A_V5_Ultra_Pedagogique_Plan_et_Liste.html — Bloc 1 monographie 14 points du SSP ; Bloc 2 liste DX.1–DX.10 ordonnée + badge + justification.
2. LOT_224_Appel_B_V5_Ultra_Pedagogique_Partie_1_DX.1_a_DX.2.html
3. LOT_224_Appel_B_V5_Ultra_Pedagogique_Partie_2_DX.3_a_DX.5.html
4. LOT_224_Appel_B_V5_Ultra_Pedagogique_Partie_3_DX.6_a_DX.7.html
5. LOT_224_Appel_B_V5_Ultra_Pedagogique_Partie_4_DX.8_a_DX.10.html

## Consigne de Vial (2026-10-21) — plan académique de repli et qualité des différentiels
11. **Plan de repli.** Quand le plan monographique en 14 points ne s'applique pas naturellement à une entité (SSP transversal, procédural, médico-légal, ou entité qui est une classe d'agents plutôt qu'une maladie), ne pas forcer : produire un **plan universitaire/académique** (I., II., III. ; A., B. ; 1., 2.) qui suit la logique propre du sujet, avec **de nombreuses fenêtres cliquables `<details>`** pour les détails (mécanismes, calculs, posologies, cadre légal, exemples). Annoncer en tête de la monographie, en une phrase, pourquoi ce plan est retenu. Les exigences de fond (sources, posologies suisses, bio-mathématique utile, guérison/recherche 2026, pièges d'examen) restent dues ; le lint accepte ce plan si la monographie contient la classe `plan-academique`.
12. **Différentiels de haut niveau.** Chaque DX doit dire ce qui le **distingue des autres DX** et des simulateurs non toxiques :
   - Appel A, Bloc 2 : outre la liste ordonnée, un **tableau comparatif des toxidromes/entités** (conscience, pupilles, FC/PA, FR, température, peau, péristaltisme, ECG, biologie clé, antidote) et un **algorithme discriminant** (quel signe ou examen fait basculer d'un DX à l'autre).
   - Chaque monographie Appel B : rubrique « Diagnostics différentiels discriminants » au point 4 (ou section équivalente), avec les 3–4 confusions les plus dangereuses, le signe ou examen qui tranche, et le piège d'examen associé ; inclure les causes non toxiques qui miment l'intoxication (hypoglycémie, AVC, méningo-encéphalite, état de mal non convulsif, sepsis, hypothermie, traumatisme crânien, troubles métaboliques).
   - Associations et co-ingestions (alcool + benzodiazépines + paracétamol) explicitement traitées : toujours doser paracétamol et éthanol dans l'ingestion volontaire inconnue si la source le soutient.
13. **Fenêtres des thèmes transversaux : très riches et très précises.** Pour tout thème transversal (cadre légal, éthique, communication, organisation des soins, prévention, santé publique, évaluation du risque suicidaire, capacité de discernement, déclaration, Tox Info Suisse, médecine légale), chaque fenêtre `<details>` contient : définition exacte ; base légale ou déontologique précise (article et alinéa via Fedlex, directive ASSM ou code FMH avec année) ; conditions d'application et exceptions ; procédure pas à pas ; exemple clinique concret avec la décision correcte ; erreur fréquente ou piège d'examen ; source datée. Une fenêtre transversale ne se limite jamais à une phrase.











## Spécificités LOT_224
**Arbitrages contraignants (agent de recherche, 22.10.2026) — sources : `evidence.json` (40 sources S1–S40).**

### Plan retenu
- **Appel A et les 10 DX : plan en 14 points transposé CanMEDS/PROFILES (PROMPT V6 § 5 bis), PAS le plan académique.** L'évaluation d'une incapacité est une démarche clinique (questions, examen, outil, arbre, suivi) : la transposition sonne juste. Point 3 = cadre légal exact ; aucune physiopathologie plaquée, sauf le déconditionnement lombaire (atrophie jusqu'à 3 %/jour au repos) [S30] et la gravité dépressive (DX.3). Annoncer ce choix en une phrase en tête de l'Appel A.
- **Non-doublon avec LOT_239 (O7.17 certificats)** : ici on évalue le DEGRÉ, la NATURE (totale/partielle/qualitative/limitée au poste) et la DURÉE de l'incapacité, au travail et à l'école. Les règles formelles du certificat (rétroactif, complaisance, CP 318, secret, demandes d'assureurs) ne sont que rappelées en une phrase avec renvoi « voir LOT_239 ».

### Les 10 DX (ordre = fréquence suisse sourcée pondérée par la gravité ; annoncer ce critère)
1. **DX.1** Affection aiguë intercurrente autolimitée (infection respiratoire ou digestive) : incapacité totale brève et contagiosité au poste — badge « 81 % des certificats pour maladie, 53 % < 1 semaine (Sentinella 2005) [S24] ».
2. **DX.2** Accident professionnel/non professionnel et maladie professionnelle (LAA) — « 18 % des certificats [S24] ; 936 965 cas LAA en 2025 [S29] ».
3. **DX.3** Troubles psychiques courants (épisode dépressif, trouble de l'adaptation, épuisement professionnel) — rang + « cofacteurs psychosociaux 19 % des certificats [S24] ; 180 nouvelles rentes AI psychiques/100 000 en 2024 [S28] ».
4. **DX.4** Lombalgie commune et TMS : incapacité partielle, activité adaptée, prévention de la chronicisation — rang (fréquence non quantifiée).
5. **DX.5** Incapacité prolongée (chronique, oncologique, postopératoire) : activité adaptée, reprise progressive, détection précoce AI — « 17 % des certificats > 3 semaines ; 48 % des certificats postopératoires > 3 semaines [S24] ».
6. **DX.6** Incapacité limitée au poste (conflit) et facteurs non médicaux — rang ; « 10 % des généralistes reçoivent chaque semaine une demande d'arrêt pour motif non médical [S25] ».
7. **DX.7** Grossesse et maternité : incapacité versus protection de la maternité au poste dangereux — rang.
8. **DX.8** Incapacité scolaire et de formation (cours, éducation physique, examen, éviction de collectivité) — rang.
9. **DX.9** Inaptitude au poste à exigences de sécurité (épilepsie, diabète sous insuline, travail de nuit, conduite professionnelle) — rang.
10. **DX.10** Plaintes incohérentes, majoration, simulation, troubles fonctionnels : plausibilité et cohérence — rang.
Les badges sans pourcentage portent « Ne rang — fréquence non quantifiée (Suisse) ». Ne jamais écrire « ≈ 49 % des rentes AI sont psychiques » sans « calcul dérivé ».

### Seuils et chiffres clés (vérifiés sur le texte)
- **Définitions** : LPGA 6 (incapacité de travail ; activité d'une autre profession exigible en cas de longue durée), LPGA 7 (incapacité de gain, non objectivement surmontable), LPGA 8 (invalidité) ; LPGA 3/4/5 (maladie/accident/maternité) [S8]. Inaptitude ≠ incapacité [S5].
- **Capacité = temps de présence × rendement** (multiplier, jamais additionner ni moyenner) ; rendement 25/50/75/100 % ; exemple SIM 50 % × 75 % = 37,5 % [S3] [S2]. Incapacité partielle non précisée = réduction du temps [S5].
- **Non-exigibilité (SIM 2026, Oliveri)** : risque inacceptable pour soi/tiers ; détérioration prévisible ; épuisement empêchant toute qualité de vie hors travail ; comportement inacceptable pour des tiers [S2].
- **Certificat** : ≤ 1 mois ou jusqu'à la prochaine consultation ; rétroactivité ≤ 3–4 jours, au plus 1 semaine ; exigible dès le 1er jour (maladie), obligatoire dès le 1er jour (accident) ; la plupart des employeurs au 3e jour [S5] [S6] [S25].
- **Droit social** : CO 324a (3 semaines la 1re année ; al. 3 grossesse) ; CO 336c (30/90/180 jours ; grossesse + 16 semaines) [S15] ; LAMal 72 (≥ 50 %, dès le 3e jour, 720 IJ/900 jours) [S13] ; LAA 16–17 (dès le 3e jour, 80 %) ; LAA 45 ; OLAA 13 (≥ 8 h/semaine pour les accidents non professionnels) [S11] [S12] ; LACI 28 (30 jours, 44 IJ) [S14].
- **AI** : annonce de détection précoce dès 30 jours consécutifs [S5] ; décision AI sous 30 jours (RAI 1quater) ; réinsertion si ≥ 50 % depuis ≥ 6 mois (LAI 14a) ; rente si ≥ 40 % en moyenne sur 1 an et invalidité ≥ 40 % (LAI 28) ; rente au plus tôt 6 mois après la demande (LAI 29) ; quotité LAI 28b (40 % → 25 % ; +2,5 % par point jusqu'à 49 % → 47,5 % ; 50–69 % = taux ; ≥ 70 % entière) [S9] [S10].
- **Lombalgie** : dépistage STarT Back/drapeaux après 2 semaines d'arrêt sans amélioration ; rester actif ; consultation spécialisée si > 1 mois ; 10 % à risque après 18 jours d'arrêt [S30].
- **Psychique** (source secondaire HUG) : EDM léger pas d'arrêt / moyen cas par cas / sévère arrêt ; burn-out : arrêt 50 % ou 100 %, pas toujours la meilleure option [S31] ; travail + clinique : ≈ 25 jours d'absence de moins sur 1 an (Cochrane, résumé) [S32].
- **Grossesse** : OProMa 7 (> 5 kg régulier/> 10 kg occasionnel jusqu'au 6e mois ; aucune charge lourde dès le 7e), 8 (< −5 °C ou > +28 °C), 10 (micro-organismes), 11 (≥ 85 dB(A)) ; certificat OProMa 3 (sans restriction/sous conditions/interruption) ; OLT 1 60–61 (≤ 9 h/j ; debout : pause 10 min/2 h dès le 4e mois, ≤ 4 h/j dès le 6e) ; LTr 35a (8 semaines post-partum ; 20 h–6 h interdit 8 semaines avant) ; LTr 35 al. 3 (80 %) ; CO 329f (14 semaines) ; LAPG 16c–16f (98 jours, 80 %, max. 220 CHF/j) [S18] [S17] [S16] [S15] [S19].
- **École** : LESp 12 (éducation physique obligatoire ; ≥ 3 périodes/semaine) ; OESp 49 (≥ 3 leçons, secondaire II ≥ 110 leçons/an) [S22] [S23] ; Vaud RLEO 99 al. 2 (certificat si > 1 semaine ou absences répétées) [S33] ; dispenses EPS datées, partielles, degré I ≥ 3 mois / degré II ≤ 3 mois [S34] ; examen : certificat dans les 3 jours (exemple UNIL 2020) [S35].
- **Sécurité** : épilepsie avérée et groupe 2 : 5 ans sans crise sans traitement ; risque acceptable 1:20 000/an [S37] ; diabète : HbA1c > 8,5 % (groupe 2) / > 10 % (groupe 1) → pas d'admission ; D/D1 exclus sous traitement hypoglycémiant sauf dérogation niveau 4 [S38] ; OAC 27 (5 ans ; dès 50 ans au plus tard à 53 ans puis 3 ans) [S39] ; OLT 1 44–45 (travail de nuit ≥ 25 nuits/an) [S17].
- **Santé publique** : OHyg 21 (maladie aiguë transmissible par les denrées alimentaires → accès interdit) [S21] ; LEp 38 (interdiction d'exercer par l'autorité) [S20].

### Conflits de sources et arbitrages
- **SIM 2026 prime sur SIM 2022 (abrogée)** : citer SIM 2022 seulement pour l'historique ou quand SIM 2026 ne la contredit pas ; facteurs étrangers : SIM 2026 = sans effet SAUF s'ils entraînent/entretiennent/aggravent une atteinte diagnostiquée.
- **SIM 2022 « moyenne » vs produit** : retenir la multiplication (SIM 2026, certificat SIM).
- **Éviction gastro-entérite 24 h (Leytron/AMCS) vs 48 h (EVAM, non lu)** : écrire « selon la règle du médecin cantonal ; 24 h dans la reprise AMCS lue (source secondaire) ».
- **Burn-out** : pas de recommandation primaire lue ; présenter la gradation HUG comme enseignement universitaire suisse secondaire, pas comme directive.
- **Posologies** : AUCUNE vérifiée dans l'information professionnelle pour ce lot. Le point 11.B pharmacologique se limite à « relève de la monographie de la maladie ; voir l'IP suisse » ; ne pas reprendre les durées d'hypnotiques/anxiolytiques HUG comme posologie.
- **Biomath** : uniquement capacité (temps × rendement), IJ LAA, quotité LAI 28b, taux d'invalidité LPGA 16 (calcul dérivé : 80 000/44 000 CHF → 45 % → 37,5 %), LAPG (plafond 220 CHF), VPP d'un test de validation (DX.10, calcul dérivé illustratif). Tous étiquetés « calcul dérivé ».

### Lacunes connues (écrire « donnée non trouvée dans les sources consultées »)
Hochstrasser 2016 (texte intégral) ; document AMCS 2020 ; guide IST 2016 ; guide FMH 7.6 en ligne ; durées de référence suisses par diagnostic/chirurgie ; fréquence des certificats scolaires, des interdictions en grossesse, des inaptitudes de sécurité et de la simulation ; règles scolaires des autres cantons et teneur 2026 du RLEO ; recommandations SSRS (somnolence) ; directive européenne lombalgie (van Tulder 2006) non lue ; Job-Stress-Index ; pages SECO maternité ; toute posologie.

