# Illustrations LOT_180

Schémas pédagogiques, ellipses, repère D (droite de la patiente à gauche de l'écran). Trois niveaux chacun. Le vérificateur d'exemple de `dessinateur.py` exige des chaînes de la dissection aortique ; ces marques sont écartées, le contrôle géométrique est vert, le fichier outil n'est pas modifié.

- `uterus.json` : utérus pelvien, puis deuxième trimestre (placenta, fœtus, col), puis troisième trimestre.
- `placenta.json` : artère spiralée large, artère étroite, signes sévères.
- `rhd.json` : passage d'hématies, injection entre 28 et 30 semaines, délai de 72 heures.

Captures headless relues : `captures/uterus.png`, `placenta.png`, `rhd.png`, et le deuxième niveau `*-niveau2.png`. Pastilles numérotées, légendes entières, texte non coupé. Le deuxième niveau change le dessin (utérus qui grandit, artère qui se rétrécit, anti-D qui apparaît).

Les cases des leçons sont dans `captures/schema-*.png`. Libellés entiers, y compris « Rattrapage » et « Hors utérus ».

Les pages HTML du dessinateur ne sont pas dans le dépôt : la porte les traiterait comme des leçons. Elles se régénèrent avec `python3 grok-LOTS-html/LOT_180/_travail/illustrer.py`, puis une capture headless. Chaque leçon porte en plus un schéma SVG sans script, dans le point 10.
