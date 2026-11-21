# IMG-267 — pas de patch du cœur

La branche `cursor/interface-didactique-ffbc` a déjà le contraste (trait 2,6 px, halo sombre), le survol lié, la palette par `couleur`, le pointillé de lésion, les zooms, le bouton Anatomie, le rappel du code couleur et le mode défi. Le manifeste IMG-267 s'y branche. Aucun fichier de `scripts/` n'est modifié.

## Comportement observé, non corrigé

`#bHide` rappelle `show()`, qui remet `anatStep` à 0. Les couches d'anatomie disparaissent quand on révèle les flèches. On les réaffiche en recliquant Anatomie. Diff proposé, non appliqué :

```diff
--- a/imagerie_GROK/harnais/scripts/app_template.html
+++ b/imagerie_GROK/harnais/scripts/app_template.html
@@
-$("#bHide").onclick=()=>{hideArr=!hideArr;if(hideArr){opened.clear();showAll=false;}show();};
+$("#bHide").onclick=()=>{const step=anatStep;hideArr=!hideArr;if(hideArr){opened.clear();showAll=false;}show();anatStep=step;document.querySelectorAll("#db .anat").forEach(svg=>{const side=svg.closest(".panel").classList.contains("n")?n:p;drawAnat(svg,side);});};
```

Ce diff est incomplet tel quel (`n` et `p` sont locaux à `show`). Il ne faut pas l'appliquer sans réécriture. La paire fonctionne sans lui.
