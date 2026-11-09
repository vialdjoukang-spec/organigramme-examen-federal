# CHANGEMENTS — PROMPT ULTIME V0, rév. 9.11.2026 (la version la plus récente fait foi)

Base : `PROMPT_Casern/PROMPT_ULTIME_PRODUCTION_LOTS_V0.md` rév. 30.10.2026 (`a6a0285`, SHA-256 e8351b63…afd01), lecture seule. Nouvelle version : `PROMPT_ULTIME_PRODUCTION_LOTS_V0_rev20261109.md` (SHA-256 c9ba302aa1a860a80b5e381f18b9e9dd5f3aaae76f49d05a159681b99d600c08). **Inchangés :** plan 14 points, format 1 + 10, noms de fichiers, bande 80–150 Ko, sections 1–23 et leurs ancres. Ordre Vial du 9.11.2026.

| § | Avant | Après |
|---|---|---|
| En-tête, métadonnées, pied | rév. 30.10 | + bandeau « rév. 9.11.2026 — la version la plus récente fait foi » ; sommaire + §24 |
| §11 intro | 14 points | + les 14 parties **forment la monographie** quand elles s'appliquent ; partie non applicable **signalée** (raison), jamais inventée ni remplie, « sans objet » au score |
| §11 point 9 | 9.a–9.d, tableau d'interprétation | + **au minimum** gold standard et/ou 1<sup>re</sup> intention sous sous-titre explicite ; **biologie** : résultats → interprétation → hypothèse (normal, positif, limite, discordant ; SI suisses) ; images + interprétation (§14.8) ; terminologie dédiée (§24) ; concision |
| §12.1 | Q9.1–Q9.6 | + **Q9.7** (gold standard / 1<sup>re</sup> intention, critique si absents), **Q9.8** biologie tabulée, **Q9.9** images, **Q9.10** terminologie dédiée, **Q9.11** fenêtres p9, **Q9.12** concision |
| §14.2 | « aucune image » | aucune image **externe** ; images embarquées du point 9 permises ; **formule en image toujours interdite** |
| §14.3 | popover par défaut | + fenêtre par défaut `<details style='display:inline;'>` (mécanisme, exemple chiffré, piège, [Sn]) ; aucune dans les phrases-clés p13 ; **une fenêtre d'urgence par 11.C** ; piège `<details>` dans `<p>` → `<div class="p">` |
| §14.7 *(nouveau)* | — | `lang="fr"`, `text-align: justify; hyphens: auto`, 14 **îlots** `<section class="ilot">` |
| §14.8 *(nouveau)* | — | Images p9 : Wikimedia Commons / Open-i / Europe PMC OA ; CC0, CC BY, CC BY-SA, DP ; légende source+auteur+licence ; anomalies entourées en pointillés contrastés ; `<ol>` numérotée concordante ; sémiologie du syndrome ; data:URI WebP/JPEG ≤ ~25 Ko ; `harnais illustrer` ; pas d'image libre fiable → le **signaler** |
| §16 rapport | Critique/Grave/Moyen/Léger | + rapport **ultra concis, structuré, coloré**, 5 classes : syntaxe, sémantique, langue, sources, sécurité |
| §17 | « 150–200 Ko » (reliquat contradictoire) | **80–150 Ko** (aligné §14) ; + interdits : image non libre/externe/non annotée/inventée ; terme vague si terme dédié existe |
| §19 checklist | — | + 8 cases : point 9 (minimum, biologie, images), terminologie, monographie/non applicable, « non validé cliniquement », fenêtres inline/`<div class="p">`, justification/îlots, rapport d'audit 5 classes |
| §22.5 *(nouveau)* | — | Gemma rédige **une seule fois** ; l'auditeur corrige tout ; **retrait de Gemma s'il n'aide pas** : part conservée sans réécriture < 50 % **ou** temps total ≥ rédaction directe (mesuré par DX, `JOURNAL.md`) ; 80–150 Ko ; « non validé cliniquement » |
| §24 *(nouveau)* | — | **Terminologie dédiée** obligatoire par modalité (radio, TDM, IRM, écho, ECG, spirométrie, biologie), vérifiée (registre suisse d'abord, puis sociétés francophones), termes vagues interdits, une fenêtre par terme ; 12 sources T1–T12 consultées le 9.11.2026 |

**Exemples retirés faute de source :** aucun (tous les exemples demandés retrouvés). Nuances : « onde Q de nécrose » sourcée hors société savante (e-cardiogram) → écrite « onde Q pathologique (« onde Q de nécrose ») », RMS ; « hyperdensité/hypodensité » attestées comme adjectifs (CNP-MN) et « hypodensité » (Revue du Praticien, non citée) ; seuil Gemma 50 % = règle d'économie de Vial, pas un chiffre externe.

**Harnais** (`coeur/harnais.py`) : `controler` + critique « p9 sans sous-titre gold standard ni 1re intention », + avertissement « termes vagues p9 » ; `squelette` porte 9.a/9.b. Tests : 16 réussis, 1 ignoré (15 anciens intacts + 1 nouveau).
