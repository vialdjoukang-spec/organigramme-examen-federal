# Audit médical ciblé — LOT_044_Phase_B_V0_DX.6.html

Version : 151572 octets, SHA-256 `f87e65d5a5ccd84edb2d0d9b18039840e03104911a9c4e529cf4cb79bef75439`. Points lus : 2, 3, 4, 8, 9, 10 (PA), 11, 12 ; AIPS confrontées aux extraits du paquet et au corpus AipsDownload_20261008.

| Point | Note et raison |
|---|---|
| P2 | sans objet — non lu dans cet audit ciblé. |
| P3 | sans objet — non lu dans cet audit ciblé. |
| P4 | 1 — graves avant fréquents ; probabilité « jusqu’à zéro » sortie de sa condition (1993). |
| P8 | 2 — UDMI4, seuils STEMI, NSTEMI, périprocédural, GRACE, Killip, ce qui ne suffit pas. |
| P9 | 1 — tableau assimile le 99e percentile au seuil d’exclusion de l’algorithme 0/1 h. |
| P11 | 1 — but chiffré et chronologie ; AAS et atorvastatine « sans AIPS » à tort ; CI Beloc adoucie ; durée énoxaparine attribuée à l’AAS. |
| P12 | 1 — trois niveaux ; colchicine sur une source 2022 dépassée par l’ESC 2023 ; pas de recommandation suisse. |

**Score : 6/10 = 60.0 %. Question finale : non.** Manque : 1 Critique (CI Beloc i.v.) ; doses AAS, atorvastatine et fentanyl absentes alors que l’AIPS existe ; confusion 99e percentile / seuil d’exclusion.

| Gravité | Point | Extrait (≤ 200 car.) | Correction | Source |
|---|---|---|---|---|
| Critique | 11 | Il est interdit si la fréquence cardiaque est inférieure à 45 battements par minute, si l'intervalle PQ dépasse 0,24 s ou si la pression systolique est inférieure à 100 mmHg aips-56191-7 . | Il est interdit si la fréquence est inférieure à 45 par minute, si PQ dépasse 0,24 s, si la systolique est inférieure à 100 mmHg ou en insuffisance cardiaque sévère aips-56191-7 . | aips-56191-7 |
| Grave | 11 | La monographie suisse de l'acide acétylsalicylique pour voie orale ou injectable est introuvable dans la base consultée. On n'écrit donc aucune dose, et la lacune est consignée dans le fichier HELP. | L'information professionnelle d'Aspirine® Cardio (n° Swissmedic 51795) prévoit 200 à 300 mg par voie intraveineuse ou orale dans l'infarctus aigu, puis 100 mg par jour aips-51795-4 . | aips-51795-4 (paquet PA ; à verser au paquet DX.6) |
| Grave | 11 | Aucune monographie AIPS lisible d'atorvastatine seule n'a été trouvée ; je n'écris donc aucune dose, conformément au fichier HELP. | L'information professionnelle de Sortis® (atorvastatine, n° Swissmedic 54085) prévoit 10 mg par jour au départ et au plus 80 mg par jour. | AIPS Sortis® 54085 (refdata, lue le 10.11.2026 ; passage à verser au paquet) |
| Grave | 9 | Troponine hs, valeur normale Moins de 14 ng/L (Roche T) ou 26,2 ng/L (Abbott I) we94dbc-38 Exclusion selon algorithme Sortie si exclusion et symptômes anciens | Troponine hs sous le 99e percentile Moins de 14 ng/L (Roche T) ou 26,2 ng/L (Abbott I) we94dbc-38 Valeur normale, qui ne vaut pas exclusion Appliquer les seuils d’exclusion propres au test à 0 et 1 he | we94dbc-38 ; we94dbc-41 |
| Grave | 11 | On y associe 100 à 325 mg d'acide acétylsalicylique par jour, pendant 2 à 8 jours aips-49456-6 aips-49456-7 aips-49456-0 . | On y associe 100 à 325 mg d'acide acétylsalicylique par jour, et l'énoxaparine dure habituellement 2 à 8 jours, jusqu'à la stabilisation clinique aips-49456-6 aips-49456-7 . | aips-49456-6 ; aips-49456-7 |
| Grave | 4 | Une douleur pleurétique ou reproductible à la palpation fait chuter la probabilité d'infarctus jusqu'à zéro, à condition que le patient n'ait aucun antécédent d'angor ni d'infarctus wfba9d7-5 . | Selon des données genevoises de 1993, la probabilité d'infarctus tombe à 0 % seulement si une douleur en coup de poignard, pleurétique ou reproductible, survient sans antécédent coronarien wfba9d7-5 . | wfba9d7-5 |
| Moyen | 11 | Chez le patient de 75 ans ou plus, on supprime le bolus et on donne 0,75 mg/kg toutes les 12 heures aips-49456-14 . | Chez le patient de 75 ans ou plus, on supprime le bolus et on donne 0,75 mg/kg toutes les 12 heures, au plus 75 mg pour les 2 premières doses aips-49456-14 . | aips-49456-14 |
| Moyen | 11 | On poursuit 15 minutes plus tard avec 50 mg par voie orale quatre fois par jour aips-56191-3 aips-56191-0 . | Si les 15 mg sont tolérés, on poursuit 15 minutes plus tard avec 50 mg par voie orale 4 fois par jour pendant 48 heures aips-56191-3 . | aips-56191-3 |
| Moyen | 11 | Le deuxième but est de limiter la thrombose récidivante par un double traitement antiplaquettaire d'au moins douze mois chez la plupart des patients, sauf risque hémorragique élevé pmc8970581-32 . | Le deuxième but est de limiter la thrombose récidivante par un double traitement antiplaquettaire de 12 mois par défaut, sauf risque hémorragique élevé pmc8970581-32 . | pmc8970581-32 ; ESC 2023 SCA |
| Moyen | 12 | D'autres essais ont observé un excès de décès non cardiovasculaires, de sorte qu'elle n'est pas recommandée en routine pmc8970581-51 . | D'autres essais ont observé un excès de décès non cardiovasculaires ; l'ESC 2023 la propose seulement comme option, sans usage systématique pmc8970581-51 wfbbc0b-28 . | pmc8970581-51 ; wfbbc0b-28 (paquet PA) |
| Grave | HELP | Fentanyl i.v. sans dose (HELP) | Citer l’AIPS Fentanyl-Mepha (53484) ou Fentanyl Sintetica (53987), présentes dans le corpus. | erweiterte_ham_ind.xlsx ; idx SmPC |
| Grave | HELP | Acide acétylsalicylique i.v. | Lire l’AIPS d’Acide acétylsalicylique Panpharma Inj 0,5 g (47256), présente dans le corpus, pour la voie i.v. du protocole HUG. | idx SmPC 47256 |
| Léger | HELP | LDL < 55 mg/dL | Donner l’unité suisse (mmol/L) après lecture de la source ESC. | pmc11317809-15 |
