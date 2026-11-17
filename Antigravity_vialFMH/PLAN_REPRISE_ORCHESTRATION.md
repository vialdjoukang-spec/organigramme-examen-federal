# Plan de reprise Antigravity & Orchestration économique (248 LOTs / 2 728 cours)

**Référence dépôt** : `origin/main` @ `73d8437` (`2026-11-16`) · **Propriété ouverte** : `ATTRIBUTIONS.json` (`ordre_2026_11_11`) + `ChatGPT_Codex/PASSATION_OUVERTE.md`.

> **BASCULE PRIORITAIRE ACTIVE — PHASE P0 (`17.11.2026`)** : Sur instruction directe de l'utilisateur, le flux de remédiation secondaire (`W0–W5`) est **mis en pause** au profit de la production L1 immédiate des **47 LOTs / 370 cours sans contenu didactique** (`194` `ABSENT` + `176` `EBAUCHE_STUB` `< 20 Ko`).  
> 👉 **Feuille de route prioritaire active** : [`Antigravity_vialFMH/PLAN_REPRISE_ABSENTS.md`](PLAN_REPRISE_ABSENTS.md) · **Journal de reprise sur quota** : [`Antigravity_vialFMH/CHECKPOINT_ABSENTS.json`](CHECKPOINT_ABSENTS.json).  
> Dès que `CHECKPOINT_ABSENTS.json → resume_cursor.remaining_courses == 0`, reprendre le schéma normal `W0 → W5` décrit ci-dessous.

---

## 1. État réel mesuré sur disque (`generer_jauges.py`)

- **Priorité P0 (cours sans contenu didactique)** : **`47` LOTs / `370` cours** — `194` `ABSENT` (`10` `T9` = `110`, `5` `T5` = `12`, `1` `T7` = `2`, `13` `T8d` = `70`) + `176` `EBAUCHE_STUB` `< 20 Ko` (`16` `T8e` = `173` + `2` `T8c` résiduels `158, 160` = `3`).
- **Couverture L1 auditée** : **`33 / 248` LOTs (`13,3 %`, `363` cours)** — `T1` (`1` Antigravity `033`), `T2a` (`6` Claude `ACCEPTE` `017–022`), `T2b` (`16` Claude `001–016`), `T2c` (`10` Claude `023–032`).
- **Score composite moyen global (`G1–G8`)** : **`50,0 / 100`** (`G`: `92,6`, `S`: `54,7`, `F`: `41,6`, `O`: `38,8`).
- **Maturité d'audit réelle (`0–4`)** : Niveau `0` = `212` · Niveau `1` = `3` (`081–083` V0) · Niveau `2` = `24` (`001–010, 012, 014–016, 023–032`) · Niveau `3` = `9` (`011, 013`, `017–022`, `033`) · Niveau `4` (`MANIFESTE.json` SHA-256 exact + `ACCEPTE`) = **`0`** (`55` manifestes présents dont `52` SHA-256 exacts : `3` Codex + `49` Grokbot).

---

## 2. Prérequis gratuits (0 token modèle) avant toute vague clinique

Ces actions d'outillage suppriment les blocages mesurés dans `Claude/_outils/` et unifient les critères d'Antigravity avec ceux de `Claude/` :

1. **Correctifs Python 3.11 sur `Claude/_outils/forme.py:326` et `Claude/_outils/migrer_l1.py:121`** : supprimer le backslash dans l'expression f-string (`re.sub(...)` sorti en variable locale) — actuellement `SyntaxError` sous Python `3.11.2`.
2. **Alignement L1 des contrôleurs** : utiliser `Claude/_outils/controle3.py --script-ok` (`80_000–150_000` octets hors images, `forme.js` autorisé) ; mettre à niveau ou ignorer les anciens seuils `100_000–200_000` (`script_ok=False`) de `Claude/_outils/detecteur_lots.py:88` et `harnais/controle_lot.py:24,91`.
3. **Matérialisation du convertisseur bidirectionnel `bundle ↔ 11 HTML`** pour Antigravity :
   - Produire les **11 fichiers séparés** (`LOT_NNN_Phase_A_V0.html` + `DX.1..10`) liés à `../_polices/forme.css` & `forme.js`, fond `#fff` pur (`0` `#f9f5ee`, `0` bleu `150°–305°`), avec `<!-- FIN_FICHIER ... -->` et `MANIFESTE.json`.
   - Générer `LOT_NNN_<CODE>_complet.html` comme **export dérivé** depuis les 11 HTML validés (sans `<script>` custom en pied de page).
4. **Réconciliation des PRs ouvertes P0 (`#524–#539`, `#732–#740`, `#575, #584, #592–#598`)** : récupérer les `LISTE_DX_CANONIQUE.md` gelées, `paquet.json`, `Phase A`/`DX.1` L1 et brouillons `Lo_9.11.26` avant toute rédaction neuve.
5. **Corpus AIPS (`PR #512`) + cache refdata/imagerie partagé** : charger `AipsDownload_20261008.xml` (`25,2 Mo`) et `4 631` `fi_fr/*.txt.gz` depuis `agentA/corpus-ressources-20261109` en espace scratch, avec `data/ck/doses_ch.json` et `imagerie_GROK/` (`555` manifestes, en évitant la confusion `EXP-045` vs `LOT_045`).

---

## 3. Principe d'orchestration puissant et économique

### A. Règle des 3 routages (économie maximale de tokens)
Sur la base des jauges `G1–G8` calculées gratuitement par `Antigravity_vialFMH/generer_jauges.py` :

| Profil mesuré | Décision d'orchestration | Coût LLM |
|---|---|---|
| **`ABSENT` (`194` cours), `EBAUCHE_STUB` (`176` cours)** — **PRIORITÉ P0** | **File P0 (`A1 → A2 → B → B2 → C1 → C2`)** : réutiliser `#524–#539` / `#732–#740` / `#575, #584, #593–#598`, réécrire les `5` `T5` dupliqués, rédiger les manquants en L1 après gel P1 (`PLAN_REPRISE_ABSENTS.md`). | Prioritaire (retour sur investissement maximal) |
| **`G1, G2, G5, G8` PASS (`PRET_AUDIT`)** — `237` cours actuels *(reprise `W0–W5`)* | **0 rédaction** : envoi direct à `planche5.py` + `Audit 1` ciblé. | Minimal (audit seul) |
| **`L1_MECANIQUE_PARTIEL` (`T3`, `T6`, `T8a`, `T8b`)** *(reprise `W0–W5`)* | **Patch chirurgical** sur les seuls axes rouges (`forme.py` gratuit pour `G8`, `renfort_citations.py` pour `G4`, ajout `.mb`/Pt 14 Q&R pour `G5/G6`). | Faible (retouche ciblée) |

### B. Topologie d'équipe & parallélisme sans collision
- **File active bornée** : `4` à `10` LOTs en parallèle (`CONSIGNES_VIAL.md:47`, `PROTOCOLE_FABLE.md:77`), **1 worktree Git isolé par LOT** (`antigravity/lot-NNN`), **0 écriture croisée** (`ANTI_COLLISION_PARALLELISME_ABSOLU.md`).
- **Pipelinage Phase A → Phase B (`1 + 5` ou `1 + 10`)** :
  1. **Chef de LOT (raisonnement élevé)** : vérifie/rédige `Phase A` + `LISTE_DX_CANONIQUE.md` → audit P1 → `Claude/_outils/geler.py` (verrou SHA-256). Dès le gel P1 du LOT `N`, le chef de LOT passe au LOT `N+1`.
  2. **Rédacteurs Phase B (5 agents × 2 DX max, ou jusqu'à 10 en parallèle)** : chacun ne charge que `Phase A` gelée + son extrait source/AIPS (`Claude/_outils/paquet.py`) + gabarit L1, et valide uniquement son fichier (`git commit -- <fichier>`). Remplacement gratuit d'un agent au-delà de `≤ 10` chapitres cumulés (`CONSIGNES_VIAL.md:48`).
  3. **Portes gratuites obligatoires (`0` token)** : `forme.py` → `controle3.py --script-ok` → `verif_aips.py` → `inventaire_images.py` → `planche5.py` → `generer_jauges.py`. Aucun auditeur n'est invoqué si une porte mécanique est `ROUGE`.
  4. **Auditeurs indépendants (`Audit 1` puis `Contre-audit 2`)** :
     - Jamais l'auteur du texte ; `Contre-audit 2` ≠ `Audit 1` ; 2 demi-passes (`PA + DX.1–5` et `DX.6–10`) pour tenir la fenêtre de contexte.
     - **Contexte minimal (-70 % tokens)** : l'auditeur reçoit **uniquement** les sorties JSON de `controle3.py`/`verif_aips.py`, `LISTE_DX_CANONIQUE.md`, `HELP.md`, les points à haut risque (`1, 3, 4, 6, 8, 9, 10, 11, 14` + `.mb` + biblio) et `planche5.py`.
     - Corrections émises en patch JSON exact `{"avant": "...", "apres": "..."}`, appliquées sans réécriture globale.
  5. **Clôture PR** : génération `MANIFESTE.json` SHA-256 (`Claude/_outils/lecon.py manifeste`), contrôle `generer_jauges.py --check`, PR avec `Prompt L1 lu et appliqué` + `## Automates actifs`, fusion `--merge` après CI verte (`garde`, `html`, `tests`, `visuel`, `checkpoint`).

---

## 4. Articulation Phase P0 (urgente) → Retour au schéma normal (`W0` → `W5`)

1. **Temps 1 — Phase P0 Absents & Stubs (`PLAN_REPRISE_ABSENTS.md`)** : solder les `47` LOTs / `370` cours sans contenu didactique (`A1` `045,080,102` → `A2` `043,044,046–050` → `B/B2` `16 T8e + 158,160` → `C1` `T5/T7` → `C2` `13 T8d`), avec suivi atomique dans `CHECKPOINT_ABSENTS.json`.
2. **Temps 2 — Retour au schéma normal (`W0` → `W5`, `248` LOTs)** une fois `remaining_courses == 0` :

| Vague normale | Périmètre exact | LOTs | Cours | Priorité & Stratégie après clôture P0 |
|---|---|---:|---:|---|
| **`DONE`** | `T2a` (`LOT_017–022`) | **6** | 66 | Déjà `ACCEPTE` (`mat=3`) ; génération `MANIFESTE.json` SHA-256 uniquement (et contrôle image `020 DX.1`). |
| **`W0`** | Clôture audits & harmonisation : `T2b` (`001–016`), `T2c` (`023–032`), `T1` (`033`), reliquats `T9` déjà intégrés en P0 | **36** | 396 | Solder les reliquats `audit2` (`001–010, 012, 014–016`) + `MANIFESTE` (`011, 013`), produire `phase_B.contre_audit.json` (`025–032`), exporter `LOT_033` en 11 HTML `forme.css` `#fff` sans `<script>` custom. |
| **`W1`** | `Claude` `T3` + `T4/T5` proches (`034–042`, `109`, `111`) | **11** | 121 | `034–039, 109, 111` ont déjà `:target` `fenetre` → patch ciblé `forme.py` + `sup.r` + `verif_aips` (`041, 042` déjà traités en P0-C1). |
| **`W2`** | `T9` orphelin (`045`) + `16` stubs `T8e` | **17** | 187 | **Déjà soldés en amont par P0-A1 & P0-B** → vérification finale de conformité & `MANIFESTE.json`. |
| **`W3`** | `Claude` héritage & partiels restants (`072–078`, `104–108`, `110`) | **13** | 143 | Migration L1 + double audit (`075–077` déjà traités en P0-C1). |
| **`W4`** | Reprise ouverte `ChatGPT_Codex` (`T6` `081–083` + `T7` `112–113, 115, 117, 119, 121–132`) | **20** | 220 | Clôture définitive de `S` et début `F` (`081–083` ont déjà `MANIFESTE` SHA-256 exact ; `122` déjà complété en P0-C1). |
| **`W5`** | Reprise industrielle `Grokbot` (`T8a` `133`, `T8b` `39`, `T8c` `92`, `T8d` `13`) | **145** | 1 595 | Traitement prioritaire de **`F`** (`133–173`) puis **`O`** (`174–248`) en files actives de `10` LOTs (`T8d` et `158, 160` déjà soldés en P0). |
| **TOTAL** | **Catalogue complet `248` PROFILES 2023** | **248** | **2 728** | **100 % traçable dans `jauges_248_lots.json`, `jauges_2728_cours.csv` et `CHECKPOINT_ABSENTS.json`.** |
