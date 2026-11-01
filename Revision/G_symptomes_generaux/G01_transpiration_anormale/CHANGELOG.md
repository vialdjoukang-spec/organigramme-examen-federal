# LOT_001 · G1 Type A — CHANGELOG

## v3.0.0 (1 nov. 2026, Zurich UTC+1) — couverture DD 15/15
- Migration vers `Revision/G_symptomes_generaux/G01_transpiration_anormale/` (banque `_bank_G01.py`, build générique `_outils/scripts/build_ssp.py`). Les originaux de `QCM-banque/LOT_001/` sont intacts.
- **+11 questions EX** (40 → 51) pour que chaque DX ait ≥ 2 EX cibles : DX.2 (exclure l'organique avant le trouble panique), DX.3 (réduire l'insuline sous aGLP-1), DX.5 (sels d'aluminium en 1re ligne), DX.7 (fièvre sous carbimazole → arrêt + hémogramme), DX.8 (sevrage d'ISRS), DX.9 (paludisme malgré prophylaxie), DX.10 (sueur asymétrique tardive → cause avant traitement), DX.11 (contact TB < 5 ans → test sans délai), DX.12 (sueurs nocturnes isolées → pas de biopsie, réévaluer), DX.14 (VIH 4e gén. négatif à 3 semaines → test moléculaire), DX.15 (NT-proBNP + écho dans le syndrome carcinoïde).
- Sources : exclusivement Phase B DX.n §13/§14 de `repo/LOT_Claude_Finaux/LOT_001/` (0 lien cassé).
- **Clés stables** : les 40 questions existantes gardent leur id et leur lettre (progression localStorage `LOT001_G1_TypeA_v2` conservée) ; seules les nouvelles équilibrent A–E → A11 B10 C10 D10 E10.
- Total : 34 EX · 10 AP · 7 SPE ; 13 R · 29 D · 9 P. Test Chrome 390 px : 0 commentaire visible au chargement et après un choix ; visible seulement après 💡.
- PDF régénéré (questions puis corrigé en annexe).

## v2.0.0 (1 nov. 2026, 22 h, Zurich UTC+1)

## Réponses plus jamais exposées (correctif urgent)
- Aucun `<details open>` dans le HTML. Le feedback `.fb` est masqué par défaut ; règle écran explicite `details.reveal:not([open]) .fb{display:none!important}`.
- Choisir une option = marque juste/faux sur les options + ligne « ✔ Juste / ✘ Faux » ; **le commentaire ne s'ouvre jamais seul** : seul le 💡 l'ouvre.
- « Tout révéler » supprimé → bouton **📖 Mode révision** avec confirmation (et « Quitter le mode révision »). État non mémorisé : au rechargement, tout est refermé.
- Plus de handler `beforeprint` qui dépliait les `<details>` à l'écran.
- PDF : questions **sans** réponses (p. 1–23), **corrigé commenté en annexe** à partir de la p. 24.
- Vérifié sous Chrome headless (mobile 390 px) : 0 feedback visible au chargement, après un choix et après rechargement ; visible seulement après 💡 ou mode révision confirmé.

## Trois niveaux (doléance Vial)
- **EX** (noir #1a1a1a) 23 Q · **AP** (bleu #0B5A8C, texte en bleu) 10 Q · **SPE** (violet #6B2D8B, badge `SPE · spécialité`) 7 Q = **40 Q** (57,5 / 25 / 17,5 %).
- SPE : Cardiologie, Dermatologie, Endocrinologie, Hématologie, Infectiologie, Oncologie (TNE), Psychiatrie.
- Bouton 🔥 sur chaque question SPE → tableau par spécialité (juste/posées, 🔥) + « Spécialité qui vous exalte ».
- Filtres Tous / EX / AP / SPE ; score par niveau, par bloc et par spécialité.

## Contenu
- 33 questions v1 conservées (ids inchangés) ; 10 reclassées (5 AP, 5 SPE).
- 7 nouvelles : AP (coup de chaleur vs fièvre, fézolinétant/NK3, toxine botulique/SNAP-25, sevrage/GABA-A, apnées/décharge sympathique) ; SPE (Psychiatrie : délai ISRS dans le trouble panique ; Hématologie : Deauville 4 en fin de traitement d'un LH). Faits issus exclusivement de Phase B DX.1/2/3/5/6/9/12 (sections 6 et 13).
- Clés rééquilibrées : 8 × A–E, jamais 3 identiques d'affilée.
- JSON : champs `niveau`, `specialite`, `media`, version 2.0.0.

## Images
- Aucune `<img>`, `<svg>`, `<figure>` ni data-URI image dans les 16 HTML LOT_001 → `media: null` partout, aucun bouton 🖼 (le code le gère si un média réel est ajouté).

## Divers
- Police Atkinson Hyperlegible intégrée (woff2 issue des leçons) → 100 % hors ligne.
- v1 archivée dans `_v1/`. Builders : `_bank_g1_v2.py`, `_template_v2.html`, `build_g1_v2.py` (+ `_print_v2.html` pour le PDF).
