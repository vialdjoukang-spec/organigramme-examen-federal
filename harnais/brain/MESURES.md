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

---

# Essais v3 demandés par Vial · 28.10.2026

Commande : `python3 harnais/brain/outils/essais_vial.py`, en lecture seule sur `origin/main`, gratuite, en 276 s. Résultats bruts : `harnais/brain/essais_vial.json`.
Cours : `LOT_001 DX.2`, `LOT_005 DX.3`, `LOT_010 DX.4` et `LOT_012 DX.5`, lus par `git show`. Les fichiers de `main` ne sont jamais modifiés ; les corrections se font en mémoire ou sur copie temporaire.

## T1 · Réduction des dépenses (jetons, 4 caractères par jeton)

La première référence correspond à 10 auditeurs qui relisent chacun tout le HTML. La seconde correspond à 10 auditeurs qui relisent chacun le texte visible. Avec le circuit, chaque auditeur reçoit seulement un brief compilé : ses doléances [agent] et les paquets des points touchés.

| Cours | Relecture HTML ×10 | Texte visible ×10 | Briefs Sonnet | Briefs Opus | Total des briefs | Réduction contre HTML | Réduction contre texte |
|---|---|---|---|---|---|---|---|
| LOT_001 DX.2 | 597 900 | 200 640 | 29 634 | 14 171 | 43 805 | 92,67 % | 78,17 % |
| LOT_005 DX.3 | 243 500 | 43 440 | 7 884 | 2 969 | 10 853 | 95,54 % | 75,02 % |
| LOT_010 DX.4 | 266 890 | 59 140 | 8 462 | 6 451 | 14 913 | 94,41 % | 74,78 % |
| LOT_012 DX.5 | 278 440 | 59 860 | 9 117 | 844 | 9 961 | 96,42 % | 83,36 % |
| **4 cours** | 1 386 730 | 363 080 | | | 79 532 | **94,26 %** | **78,10 %** |
| Doré (cours sans faute) | 127 060 | | | | 1 040 | 99,18 % | |

**La cible de 99,99 % n'est pas atteinte.** Pour l'atteindre sur ces 4 cours, le total des briefs devrait rester sous 139 jetons ; il atteint 79 532 jetons, soit 573 fois plus. Le plancher vient du contenu même des briefs : un auditeur doit lire le paquet du point qu'il corrige. Seul un cours sans doléance [agent] s'en approche (doré : 99,18 %). Les jetons de rédaction (Phase A et Phase B) ne sont pas comptés ici.

## T2 · Application à 4 cours réels de LOT différents

| Cours | α avant | α après les scripts | β | Tours jusqu'au point fixe | Idempotent | `main` intact | Texte visible conservé | Verdict | Durée |
|---|---|---|---|---|---|---|---|---|---|
| LOT_001 DX.2 | 158 | 133 | 20 | 2 | oui | oui | 102,7 % | retour : 28 fautes graves | 9,1 s |
| LOT_005 DX.3 | 62 | 50 | 2 | 2 | oui | oui | 106,2 % | retour : 12 fautes graves | 5,5 s |
| LOT_010 DX.4 | 39 | 25 | 5 | 2 | oui | oui | 106,2 % | retour : 8 fautes graves | 5,8 s |
| LOT_012 DX.5 | 44 | 30 | 1 | 2 | oui | oui | 105,7 % | retour : 13 fautes graves | 5,6 s |

Les scripts suppriment 12 à 25 doléances par cours sans retirer de texte : le texte visible augmente, car la barre des 14 points s'ajoute. Aucun des 4 cours ne sort audité. Les fautes graves restantes reviennent aux auditeurs.

## T3 · Nombre de connexions sans conflit possible

- **Preuve statique.** Les 160 scriptones comptent 64 écrivains pour 71 zones : 70 zones du cours et la quarantaine du journal (s14). Chaque zone a une seule écrivaine, et `conflits_statiques = {}`. Les 96 autres scriptones ne font que lire. Le registre compte 601 connexions : 160 entrées, 160 sorties vers le bus, 71 écritures, 26 relais en zigzag, 146 liens vers un jumeau et 38 liens vers les auditeurs. Le nombre de connexions d'écriture ne peut pas dépasser le nombre de zones. Les connexions de lecture ne sont pas limitées, car une lectrice produit seulement des doléances.
- **Confluence dynamique.** Le test compare 8 ordres aléatoires des écrivains, chacun mené jusqu'au point fixe, sur chacun des 4 cours. **Défaut trouvé :** les 4 cours donnaient un texte différent selon l'ordre (O2). La cause était l'emplacement des blocs `<style>` posés par s1, s2, s5 et s6. **Correctif :** `bus.pose_style` insère désormais chaque bloc à son rang canonique. Après correctif : 0 divergence et 0 paire d'écrivains non commutative.
- **Conflits injectés, tous détectés :** deux écrivains sur une zone (O1), duel (O2, O4), écrivain non idempotent (O3, O4), intrus (O3, O4).
- **Couverture selon le nombre de familles par synapse.** Le test injecte les 770 mutants des 140 synapses, au point de chaque mutant. La couverture vaut 54,3 % avec α seule, 56,8 % avec β seule et 100 % avec α et β. En choisissant à chaque fois le meilleur ensemble, elle vaut 21 % avec 1 famille, 78 % avec 5, 96 % avec 8, 100 % avec 9 et 100 % avec 10. **L'optimum mesuré est de 9 familles.** βM n'ajoute aucune couverture à cette batterie. Son rôle est autre : elle mute le fichier réel pour vérifier qu'α y reste sensible (BM1). Elle reste donc requise. 83 % des mutants ne sont vus que par une seule famille (redondance moyenne : 1,2). Le jumeau et l'escalade vers l'auditeur restent donc nécessaires.
- **16 cours simultanés.** Le test fait passer 4 cours × 4 copies avec écriture réelle sur les copies. Chaque copie est identique à la correction séquentielle, sans panne. Durées : 101 s pour 1 processus, 27 s pour 4 et 27 s pour 16. La machine n'a que 4 cœurs : au-delà, le gain plafonne.

## T4 · Auto-adaptation sur pannes injectées

| Panne | Résultat |
|---|---|
| Exception dans chacune des 140 synapses | 140 sur 140 signalées (Z1), 140 sur 140 ré-routées vers le jumeau |
| Contrat rompu dans chacune des 140 | 140 sur 140 signalées, 140 sur 140 ré-routées |
| Lenteur dans chacune des 140 | 140 sur 140 signalées (Z4) ; résultat conservé, disjoncteur ouvert pour la suite |
| Synapse et jumeau en panne (×140) | 140 sur 140 escaladées (Z2, critique) |
| 14 pannes simultanées, une par point | 0 des 126 autres synapses modifiée (aucune influence) ; 14 sur 14 couvertes par le jumeau ; 6 doléances propres rendues à l'auditeur |
| Orchestre sur le doré | sans panne : sorti audité ; une panne couverte : sorti audité ; double panne : retour (2 escalades) ; 10 pannes aléatoires : retour (3 escalades) |
| Stagnation | 2ᵉ passage avec les mêmes doléances : « bloqué (stagnation) » ; Z3 signalé |

**Défaut trouvé et corrigé :** l'orchestre comptait la panne sans jumeau (Z2) dans le journal, mais pas dans le verdict. Un cours pouvait donc sortir « audité » avec une exigence non couverte. Désormais, cette panne retient le cours.

## Mutation des 160 scriptones (v3)

Commande : `mutation.py --n 64`. Elle couvre 159 scriptones Python ; s7, écrit en JavaScript, est testé au navigateur par `test_scriptones`.

- 33 314 mutants détectés sur 33 314 injectés (32 877 distincts), en 230 s.
- Borne d'évasion à 95 % : 0,0091 %, soit au moins 99,99 % de détection des erreurs connues.
- Aucun faux positif et aucun défaut d'idempotence.

Relevé brut : `mutation_v3.json`. Les autres suites sont vertes (`tests_v3.json`) : `test_scriptones` 14/14, `test_synapses` 13/13, `test_robustesse` 9/9 et `autotest` 109/109.

Livrables : `BRAIN_3D.html`, construit par `outils/construire_3d.py`, et `CHANTIER_BRAIN_HARNESS.pdf`, construit par `outils/construire_pdf.py`.

## Limites de la v3

- La réduction de 94 % est une estimation à 4 caractères par jeton ; elle ne remplace pas une facturation. Les jetons de sortie des auditeurs ne sont pas mesurés, car aucun agent n'est appelé.
- La couverture porte sur les mutants connus, conçus par famille ; elle ne mesure pas le jugement clinique (métrique M5, phase P4).
- Le passage de 5 à 16 auditeurs par étage n'est pas tranché : il faut mesurer le gain de détection d'agents réels.
- `controle_lot.py` ne dépend plus de `BANDE.json`, absent de `main` : à défaut, il se replie sur 100–200 Ko.
