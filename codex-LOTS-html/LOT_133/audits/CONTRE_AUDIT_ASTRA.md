# Contre-audit médical ciblé — Phase A du LOT 133

Date : 2026-11-02T01:38:14.080062+00:00. Auditeur indépendant du rédacteur : `astra_medical133`. Aucun score numérique, gel de liste ou validation médicale humaine.

**Verdict : corrections ciblées recevables ; réserves documentaires globales maintenues.** Aucune erreur clinique nouvelle identifiée dans les ajouts examinés sur l’appel 144, la méningococcémie et la surveillance de l’insuffisance cardiaque. Ce verdict ne valide pas les dix parcours diagnostiques.

Version HTML auditée : 84 575 octets, SHA-256 `983751389e008283739dda8fc65f0672ddf2842513dcffd9c399cd0644fe5739`. Comparaison ciblée aux constats du rapport `MEDICAL_ASTRA.md` et aux passages antérieurement lus ; lecture de `_travail/PHASE_A_REDACTION.md` points 4/10/11/12, des entrées pertinentes de `_travail/phase_a.py` et des infobulles HTML 4/7/8/9/10/11/12. Aucun diff Git ni lecture intégrale du HTML. Concordance constatée entre rédaction, tableau générateur et rendu textuel HTML sur ces corrections.

| Correction | Résultat | Justification et limite |
|---|---|---|
| Appel 144 devant déficit neurologique brutal, même régressif | Recevable — P4/P10/P11 et DX.1 | HUG AVC/AIT demande une hospitalisation urgente et l’appel sans tarder au 144, même si les signes disparaissent. La notation de l’heure ne doit pas retarder l’appel, désormais explicite. |
| Étouffement, douleur thoracique, malaise/perte de connaissance | Recevable dans le contexte documenté — P4/P10/P12 et DX.7 | Le tableau de la brochure HUG insuffisance cardiaque prescrit l’appel immédiat pour chacun de ces signes. P4/P12 identifient la population et la source ; P10 renvoie à P4. Ne pas présenter cette brochure comme protocole diagnostique universel du malaise. |
| Purpura préoccupant et suspicion de méningococcémie | Recevable — P4/DX.2 | La source HUG pédiatrique fait rechercher et traiter rapidement une suspicion de méningococcémie. L’ajout « suspecté » et la distinction entre non-blanchiment et sepsis sont pertinents. Portée pédiatrique et autres causes préservées ; pas de seuil ni de dose transposé. |
| Surveillance et prévention de l’aggravation d’une IC connue | Recevable — P10/P12 et résumé P12 | Traitement prescrit, activité adaptée, poids quotidien dans les mêmes conditions, souffle et œdèmes correspondent à la brochure. Le texte distingue contact médecin/infirmier et appel 144 et précise qu’il ne confirme pas une IC. Aucun seuil pondéral universel ajouté. |
| Stabilisation sans attendre un bilan exhaustif | Recevable comme principe d’urgence | Cohérent avec les filières d’alerte HUG et l’absence de délai induit. Le texte ne prétend pas décrire un protocole thérapeutique complet. |
| Absence de posologie nouvelle | Constat confirmé sur les ajouts | Pas de prescription chiffrée. L’obligation AIPS pour toute future dose reste explicite ; aucune validation posologique extrapolée des PDF. |

## Réserves toujours ouvertes avant tout gel

| Domaine | Lacune restante et suite |
|---|---|
| Population et liste | Dix exemples pédagogiques non exhaustifs, mélange assumable de syndromes et maladies. La population visée et la justification de sélection doivent être définies ; aucun ordre suisse de fréquence n’est démontré. |
| DX.1/DX.2/DX.7 | L’alerte est améliorée, mais HUG AVC/AIT est informatif, le purpura est pédiatrique et la brochure IC porte sur le suivi : ces lectures ne suffisent pas à valider toutes les étapes spécialisées de confirmation. |
| DX.3/DX.4/DX.5/DX.6 | Sources spécifiques CH/UE et bilan initial/confirmation encore à compléter selon population. Pas de nouvelle preuve suffisante dans cette correction. |
| DX.8 | « Choisir le parcours de confirmation » reste trop vague ; documenter le parcours de suspicion de TVP et l’évaluation en l’absence de symptômes respiratoires. |
| DX.9/DX.10 | Source spécifique pour thrombopénie, critères d’hippocratisme, autres causes et exploration bronchopulmonaire toujours nécessaire. |
| P8/P9 | La promesse de sourcer les critères dans une version future reste présente ; les moyens de confirmation de plusieurs DD restent non nommés. |
| Sources générales | NHS britannique reste hors CH/UE ; introduction UNESS seule ne valide pas l’ensemble du cours. La correction n’a pas résolu ces lacunes de couverture. |

## Preuves relues

Les passages pertinents ont été relus dans les caches acquis directement avec HTTP 200 le 02.11.2026 lors du premier audit ; pas de nouvelle récupération réseau nécessaire.

| Source | Passage contrôlé | Cache local ignoré |
|---|---|---|
| [HUG AVC/AIT](https://www.hug.ch/accident-vasculaire-cerebral/qu-est-qu-avc-ait) | Signes d’alerte et appel 144 même après disparition des symptômes. | `_travail/_cache/astra/astra_hug_avc.txt` |
| [HUG pétéchies fébriles](https://www.hug.ch/sites/interhug/files/structures/saup_professionnels/Procedures_medicales/les_petechies_febriles_algorithme_update_18.02.2026.pdf) | Mauvais état général, suspicion de méningococcémie et note sur risque non nul avec peu de pétéchies. | `_travail/_cache/astra/astra_hug_petechies.txt` |
| [HUG contrôle de l’insuffisance cardiaque](https://www.hug.ch/sites/interhug/files/documents/insuffisance_cardiaque.pdf) | Tableau d’appel 144 ; traitement, poids, souffle, œdèmes et recours. | `_travail/_cache/astra/astra_hug_ic.txt` |

URL, dates, empreintes et limites de lecture conservées dans `evidence/astra_lectures.json`. Aucun texte intégral réintroduit dans les preuves publiables. Aucun HTML modifié par le contre-auditeur. Prochaine étape : documentation des lacunes persistantes, puis contrelecture des nouveaux parcours avant gel ; le présent rapport ne vaut pas levée de ces réserves.

Vérification de concurrence : le rédacteur a retiré la consigne de licence du contenu du cours pendant la contrelecture ; version finale contrôlée de 84 575 octets, empreinte ci-dessus. Cette suppression documentaire ne modifie pas les corrections cliniques auditées.
