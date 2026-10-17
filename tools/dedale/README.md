# tools/dedale/ · Dédale, automates de dessin anatomique (zéro jeton)

Les schémas des nerfs crâniens dérivent par automate de sources sous licence ; rien n’est dessiné à la main
et aucun pixel n’est généré par IA (skills ssp-schema-nerf et ssp-images-licence). Les instructions complètes
sont en tête de chaque script.

| Automate | Rôle | Commande |
|---|---|---|
| `freestyle.py` (Dédale-3D) | Rendu Freestyle du modèle Z-Anatomy : peau en contour seul, crâne en transparence, tronc cérébral, muscles rattachés au nerf ; nerf projeté depuis ses courbes ; ancres projetées. Écrit `nc/trait/<nerf>-<vue>.svg/.json`. | `blender -b /workspace/ssp/nc_src/Z-Anatomy/Startup.blend -P tools/dedale/freestyle.py -- nc07` (`--tour --sortie /workspace/ssp/nc_src/render` pour les 8 vues) |
| `trace.py` (Dédale-T) | Plan du nerf depuis une planche de Gray : crayon par densité (dodge sur flou gaussien), retrait des légendes, masque de couleur, potrace. | `python3 tools/dedale/trace.py /workspace/ssp/nc_src/gray/Gray788.png nc07 --sans-texte` |
| `masques.py` (Dédale-M) | Aplats des territoires (moteur, goût, sécrétion, sensibilité) : n’ajoute au fichier vide que les collections et objets utiles (environ 450 Mo de mémoire, jamais le modèle complet), même caméra que freestyle.py (contrôlée à 0,6 px près), rendu Cycles en silhouette, potrace. Écrit `nc/trait/<nerf>-<vue>-masques.svg/.json`. | `blender -b --factory-startup -P tools/dedale/masques.py -- nc07` |
| `annoter.py` (Dédale-A) | Un préréglage = une idée = une image : compose `assets/nc/<nerf>-<préréglage>.svg` depuis `nc/presets/<nerf>.yml` (vue, cadrage zoomé, encart, couches visibles, 8 étiquettes au plus, légende courte) et `nc/annot/<nerf>.yml` (sources) ; étiquettes de 30 px posées à côté de leur structure, sans chevauchement (placement rejouable) ; les 7 couches restent dans chaque SVG, celles hors préréglage masquées ; écrit aussi `<nerf>-presets.json` pour Hermès et `credits.json` ; `--tour` fait le sprite WebP. | `python3 tools/dedale/annoter.py nc07` |
| `verifier.py` (Dédale-V) | Couches et préréglage, texte ≥ 13 px à 360 px, au plus 8 étiquettes, aucun chevauchement, dessin ≥ 60 % de l’image, légende ≤ 4 lignes, poids (120 Ko par SVG, 200 Ko par WebP), crédits TASL « œuvre dérivée », couleurs (aplats pâles déclarés seulement), aucune image intégrée, rejeu à l’octet. | `python3 tools/dedale/verifier.py --tous` |

Configuration : `nerfs.json` (noms d’objets du modèle, caméras), `svgo.config.mjs` (svgo figé), `../../nc/sources.yml` (licences vérifiées).
Prérequis du box : Blender 3.6.19 (`/workspace/cache/blender-3.6.19-linux-x64`, lien `/usr/local/bin/blender`), potrace 1.16, svgo 4.0.0, Playwright (sprite).
Le modèle complet occupe environ 11 Go au chargement : il est désormais interdit sur le box partagé. Tout nouveau rendu ajoute seulement les objets utiles à un fichier vide (`bpy.data.libraries.load`, comme masques.py) ; au-delà de 5 Go, ne pas lancer.
Playwright et les tests tournent sous `flock /tmp/oef-playwright.lock`.

Basculer une couche dans l’application (Hermès) : `svg.querySelectorAll('[data-couche="nerf"]')` puis `display`. Chaque couche figure aussi dans l’encart.
