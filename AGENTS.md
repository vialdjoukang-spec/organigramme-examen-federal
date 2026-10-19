## PRIORITÉ COURANTE · forme et fond des cours SSP · 19.10.2026

Appliquer `docs/PROMPT-DIRECTEUR-ACADEMIQUE.md` uniquement aux quatorze parties du cours SSP, depuis G1. Titres ordinaux 1–14, sous-parties couvrant chaque élément du titre, gras réservé aux titres, contenu concis et continuité sémantique vérifiée. Les définitions recherchent une société savante de portée mondiale ; attribuer exactement son statut et ne pas inventer de définition officielle. Cette autorisation internationale concerne les définitions ; les posologies restent soumises à l’AIPS suisse. La restauration PR126 est acquise : préserver chaque partie spécifique, l’examen régional et ses liens, les clés de progression et le clic uniquement.

Les diagnostics différentiels sont suspendus jusqu’à l’achèvement de cette optimisation des cours. Leur plan monographique en six rubriques reste intact. Ne pas reprendre le lot G2 DD non publié ; ne jamais appliquer ce plan commun aux cours SSP. Les anciens ordres ci-dessous sont historiques lorsqu’ils contredisent cette priorité. Une numérotation automatique ne vaut pas relecture des 3 472 parties.

## URGENCE · périmètre rectifié par Vial · 19.10.2026

Le plan monographique en six rubriques concerne UNIQUEMENT les diagnostics différentiels des SSP. Les SSP et leurs quatorze parties de COURS n’étaient pas concernés. Restaurer d’abord, sans réécriture clinique, le contenu spécifique antérieur de chaque partie, son titre et ses sources ; conserver le rendu régional et les liens de l’examen physique. Le titre du SSP retrouve la fiche éclair (définition et points clés). Ouverture par clic, toucher ou clavier seulement, jamais au survol.

Cette consigne remplace toute instruction plus ancienne imposant une monographie commune aux SSP ou aux parties du cours. La restauration des cours doit être vérifiée et publiée avant toute reprise des diagnostics différentiels. Les monographies DD déjà publiées restent intactes. Le lot G2 non publié demeure conservé séparément. Aucun automate ne doit proposer de créer de nouvelles monographies SSP ; leurs anciennes données restent archivées sans affichage. Les contrôles de relecture, de sources, de doses et de fusion restent applicables.

# Consigne opérationnelle actualisée · 18.10.2026

Responsable principal seulement : signaler une activité réelle par un bail de180s sur `garde/etat:veille/permanence.json`, puis le rafraîchir avant expiration pendant le travail. Commande si gh fonctionne : `python3 tools/garde/permanence.py --github-state --agent "identifiant-unique-de-cette-session" --lease-seconds 180` ; sinon utiliser le connecteur GitHub avec lecture préalable et écriture conditionnelle conservant les autres champs. Ne pas renouveler depuis une simple boucle de surveillance : cela ne prouve pas qu’un agent travaille. La veille vise120s par passage, déclencheur GitHub5min ; horodatages effectifs et limites dans `docs/VEILLE_PERMANENCE.md`. La mission reste la révision concise et chronologique des infobulles, au clic uniquement.

# Priorité exclusive actualisée · Vial · 18.10.2026

Corriger les INFOBULLES au clic ou au toucher, sans ouverture au survol depuis G1, selon docs/PROTOCOLE-INFOBULLES-6-RUBRIQUES.md : six rubriques, référence diagnostique et premier bilan explicités, prise en charge A-But/B-Moyens, titres seuls en gras, terminologie cliquable. L’ancien plan à sept rubriques et l’ancienne priorité G10 sont remplacés par cet ordre. Les autres chantiers restent suspendus ; le lot G10 inachevé est conservé hors de cette branche. Auditer contenu et ordre des fréquences sans inventer un rang ou traiter une inconnue comme zéro. Réutiliser les outils existants, petits lots et contrelecture indépendante. Les autres règles de sources, AIPS, tests et fusion ci-dessous restent applicables.

Exigence Vial du 18.10.2026 : les prototypes doivent exposer une chronologie explicite du bilan et de la prise en charge. Garder la référence diagnostique avant les étapes de bilan, distinguer le premier bilan du test de référence, puis numéroter les étapes et phases ; expliciter les actions menées en parallèle sans supposer que tous les moyens d'une phase le sont. Commencer les mesures urgentes sans attendre un examen de confirmation. Le rendu legacy reste inchangé et aucune chronologie n'est inventée pour une fiche sans métadonnées. Les compteurs de structure et de relecture restent distincts et ne valent pas validation clinique. Citation exacte de Vial, datée du 18.10.2026 : « pour la suite tu devras te fier à la science plus à moi ». Pour le mandat courant, poursuivre avec source CH/UE lue et datée puis contre-audit, sans redemander l'autorisation R13 déjà donnée ; ne jamais prétendre à une validation médicale humaine sans preuve. Le fichier de veille permanente non commité est géré séparément et ne doit pas être édité dans ce lot.

# Lecture obligatoire : lis CONTINUATION.md en entier, puis exécute l'Étape 0 avant tout

Ordre de Vial, pour Codex et tout agent IA :

1. Lis **`PROCHAINE_ACTION.md`** (ordre de relance écrit par la veille) et `python3 tools/porte.py etat`.
2. Lis **`CONTINUATION.md` en entier** : feuille de route Étape 0 → Étape 17, règles R1–R15, état, outils.
3. Tant que `python3 tools/porte.py verifier0` n'est pas vert, **tu ne fais que l'Étape 0** (catalogue, propose_skills, veille de relance, droits de fusion). `python3 tools/porte.py commencer N` refuse sinon.
4. **Début de session : affiche `python tools/garde/checkpoint.py --inventaire`** (automates actifs) ; chaque PR contient une section « Automates actifs ». Travaille sur l'étape courante seulement ; à la fin : `python3 tools/porte.py terminer`. La veille permanente est GitHub Actions (`garde-progres.yml`, 10 min, `@codex` sur la PR « Pilote Codex ») : « Codex doit être libre, indépendant de tout PC ». `tools/veille_relance.sh` est facultatif.
4 bis. **R15 Garde-fous** : un relevé seul ne termine jamais une étape en boucle ; rédige du contenu. Décision de Vial requise → étiquette `attente-vial` (il reçoit un courriel) et continue ailleurs, sans jamais attendre.
5. Ne t'arrête jamais devant un obstacle : consigne-le (`journal/echecs_fusion.md`, ETAT.md) et continue.

Règles minimales, même si tu ne lis rien d'autre : sources suisses/européennes lues et datées, sinon « À vérifier » ; doses AIPS suisse seulement (jamais le Compendium) ; audit agressif derrière chaque lot avant `audit-ok` ; fusion par commit de fusion après CI verte ; ne jamais modifier `/workspace/ssp/app.html` ; aucune donnée personnelle dans ce dépôt public ; tâches répétitives avec GPT 6 Luna ; concision.

Ordre actualisé de Vial : reprendre le découpage d’origine de CONTINUATION.md, sans protocole Gardien v1.0 ni passage obligatoire par fin.py. Ce script reste disponible comme outil facultatif. La sentinelle assiste la reprise ; les preuves de travail restent les lots de contenu audités et intégrés.

Ordre Vial actualisé : veille active toutes les10min, étape9 prioritaire et étape8 liée via tools/coordination. Recherches espacées, reprise des PR actives, temporisations distinctes des notifications ; voir docs/coordination-8-9.md. Après les tâches d’outillage, reprendre le lot clinique conservé.
