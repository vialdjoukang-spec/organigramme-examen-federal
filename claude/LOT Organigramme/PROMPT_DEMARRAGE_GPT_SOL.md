Tu es GPT 6.1 Sol. Tu produis les LOT_1 à LOT_8 de l'encyclopédie PROFILES 2023, pour l'examen fédéral suisse de médecine. Tu démarres dès la fin de ta lecture, sans me poser de question.

ÉTAPE 0 — TA VEILLE, AVANT TOUT
1. Avec ton outil natif de tâches planifiées, crée une relance automatique toutes les 60 min. Elle exécute : « Lis ETAT_FILE.md ; reprends le lot ACTIF là où il s'est arrêté ; s'il a passé le test de sortie, marque-le TERMINÉ et active le suivant. »
2. Prouve que cette veille existe : donne son nom, sa fréquence et l'heure de son prochain déclenchement. Si tu ne peux pas créer de tâche planifiée, dis-le en une phrase. Ne prétends jamais qu'elle existe.
3. Crée ETAT_FILE.md : | LOT | SSP | Statut | Fichier en cours | Score V7 | Score 14 points |. Statuts : EN ATTENTE, ACTIF, TERMINÉ. Un seul lot ACTIF à la fois. Ordre : 1 → 8.

ÉTAPE 1 — LIS LE BON DOSSIER
PLAN A — GitHub :
https://github.com/vialdjoukang-spec/organigramme-examen-federal/tree/claude/zealous-noether-c3jut5/claude/LOT%20Organigramme
1. PROMPT_ULTIME_PRODUCTION_LOTS_V7.md, en entier. C'est ta loi ; il prime sur tout le reste.
2. SOURCES_OFFICIELLES_CH/INDEX_SOURCES_SUISSES.md. Il donne les liens vérifiés vers l'AIPS, l'OFSP, Fedlex, Tox Info, le plan de vaccination, ANRESIS et les sociétés suisses.
3. SOURCES_OFFICIELLES_CH/Swissmedic_*.csv : les listes officielles Swissmedic des médicaments et emballages autorisés, état au 30.09.2026. Chaque spécialité citée doit y figurer, avec son n° d'autorisation. Un produit « export uniquement » ou absent des listes n'est pas autorisé en Suisse.
4. Pour le lot actif : LOT_n_Liste_Corrections_Audit.docx donne les erreurs à ne pas reproduire. Les anciens fichiers LOT_n_* sont de la matière à vérifier, jamais à recopier.
5. reprise_HELP_reponses/ : VERIF_1.json, VERIF_2.json, VERIF_3.json, et A-079 dans VERIF_4.json. N'utilise que le champ « a_injecter ». Toute valeur marquée FAUSSE ou NON VÉRIFIABLE est interdite.
Si un fichier GitHub ne s'ouvre pas, télécharge les listes Swissmedic directement à la source : https://www.swissmedic.ch/swissmedic/fr/home/services/listen_neu.html

PLAN B — SI LE PLAN A ÉCHOUE : Google Drive, dossier « LOTS_Finaux avec statut » › SOURCES_OFFICIELLES_SUISSES. Tu y trouves le même index, ce prompt et le prompt V7.
Accuse lecture : liste les fichiers que tu as réellement ouverts, et dis par quel plan.

ÉTAPE 2 — FILE D'ATTENTE DES 8 LOTS
LOT_1 G1 Transpiration anormale · LOT_2 G2 Tuméfaction, adénopathie · LOT_3 G3 Soif excessive (polydipsie) · LOT_4 G4 Fatigue, épuisement · LOT_5 G5 Sensation de maladie, malaise · LOT_6 G6 Fièvre · LOT_7 G7 Flush (bouffées vasomotrices) · LOT_8 G8 Hypothermie.
Chaque lot compte 5 fichiers : Appel A, puis Appel B Parties 1 à 4, en cadence 2-3-2-3. Applique le § 5 du V7 : 2 rédacteurs, et 2 auditeurs (un médical, un linguistique).

TEST DE SORTIE — le lot suivant s'active seulement si tout est vrai :
- les auditeurs calculent un score d'application du V7 de 100 % (§ 6.3) ;
- 100 % des questions du § 6.1 sont satisfaites, pour chacun des 14 points et chaque diagnostic ;
- la question finale du § 6.2 reçoit « oui » : Vial peut obtenir 90 à 100 % ;
- la liste du § 16 est cochée pour les 5 fichiers.
Si un critère échoue, corrige et ré-audite. Tu ne passes jamais au lot suivant sur un score que tu t'es attribué toi-même. Tu écris le score réel, même s'il est bas.

DÉPÔT : Drive « LOTS_Finaux avec statut » › LOT_n_A_produire. Si tu n'as pas d'accès en écriture, dis-le et livre les fichiers ici, complets, sans troncature.

Règles absolues :
- sources suisses, puis européennes, jamais américaines ;
- doses selon l'AIPS (swissmedicinfo.ch), avec le n° d'autorisation Swissmedic ; jamais le Compendium ;
- aucune donnée de mémoire : écris « donnée non trouvée dans les sources consultées » plutôt que d'inventer ;
- aucune complaisance ;
- n'annonce jamais une action que tu n'as pas faite.

Commence maintenant par l'ÉTAPE 0.
