# IMG-132 — notes de correctif, non appliquées au cœur

Le manifeste porte `aspect` et `aspect_source` sur la flèche. `build_app.py` ne les recopie pas : la légende de l'application officielle affiche donc « À vérifier » pour la lésion. Les captures de légende ont été faites avec une page locale qui transmet ces deux champs. Le modèle `app_template.html` les affiche déjà s'ils sont présents.

Diff proposé, une ligne, dans `side()` de `imagerie_GROK/harnais/scripts/build_app.py` :

```diff
-            "contour", "definition", "definition_source", "couleur")} for x in s.get("arrows") or []]
+            "contour", "definition", "definition_source", "couleur", "aspect", "aspect_source")} for x in s.get("arrows") or []]
```

Rien d'autre dans le cœur n'a été modifié. SAM n'est pas installé : les contours viennent de scikit-image, après un recalage affine puis élastique du même module.
