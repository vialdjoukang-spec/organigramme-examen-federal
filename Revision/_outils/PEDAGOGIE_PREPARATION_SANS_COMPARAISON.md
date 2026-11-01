# Préparation sans comparaison — architecture pédagogique

*Médecin Grand Maître Professeur Bitunder · Revision / Flash / Organigramme · examen fédéral de médecine humaine (CH)*
*Rédigé le dimanche 1er novembre 2026 (Europe/Zurich, UTC+1). Document vivant, dans `Revision/_outils/`.*

> « On ne se prépare pas *contre* les autres. On se prépare *vers* un référentiel. »

---

## 0. En une minute

- **Préparation sans comparaison** : je mesure la progression de Vial **contre un référentiel fixe**, à savoir PROFILES 2023 (265 SSP) et le blueprint MEBEKO/IML. Je ne la mesure jamais contre des pairs : pas de rang, pas de percentile, pas de classement.
- **Le benchmark est double** : (1) la **couverture DD** de chaque SSP (tous les diagnostics différentiels du LOT sont interrogés au moins une fois), et (2) la **maîtrise** (seuils absolus de réussite par niveau EX / AP / SPE).
- **Sept couches** : A cartographie → B noyau Type A réflexe → C approfondissement AP → D spécialiste SPE → E feedback 💡 en 4 blocs → F état des lieux % et relève Λ → G cycle G → S → F → O.
- **Une séance dure 25 à 40 min**, découpée en échauffement, noyau, consolidation et clôture (§ 4). Elle n'a pas de chronomètre punitif ni de badge comparatif.
- **« Prêt examen »** se décide par SSP, selon des critères objectifs (§ 5). Ils sont vérifiables par `resume_jour.py` et dans `_index/REGISTRE.csv`.

---

## 1. Vision

### 1.1 Ce que « sans comparaison » veut dire
| Sens | Ce que l'on fait | Ce que l'on ne fait pas |
|---|---|---|
| **Sans comparaison aux pairs** | On compare Vial d'aujourd'hui à Vial d'hier, et l'écart au référentiel fédéral. | Rang, moyenne de promotion, « meilleur que 80 % ». |
| **Sans équivalent (qualité)** | Chaque question est ancrée sur un DD réel du LOT, une source suisse et une leçon précise (lien § Phase A / DX). | Banque générique, questions copiées, items IML (ils sont sous copyright). |
| **Trajectoire individuelle maîtrisée** | Ordre fixe, seuils absolus, reprise ciblée des erreurs. | Butinage aléatoire, volume pour le volume. |

### 1.2 Pourquoi c'est la bonne cible pour l'examen fédéral
- L'examen est **critérié** : le seuil est fixé par Angoff, Hofstee et un ancrage, sans points négatifs (Exigences MEBEKO 2026, § 5.1). Ce qui compte, c'est le niveau absolu de maîtrise, pas la position dans la cohorte.
- Le blueprint tire au sort des **SSP** croisées avec trois tâches (*mechanisms*, *assessment/diagnosis*, *management*). Couvrir les SSP **et** leurs DD, c'est donc couvrir l'espace d'examen.
- Le stress comparatif dégrade la consolidation. Une métrique interne et stable soutient la régularité, qui est le vrai facteur de réussite.

### 1.3 Le référentiel (benchmark officiel)
1. **PROFILES 2023** : 265 SSP (G, S, F, O), rôles CanMEDS, 9 EPA.
2. **Exigences MEBEKO / IML 2026** : 240 QCM, Type A, K′, menu long, séquences et vignettes brèves.
3. **Couverture DD du LOT** : liste `dx_cibles` de chaque LOT (Phase A + DX.1…n).
4. **Sources suisses d'abord** : OFSP, SSMI/SGAIM, mediX, HUG, CHUV, Swissmedic, compendium ; ensuite seulement les sources européennes et internationales.

---

## 2. Le rôle du Grand Maître Professeur Bitunder

### 2.1 Posture
- **Professeur clinicien suisse** qui parle à un confrère médecin : exigeant, bref, bienveillant, jamais condescendant.
- **Maître du raisonnement, pas de la récitation** : chaque question entraîne un réflexe (danger ? profil ? examen qui tranche ?).
- **Gardien de la vérité clinique** : il préfère une question de moins à une question douteuse. Il n'invente rien, ni fait, ni image, ni référence.
- **Architecte** : chaque livrable s'insère dans une couche (§ 3) et met à jour la relève Λ.

### 2.2 Critères d'exigence (les « 7 sceaux »)
1. **Ancrage** : chaque item renvoie à un DX du LOT (`dx`, `dx_cibles`) et à une ancre de leçon (`source_lecon.href`).
2. **Format IML** : stem long et options courtes, homogènes et plausibles. Le test de couverture doit passer. Pas de *cue*, pas de « toujours / jamais », pas de double négation, ≤ 5 % de A négatif.
3. **Blueprint** : `tache` ∈ {mechanisms, assessment_diagnosis, management} et `setting` ∈ {cabinet, urgences, hôpital, EMS}, répartis sur la banque.
4. **Niveau juste** : EX = réflexe attendu de tout candidat ; AP = mécanisme ou nuance ; SPE = décision de spécialiste, étiquetée par spécialité.
5. **Feedback 💡 complet** en 4 blocs (§ 3 E), fermé par défaut.
6. **Équilibre des clés** : répartition A–E à ± 1 près, jamais 3 clés identiques d'affilée.
7. **Traçabilité** : JSON versionné, CHANGELOG, statut `revue_auto` → `revue_humaine` → `valide`.

### 2.3 Comment il « recycle » l'expertise déjà posée ♻️
| Actif existant | Recyclé en | Où |
|---|---|---|
| Stratégie QCM CH (formats, règles IML, typologie A / séquence / K′ / menu long) | Règles de rédaction et mix cible de la banque | `/workspace/grok/STRATEGIE_QCM_EXAMEN_CH.md` → `_outils/CHARTE_REDACTION.md` |
| Banque G01 v2 (40 Q : 23 EX, 10 AP, 7 SPE ; blocs Raisonner / Discriminer / Pièges & alarmes) | **Gabarit canonique** de tout SSP G | `G_symptomes_generaux/G01_transpiration_anormale/` (`_bank_G01.py`, `.json`, `.html`) |
| Feedback 💡 fermé par défaut, mode révision confirmé | Contrat UX non négociable | `_outils/templates/_ssp_reflexe.html`, `_ssp_script.js` |
| Carte réflexe (3 questions + axes temporalité / topographie / signes associés) | Couche B (noyau) de chaque SSP | champ `rendu.carte_html` du JSON |
| Charte Flash (Atkinson Hyperlegible, rouge #C8102E, fond bleu ciel pâle, anat → physio → physiopath → clinique → tt) | Charte visuelle et chaîne explicative du feedback | `_outils/templates/_fonts.css` + CHARTE_REDACTION |
| `resume_jour.py`, ETAT_DES_LIEUX, REGISTRE | Couche F (mesure absolue + relève Λ) | `_outils/scripts/resume_jour.py`, `_index/REGISTRE.csv` |
| Builder | Industrialisation G02 → G16 | `_outils/scripts/build_ssp.py`, `G02_*/_bank_G02.py` |

**Principe de recyclage** : on ne réécrit pas, on **réinstancie** le gabarit G01 sur chaque SSP. On change le contenu (DD du LOT), jamais le contrat (structure JSON, UX 💡, niveaux, charte).

---

## 3. Architecture en sept couches

```
 (A) Cartographie SSP / PROFILES ──► définit QUOI couvrir
        │
 (B) Noyau Type A réflexe (EX) ────► socle examen : réflexes et DD
        │
 (C) Approfondissement AP ─────────► mécanismes, nuances, pièges fins
        │
 (D) Spécialiste SPE ──────────────► décisions de spécialiste, étiquetées
        │
 (E) Feedback 💡 en 4 blocs ───────► transforme l'erreur en apprentissage
        │
 (F) État des lieux % + relève Λ ──► mesure absolue, jamais relative
        │
 (G) Cycle G → S → F → O ──────────► ordre de progression du programme
```

### (A) Cartographie SSP / PROFILES
- **Unité = 1 SSP = 1 LOT** (LOT_001 = G1 … LOT_016 = G16, puis S, F, O selon la numérotation PROFILES).
- Pour chaque SSP : titre, LOT, liste des **DD** (Phase A + DX.1…n), *red flags*, tâches et settings.
- Fichiers : `_index/MAP_G1_G16.json` (carte), `_index/REGISTRE.csv` (registre généré).
- **Sortie** : la **matrice de couverture DD × tâche** du SSP. Elle sert de cahier des charges à la banque.

### (B) Noyau Type A réflexe — niveau EX (noir #1a1a1a)
- 55–60 % de la banque (G01 : 23/40). Ce sont des vignettes brèves en contexte suisse (cabinet, urgences, EMS, hôpital).
- Trois blocs : **Raisonner** (triage, prochain pas, *red flag*, mécanisme de base) ; **Discriminer** (DD réel contre DD réel, examen qui tranche) ; **Pièges & alarmes** (fausses réassurances, contre-indications).
- **Règle de couverture** : chaque DD du LOT apparaît **au moins une fois** comme bonne réponse ou distracteur discriminant au niveau EX.

### (C) Approfondissement — niveau AP (bleu #0B5A8C)
- Environ 25 % (G01 : 10/40). Le mécanisme est expliqué par la chaîne **anat → physio → physiopath → clinique → tt** (exemples G01 : NK3/fézolinétant, SNAP‑25/toxine botulique, GABA‑A/sevrage).
- Cible la tâche *Understanding mechanisms of disease* du blueprint, qui est souvent sous-entraînée.

### (D) Spécialiste — niveau SPE (violet #6B2D8B + badge `SPE · spécialité`)
- 15–20 % (G01 : 7/40, 7 spécialités). Ce sont des décisions de deuxième ligne (p. ex. Deauville 4 en fin de traitement d'un LH, délai des ISRS dans le trouble panique).
- Le bouton 🔥 alimente le tableau « spécialité qui vous exalte ». C'est une **boussole d'intérêt personnel**, pas un classement.
- **SPE n'est pas requis pour « prêt examen »** : c'est un bonus d'excellence (§ 5).

### (E) Feedback 💡 — 4 blocs, fermé par défaut
Le feedback s'ouvre **uniquement** au clic 💡 ou en mode révision confirmé. Il n'est jamais `<details open>` et n'est jamais déplié à l'impression écran.
1. **Clé + pourquoi c'est juste** (`pourquoi_vrai`), en enchaînant les maillons de la chaîne anat → tt.
2. **Pourquoi chaque autre option est fausse** (`pourquoi_faux_par_option`), une ligne par distracteur, en citant le DD concerné.
3. **Perle clinique** (`perle_clinique`) : le réflexe à emporter, les probabilités en **rouge #C8102E**.
4. **Source de la leçon** (`source_lecon` : libellé + ancre HTML), pour revenir au cours Flash en un clic.

### (F) État des lieux % + relève Λ
- **Métrique absolue** : % des SSP de la tranche prêts (aujourd'hui G1–G16 : 1/16 = 6,2 %), puis, par SSP, Q, EX, AP, SPE et statut.
- **Relève Λ** : un bloc court à la fin de chaque résumé (progression, prochain SSP, contraintes). Il permet à n'importe quel agent futur de reprendre sans perte.
- Commande : `python3 /workspace/grok/Revision/_outils/scripts/resume_jour.py --write`. Elle génère `RESUME_JOUR.md`, `ETAT_DES_LIEUX_QCM.md` et `_index/REGISTRE.csv`.
- **Interdit** : toute métrique relative (rang, percentile, comparaison inter-utilisateurs).

### (G) Cycle G → S → F → O
1. **G1 → G16** (symptômes généraux) d'abord. C'est le socle transversal, et il nourrit tous les DD ultérieurs.
2. Puis **S** (symptômes par système), **F** (résultats et fonctions), **O** (situations).
3. **On ne passe pas** au SSP suivant tant que le SSP courant n'a pas sa banque HTML en `revue_auto` minimum. On ne passe pas à la famille suivante (G → S) tant que ≥ 80 % de la famille n'est pas « prêt examen » (§ 5).
4. **Temps 1** = Type A + 💡 sur toute la famille. **Temps 2** = K′, séquences de 2–3 Q et menu long sur les mêmes SSP (mix cible de la stratégie : A 50 %, séquences 15 %, K′ 25 %, menu long 10 %).

---

## 4. Parcours d'une séance type (25–40 min), sans gamification comparative

| Phase | Durée | Contenu | Pourquoi |
|---|---|---|---|
| **1. Échauffement** | 3–5 min | Relire la **carte réflexe** du SSP (3 questions réflexes + axes). | Amorcer le schéma avant l'effort. |
| **2. Rappel espacé** | 5–8 min | 5–8 Q **ratées lors des séances précédentes** (tous SSP déjà vus), filtre EX. | Consolidation, effet de test. |
| **3. Noyau du jour** | 10–15 min | 10–15 Q nouvelles du SSP courant : EX d'abord, puis AP. Répondre, puis ouvrir 💡 **même si la réponse est juste**. | Le feedback compte autant que la réponse. |
| **4. Approfondissement** | 5–8 min | 3–5 AP/SPE. Signaler 🔥 si une spécialité attire. | Mécanismes, désir d'apprendre. |
| **5. Clôture** | 2–4 min | Noter 1 perle et 1 erreur type ; lancer `resume_jour.py --write`. | Méta-cognition, relève Λ. |

**Rythme d'examen** : environ 97 s par question à l'examen (240 Q en 2 × 3 h 15). En séance, on vise ≤ 90 s par question EX. Le temps est une **information**, pas une sanction.

**Ce qui est banni** : classements, points comparés, « streaks » culpabilisants, badges de rang. **Ce qui est permis** : la courbe personnelle (score par niveau, par bloc et par spécialité dans le HTML), le tableau 🔥, la progression % du référentiel.

**Fréquence** : 1 séance par jour ouvré. Le rappel espacé suit J+1, J+3, J+7 et J+21 pour chaque erreur.

---

## 5. Critères « prêt examen » par SSP (seuils absolus)

Un SSP est **PRÊT EXAMEN** si et seulement si **les 6 critères** sont remplis :

| # | Critère | Seuil |
|---|---|---|
| 1 | **Banque** | ≥ 30 Q Type A (cible 40), JSON + HTML, statut ≥ `revue_auto` |
| 2 | **Couverture DD** | 100 % des DD du LOT interrogés ≥ 1 fois ; chaque *red flag* ≥ 1 fois en bloc « Pièges & alarmes » |
| 3 | **Blueprint** | Les 3 tâches présentes (mechanisms ≥ 15 %, assessment ≥ 40 %, management ≥ 25 %) ; ≥ 3 settings différents |
| 4 | **Maîtrise EX** | ≥ **85 %** de réussite au 1er passage d'une série EX complète, **sans** ouvrir 💡 avant de répondre |
| 5 | **Maîtrise AP** | ≥ **70 %** de réussite AP |
| 6 | **Rétention** | ≥ 80 % au rappel J+7 des questions initialement ratées |

- **SPE** : ≥ 60 % = mention « excellence ». Ce n'est **pas** bloquant.
- **Famille prête** (p. ex. G1–G16) : ≥ 80 % des SSP « prêts examen », et 100 % des SSP avec banque disponible.
- **Maîtrise DD avant examen** : l'objectif final est que 100 % des SSP G aient les critères 1–2 remplis avant la session, puis S, F et O selon le temps disponible.
- Les critères 1–3 sont **vérifiables automatiquement** (JSON). Les critères 4–6 dépendent du score saisi par Vial ; un champ futur `progression_perso` du REGISTRE est prévu pour les suivre.

---

## 6. Lien concret avec les fichiers existants

| Rôle | Chemin (sous `/workspace/grok/`) |
|---|---|
| Stratégie QCM CH (formats, sources) | `STRATEGIE_QCM_EXAMEN_CH.md` / `.html` / `.pdf` |
| Gabarit canonique G01 v2 | `Revision/G_symptomes_generaux/G01_transpiration_anormale/LOT_001_G1_TypeA_Reflexe.{json,html,pdf}` |
| Banque source G01 | `Revision/G_symptomes_generaux/G01_transpiration_anormale/_bank_G01.py` |
| Journal G01 | `Revision/G_symptomes_generaux/G01_transpiration_anormale/CHANGELOG.md` |
| Prochain SSP en chantier | `Revision/G_symptomes_generaux/G02_adenopathie_tumefaction/_bank_G02.py` |
| Template HTML et JS (💡 fermé, filtres EX/AP/SPE, 🔥) | `Revision/_outils/templates/_ssp_reflexe.html`, `_ssp_script.js`, `_fonts.css` |
| Builder générique | `Revision/_outils/scripts/build_ssp.py` |
| Mesure dynamique + relève Λ | `Revision/_outils/scripts/resume_jour.py --write` → `Revision/RESUME_JOUR.md`, `Revision/ETAT_DES_LIEUX_QCM.md`, `Revision/_index/REGISTRE.csv` |
| Carte G1–G16 | `Revision/_index/MAP_G1_G16.json` |
| Arborescence S / F / O (à remplir) | `Revision/S_symptomes_systemes/`, `Revision/F_fonctions/`, `Revision/O_situations/` |
| Charte de rédaction | `Revision/_outils/CHARTE_REDACTION.md` |
| Persona agent | `Revision/_outils/PROFIL_GRAND_MAITRE_BITUNDER.md` |
| Ce document | `Revision/_outils/PEDAGOGIE_PREPARATION_SANS_COMPARAISON.md` |

**Versionnage** : GitHub uniquement, branche `grok/revision` (dépôt `organigramme-examen-federal`). Jamais Drive. Pas de PR, de merge vers `main` ni de force-push sans ordre explicite de Vial.

---

## 7. Feuille de route immédiate

1. **G02** (tuméfaction / adénopathie) : finaliser `_bank_G02.py` sur le gabarit G01, puis build HTML/PDF et `resume_jour.py --write` (→ 12,5 %).
2. G03 → G16 au rythme d'un SSP par jour de production, chacun avec CHANGELOG.
3. Ajouter `progression_perso` (scores EX/AP/SPE, date du dernier passage, J+7) au REGISTRE pour automatiser les critères 4–6.
4. Temps 2 sur G : K′ et séquences, après « famille G prête ».
