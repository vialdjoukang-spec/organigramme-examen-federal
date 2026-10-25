# Vérification fonctionnelle des harnais

Vial a demandé le25octobre2026 un contrôle hébergé gratuitement sur GitHub toutes les cinq minutes pour LOT225 et LOT226. Cette infrastructure est indépendante de la veille générale de progression existante. Elle n'écrit aucun contenu clinique, ne fusionne aucune PR et ne relance pas une IA.

Le workflow `.github/workflows/harnais-5min.yml` utilise un runner Ubuntu standard, les actions officielles épinglées par commit et un jeton en lecture seule. Le cron `2-59/5 * * * *` vise les minutes02,07,12,…57 de chaque heure pour éviter le début de l'heure. Il ne devient planifié qu'après intégration dans la branche par défaut. GitHub peut retarder ou omettre un déclenchement sous forte charge; un dépôt public sans activité pendant60jours peut voir ses crons désactivés. Une surveillance gratuite GitHub n'est donc pas une garantie de temps réel ni de permanence absolue. Aucun mécanisme ne simule de l'activité pour empêcher cette expiration.

## Deux contrôles complémentaires

1. Le runner exécute réellement Chonkie (plusieurs segments et reconstruction exacte), GPTCache (écriture/lecture exacte et absence de collision entre clés distinctes) et LLMLingua (modèle Microsoft multilingue, révision épinglée, compression mesurée sur du texte éditorial synthétique). Aucun extrait, seuil ou dosage médical n'est comprimé; aucune API IA payante n'est appelée. GPTCache est testé en correspondance exacte, pas comme validation d'un cache sémantique clinique.
2. Le watcher lit les branches propres à chaque agent, fixe leur SHA au début du passage, puis vérifie identité, horodatages, trois résultats fonctionnels, empreintes du harnais, empreinte du rapport runtime et artefacts de travail. Il n'exécute jamais les scripts des branches surveillées. Il ne peut pas observer directement les processus d'une session ChatGPT: il contrôle les preuves publiées, sans les transformer en télémétrie directe.

Une activité déclarée `working` devient périmée au-delà de15minutes sans nouveau signal réel. Le test runtime doit dater de moins d'une heure pendant le travail. Les seuils figurent dans `config.json`. Les états `paused`, `blocked` et `finished` restent explicites et ne sont jamais affichés comme actifs. La validité des empreintes et des tests reste contrôlée dans ces états. Le watcher ne renouvelle jamais un signal et ne fabrique pas une reprise d'agent.

## Produire sa preuve pendant du travail réel

Chaque agent exécute lui-même le test, puis le signal explicite, et publie les deux JSON dans son seul lot. Le signal n'est pas lancé depuis une boucle d'attente. Il est refait pendant une étape de travail réellement exécutée; les empreintes des artefacts empêchent d'attacher le signal à un contenu différent.

```bash
python harnais/surveillance/runtime_probe.py --agent LOT_226 --output 'lot en cours de production/LOT_226/PREUVE_RUNTIME_HARNAIS.json'
python harnais/surveillance/record_activity.py --agent LOT_226 --phase 'Rédaction ou contrôle réellement en cours' --artifact 'lot en cours de production/LOT_226/LOT_226_Appel_B_V8_Partie_1_DX.1_a_DX.2.html'
```

LOT225 utilise son identifiant et ses propres chemins. L'interpréteur doit être celui où les dépendances sont installées. Le runtime local isolé utilisé pour les premières preuves n'est pas inclus dans le dépôt. Le workflow installe les versions épinglées et le modèle sur son propre runner; ces installations ne prétendent pas installer quoi que ce soit dans les sessions des agents.

Les résultats apparaissent dans le résumé du job et les journaux Actions. Un contrôle faux ou incomplet fait échouer le job; les notifications suivent les réglages GitHub de l'utilisateur. Aucun email, message à un tiers ou ticket n'est envoyé par le script. Aucun artefact Actions n'est téléversé; le cache de modèle est limité à une révision et le cache pip suit la clé des dépendances. Le workflow n'utilise ni runner payant ni service externe payant. Si le dépôt devient privé, la gratuité illimitée des minutes publiques ne s'applique plus; le workflow refuse alors l'exécution planifiée.

## Vérifications et limites

La suite cible les faux positifs: preuve absente, périmée, future ou sans fuseau; confusion d'agent; modification d'artefact ou de harnais; échec du cache; compression fictive; tentative de sortie du lot. Les 27 tests ciblés sont déterministes et n'appellent pas le réseau.

Le sélecteur `bracelet_suggest` est testé séparément. Les scores1,6/1,3/1,3 ne sont pas les versions des bibliothèques. Un sélecteur vert n'est pas une preuve d'exécution de celles-ci.

Sources officielles consultées le25octobre2026:

- https://docs.github.com/en/actions/reference/workflows-and-actions/events-that-trigger-workflows#schedule
- https://docs.github.com/en/billing/concepts/product-billing/github-actions
- https://github.com/feyninc/chonkie
- https://github.com/microsoft/LLMLingua
- https://github.com/zilliztech/GPTCache
