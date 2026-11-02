---
name: controle-medical
description: Lis ce skill pour corriger un fichier d'après un rapport MED_ du contrôle médical par script (doses vs AIPS, PMID, chiffres vs sources, structure §11).
---
Le rapport commence par `RESULTAT score=.. critiques=.. question=..`. Traite d'abord les lignes CRITIQUE : dose absente du texte AIPS → relis `aips_texte.py <n°> --section <mot>` et recopie la formulation exacte ; PMID inexistant → `harnais/pubmed.py chercher|verifier` ; chiffre non retrouvé → rouvre la source, corrige ou écris « non quantifiée » ; « À vérifier » → résous par une source lue ou laisse une question dans HELP_<label>.md. Ne contourne jamais le script ; il détecte l'écart à la source, pas la justesse clinique : relis ce que tu écris.
