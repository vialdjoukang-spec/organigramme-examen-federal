# Épidémiologie PROFILES 2023 : concordance puis injection des seules valeurs prouvées

Le référentiel (221 valeurs, 194 entités) vient de la capture « Audit Épidémiologique PROFILES 2023 (248 SSP) » du 15.11.2026.

## Résultat de la concordance
- 19 valeurs sont concordantes : le cours de référence donne le même chiffre dans une phrase citée, la page de la source le contient, et la revue confirme la même mesure et la même population.
- 67 valeurs sont discordantes et 135 restent non vérifiables ; `NON_INJECTE.md` donne le motif de chacune.
- Ce lot n'injecte que 11 valeurs concordantes (10 cours des LOTs 001 à 032) ; 4 valeurs sont refusées pour la taille (cours ≥ 150 000 octets) et 4 visent des LOTs absents de la plateforme.

## Fichiers
- `CONCORDANCE.md`, `CONCORDANCE.csv`, `concordance.json` : statut, preuve dans le cours et URL de la source pour chaque valeur.
- `NON_INJECTE.md` : valeurs discordantes ou non vérifiables, avec leur motif.
- `REFERENTIEL_EPIDEMIO_PROFILES.md`, `referentiel.json`, `referentiel.csv` : référentiel complet, lisible sur téléphone.
- Scripts : `tools/epidemio_profiles/` ; `concordance.py` lance la légion (16 processus pour les cours, 24 fils pour les sources).

## Règles
L'encadré se place à la fin du point 2 Épidémiologie, entre `<!-- EPI_PROFILES:DEBUT DXn -->` et `<!-- EPI_PROFILES:FIN DXn -->` ; une relance le régénère à l'identique. Aucun chiffre existant n'est remplacé.
