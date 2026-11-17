# LOT_219 — SPEC commune (PROFILES 2023, SSP O6.6 « issues related to family life such as divorce, single parenthood and reconstructed family »)

## Identité
- LOT_219 = PROFILES 2023, SSP **O6.6 — Vie familiale : divorce, monoparentalité, famille recomposée** (source : https://smifk-cims.ch/profiles-2023/ssps, consulté 2026-10-21).
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
- Conteneur `<div id="lot219-appel[A|B]-v5" style="font-family: sans-serif; line-height: 1.65; max-width: 980px; margin: auto;">`, h2 bleu #1a5276 bordure #2980b9, sous-titre gris.
- Chaque monographie = `<details open ...>` style du gabarit, `<summary>` « DX.n — Nom <span style="font-size:0.8em;color:#2e8b57;">badge</span> ».
- Grands titres `<p><strong>1. …</strong><br>` ; sous-titres en `<em>` ou `<strong><em>`.
- Fenêtres bio-mathématiques : `<details>` bordure gauche #2980b9 fond #ebf5fb, summary « 🔍 Fenêtre Interactive Bio-Mathématique N.k : … ».
- **CORRECTION** : ne PAS utiliser `<a href="#" title="…">` (inaccessible au toucher, saute en haut de page). Pour un terme interactif, utiliser un `<details>` en ligne :
  `<details class="t" style="display:inline;"><summary style="display:inline;cursor:pointer;color:#1f618d;text-decoration:underline dotted;">terme</summary><span style="display:block;margin:4px 0 8px;padding:8px;background:#f4f6f7;border-left:3px solid #1f618d;font-size:0.93em;">Définition / mécanisme. <em>Source : …</em></span></details>`
- Tableaux : `border="1" cellpadding="7" cellspacing="0" style="width:100%;border-collapse:collapse;..."` thead #d4e6f1 ; envelopper chaque tableau dans `<div style="overflow-x:auto;">` (lecture mobile).
- En fin de fichier : section « Sources » numérotée (titre, organisme, année, URL, date d'accès) et mention : « Contenu produit par IA à partir des sources citées ; non validé cliniquement par un médecin. »

## Fichiers du lot
1. LOT_219_Appel_A_V5_Ultra_Pedagogique_Plan_et_Liste.html — Bloc 1 monographie 14 points du SSP ; Bloc 2 liste DX.1–DX.10 ordonnée + badge + justification.
2. LOT_219_Appel_B_V5_Ultra_Pedagogique_Partie_1_DX.1_a_DX.2.html
3. LOT_219_Appel_B_V5_Ultra_Pedagogique_Partie_2_DX.3_a_DX.5.html
4. LOT_219_Appel_B_V5_Ultra_Pedagogique_Partie_3_DX.6_a_DX.7.html
5. LOT_219_Appel_B_V5_Ultra_Pedagogique_Partie_4_DX.8_a_DX.10.html

## Consigne de Vial (2026-10-21) — plan académique de repli et qualité des différentiels
11. **Plan de repli.** Quand le plan monographique en 14 points ne s'applique pas naturellement à une entité (SSP transversal, procédural, médico-légal, ou entité qui est une classe d'agents plutôt qu'une maladie), ne pas forcer : produire un **plan universitaire/académique** (I., II., III. ; A., B. ; 1., 2.) qui suit la logique propre du sujet, avec **de nombreuses fenêtres cliquables `<details>`** pour les détails (mécanismes, calculs, posologies, cadre légal, exemples). Annoncer en tête de la monographie, en une phrase, pourquoi ce plan est retenu. Les exigences de fond (sources, posologies suisses, bio-mathématique utile, guérison/recherche 2026, pièges d'examen) restent dues ; le lint accepte ce plan si la monographie contient la classe `plan-academique`.
12. **Différentiels de haut niveau.** Chaque DX doit dire ce qui le **distingue des autres DX** et des simulateurs non toxiques :
   - Appel A, Bloc 2 : outre la liste ordonnée, un **tableau comparatif des toxidromes/entités** (conscience, pupilles, FC/PA, FR, température, peau, péristaltisme, ECG, biologie clé, antidote) et un **algorithme discriminant** (quel signe ou examen fait basculer d'un DX à l'autre).
   - Chaque monographie Appel B : rubrique « Diagnostics différentiels discriminants » au point 4 (ou section équivalente), avec les 3–4 confusions les plus dangereuses, le signe ou examen qui tranche, et le piège d'examen associé ; inclure les causes non toxiques qui miment l'intoxication (hypoglycémie, AVC, méningo-encéphalite, état de mal non convulsif, sepsis, hypothermie, traumatisme crânien, troubles métaboliques).
   - Associations et co-ingestions (alcool + benzodiazépines + paracétamol) explicitement traitées : toujours doser paracétamol et éthanol dans l'ingestion volontaire inconnue si la source le soutient.
13. **Fenêtres des thèmes transversaux : très riches et très précises.** Pour tout thème transversal (cadre légal, éthique, communication, organisation des soins, prévention, santé publique, évaluation du risque suicidaire, capacité de discernement, déclaration, Tox Info Suisse, médecine légale), chaque fenêtre `<details>` contient : définition exacte ; base légale ou déontologique précise (article et alinéa via Fedlex, directive ASSM ou code FMH avec année) ; conditions d'application et exceptions ; procédure pas à pas ; exemple clinique concret avec la décision correcte ; erreur fréquente ou piège d'examen ; source datée. Une fenêtre transversale ne se limite jamais à une phrase.











## Spécificités LOT_219
Arbitrages contraignants (agent de recherche, 22.10.2026). Dossier de preuves : `evidence.json` (48 sources [S1]–[S48], 320 affirmations sourcées). Tout chiffre absent de ce dossier s'écrit « donnée non trouvée dans les sources consultées ».

**A. Plan retenu.**
- Appel A (monographie du SSP) : **plan académique** (I./A./1.), conteneur avec la classe `plan-academique`, annoncé en une phrase : O6.6 est une situation psychosociale et médico-légale, non une maladie ; plaquer une physiopathologie serait faux (PROMPT V6 § 5 bis). Les contenus des clés p1–p14 de `ssp` restent tous à couvrir (définitions, démographie OFS, cadre légal, évaluation, drapeaux rouges, outils, arbre, A-B-C-D, prévention, points clés, pièges).
- Appel B : DX.1, DX.2, DX.4 et DX.9 en **14 points cliniques** ; DX.3, DX.6, DX.7 et DX.8 en **14 points transposés CanMEDS** (§ 5 bis) ; DX.5 et DX.10 en **plan académique** (`plan-academique`), justifié en une phrase (situations purement juridiques).
- Contenu des « toxidromes » de la règle 12 générique : **sans objet**. Le tableau comparatif de l'Appel A compare : personne qui consulte, signe ou indice clé, outil/examen clé, base légale, danger principal, conduite immédiate.

**B. Les 10 DX (ordre contraignant : fréquence suisse pondérée par la gravité).**
1. DX.1 Trouble de l'adaptation de l'adulte après séparation : badge « 1er rang — fréquence non quantifiée (Suisse) » ; 1–2 % en population générale [S22].
2. DX.2 Épisode dépressif et crise suicidaire : 12,5 % de pensées suicidaires chez les parents seuls [S6] ; RR 3,18 (séparé/divorcé, 35–65 ans) [S29].
3. DX.3 Violence dans le couple en phase de séparation (harcèlement, enfants co-victimes) : 22 066 infractions en 2025 [S14].
4. DX.4 Enfant/adolescent face à la séparation parentale : 13 % des parents d'enfants mineurs séparés [S3].
5. DX.5 Conflit parental de haute intensité : autorité parentale, consentement, information (CC 275a), certificats (CP 318) : 61 % d'autorité conjointe [S3].
6. DX.6 Mise en danger de l'enfant et avis à l'APEA (CC 307, 314c–e) : 2380 enfants maltraités traités en 2025 (secondaire) [S21].
7. DX.7 Monoparentalité : précarité, renoncement aux soins, épuisement parental : 16 % des ménages familiaux [S3] ; pauvreté 10,6 % [S5].
8. DX.8 Famille recomposée et rôle légal du beau-parent (CC 299, 278 al. 2, 264c) : 6 % des enfants [S3].
9. DX.9 Mésusage d'alcool dans la crise familiale : ~4 % de consommation chronique à risque [S41].
10. DX.10 Déménagement et enlèvement parental international (CC 301a, CLaH 80, LF-EEA, CP 220) : 154 cas OFJ en 2025 [S46].

**C. Conflits de sources et arbitrages.**
- Pauvreté monoparentale : 19,3 % (SILC 2018, OFS 2021) et 10,6 % (2023, CSIAS citant OFS) : présenter les deux avec l'année ; ne pas écrire « baisse ».
- Aide sociale monoparentale : 18,6 % et 19,6 % dans le même document CSIAS → écrire « 18,6–19,6 % ».
- Dépression : la référence suisse est SSAD/SSBP/SSPP 2016 [S24] mise à jour 2024 (compte rendu [S25], texte intégral non publié) ; la conduite graduée (faible intensité → psychothérapie à 14 jours → réévaluation après 6–10 séances ; non-réponse à 4 semaines d'antidépresseur) est citée comme « mise à jour suisse 2024 (compte rendu) ».
- Médicaments : IP suisses priment. Zoloft® (sertraline) 50 mg/j, paliers ≤ 50 mg/semaine, max 200 mg/j ; Child A–B dose ÷ 2 au moins, Child C contre-indiqué ; **non recommandé pour la dépression < 18 ans** [S26]. Cipralex® 10 mg/j, max 20 mg/j, ≥ 6 mois ; ne pas utiliser < 18 ans ; CI QT long [S27]. Campral® 2 cp de 333 mg 3×/j, 6–12 mois, CI créatinine > 120 µmol/L et allaitement [S43]. Naltrexin 50 mg/j ≥ 3 mois, CI opioïdes/Child B–C [S44]. Antabus® 2 cp 400 mg/j × 3 j puis ½ cp/j ou 1 cp/2 j, **CI risque suicidaire, psychose, grossesse** [S45]. Aucun médicament n'est indiqué pour le trouble de l'adaptation [S22, S26].
- Obligation versus droit d'aviser : le médecin a un **droit** d'aviser l'APEA (CC 314c al. 2) ; l'**obligation** de CC 314d ne vise que les professionnels non soumis au secret pénal ; ne jamais écrire que le médecin est obligé.
- « Aliénation parentale » : terme controversé (source de presse [S48]) ; ne pas le présenter comme diagnostic.
- Alinéas CC 298 al. 2bis/2ter et 301 al. 1bis : contenu vérifié sur Fedlex, numéro d'alinéa à revérifier (l'extraction ne l'affiche pas).

**D. Seuils et chiffres clés (à reprendre tels quels).**
- Divorces 2025 : 15 800 ; indicateur de divortialité 39,1 % ; 35 900 mariages [S2].
- Trouble de l'adaptation (CIM-11) : début ≤ 1 mois après le stresseur ; préoccupation + échec d'adaptation ; résolution attendue ≤ 6 mois après la fin du stresseur [S22].
- PHQ-9 ≥ 10 : Se 88 %, Sp 88 % ; 5/10/15/20 [S28]. AUDIT ≥ 8 : 92 %/94 % [S42]. Échelles suicidaires : VPP 5,5 % [S31]. Plan de sécurité RR 0,570, NNT 16 [S32]. ASSIP 8,3 % vs 26,7 % [S33]. Numéros 143 et 147 [S34].
- Violence : poursuite d'office des lésions simples, voies de fait réitérées et menaces entre (ex-)conjoints/partenaires jusqu'à **1 an** après le divorce ou la séparation (CP 123 ch. 2, 126 al. 2, 180 al. 2) ; CP 55a suspension ≤ 6 mois ; CP 181b harcèlement depuis le 1.1.2026 ; CC 28c bracelet ≤ 6 mois renouvelables ; strangulation OR 7,48 [S35] ; tentatives d'homicide dans le couple : ~1/3 séparés, dont ~1/2 depuis < 6 mois [S15].
- Enfants : 13 % en ménage monoparental, 6 % en famille recomposée ; 5,9 jours/mois chez le second parent ; 1/10 des parents non gardiens sans contact [S3] ; privation 14,1 % vs 3,4 % [S4] ; OR à long terme du divorce parental : dépression 1,29, tentative de suicide 1,35, idées suicidaires 1,48, alcool 1,43 [S36].
- Capacité de discernement du mineur : pas de limite fixe ; repères ≈ 7 ans (bénin), 12 ans (simple), 16 ans (complexe/long) [S18] ; mineur capable = décide seul et secret envers les deux parents [S19].
- CLaH 80 : jusqu'à 16 ans ; < 1 an = retour immédiat ; décision en 6 semaines ; exceptions art. 13 [S10] ; 80 % de mères ravisseuses, âge moyen ≈ 7 ans [S46].
- Épuisement parental Suisse : 7,1 % (seuil 86), 4,8 % (seuil 92), 4,6 % pondéré [S39].

**E. Lacunes connues (à signaler, pas à combler de mémoire).** Nombre annuel d'enfants mineurs concernés par un divorce (OFS) ; prévalence suisse du trouble de l'adaptation ; texte OMS CIM-11 non lu directement ; texte intégral suisse dépression 2024 ; code FMH ; pauvreté monoparentale 2024 ; données suisses sur les familles recomposées et le risque lié au beau-parent ; instruments cantonaux d'évaluation du danger ; part des ex-partenaires dans la violence domestique 2025 ; essais NCT ; AUDIT-C suisse ; statut du concubin pour représenter l'enfant du partenaire. Ces lacunes vont dans HELP après audit.
