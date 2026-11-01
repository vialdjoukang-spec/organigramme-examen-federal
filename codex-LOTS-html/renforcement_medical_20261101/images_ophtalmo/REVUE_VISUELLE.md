# Revue réelle de l’illustration ERDES — 1 novembre 2026

Agent iconographe de cette session ; **relecture interne**, pas audit médical indépendant.

- Source réellement acquise : planche `labeling_rd.png` du dépôt officiel OSUPCVLab/ERDES, commit fixé dans `ACQUISITION_ERDES.json`. La planche complète a été ouverte avec `view_image` ; le cinquième panneau est coché positif selon les auteurs.
- Panneau retenu : x=852, y=95, largeur=200, hauteur=200 pixels. Le fichier clinique original complet reste inchangé. Aucun identifiant patient n’est visible dans le panneau.
- Image recadrée et agrandissement d’inspection ouverts visuellement. Une membrane curviligne échogène est visible dans le vitré. Le contour dessiné en longe l’enveloppe et la jonction postérieure ; il n’encadre pas tout le globe et ne prétend pas identifier la macula ou la papille.
- Rendu final `rendu-desktop.png` examiné : source à gauche, même cliché à droite, trait rouge pointillé contrasté, numéro 1 lisible dans la région noire à droite de la membrane. La membrane reste visible entre les contours. Légende française concordante avec la structure visible.
- Rendu mobile annoté `rendu-mobile-annotation.png` examiné : deux images empilées, contour et numéro lisibles, paragraphe accessible par défilement. La juxtaposition devient verticale sous 600 px pour conserver la lisibilité.
- Test Chromium/Playwright réellement exécuté : ouverture depuis le signe, ouverture/fermeture de la définition, fermeture de la fenêtre, mobile sans débordement horizontal, aucune erreur JavaScript. Détails dans `CONTROLES_NAVIGATEUR.json`. Il s’agit du fragment dans sa page d’aperçu, **pas d’un test d’intégration dans le cours final**.
- Vérification des pixels : le PNG embarqué à gauche et sous le contour à droite est identique pixel à pixel au recadrage du PNG original. Aucun traitement clinique de l’image ; export PNG sans perte.

## Limites médicales

La classification « décollement rétinien » est celle de la planche des auteurs. Le cliché isolé ne permet ni adjudication diagnostique indépendante ni évaluation du statut maculaire, du côté atteint, d’une déchirure ou d’une insertion papillaire. L’interprétation d’une membrane nécessite l’examen dynamique et la confrontation clinique. L’image native est petite (200×200), explicitement signalée. Aucun traitement suisse n’est inféré de cette source américaine.

## Licence et attribution

La page officielle archivée `index.html` attribue CC BY 4.0 au dataset, distinctement du code GPL. `SOURCES.json` contient auteurs, date d’accès, preuve, emplacement et modification. Le recadrage et les annotations sont signalés dans la légende. Les fichiers vidéo et `centre-*.png` restent des éléments de recherche non sélectionnés : pas de diagnostic individuel documenté pour ces vues.

## Intégration proposée

Dans la partie 9 « Examens complémentaires » de LOT018 PhaseA, placer un lien/bouton depuis **membrane échogène intravitréenne à l’échographie oculaire** vers une fenêtre d’examen contenant `fragments/erdes-membrane-retinienne.html`. Le fragment est autosuffisant, sans requête réseau pour les pixels. Réutilisation possible dans une future monographie sur le décollement rétinien. Ne pas introduire cette image dans le cours DX1 de réfraction, où elle serait hors sujet.

Le script `illustrer_erdes.py` est une copie privée du générateur commun : ajout des domaines officiels Github/ERDES autorisés par Vial, export PNG sans perte et traits adaptés aux 200 pixels. Les outils communs restent intacts. La génération est reproductible depuis `specification_erdes.json`.
