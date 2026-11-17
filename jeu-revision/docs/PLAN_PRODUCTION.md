# PLAN DE PRODUCTION · INTERNAT

## Équipe
- **Grok Bot** administre, audite chaque spécialité et informe Vial.
- **Eta_Bot** construit le moteur et produit les spécialités ; il lance des agents en parallèle, un par spécialité, sur des fichiers séparés.
- **Un auditeur indépendant** contrôle chaque spécialité avant le push (sources, différentiels, cohérence du cas, absence d'abus de prescription).

## Phase 0 · Moteur (priorité)
1. Implémente l'écran Règles, les étoiles, les modes Urgence, Consultation, Entraînement et Fondamentaux.
2. Implémente la pénalité des examens inutiles et le chronomètre.
3. Ajoute la Web Audio API, le bouton muet et les effets.
4. Étends le schéma de carte et de cas aux 8 rubriques du prompt ; écris le validateur.
5. Écris un gabarit de cas qui structure les 8 rubriques depuis les sources suisses (sans ouvrir les cours ni les LOT du dépôt).
6. Ajoute une carte du parcours : une salle par spécialité, verrouillée ou ouverte.

## Phase 1 · Spécialités, par lots (couverture exhaustive)
Couvre chaque pathologie de la spécialité retenue par PROFILES (liste des objectifs publics, sans ouvrir les LOT du dépôt) : donne-lui au moins un cas, et donne un cas Urgence ET un cas Consultation à chaque pathologie fréquente ou grave. Publie pour chaque spécialité la liste des pathologies couvertes et manquantes.
- **Lot A, médecine interne** : cardiologie (compléter), angiologie, pneumologie, gastro-entérologie et hépatologie, néphrologie, endocrinologie et diabétologie, hématologie, oncologie, infectiologie, rhumatologie, immunologie et allergologie, gériatrie.
- **Lot B, neurosciences et santé mentale** : neurologie, psychiatrie et psychothérapie, pédopsychiatrie, addictologie.
- **Lot C, mère et enfant** : pédiatrie, néonatologie, gynécologie, obstétrique.
- **Lot D, chirurgie** : chirurgie viscérale, traumatologie et orthopédie, urologie, chirurgie vasculaire, chirurgie thoracique et cardiaque, neurochirurgie.
- **Lot E, organes des sens et peau** : ORL, ophtalmologie, dermatologie et vénéréologie.
- **Lot F, aigu et fin de vie** : médecine d'urgence, anesthésiologie, médecine intensive, toxicologie, médecine palliative.
- **Lot G, premier recours et société** : médecine de famille, médecine des voyages et tropicale, médecine du travail, médecine physique et réadaptation, prévention et santé publique, médecine légale, génétique médicale.

## Phase 2 · Paraclinique (cartes Examen transversales)
Radiologie, médecine nucléaire, laboratoire (chimie, hématologie, microbiologie), anatomopathologie, ECG, EFR et explorations fonctionnelles. Relie-les aux `imagerie_GROK/` existants dès qu'ils seront prêts.

## Phase 3 · Disciplines transversales
Éthique, droit médical suisse, communication, EBM et statistiques, système de santé et assurances suisses (LAMal, LAA, AI), pharmacologie clinique.

## Phase 4 · Sciences fondamentales (mode Fondamentaux)
Anatomie, physiologie, physiopathologie, biochimie, pharmacologie, microbiologie, immunologie, génétique, histologie, embryologie ; relie chaque carte aux cas cliniques qui l'utilisent.

## Ordre et cadence
Termine la Phase 0, puis produis le lot A dans l'ordre listé, puis B à G. Lance au plus 3 spécialités en parallèle. Audite et pousse chaque spécialité dès qu'elle est finie.

## Économie
N'ouvre jamais les cours ni les LOT du dépôt ; mets en cache les sources suisses lues. Utilise des scripts pour la validation et les captures, jamais un modèle. Ne relis que le diff.
