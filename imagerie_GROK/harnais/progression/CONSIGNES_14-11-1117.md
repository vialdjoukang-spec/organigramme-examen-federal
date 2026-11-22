# Consignes de Vial du 14.11.2026, 11 h 17

Elles s'ajoutent aux précédentes. Le modèle est IMG-134, dans `progression/captures-interface/vitrine/`.

- Traits de 2 à 3 px, halo sombre de 1 à 2 px. Étiquettes : fond opaque sombre, texte blanc. Pas de couleur terne.
- Survol des deux côtés. La structure s'allume (trait plus épais, remplissage léger) et la bulle donne le nom et la description radiologique normale. Même identifiant, même couleur à gauche et à droite. Le survol est lié.
- Lésions : palette distincte de l'anatomie, une couleur différente par lésion, trait pointillé. Champ `couleur`. `validate.py` refuse un doublon ou une couleur déjà prise par l'anatomie.
- Zoom +, zoom −, réinitialisation, et « Zoom lié ». Les contours suivent le zoom.
- Contours : `segment.py`, graine par structure, SAM si un poids CPU est là, sinon scikit-image. Recalage affine puis élastique vers la pathologique, puis nouvelle segmentation. Même `id` des deux côtés. Ordre du manifeste, de l'externe vers l'interne. Chaque superposition est relue à l'œil.
- Ne pas marquer complet sans `validate.py` vert et sans capture relue. Ne pas inventer une seconde lésion.
