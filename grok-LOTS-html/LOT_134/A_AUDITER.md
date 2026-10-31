# LOT_134 — audit médical en cours (grok-4.6)

Sujet : F1.5 « Anomalies à la palpation ». Rédaction grok-4.7. Audit médical avec correction en place.

Le contrôle `controle_lot.py --sans-nom` signale, sur le format V8, la feuille Atkinson Hyperlegible et l'absence de `[S1]`. La Phase A ajoute `title=` sur les abréviations. Ces critiques sont celles du modèle (piège P-01). La porte zéro jeton est le seuil de ce run.

| Fichier | Poste consigné | Porte | x | Audit médical | Taille |
|---|---|---|---|---|---|
| LOT_134_Phase_A_V0.html | redacteur-phase-a, puis auditeur-medical | ORANGE (journal, sigles) | 8936 octets | 8 corr. (0 crit., 3 graves) · score 93 | T = 8.9 Ko (+ 74.3 Ko), 189 fenêtres, 15 dépliants |
| LOT_134_Phase_B_V0_DX.1.html | redacteur, puis auditeur-medical | ORANGE (journal, phrase_double) | 3794 octets | 3 corr. (0 crit., 2 moyens) · score 94 | T = 3.8 Ko (+ 46.2 Ko), 101 fenêtres, 15 dépliants |
| LOT_134_Phase_B_V0_DX.2.html | redacteur, puis auditeur-medical | ORANGE (journal) | 4450 octets | 3 corr. (0 crit., 1 grave) · score 93 | T = 4.5 Ko (+ 46.3 Ko), 110 fenêtres, 15 dépliants |
| LOT_134_Phase_B_V0_DX.3.html | redacteur, puis auditeur-medical | ORANGE (journal) | 3488 octets | 1 corr. (0 crit., 0 grave) · score 94 | T = 3.5 Ko (+ 43.6 Ko), 119 fenêtres, 15 dépliants |
| LOT_134_Phase_B_V0_DX.4.html | redacteur, puis auditeur-medical | ORANGE (journal) | 2874 octets | 3 corr. (0 crit., 2 graves) · score 93 | T = 2.9 Ko (+ 43.0 Ko), 117 fenêtres, 15 dépliants |
| LOT_134_Phase_B_V0_DX.5.html | redacteur, puis auditeur-medical | ORANGE (journal) | 3024 octets | 2 corr. (0 crit., 0 grave) · score 94 | T = 3.0 Ko (+ 41.2 Ko), 111 fenêtres, 15 dépliants |
| LOT_134_Phase_B_V0_DX.6.html | redacteur, puis auditeur-medical | ORANGE (journal) | 2790 octets | 2 corr. (0 crit., 0 grave) · score 95 | T = 2.8 Ko (+ 35.7 Ko), 102 fenêtres, 15 dépliants |
| LOT_134_Phase_B_V0_DX.7.html | redacteur, puis redacteur (approfondissement V8) | ORANGE (journal) | 2617 octets | non fait | T = 2.6 Ko (+ 37.1 Ko), 109 fenêtres, 15 dépliants |
| LOT_134_Phase_B_V0_DX.8.html | redacteur, puis redacteur (approfondissement V8) | ORANGE (journal) | 2616 octets | non fait | T = 2.6 Ko (+ 37.7 Ko), 107 fenêtres, 15 dépliants |
| LOT_134_Phase_B_V0_DX.9.html | redacteur, puis redacteur (approfondissement V8) | ORANGE (journal) | 2618 octets | non fait | T = 2.6 Ko (+ 40.3 Ko), 105 fenêtres, 15 dépliants |
| LOT_134_Phase_B_V0_DX.10.html | redacteur, puis redacteur (approfondissement V8) | ORANGE (journal) | 2430 octets | non fait | T = 2.4 Ko (+ 37.4 Ko), 114 fenêtres, 15 dépliants |

Liste provisoire : `LISTE_DX_CANONIQUE_PROVISOIRE.md`. Le gel `LISTE_DX_CANONIQUE.md` appartient à l'auditeur médical.
