# Audit médical agressif — PP-S9 à PP-S12 (36 fiches, 121 affections)

Auditeur indépendant (non rédacteur), 14.11.2026. Posture : skills `medecin-expert` et `expert-web`.
Méthode : lecture intégrale des 36 JSON par script ; contrôle automatique de tous les renvois (SY, S, IMG, EX, PH) contre les catalogues ; recherche de doses (regex mg, µg, UI, mmol) ; vérification web de deux sources Swissmedic. Aucun fichier modifié hors ce rapport ; ni commit ni push.

## 1. Contrôles mécaniques

| Contrôle | Résultat |
|---|---|
| Renvois SY, S, IMG, EX, PH existants | 100 % trouvés dans les catalogues ; aucun identifiant orphelin |
| Doses chiffrées | Aucune ; champ `doses` renvoie à l'AIPS |
| Swissmedic « Fluoroquinolones et tendons » (26.11.2022) | Date confirmée sur l'index Vigilance-News, lu le 14.11.2026 |
| Swissmedic « Métamizole et agranulocytose » (09.05.2023) | Date confirmée sur l'index Vigilance-News, lu le 14.11.2026 |
| Champs du schéma | Présents ; `niveau`, `detail_affections`, `doses` et `statut` étendent le schéma sans le contredire |

## 2. Défauts de sources (transversaux)

| # | Gravité | Emplacement | Défaut | PATCH exact |
|---|---|---|---|---|
| S1 | Grave | 36 fiches, `sources[]` | La même liste est copiée dans les 9 lettres de chaque système. Ainsi, la source « Fluoroquinolones » figure dans PP-S9-V, -T, -C, etc. ; la source « Métamizole » dans PP-S10-V, -C, etc. ; l'OMS « malaria » dans les 9 fiches S10. Une source qui ne soutient aucune phrase de la fiche y crée une fausse caution. | Garder Fluoroquinolones dans **PP-S9-Ia** seulement ; Métamizole dans **PP-S10-Ia** seulement ; OMS malaria dans **PP-S10-I** seulement. Les supprimer ailleurs. |
| S2 | Grave | PP-S10-I, source OMS malaria | Une source suisse existe pour le paludisme (Swiss TPH / ECTM, healthytravel.ch ; OFSP). Le recours à l'OMS viole l'ordre Suisse → Europe → OMS. | Insérer avant l'OMS : `{"ref":"Swiss TPH / Comité d'experts en médecine des voyages (ECTM) : paludisme, diagnostic et traitement","etiquette":"Suisse","statut":"non lu"}`. |
| S3 | Moyen | 36 fiches, étiquette « Suisse, non vérifié CH » | L'étiquette se contredit : la source est suisse mais n'a pas été lue. | Remplacer par `"etiquette":"Suisse"` et garder `"statut":"non lu"`. |
| S4 | Moyen | 36 fiches, « Raisonnement physiopathologique de cours » | Le statut « non lu » n'a pas de sens pour une déduction. | `"statut":"déduction de l'auteur, non sourcée"`. |
| S5 | Moyen | PP-S11-* (9 fiches), WFSBP | L'étiquette « source internationale » ne figure pas dans l'ordre de Vial. Aucune source européenne n'est citée. | Ajouter `{"ref":"European Psychiatric Association (EPA) : guidance","etiquette":"source européenne","statut":"non lu"}` ; garder WFSBP avec l'étiquette `"source internationale (hors ordre CH/EU)"`. |
| S6 | Moyen | 36 fiches | Aucune source n'est réellement lue au-delà de deux titres Swissmedic. Toutes les fiches reposent donc sur la déduction. | Garder `statut:"brouillon"` ; ne pas poser `audit-ok` avant au moins une source suisse lue par système. |

## 3. Erreurs médicales et omissions de sécurité

| # | Gravité | Emplacement | Extrait (≤ 200 car.) | Défaut | PATCH exact |
|---|---|---|---|---|---|
| M1 | **Grave** | PP-S11-Ia, physostigmine, `cible_therapeutique` | « la physostigmine, inhibiteur de la cholinestérase, restaure l'acétylcholine en milieu surveillé » | Dans la même fiche, l'ECG cherche un QRS large dû aux tricycliques. Or la physostigmine est contre-indiquée dans ce cas (risque de bradycardie, d'asystolie). | Ajouter : « …en milieu surveillé ; on ne la donne pas si le QRS s'élargit (intoxication aux tricycliques), car elle peut provoquer une asystolie. » Source : Tox Info Suisse (Suisse, non lu). |
| M2 | **Grave** | PP-S11-F, trouble bipolaire, `cible_therapeutique` | « Le lithium et le valproate stabilisent l'humeur par la signalisation intracellulaire » | L'alerte tératogène manque pour le valproate, alors que PP-S12-F la donne pour l'isotrétinoïne. Swissmedic impose un programme de prévention de la grossesse. | Ajouter : « le valproate est tératogène : on l'évite chez la femme en âge de procréer, sauf programme de prévention de la grossesse (AIPS Swissmedic, à lire mot pour mot) ». |
| M3 | **Grave** | PP-S11-Ia (omission) | — | Le syndrome malin des neuroleptiques manque. On ne le trouve que dans le mnémonique de PP-S11-A et dans PP-S1-Ia. C'est une urgence classique de l'examen. | Ajouter une affection : « Syndrome malin des neuroleptiques » ; mécanisme : « Le blocage D2 du striatum et de l'hypothalamus provoque rigidité et dysrégulation thermique. » ; clinique : « Rigidité en tuyau de plomb, hyperthermie, dysautonomie et confusion apparaissent ; les CK s'élèvent. » ; examen : EX-1-S9-cpk ; cible : « On arrête l'antipsychotique ; on refroidit et on réhydrate ; le dantrolène relâche le muscle, la bromocriptine restaure le tonus dopaminergique. » ; renvois SY-71, S-26. |
| M4 | Moyen | PP-S10-V, CIVD, `examen` | « Les plaquettes et le fibrinogène baissent, le TP s'allonge » | Le TP (taux de prothrombine, Quick en %) baisse ; c'est le temps de Quick qui s'allonge. | « …le TP (Quick) baisse, le TCA s'allonge, les D-dimères montent. » |
| M5 | Moyen | PP-S10-A, AHAI, `cible_therapeutique` | « Les corticoïdes réduisent la production d'anticorps et la phagocytose ; … on évite le froid dans la forme froide » | Le texte laisse croire que les corticoïdes agissent aussi dans la forme froide, où ils agissent peu. | « Dans la forme chaude, les corticoïdes réduisent… ; dans la forme froide, ils agissent peu : on évite le froid, le rituximab supprime le clone B. » |
| M6 | Moyen | PP-S10-A, AHAI, `mecanisme[1]` | « Des IgM « froides » fixent le complément et lysent les hématies au froid » | La fixation se fait au froid, mais l'hémolyse est surtout extravasculaire et hépatique (hématies opsonisées par C3b). | « Des IgM froides se fixent en périphérie froide et déposent C3 ; le foie détruit surtout ces hématies (hémolyse extravasculaire), parfois le complément les lyse. » |
| M7 | Moyen | PP-S9-I, spondylodiscite, `mecanisme[0]` | « Le germe atteint par voie hématogène le disque, avasculaire chez l'adulte » | La phrase se contredit : un disque avasculaire ne reçoit pas le germe par le sang. Chez l'adulte, le germe se fixe d'abord dans le plateau vertébral, puis gagne le disque. | « Le germe se fixe par voie hématogène dans le plateau vertébral sous-chondral, puis gagne le disque avasculaire et le plateau voisin. » |
| M8 | Moyen | PP-S9-T, sarcomes, `cible_therapeutique` | « La chimiothérapie néoadjuvante cible la prolifération, puis la chirurgie large » | Cette séquence vaut pour l'ostéosarcome et le sarcome d'Ewing ; le chondrosarcome et la plupart des sarcomes des parties molles résistent à la chimiothérapie. | « Dans l'ostéosarcome et le sarcome d'Ewing, la chimiothérapie néoadjuvante précède la chirurgie large ; le chondrosarcome se traite par chirurgie seule. » |
| M9 | Moyen | PP-S9-T, métastases, `cible_therapeutique` | « la radiothérapie soulage et décomprime » | La compression médullaire, déjà annoncée dans la clinique, n'a pas de prise en charge urgente complète. | Ajouter : « En cas de compression médullaire, les corticoïdes réduisent l'œdème en urgence ; la chirurgie ou la radiothérapie décompriment. » |
| M10 | Moyen | PP-S12-I, impétigo, `mecanisme[1]` | « Les toxines exfoliatives clivent l'épiderme et forment des bulles fragiles » | Ce mécanisme décrit l'impétigo bulleux (S. aureus), alors que la clinique décrit la forme croûteuse non bulleuse. | « Dans la forme bulleuse, les toxines exfoliatives du staphylocoque clivent la desmogléine 1 ; la forme commune donne des croûtes mélicériques. » |
| M11 | Moyen | PP-S9-Ia, statines | « On arrête ou change la statine » | La myopathie nécrosante auto-immune anti-HMGCR manque ; elle persiste après l'arrêt et demande un immunosuppresseur. | Ajouter : « Une faiblesse qui persiste après l'arrêt, avec des CK élevées, évoque une myopathie nécrosante anti-HMGCR (immunosuppression). » |
| M12 | Moyen | PP-S11-Ia, sevrages | Classement « Ia » pour le sevrage d'alcool et d'opioïdes | Le sevrage d'alcool n'est pas iatrogène ; le classement VITE DIT CAFé devient faux. | Garder sous Ia seulement le sevrage des benzodiazépines et opioïdes **prescrits** ; déplacer le sevrage alcoolique dans PP-S11-F (addictions). |
| M13 | Léger | PP-S10-Ia, métamizole | « Le métamizole induit le plus souvent des anticorps » | Le mécanisme immun reste probable, non prouvé. | « Le métamizole détruit probablement les neutrophiles par un mécanisme immun (incomplètement connu). » |
| M14 | Léger | PP-S11-Tr, trouble de l'adaptation | « La réaction reste proportionnée dans le temps » | La CIM-11 décrit une préoccupation et un échec d'adaptation, non une réaction proportionnée. | « Les symptômes apparaissent dans le mois qui suit le stress et cèdent en général dans les six mois après sa disparition. » (OMS CIM-11, dernier recours, non lu) |
| M15 | Léger | PP-S9-Ia, titre | « ostéonécrose de la mâchoire aux bisphosphonates » | Le titre est trop étroit, puisque le texte cite le dénosumab. | Renommer : « ostéonécrose de la mâchoire liée aux antirésorbeurs ». |
| M16 | Léger | PP-S11-Ia, sevrage, `mecanisme[0]` | « le cerveau réduit le GABA et renforce le glutamate » | Le récepteur GABA-A est désensibilisé ; le taux de GABA ne baisse pas. | « le cerveau désensibilise le récepteur GABA-A et multiplie les récepteurs NMDA ». |
| M17 | Léger | PP-S10-T et PP-S9-T | Myélome décrit deux fois, avec le même mnémonique CRAB | C'est une redondance. | Garder le détail dans PP-S10-T ; dans PP-S9-T, réduire à l'atteinte osseuse avec un renvoi vers PP-S10-T. |
| M18 | Léger | PP-S10-F, Biermer ; PP-S10-V, PTT acquis | Mécanismes auto-immuns classés F et V | Le classement s'écarte de VITE DIT CAFé. | Ajouter une ligne dans PP-S10-A (« Biermer : voir PP-S10-F » ; « PTT acquis : voir PP-S10-V »). |

## 4. Renvois et pivots mal choisis

| # | Gravité | Emplacement | Défaut | PATCH exact |
|---|---|---|---|---|
| R1 | Moyen | PP-S11-A `traitement_cible` = PH-S11-antipsychotiques | Le pivot contredit le mnémonique de la fiche (« les antipsychotiques aggravent… »). | `"traitement_cible": null` ou PH d'immunothérapie quand il existera. |
| R2 | Moyen | PP-S11-D `traitement_cible` = PH-S11-antipsychotiques | Le pivot ne correspond pas : la cible décrite est cholinergique et NMDA. | `"PH-S1-antidementiels"` (existe). |
| R3 | Moyen | PP-S11-T `traitement_cible` = PH-S11-antipsychotiques | Aucune affection de la fiche n'est traitée par antipsychotique. | `null` (traitement chirurgical et corticoïde). |
| R4 | Moyen | PP-S11-F, bipolaire | La fiche n'a pas de renvoi PH, alors que PH-S11-thymoregulateurs existe. | Ajouter `"renvoi_pharmaco":["PH-S11-thymoregulateurs"]`. |
| R5 | Moyen | PP-S12-Tr `examen_cle` = EX-1-S10-hemogramme-leucocytes-formule | Cet examen n'est pas pertinent pour une brûlure, une plaie ou une morsure. | `"EX-2-S9-radiographie-standard-age-osseux"` (corps étranger, fracture). |
| R6 | Léger | PP-S12-F `examen_cle` = EX-3-S12-dermatoscopie | La dermatoscopie n'aide ni pour l'acné, ni pour la rosacée, ni pour l'hyperhidrose. | `null` (diagnostic clinique). |
| R7 | Léger | PP-S12-V, ulcères, SY-22 | SY-22 renvoie à l'ischémie **aiguë**, alors que l'ulcère artériel est chronique. | Remplacer par S-23 seul ; garder IMG-311. |
| R8 | Léger | PP-S9-T, sarcomes, S-04 | Un sarcome atteint rarement les ganglions. | Remplacer par S-20, S-21. |
| R9 | Léger | PP-S12-Tr, morsures, S-35 | Le renvoi médico-légal n'est pas pertinent pour une morsure animale. | Supprimer S-35. |
| R10 | Léger | PP-S9-A, lupus ; PP-S10-Tr, rupture splénique | `renvoi_examens` reste vide. | Lupus : `["EX-1-S6-complement"]` ; rate : `["EX-2-S5-echographie-abdominale"]`. |

## 5. Affections importantes absentes (examen fédéral)

| Système | Gravité | Absentes, à ajouter (lettre) | Indice que le recensement les attend |
|---|---|---|---|
| S9 | Grave | Legg-Calvé-Perthes (V), épiphysiolyse fémorale (Tr), arthrite de Lyme (I), canal lombaire étroit (D), myopathie de Duchenne (C, absente des 10 systèmes) | IMG-083 (canal étroit) est déjà cité ; IMG-296 (hanche de l'enfant) existe |
| S9 | Moyen | Sclérodermie systémique et Raynaud (A), maladie de Paget (D), SDRC (F), achondroplasie (C), fracture atypique du fémur sous bisphosphonates (Ia), tuberculose ostéo-articulaire (I) | IMG-335 cite l'achondroplasie |
| S10 | Grave | Aplasie médullaire (A), leucémie aiguë promyélocytaire avec CIVD (T), syndrome des antiphospholipides (A ; présent seulement dans S7 et S8, sans renvoi) | — |
| S10 | Moyen | Parvovirus B19 et crise aplasique (I), méthémoglobinémie (Ia), SHU (renvoi vers PP-S6-V), MGUS (T) | — |
| S11 | **Grave** | TDAH (C), troubles des conduites alimentaires (F), TOC (F), troubles de la personnalité (F) | EX-9-S11-tdah, EX-9-S11-troubles-conduites-alimentaires et PH-S11-psychostimulants existent sans fiche PP |
| S11 | Moyen | Encéphalite herpétique (I), hydrocéphalie à pression normale (D, démence curable ; IMG-022 déjà cité), Wernicke-Korsakoff (F), intoxication au lithium (Ia ; renvoi PP-S8-Ia), syndrome post-commotionnel (Tr) | — |
| S12 | Grave | Eczéma de contact allergique (A/Ia) | EX-6-S12-tests-epicutanes est cité sans affection correspondante |
| S12 | Moyen | Angio-œdème bradykinique sous IEC (Ia), lichen plan (A), syphilis secondaire (I), varicelle et verrues (I), mycosis fongoïde (T), hidradénite suppurée (F) | — |

## 6. Points exacts (aucun défaut retenu)

Les chaînes suivantes sont exactes et bien expliquées : syndrome des loges, arthrite septique, PR, spondyloarthrites, goutte et chondrocalcinose, TVP, PTT, TIH, anticoagulants et antidotes, drépanocytose, sphérocytose, G6PD, hémophilies, Willebrand, carences, anémie inflammatoire (hepcidine), EBV (CD21), VIH (CCR5/CXCR4), schizophrénie (voies dopaminergiques), anti-NMDA, SJS/NET (HLA-B*15:02, B*58:01), DRESS (HHV-6), pemphigus et pemphigoïde, psoriasis (IL-23/IL-17), dermatite atopique (Th2, dupilumab), BCC (PTCH1), mélanome (BRAF, Breslow), acné (isotrétinoïne et contraception). Phrases verbales et concises dans l'ensemble.

## 7. Verdict

| Critère | Note |
|---|---|
| Exactitude physiopathologique | 1/2 : chaînes justes en majorité ; 3 omissions de sécurité graves (M1 à M3) et 9 erreurs moyennes |
| Classement VITE DIT CAFé | 1/2 : sevrage d'alcool classé Ia ; Biermer et PTT acquis sans renvoi A |
| Couverture de l'examen fédéral | 1/2 : S11 lacunaire (TDAH, TCA, TOC, personnalité) ; S9 et S10 incomplets |
| Renvois | 1/2 : tous existent ; 5 pivots PH ou EX sont hors sujet |
| Doses | 2/2 : aucune dose |
| Sources | 0/2 : listes copiées hors sujet, OMS avant la source suisse, quasi rien lu |

**Verdict : NON (refus d'`audit-ok`).** Pour obtenir « oui », il faut appliquer M1 à M3, S1 et S2, les défauts Moyen, et ajouter au minimum les affections « Grave » du §5 (TDAH, TCA, syndrome malin, aplasie, LAP, Perthes, Lyme, canal lombaire étroit, eczéma de contact). Il faut aussi lire au moins une source suisse par système.

Sources consultées par l'auditeur : [Swissmedic, Vigilance-News, index](https://www.swissmedic.ch/swissmedic/de/home/humanarzneimittel/marktueberwachung/pharmacovigilance/vigilance-news.html) (lu le 14.11.2026) ; [Swissmedic, Fluorchinolone und Sehnen](https://www.swissmedic.ch/swissmedic/de/home/humanarzneimittel/marktueberwachung/pharmacovigilance/vigilance-news/fluoroquinolones-and-tendonitis-tendon-rupture.html) (lu) ; [Swissmedic, Métamizole et agranulocytose](https://www.swissmedic.ch/swissmedic/fr/home/medicaments-a-usage-humain/surveillance-du-marche/pharmacovigilance/vigilance-news/novalgin_und_agranulozytose.html) (résumé de recherche). Les corrections M1, M2, S2 et M14 citent des sources que l'auditeur n'a pas lues (marquées « non lu »).
