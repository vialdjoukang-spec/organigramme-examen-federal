# INSTRUCTIONS POUR CONTINUER AISÉMENT — PROJET 248 SSP EN JSON (`3. Grok_AI_json_Project`)

> [!IMPORTANT]
> **RÈGLE D'ACCUEIL OBLIGATOIRE POUR GROK :**
> **Après la prise de contact, Grok DOIT absolument faire un résumé complet et structuré de l'ensemble du projet (objectifs, historique, architecture `.json`, règles de qualité, calibre `90–120 Ko`, cascade suisse, zéro arbre décisionnel, répartition des 248 LOTS et des 3 comptes images) AVANT de commencer toute rédaction.**

---

## 0. Comprendre TOTALEMENT le projet depuis le début
- **Objectif global** : produire et auditer l'intégralité des **248 SSP suisses (PROFILES 2023)** pour l'Examen Fédéral de Médecine en Suisse, soit **3 975 entités cliniques (`DX.1..N`) + 248 Chapitres 0 (`Phase A`)**.
- **Évolution du cahier des charges (historique complet)** :
  1. **Prompt Alpha (`19.11.2026`)** : calibre initial `80–100 Ko` de texte pur par cours, cascade posologique suisse à 4 paliers (AIPS Swissmedic → Compendium.ch → Sociétés savantes & CHU suisses → Sociétés européennes), phrases verbales exclusives, 100 % des notions de la *Cartographie Renouveau*.
  2. **Phase intermédiaire (`20.11.2026`)** : essai à `30–50 Ko` abandonné car jugé trop pauvre/médiocre, puis retour à `80–100 Ko` et suppression définitive des arbres décisionnels (`.fm-canvas`, réalisés par Vial lui-même).
  3. **Architecture finale `.json` (`21.11.2026`)** : rédaction **100 % en `.json` pur sans balise HTML** dans `SSP_nnn/source_json/` avec un calibre **`90–120 Ko` de texte médical pur sans balise** par cours, puis compilation déterministe finale vers HTML L1 + `UNIQUE.html` (police **Atkinson Hyperlegible**, modales `.fen` + 2 onglets PK/PD SVG, infobulles `Why`, signature `#signature-ia`).
- **État actuel & classement par gravité** :
  - Les **248 LOTS** ont été audités et classés du plus catastrophique (`1.`) au moins catastrophique (`248.`) dans `GEMINI_word_à_générer/00_CLASSEMENT_GRAVITE_248_LOTS.json`.
  - Les **5 LOTS les plus critiques** (`#1 SSP_246`, `#2 SSP_236`, `#3 SSP_247`, `#4 SSP_240`, `#5 SSP_034`) sont déjà amorcés en `source_json/`.
  - Les **208 SSP cliniques applicables** pour les images d'examens complémentaires sont répartis pour les **3 comptes Google Pro** dans `DEMANDES_IMAGES_3_COMPTES/`.

---

## 1. Structure du dossier `3. Grok_AI_json_Project`
- **`GEMINI_word_à_générer\`** :
  - `00_CLASSEMENT_GRAVITE_248_LOTS.json` : classement officiel des **248 LOTS** du plus catastrophique (`1.`) au moins catastrophique (`248.`).
  - `1. SSP_nnn — <Nom>\` … `248. SSP_nnn — <Nom>\` : chaque dossier contient le `.json` du SSP avec son `sommaire`, les plans en 14 points (`phase_a` et `phase_b` avec 100 % des `notions_obligatoires` de `NOTIONS.json`), `rappel_obligatoire_avant_redaction`, `specificites_locales_ssp`, et le `prompt_alpha_a_jour` collé intégralement.
  - `00_IMAGES_EXAMENS_COMPLEMENTAIRES_PAR_SSP.json` : liste filtrée des **208 SSP cliniques applicables** nécessitant des illustrations d'examens complémentaires.
- **`DEMANDES_IMAGES_3_COMPTES\`** :
  - `00_INDEX_DEMANDES_IMAGES.json` + `COMPTE_1_IMAGES_EXAMENS.json`, `COMPTE_2_IMAGES_EXAMENS.json`, `COMPTE_3_IMAGES_EXAMENS.json` (70 / 69 / 69 SSP) prêts à être remplis avec les URL directes valides.
- **`_outils_copie\`** :
  - `verif_source_json.py` (validateur strict `90–120 Ko` sans balise)
  - `compilateur_json_vers_html.py` (compilateur déterministe `source_json → HTML L1 + UNIQUE.html`)
  - `verif_mission.py`, `catalogue_248.json`, `cartographie_DATA.json`

---

## 2. Règles Absolues de Rédaction (À NE JAMAIS ENFREINDRE)
1. **Format de travail** : rédiger **exclusivement en `.json` pur** dans `1_Claude AI\SSP_nnn\source_json\` (`Phase_A.json` et `DX.1.json` … `DX.N.json`) — **1 cours complet par requête** (production graduelle).
2. **Calibre obligatoire** : **`90,0–120,0 Ko` (`92 160` à `122 880` octets) de texte médical pur sans balise HTML** par fichier `.json`. Répartir la densité proportionnellement à l'importance clinique (aucun quota rigide par section, zéro remplissage).
3. **Qualité clinique maximale & zéro médiocrité** :
   - Zéro prose générique ou patronnée où seul le nom de la maladie change.
   - Zéro phrase nominale (`PHRASE_NOMINALE`), zéro phrase partagée entre cours d'un même SSP (`PHRASE_PARTAGEE`), zéro gabarit `cartographie_DATA.json`, zéro terme de chantier (`LOT`, `V0`, `Phase A/B`, `DX.n`, `Partie n`).
   - Utiliser les guillemets typographiques français `« … »` dans les chaînes JSON.
4. **Zéro arbre décisionnel** : ne jamais générer d'arbre décisionnel graphique (`.fm-canvas`, SVG décisionnel). L'auteur (Vial) les réalise lui-même.
5. **Respect des circuits** :
   - `MONOGRAPHIQUE` (189 SSP) : plan maladie en 14 points.
   - `NON_MONOGRAPHIQUE` (52 SSP) : 14 points adaptés en Leçons Suisses Structurées (**jamais** de titres « Physiopathologie / Approche syndromique / Diagnostic positif »).
   - `MIXTE` (7 SSP) : adapter chaque chapitre selon sa nature.
6. **Cascade posologique suisse à 4 paliers** :
   1. **AIPS Swissmedic** (n° à 5 chiffres) → 2. **Compendium.ch** → 3. **Sociétés savantes & CHU suisses** (HUG, CHUV, Inselspital, USZ, USB, OFSP, ASSM, SSMIG, Tox Info Suisse 145) → 4. **Sociétés savantes européennes** (ESC, ERS, EASL, ESMO, etc.).
7. **100 % des notions obligatoires** : couvrir chaque notion de `NOTIONS.json` (`0 NON`, `0` sous `60 %`).

---

## 3. Schéma JSON attendu dans `SSP_nnn\source_json\<Phase_A|DX.i>.json`
```json
{
  "meta": {
    "ssp": "SSP_246",
    "code_profiles": "O7.24",
    "circuit": "NON_MONOGRAPHIQUE",
    "titre": "Titre exact du cours",
    "cim": "Code CIM-10",
    "urgence": "immediat | urgent | semi-urgent | chronique"
  },
  "sections": [
    {
      "point": 1,
      "titre": "Titre adapté au circuit",
      "paragraphes": ["Texte médical en phrases verbales exclusives..."],
      "points_cles": ["Point clé en phrase verbale conjuguée..."]
    }
  ],
  "tableaux_cliniques": [
    {
      "titre": "Titre du tableau",
      "colonnes": ["Col 1", "Col 2", "Col 3"],
      "lignes": [["...", "...", "..."]]
    }
  ],
  "fiches_pkpd": [
    {
      "nom": "Nom molécule",
      "titre": "DCI — Spécialité® (Compendium.ch AIPS n° XXXXX)",
      "cible_moleculaire": "Mécanisme pharmacodynamique moléculaire exact",
      "pharmacocinetique": [{"parametre": "Absorption / Tmax / T½", "valeur": "..."}],
      "pharmacodynamique": [{"parametre": "Posologie suisse / CI / Grossesse", "valeur": "..."}]
    }
  ],
  "infobulles_why": [
    {"section": 1, "terme": "Terme clé", "explication": "Justification physiopathologique ou règle suisse (1-3 phrases, sans >)."}
  ],
  "vignettes_qcm": [
    {
      "titre": "Titre clinique",
      "enonce": "Vignette clinique suisse...",
      "options": ["A. ...", "B. ...", "C. ...", "D. ..."],
      "reponse_justifiee": "Réponse B. Justification clinique et légale suisse..."
    }
  ],
  "sources_suisses": [
    {"id": "aips-XXXXX", "organisation": "Swissmedic AIPS", "titre": "...", "date": "2025"}
  ]
}
```

---

## 4. Commandes de Contrôle & Compilation Finale
Depuis `c:\Users\viald\OneDrive\Documents\DOSSIER_LOCAL_Examen_Fédéral\1_Claude AI\` :
- **Valider un SSP en `source_json\` (`90–120 Ko`, `0` erreur)** :
  `python _outils/verif_source_json.py 246`
- **Compiler `source_json\` → HTML L1 + `SSP_nnn_<code>_UNIQUE.html`** (en fin de projet) :
  `python _outils/compilateur_json_vers_html.py 246`
- **Vérifier la télémétrie bloquante** :
  `python _outils/watchdog_telemetrie.py`

---

## 5. Ordre de Reprise Immédiate (du plus catastrophique au moins catastrophique)
Les 5 premiers LOTS prioritaires (`#1 SSP_246`, `#2 SSP_236`, `#3 SSP_247`, `#4 SSP_240`, `#5 SSP_034`) sont déjà amorcés dans `1_Claude AI\SSP_nnn\source_json\`. Enchaîner ensuite dans l'ordre exact de `GEMINI_word_à_générer\00_CLASSEMENT_GRAVITE_248_LOTS.json` (`#6 SSP_035`, `#7 SSP_248`, `#8 SSP_157`, `#9 SSP_036`, `#10 SSP_038`, … jusqu'à `#248`).
