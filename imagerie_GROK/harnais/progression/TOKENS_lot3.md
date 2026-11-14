# Jetons — lot 3 (IMG-172 → IMG-087)

Les durées et les appels évités sont des estimations, marquées comme telles.

## IMG-172 à IMG-168

- Éléments traités : 5 diagnostics (IMG-172, 171, 170, 169, 168), tous partiels. Aucun complet.
- Appels de jugement visuel : environ 25 lectures d'image (candidates rejetées comprises : schéma Blausen, Doppler de cirrhose, coupes TDM trop hautes, examen abdominal normal hors foie). Estimation.
- Durée : une passe de recherche et de contrôle visuel. Estimation : le temps d'une session, pas une mesure d'horloge.
- Épargné par les scripts (estimation) : `fetch_commons.py` a filtré les licences et servi les vignettes ; `normalize.py` a produit les JPEG ; `validate.py` a refusé seul un contour ouvert ou une licence hors liste. Le CDN Open-i renvoyait une page d'erreur : les figures PMC ont été prises sur cdn.ncbi.nlm.nih.gov après lecture de la légende Europe PMC, puis normalisées par le script.

## IMG-167

- Éléments traités : 1 diagnostic de plus (IMG-167), partiel. Total de la session : 6.
- Appels de jugement visuel : 2 lectures de la TDM triphasique et 1 de l'aperçu des contours, plus les coupes normales déjà ouvertes pour IMG-168. Estimation.
- Durée : courte par rapport au premier lot de cinq, le fichier et la normale étaient déjà téléchargés. Estimation.
- Épargné par les scripts (estimation) : la recherche de catégorie Commons et la validation du décalage de phase (avertissement, pas une erreur, statut partiel).

## IMG-166 à IMG-160 (IMG-161 non fait)

- Éléments traités : 6 diagnostics. Partiels : 166, 164, 163, 162, 160. Introuvable : 165. IMG-161 reste à faire.
- Appels de jugement visuel : environ 15 lectures (hémangiome et ses recadrages, côtes des deux côtés, mammographie et son contour corrigé deux fois, kystes, abcès, implant explanté rejeté). Estimation.
- Durée : une passe de recherche Commons par catégories. Estimation : plus courte que le premier groupe, les catégories de thorax et de sein sont directes.
- Épargné par les scripts (estimation) : `fetch_commons.py cat` a listé les côtes, le pneumothorax, l'épanchement et les BI-RADS sans ouvrir les pages. `validate.py` a accepté un partiel sans image normale (avertissement seulement).

## IMG-134 et IMG-132

- Éléments traités : 2 diagnostics, tous deux partiels. La même radiographie normale de Häggström sert de témoin.
- Appels de jugement visuel : 4 lectures (clichés et aperçus corrigés). Estimation.
- Durée : courte, les fichiers étaient déjà dans les catégories listées plus tôt. Estimation.
- Épargné par les scripts (estimation) : le second téléchargement de la normale est sorti du cache ; `validate.py` a signalé l'écart d'incidence sans bloquer le statut partiel.

## IMG-161, IMG-159, IMG-158, IMG-157, IMG-156

- Éléments traités : 5 diagnostics. Partiels : 161, 159, 158, 157. Introuvable : 156.
- Appels de jugement visuel : environ 10 lectures (mammographies CC et MLO, deux TDM caves dont une rejetée pour date, TEP pathologique et normale, hématome et son contour déplacé). Estimation.
- Durée : une passe. Estimation : les catégories Commons et une recherche Open-i ont suffi ; pas de second tour sur IMG-156.
- Épargné par les scripts (estimation) : `fetch_openi.py` a marqué d'un `!` les licences NC-ND de la lésion traumatique de l'aorte, sans téléchargement. `validate.py` a contrôlé les cinq manifestes en une commande.
