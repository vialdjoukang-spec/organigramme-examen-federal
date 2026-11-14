# Fiches Anamnèse (anamnese/A-xx.json), Management (management/M-xx.json), Communication (communication/K-xx.json)

## Anamnèse orientée par motif (A-MOT-x ; A-TRAME et A-SPE suivent la même logique)
{ "id": "A-MOT-1", "titre": "Douleur thoracique", "systeme": "...", "niveau": "m|c", "ssp": "n° SSP PROFILES 2017 si identifiable",
  "ouverture": "première question ouverte, mot pour mot",
  "questions": [{"axe": "Temps|Lieu|Caractéristiques|Facteurs d'influence|Symptômes associés|Contexte (ATCD, médicaments, habitudes, famille, social)", "items": ["question exacte au patient", "..."]}],
  "drapeaux_rouges": [{"question": "...", "si_oui": "conduite immédiate et pourquoi"}],
  "hypotheses": [{"lettre": "VITE DIT CAFé", "diagnostics": ["classés par gravité puis fréquence"], "question_discriminante": "..."}],
  "idees_craintes_attentes": ["question ICE exacte"],
  "liens": {"status": ["S-xx"], "syndromes": ["SY-xx"], "imagerie": ["IMG-xxx"]},
  "synthese_cs": "résumé oral de 2 phrases à l'examinateur",
  "pieges": ["..."], "sources": ["…(étiquette si non suisse)"] }
Cadre suisse de référence : ASSM « La communication dans la médecine au quotidien » 2022 (CC BY 4.0 : axes Temps, Lieu, Caractéristiques, Facteurs d'influence ; ARRR, NURSE) ; PROFILES 2017 EPA 1 ; MEBEKO 2026.

## Management (M-xx) et Communication (K-xx)
{ "id": "...", "titre": "...", "niveau": "m|c", "objectif": "ce que l'examinateur attend, une phrase",
  "etapes": [{"etape": "...", "faire": ["actions verbales"], "dire": ["formulation type mot pour mot"]}],
  "grille": ["ce qui rapporte à la station (critères observables ; ancres 1–5 de la KK « construites, non officielles »)"],
  "erreurs": ["..."], "exemple_station": "mini-scénario de 3 à 5 lignes avec la réponse attendue",
  "liens": ["S-xx", "SY-xx", "A-xx"], "sources": ["…"] }
Doses éventuelles : AIPS suisse seulement, mot pour mot (aips_fiche.py). Aucune image générée ; image réelle libre facultative.
