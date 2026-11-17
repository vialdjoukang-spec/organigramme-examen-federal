# G11 · Contrôle docimologique des troubles du sommeil

Les lots 103 à 112 rassemblent 200 questions. Parmi les 120 questions A, 95 comportent quatre options et 25 en comportent cinq. Les 40 K′ ont quatre assertions. Les 40 menus longs contiennent 20 entrées pour six questions, 25 pour vingt-quatre et 26 pour dix.

La mesure utilise le script `docimologie.mjs` du dépôt avec Node. Sur le même ensemble de 40 manuscrits, la seconde exécution applique d’abord les options révisées, puis les reformulations lexicales sur leur texte d’origine et leur valeur de vérité. Les versions et les empreintes figurent ci-dessous. Le contrôle de contenu couvre 88 questions distinctes entre les deux manifestes. Parmi les 55 questions du premier manifeste, 32 A ont une clé révisée, 22 K′ changent de vecteur et une K′ conserve ses valeurs de vérité tout en remplaçant une assertion redondante. Le second manifeste modifie 60 propositions sur 41 questions.

| Mesure | Avant | Après les deux manifestes |
|---|---:|---:|
| Clé A strictement la plus longue en caractères | 59/120 | 28/120 |
| Clé A de longueur maximale ex æquo | 9 | 8 |
| Clé A dépassant de plus de 60 % le plus long distracteur | 0 | 0 |
| Clé A strictement la plus longue en mots | 42 | 15 |
| K′ comportant zéro vraie | 1 | 2 |
| K′ comportant une vraie | 1 | 10 |
| K′ comportant deux vraies | 32 | 12 |
| K′ comportant trois vraies | 5 | 13 |
| K′ comportant quatre vraies | 1 | 3 |
| Options A avec un marqueur lexical, fausses / vraies | 26 / 1 | 1 / 1 |
| Assertions K′ avec un marqueur lexical, fausses / vraies | 9 / 1 | 0 / 1 |

La longueur en caractères se compte en points de code après retrait des espaces périphériques. Le décompte de mots utilise les espaces comme séparateurs. Le contrôle lexical compte une proposition au plus une fois. Il repère « toujours », les mots commençant par « systématiqu », « suffit/suffisent », « exclut/exclure », « écarte/écarter », « obligatoirement », « à lui seul », « à elle seule », « uniquement » et « exclusivement ». Les trois emplois subsistants se trouvent en G11-132, G11-166 et G11-174.

La révision de G11-149 distingue la prévention de la compression nocturne d’un capteur de glucose du geste de mesure capillaire évalué en G1-179. La conduite de sécurité en cas de discordance reste expliquée. G11-144 et G11-159 modifient chacune une assertion après contrelecture du lot 110.

La banque permute les positions par Fisher–Yates et tirage uniforme par rejet avec `crypto.getRandomValues`. Le même ordre est conservé au corrigé. Le profil du nombre de vraies d’une K′ dépend de son contenu. Les répétitions fortuites d’une position restent possibles. Les indicateurs présentés portent sur la forme des propositions. La difficulté empirique et la discrimination psychométrique demandent des données de passation.

## Fichiers contrôlés

- `G11_OPTIONS_DOCIMOLOGIE.json`, blob `f09f9a5d6470d3c14bd8b9a589d725be627d4232`.
- `G11_INDICES_LEXICAUX.json`, blob `ce89d0fc60e79d7a2b3babc891a4b8cd5e568b2a`.
- Le contre-audit indépendant par IA est consigné dans `G11_OPTIONS_CONTRE_AUDIT.json` au commit `37ff33d909ce71e1a6ac2787499a83eef903a34f`. Le contrôle final du HTML publié appartient à l’intégration.

## Empreintes des manuscrits comparés

| Tranche | SHA Git |
|---|---|
| 103-G11-001.json | `22caae96e9b09a2bc29b141869371090c5de9dcb` |
| 103-G11-006.json | `a70f3098a7c6d2060682c38b98687ea68ba3087a` |
| 103-G11-011.json | `9ba14fc41d1fbc52cb69f3cabb563453599059d0` |
| 103-G11-016.json | `a71813c2d73acc7ba842e2f0340e0764fa6978ef` |
| 104-G11-021.json | `59cccab1e22a54d454f47ef4d67bfa0f69c5ac04` |
| 104-G11-026.json | `1509b870a8811014bbf000734530ffc79efd057e` |
| 104-G11-031.json | `d81299fb9d5b1758b0a165825c9669bf679dd0ec` |
| 104-G11-036.json | `31f756dcf7986e4845e3a7756c3905e3c320247a` |
| 105-G11-041.json | `a9e9ff4fb1b1383fe441b35c37b0835ae36fd5a1` |
| 105-G11-046.json | `8f6591362ad7e0808da5685294c441e888c59f2d` |
| 105-G11-051.json | `d3c4f326effd40b0a53ae8d33d6aafc61be9966d` |
| 105-G11-056.json | `c8ef477e08a77fc0c44cf1b43086ad95ac6c9769` |
| 106-G11-061.json | `3e3d1704bb1b8dece8dcebb29daf79b59b23dfae` |
| 106-G11-066.json | `ae14ed3875a72ba77670109b54d0066b03ecc9b4` |
| 106-G11-071.json | `b9d3196da9c90f336e2eeea2e1cdf7729cc4f1a9` |
| 106-G11-076.json | `08b43e7061e2ec5b7b2c6dbf72d0cb86c6393d9e` |
| 107-G11-081.json | `f99c63f4fb61a47a5ef4f11fbdf1ab2e3a93334f` |
| 107-G11-086.json | `4e057ece5723058adeb973bf19430e84c0f6acc3` |
| 107-G11-091.json | `20e18c592fbbdef0c6e37394e9408ced2b5951e0` |
| 107-G11-096.json | `3e2d0240cb70a7b0469e55fd7ea64b71b2b2aa73` |
| 108-G11-101.json | `01d854517107238643df47dc8964638b28100d56` |
| 108-G11-106.json | `82226f7d92085fbc0ac6543d4f344493e9583493` |
| 108-G11-111.json | `6142803d070967db03318fa91000af9f3f3c4eb7` |
| 108-G11-116.json | `3be26c6471ff54012389facbcf664a4a10d7fe90` |
| 109-G11-121.json | `8da7ae004c153886995250c503840139527daf06` |
| 109-G11-126.json | `efe809298914e05d7e8afd61549dacd39436154a` |
| 109-G11-131.json | `005c63d8675175674af12dfcbd4f9ca077367a9a` |
| 109-G11-136.json | `9a047583b8b63fa850528d6cbc23398fb6a2d8ef` |
| 110-G11-141.json | `ace1b6c5d1b238a5d8ba75ee8810acaa1be3fbf7` |
| 110-G11-146.json | `3e29d2d2d0481839b0cf8129d5e5d1345fc2b931` |
| 110-G11-151.json | `664fe67c5ca29030a17ec55af31b626140f93ea2` |
| 110-G11-156.json | `3765f023a73838b360dd416ee8625eca1689d84e` |
| 111-G11-161.json | `0ad2849b30e4fd8ecbb60739e18bedadddbcd283` |
| 111-G11-166.json | `94e58ff2a50fc45ab257be6ea7f3d36b72c6c95b` |
| 111-G11-171.json | `f2ff5fde0008f82ff7f190b4feea8d6f7ca3dedc` |
| 111-G11-176.json | `a232909ddf2988d29b1134496f9015618aee8c95` |
| 112-G11-181.json | `422fd8b1094a0a39fe6290ff9112e6f534a797d1` |
| 112-G11-186.json | `b61c81124b0ec752d63e9aa5c4637e47e0fe6106` |
| 112-G11-191.json | `a87d7b49e0f0af71714accc1ed20075c59d64155` |
| 112-G11-196.json | `6ca8fba1d3539f1f9850c2d41a69e2c8d956bca2` |
