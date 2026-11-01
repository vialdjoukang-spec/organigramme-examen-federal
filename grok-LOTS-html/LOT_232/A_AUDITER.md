# LOT_232 — rédigé et certifié · 01.11.2026

Sujet : O7.10 « Demande de consentement éclairé pour une intervention ». Rédacteur B, grok-4.7. Aucun audit médical dans cette passe : la certitude est le script `outils/certitude_redaction.py`. Porte `avant redacteur-phase-a` et `avant redacteur`, avec `--preuves`. Conscience de lot : 0 BLOQUANT, 0 SIGNAL. Aucune PR. Branche `grok/lots`.

Certitude : 11/11 VERT. Porte : 11/11 VERT après le correctif du 01.11.2026 (voir plus bas) ; avant : 11/11 ORANGE (phrases longues et phrases répétées). Zéro retrait des éléments centraux (capacité de discernement, information, forme et documentation, urgence et incapacité, représentant thérapeutique, directives anticipées, mineurs, refus de soins, conduite à tenir). Rédaction de zéro, aucune branche Flash. Textes lus le 1er novembre 2026 : code civil, directives de 2019, guide du 22 juin 2026, arrêt 4A_547/2019, loi du 30 septembre 2011 sur la recherche. Trois schémas (capacité et représentation, chaîne de l'information, urgence et refus), captures headless de l'état simple et de l'ancre. Aucune image téléchargée ni injectée. Onze repères dans `CLICHES.json`.

| Fichier | Certitude | Porte avant | T | SHA contenu | Commit |
|---|---|---|---|---|---|
| Phase_A | VERT | VERT | 5.2 (+ 72.1) Ko | be29530616fe31f5 | 1d70039e6 → correctif porte |
| DX.1 | VERT | VERT | 5.0 (+ 36.1) Ko | 7b14696a3b9dabe2 | e13b63cb8 → correctif porte |
| DX.2 | VERT | VERT | 5.1 (+ 37.8) Ko | 6dcc20aa0de0c99a | 3616e9b65 → correctif porte |
| DX.3 | VERT | VERT | 5.1 (+ 37.7) Ko | 69bb61848ccf7ea9 | d829601ae → correctif porte |
| DX.4 | VERT | VERT | 5.0 (+ 36.4) Ko | d2ac69694f66ad02 | ec405c089 → correctif porte |
| DX.5 | VERT | VERT | 5.1 (+ 39.2) Ko | 43018c26d5347b4c | e850baa04 → correctif porte |
| DX.6 | VERT | VERT | 5.0 (+ 36.3) Ko | acc43d44ba4f2bc1 | a92eb45fb → correctif porte |
| DX.7 | VERT | VERT | 5.1 (+ 37.2) Ko | 955770148c66a504 | 4fb7ede26 → correctif porte |
| DX.8 | VERT | VERT | 5.1 (+ 36.6) Ko | 614dfd164a0a9be7 | dfdd88a5f → correctif porte |
| DX.9 | VERT | VERT | 5.0 (+ 37.7) Ko | c4330f029dc59a02 | 4ec021472 → correctif porte |
| DX.10 | VERT | VERT | 5.1 (+ 36.6) Ko | 832f88e0e55afea7 | 6c5532a10 → correctif porte |

Liste : `LISTE_DX_CANONIQUE.md`. Faits non écrits : `INCERTITUDES.md`. Prochain LOT du rédacteur B : **(fin de file : aucun, prévenir Vial)**.

## Automates actifs
Veille du routage active dans cette session (`routage_grok.py veille`, session `veille-routage-grok`). Aucune fusion, aucune étiquette `audit-ok`.

## Correctif porte — 01.11.2026 (ordre de Vial « Corrige ce qu'il faut »)
- Phrases > 35 mots : 7 gabarits scindés à la source (`rediger.py`, `allonge.py`, `cours.py`, `oral.py`), sens et articles inchangés (CC 16, 377, 378, 379, 380, 381 ; arrêt 4A_547/2019).
- Phrases répétées : `_travail/dedoublonner.py` retire, à l'assemblage, toute phrase de 8 mots ou plus déjà dite plus haut dans le même fichier (première occurrence gardée, rien d'ajouté). Phase A : titres `<h3>` des développements une fois par situation.
- DX.6 : deux paragraphes propres au dossier (gabarit de trace, retrait du oui au bloc) pour rester au-dessus de 36 Ko.
- Mesures : porte 11/11 VERT (phrase_longue 0, phrase_double 0), certitude 11/11 VERT, conscience 0 BLOQUANT / 0 SIGNAL. y DX 36,1–39,2 Ko, Phase A 72,1 Ko. Éléments centraux conservés (capacité, information, liberté, urgence, représentant, directives, mineur, refus).
