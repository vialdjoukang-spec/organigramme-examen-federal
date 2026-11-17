# Contrôle docimologique de G10 · Douleurs de tous types

Les 40 tranches des lots 093 à 102 couvrent G10-001 à G10-200. Les 120 questions A comportent 1 questions à 3 options et 119 questions à 4 options. Les 40 K′ ont quatre assertions. Les 40 menus longs proposent entre 25 et 26 entrées.

Le script `docimologie.mjs` du dépôt a été exécuté avec Node sur deux copies des données originales des manuscrits. La première contient les textes et les vecteurs initiaux. La seconde applique successivement les deux manifestes validés contre les décisions et les textes d’origine. Les 48 identifiants affectés comprennent dix K′ dont le vecteur de correction évolue et dix-huit A dont la clé a été raccourcie. Les vingt-cinq reformulations lexicales réparties sur vingt-deux questions conservent leur valeur de vérité.

| Indicateur | Avant | Après |
|---|---:|---:|
| Clé A strictement la plus longue en caractères | 51/120 | 35/120 |
| Clé A de longueur maximale ex æquo | 2 | 3 |
| Clé A dépassant 1,6 fois la longueur du plus long distracteur | 1 (G10-129, rapport 1,78) | 0 |
| Clé A strictement la plus longue en mots | 35 | 22 |
| K′ comptant zéro affirmation vraie | 0 | 3 |
| K′ comptant une affirmation vraie | 4 | 6 |
| K′ comptant deux affirmations vraies | 21 | 17 |
| K′ comptant trois affirmations vraies | 15 | 10 |
| K′ comptant quatre affirmations vraies | 0 | 4 |
| Options A avec marqueur de forme, fausses / vraies | 13 / 4 | 0 / 4 |
| Assertions K′ avec marqueur de forme, fausses / vraies | 13 / 1 | 1 / 1 |

Les longueurs en caractères sont comptées en points de code, après suppression des espaces périphériques. Les mots sont délimités par un ou plusieurs espaces. Le comptage lexical compte chaque proposition une fois, ignore la casse et respecte les caractères accentués. Il recherche « toujours », les formes commençant par « systématiqu », « suffit/suffisent », « exclut/exclure », « écarte/écarter », « obligatoirement », « à lui seul », « à elle seule », « uniquement » et « exclusivement ». Après correction, un de ces termes subsiste en G10-043, 084, 098, 103, 118 et 192.

Le tirage de session applique Fisher–Yates avec un entier aléatoire uniforme issu de `crypto.getRandomValues` et d’un rejet des valeurs hors intervalle divisible. L’ordre des options pour une question reste stable lors de la correction. Une position de réponse peut se répéter par hasard. Les fréquences des nombres d’assertions vraies sont des propriétés du contenu. L’analyse ne mesure ni la difficulté constatée chez des candidats ni la discrimination empirique des distracteurs.

## Versions

- `G10_OPTIONS_DOCIMOLOGIE.json`, blob `a0753ca144a43cf99d7b7fdea2e73c1d8e4ae45f`. Contrôler la concordance de la décision avant d’appliquer les options, la réponse et les justifications. G10-182 a été retirée du manifeste après remplacement de l’ancienne question.
- `G10_INDICES_LEXICAUX.json`, blob `cbcc36b7a07a2db58da1cff4f7d967038107b2d7`. Appliquer ensuite chaque édition à la position indiquée en contrôlant le texte précédent et sa valeur de vérité.
- La contrelecture documentaire indépendante par IA est consignée séparément dans `G10_OPTIONS_CONTRE_AUDIT.json`. L’intégrateur vérifie ces mesures sur la banque HTML après les deux corrections.

### Empreintes des manuscrits mesurés

| Tranche | SHA Git |
|---|---|
| 093-G10-001.json | `6177dc03128edf70ef8f1ec204f5a5238231974e` |
| 093-G10-006.json | `ba63b25701369f9d0683f8f681e80dd4060b7b16` |
| 093-G10-011.json | `b7272a106fcf1828829ea07b47c2abee96ee7f92` |
| 093-G10-016.json | `45d2356f560c7295c26d26d79545819cb50adfeb` |
| 094-G10-021.json | `0412a60453459d84fdf5c0a82eaf51595ba80090` |
| 094-G10-026.json | `cc0f3d20b9ae459a9a7d047a3883cf246754c272` |
| 094-G10-031.json | `cd71571678541522e88f7f445d22858bb27fbe8c` |
| 094-G10-036.json | `a1b9c555ddc94be668a42ddf0096a5903d376b16` |
| 095-G10-041.json | `0f59124a94cc990779126733e31489b440206b5a` |
| 095-G10-046.json | `c43f6c00dcba31f55a1848a68adc3bc37234880b` |
| 095-G10-051.json | `ea479f27f8e4b6274993a77de50e747b484982d3` |
| 095-G10-056.json | `3ca94425518f088bdad2e0c6e876a80cb5b08224` |
| 096-G10-061.json | `751af1ef08f11e7b426b40e065ea8a561df0f7f4` |
| 096-G10-066.json | `e282232cd4908fec2bafa247e5bb1b447f633780` |
| 096-G10-071.json | `4e6056519b7073502593b807484be6eb771c4500` |
| 096-G10-076.json | `5448278a573e74c65362aec956316d912c2d176b` |
| 097-G10-081.json | `a7029f50aa059d7535161ba9cc3b0d37667e14cc` |
| 097-G10-086.json | `5d4ca6e40a65fb256394bf8739e59d5f62e247a9` |
| 097-G10-091.json | `268a7a57b35f67fd16ab8a7f98a0bc5b21546472` |
| 097-G10-096.json | `3c2c821d4932423085e3052fbd5c68fa4f3c612b` |
| 098-G10-101.json | `661f24c1b977e1b53bb69a017c595e5af3bd8e51` |
| 098-G10-106.json | `a5d830c006e8b3ddcb6ccd467da038100d032226` |
| 098-G10-111.json | `582d55e29ac94a1caf15361bec1dfdda99a74821` |
| 098-G10-116.json | `3eb2bc11db0597e9b0115f9d3af62f86ba60eafe` |
| 099-G10-121.json | `57e62558a3fdcc512e07187183878d6bfe957f39` |
| 099-G10-126.json | `5a1b00f60715bc7c75aa89546748f8ad469aa031` |
| 099-G10-131.json | `ac6499c97215c20555b1e25868de05ae3db40b53` |
| 099-G10-136.json | `ff60d3d1284ef2af426095ed79bc872b6cca1a04` |
| 100-G10-141.json | `835b80505bc99986c5e144e1676b8a1971637b20` |
| 100-G10-146.json | `b4b706da732718da389cbada1e935127afec0bdd` |
| 100-G10-151.json | `9407fc0691eac2928517d38742db17cc48c483db` |
| 100-G10-156.json | `5e7ba963c2f5744424d6943cf491f9f44cb81097` |
| 101-G10-161.json | `1727899636fc3dfe1ca4973f8c2a3767119972c8` |
| 101-G10-166.json | `02ac7ca6c983252c21a81f2727e5cba97cafe6a1` |
| 101-G10-171.json | `c45bd0b039f15a281b1ea4e4c405e7b94bfa41b9` |
| 101-G10-176.json | `40e27387bad00c40246975182ea289f5a7aa2ab8` |
| 102-G10-181.json | `c201e087f02666e501b95d07db44cf974e2e9680` |
| 102-G10-186.json | `665ba06a87bbc15514daaf353e122a8f9f5cad90` |
| 102-G10-191.json | `f1942ac8f07ba5b518a746a1ff3ff15d7e81b75d` |
| 102-G10-196.json | `bb71540c307ddd535761a1069a19205ec14386a5` |
