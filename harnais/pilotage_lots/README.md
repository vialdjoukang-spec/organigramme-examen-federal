# Reprise de la vague inverse V8

**TRANSITION / ARRÊT demandé par Vial.** Ce prototype n’est ni contre-audité ni déployé. Son registre est sauvegardé avec `paused` et `stop_requested:true`. La branche de pilotage distante n’a pas été créée et la tâche GPT horaire n’a pas été installée. Une reprise par Codex exige un nouveau lancement explicite; aucune activité de fond n’est présumée.

Mandat Vial du25octobre2026 : avancer de LOT226 vers001, avec deux agents, sous V8 et harnais. La préférence de cadence confirmée est GitHub5min + GPT1h. Ce dispositif ne promet ni un temps réel GitHub, ni une session GPT permanente, ni une consommation intégrale mesurable du forfait.

## Deux exécutants distincts

Le workflow existant `harnais-5min.yml` teste réellement les trois outils et lit le registre sur `pilotage/lots-inverses-v8`, fichier `harnais/pilotage_lots/etat.json`. Le contrôleur lit les fichiers de chaque branche à un SHA fixe, vérifie les cinq HTML et les preuves de validation. Il ne modifie aucun lot, ne renouvelle aucun heartbeat et ne poste aucun message. Ses permissions restent `contents:read`. Un bilan de brouillon à corriger n’est pas un échec technique du moteur et n’est jamais une validation clinique.

La tâche GPT horaire reprend le contenu et les audits selon `REPRISE_GPT.md`. Son existence, son identifiant et son activation doivent être confirmés par l’outil natif, pas par ce README. Elle reconstruit son contexte depuis GitHub et ne suppose pas que les fichiers temporaires de cette session seront conservés. Elle ne peut utiliser que les outils et crédits réellement disponibles lors du passage. Le script GitHub ne constitue pas une deuxième IA et ne consomme aucune API OpenAI payante.

## Registre, bail et progression

Un coordinateur acquiert un bail réel de20minutes avant toute mutation de pilotage. La fonction `acquire` produit un nouvel état; l’enregistrement doit utiliser un commit enfant du SHA lu et `update_ref(expected_sha=SHA_lu, force=false)`. Un refus de comparaison impose une relecture, jamais un force-push. Un détenteur concurrent non expiré interdit la reprise. Un bail expiré ne dispense pas de vérifier l’absence de session effectivement active et les preuves de travail récentes. Renouveler seulement pendant une action réelle; aucune boucle de watcher ne produit de preuve d’activité.

La fonction `advance` n’autorise le prochain lot que si le lot courant a réellement passé ses portes. Elle exige un inventaire distant complet et récent de toutes les branches et PR pouvant réserver un numéro. L’agent doit le collecter sans tronquer la pagination; une erreur d’accès rend l’inventaire incomplet. Les LOT001–012 sont protégés par défaut à cause des autres vagues. Le contrôleur ne supprime pas ces réservations et ne reprend pas les branches d’un autre auteur. Une réservation sans arbitrage reste bloquante.

Les lectures périodiques portent sur les lots actifs, afin de borner les appels API. Les clôtures passées sont affichées comme historiques enregistrés, avec leur SHA de validation, sans prétendre les avoir toutes réauditées à chaque passage. Une modification ultérieure d’un lot clos nécessite une nouvelle validation de cette version.

`status=paused`, `stop_requested=true` ou `quota_exhausted` empêche toute nouvelle affectation. Un arrêt explicite de Vial prime toujours. Les crédits restants ne sont pas accessibles via ce dispositif; aucun solde ni heure d’épuisement n’est inventé. Un quota réellement refusé arrête proprement le travail au dernier checkpoint, sans changement de compte, achat, API payante ou contournement.

## Preuves nécessaires pour chaque HTML

Le fichier propre au lot `VALIDATION_V8.json` doit contenir `schema_version:1` et `files`, avec les clés `A,B1,B2,B3,B4`. Chaque entrée contient les quatre attestations suivantes. Elles sont liées au SHA256 exact du HTML. Les rapports restent dans le même lot et leurs octets sont relus pour vérifier leur empreinte.

- `medical` et `linguistique` déclarent `role`, `auditor_id` distinct de tous les auteurs, `score` compris entre90et100, `critical_count:0`, `full_read:true`, `file_sha256`, `checked_at`, `report_path`, `report_sha256`. L’attestation médicale exige aussi `critical_sources_read:true`. Un rôle manquant, un score documentaire partiel ou une correction non relue ne passe pas automatiquement.
- `visual` déclare `width_px:390`, `performed:true`, `authorized_environment:true`, la date, le rapport et les empreintes. La politique du navigateur ayant refusé le rendu des lots dans cette session, aucune reprise ne doit tenter le même résultat par un contournement. Une vraie preuve obtenue de façon autorisée est nécessaire; ne jamais fabriquer la case verte.
- `delivery` déclare `destination:"Drive Finaux"`, `remote_file_id`, `verified:true` et les mêmes champs de date et d’empreintes. Elle n’est produite qu’après les deux Appels complets et validés et une vraie vérification de la copie HTML, sans conversion, octet pour octet.

Ces attestations restent des preuves publiées par les agents, non des signatures cryptographiques d’un médecin. Le code détecte des incohérences, pas la véracité scientifique de chaque phrase. Il ne valide jamais cliniquement par le seul fait qu’un JSON dit vrai. Les agents doivent lire réellement les sources et rapports, conserver l’indépendance des audits, les limites et la mention de non-validation humaine.

## État initial honnête

LOT226 et225 disposent des cinq fichiers brouillons. Les audits B226 complets et B225 P4 manquent; les scores A225 et plusieurs B225 restent sous90. QA390 n’est pas réalisée. Aucune attestation finale n’est générée artificiellement. Le premier travail du coordinateur est donc une relecture ou une correction, pas l’ouverture automatique de224.

Le contrôleur ajoute des portes utiles mais ne peut garantir mécaniquement chaque obligation sémantique du prompt. Les contrôles déjà présents et les audits scientifiques restent nécessaires. Il ne lance jamais `tools/arsenal/pr.sh` pendant une rédaction active et ne modifie pas `PROMPT_Casern`, `ETAT.md`, `HANDOFF.md` ou les cours de l’application.
