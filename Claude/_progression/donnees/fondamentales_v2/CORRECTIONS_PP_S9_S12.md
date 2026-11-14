# Corrections après audit : PP-S9 à PP-S12

Rédacteur : agent PP S9 à S12, le 14.11.2026, en réponse à `AUDIT_PP_S9_S12.md`. Ni commit ni push.
Les 36 JSON sont réécrits et validés automatiquement : 0 erreur, 140 affections (121 avant audit, 19 ajoutées).
Le validateur contrôle les renvois SY, S, IMG, EX et PH contre les catalogues, l'absence de dose, le cadrage conservé en tête de liste et l'absence de sources hors sujet.
Les affections ajoutées sont listées dans le champ `ajouts_audit` de chaque fiche.

## Sources (S1 à S6)

| # | Correction appliquée |
|---|---|
| S1 | Chaque fiche porte désormais ses propres sources. La base de chaque système se limite à la société suisse, à la société européenne et à la déduction. La source Fluoroquinolones ne figure plus que dans PP-S9-Ia, la source Métamizole que dans PP-S10-Ia, et l'OMS malaria que dans PP-S10-I. Les autres sources sont propres à la lettre (SSI, Swiss Orthopaedics, ASCO, SAKK, Swiss Memory Clinics, HUG, Tox Info Suisse, Ligue contre le cancer, etc.). |
| S2 | Dans PP-S10-I, Swiss TPH / ECTM (healthytravel.ch) passe avant l'OMS. La page d'accueil a été lue le 14.11.2026 (éditeur ECTM, secrétariat SSTTM aux HUG) ; les recommandations professionnelles sont sous accès restreint et n'ont pas été lues. |
| S3 | L'étiquette « Suisse, non vérifié CH » devient « Suisse », avec le statut « non lu ». |
| S4 | La déduction porte le statut « déduction de l'auteur, non sourcée ». |
| S5 | L'EPA est ajoutée comme source européenne à tout S11. La WFSBP ne reste que dans PP-S11-F, avec l'étiquette « source internationale (hors ordre CH/EU) ». |
| S6 | Il y a désormais au moins une source suisse lue ou résumée par système. S9 : Swissmedic Fluoroquinolones, **lu**. S10 : Swissmedic Métamizole, **lu**, et healthytravel.ch, résumé. S11 : Swissmedic Vigilance-News mai 2024 sur le valproate, résumé ; Pharmacie des HUG, récapitulatif des antidotes, résumé. S12 : Ligue contre le cancer (mélanome, protection solaire), résumé. Le statut reste « brouillon corrigé » ; `audit-ok` n'est pas posé. |

## Erreurs médicales (M1 à M18)

| # | Correction appliquée |
|---|---|
| M1 | Physostigmine (PP-S11-Ia) : elle se donne sous monitorage cardiaque et jamais si le QRS s'élargit (tricycliques), à cause du risque de bradycardie et d'asystolie. |
| M2 | Valproate (PP-S11-F, trouble bipolaire) : l'alerte tératogène est ajoutée avec le programme de prévention de la grossesse (Swissmedic ; AIPS à lire mot pour mot). Le renvoi `renvoi_pharmaco` est ajouté. |
| M3 | Le syndrome malin des neuroleptiques est ajouté à PP-S11-Ia (blocage D2, CK, dantrolène, bromocriptine). |
| M4 | CIVD : le TP (Quick, en %) baisse et le TCA s'allonge. |
| M5, M6 | AHAI froide : C3 est déposé et l'hémolyse est surtout extravasculaire hépatique. Les corticoïdes agissent peu dans la forme froide ; le rituximab supprime le clone B. |
| M7 | Spondylodiscite : le germe se fixe d'abord dans le plateau sous-chondral, puis gagne le disque. |
| M8 | Sarcomes : la chimiothérapie néoadjuvante concerne l'ostéosarcome et le sarcome d'Ewing ; le chondrosarcome se traite par chirurgie seule. |
| M9 | Métastases osseuses : la conduite d'urgence de la compression médullaire est ajoutée (corticoïdes, puis chirurgie ou radiothérapie). |
| M10 | Impétigo : la forme bulleuse (toxines, desmogléine 1) est distinguée de la forme croûteuse. |
| M11 | Statines : la myopathie nécrosante anti-HMGCR est ajoutée. |
| M12, M16 | PP-S11-Ia ne garde que le sevrage des benzodiazépines et opioïdes **prescrits**, avec une décroissance progressive. Le sevrage alcoolique passe dans PP-S11-F. Le mécanisme dit maintenant que le récepteur GABA-A est désensibilisé et que les récepteurs NMDA se multiplient. Un renvoi croisé relie les deux fiches. |
| M13 | Métamizole : la réaction est immune, de type allergique et non dose-dépendante (Swissmedic, lu). Le constat de l'auditeur (mécanisme « probable ») est remplacé par le texte de la source lue. |
| M14 | Trouble de l'adaptation : la formulation suit la CIM-11 (OMS, dernier recours, non lu). |
| M15 | Le nom du cadrage est conservé, pour garder l'identité avec recensement_sf. Le champ `nom_audit` donne « ostéonécrose de la mâchoire liée aux antirésorbeurs (bisphosphonates, dénosumab) ». Renommer le cadrage relève du coordinateur. |
| M17 | Myélome : PP-S9-T se réduit à l'atteinte osseuse et renvoie à PP-S10-T (`renvoi_fiche`). |
| M18 | PP-S10-A reçoit `renvois_croises` vers Biermer (PP-S10-F) et vers le PTT acquis (PP-S10-V). |

## Pivots et renvois (R1 à R10)

| # | Correction appliquée |
|---|---|
| R1, R3 | PP-S11-A et PP-S11-T : `traitement_cible` vaut `null`. |
| R2 | PP-S11-D : `PH-S1-antidementiels`. |
| R4 | Le trouble bipolaire renvoie à `PH-S11-thymoregulateurs`, avec le lithium et le valproate. |
| R5 | PP-S12-Tr : `examen_cle` devient `EX-2-S9-radiographie-standard-age-osseux`. |
| R6 | PP-S12-F : `examen_cle` vaut `null`. |
| R7 | Ulcères : SY-22 est retiré ; les renvois sont S-24 et S-23. |
| R8 | Sarcomes : S-04 est remplacé par S-20 et S-21. |
| R9 | Morsures : S-35 est retiré. |
| R10 | Lupus : `EX-1-S6-complement`. Rupture splénique : `EX-2-S5-echographie-abdominale`. |
| En plus | Deux pivots hors sujet du même type, non signalés par l'audit, sont corrigés. PP-S11-I passe à `null` (traitement anti-infectieux). PP-S11-C passe à `PH-S11-psychostimulants` (TDAH). PP-S11-V passe à `PH-S11-antidepresseurs` (dépression post-AVC). |

## Affections ajoutées (§5)

| Fiche | Ajouts |
|---|---|
| Graves | Legg-Calvé-Perthes (S9-V), arthrite de Lyme (S9-I), canal lombaire étroit (S9-D), épiphysiolyse fémorale (S9-Tr), myopathie de Duchenne (S9-C), LAM promyélocytaire (S10-T), aplasie médullaire et syndrome des antiphospholipides (S10-A), TDAH (S11-C), troubles des conduites alimentaires, TOC et troubles de la personnalité (S11-F), syndrome malin des neuroleptiques (S11-Ia), eczéma de contact allergique (S12-A). |
| Moyens repris | Parvovirus B19 et crise aplasique (S10-I), sevrage alcoolique (S11-F), hydrocéphalie à pression normale (S11-D), encéphalite herpétique (S11-I), angio-œdème bradykinique sous IEC (S12-Ia). |
| Non traités (moyens §5) | Sclérodermie et Raynaud, Paget, SDRC, achondroplasie, fracture atypique du fémur, tuberculose ostéo-articulaire, méthémoglobinémie, SHU, MGUS, Wernicke-Korsakoff (seulement mentionné dans le sevrage alcoolique), intoxication au lithium, syndrome post-commotionnel, lichen plan, syphilis secondaire, varicelle et verrues, mycosis fongoïde, hidradénite suppurée. Ils restent à faire. |

## Restant avant `audit-ok`

- Lire en entier au moins une recommandation de société suisse par système. Aujourd'hui, on n'a lu que les pages Swissmedic et des extraits de recherche.
- Faire contre-auditer les 19 affections ajoutées, qui n'ont pas été auditées.
- Le script générateur et correcteur se trouve dans le scratchpad de session (`gen.py`, `patch.py`) ; il n'est pas versionné.

## Tour 2 (réponse à `AUDIT_PP_S9_S12_V2.md`, 14.11.2026)

Les 36 JSON sont réécrits et validés : 0 erreur, 140 affections, plus aucun `nom_audit`.

| # | Correction appliquée |
|---|---|
| M15 | PP-S9-Ia : la quatrième affection devient « ostéonécrose de la mâchoire liée aux antirésorbeurs (bisphosphonates, dénosumab) » dans `affections` et `detail_affections` ; `nom_audit` est supprimé. Dans `recensement_sf/recensement_sf.json`, seule la ligne 3771 change, avec ce même libellé ; le JSON reste valide. |
| N1 | Le texte du valproate (PP-S11-F, trouble bipolaire) reprend la formulation de Swissmedic, Vigilance-News éd. 32. Sa prescription est contre-indiquée chez les jeunes filles et les femmes en âge de procréer, sauf programme de prévention de la grossesse. Elle est aussi contre-indiquée pendant la grossesse dans le trouble bipolaire. Le texte ajoute le risque possible de troubles neurodéveloppementaux chez l'enfant d'un père traité dans les trois mois précédant la conception. J'ai lu moi-même le PDF français (messages-clés 2 et 3) ; le statut de la source devient « lu le 14.11.2026 », avec citation. |
| N2 | LAP : le syndrome de différenciation est ajouté (fièvre, détresse respiratoire, épanchements, prise de poids), traité par corticoïdes. |
| N3 | Angio-œdème sous IEC : l'icatibant et le concentré d'inhibiteur de C1 « se discutent hors indication » dans les formes graves, « sans efficacité démontrée par les essais ». Les voies aériennes passent en premier. |
| N4 | Encéphalite herpétique : `EX-1-S1-lcr-pcr-multiplex` est placé en tête des renvois. |
| N5 | Duchenne : les thérapies ciblées sont « en développement ou d'autorisation limitée (statut Swissmedic non vérifié) ». |
| N6 | L'épiphysiolyse reste dans PP-S9-Tr, pour ne pas modifier la liste du cadrage. Elle reçoit `renvoi_fiche` vers PP-S9-D (terrain endocrinien, IMG-294 classée D). |
| N7 | Arthrite de Lyme : la séquence est corrigée. Une seconde cure orale ou la ceftriaxone intraveineuse traitent l'arthrite qui persiste ; la synovite post-antibiotique relève d'un anti-inflammatoire, voire d'une synovectomie. |
| N8 | SAPL : pendant la grossesse, l'aspirine et l'HBPM remplacent les AVK, qui sont tératogènes. |
| N9 | Parvovirus B19 : l'anémie fœtale et l'anasarque chez la femme enceinte sont ajoutées. |
| N10 | TOC : « (AIPS) » devient « (AIPS suisse, non lu) ». |

Réserve maintenue : 17 omissions « Moyen » du §5 V1 restent ouvertes, et aucune recommandation de société suisse n'a été lue en entier.
