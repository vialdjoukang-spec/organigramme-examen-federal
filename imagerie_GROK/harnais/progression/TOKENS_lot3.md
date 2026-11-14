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

## IMG-155

- Éléments traités : 1 diagnostic, partiel. Le sac mesuré 73 mm a été revu sur l'aperçu après resserrement du contour.
- Appels de jugement visuel : 2 lectures. Estimation.
- Durée : courte, l'image était déjà téléchargée. Estimation.
- Épargné par les scripts (estimation) : la recherche de pixels jaunes de la mesure « 73 mm » a placé le contour sans nouvelle requête.

## IMG-154, IMG-153, IMG-152, IMG-151, IMG-150

- Éléments traités : 5 diagnostics. Partiels : 154, 153, 152, 150. Introuvable : 151.
- Appels de jugement visuel : environ 14 lectures (quatre TDM de dissection, radiographie du cathéter et son coin « Na stojąco », myxome et contour déplacé, CIA et CIV rejetées pour date, CAVC rejeté pour un nom, scintigraphie DPD). Estimation.
- Durée : une passe. Estimation : Open-i renvoyait une page HTML, les catégories Commons ont porté la recherche.
- Épargné par les scripts (estimation) : `fetch_commons.py` a donné licence et auteur ; le wikitexte a fourni l'auteur manquant des clichés de Lenes, écartés ensuite pour la date gravée. `validate.py` a accepté l'introuvable et les partiels sans normale.

## IMG-149

- Éléments traités : 1 diagnostic, partiel. Cœur pulmonaire, ventricule droit étiqueté.
- Appels de jugement visuel : 2 lectures. Estimation.
- Durée : courte. Estimation.
- Épargné par les scripts (estimation) : la recherche Commons a écarté les animations ; `validate.py` a signalé l'absence de normale sans erreur.

## IMG-148, IMG-147, IMG-146, IMG-145, IMG-144

- Éléments traités : 5 diagnostics. Partiels : 148, 145, 144. Introuvables : 147, 146.
- Appels de jugement visuel : environ 12 lectures (Doppler aortique, échos de péricarde rejetés pour identifiant ou espèce, végétation et son contour abaissé, deux coronarographies). Estimation.
- Durée : une passe. Estimation : Open-i répondait tantôt par une page HTML, tantôt par des licences NC-ND.
- Épargné par les scripts (estimation) : `fetch_commons.py` a listé les catégories vides de myocardite en IRM et a marqué les vidéos ; `validate.py` a accepté les introuvables et les partiels sans normale.

## IMG-143, IMG-142, IMG-141, IMG-140, IMG-139

- Éléments traités : 5 diagnostics, tous partiels.
- Appels de jugement visuel : environ 10 lectures (rehaussement tardif, sténose de l'IVA, hernie néonatale, deux TDM de Boerhaave, médiastinite et contour resserré deux fois). Estimation.
- Durée : une passe. Estimation : Open-i a donné des licences NC pour l'infarctus et une page d'erreur pour la médiastinite.
- Épargné par les scripts (estimation) : `fetch_commons.py` a trouvé le fichier « 4CH IR infarct » et la catégorie Boerhaave ; `validate.py` a contrôlé les cinq manifestes sans erreur.

## IMG-138, IMG-137, IMG-136, IMG-135, IMG-133

- Éléments traités : 5 diagnostics, tous partiels. IMG-134 était déjà fait.
- Appels de jugement visuel : environ 12 lectures (thymome et son contour remonté, plaques et recadrage, mésothéliome ramené sur la paroi, hémothorax, empyème avec gaz). Estimation.
- Durée : une passe. Estimation : Open-i a surtout renvoyé des licences non blanches.
- Épargné par les scripts (estimation) : `fetch_commons.py cat` a listé les thymomes et les empyèmes ; `validate.py` a accepté les écarts de phase sans erreur.
