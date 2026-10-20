# GAMMA · CS régions (Modification_2_CS)
- Phase 1 : `#g-reg` en grille à une ligne (`grid-auto-flow:column`), 22 boutons de largeur égale, hauteur étirée au plus haut ; défilement horizontal focalisable, sans débordement de page (1280 et 390 px).
- Phase 2 : teinte distincte par région (22 teintes), texte sombre sur fond clair ; sélection = fond plein + ✓ + `aria-pressed` + nom accessible « …, sélectionnée ». Fond blanc cassé et cartes de PR147 inchangés.
- Phase 3 : étiquette d'axe (Région/Système/Population), compteur en bas, focus visible, accrochage au défilement, sélection ramenée dans la vue.
- Périmètre : CSS + JS de configuration (`assets/style/cs-regions.css`, `assets/config/cs-regions.js`, patch 0120) ; aucun contenu clinique ; `fonctions.js` intact.
- Tests locaux : 290/290 + `test_cs_regions.py` 8/8 ; gardes 5/5 ; empreinte orig conforme.

## Automates actifs
- `tools/patches/0120-gamma-cs-regions.py`
- `ssp-patch` (skill)
- `ssp-fusion-patch` (skill)
- `ssp-tests` (skill)

## Audit de forme phases 1-2 (grok-bot)
Ligne unique, symétrie, défilement mobile sans débordement, 22 teintes, contraste ≥ 5,7:1, sélection ✓ + aria-pressed : conforme. axe : 0 nouveau problème. Écarts pixels limités à la vue Gestes, voulus.
- Correctif : boutons mobiles plus bas (9,5 rem), défilement non animé, pour des captures stables.
