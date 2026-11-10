# Journal — ordre de Vial du 10 novembre 2026

## État actuel

31 nouvelles leçons sont poussées : les 11 du LOT080, les 11 du LOT081 et 9 du LOT082. Aucun LOT n’a encore franchi P4. Le LOT080 est clos en REFUSE pour DX5 et DX6 après deux échecs P3. Le LOT081 a onze leçons auditées et sa PR567 attend la fusion automatique après synchronisation avec main et contrôles. Le LOT082 poursuit les audits et les deux dernières rédactions. Les 858 leçons existantes consolidées sont sur main.

## Historique de la première passe documentaire — état alors constaté

La mission de contenu reste non accomplie : aucune des 253 leçons des LOTs 080–102 n’est produite. Les 23 tentatives documentaires ont un audit indépendant P1 `NON_FRANCHIE` et aucun score clinique attribué (`score_pct: null`). Leurs branches sont poussées.

Les sources établissent des ordres partiels dans certains cadres (lombalgie commune en premier recours ; goutte dans la monoarthrite aiguë ; ulcère veineux parmi les plaies chroniques ; certains vertiges périphériques). Les paquets consultés ne démontrent pas dix positions pour les sélections complètes. Les diagnostics fourre-tout, dénominateurs incompatibles et registres historiques sans source ne sont pas convertis en rangs canoniques. Ces limites ne démontrent pas une absence de données dans toute la littérature.

Les preuves, candidats non classés, paquets, conditions de reprise et audits figurent dans chaque branche. Aucun gel, HTML, audit P3 ou manifeste de cours n’est déclaré. Le passage au LOT suivant a suivi l’instruction de Vial après chaque échec P1.

## Consolidation préalable

858 leçons existantes de mon ressort ont été récupérées en quinze passes de 60 au plus, avec comparaison de chaque blob et de chaque SHA-256. Neuf copies périmées ont été supprimées dans le ressort calculé. La carte brute et la provenance de chaque copie sont conservées dans `_outils/rapports/consolidation-20261110/`. Le pilote de session consomme une file dérivée parce que l’outil original ne retire pas de sa carte les copies déjà écrites. Dernière passe : zéro leçon à écrire.

[PR 516 fusionnée après CI verte](https://github.com/vialdjoukang-spec/organigramme-examen-federal/pull/516), commit `78d3abd2bab2f5ef465bd9d508c384cbcc4febb6`. Retard sur main vérifié nul avant fusion. Les 858 SHA-256 ont aussi été revérifiés sur main après fusion. Cette consolidation ne compte pas comme rédaction des leçons absentes.

## Branches de la première tentative — historique antérieur aux reprises

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


Dépôt individuel : LOT_080_Phase_B_V0_DX.2.html, 139357 octets, SHA256 8d108b7a840e35438372d39056340399a1fdfc12b8bd77155abfc6c82cfc00b2. Les audits médicaux sont consignés séparément ; le LOT n’est pas encore livré.


Dépôt individuel : LOT_080_Phase_B_V0_DX.8.html, 149535 octets, SHA256 73837389f7698495db62a33c5595cad534f3de49c9687a4c90d992c7045de093. Les audits médicaux sont consignés séparément ; le LOT n’est pas encore livré.


Dépôt individuel : LOT_080_Phase_B_V0_DX.3.html, 130755 octets, SHA256 c33f3efeac911563f7d25122905ee27b3d2e7ddef04f69aade7982486d4dfcb1. Les audits médicaux sont consignés séparément ; le LOT n’est pas encore livré.


Dépôt individuel : LOT_080_Phase_B_V0_DX.5.html, 100969 octets, SHA256 c5182997965c311b631bbb687f09ec398dbca0e898bf4457ca700a028d12e774. Les audits médicaux sont consignés séparément ; le LOT n’est pas encore livré.


Dépôt individuel : LOT_080_Phase_B_V0_DX.1.html, 140188 octets, SHA256 90d58f32ca79e5f972daccb57b4d378221c31d354393e8822b1a705d09bc85e1. Les audits médicaux sont consignés séparément ; le LOT n’est pas encore livré.


Dépôt individuel : LOT_080_Phase_B_V0_DX.9.html, 154503 octets, SHA256 1b08b53bbe6fe14f5efa73e7afc2803315367c2776c853a9840d4fda7397c2a4. Les audits médicaux sont consignés séparément ; le LOT n’est pas encore livré.


Dépôt individuel : LOT_080_Phase_B_V0_DX.6.html, 108203 octets, SHA256 1a1dfac05b92b3832095731361ad2df714187f9335b17705326d2c17d07ed252. Les audits médicaux sont consignés séparément ; le LOT n’est pas encore livré.


Dépôt individuel : LOT_080_Phase_B_V0_DX.10.html, 170055 octets, SHA256 c64ceb661b4c8b9083f582ac6e314585c5180f6c8d8477fcfdb2713a392ba1ab. Les audits médicaux sont consignés séparément ; le LOT n’est pas encore livré.

LOT081 DX2 : dépôt individuel ; contrôle technique VERT, audit P3 indépendant à effectuer.

LOT081 DX5 : dépôt individuel ; contrôle technique VERT, audit P3 indépendant à effectuer.

LOT081 DX4 : dépôt individuel ; contrôle technique VERT, audit P3 indépendant à effectuer.

LOT081 DX1 : dépôt individuel ; contrôle technique VERT, audit P3 indépendant à effectuer.

LOT081 Phase A : dépôt individuel ; contrôle technique ORANGE (phrases verbales non reconnues par heuristique), aucun défaut A/C. Audit P3 indépendant à effectuer.

LOT081 DX7 : dépôt individuel ; contrôle technique ORANGE B seulement, audit P3 indépendant à effectuer.

LOT081 DX3 : dépôt individuel ; contrôle technique VERT, audit P3 indépendant à effectuer.

LOT081 DX6 : dépôt individuel ; contrôle technique VERT, audit P3 indépendant à effectuer. DX3 franchit P3 à48/52 ; DX7 à46/52 nécessite correction ciblée après sa première contrelecture.

LOT081 DX8 : dépôt individuel ; contrôle technique VERT, audit P3 indépendant à effectuer. DX4 et DX5 franchissent leur première contrelecture ; harmonisation des deux badges E de DX4 préparée.

LOT081 DX10 : dépôt individuel ; contrôle technique ORANGE B seulement, navigation vérifiée, audit P3 indépendant en cours.


LOT081 : PA, DX1 et DX10 corrigées et poussées ; contrelectures indépendantes franchies. Sept versions P3 validées (PA, DX1, DX3, DX4, DX5, DX8, DX10), empreintes dans VALIDATIONS_P3.json. DX6 en contrelecture finale ; DX2 en premier audit ; DX9 rédaction et DX7 correction à terminer.


LOT081 DX9 : dépôt individuel 187321 octets, contrôle ORANGE B seulement ; première contrelecture indépendante en cours. Les onze leçons sont écrites, huit versions validées P3.


LOT081 : dix versions ont franchi P3 ; DX2 corrigée est poussée et attend sa seconde contrelecture. Les onze structures finales passent les contrôles ; main intégré sans conflit. LOT082 P1 reprise franchie sur propositionv3, gel à effectuer sur sa branche.


LOT081 : onze leçons P2/P3 franchies, empreintes finales et navigation vérifiées. Main intégré sans conflit ; PR et CI en préparation, aucune fusion encore annoncée.


LOT082 : branche historique reprise et main intégré. Conflit limité au journal commun résolu avec la version de suivi la plus récente du LOT081, sans perdre ses22leçons poussées. PR567 LOT081 ouverte, CI en cours, fusion autorisée dès verte.


LOT082 DX3 : première leçon déposée individuellement ;170601octets, contrôleORANGE B seulement, auditP3 indépendant à effectuer. PR567LOT081 fusionautomatique activée souscontrôles, mainavanceencore ; aucunefusionannoncée.


LOT082 DX6 : dépôt individuel,129553octets, contrôleVERT zéro défaut ; contrelecture indépendante à effectuer.

LOT082 DX4 : leçon produite,155860octets, contrôle sans défautA/C ; DX3 reformaté sans modification clinique pour conserver les citations lisibles par le contrôleur. Audits indépendants en cours.

LOT082 DX8 : fracture déplacée du radius produite,105119octets, contrôleVERT zéro défaut ; P3 indépendant requis. PR567 : main intégré à nouveau avant fusion autorisée.

LOT082 DX2 : hallux valgus produit,191704octets, contrôleVERT ; contrelecture indépendante requise. DX6 premierP3 46/52, correction ciblée demandée avant secondelecture.

LOT082 DX7 : scoliose idiopathique de l’adolescent produite,169831octets, contrôleORANGE B seulement ; auditindépendant requis.

LOT082 DX1 : arthrose déformante de la main produite,151447octets, contrôleORANGE B seulement ; P3 indépendant requis.

LOT082 DX9 : Charcot du pied diabétique produit,191679octets, contrôleORANGE B seulement ; P3 indépendant engagé. DX8 premierP3non avec correction pharmacologique pédiatrique demandée.

LOT082 PhaseA : leçon générale produite,194464octets ; contrôleORANGE B seulement, audit indépendant demandé.

LOT082 DX6 : version corrigée138039octets, secondeP3 indépendante51/52finaleoui ; premièreversion conservée danshistoriqueGit.

LOT082 DX8 : corrections ciblées120830octets, notamment intervalle pédiatrique paracétamol, syndrome de loge et fracture ouverte ; secondeP3 à effectuer.

LOT082 DX9 : restriction ESUR mère enceinte ou allaitante insuffisante rénale complétée ;194255octets, secondeP3 indépendante engagée.

LOTs livrés : 0/23 ; leçons poussées : 31/253 après poussée de ce commit, 858 existantes consolidées ; blocages : LOT080 DX5 et DX6 REFUSE P3 ; LOT081 PR567 CI/fusion en cours ; LOT082 production/audits en cours ; LOT083–102 à produire.
