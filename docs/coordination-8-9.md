# Coordination des étapes 8 et 9

Ordre de Vial du18.10.2026 : étape9 prioritaire, étape8 liée, veille active toutes les dix minutes ; reprendre ensuite le lot clinique conservé.

Le calculateur `tools/coordination/calculer.py` conserve deux identités : la clé normalisée du diagnostic pour une monographie partagée et SSP#index+empreinte pour la prévalence. Il affiche séparément structure, relecture inscrite au registre, réserves et documentation des deux volets. Un pourcentage n’est jamais transféré à un autre SSP. Le registre démarre avec les deux relectures du dernier lot G10 ; les autres audits historiques restent à migrer, sans être invalidés ou certifiés automatiquement.

Une relecture demande une date non future, les sources enregistrées, l’empreinte du contenu et celle d’un rapport présent dans le dépôt. Le couplage exige aussi la levée explicite des réserves et l’applicabilité de la prévalence à la plainte concernée. Les SSP sans DD, les doublons, champs manquants et réserves bloquent une maturité documentaire globale. Il ne s’agit jamais d’un accord médical humain. La porte des étapes8/9 utilise les nombres exacts et le couplage ; aucun arrondi à100% ne clôt la boucle.

La veille existante `garde-progres.yml` est l’unique horloge : toutes les10min, elle produit le plan commun, vérifie les exécutions et demande une recherche seulement si elle est due. `relance.py` ne lance rien par défaut. Avec `--lancer`, une recherche déjà active, une erreur API ou une date inconnue empêche un nouveau lancement. Les recherches lourdes sont espacées de240min ; les runs planifiés directement dans le workflow de recherche ont été retirés pour éviter deux horloges concurrentes.

La file documentaire régule le volume : à partir de200 extraits, deux diagnostics par catégorie ; sinon huit. Maximum deux catégories simultanées et deux workers par catégorie ; budget180s par catégorie. Les tâches de prévalence correspondant aux prochains diagnostics du lot monographique sont prioritaires, puis le SSP courant, puis le catalogue existant. Les quatre catégories restent servies ; seule la liste des diagnostics éligibles est réordonnée. Les résultats partiels restent partiels.

Les appels publics conservent leur cache. Après trois échecs HTTP transitoires ou réseau d’un même appel, cet hôte est suspendu300s et cette temporisation est conservée dans le cache du runner. Un refus401/403 n’est pas contourné. Les requêtes évitées et les lectures du cache sont comptées. Deux documents officiels déjà relus (SPILF et SFMV) sont ajoutés à la découverte ciblée ; identité reconnue ne signifie jamais étude représentative.

Les notifications sont indépendantes du contrôle10min : garde Codex au plus toutes les20min en stagnation, agent statistique12h, recyclage des PR180min par PR, appel Vial60min. Une hausse globale ne prouve pas le progrès conjoint : le tableau commun garde les compteurs séparés. La relance demande de rechercher la PR active avant d’en ouvrir une autre. Les groupes de concurrence empêchent le chevauchement d’un même workflow ; un push concurrent reste refusé sans force puis doit être consolidé.

Le succès d’un commentaire prouve seulement la demande de reprise. Une exécution Actions, un commit/PR et une relecture complète sont des preuves distinctes. Ce dispositif ne peut ni maintenir ouverte une session ChatGPT ni garantir l’exécution d’une intégration Codex externe ; aucune clé de modèle n’est ajoutée. Les scripts fonctionnent sans consommation de jetons ; les agents restent soumis aux quotas du service.

## Commandes

```sh
python3 tools/coordination/calculer.py --state-dir .etat_local/prevalences --output work/coordination
python3 tools/coordination/relance.py --plan work/coordination/priorites.json
python3 -m unittest discover -s tests -p 'test_prevalences_*.py'
gh workflow run garde-progres.yml --ref main
```

Pages publie `coordination.html` et `coordination.json` avec les jauges et le PDF existants. Les réserves documentaires précèdent désormais les pannes répétées dans les exemples du PDF.

À l’intégration d’une configuration de coordination, la garde démarre aussi sur push et amorce une recherche unique. Cette activation peut ignorer la temporisation de4h, jamais une exécution active ou un état inconnu. Les contrôles périodiques reviennent ensuite au rythme régulé. En cas de refus d’authentificationCLI, les opérations du dépôt peuvent utiliser le MCPGitHub déjà connecté ; ne pas copier de jeton.
