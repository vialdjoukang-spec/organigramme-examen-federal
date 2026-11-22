# IMG-243 — notes de correctif, non appliquées

Le cœur (`build_app.py`, `app_template.html`, `segment.py`) n'a pas été modifié. Le manifeste dit `échographie` pour que la légende reconnaisse la technique.

## 1. `aspectScale` ignore le sigle US

`app_template.html`, fonction `aspectScale`. Avec `modality: "US"`, l'en-tête de la légende disait « Technique non précisée ».

```javascript
if(/echo|échograph|ultras|\bus\b/.test(m)) return "Échographie : l'aspect attendu se dit anéchogène, hypoéchogène ou hyperéchogène.";
```

## 2. La bulle est recopiée même sans homologue

`lightStruct` écrit le même HTML dans tous les `.atip`. Sur IMG-243, la paroi et le testicule gauche n'existent qu'à gauche : le texte apparaît quand même à droite, sans trait.

```javascript
document.querySelectorAll("#db .panel").forEach(panel=>{
  const g=id&&panel.querySelector(`.anat g[data-sid="${CSS.escape(id)}"]`);
  const tip=panel.querySelector(".atip");
  if(tip) tip.innerHTML=g?`<b>${esc(g.dataset.nom)}</b> — ${esc(g.dataset.desc)}`:"";
});
```

## 3. Âge absent

`demo()` n'affiche l'âge que si `age_ans` est un nombre. Un âge inconnu disparaît au lieu de « âge à vérifier ».

## 4. `segment.py` sur cette échographie

`polygon()` (seuil, watershed, contour actif) a suivi le cadre de l'image, pas le parenchyme. SAM absent. Les modes `air`, `os`, `enveloppe`, `foyer` sont ceux du thorax de face. Le recalage affine+élastique s'est plafonné à 8 % et n'a pas superposé les deux clichés. Les silhouettes retenues viennent de scikit-image (crête de la peau, watershed des testicules, enveloppe du parenchyme pathologique), pas d'un polygone régulier.
