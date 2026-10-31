# Dessinateur

Fragment HTML/SVG interactif pour une fenêtre d'examen cliquable. Python 3, bibliothèque standard. Police Atkinson Hyperlegible (SIL OFL, dossier `polices/`). Aucun appel réseau au moment de l'affichage.

```text
python3 grok-LOTS-html/outils/dessinateur/dessinateur.py --autotest
python3 grok-LOTS-html/outils/dessinateur/dessinateur.py rendre description.json -o page.html
```

`--police` est l'URL relative de la police depuis la page écrite. Depuis `exemples/LOT_150/`, la valeur par défaut `../../polices/AtkinsonHyperlegible-Regular.ttf` convient.

## Entrée

Un JSON : `id`, `titre`, `question` (`intitule`, `html`), `sources_courtes` (HTML de la légende, liens permis), `niveaux` (au moins trois).

Chaque niveau : `id` (lettres minuscules, chiffres, tirets), `etiquette`, `note` (toujours visible, une ligne), `viewBox` `[x, y, largeur, hauteur]`, `repere` (`texte` doit être `D`, plus `x`, `y`, `titre`), `structures`, et `defaut` sur un seul niveau.

Chaque structure : `id`, `nom`, `numero` (1, 2, 3… sans trou), `geometrie`, couleurs `remplissage` / `contour` / `epaisseur`. `definition` : phrase courte, affichée seulement au survol, au focus ou au toucher. `lesion: true` oblige une définition. `trait: true` pour un vaisseau ou un voile dessiné en trait.

Géométries : `ellipse`, `chemin` (`d`), `trait` (`d`), `anneau` (paroi), `part` (corde verticale, `cote` `gauche` ou `droite`), `secteur` (angles : 0° à droite, 90° en bas), `croissant`, `vertebre`.

Le moteur refuse un chemin qui sort du cadre.

## Sortie

Fragment autonome : SVG inline, CSS, quelques lignes de JavaScript. Un seul niveau visible. Boutons radio, donc la bascule marche sans JavaScript.

Survol (souris) : contour pointillé et nom. Toucher : le nom reste jusqu'au toucher suivant. Clavier : `tabindex`, `<title>`. Sans JavaScript, le `<title>` de chaque zone reste lu par le navigateur et la question est un `<details>`.

La page de base montre le dessin, le repère D, une pastille numérotée sur chaque structure, la note et la légende. Les définitions restent dans l'infobulle. Un niveau peut déclarer `"cliche"` : fichier image voisin. Le bouton « Superposer le cliché » et le curseur d'opacité servent à vérifier l'alignement.

## Autre LOT, autre lésion, autre imagerie

Changer le JSON, pas le moteur. Garder l'orientation radiologique (droite du patient à gauche, repère D). Pour une autre modalité, adapter les couleurs et la note, et ne dessiner une lésion que si la coupe la montre vraiment. Tout fait non sourcé va dans `INCERTITUDES.md`, pas dans le dessin.

La fiche DD de base (au plus 9 Ko) ne contient qu'un lien vers la fenêtre, par exemple :

```html
<p><a href="fenetre-dissection-aortique.html">Schéma interactif : dissection aortique</a></p>
```

## Dérogation de taille

Ces figures détaillées ont une dérogation automatique : leur poids n'est pas tenu par le plafond de la fiche DD. Le fragment vise 60 Ko : chemins simplifiés, pas d'image embarquée. L'exemple tient dans 55 Ko. Le cliché de superposition est un JPEG voisin (lien relatif, environ 48 Ko), hors du fragment. La police TTF (environ 54 Ko) est aussi à part.

## Exemple

`exemples/LOT_150/dissection_aortique.html`, description dans le JSON voisin. Quatre niveaux : crosse et isthme, bifurcation pulmonaire, aorte thoracique basse (calée sur le cliché), artères rénales. Captures dans `exemples/LOT_150/captures/`.
