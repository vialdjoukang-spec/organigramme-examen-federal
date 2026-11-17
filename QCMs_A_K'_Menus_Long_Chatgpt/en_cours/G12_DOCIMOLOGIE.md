# G12 · Contrôle docimologique de « Œdème diffus ou localisé »

Les lots 113 à 122 comptent 200 questions. Parmi les 120 questions à meilleure réponse unique, 90 présentent quatre choix et 30 en présentent cinq. Les 40 K′ contiennent quatre assertions. Trente menus longs ont 25 entrées et dix en ont 26.

La mesure compare les 40 manuscrits sources avec les mêmes questions après application successive des deux manifestes. Le premier révise 30 clés A et 18 vecteurs K′. Le second reformule 70 propositions dans 46 questions en conservant leur valeur de vérité. Les deux manifestes portent au total sur 68 questions distinctes.

| Indicateur | Manuscrits | Après les deux manifestes |
|---|---:|---:|
| Clé A strictement la plus longue en caractères | 48/120 | 26/120 |
| Clé A de longueur maximale ex æquo | 6 | 10 |
| Clé A strictement la plus courte en caractères | 30 | 32 |
| Clé A dépassant de plus de 60 % le plus long distracteur | 0 | 0 |
| Clé A strictement la plus longue en mots | 31 | 24 |
| K′ avec 0 assertion vraie | 1 | 2 |
| K′ avec 1 assertion vraie | 3 | 9 |
| K′ avec 2 assertions vraies | 30 | 12 |
| K′ avec 3 assertions vraies | 4 | 13 |
| K′ avec 4 assertions vraies | 2 | 4 |
| Propositions A avec marqueur lexical, fausses / vraies | 9 / 0 | 0 / 0 |
| Assertions K′ avec marqueur lexical, fausses / vraies | 12 / 0 | 0 / 0 |

Le script `docimologie.mjs` mesure les longueurs après retrait des espaces périphériques et classe les K′ selon leur nombre de vraies. Le contrôle complémentaire compte les mots séparés par des espaces. Il recherche dans le texte proposé au candidat « toujours », les mots commençant par « systématiqu », « suffit », « suffisent », « exclut », « exclure », « écarte », « écarter », « obligatoirement », « à lui seul », « à elle seule », « uniquement » et « exclusivement ». Une proposition contenant plusieurs marqueurs compte une seule fois.

La banque permute les positions par Fisher–Yates avec tirage uniforme par rejet à partir de `crypto.getRandomValues`. L’ordre présenté au candidat est conservé dans le corrigé. Le tirage admet les répétitions fortuites. La difficulté, la fidélité et la discrimination psychométriques nécessitent des données de passation.

## Empreintes contrôlées

- `G12_OPTIONS_DOCIMOLOGIE.json`, blob `91a7e659e8cf89f7e78eb02e0edff03897ffcc74`.
- `G12_INDICES_LEXICAUX.json`, blob `97e506149bf89f39b33def780c8ca385a6eceb7d`.
- Contre-audit indépendant par IA consigné dans `G12_OPTIONS_CONTRE_AUDIT.json`, blob `1605c573b00bc3424c837f1f44a2222b20a324fa`.

| Tranche | SHA Git du manuscrit |
|---|---|
| 113-G12-001.json | `a3b990771aac27921f2a2366583485b4cbc5596b` |
| 113-G12-006.json | `7b3099077dbb3bd2299f81908f9df8e581269251` |
| 113-G12-011.json | `5b170a43b7d68d56d1a172072a965215eb6c9ab5` |
| 113-G12-016.json | `c2e8c6d8c8d411d266d49262bc6a4d3827ec5177` |
| 114-G12-021.json | `b37f402606c1d62bc2acfc9c80ab43575ffc83e6` |
| 114-G12-026.json | `2368b1ac88340e0f471c40e620e8fb4215f24b80` |
| 114-G12-031.json | `e78e26084a1d1ab20274790e3df6e21111c0f7ca` |
| 114-G12-036.json | `9600e655dd70914b6c4aa5015be227ca80285dbf` |
| 115-G12-041.json | `4dec8854d03890828e10fd55f0ad53ce95623cb3` |
| 115-G12-046.json | `30d606a7b6c9a1a7e0d4c99f8c72881066783e44` |
| 115-G12-051.json | `8855842b59ac01a7306df8e98e53ad6e2bfd0ed3` |
| 115-G12-056.json | `46a3d4ca60bcb608e992cda2a1c0d883de9826d5` |
| 116-G12-061.json | `caabdcd60e563479952816d0dcd1b9a4adc47d17` |
| 116-G12-066.json | `a8da6362342b012c4127ecd7194c8059b6804a4f` |
| 116-G12-071.json | `5259bd38c2f1f9876c335fc3247c3df22b80b10e` |
| 116-G12-076.json | `ee781d0a678ef5efc580dba86ce6c1b97c693db1` |
| 117-G12-081.json | `e63ca1115945251865a3e12d7a00d9e8cb17d02f` |
| 117-G12-086.json | `955d9f79e5553e82dc4fc001d96c3620fb1f85f6` |
| 117-G12-091.json | `6f1c3d3a89df807b8f07bac2345766bd741f090e` |
| 117-G12-096.json | `c499a07a405048491d5ac6ad613543b840125ea7` |
| 118-G12-101.json | `0932292443e2ba23f1925322c26d5137b650ac20` |
| 118-G12-106.json | `5f7cd1138f61e216aaf7d2515020c9df80b2f3c7` |
| 118-G12-111.json | `e92ebe56794f1695b17ec2da1a4c6dc7330af1ba` |
| 118-G12-116.json | `45912a0f0b3e5342e4a9f35b8e326343e913e297` |
| 119-G12-121.json | `f7ee1670ae78c86c95ff761570a47b7d239d893d` |
| 119-G12-126.json | `aa2aff3f8fa076c9fcfd128fccf5670b4d606fc5` |
| 119-G12-131.json | `f1e2c3f6f9b381f3e0c24fbfd4951d2f5650fcf0` |
| 119-G12-136.json | `37fff7196e8446cf9fb1e92185a639f9ca5fcc75` |
| 120-G12-141.json | `ed5abb579f5e6bd333387d05db1c1145f310a9df` |
| 120-G12-146.json | `2e59c12c92039aa6729159df9f8faf220cf070a6` |
| 120-G12-151.json | `3f34022acf0b31e13b5a5dcb5ee0d3002d58c0b7` |
| 120-G12-156.json | `bba4bb98912a6513f6f76eb2b183440da7fc496d` |
| 121-G12-161.json | `017b1f9929f2a7960d284943cc0a4912e4a54f13` |
| 121-G12-166.json | `8c512d2d6443e3c873c2540d997f1cc455b1fe05` |
| 121-G12-171.json | `79bcd3c8f323b7d50cd68d4673165d1c078808ca` |
| 121-G12-176.json | `487005c3994840bcfdb2cbd7c5599ea95e1d8689` |
| 122-G12-181.json | `62252272b963d8ad908e148852aabb8aabf28a1d` |
| 122-G12-186.json | `3a42dadd4f85393a703df80334a949253c5a7043` |
| 122-G12-191.json | `6e0c057e6099f1ba66ea357c5f0a251dae923b71` |
| 122-G12-196.json | `398d7face4fae06b4bb014a48e3aa2a370c6aae0` |
