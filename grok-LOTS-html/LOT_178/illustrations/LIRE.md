# Illustrations LOT_178

Schémas pédagogiques, ellipses, repère D (droite du patient à gauche de l'écran). Trois niveaux chacun. Le vérificateur d'exemple de `dessinateur.py` exige des chaînes de la dissection aortique ; ces marques sont écartées, le contrôle géométrique est vert, le fichier outil n'est pas modifié.

- `portes.json` : saignement, tracé, blocage.
- `perinee.json` : degrés 2, 3 et 4.
- `epaules.json` : hanches fléchies, pression sus-pubienne, bras postérieur. Le fond est marqué interdit au troisième niveau.
- `cordon.json` : cordon devant, main qui relève, naissance préparée. Pas de volume vésical.

Captures headless relues : `captures/portes.png`, `perinee.png`, `epaules.png`, `cordon.png`, et le deuxième niveau `*-niveau2.png`. Pastilles numérotées, légendes entières, texte non coupé. Le deuxième niveau change le dessin (sphincter qui passe au rouge, pression qui apparaît, présentation relevée).

Les pages HTML du dessinateur ne sont pas dans le dépôt : la porte les traiterait comme des leçons. Elles se régénèrent avec `python3 grok-LOTS-html/LOT_178/_travail/illustrer.py`, puis une capture headless. Chaque leçon porte en plus un schéma SVG sans script, dans le point 10.
