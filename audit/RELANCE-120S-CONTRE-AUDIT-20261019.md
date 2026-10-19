# Contre-audit indépendant · relance locale 120 secondes

Date : 19.10.2026 UTC. Branche : `fix/relance-120s`. Base examinée : `2e33e1c5260bb3a408af1e5c4bcc94956f453eed`, avec les fichiers de travail dont les empreintes figurent ci-dessous. Relecteur distinct du rédacteur : agent `contre_audit_g2`. Lecture des données et du code seulement ; seule écriture de cette contrelecture : ce rapport. Aucun bail d’activité clinique déclaré par le relecteur.

## Verdict

**Favorable pour le correctif technique exact examiné**, après correction des réserves reproduites pendant la contrelecture. Aucun défaut bloquant résiduel concret identifié sur ce périmètre. Ce verdict ne prouve ni activation durable du relanceur, ni réponse obtenue d’un modèle, ni progression clinique. La relance effective autonome demandée reste à démontrer dans un environnement où l’accès au modèle est autorisé ; la CI de la tête finale reste également requise.

Le script vise un passage et un seuil d’inactivité de 120 secondes. Il conserve l’étape courante, refuse l’état invalide et les activités inconnues, réserve le lancement par compare-and-swap, supervise le processus CLI et distingue une tentative technique d’un travail utile. Il ne fait plus avancer automatiquement l’étape et ne lance plus de file de fusion. Les données cliniques, leur relecture et leurs jauges restent hors de ce correctif.

## Périmètre réellement lu

- `tools/veille_relance.sh`, `tools/garde/relance_bail.py`, les deux nouvelles suites de tests et leur ajout dans `.github/workflows/ci.yml`.
- `tools/garde/permanence.py` : Store local/Contents GitHub et CAS, reconnaissance des baux, détection CI/processus, limites des appels réseau et déclaration d’un agent réel.
- `tools/porte.py`, `tools/etapes.json`, `AGENTS.md`, consignes courantes de `CONTINUATION.md` et `docs/VEILLE_PERMANENCE.md` pour vérifier la mission exclusive et la portée des états.
- Aide de la CLI installée pour la compatibilité des arguments. Aucun appel réussi à un modèle n’est déduit d’une aide CLI ou d’un exécuteur simulé.

## Défauts trouvés, reproductions et résolution

| Défaut observé avant correction | Preuve de contrelecture | État final vérifié |
|---|---|---|
| JSON d’état corrompu remplacé par un état initial ; opérations possibles avant validation | Fixture temporaire avec JSON tronqué | Original conservé ; aucune relance ni mutation de l’étape. |
| Bail malformé interprété comme expiré | Bail `expires` textuel ; comparaison avec les règles réelles de `live` | Propriétaire non vide, expiration numérique finie et type de demande connus exigés ; l’inconnu bloque. |
| Verrou local insuffisant entre checkouts et course après observation de l’activité | Agent apparaissant pendant `git fetch` ; réservation concurrente via Store CAS | Nouvelle lecture et réservation CAS avant les écritures du chemin CLI. Aucun appel mutateur à `porte` ou à la file de fusion. |
| Mission exclusive pouvant avancer de 9 à 10 | Étape 9 terminée et avancement simulé vers une étape suspendue | Le relanceur lit seulement l’ordre courant ; l’état 9 et la mission exclusive sont conservés. |
| Deuxième tentative trop rapide depuis un autre checkout après sortie | Réservation à t=100, libération à t=101, nouvelle réservation à t=103 acceptée dans l’ancienne version | Temporisation partagée de 120 secondes après sortie, conservée sous un statut explicitement technique ; propriétaire étranger préservé. |
| CLI longue perdant sa protection après expiration fixe | Réservation à t=100 puis seconde réservation à t=221 dans l’ancienne version | Supervision et renouvellement toutes les 30 secondes, bail de processus de 180 secondes, sans fabriquer de bail de travail IA. |
| Latence réseau pouvant dépasser le bail pendant le renouvellement | Calcul à partir des bornes réelles : lecture 30 s, écriture 35 s, attente 30 s | Horodatage après lecture ; TTL 180 s ; test sur quatre cycles lents avec marge avant l’ancienne échéance. |
| SIGTERM du superviseur laissant son enfant vivant | Enfant Python réel en sommeil, superviseur terminé : enfant resté vivant avant correction ; enfant nettoyé par le relecteur | TERM/HUP/INT traversent le nettoyage ; arrêt du groupe, puis KILL après cinq secondes si nécessaire. Régression réelle ajoutée sans modèle. |
| Ancienne erreur de modèle déclenchant un secours sur un nouvel échec sans rapport | Journal ancien « model invalid », nouvel échec code 23 : deux appels dans l’ancienne version | Analyse limitée au fichier de la tentative courante ; un seul appel dans ce cas. Coût du secours annoncé non vérifié. |
| Écriture technique donnant l’impression d’une activité utile | Lecture des journaux, des états et vérification de l’horodatage d’ETAT | Tentative, processus et travail réel restent distincts ; ETAT.json et son horodatage ne sont pas modifiés par une tentative échouée. |

Les reproductions adverses du relecteur ont utilisé des répertoires temporaires et des exécuteurs explicitement simulés, ou un enfant Python local pour les signaux. Aucun modèle, commentaire GitHub, fusion ou modification clinique n’a été déclenché par ces reproductions.

## Vérifications exécutées

- `python3 -m unittest discover -s tests -p 'test_*relance*.py' -v` : **34 tests réussis**, dont 25 tests directs du shell et du helper, et 9 tests adjacents des notifications de reprise.
- `python3 -m unittest discover -s tests -p 'test_garde_permanence.py' -v` : **12 tests réussis**.
- `bash -n tools/veille_relance.sh`, compilation Python du helper et `git diff --check` : réussis.

Les tests vérifient notamment le seuil, l’activité récente, les baux/CI/processus actifs, l’activité inconnue, l’état invalide conservé, l’agent apparaissant durant fetch, la mission exclusive terminée, l’absence de fusion, les verrous, la réservation CAS concurrente, le délai partagé, le renouvellement long, la perte de réservation, la latence, les signaux, les sorties et le fichier STOP. Les tests de transport distant utilisent des simulations et le Store local CAS ; ils ne constituent pas un test d’exclusion distribué réel entre deux hôtes GitHub.

## Limites à conserver dans la communication

1. Les essais de modèle consignés par le rédacteur restent bloqués par CONNECT 403 vers `chatgpt.com`. Cette contrelecture n’a obtenu aucune réponse IA réelle et n’a lancé aucun démon. Un code zéro d’un faux exécuteur prouve seulement le chemin testé.
2. Un seuil de 120 secondes et une scrutation de 120 secondes donnent une détection possible entre 120 et 240 secondes après la dernière modification d’ETAT, davantage avec les opérations réseau ou une activité reconnue. Ils ne garantissent pas une reprise exactement à 120 secondes. Une machine arrêtée ne fait plus tourner ce relanceur local ; ce code ne réveille pas le fil ChatGPT.
3. Le bail de processus empêche les lancements coopérants concurrents pendant une CLI supervisée ; il ne prouve ni raisonnement, ni production, ni qualité. Le travail réel doit déclarer et rafraîchir séparément son bail et fournir des résultats audités.
4. SIGKILL du superviseur, suspension prolongée de la machine, destruction de l’environnement et défaillances non bornées ne permettent pas une garantie universelle de nettoyage. Les signaux traitables et les pertes détectées d’état sont couverts. Les horloges des hôtes coopérants doivent rester cohérentes.
5. STOP et la configuration commune empêchent les nouveaux passages ; une CLI déjà en cours conserve sa supervision jusqu’à sa sortie. Le mode sans CLI écrit seulement une consigne et ne satisfait pas à lui seul la relance réelle.
6. Aucune source médicale, dose, attestation de relecture clinique ou validation humaine n’est créée par ce correctif. Les règles CH/UE, six rubriques, chronologies et contre-audit restent nécessaires aux prochains lots.

## Empreintes SHA-256 des octets examinés

| Fichier | SHA-256 |
|---|---|
| `tools/veille_relance.sh` | `e1a5ac72b03b31e77fb0b1f68f9996d1557ce789c7d1ba5c8d4e81c1abeb094c` |
| `tools/garde/relance_bail.py` | `68e10d70fc227b3d54a76985910d185b7c3faf6e38c7e5c6fd6c1dd44166dcf7` |
| `tests/test_veille_relance.py` | `254ba30ae34fcc37ecf8aab6da93f9ae68edf4257385454ff4c35ca8ecaee08f` |
| `tests/test_relance_bail.py` | `adaddd75d0287e7d16c1d971deeeee8e0f853aa87a04e04bb8bac786609e069b` |
| `.github/workflows/ci.yml` | `f87062699d5e321c8cfd4232b62f978e77bc8001d51feea868e6b66a26a79de1` |
| `docs/VEILLE_PERMANENCE.md` | `bd9565185d6a3da9e2f3a92adf0836aaadb0e7aa10a34cf9b4887eca2885ffd1` |

Toute modification ultérieure de ces fichiers demande de vérifier sa portée sur ce verdict et d’actualiser les empreintes concernées. Les corrections ont été apportées par le rédacteur ; ce rapport atteste une contrelecture indépendante technique, pas une validation médicale humaine.
