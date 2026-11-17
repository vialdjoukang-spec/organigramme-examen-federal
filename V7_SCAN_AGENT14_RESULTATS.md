# V7 — balayage agent 14 (lots 113 → 007)

Lecture seule, 2026-10-25. Aucune écriture Drive. Ordre 248→001, moitié basse.

Critère d’une entité complète : 14 parties. Un lot est **complet** s’il a les 11 entités (1 SSP + 10 DD) et le package Drive 5/5 (A + P1 + P2 + P3 + P4).

Sources : `PACKAGE_5_5_agent14.json` (package) ; `V7_14PARTIES_CHECK` (Appel B, OK_14, non recompté) ; `analyze14.py` sur les 12 HTML Appel A.

## Tableau

| Lot | package_5_5 | SSP | DD | Statut |
|-----|-------------|-----|----|--------|
| LOT_113 | true | 14/14 | 10/10 | complet |
| LOT_109 | true | 14/14 | 10/10 | complet |
| LOT_108 | true | 14/14 | 10/10 | complet |
| LOT_107 | true | 14/14 | 10/10 | complet |
| LOT_106 | true | 14/14 | 10/10 | complet |
| LOT_105 | true | 14/14 | 10/10 | complet |
| LOT_012 | true | 14/14 | 10/10 | complet |
| LOT_011 | true | 14/14 | 10/10 | complet |
| LOT_010 | true | 14/14 | 10/10 | complet |
| LOT_009 | true | 14/14 | 10/10 | complet |
| LOT_008 | true | 14/14 | 10/10 | complet |
| LOT_007 | true | 14/14 | 10/10 | complet |

## Résumé

- n_complet : **12**
- n_incomplet : **0**
- Incomplets : aucun.

## Détail par lot

Appel B, tous les lots : 10 runs de 14. Répartition P1 = DX.1–2, P2 = DX.3–5, P3 = DX.6–7, P4 = DX.8–10. LOT_105 : DX.1 dans `B_P1a`, DX.2 dans `B_P1b`. LOT_012 : fichiers `Appel_B_V7_Partie_1` à `_4`.

Appel A, run `analyze14.py` en un seul bloc 1..14 : LOT_113, LOT_109, LOT_108, LOT_107, LOT_106, LOT_105.

Notes de package (le booléen reste true) :

- LOT_105 : P1 scindé en P1(a) et P1(b).
- LOT_012 : Appel A V7 de 57 Ko ; B sous les noms `Appel_B_V7_Partie_*`.
- LOT_011 : le sous-dossier corbeille n’est pas dans le décompte du package.

### SSP dont le run brut d’analyze14.py n’est pas un seul 1..14

Les 14 parties sont présentes. Le script ne les enchaîne pas, pour une raison de forme.

- **LOT_012** — titres 1 à 14 en début de ligne. `analyze14.py` : runs `[1–10]` puis `[1]` (15 hits). L’item « 1. Traiter les menaces » est à l’intérieur de la partie 10 ; 11, 12, 13 et 14 suivent et ne sont pas rattachés. Chapitre 1 = monographie SSP.
- **LOT_011** — `analyze14.py` : 11 runs de 14. Le premier est le Bloc 1 (SSP). Les dix suivants sont les monographies DX dans le même HTML. Les 10 DD du lot sont ceux d’Appel B, déjà OK_14.
- **LOT_010, LOT_009, LOT_008, LOT_007** — la plupart des « N. Titre » sont collés à la phrase précédente, donc absents du début de ligne. `analyze14.py` ne voit que quelques hits (010 : 1, 4, 8, 9 ; 009 : 1, 4, 8, 9, 11 ; 008 : 1, 8, 9, 11 ; 007 : 1, 4, 9) et un run de longueur 1. Dans le texte, chacun des 14 intitulés (définition, épidémiologie, physiopathologie, démarche, anamnèse, examen, approche syndromique, diagnostic positif, examens, arbre, prise en charge, prévention, points clés, pièges) apparaît une fois.
