# Audit agressif V0 — LOT_010 — G10 Douleurs de tous types

| | |
|---|---|
| Date | 25 octobre 2026 (Europe/Zurich) |
| Référentiel | PROMPT ULTIME V0, révision densification + AIPS Medina |
| Rôle | Auditeur (médical et conformité). Rapport seul. |
| Objet versionné | Branche `lot/LOT_010`, commit `639a79bff00ce740f9bad51e5569c149675a16d2` (24.10.2026), cinq HTML dans `LOTS/LOT_010/` |
| Drive Finaux | Dossier `1rupiUExpNyLfiTAgSC7JmT9kbb_54p4r`. Tailles API Drive = tailles git, octet annoncé pour octet. SHA-256 ci-dessous calculés sur les blobs git, pas sur un second téléchargement Drive. |
| Corpus AIPS | `AipsDownload_20261008.zip` (index SmPC du 08.10.2026). Monographies FR lues sur les HTML pointés par ce zip. |
| Décision | **Prêt-dépôt : NON.** Ne pas fusionner. Ne pas déposer dans Drive Finaux. |

Question finale (Vial peut-il gagner 90–100 % des points et prendre en charge ce patient en sécurité ?) : **non**, pour le lot entier et pour chaque fichier.

Un score chiffré, même s’il dépassait 90 %, ne lèverait pas ce refus : il y a au moins une critique, et la question finale est « non ».

## Prêt-dépôt

**NON.**

## Trois critiques (bloquantes)

### 1. Densité — omission critique sur les 11 entités

Bande V0 : **150–200 Ko par entité** (monographie SSP, puis chaque DX), après densification au-delà de 200 Ko puis rabotage. Moins de 150 Ko = omission critique. Aucun fichier du lot ne documente un premier jet > 200 Ko.

Taille = HTML de la monographie (`<details>` racine), en-têtes et sources du fichier exclus.

| Entité | Octets | Ko | Bande 150–200 Ko |
|---|---:|---:|---|
| SSP (Bloc 1, Phase A) | 93 471 | 91,3 | Non — omission |
| DX.1 Douleur aiguë nociceptive | 78 759 | 76,9 | Non |
| DX.2 Lombalgie commune | 73 394 | 71,7 | Non |
| DX.3 Douleur neuropathique périphérique | 31 959 | 31,2 | Non |
| DX.4 Douleur liée au cancer | 26 264 | 25,6 | Non |
| DX.5 Syndrome des loges aigu | 23 398 | 22,8 | Non |
| DX.6 Douleur entretenue par les antalgiques | 45 670 | 44,6 | Non |
| DX.7 Fibromyalgie | 42 044 | 41,1 | Non |
| DX.8 Névralgie du trijumeau | 43 705 | 42,7 | Non |
| DX.9 SDRC | 42 232 | 41,2 | Non |
| DX.10 Symptômes somatiques et dépression | 41 511 | 40,5 | Non |

Les fichiers HTML font 94 à 169 Ko **parce qu’ils empilent** 2 ou 3 entités, pas parce qu’une entité atteint la bande. DX.2 renvoie explicitement aux fiches du DX.1 (« Fiche complète : voir le DX.1, point 11 ») pour l’ibuprofène, le paracétamol et le tramadol : renvoi interdit (monographie allégée).

HTML unique SSP+10 DD : **absent** (cinq fichiers distincts). Ce point-là est respecté. Le nommage reste V7 (« Appel A / Appel B »), pas `Phase_A_V0` / `Phase_B_V0`.

### 2. AIPS — texte adouci, mauvais numéro, Compendium, doses non relues

Corpus prioritaire : zip Medina du 08.10.2026, type SmPC, HTML français. Les fichiers citent swissmedicinfo.ch ou le Compendium. Plusieurs URL de l’Appel A et de la Partie 1 sont cassées (`textType=FI⟨=FR` à la place de `textType=FI&lang=FR`).

Lu dans le SmPC, et en écart avec le lot :

- **Ibuprofène, Brufen®, autorisation 45031.** Le 3<sup>e</sup> trimestre est une contre-indication. Le 1<sup>er</sup> et le 2<sup>e</sup> trimestre sont à éviter sauf nécessité claire. À partir de la 20<sup>e</sup> semaine : oligohydramnios, atteinte rénale fœtale, retentissement sur le canal artériel. L’Appel A écrit : « AINS évités au 3<sup>e</sup> trimestre » et « opioïdes possibles sur la durée la plus courte ». Le DX.1 écrit « contre-indiqué au 3<sup>e</sup> trimestre » et omet la 20<sup>e</sup> semaine et les deux premiers trimestres. Texte AIPS adouci.
- **Tramadol.** Le lot cite l’autorisation **43787**. Ce numéro **n’existe pas** dans le zip. Tramal® est **40858** ; Tramal® retard est **53683**. Le plafond de 400 mg/j de chlorhydrate, lui, est bien dans le SmPC 40858. Les nausées « 15 % » ne sont pas dans le SmPC lu (nausées et vertiges > 10 % ; vertiges 14 % — ce dernier chiffre est exact).
- **Naloxone, Naloxon OrPha®, 56952.** « 0,1 à 0,2 mg IV puis 0,1 mg toutes les 2 à 3 minutes » est la posologie de la **dépression peropératoire**, pas la dose adulte unique. Surdosage connu ou suspecté : **0,4 à 2 mg**. La fiche présente la première comme « selon l’AIPS » sans la seconde.
- **Morphine, Sevredol®, 52076.** « 10 mg / 4 h » et « réserve 5–10 % » figurent dans le SmPC, comme **jour 1 d’un schéma qui monte** (20, 30, 50, 70, 100 mg / 4 h aux jours 2 à 6). Le recopier comme dose du patient naïf en douleur aiguë, sans dire d’arrêter l’escalade, est dangereux.
- **Partie 4.** Les doses sont sourcées au **Compendium** (information abrégée), canal interdit. La carbamazépine 200–400 mg/j puis 200 mg 3–4×/j, maximum 1 200 mg/j, **coïncide** avec Tégrétol® **29789** (relu ici). La grossesse du même SmPC (« ne doit pas être utilisé pendant la grossesse à moins que cela soit absolument nécessaire », spina bifida) est remplacée par « selon l’IPr ».
- **DX.9.** Le HELP du fichier dit que les doses de pamidronate et de prednisone viennent de la Revue médicale suisse et **n’ont pas été vérifiées dans une AIPS**. Ces molécules sont dans le corpus. « À vérifier » alors que le zip contient la molécule est interdit.
- **Oxcarbazépine, Trileptal®, 52852.** Indication AIPS : épilepsie, pas la névralgie. La fiche DX.8 le dit (hors indication, selon la SSC). L’Appel A, lui, met carbamazépine ou oxcarbazépine en premier choix sans cette réserve.

Doses relues et **concordantes** (pour ne pas tout rejeter en bloc) : paracétamol oral Dafalgan® 47503 (> 40 kg : 500–1 000 mg, intervalle 4–8 h, maximum 4 g ; enfant 22–30 kg : 300–500 mg ; clairance 10–50 ml/min : 6 h et 3 g/j) ; paracétamol IV Sintetica® 58716 (> 50 kg : 1 g jusqu’à 4 fois, intervalle 4 h — la perfusion AIPS est de **10 à 15** minutes, et la durée IV est plafonnée à **2 jours**, deux limites omises) ; métamizole Novalgin® 16951 (500–1 000 mg, 3–4×/j, maximum 4 g ; agranulocytose ; G6PD) ; ibuprofène rhumatismal 1 200–1 800 mg/j, maximum 2 400 mg, céphalée 400 mg ; Algifor® Junior 56046, 20–30 mg/kg/j ; prégabaline Lyrica® 57057, à ne pas utiliser si clairance < 30 ml/min (la Partie 2 le dit correctement) ; duloxétine axapharm 65781, indications dépression, prévention de récidive, douleur neuropathique diabétique, anxiété généralisée — le DX.2 dit explicitement que la lombalgie chronique n’y figure pas.

Insuffisance hépatique sévère : le SmPC Dafalgan **contre-indique** ; le plafond de 2 g vise la maladie hépatique non sévère et la cachexie. La fiche SSP mélange « insuffisance hépatique ou cachexie, 2 g » puis, ailleurs, « insuffisance hépatique sévère : ni paracétamol ».

### 3. Liste des dix différentiels — gravité non marquée, fourre-tout, source fausse

Critère annoncé dans l’Appel A : « fréquence **pondérée par la gravité** », et le syndrome des loges est « avancé au 5<sup>e</sup> rang ». V0 exige l’ordre de **prévalence décroissante**, le grave rare **gardant son rang de fréquence**, avec badge 🚩, rang E et place en tête d’algorithme.

Constat :

- Aucun 🚩. Aucun rang E1, E2, E3. Pas de colonne « À exclure en priorité ».
- L’algorithme commence bien par le syndrome des loges, puis retombe dans les fréquents. Il ne nomme pas, comme exclusions initiales, le syndrome coronarien, la dissection, la méningite, la grossesse extra-utérine, l’abdomen chirurgical.
- DX.1 (« douleur aiguë nociceptive ») est une catégorie fourre-tout. DX.3 empile polyneuropathie diabétique, névralgie post-zostérienne et radiculopathie. DX.6 empile céphalée par abus et hyperalgésie aux opioïdes. DX.10 empile symptômes somatiques persistants et dépression.
- Les intitulés DX.1–DX.10 sont les **mêmes** de l’Appel A aux quatre Parties (pas l’erreur LOT_001 où la liste change). Il n’y a pas de `LISTE_DX_CANONIQUE.md`.
- Incidence du trijumeau « 12,6 à 28,9 pour 100 000 personnes-années **[S12]** ». Dans l’Appel A, S12 est van Hecke 2014, revue de prévalence de la **douleur neuropathique** (le 6,9–10 % du DX.3), pas cette incidence.

Les drapeaux rouges du SSP citent loges, queue de cheval, arthrite septique, spondylodiscite, cancer. Ils ne couvrent pas le thorax, le crâne brutal ni l’abdomen. Pour le SSP G10 « douleurs de tous types », la question finale reste « non ».

## Scores — grille 2 / 1 / 0

46 questions du §12. Maximum 92. **2** seulement si le critère a été lu et tenu. **1** si l’élément est présent, incomplet, ou non démontré ligne à ligne. **0** si absent ou faux. Un 2 n’est jamais reporté d’une version antérieure : il n’y a pas d’audit V0 antérieur à reporter.

Méthode complaisante (2 dès qu’un titre est là) **écartée** : elle reproduirait l’erreur « score élevé, question finale non ».

### Phase A — monographie SSP (calculé)

| Note | Questions |
|---|---|
| 2 (×9) | 1.1, 1.2, 1.3, 2.1, 2.4, 3.4, 3.5, 11.10, 13.1 |
| 0 (×4) | 4.1 graves non placées avant les fréquentes comme liste d’exclusion ; 9.1 gold standard non dit ; 9.5 cas de figure non traités ; 11.8 grossesse AIPS adoucie |
| 1 (×33) | tout le reste |

**51 / 92 = 55,4 %.** Question finale : non.

### Phase B — plafonds

Aucun 2 accordé : ces monographies n’ont pas été notées question par question. Chaque 0 démontré remplace un 1. Le chiffre est un **plafond**, pas une validation.

| Entité | 0 démontrés | Plafond | Q. finale |
|---|---|---:|---|
| DX.1 | 11.8 (AINS limités au 3<sup>e</sup> trimestre) | 45/92 = 48,9 % | non |
| DX.2 | 11.5 (fiches renvoyées au DX.1) ; 11.8 (même limite de trimestre) | 44/92 = 47,8 % | non |
| DX.3 | aucun 0 clinique sur l’échantillon lu (rein de la prégabaline conforme au SmPC) | 46/92 = 50 % | non |
| DX.4 | — | 50 % | non |
| DX.5 | seuil de pression non recontrôlé sur le PDF HUG dans cette session ; non falsifié ici | 50 % | non |
| DX.6 | — | 50 % | non |
| DX.7 | 8.1 critères ACR 2016 comme critère qui pose le diagnostic (société américaine) | 45/92 = 48,9 % | non |
| DX.8 | 11.8 grossesse renvoyée à l’IPr, sans le texte tératogène du SmPC 29789 | 45/92 = 48,9 % | non |
| DX.9 | 11.5 pamidronate et prednisone non lus dans l’AIPS (admis dans le HELP) | 45/92 = 48,9 % | non |
| DX.10 | — | 50 % | non |

### Synthèse par fichier

| Fichier | Octets | SHA-256 | Score retenu | ≥ 90 % | Critique | Q. finale |
|---|---:|---|---:|---|---|---|
| `LOT_010_Appel_A_V7_Plan_et_Liste.html` | 134 784 | `9a1f7eab142b466f98e09fd85f6a4568a68607d4120bf129500b39b0170a3064` | SSP 55,4 % | Non | Oui (1, 2, 3) | Non |
| `LOT_010_Appel_B_V7_Partie_1_DX.1_a_DX.2.html` | 172 966 | `c023097ae6ab3585112ef3e800d2dee038492bd444d034a1ad8cca8d3a746758` | plafond 48,4 % | Non | Oui | Non |
| `LOT_010_Appel_B_V7_Partie_2_DX.3_a_DX.5.html` | 96 687 | `36b2aa7e55967246b6264b5b9fa51fc9ca336c8896bcd66072becb85dda5ea75` | plafond 50 % | Non | Oui | Non |
| `LOT_010_Appel_B_V7_Partie_3_DX.6_a_DX.7.html` | 104 097 | `09711a23bde449a5143234fe0c1d71e1cb63aac5e62cebf31b95638fe977d1d7` | plafond 49,5 % | Non | Oui | Non |
| `LOT_010_Appel_B_V7_Partie_4_DX.8_a_DX.10.html` | 147 142 | `107266a36e086542833217248c2d62608a64012e2cde0f96f4f9da3577f482aa` | plafond 49,3 % | Non | Oui | Non |

Score du lot = tous les fichiers au seuil. **Aucun ne l’atteint.** Cohérence des noms DX : tenue. Cohérence de la gravité (🚩, E) : non.

## Graves (non exhaustif, hors les trois critiques)

- Schéma Sevredol jour 1 cité sans l’escalade J2–J6.
- Naloxone de surdosage (0,4–2 mg) absente.
- Numéro Swissmedic du tramadol absent du corpus.
- Liens AIPS `FI⟨=FR` illisibles (Appel A, Partie 1).
- Paracétamol IV : « 15 minutes » au lieu de 10 à 15, et silence sur le maximum de 2 jours.
- Plafond 2 g du paracétamol collé à « insuffisance hépatique » alors que la forme sévère est une contre-indication.
- Fenêtres de l’Appel A qui s’impriment dans la phrase (« fenêtre complète… à sa première mention plus haut ») et la coupent (DN4, IRM, dans le bloc 2).
- Partie 2 : zéro fenêtre `<details>` en ligne ; beaucoup de titres nominaux.
- Pas de `DECISION_SEANCE.md`, pas de `evidence/`, pas de gel SHA, pas d’audit antérieur V0 dans le lot. `FIN_FICHIER` présent sur les cinq. Pas de `title=`. Tableaux enveloppés. Pas de script ni d’image.

## Ce qui n’a pas été fait

- PDF HUG (douleur aiguë, lombalgie, loges, antalgie 2023) non rouverts dans cette session. Les seuils qui ne s’appuient que sur ces PDF (pression > 30 mmHg, tramadol 200 mg chez l’âgé) ne sont ni confirmés ni infirmés ici.
- Enquête suisse sur la santé 2022 non rouverte. Les 49,9 % / 40,1 % « dos ou reins » restent attribués à l’OFS par le fichier, sans relecture de l’archive.
- Aucune réécriture des monographies. Aucune fusion. Aucun dépôt Drive.

Contenu d’audit établi à partir des HTML du commit cité et des SmPC du zip Medina ouverts le 25.10.2026. Non validé cliniquement par un médecin.
