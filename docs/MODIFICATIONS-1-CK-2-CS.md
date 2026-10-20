## Reprise autorisée après pause · 20.10.2026 Europe/Zurich

Vial demande de continuer les **parties des cours S** avec rédaction **GPT-6.1 Sol, raisonnement élevé**. Les cours gardent leurs14parties spécifiques ; les DD en six rubriques restent dans leur chantier distinct. Point courant : PR161 S3.6/S3.7, correction des phases contre-auditée ; nouvelle CI complète, fusion puis publication à vérifier. Deux auteurs réellement lancés reprennent167(S3.10/S4.1) et170(S4.2/S4.3), deux cours chacun. Contre-audit indépendant Astra, intégrations centralisées. La pause précédente est levée par cette instruction ; sauvegarde historique sur `checkpoint/pause-20261020-1314`, aucun historique supprimé.

# Mandat courant : Modification_1_CK puis Modification_2_CS

Ordre de Vial du 20.10.2026, Europe/Zurich. Ce document remplace les anciens arrêts à G16, les deux chaînes opposées et les anciens modèles de production. Les références et protections existantes restent applicables. Autorisation réitérée : prendre les décisions nécessaires, résoudre les blocages, poursuivre les tâches non bloquées ; aucune nouvelle demande d'avis entre les lots.

## Ordre réel et état de départ

L'inventaire provient des identifiants de `SSP` et `TIP`, pas d'une suite numérique supposée. Les codes restent des chaînes : `S1.1` et `S1.10` sont deux situations différentes.

| Catégorie | SSP | Étendue | État au départ |
|---|---:|---|---|
| G | 16 | G1–G16 | 14 parties par cours déjà relues et publiées ; conserver |
| S | 113 | S1.1–S9.13 | ALPHA phase 1 |
| F | 44 | F1.1–F2.25 | ALPHA phase 2 |
| O | 75 | O1.1–O7.26 | ALPHA phase 3 |

Le catalogue initial comporte 248 SSP, 3 472 parties de cours, 2 587 occurrences de différentiels et 2 287 libellés normalisés uniques. Douze SSP n'ont aucun différentiel dans l'instantané initial : BETTA doit décider de l'applicabilité, sans inventer une maladie pour remplir une case. Les compteurs sont recalculés par `python3 tools/mandat/planifier.py`.

## Modification_1_CK — ALPHA

Traiter S entièrement, puis F, puis O. Dans une phase, les auteurs travaillent en parallèle sur des lots disjoints de deux SSP au plus. Capacité de cette session : un responsable et trois autres agents actifs au maximum. Alterner les slots de production et d'audit ; les lots proposés par un script ne sont pas des agents démarrés.

Les auteurs utilisent `gpt-6-sol`, raisonnement `high` (GPT-6 élevé). Les contre-auditeurs utilisent `gpt-6-astra`. Noter le modèle réellement démarré ; une configuration GitHub ne garantit pas sa disponibilité chez un autre exécuteur.

Chaque cours conserve ses **14 parties spécifiques**, selon `docs/PROMPT-DIRECTEUR-ACADEMIQUE.md` : titres ordinaux, sous-parties correspondant à chaque élément du titre, titres seuls en gras, phrases verbales courtes, continuité sémantique, ordre du bilan et des soins. Préserver identifiants, progression, DD, fondamentaux, régions, phases et liens d'examen. Ouverture au clic, au toucher ou au clavier uniquement.

Réutiliser `tools/cours/appliquer.py` et les lots à empreintes avant/après. Un contre-auditeur indépendant relit les textes et les sources et produit un rapport lié aux 14 empreintes exactes. Le registre `tools/cours/registre.json` reçoit seulement ces contre-audits réels. Les mises en forme automatiques ne créent aucun visa.

Fusionner les petits lots audités après CI verte sur le SHA exact, dans l'ordre du catalogue, puis vérifier Pages. À la fin de S, l'audit de phase et les preuves de publication doivent être présents avant F. Même exigence pour F puis O. Aucun audit documentaire ne constitue une validation médicale humaine.

## Modification_1_CK — BETTA

Commencer seulement après les trois phases ALPHA publiées et auditées. Reprendre les SSP dans l'ordre G → S → F → O. Pour un SSP, distribuer ses différentiels par lots disjoints de trois au plus, avec audit Astra indépendant par lot. Terminer et auditer ce SSP avant le suivant.

Le plan en **six rubriques** s'applique aux diagnostics différentiels, jamais aux cours SSP. Suivre `docs/PROTOCOLE-INFOBULLES-6-RUBRIQUES.md`, avec bilan et prise en charge chronologiques. La référence diagnostique précède le premier bilan ; les soins urgents ne doivent pas attendre une confirmation. Adapter explicitement les rubriques pour un syndrome, mécanisme, situation physiologique ou demande de conseil. Justifier une rubrique sans objet ; ne pas transformer une situation non morbide en maladie.

Les monographies partagées gardent leur identifiant normalisé. Avant de traiter un libellé déjà revu, contrôler son empreinte et son adéquation au SSP courant ; ne pas réécrire concurremment la même monographie. Conserver séparément les probabilités propres à chaque plainte et population : inconnue ne signifie pas zéro, prévalence de population ne signifie pas probabilité conditionnelle.

Un SSP sans différentiel appelle une décision documentaire d'applicabilité. Si le plan convient avec adaptation, documenter l'adaptation. S'il n'existe pas de différentiel applicable, documenter le motif et sa contrelecture. Les anciennes monographies et le lot G2 non publié restent disponibles pour comparaison ; leurs anciennes attestations ne prouvent pas une relecture actuelle.

## Modification_2_CS — GAMMA

Commencer après BETTA. Phase 1 : organiser les régions en une seule ligne de boutons cliquables, de gauche à droite, avec largeur et hauteur symétriques. Tous les boutons prennent la hauteur du plus haut. Si l'ensemble dépasse l'écran mobile, conserver cette ligne dans une zone à défilement horizontal accessible, sans débordement de la page.

Phase 2 : attribuer une couleur distincte à chaque région, avec contraste lisible, nom accessible et état sélectionné qui ne repose pas seulement sur la couleur. Conserver le fond et les surfaces de lecture d'origine rétablis par PR147 : blanc cassé et cartes blanches, sans sélecteur de thèmes.

Phase 3 : dans chaque région, présenter les temps de l'examen, concis et précis, à gauche et l'image clinique ou anatomique pertinente à droite. Sur écran étroit, empiler ces éléments dans l'ordre de lecture. Conserver les gestes et liens ; images exactes et droits documentés selon `ssp-images-licence`. Auditer anatomie, cohérence geste–image, lisibilité, clavier, mobile et absence de chevauchement.

Complément utilisateur du 20.10 à 00:16 : la partie « Gestes » de CS peut être vidée pour libérer de l'espace, puis reconstruite à GAMMA. Préserver les identifiants nécessaires aux renvois et exposer son état de reconstruction. L'historique Git du dépôt conserve la version antérieure. Aucun livrable dans un autre dépôt ou espace ; les fichiers locaux ne servent qu'à l'édition et aux contrôles temporaires.

## Preuves, réservations et reprise

`tools/mandat/contrat.json` contient le mandat ; `registre.json` contient réservations, preuves de publication, audits de phase et décisions d'applicabilité. Le planificateur ne fabrique aucune preuve. Il refuse les doublons, les lots trop grands et les réservations actives dans une autre phase.

Les étapes d'une réservation sont `en_redaction`, `a_auditer`, `en_audit`, `a_corriger`, `a_integrer`, `a_publier`, puis `publie`. Une réservation interrompt l'attribution d'un doublon : le prochain exécuteur reprend la branche indiquée et contrôle son état. Les agents ne partagent jamais leur fichier de travail. Le responsable seul assemble les lots et le registre.

Une preuve de publication porte le commit intégré, les empreintes des unités et des fichiers HTTP 200 identiques à leurs octets attendus. Le registre lie cette preuve à son SHA-256. Une attestation de phase exige un rapport indépendant Astra et l'empreinte du périmètre exact. Un simple nombre ou un label ne suffit pas.

## Relance 120 secondes : capacité et limite observées

Conserver le relais existant `codex-cloud-120.yml`, raccordé au planificateur. Les contrôles visent 120 secondes pendant des fenêtres de 20 minutes ; GitHub démarre ces fenêtres par cron de cinq minutes avec retards possibles. Les demandes Codex sont espacées d'au moins 30 minutes pour éviter les sessions concurrentes. Ne pas créer de second watcher, ni renouveler le bail d'un agent depuis une boucle de surveillance.

Le responsable réellement actif déclare un bail de 180 secondes sur `garde/etat:veille/permanence.json`. Les baux de l'agent, du worker et de la demande restent séparés ; les écritures conservent les autres champs et vérifient le SHA courant.

Preuve initiale historique : run GitHub `39305516260`, contrôles réellement espacés de deux minutes ; réponse `6274859740` signalant un environnement Codex cloud manquant. État réexaminé le 20.10.2026 : la demande `6280094052` reçoit la réponse officielle `6280096230` à 00:05:15 UTC, qui signale un quota Codex épuisé. `execution_ia_prouvee:false`. Réactiver le workflow ne rétablit pas ce quota. La production et les audits actifs de cette session sont distincts du relais. Une notification, une réaction ou un bail ne prouve jamais le démarrage d’une IA distante.

## Validation et publication

Sources CH/Europe lues et datées ; définition internationale seulement avec attribution et périmètre exacts. Posologies AIPS suisse exclusivement, sinon réserve précise. Les corrections médicales et de forme suivent une relecture croisée ; toute limite reste visible.

Exécuter les gardes, le contrôle des sources, Lyncée, les compilateurs, les tests de cours et les parcours navigateur existants. Aucun seuil, budget, référence visuelle ni protection de fusion n'est abaissé pour obtenir un résultat vert. Toute externalisation technique conserve les octets des contenus et fait l'objet d'une preuve indépendante.

PR avec section « Automates actifs », contrôle du SHA final, fusion par commit de fusion, publication Pages puis vérification publique. Mettre à jour HANDOFF, PROCHAINE_ACTION, ETAT et le registre avec l'action suivante exacte. Les trois étapes ne sont terminées que lorsque leurs preuves courantes concordent.

## Contrat des preuves contrôlé après contre-audit technique

Le planificateur est un lecteur déterministe de preuves. Il ne lance pas d’agent, ne crée pas de réservation, ne télécharge pas Pages et ne certifie pas l’identité d’un modèle. Le responsable réalise les observations, puis committe leurs rapports. La contrelecture vérifie la cohérence de ces attestations ; leur existence ne constitue pas une signature de médecin ou une attestation cryptographique d’exécution IA.

### Publication

Chaque entrée de `publications` pointe vers `{rapport, rapport_sha256}`. L’empreinte du rapport est le SHA-256 de ses octets. Son contenu exige :

- `statut: publication_verifiee` ; `commit` est un commit Git existant et ancêtre de `origin/main`.
- `verifie_le` est un horodatage ISO avec fuseau, non futur ; `workflow_pages` est l’URL du vrai run Pages observé dans ce dépôt.
- `unites` associe `ALPHA:<SSP>`, `BETTA:<diagnostic_id>` ou `GAMMA:<phase>` à son empreinte canonique `planifier.empreinte`.
- `fichiers` contient `path`, `public_path` facultatif, `url`, `http: 200`, `sha256_attendu`, `sha256_public`. Les deux empreintes sont des SHA-256 des octets, jamais des identifiants Git SHA-1. Le vérificateur recalcule l’attendu depuis le blob du commit. L’URL appartient à la base Pages canonique documentée dans README.md. `app_v2.html` peut être vérifié sous son nom ou sous `index.html`.

Pour ALPHA, la preuve contient `app_v2.html` et le cours extrait du TIP de ce commit doit correspondre au digest de l’unité. Pour BETTA, une seule monographie doit porter la clé ; sa tranche `assets/mono/mono-<tranche>.js` figure dans les fichiers vérifiés. Pour GAMMA, les fichiers déployés du périmètre calculé doivent tous avoir été observés ; les données `data/cs` sont vérifiées dans Git, puisqu’elles ne sont pas exposées par Pages.

Le rapport de publication est produit après le run Pages et la comparaison HTTP réels, puis ajouté dans un commit suivant. Le planificateur contrôle la cohérence de cette observation passée, sans prétendre refaire une observation réseau en direct à chaque passage. Une URL de run conforme en syntaxe ne prouve pas seule la réussite du déploiement ; le responsable vérifie réellement son SHA et son résultat avant d’attester.

### Audits et contexte partagé

Les rapports favorables exigent `modele: gpt-6-astra`, un `relecteur_independant` non vide distinct de `auteur` lorsque celui-ci est fourni, et une date cohérente. Un rapport daté au jour local suivant est accepté avec `audit_utc` non futur et `fuseau_date_lecture` IANA ; sa `lu_le` doit être exactement la date de cet instant dans ce fuseau. Les rapports cliniques ALPHA restent liés aux quatorze empreintes et aux sources lues, via le registre de cours existant.

Chaque `audits_dd[diagnostic_id]` lie un rapport Astra au périmètre `{ "BETTA:<diagnostic_id>": "<empreinte monographie>" }`. En plus, l’audit de chaque SSP BETTA porte sur les digests des monographies et sur `CONTEXTE:<SSP>`, empreinte de `{ssp, titre, differentiels}` issu du NOT courant. Une monographie partagée peut donc être réutilisée, mais l’adéquation au contexte suivant ne se déduit pas automatiquement de son audit précédent.

Une décision d’applicabilité vide ne peut fermer le SSP que si un rapport Astra justifie `sans_differentiel_applicable`. `plan_adapte` appelle du travail effectif et ne vaut pas achèvement. L’inventaire reçu de la coordination doit correspondre au NOT courant. Les monographies en double bloquent la progression.

Le périmètre GAMMA est calculé à partir de `app_v2.html`, des CSS sous `assets`, des JS de `assets/config` et `assets/st`, et des JSON de `data/cs`. Une liste arbitraire de fichiers dans le registre ne peut réduire ce périmètre.

### Réservations et reprises

Les statuts autorisés sont les sept états décrits plus haut et `annule`. Chaque réservation active porte agent, branche, modèle GPT-6 et raisonnement élevé ; agent, branche et unités sont uniques parmi les réservations actives. Une anomalie interdit toute proposition de lot. Aucune réservation active ne peut subsister dans un résultat complet. Le planificateur n’effectue aucune mutation concurrente du registre : le responsable reste son seul écrivain, avec les protections Git existantes.

Le checkout du relais conserve l’historique complet (`fetch-depth: 0`). La reprise depuis un clone shallow récupère d’abord l’historique manquant ; un commit absent ou non intégré reste refusé. Le bail du worker est distinct du bail d’activité réelle et de la réservation de demande. La cadence de contrôle demeure 120 secondes ; la temporisation des demandes est au moins 1 800 secondes.

Le plafond des slots compte seulement les états `en_redaction` et `en_audit`. Les lots en attente `a_auditer`, `a_corriger`, `a_integrer` ou `a_publier` conservent leur réservation anti-doublon sans prétendre occuper un agent. Dès qu’un agent commence une correction, son lot revient `en_redaction`. Les propositions de reprise exposent le statut et le travail attendu : un lot `a_publier` demande la vérification de publication, aucune nouvelle rédaction.

Les lots terminés `a_publier` peuvent partager la branche d’intégration du responsable. L’unicité des branches de travail est imposée aux réservations effectivement occupées (`en_redaction`, `en_audit`) ; toutes les réservations conservent une branche explicite et des unités distinctes.
