# Vitrine IMG-136 — mésothéliome pleural, relue le 14.11.2026

Bureau 1440×900, mobile 390×844. Statut validé : partiel. `validate.py --only IMG-136` : 0 erreur. Pas complet.

- `01-vue-initiale.png` — Âge 21 ans et sexe à gauche, « À vérifier » à droite, Source, diagnostic, zoom. Aucun contour, flèches cachées. Le fichier normal est un montage : la coupe est à gauche, le topogramme à droite.
- `02-anatomie-paroi.png` — Étape 1, paroi cyan des deux côtés, sur la peau. Le topogramme n'est pas tracé.
- `03-anatomie-poumons.png` — Étape 2, poumon droit vert et poumon gauche turquoise, même couleur des deux côtés. Le poumon droit pathologique est le plus petit.
- `04-anatomie-coeur.png` — Étape 3, cœur et gros vaisseaux magenta. Le contour normal descend vers le rachis. Le contour pathologique s'arrête devant le corps vertébral.
- `05-survol-poumon-droit-depuis-gauche.png` — Survol à gauche : les deux poumons droits s'allument, bulle blanche sur fond sombre.
- `06-survol-poumon-gauche-depuis-droite.png` — Survol à droite : l'homologue gauche s'allume aussi.
- `07-survol-coeur.png` — Survol du cœur pathologique, remplissage magenta des deux côtés.
- `08-survol-paroi.png` — Survol du trait de paroi : le nom s'affiche des deux côtés. L'épaississement du trait est peu visible. Le remplissage ne couvre pas le cliché.
- `09-legende-couleurs.png` — Pastilles #00E5FF, #7CFF4F, #4DFFDF, #FF4DFF, lésion pointillée #FF1744. Tous les aspects affichés sont « À vérifier » : le manifeste a pourtant une source HAS pour la lésion, que `build_app.py` n'embarque pas.
- `10-indice-diagnostic.png` — « Diagnostic : Mésothéliome pleural ».
- `11-indice-region.png` — Indice région : manteau latéral, côté droit du patient, à gauche de l'image.
- `12-indice-signe.png` — Indice signe : manchon et réduction de volume.
- `13-revelation.png` — Flèche 1, numéro blanc sur pastille sombre. « Lésion révélée. »
- `14-bande-lesion.png` — Pointillé rouge le long du manteau latéral, pas sur tout le poumon. Définition, source HAS, preuve et « Confiance : moyenne » entiers.
- `15-autres-lesions.png` — « Lésion révélée. » Une seule flèche. L'épanchement basal de la légende et les métastases du titre ne sont pas sur cette coupe.
- `16-zoom-plus.png` — Zoom + sur la pathologique. Le pointillé, le poumon et le cœur suivent l'image.
- `17-zoom-moins.png` — Un cran en arrière, le manteau reste dans le cadre.
- `18-zoom-lie.png` — Zoom lié : les deux côtés grandissent ensemble. La normale garde en plus son échelle 1,12.
- `19-survol-source.png` — Bulle Source opaque : Häggström, CC0, URL et légende.
- `20-mobile-initiale.png` — Mobile. Âge, sexe, Source, diagnostic. Les deux clichés sont l'un sous l'autre.
- `21-mobile-anatomie.png` — Mobile, trois couches, mêmes couleurs. Le bas du cliché pathologique sort de l'écran.
- `22-mobile-survol.png` — Mobile, poumon droit allumé des deux côtés, description au-dessus de chaque cliché.
- `23-mode-defi.png` — Mode défi, flèches cachées, consigne de clic visible.
