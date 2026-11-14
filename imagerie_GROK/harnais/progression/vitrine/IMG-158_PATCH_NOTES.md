# IMG-158 — notes de correctif, non appliquées

Le cœur (`build_app.py`, `app_template.html`, `segment.py`) n'a pas été modifié. La vitrine tourne avec le code déjà sur `cursor/interface-didactique-ffbc`.

## 1. L'aspect des lésions n'arrive pas dans la page

`build_app.py`, fonction `side`, ne copie que ces clés de flèche : `tip`, `from`, `label`, `role`, `evidence`, `confidence`, `contour`, `definition`, `definition_source`, `couleur`.

Le manifeste IMG-158 a `aspect` et `aspect_source` sur la flèche. La légende affiche donc « À vérifier » pour la lésion, alors que le texte sourcé est dans le JSON. Les structures passent, elles : `anatomie` est copiée entière.

```diff
--- a/imagerie_GROK/harnais/scripts/build_app.py
+++ b/imagerie_GROK/harnais/scripts/build_app.py
@@ -65,7 +65,7 @@ def main():
         o["arrows"] = [{k: x.get(k) for k in (
             "tip", "from", "label", "role", "evidence", "confidence",
-            "contour", "definition", "definition_source", "couleur")} for x in s.get("arrows") or []]
+            "contour", "definition", "definition_source", "couleur", "aspect", "aspect_source")} for x in s.get("arrows") or []]
         return o
```

## 2. La modalité MN n'a pas de phrase d'aspect

`aspectScale` ne connaît que radio, scanner, IRM et échographie. Pour `MN`, la légende dit « Technique non précisée. » Les phrases par structure restent celles du manifeste.

```diff
--- a/imagerie_GROK/harnais/scripts/app_template.html
+++ b/imagerie_GROK/harnais/scripts/app_template.html
@@ -463,6 +463,7 @@ function aspectScale(mod){
  if(/tdm|scanner|\bct\b/.test(m)) return "Scanner : l'aspect attendu se dit hypodense, isodense ou hyperdense.";
  if(/irm|\bmr\b/.test(m)) return "IRM : l'aspect attendu précise le signal en T1, en T2 et dans les autres séquences du cliché.";
  if(/echo|échograph|ultras/.test(m)) return "Échographie : l'aspect attendu se dit anéchogène, hypoéchogène ou hyperéchogène.";
+ if(/\bmn\b|tep|\bpet\b|fdg/.test(m)) return "TEP-FDG : l'aspect se dit en fixation, cotée par rapport au médiastin puis au foie.";
  return "Technique non précisée.";
 }
```

## 3. Recalage

`preparer_recalage` n'essaie que les échelles 0,98, 1,00 et 1,02. Une planche corps entier ne se cale pas sur un zoom de racine. Pour IMG-158, le recalage a été lancé sur la fenêtre cardiaque de chaque image (scikit-image, affine puis élastique). Le point recalé tombe dans le cœur pathologique. SAM absent. Pas de changement proposé : élargir l'échelle casserait les thorax de face déjà cadrés.
