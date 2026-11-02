# Pipeline iconographique — contrôle technique du 02.11.2026

Défaut confirmé : `reachable()` recherchait exclusivement la partie9. Le plan iconographique actuel place DX10 dans `dx10-detail8`, fenêtre du bilan d’extension. L’insertion y était donc refusée.

Correction ciblée : `partie_insertion: 8` dans le fichier de travail d’intégration sélectionne désormais explicitement P8. La valeur absente conserve P9 ; les seules valeurs admises sont les entiers8 et9. Le suffixe d’identifiant doit correspondre exactement à la partie, qui doit être unique. La traversée des liens externes à la section ne suit que les cibles uniques portant l’attribut `popover`. La figure générée reste dans un nouveau popover. Aucun changement du renderer, du harnais, des fichiers cliniques ou des registres.

Vérifications réellement exécutées :

- `python3 -B -m unittest discover -s codex-LOTS-html/outils/illustration -p test_pipeline_images.py -v` : 28 tests réussis. Ajouts couvrant sélection explicite P8, compatibilité P9, parties non autorisées, suffixes trompeurs, sections dupliquées, chaînes de fenêtres P8/P9 et refus d’une cible sans popover, y compris intermédiaire.
- Essai en mémoire sur le HTML réel DX10 : refus attendu avec défaut P9. L’expression du plan `TDM thoraco-abdomino-pelvienne` est fragmentée par une balise `abbr` et reste refusée. Avec P8 explicite et l’expression contiguë `thoraco-abdomino-pelvienne` : réussite, bouton unique dans `dx10-detail8`, figure dans son nouveau popover et nombre de titres conservé. Aucun aperçu ni fichier clinique écrit par cet essai.

Les fixtures et attestations des tests sont techniques et simulées. Ce contrôle ne constitue ni une inspection visuelle d’image clinique ni une validation médicale. Pour DX10, ajouter `"partie_insertion": 8` au JSON d’intégration ; conserver ensuite les étapes habituelles d’inspection de l’original, préparation, revue du rendu et intégration sous verrou.

À la demande complémentaire du responsable, ajout du script central `outils/illustration/controle_navigateur.js` : arguments JSON d’intégration, aperçu HTML et dossier de captures. Il contrôle P8/P9, suit les fenêtres liées, vérifie l’expression du bouton, l’ouverture, la paire originale/annotée, le décodage de l’original, les définitions, les erreurs JavaScript et le débordement horizontal. Captures couvrant toute la hauteur avec recouvrement, en bureau et mobile tactile émulé ; SHA256 de chaque capture, aperçu et travail. Les requêtes réseau du navigateur sont bloquées. Le rapport garde `inspection_visuelle:false` et `validation_clinique:false`.

Essais exécutés sous Chromium/Playwright1.62.1 : vérification syntaxique Node ; rendu réel DX3 P9 puis copie temporaire simulant P8. Dans chaque essai : deux définitions ouvertes/fermées en bureau et mobile, zéro erreur JavaScript, deux captures bureau et quatre mobile. Dossiers temporaires supprimés après tests. Ces captures de test ne sont pas des preuves d’inspection visuelle ; le responsable devra exécuter le script sur chaque nouvel aperçu et inspecter ses captures persistantes.
