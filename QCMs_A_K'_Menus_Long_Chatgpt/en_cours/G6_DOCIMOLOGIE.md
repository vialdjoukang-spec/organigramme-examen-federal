# G6 · Contrôle docimologique des 200 questions

**Fièvre, frissons, hyperthermie**, 17 novembre 2026. Les 180 items publiés dans le HTML d’empreinte `dd2f7859d24e8dca9bf23ab6cb2faad1ce63fb2c` ont été complétés par les 20 derniers manuscrits du lot 062. Les 200 identifiants sont uniques. Le tableau compare cet instantané avec la même banque après application du correctif `G6_OPTIONS_DOCIMOLOGIE.json` (blob `e78476f3936924cac7e4a8b1903a33d9eb5bc8e9`).

## Longueur des réponses de type A

La banque compte 120 questions A, 40 K′ et 40 menus longs. Chaque A comporte quatre propositions et une clé, chaque K′ quatre assertions. La stratégie simulée choisit la réponse de longueur maximale et répartit son choix uniformément en cas d’égalité. Une stratégie équiprobable donnerait 30 bonnes réponses sur 120.

| Mesure sur les 120 A | Avant | Après |
|---|---:|---:|
| Clé seule la plus longue (caractères) | 28 | 25 |
| Clé seule la plus courte (caractères) | 37 | 38 |
| Clé parmi les plus longues ex æquo (caractères) | 6 | 6 |
| Bonnes réponses attendues en choisissant le libellé le plus long (caractères) | 30,25 | 27,25 |
| Même stratégie en mots | 24,17 | 22,33 |
| Clé dépassant chaque distracteur d’au moins 40 % et quatre caractères | G6-014, G6-054, G6-063 | Aucune |

Le seuil de 40 % sert à sélectionner des items à examiner ; les longueurs se mesurent après suppression des espaces externes, en points de code Unicode ou en groupes séparés par des espaces.

## Nombre de propositions vraies en K′

| Vérités par question | 0 | 1 | 2 | 3 | 4 |
|---|---:|---:|---:|---:|---:|
| Avant | 1 | 3 | 18 | 17 | 1 |
| Après | 1 | 5 | 16 | 16 | 2 |

Les K′ totalisent 94 assertions vraies sur 160 avant correction et 93 après. Marquer toutes les propositions comme vraies réussirait intégralement 2 K′ sur 40. Les numéros à changement de vérité sont G6-039, G6-133, G6-143. Le mélange des positions à l’affichage préserve ces proportions et peut produire des répétitions.

## Marqueurs dans les propositions visibles

Repérage insensible à la casse de « toujours », « systématiqu… », « suffit/suffisent », « exclut/exclure », « écarte/écarter », « obligatoirement », « à lui seul », « à elle seule », « uniquement » et « exclusivement ». Une proposition est comptée une fois, même si elle contient plusieurs marqueurs. Les justifications révélées après réponse sont exclues.

| Format | Vraies avant | Fausses avant | Vraies après | Fausses après |
|---|---:|---:|---:|---:|
| A | 0 | 12 | 0 | 0 |
| K′ | 1 | 11 | 2 | 3 |

Le correctif concerne 22 questions ; les formulations restantes sont relues dans leur contexte clinique. Les 22 corrections et leurs trois changements de vecteur de vérité ont été contre-résolus par un second agent IA ; manifeste indépendant `b99709416158211975702865333fc7e1960307f4`. Les données ne proviennent pas de passations auprès de candidats. Difficulté, discrimination et fidélité psychométrique restent à mesurer.

## Reproduction

Extraire les questions G6 du bloc JSON `donnees` du HTML. Compléter uniquement les numéros absents par leur manuscrit. Vérifier chaque identifiant, format et clé ; appliquer les options par identifiant, puis recompter longueurs, marqueurs et combinaisons K′. Le mélange d’affichage n’entre pas dans le calcul des longueurs.
