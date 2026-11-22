# IMG-164 — notes de correctif, non appliquées au cœur

Le gabarit (`scripts/app_template.html`, `build_app.py`) couvre déjà le contraste, le survol lié, la palette, le pointillé, les zooms, l'anatomie progressive, la légende et le défi. Rien de ce fichier n'est reporté dans le cœur.

## Recalage : le canevas force le portrait

`segment.py`, `preparer_recalage`, redimensionne les deux clichés en `(384, 288)`. IMG-164 normale est 895×1024, pathologique 756×603. Le recalage affine+élastique annonce une échelle 1,02 et un décalage horizontal d'environ 23 px sur ce canevas. La graine de paroi `(0,10 ; 0,22)` arrive en `x = 0`, sur le cadre. Les graines pulmonaires tombent trop à gauche. Elles ont été ramenées dans la structure avant la segmentation. SAM est absent (`torch` et `segment_anything` non installés, aucun poids) : repli scikit-image, déjà prévu par le script.

Diff proposé, non appliqué :

```diff
--- a/imagerie_GROK/harnais/scripts/segment.py
+++ b/imagerie_GROK/harnais/scripts/segment.py
@@ -307,11 +307,24 @@ def contour_from_seed(im, x, y, mode, n=28):
 def _canvas(im, shape):
     from skimage.transform import resize
-    x = resize(im.astype(np.float32), shape, anti_aliasing=True, preserve_range=True)
+    # Letterbox : ne pas étirer un thorax paysage dans un canevas portrait.
+    H, W = shape
+    h, w = im.shape
+    scale = min(H / h, W / w)
+    rh, rw = max(1, int(round(h * scale))), max(1, int(round(w * scale)))
+    resized = resize(im.astype(np.float32), (rh, rw), anti_aliasing=True, preserve_range=True)
+    x = np.zeros(shape, np.float32)
+    y0, x0 = (H - rh) // 2, (W - rw) // 2
+    x[y0:y0 + rh, x0:x0 + rw] = resized
     lo, hi = np.percentile(x, (2, 98))
     if hi <= lo:
         hi = lo + 1
     return np.clip((x - lo) / (hi - lo), 0, 1)
```

Il faudra aussi mapper les graines dans ce letterbox (`appliquer_recalage`), sinon le décalage du cadre n'est pas inversé. Ce second changement n'est pas écrit ici : il n'a pas été essayé.
