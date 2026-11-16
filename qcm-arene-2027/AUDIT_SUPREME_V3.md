# Audit Suprême · Arène QCM Examen Fédéral Suisse de Médecine 2027 (v3)

## 1. Volumétrie & Proportions vérifiées
- **248 / 248 situations de départ PROFILES (SSP)** réparties en 4 secteurs : `G` (16), `S` (113), `F` (44), `O` (75).
- **102'527 QCMs Type Examen** générés et audités (min **405** / moyenne **413.4** / max **420** QCMs par SSP ; soit > **5'200 pages** à 20 QCMs/page).
- **Proportions strictement positives** (`a, k', m > 0`) :
  - `a = 0.5478` (**56'167 Type A** — 1 seule meilleure réponse sur 5)
  - `k' = 0.3048` (**31'248 Type K'** — 4 propositions indépendantes `+ Vrai / - Faux`, barème officiel IML `4/4=1`, `3/4=0.5`, `≤2/4=0`)
  - `m = 0.1474` (**15'112 Menu Long** — sélection dans une liste étendue avec recherche instantanée)
- **2'477 diagnostics différentiels** stratifiés en **5 niveaux de fréquence** (*Très fréquente, Fréquente, Peu fréquente, Moins fréquente, Rare*) et drapeaux rouges **« À ne pas manquer »**.

## 2. Double Audit Indépendant (2 Passes Complètes)

### Passe 1 — Structure & Contrôleur d'Aléa Absolu (`scripts/audit_pass1_structure_randomness.py`)
- Distribution Type A globale : **A = 20.01 % · B = 20.03 % · C = 19.98 % · D = 19.98 % · E = 19.99 %**.
- **Streak maximal consécutif Type A** (dans chaque SSP et globalement) : **2** (zéro séquence ≥ 3).
- **Cycles alternants `X-Y-X-Y-X`** : **0**.
- **Type K'** : **16 / 16 vecteurs 4-bit** couverts (`0..4` Vrais), **0 répétition consécutive** de vecteur.
- **Menu Long** : **0 répétition consécutive d'index**, dispersion sur les 16 index.
- **Entrelacement erratique** : séquence maximale d'un même type = **4**.
- **Résultat Passe 1** : **SUCCÈS TOTAL (0 erreur)**.

### Passe 2 — Clinique, Justifications & Pratiques suisses (`scripts/audit_pass2_medical_ch.py`)
- **Alignement 1-à-1** entre réponse exacte et justifications option par option sur **102'527 QCMs** : **0 incohérence**.
- **6'225 QCMs dédiés aux pratiques suisses** (Compendium / AIPS Swissmedic, Smarter Medicine SSMIG/SGAIM Hospitalier 2023 & Ambulatoire 2021, OFSP déclaration obligatoire, SSI Guidelines, HUG/CHUV continuité jusqu'à la sortie d'hospitalisation).
- **Hygiène rédactionnelle** : **0 fuite HTML**, **0 placeholder « À vérifier »**.
- **Résultat Passe 2** : **SUCCÈS TOTAL (0 erreur, 0 avertissement)**.

## 3. Intégration Visuelle & Interface
- Fond blanc papier (`#fcfbf7`), 4 palettes colorées distinctes (`G`, `S`, `F`, `O`) avec cellules de taille uniforme non collées à effet 3D/luminescent.
- Bandeau santé suisse + Veille Examen fédéral 2027 avec liens directs vers OFSP, MEBEKO, IML Berne, Compendium/AIPS, SSMIG/SGAIM, Smarter Medicine, SSI, HUG, CHUV, Inselspital, USZ, USB et Facultés de médecine suisses.
- Pleine page **Réponses** (bouton vert) incluant : verdict, justification option par option, **Rappel de base (sciences fondamentales)**, **Explication plus spécifique**, source datée, **19 planches anatomiques** (`assets/cs/*.webp`), **6 schémas/courbes physiologiques SVG annotés** (ECG STEMI, Spirométrie Débit-Volume, Davenport Gazométrie, Dissociation Hb-O2 Bohr, Système Nerveux Autonome, Parcours Clinique Suisse) et **Panoramique stratifié des causes** directement intégré.
