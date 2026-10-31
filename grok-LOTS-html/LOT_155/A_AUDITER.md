# LOT_155 — rédigé et certifié · 31.10.2026

Sujet : F2.7 « Électrolytes anormaux ». Rédacteur A, grok-4.7. Aucun audit en boucle : certitude `outils/certitude_redaction.py`, puis conscience `outils/conscience/conscience.py` sur les fichiers restants (avant certitude et porte). Aucune PR. Branche `grok/lots`.

Certitude : 11/11 VERT. Porte `avant redacteur` : 11/11 VERT. Conscience de lot : 0 BLOQUANT, 2 SIGNAL (plage AIPS du cache non comparée pour Samsca, Zometa et Aclasta). Les doses restent celles des informations professionnelles lues. Ce n'est pas un ordre SOURCER.

| Fichier | Certitude | Porte avant | Conscience | T | SHA contenu | Commit |
|---|---|---|---|---|---|---|
| Phase_A | VERT | VERT | SIGNAL plage Samsca | 7.6 (+ 73.8) Ko | b1ab2070490a | 28cbc94e |
| DX.1 | VERT | VERT | 0 ordre | 5.9 (+ 37.1) Ko | 7cab50f00b54 | dce43e5e |
| DX.2 | VERT | VERT | 0 ordre | 6.0 (+ 36.4) Ko | 663da5a3d93e | ae09f732 |
| DX.3 | VERT | VERT | 0 ordre | 5.9 (+ 38.4) Ko | f846df628b93 | b5778741 |
| DX.4 | VERT | VERT | 0 ordre | 6.0 (+ 35.6) Ko | b83e24fbcbb9 | f9d7193d |
| DX.5 | VERT | VERT | 0 ordre | 5.9 (+ 33.6) Ko | 66f97d22e2ff | 989f22e9 |
| DX.6 | VERT | VERT | SIGNAL plage Zometa, Aclasta | 6.0 (+ 34.0) Ko | ee709ba967ff | eafbad86 |
| DX.7 | VERT | VERT | 0 ordre | 6.0 (+ 32.1) Ko | d308d13dab33 | f3040619 |
| DX.8 | VERT | VERT | 0 ordre | 6.2 (+ 30.6) Ko | d0e754b74c73 | aebaa6f5 |
| DX.9 | VERT | VERT | 0 ordre | 6.1 (+ 32.0) Ko | c7db1ce42404 | 960fc4ba |
| DX.10 | VERT | VERT | 0 ordre | 6.1 (+ 29.5) Ko | d9fe825543a3 | b3275a9d |

Doses lues : Samsca 66962 (15 mg, jusqu'à 60 mg, 7,5 mg si risque de correction rapide) ; Lokelma 67851 (10 g trois fois par jour en correction, entretien 5 g à 10 g, dialyse 5 g à 15 g les jours sans séance) ; Veltassa 66411 (au moins 8,4 g, maximum 25,2 g) ; Resonium A 33379 (15 g par la bouche, 30 g par le rectum) ; Kaliumchlorid B. Braun 29552 (plafonds indicatifs 400 mmol et 200 mmol, vitesses écrites 40 mmol par litre et par heure et 10 mmol par litre et par heure) ; Zometa 56257 (4 mg, au moins 15 minutes) ; Aclasta 57363 (5 mg, os, pas l'hypercalcémie maligne) ; Minirin injectable 43585 (1 à 4 µg, test 4 µg, enfant 0,1 à 1 µg, nourrisson 0,05 µg). Cinq retraits dans `INCERTITUDES.md`. Prochain LOT de ce rédacteur : LOT_157.
