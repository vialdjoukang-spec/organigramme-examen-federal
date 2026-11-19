# Jauges fines de production — 248 LOTs & 2 728 cours

**Source canonique** : `Antigravity_vialFMH/jauges_248_lots.json`, `Antigravity_vialFMH/jauges_2728_cours.csv` et `Antigravity_vialFMH/CHECKPOINT_ABSENTS.json` (générés par `python3 Antigravity_vialFMH/generer_jauges.py`, réf. `4727a6e`).

## 1. Synthèse globale mesurée sur disque

| Indicateur | Valeur mesurée |
|---|---:|
| LOTs PROFILES 2023 | **248** |
| Cours totaux (`248 × 11`) | **2728** |
| Cours physiquement présents sur `main` | **2622** (96.1 %) |
| Cours absents sur `main` (priorité urgente) | **106** |
| LOTs L1 audités (`T1 + T2a + T2b + T2c`) | **33 / 248** (13.3 %) |
| Score composite moyen global (`G1–G8`) | **53.5 / 100** |
| Maturité d'audit (`0 / 1 / 2 / 3 / 4`) | `0:201` · `1:4` · `2:34` · `3:9` · `4:0` |
| `MANIFESTE.json` présents / SHA-256 exacts | `63 / 248` présents · `60 / 248` SHA-256 exacts |
| Statuts cours (`2 728`) | `AUDITE_CONFORME:80` · `PRET_AUDIT:357` · `L1_MECANIQUE_PARTIEL:1767` · `HERITAGE_PRE_L1:275` · `EBAUCHE_STUB:143` · `ABSENT:106` |

## 2. Spécification des 8 axes par cours (`G1`–`G8`) et des 5 agrégats LOT

| Axe | Poids | Critères mesurés (0-token / Audit) | Seuil PASS |
|---|---:|---|---|
| **G1. Structure & Gabarit L1** | 18 % | `14/14` points (`id="*p1..p14"`), `FIN_FICHIER` (ou `FIN_COURS` en bundle), balises équilibrées, 0 arbre CIM, Pt 1 Définition seule, 0 `title=`, tableaux enveloppés, 0 ancre cassée, 0 fenêtre imbriquée, 0 gabarit `({..})`, `>=1` `.fenetre`, 0 `<script>` hors `forme.js` (y compris hors `<article>` en bundle). | 14 pts + 0 défaut L1 bloquant |
| **G2. Volume hors images** | 14 % | `bytes_no_img` (retrait `<img>`, `<svg>`, `<picture>`, `data:image` conforme à `controle3.py:192-195`). | `80 000 <= bytes_no_img <= 150 000` (cible `115–145 Ko`) |
| **G3. Langue & Non-Redondance** | 12 % | Phrases verbales (`VERBES`/`VERBE_RE`, apostrophe `’` normalisée), longueur `<=32` mots, 0 doublon intra-fichier, **0 phrase partagée inter-fichiers** dans le LOT, `connecteur%`, paragraphes `>40` mots sans connecteur. | 0 doublon intra/inter, `<=3` nominales/longues |
| **G4. Sources & Véracité CH/EU** | 14 % | `<sup class="r">`, entrées biblio `sb-*`/`*-ref-*`/`src-*`/`div.sb` datées (`consulté`/année), ratio URLs conformes `qa/domaines.yml` (CH/EU), 0 formule lacune (`À vérifier`), chiffres non cités. | `sup.r>=10`, `bib>=3`, 0 lacune, `<=5` chiffres non cités |
| **G5. Pharmacologie & AIPS** | 14 % | Doses (`mg`, `µg`, `UI`…) liées à AIPS (`sb-aips-*` / `files.refdata.ch` / `Swissmedic n°`) ou `hors AIPS`, 0 `compendium.ch`, fiches `.mb`, modal `Urgence — conduite chronologique`. | 0 `compendium.ch`, 0 dose non sourcée |
| **G6. Complétude pédagogique (`µ3` + 11.11)** | 10 % | Pt 3 prérequis anatomo-fonctionnel (`LOT_021+` & `020 DX.1`), Pt 6 `>=1` fenêtre par région, Pt 11 `11.A–11.D`, Pt 13 intact sans `.fenetre`, Pt 14 `>=6` Q&R. | `14` pts + `Pt14>=6` + `Pt3` anatomo (`021+`) |
| **G7. Images pédagogiques (`µ6 v2`)** | 8 % | Présence `<img>`/`<svg>`/`<figure>`, licence libre (`CC0`/`CC BY`/`CC BY-SA`/`PD`), 0 `NC/ND`, lecture guidée (`INTERP`). | `>=1` image licence libre, 0 `NC/ND` |
| **G8. Design & Front-End Uniforme** | 10 % | Liens `../_polices/forme.css` & `forme.js`, `#brain-barre14`, `#fm-bandeau`, fond `#fff` pur, **0 hex crème/beige/ivoire** (`#f9f5ee`…), **0 bleu `150°–305°`**. | `forme.css` + `forme.js` + 0 crème + 0 bleu |

**Agrégats LOT (`LOT_001`–`LOT_248`)** : `completion_mecanique` (`N/11` cours validant `G1+G2+G5+G8`), `P1_gel` (`LISTE_DX_CANONIQUE.md` + `LISTE_DX.audit.json == GEL`), `coherence_AB` (`DX.1..10` alignés sur Phase A + 0 doublon inter-fichiers), `couverture_images` (`N/11` cours illustrés), `maturite_audit` (`0` non audité · `1` Audit 1 / V0 · `2` Audit 2 `CORRECTIONS` / `finale:non` · `3` Contre-audit 2 Phase B `ACCEPTE`/`APPROVE` · `4` `ACCEPTE` + `MANIFESTE.json` SHA-256 exact).

## 3. Répartition par groupe PROFILES (`G / S / F / O`)

| Groupe | LOTs | Cours présents / Total | L1 audités (`T1–T2`) | Maturité ≥ 3 | Cours `80–150 Ko` | Cours `forme.css/js` | Cours illustrés | Score moyen |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| **G** | 16 | 176 / 176 | 16 | 2 | 173 | 176 | 89 | **92.6** |
| **S** | 113 | 1207 / 1243 | 17 | 7 | 944 | 297 | 296 | **62.3** |
| **F** | 44 | 474 / 484 | 0 | 0 | 159 | 0 | 128 | **41.6** |
| **O** | 75 | 765 / 825 | 0 | 0 | 147 | 0 | 448 | **38.8** |

## 4. Répartition par palier (`T1`–`T9`) et par vague (`DONE`, `W0`–`W5`)

| Palier | Description | LOTs | Cours (×11) |
|---|---|---:|---:|
| **`T1`** | Antigravity L1 Audité (bundle) | 1 | 11 |
| **`T2a`** | Claude L1 Audité (`ACCEPTE`) | 6 | 66 |
| **`T2b`** | Claude L1 + `audit2` (`001–016`) | 16 | 176 |
| **`T2c`** | Claude L1 + `PLANCHE` (`023–032`) | 10 | 110 |
| **`T3`** | Claude `fenetre` (sans `forme.css`/`cite`) | 19 | 209 |
| **`T4`** | Claude Héritage 11 HTML | 11 | 121 |
| **`T5`** | Claude Partiel (<11 HTML) | 5 | 55 |
| **`T6`** | Codex Pré-L1 Audité V0 | 3 | 33 |
| **`T7`** | Codex Pré-L1 Non Audité / Partiel | 17 | 187 |
| **`T8a`** | Grokbot 11 HTML `80–150 Ko` + `fenetre` | 1 | 11 |
| **`T8b`** | Grokbot 11 HTML `80–150 Ko` (sans `fenetre`) | 39 | 429 |
| **`T8c`** | Grokbot 11 HTML Tailles mixtes | 92 | 1012 |
| **`T8d`** | Grokbot Partiel (<11 HTML) | 13 | 143 |
| **`T8e`** | Grokbot Ébauches / Stubs (`<20 Ko`) | 13 | 143 |
| **`T9`** | `MISSING` sur `main` (0 HTML) | 2 | 22 |

| Vague | Périmètre & Stratégie | LOTs | Cours (×11) |
|---|---|---:|---:|
| **`DONE`** | Clôturé (`017–022` : `MANIFESTE.json` seul) | 6 | 66 |
| **`W0`** | Clôture audits `001–016`/`023–032`, harmonisation `033`, PRs `#732–#740` | 29 | 319 |
| **`W1`** | Renfort rapide `Claude` `T3/T4/T5` (`034–042`, `109`, `111`) | 22 | 242 |
| **`W2`** | Orphelin `T9` (`045`) + `16` stubs `T8e` (`<20 Ko`) | 13 | 143 |
| **`W3`** | Rattrapage `Claude` héritage & partiels (`072–078`, `104–108`, `110`) | 13 | 143 |
| **`W4`** | Reprise ouverte `ChatGPT_Codex` (`T6` + `T7`) | 20 | 220 |
| **`W5`** | Reprise de masse `Grokbot` (`T8a`–`T8d`) | 145 | 1595 |

## 5. Tableau complet des 248 LOTs (mesures directes sur disque)

| LOT | Code | Grp | Palier | Vague | Conteneur | Prés. | Méca `N/11` | `P1` | Cohér. `A↔B` (dup) | Img `N/11` | Mat. (0–4) | `G1` | `G2` | `G3` | `G4` | `G5` | `G6` | `G7` | `G8` | Score | Intitulé SSP |
|---|---|---:|---|---|---|---|---:|:---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `001` | `G1` | G | `T2b` | `W0` | `Claude` | 11/11 | 9/11 | ABSENT | 8/10 (0) | 10/11 | 2 | 100.0 | 93.4 | 99.1 | 93.0 | 90.0 | 91.4 | 88.6 | 99.1 | **94.7** | Transpiration anormale |
| `002` | `G2` | G | `T2b` | `W0` | `Claude` | 11/11 | 11/11 | ABSENT | 10/10 (0) | 11/11 | 2 | 100.0 | 97.8 | 99.1 | 95.1 | 97.7 | 93.2 | 100.0 | 100.0 | **97.9** | Tuméfaction, tumeur, y compris augmentation de volu… |
| `003` | `G3` | G | `T2b` | `W0` | `Claude` | 11/11 | 10/11 | ABSENT | 10/10 (0) | 11/11 | 2 | 100.0 | 94.9 | 100.0 | 90.5 | 98.2 | 82.7 | 100.0 | 99.1 | **95.9** | Soif excessive, consommation excessive de liquides… |
| `004` | `G4` | G | `T2b` | `W0` | `Claude` | 11/11 | 8/11 | ABSENT | 10/10 (2) | 8/11 | 2 | 100.0 | 95.6 | 97.3 | 88.2 | 98.2 | 88.6 | 74.5 | 97.3 | **93.7** | Fatigue, lassitude |
| `005` | `G5` | G | `T2b` | `W0` | `Claude` | 11/11 | 10/11 | ABSENT | 5/10 (0) | 9/11 | 2 | 100.0 | 93.5 | 99.9 | 87.7 | 97.7 | 97.7 | 81.8 | 99.1 | **95.3** | Sensation de maladie |
| `006` | `G6` | G | `T2b` | `W0` | `Claude` | 11/11 | 10/11 | ABSENT | 10/10 (0) | 7/11 | 2 | 100.0 | 92.7 | 99.1 | 90.9 | 97.7 | 100.0 | 63.6 | 99.1 | **94.3** | Fièvre, frissons, hyperthermie |
| `007` | `G7` | G | `T2b` | `W0` | `Claude` | 11/11 | 11/11 | ABSENT | 10/10 (0) | 7/11 | 2 | 100.0 | 94.2 | 100.0 | 87.6 | 98.6 | 93.2 | 63.6 | 100.0 | **93.7** | Bouffées vasomotrices (flush) |
| `008` | `G8` | G | `T2b` | `W0` | `Claude` | 11/11 | 11/11 | ABSENT | 10/10 (0) | 9/11 | 2 | 100.0 | 94.9 | 100.0 | 88.2 | 96.8 | 100.0 | 81.8 | 100.0 | **95.7** | Hypothermie |
| `009` | `G9` | G | `T2b` | `W0` | `Claude` | 11/11 | 10/11 | GEL | 10/10 (0) | 0/11 | 2 | 100.0 | 92.0 | 99.9 | 84.2 | 96.4 | 100.0 | 1.8 | 99.1 | **88.2** | Prurit |
| `010` | `G10` | G | `T2b` | `W0` | `Claude` | 11/11 | 11/11 | GEL | 10/10 (0) | 0/11 | 2 | 100.0 | 94.2 | 99.1 | 93.9 | 89.5 | 88.6 | 1.8 | 100.0 | **87.8** | Douleurs de tous types |
| `011` | `G11` | G | `T2b` | `W0` | `Claude` | 11/11 | 11/11 | GEL | 10/10 (0) | 2/11 | 3 | 100.0 | 92.0 | 100.0 | 97.8 | 90.9 | 100.0 | 20.0 | 100.0 | **90.9** | Troubles du sommeil (insomnies, hypersomnies ou som… |
| `012` | `G12` | G | `T2b` | `W0` | `Claude` | 11/11 | 11/11 | GEL | 10/10 (0) | 11/11 | 2 | 100.0 | 95.6 | 98.2 | 96.3 | 97.7 | 100.0 | 100.0 | 100.0 | **98.3** | Œdème diffus ou localisé |
| `013` | `G13` | G | `T2b` | `W0` | `Claude` | 11/11 | 9/11 | GEL | 10/10 (0) | 1/11 | 3 | 100.0 | 92.7 | 100.0 | 93.0 | 85.5 | 95.5 | 9.1 | 100.0 | **88.2** | Décès non naturel |
| `014` | `G14` | G | `T2b` | `W0` | `Claude` | 11/11 | 11/11 | GEL | 10/10 (0) | 0/11 | 2 | 100.0 | 92.7 | 100.0 | 98.7 | 90.9 | 91.4 | 1.8 | 100.0 | **88.8** | Décès inattendu ou mort subite |
| `015` | `G15` | G | `T2b` | `W0` | `Claude` | 11/11 | 10/11 | GEL | 10/10 (0) | 2/11 | 2 | 100.0 | 90.4 | 98.2 | 89.2 | 100.0 | 95.5 | 20.0 | 99.1 | **90.0** | Prise de poids, obésité |
| `016` | `G16` | G | `T2b` | `W0` | `Claude` | 11/11 | 10/11 | GEL | 10/10 (0) | 1/11 | 2 | 100.0 | 91.2 | 98.2 | 88.2 | 100.0 | 79.5 | 10.9 | 99.1 | **87.6** | Perte de poids, perte d’appétit |
| `017` | `S1.1` | S | `T2a` | `DONE` | `Claude` | 11/11 | 11/11 | GEL | 10/10 (0) | 5/11 | 3 | 100.0 | 94.9 | 100.0 | 95.6 | 100.0 | 100.0 | 47.3 | 100.0 | **94.5** | Diplopie, ptosis, mouvements oculaires anormaux |
| `018` | `S1.2` | S | `T2a` | `DONE` | `Claude` | 11/11 | 11/11 | GEL | 10/10 (0) | 8/11 | 3 | 100.0 | 92.7 | 100.0 | 96.0 | 100.0 | 98.2 | 72.7 | 100.0 | **96.1** | Perte de vision aiguë ou progressive (rapide, lente… |
| `019` | `S1.3` | S | `T2a` | `DONE` | `Claude` | 11/11 | 8/11 | GEL | 10/10 (0) | 0/11 | 3 | 100.0 | 97.1 | 100.0 | 93.1 | 93.2 | 100.0 | 1.8 | 99.1 | **89.7** | Altération de la voix (enrouement, aphonie, dysphon… |
| `020` | `S1.4` | S | `T2a` | `DONE` | `Claude` | 11/11 | 9/11 | GEL | 10/10 (1) | 3/11 | 3 | 100.0 | 97.8 | 99.1 | 89.7 | 100.0 | 98.2 | 29.1 | 98.2 | **92.1** | Asymétrie ou déformation du visage |
| `021` | `S1.5` | S | `T2a` | `DONE` | `Claude` | 11/11 | 10/11 | CORRIGER | 10/10 (0) | 11/11 | 3 | 100.0 | 92.0 | 100.0 | 94.9 | 96.8 | 100.0 | 100.0 | 100.0 | **97.7** | Épistaxis |
| `022` | `S1.6` | S | `T2a` | `DONE` | `Claude` | 11/11 | 11/11 | CORRIGER | 10/10 (0) | 11/11 | 3 | 100.0 | 92.0 | 100.0 | 94.7 | 100.0 | 98.2 | 100.0 | 100.0 | **98.0** | Blépharospasme |
| `023` | `S1.7` | S | `T2c` | `W0` | `Claude` | 11/11 | 9/11 | CORRIGER | 10/10 (0) | 11/11 | 2 | 100.0 | 92.0 | 100.0 | 97.5 | 95.9 | 95.9 | 100.0 | 99.1 | **97.5** | Difficulté à avaler, étouffement |
| `024` | `S1.8` | S | `T2c` | `W0` | `Claude` | 11/11 | 11/11 | CORRIGER | 10/10 (0) | 10/11 | 2 | 100.0 | 92.0 | 100.0 | 95.9 | 100.0 | 97.7 | 90.9 | 100.0 | **97.4** | Écoulement auriculaire |
| `025` | `S1.9` | S | `T2c` | `W0` | `Claude` | 11/11 | 11/11 | CORRIGER | 10/10 (0) | 11/11 | 2 | 100.0 | 92.0 | 95.1 | 96.2 | 97.3 | 97.7 | 100.0 | 100.0 | **97.2** | Sécheresse, douleur, masse buccale ou pharyngée, lé… |
| `026` | `S1.10` | S | `T2c` | `W0` | `Claude` | 11/11 | 9/11 | NON_AUDITE | 10/10 (0) | 11/11 | 2 | 100.0 | 92.7 | 100.0 | 96.3 | 95.9 | 100.0 | 100.0 | 99.1 | **97.8** | Otalgie |
| `027` | `S1.11` | S | `T2c` | `W0` | `Claude` | 11/11 | 11/11 | NON_AUDITE | 10/10 (0) | 11/11 | 2 | 100.0 | 92.7 | 97.7 | 90.8 | 96.4 | 90.9 | 100.0 | 100.0 | **96.0** | Douleurs faciales, mandibulaires ou dentaires, tris… |
| `028` | `S1.12` | S | `T2c` | `W0` | `Claude` | 11/11 | 7/11 | NON_AUDITE | 10/10 (0) | 11/11 | 2 | 100.0 | 92.0 | 100.0 | 99.4 | 82.7 | 100.0 | 97.7 | 100.0 | **96.2** | Troubles de l’audition : hyperacousie, hypoacousie,… |
| `029` | `S1.13` | S | `T2c` | `W0` | `Claude` | 11/11 | 8/11 | NON_AUDITE | 10/10 (0) | 11/11 | 2 | 100.0 | 92.7 | 100.0 | 96.8 | 89.1 | 100.0 | 94.1 | 99.1 | **96.5** | Microcéphalie et macrocéphalie |
| `030` | `S1.14` | S | `T2c` | `W0` | `Claude` | 11/11 | 9/11 | NON_AUDITE | 10/10 (0) | 11/11 | 2 | 100.0 | 92.7 | 100.0 | 96.5 | 93.2 | 100.0 | 100.0 | 99.1 | **97.5** | Écoulement nasal |
| `031` | `S1.15` | S | `T2c` | `W0` | `Claude` | 11/11 | 11/11 | NON_AUDITE | 10/10 (0) | 11/11 | 2 | 100.0 | 92.0 | 100.0 | 99.4 | 94.5 | 85.5 | 100.0 | 100.0 | **96.6** | Obstruction nasale |
| `032` | `S1.16` | S | `T2c` | `W0` | `Claude` | 11/11 | 8/11 | NON_AUDITE | 10/10 (1) | 11/11 | 2 | 100.0 | 92.7 | 99.1 | 98.1 | 95.5 | 95.5 | 97.7 | 97.3 | **97.1** | Raideur et douleur cervicales |
| `033` | `S1.17` | S | `T1` | `W0` | `Antigravity_LOTs_du_16_11_2026` | 11/11 | 0/11 | GEL_BUNDLE | 10/10 (0) | 10/11 | 3 | 91.7 | 100.0 | 64.7 | 80.0 | 62.5 | 92.7 | 90.5 | 20.0 | **76.7** | Yeux douloureux, rouges ou prurigineux ; écoulement… |
| `034` | `S1.18` | S | `T3` | `W1` | `Claude` | 11/11 | 0/11 | ABSENT | 10/10 (62) | 1/11 | 0 | 75.0 | 83.7 | 29.0 | 0.0 | 58.5 | 46.4 | 10.9 | 15.0 | **43.9** | Ronflement |
| `035` | `S1.19` | S | `T3` | `W1` | `Claude` | 11/11 | 0/11 | ABSENT | 10/10 (130) | 0/11 | 0 | 75.0 | 83.6 | 27.8 | 2.3 | 53.8 | 80.0 | 1.8 | 15.0 | **46.0** | Mal de gorge |
| `036` | `S1.20` | S | `T3` | `W1` | `Claude` | 11/11 | 0/11 | ABSENT | 10/10 (148) | 0/11 | 0 | 75.0 | 90.9 | 28.1 | 0.0 | 61.5 | 80.0 | 1.8 | 15.0 | **47.9** | Strabisme |
| `037` | `S1.21` | S | `T3` | `W1` | `Claude` | 11/11 | 0/11 | ABSENT | 10/10 (298) | 0/11 | 0 | 75.0 | 92.7 | 24.2 | 0.0 | 43.4 | 70.9 | 1.8 | 15.0 | **44.2** | Gonflement du visage, des lèvres ou du cou |
| `038` | `S1.22` | S | `T3` | `W1` | `Claude` | 11/11 | 0/11 | ABSENT | 10/10 (251) | 0/11 | 0 | 75.0 | 92.0 | 23.2 | 0.0 | 50.4 | 80.0 | 1.8 | 15.0 | **45.9** | Gonflement de la paupière |
| `039` | `S1.23` | S | `T3` | `W1` | `Claude` | 11/11 | 0/11 | ABSENT | 10/10 (43) | 0/11 | 0 | 75.0 | 92.0 | 24.4 | 0.0 | 51.5 | 80.0 | 1.8 | 15.0 | **46.2** | Troubles visuels, photophobie, éclairs lumineux, co… |
| `040` | `S2.1` | S | `T4` | `W1` | `Claude` | 11/11 | 0/11 | ABSENT | 9/10 (391) | 1/11 | 0 | 69.7 | 72.1 | 8.8 | 2.3 | 68.5 | 15.9 | 10.9 | 15.0 | **37.6** | Apnée, apnée avec éveil |
| `041` | `S2.2` | S | `T5` | `W1` | `Claude` | 10/11 | 0/11 | ABSENT | 9/10 (140) | 0/11 | 0 | 75.7 | 62.2 | 25.1 | 0.3 | 55.6 | 2.3 | 1.8 | 13.6 | **34.9** | Modification du rythme respiratoire |
| `042` | `S2.3` | S | `T5` | `W1` | `Claude` | 9/11 | 0/11 | ABSENT | 8/10 (4710) | 0/11 | 0 | 61.4 | 49.8 | 2.7 | 2.3 | 32.3 | 1.4 | 1.8 | 15.0 | **24.9** | Masse mammaire, écoulement mamelonnaire, modificati… |
| `043` | `S2.4` | S | `T3` | `W1` | `Claude` | 11/11 | 11/11 | CORRIGER | 10/10 (0) | 0/11 | 2 | 100.0 | 98.5 | 100.0 | 92.1 | 90.5 | 85.5 | 1.8 | 100.0 | **88.0** | Gêne thoracique |
| `044` | `S2.5` | S | `T3` | `W1` | `Claude` | 11/11 | 11/11 | CORRIGER | 10/10 (0) | 0/11 | 2 | 100.0 | 98.5 | 100.0 | 91.2 | 90.9 | 86.4 | 1.8 | 100.0 | **88.1** | Douleur thoracique |
| `045` | `S2.6` | S | `T3` | `W1` | `Claude` | 11/11 | 11/11 | CORRIGER | 10/10 (0) | 0/11 | 2 | 100.0 | 96.4 | 100.0 | 91.2 | 93.6 | 91.8 | 1.8 | 100.0 | **88.7** | Toux, expectorations, hémoptysie |
| `046` | `S2.7` | S | `T3` | `W1` | `Claude` | 11/11 | 11/11 | CORRIGER | 10/10 (0) | 0/11 | 2 | 100.0 | 98.5 | 100.0 | 90.3 | 90.9 | 84.5 | 1.8 | 100.0 | **87.7** | Dyspnée |
| `047` | `S2.8` | S | `T3` | `W1` | `Claude` | 11/11 | 11/11 | CORRIGER | 10/10 (0) | 2/11 | 2 | 100.0 | 98.5 | 100.0 | 94.3 | 91.8 | 80.9 | 18.2 | 100.0 | **89.4** | Brûlures rétrosternales (pyrosis) |
| `048` | `S2.9` | S | `T3` | `W1` | `Claude` | 11/11 | 10/11 | CORRIGER | 10/10 (0) | 0/11 | 2 | 100.0 | 97.8 | 100.0 | 93.6 | 88.6 | 80.9 | 1.8 | 100.0 | **87.4** | Passage difficile ou douloureux des aliments, dysph… |
| `049` | `S2.10` | S | `T3` | `W1` | `Claude` | 11/11 | 11/11 | CORRIGER | 10/10 (0) | 0/11 | 2 | 100.0 | 98.5 | 100.0 | 92.1 | 90.9 | 88.2 | 1.8 | 100.0 | **88.4** | Respiration douloureuse, sibilances, stridor |
| `050` | `S2.11` | S | `T3` | `W1` | `Claude` | 11/11 | 11/11 | CORRIGER | 10/10 (0) | 1/11 | 2 | 100.0 | 96.4 | 100.0 | 92.9 | 90.9 | 86.8 | 9.1 | 100.0 | **88.6** | Palpitations |
| `051` | `S2.12` | S | `T3` | `W1` | `Claude` | 11/11 | 11/11 | CORRIGER | 10/10 (0) | 0/11 | 2 | 100.0 | 99.3 | 100.0 | 92.7 | 90.9 | 83.2 | 1.8 | 100.0 | **88.1** | Douleur de la paroi thoracique |
| `052` | `S3.1` | S | `T3` | `W1` | `Claude` | 11/11 | 11/11 | CORRIGER | 10/10 (0) | 0/11 | 2 | 100.0 | 99.3 | 100.0 | 94.3 | 90.5 | 83.2 | 1.8 | 100.0 | **88.2** | Douleur abdominale |
| `053` | `S3.2` | S | `T8e` | `W2` | `Grokbot` | 11/11 | 0/11 | NON_AUDITE | 0/10 (0) | 0/11 | 0 | 83.3 | 5.0 | 20.0 | 90.0 | 15.0 | 35.0 | 1.8 | 15.0 | **37.9** | Distension abdominale |
| `054` | `S3.3` | S | `T3` | `W1` | `Claude` | 11/11 | 11/11 | CORRIGER | 10/10 (0) | 0/11 | 1 | 100.0 | 99.3 | 100.0 | 92.1 | 90.9 | 79.5 | 1.8 | 100.0 | **87.6** | Masse abdominale |
| `055` | `S3.4` | S | `T8b` | `W5` | `Grokbot` | 11/11 | 0/11 | NON_AUDITE | 3/10 (0) | 0/11 | 0 | 83.3 | 100.0 | 90.0 | 100.0 | 62.7 | 35.0 | 1.8 | 15.0 | **67.7** | Modification du transit intestinal, incontinence an… |
| `056` | `S3.5` | S | `T8b` | `W5` | `Grokbot` | 11/11 | 0/11 | NON_AUDITE | 2/10 (0) | 0/11 | 0 | 83.3 | 99.3 | 90.0 | 100.0 | 62.7 | 35.0 | 1.8 | 15.0 | **67.6** | Prurit anal, douleur anale, protrusion anale |
| `057` | `S3.6` | S | `T8b` | `W5` | `Grokbot` | 11/11 | 0/11 | NON_AUDITE | 2/10 (0) | 0/11 | 0 | 83.3 | 92.0 | 90.0 | 90.0 | 62.7 | 35.0 | 1.8 | 15.0 | **65.2** | Hématémèse |
| `058` | `S3.7` | S | `T8e` | `W2` | `Grokbot` | 11/11 | 0/11 | NON_AUDITE | 0/10 (0) | 0/11 | 0 | 83.3 | 5.0 | 20.0 | 90.0 | 15.0 | 35.0 | 1.8 | 15.0 | **37.9** | Constipation |
| `059` | `S3.8` | S | `T8e` | `W2` | `Grokbot` | 11/11 | 0/11 | NON_AUDITE | 0/10 (0) | 0/11 | 0 | 83.3 | 5.0 | 20.0 | 90.0 | 15.0 | 35.0 | 1.8 | 15.0 | **37.9** | Diarrhée |
| `060` | `S3.9` | S | `T8b` | `W5` | `Grokbot` | 11/11 | 0/11 | NON_AUDITE | 2/10 (0) | 0/11 | 0 | 83.3 | 92.0 | 100.0 | 90.0 | 62.7 | 35.0 | 1.8 | 15.0 | **66.4** | Rectorragie, méléna ; sang frais, mucus ou pus dans… |
| `061` | `S3.10` | S | `T8b` | `W5` | `Grokbot` | 11/11 | 0/11 | NON_AUDITE | 2/10 (0) | 0/11 | 0 | 83.3 | 93.5 | 90.0 | 90.0 | 62.7 | 35.0 | 1.8 | 15.0 | **65.4** | Nausées, vomissements |
| `062` | `S4.1` | S | `T8b` | `W5` | `Grokbot` | 11/11 | 0/11 | NON_AUDITE | 3/10 (0) | 0/11 | 0 | 83.3 | 92.0 | 90.0 | 90.0 | 62.7 | 35.0 | 1.8 | 15.0 | **65.2** | Variations du développement sexuel |
| `063` | `S4.2` | S | `T8b` | `W5` | `Grokbot` | 11/11 | 0/11 | NON_AUDITE | 2/10 (0) | 0/11 | 0 | 83.3 | 93.5 | 90.0 | 90.0 | 62.7 | 35.0 | 1.8 | 15.0 | **65.4** | Anurie, pollakiurie, oligurie, polyurie |
| `064` | `S4.3` | S | `T8b` | `W5` | `Grokbot` | 11/11 | 0/11 | NON_AUDITE | 3/10 (0) | 0/11 | 0 | 83.3 | 92.0 | 90.0 | 90.0 | 62.7 | 35.0 | 1.8 | 15.0 | **65.2** | Dysurie, pyurie, hématurie |
| `065` | `S4.4` | S | `T8b` | `W5` | `Grokbot` | 11/11 | 0/11 | NON_AUDITE | 0/10 (0) | 0/11 | 0 | 83.3 | 92.0 | 100.0 | 90.0 | 62.7 | 35.0 | 1.8 | 15.0 | **66.4** | Questions relatives à la conception, notamment infe… |
| `066` | `S4.5` | S | `T8b` | `W5` | `Grokbot` | 11/11 | 0/11 | NON_AUDITE | 0/10 (0) | 0/11 | 0 | 83.3 | 92.0 | 90.0 | 90.0 | 62.7 | 35.0 | 1.8 | 15.0 | **65.2** | Troubles menstruels, dysménorrhée, symptômes prémen… |
| `067` | `S4.6` | S | `T8b` | `W5` | `Grokbot` | 11/11 | 0/11 | NON_AUDITE | 0/10 (0) | 0/11 | 0 | 83.3 | 92.0 | 90.0 | 90.0 | 62.7 | 35.0 | 1.8 | 15.0 | **65.2** | Masse pelvienne |
| `068` | `S4.7` | S | `T8b` | `W5` | `Grokbot` | 11/11 | 0/11 | NON_AUDITE | 0/10 (0) | 0/11 | 0 | 83.3 | 92.0 | 90.0 | 90.0 | 62.7 | 35.0 | 1.8 | 15.0 | **65.2** | Douleur pelvienne |
| `069` | `S4.8` | S | `T8b` | `W5` | `Grokbot` | 11/11 | 0/11 | NON_AUDITE | 0/10 (0) | 0/11 | 0 | 83.3 | 92.0 | 90.0 | 90.0 | 62.7 | 35.0 | 1.8 | 15.0 | **65.2** | Demande de contraception, contraception d’urgence |
| `070` | `S4.9` | S | `T8b` | `W5` | `Grokbot` | 11/11 | 0/11 | NON_AUDITE | 2/10 (0) | 0/11 | 0 | 83.3 | 100.0 | 90.0 | 90.0 | 62.7 | 35.0 | 1.8 | 15.0 | **66.3** | Douleur, gonflement ou masse du scrotum |
| `071` | `S4.10` | S | `T8b` | `W5` | `Grokbot` | 11/11 | 0/11 | NON_AUDITE | 2/10 (0) | 0/11 | 0 | 83.3 | 92.0 | 90.0 | 90.0 | 62.7 | 35.0 | 1.8 | 15.0 | **65.2** | Plaintes et dysfonctions sexuelles |
| `072` | `S4.11` | S | `T4` | `W3` | `Claude` | 11/11 | 0/11 | ABSENT | 6/10 (144) | 0/11 | 0 | 73.5 | 65.2 | 9.1 | 0.0 | 76.5 | 0.0 | 1.8 | 15.0 | **35.8** | Gonflement ou douleur de l’aine |
| `073` | `S4.12` | S | `T4` | `W3` | `Claude` | 11/11 | 0/11 | ABSENT | 10/10 (424) | 0/11 | 0 | 78.8 | 62.9 | 5.0 | 2.3 | 58.6 | 2.3 | 1.8 | 15.0 | **34.0** | Symptômes liés à la ménopause |
| `074` | `S4.13` | S | `T4` | `W3` | `Claude` | 11/11 | 0/11 | ABSENT | 10/10 (1450) | 0/11 | 0 | 84.8 | 64.9 | 13.6 | 26.8 | 31.8 | 49.1 | 1.8 | 15.0 | **40.7** | Écoulement urétral |
| `075` | `S4.14` | S | `T5` | `W3` | `Claude` | 8/11 | 0/11 | ABSENT | 7/10 (2077) | 0/11 | 0 | 60.6 | 46.0 | 9.1 | 0.0 | 34.6 | 2.7 | 1.8 | 11.8 | **24.9** | Incontinence urinaire et énurésie |
| `076` | `S4.15` | S | `T5` | `W3` | `Claude` | 9/11 | 0/11 | ABSENT | 8/10 (5237) | 0/11 | 0 | 63.6 | 51.8 | 7.3 | 0.0 | 30.0 | 2.7 | 1.8 | 12.3 | **25.4** | Rétention urinaire |
| `077` | `S4.16` | S | `T5` | `W3` | `Claude` | 7/11 | 0/11 | ABSENT | 6/10 (3700) | 0/11 | 0 | 56.8 | 36.1 | 5.3 | 30.0 | 25.0 | 35.5 | 1.8 | 9.5 | **28.3** | Prolapsus utérin, relâchement du plancher pelvien |
| `078` | `S4.17` | S | `T4` | `W3` | `Claude` | 11/11 | 0/11 | ABSENT | 10/10 (1862) | 0/11 | 0 | 78.0 | 70.3 | 4.1 | 0.0 | 41.1 | 2.3 | 1.8 | 19.5 | **32.5** | Saignement vaginal |
| `079` | `S4.18` | S | `T8b` | `W5` | `Grokbot` | 11/11 | 0/11 | NON_AUDITE | 2/10 (0) | 0/11 | 0 | 83.3 | 92.0 | 90.0 | 90.0 | 62.7 | 35.0 | 1.8 | 15.0 | **65.2** | Écoulement vaginal |
| `080` | `S5.1` | S | `T9` | `W0` | `ABSENT` | 0/11 | 0/11 | ABSENT | 0/10 (0) | 0/11 | 0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | **0.0** | Posture anormale et déformations du dos |
| `081` | `S5.2` | S | `T6` | `W4` | `ChatGPT_Codex` | 11/11 | 0/11 | NON_AUDITE | 10/10 (0) | 0/11 | 1 | 92.5 | 63.7 | 87.9 | 90.0 | 88.6 | 95.9 | 1.8 | 15.0 | **72.3** | Douleur dorsale ou lombaire |
| `082` | `S5.3` | S | `T6` | `W4` | `ChatGPT_Codex` | 11/11 | 0/11 | NON_AUDITE | 10/10 (4) | 0/11 | 1 | 91.7 | 67.7 | 76.1 | 91.1 | 79.1 | 95.0 | 1.8 | 15.0 | **70.1** | Déformations du squelette et des articulations |
| `083` | `S5.4` | S | `T6` | `W4` | `ChatGPT_Codex` | 11/11 | 0/11 | NON_AUDITE | 10/10 (4) | 0/11 | 1 | 92.5 | 65.1 | 68.0 | 91.4 | 90.5 | 99.1 | 1.8 | 15.0 | **70.9** | Myalgies |
| `084` | `S5.5` | S | `T8b` | `W5` | `Grokbot` | 11/11 | 0/11 | NON_AUDITE | 2/10 (0) | 0/11 | 0 | 83.3 | 93.5 | 90.0 | 90.0 | 62.7 | 35.0 | 1.8 | 15.0 | **65.4** | Douleur, brûlure, crampe ou engourdissement des ext… |
| `085` | `S5.6` | S | `T8b` | `W5` | `Grokbot` | 11/11 | 0/11 | NON_AUDITE | 2/10 (0) | 0/11 | 0 | 83.3 | 92.0 | 90.0 | 100.0 | 62.7 | 35.0 | 1.8 | 15.0 | **66.6** | Articulations gonflées ou douloureuses, raideur mat… |
| `086` | `S6.1` | S | `T8b` | `W5` | `Grokbot` | 11/11 | 0/11 | NON_AUDITE | 2/10 (0) | 0/11 | 0 | 83.3 | 92.0 | 90.0 | 100.0 | 62.7 | 35.0 | 1.8 | 15.0 | **66.6** | Modifications des muqueuses buccales, génitales ou… |
| `087` | `S6.2` | S | `T8b` | `W5` | `Grokbot` | 11/11 | 0/11 | NON_AUDITE | 2/10 (0) | 0/11 | 0 | 83.3 | 92.0 | 90.0 | 100.0 | 62.7 | 35.0 | 1.8 | 15.0 | **66.6** | Ecchymoses, hématomes, purpura |
| `088` | `S6.3` | S | `T8b` | `W5` | `Grokbot` | 11/11 | 0/11 | NON_AUDITE | 2/10 (0) | 0/11 | 0 | 83.3 | 96.4 | 90.0 | 90.0 | 62.7 | 35.0 | 1.8 | 15.0 | **65.8** | Hyperpigmentation ou hypopigmentation |
| `089` | `S6.4` | S | `T8b` | `W5` | `Grokbot` | 11/11 | 0/11 | NON_AUDITE | 2/10 (0) | 0/11 | 0 | 83.3 | 93.5 | 90.0 | 90.0 | 62.7 | 35.0 | 1.8 | 15.0 | **65.4** | Plaie infectée, retard de cicatrisation, ulcères cu… |
| `090` | `S6.5` | S | `T8b` | `W5` | `Grokbot` | 11/11 | 0/11 | NON_AUDITE | 2/10 (0) | 0/11 | 0 | 83.3 | 95.6 | 90.0 | 90.0 | 62.7 | 35.0 | 1.8 | 15.0 | **65.7** | Ictère |
| `091` | `S6.6` | S | `T8b` | `W5` | `Grokbot` | 11/11 | 0/11 | NON_AUDITE | 2/10 (0) | 0/11 | 0 | 83.3 | 92.7 | 90.0 | 90.0 | 62.7 | 35.0 | 1.8 | 15.0 | **65.3** | Absence ou perte de cheveux et de poils, pilosité e… |
| `092` | `S6.7` | S | `T8b` | `W5` | `Grokbot` | 11/11 | 0/11 | NON_AUDITE | 2/10 (0) | 0/11 | 0 | 83.3 | 92.0 | 90.0 | 90.0 | 62.7 | 35.0 | 1.8 | 15.0 | **65.2** | Macules, papules, pustules, vésicules, ulcères, abc… |
| `093` | `S6.8` | S | `T8b` | `W5` | `Grokbot` | 11/11 | 0/11 | NON_AUDITE | 2/10 (0) | 0/11 | 0 | 83.3 | 92.0 | 90.0 | 100.0 | 62.7 | 35.0 | 1.8 | 15.0 | **66.6** | Plaintes concernant les ongles |
| `094` | `S6.9` | S | `T8b` | `W5` | `Grokbot` | 11/11 | 0/11 | NON_AUDITE | 2/10 (0) | 0/11 | 0 | 83.3 | 97.1 | 90.0 | 100.0 | 62.7 | 35.0 | 1.8 | 15.0 | **67.3** | Rougeur cutanée localisée ou diffuse et/ou rougeur… |
| `095` | `S7.1` | S | `T8b` | `W5` | `Grokbot` | 11/11 | 0/11 | NON_AUDITE | 2/10 (0) | 0/11 | 0 | 83.3 | 92.0 | 90.0 | 90.0 | 62.7 | 35.0 | 1.8 | 15.0 | **65.2** | Troubles de l’équilibre, chutes |
| `096` | `S7.2` | S | `T8b` | `W5` | `Grokbot` | 11/11 | 0/11 | NON_AUDITE | 2/10 (0) | 0/11 | 0 | 83.3 | 92.0 | 90.0 | 90.0 | 62.7 | 35.0 | 1.8 | 15.0 | **65.2** | Troubles de la marche |
| `097` | `S7.3` | S | `T8b` | `W5` | `Grokbot` | 11/11 | 0/11 | NON_AUDITE | 2/10 (0) | 0/11 | 0 | 83.3 | 97.8 | 90.0 | 90.0 | 62.7 | 35.0 | 1.8 | 15.0 | **66.0** | Mouvements involontaires anormaux, tremblements, ti… |
| `098` | `S7.4` | S | `T8b` | `W5` | `Grokbot` | 11/11 | 0/11 | NON_AUDITE | 2/10 (0) | 0/11 | 0 | 83.3 | 92.0 | 90.0 | 90.0 | 62.7 | 35.0 | 1.8 | 15.0 | **65.2** | Troubles de la parole ou du langage |
| `099` | `S7.5` | S | `T8b` | `W5` | `Grokbot` | 11/11 | 0/11 | NON_AUDITE | 2/10 (0) | 0/11 | 0 | 83.3 | 92.0 | 100.0 | 90.0 | 62.7 | 35.0 | 1.8 | 15.0 | **66.4** | Étourdissements, vertiges |
| `100` | `S7.6` | S | `T8b` | `W5` | `Grokbot` | 11/11 | 0/11 | NON_AUDITE | 2/10 (0) | 0/11 | 0 | 83.3 | 92.0 | 90.0 | 90.0 | 62.7 | 35.0 | 1.8 | 15.0 | **65.2** | Céphalées |
| `101` | `S7.7` | S | `T8b` | `W5` | `Grokbot` | 11/11 | 0/11 | NON_AUDITE | 0/10 (0) | 0/11 | 0 | 83.3 | 97.1 | 90.0 | 90.0 | 62.7 | 35.0 | 1.8 | 15.0 | **65.9** | Troubles cognitifs, notamment difficultés de concen… |
| `102` | `S7.8` | S | `T9` | `W0` | `ABSENT` | 0/11 | 0/11 | ABSENT | 0/10 (0) | 0/11 | 0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | **0.0** | Parésie, paralysie |
| `103` | `S7.9` | S | `T8e` | `W2` | `Grokbot` | 11/11 | 0/11 | NON_AUDITE | 0/10 (0) | 0/11 | 0 | 83.3 | 9.2 | 34.5 | 98.2 | 25.9 | 35.0 | 1.8 | 15.0 | **43.0** | Troubles de la sensibilité (hyperesthésie, hypoesth… |
| `104` | `S7.10` | S | `T4` | `W3` | `Claude` | 11/11 | 0/11 | ABSENT | 9/10 (1775) | 0/11 | 0 | 87.1 | 65.5 | 15.0 | 0.0 | 85.5 | 0.0 | 1.8 | 15.0 | **40.3** | Secousses musculaires, fasciculations, convulsions,… |
| `105` | `S8.1` | S | `T4` | `W3` | `Claude` | 11/11 | 0/11 | ABSENT | 10/10 (1697) | 0/11 | 0 | 83.3 | 82.2 | 12.7 | 0.0 | 32.7 | 5.0 | 1.8 | 25.0 | **35.8** | Traumatismes abdominaux |
| `106` | `S8.2` | S | `T4` | `W3` | `Claude` | 11/11 | 0/11 | ABSENT | 10/10 (2048) | 0/11 | 0 | 83.3 | 90.1 | 12.3 | 0.0 | 31.8 | 5.0 | 1.8 | 25.0 | **36.7** | Brûlures, lésions dues au froid |
| `107` | `S8.3` | S | `T4` | `W3` | `Claude` | 11/11 | 0/11 | ABSENT | 10/10 (1815) | 0/11 | 0 | 83.3 | 95.6 | 13.6 | 0.0 | 33.6 | 5.0 | 1.8 | 25.0 | **37.9** | Contusions, lésions contusives des tissus mous |
| `108` | `S8.4` | S | `T4` | `W3` | `Claude` | 11/11 | 0/11 | ABSENT | 10/10 (1771) | 0/11 | 0 | 83.3 | 95.6 | 14.5 | 0.0 | 30.0 | 5.0 | 1.8 | 25.0 | **37.5** | Luxation articulaire |
| `109` | `S8.5` | S | `T3` | `W1` | `Claude` | 11/11 | 0/11 | ABSENT | 10/10 (1510) | 11/11 | 0 | 83.3 | 92.0 | 20.6 | 55.0 | 67.3 | 45.0 | 75.0 | 15.0 | **59.5** | Noyade ou quasi-noyade |
| `110` | `S8.6` | S | `T4` | `W3` | `Claude` | 11/11 | 0/11 | ABSENT | 0/10 (3603) | 0/11 | 0 | 81.8 | 65.0 | 18.2 | 0.0 | 82.7 | 0.9 | 1.8 | 15.0 | **39.3** | Lésion par corps étranger |
| `111` | `S8.7` | S | `T3` | `W1` | `Claude` | 11/11 | 0/11 | ABSENT | 10/10 (1510) | 11/11 | 0 | 83.3 | 92.0 | 20.8 | 55.0 | 67.3 | 45.0 | 75.0 | 15.0 | **59.5** | Lésions et traumatismes crâniens et cérébraux |
| `112` | `S8.8` | S | `T7` | `W4` | `ChatGPT_Codex` | 11/11 | 0/11 | ABSENT | 9/10 (186) | 0/11 | 0 | 70.5 | 64.7 | 24.3 | 0.0 | 74.1 | 3.2 | 1.8 | 15.0 | **37.0** | Traumatismes des extrémités |
| `113` | `S8.9` | S | `T7` | `W4` | `ChatGPT_Codex` | 11/11 | 0/11 | ABSENT | 10/10 (1510) | 11/11 | 0 | 83.3 | 92.0 | 20.8 | 55.0 | 67.3 | 45.0 | 75.0 | 15.0 | **59.5** | Lacération, plaie fermée ou ouverte, perte de sang |
| `114` | `S8.10` | S | `T8e` | `W2` | `Grokbot` | 11/11 | 0/11 | NON_AUDITE | 0/10 (0) | 0/11 | 0 | 83.3 | 6.4 | 27.3 | 98.2 | 21.8 | 35.0 | 1.8 | 15.0 | **41.1** | Traumatismes du rachis |
| `115` | `S8.11` | S | `T7` | `W4` | `ChatGPT_Codex` | 11/11 | 0/11 | ABSENT | 10/10 (1510) | 11/11 | 0 | 83.3 | 92.0 | 20.8 | 55.0 | 67.3 | 45.0 | 75.0 | 15.0 | **59.5** | Traumatismes thoraciques |
| `116` | `S8.12` | S | `T8e` | `W2` | `Grokbot` | 11/11 | 0/11 | NON_AUDITE | 0/10 (0) | 0/11 | 0 | 83.3 | 5.0 | 20.0 | 78.2 | 15.0 | 35.0 | 1.8 | 15.0 | **36.3** | Lésions vasculaires |
| `117` | `S9.1` | S | `T7` | `W4` | `ChatGPT_Codex` | 11/11 | 0/11 | ABSENT | 10/10 (1510) | 11/11 | 0 | 83.3 | 92.0 | 20.8 | 55.0 | 67.3 | 45.0 | 75.0 | 15.0 | **59.5** | Anxiété et panique |
| `118` | `S9.2` | S | `T8e` | `W2` | `Grokbot` | 11/11 | 0/11 | NON_AUDITE | 0/10 (0) | 0/11 | 0 | 83.3 | 5.0 | 20.0 | 93.6 | 15.0 | 35.0 | 1.8 | 15.0 | **38.5** | Déficit de l’attention |
| `119` | `S9.3` | S | `T7` | `W4` | `ChatGPT_Codex` | 11/11 | 0/11 | ABSENT | 10/10 (1510) | 11/11 | 0 | 83.3 | 92.0 | 20.8 | 55.0 | 67.3 | 45.0 | 75.0 | 15.0 | **59.5** | Modification du comportement |
| `120` | `S9.4` | S | `T8e` | `W2` | `Grokbot` | 11/11 | 0/11 | NON_AUDITE | 0/10 (0) | 0/11 | 0 | 83.3 | 5.0 | 20.0 | 96.4 | 15.0 | 35.0 | 1.8 | 15.0 | **38.8** | Modification du comportement alimentaire |
| `121` | `S9.5` | S | `T7` | `W4` | `ChatGPT_Codex` | 11/11 | 0/11 | ABSENT | 0/10 (305) | 11/11 | 0 | 83.3 | 92.7 | 39.1 | 15.0 | 50.5 | 48.6 | 80.5 | 15.0 | **54.7** | Modification de l’humeur |
| `122` | `S9.6` | S | `T7` | `W4` | `ChatGPT_Codex` | 9/11 | 0/11 | ABSENT | 8/10 (0) | 3/11 | 0 | 65.9 | 75.3 | 37.8 | 0.4 | 35.0 | 15.5 | 26.8 | 12.3 | **36.8** | Hyperactivité |
| `123` | `S9.7` | S | `T7` | `W4` | `ChatGPT_Codex` | 11/11 | 0/11 | ABSENT | 0/10 (4) | 7/11 | 0 | 84.8 | 92.7 | 39.4 | 16.2 | 49.5 | 44.5 | 47.7 | 15.0 | **52.0** | Peur irrationnelle, peur de la maladie |
| `124` | `S9.8` | S | `T7` | `W4` | `ChatGPT_Codex` | 11/11 | 0/11 | ABSENT | 0/10 (0) | 5/11 | 0 | 88.6 | 97.1 | 35.2 | 0.0 | 45.5 | 52.7 | 38.6 | 15.0 | **50.0** | Irritabilité, comportement agressif et violent |
| `125` | `S9.9` | S | `T7` | `W4` | `ChatGPT_Codex` | 11/11 | 0/11 | ABSENT | 0/10 (10) | 11/11 | 0 | 83.3 | 92.0 | 45.5 | 0.0 | 49.2 | 35.0 | 88.6 | 15.0 | **52.3** | Altération de l’état mental : confusion, delirium,… |
| `126` | `S9.10` | S | `T7` | `W4` | `ChatGPT_Codex` | 11/11 | 0/11 | ABSENT | 10/10 (36) | 5/11 | 0 | 81.0 | 95.6 | 45.3 | 39.1 | 61.5 | 64.5 | 32.7 | 19.5 | **58.5** | Comportement obsessionnel et/ou compulsif |
| `127` | `S9.11` | S | `T7` | `W4` | `ChatGPT_Codex` | 11/11 | 0/11 | ABSENT | 10/10 (605) | 9/11 | 0 | 83.3 | 92.0 | 35.0 | 25.0 | 52.5 | 63.6 | 68.2 | 15.0 | **56.2** | Réactions à des événements fortement stressants |
| `128` | `S9.12` | S | `T7` | `W4` | `ChatGPT_Codex` | 11/11 | 0/11 | ABSENT | 10/10 (0) | 6/11 | 0 | 83.3 | 94.9 | 47.1 | 5.9 | 56.8 | 65.0 | 40.9 | 15.0 | **54.0** | Automutilation et comportements autoagressifs, y co… |
| `129` | `S9.13` | S | `T7` | `W4` | `ChatGPT_Codex` | 11/11 | 0/11 | ABSENT | 2/10 (5) | 11/11 | 0 | 83.3 | 92.0 | 35.9 | 58.5 | 47.2 | 46.8 | 88.6 | 15.0 | **60.3** | Usage non médical de substances, addictions : tabac… |
| `130` | `F1.1` | F | `T7` | `W4` | `ChatGPT_Codex` | 11/11 | 0/11 | ABSENT | 10/10 (0) | 11/11 | 0 | 84.8 | 95.6 | 35.6 | 37.6 | 46.7 | 68.2 | 90.9 | 15.0 | **60.3** | Pression artérielle anormale |
| `131` | `F1.2` | F | `T7` | `W4` | `ChatGPT_Codex` | 11/11 | 0/11 | ABSENT | 10/10 (11) | 9/11 | 0 | 83.3 | 92.7 | 85.4 | 79.1 | 67.3 | 47.3 | 65.9 | 15.0 | **70.2** | Variations des organes génitaux externes : physiolo… |
| `132` | `F1.3` | F | `T7` | `W4` | `ChatGPT_Codex` | 11/11 | 0/11 | ABSENT | 10/10 (4) | 11/11 | 0 | 83.3 | 98.5 | 36.6 | 29.2 | 41.3 | 77.3 | 67.3 | 19.5 | **58.1** | Anomalies à l’auscultation |
| `133` | `F1.4` | F | `T8a` | `W5` | `Grokbot` | 11/11 | 0/11 | ABSENT | 10/10 (58) | 11/11 | 0 | 81.0 | 92.7 | 13.3 | 0.0 | 59.9 | 43.6 | 100.0 | 15.0 | **51.4** | Anomalies à l’inspection |
| `134` | `F1.5` | F | `T8c` | `W5` | `Grokbot` | 11/11 | 0/11 | ABSENT | 10/10 (188) | 1/11 | 0 | 98.5 | 89.2 | 11.0 | 0.0 | 70.5 | 44.5 | 6.8 | 15.0 | **47.9** | Anomalies à la palpation |
| `135` | `F1.6` | F | `T8c` | `W5` | `Grokbot` | 11/11 | 0/11 | ABSENT | 10/10 (1257) | 1/11 | 0 | 90.9 | 90.2 | 10.0 | 0.9 | 34.4 | 32.3 | 5.9 | 15.0 | **40.3** | Anomalies à la percussion |
| `136` | `F1.7` | F | `T8c` | `W5` | `Grokbot` | 11/11 | 0/11 | ABSENT | 10/10 (2380) | 0/11 | 0 | 90.9 | 84.3 | 10.6 | 0.0 | 13.6 | 35.9 | 1.8 | 15.0 | **36.6** | Bradycardie, tachycardie, pouls irrégulier |
| `137` | `F1.8` | F | `T8c` | `W5` | `Grokbot` | 11/11 | 0/11 | ABSENT | 10/10 (1366) | 0/11 | 0 | 90.9 | 59.4 | 2.3 | 4.6 | 70.9 | 45.0 | 1.8 | 15.0 | **41.7** | Cachexie et malnutrition |
| `138` | `F1.9` | F | `T8c` | `W5` | `Grokbot` | 11/11 | 0/11 | ABSENT | 10/10 (3193) | 6/11 | 0 | 91.7 | 88.6 | 48.2 | 0.0 | 54.7 | 40.0 | 21.8 | 15.0 | **49.6** | Troubles cognitifs |
| `139` | `F1.10` | F | `T8c` | `W5` | `Grokbot` | 11/11 | 0/11 | ABSENT | 10/10 (1723) | 1/11 | 0 | 91.7 | 71.8 | 40.2 | 0.0 | 13.6 | 30.0 | 8.2 | 15.0 | **38.5** | Cyanose |
| `140` | `F1.11` | F | `T8c` | `W5` | `Grokbot` | 11/11 | 0/11 | ABSENT | 10/10 (3229) | 7/11 | 0 | 91.7 | 88.3 | 52.4 | 0.0 | 36.4 | 40.0 | 36.8 | 15.0 | **48.7** | Parole ou élocution anormale |
| `141` | `F1.12` | F | `T8c` | `W5` | `Grokbot` | 11/11 | 0/11 | ABSENT | 10/10 (3206) | 1/11 | 0 | 91.7 | 71.9 | 38.6 | 0.0 | 13.6 | 30.0 | 4.5 | 15.0 | **38.0** | Exophtalmie, myosis ou mydriase |
| `142` | `F1.13` | F | `T8c` | `W5` | `Grokbot` | 11/11 | 0/11 | ABSENT | 10/10 (3155) | 9/11 | 0 | 91.7 | 91.5 | 47.2 | 0.0 | 67.3 | 40.0 | 32.7 | 15.0 | **52.5** | Halitose (fetor oris) |
| `143` | `F1.14` | F | `T8c` | `W5` | `Grokbot` | 11/11 | 0/11 | ABSENT | 10/10 (3194) | 1/11 | 0 | 91.7 | 70.7 | 32.3 | 0.0 | 13.6 | 30.0 | 4.5 | 15.0 | **37.1** | Gangrène |
| `144` | `F1.15` | F | `T8c` | `W5` | `Grokbot` | 11/11 | 0/11 | ABSENT | 10/10 (3072) | 9/11 | 0 | 91.7 | 90.1 | 44.9 | 0.0 | 58.2 | 40.0 | 44.1 | 15.0 | **51.7** | Altération ou perte de conscience, coma |
| `145` | `F1.16` | F | `T8c` | `W5` | `Grokbot` | 11/11 | 0/11 | ABSENT | 10/10 (117) | 11/11 | 0 | 94.7 | 78.6 | 37.8 | 0.0 | 31.8 | 40.0 | 67.3 | 15.0 | **47.9** | Œdème |
| `146` | `F1.17` | F | `T8c` | `W5` | `Grokbot` | 11/11 | 0/11 | ABSENT | 10/10 (2757) | 7/11 | 0 | 91.7 | 89.1 | 40.3 | 0.0 | 38.9 | 40.0 | 39.1 | 15.0 | **47.9** | Pâleur |
| `147` | `F1.18` | F | `T8d` | `W5` | `Grokbot` | 7/11 | 0/11 | ABSENT | 6/10 (2675) | 0/11 | 0 | 48.5 | 39.7 | 1.8 | 2.3 | 23.6 | 0.5 | 1.8 | 10.5 | **19.4** | Patient sans pouls, troubles et arrêt cardiorespira… |
| `148` | `F1.19` | F | `T8d` | `W5` | `Grokbot` | 5/11 | 0/11 | ABSENT | 4/10 (1507) | 0/11 | 0 | 37.9 | 31.0 | 2.3 | 0.0 | 21.8 | 0.0 | 1.8 | 11.4 | **15.8** | Perte de conscience transitoire, syncope |
| `149` | `F2.1` | F | `T8c` | `W5` | `Grokbot` | 11/11 | 0/11 | ABSENT | 10/10 (414) | 0/11 | 0 | 91.7 | 61.2 | 36.7 | 0.0 | 52.4 | 46.8 | 1.8 | 15.0 | **43.1** | Gaz du sang anormaux |
| `150` | `F2.2` | F | `T8c` | `W5` | `Grokbot` | 11/11 | 0/11 | ABSENT | 0/10 (954) | 1/11 | 0 | 90.9 | 62.3 | 17.7 | 0.9 | 72.7 | 35.9 | 4.5 | 15.0 | **43.0** | Enzymes cardiaques anormales |
| `151` | `F2.3` | F | `T8c` | `W5` | `Grokbot` | 11/11 | 0/11 | ABSENT | 2/10 (570) | 0/11 | 0 | 91.7 | 68.2 | 12.2 | 0.0 | 13.6 | 30.0 | 1.8 | 15.0 | **34.1** | Bilan de coagulation anormal |
| `152` | `F2.4` | F | `T8c` | `W5` | `Grokbot` | 11/11 | 0/11 | ABSENT | 0/10 (1014) | 0/11 | 0 | 99.2 | 60.5 | 14.1 | 0.0 | 66.0 | 36.8 | 1.8 | 15.0 | **42.6** | Radiographies abdominales, thoraciques ou squeletti… |
| `153` | `F2.5` | F | `T8c` | `W5` | `Grokbot` | 11/11 | 0/11 | ABSENT | 0/10 (396) | 0/11 | 0 | 91.7 | 69.9 | 40.8 | 9.1 | 59.1 | 40.0 | 1.8 | 15.0 | **46.4** | Numération leucocytaire anormale |
| `154` | `F2.6` | F | `T8c` | `W5` | `Grokbot` | 11/11 | 0/11 | ABSENT | 10/10 (1025) | 0/11 | 0 | 90.9 | 63.6 | 8.2 | 2.3 | 46.9 | 35.0 | 1.8 | 15.0 | **38.3** | Électrocardiogramme anormal |
| `155` | `F2.7` | F | `T8c` | `W5` | `Grokbot` | 11/11 | 0/11 | ABSENT | 0/10 (205) | 0/11 | 0 | 91.7 | 66.4 | 41.6 | 0.0 | 59.3 | 40.0 | 1.8 | 15.0 | **44.7** | Électrolytes anormaux |
| `156` | `F2.8` | F | `T8c` | `W5` | `Grokbot` | 11/11 | 0/11 | ABSENT | 0/10 (1005) | 0/11 | 0 | 90.9 | 59.4 | 5.9 | 0.0 | 56.0 | 35.0 | 1.8 | 15.0 | **38.4** | Analyses des selles anormales, sang occulte, parasi… |
| `157` | `F2.9` | F | `T8c` | `W5` | `Grokbot` | 11/11 | 0/11 | ABSENT | 1/10 (1216) | 0/11 | 0 | 83.3 | 47.5 | 31.7 | 6.8 | 36.4 | 31.8 | 1.8 | 15.0 | **36.3** | Glycémie et marqueurs de l’homéostasie glucidique a… |
| `158` | `F2.10` | F | `T8c` | `W5` | `Grokbot` | 11/11 | 0/11 | ABSENT | 10/10 (610) | 0/11 | 0 | 91.7 | 30.3 | 17.8 | 6.8 | 58.6 | 35.0 | 1.8 | 15.0 | **37.2** | Histologie, cytologie et tests de génétique molécul… |
| `159` | `F2.11` | F | `T8c` | `W5` | `Grokbot` | 11/11 | 0/11 | ABSENT | 10/10 (167) | 0/11 | 0 | 90.2 | 62.8 | 22.7 | 0.0 | 45.5 | 31.8 | 1.8 | 15.0 | **38.9** | Enzymes hépatiques anormales |
| `160` | `F2.12` | F | `T8c` | `W5` | `Grokbot` | 11/11 | 0/11 | ABSENT | 0/10 (121) | 0/11 | 0 | 84.8 | 26.0 | 29.2 | 0.0 | 37.8 | 30.9 | 1.8 | 15.0 | **32.5** | Marqueurs de la fonction rénale anormaux |
| `161` | `F2.13` | F | `T8c` | `W5` | `Grokbot` | 11/11 | 0/11 | ABSENT | 1/10 (1984) | 0/11 | 0 | 90.9 | 69.3 | 28.1 | 0.0 | 36.4 | 30.9 | 1.8 | 15.0 | **39.3** | Lipides sériques anormaux |
| `162` | `F2.14` | F | `T8c` | `W5` | `Grokbot` | 11/11 | 0/11 | ABSENT | 0/10 (539) | 0/11 | 0 | 89.4 | 65.5 | 15.5 | 0.0 | 15.9 | 32.3 | 1.8 | 15.0 | **34.2** | Hormones thyroïdiennes anormales |
| `163` | `F2.15` | F | `T8c` | `W5` | `Grokbot` | 11/11 | 0/11 | ABSENT | 0/10 (2027) | 3/11 | 0 | 88.6 | 63.8 | 2.5 | 0.0 | 36.4 | 30.0 | 20.5 | 15.0 | **36.4** | Sédiment urinaire anormal |
| `164` | `F2.16` | F | `T8c` | `W5` | `Grokbot` | 11/11 | 0/11 | ABSENT | 10/10 (42) | 0/11 | 0 | 90.9 | 70.0 | 13.2 | 0.0 | 22.9 | 30.0 | 1.8 | 15.0 | **35.6** | Anémie |
| `165` | `F2.17` | F | `T8c` | `W5` | `Grokbot` | 11/11 | 0/11 | ABSENT | 10/10 (1851) | 2/11 | 0 | 91.7 | 68.2 | 1.4 | 0.0 | 42.5 | 30.9 | 9.1 | 15.0 | **37.5** | Incompatibilité de groupe sanguin |
| `166` | `F2.18` | F | `T8c` | `W5` | `Grokbot` | 11/11 | 0/11 | ABSENT | 0/10 (360) | 1/11 | 0 | 90.9 | 68.0 | 8.1 | 0.0 | 43.3 | 32.7 | 8.2 | 15.0 | **38.3** | Épanchement abdominal ou pleural détecté à l’échogr… |
| `167` | `F2.19` | F | `T8c` | `W5` | `Grokbot` | 11/11 | 0/11 | ABSENT | 10/10 (342) | 3/11 | 0 | 84.8 | 87.7 | 15.0 | 0.0 | 37.6 | 39.1 | 13.6 | 15.0 | **41.1** | Élévation des biomarqueurs de l’inflammation |
| `168` | `F2.20` | F | `T8c` | `W5` | `Grokbot` | 11/11 | 0/11 | ABSENT | 0/10 (1839) | 3/11 | 0 | 90.9 | 71.3 | 2.3 | 0.0 | 36.4 | 30.0 | 13.6 | 15.0 | **37.3** | Diminution de la densité osseuse |
| `169` | `F2.21` | F | `T8c` | `W5` | `Grokbot` | 11/11 | 0/11 | ABSENT | 0/10 (917) | 2/11 | 0 | 83.3 | 70.9 | 21.1 | 0.0 | 27.3 | 32.3 | 7.3 | 15.0 | **36.6** | Carences nutritionnelles |
| `170` | `F2.22` | F | `T8c` | `W5` | `Grokbot` | 11/11 | 0/11 | ABSENT | 0/10 (2333) | 1/11 | 0 | 91.7 | 75.3 | 7.9 | 0.0 | 63.6 | 30.0 | 4.5 | 15.0 | **41.8** | Polyglobulie |
| `171` | `F2.23` | F | `T8c` | `W5` | `Grokbot` | 11/11 | 0/11 | ABSENT | 10/10 (2105) | 4/11 | 0 | 91.7 | 67.1 | 12.8 | 0.0 | 46.9 | 30.0 | 22.7 | 15.0 | **40.3** | Protéinémie, albuminémie |
| `172` | `F2.24` | F | `T8c` | `W5` | `Grokbot` | 11/11 | 0/11 | ABSENT | 0/10 (1053) | 1/11 | 0 | 90.9 | 62.2 | 4.7 | 0.0 | 50.2 | 30.0 | 3.6 | 15.0 | **37.5** | Protéinurie |
| `173` | `F2.25` | F | `T8c` | `W5` | `Grokbot` | 11/11 | 0/11 | ABSENT | 0/10 (1769) | 11/11 | 0 | 90.2 | 88.1 | 1.4 | 0.0 | 32.0 | 30.0 | 75.0 | 15.0 | **43.7** | Thrombopénie, thrombocytose |
| `174` | `O1.1` | O | `T8c` | `W5` | `Grokbot` | 11/11 | 0/11 | ABSENT | 10/10 (4211) | 8/11 | 0 | 90.9 | 75.4 | 32.3 | 0.0 | 13.6 | 30.0 | 40.9 | 15.0 | **40.5** | Poids de naissance anormal et prématurité |
| `175` | `O1.2` | O | `T8c` | `W5` | `Grokbot` | 11/11 | 0/11 | ABSENT | 10/10 (2649) | 11/11 | 0 | 90.9 | 65.8 | 32.3 | 0.0 | 13.6 | 30.0 | 56.8 | 15.0 | **40.4** | Soins de base lors d’un accouchement normal et dura… |
| `176` | `O1.3` | O | `T8c` | `W5` | `Grokbot` | 11/11 | 0/11 | ABSENT | 0/10 (4576) | 11/11 | 0 | 90.9 | 76.6 | 32.3 | 0.0 | 13.6 | 30.0 | 72.7 | 15.0 | **43.2** | Dépistage préconceptionnel et postconceptionnel des… |
| `177` | `O1.4` | O | `T8c` | `W5` | `Grokbot` | 11/11 | 0/11 | ABSENT | 0/10 (616) | 11/11 | 0 | 91.7 | 66.8 | 32.3 | 0.0 | 50.5 | 30.0 | 59.1 | 15.0 | **46.1** | Problèmes maternels pendant la grossesse : fièvre,… |
| `178` | `O1.5` | O | `T8c` | `W5` | `Grokbot` | 11/11 | 0/11 | ABSENT | 0/10 (1904) | 11/11 | 0 | 90.9 | 74.0 | 32.3 | 0.0 | 78.5 | 30.0 | 75.0 | 15.0 | **52.1** | Problèmes liés à l’accouchement |
| `179` | `O1.6` | O | `T8c` | `W5` | `Grokbot` | 11/11 | 0/11 | ABSENT | 0/10 (3384) | 11/11 | 0 | 91.7 | 67.2 | 40.8 | 0.0 | 68.7 | 30.0 | 75.0 | 15.0 | **50.9** | Problèmes liés à l’allaitement |
| `180` | `O1.7` | O | `T8c` | `W5` | `Grokbot` | 11/11 | 0/11 | ABSENT | 0/10 (209) | 11/11 | 0 | 91.7 | 72.1 | 37.3 | 0.0 | 31.8 | 55.0 | 52.3 | 15.0 | **46.7** | Soins de base autour de la conception et pendant la… |
| `181` | `O1.8` | O | `T8c` | `W5` | `Grokbot` | 11/11 | 0/11 | ABSENT | 10/10 (6725) | 0/11 | 0 | 87.9 | 62.8 | 1.4 | 35.5 | 37.7 | 38.2 | 1.8 | 19.5 | **41.0** | Demande d’interruption de grossesse |
| `182` | `O1.9` | O | `T8c` | `W5` | `Grokbot` | 11/11 | 0/11 | ABSENT | 9/10 (4634) | 0/11 | 0 | 83.3 | 63.9 | 16.8 | 35.5 | 37.3 | 32.7 | 1.8 | 15.0 | **41.1** | Suspicion de grossesse, grossesse non planifiée |
| `183` | `O2.1` | O | `T8c` | `W5` | `Grokbot` | 11/11 | 0/11 | ABSENT | 10/10 (4908) | 0/11 | 0 | 83.3 | 68.8 | 5.5 | 0.0 | 45.5 | 0.0 | 1.8 | 15.0 | **33.3** | Croissance anormale, puberté précoce ou retardée, r… |
| `184` | `O2.2` | O | `T8c` | `W5` | `Grokbot` | 11/11 | 0/11 | ABSENT | 0/10 (645) | 11/11 | 0 | 91.7 | 72.2 | 23.2 | 0.0 | 17.3 | 30.0 | 50.0 | 15.0 | **40.3** | Problèmes comportementaux durant l’enfance et l’ado… |
| `185` | `O2.3` | O | `T8c` | `W5` | `Grokbot` | 11/11 | 0/11 | ABSENT | 10/10 (2343) | 11/11 | 0 | 90.9 | 63.3 | 42.0 | 0.0 | 68.2 | 30.0 | 54.5 | 15.0 | **48.7** | Maltraitance et négligence envers l’enfant |
| `186` | `O2.4` | O | `T8c` | `W5` | `Grokbot` | 11/11 | 0/11 | ABSENT | 0/10 (909) | 11/11 | 0 | 91.7 | 74.8 | 33.4 | 0.0 | 63.6 | 30.0 | 56.8 | 15.0 | **48.9** | Vaccination de l’enfant |
| `187` | `O2.5` | O | `T8c` | `W5` | `Grokbot` | 11/11 | 0/11 | ABSENT | 0/10 (181) | 11/11 | 0 | 91.7 | 63.7 | 42.1 | 0.0 | 45.5 | 30.0 | 50.0 | 15.0 | **45.3** | Retard du développement |
| `188` | `O2.6` | O | `T8c` | `W5` | `Grokbot` | 11/11 | 0/11 | ABSENT | 0/10 (594) | 11/11 | 0 | 91.7 | 76.1 | 33.8 | 0.0 | 13.6 | 30.0 | 75.0 | 15.0 | **43.6** | Problèmes d’alimentation durant la petite enfance,… |
| `189` | `O2.7` | O | `T8c` | `W5` | `Grokbot` | 11/11 | 0/11 | ABSENT | 0/10 (220) | 11/11 | 0 | 91.7 | 61.2 | 43.9 | 0.0 | 50.0 | 30.0 | 52.3 | 15.0 | **46.0** | Problèmes fœtaux pendant la grossesse |
| `190` | `O2.8` | O | `T8c` | `W5` | `Grokbot` | 11/11 | 0/11 | ABSENT | 0/10 (872) | 11/11 | 0 | 91.7 | 73.0 | 32.9 | 0.0 | 13.6 | 30.0 | 52.3 | 15.0 | **41.3** | Décès d’un nourrisson |
| `191` | `O2.9` | O | `T8c` | `W5` | `Grokbot` | 11/11 | 0/11 | ABSENT | 10/10 (156) | 11/11 | 0 | 90.9 | 64.3 | 39.9 | 0.0 | 61.6 | 30.0 | 54.5 | 15.0 | **47.6** | Nourrisson irritable ou qui pleure |
| `192` | `O2.10` | O | `T8c` | `W5` | `Grokbot` | 11/11 | 0/11 | ABSENT | 10/10 (2754) | 11/11 | 0 | 89.4 | 68.9 | 41.2 | 0.0 | 54.5 | 30.0 | 40.0 | 15.0 | **46.0** | Difficultés d’apprentissage et problèmes scolaires… |
| `193` | `O2.11` | O | `T8c` | `W5` | `Grokbot` | 11/11 | 0/11 | ABSENT | 10/10 (495) | 11/11 | 0 | 90.9 | 67.1 | 26.4 | 0.0 | 61.5 | 30.0 | 75.0 | 15.0 | **48.0** | Faible tonus musculaire et hypotonie |
| `194` | `O2.12` | O | `T8c` | `W5` | `Grokbot` | 11/11 | 0/11 | ABSENT | 0/10 (2582) | 11/11 | 0 | 88.6 | 69.2 | 35.9 | 0.0 | 45.5 | 30.9 | 46.8 | 15.0 | **44.6** | Consultations de suivi du nourrisson, de l’enfant e… |
| `195` | `O3.1` | O | `T8c` | `W5` | `Grokbot` | 11/11 | 0/11 | ABSENT | 10/10 (640) | 11/11 | 0 | 91.7 | 68.3 | 20.1 | 0.0 | 78.7 | 30.0 | 50.0 | 15.0 | **48.0** | Maltraitance et négligence envers la personne âgée |
| `196` | `O3.2` | O | `T8c` | `W5` | `Grokbot` | 11/11 | 0/11 | ABSENT | 0/10 (109) | 11/11 | 0 | 90.9 | 65.8 | 42.3 | 0.0 | 40.2 | 30.0 | 40.0 | 15.0 | **44.0** | Déficit fonctionnel cognitif, sensoriel ou moteur |
| `197` | `O3.3` | O | `T8c` | `W5` | `Grokbot` | 11/11 | 0/11 | ABSENT | 0/10 (2528) | 11/11 | 0 | 83.3 | 76.4 | 32.3 | 0.0 | 13.6 | 30.0 | 75.0 | 15.0 | **42.0** | Malnutrition et sarcopénie |
| `198` | `O3.4` | O | `T8c` | `W5` | `Grokbot` | 11/11 | 0/11 | ABSENT | 0/10 (268) | 11/11 | 0 | 90.9 | 66.7 | 43.2 | 0.0 | 34.7 | 30.0 | 40.0 | 15.0 | **43.5** | Patient polymorbide et polymédiqué |
| `199` | `O3.5` | O | `T8c` | `W5` | `Grokbot` | 11/11 | 0/11 | ABSENT | 10/10 (3878) | 11/11 | 0 | 90.2 | 74.0 | 31.6 | 0.0 | 37.1 | 30.0 | 65.0 | 15.0 | **45.3** | Escarres |
| `200` | `O3.6` | O | `T8c` | `W5` | `Grokbot` | 11/11 | 0/11 | ABSENT | 0/10 (181) | 11/11 | 0 | 90.9 | 67.6 | 42.3 | 0.0 | 41.5 | 30.0 | 40.0 | 15.0 | **44.4** | Patient dont la dépendance augmente progressivement |
| `201` | `O3.7` | O | `T8c` | `W5` | `Grokbot` | 11/11 | 0/11 | ABSENT | 10/10 (3654) | 11/11 | 0 | 91.7 | 71.2 | 32.3 | 0.0 | 28.5 | 30.0 | 65.0 | 15.0 | **44.0** | Incontinence urinaire et fécale |
| `202` | `O4.1` | O | `T8c` | `W5` | `Grokbot` | 11/11 | 0/11 | ABSENT | 10/10 (262) | 11/11 | 0 | 91.7 | 65.3 | 37.7 | 0.0 | 39.5 | 30.0 | 58.2 | 15.0 | **44.9** | Consultation avant une activité sportive ou après u… |
| `203` | `O4.2` | O | `T8c` | `W5` | `Grokbot` | 11/11 | 0/11 | ABSENT | 0/10 (4279) | 11/11 | 0 | 91.7 | 68.5 | 32.3 | 6.8 | 15.9 | 30.0 | 65.0 | 15.0 | **42.9** | Plan de vaccination |
| `204` | `O4.3` | O | `T8c` | `W5` | `Grokbot` | 11/11 | 0/11 | ABSENT | 0/10 (234) | 11/11 | 0 | 91.7 | 65.4 | 35.9 | 0.0 | 53.6 | 30.0 | 58.2 | 15.0 | **46.6** | Promotion d’un mode de vie sain |
| `205` | `O4.4` | O | `T8c` | `W5` | `Grokbot` | 11/11 | 0/11 | ABSENT | 0/10 (559) | 11/11 | 0 | 91.7 | 59.6 | 39.5 | 0.0 | 58.2 | 30.0 | 40.0 | 15.0 | **45.4** | Demande et organisation de bilans de santé, d’exame… |
| `206` | `O4.5` | O | `T8c` | `W5` | `Grokbot` | 11/11 | 0/11 | ABSENT | 0/10 (292) | 11/11 | 0 | 90.9 | 66.5 | 38.6 | 0.0 | 25.3 | 30.0 | 40.0 | 15.0 | **41.5** | Promotion de la santé sexuelle et de la fertilité |
| `207` | `O4.6` | O | `T8c` | `W5` | `Grokbot` | 11/11 | 0/11 | ABSENT | 10/10 (776) | 11/11 | 0 | 90.9 | 71.8 | 32.7 | 6.8 | 40.9 | 30.0 | 42.3 | 15.0 | **44.9** | Évaluation partagée des risques et bénéfices du dép… |
| `208` | `O4.7` | O | `T8c` | `W5` | `Grokbot` | 11/11 | 0/11 | ABSENT | 10/10 (3505) | 0/11 | 0 | 83.3 | 63.2 | 3.6 | 4.5 | 52.7 | 2.7 | 1.8 | 17.7 | **34.5** | Évaluation partagée des facteurs de risque et de pr… |
| `209` | `O5.1` | O | `T8c` | `W5` | `Grokbot` | 11/11 | 0/11 | ABSENT | 10/10 (3261) | 0/11 | 0 | 83.3 | 62.6 | 16.8 | 31.4 | 76.5 | 1.4 | 1.8 | 15.0 | **42.7** | Fatigue et épuisement des proches aidants |
| `210` | `O5.2` | O | `T8c` | `W5` | `Grokbot` | 11/11 | 0/11 | ABSENT | 10/10 (4281) | 0/11 | 0 | 84.8 | 70.4 | 10.0 | 0.0 | 65.1 | 0.0 | 1.8 | 20.5 | **37.6** | Modification des objectifs thérapeutiques et décisi… |
| `211` | `O5.3` | O | `T8b` | `W5` | `Grokbot` | 11/11 | 0/11 | ABSENT | 10/10 (1482) | 0/11 | 0 | 83.3 | 92.0 | 14.5 | 0.0 | 28.7 | 39.1 | 1.8 | 15.0 | **39.2** | Prise en charge globale du patient en fin de vie |
| `212` | `O5.4` | O | `T8b` | `W5` | `Grokbot` | 11/11 | 0/11 | ABSENT | 8/10 (1635) | 0/11 | 0 | 83.3 | 94.9 | 18.2 | 0.0 | 40.2 | 39.1 | 1.8 | 15.0 | **41.6** | Prise en charge des symptômes réfractaires, notamme… |
| `213` | `O5.5` | O | `T8b` | `W5` | `Grokbot` | 11/11 | 0/11 | ABSENT | 10/10 (1788) | 0/11 | 0 | 75.8 | 94.2 | 19.5 | 0.0 | 67.1 | 5.0 | 1.8 | 15.0 | **40.7** | Besoin de soutien psychosocial ou d’une autre forme… |
| `214` | `O6.1` | O | `T8b` | `W5` | `Grokbot` | 11/11 | 0/11 | ABSENT | 9/10 (1922) | 0/11 | 0 | 78.0 | 92.7 | 18.6 | 2.3 | 37.9 | 5.0 | 1.8 | 15.0 | **37.0** | Absentéisme scolaire ou professionnel |
| `215` | `O6.2` | O | `T8c` | `W5` | `Grokbot` | 11/11 | 0/11 | ABSENT | 10/10 (1983) | 0/11 | 0 | 78.0 | 83.6 | 13.6 | 0.0 | 32.7 | 5.0 | 1.8 | 15.0 | **34.1** | Préoccupations concernant l’apparence et l’image co… |
| `216` | `O6.3` | O | `T8c` | `W5` | `Grokbot` | 11/11 | 0/11 | ABSENT | 10/10 (2182) | 0/11 | 0 | 78.0 | 83.0 | 19.5 | 0.0 | 33.2 | 5.0 | 1.8 | 15.0 | **34.8** | Violence domestique, abus sexuels, viol |
| `217` | `O6.4` | O | `T8c` | `W5` | `Grokbot` | 11/11 | 0/11 | ABSENT | 9/10 (2367) | 0/11 | 0 | 78.0 | 90.7 | 20.0 | 0.0 | 37.0 | 5.0 | 1.8 | 15.0 | **36.5** | Harcèlement, intimidation, mobbing |
| `218` | `O6.5` | O | `T8b` | `W5` | `Grokbot` | 11/11 | 0/11 | ABSENT | 10/10 (1768) | 0/11 | 0 | 77.3 | 93.5 | 20.5 | 2.3 | 54.9 | 5.0 | 1.8 | 15.0 | **39.6** | Questions relatives à la diversité des orientations… |
| `219` | `O6.6` | O | `T8c` | `W5` | `Grokbot` | 11/11 | 0/11 | ABSENT | 0/10 (1184) | 11/11 | 0 | 90.9 | 65.7 | 36.8 | 0.0 | 56.0 | 30.0 | 40.0 | 15.0 | **45.5** | Questions liées à la vie familiale : divorce, monop… |
| `220` | `O6.7` | O | `T8c` | `W5` | `Grokbot` | 11/11 | 0/11 | ABSENT | 10/10 (395) | 11/11 | 0 | 90.9 | 67.5 | 33.2 | 0.0 | 54.9 | 30.0 | 46.8 | 15.0 | **45.7** | Perte, décès, deuil, maladie d’un proche |
| `221` | `O6.8` | O | `T8c` | `W5` | `Grokbot` | 11/11 | 0/11 | ABSENT | 0/10 (758) | 11/11 | 0 | 90.9 | 65.6 | 35.0 | 0.0 | 43.8 | 30.0 | 42.3 | 15.0 | **43.8** | Souffrance psychique ou spirituelle |
| `222` | `O6.9` | O | `T8c` | `W5` | `Grokbot` | 11/11 | 0/11 | ABSENT | 0/10 (365) | 11/11 | 0 | 90.9 | 68.0 | 33.4 | 0.0 | 53.8 | 30.0 | 62.7 | 15.0 | **47.0** | Problèmes liés aux conditions de travail, à l’épuis… |
| `223` | `O7.1` | O | `T8c` | `W5` | `Grokbot` | 11/11 | 0/11 | ABSENT | 0/10 (469) | 11/11 | 0 | 90.9 | 65.7 | 33.2 | 0.0 | 37.3 | 30.0 | 42.3 | 15.0 | **42.7** | Consultation avant ou après un voyage à l’étranger,… |
| `224` | `O7.2` | O | `T8c` | `W5` | `Grokbot` | 11/11 | 0/11 | ABSENT | 0/10 (219) | 11/11 | 0 | 90.9 | 67.4 | 36.8 | 0.0 | 62.7 | 30.0 | 62.7 | 15.0 | **48.5** | Détermination de l’incapacité de travail ou de fréq… |
| `225` | `O7.3` | O | `T8c` | `W5` | `Grokbot` | 11/11 | 0/11 | ABSENT | 0/10 (1064) | 11/11 | 0 | 91.7 | 69.0 | 33.6 | 0.0 | 41.6 | 30.0 | 40.0 | 15.0 | **43.7** | Conseil diététique pour une alimentation saine et d… |
| `226` | `O7.4` | O | `T8c` | `W5` | `Grokbot` | 11/11 | 0/11 | ABSENT | 10/10 (281) | 11/11 | 0 | 87.1 | 64.5 | 32.3 | 0.0 | 55.8 | 30.0 | 40.0 | 15.0 | **44.1** | Aspects environnementaux et psychosociaux des malad… |
| `227` | `O7.5` | O | `T8c` | `W5` | `Grokbot` | 11/11 | 0/11 | ABSENT | 10/10 (324) | 0/11 | 0 | 83.3 | 71.8 | 17.3 | 0.0 | 57.3 | 1.4 | 1.8 | 15.0 | **36.9** | Erreurs ou fautes d’un collègue ou d’un autre profe… |
| `228` | `O7.6` | O | `T8c` | `W5` | `Grokbot` | 11/11 | 0/11 | ABSENT | 10/10 (822) | 0/11 | 0 | 83.3 | 83.6 | 12.3 | 0.0 | 33.6 | 2.7 | 1.8 | 15.0 | **34.8** | Patient immunodéprimé |
| `229` | `O7.7` | O | `T8d` | `W5` | `Grokbot` | 5/11 | 0/11 | ABSENT | 4/10 (379) | 0/11 | 0 | 37.9 | 34.4 | 6.8 | 0.0 | 17.3 | 1.4 | 1.8 | 6.8 | **15.8** | Questions relatives à la tolérance alimentaire |
| `230` | `O7.8` | O | `T8e` | `W2` | `Grokbot` | 11/11 | 0/11 | NON_AUDITE | 0/10 (0) | 0/11 | 0 | 83.3 | 5.0 | 20.0 | 100.0 | 15.0 | 35.0 | 1.8 | 15.0 | **39.3** | Symptômes médicalement inexpliqués |
| `231` | `O7.9` | O | `T8d` | `W5` | `Grokbot` | 6/11 | 0/11 | ABSENT | 5/10 (445) | 0/11 | 0 | 45.4 | 39.1 | 7.4 | 0.0 | 20.5 | 0.5 | 1.8 | 10.0 | **18.6** | Infection nosocomiale |
| `232` | `O7.10` | O | `T8c` | `W5` | `Grokbot` | 11/11 | 0/11 | ABSENT | 0/10 (2079) | 11/11 | 0 | 83.3 | 61.0 | 31.0 | 0.0 | 62.7 | 30.0 | 50.0 | 15.0 | **44.5** | Demande de consentement éclairé pour une interventi… |
| `233` | `O7.11` | O | `T8d` | `W5` | `Grokbot` | 7/11 | 0/11 | ABSENT | 5/10 (1435) | 0/11 | 0 | 53.0 | 36.5 | 4.1 | 0.0 | 20.9 | 1.4 | 1.8 | 9.5 | **19.3** | Patient refusant un traitement |
| `234` | `O7.12` | O | `T8d` | `W5` | `Grokbot` | 6/11 | 0/11 | ABSENT | 5/10 (491) | 0/11 | 0 | 45.4 | 28.6 | 11.4 | 0.0 | 20.5 | 0.0 | 1.8 | 8.2 | **17.4** | Patient présentant une infection sexuellement trans… |
| `235` | `O7.13` | O | `T8d` | `W5` | `Grokbot` | 3/11 | 0/11 | ABSENT | 2/10 (86) | 0/11 | 0 | 22.7 | 23.8 | 5.6 | 0.0 | 10.9 | 0.0 | 1.8 | 4.1 | **10.2** | Patient d’un autre milieu culturel, migration |
| `236` | `O7.14` | O | `T8e` | `W2` | `Grokbot` | 11/11 | 0/11 | NON_AUDITE | 0/10 (0) | 0/11 | 0 | 83.3 | 5.0 | 20.0 | 100.0 | 15.0 | 35.0 | 1.8 | 15.0 | **39.3** | Réadaptation physique et psychosociale en milieu ho… |
| `237` | `O7.15` | O | `T8d` | `W5` | `Grokbot` | 3/11 | 0/11 | ABSENT | 0/10 (326) | 0/11 | 0 | 22.7 | 15.4 | 1.4 | 0.0 | 1.4 | 1.4 | 0.0 | 4.1 | **7.1** | Mauvaise adhésion au traitement |
| `238` | `O7.16` | O | `T8c` | `W5` | `Grokbot` | 11/11 | 0/11 | ABSENT | 10/10 (1199) | 0/11 | 0 | 83.3 | 77.3 | 9.7 | 10.0 | 36.4 | 4.1 | 1.8 | 15.0 | **35.5** | Évaluation préinterventionnelle et préopératoire |
| `239` | `O7.17` | O | `T8c` | `W5` | `Grokbot` | 11/11 | 0/11 | ABSENT | 10/10 (1493) | 0/11 | 0 | 83.3 | 89.1 | 22.3 | 0.0 | 69.5 | 5.0 | 1.8 | 25.0 | **43.0** | Demande de certificat, d’attestation ou d’expertise… |
| `240` | `O7.18` | O | `T8e` | `W2` | `Grokbot` | 11/11 | 0/11 | NON_AUDITE | 0/10 (0) | 0/11 | 0 | 83.3 | 5.0 | 20.0 | 100.0 | 15.0 | 35.0 | 1.8 | 15.0 | **39.3** | Demande d’examens et de traitements non justifiés |
| `241` | `O7.19` | O | `T8d` | `W5` | `Grokbot` | 6/11 | 0/11 | ABSENT | 4/10 (276) | 0/11 | 0 | 45.4 | 31.4 | 15.2 | 6.9 | 20.5 | 1.4 | 1.8 | 8.2 | **19.3** | Demande d’information sur la thérapie génique |
| `242` | `O7.20` | O | `T8d` | `W5` | `Grokbot` | 7/11 | 0/11 | ABSENT | 6/10 (1882) | 0/11 | 0 | 53.0 | 28.2 | 4.5 | 0.0 | 23.6 | 3.2 | 1.8 | 9.5 | **18.8** | Demande d’information sur le don d’organes et la tr… |
| `243` | `O7.21` | O | `T8d` | `W5` | `Grokbot` | 9/11 | 0/11 | ABSENT | 5/10 (768) | 0/11 | 0 | 68.2 | 46.5 | 8.7 | 0.0 | 30.0 | 1.4 | 1.8 | 12.3 | **25.5** | Bénéfices et risques des médecines complémentaires… |
| `244` | `O7.22` | O | `T8d` | `W5` | `Grokbot` | 6/11 | 0/11 | ABSENT | 4/10 (860) | 0/11 | 0 | 45.4 | 31.3 | 6.4 | 5.0 | 17.7 | 0.0 | 1.8 | 8.2 | **17.5** | Suspicion d’intolérance ou d’interaction médicament… |
| `245` | `O7.23` | O | `T8c` | `W5` | `Grokbot` | 11/11 | 0/11 | ABSENT | 0/10 (2672) | 11/11 | 0 | 91.7 | 69.4 | 49.5 | 0.0 | 62.7 | 30.0 | 40.0 | 15.0 | **48.6** | Suspicion de maladie rare |
| `246` | `O7.24` | O | `T8e` | `W2` | `Grokbot` | 11/11 | 0/11 | NON_AUDITE | 0/10 (0) | 0/11 | 0 | 83.3 | 5.0 | 20.0 | 100.0 | 15.0 | 35.0 | 1.8 | 15.0 | **39.3** | Patients vulnérables |
| `247` | `O7.25` | O | `T8e` | `W2` | `Grokbot` | 11/11 | 0/11 | NON_AUDITE | 0/10 (0) | 0/11 | 0 | 83.3 | 5.0 | 20.0 | 100.0 | 15.0 | 35.0 | 1.8 | 15.0 | **39.3** | Demande de conseil génétique |
| `248` | `O7.26` | O | `T8d` | `W5` | `Grokbot` | 3/11 | 0/11 | ABSENT | 0/10 (284) | 0/11 | 0 | 22.7 | 18.1 | 7.7 | 0.0 | 10.9 | 0.0 | 0.0 | 4.1 | **9.5** | Intoxication, empoisonnement |
