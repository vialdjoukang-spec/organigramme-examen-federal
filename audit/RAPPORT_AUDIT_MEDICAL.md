# Rapport d'audit médical : les fautes corrigées

Galien, auditeur médical et linguistique, relit chaque groupe de prévalence des diagnostics différentiels (data/ck/prev.json) juste après qu'Asclépios l'a poussé. Chaque ligne nomme le SSP, la faute, la correction, la source relue et le type de faute. Les fautes critiques, qui touchent la sécurité du patient, figurent aussi dans la section « Fautes critiques pour Vial ».

## Fautes critiques pour Vial

Aucune faute critique pour l'instant.

## G1 · thorax (S2.4, S2.5) · PR #43 · relu le 17.10.2026

Les 11 chiffres d'Asclépios ont été recalculés sur le tableau 1 de Verdon 2008 (n = 672) : tous sont exacts, et l'ordre décroissant est juste.

| SSP | Avant | Après | Source | Type |
|---|---|---|---|---|
| S2.4, S2.5 | L'angor stable manquait aux différentiels, alors qu'il est la 2e cause de douleur thoracique en médecine de famille romande. | Le différentiel « Angor stable (syndrome coronarien chronique) » a été ajouté avec 11,2 % (75 sur 672), son texte de fenêtre et ses sources ; il s'affiche au 2e rang. | R-VERDON-SMW-2008, tableau 1 (Acute angina 75/672) et Résultats ; ESC 2024, syndromes coronariens chroniques (étapes 1 à 3 : coroscanner si la vraisemblance est de > 5 à 50 %, imagerie de stress si elle est de > 15 à 85 %) ; ESC 2023, SCA (angor instable), lus le 2026-10-17 | Médical (majeure) |
| S2.4 | La note de « Douleur pariétale » (48,7 %) ne citait que les 287 syndromes de la paroi thoracique. | La note détaille tout le groupe : 26 traumatismes, dont 7 fractures de côte, 7 douleurs projetées et 7 métastases costales, que le clinicien ne doit pas manquer. | R-VERDON-SMW-2008, tableau 1, lu le 2026-10-17 | Médical (mineure) |
| S2.4 | Le cadre disait que la gêne thoracique était comprise dans l'étude, ce que la source n'écrit pas. | Le cadre reprend les critères de la source : patients de plus de 16 ans, douleur thoracique comme symptôme principal ou accessoire ; il précise que l'étude ne distingue pas la gêne de la douleur. | R-VERDON-SMW-2008, Méthodes, lu le 2026-10-17 | Médical (mineure) |
