# Vérification ciblée G1 — LOT_001, DX.1, point 10 (algo1)

Périmètre : seul le modèle JSON `<template class="algo-modele">` de `algo1` (lignes 462–968) a été lu. Je n'ai rien modifié dans le cours. Python était bloqué (approbation requise) : j'ai donc relu les 31 nœuds et les 53 liens à la main.

## 1. Liens de reprise exigés par G1

| Lien | Attendu (audit it8) | Trouvé | État |
|---|---|---|---|
| f4 (resucrage) | → qe8 | f4 → qe8 | Corrigé |
| f3 (hyperthyroïdie) | → q5 | f3 → q5 | Corrigé |
| f5 (médicament) | → q10 | f5 → q10 | Corrigé |
| f10 (SAOS) | → q11 | f10 → q11 | Corrigé |
| f11 (anxiété) | → q12 | f11 → q12 | Corrigé |
| f12 (hyperhidrose) | → q13 | f12 → q13 | Corrigé |
| f13 (obésité) | → q7 | f13 → q7 | Corrigé |

Aucun lien `→ q7` ne subsiste hors de q13 et f13. Chaque chemin qui mène au THM (t2) passe par qe8 (saignement post-ménopausique), q6 (grossesse), q1, q2, q3, q5, q10–q13, puis q9 (contre-indications).

## 2. Contrôle du graphe

| Contrôle | Résultat |
|---|---|
| Losanges : une sortie Oui et une sortie Non | 24/24 conformes |
| Cases : une sortie | f3, f4, f5, f10–f13, a7, d, t1, t2 conformes |
| Fins sans sortie | u0, fe8, f6, f1, f2, fz, f7, f8, r conformes |
| Nœud inatteignable | Aucun |
| Cycle | Aucun |
| Cul-de-sac (case sans sortie) | Aucun |
| Drapeaux rouges (q0, q4/q4b, qe8, q6, q1, q2) | Placés avant tout diagnostic ; aucun lien ne les contourne |

## 3. Constats restants (aucun Critique ni Grave)

| Classe | Emplacement | Extrait (≤ 200 car.) | Correction proposée | Source |
|---|---|---|---|---|
| Moyen | Nœud f4, detail | « Le médecin administre du sucre par voie orale (resucrage) » | Ajouter une condition : « si la patiente est consciente et peut avaler ; sinon glucose IV ou glucagon ». | Protocole hypoglycémie HUG, mise à jour du 28.03.2024 (sb-43, déjà cité ; non relu ici) |
| Léger | Lien q4 → qe8 (Non) | « Diabète sous insuline ou sulfonylurée ? » | Chez la non-diabétique, la glycémie n'est jamais mesurée. Pour couvrir E6, il suffit de préciser dans le detail : « glycémie si malaise neuroglucopénique ». | Point 4, E6 du cours |
| Léger | Nœud q1, après q1 | « …ou sueurs nocturnes profuses » | Les SVM typiques comportent des sueurs nocturnes abondantes, ce qui donne des faux positifs vers f1. Préciser : « sueurs trempant le linge, avec fièvre ou perte > 10 % du poids en 6 mois ». Le constat rejoint M3 de l'it8. | Lugano 2014 |

Hors périmètre, non vérifié : les doses de VEOZA™ et de LYNKUET® du nœud r. Je ne les ai pas confrontées à l'AIPS dans cette vérification.

## 4. Conclusion

G1 est corrigé exactement comme demandé. L'arbre ne contient plus de défaut de chaînage, de cul-de-sac ni de drapeau rouge contourné de classe Critique ou Grave. Il reste un défaut Moyen de sécurité (f4) à corriger avant présentation.

VERDICT G1: corrigé · graves 0
