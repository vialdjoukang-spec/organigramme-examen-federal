# Contre-audit V2 — PHY-S9 à PHY-S12

Auditeur indépendant, 14.11.2026. J'ai lu `CORRECTIONS_PHY_S9_S12.md`, puis les champs corrigés des 23 JSON. Par script, j'ai vérifié que les JSON se chargent, que Guyton et Boron ont disparu, qu'aucune dose ne figure et que le seuil « < 0,9 » n'existe plus. J'ai aussi contrôlé les passerelles ajoutées et retirées. Les 10 titres nominaux du champ `fonction` viennent du recensement et ne bloquent pas. Ni commit ni push.

## Statut de M1 à M10

| # | Statut | Constat |
|---|---|---|
| M1 S9-4 | Corrigé | « > 3 mois » a disparu ; la pseudarthrose est à ≥ 6 mois, avec la mention « non vérifié CH ». Réserve : voir L-a. |
| M2 S11-6 | Corrigé | La marche est située à ≈ 12 mois (8,5–20), avec un seuil d'investigation à 20 mois. La source FNS 2013 figure. |
| M3 S12-3 | Corrigé | Le texte retient la pression humérale la plus haute et le seuil ≤ 0,90 (ESC 2024). Il indique < 0,5 et 0,5–0,8 (CHUV 2019). L'exemple 60 ÷ 140 donne 0,43 : calcul juste. |
| M4 S12-4 | Corrigé | La population est restreinte aux origines Han et thaïe. Le texte dit « prédit fortement » et « réduit le risque sans l'annuler ». L'AIPS reste « À vérifier ». |
| M5 S11-3 | Corrigé | L'hippocampe est décrit comme un relais qui freine le noyau paraventriculaire. |
| M6 S9-1 | Corrigé | Le texte relie l'ATP au détachement et explique la rigidité par l'absence d'ATP. |
| M7 S10-3 | Corrigé | Le texte distingue l'acide folinique, qui contourne la DHFR, de l'acide folique, qui réduit la toxicité à faible dose. |
| M8 S12-5 | Corrigé | Les valeurs HUG 2011 sont reprises : 30–80 cheveux/j, télogène 10–15 %, anagène 3 ou 6 ans, catagène 2–3 semaines, effluvium à 2–3 mois. |
| M9 Passerelles | Corrigé | Les 8 ajouts sont présents et `PP-S9-A` est retiré de S9-2. Les cibles traitent bien l'entité : PP-S4-T pour le Lambert-Eaton, PP-S7-A pour l'anti-D, PP-S1-D pour le trouble du comportement en sommeil paradoxal. |
| M10 Sources | Corrigé | Guyton et Boron n'apparaissent plus dans aucune fiche. Chaque fiche porte « (déduction), aucune source lue » pour les mécanismes. Les sources lues sont datées et leur statut est indiqué. |

Légers L1 à L9 : tous appliqués (vérifiés sur S11-4, S12-2, S11-3, S10-5, S10-1, S10-7, S10-6, S11-1). Je n'ai relevé aucune erreur médicale nouvelle.

## Deux défauts légers d'étiquetage de source (non bloquants)

| # | Fiche, champ | Extrait | PATCH exact |
|---|---|---|---|
| L-a | PHY-S9-4 `valeurs_normales[1].parametre` et `sources` | « (non vérifié CH ; HAS, résumé ; FDA : 9 mois) » ; la HAS ne figure pas dans `sources` | `parametre` : `"pseudarthrose : absence de consolidation sans progression (non vérifié CH ; HAS citée par une revue française, non lue ; FDA : 9 mois)"`. Ajouter dans `sources` : `"HAS (France), seuil de 6 mois cité par une revue française dans un résultat de recherche ; texte HAS non lu (audit du 14.11.2026)"`. L'audit n'a lu qu'un résumé de recherche, pas la HAS. |
| L-b | PHY-S11-4 `sources[0]` | « page « Le sommeil » » | `"HUG, pages « Structure du sommeil » (laboratoire du sommeil) et « Cycle veille-sommeil » (Centre de médecine du sommeil), mises à jour le 12.02.2026 (lu par l'audit du 14.11.2026)"` |

## Verdict

**Publiable : oui.** M1 à M10 sont corrigés, sans erreur nouvelle. L-a et L-b sont facultatifs. Reste hors périmètre PHY : les lacunes côté PP (§ 4 du premier audit) sont à consigner comme compléments à venir.

## Clôture
**audit-ok** pour PHY-S9 à S12 (deux étiquettes de source optionnelles listées en compléments).
