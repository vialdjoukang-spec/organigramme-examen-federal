# `Antigravity_vialFMH` — Reprise de production, Priorité Absents, Jauges fines & Schéma d'orchestration

Ce dossier centralise les livrables analytiques, outillés et opérationnels pour organiser la **reprise de la production initiée par Antigravity** (`LOT_033` / `S1.17`, commit `73d8437`) sur l'ensemble des **248 LOTs PROFILES 2023 (`2 728` cours)**.

> **PRIORITÉ COURANTE ACTIVE (réorientation utilisateur du 17.11.2026)** : pause du flux de remédiation secondaire et **bascule immédiate sur la file P0 des LOTs/cours sans contenu didactique (`47` LOTs / `370` cours = `194` `ABSENT` + `176` `EBAUCHE_STUB` `<20 Ko`)** conformément au Prompt L1, avec check-points de reprise sur quota consignés dans [`PLAN_REPRISE_ABSENTS.md`](PLAN_REPRISE_ABSENTS.md) et [`CHECKPOINT_ABSENTS.json`](CHECKPOINT_ABSENTS.json). Retour au schéma normal [`PLAN_REPRISE_ORCHESTRATION.md`](PLAN_REPRISE_ORCHESTRATION.md) (`W0 → W5`) une fois la phase P0 soldée.

---

## 1. Synthèse exécutive (mesures exactes sur `main` @ `73d8437` après audit critique)

- **File prioritaire P0 (Absents & Stubs)** : **`47` LOTs / `370` cours sans contenu didactique** — `194` `ABSENT` (`10` `T9` = `110`, `5` `T5` = `12`, `1` `T7` = `2`, `13` `T8d` = `70`) + `176` `EBAUCHE_STUB` `< 20 Ko` (`16` `T8e` = `173` + `2` `T8c` résiduels `158, 160` = `3`).
- **Production L1 auditée** : **`33 / 248` LOTs (`13,3 %`, `363` cours)** — `T1` (`1` Antigravity `LOT_033`), `T2a` (`6` Claude `ACCEPTE` `017–022`), `T2b` (`16` Claude `001–016`), `T2c` (`10` Claude `023–032`).
- **Maturité d'audit réelle (`0–4`)** : `0: 212` · `1: 3` (`081–083`) · `2: 24` · `3: 9` (`011, 013, 017–022, 033`) · `4: 0` (`MANIFESTE.json` présents : `55/248`, SHA-256 exacts : `52/55`).
- **Score composite moyen global (`G1–G8`)** : **`50,0 / 100`** (`G`: `92,6`, `S`: `54,7`, `F`: `41,6`, `O`: `38,8`). Statuts cours (`2 728`) : `AUDITE_CONFORME: 80` · `PRET_AUDIT: 237` · `L1_MECANIQUE_PARTIEL: 1 766` · `HERITAGE_PRE_L1: 275` · `EBAUCHE_STUB: 176` · `ABSENT: 194`.
- **Découvertes clés** :
  1. **Gisements immédiats pour la file P0 (`T9` + `T8e`)** : les **10 LOTs `T9` (`110` cours)** disposent tous de matière réutilisable dans des PRs ouvertes (`#524–#539` avec `LISTE_DX_CANONIQUE.md` gelée SHA-256 + `paquet.json`, et `#732–#740` L1 `Phase A` + `DX.1` ; seul `045` est sans `#73x` mais possède `#524`). De même, `6` LOTs `T8e` (`051–054, 058–059`) disposent des PRs `#575, #584, #593–#598`, et `PR #512` fournit `AipsDownload_20261008.xml` + `4 631` notices `fi_fr`.
  2. **Divergence de format d'Antigravity (`LOT_033`)** : `LOT_033_S1.17_complet.html` (`5,97 Mo`) passe les `4` portes cliniques (`97,1 %`, `96,4 %`, `CLEAN`, `APPROVE`), mais obtient `G1=91,7`, `G8=20,0`, `score=76,7` (bundle monolithique vs 11 HTML attendus par `FedMed_Progression.html`, fond crème `#f9f5ee`, `<script>` en pied de `<body>` hors `<article>`).
  3. **Prérequis 0-token sur cette VM** : corriger l'erreur Python 3.11 (antislash dans f-string) dans `Claude/_outils/forme.py:326` et `Claude/_outils/migrer_l1.py:121`, et utiliser `controle3.py --script-ok` (seuil L1 `80–150 Ko`) plutôt que `detecteur_lots.py:88` / `harnais/controle_lot.py:24,91` (`100–200 Ko`).

---

## 2. Index des fichiers de `Antigravity_vialFMH/`

| Fichier | Rôle |
|---|---|
| `README.md` | Synthèse exécutive, priorité P0 Absents, index des livrables et reproduction |
| `PLAN_REPRISE_ABSENTS.md` | **Priorité courante P0** : inventaire complet des `47` LOTs / `370` cours sans contenu didactique, file ordonnée `A1 → A2 → B → B2 → C1 → C2`, PRs réutilisables et protocole de reprise sur quota |
| `CHECKPOINT_ABSENTS.json` | Journal machine déterministe (`resume_cursor`, `projection_reprise`, `queue` par LOT et par module) pour reprise exacte en cas de limite de quota |
| `SCHEMA_PRODUCTION_ROBUSTE.md` | Relevé des mises à jour (`10–17.11.2026`) et schéma concis (Mermaid + leviers chiffrés) incluant la phase P0 |
| `PLAN_REPRISE_ORCHESTRATION.md` | Plan complet de reprise Antigravity : prérequis 0-token, routage économique, parallélisme sans collision et vagues normales `W0`–`W5` (après clôture P0) |
| `JAUGES_FINES_PRODUCTION.md` | Spécification des 8 axes (`G1`–`G8`) + 5 agrégats LOT + tables par groupe/palier/vague + tableau des **248 LOTs** |
| `generer_jauges.py` | Script Python `3.11+` (`stdlib` uniquement, lecture seule hors `Antigravity_vialFMH/`) générant JSON, CSV, `CHECKPOINT_ABSENTS.json`, Markdown et synchronisation Dashboard |
| `jauges_248_lots.json` | Export JSON déterministe complet (`248` LOTs + agrégats + détail par cours) |
| `jauges_2728_cours.csv` | Export CSV granulaire des **2 728 cours** (`LOT_001..248 × PA, DX.1..DX.10`, `39` colonnes) |
| `DASHBOARD_PRODUCTION_ANTIGRAVITY.html` | Tableau de bord HTML5 autonome (`#fff` pur, 0 bleu `150°–305°`, 0 crème) : bandeau/file P0 Absents, schéma SVG, **matrice graphique dynamique par chapitres (`248 × 11`, vert = validé)** et explorateur de jauges |

---

## 3. Reproduction & vérification déterministe

```bash
# 1. Régénérer jauges_248_lots.json, jauges_2728_cours.csv, CHECKPOINT_ABSENTS.json, MD et sync HTML (0 token)
python3 Antigravity_vialFMH/generer_jauges.py

# 2. Vérifier la parité stricte JSON / CSV / CHECKPOINT / Markdown / Dashboard HTML (lecture seule)
python3 Antigravity_vialFMH/generer_jauges.py --check

# 3. Gardes locales du dépôt
python3 tools/check_hash.py
python3 tools/budget.py
python3 tests/test_gardes.py
```

---

## 4. Conformité GitHub & Gardes CI

- Aucun sous-dossier `LOT_\d{3}` n'est créé dans `Antigravity_vialFMH/`.
- Aucun fichier protégé (`orig/`, `app_v2.html`, `qa/visuel/reference*`, `data/`, `assets/`, `Claude/`, `tools/`) n'est modifié.
- La PR sur `main` respecte `.github/workflows/checkpoint.yml` (`## Automates actifs`) et passe les contrôles `garde`, `html`, `tests`, `visuel`, `schemas`, `liens` avec fusion par commit de fusion (`--merge`).
