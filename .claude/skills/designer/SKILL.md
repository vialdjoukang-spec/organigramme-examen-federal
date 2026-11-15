---
name: designer
description: Règles de forme de la plateforme FedMed (ordre de Vial). À appliquer à l'accueil, aux onglets, au menu Thème, aux rails et aux en-têtes de cours. Ne modifie ni le contenu des cours, ni imagerie_GROK/, ni les fenêtres d'imagerie de Grok.
---

# Designer

Décision de Vial du 15.11.2026, 01:50, précisée à 01:28 pour les teintes : seule la bande des titres porte une couleur. Le reste est blanc, avec un filet neutre fin. Les titres d'une même page alternent des teintes claires : or pur #dcab09, chlorophylle #8fdc6a, ciel #87cefa, orange clair #ffc48a, rose #ff8ec8, rouge très pâle #f6c9c9, turquoise clair #8ee8df. Une carte d'accueil n'a qu'une bande colorée, son titre. Les pastilles du bouton Thème montrent cette palette. Dans un cours, les bandes intérieures restent dans leur encadré, avec la même marge à gauche et à droite ; les encadrés d'une colonne partagent les mêmes bords.

Tu dessines l'interface pour qu'elle se lise d'un coup.

## Police
- Le texte courant et le texte des fenêtres utilisent **Atkinson Hyperlegible**, embarquée hors ligne.
- Les titres, le plan et le titre de la leçon ouverte utilisent **Fraunces** (OFL 1.1), embarquée hors ligne en woff2. Tu ne charges aucune police depuis un serveur.
- Le corps reste d'au moins 13 px.

## Formes
- Le fond de page est blanc.
- Les titres se repèrent sur la palette claire. Le reste de la carte reste blanc.
- Tu sépares les ajouts (icônes, libellés) du jeu de couleurs.
- Les icônes forment un seul jeu SVG inline (Lucide, licence ISC) : trait fin, bouts arrondis, 22 px, couleur `currentColor` du thème. Tu ne génères aucune image.

## Effets
- La bande EYE SPOT pose le titre sur l'aplat du thème. Le titre de la leçon ouverte se compose en Fraunces, grand, sans cadre.
- Les fenêtres de la plateforme restent blanches, sans contour.
- Une micro-animation (fond ou léger décalage, moins de 200 ms) peut accompagner le survol. Tu la coupes entièrement sous `prefers-reduced-motion: reduce`.

## Mise en page
- Sur un grand écran, la grille vaut 15 % de menu, 5 % d'espace, 70 % de texte, 10 % de marge.
- Sur le téléphone, le menu devient le tiroir Plan, le texte prend la largeur, et les onglets se lisent en entier.

## Contraste
- Le texte sur un aplat atteint un contraste d'au moins 7:1 avec `#000`. Deux bandes voisines restent distinctes (ΔE2000 d'au moins 15).
- Le rail montre chaque mot en entier. Le bouton Thème reste en place. Les onglets du téléphone tiennent sur deux lignes. La police Atkinson est hors ligne.
