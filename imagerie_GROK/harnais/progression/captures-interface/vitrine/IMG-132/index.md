# Vitrine IMG-132 — épanchement pleural, relue le 14.11.2026

Bureau 1440×900, mobile 390×844. `validate.py --only IMG-132` : partiel, 0 erreur, 1 avertissement (incidence postéro-antérieure ≠ face debout). Pas un complet.

- `01-vue-initiale.png` — Âge 21 ans et femme à gauche. À droite, sexe « À vérifier », pas d'âge. Source soulignée. Diagnostic affiché. Aucun trait. Zoom sur chaque côté. La normale est un peu plus grande.
- `02-anatomie-paroi.png` — Étape 1. Trait cyan latéral des deux côtés. À droite, le trait du côté du L reste court : le poumon aéré s'arrête haut.
- `03-anatomie-poumons.png` — Étape 2. Vert et turquoise, mêmes couleurs des deux côtés. Le poumon du côté du L ne couvre que l'apex encore clair.
- `04-anatomie-coeur.png` — Étape 3. Silhouette magenta. À gauche elle suit le cœur, bord inférieur peu bombé. À droite elle ne couvre que le médiastin encore bordé par le poumon aéré.
- `05-anatomie-diaphragme.png` — Étape 4. Orange sur les bases visibles. À droite, le trait suit la base du poumon clair, pas une coupole prouvée sous l'opacité.
- `06-survol-poumon-droit-vers-droite.png` — Survol à gauche : les deux poumons droits s'allument, texte foncé sur carte bleu ciel des deux côtés.
- `07-survol-poumon-gauche-vers-gauche.png` — Survol à droite : l'homologue gauche s'allume, même texte.
- `08-survol-coeur.png` — Les deux silhouettes cardiaques s'allument.
- `09-survol-paroi.png` — Les quatre traits de paroi s'épaississent, sans remplir le cliché.
- `10-survol-diaphragme-droite.png` — Survol à droite : les deux coupoles s'épaississent.
- `11-legende-couleurs.png` — Pastilles #00E5FF, #7CFF4F, #4DFFDF, #FF4DFF, #FF9F1C, lésion pointillée #FF1744. Aspects radiographiques sourcés (Broder 2011, Fleischner 2024). Scanner, IRM et échographie restent « À vérifier ». Cette capture passe les champs d'aspect de la flèche ; `build_app.py` ne le fait pas encore (voir le correctif).
- `12-defi-indice-1-diagnostic.png` — Mode défi. « Diagnostic : Épanchement pleural ». Flèche cachée.
- `13-defi-indice-2-region.png` — « Région : base thoracique droite du patient, à l'opposé du marqueur L ».
- `14-defi-indice-3-signe.png` — « Signe : opacité sous le poumon aéré, limite supérieure courbe, cul-de-sac effacé ».
- `15-revelation.png` — Flèche 1, numéro blanc sur pastille sombre, pointe sur le ménisque à gauche de l'image. Texte : « Lésion révélée. »
- `16-bande-lesion.png` — Bande pointillée rouge sur l'interface, pas sur tout l'abdomen. Définition entière jusqu'à « Confiance : moyenne ».
- `17-autres-lesions.png` — Une seule lésion dans la liste. L'opacité du côté du L reste visible et non annotée.
- `18-zoom-plus.png` — Zoom + sur la pathologique seule. La flèche suit l'image. La normale ne bouge pas.
- `19-zoom-moins.png` — Un cran de zoom arrière sur la pathologique seule.
- `20-zoom-lie.png` — Zoom lié. Facteur interne mesuré 1,5625 des deux côtés. La normale garde en plus son échelle 1,12, donc elle paraît un peu plus grande. La queue de la flèche sort du cadre.
- `21-survol-source.png` — Bulle normale : Häggström, CC0, URL, légende des 21 ans.
- `22-survol-source-patho.png` — Bulle pathologique : Hellerhoff, CC BY-SA 3.0, URL, légende entière.
- `23-mobile-initiale.png` — Les deux clichés se suivent. Le bas du cliché pathologique est coupé par la hauteur de l'écran.
- `24-mobile-anatomie.png` — Quatre couches, mêmes couleurs. Le bas du cliché pathologique reste coupé.
- `25-mobile-survol.png` — Poumon droit allumé des deux côtés, description au-dessus de chaque cliché.
- `26-mobile-source.png` — Bulle Hellerhoff entière. Elle recouvre le haut du cliché pathologique.
