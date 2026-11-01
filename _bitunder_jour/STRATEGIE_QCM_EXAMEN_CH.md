# Stratégie de production de questions type examen — cours audités (LOT_001–248)

*Rédigé le dimanche 1er novembre 2026, 21 h 45 (heure de Zurich, UTC+1). Sources web consultées le même jour.*

---

## 0. En une minute

- L'examen fédéral (épreuve **CK**, *Clinical Knowledge*) comporte **240 QCM** en **2 × 120 questions**, avec **3 h 15 par partie**. Cela laisse environ **97 s par question**.
- Il utilise **3 formats** : **Type A**, **K‑prime** et **menu long**. Les questions peuvent aussi être posées en **séquences de 2 à 3 questions** sur un même cas. *La majorité des questions repose sur de brèves vignettes cliniques.*
- Le blueprint de l'examen repose sur **PROFILES**. On tire au sort parmi les **265 situations de départ (SSP)**, en croisant trois tâches médicales : **mécanismes de la maladie / évaluation-diagnostic / prise en charge**. Le rôle visé est celui de *Medical Expert*.
- Les LOT suivent déjà la numérotation PROFILES (par exemple LOT_001 = G1, LOT_145 = F1.16). Chaque LOT correspond donc à une SSP de l'examen, ce qui donne un alignement natif.
- **Cadence recommandée** : un noyau de **30 questions par LOT**, puis une extension jusqu'à **60–80 questions par LOT**.
- **Corpus audité trouvé sur le box : N = 29 LOT**. Cela donne environ **870 questions en noyau** et **1 700 à 2 300 questions en extension**, après revue.

---

## 1. Synthèse des formats suisses (avec sources)

### 1.1 Examen fédéral de médecine humaine (MEBEKO/OFSP, compilé par l'IML de Berne)

| Élément | Règle officielle 2026 | Source |
|---|---|---|
| Volume | 240 QCM, soit 2 parties de 120 questions en 3 h 15 chacune (4 et 6 août 2026), sur tablette | [Exigences MEBEKO 2026 (FR)](https://www.bag.admin.ch/dam/fr/sd-web/fL9EvX0YPT2d/20260204_Exigences%20MED%202026_f.pdf) · [Infotext 2026 (DE)](https://www.bag.admin.ch/dam/de/sd-web/KdRYk-5ILb74/20260204_Infotext%20MED_2026_d_final.pdf) |
| Type A | Une seule réponse juste, ou la meilleure, parmi 3 à 5 propositions. Formulation **positive ou négative** (« la plus mauvaise », « la réponse erronée »). Vaut 1 point. | idem |
| K‑prime (K′) | 4 affirmations, chacune à marquer juste ou faux. 4 réponses correctes = 1 point ; 3 correctes = ½ point. | idem |
| Menu long | Réponse cherchée dans une longue liste invisible, via une recherche textuelle. Vaut 1 point. | idem |
| Séquences | 2 à 3 questions sur un même cas. La suite (avec de nouvelles données) n'apparaît qu'après validation de la réponse précédente, qui ne peut plus être modifiée. | idem · [UNIL FBM : examen fédéral](https://www.unil.ch/fbm/fr/home/ressources/espaces/espace-interne-em/examens-evaluations/examen-federal.html) |
| Vignettes | « La majeure partie des questions se base sur de brèves descriptions de cas ». Les valeurs normales sont fournies si nécessaire. Les unités peuvent varier (g/dl ou g/l, mmHg ou kPa). Chaque question est autonome. | Infotext 2026 |
| Blueprint | Basé sur PROFILES. Dimensions principales : SSP (265 situations), Medical Tasks (CK : *Understanding mechanisms of disease*, *Assessment/Diagnosis*, *Management*), General Objectives (rôle de Medical Expert). Dimensions secondaires : aigu, subaigu ou chronique ; contexte (cabinet, hôpital, EMS, autre). | Exigences MEBEKO 2026, § 2.1–2.2 |
| Qualité | Questions rédigées par les facultés, puis passées en **review board national** par consensus (correction, niveau, pertinence, clé de réponse), avec relecture formelle et linguistique. Après l'examen, les items statistiquement défaillants sont éliminés. Le seuil est fixé par Angoff, Hofstee et un ancrage. Pas de points négatifs. | Exigences MEBEKO 2026, § 1 c et § 5.1 |
| Nouveautés numériques | Depuis 2022 : séquences, courtes vidéos, menu long | [IML : examen écrit numérique](https://www.iml.unibe.ch/themen/uebersichten/artikel/schriftliche-eidgenoessische-pruefung-in-humanmedizin-erstmals-digital) · UNIL FBM |
| Entraînement officiel | Auto-évaluation de l'IML. Elle **ne montre pas** la bonne réponse et les questions sont sous copyright, interdites de collecte. | [IML Self‑Assessment](https://www.iml.unibe.ch/angebote/assessment/pruefungsdienstleistungen/self-assessment) |

### 1.2 Facultés

| Faculté | Ce qui est publié | Source |
|---|---|---|
| **Bâle** (UniBas) | Type A positif ou négatif (5 options), K‑prime, menu long (y compris à plusieurs champs : 2 sur 3 justes donnent ½ point), séquences de 2 à 3 questions. Examen de **120 à 150 QCM en 4 à 4,5 h** par semestre. Les questions sont réparties selon la charge d'apprentissage et stockées dans un pool révisé en continu. Seuil adaptatif par ancrage de Rasch. | [UniBas : MC‑Prüfungen auf iPad](https://medizinstudium.unibas.ch/de/studium/pruefungen/multiple-choice-pruefungen-auf-ipad-mc-pruefungen/) |
| **Zurich** (UZH) | En master, examens QCM semestriels. En 4e année, environ **110 à 130 questions en 4 h** par examen (M111MC, M112MC). | [UZH : brochure 4e année](https://www.med.uzh.ch/dam/jcr:62dfa692-2a31-4ad5-bbec-ef9f50009b2e/4_SJ_Infobroschuere_mit_Titelblatt_def.pdf) · [UZH : Prüfungen](https://www.med.uzh.ch/de/studium/Pruefungen.html) |
| **Genève** (UNIGE) | En BA1, environ **70 % de type A et 30 % de K′**, 1 point chacune. Dès la BA2, évaluations sur ordinateur (EAO) combinant A, K′, QROC, vignettes, intervalles et zones d'image (ROI). Le master utilise des EAO avec QCM et vignettes. | [UNIGE : examen BA1](https://www.unige.ch/medecine/enseignement1/bachelor-et-master-en-medecine-humaine/examens-bachelor/bachelor1) · [UNIGE : examens BA2–3](https://www.unige.ch/medecine/enseignement1/bachelorscienessbiomedicales/examens-bachelor/examens-bachelor-2e-et-3e-annees) |
| **Lausanne** (UNIL FBM) | Décrit les nouveaux formats de l'examen fédéral (séquences, vidéos, menu long) et renvoie à l'auto-évaluation de l'IML. | UNIL FBM (ci-dessus) |
| **Fribourg** (UniFR) | Rappelle le format de l'examen fédéral : CK de 240 questions, CS de 12 stations ECOS. | [UniFR : examen fédéral](https://www.unifr.ch/med/fr/studies/msc/med/exafed.html) |
| **Berne** (IML) | Guide de référence suisse pour la rédaction des QCM (R. Krebs) : types A, A‑négatif, B, **R (appariement étendu, jusqu'à 26 options)**, PickN, K′ et E. Contient les règles anti‑indices (*cues*). | [IML : MC‑Anleitung (PDF)](https://www.iml.unibe.ch/attachment/7/download/mc_anleitung.pdf) |
| Référentiel | PROFILES 2023 : rôles CanMEDS, 9 EPA, 265 SSP (G, S, F, O). | [PROFILES 2023 (UNIGE, PDF)](https://www.unige.ch/medecine/application/files/6617/5939/2636/2023_PROFILES_final_Intregre2025.pdf) · [SMIFK‑CIMS](https://smifk-cims.ch/profiles-2023) |

**Non trouvé publiquement** : la répartition A / K′ / menu long au sein des 240 questions de l'examen fédéral. Les documents officiels ne la publient pas. USI Lugano n'a pas été vérifiée en détail ; son master applique les mêmes règles fédérales.

### 1.3 Règles de rédaction retenues (guide IML et pratiques des facultés)

1. **Stem long, réponses courtes.** La vignette suit cet ordre : âge et sexe → lieu de prise en charge → motif → durée → anamnèse → status → examens complémentaires → éventuellement évolution. La question elle-même tient en une phrase.
2. **Test de la couverture** : on doit pouvoir répondre en cachant les options. Pas de « toutes / aucune des réponses ».
3. **Options homogènes** (une seule dimension : soit des diagnostics, soit des examens, soit des traitements), plausibles, de même longueur, accordées grammaticalement.
4. **Aucun indice** : pas de réponse plus longue ou plus nuancée que les autres, pas de convergence (réponse qui partage le plus d'éléments avec les autres), pas de paire de contraires, pas de répétition d'un mot du stem dans la bonne réponse, pas de « jamais » ou « toujours ».
5. **Pas de question piège.** La difficulté vient de la complexité clinique et de la proximité des options, pas de la forme. Pas de double négation. Le Type A négatif reste rare.
6. Abréviations courantes seulement. Valeurs normales fournies. Unités suisses (SI et parfois mmHg).

---

## 2. Typologie retenue (4 types, plus 1 optionnel)

Mix cible pour la banque. Il s'agit d'une hypothèse calée sur la répartition BA1 de l'UNIGE et sur les formats de l'examen fédéral ; aucune répartition officielle n'est publiée.

| Type | Part | Usage principal |
|---|---|---|
| **A‑vignette** (dont ≤ 5 % de A négatif) | ~50 % | Diagnostic le plus probable, examen suivant, traitement de première ligne |
| **Séquence de cas (2–3 × A)** | ~15 % (en questions) | Démarche diagnostique → prise en charge : c'est le format « révélation progressive » |
| **K‑prime** | ~25 % | Physiopathologie, signes d'alarme, contre-indications, pièges |
| **Menu long** | ~10 % | Diagnostic final ou molécule, sans indice visuel |
| *(Option) Type R* | entraînement seulement | Appariement de différentiels au niveau d'un LOT ; absent de l'examen fédéral |

### 2.1 A‑vignette (structure)
```
STEM : « Un homme de 67 ans consulte son médecin de famille pour un œdème du membre inférieur gauche apparu en 3 jours… Status… D-dimères… »
QUESTION : « Quel est l'examen le plus approprié à ce stade ? »
OPTIONS (5, homogènes) : A … E
CLÉ : C
```
Source dans le LOT : sections 4 à 11 d'un DX (démarche → prise en charge).

### 2.2 Séquence de cas (révélation progressive)
`Q1 diagnostic` → validation → nouvelles données (résultat d'un examen) → `Q2 examen ou stratification` → validation → `Q3 traitement`. La réponse est **verrouillée** après chaque étape, comme à l'examen fédéral.
Source dans le LOT : le fil d'un DX (sections 5, 6, 9, 10, 11).

### 2.3 K‑prime
```
STEM : courte mise en situation, ou énoncé « Concernant X, lesquelles des affirmations suivantes sont justes ? »
4 affirmations indépendantes, chacune juste ou fausse (0 à 4 justes)
Barème : 4 justes = 1 point ; 3 justes = ½ point
```
Source dans le LOT : section 3 (physiopathologie), section 13 (points clés), section 14 (pièges), signes d'alarme de la Phase A.

### 2.4 Menu long
Le stem est une vignette ; la réponse est un champ libre avec autocomplétion sur une **liste maîtresse** (diagnostics ou médicaments) partagée par toute la banque.
Source dans le LOT : `LISTE_DX_CANONIQUE.md` et les différentiels de la Phase A. Pour la liste maîtresse, on fusionne les DX canoniques des 248 LOT.

---

## 3. Du LOT à la question : qui produit quoi

Structure constatée dans les fichiers VERT (exemple : `grok/repo/grok-LOTS-html/LOT_145/`) :
- **Phase A** : environ 90 à 150 Ko, sections L'essentiel → 1 Définition … 14 Pièges → Sources ;
- **10 fichiers DX** de 50 à 100 Ko, avec **les mêmes 14 sections**.

| Section du LOT | Tâche médicale (blueprint) | Type de question à tirer |
|---|---|---|
| 3 Physiopathologie | *Understanding mechanisms* | K′ (mécanismes), A « pourquoi ce signe ? » |
| 4–8 Démarche, anamnèse, status, syndromique, diagnostic positif | *Assessment/Diagnosis* | A‑vignette diagnostic, menu long, Q1 de séquence |
| 9–10 Examens, arbre décisionnel | *Assessment/Diagnosis* | A « examen suivant », Q2 de séquence |
| 11–12 Prise en charge, prévention | *Management* | A « première ligne », K′ contre-indications, Q3 de séquence |
| 13–14 Points clés, pièges | transversal | K′ (pièges transformés en affirmations), perle clinique du feedback |
| Phase A (différentiels, signes d'alarme) | Diagnostic différentiel | Menu long, A « diagnostic le plus probable » qui fait discriminer les DX du LOT entre eux |

**Variation obligatoire des contextes** (dimensions secondaires) : alterner aigu, subaigu et chronique, ainsi que cabinet, urgences, hôpital et EMS, et l'âge (enfant, adulte, personne âgée).

### 3.1 Densité réaliste (règle proposée, pas un chiffre publié)

**Formule par LOT :**
`Q_LOT = Q_PhaseA + Σ (Q_DX)` avec `Q_DX = 1 séquence (2–3 questions) + 1–2 K′ + 1–2 A isolées + 0–1 menu long`

| Niveau | Phase A | Par DX (× 10) | Total par LOT |
|---|---|---|---|
| **Noyau** (prioritaire) | 6 | 2–3 → 24 | **≈ 30** |
| **Standard** | 10–12 | 5–6 → 50–60 | **≈ 60–70** |
| **Maximum utile** | 15–18 | 7–8 → 70–80 | **≈ 85–98** |

Au-delà d'environ 8 questions par DX, on produit surtout du **trivia** : chiffres d'épidémiologie, détails de doses. Le blueprint fédéral échantillonne environ **0,9 question par SSP et par session** (240 questions pour 265 SSP). Une banque de 30 à 70 questions par SSP couvre donc largement l'entraînement.

**Taux de rétention après revue** (hypothèse fondée sur l'expérience des review boards ; aucun chiffre suisse publié) : **75 à 85 %**.

### 3.2 Volume pour le corpus

**N audités trouvés sur le box : 29 LOT.**
- **18** avec la méthode *AUDITEUR* dans `grok/EVALUATION_MEDICAL_LANGUE_LOT_001_248.json` : LOT_001–016 (harnais Claude, médical ≈ 96) et LOT_134–135 (*AUDITEUR auto*, médical 93–94) ;
- **11** clos « VERT / porte VERT » dans `grok/ETAT_DES_LIEUX_2026-11-01.html` : LOT_138–146, 232 et 245 (232 est passé d'ORANGE à VERT avec le commit local 166adb0c, *à pousser*).
- Pour information : 35 LOT sont « clos » dans `LOT_Tunder/RESUME_PROGRESSION_FLASH.md`, mais « clos » ne veut pas dire « audité ». Les 174 LOT notés le sont surtout par heuristique (156), ce qui ne vaut pas validation.
- ⚠️ **Incohérence à trancher** : LOT_145 est VERT d'après l'état des lieux, mais obtient un score heuristique médical de 55 dans l'évaluation 001–248 (méthode heuristique et/ou snapshot différent). **Faire valider la liste des 29 par Vial avant production.**

| Corpus | Noyau (30) | Standard (60–70) | Retenues après revue (×0,75–0,85) |
|---|---|---|---|
| **29 LOT audités** | **870** | 1 740 – 2 030 | ≈ 650 – 1 730 |
| 248 LOT (à terme) | 7 440 | 14 880 – 17 360 | ≈ 5 600 – 14 750 |

Repère : **870 questions ≈ 3,6 examens CK blancs complets** (240 questions chacun).

---

## 4. Révélation de la réponse à la pression d'une icône (UX)

### 4.1 Principes
- **Une icône 💡 par question.** Avant d'appuyer, rien n'est visible. Après, un panneau compact s'affiche en **4 blocs fixes**, de 60 à 120 mots au total.
- **Sur mobile, le feedback reste d'abord fermé.** On peut ouvrir le détail de chaque option (accordéon).
- **Séquence** : l'icône de Q1 révèle la réponse ET déverrouille Q2. La réponse choisie à Q1 est figée.
- Fonctionnement **hors ligne et sans framework** : `<details>/<summary>` natif, plus 20 lignes de JS pour le score et le verrouillage.

### 4.2 Gabarit du feedback (ultra structuré)
```
✅ Réponse : C — Échographie de compression veineuse
① Pourquoi vrai   (1–2 lignes : raisonnement clinique, pas de récitation)
② Pourquoi pas…   A : …  ·  B : …  ·  D : …  ·  E : …   (≤ 1 ligne par option)
③ Perle clinique  (1 ligne, à retenir pour la garde)
④ Source CH       (guideline suisse ou section du LOT + lien d'ancrage)
```

### 4.3 Schéma JSON (une question)
```json
{
  "id": "Q-LOT145-DX01-A-003",
  "version": "1.0.0",
  "lot": "LOT_145",
  "ssp": "F1.16",
  "source_lecon": "LOT_145_Phase_B_V0_DX.1.html#s9",
  "dx": "DX.1",
  "type": "A",
  "polarite": "positive",
  "sequence": {"id": "SEQ-LOT145-DX01-1", "etape": 2, "sur": 3, "revelation_avant": "Échographie : thrombus fémoral commun."},
  "blueprint": {"tache": "assessment_diagnosis", "condition": "aigu", "setting": "cabinet"},
  "difficulte_visee": "moyenne",
  "stem": "Un homme de 67 ans…",
  "question": "Quel est l'examen le plus approprié à ce stade ?",
  "options": [
    {"cle": "A", "texte": "…"}, {"cle": "B", "texte": "…"}, {"cle": "C", "texte": "…"},
    {"cle": "D", "texte": "…"}, {"cle": "E", "texte": "…"}
  ],
  "correct": ["C"],
  "kprim_cle": null,
  "menu_long": null,
  "feedback": {
    "pourquoi_vrai": "…",
    "pourquoi_faux_par_option": {"A": "…", "B": "…", "D": "…", "E": "…"},
    "perle_clinique": "…",
    "source_ch": {"libelle": "…", "url": "…", "ancre_lot": "#s9"}
  },
  "qualite": {"statut": "brouillon|revue_auto|revue_humaine|valide|retire",
              "checklist_iml": {"couverture": true, "homogene": true, "sans_cue": true, "sans_trivia": true},
              "relecteur": null, "date_validation": null},
  "historique": [{"version": "1.0.0", "date": "2026-11-01", "note": "création"}]
}
```
- **K′** : `"kprim_cle": [true,false,true,false]`, et `pourquoi_faux_par_option` est indexé de 1 à 4 (chaque affirmation, juste ou fausse, est expliquée).
- **Menu long** : `"menu_long": {"liste": "MASTER_DX_v1", "accepte": ["Thrombose veineuse profonde proximale", "TVP proximale"]}`.

### 4.4 HTML minimal (rendu)
```html
<article class="qcm" data-id="Q-LOT145-DX01-A-003" data-type="A">
  <p class="stem">Un homme de 67 ans…</p>
  <p class="q"><b>Quel est l'examen le plus approprié à ce stade ?</b></p>
  <ol type="A" class="opts"><li>…</li><li>…</li><li>…</li><li>…</li><li>…</li></ol>
  <details class="reveal">
    <summary aria-label="Afficher la réponse">💡</summary>
    <div class="fb">
      <p class="ok">✅ <b>C</b> — …</p>
      <p><b>① Pourquoi</b> …</p>
      <details><summary><b>② Les autres options</b></summary>
        <ul><li><b>A</b> …</li><li><b>B</b> …</li><li><b>D</b> …</li><li><b>E</b> …</li></ul></details>
      <p><b>③ Perle</b> …</p>
      <p class="src"><b>④ Source</b> <a href="LOT_145_Phase_B_V0_DX.1.html#s9">Leçon §9</a> · …</p>
    </div>
  </details>
</article>
```

---

## 5. Organisation concrète

### 5.1 Arborescence (module séparé, qui ne touche **pas** les leçons VERT)
```
grok/repo/QCM-banque/
  README.md                      ← règles, gabarits, checklist IML
  _schema/question.schema.json
  _listes/MASTER_DX_v1.json      ← liste maîtresse du menu long
  _registre/REGISTRE_QCM.csv     ← id, lot, type, statut, version, relecteur
  LOT_145/
    LOT_145_QCM_v1.json          ← toutes les questions du LOT
    LOT_145_QCM_v1.html          ← rendu généré (icône 💡)
    REVUE_LOT_145.md             ← remarques et décisions de revue
  LOT_001/ …
  _examens_blancs/BLANC_01_120Q.html   ← tirage pondéré selon le blueprint
```
- **Nommage** : `Q-<LOT>-<PhaseA|DXnn>-<A|AN|KP|LM|SEQ>-<nnn>`. Version **sémantique** : un changement de clé ou de contenu médical incrémente le chiffre majeur ; une correction de forme incrémente le mineur.
- **Lien LOT → banque** : le champ `source_lecon` pointe vers l'ancre de section. Le HTML de la leçon peut recevoir **plus tard**, dans un commit séparé après VERT comme pour les clichés, un simple bouton « 🧪 S'entraîner (n questions) » vers `LOT_xxx_QCM_v1.html`. Le texte médical n'est jamais réécrit.
- **Vue double** : la leçon garde sa double vue ; le QCM est une **3e vue** autonome, ce qui évite d'alourdir des fichiers de 70 à 150 Ko.

### 5.2 Workflow (porte d'entrée : LOT audité uniquement)
1. **Éligibilité** : le LOT figure dans la liste « audités » validée par Vial (les 29 actuels).
2. **Génération** (agent) : noyau de 30 questions par LOT selon le tableau du § 3. Chaque question est **traçable à une section** ; tout fait non présent dans le LOT ou sans source suisse est interdit.
3. **Revue automatique** : validation du schéma, checklist IML (longueur des options ±20 %, mots du stem repris dans la clé, absolus, convergence, « toutes/aucune »), détection de doublons entre LOT, équilibre des clés (A à E ≈ 20 % chacune).
4. **Revue humaine** (Vial ou un pair) : 1 ou 2 minutes par question, statut `valide` ou `retire`, motif noté dans `REVUE_LOT_xxx.md`. C'est l'équivalent du *review board* fédéral, à petite échelle.
5. **Publication** : génération du HTML et du PDF, mise à jour du registre, commit sur une branche dédiée (`grok/qcm`), sans PR ni fusion sans ordre.
6. **Retour d'usage** : marquer les questions « ratées par tout le monde » ou « triviales », puis les réviser. C'est l'équivalent artisanal de l'analyse d'items de l'IML (difficulté P, discrimination R).

### 5.3 Priorités
1. **Pilote** : 1 LOT VERT riche (LOT_145 ou LOT_138), noyau de 30 questions, rendu 💡, validation du gabarit par Vial.
2. Noyau de 30 questions pour les **28 autres LOT audités**, soit environ 840 questions de plus.
3. Liste maîtresse du menu long et premier **examen blanc de 120 questions** (tirage pondéré : tâches environ 1/3 chacune, aigu/chronique et contextes variés).
4. Extension « standard » (60–70 questions par LOT) seulement pour les LOT les plus rentables à l'examen (SSP fréquentes ou urgentes).
5. Les nouveaux LOT entrent dans la banque **au moment où ils passent VERT**.

### 5.4 Critères anti-piège et anti-trivia (bloquants en revue)
- ❌ Chiffre d'épidémiologie isolé, dose exacte sans enjeu clinique, éponyme rare, classification par cœur.
- ❌ Question ou bonne réponse non vérifiable dans le LOT ou dans une source suisse ou internationale citée.
- ❌ Plus d'une réponse défendable (risque de contestation). La meilleure réponse doit l'emporter **clairement** sur la deuxième.
- ✅ Chaque question correspond à une **décision clinique** au premier jour d'assistanat (logique EPA et SSP de PROFILES).
- ✅ Spécificités suisses quand elles existent (guidelines SGIM/SSMIG, Swissmedic, SSI/Tox Info Suisse, vaccinations OFSP).

---

## 6. Recommandations actionnables pour Vial

1. **Valider la liste des 29 LOT audités** (001–016, 134–135, 138–146, 232, 245) et trancher l'incohérence de LOT_145 (VERT contre 55 en heuristique).
2. **Adopter 4 formats seulement** : A‑vignette, séquence de 2–3 questions, K′ et menu long, avec la même mécanique que l'examen fédéral (pas de points négatifs ; ½ point à 3/4 en K′).
3. **Viser d'abord 30 questions par LOT** (environ 870 au total, soit à peu près 3,6 examens blancs). Monter à 60–70 seulement sur les SSP prioritaires.
4. **Approuver le gabarit 💡 en 4 blocs** (pourquoi vrai / pourquoi pas les autres / perle / source CH), limité à 120 mots et dépliable.
5. **Produire un pilote sur un LOT** (LOT_145 ou LOT_138), puis le relire en 30 à 45 minutes avant de lancer la série.
6. **Créer un module séparé `QCM-banque/`** : on ne modifie pas les leçons VERT, sauf un bouton d'accès ajouté plus tard dans un commit séparé.
7. **Construire la liste maîtresse du menu long** à partir des `LISTE_DX_CANONIQUE.md` de tous les LOT.
8. **Garder 10 % de questions « fraîches »** : ne pas les montrer dans le module LOT et les réserver aux examens blancs, pour mesurer réellement le niveau.

---

### Sources principales
- MEBEKO/OFSP, *Exigences examen fédéral médecine humaine 2026* (FR) : https://www.bag.admin.ch/dam/fr/sd-web/fL9EvX0YPT2d/20260204_Exigences%20MED%202026_f.pdf
- OFSP, *Infotext eidg. Prüfung Humanmedizin 2026* (DE, avec exemples A, K′ et menu long) : https://www.bag.admin.ch/dam/de/sd-web/KdRYk-5ILb74/20260204_Infotext%20MED_2026_d_final.pdf
- OFSP, page de l'examen fédéral : https://www.bag.admin.ch/fr/examen-federal-en-medecine-humaine
- IML Berne, *MC‑Fragen und MC‑Prüfungen* (R. Krebs) : https://www.iml.unibe.ch/attachment/7/download/mc_anleitung.pdf
- IML, Self‑Assessment : https://www.iml.unibe.ch/angebote/assessment/pruefungsdienstleistungen/self-assessment
- IML, examen numérique : https://www.iml.unibe.ch/themen/uebersichten/artikel/schriftliche-eidgenoessische-pruefung-in-humanmedizin-erstmals-digital
- UniBas, MC‑Prüfungen : https://medizinstudium.unibas.ch/de/studium/pruefungen/multiple-choice-pruefungen-auf-ipad-mc-pruefungen/
- UZH, brochure 4e année : https://www.med.uzh.ch/dam/jcr:62dfa692-2a31-4ad5-bbec-ef9f50009b2e/4_SJ_Infobroschuere_mit_Titelblatt_def.pdf
- UNIGE, examen BA1 : https://www.unige.ch/medecine/enseignement1/bachelor-et-master-en-medecine-humaine/examens-bachelor/bachelor1
- UNIL FBM, examen fédéral : https://www.unil.ch/fbm/fr/home/ressources/espaces/espace-interne-em/examens-evaluations/examen-federal.html
- UniFR, examen fédéral : https://www.unifr.ch/med/fr/studies/msc/med/exafed.html
- PROFILES 2023 : https://www.unige.ch/medecine/application/files/6617/5939/2636/2023_PROFILES_final_Intregre2025.pdf
