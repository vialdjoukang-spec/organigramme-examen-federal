# RAPPORT D’AUDIT · LOT_004 (24.10.2026)

Périmètre : Appel A (SSP G4 « Fatigue, épuisement » et liste du bloc 2), plus les 10 DX de l’Appel B. Grille V7 à 14 points. Le point 13.b est HUMAIN, d’où un plafond automatique de 98,8 %.
Avant = work/LOT_004 (phase 0, originaux : 5 exports Google Docs V5, sans aucune source). Après = source/eval.sh (decoupe_l → examens → style → score → verif_v7), plus outils/contraste.py.
Aucune capture d’écran (consigne de l’utilisateur ; captures3.py non lancé).

| Cours | Score avant | Score après | Examens cliquables / fenêtres à 2 onglets (avant → après) | Phrases > 30 mots (avant → après) | Sigles non développés (avant → après) | Probas rouges (après) | Fichier(s) (octets) |
|---|---|---|---|---|---|---|---|
| SSP + bloc 2 | 30,0 % | 98,8 % | 3 / 0 → 60 / 60 | 4 → 0 | 26 → 0 | 26 | LOT_004_Appel_A_SSP_G4_Fatigue_epuisement_AUDITÉ_a.html (118 380)<br>…_AUDITÉ_b.html (147 299) |
| DX.1 Anémie ferriprive | 30,0 % | 98,8 % | 1 / 0 → 56 / 56 | 5 → 0 | 5 → 0 | 16 | LOT_004_DX1_Anemie_ferriprive_AUDITÉ.html (178 897) |
| DX.2 Dépression, burn-out | 28,8 % | 98,8 % | 0 / 0 → 31 / 31 | 2 → 0 | 8 → 0 | 16 | LOT_004_DX2_Depression_burn_out_AUDITÉ.html (160 209) |
| DX.3 SAOS | 31,2 % | 98,8 % | 2 / 0 → 20 / 20 | 8 → 0 | 7 → 0 | 16 | LOT_004_DX3_SAOS_AUDITÉ.html (131 457) |
| DX.4 Hypothyroïdie | 32,5 % | 98,8 % | 1 / 0 → 47 / 47 | 11 → 0 | 6 → 0 | 16 | LOT_004_DX4_Hypothyroidie_primaire_AUDITÉ.html (162 688) |
| DX.5 Asthénies post-infectieuses | 35,0 % | 98,8 % | 1 / 0 → 45 / 45 | 10 → 0 | 20 → 0 | 16 | LOT_004_DX5_Asthenies_post_infectieuses_AUDITÉ.html (164 019) |
| DX.6 Insuffisance cardiaque | 35,0 % | 98,8 % | 3 / 0 → 43 / 43 | 12 → 0 | 22 → 0 | 16 | LOT_004_DX6_Insuffisance_cardiaque_AUDITÉ.html (150 921) |
| DX.7 Maladie rénale chronique | 33,8 % | 98,8 % | 0 / 0 → 36 / 36 | 14 → 0 | 16 → 0 | 16 | LOT_004_DX7_Maladie_renale_chronique_AUDITÉ.html (157 545) |
| DX.8 Néoplasie occulte | 31,2 % | 98,8 % | 1 / 0 → 58 / 58 | 12 → 0 | 22 → 0 | 16 | LOT_004_DX8_Neoplasie_occulte_AUDITÉ.html (182 434) |
| DX.9 EM/SFC, POTS | 40,0 % | 98,8 % | 0 / 0 → 26 / 26 | 12 → 0 | 24 → 0 | 16 | LOT_004_DX9_EM_SFC_POTS_AUDITÉ.html (126 386) |
| DX.10 Maladie d’Addison | 32,5 % | 98,8 % | 1 / 0 → 32 / 32 | 13 → 0 | 9 → 0 | 16 | LOT_004_DX10_Maladie_d_Addison_AUDITÉ.html (153 458) |
| **LOT** | **32,7 %** | **98,8 %** | 13 / 0 → 454 / 454 | 103 → 0 | 165 → 0 | | 12 fichiers |

Probabilités dans l’original : aucune balise `proba` (0 dans les 5 exports).

verif_v7 : OK sur les 12 fichiers. Les contrôles couvrent l’absence de script, d’img, de CSS externe et de `title=`, ainsi que FIN_FICHIER, le glossaire des sigles et la mention « contenu produit par IA, non validé cliniquement ». La police est Atkinson Hyperlegible.
Tailles : toutes entre 90 et 200 Ko. La SSP est découpée en _a/_b, car elle dépasse 200 Ko d’un seul tenant.
Contraste (outils/contraste.py, chemins absolus, `.proba` incluse) : 0 élément sur les 12 fichiers. Les probabilités utilisent `.proba{color:#C8102E;font-weight:700}`, sans halo. Le fond bleu ciel pâle est appliqué par le pipeline.
Toutes les fenêtres d’examen cliquables ont 2 onglets (Principe / Interprétation). Neuf examens étaient inclus dans un titre de fenêtre non-examen (DX1, DX4, DX5, DX7, DX10) : les titres ont été reformulés.
Les occurrences non cliquables restantes se trouvent dans le glossaire des sigles, comme dans LOT_003.

Écart résiduel connu : une phrase jugée « creuse » par style.py (« La fenêtre sérologique peut la rendre faussement rassurante ; ») vient du fragment VIH de bibliotheque_examens/. Elle n’a pas été modifiée (bibliothèque en lecture seule) et apparaît 1 à 6 fois par fichier.

## Règles appliquées
- Ordre anatomie → physiologie → physiopathologie → clinique → examens → traitement, le pourquoi d’abord.
- Phrases verbales ≤ 30 mots ; mot courant + terme exact.
- Chiffres sourcés, sources suisses d’abord (OFS, Obsan, OFSP, mediX, SKIPOGH, HypnoLaus, CoLaus), jamais inventés. Un chiffre non sourcé de l’original est retiré ou marqué « non retrouvé ».
- Prévalences comparables : tableau 1 en prévalence pour 100 000 habitants en population générale (commun aux 11 cours). Le tableau 2 (% des patients fatigués en premier recours, Stadje 2016) est séparé et nommé comme autre population.

## Corrections de fond (synthèse ; détail dans PROGRESS.md)
- **SSP**
  - Plaintes de fatigue chez 11–33 % des patients de premier recours (RMS 2006), au lieu de « 10–20 % des consultations ».
  - Cause trouvée chez 50–60 % des patients (RMS 2015), au lieu de 30–40 %.
  - Les « critères OMS » de la fatigue chronique n’existent pas : remplacés par IOM 2015 et NICE 2021.
  - Le pacing n’est pas une activité physique graduée ; le NICE déconseille l’activité physique graduée.
  - Néoplasie et insuffisance cardiaque terminale retirées de la liste des urgences.
  - Benzodiazépines : aggravation des apnées, et non « arrêts respiratoires fatals ».
  - Bloc 2 : pourcentages et sources non retrouvés remplacés par des prévalences sourcées de même unité.
- **DX.1** : Maltofer® est du fer ferrique ; l’hepcidine reste élevée environ 24 h ; plus de dépistage systématique en grossesse sans anémie ; chiffres suisses sourcés (Zurich 22,7 % / 2,2 %).
- **DX.2** : Obsan 9,8 % ; MonAM 30,3 % ; Job Stress Index 28,2 % ; burn-out QD85 (non classé comme maladie) ; PLAFA ; Spravato®.
- **DX.3** : règle OPAS de la polygraphie ; pression en cmH₂O ; Inspire® ; AD109 non autorisé ; HypnoLaus 49,7 % / 23,4 % ; Benjafield.
- **DX.4** : iodation du sel ; Novothyral® (T4 + T3) ; Garmendia 4,94 % / 0,62 % ; seuil ETA de 70 ans ; hydrocortisone avant lévothyroxine si insuffisance surrénale.
- **DX.5** : rash sous amoxicilline 29,5 % ; critères de Hoagland ; vaccins EBV en phase 1–2 ; Dubbo 12 % ; prednisone réservée aux complications ; affirmation « OFSP » sur le test VIH corrigée.
- **DX.6** : B3 non pathognomonique ; CHAMPIT = facteurs de décompensation ; fréquence cardiaque cible < 70/min ; seuils de K⁺ des antagonistes minéralocorticoïdes ; Entresto® 24/26 ou 49/51 mg ; omecamtiv non autorisé ; fer IV selon ESC 2023, HEART-FID neutre, AFFIRM-AHF.
- **DX.7** : SKIPOGH 10,4 % au lieu de « 800 000 » ; seuils KDIGO ; Payne peu fiable ; produit de contraste iodé non contre-indiqué de façon absolue ; PAS < 120 ; Hb sous ASE 100–115 g/L ; iSGLT2 dès DFGe ≥ 20 ; finérénone 10/20 mg ; metformine selon le DFGe.
- **DX.8** : 42 750 cas par an (OFS) ; cancer chez 0,6 % des patients fatigués ; CRAB et SLiM séparés ; Troisier non pathognomonique ; dexaméthasone 4 mg 2×/j ; méthylphénidate pas mieux que le placebo ; dépistage du côlon de 50 à 69 ans.
- **DX.9** : malaise post-effort cardinal, non pathognomonique ; Lim 0,68 % ; mécanismes présentés comme hypothèses ; IOM et NICE distingués ; critères HRS du POTS ; activité physique graduée déconseillée ; PACE contesté ; pas de recommandation suisse.
- **DX.10** : seuil du cortisol avec les dosages récents ≈ 390–415 nmol/L ; fludrocortisone 50–100 µg ; crise : 100 mg IV puis 200 mg/24 h ; règles de stress ; Efmody® autorisé pour l’hyperplasie congénitale, pas pour l’Addison ; SSED et rapport Na/K retirés.

## Outils (aucune écriture dans outils/ ni bibliotheque_examens/)
- Copies locales dans source/outils_local/ ; fragments d’examens supplémentaires dans source/bib_extra/ ; sigles ajoutés dans outils_local/sigles_extra.py.
- decoupe_l.py reconnaît « SSP G4 · … ».
- Écritures hors LOT_004 : les outils d’évaluation partagés écrivent work/LOT_004_AUDITE/. Une évaluation LOT_003 lancée par erreur en début d’audit a réécrit work/LOT_003_AUDITE/*, des fichiers dérivés et régénérables par LOT_003/source/eval.sh. Aucun fichier de corriges/LOT_003 n’a été touché.
- Originaux non modifiés ; aucune écriture Drive, aucun push GitHub, aucun message.

## Chiffres et doses à vérifier (contrôle humain requis)
- **SSP** : RMS 2006 11–33 % ; RMS 2015 50–60 % ; CoLaus 21,9 % ; normes de laboratoire (TSH 0,4–4 mU/L, CRP < 5 mg/L) ; réticulocytes vers J7–10 ; doses reprises des DX (Ferinject® 20 mg/kg max 1000 mg/sem., fer oral 100–150 mg un jour sur deux, lévothyroxine 1,6 µg/kg/j, sertraline 50–200 mg) ; prévalence « cancer dans les 10 ans ≈ 2600/100 000 ».
- **DX.1** : Zurich 22,7 % / 2,2 % (étude ancienne citée par mediX) ; formule de Ganzoni ; Ferinject® 1re perfusion ≤ 500 mg ; 15 mg/j chez l’âgé ; Vaucher 80 mg/j.
- **DX.2** : doses des ISRS et de la venlafaxine ; statut et remboursement de Spravato® ; seuils PHQ-9.
- **DX.3** : règle OPAS (≥ 4 h, 70 %) ; HypnoLaus ; Benjafield (≈ 425 millions modérés à sévères) ; tirzépatide (SURMOUNT-OSA) et statut suisse ; AD109.
- **DX.4** : Garmendia 4,94 % / 0,62 % ; seuil ETA de 70 ans ; iode 25 mg/kg de sel ; doses de lévothyroxine.
- **DX.5** : rash 29,5 % (Chovel-Sella) ; Dubbo 12 % à 6 mois ; Ebell 2016 (Se/Sp) ; phase des vaccins EBV.
- **DX.6** : VPN du NT-proBNP 94–98 % ; hausse de créatinine ≤ 30 % ; demi-vies ; remboursement de la réadaptation.
- **DX.7** : Nephrotrans® 500 mg 2–6/j ; doses de finérénone ; demi-vie des ASE ; statut suisse du roxadustat ; protéines 0,8 g/kg.
- **DX.8** : dose de dexaméthasone ; Fearon > 5 % ; pembrolizumab 200/400 mg ; programmes cantonaux de mammographie ; statut du ponsegromab.
- **DX.9** : CIM-10 G93.3 ; doses d’ivabradine, de propranolol, de midodrine et de naltrexone à faible dose ; « rémission plus fréquente chez l’enfant » ; source 41 utilisée pour le plan de vaccination (faible).
- **DX.10** : cause auto-immune 80–90 % ; crises 8,3/100 patients-années ; grossesse +20–40 % ; œstrogènes arrêtés 6 semaines avant le test ; remboursement LAMal du kit d’urgence ; Plenadren® en Suisse ; taux de positivité des anti-21-hydroxylase.
- Général : toutes les sources marquées « non relu » dans src_lot4.py, et toutes les posologies à contrôler dans l’AIPS (Swissmedic).

## Révision 1 — vérification utilisateur 24.10.2026

Source : `verif_utilisateur/LOT_004_synthese_utilisateur.md`. Chaque point a été recoupé de façon indépendante : PubMed E-utilities (auteurs, année, revue, sujet), informations professionnelles suisses (swissmedicinfo / ODDB), OFSP (Liste des spécialités), LiMA et communiqués du fabricant. Le détail se trouve dans `source/r1_verif_notes.md` ; le journal des modifications par cours, dans `source/r1_changes.md`. Toutes les modifications passent par les générateurs de `source/`.

### Vérification des PMID
| PMID | Référence | Résultat |
|---|---|---|
| 5413918 | Ganzoni, Schweiz Med Wochenschr 1970 (fer-dextran IV) | Confirmé (src 13) |
| 24783053 | Pearce, ETA, Eur Thyroid J 2013 | Confirmé (src 19) |
| 25266247 | Jonklaas, ATA, Thyroid 2014 | Confirmé (src 20) |
| 34447992 | McDonagh, ESC IC, Eur Heart J 2021 | Confirmé (src 25) |
| 25419882 | Hahner, JCEM 2015 (64 crises / 767,5 PA = 8,3/100 PA) | Confirmé (src 39) |
| 11556941 | Kroenke, PHQ-9, J Gen Intern Med 2001 (Se/Sp 88 % au seuil 10) | Confirmé (src 43) |
| 38912654 | Malhotra, SURMOUNT-OSA, NEJM 2024 | Confirmé (src 49) |
| 29032957 | Stoffel, Lancet Haematol 2017 (fer un jour sur deux) | Confirmé (src 11) |
| 16950834 | Hickie, Dubbo, BMJ 2006 | Confirmé (src 22) |
| 23589810 | Chovel-Sella, Pediatrics 2013 | Confirmé (src 23) |
| 32016310 | Wolf, JAMA 2020 (hypophosphatémie Ferinject vs Monofer) | Confirmé (src 74) |
| 28402245 | Stott, TRUST, NEJM 2017 | Confirmé (src 79) |
| 31269224 | Indiqué pour Nowak 2019 (Delphi suisse fer) | **Faux** : Heinisch 2019, correction tardive de la tétralogie de Fallot. Le bon PMID est **31269223** (src 73) |
| 24526250 | Younger, Clin Rheumatol 2014 (LDN) | PMID exact, mais **portée limitée** : revue de la douleur chronique (fibromyalgie, Crohn, SEP, SDRC), sans essai EM/SFC. Cité seulement pour le mécanisme et les doses, avec cette réserve (src 83) |

### Les 7 points demandés
1. **AD109, NDA et date PDUFA** : confirmé. Le communiqué Apnimed du 14.07.2026 indique que la FDA a accepté la NDA. La date PDUFA est le 28.02.2027 ; le nom proposé est Oxnimbi. Aucune autorisation n'a été trouvée en Suisse ni dans l'UE. Correction du cours : « atomoxétine-oxybutynine en phase III, sans autorisation » devient « aroxybutynine-atomoxétine, NDA acceptée, décision le 28.02.2027, non autorisée en Suisse et dans l'UE » (src 77).
2. **Spravato®, SL au 1.10.2025, 52 centres** : confirmé. L'OFSP indique une admission dans la SL au 1.10.2025, limitée dans le temps jusqu'au 30.09.2028. La liste OFSP compte 52 centres (valable dès le 01.10.2025).
   - Limitation : 18–74 ans, CGI-S ≥ 5, échec de ≥ 2 antidépresseurs et d'une augmentation, ECT non indiquée, refusée ou inaccessible, association à un antidépresseur oral.
   - Prescription par un psychiatre, avec garantie du médecin-conseil, pour 10 mois au plus.
   - Nuance : la SL affiche une première admission au 01.10.2022.
   - L'indication Swissmedic comprend aussi l'urgence psychiatrique, alors que la SL ne rembourse que la dépression résistante.
   - La catégorie « A » n'a pas été vérifiée.
3. **Limitation SL de Plenadren®** : confirmée. Plenadren® est dans la SL depuis le 1.6.2025, avec garantie de prise en charge par le médecin-conseil.
   - Indication : insuffisance surrénalienne primaire seulement, avec fatigue ou qualité de vie insuffisante après ≥ 6 mois d'hydrocortisone classique optimale.
   - Prescription par un endocrinologue d'un centre hospitalier formateur FMH (catégorie A/B) ; arrêt sans amélioration à 6 mois.
   - Posologie : 20–30 mg le matin. En cas de maladie intercurrente, la même dose est répétée 2–3×/j (toutes les 8 ± 2 h). Cette posologie a été lue dans un résumé de recherche de l'IP ODDB ; elle est à relire.
   - La catégorie de remise « B » n'a pas été vérifiée.
4. **Younger 2014, PMID 24526250** : le PMID est exact, mais il ne prouve rien dans l'EM/SFC. Voir le tableau.
5. **Ganzoni, PMID 5413918** : confirmé. La formule de l'IP suisse de Ferinject® (juin 2025) a aussi été vérifiée : Hb cible 15 g/dL, × 2,4, + 500 mg de réserves si > 35 kg, poids idéal (IMC 25) si obésité.
6. **Midodrine, max ≈ 30 mg/j** : confirmé par l'IP suisse de Gutron® (plus de 30 mg/j en 3 prises : non recommandé). Les doses de départ sont de 2,5 mg 2–3×/j ; la dernière prise a lieu ≥ 4 h avant le coucher.
7. **Ivabradine 2,5 mg dans le POTS** : **désaccord sur l'attribution**.
   - L'IP suisse de Procoralan® ne mentionne pas le POTS. Elle prévoit 5 mg 2×/j, 2,5 mg 2×/j si ≥ 75 ans, et un maximum de 7,5 mg 2×/j.
   - Dans l'insuffisance cardiaque, la fenêtre 50–60 /min sert à la titration de l'IP (pas la cible de l'ESC).
   - La dose de 2,5 mg dans le POTS relève de la littérature et de la pratique (HRS), hors indication. Le cours l'affiche ainsi.

### Autres points : confirmé / corrigé / désaccord
- **SSP (fiche)** — corrigé :
  - Ferinject® : « 20 mg/kg, max 1000 mg/sem » devient « besoin 500–2000 mg ; ≤ 20 mg/kg et ≤ 1000 mg par perfusion ; 1000 mg/sem ; surveillance 30 min » (IP CH).
  - Fer oral : « 100–150 mg un jour sur deux » devient « 60–100 mg un jour sur deux (ou 80–100 mg/j) ».
  - Lévothyroxine et sertraline : paliers précisés.
- **DX.1** — corrigé :
  - Ajout de l'Hb cible 15 et du schéma simplifié Swissmedic.
  - Exemple : « ≈ 1,4 g » devient « 1300 mg après arrondi de l'IP ».
  - Fer oral : 100–150 devient 60–100 mg un jour sur deux.
  - Ferinject® : la limite Swissmedic de 1000 mg par perfusion est distinguée du plafond clinique mediX de ≤ 500 mg en 1re perfusion. Ajout de l'hypophosphatémie liée au FGF-23 (Wolf 2020).
  - Nowak 2019 est cité avec le PMID corrigé 31269223.
- **DX.2** :
  - Corrigé : doses des ISRS et IRSN (escitalopram et citalopram plafonnés après 65 ans ; venlafaxine max 375 mg). Ces valeurs sont fournies par l'utilisateur et non revérifiées dans chaque IP.
  - Confirmé : les bandes PHQ-9.
  - Corrigé : Spravato®, voir le point 2.
- **DX.3** :
  - **Désaccord partiel** sur la règle « OPAS/LiMA 14.05 : ≥ 4 h sur ≥ 70 % des nuits ». La position LiMA des appareils de PPC est la 14.11, pas la 14.05. Elle renvoie aux recommandations SSSSC du 15.12.2020, qui exigent un contrôle d'efficacité et d'observance à 3 mois puis chaque année, sans seuil chiffré retrouvé. Le seuil 4 h / 70 % est la définition classique de l'observance et la règle des CMS (assurance publique américaine). Le cours affiche désormais cette cible d'observance, en précisant qu'elle n'est pas écrite dans la LiMA (à vérifier auprès des assureurs).
  - Corrigé : tirzépatide. Indication suisse (IMC ≥ 30, ou ≥ 27 avec une comorbidité, dont le SAOS) et posologie jusqu'à 15 mg. Le remboursement n'est pas revérifié.
  - AD109 : voir le point 1.
- **DX.4** — corrigé :
  - Cibles : « 0,4–4,0 ; très âgé ≈ 6 » devient « 0,4–2,5 (< 70 ans) ; 1–5 (> 70 ans) ».
  - Essai thérapeutique : « 3 mois, < 70 ans » devient « 3–6 mois, < 65–70 ans ».
  - Ajout : abstention si ≥ 70 ans et TSH < 10 (TRUST).
  - Nuance ETA : le résumé ne formule le « wait-and-see » que pour > 80–85 ans avec TSH ≤ 10. Entre 60 et 70 ans, l'ETA demande une évaluation individuelle du risque cardiovasculaire.
- **DX.5** :
  - Confirmé et précisé : Chovel-Sella (IC 18,5–42,6 ; 23 % sans antibiotique) ; Dubbo 12 % / 11 % à 6 mois.
  - Corrigé : « cohorte internationale » devient « australienne ».
  - **Désaccord partiel** : les taux de 27 % à 3 mois et de 9 % à 12 mois concernent le syndrome post-infectieux *provisoire*, pas les critères EM/SFC. Le cours les présente ainsi.
- **DX.6** — confirmé et complété : seuils 125 et 300 ng/L, VPN 94–98 %. Ajout des seuils d'inclusion selon l'âge 450 / 900 / 1800 ng/L, fournis par l'utilisateur (consensus ICON/HFA ; non relus dans le texte ESC 2021).
- **DX.7** — confirmé et complété : finérénone selon l'IP Kerendia®. Nouvelle indication suisse dans l'insuffisance cardiaque à FEVG ≥ 40 % (9.1.2026), avec une cible de 40 mg si DFGe ≥ 60. Nuance : dans l'insuffisance cardiaque, le traitement peut débuter jusqu'à K⁺ ≤ 5,0.
- **DX.8** — confirmé : pembrolizumab 200 mg toutes les 3 semaines ou 400 mg toutes les 6 semaines. La durée de perfusion de 30 min est fournie par l'utilisateur ; l'IP de Keytruda® n'a pas été relue.
- **DX.9** — corrigé : ivabradine (point 7), midodrine (point 6), LDN (départ 0,5–1,5 mg, mécanisme TLR4, réserve sur Younger 2014).
- **DX.10** — confirmé et complété :
  - Hahner : 64 crises en 767,5 PA ; décès 0,5/100 PA ; déclencheurs à ≈ 20 % chacun.
  - Plenadren® : voir le point 3.

### Reste à vérifier (Révision 1)
- Points fournis par l'utilisateur et non revérifiés :
  - doses maximales de chaque ISRS et de la venlafaxine ;
  - lévothyroxine 50–100 µg/j au départ chez l'adulte jeune ;
  - seuils NT-proBNP d'inclusion selon l'âge ;
  - durée de perfusion du pembrolizumab ;
  - titration de la LDN ;
  - fer oral 80–100 mg/j.
- Posologie de Plenadren® en maladie intercurrente : à relire dans l'IP complète.
- Catégories de remise de Spravato® (A) et de Plenadren® (B).
- Remboursement de la tirzépatide.
- Existence éventuelle d'un seuil chiffré d'observance de la PPC chez les assureurs suisses.

### Contrôles après Révision 1
- eval.sh : 98,8 % pour les 12 fichiers (seul 13.b, noté par un humain, reste ouvert). verif_v7 OK pour les 12 fichiers. contraste.py : 0 écart. Sigles non développés : 0 ; phrases > 30 mots : 0.
- Tailles : de 118 304 à 182 443 octets (toutes entre 90 et 200 Ko).
- MANIFEST.sha256 régénéré (12 fichiers, `sha256sum -c` OK). Le json orphelin du SSP non scindé, recréé par gen_ssp.py, a été supprimé.
