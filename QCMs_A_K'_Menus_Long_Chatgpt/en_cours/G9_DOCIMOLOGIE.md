# Contrôle docimologique de G9 · Prurit

Les 40 tranches des lots 083 à 092 fournissent 200 questions numérotées de G9-001 à G9-200, dont 120 A, 40 K′ et 40 menus longs. Parmi les A, 113 ont quatre options et sept en ont cinq. Chaque K′ comporte quatre affirmations. Les menus longs comprennent 25 à 27 termes.

Le script du dépôt `docimologie.mjs` a été exécuté avec Node sur les manuscrits, puis sur les mêmes questions après application des deux correctifs. Les options, identifiants et types ont été conservés dans les données d’entrée du script. Le premier correctif porte sur vingt items et le second sur vingt, avec deux identifiants communs (G9-127 et G9-136).

| Indicateur | Manuscrits | Après les deux correctifs |
|---|---:|---:|
| Clé A strictement la plus longue en caractères | 41/120 | 27/120 |
| Clé A de longueur maximale ex æquo | 8 | 9 |
| Clé A dépassant 1,6 fois le distracteur le plus long | 0 | 0 |
| Clé A strictement la plus longue en mots | 21/120 | 16/120 |
| K′ comportant 0 affirmation vraie | 0 | 2 |
| K′ comportant 1 affirmation vraie | 2 | 5 |
| K′ comportant 2 affirmations vraies | 20 | 14 |
| K′ comportant 3 affirmations vraies | 16 | 16 |
| K′ comportant 4 affirmations vraies | 2 | 3 |
| Options A contenant un marqueur, fausses / vraies | 17 / 1 | 4 / 1 |
| Assertions K′ contenant un marqueur, fausses / vraies | 13 / 0 | 3 / 0 |

Le script compte les points de code après retrait des espaces périphériques. Pour le contrôle complémentaire, un mot est délimité par un ou plusieurs espaces. Le comptage lexical est insensible à la casse, tient compte des lettres accentuées et compte chaque option une seule fois. Il porte sur « toujours », les formes commençant par « systématiqu », « suffit/suffisent », « exclut/exclure », « écarte/écarter », « obligatoirement », « à lui seul », « à elle seule », « uniquement » et « exclusivement ». Les marqueurs résiduels concernent G9-019, 052, 097, 110, 135 (deux options), 140 et 154.

La page d’examen permute les positions selon Fisher–Yates avec tirage cryptographique par rejet et conserve l’ordre attribué à une question pendant la session. Cela donne à chaque emplacement d’une question A la même probabilité d’afficher la clé. Les suites de réponses identiques restent possibles. Les nombres d’affirmations vraies ci-dessus sont observés sur les textes cliniques et ne sont pas générés aléatoirement à l’affichage. La difficulté, la discrimination et la qualité empirique des distracteurs demanderaient des réponses anonymisées de candidats.

## Versions mesurées

- Correctif des options `G9_OPTIONS_DOCIMOLOGIE.json`, blob `60a28a6e748199b7bbec5c72d3c076eb710cdbb3`. Les profils modifiés concernent G9-009, 028, 048, 088, 149 et 168.
- Correctif des indices lexicaux `G9_INDICES_LEXICAUX.json`, blob `8c3bdb47d0454c4920ec784633b97c44a84c2ba9`. Pour chaque édition, remplacer le texte et sa justification à la position indiquée après contrôle du texte initial et de la vérité.
- Contre-audit indépendant des deux correctifs à consigner dans `G9_OPTIONS_CONTRE_AUDIT.json`. L’application au HTML et l’exécution de `verifier.mjs` sur la banque publiée relèvent de l’intégration.

### Blobs des manuscrits utilisés pour les mesures

| Tranche | SHA Git |
|---|---|
| 083-G9-001.json | `d66a49ed3511f270549cd878d768609a74063724` |
| 083-G9-006.json | `b6cfcfd8683a1500b05b958092eda2efc08cdeec` |
| 083-G9-011.json | `538b836c9cf4d926999f8512589eca140bcb7322` |
| 083-G9-016.json | `a80ff26318842f33c17088d7438dca06cef804a9` |
| 084-G9-021.json | `0e7b59198335929a02d43f9115063026eac9c162` |
| 084-G9-026.json | `bcd20694f3c5e44f06f21435042fa556fecd0a48` |
| 084-G9-031.json | `5ada0312f6ad56d4cf5c1509488725098000d9b1` |
| 084-G9-036.json | `c5ff6576caf9b4c7570119d8cd9f0f39abebac99` |
| 085-G9-041.json | `85b2a90865072e0b5d5de13da7dd9a57aef11ee1` |
| 085-G9-046.json | `f6c69c223674ad6790c86757273c40779f4e8e95` |
| 085-G9-051.json | `b19a3db3ea6b67924bf8d4823a0b7e2765920b53` |
| 085-G9-056.json | `e461645167b26cb82aa6b2c7788c2b7afde3d39d` |
| 086-G9-061.json | `da38a5aad81fe8d79fdffbb16ab74400b1a2f602` |
| 086-G9-066.json | `7db68815bcf66c19534fc4e42807b6a0af418d5c` |
| 086-G9-071.json | `7b24f5291ff334a4636d244020700b2f34d6ec9d` |
| 086-G9-076.json | `1e98a777712889b8e62067a3a604d39fbfe164fe` |
| 087-G9-081.json | `54359ab2d779dbd051e62e940a9a87b0234b8f19` |
| 087-G9-086.json | `de078bf6285fde0638ee91fe658d5f401d92fa79` |
| 087-G9-091.json | `53b53f6f6c48a32dfc375a890bc6be672adfc82c` |
| 087-G9-096.json | `3c91bd2936b3fbd9f98a9625089a27a7dfe537aa` |
| 088-G9-101.json | `56b9d47a7a43b77a6584b3d46f2732209e7633e0` |
| 088-G9-106.json | `048d37de888d4a4c6455a310cbb7b28a18c4c337` |
| 088-G9-111.json | `ef82ba7d73ed2582392a0ca2451183db2dee3bef` |
| 088-G9-116.json | `370934966bc2721ee8765102d571bf36e7e4cc33` |
| 089-G9-121.json | `34c2d0854b74ed9b86ef86456186a58afb4eb589` |
| 089-G9-126.json | `f379c7c449e828b57ac1b73643d61b0158dc6c98` |
| 089-G9-131.json | `7d03634b858c32eb59b46cb5d1783fcf71a25925` |
| 089-G9-136.json | `178ba146c32c56defb5807ea0fd82bf2748a297a` |
| 090-G9-141.json | `b1d90facf4b8cba7ff5a116fab312af4830118ad` |
| 090-G9-146.json | `90db5840337d45affd94f2e14567f73fcddb37b7` |
| 090-G9-151.json | `e17d06b9ffd126c1934e12265e325826e138ddbf` |
| 090-G9-156.json | `cd0a84f200ffbe1138e78aa4c4ba76123a05c5af` |
| 091-G9-161.json | `fa40c16aba903ccaf2f0df8500bd4a83df20b862` |
| 091-G9-166.json | `5779651dd64a0b4d67fd718b6fd2289f1875d60f` |
| 091-G9-171.json | `9790f81bcb77fe93b49a70dc3b1f9bb798625a91` |
| 091-G9-176.json | `cd3927c253465b93a6e108cd84e5ea2b71fdc1c7` |
| 092-G9-181.json | `a5cee7f6b31994c175fa606f2a7c49f0f08d4bc5` |
| 092-G9-186.json | `aa496a842995d535e70aa49c9e9661c12dbfe0ff` |
| 092-G9-191.json | `7c5be11d9ced93d9dea184dd645052f3a64a9dd0` |
| 092-G9-196.json | `70ab1cc02820f9fa47d2d5a036f65a6d5a5b2a25` |
