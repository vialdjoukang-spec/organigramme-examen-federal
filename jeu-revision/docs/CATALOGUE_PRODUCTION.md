# Catalogue de production · INTERNAT

## REPRISE

Tu es un agent neuf. Lis d'abord jeu-revision/docs/PROMPT_PROJET.md, docs/PLAN_PRODUCTION.md, docs/PROGRESSION.md et docs/progression.json. N'ouvre aucun cours ni aucun LOT du dépôt. Ne modifie pas js/, css/, data/ ni index.html (Eta_Bot produit le jeu). Lance : python3 jeu-revision/tools/progression.py status puis python3 jeu-revision/tools/progression.py next. Après chaque spécialité auditee, exécute la commande set puis render, puis pousse depuis origin/main (fetch juste avant le push).

Commandes du script : `python3 jeu-revision/tools/progression.py status` · `next` · `set <id> --statut …` · `render`. La source de vérité est `docs/progression.json` ; ce fichier Markdown est régénéré, ne l'édite pas à la main.

Dernière mise à jour : 17.11.2026 14:47 (Europe/Amsterdam).

## Dénombrement

Le plan de production (lots A à G, paraclinique, transversales, sciences fondamentales) compte **63** spécialités et disciplines, **pas 45**. Le détail figure ci-dessous, groupé comme dans PLAN_PRODUCTION.md. La Phase 0, la veille et l'examen blanc s'ajoutent au chantier mais n'entrent pas dans le compteur joueur.

Le catalogue joueur (`catalogue.html`) affiche aujourd'hui **1 / 63** spécialité(s) disponible(s).

## 0 · Veille

### Veille (examen fédéral, santé publique, sociétés savantes)

- Identifiant : `veille`.
- Statut : en cours.
- Pathologies couvertes : à établir sur un total visé de à établir.
- Cas Urgence : à établir. Cas Consultation : à établir.
- Taux « À vérifier » : à établir.
- Commit : aucun pour l'instant.
- Planche : pas encore produite.
- Notes : La veille réutilise veille/veille.py, veille/sources.yml et les workflows ve1/ve2, puis les étend. Les données quotidiennes s'écrivent sur la branche veille-etat, pas sur main.

## Phase 0 · Moteur

### Moteur (règles, étoiles, modes, sons, traqueur, carte du parcours)

- Identifiant : `moteur`.
- Statut : poussé.
- Pathologies couvertes : à établir sur un total visé de à établir.
- Cas Urgence : à établir. Cas Consultation : à établir.
- Taux « À vérifier » : à établir.
- Commit : [`8de11ee8762ac9e1250341a7f94d6c55509a497f`](https://github.com/vialdjoukang-spec/organigramme-examen-federal/commit/8de11ee8762ac9e1250341a7f94d6c55509a497f).
- Planche : pas encore produite.
- Notes : La Phase 0 (moteur v2, confiance, traqueur, parcours, sons, outils de couverture et planche) a été poussée sur main le 17.11.2026 (commit 8de11ee). Le détail figure dans docs/CONTINUITE.md et le jeu publié dans jeu-revision/.

## Lot A · Médecine interne

### Cardiologie

- Identifiant : `cardiologie`.
- Statut : à faire.
- Pathologies couvertes : 0 sur un total visé de à établir.
- Cas Urgence : 1. Cas Consultation : 0.
- Taux « À vérifier » : 35/180.
- Commit : [`8de11ee8762ac9e1250341a7f94d6c55509a497f`](https://github.com/vialdjoukang-spec/organigramme-examen-federal/commit/8de11ee8762ac9e1250341a7f94d6c55509a497f).
- Planche : `planches/cardiologie.html`.
- Notes : Le prototype « urgences cardio » et la Phase 0 sont sur main (commit 8de11ee) : 18 cartes, 1 cas Urgence, 4 duels, planche planches/cardiologie.html. Le rapport docs/couverture/cardiologie.md (lu le 17.11.2026) compte 6 pathologies dans le catalogue initial, dont 0 couverte, 3 partielles et 3 manquantes ; 35 affirmations « À vérifier » sur 180 (19,4 %). Le total visé pour la spécialité complète reste à établir : le catalogue initial doit encore être complété depuis des sources suisses. Aucune pathologie n'est donc déclarée maîtrisée ou entièrement couverte.

### Angiologie

- Identifiant : `angiologie`.
- Statut : à faire.
- Pathologies couvertes : à établir sur un total visé de à établir.
- Cas Urgence : à établir. Cas Consultation : à établir.
- Taux « À vérifier » : à établir.
- Commit : aucun pour l'instant.
- Planche : pas encore produite.

### Pneumologie

- Identifiant : `pneumologie`.
- Statut : à faire.
- Pathologies couvertes : à établir sur un total visé de à établir.
- Cas Urgence : à établir. Cas Consultation : à établir.
- Taux « À vérifier » : à établir.
- Commit : aucun pour l'instant.
- Planche : pas encore produite.

### Gastro-entérologie et hépatologie

- Identifiant : `gastro-enterologie-hepatologie`.
- Statut : à faire.
- Pathologies couvertes : à établir sur un total visé de à établir.
- Cas Urgence : à établir. Cas Consultation : à établir.
- Taux « À vérifier » : à établir.
- Commit : aucun pour l'instant.
- Planche : pas encore produite.

### Néphrologie

- Identifiant : `nephrologie`.
- Statut : à faire.
- Pathologies couvertes : à établir sur un total visé de à établir.
- Cas Urgence : à établir. Cas Consultation : à établir.
- Taux « À vérifier » : à établir.
- Commit : aucun pour l'instant.
- Planche : pas encore produite.

### Endocrinologie et diabétologie

- Identifiant : `endocrinologie-diabetologie`.
- Statut : à faire.
- Pathologies couvertes : à établir sur un total visé de à établir.
- Cas Urgence : à établir. Cas Consultation : à établir.
- Taux « À vérifier » : à établir.
- Commit : aucun pour l'instant.
- Planche : pas encore produite.

### Hématologie

- Identifiant : `hematologie`.
- Statut : à faire.
- Pathologies couvertes : à établir sur un total visé de à établir.
- Cas Urgence : à établir. Cas Consultation : à établir.
- Taux « À vérifier » : à établir.
- Commit : aucun pour l'instant.
- Planche : pas encore produite.

### Oncologie

- Identifiant : `oncologie`.
- Statut : à faire.
- Pathologies couvertes : à établir sur un total visé de à établir.
- Cas Urgence : à établir. Cas Consultation : à établir.
- Taux « À vérifier » : à établir.
- Commit : aucun pour l'instant.
- Planche : pas encore produite.

### Infectiologie

- Identifiant : `infectiologie`.
- Statut : à faire.
- Pathologies couvertes : à établir sur un total visé de à établir.
- Cas Urgence : à établir. Cas Consultation : à établir.
- Taux « À vérifier » : à établir.
- Commit : aucun pour l'instant.
- Planche : pas encore produite.

### Rhumatologie

- Identifiant : `rhumatologie`.
- Statut : à faire.
- Pathologies couvertes : à établir sur un total visé de à établir.
- Cas Urgence : à établir. Cas Consultation : à établir.
- Taux « À vérifier » : à établir.
- Commit : aucun pour l'instant.
- Planche : pas encore produite.

### Immunologie et allergologie

- Identifiant : `immunologie-allergologie`.
- Statut : à faire.
- Pathologies couvertes : à établir sur un total visé de à établir.
- Cas Urgence : à établir. Cas Consultation : à établir.
- Taux « À vérifier » : à établir.
- Commit : aucun pour l'instant.
- Planche : pas encore produite.

### Gériatrie

- Identifiant : `geriatrie`.
- Statut : à faire.
- Pathologies couvertes : à établir sur un total visé de à établir.
- Cas Urgence : à établir. Cas Consultation : à établir.
- Taux « À vérifier » : à établir.
- Commit : aucun pour l'instant.
- Planche : pas encore produite.

## Lot B · Neurosciences et santé mentale

### Neurologie

- Identifiant : `neurologie`.
- Statut : à faire.
- Pathologies couvertes : à établir sur un total visé de à établir.
- Cas Urgence : à établir. Cas Consultation : à établir.
- Taux « À vérifier » : à établir.
- Commit : aucun pour l'instant.
- Planche : pas encore produite.

### Psychiatrie et psychothérapie

- Identifiant : `psychiatrie-psychotherapie`.
- Statut : à faire.
- Pathologies couvertes : à établir sur un total visé de à établir.
- Cas Urgence : à établir. Cas Consultation : à établir.
- Taux « À vérifier » : à établir.
- Commit : aucun pour l'instant.
- Planche : pas encore produite.

### Pédopsychiatrie

- Identifiant : `pedopsychiatrie`.
- Statut : à faire.
- Pathologies couvertes : à établir sur un total visé de à établir.
- Cas Urgence : à établir. Cas Consultation : à établir.
- Taux « À vérifier » : à établir.
- Commit : aucun pour l'instant.
- Planche : pas encore produite.

### Addictologie

- Identifiant : `addictologie`.
- Statut : à faire.
- Pathologies couvertes : à établir sur un total visé de à établir.
- Cas Urgence : à établir. Cas Consultation : à établir.
- Taux « À vérifier » : à établir.
- Commit : aucun pour l'instant.
- Planche : pas encore produite.

## Lot C · Mère et enfant

### Pédiatrie

- Identifiant : `pediatrie`.
- Statut : à faire.
- Pathologies couvertes : à établir sur un total visé de à établir.
- Cas Urgence : à établir. Cas Consultation : à établir.
- Taux « À vérifier » : à établir.
- Commit : aucun pour l'instant.
- Planche : pas encore produite.

### Néonatologie

- Identifiant : `neonatologie`.
- Statut : à faire.
- Pathologies couvertes : à établir sur un total visé de à établir.
- Cas Urgence : à établir. Cas Consultation : à établir.
- Taux « À vérifier » : à établir.
- Commit : aucun pour l'instant.
- Planche : pas encore produite.

### Gynécologie

- Identifiant : `gynecologie`.
- Statut : à faire.
- Pathologies couvertes : à établir sur un total visé de à établir.
- Cas Urgence : à établir. Cas Consultation : à établir.
- Taux « À vérifier » : à établir.
- Commit : aucun pour l'instant.
- Planche : pas encore produite.

### Obstétrique

- Identifiant : `obstetrique`.
- Statut : à faire.
- Pathologies couvertes : à établir sur un total visé de à établir.
- Cas Urgence : à établir. Cas Consultation : à établir.
- Taux « À vérifier » : à établir.
- Commit : aucun pour l'instant.
- Planche : pas encore produite.

## Lot D · Chirurgie

### Chirurgie viscérale

- Identifiant : `chirurgie-viscerale`.
- Statut : à faire.
- Pathologies couvertes : à établir sur un total visé de à établir.
- Cas Urgence : à établir. Cas Consultation : à établir.
- Taux « À vérifier » : à établir.
- Commit : aucun pour l'instant.
- Planche : pas encore produite.

### Traumatologie et orthopédie

- Identifiant : `traumatologie-orthopedie`.
- Statut : à faire.
- Pathologies couvertes : à établir sur un total visé de à établir.
- Cas Urgence : à établir. Cas Consultation : à établir.
- Taux « À vérifier » : à établir.
- Commit : aucun pour l'instant.
- Planche : pas encore produite.

### Urologie

- Identifiant : `urologie`.
- Statut : à faire.
- Pathologies couvertes : à établir sur un total visé de à établir.
- Cas Urgence : à établir. Cas Consultation : à établir.
- Taux « À vérifier » : à établir.
- Commit : aucun pour l'instant.
- Planche : pas encore produite.

### Chirurgie vasculaire

- Identifiant : `chirurgie-vasculaire`.
- Statut : à faire.
- Pathologies couvertes : à établir sur un total visé de à établir.
- Cas Urgence : à établir. Cas Consultation : à établir.
- Taux « À vérifier » : à établir.
- Commit : aucun pour l'instant.
- Planche : pas encore produite.

### Chirurgie thoracique et cardiaque

- Identifiant : `chirurgie-thoracique-cardiaque`.
- Statut : à faire.
- Pathologies couvertes : à établir sur un total visé de à établir.
- Cas Urgence : à établir. Cas Consultation : à établir.
- Taux « À vérifier » : à établir.
- Commit : aucun pour l'instant.
- Planche : pas encore produite.

### Neurochirurgie

- Identifiant : `neurochirurgie`.
- Statut : à faire.
- Pathologies couvertes : à établir sur un total visé de à établir.
- Cas Urgence : à établir. Cas Consultation : à établir.
- Taux « À vérifier » : à établir.
- Commit : aucun pour l'instant.
- Planche : pas encore produite.

## Lot E · Organes des sens et peau

### ORL

- Identifiant : `orl`.
- Statut : à faire.
- Pathologies couvertes : à établir sur un total visé de à établir.
- Cas Urgence : à établir. Cas Consultation : à établir.
- Taux « À vérifier » : à établir.
- Commit : aucun pour l'instant.
- Planche : pas encore produite.

### Ophtalmologie

- Identifiant : `ophtalmologie`.
- Statut : à faire.
- Pathologies couvertes : à établir sur un total visé de à établir.
- Cas Urgence : à établir. Cas Consultation : à établir.
- Taux « À vérifier » : à établir.
- Commit : aucun pour l'instant.
- Planche : pas encore produite.

### Dermatologie et vénéréologie

- Identifiant : `dermatologie-venereologie`.
- Statut : à faire.
- Pathologies couvertes : à établir sur un total visé de à établir.
- Cas Urgence : à établir. Cas Consultation : à établir.
- Taux « À vérifier » : à établir.
- Commit : aucun pour l'instant.
- Planche : pas encore produite.

## Lot F · Aigu et fin de vie

### Médecine d'urgence

- Identifiant : `medecine-urgence`.
- Statut : à faire.
- Pathologies couvertes : à établir sur un total visé de à établir.
- Cas Urgence : à établir. Cas Consultation : à établir.
- Taux « À vérifier » : à établir.
- Commit : aucun pour l'instant.
- Planche : pas encore produite.

### Anesthésiologie

- Identifiant : `anesthesiologie`.
- Statut : à faire.
- Pathologies couvertes : à établir sur un total visé de à établir.
- Cas Urgence : à établir. Cas Consultation : à établir.
- Taux « À vérifier » : à établir.
- Commit : aucun pour l'instant.
- Planche : pas encore produite.

### Médecine intensive

- Identifiant : `medecine-intensive`.
- Statut : à faire.
- Pathologies couvertes : à établir sur un total visé de à établir.
- Cas Urgence : à établir. Cas Consultation : à établir.
- Taux « À vérifier » : à établir.
- Commit : aucun pour l'instant.
- Planche : pas encore produite.

### Toxicologie

- Identifiant : `toxicologie`.
- Statut : à faire.
- Pathologies couvertes : à établir sur un total visé de à établir.
- Cas Urgence : à établir. Cas Consultation : à établir.
- Taux « À vérifier » : à établir.
- Commit : aucun pour l'instant.
- Planche : pas encore produite.

### Médecine palliative

- Identifiant : `medecine-palliative`.
- Statut : à faire.
- Pathologies couvertes : à établir sur un total visé de à établir.
- Cas Urgence : à établir. Cas Consultation : à établir.
- Taux « À vérifier » : à établir.
- Commit : aucun pour l'instant.
- Planche : pas encore produite.

## Lot G · Premier recours et société

### Médecine de famille

- Identifiant : `medecine-famille`.
- Statut : à faire.
- Pathologies couvertes : à établir sur un total visé de à établir.
- Cas Urgence : à établir. Cas Consultation : à établir.
- Taux « À vérifier » : à établir.
- Commit : aucun pour l'instant.
- Planche : pas encore produite.

### Médecine des voyages et tropicale

- Identifiant : `medecine-voyages-tropicale`.
- Statut : à faire.
- Pathologies couvertes : à établir sur un total visé de à établir.
- Cas Urgence : à établir. Cas Consultation : à établir.
- Taux « À vérifier » : à établir.
- Commit : aucun pour l'instant.
- Planche : pas encore produite.

### Médecine du travail

- Identifiant : `medecine-travail`.
- Statut : à faire.
- Pathologies couvertes : à établir sur un total visé de à établir.
- Cas Urgence : à établir. Cas Consultation : à établir.
- Taux « À vérifier » : à établir.
- Commit : aucun pour l'instant.
- Planche : pas encore produite.

### Médecine physique et réadaptation

- Identifiant : `medecine-physique-readaptation`.
- Statut : à faire.
- Pathologies couvertes : à établir sur un total visé de à établir.
- Cas Urgence : à établir. Cas Consultation : à établir.
- Taux « À vérifier » : à établir.
- Commit : aucun pour l'instant.
- Planche : pas encore produite.

### Prévention et santé publique

- Identifiant : `prevention-sante-publique`.
- Statut : à faire.
- Pathologies couvertes : à établir sur un total visé de à établir.
- Cas Urgence : à établir. Cas Consultation : à établir.
- Taux « À vérifier » : à établir.
- Commit : aucun pour l'instant.
- Planche : pas encore produite.

### Médecine légale

- Identifiant : `medecine-legale`.
- Statut : à faire.
- Pathologies couvertes : à établir sur un total visé de à établir.
- Cas Urgence : à établir. Cas Consultation : à établir.
- Taux « À vérifier » : à établir.
- Commit : aucun pour l'instant.
- Planche : pas encore produite.

### Génétique médicale

- Identifiant : `genetique-medicale`.
- Statut : à faire.
- Pathologies couvertes : à établir sur un total visé de à établir.
- Cas Urgence : à établir. Cas Consultation : à établir.
- Taux « À vérifier » : à établir.
- Commit : aucun pour l'instant.
- Planche : pas encore produite.

## Phase 2 · Paraclinique

### Radiologie

- Identifiant : `radiologie`.
- Statut : à faire.
- Pathologies couvertes : à établir sur un total visé de à établir.
- Cas Urgence : à établir. Cas Consultation : à établir.
- Taux « À vérifier » : à établir.
- Commit : aucun pour l'instant.
- Planche : pas encore produite.

### Médecine nucléaire

- Identifiant : `medecine-nucleaire`.
- Statut : à faire.
- Pathologies couvertes : à établir sur un total visé de à établir.
- Cas Urgence : à établir. Cas Consultation : à établir.
- Taux « À vérifier » : à établir.
- Commit : aucun pour l'instant.
- Planche : pas encore produite.

### Laboratoire (chimie, hématologie, microbiologie)

- Identifiant : `laboratoire`.
- Statut : à faire.
- Pathologies couvertes : à établir sur un total visé de à établir.
- Cas Urgence : à établir. Cas Consultation : à établir.
- Taux « À vérifier » : à établir.
- Commit : aucun pour l'instant.
- Planche : pas encore produite.

### Anatomopathologie

- Identifiant : `anatomopathologie`.
- Statut : à faire.
- Pathologies couvertes : à établir sur un total visé de à établir.
- Cas Urgence : à établir. Cas Consultation : à établir.
- Taux « À vérifier » : à établir.
- Commit : aucun pour l'instant.
- Planche : pas encore produite.

### ECG

- Identifiant : `ecg`.
- Statut : à faire.
- Pathologies couvertes : à établir sur un total visé de à établir.
- Cas Urgence : à établir. Cas Consultation : à établir.
- Taux « À vérifier » : à établir.
- Commit : aucun pour l'instant.
- Planche : pas encore produite.

### EFR et explorations fonctionnelles

- Identifiant : `efr-explorations-fonctionnelles`.
- Statut : à faire.
- Pathologies couvertes : à établir sur un total visé de à établir.
- Cas Urgence : à établir. Cas Consultation : à établir.
- Taux « À vérifier » : à établir.
- Commit : aucun pour l'instant.
- Planche : pas encore produite.

## Phase 3 · Disciplines transversales

### Éthique

- Identifiant : `ethique`.
- Statut : à faire.
- Pathologies couvertes : à établir sur un total visé de à établir.
- Cas Urgence : à établir. Cas Consultation : à établir.
- Taux « À vérifier » : à établir.
- Commit : aucun pour l'instant.
- Planche : pas encore produite.

### Droit médical suisse

- Identifiant : `droit-medical-suisse`.
- Statut : à faire.
- Pathologies couvertes : à établir sur un total visé de à établir.
- Cas Urgence : à établir. Cas Consultation : à établir.
- Taux « À vérifier » : à établir.
- Commit : aucun pour l'instant.
- Planche : pas encore produite.

### Communication

- Identifiant : `communication`.
- Statut : à faire.
- Pathologies couvertes : à établir sur un total visé de à établir.
- Cas Urgence : à établir. Cas Consultation : à établir.
- Taux « À vérifier » : à établir.
- Commit : aucun pour l'instant.
- Planche : pas encore produite.

### EBM et statistiques

- Identifiant : `ebm-statistiques`.
- Statut : à faire.
- Pathologies couvertes : à établir sur un total visé de à établir.
- Cas Urgence : à établir. Cas Consultation : à établir.
- Taux « À vérifier » : à établir.
- Commit : aucun pour l'instant.
- Planche : pas encore produite.

### Système de santé et assurances suisses (LAMal, LAA, AI)

- Identifiant : `systeme-sante-assurances`.
- Statut : à faire.
- Pathologies couvertes : à établir sur un total visé de à établir.
- Cas Urgence : à établir. Cas Consultation : à établir.
- Taux « À vérifier » : à établir.
- Commit : aucun pour l'instant.
- Planche : pas encore produite.

### Pharmacologie clinique

- Identifiant : `pharmacologie-clinique`.
- Statut : à faire.
- Pathologies couvertes : à établir sur un total visé de à établir.
- Cas Urgence : à établir. Cas Consultation : à établir.
- Taux « À vérifier » : à établir.
- Commit : aucun pour l'instant.
- Planche : pas encore produite.

## Phase 4 · Sciences fondamentales

### Anatomie

- Identifiant : `anatomie`.
- Statut : à faire.
- Pathologies couvertes : à établir sur un total visé de à établir.
- Cas Urgence : à établir. Cas Consultation : à établir.
- Taux « À vérifier » : à établir.
- Commit : aucun pour l'instant.
- Planche : pas encore produite.

### Physiologie

- Identifiant : `physiologie`.
- Statut : à faire.
- Pathologies couvertes : à établir sur un total visé de à établir.
- Cas Urgence : à établir. Cas Consultation : à établir.
- Taux « À vérifier » : à établir.
- Commit : aucun pour l'instant.
- Planche : pas encore produite.

### Physiopathologie

- Identifiant : `physiopathologie`.
- Statut : à faire.
- Pathologies couvertes : à établir sur un total visé de à établir.
- Cas Urgence : à établir. Cas Consultation : à établir.
- Taux « À vérifier » : à établir.
- Commit : aucun pour l'instant.
- Planche : pas encore produite.

### Biochimie

- Identifiant : `biochimie`.
- Statut : à faire.
- Pathologies couvertes : à établir sur un total visé de à établir.
- Cas Urgence : à établir. Cas Consultation : à établir.
- Taux « À vérifier » : à établir.
- Commit : aucun pour l'instant.
- Planche : pas encore produite.

### Pharmacologie

- Identifiant : `pharmacologie`.
- Statut : à faire.
- Pathologies couvertes : à établir sur un total visé de à établir.
- Cas Urgence : à établir. Cas Consultation : à établir.
- Taux « À vérifier » : à établir.
- Commit : aucun pour l'instant.
- Planche : pas encore produite.

### Microbiologie

- Identifiant : `microbiologie`.
- Statut : à faire.
- Pathologies couvertes : à établir sur un total visé de à établir.
- Cas Urgence : à établir. Cas Consultation : à établir.
- Taux « À vérifier » : à établir.
- Commit : aucun pour l'instant.
- Planche : pas encore produite.

### Immunologie

- Identifiant : `immunologie`.
- Statut : à faire.
- Pathologies couvertes : à établir sur un total visé de à établir.
- Cas Urgence : à établir. Cas Consultation : à établir.
- Taux « À vérifier » : à établir.
- Commit : aucun pour l'instant.
- Planche : pas encore produite.

### Génétique

- Identifiant : `genetique`.
- Statut : à faire.
- Pathologies couvertes : à établir sur un total visé de à établir.
- Cas Urgence : à établir. Cas Consultation : à établir.
- Taux « À vérifier » : à établir.
- Commit : aucun pour l'instant.
- Planche : pas encore produite.

### Histologie

- Identifiant : `histologie`.
- Statut : à faire.
- Pathologies couvertes : à établir sur un total visé de à établir.
- Cas Urgence : à établir. Cas Consultation : à établir.
- Taux « À vérifier » : à établir.
- Commit : aucun pour l'instant.
- Planche : pas encore produite.

### Embryologie

- Identifiant : `embryologie`.
- Statut : à faire.
- Pathologies couvertes : à établir sur un total visé de à établir.
- Cas Urgence : à établir. Cas Consultation : à établir.
- Taux « À vérifier » : à établir.
- Commit : aucun pour l'instant.
- Planche : pas encore produite.

## Examen blanc PROFILES

### Examen blanc PROFILES

- Identifiant : `examen-blanc-profiles`.
- Statut : à faire.
- Pathologies couvertes : à établir sur un total visé de à établir.
- Cas Urgence : à établir. Cas Consultation : à établir.
- Taux « À vérifier » : à établir.
- Commit : aucun pour l'instant.
- Planche : pas encore produite.

