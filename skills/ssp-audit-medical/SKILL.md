---
name: ssp-audit-medical
description: >-
  Lis ce skill avant toute fusion qui touche un contenu clinique : l’audit
  médical passe d’abord par huit contrôles déterministes à zéro jeton, puis par
  une revue clinique ciblée de Galien, limitée au diff et aux signalements.
---
# But
Ce skill automatise tout ce qu’une machine vérifie sans perte de qualité, et réserve le jugement clinique aux seuls éléments qui en ont besoin.
# Déclencheur
Toute demande de fusion qui modifie data/ck/, GES, TIP, NOT ou assets/nc/.
# Niveau 1 · contrôles déterministes (CI, zéro jeton)
- G1 doses : chaque dose détectée (nombre + mg, µg, g, UI, mmol, mL, /kg, /j) correspond à une ligne de `data/ck/doses_ch.json` (substance, dose, voie, population) lue à la main et datée ; sinon le badge « À vérifier » est présent ; sinon échec.
- G2 source et date : chaque affirmation porte `src` et `lu_le` (date ISO au plus tard aujourd’hui), ou `statut: "À vérifier"`.
- G3 domaines : chaque URL clinique appartient à `qa/domaines.yml` (Suisse, puis Europe) ; l’anatomie admet aussi Commons et Z-Anatomy.
- G4 termes : Lyncée trouve 0 terme nouveau non défini ; chaque identifiant `glo|…` renvoie à une entrée existante.
- G5 chaîne : chaque nerf et chaque entrée CK ont lésion, sémiologie, exploration (référence ou 1re et 2e intention, avec « recherche »), objectif, mesures générales et moyens spécifiques (jsonschema).
- G6 verbes : chaque phrase contient au moins une forme verbale conjuguée (formes de Lexique 3.83) ; les titres et libellés courts sont exemptés par leur champ.
- G7 rouge : la couleur rouge apparaît seulement sur les éléments marqués `bloquant: true` ou `.urg`.
- G8 justification : chaque examen de `hyp.json` (`exam.reference`, `exam.lignes`) porte `mecanisme`, `principe` et `pourquoi_ce_choix` ; chaque moyen spécifique porte en plus `limites`. Chaque champ fait au moins 20 caractères et 3 mots et ne recopie ni un autre champ ni le nom du moyen ; l’ancien champ `pourquoi` est refusé. Le schéma `hyp.schema.json` exige les mêmes champs (G5).
Le niveau 1 écrit `qa/audit-flags.json` (élément, contrôle, motif, ligne) en artefact.
# Niveau 2 · revue clinique ciblée (Galien)
1. Tu lis seulement `git diff origin/main -- data/ck assets/nc` et `qa/audit-flags.json`.
2. Pour chaque élément modifié ou signalé, tu juges : indication, examen de référence désigné par la source, ordre des lignes, précautions et contre-indications, adéquation au contexte suisse, cohérence avec la chaîne, et justesse de la justification (le mécanisme est celui de la maladie, le principe agit bien sur lui, le choix est comparé aux autres moyens, les limites sont celles de la source).
3. Tu écris `qa/audit-galien-<branche>.md` : un verdict par élément (accepté, à corriger, À vérifier) avec la source relue.
4. Tu ne relis pas un élément inchangé et non signalé.
# Audit synchrone par région
1. Six automates régionaux, dirigés par Galien : Neuro (nerfs crâniens, neuro-nc, neuro-moteur, méningé), TêteCou (tête-cou, ORL, yeux), CœurThorax (thorax, cœur, vaisseaux, seins), AbdoPelvis (abdomen, TR et organes génitaux), Locomoteur (rachis, épaule, coude-main, hanche, genou, cheville-pied), PeauPopulations (peau, constantes, ganglions, pédiatrie, gériatrie, psychiatrie).
2. Déclencheur : un commit « unite:<id> prête » d’un agent auteur ; l’automate de la région reprend l’unité aussitôt, après le niveau 1.
3. Chaque faute se corrige par un commit dédié : « audit(galien-<région>): <unité> · <faute> → <correction> [source] (critique|majeure|mineure) ».
4. Chaque correction s’ajoute à `qa/audit/fautes.jsonl` (unité, champ, faute, correction, source, lu_le, gravité, commit).
5. `tools/audit/rapport_fautes.py` régénère « Rapport d’audit médical : les fautes corrigées » (`qa/audit/RAPPORT_FAUTES.md`), groupé par unité.
6. Une dose ne se corrige que vers une ligne de `doses_ch.json` ; un doute clinique devient « À vérifier », jamais une correction inventée.
7. Une faute critique est signalée en tête du rapport, en rouge, et sa correction attend l’accord de Vial avant fusion (décision du 17.10.2026).
# Interdits
Aucun seuil abaissé pour obtenir une CI verte ; aucune lecture automatisée du Compendium ; aucun audit de ses propres textes sans contrôle croisé (Janus, ou Asclépios pour le glossaire).
# Règle universelle
Le projet cible doit avoir un résultat de HAUTE QUALITÉ. L’usage des jetons doit être raisonnable et optimisé, et tout gaspillage est formellement interdit. L’économie de jetons est autorisée si et seulement si elle ne dégrade pas la qualité du travail.
