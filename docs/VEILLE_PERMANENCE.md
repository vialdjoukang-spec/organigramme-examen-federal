# Veille de la cellule infobulles

Exigence clarifiée par Vial le19.10.2026 : « sentinelle des120secondes » désigne un relanceur effectif du travail après inactivité, sans nouveau message de sa part. La surveillance ci-dessous ne satisfait pas seule cette exigence. Test réel du19.10 à07:55UTC : la CLI annonce une connexion au compte, mais la politique réseau appliquée refuse son accès à `chatgpt.com` (CONNECT403) ; aucune réponse IA obtenue. Le script local historique utilise aussi une option `--full-auto` refusée par la CLI installée, et ses seuils180secondes/20minutes ne sont pas120secondes. Constat sur la version historique ; réparation séparée du lot clinique décrite ci-dessous. Preuve : `audit/SENTINELLE-RELANCE-REELLE-20261019.json`.

La veille contrôle les révisions de **tous les SSP et tous les diagnostics** au prototype six rubriques, avec une contrelecture documentaire liée à l’empreinte actuelle. Trois fiches relues ou les anciennes monographies à sept rubriques ne terminent pas cette mission. Les inconnues restent explicites ; aucun compteur n’est une validation clinique humaine.

GitHub Actions ne propose pas une cadence cron de deux minutes. Le déclencheur est donc `*/5 * * * *`, avec des passages internes toutes les **120secondes pendant20minutes**. Le prochain déclenchement peut ainsi rester en attente pendant une fenêtre active : le relais dépend moins d’un lancement cron à la minute exacte. Une seule fenêtre s’exécute à la fois. Le groupe de concurrence existant `garde-progres` sérialise les fenêtres. Chaque passage extrait un instantané actualisé de `origin/main`, sans réinitialiser le checkout interactif, recalcule le plan, et n’exécute jamais de recherche transversale. Les attentes sont fractionnées à 25 secondes avec journal d’échéance.

Un retard GitHub, une file de runners ou une panne peut espacer les passages : la fréquence effective doit se constater dans les journaux. Une fenêtre terminée n’est pas une mission terminée. La première fenêtre publiée dans #120 durait quatre minutes ; elle a été étendue après constat que le cron GitHub peut démarrer tardivement. L’environnement local peut être arrêté ; ce mécanisme n’est pas une garantie d’hébergement local24h/24, d’exécution d’une IA ou de réveil de ChatGPT.

## Relance CLI locale corrigée, activation non prouvée

`tools/veille_relance.sh` utilise maintenant un seuil d’inactivité et un passage cible de120secondes ; l’ancienne option `--full-auto` est remplacée par les arguments reconnus de la CLI installée. Sans CLI, le modeB laisse uniquement un ordre de reprise : il ne satisfait pas l’exigence de relance réelle.

Dans le chemin CLI, avant toute écriture de relève ou exécution, le relanceur vérifie le responsable, la CI, la mission et l’état, puis réserve conditionnellement le lancement dans l’état GitHub partagé. Un état corrompu ou inconnu bloque la relance et reste intact. Les étapes et les autres chaînes de fusion ne sont jamais modifiées par le watcher ; l’agent reprend la mission enregistrée. Les tests incluent l’arrivée d’un responsable pendant la lecture, un lot9 terminé et la protection contre un passage à un chantier suspendu.

`tools/garde/relance_bail.py` supervise le processus CLI et renouvelle sa réservation de processus de180secondes toutesles30secondes, pour empêcher un second hôte de lancer une autre CLI au bout de120secondes. Ce bail est une preuve de processus, jamais de rédaction utile ni de validation clinique. Si sa réservation est perdue ou ne peut plus être vérifiée, le groupe CLI est arrêté. Le bail de180secondes garde une marge face aux délais réseau bornés (lecture30secondes, écriture35secondes) ; la date de renouvellement est prise après lecture. Les signaux TERM, HUP et INT déclenchent aussi le nettoyage du groupe enfant. SIGKILL ou la destruction de l’environnement ne permettent pas ce nettoyage : la réservation finit par expirer, sans garantie de conservation d’un processus ou de réveil du fil. À la sortie, une temporisation partagée de120secondes est conservée ; seul le bail d’activité portant exactement le propriétaire de cette exécution peut être nettoyé. Le responsable IA déclare et renouvelle séparément son activité réelle.

Les passages sont visés toutesles120secondes depuis le début du passage précédent. Ils peuvent être retardés par le réseau ou les commandes. Un seuil de120secondes et une scrutation de120secondes ne promettent pas un réveil exactement120secondes après la dernière action : la détection peut survenir entre120et240secondes, davantage si un bail valide ou une commande se prolonge. Une machine éteinte n’exécute plus cette boucle locale. Le code ne réveille pas ce fil ChatGPT.

Vérifications : tests d’intégration avec exécuteur simulé explicitement identifié ; syntaxe shell et arguments réels de la CLI acceptés. Aucun appel réussi à un modèle n’est revendiqué. Le test réel reste bloqué par CONNECT403 vers `chatgpt.com` ; nouvelle lecture de la configuration appliquée, révision10 : domaine toujours absent. Aucun démon de relance CLI n’a donc été démarré. Après autorisation réseau dans la configuration de l’environnement et réponse de test réelle obtenue, le lancement prévu est :

```bash
mkdir -p .etat_local
nohup bash tools/veille_relance.sh --boucle 120 > .etat_local/relance.log 2>&1 &
```

Le fichier `.etat_local/permanence/STOP` et `permanence_enabled:false` arrêtent les passages. Une exécution IA déjà en cours conserve sa supervision jusqu’à sa sortie ; ce contrôle d’arrêt du relanceur ne prétend pas annuler ses actions distantes.

## Commandes locales

Observation bornée, sans notification GitHub :

```bash
python3 tools/garde/permanence.py --window 240
```

Veille durable, état partagé et notifications autorisées par le mandat, avec les identifiants GitHub déjà configurés :

```bash
mkdir -p .etat_local/permanence
nohup python3 tools/garde/permanence.py --daemon --refresh-main --github-state --notifier > .etat_local/permanence/worker.log 2>&1 &
```

Le script ne lance **aucun agent IA**. Il mesure et peut demander une reprise via le garde existant. Un commentaire est marqué comme demande sans exécution prouvée. Un bail de demande de deux minutes évite les sollicitations cumulées ; il ne compte pas comme preuve d’un agent actif. Une CI active sur une PR ouverte, un processus local `codex exec` ou un bail d’agent effectivement déclaré empêche une nouvelle demande. Si l’activité distante est inconnue, aucune relance aveugle.

Le responsable réellement actif déclare et rafraîchit son bail, avec le même identifiant :

```bash
python3 tools/garde/permanence.py --github-state --agent "identifiant-unique-de-cette-session" --lease-seconds 180
```

Cette commande signale une activité connue du responsable ; elle ne crée aucune session. Le bail doit être renouvelé avant expiration pendant un travail prolongé. Un second identifiant n’écrase pas un bail encore vivant. Les écritures utilisent compare-and-swap, et les workers se réservent un bail distinct. Les conflits, accès401 et états corrompus interrompent la fenêtre sans envoyer de demande ni déclarer la fin.

## Arrêt et reprise

Arrêt local contrôlable :

```bash
touch .etat_local/permanence/STOP
```

Le contrôle attend au plus25secondes entre deux lectures du fichier pendant les attentes ; une commande réseau en cours conserve son timeout borné. Retirer ce fichier permet une reprise explicite. Pour l’arrêt commun et persistant, passer `permanence_enabled` à `false` dans `tools/garde/config.json`, intégrer sur main ; le prochain passage actualise main et respecte l’arrêt. Aucune modification automatique de cette consigne n’est faite par le worker.

L’autre motif d’arrêt fonctionnel est le calcul exact : SSP structurés et relus = totalSSP, et diagnostics prototypes structurés et relus = totaldiagnostics, sans SSP dépourvu de différentiel, sans doublons ni anomalies. Les attestations sont recalculées sur le contenu et les rapports actuels. Une reprise après régression réévalue les preuves et ne réutilise jamais un ancien verdict de fin mis en cache.

L’état partagé réside dans `veille/permanence.json` sur `garde/etat`, distinct des données cliniques. Le bail du worker expire après180secondes au maximum et sa libération est tentée même après une exception. Les instantanés temporaires sont nettoyés ; le calcul relit l’état runtime partagé existant, sans recopier ses données à chaque passage. Le miroir local et les journaux ne contiennent aucun jeton. Le verrou local évite deux workers dans le même répertoire ; le bail distant et le groupe GitHub couvrent les autres instances coopérantes. Le worker ne force ni push, ni fusion, ni modification de référence visuelle.

## Exigence chronologique actualisée

Le contrat du calculateur est désormais le protocole2, six rubriques et chronologie obligatoire. La clôture exige aussi l’égalité exacte des compteurs `chronologie_structures` et `chronologie_relectures` avec le total des diagnostics, et des compteurs SSP équivalents avec le totalSSP. Les preuves proviennent du registre central : drapeau `chronologie_relue: true`, fiche actuelle, rapport existant et empreintes concordantes. Un ancien rapport sans ce contrat ne peut plus déclencher une fin.

Le rythme des tentatives et celui des appels humains restent distincts : la relance vise120s si aucun responsable ou traitement CI actif n’est confirmé ; l’escalade vers Vial reste au plus horaire et seulement après30constats espacés d’au moins2minutes, soit environ une heure d’échec persistant. La nouvelle cadence ne transforme pas l’ancien seuil d’une heure en courriel après six minutes.
