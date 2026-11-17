# G5 · Contrôle docimologique des 200 questions

**Sensation de maladie**, 17 novembre 2026. La mesure réunit les 180 items publiés dans le HTML d’empreinte `dc916b434feae67211e51c976af297bf38acdbb1` et les 20 manuscrits du lot 052. Les identifiants G5-001 à G5-200 sont présents une fois chacun. Les éditeurs peuvent reproduire la mesure après toute retouche clinique du dernier lot.

## Questions A

Sur 200 questions, 120 sont de type A, 40 de type K′ et 40 des menus longs. Chacune des 120 questions A présente quatre propositions et une seule clé. Le tableau compare l’instantané initial avec le même instantané après application en mémoire du correctif `G5_OPTIONS_DOCIMOLOGIE.json` (24 items, blob `c8eb4fcbc9c0ecd1a4243a970a0a78922ac7e789`).

| Indicateur sur les 120 A | Avant | Après |
|---|---:|---:|
| Clé seule la plus longue, en caractères | 27 | 28 |
| Clé seule la plus courte, en caractères | 36 | 35 |
| Clé parmi les plus longues ex æquo | 2 | 2 |
| Choix de la proposition la plus longue, bonnes réponses en espérance (caractères) | 27,75 | 28,75 |
| Même stratégie avec la longueur en mots | 27,00 | 26,83 |
| Clé dépassant chaque distracteur de 40 % et d’au moins quatre caractères | 0 | 0 |

Le hasard équiprobable donnerait 30 réponses justes en moyenne sur 120. Les libellés sont mesurés après retrait des espaces externes, en points de code Unicode ou en groupes séparés par des espaces. En cas d’ex æquo, la stratégie simulée choisit uniformément parmi les propositions à la longueur maximale.

## Profils des questions K′

| Nombre de propositions vraies | 0 | 1 | 2 | 3 | 4 |
|---|---:|---:|---:|---:|---:|
| Nombre de questions | 1 | 3 | 16 | 15 | 5 |

Les 40 K′ présentent chacune quatre assertions. Le correctif conserve chaque valeur de vérité. Sur les 160 assertions, 100 sont vraies (62,5 %). Une stratégie consistant à tout marquer vrai réussirait cinq questions entières sur 40. La permutation des propositions à l’affichage change leurs positions et conserve cette asymétrie de composition. Ces effectifs décrivent cette banque pédagogique ; la distribution fédérale des combinaisons K′ n’a pas été établie.

## Indices lexicaux

Recherche insensible à la casse dans les seules propositions visibles. Le filtre couvre « toujours », « systématiqu… », « suffit/suffisent », « exclut/exclure », « écarte/écarter », « obligatoirement », « à lui seul », « à elle seule », « uniquement » et « exclusivement ». Une proposition est comptée une seule fois, même si plusieurs termes concordent. Les commentaires révélés après réponse ne sont pas pris en compte.

| Format | Vraies avant | Fausses avant | Vraies après | Fausses après |
|---|---:|---:|---:|---:|
| A | 0 | 14 | 0 | 0 |
| K′ | 1 | 13 | 1 | 2 |

Les deux assertions fausses restantes appartiennent à G5-192. La formulation « suffit toujours à exclure » a été transmise à l’auditeur du lot 052 pour révision. La proposition vraie restante concerne la sensibilité insuffisante d’une coloration de Gram dans G5-173. Le correctif de libellés a été contre-résolu par un second agent IA ; le manifeste correspondant est `19a10498f1cb5f27b8c51128a1baeb2aa7cdbded`. Aucune réponse réelle de candidat n’a été exploitée. Une mesure de difficulté et de discrimination exige des données de passation.

## Reproduction

1. Extraire les G5 du script JSON `donnees` dans le HTML et compléter les numéros non publiés avec leur manuscrit. Préférer la version publiée pour les doublons d’identifiant.
2. Trier les 200 identifiants, vérifier formats et nombres de clés. Appliquer le correctif par identifiant après vérification de chaque vecteur booléen.
3. Compter les longueurs et appliquer le filtre décrit ci-dessus aux assertions visibles, avant puis après substitution. Répéter au scellement si les questions sources ont évolué.
