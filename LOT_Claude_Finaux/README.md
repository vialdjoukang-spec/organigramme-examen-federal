# LOT_Claude_Finaux — dépôt final des LOTS audités

Un LOT n'entre ici qu'après audit conforme au PROMPT ULTIME V0 (≥ 90 %, zéro critique, question finale « oui », LOT COMPLET, `controle_lot.py verifier` = CONFORME).

```text
LOT_Claude_Finaux/
├── README.md                 ce fichier
├── CATALOGUE_248.csv         248 SSP PROFILES 2023 (FR | EN), statut FAIT / NON_FAIT
├── ETAT_FILE.json            file des 75 LOTS FAIT, cycles, scores, verdicts
├── PROGRESSION.html          vue de progression (créée à la première étape)
├── ARRET.md                  présent seulement si la mission s'est arrêtée (cause, état, suite)
├── HELP_QUESTIONNAIRE/       lacunes reportées après validation d'un LOT
├── _OBSOLETES/               versions remplacées (suffixe _OBSOLETE_), jamais supprimées
└── LOT_XXX/
    ├── LOT_XXX_Phase_A_V0.html
    ├── LOT_XXX_Phase_B_V0_DX.1.html … LOT_XXX_Phase_B_V0_DX.10.html
    ├── MANIFESTE.json        nom, octets, SHA-256 de chacun des 11 fichiers
    └── audits/               rapports médical et linguistique par fichier
```

Ko = 1 000 octets. Chaque HTML pèse 150–200 Ko. Aucun HTML consolidé.
