# Illustration de lésions (libre)

Outil : `illustrer.py`. Python 3, bibliothèque Pillow, police Atkinson Hyperlegible (SIL OFL, dossier `polices/`).

```text
python3 grok-LOTS-html/outils/illustration/illustrer.py --autotest
python3 grok-LOTS-html/outils/illustration/illustrer.py --outils
python3 grok-LOTS-html/outils/illustration/illustrer.py --chercher wikimedia "requête"
python3 grok-LOTS-html/outils/illustration/illustrer.py --chercher openi "requête"
python3 grok-LOTS-html/outils/illustration/illustrer.py --chercher pmc "requête"
python3 grok-LOTS-html/outils/illustration/illustrer.py --rendre annotation.json -o DOSSIER --page exemple.html
```

## Ce qui est réutilisé

- `harnais/bracelet/bracelet_suggest.py` (et le bracelet de `/cursor/stores/bot`) : il désigne un cache HTTP. Le cache est écrit ici en bibliothèque standard (fichier, durée de vie de 7 jours, pas de second téléchargement). Hishel et requests-cache ne sont pas installés.
- `harnais/surveillance/watchdog.py` : modèle d'en-tête `User-Agent` avec `urllib`, lu, non importé.
- `grok-LOTS-html/outils/extraire_v8.py` : `extraire_v8()`, si un contexte de leçon est utile. Lecture seule.

## Sources et licences

Entrepôts : Wikimedia Commons (API `imageinfo`), Open-i (sous-ensemble `coll=pmc`), Europe PMC (articles en accès ouvert).

Licence acceptée : CC0, CC BY, CC BY-SA, domaine public. Refus si le champ est vide, NC, ND, « open access » seul, ou inconnu. Radiopaedia n'est pas contacté.

Pour Commons, la licence et l'auteur sont relus par l'API au moment du rendu. La date d'accès est celle du téléchargement. Tout est copié dans `SOURCES.json` et dans la légende.

Open-i a renvoyé une page d'erreur HTML le 31.10.2026. L'outil le dit, il n'invente pas d'image. Europe PMC sert à confirmer la licence d'un article ; sans URL de fichier image, aucune figure n'est fabriquée.

Un schéma biologique (`"entrepot": "schema"`) ne télécharge pas d'image. Chaque référence doit avoir un titre et une `date_lecture`. Les seuils chiffrés ne viennent que du texte de l'annotation, jamais du moteur.

## Format d'annotation

```json
{
  "id": "identifiant-fichier",
  "type": "imagerie",
  "modalite": "scanner",
  "titre": "Titre français",
  "alt": "Texte alternatif",
  "source": {"entrepot": "wikimedia", "identifiant": "File:Exemple.jpg"},
  "cadre": {"x": 0, "y": 0, "largeur": 800, "hauteur": 600},
  "modification": "Ce qui a été changé (recadrage, contours).",
  "lesions": [
    {
      "ordre": 1,
      "forme": "polyligne",
      "points": [[120, 80], [140, 110]],
      "legende": "Phrase médicale française."
    }
  ],
  "semiologie": "Description du syndrome visible.",
  "pieges": ["Phrase courte."]
}
```

`forme` : `polyligne` (ouvert), `polygone` (fermé), `ellipse` (`ellipse.cx/cy/rx/ry`, `norm` vrai si 0–1), `rect` (`rect.x/y/w/h`).

`points` : pixels du fichier entier, avant le cadre. `points_norm` : 0–1 de l'image déjà cadrée. `reperes` : `[{texte, x, y}]`, repère d'orientation en pixels du fichier entier.

`ordre` fixe la lecture. Sans `ordre`, le cliché se lit de haut en bas puis de gauche à droite. Pour un ECG, de gauche à droite. Les numéros 1, 2, 3 suivent cet ordre. Rien n'est ajouté s'il n'y a pas de coordonnées.

Biologie, sans image tierce :

```json
{
  "type": "biologie",
  "modalite": "courbe",
  "source": {"references": [{"titre": "...", "support": "...", "date_lecture": "2026-10-31"}]},
  "axe_x": "Heures (schéma).",
  "graduations_x": [["0", 0], ["3", 1]],
  "elements": [
    {"ordre": 1, "forme": "ligne", "y_rel": 0.4, "legende": "..."},
    {"ordre": 2, "forme": "courbe", "points_rel": [[0, 0.2], [1, 0.8]], "legende": "..."}
  ],
  "semiologie": "...",
  "pieges": []
}
```

`y_rel` et le second nombre de `points_rel` : 0 en bas, 1 en haut, qualitatif. `graduations_x` : libellé et position 0–1.

## Sortie

PNG annoté (contour en pointillés, couleur calculée sur le fond local, numéro, légende sous l'image) et fragment `{id}.fragment.html` (`figure`, `figcaption`, liste numérotée, attribution). Ce fragment est fait pour être collé dans une leçon. Il n'est pas versionné : sous un chemin `LOT_nnn`, le hook local le contrôle comme une leçon entière. La page `exemple.html` contient les mêmes figures. Police Atkinson Hyperlegible. Couleurs de la leçon V8. Le schéma biologique est aussi un SVG.

La couleur est le contraste WCAG le plus fort avec un anneau de pixels autour du trait, puis une couleur encore libre pour la lésion suivante, afin que deux traits ne se confondent pas.

## Exemple LOT 150

`exemples/LOT_150/` : dissection aortique (DX.9) et cinétique de troponine. La page `exemple.html` montre les deux. Le dossier du LOT n'est pas modifié.
