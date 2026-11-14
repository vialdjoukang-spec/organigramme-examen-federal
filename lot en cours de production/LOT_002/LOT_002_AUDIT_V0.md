# LOT_002 — Audit V0 (G2 · Tuméfaction, masse et adénopathie)

Date : 25 octobre 2026. Matériau audité : branche `audit/LOT_002` (HTML « AUDITÉ » du 24.10.2026, vocabulaire Appel A/B). Prompt : PROMPT ULTIME V0 (PR #447), poids **par entité**, pas par fichier consolidé. Aucun HTML unique n’a été produit.

Les scores ci-dessous notent le **matériau hérité**, pas les fichiers corrigés de cette branche. Le rédacteur de la correction ne s’audite pas. Question finale des deux phases : **non**. Dépôt : **non**.

## Scores

Barème : 46 questions, 2/1/0, maximum 92. Une critique suffit à refuser, même si le pourcentage était plus haut.

| Phase | Score | % | Finale | Critique | Décision |
|---|---|---|---|---|---|
| A — SSP | 36/92 | **39 %** | non | oui | refusé |
| B — moyenne des 10 DX | — | **34 %** | non | oui | refusé |

Détail Phase A (lecture du texte et des fenêtres, pas le proxy 98,8 % du 24.10) :

| Point | Obtenu | Max | Motif principal |
|---|---|---|---|
| 1 | 4 | 6 | définition utilisable, mais autorité AFP 1998/2016, pas une société savante |
| 2 | 5 | 8 | incidences NKRS justes ; pas de distribution suisse de la plainte |
| 3 | 4 | 10 | chaîne courte ; pas de lien lésion → classe médicamenteuse |
| 4 | 2 | 4 | urgences nommées dans le texte, liste sans 🚩 ni rang E |
| 5 | 2 | 4 | questions présentes, plusieurs sans seuil suisse relu |
| 6 | 2 | 4 | geste décrit trop brièvement |
| 7 | 4 | 10 | syndromes nommés, pas éclatés en 7.1 avec geste et mécanisme partout |
| 8 | 1 | 4 | NICE NG12 (Royaume-Uni) à la place d’un critère CH/UE |
| 9 | 5 | 12 | fenêtres d’examens riches mais souvent copiées hors sujet |
| 10 | 1 | 2 | embranchements présents, graves non en tête |
| 11 | 3 | 22 | but non chiffré, pharmacologie et sortie incomplètes, doses hors AIPS |
| 12 | 1 | 2 | trois niveaux nommés, peu de substance suisse relue |
| 13 | 1 | 2 | phrases utiles |
| 14 | 1 | 2 | pièges réels, sources surtout américaines ou NICE |

Phase B, même barème, pénalités du générateur commun (fenêtres copiées, sources US/NICE/NHS, doses non extraites de l’AIPS, entité < 150 Ko) plus le défaut propre :

| Fichier hérité | Octets | Score | Défaut propre |
|---|---|---|---|
| DX.1 Adénopathie réactionnelle | 130 638 | 41 % | paracétamol compatible avec l’extrait AIPS lu ensuite ; rang non suisse |
| DX.2 Lymphadénite | 117 000 | 33 % | titre divergent ; IDSA ; co-amoxicilline non relue |
| DX.3 Mononucléose | 123 097 | 37 % | prednisone 40–60 mg non relue dans l’AIPS |
| DX.4 VIH | 130 465 | 36 % | titre divergent ; 318 cas et 3,5/100 000 confirmés |
| DX.5 Tuberculose | 108 077 | 29 % | **22 % faux** |
| DX.6 Lymphome | 135 182 | 32 % | doses de R-CHOP sans extrait AIPS |
| DX.7 Métastase | 119 623 | 33 % | titre divergent ; NICE ; platine sans AIPS |
| DX.8 Lipome | 90 671 | 28 % | fichier le plus court ; lidocaïne non relue ; IRM hors sujet |
| DX.9 Sarcome | 92 266 | 28 % | anthracycline non relue ; IRM hors sujet répétée |
| DX.10 Nodule thyroïdien | 146 765 | 38 % | NHS ; taux unique 9/100 000 qui masque 4,9 et 12,0 |

Moyenne B = (41+33+37+36+29+32+33+28+28+38) / 10 = **33,5 %**, arrondie à **34 %**.

## Trois critiques

### 1. Cohérence des noms et gravité invisible

Le prompt V0 classe une seule divergence de nom comme critique. Trois titres Phase B ne recopiaient pas la Phase A :

- DX.2 : « Lymphadénite bactérienne et adénite suppurée » contre « Lymphadénite bactérienne »
- DX.4 : « Infection par le VIH révélée par des adénopathies » contre « VIH révélé par adénopathies »
- DX.7 : « Métastase ganglionnaire d’un carcinome » contre « Métastase ganglionnaire de carcinome »

Aucun 🚩 et aucun rang E dans les onze fichiers hérités. Le sarcome (DX.9), le lymphome (DX.6) et la métastase (DX.7) n’étaient pas en tête d’algorithme. L’ordre 1→10 n’est pas une prévalence suisse : les incidences de cancer, les 318 VIH et les 432 tuberculoses ne classent pas les motifs de consultation. Le lipome et le nodule thyroïdien sont numérotés après des maladies plus rares sans que cette place soit sourcée. Les numéros n’ont pas été réinventés.

### 2. Épidémiologie fausse de la tuberculose

Extrait hérité, DX.5, point 2 : « En 2024, 22 % des cas étaient purement extrapulmonaires, la forme ganglionnaire étant la plus fréquente d’entre elles. »

Bulletin OFSP 2025 lu le 25.10.2026, tableau 1 : 2024, 18 cas extrapulmonaires exclusifs sur 432 (calcul dérivé 4,2 %) ; 2025, 32 sur 544 (calcul dérivé 5,9 %). Le bulletin écrit qu’en 2025, 268 cas étaient exclusivement pulmonaires, 238 mixtes, et que 94 % des personnes malades ont été touchées aux poumons. La part ganglionnaire n’y figure pas. Les totaux 432, 4,8/100 000, 544 et 6,0/100 000, ainsi que la moyenne européenne 8,4/100 000 en 2024, sont eux corrects.

### 3. Doses hors AIPS et fenêtres d’un autre organe

Les onze fichiers avertissent que des posologies sont « hors AIPS ». Ce n’est pas une autorisation de les enseigner. Non relus le 25.10.2026, donc non confirmés : co-amoxicilline 2,2 g × 3, prednisone 40–60 mg, R-CHOP (rituximab 375 mg/m² et le reste), cisplatine, cétuximab, pembrolizumab, doxorubicine 75 mg/m², antituberculeux, lévothyroxine, carbimazole, lidocaïne. Le numéro 47503 ouvre une notice patient italienne de Dafalgan effervescent, pas l’ensemble des spécialités du lot. Seul l’adulte de plus de 40 kg a été relu : 500 à 1 000 mg, intervalle 4 à 8 heures, maximum 4 g par 24 heures (notice 47503 et information allemande 56318). L’adaptation rénale n’était pas dans cet extrait.

La fenêtre IRM répétait, jusque dans le sarcome et le lipome, trois lignes d’un autre chapitre : « Adénome hypophysaire », « Muscles oculomoteurs épaissis en hypersignal STIR », « Masse surrénalienne en hypersignal T2 ». Dix occurrences dans DX.8 et dix dans DX.9.

## Ce qui a été vérifié et qui tient

- VIH 2024 : 318 cas, 3,5/100 000 ; 357 cas en 2023 ; cascade lue 93 % / 98 % / 96 %.
- Cancers, moyennes annuelles 2018-2022 (Krebsliga, novembre 2025) : LNH 1 700, Hodgkin 290, thyroïde 850, sarcome 340, bouche/pharynx 1 200, larynx 260.
- Thyroïde : 4,9/100 000 chez l’homme et 12,0/100 000 chez la femme (monitoring OFS).

## Corrections écrites (non réauditées)

Fichiers séparés dans ce dossier. Poids **fichier** après correction, tous entre 150 et 200 Ko (kilo-octet = 1 000 octets) :

| Fichier | Octets | Ko | SHA-256 |
|---|---|---|---|
| LOT_002_Phase_A_V0_SSP_et_10DD.html | 186 588 | 187 | `6e15b61da29a26dd304f5cb708a2d924b8e0c5a09ae2be9525a4f0142724eb5e` |
| Partie_1 DX.1 | 171 326 | 171 | `78b3d91b49a65683edbcb88450c055b91e24f08edbbb93d128a13d05ebecb9b7` |
| Partie_2 DX.2 | 158 540 | 159 | `6ed133d6ce449f868fdfdcf06081b57c4b0aa03df41b8a1f7c690b7fb3ec6b0b` |
| Partie_3 DX.3 | 164 774 | 165 | `49fc0a03764c076f3d44d6bcf569077a9ce508887c650b7461cb96ef2ab79233` |
| Partie_4 DX.4 | 173 748 | 174 | `9bebe0af163eda1a458d8bce5d6ce96e79d48f8bb0e4b752e79f1aa9ad090cd9` |
| Partie_5 DX.5 | 161 732 | 162 | `9b78d6f16a034a9c842373ddb9e72ad591c1d0845cb85c8df6262adbff14ca02` |
| Partie_6 DX.6 | 177 778 | 178 | `6bb23f62c3be6f57bd28156eb298f7a5d2ef84b9bcf1a76ea8e78c12e4db2e9d` |
| Partie_7 DX.7 | 161 473 | 161 | `71089b2af3d77c7821d91d5699df7f92a49d3ffb856874207ddc6a76d4aa769c` |
| Partie_8 DX.8 | 168 479 | 168 | `7d74f470f1af47d3d52dbb244f83c32936b9588a49658c42246b0ce3552b66ef` |
| Partie_9 DX.9 | 169 689 | 170 | `fb458621b34e1471ad69fb96afed0a3d5e1b85d1deaadbb972044f57c3462ed8` |
| Partie_10 DX.10 | 186 194 | 186 | `9092705c0970fb0edffc861b5508d809cc37bfa887e3ff8fb27cf3da62e48c91` |

Le texte hors balises reste entre environ 98 et 123 Ko. Le critère « 150–200 Ko de contenu » n’est donc pas atteint si l’on retire le balisage. Les situations ajoutées partagent un cadre de sécurité ; elles ne remplacent pas une monographie relue par un second auditeur. Des lignes héritées dépassent 3 000 caractères.

## Prêt-dépôt

**Non.** Score A 39 %, score B 34 %, critiques présentes sur le matériau audité, liste non gelée, doses encore « À vérifier (AIPS) », pas de second audit des fichiers corrigés, pas de Drive.
