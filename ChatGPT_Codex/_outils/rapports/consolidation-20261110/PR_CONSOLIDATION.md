Consolide les 858 leçons existantes attribuées à ChatGPT_Codex par le détecteur de référence, à leur destination unique `ChatGPT_Codex/LOT_XXX/`. Les contenus des leçons sont identiques aux blobs retenus ; neuf copies périmées appartenant au ressort calculé sont supprimées.

Validation : 858 destinations uniques et 858 SHA-256 vérifiés. Carte initiale, provenance de chaque copie et file épuisée archivées. Jauges régénérées. Cette récupération ne vaut pas nouvel audit clinique et ne livre aucune des 253 leçons absentes des LOTs 080–102.

Les outils originaux viennent de `reference/prompts-9.11.26` et sont copiés dans le seul dossier autorisé. Le pilote de session consomme une file séparée parce que l'outil original ne détecte pas les copies déjà effectuées sur une carte inchangée.

## Automates actifs

- `tools/garde/checkpoint.py` — inventaire réellement exécuté au démarrage ; workflows GitHub Actions inchangés.
