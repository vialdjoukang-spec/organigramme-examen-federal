# Plan de reprise Antigravity & Orchestration économique (248 LOTs / 2 728 cours)

**Référence dépôt** : `origin/main` @ `73d8437` (`2026-11-16`) · **Propriété ouverte** : `ATTRIBUTIONS.json` (`ordre_2026_11_11`) + `ChatGPT_Codex/PASSATION_OUVERTE.md`.

---

## 1. État réel mesuré sur disque (`generer_jauges.py`)

- **Couverture L1 auditée** : **`33 / 248` LOTs (`13,3 %`, `363` cours)** — `T1` (`1` Antigravity `033`), `T2a` (`6` Claude `ACCEPTE` `017–022`), `T2b` (`16` Claude `001–016`), `T2c` (`10` Claude `023–032`).
- **Reste à traiter** : **`215 / 248` LOTs (`86,7 %`, `2 365` cours)**, dont `194` cours physiquement absents de `main` (`110` sur les `10` LOTs `T9`, `84` sur les `19` LOTs partiels `T5`/`T7`/`T8d`) et `176` ébauches `< 20 Ko` (`16` LOTs `T8e`).
- **Score composite moyen global (`G1–G8`)** : **`49,5 / 100`** (`G`: `87,7`, `S`: `54,6`, `F`: `41,3`, `O`: `38,6`).
- **Maturité d'audit (`0–4`)** : Niveau `0` = `212` · Niveau `1` = `3` (`081–083` V0) · Niveau `2` = `20` · Niveau `3` = `13` (`002,006,007,008,011,013`, `017–022`, `033`) · Niveau `4` (`MANIFESTE.json` SHA-256 exact + `ACCEPTE`) = **`0`**.

---

## 2. Pré-requis gratuits (0 token modèle) avant toute vague clinique

Ces actions d'outillage suppriment les blocages mesurés dans `Claude/_outils/` et unifient les critères d'Antigravity avec ceux de `Claude/` :

1. **Correctif Python 3.11 sur `Claude/_outils/forme.py:326`** : supprimer le backslash dans l'expression f-string (`re.sub(r"^[0-9.\s]+", "", lib)` sorti en variable locale) — actuellement `SyntaxError` sous Python `3.11.2`.
2. **Alignement L1 de `Claude/_outils/detecteur_lots.py:88` et `harnais/controle_lot.py:24,91`** : passer de `100_000–200_000` (`script_ok=False`) à `80_000–150_000` hors images (`script_ok=True` pour `../_polices/forme.js`), afin de ne plus pénaliser les cours L1 conformes.
3. **Matérialisation du convertisseur bidirectionnel `bundle ↔ 11 HTML`** pour Antigravity :
   - Produire les **11 fichiers séparés** (`LOT_NNN_Phase_A_V0.html` + `DX.1..10`) liés à `../_polices/forme.css` & `forme.js`, fond `#fff` pur (`0` `#f9f5ee`, `0` bleu `150°–305°`), avec `<!-- FIN_FICHIER ... -->` et `MANIFESTE.json`.
   - Générer `LOT_NNN_<CODE>_complet.html` comme **export dérivé** depuis les 11 HTML validés (et non comme source primaire divergente).
4. **Réconciliation des PRs brouillons `#732–#740` (15.11.2026)** : récupérer et auditer les `25` HTML déjà produits pour `LOT_043, 044, 046–050, 080, 102` avant de relancer des rédacteurs sur `T9`.
5. **Requête `verif_aips.py` + cache refdata partagé** : indexer localement les extraits AIPS déjà validés et `imagerie_GROK/` (`555` manifestes) en lecture partagée (0 téléchargement redondant).

---

## 3. Principe d'orchestration puissant et économique

### A. Règle des 3 routages (économie maximale de tokens)
Sur la base des jauges `G1–G8` calculées gratuitement par `Antigravity_vialFMH/generer_jauges.py` :

| Profil mesuré | Décision d'orchestration | Coût LLM |
|---|---|---|
| **`G1, G2, G5, G8` PASS (`PRET_AUDIT`)** — `255` cours actuels | **0 rédaction** : envoi direct à `planche5.py` + `Audit 1` ciblé. | Minimal (audit seul) |
| **`L1_MECANIQUE_PARTIEL` (`T3`, `T6`, `T8a`, `T8b`)** | **Patch chirurgical** sur les seuls axes rouges (`forme.py` gratuit pour `G8`, `renfort_citations.py` pour `G4`, ajout `.mb`/Pt 14 Q&R pour `G5/G6`). | Faible (retouche ciblée) |
| **`ABSENT` (`T9`, `194` cours), `EBAUCHE_STUB` (`T8e`, `176` cours), `HERITAGE_PRE_L1`** | **Rédaction complète L1** selon `PROTOCOLE_FABLE.md` après gel P1. | Standard contrôlé |

### B. Topologie d'équipe & parallélisme sans collision
- **File active bornée** : `4` à `10` LOTs en parallèle (`CONSIGNES_VIAL.md:47`, `PROTOCOLE_FABLE.md:77`), **1 worktree Git isolé par LOT** (`antigravity/lot-NNN`), **0 écriture croisée** (`ANTI_COLLISION_PARALLELISME_ABSOLU.md`).
- **Pipelinage Phase A → Phase B (`1 + 5` ou `1 + 10`)** :
  1. **Chef de LOT (raisonnement élevé)** : vérifie/rédige `Phase A` + `LISTE_DX_CANONIQUE.md` → audit P1 → `geler.py` (verrou SHA-256). Dès le gel P1 du LOT `N`, le chef de LOT passe au LOT `N+1`.
  2. **Rédacteurs Phase B (5 agents × 2 DX max, ou jusqu'à 10 en parallèle)** : chacun ne charge que `Phase A` gelée + son extrait source/AIPS + gabarit L1, et valide uniquement son fichier (`git commit -- <fichier>`). Remplacement gratuit d'un agent au-delà de `≤ 10` chapitres cumulés (`CONSIGNES_VIAL.md:48`).
  3. **Portes gratuites obligatoires (`0` token)** : `forme.py` → `controle3.py --script-ok` → `verif_aips.py` → `inventaire_images.py` → `planche5.py` → `generer_jauges.py`. Aucun auditeur n'est invoqué si une porte mécanique est `ROUGE`.
  4. **Auditeurs indépendants (`Audit 1` puis `Contre-audit 2`)** :
     - Jamais l'auteur du texte ; `Contre-audit 2` ≠ `Audit 1` ; 2 demi-passes (`PA + DX.1–5` et `DX.6–10`) pour tenir la fenêtre de contexte.
     - **Contexte minimal (-70 % tokens)** : l'auditeur reçoit **uniquement** les sorties JSON de `controle3.py`/`verif_aips.py`, `LISTE_DX_CANONIQUE.md`, `HELP.md`, les points à haut risque (`1, 3, 4, 6, 8, 9, 10, 11, 14` + `.mb` + biblio) et `planche5.py`.
     - Corrections émises en patch JSON exact `{"avant": "...", "apres": "..."}`, appliquées sans réécriture globale.
  5. **Clôture PR** : génération `MANIFESTE.json` SHA-256, contrôle `generer_jauges.py --check`, PR avec `Prompt L1 lu et appliqué` + `## Automates actifs`, fusion `--merge` après CI verte (`garde`, `html`, `tests`, `visuel`, `checkpoint`).

---

## 4. Plan de reprise par vagues (`W0` → `W5`) — Total = `248` LOTs

| Vague | Périmètre exact | LOTs | Cours | Priorité & Stratégie |
|---|---|---:|---:|---|
| **`DONE`** | `T2a` (`LOT_017–022`) | **6** | 66 | Déjà `ACCEPTE` (`mat=3`) ; génération `MANIFESTE.json` SHA-256 uniquement (et contrôle image `020 DX.1`). |
| **`W0`** | Clôture audits & harmonisation : `T2b` (`001–016`), `T2c` (`023–032`), `T1` (`033`), `T9` avec PR `#732–#740` (`043,044,046–050,080,102`) | **36** | 396 | **Urgence immédiate** : solder les reliquats `audit2` (`001–016`), produire `phase_B.contre_audit.json` (`025–032`), exporter `LOT_033` en 11 HTML `forme.css` `#fff`, réconcilier les `9` PRs `#732–#740`. |
| **`W1`** | `Claude` `T3` + `T4/T5` proches (`034–042`, `109`, `111`) | **11** | 121 | `034–039, 109, 111` ont déjà `:target` `fenetre` → patch ciblé `forme.py` + `sup.r` + `verif_aips` + compléter `041` (`10/11`) & `042` (`9/11`). |
| **`W2`** | `T9` orphelin (`045` / `S2.6`) + `16` stubs `T8e` (`051–054, 058–059, 103, 114, 116, 118, 120, 230, 236, 240, 246, 247`) | **17** | 187 | Rédaction L1 complète `1 + 5` (clôt le groupe **`S`** sur `S2–S3` et supprime les coquilles `< 20 Ko`). |
| **`W3`** | `Claude` héritage & partiels restants (`072–078`, `104–108`, `110`) | **13** | 143 | Migration L1 + complétion `075` (`8/11`), `076` (`9/11`), `077` (`7/11`) + double audit. |
| **`W4`** | Reprise ouverte `ChatGPT_Codex` (`T6` `081–083` + `T7` `112–113, 115, 117, 119, 121–132`) | **20** | 220 | Clôture définitive des groupes **`S`** (`S5–S8`) et début **`F`** (`130–132`). `081–083` ont déjà citations & fenêtres V0 (`score=72–75`), passage L1 accéléré. |
| **`W5`** | Reprise industrielle `Grokbot` (`T8a` `133`, `T8b` `39`, `T8c` `92`, `T8d` `13`) | **145** | 1 595 | Traitement prioritaire de **`F`** (`133–173`) puis **`O`** (`174–248`) en files actives de `10` LOTs : d'abord `T8a/T8b` (`40` LOTs déjà dans `80–150 Ko`), puis `T8c` (`92`), puis `T8d` (`13` partiels). |
| **TOTAL** | **Catalogue complet `248` PROFILES 2023** | **248** | **2 728** | **100 % traçable dans `jauges_248_lots.json` et `jauges_2728_cours.csv`.** |
