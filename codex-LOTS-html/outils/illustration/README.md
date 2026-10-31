# Illustrer une leçon Codex

Scripts créés à la demande explicite de Vial. Ils restent dans le périmètre Codex et ne remplacent pas le harnais commun.

- `illustrer.py specification.json sortie.html` : image locale sourcée, licence contrôlée, empreinte de l'original, recadrage explicite facultatif, contours pointillés, numéros, définitions au clic et noms au survol/toucher. Le résultat embarque l'image et fonctionne sans requête distante.
- `../dessinateur/dessinateur.py specification.json sortie.html` : formes SVG expliquées, vues dépliables et repères interactifs. Le rendu indique qu'il s'agit d'un schéma pédagogique, hors échelle, sans image ou mesure de patient.
- `test_illustrer.py` : tests des licences refusées, attributions manquantes, URL incohérentes, empreinte altérée, coordonnées hors image et sorties hors périmètre.

Exemples complets : `LOT_018/illustrations/optique.json` et `retine.json`. Exécuter avec `python3 -B` depuis la racine du dépôt. Les coordonnées de l'annotation correspondent à l'image après recadrage ; elles ne sont pas devinées par le script.

Avant chaque intégration : vérifier la page de licence et les crédits de la figure, conserver le fichier source intact et sa provenance, lire les références médicales de la légende. Pour un schéma original, déclarer sa nature et sa source médicale ; ne pas lui attribuer une provenance Commons inventée. Refuser NC, ND et licence inconnue pour les images réutilisées.

Insérer le fragment dans la fenêtre d'examen pertinente. Le script d'exemple `LOT_018/illustrations/integrer.py` préserve le contenu antérieur, sauvegarde les originaux, évite les doublons et actualise le manifeste ; ses cibles sont propres à LOT_018 et doivent être adaptées explicitement pour un autre lot.

Après rendu : inspection visuelle obligatoire, corrections, tests des interactions, contrôle V8 et taille x. Renseigner `SOURCES.json` et une preuve de revue datée avec l'empreinte exacte du rendu examiné. Un succès technique ne vaut pas validation clinique. Toute modification des coordonnées ou du rendu impose une nouvelle inspection. La validation humaine reste distincte et ne doit pas être inventée.

Les captures et tests Chromium de LOT_018 sont de vrais essais sur HTML local chargé par `setContent`, avec émulation tactile ; ils ne prouvent pas un essai sur téléphone physique. Le chargement par URL `file://` a échoué dans cet environnement ; cette limite est conservée dans le journal.
