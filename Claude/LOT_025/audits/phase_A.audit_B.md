# Audit B (conformité L1) — LOT_025 Phase A V0

Fichier : `LOT_025_Phase_A_V0.html` (81 427 octets). Vérifié : `controle_lot.py verifier` (critique reprise telle quelle), 14 points, fenêtres, image (cercles SVG superposés par PIL, regardés), liste canonique.

## Constats conformes
- 14 points présents dans l'ordre ; point 1 = définition seule (3 phrases, aucun chiffre ni conduite).
- Point 6 : 6 fenêtres = 6 régions (respiration, bouche, oropharynx, glandes, cou, extra-buccal).
- Point 14 : 8 questions, renvois (points 3, 4, 6, 8, 9, 11) exacts ; 11.A à 11.D présents ; 🚩 E1 et E2 en points 4, 8, 10.
- Fenêtres : 44 `section.fenetre`, toutes filles directes de `section.monograph` ; aucune imbrication.
- Image réelle en couleurs (Blausen, CC BY 3.0, 900×900) ; repères justes : 1 parotide, 2 extrémité du canal parotidien, 3 sous-mandibulaire, 4 sublinguale.
- Titres DX de la Phase A (tableau point 8) = liste canonique mot pour mot, même ordre.

## Corrections
1. [bloquante] Critique du harnais : « script, image ou feuille de style externe présent » : `<img src="images/Blausen_0780_SalivaryGlands.webp">` et `<image href="images/...webp">`. Correction : intégrer l'image en `data:image/webp;base64` (le modèle LOT_022 utilise aussi un fichier externe : trancher selon la règle de dépôt).
2. [bloquante pour tout le LOT] Phase B incohérente avec la liste canonique. Titres trouvés : DX.2 « DX.6 — Xérostomie médicamenteuse » ; DX.4 « DX.2 — Stomatite… » ; DX.6 « DX.4 — Gingivostomatite… » ; DX.8 « DX.9 — Abcès… » ; DX.9 « DX.10 — Carcinome… » ; DX.10 « DX.8 — Sialolithiase… ». Correction : réaligner titres, mentions « DX.n » et préfixes d'identifiants sur la liste (DX.2 Xérostomie, DX.4 Stomatite, DX.6 Gingivostomatite, DX.8 Abcès 🚩 E1, DX.9 Carcinome 🚩 E2, DX.10 Sialolithiase). Les 10 fichiers B portent aussi `title=` et n'ont pas de section Sources (critiques du harnais, hors de mon périmètre A).
3. [majeure] Abréviations non développées au premier emploi : « HUG » (point 2 : « le chiffre des HUG ») et « CHUV » (point 2 : « selon le CHUV »). Correction : « Hôpitaux universitaires de Genève (HUG) », « Centre hospitalier universitaire vaudois (CHUV) » au premier emploi.
4. [majeure] Redites : (a) débits salivaires 0,3–0,5 / 0,01–0,1 / 1–2 / 0,7 mL/min en point 3 et en fenêtre du point 9 ; (b) tableau E1/E2 du point 4 répété en point 10 ; (c) « panendoscopie avant tout traitement » en points 4, 8, 9, 11 ; (d) « Piège : la SSI ne recommande pas la culture » (fenêtre point 9) repris au point 14. Correction : garder chaque fait dans un seul point et renvoyer ailleurs par « voir point n ».
5. [majeure] Avertissement du harnais repris : mention « non validé cliniquement » absente. Correction : l'ajouter en tête.
6. [mineure] Phrase de 30 mots (limite 28) : « Le cancer de la cavité buccale et du pharynx a une survie relative à cinq ans de 54 % chez l’homme et de 63 % chez la femme en Suisse. » → couper après « cinq ans ».
7. [mineure] Point 1 : « le plus souvent virale » relève de l'épidémiologie. Correction : supprimer ce membre de phrase.
8. [mineure] Image : légendes anglaises incrustées (« Parotid gland », « Salivary Glands »). Correction : le signaler dans la légende ou choisir une version en français ; « cliché brut » dans l'attribut alt → « illustration sans repères ».
9. [mineure] Typographie : « Ce que l'image décide » (apostrophe droite) → « l’image ». Phrases de moins de 12 mots hors tableaux : « Le repère 1 montre la parotide, en avant de l’oreille. » (10 mots, idem repères 3 et 4) et « Une glande qui gonfle au repas évoque un calcul salivaire. » (10) ; les allonger à 12 mots ou plus.
10. [mineure] Point 14, question « antifongique préventif » : la réponse est en point 11 (fenêtre candidose) et 12 ; renvoi correct, mais le point 11 ne cite le fait que dans une fenêtre : ajouter une phrase dans le corps du 11.B.

## Question finale
Dépôt autorisé : **non** (corrections 1 et 2 bloquantes ; 3 à 5 majeures).
