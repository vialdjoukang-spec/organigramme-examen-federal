# Consignes de Vial du 14.11.2026, 11 h 01

Elles remplacent ce qui les contredit. La segmentation scriptée (`scripts/segment.py`) reste obligatoire pour les contours de lésion.

1. Taille : l'interface agrandit déjà l'image normale à l'affichage (échelle 1,12, sans déformation). Ne pas déformer le fichier.
2. Tranche d'âge comparable, pas seulement « adulte ». Écrire `age_ans` des deux côtés. Écart d'au plus 15 ans pour un complet. Le sexe concordant reste exigé pour le bassin, le sein et les organes génitaux.
3. Licence libre, origine indifférente. Masquer noms, identifiants, dates et établissements incrustés. Ne garder que l'âge et le sexe. Écrire `anonymisation_verifiee` = `oui` seulement après relecture. Sinon `non` ou « À vérifier ».
4. Image normale : radio-anatomie du niveau de coupe. Champ `anatomie`, couches de dehors en dedans (`ordre`, `nom`, `contour` d'au moins 8 points, `description`, `source` ou « À vérifier »). Le bouton Anatomie et le survol sont déjà dans l'interface.
5. Image pathologique : champ `indices` avec `diagnostic`, `region`, `signe`. Les autres lésions visibles sont des flèches numérotées : l'interface dit « Il reste d'autres anomalies ». Ne pas inventer une lésion.
6. Complet seulement si, en plus des règles déjà en vigueur : anatomie par couches, anonymisation vérifiée, âges comparables, et accompagnement des lésions. `validate.py` bloque sinon. Une capture relue à l'œil reste exigée.
