# BRAIN-HARNESS · mesures du 27.10.2026

Essai en lecture seule sur deux cours de `origin/main` ; aucun fichier de LOT n'est modifié. Les corrections se font sur des copies, hors du dépôt.

- **Cours A** : `LOT_008_Phase_B_V0_DX.3.html` (hypothermie, 91 Ko).
- **Cours B** : `LOT_009_Phase_B_V0_DX.4.html` (prurit systémique, 158 Ko).

Commandes : `cerveau.py mesurer`, `cerveau.py corriger --appliquer` (sur copie), `node harnais/bilan/captures.js --fichier …` (avant et après).

## 1. Détection des 8 doléances de Vial

Circuit existant (`grille_agent.ecarts_points` et `forme_interactive.controle`) : **0 écart** sur A comme sur B. Il repère donc 0 des 8 doléances.

| Doléance | Codes | A : avant → après script | B : avant → après script | Exécutant |
|---|---|---|---|---|
| 1 Police | P4, P7 · V1 | 3 → 0 · police non chargée → chargée (400, 700) | 3 → 0 · idem | script |
| 2 Mise en page | L4, L5, L6 · V2 | 4 → 0 · orphelines au pixel 5 → 1 | 6 → 0 · orphelines 3 → 3 | script |
| 3 Concision | C2, C4 / C2, C3 | 6 → 6 | 4 → 4 | agent |
| 4 Budget du point 2 | B1, B2, B3 | 13 → 13 | 3 → 3 | agent |
| 5 et 6 Arbre | A2, A3 / A2, A3, A6 | 3 → 2 (rendu cliquable fait ; 2 parents sans homologues) | 4 → 3 | script, puis agent |
| 7 Captures | — | 15/15 chapitres, couverture 99 % | 15/15, couverture 99 % | script |
| 8 Tableaux | T3, T4 / T2, T5, T6 | 3 → 1 (« Mortalité » → « Mortalité dans ce stade (%) ») | 3 → 3 (« Donnée », « Valeur ») | script, puis agent |
| **Total** | | **32 → 22 pour l'agent** | **23 → 13 pour l'agent** | |

Le script résout 10 doléances par cours ; il ne crée aucun contenu médical. Les 35 doléances [agent] ont été relues à la main : toutes répondent à la règle énoncée. Choix à confirmer par Vial : B2 exige la source dans chaque phrase chiffrée, même si la phrase précédente la porte déjà.

## 2. Lignes du point 2 (épidémiologie, budget 3 à 4 lignes)

| | Estimation (S4, 110 car./ligne) | Mesure navigateur avant (car./ligne) | Après correction mécanique (colonne de 78 ch) |
|---|---|---|---|
| A | 15 lignes | 14 (107) | 15 (97) |
| B | 8 lignes | 8 (99) | 9 (90) |

Aucun des deux cours ne tient le budget. Réduire le texte relève de l'agent (B1). La doléance joint l'inventaire des chiffres à conserver, par exemple 28 chiffres pour A. Un chiffre qui ne tient pas dans le budget passe dans le tableau ; aucun chiffre n'est supprimé.

## 3. Jetons d'une boucle de correction (estimation : 4 caractères par jeton)

| | Relecture intégrale du HTML | Texte visible du cours | Doléances [agent] compactes | Gain |
|---|---|---|---|---|
| A | 22 418 | 4 678 | 1 633 | **−92,7 %** |
| B | 38 854 | 7 486 | 1 100 | **−97,2 %** |

## 4. Constat majeur : police jamais chargée

Dans les 162 fichiers HTML de `main` (LOT_001 à LOT_011), Atkinson Hyperlegible **ne s'affiche jamais**. Le navigateur ne charge aucune police embarquée (`document.fonts.size = 0`) et le texte s'affiche en Verdana.

- Cause : `coupe_lignes` (lignes de plus de 3 000 caractères) insère un saut de ligne dans l'URL `data:` non citée du `@font-face`. Le navigateur ignore alors la règle entière.
- Répartition : 158 fichiers avec police cassée (P7), 4 sans police embarquée (P1).
- Correctif à la source : `forme_interactive.py` émet désormais une URL citée, coupée par continuation CSS (barre oblique inverse suivie d'un saut de ligne). Sur copie, le navigateur charge les graisses 400 et 700.
- Fichiers déjà convertis : `s1_police.py --appliquer` les répare. Cette réparation fait partie de la correction de masse, qui attend l'ordre de Vial.

## 5. Corpus `main` (162 fichiers, 29 s, lecture seule) : fichiers touchés par code

A2 162 · A3 162 · P4 162 · L5 162 · P7 158 · L4 150 · B1 142 · C4 125 · L6 123 · T6 113 · T2 107 · B3 101 · B2 89 · L3 84 · C2 78 · C3 59 · T5 47 · T7 37 · T3 21 · A4 18 · T4 18 · B4 12 · A6 10 · P1 4 · L1 2.

## 6. Fiabilité des scriptones (jeu doré et mutation)

`mutation.py --n 1340` : **30 820 mutants injectés (30 452 distincts), 30 820 détectés, aucune évasion**, en 129 s.

- Borne supérieure de l'évasion à 95 % : 3 / 30 452 = **0,0099 %**, soit une détection d'au moins **99,99 %** (métrique M1).
- Mutants : 23 classes d'erreurs, chacune injectée dans un contexte varié (chiffres et phrase neutre).

- Faux positifs sur le jeu doré et sur ses variations neutres : 0.
- Idempotence : scriptones seuls et chaîne complète, sur le doré, les mutants et les deux cours réels (`idempotent: true`).
- Tests : `test_scriptones.py` 14/14 (dont le contrôle au navigateur de la police cassée) ; autotest 109/109.

## 7. Limites

- Les 99,99 % portent sur les **classes d'erreurs connues** (23 mutants). Ils ne mesurent pas encore les erreurs médicales de fond : les mutants médicaux sont prévus en P4 (métrique M5).
- S3 et S4 reposent sur des heuristiques sans spaCy : jetons de 6 lettres et 110 caractères par ligne. Le navigateur mesure de 99 à 107 caractères par ligne, et `captures.js` sert d'étalon.
- Les fins orphelines estimées par S2 restent approximatives ; la mesure au pixel fait foi (V2).
- `text-wrap:pretty` ne corrige pas toutes les orphelines (B : 3 → 3). Le reste demande une reformulation.
- Les homologues (A3) et les en-têtes réécrits (T2, T5) demandent du contenu sourcé. Ils restent à l'agent.
