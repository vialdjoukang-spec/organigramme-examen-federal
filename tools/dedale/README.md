# tools/dedale/ · Dédale, automates de dessin anatomique (zéro jeton)

Les schémas des nerfs crâniens dérivent par automate de sources sous licence ; rien n’est dessiné à la main
et aucun pixel n’est généré par IA (skills ssp-schema-nerf et ssp-images-licence). Les instructions complètes
sont en tête de chaque script.

| Automate | Rôle | Commande |
|---|---|---|
| `freestyle.py` (Dédale-3D) | Courbes du nerf projetées et ancres (`nc/trait/<nerf>-<vue>.svg/.json`). **Ouvre le modèle complet (11 Go) : interdit sur le box** ; sorties du VII versionnées ; à porter en mode ajout seul avant une autre paire. | (historique) `blender -b …/Startup.blend -P tools/dedale/freestyle.py -- nc07` |
| `crane.py` (Dédale-C) | Crâne 3D au crayon : os seuls, ajoutés à une scène vide puis décimés (pic ≈ 1 Go) ; Freestyle en trois graisses (silhouette 4,6 px, contours 2,2 px, détails 1 px ; dents légères), traits effilés, vectorisés par potrace ; noyaux pleins. Écrit `nc/trait/<nerf>-<vue>-crane.svg/.json`. | `blender -b --factory-startup -P tools/dedale/crane.py -- nc07` |
| `trace.py` (Dédale-T) | Plan du nerf depuis une planche de Gray (donnée source seulement, plus publiée) : crayon par densité (dodge sur flou gaussien), retrait des légendes, masque de couleur, potrace. | `python3 tools/dedale/trace.py /workspace/ssp/nc_src/gray/Gray788.png nc07 --sans-texte` |
| `masques.py` (Dédale-M) | Aplats des territoires (moteur, goût, sécrétion, sensibilité) : n’ajoute au fichier vide que les collections et objets utiles (environ 450 Mo de mémoire, jamais le modèle complet), même caméra que freestyle.py (contrôlée à 0,6 px près), rendu Cycles en silhouette, potrace. Écrit `nc/trait/<nerf>-<vue>-masques.svg/.json`. | `blender -b --factory-startup -P tools/dedale/masques.py -- nc07` |
| `annoter.py` (Dédale-A) | Trois images par nerf, `assets/nc/<nerf>-{face,profil,34}.svg` : crâne au crayon, nerf jaune #FFC400 cerné de #5a4500 sur tout son trajet, noyaux jaunes ; chaque SVG contient tous les états de `nc/presets/<nerf>.yml` (trajet, branches, fonctions, lésions : couches visibles, 8 étiquettes au plus, légende courte) ; étiquettes de 30 px sans chevauchement (placement rejouable) ; écrit `<nerf>-presets.json` pour Hermès et `credits.json`. | `python3 tools/dedale/annoter.py nc07` |
| `verifier.py` (Dédale-V) | Couches et états, texte ≥ 13 px à 360 px, ≤ 8 étiquettes et aucun chevauchement par état, dessin ≥ 60 %, légende ≤ 4 lignes par état, 120 Ko par SVG, crédits TASL « œuvre dérivée », couleurs (nerf jaune obligatoire, ancien vert refusé, aplats pâles déclarés, rouge en lésions seulement), exactement 3 vues publiées, rejeu à l’octet. | `python3 tools/dedale/verifier.py --tous` |

Configuration : `nerfs.json` (noms d’objets du modèle, caméras), `svgo.config.mjs` (svgo figé), `../../nc/sources.yml` (licences vérifiées).
Prérequis du box : Blender 3.6.19 (`/workspace/cache/blender-3.6.19-linux-x64`, lien `/usr/local/bin/blender`), potrace 1.16, svgo 4.0.0, Playwright (aperçus).
Le modèle complet occupe environ 11 Go au chargement : il est désormais interdit sur le box partagé. Tout nouveau rendu ajoute seulement les objets utiles à un fichier vide (`bpy.data.libraries.load`, comme masques.py) ; au-delà de 5 Go, ne pas lancer.
Playwright et les tests tournent sous `flock /tmp/oef-playwright.lock`.

Changer d’état dans l’application (Hermès) : `const m = JSON.parse(svg.dataset.etats)` ; pour chaque élément `[data-etat]`, `setAttribute('display', e === X ? 'inline' : 'none')` ; pour chaque `g[id][data-couche]`, `display` selon `m[X].includes(couche)`. (Un style en ligne vide ne suffit pas : l’attribut `display="none"` reste.)
