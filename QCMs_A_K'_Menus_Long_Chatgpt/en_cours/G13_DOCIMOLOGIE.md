# G13 · Contrôle docimologique de « Décès non naturel »

Les lots 123 à 132 comptent 200 questions. La distribution comprend 120 questions A (90 à 4, 30 à 5 propositions), 40 K′ à quatre assertions et 40 menus longs (30 à 25, 10 à 26 entrées).

La mesure compare les 40 manuscrits sources avec la banque après remplacement intégral de la Q045 et application successive des deux manifestes. Le premier révise 26 questions A et les assertions de 18 K′. Le second reformule 76 propositions dans 53 questions en conservant leur valeur de vérité. Les deux manifestes portent au total sur 77 questions distinctes.

| Indicateur | Manuscrits | Après remplacement et manifestes |
|---|---:|---:|
| Clé A strictement la plus longue en caractères | 53/120 | 27/120 |
| Clé A de longueur maximale ex æquo | 4 | 5 |
| Clé A strictement la plus courte en caractères | 25 | 34 |
| Clé A dépassant de plus de 60 % le plus long distracteur | 2 | 0 |
| Clé A strictement la plus longue en mots | 37 | 20 |
| K′ avec 0 assertion vraie | 0 | 2 |
| K′ avec 1 assertion vraie | 3 | 8 |
| K′ avec 2 assertions vraies | 32 | 14 |
| K′ avec 3 assertions vraies | 3 | 12 |
| K′ avec 4 assertions vraies | 2 | 4 |
| Propositions A avec marqueur lexical, fausses / vraies | 24 / 2 | 0 / 1 |
| Assertions K′ avec marqueur lexical, fausses / vraies | 15 / 0 | 0 / 0 |

Le script `docimologie.mjs` mesure les longueurs après retrait des espaces périphériques et classe les K′ selon leur nombre de vraies. Le contrôle complémentaire compte les mots séparés par des espaces. Il recherche dans le texte proposé au candidat « toujours », les mots commençant par « systématiqu », « suffit », « suffisent », « exclut », « exclure », « écarte », « écarter », « obligatoirement », « à lui seul », « à elle seule », « uniquement » et « exclusivement ». Une proposition contenant plusieurs marqueurs compte une seule fois.

La banque permute les positions par Fisher–Yates avec tirage uniforme par rejet à partir de `crypto.getRandomValues`. L’ordre présenté au candidat est conservé dans le corrigé. Le tirage admet les répétitions fortuites. La difficulté, la fidélité et la discrimination psychométriques nécessitent des données de passation.

Le contrôle distinct des menus a révisé G13-013 et G13-153. Leurs listes conservent le même nombre de réponses et la même clé. L’erratum de G13-055 corrige une référence juridique sans modifier ses propositions.

## Empreintes contrôlées

- Remplacement clinique de G13-045, blob `e3867aaeaf1de4daf91337e7e69cf1669f5e7a6b`, contre-audit `0cdc53135df90d7323c74e85d220c60af07ab566`.
- `G13_OPTIONS_DOCIMOLOGIE.json`, blob `2376bed3b6c1808d4e100b14b8698e06129fdc5b`.
- `G13_INDICES_LEXICAUX.json`, blob `fb21cc4adc4b77e181b3091678c6929bae4016d5`.
- Contre-audit indépendant par IA consigné dans `G13_OPTIONS_CONTRE_AUDIT.json`, blob `8d6973981aec9e4d0550fb2e2bcbd95c1846644c`.

| Tranche | SHA Git du manuscrit |
|---|---|
| 123-G13-001.json | `b52fb074b9a8f8fdac4a89aa0ff66e49f3c55b74` |
| 123-G13-006.json | `e7887732d4f845d06ce27c064c560992a6c35591` |
| 123-G13-011.json | `3ab4e2b9d8a439ecf73146a3d24958a3595e8671` |
| 123-G13-016.json | `bef20e199accea69679e39390107e3b6b90c9f77` |
| 124-G13-021.json | `8bf1f114c33a6d031d56671446f17f1d550ff91b` |
| 124-G13-026.json | `4efe749523df44b540712490395cf5a5fe0b05da` |
| 124-G13-031.json | `7bcd4392579a86c9ac1104f6a56052c62e7b4169` |
| 124-G13-036.json | `9730a1f429f1bb4bdac2d6bc42527dfec3200676` |
| 125-G13-041.json | `5c2371d9df193ac0673cdef47ebbcca76a23036a` |
| 125-G13-046.json | `89dc483d90711c0867253c60c525b4eeac4d0c5a` |
| 125-G13-051.json | `156601dbad1803879e6074a79ab4eee062706f83` |
| 125-G13-056.json | `1e8db3a19e9d7fa5223cbddb97613ba82d2b873b` |
| 126-G13-061.json | `9802025df4bcd0904850d93e9126f9056bab4486` |
| 126-G13-066.json | `a2a6c5de0f433e255e37f7e52c9809fa346a6483` |
| 126-G13-071.json | `4133544e5baf6ba63d6abe34670087161e56b559` |
| 126-G13-076.json | `22c9b1c495fb4051a4dc2a2dc4dad65f08197527` |
| 127-G13-081.json | `e3abccaa61a0eccfe483070f410038f6ff5b65f4` |
| 127-G13-086.json | `c1126843f895d8545a2cba986aeed78a7ca00ab0` |
| 127-G13-091.json | `728e4c8ee6826d484f8d6ae8b79e539a900dec7c` |
| 127-G13-096.json | `140078759141c80f2efa2c0503f7ba52bb7ab692` |
| 128-G13-101.json | `9d6693b914b74c21f4d78b6af82dcd0ef664b21c` |
| 128-G13-106.json | `7f3ea517cfb7c11c582c3fd8e0e135ba6e47f055` |
| 128-G13-111.json | `35d46b82b9601e073c51486e5f2a0ca4ef84df02` |
| 128-G13-116.json | `30cc5296f2a6b4baacdc27386efc98e51f14310d` |
| 129-G13-121.json | `724b46f912f41e42cb1863394e7dc097ba36f8a0` |
| 129-G13-126.json | `a6e6d449be9b2988bd73cd616b4f6eeb95199cdd` |
| 129-G13-131.json | `60c7ac1344c7836a2eb7720d72c861bfdc4dccd3` |
| 129-G13-136.json | `8503b2192de93c8b70c7cc8c4cf47612213419fa` |
| 130-G13-141.json | `34c3ec3a0eaa4e3cfa18911ed103fc13b680d3d9` |
| 130-G13-146.json | `300d99ac2b93a3ffea60dded2dfc4cc42f681520` |
| 130-G13-151.json | `7e482cc922c0474ce04ea1e812a6eb85b54c32d1` |
| 130-G13-156.json | `ad9610de80189e1ef937dc8d91d407aca76e221d` |
| 131-G13-161.json | `daae57734179085783ea816737088d452fbd1863` |
| 131-G13-166.json | `c4ef8399d8e7904d9528f789c1dbc82cf5d36ca8` |
| 131-G13-171.json | `e40c1bea6e7ccad40ddf5f794e4709b4b9fa14ee` |
| 131-G13-176.json | `75e42a645bb9979a6c1b6380e94c827f80143cc9` |
| 132-G13-181.json | `166eae0621f167245ba9b8572095b2d4e84bf853` |
| 132-G13-186.json | `106b2a8fa0e381e9344ab74da8b19424f581f1cc` |
| 132-G13-191.json | `f3c6f391f1d316ecf4ff5a94c7d84fac8d3c1f55` |
| 132-G13-196.json | `f9d0c08e35bd7dc4ae92c79462d07d8b18aae455` |
