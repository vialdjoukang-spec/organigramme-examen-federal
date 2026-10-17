# tools/dedale/ · Dédale, automates de dessin anatomique (zéro jeton)

Les schémas des nerfs crâniens dérivent par automate de sources sous licence ; rien n’est dessiné à la main
et aucun pixel n’est généré par IA (skills ssp-schema-nerf et ssp-images-licence). Les instructions complètes
sont en tête de chaque script.

| Automate | Rôle | Commande |
|---|---|---|
| `freestyle.py` (Dédale-3D) | Rendu Freestyle du modèle Z-Anatomy : peau en contour seul, crâne en transparence, tronc cérébral, muscles rattachés au nerf ; nerf projeté depuis ses courbes ; ancres projetées. Écrit `nc/trait/<nerf>-<vue>.svg/.json`. | `blender -b /workspace/ssp/nc_src/Z-Anatomy/Startup.blend -P tools/dedale/freestyle.py -- nc07` (`--tour --sortie /workspace/ssp/nc_src/render` pour les 8 vues) |
| `trace.py` (Dédale-T) | Plan du nerf depuis une planche de Gray : crayon par densité (dodge sur flou gaussien), retrait des légendes, masque de couleur, potrace. | `python3 tools/dedale/trace.py /workspace/ssp/nc_src/gray/Gray788.png nc07 --sans-texte` |
| `annoter.py` (Dédale-A) | Compose `assets/nc/<nerf>-<vue>.svg` (couches trait, territoires, nerf, noyaux, foramens, lesions, legendes) depuis `nc/annot/<nerf>.yml`, passe svgo 4.0.0, met à jour `assets/nc/credits.json` ; `--tour` fait le sprite WebP. | `python3 tools/dedale/annoter.py nc07` |
| `verifier.py` (Dédale-V) | Couches, texte ≥ 9 px à 360 px, poids (120 Ko par SVG, 200 Ko par WebP), crédits TASL « œuvre dérivée », couleurs, aucune image intégrée, rejeu à l’octet. | `python3 tools/dedale/verifier.py --tous` |

Configuration : `nerfs.json` (noms d’objets du modèle, caméras), `svgo.config.mjs` (svgo figé), `../../nc/sources.yml` (licences vérifiées).
Prérequis du box : Blender 3.6.19 (`/workspace/cache/blender-3.6.19-linux-x64`, lien `/usr/local/bin/blender`), potrace 1.16, svgo 4.0.0, Playwright (sprite).
Le modèle évalué occupe environ 11 Go de mémoire au chargement : une seule instance de Blender à la fois sur le box.
