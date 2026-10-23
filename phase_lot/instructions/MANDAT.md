> **Consigne humaine prioritaire, mise à jour le 24.10.2026 :** Thunder est l’utilisateur humain (compte GitHub vialdjoukang-spec), et non une IA Grok. ChatGPT rédige A et B. Rien n’est transmis, déposé ou publié sans sa validation humaine explicite du livrable concerné. Les rédactions restent locales jusque-là. LOT_Tunder, sur main, sert à la réception pour relecture après fusion effective de la PR272 et autorisation de transmission. LOT_Finaux_Audités reste réservé aux cours acceptés. Aucun agent ne fabrique une approbation humaine ni ne l’infère d’un commit sur le compte partagé. Les anciennes mentions d’un compte externe/IA ou d’une publication automatique ci-dessous sont remplacées par cette consigne.

# Organisation pratique

## Dépôt et isolation

Dépôt vérifié : `vialdjoukang-spec/organigramme-examen-federal`. Branche de contrôle nouvellement créée : `Organigramme`, issue de main `a02bc1cd18437a2d78db99b235b6496b1d196288`.
Les anciennes données se trouvent notamment sur `claude/zealous-noether-c3jut5`, dossier `claude/LOT Organigramme`, et dans Drive. Ne rien supprimer.

Branches par LOT : `lot/001/a`, puis `lot/001/b1` à `b5`, puis `lot/001/candidat`. Reproduire pour 002–010 uniquement quand le LOT devient actif. Tous les auteurs partent du même commit A terminé ; ils écrivent des chemins disjoints. Le coordinateur ne fait pas de fusion globale aveugle des branches : il importe les fichiers réservés et vérifie leurs SHA-256. Cela évite les conflits de contenu entre auteurs respectant le contrat ; des changements externes restent possibles et sont détectés par comparaison de la tête distante, jamais écrasés.

Chemins des auteurs : `LOT_Candidats/LOT_001/A/` et `LOT_Candidats/LOT_001/B1/` ... `B5/`. Les auteurs y déposent HTML, evidence.json, HELP.json, checkpoint.json. Aucun répertoire de candidat dans la branche canonique. Tunder relit la branche candidat agrégée ; son audit référence le commit et les empreintes de chaque HTML. Les noms et l'ordre des dix DX sont gelés dans selection.json. Une modification de sélection invalide les travaux B qui en dépendent.

## Deux phases par rôle

Recherche high : ouvrir les sources primaires, noter titre, version, date, passage, URL, portée, unités ; vérifier l'existence de versions plus récentes. Rédaction medium : reprendre ce fichier de preuves, rédiger une monographie entière à la fois, sans recherche de mémoire ni données ajoutées sans preuve. Si une lacune exige une nouvelle recherche, retourner à high. Les outils de sous-agents ne modifient pas le niveau à chaud : le coordinateur relance une invocation medium avec le même rôle et sa passation, consigne les deux identifiants, puis clôt la précédente.

## Outils réellement disponibles

- MCP Google Drive : lecture des prompts et inventaire historique. Aucun nouveau cours n'est écrit dans Drive.
- MCP GitHub : lecture/écriture et vérification des commits ; CLI Git/gh en complément lorsque le connecteur n'offre pas l'opération nécessaire.
- MCP Parallel Search : recherches et ouvertures primaires ; objectifs indépendants en parallèle, variantes liées dans une requête ; ne pas inventer model_name (champ facultatif).
- Scripts Python standard : grille 14 points, suivi structurel, registre de liens, empreintes, contrôle de l'audit et état de la file.
- Skills appliqués : Google Drive (découverte), cloud-environment-runtime (réseau) ; dépôt ARSENAL et ssp-verite (preuves, concision et contrôles). Aucun skill ne garantit l'absence d'erreur médicale.

## Contrat HTML et contrôles

Chaque monographie utilise `<article data-monograph="G1">` ou `DX.1`, et chaque point un `<section data-point="1">` jusqu'à 14. Les sous-parties utilisent data-subpoint="9.a" à "9.d" et "11.A" à "11.D". Les titres restent strong et les sous-titres em. Les tableaux sont enveloppés, le fichier autonome se termine par FIN_FICHIER ; 90–200 Ko selon V7, jamais gonflé pour atteindre une taille. Si le contenu nécessaire excède la limite, scinder aux points complets en conservant la traçabilité. Un fichier trop court reste candidat non conforme, même s'il est utile.

`validate.py` produit les écarts structurels et la liste exhaustive des questions du §6.1 à traiter. `--watch` observe les changements, écrit un rapport à chaque modification et le rédacteur le relit après chaque point. Il ne retouche aucun fait médical. Le rapport porte explicitement semantic_validation=false.

`links.py` sonde un registre fini d'URL CH/UE/internationales ; il donne statut, redirection, date et erreur. HTTP 200 ne prouve ni pertinence ni recommandation à jour. Le script ne prétend pas parcourir toutes les sociétés savantes du monde. Ajouter les liens propres à chaque sujet puis les sonder ; les sites bloqués ou illisibles restent déclarés.

## Audit Tunder et passage au final

Thunder est l’utilisateur humain, identifié par sa réponse dans le chat et le compte GitHub `vialdjoukang-spec` (droits admin vérifiés). Il vérifie les informations médicales, les 14 parties et la langue : français soutenu, clair, compréhensible, avec connecteurs logiques. ChatGPT ne réalise pas ni ne signe cet audit à sa place.

Une validation humaine explicite doit désigner le livrable exact et ses empreintes. Le coordinateur la consigne avec sa référence réelle ; une branche verte, un commit du compte partagé ou un champ JSON ne prouvent pas à eux seuls une intervention humaine. Le script audit_gate.py refuse tout passage si human_approval est absent ou ne correspond pas au candidat et aux fichiers. Aucun automate ne remplit cette approbation.

Le dossier de réception est `main:LOT_Tunder/`, créé par la PR272. Ne rien y déposer avant fusion constatée et autorisation humaine de transmission. La source finale `LOT_Finaux_Audités` reste réservée aux cours ensuite acceptés par Thunder. Le rapport V7 peut être conservé dans le dépôt, mais son attribution au compte partagé ne démontre pas à elle seule l'identité humaine : la validation explicite reste nécessaire.

## Reprise et cadence

Le checkpoint persiste sur GitHub après chaque fichier. Une relance lit config/file.json, n'active qu'une seule production et reprend le dernier point complet. Production finie : marquer PRODUIT_EN_ATTENTE_AUDIT et activer le suivant ; cours audité et déposé : FINAL_AUDITE. Une interruption laisse le travail ACTIF, jamais terminé implicitement.

Une automatisation ChatGPT horaire peut reprendre ce mandat après lecture de GitHub. Son enregistrement ne prouve pas encore un premier réveil ; conserver l'heure de prochaine exécution. La fréquence minimale est une heure. Le workflow GitHub de sonde à 30 minutes est fourni séparément et doit exister sur main pour être planifié ; une exécution de sonde ne démarre pas une IA. Aucun endpoint public de réveil de ce chat ni identité xAI n'est actuellement configuré. Ne pas injecter de secret dans le dépôt ni dans le chat.
