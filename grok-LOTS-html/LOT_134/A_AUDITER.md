# LOT_134 — à auditer (grok-4.6, run séparé)

Sujet : F1.5 « Anomalies à la palpation ». Rédaction grok-4.7. Aucun audit médical dans ce run.

Le contrôle `controle_lot.py --sans-nom` signale, sur le format V8, la feuille Atkinson Hyperlegible et l'absence de `[S1]`. La Phase A ajoute `title=` sur les abréviations. Ces critiques sont celles du modèle (piège P-01). La porte zéro jeton est le seuil de ce run.

| Fichier | Poste consigné | Porte | x | Audit médical | Taille après approfondissement |
|---|---|---|---|---|
| LOT_134_Phase_A_V0.html | redacteur-phase-a | VERT | 8301 octets | non fait |
| LOT_134_Phase_B_V0_DX.1.html | redacteur, puis redacteur (approfondissement V8) | VERT | 3662 octets | non fait | T = 3.7 Ko (+ 46.1 Ko), 101 fenêtres |
| LOT_134_Phase_B_V0_DX.2.html | redacteur, puis redacteur (approfondissement V8) | ORANGE (journal) | 4121 octets | non fait | T = 4.1 Ko (+ 46.1 Ko), 110 fenêtres, 15 dépliants |
| LOT_134_Phase_B_V0_DX.3.html | redacteur, puis redacteur (approfondissement V8) | ORANGE (journal) | 3325 octets | non fait | T = 3.3 Ko (+ 43.5 Ko), 119 fenêtres, 15 dépliants |
| LOT_134_Phase_B_V0_DX.4.html | redacteur, puis redacteur (approfondissement V8) | ORANGE (journal) | 2781 octets | non fait | T = 2.8 Ko (+ 42.8 Ko), 117 fenêtres, 15 dépliants |
| LOT_134_Phase_B_V0_DX.5.html | redacteur, puis redacteur (approfondissement V8) | ORANGE (journal) | 2814 octets | non fait | T = 2.8 Ko (+ 41.0 Ko), 111 fenêtres, 15 dépliants |
| LOT_134_Phase_B_V0_DX.6.html | redacteur, puis redacteur (approfondissement V8) | ORANGE (journal) | 2681 octets | non fait | T = 2.7 Ko (+ 35.6 Ko), 102 fenêtres, 15 dépliants |
| LOT_134_Phase_B_V0_DX.7.html | redacteur, puis redacteur (approfondissement V8) | ORANGE (journal) | 2617 octets | non fait | T = 2.6 Ko (+ 37.1 Ko), 109 fenêtres, 15 dépliants |
| LOT_134_Phase_B_V0_DX.8.html | redacteur | VERT | 3891 octets | non fait |
| LOT_134_Phase_B_V0_DX.9.html | redacteur | VERT | 4101 octets | non fait |
| LOT_134_Phase_B_V0_DX.10.html | redacteur | VERT | 4026 octets | non fait |

Liste provisoire : `LISTE_DX_CANONIQUE_PROVISOIRE.md`. Le gel `LISTE_DX_CANONIQUE.md` appartient à l'auditeur médical.
