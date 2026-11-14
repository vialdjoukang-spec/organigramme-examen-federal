---
name: designer
description: Règles de forme de la plateforme FedMed (ordre de Vial). À appliquer à l'accueil, aux onglets, au menu Thème, aux rails et aux en-têtes de cours. Ne modifie ni le contenu des cours, ni imagerie_GROK/, ni les fenêtres d'imagerie de Grok.
---

# Designer

Tu dessines l'interface pour qu'elle se lise d'un coup, avec beaucoup d'air et des aplats francs.

## Police
- Le texte courant et le texte des fenêtres utilisent **Atkinson Hyperlegible**, embarquée hors ligne.
- Les titres, le plan et le titre de la leçon ouverte utilisent **Fraunces** (OFL 1.1), embarquée hors ligne en woff2. Tu ne charges aucune police depuis un serveur.
- Le corps reste d'au moins 13 px.

## Formes
- Le fond de page est blanc.
- Tu ne poses aucun trait et aucune bordure. Un aplat suffit. Son bord est franc.
- Tu sépares les blocs par de l'espace blanc, pas par une ligne.
- Les icônes forment un seul jeu SVG inline (Lucide, licence ISC) : trait fin, bouts arrondis, 22 px, couleur `currentColor` du thème. Tu ne génères aucune image.

## Effets
- La bande EYE SPOT pose le titre sur l'aplat du thème. Le titre de la leçon ouverte se compose en Fraunces, grand, sans cadre.
- Les fenêtres de la plateforme restent blanches, sans contour.
- Une micro-animation (fond ou léger décalage, moins de 200 ms) peut accompagner le survol. Tu la coupes entièrement sous `prefers-reduced-motion: reduce`.

## Mise en page
- Sur un grand écran, la grille vaut 15 % de menu, 5 % d'espace, 70 % de texte, 10 % de marge.
- Sur le téléphone, le menu devient le tiroir Plan, le texte prend la largeur, et les onglets se lisent en entier.

## Contraste
- Le texte sur un aplat atteint un contraste d'au moins 7:1. L'encre est `#111` ou `#fff`, selon le champ `encre` du rôle.
