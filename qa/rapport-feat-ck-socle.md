# Rapport · feat/ck-socle · Atlas et Janus · 17.10.2026

**Verdict :** prêt à fusionner si la CI (garde avec l’audit G1 à G7, html, liens, tests, visuel) réussit.

- Le diff touche app_v2.html par le seul patch 0011 (un ancrage unique, rejouable après 0010 d’Hermès) : +659 octets (5 792 254 → 5 792 913, après fusion de main et des PR #18 et #19, budget 6 000 000 ; critère < 40 Ko). Aucune donnée CK n’entre dans app_v2.html ; orig/ reste intact.
- assets/ck : 7 fichiers, 742 octets (budget 2 500 000) ; assets/nc : 0 octet (budget 3 000 000).
- Suite locale 133/133 (dont 12 de tests/test_ck_socle.py : chargement hors ligne en file://, index après DOMContentLoaded, une balise par fichier, échec propre d’un fichier absent), gardes 5/5, tests/test_ck.py 61/61 (chaque contrôle G1 à G7, budgets, SVG et rapport des fautes échoue quand sa règle est violée).
- Lyncée sur main : 3 868 candidats, 19 exclusions motivées, 3 849 termes dans la référence ; G1 à G7 réussissent sur le dépôt (données CK vides et conformes).
- Écarts au plan, motivés dans journal/nerfs-ck.md : filtres MeSH et Lexique hors CI (déterminisme) ; liste G6 issue d’un conjugueur interne (lexique.org indisponible) ; G7 limité aux données CK et aux règles `.ck-…`.
