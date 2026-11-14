# IMG-250 — modification générique du gabarit

Appliquée sur la branche `cursor/vitrine-IMG-250` seulement, pour que les captures de cette paire montrent la règle de Vial du 14.11.2026, 13 h 04. Le fichier touché est `imagerie_GROK/harnais/scripts/app_template.html`. `build_app.py` n'est pas modifié.

Cartes explicatives : fond `#E6F4FF`, bordure `#9CCBF0`, texte `#0B2540`.

- bulle de survol : `.atip:not(:empty)` et `.structTip`
- indice : `.step`
- légende du code couleur : `.codeLegend` (titres compris)
- fiche de définition : `.bub.sheet` et son texte
- bulle Source : `.src-pop`

Les petites étiquettes posées sur l'image restent sombres : `.bub.compact` (`#07090c`, texte blanc) et le numéro de flèche (pastille `#07090c`, chiffre blanc). Les boutons de zoom ne sont pas des cartes.

Le script posait `borderColor` de la fiche sur la couleur du rôle (`#FFD400` pour la lésion principale), ce qui écrasait la bordure bleu ciel. Cette affectation est retirée pour `.bub.sheet` seulement. L'étiquette compacte sur l'image garde la couleur du rôle.

```diff
 .src-pop{...background:#07090c;color:#FFFFFF;border:2px solid var(--link)...}
+.src-pop{...background:#E6F4FF;color:#0B2540;border:2px solid #9CCBF0...}
+.src-pop a{color:#0B2540;background:#E6F4FF;text-decoration:underline}

-.step{color:var(--ac)}
+.step{color:#0B2540;background:#E6F4FF;border:2px solid #9CCBF0;border-radius:8px;margin:6px 8px}
+.atip:not(:empty){color:#0B2540;background:#E6F4FF;border:2px solid #9CCBF0;border-radius:8px;margin:6px 8px}

-.structTip{...background:#07090c;color:#FFFFFF;border:2px solid var(--link)...}
+.structTip{...background:#E6F4FF;color:#0B2540;border:2px solid #9CCBF0...}
-.codeLegend{...background:#07090c;color:#FFFFFF;border:2px solid #FFD400...}
+.codeLegend{...background:#E6F4FF;color:#0B2540;border:2px solid #9CCBF0...}
-.codeLegend h3,.codeLegend h4{...color:#FFFFFF}
+.codeLegend h3,.codeLegend h4{...color:#0B2540;background:#E6F4FF}

+.bub.sheet{...background:#E6F4FF;color:#0B2540;border:2px solid #9CCBF0;box-shadow:none}
+.bub.sheet .ev,.bub.sheet .src,.bub.sheet .cf,.bub.sheet .def,.bub.sheet .r{color:#0B2540;background:#E6F4FF}
+.bub.sheet .r{color:#0B2540 !important;background:#E6F4FF}
 .bub.compact{...color:#FFFFFF;background:#07090c;border:2px solid #FFD400}

-  const col=`var(--c-${a.role})`;s.style.borderColor=col;
+  const col=`var(--c-${a.role})`;
```

`contraste.py` reste vert : `#0B2540` sur `#E6F4FF` dépasse 7:1. Le gris pâle de texte n'est pas utilisé.

Non corrigé dans ce gabarit, visible sur la légende d'IMG-250 :

- `aspectScale` ne reconnaît pas le code `US` : la phrase d'introduction dit « Technique non précisée ».
- `build_app.py` ne copie pas `aspect` ni `aspect_source` des flèches : la ligne du fibrome affiche « À vérifier » même si le manifeste détaille les quatre techniques.
