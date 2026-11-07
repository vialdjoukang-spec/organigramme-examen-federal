# HELP_DX5 — LOT_015 — Phase B DX.5 « Hypothyroïdie »

Questions ouvertes par le rédacteur Phase B le 30.10.2026. Format : identifiant ; contexte ; question ; déjà cherché ; emplacement cible.

## H15-DX5-01 — Lévothyroxine (et liothyronine) injectable en Suisse pour le coma myxœdémateux
- Contexte : aucune spécialité injectable de lévothyroxine ni de liothyronine seule dans le XML AIPS du 08.10.2026 ni dans la liste des spécialités (recherche « Levothyroxin », « Liothyronin » : seul Novothyral). Le HTML écrit « À vérifier (AIPS) » sans dose ; la NIV 2013 recommande une substitution parentérale à dose élevée (T4 + T3).
- Question : quelle spécialité injectable est autorisée ou importée (OAMéd) en Suisse, avec numéro Swissmedic, dose AIPS et texte grossesse ? Quelle recommandation suisse ou européenne récente (SSED, ESE, ETA) fixe la dose ?
- Déjà cherché : XML AIPS local (noms de spécialités, DCI) ; API liste des spécialités (Levothyroxin, Liothyronin, Thybon, Cytomel, Cynomel) ; swissmedicinfo.ch (application dynamique non lisible par curl), 30.10.2026.
- Emplacement : DX.5, point 11.B, fenêtre « Urgence — conduite chronologique ».

## H15-DX5-02 — Recommandation suisse sur l'hypothyroïdie de l'adulte et pendant la grossesse
- Contexte : le HTML s'appuie sur la HAS 2022 (France), l'ESE 2020 et le BMJ 2019 ; aucune recommandation SSED/SGED, SSGO/SGGG, HUG ou Forum Médical Suisse n'a été trouvée. La Revue Médicale Suisse 2020;16(684):455–8 (« Rapid Recommendations ») est repérée mais non lue.
- Question : quelle recommandation suisse en vigueur (organisme, année, URL) fixe les seuils de TSH, la cible pendant la grossesse et la conduite dans la forme infraclinique ?
- Déjà cherché : recherches web FR/DE (SSED, SGGG Expertenbrief, HUG, Forum Médical Suisse), 30.10.2026.
- Emplacement : DX.5, points 8, 11.B (situations spéciales), 12.

## H15-DX5-03 — Textes intégraux ETA 2013 (forme infraclinique), ETA 2014 (grossesse, enfant) et version plus récente
- Contexte : la position ETA 2013 n'est citée que via le tableau 1 du BMJ 2019 ; l'ETA 2014 n'est pas lue.
- Question : texte des recommandations ETA (2013, 2014) et existe-t-il une ligne directrice ETA plus récente sur l'hypothyroïdie de l'adulte ?
- Déjà cherché : PMC3923601 et PMC4109520 (reCAPTCHA ; Europe PMC sans texte intégral), 30.10.2026.
- Emplacement : DX.5, point 11.B (fenêtre « forme fruste »).

## H15-DX5-04 — Prévalence suisse de l'hypothyroïdie
- Contexte : l'OFSP (HTA 2022) écrit qu'aucune donnée épidémiologique suisse n'existe et applique 3,8 % (Europe) ; seule la cohorte CoLaus donne 3,8 % d'utilisateurs chroniques de lévothyroxine à Lausanne.
- Question : existe-t-il une prévalence suisse (OFS, Obsan, assureurs) de l'hypothyroïdie avérée et infraclinique, et de l'usage de lévothyroxine ?
- Déjà cherché : OFSP HTA, CoLaus, recherches web, 30.10.2026.
- Emplacement : DX.5, point 2.

## H15-DX5-05 — Ampleur de la prise de poids et performances diagnostiques
- Contexte : les sources donnent un gain « modéré » et une perte < 10 % après traitement, sans chiffre de gain en kg ni délai ; la sensibilité et la spécificité de la TSH et des signes cliniques ne sont pas chiffrées.
- Question : quelle source européenne chiffre le gain de poids attribuable à l'hypothyroïdie, le délai de perte après traitement et les performances de la TSH et des signes (réflexe achilléen) ?
- Déjà cherché : ESE 2020, HAS 2022 (argumentaire), BMJ 2019, 30.10.2026.
- Emplacement : DX.5, points 2, 6, 9.a, 11.A.

## H15-DX5-06 — Mortalité du coma myxœdémateux, critères de sortie, aptitude à la conduite et travail
- Contexte : la NIV qualifie la mortalité d'« élevée » sans chiffre ; aucune liste officielle de critères de sortie ; aucune règle suisse de conduite ou d'arrêt de travail propre à l'hypothyroïdie.
- Question : quels chiffres européens récents de mortalité, quels critères de sortie publiés, quelles règles suisses (médecine du trafic, LAI) s'appliquent ?
- Déjà cherché : NIV 2013, HAS 2022, AIPS (rubrique conduite), 30.10.2026.
- Emplacement : DX.5, points 2, 11.B (fenêtre sociale), 11.D.

## Suivi d'audit médical — 30.10.2026 (auditeur-medical, opus, xhigh)

Fichier : `LOT_015_Phase_B_V0_DX.5.html`, 119 108 → 126 944 octets ; SHA-256 final `ade7ea510d14e4dea0b8e1c8889f39318ce6fa4b0c9dd810872d2e097728a520`. Journal : `LOT_Claude_Finaux/LOT_015/audits/corrections.jsonl` (26 lignes DX.5 : 1 grave, 12 moyennes, 13 légères).

| ID | État | Ce que l'audit a trouvé à la source |
|---|---|---|
| H15-DX5-01 | Comblée en partie | XML AIPS du 08.10.2026 relu par nom de spécialité (L-Thyroxin, Levothyrox, Thyrax, Syntroxine, Thybon, Cytomel, Cynomel, Triostat, Serb, Henning, liothyronine) : aucune forme injectable. Liste Swissmedic « Conditionnements autorisés à usage humain » du 1.10.2026 (https://www.swissmedic.ch/dam/swissmedic/de/dokumente/internetlisten/zugelassene_packungen_human.xlsx.download.xlsx/zugelassene_packungen_ham.xlsx) : lévothyroxine en formes orales seulement → produit non autorisé en Suisse ; importation selon l'art. 49 OAMéd (al. 1 et 3), état au 15.3.2025 (https://www.fedlex.admin.ch/eli/cc/2018/786/fr). Dose AIPS : reste « À vérifier (AIPS) ». Doses NIV (T4 200–250 µg i.v., T3 10 µg) non reprises : aucune AIPS suisse. |
| H15-DX5-02 | Ouverte | Aucune recommandation suisse en vigueur trouvée. Serval UNIL : seule une revue RMS 2012;8(331):501–2 (Virgini, Collet, Rodondi), pas une recommandation. RMS 2020;16(684):455–8 : texte intégral non obtenu. |
| H15-DX5-03 | Comblée | ETA 2013 lue en texte intégral (https://www.eurothyroid.com/files/download/ETA-Guideline-Management-of-Subclinical-Hypothyroidism.pdf) : seuil « <65–70 years », cible 0,4–2,5 mU/L (R20), 1–5 mU/L après 70–75 ans (R22), arrêt de l'essai à 3–4 mois (R23), progression 5–8 %/an. Version plus récente : ETA 2025 sur la lévothyroxine en monothérapie (Eur Thyroid J 2025;14:e250123 ; copie https://eprints.ncl.ac.uk/309310), citée [S28]. ETA 2014 (grossesse, enfant) : 403 chez l'éditeur, non lue. |
| H15-DX5-04 | Ouverte | Aucune donnée OFS/Obsan trouvée ; non traitée plus avant. |
| H15-DX5-05 | Ouverte | ESE 2020 relue : « usually of less than 10% » et « modest weight loss » confirmés ; aucun gain chiffré en kg ni délai. |
| H15-DX5-06 | Comblée en partie | NIV : 6 décès sur 24 (25 %) dans l'enquête allemande 1993–1995 → écrit au point 2. Critères de sortie et règles suisses de conduite ou LAI : toujours non trouvés. |

Constats hors HELP corrigés dans le fichier : contre-indication Cordarone® « Affections thyroïdiennes (hypo- ou hyperthyroïdie) » (n° 33393) et restriction Quilonorm® « hypothyroïdie non traitée » (n° 35960) ajoutées ; hydrocortisone d'abord, puis hormone thyroïdienne ; Solu-CORTEF® : vitesse et non dose propre à l'indication, contre-indications, grossesse et allaitement ; Novothyral® (posologie, contre-indications, limitation) ; divergences AIPS ↔ ETA 2025 (orlistat ≥ 4 h, calcium 4–6 h, prise au coucher) ; Mounjaro® n° 68726, 69415, 69696.
