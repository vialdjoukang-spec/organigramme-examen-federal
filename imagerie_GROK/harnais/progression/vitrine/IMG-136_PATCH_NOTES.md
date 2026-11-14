# IMG-136 — notes de correctif, 14.11.2026

Le correctif 1 ci-dessous est intégré dans `build_app.py` le 14.11.2026. La légende d'IMG-136 affiche l'aspect et la source HAS du manteau. La normale a été remplacée par une coupe axiale unique (Häggström, 37 ans, CC0) : l'ancien fichier était un montage.

## 1. L'aspect sourcé de la lésion n'arrive pas à l'écran

Le manifeste porte `aspect` et `aspect_source` (HAS, juillet 2013) sur la flèche. `build_app.py` ne copie pas ces deux champs. La légende affiche donc « À vérifier » pour le manteau, alors que la source est écrite.

```diff
--- a/imagerie_GROK/harnais/scripts/build_app.py
+++ b/imagerie_GROK/harnais/scripts/build_app.py
@@
-            "contour", "definition", "definition_source", "couleur")} for x in s.get("arrows") or []]
+            "contour", "definition", "definition_source", "couleur",
+            "aspect", "aspect_source")} for x in s.get("arrows") or []]
```

## 2. `segment.py` est fait pour une radio de thorax, pas pour cette TDM

`mode air` coupe les 24 % inférieurs et ferme le poumon par un trait droit. Sur IMG-136 les bases dépassent ce seuil. Le mode `enveloppe` accroche la table du scanner. SAM est absent (pas de poids CPU).

Les silhouettes de cette paire viennent de scikit-image, une graine par structure, rééchantillonnées par `_resample` de `segment.py`. Le recalage `preparer_recalage` (affine + élastique, échelle 1,02) a été exécuté : les graines des poumons tombent dans l'air homologue ; celles du cœur et de la paroi tombent dans l'air, à cause de la réduction de volume, et ont été reprises dans la structure.

Pas de second correctif proposé : un mode « TDM axiale » dans `segment.py` servirait aux autres paires, il ne doit pas être écrit depuis une seule paire.
