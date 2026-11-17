# G4 · Contrôle docimologique des 200 questions

Banque francophone · Fatigue, lassitude. Contrôle du 17 novembre 2026 (UTC). Les 200 vignettes ont été prises en compte. Le point de départ compte 180 items lus dans le HTML et 20 lus dans les derniers manuscrits ; empreinte du HTML de référence : `500c85f9beaf2b949ebe70a90e6e7277bbc3e596`. Les mesures après modification résultent de l’application en mémoire du correctif `G4_OPTIONS_DOCIMOLOGIE.json` à ces mêmes items.

## Formats et propositions

120 questions A, 40 questions K′ et 40 menus longs. Chaque A contient quatre propositions et une clé. Chaque K′ contient quatre assertions. Les 27 ajustements portent sur des items existants. Vérification des 640 valeurs de vérité, identiques avant et après dans ce périmètre.

## Longueur des réponses A

Le calcul porte sur le libellé affiché, espaces externes retirés. La longueur en caractères compte les points de code Unicode, la longueur en mots sépare les groupes par les espaces. Lors d’un ex æquo à la longueur maximale, la stratégie simulée répartit son choix uniformément entre les options concernées. Une sélection indépendante du contenu donnerait en moyenne 30 réponses justes sur 120.

| Critère | Avant | Après |
|---|---:|---:|
| Clé seule la plus longue, en caractères | 32 | 33 |
| Clé seule la plus courte, en caractères | 33 | 34 |
| Clé à égalité en tête, en caractères | 4 | 4 |
| Espérance de bonnes réponses en choisissant le libellé le plus long, en caractères | 34 / 120 | 35 / 120 |
| Même stratégie, en mots | 35,83 / 120 | 33,58 / 120 |
| Clé dépassant la deuxième option de 40 % et d’au moins 4 caractères | G4-048, G4-200 | Aucune |

Le seuil de 40 % sert à choisir les libellés à examiner ; il ne représente pas une norme fédérale. Le mélange de l’ordre des propositions ne supprime pas un indice de longueur.

## Composition des K′

| Nombre d’assertions vraies | 0 | 1 | 2 | 3 | 4 |
|---|---:|---:|---:|---:|---:|
| Effectif sur 40 | 2 | 5 | 18 | 13 | 2 |

Le nombre de vraies varie de zéro à quatre. La distribution décrit des combinaisons cliniques choisies éditorialement. Avant affichage, la banque permute les options A et K′ par Fisher–Yates avec des indices tirés par `crypto.getRandomValues` et rejet des valeurs hors d’un multiple de la borne. Les positions source ne prédisent donc pas les positions affichées. Des répétitions sont possibles dans une suite aléatoire.

## Indices lexicaux

Filtre appliqué aux propositions affichées, sans tenir compte de la casse. Recherche des termes « toujours », « systématiqu… », « suffit », « exclut », « écarte », « obligatoirement », « à lui seul » et « à elle seule ». Une proposition comportant plusieurs marqueurs est comptée une seule fois. Les justificatifs révélés après réponse sont exclus.

| Format | Vraies avant | Fausses avant | Vraies après | Fausses après |
|---|---:|---:|---:|---:|
| A | 0 | 11 | 0 | 0 |
| K′ | 0 | 28 | 4 | 5 |

Les formulations conservées doivent se lire dans leur contexte clinique. Un seul mot peut encore identifier une réponse dans un petit échantillon ; le comptage ne constitue pas une étude psychométrique des candidats. Les corrigés, la plausibilité des distracteurs et l’absence de changement de décision ont fait l’objet d’une contre-lecture indépendante par un second agent IA ; une validation humaine indépendante n’est pas documentée.

## Pour reproduire la mesure

1. Charger les items G4 du bloc JSON `donnees` dans le HTML ; pour les numéros non encore intégrés, compléter depuis le sous-lot correspondant.
2. Trier par ID G4-001 à G4-200 et vérifier l’unicité. Comparer chaque vecteur booléen à celui du correctif avant de substituer les options par ID.
3. Pour les A, mesurer les quatre libellés et créditer la stratégie de 1/k si la clé figure parmi les k options les plus longues ; sinon créditer 0. Pour les K′, compter les valeurs vraies par vignette. Appliquer le filtre lexical aux textes visibles.

Ces proportions de formats et de profils sont celles de cette banque d’entraînement. Toute mesure de difficulté, de discrimination ou d’indice de fidélité nécessite des réponses réelles de candidats.
