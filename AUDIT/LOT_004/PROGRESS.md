# LOT_004 — progression (audit du 24.10.2026)
Thème : SSP G4 « Fatigue, épuisement » + 10 DX (originaux : originaux/LOT_004/, 5 exports Google Docs V5).
Méthode (copiée de LOT_003) : source/gen_xxx.py importe source/lot4_commun.py (→ source/outils_local/gen_v7l.py, sources src_lot4.py, DIFF commun, SOCIAL, FICHE).
Évaluation : source/eval.sh (decoupe_l → examens → style → score → verif_v7) ; contraste : venv/bin/python outils/contraste.py <chemins absolus>.
decoupe_l.py : le motif `^SSP(\s+G\d+)?\s*·` reconnaît « SSP G4 · … ».
Aucune capture (consigne utilisateur). Écriture uniquement dans corriges/LOT_004/ (+ work/LOT_004_AUDITE écrit par les outils d'évaluation partagés).
Scores AVANT (work/LOT_004/score.json) : SSP 30,0 · DX1 30,0 · DX2 28,8 · DX3 31,2 · DX4 32,5 · DX5 35,0 · DX6 35,0 · DX7 33,8 · DX8 31,2 · DX9 40,0 · DX10 32,5 (LOT 32,7).
## État
- [x] Phase 0 / lecture des 11 textes (source/orig_txt) ; copies outils_local ; eval.sh
- [x] src_lot4.py, lot4_commun.py, bib_extra (19 fragments)
- [x] DX.1 … DX.10 : 98,8 % chacun, verif OK, 0 phrase > 30 mots, 0 sigle non développé, contraste 0
- [x] SSP + bloc 2 : 98,8 %, découpée _a/_b
- [x] Fenêtres d’examen : 454 cliquables / 454 à 2 onglets
- [x] RAPPORT_AUDIT.md, MANIFEST.sha256 (sha256sum -c OK)
- [x] Fichier orphelin …SSP…AUDITÉ.html.fenetres.json (version non découpée) supprimé
## Résultats (après)
| Cours | Score | Octets |
|---|---|---|
| SSP _a / _b | 98,8 % | 118 380 / 147 299 |
| DX.1 | 98,8 % | 178 897 |
| DX.2 | 98,8 % | 160 209 |
| DX.3 | 98,8 % | 131 457 |
| DX.4 | 98,8 % | 162 688 |
| DX.5 | 98,8 % | 164 019 |
| DX.6 | 98,8 % | 150 921 |
| DX.7 | 98,8 % | 157 545 |
| DX.8 | 98,8 % | 182 434 |
| DX.9 | 98,8 % | 126 386 |
| DX.10 | 98,8 % | 153 458 |
## Chiffres à vérifier
Voir la liste complète dans RAPPORT_AUDIT.md, section « Chiffres et doses à vérifier ».
Pour DX.1 à DX.5, la liste a été reconstituée en fin d’audit à partir des corrections ; à relire en priorité.
