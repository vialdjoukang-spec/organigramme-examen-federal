# Journal — ordre de Vial du 10 novembre 2026

## Résultat de la mission

La mission de contenu reste non accomplie : aucune des 253 leçons des LOTs 080–102 n’est produite. Les 23 tentatives documentaires ont un audit indépendant P1 `NON_FRANCHIE` et aucun score clinique attribué (`score_pct: null`). Leurs branches sont poussées.

Les sources établissent des ordres partiels dans certains cadres (lombalgie commune en premier recours ; goutte dans la monoarthrite aiguë ; ulcère veineux parmi les plaies chroniques ; certains vertiges périphériques). Les paquets consultés ne démontrent pas dix positions pour les sélections complètes. Les diagnostics fourre-tout, dénominateurs incompatibles et registres historiques sans source ne sont pas convertis en rangs canoniques. Ces limites ne démontrent pas une absence de données dans toute la littérature.

Les preuves, candidats non classés, paquets, conditions de reprise et audits figurent dans chaque branche. Aucun gel, HTML, audit P3 ou manifeste de cours n’est déclaré. Le passage au LOT suivant a suivi l’instruction de Vial après chaque échec P1.

## Consolidation préalable

858 leçons existantes de mon ressort ont été récupérées en quinze passes de 60 au plus, avec comparaison de chaque blob et de chaque SHA-256. Neuf copies périmées ont été supprimées dans le ressort calculé. La carte brute et la provenance de chaque copie sont conservées dans `_outils/rapports/consolidation-20261110/`. Le pilote de session consomme une file dérivée parce que l’outil original ne retire pas de sa carte les copies déjà écrites. Dernière passe : zéro leçon à écrire.

[PR 516 fusionnée après CI verte](https://github.com/vialdjoukang-spec/organigramme-examen-federal/pull/516), commit `78d3abd2bab2f5ef465bd9d508c384cbcc4febb6`. Retard sur main vérifié nul avant fusion. Les 858 SHA-256 ont aussi été revérifiés sur main après fusion. Cette consolidation ne compte pas comme rédaction des leçons absentes.

## Branches de tentative

| LOT | Branche et preuves | Verdict | Premier motif |
|---|---|---|---|
| LOT_080 | [codex/lot-080](https://github.com/vialdjoukang-spec/organigramme-examen-federal/tree/codex/lot-080/ChatGPT_Codex/LOT_080) | NON_FRANCHIE | Les proportions idiopathiques/secondaires portent sur les scolioses et ne classent pas toutes les causes de posture anormale. |
| LOT_081 | [codex/lot-081](https://github.com/vialdjoukang-spec/organigramme-examen-federal/tree/codex/lot-081/ChatGPT_Codex/LOT_081) | NON_FRANCHIE | La première place de la lombalgie commune est explicitement soutenue par HUG2022 ; cela ne constitue pas dix positions étiologiques. |
| LOT_082 | [codex/lot-082](https://github.com/vialdjoukang-spec/organigramme-examen-federal/tree/codex/lot-082/ChatGPT_Codex/LOT_082) | NON_FRANCHIE | La proposition ne comporte que six candidats et deux restent des catégories à préciser, plutôt que dix diagnostics définis. |
| LOT_083 | [codex/lot-083](https://github.com/vialdjoukang-spec/organigramme-examen-federal/tree/codex/lot-083/ChatGPT_Codex/LOT_083) | NON_FRANCHIE | La source2023 identifie effort, traumatisme, médicaments et infections virales parmi les causes les plus courantes sans leur donner un ordre interne. |
| LOT_084 | [codex/lot-084](https://github.com/vialdjoukang-spec/organigramme-examen-federal/tree/codex/lot-084/ChatGPT_Codex/LOT_084) | NON_FRANCHIE | Les extraits Unisanté décrivent les caractéristiques et atypies des polyneuropathies, tandis que l’ESC documente la menace ischémique aiguë : ils étayent le triage, sans établir dix fréquences relatives. |
| LOT_085 | [codex/lot-085](https://github.com/vialdjoukang-spec/organigramme-examen-federal/tree/codex/lot-085/ChatGPT_Codex/LOT_085) | NON_FRANCHIE | HUG2024 soutient la prédominance microcristalline, en particulier la goutte, dans la monoarthrite aiguë non traumatique ; ce cadre ne couvre pas toutes les plaintes chroniques et polyarticulaires de la SSP. |
| LOT_086 | [codex/lot-086](https://github.com/vialdjoukang-spec/organigramme-examen-federal/tree/codex/lot-086/ChatGPT_Codex/LOT_086) | NON_FRANCHIE | Les extraits décrivent surtout les affections buccales ; la couverture génitale et périanale du libellé SSP n’est pas documentée dans la préparation. |
| LOT_087 | [codex/lot-087](https://github.com/vialdjoukang-spec/organigramme-examen-federal/tree/codex/lot-087/ChatGPT_Codex/LOT_087) | NON_FRANCHIE | La documentation est principalement pédiatrique ; l’incidence du PTI chez les enfants et la rareté du PTT parmi les microangiopathies ne classent pas les causes de toute ecchymose, tout hématome ou purpura. |
| LOT_088 | [codex/lot-088](https://github.com/vialdjoukang-spec/organigramme-examen-federal/tree/codex/lot-088/ChatGPT_Codex/LOT_088) | NON_FRANCHIE | Paediatrica porte sur l’hypopigmentation de l’enfant, le résumé SONAR sur une classification et le vitiligo parmi les dépigmentations auto-immunes, et USZ sur le mélasma. |
| LOT_089 | [codex/lot-089](https://github.com/vialdjoukang-spec/organigramme-examen-federal/tree/codex/lot-089/ChatGPT_Codex/LOT_089) | NON_FRANCHIE | HUG et USZ soutiennent la prédominance veineuse parmi les ulcères ou plaies chroniques ; cette information est utile et ne doit pas être rejetée faute d’une cohorte unique. |
| LOT_090 | [codex/lot-090](https://github.com/vialdjoukang-spec/organigramme-examen-federal/tree/codex/lot-090/ChatGPT_Codex/LOT_090) | NON_FRANCHIE | Les extraits HUG décrivent le métabolisme et des mécanismes d’hyperbilirubinémie, sans fournir un ordre de fréquence parmi les patients ictériques. |
| LOT_091 | [codex/lot-091](https://github.com/vialdjoukang-spec/organigramme-examen-federal/tree/codex/lot-091/ChatGPT_Codex/LOT_091) | NON_FRANCHIE | Le CHUV soutient la première place du syndrome des ovaires polykystiques parmi les hirsutismes et la rareté relative des tumeurs dans ce cadre. |
| LOT_092 | [codex/lot-092](https://github.com/vialdjoukang-spec/organigramme-examen-federal/tree/codex/lot-092/ChatGPT_Codex/LOT_092) | NON_FRANCHIE | Les extraits HUG 2025 définissent l’acné et signalent des diagnostics tumoraux graves ; les extraits de 2018 donnent un ordre partiel au sein des toxidermies. |
| LOT_093 | [codex/lot-093](https://github.com/vialdjoukang-spec/organigramme-examen-federal/tree/codex/lot-093/ChatGPT_Codex/LOT_093) | NON_FRANCHIE | La préparation propose huit diagnostics, sans atteindre la liste de dix requise à P1. |
| LOT_094 | [codex/lot-094](https://github.com/vialdjoukang-spec/organigramme-examen-federal/tree/codex/lot-094/ChatGPT_Codex/LOT_094) | NON_FRANCHIE | La préparation ne contient que sept candidats et le dernier conserve un libellé à préciser. |
| LOT_095 | [codex/lot-095](https://github.com/vialdjoukang-spec/organigramme-examen-federal/tree/codex/lot-095/ChatGPT_Codex/LOT_095) | NON_FRANCHIE | La préparation propose seulement quatre candidats et ne soumet pas dix diagnostics distincts. |
| LOT_096 | [codex/lot-096](https://github.com/vialdjoukang-spec/organigramme-examen-federal/tree/codex/lot-096/ChatGPT_Codex/LOT_096) | NON_FRANCHIE | La proposition ne contient que sept candidats, sans liste de dix soumise à la porte P1. |
| LOT_097 | [codex/lot-097](https://github.com/vialdjoukang-spec/organigramme-examen-federal/tree/codex/lot-097/ChatGPT_Codex/LOT_097) | NON_FRANCHIE | La source RMS soutient explicitement la prééminence qualitative du tremblement essentiel ; cet argument de première place est recevable dans sa portée. |
| LOT_098 | [codex/lot-098](https://github.com/vialdjoukang-spec/organigramme-examen-federal/tree/codex/lot-098/ChatGPT_Codex/LOT_098) | NON_FRANCHIE | La préparation propose quatre causes et ne fournit pas la sélection de dix requise à P1. |
| LOT_099 | [codex/lot-099](https://github.com/vialdjoukang-spec/organigramme-examen-federal/tree/codex/lot-099/ChatGPT_Codex/LOT_099) | NON_FRANCHIE | HUG 2024 donne un ordre qualitatif recevable en premier recours : VPPB, vestibulopathie unilatérale aiguë, maladie de Ménière ; cette information est vérifiée indépendamment. |
| LOT_100 | [codex/lot-100](https://github.com/vialdjoukang-spec/organigramme-examen-federal/tree/codex/lot-100/ChatGPT_Codex/LOT_100) | NON_FRANCHIE | La préparation comporte dix candidats identifiables et des comparaisons partielles recevables entre céphalées primaires et secondaires. |
| LOT_101 | [codex/lot-101](https://github.com/vialdjoukang-spec/organigramme-examen-federal/tree/codex/lot-101/ChatGPT_Codex/LOT_101) | NON_FRANCHIE | Le document Swiss Memory Clinics fournit un cadre diagnostique, des comorbidités à rechercher et un groupe de causes non dégénératives potentiellement guérissables. |
| LOT_102 | [codex/lot-102](https://github.com/vialdjoukang-spec/organigramme-examen-federal/tree/codex/lot-102/ChatGPT_Codex/LOT_102) | NON_FRANCHIE | Les extraits CHUV/Pedlaus et CEN établissent une priorité urgente pour un déficit brutal suspect d’AVC ; ils ne donnent pas un ordre de fréquence pour dix causes de parésie ou paralysie. |

## Vérifications et limites

- Les 23 commits de tentative correspondent aux branches réellement poussées. Leurs différences ne portent que sur le dossier du LOT concerné et ce journal.
- Les 23 empreintes des préparations, paquets et audits concordent. Les collecteurs sont distincts de l’auditeur ; les rapports précisent les lectures primaires ou partielles réellement réalisées.
- Les outils de référence sont inchangés ; seuls des copies et pilotes de session figurent dans `_outils/`. Aucun chiffre ou dose nouvelle n’a été ajouté à un cours.
- L’environnement a été réinitialisé pendant la poussée du LOT100. Les commits déjà poussés ont été vérifiés ; le commit100 conservé localement a été poussé, puis les LOTs101 et102 ont été archivés.
- Images et perfectionnement sont restés hors mission. Aucune PR de livraison n’a été ouverte pour les LOTs bloqués. Le relevé complet est dans `_outils/rapports/BILAN_080_102_20261110.json`.

- Détection finale : 364 branches, 1973 leçons trouvées ; aucune des 253 leçons 080–102. Jauges régénérées avec progression.py. La nouvelle carte est conservée dans `_outils/rapports/carte_finale_20261110.json`.


## Reprise demandée par Vial

La conclusion précédente est un état historique, pas une clôture. Vial demande de poursuivre jusqu’à la fin des LOTs. Reprise au LOT080 : approfondissement des sources de la liste et rédaction des fragments de Phase A en parallèle. Les fragments restent préparatoires tant que les portes ne sont pas franchies.


### LOT080 — première leçon rédigée

P1 franchie après recontrôle indépendant ; liste gelée et cadres de classement conservés. Phase A assemblée, 171803 octets, 14 points, 155 références citées (dont la consigne éditoriale de la question finale). Contrôle3 ORANGE, sans défaut A ou C ; audit médical P3 en cours. La présence du fichier poussé ne signifie pas que le LOT est livré. Les dix DX sont en rédaction parallèle.


Phase A corrigée : 172129 octets, P3 VERT 92,59 %, finale oui, sans critique. DX4 rédigé : 112791 octets, contrôle VERT ; P3 en cours.


DX7 rédigé : 187499 octets, quatorze points et posologie Celebrex fondée sur AIPS54994. Contrôle ORANGE B uniquement, audit médical en cours.

LOTs livrés : 0/23 (080–102) ; leçons poussées : 3/253 nouvelles, 858 existantes consolidées ; blocages : huit DX du LOT080 à pousser et audits DX en cours ; LOT081–102 à produire.
