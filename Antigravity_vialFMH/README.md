# `Antigravity_vialFMH` — Reprise de production, Jauges fines & Schéma d'orchestration

Ce dossier centralise les livrables analytiques, outillés et opérationnels demandés pour organiser la **reprise de la production initiée par Antigravity** (`LOT_033` / `S1.17`, commit `73d8437`) sur l'ensemble des **248 LOTs PROFILES 2023 (`2 728` cours)** selon un principe d'orchestration **puissant, économique (0-token en pré-portes) et conforme aux règles L1**.

---

## 1. Synthèse exécutive (mesurée au commit `73d8437`)

- **Production L1 auditée** : **`33 / 248` LOTs (`13,3 %`, `363` cours)** — `T1` (`1` Antigravity `LOT_033`), `T2a` (`6` Claude `ACCEPTE` `017–022`), `T2b` (`16` Claude `001–016`), `T2c` (`10` Claude `023–032`).
- **Backlog restant** : **`215 / 248` LOTs (`86,7 %`, `2 365` cours)**, dont `194` cours physiquement absents de `main` (`10` LOTs `T9` + `19` partiels) et `176` ébauches `< 20 Ko` (`16` LOTs `T8e`).
- **Score composite moyen global (`G1–G8`)** : **`49,5 / 100`** (`G`: `87,7`, `S`: `54,6`, `F`: `41,3`, `O`: `38,6`).
- **Découvertes clés** :
  1. **Divergence de format d'Antigravity (`LOT_033`)** : `LOT_033_S1.17_complet.html` (`5,97 Mo`) passe les `4` portes cliniques (`97,1 %`, `96,4 %`, `CLEAN`, `APPROVE`), mais diverge sur `G8` (`20,0/100` : fond crème `#f9f5ee`, script inline, absence de `../_polices/forme.css`) et sur le découpage en **11 HTML séparés** attendu par `FedMed_Progression.html` et `Claude/_outils/controle3.py`.
  2. **Dette d'outillage à corriger à 0 token** : `Claude/_outils/forme.py:326` échoue sous Python `3.11.2` (`SyntaxError` backslash f-string) et `Claude/_outils/detecteur_lots.py:88` score encore contre `100–200 Ko` (`script_ok=False`).
  3. **Gisements d'économie immédiats** : `9` des `10` LOTs manquants `T9` ont déjà des PRs brouillons du `15.11.2026` (`#732–#740`), `255` cours sont déjà `PRET_AUDIT` sans rédaction, et `555` manifestes `imagerie_GROK/` sont réutilisables.

---

## 2. Index des fichiers de `Antigravity_vialFMH/`

| Fichier | Rôle |
|---|---|
| `README.md` | Synthèse exécutive, index des livrables, reproduction et conformité CI |
| `SCHEMA_PRODUCTION_ROBUSTE.md` | Relevé des mises à jour (`10–16.11.2026`) et schéma concis (Mermaid + leviers chiffrés) d'une production robuste, fiable et plus rapide |
| `PLAN_REPRISE_ORCHESTRATION.md` | Plan complet de reprise Antigravity : pré-requis 0-token, routage économique, parallélisme sans collision et vagues `W0`–`W5` |
| `JAUGES_FINES_PRODUCTION.md` | Spécification des 8 axes (`G1`–`G8`) + 5 agrégats LOT + tables par groupe/palier/vague + tableau des **248 LOTs** |
| `generer_jauges.py` | Script Python `3.11+` (`stdlib` uniquement, lecture seule hors `Antigravity_vialFMH/`) scannant les 5 conteneurs et découpant le bundle Antigravity |
| `jauges_248_lots.json` | Export JSON déterministe complet (`248` LOTs + agrégats + détail par cours) |
| `jauges_2728_cours.csv` | Export CSV granulaire des **2 728 cours** (`LOT_001..248 × PA, DX.1..DX.10`, `39` colonnes) |
| `DASHBOARD_PRODUCTION_ANTIGRAVITY.html` | Tableau de bord HTML5 autonome (`#fff` pur, contraste `>= 7:1`, 0 bleu `150°–305°`, 0 crème, SVG schéma + explorateur interactif `248` LOTs / `2 728` cours) |

---

## 3. Reproduction & vérification déterministe

```bash
# 1. Régénérer jauges_248_lots.json et jauges_2728_cours.csv depuis le dépôt réel (0 token)
python3 Antigravity_vialFMH/generer_jauges.py

# 2. Vérifier la parité exacte JSON / CSV / Markdown / Dashboard HTML
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
