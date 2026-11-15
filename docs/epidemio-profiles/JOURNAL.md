# Journal : injection épidémiologie PROFILES 2023 (15.11.2026, heure de Zurich)

- 18:40 : la capture MHT est décodée proprement : partie HTML n° 11 (iframe Google Sites), UTF-8, binaire.
- 19:10 : `parse_mht.py` extrait 221 valeurs et 194 entités ; les compteurs 82/49/43/47 concordent (PASS).
- 19:20 : `mapping.py` rattache les 221 valeurs à leur LOT par le code SSP ; le nom du DX est contrôlé contre le titre du cours de référence.
- 19:35 : `inject.py --dry-run` rend `DRYRUN.md` ; les règles de prudence s'ajoutent : nom du DX vérifié au-delà du LOT 032, cours de remplissage écartés, LOTs 125 à 132 laissés aux agents.
- 19:50 : l'injection écrit 16 cours dans `out/stage` ; la relance donne 0 diff (idempotence) ; `verifier.py` rend PASS (taille, balises, marqueurs).
- 20:00 : `REFERENTIEL_EPIDEMIO_PROFILES.md` rejoint le dossier Brief ; `generer.py` ajoute la consigne aux deux briefs.
- 20:10 : la branche `leona/epidemio-profiles` reçoit les commits ; la PR s'ouvre sans fusion ni label.
- 19:10 : Vial demande la concordance avant toute injection ; `concordance.py` confronte en parallèle 239 cibles et télécharge 63 pages sources (cache disque, 3 essais).
- 19:15 : la revue écarte 11 faux positifs (autre mesure ou autre population) ; 19 valeurs restent concordantes.
- 19:20 : `inject_progression.py` prépare `Claude/FedMed_Progression.html` (11 valeurs, 10 cours embarqués, idempotent) ; le connecteur GitHub refuse ce fichier de 85 Mo (plafond de 8 Mo par fichier).
- 19:25 : les 10 cours sources reçoivent le même encadré ; la branche et la PR portent ces cours, la fusion attend la décision de Vial.
