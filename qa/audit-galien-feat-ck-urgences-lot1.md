# Audit médical de niveau 2 · chaîne clinique des urgences, lot 1 · branche feat/ck-urgences-lot1

**Relecteur** : Podalire, auteur du lot, selon la méthode de Galien (skill ssp-audit-medical). **Date** : 17.10.2026, Europe/Zurich.
**Statut** : relecture d’auteur. Elle ne remplace pas la contre-lecture indépendante de Galien, qui reste exigée (étiquette audit:galien).

## Méthode

Le relecteur a lu le diff de `data/ck` par rapport à `origin/main` (hyp, syn, glo, src, loc) et les signalements de niveau 1 (`tools/audit/niveau1.py` : G1 à G8 réussis, Lyncée sans terme nouveau). Il a confronté chaque affirmation à risque au paragraphe exact de sa source, relu le 17.10.2026 : ESC 2023 SCA, ESC 2019 EP, ESC 2024 aorte (§ 9.3), SSC 2021, EAACI 2021, JBDS 2023, DGN S2k état de mal, ESCMID 2016, ERC 2021. Les hypothèses et les syndromes n’ont pas de champ région : la région du registre a été choisie d’après l’organe (CœurThorax, Neuro).

## Rapport d’audit médical : les fautes corrigées

Trois fautes mineures ont été corrigées, chacune par son propre commit ; leurs lignes figurent dans `qa/audit/fautes.jsonl` et `qa/audit/RAPPORT_FAUTES.md`.

1. `hyp|sca`, premier moyen : la coronarographie dans les 24 heures du NSTE-ACS à haut risque était écrite comme systématique ; la ligne directrice la classe « à envisager ». Correction : « s’envisage ».
2. `hyp|sca`, limites de l’angioplastie primaire : la limite des 48 heures manquait (l’angioplastie de routine d’une artère occluse n’est plus recommandée après 48 heures sans symptôme persistant). Correction : limite ajoutée.
3. `hyp|etat-de-mal-epileptique`, deuxième moyen : l’absence d’autorisation du lévétiracétam dans l’état de mal était limitée à l’Allemagne ; la ligne directrice l’écrit pour l’Europe. Correction : « en Europe ».

Corrections faites pendant la rédaction, avant le premier commit, donc sans ligne de registre : définition du choc septique alignée sur l’ERC ; démarrage périphérique bref de la noradrénaline admis (SSC, recommandations 43 et 44) ; rythme de surveillance de l’acidocétose (60 minutes, 2 heures, puis toutes les 2 heures) ; justification non sourcée de la dexaméthasone retirée ; rôle de l’équipe pluridisciplinaire de l’EP écrit « peut organiser ».

## Points vérifiés sans faute

- La fosphénytoïne n’est pas autorisée en Suisse : la ligne directrice DGN l’écrit dans sa remarque sur le statut d’autorisation.
- L’arrêt de la dexaméthasone si le germe n’est ni Haemophilus influenzae ni le pneumocoque, et son début possible jusqu’à 4 heures après l’antibiotique, figurent dans l’ESCMID (grades B et C).
- Les glucocorticoïdes « pourraient être délétères chez l’enfant » figure dans l’EAACI.
- L’hypoglycémie après insuline et glucose « jusqu’à 28 % » figure dans l’ERC.
- La mortalité de la dissection de type A sans chirurgie (environ 50 % en 48 heures, 1 à 2 % par heure) et la mortalité opératoire (17 à 25 %) figurent dans l’ESC 2024 ; le TEVAR entre 14 et 90 jours aussi.

## Doutes laissés à Vial (aucun n’est classé critique)

- Aucune posologie n’est écrite : chaque dose et chaque volume restent « À vérifier » jusqu’à la lecture manuelle de l’AIPS par Galien.
- Contre-indications de la fibrinolyse et de la thrombolyse, traitement de la dissection quand les bêtabloquants sont contre-indiqués, complications du TEVAR et du coma thérapeutique : à lire dans les lignes directrices.
- Ligne POCUS du pneumothorax sous tension et analgésie de la thoracostomie : « À vérifier ».
- Sources hors Suisse : SSC est internationale (copubliée par l’ESICM) ; JBDS est britannique et son DOI vise la version 2022, alors que le texte lu est la révision de mars 2023 ; la validité AWMF du DGN état de mal est échue depuis 2025.

## Ce que cet audit ne couvre pas

Les 44 entrées nouvelles du glossaire n’ont pas d’entrée dans `qa/audit/glo-meta.json`, donc `galien_region.py travail` ne les distribue à aucun automate régional ; leur contre-lecture revient à Galien. L’outil `corriger` ne sait pas modifier un champ imbriqué de hyp.json : les trois corrections ont été faites par commit direct, avec la même ligne « Registre » que l’outil.
