# Vitrine IMG-161 — dépistage mammographique, relue le 14.11.2026

`validate.py --only IMG-161` : déclaré partiel, validé partiel, 0 erreur, 0 avertissement. Ce n'est pas un complet.

Bureau 1440×900, mobile 390×844. Console sans erreur.

- `01-vue-initiale.png` — Âge 40 ans et femme à gauche, « À vérifier » à droite, Source, diagnostic, zoom. Aucun trait. Coins noirs du cliché pathologique.
- `02-anatomie-peau.png` — Peau cyan à gauche de l'image, verte à droite, mêmes couleurs des deux côtés. Trait coupé sur la ligne médiane. Petite encoche sur la pastille cutanée.
- `03-anatomie-graisse.png` — Liseré de graisse sous la peau. Le liseré s'interrompt en bas, au milieu.
- `04-anatomie-glande.png` — Tissu dense magenta à gauche de l'image, orange à droite. Contour irrégulier, un peu anguleux.
- `05-survol-glande-droite-vers-gauche.png` — Survol à gauche : les deux tissus droits s'allument en magenta. Bulle blanche sur fond opaque.
- `06-survol-glande-gauche-vers-droite.png` — Survol à droite : l'homologue s'allume en orange des deux côtés.
- `07-survol-peau-droite.png` — Peau droite épaissie des deux côtés, description au-dessus de chaque image.
- `08-legende-couleurs.png` — Pastilles #00E5FF, #7CFF4F, #4DFFDF, #FFE14D, #FF4DFF, #FF9F1C, lésion pointillée #FF1744. Tous les aspects sont « À vérifier ».
- `09-defi-indice-diagnostic.png` — Mode défi. Indice : Dépistage mammographique organisé. Flèche cachée.
- `10-defi-indice-region.png` — Sein droit, quadrant externe, incidence crânio-caudale.
- `11-defi-indice-signe.png` — Asymétrie de densité avec microcalcifications groupées.
- `12-revelation.png` — Flèche rouge sur le foyer blanc. « Lésion révélée. »
- `13-bande-lesion.png` — Bande pointillée autour du foyer. Définition « À vérifier », preuve de la légende, confiance moyenne. Texte entier.
- `14-autres-lesions.png` — « Lésion révélée. » Une seule flèche. Pas de seconde lésion annotée.
- `15-zoom-plus.png` — Zoom + sur la pathologique seule. La flèche reste sur le foyer.
- `16-zoom-lie.png` — Zoom lié : les deux côtés grandissent. La flèche reste sur le foyer.
- `17-survol-source.png` — Bulle : Nevit Dilmen, CC BY-SA 3.0, URL, légende « 40 F, CC Digital mammography ».
- `18-survol-source-patho.png` — Bulle : SCiardullo, CC BY-SA 4.0, URL, légende entière. Pas de nom de personne.
- `19-zoom-moins.png` — Un cran en arrière après deux crans avant : échelle 1,25 à droite, 1,12 à gauche.
- `20-mobile-initiale.png` — Le cliché normal tient. Le pathologique est coupé en bas : les deux ne tiennent pas ensemble en 390×844.
- `21-mobile-anatomie.png` — Mêmes couleurs. Le bas du cliché pathologique sort de l'écran.
- `22-mobile-survol.png` — Description de la peau au-dessus de chaque panneau. L'image pathologique est hors cadre.
- `23-mobile-source.png` — Bulle Source entière sur le cliché normal.
- `24-mobile-lesion.png` — Flèche sur le foyer, « Lésion révélée. » Le numéro est coupé au bord gauche.
