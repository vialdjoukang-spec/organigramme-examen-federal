# Relais GitHub → Codex cloud · 19.10.2026

Le nouveau `tools/garde/codex_cloud_120.py`, hébergé dans ce dépôt, contrôle le travail des cours SSP toutes les120secondes pendant des fenêtres de20minutes. Le workflow `codex-cloud-120.yml` le lance sur GitHub, sans PC personnel. L’ancien garde devient un secours manuel désactivé ; son historique reste conservé.

| Composant | Fonction et preuve |
|---|---|
| Script `tools/garde/codex_cloud_120.py` | Relit main, recalcule les cours réellement relus, observe le connecteur, décide d’une reprise. Aucun contenu clinique généré par ce script. |
| Configuration `tools/garde/codex_cloud_120.json` | Activation, cadence120s et espacement minimal1800s entre demandes cloud. |
| Workflow `.github/workflows/codex-cloud-120.yml` | Déclencheur GitHub5min et fenêtres20min ; concurrence commune avec l’ancien garde. |
| État `garde/etat:veille/permanence.json` | Baux worker/agent/demande distincts ; champ `codex_cloud` avec contrôles, liens de demandes et réponses. Écriture conditionnelle sur SHA. |
| PR94 « Pilote Codex » | Fil existant réutilisé pour envoyer une demande autorisée et observer la réponse du connecteur officiel. |
| CI et contre-audit | Tests sans appels distants : cadence, conflits, arrivée d’un agent, erreur réseau, identité, absence d’environnement, conservation des preuves. |

## Blocage constaté et action nécessaire

Le connecteur officiel reçoit déjà les mentions, mais répond : « To use Codex here, create an environment for this repo ». Exemple lu le19.10.2026 : commentaire6266808017 de `chatgpt-codex-connector[bot]`, après demande6266804079 sur la PR94. Cela prouve le blocage d’environnement, pas le démarrage d’une IA.

Créer ou rattacher l’environnement de ce dépôt dans les [paramètres Codex cloud](https://chatgpt.com/codex/cloud/settings/environments), avec l’accès au dépôt GitHub. Ce réglage appartient à Codex cloud ; l’environnement d’exécution de ce chat est distinct. Le relais détecte `environnement_cloud_manquant`, continue ses contrôles120s et ne tente une nouvelle demande qu’après30minutes au minimum. Une fois la configuration corrigée, la prochaine tentative régulée peut reprendre le travail sans redéployer le script.

Une demande envoyée, une réaction et une réponse du connecteur ne valent jamais exécution prouvée. Le script ne fabrique aucun bail d’agent : seul le responsable réellement actif le déclare et le renouvelle180s pendant son travail. Une livraison inconnue après timeout conserve sa réservation et se réconcilie avec le fil ; elle n’est pas immédiatement renvoyée.

## Coordination et limites

Une CI active, un bail valide ou une progression réelle empêche une nouvelle demande. Un état corrompu, une identité non confirmée, une API indisponible ou un conflit d’écriture interrompt la fenêtre sans lancement aveugle. Aucun repli vers un commentaire de `github-actions[bot]` n’est présenté comme une relance Codex. Le jeton existant `AUTO_FUSION_TOKEN` doit appartenir au compte autorisé ; aucun nouveau secret ni appel API payant n’est ajouté.

Les échéances sont monotoniques :0,120,…,1200s. Une commande lente peut les retarder ; les échéances entièrement périmées sont sautées pour éviter les rafales. GitHub impose un minimum5min aux déclencheurs planifiés, peut les retarder et ne garantit aucune permanence120s entre deux fenêtres. Le journal `cloud120_passage` donne les heures réelles. Une fenêtre terminée ne ferme aucune mission.

Le groupe de concurrence `garde-progres` et le bail distant commun empêchent deux workers coopérants de lancer simultanément. Les anciens workers déjà démarrés voient `permanence_enabled:false` en actualisant main ; le nouveau utilise sa propre activation. Les données cliniques, les protections de fusion et les références visuelles restent intactes.

## Mission et arrêt

La relance s’applique exclusivement à la forme et au fond des14parties spécifiques des cours SSP, selon `docs/PROMPT-DIRECTEUR-ACADEMIQUE.md`. G1 publié :14/3472parties ; prochain G2, brouillon conservé sur `feat/forme-cours-g2`. Les diagnostics différentiels sont suspendus. La consigne de reprise demande contre-audit, CI verte sur le SHA exact, fusion protégée et vérification Pages.

Arrêt commun : intégrer `enabled:false` dans `tools/garde/codex_cloud_120.json` ; le prochain passage respecte ce réglage. Arrêt d’une fenêtre : annulation du workflow dans Actions, ou fichier local `.etat_local/cloud120/STOP`. Le relais ne prétend pas annuler une tâche cloud déjà acceptée. Reprise : `enabled:true` puis workflow manuel ou prochain déclencheur. L’état et les baux expirables restent préservés ; aucun effacement de preuves n’est requis.

Le code Python est gratuit. Les runners GitHub standards sont gratuits pour ce dépôt public selon les conditions GitHub ; l’usage de Codex dépend de l’abonnement et des limites du compte. Aucun coût nul universel ni fonctionnement sans interruption n’est promis.

Références officielles lues le19.10.2026 : [intégration GitHub Codex](https://developers.openai.com/codex/integrations/github/), [planification GitHub Actions](https://docs.github.com/en/actions/reference/workflows-and-actions/events-that-trigger-workflows#schedule). La première documente les mentions hors revue pour lancer un travail cloud avec le contexte de PR ; la seconde documente le minimum5min et les retards possibles.
