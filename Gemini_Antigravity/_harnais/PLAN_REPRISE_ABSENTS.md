# Plan d'urgence prioritaire P0 — Production L1 des LOTs & Cours ABSENTS / Stubs

**Statut d'exécution** : **PRIORITÉ ABSOLUE ACTIVE** (réorientation utilisateur du `17.11.2026`, pause du flux secondaire `W0–W5` jusqu'à complétion didactique de tous les cours manquants ou ébauches `< 20 Ko`).  
**Source machine déterministe** : `Antigravity_vialFMH/CHECKPOINT_ABSENTS.json` (régénéré et vérifié par `python3 Antigravity_vialFMH/generer_jauges.py --check`).  
**Retour au schéma normal** : dès que `resume_cursor.remaining_courses == 0` (`248/248` LOTs et `2 728/2 728` cours dotés de contenu didactique), reprendre le schéma normal `W0 → W5` (`Antigravity_vialFMH/PLAN_REPRISE_ORCHESTRATION.md`).

---

## 1. Bilan exact des cours sans contenu didactique (`47` LOTs / `370` cours)

| Catégorie | Nb LOTs | Cours `ABSENT` | Cours `EBAUCHE_STUB` (`<20 Ko`) | Total sans didactique | Périmètre exact |
|---|---:|---:|---:|---:|---|
| **File A1 · `T9` Lot 1** | 3 | 33 | 0 | **33** | `LOT_045` (`S2.6`, `#524`), `LOT_080` (`S5.1`, `#735`), `LOT_102` (`S7.8`, `#732`/`#592`) |
| **File A2 · `T9` Lot 2** | 7 | 77 | 0 | **77** | `LOT_043, 044, 046, 047, 048, 049, 050` (appariement `#733–#740` + `#525–#539`) |
| **File B · `T8e` Stubs (`<20 Ko`)** | 16 | 0 | 173 | **173** | `051–054, 058–059` (PRs `#575, #584, #593–#598`) + `103, 114, 116, 118, 120, 230, 236, 240, 246, 247` *(nb : `103 PA,DX.1` et `114 PA` >20 Ko)* |
| **File B2 · `T8c` Stubs résiduels** | 2 | 0 | 3 | **3** | `LOT_158` (`F2.10` : `DX.3`), `LOT_160` (`F2.12` : `DX.6, DX.9`) |
| **File C1 · Partiels `T5` / `T7`** | 6 | 14 | 0 | **14** | `Claude/LOT_041, 042, 075–077` (`T5`, **réécriture L1 complète requise**) + `ChatGPT_Codex/LOT_122` (`T7`) |
| **File C2 · Partiels `T8d` (`Grokbot`)** | 13 | 70 | 0 | **70** | `Grokbot/LOT_147, 148, 229, 231, 233–235, 237, 241–244, 248` |
| **TOTAL PHASE P0** | **47** *(45 principaux + 2 résiduels)* | **194** | **176** | **370** | **100 % des cours `ABSENT` + `EBAUCHE_STUB` du dépôt** |

---

## 2. Prérequis gratuits sur cette VM (0 token modèle, `< 2 min`)

Avant de lancer la file A1, appliquer ou charger ces éléments vérifiés :

1. **Déblocage Python 3.11 de la chaîne L1** :
   - `Claude/_outils/forme.py:326` et `Claude/_outils/migrer_l1.py:121` contiennent un antislash dans une expression f-string (`SyntaxError` sous Python `3.11.2`) → extraire `re.sub(...)` dans une variable locale dans le worktree de production.
   - `Claude/_outils/detecteur_lots.py:88` et `harnais/controle_lot.py:24,91` : utiliser `Claude/_outils/controle3.py --script-ok` (gabarit L1 `80 000–150 000` octets hors images, gabarit or validé sur `Claude/LOT_015/LOT_015_Phase_B_V0_DX.9.html` → `VERT`).
2. **Corpus AIPS & Sources suisses/européennes (`PR #512`)** :
   - `/home/user/Medina/` est absent sur cette VM ; télécharger en espace scratch (`<appDataDir>/scratch/`) `AipsDownload_20261008.xml` (`25,2 Mo`) et les `fi_fr/*.txt.gz` (`4 631` notices) depuis la branche `agentA/corpus-ressources-20261109` (`PR #512`, `HTTP/2 200`), en complément de `data/ck/doses_ch.json` et des accès directs `HTTP 200` (`files.refdata.ch`, `swissmedicinfo.ch`, `revmed.ch`, `bag.admin.ch`, `hug.ch`, `escardio.org`).
3. **Piège d'identifiants à éviter** :
   - Dans `imagerie_GROK/harnais/manifest/`, les fichiers `EXP-NNN.json` / `IMG-NNN.json` utilisent une numérotation séquentielle de pathologies (`EXP-045` = *Fibrillation auriculaire*) et **non** les numéros de LOT PROFILES (`LOT_045` = `S2.6` *Toux, expectorations, hémoptysie*).

---

## 3. Inventaire exhaustif et file de production Prompt L1 (`A1 → A2 → B → B2 → C1 → C2`)

### File A1 — `T9` Lot 1 (`3` LOTs / `33` cours `ABSENT`) — Lancement immédiat en 3 worktrees parallèles

| Ordre | LOT | SSP | Titre PROFILES 2023 | PRs ouverts réutilisables (vérifiés) | Action Prompt L1 |
|---:|---|---|---|---|---|
| **1** | `045` | `S2.6` | Toux, expectorations, hémoptysie | **`#524`** (`claude/lot-045`, non-draft, `Lo_9.11.26` `11/11` + `LISTE_DX_CANONIQUE.md` gelée SHA-256 + `paquet.json`) | Extraire `LISTE_DX_CANONIQUE.md` + `paquet.json` + 11 HTML de `#524`, migrer en **L1** (`80–150 Ko`, `1. Définition`, `:target`, `#fff`, `forme.css/js`), `controle3 --script-ok` VERT, `verif_aips`, double audit. |
| **2** | `080` | `S5.1` | Posture anormale et déformations du dos | **`#735`** (`grok/redaction-lot-080`, L1 `PA` `147,3 Ko` + `DX.1` `131,4 Ko`, `controle3 VERT`) | Reprendre `PA + DX.1` de `#735`, geler `LISTE_DX_CANONIQUE.md` (`geler.py`), produire `DX.2–DX.10` en L1 (`1 + 5` parallèles), double audit. |
| **3** | `102` | `S7.8` | Parésie, paralysie | **`#732`** (`grok/redaction-lot-102`, L1 `PA` `84,7 Ko`) + **`#592`** (`grok/lot-102`, pre-L1 `11/11`) | Reprendre `PA` L1 de `#732`, vérifier `DX` dans `#592`, geler `P1`, produire `DX.1–DX.10` en L1, double audit. |

### File A2 — `T9` Lot 2 (`7` LOTs / `77` cours `ABSENT`) — Appariement `#733–#740` + `#525–#539`

| Ordre | LOT | SSP | Titre PROFILES 2023 | PR L1 `PA+DX.1` | PR `Lo_9.11.26` `11/11` + `LISTE_DX` | Ajustement requis |
|---:|---|---|---|---|---|---|
| **4** | `043` | `S2.4` | Gêne thoracique | `#737` | `#527` (open) | Garder `PA+DX.1` L1, migrer `DX.2–10` de `#527` vers L1 (`80–150 Ko`). |
| **5** | `044` | `S2.5` | Douleur thoracique | `#733` | `#525` (open) | **Réduire `PA` de `161,6 Ko` à `≤ 150 Ko`** (`-11,6 Ko`), migrer `DX.2–10` de `#525`. |
| **6** | `046` | `S2.7` | Dyspnée | `#740` | `#532` (draft) | Garder `PA+DX.1` L1, migrer `DX.2–10` de `#532`. |
| **7** | `047` | `S2.8` | Brûlures rétrosternales (pyrosis) | `#734` | `#537` (draft) | Garder `PA+DX.1` L1, migrer `DX.2–10` de `#537`. |
| **8** | `048` | `S2.9` | Dysphagie, régurgitation | `#739` | `#533` (draft) | Garder `PA+DX.1` L1, migrer `DX.2–10` de `#533`. |
| **9** | `049` | `S2.10` | Respiration douloureuse, sibilances, stridor | `#738` | `#535` (draft) | Garder `PA+DX.1` L1, migrer `DX.2–10` de `#535`. |
| **10** | `050` | `S2.11` | Palpitations | `#736` | `#539` (draft) | Garder `PA+DX.1` L1, migrer `DX.2–10` de `#539`. |

### File B & B2 — Remplacement des `16` LOTs Stubs `T8e` (`173` stubs) + `2` LOTs `T8c` résiduels (`3` stubs)

1. **Sous-vague B-PR (`6` LOTs `T8e` avec PRs `Lo_9.11.26` déjà rédigées — `66` stubs)** :
   - **11.** `LOT_051` (`S2.12`) : `#584` (`162 Ko`) + `#593` (`118,5 Ko`) → convertir/ajuster en L1.
   - **12.** `LOT_052` (`S3.1`) : `#575` + `#594` (`103,5 Ko`) → convertir/ajuster en L1.
   - **13.** `LOT_053` (`S3.2`) : `#595` → convertir/ajuster en L1.
   - **14.** `LOT_054` (`S3.3`) : `#596` → convertir/ajuster en L1.
   - **15.** `LOT_058` (`S3.7`) : `#597` → convertir/ajuster en L1.
   - **16.** `LOT_059` (`S3.8`) : `#598` → convertir/ajuster en L1.
2. **Sous-vague B-Neuf (`10` LOTs `T8e` sans PR ouverte — `107` stubs + `3` modules `<34 Ko` sur `103/114`)** :
   - **17.** `LOT_103` (`S7.9`, `9` stubs `DX.2–10`, `PA`/`DX.1` pré-L1 à aligner)
   - **18.** `LOT_114` (`S8.10`, `10` stubs `DX.1–10`, `PA` pré-L1 à aligner)
   - **19–26.** `LOT_116` (`S8.12`), `LOT_118` (`S9.2`), `LOT_120` (`S9.4`), `LOT_230` (`O7.8`), `LOT_236` (`O7.14`), `LOT_240` (`O7.18`), `LOT_246` (`O7.24`), `LOT_247` (`O7.25`) — `11/11` stubs chacun.
3. **Sous-vague B2 (`2` LOTs `T8c` à stubs résiduels — `3` stubs)** :
   - **27.** `LOT_158` (`F2.10` : `DX.3`), **28.** `LOT_160` (`F2.12` : `DX.6, DX.9`).

### File C1 & C2 — `19` LOTs Partiels (`84` cours `ABSENT`)

- **File C1 (`5` LOTs `T5` Claude = `12` `ABSENT` + `1` LOT `T7` Codex = `2` `ABSENT`)** :
  - **29.** `LOT_041` (`S2.2`, `ABSENT`: `DX.5`, unique `7/10`) · **30.** `LOT_042` (`S2.3`, `ABSENT`: `DX.3, DX.4`, unique `5/9`, PR `#432`) · **31.** `LOT_075` (`S4.14`, `ABSENT`: `DX.3, DX.4, DX.5`, unique `5/8`, PRs `#430–#431`) · **32.** `LOT_076` (`S4.15`, `ABSENT`: `DX.3, DX.4`, unique `4/9`, PR `#433`) · **33.** `LOT_077` (`S4.16`, `ABSENT`: `DX.1, DX.2, DX.3, DX.4`, unique `3/7`).
  - **Constat critique vérifié** : les `5` LOTs `T5` n'ont ni `LISTE_DX_CANONIQUE.md` ni `_travail/` et contiennent des fichiers Appel B groupés et dupliqués (`160–196 Ko` pré-L1). **Il faut obligatoirement geler `P1` et réécrire/éclater les 11 HTML en L1**, pas seulement combler les 12 emplacements manquants.
  - **34.** `LOT_122` (`S9.6`, `ChatGPT_Codex`, `T7`, `ABSENT`: `DX.8, DX.10`) : geler `P1`, migrer les 9 HTML pré-L1 et rédiger `DX.8, DX.10` en L1.
- **File C2 (`13` LOTs `T8d` `Grokbot` = `70` `ABSENT`)** :
  - **35.** `LOT_147` (`F1.18`: `DX.1–4`) · **36.** `LOT_148` (`F1.19`: `DX.5–10`) · **37.** `LOT_229` (`O7.7`: `DX.3–5, 8–10`) · **38.** `LOT_231` (`O7.9`: `DX.1–5`) · **39.** `LOT_233` (`O7.11`: `DX.1–2, 6–7`) · **40.** `LOT_234` (`O7.12`: `DX.3–7`) · **41.** `LOT_235` (`O7.13`: `DX.1–5, 8–10`) · **42.** `LOT_237` (`O7.15`: `PA, DX.1–7`) · **43.** `LOT_241` (`O7.19`: `DX.1–2, 8–10`) · **44.** `LOT_242` (`O7.20`: `DX.1–2, 6–7`) · **45.** `LOT_243` (`O7.21`: `DX.6–7`) · **46.** `LOT_244` (`O7.22`: `DX.6–10`) · **47.** `LOT_248` (`O7.26`: `PA, DX.1–2, 6–10`).

---

## 4. Projection de vagues & Protocole de reprise en cas de limite de quota

### Projection de vagues P0 (avant retour au schéma normal `W0–W5`)

| Phase P0 | Périmètre | LOTs | Cours sans didactique | Cadence recommandée (`CONSIGNES_VIAL.md`) |
|---|---|---:|---:|---|
| **P0-A1** | `LOT_045, 080, 102` | 3 | 33 | 3 worktrees parallèles (`antigravity/lot-045`, `-080`, `-102`), PR `#524/#735/#732` |
| **P0-A2** | `LOT_043, 044, 046–050` | 7 | 77 | 2 vagues de 3–4 LOTs (appariement `#733–#740` + `#525–#539`) |
| **P0-B / B2** | `16 T8e` + `158, 160` | 18 | 176 | 3 vagues de 6 LOTs (d'abord `#575, #584, #593–#598`, puis neufs + résiduels) |
| **P0-C1** | `5 T5` + `LOT_122` | 6 | 14 | 1 vague de 6 LOTs (réécriture L1 complète `041,042,075–077` + `122`) |
| **P0-C2** | `13 T8d` (`Grokbot`) | 13 | 70 | 2 vagues de 6–7 LOTs |
| **Sortie P0** | **Transition vers schéma normal** | **47** | **370 → 0** | **Basculer sur `PLAN_REPRISE_ORCHESTRATION.md` (`W0 → W5`)** |

### Protocole obligatoire de check-point & continuité sur limite d'utilisation (quota)

1. **Unité atomique de progression** : `1 LOT` dans un worktree dédié (`antigravity/lot-NNN`) avec écriture incrémentale par module (`PA`, puis `DX.1..DX.10`).
2. **Avant d'arrêter ou en cas d'alerte de quota** :
   - Commiter chaque module terminé et validé par `controle3.py --script-ok` + `verif_aips.py` sur la branche du LOT (jamais de travail non sauvegardé hors Git).
   - Relancer `python3 Antigravity_vialFMH/generer_jauges.py` : le script recalcule automatiquement l'état réel sur disque et met à jour `CHECKPOINT_ABSENTS.json` (`resume_cursor.next_lot`, `resume_cursor.next_course`, `remaining_lots`, `remaining_courses`).
3. **À la reprise dans une nouvelle session** :
   - Lire uniquement `Antigravity_vialFMH/CHECKPOINT_ABSENTS.json` (`resume_cursor`) + `git worktree list` + `PLAN_REPRISE_ABSENTS.md` (zéro rescan manuel du dépôt).
   - Reprendre **exactement** au couple `(next_lot, next_course)` sans refaire les modules déjà passés `VERT`.
4. **Condition de clôture de la phase P0** :
   - `python3 Antigravity_vialFMH/generer_jauges.py --check` retourne `courses_absents == 0` et `EBAUCHE_STUB == 0`.
   - À cet instant, reprendre immédiatement le flux normal **`W0 → W5`** dans `Antigravity_vialFMH/PLAN_REPRISE_ORCHESTRATION.md`.
