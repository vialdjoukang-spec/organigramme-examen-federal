# Contre-audit V3 — PP-S9 à PP-S12 (vérification finale)

Auditeur indépendant, 14.11.2026. J'ai contrôlé seulement N1, N2, N3, M15 et les légers N4 à N10, par lecture des JSON. J'ai vérifié par script la validité JSON des 36 fiches et de `recensement_sf.json`, et l'absence de dose. Ni commit ni push.

| # | Statut | Constat |
|---|---|---|
| N1 Valproate | Corrigé | La fiche reprend la formulation de Swissmedic, Vigilance-News éd. 32, messages-clés 2 et 3, que j'ai lus dans le PDF au tour V2. Elle reprend la contre-indication chez la femme en âge de procréer, sauf programme de prévention de la grossesse, et pendant la grossesse dans le trouble bipolaire, ainsi que le risque de troubles neurodéveloppementaux par voie paternelle. La source porte le statut « lu », avec citation. |
| N2 LAP | Corrigé | Le syndrome de différenciation et son traitement par corticoïdes figurent. |
| N3 Angio-œdème sous IEC | Corrigé | Le texte dit « se discutent hors indication… sans efficacité démontrée » et place les voies aériennes en premier. |
| M15 | Corrigé | Le libellé « …liée aux antirésorbeurs (bisphosphonates, dénosumab) » figure dans PP-S9-Ia et dans `recensement_sf.json` ligne 3771 ; `nom_audit` est supprimé ; le JSON est valide. |
| N4 | Corrigé | `EX-1-S1-lcr-pcr-multiplex` est en tête des renvois. |
| N5 | Corrigé | Le texte précise « statut Swissmedic non vérifié ». |
| N6 | Corrigé, avec une réserve mineure | Le champ `renvoi_fiche` contient une phrase au lieu d'un identifiant, et PP-S9-D ne mentionne pas l'épiphysiolyse. PATCH facultatif : `"renvoi_fiche": "PP-S9-D"`. Ce point ne bloque pas. |
| N7 | Corrigé | La séquence de traitement de l'arthrite de Lyme est exacte. |
| N8 | Corrigé | L'aspirine et l'HBPM remplacent les AVK pendant la grossesse. |
| N9 | Corrigé | L'anémie fœtale et l'anasarque figurent. |
| N10 | Corrigé | Le texte dit « (AIPS suisse, non lu) ». |

## Les 17 omissions « Moyen » restantes

**Elles ne bloquent pas la publication.** Ce sont des compléments de couverture, non des erreurs ni des risques de sécurité :
- toutes les urgences et pièges de sécurité signalés (« Grave ») sont traités ;
- aucune phrase publiée n'est fausse du fait de ces absences.

Condition de publication : les lister dans un champ ou un fichier « compléments à venir », avec leur fiche cible, sans prétendre à l'exhaustivité.
- **S9** : sclérodermie et Raynaud (A), Paget (D), SDRC (F), achondroplasie (C), fracture atypique du fémur (Ia), tuberculose ostéo-articulaire (I).
- **S10** : méthémoglobinémie (Ia), SHU (renvoi PP-S6-V), MGUS (T).
- **S11** : Wernicke-Korsakoff (F), intoxication au lithium (Ia, renvoi PP-S8-Ia), syndrome post-commotionnel (Tr).
- **S12** : lichen plan (A), syphilis secondaire (I), varicelle et verrues (I), mycosis fongoïde (T), hidradénite suppurée (F).

Réserve de sources, maintenue et à consigner : aucune recommandation de société suisse n'a été lue en entier. Seules les pages Swissmedic ont été lues.

## Verdict

**OUI : `audit-ok` est accordé, sous deux réserves consignées et non bloquantes :**
1. la liste des 17 compléments à venir ;
2. la lecture intégrale d'au moins une recommandation suisse par système au prochain cycle.
