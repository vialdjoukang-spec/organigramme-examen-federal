# IMG-161 — pas de modification du cœur

Le gabarit déjà en place (trait 2,5 px, halo, survol lié, zoom, zoom lié, légende, indices) suffit pour cette paire. Aucun diff de `build_app.py`, de `app_template.html` ni de `segment.py` n'est proposé.

`segment.py` a été lancé sur la graine du foyer (scikit-image, SAM absent). Le seuil global a dessiné presque tout le sein. Le contour retenu est une croissance locale scikit-image autour de la graine, relue à l'œil. Un mode « mammographie » dans `segment.py` changerait les autres paires : il n'est pas proposé.

Le recalage affine puis élastique a été calculé. Le décalage envoyait des graines du sein gauche de l'image vers le sein droit. Ces points ont été écartés après relecture. Chaque côté a été segmenté sur ses propres graines.
