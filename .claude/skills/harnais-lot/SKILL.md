---
name: harnais-lot
description: Lis ce skill avant de rédiger ou corriger un fichier d'un LOT (Phase A ou DD) : procédure du Harnais, seul circuit de vérité, sans audit externe.
---
1. `python3 harnais/prompt_projet.py` puis `python3 harnais/prompt_expert.py <redacteur|phase-a>` puis `harnais/LECONS/<rôle>.md`.
2. Prends ta tâche : `python3 harnais/tableau_taches.py prendre ecrire <LOT> <label> <bloc>` ; verrou : `python3 harnais/verrou.py claim <fichier> <label>` (code 3 = STOP).
3. Écris uniquement ton fichier (100–200 Ko, 14 points, FIN_FICHIER, sans title=). Doses : `python3 harnais/aips_texte.py <n°> --section <mot>`. Sources : `harnais/pubmed.py`, `harnais/SOURCES_AUTORISEES.md`. Chiffre non lu → « À vérifier ».
4. Avant de rendre la main : `python3 harnais/controle_medical.py <fichier>` et `python3 harnais/controle_langue.py <fichier>` ; corrige jusqu'à RESULTAT ≥ 90, 0 critique.
5. `python3 harnais/tableau_taches.py fait ecrire <LOT> <i>` puis `verrou.py release`.
Crédo : exhaustivité dans une grande densité, concision, sans perte d'information.
