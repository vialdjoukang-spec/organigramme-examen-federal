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

Configurer le vrai login de Tunder dans config/policy.json après vérification des droits. Ne pas accorder l'accès à un compte supposé. Le rapport suit config/audit.schema.example.json : identité de l'auditeur, commit candidat, empreintes, scores à chaque question pour chaque monographie, justification des sans objet, contrôle médical et linguistique, zéro critique, verdict accepté. Les scores proviennent de Tunder, jamais du script ou de l'auteur. Le seuil opérationnel retenu est 100% des questions applicables, conformément au prompt de démarrage ; le V7 seul fixe 90% comme minimum de dépôt.

`audit_gate.py` vérifie le rapport et l'attribution du commit d'audit via GitHub (login relié par GitHub et signature vérifiée), puis prépare une copie finale dans une destination vide. Il ne pousse rien. Le coordinateur recontrôle rapport et CI avant dépôt dans `LOT_Finaux_Audités/LOT_001_G1/` sur Organigramme. Si Tunder utilise le même compte GitHub que le coordinateur, l'identité distincte de l'IA n'est pas prouvée : conserver un journal externe vérifiable, ne pas annoncer l'indépendance sur la seule identité du compte.

## Reprise et cadence

Le checkpoint persiste sur GitHub après chaque fichier. Une relance lit config/file.json, n'active qu'une seule production et reprend le dernier point complet. Production finie : marquer PRODUIT_EN_ATTENTE_AUDIT et activer le suivant ; cours audité et déposé : FINAL_AUDITE. Une interruption laisse le travail ACTIF, jamais terminé implicitement.

Une automatisation ChatGPT horaire peut reprendre ce mandat après lecture de GitHub. Son enregistrement ne prouve pas encore un premier réveil ; conserver l'heure de prochaine exécution. La fréquence minimale est une heure. Le workflow GitHub de sonde à 30 minutes est fourni séparément et doit exister sur main pour être planifié ; une exécution de sonde ne démarre pas une IA. Aucun endpoint public de réveil de ce chat ni identité xAI n'est actuellement configuré. Ne pas injecter de secret dans le dépôt ni dans le chat.
