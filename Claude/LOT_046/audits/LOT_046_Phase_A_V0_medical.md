# Audit médical — LOT_046_Phase_A_V0.html
Version : 171790 octets, SHA-256 `977959113918c7d9`. Audit ciblé Θ3, points 4, 8, 9, 10, 11 ; extraits AIPS du paquet et liste HAM 30.09.2026 lus.

| Point | Note | Raison |
|---|---|---|
| 4 | 1/2 | Graves avant fréquents, discriminants donnés ; pneumothorax compressif et EP à haut risque sans geste qui tranche |
| 8 | 1/2 | Seuils datés ; critère SCA = délai d'ECG, pas un critère diagnostique ; nombres en lettres |
| 9 | 1/2 | Gold standard déclaré ; seuils BNP non aigus, SpO2 « normale » 92 % |
| 10 | 1/2 | Embranchements décisionnels ; nœud ECG illogique ; pas de reperfusion ni de décompression |
| 11 | 0/2 | Numéro Swissmedic faux (Ventolin), voie AIPS déformée (Aspirine Cardio), CI nitrés renvoyées alors que lues, doses en lettres |

**Score : 40.0 %. Question finale : non.** Corrections Critique ouvertes ; le fichier ne passe pas la porte.

| Gravité | Pt | Extrait (≤ 200 car.) | Source |
|---|---|---|---|
| Critique | 11 | (Swissmedic 37397 aips-37397-0 ) s'utilise, chez l'adulte et l'adolescent de plus de 12 ans, à raison de 1 à 2 inhalations en cas de bronchospasme aigu avec le nébuliseur-doseur aips-37397-3 . | aips-37397-43 (n° 37397 = solution concentrée pour aérosols ; nébuliseur-doseur = 54320, Diskus = 53898) |
| Critique | 11 | Salbutamol (Ventolin®, 37397) | aips-37397-43 |
| Critique | 11 | l'Aspirine® Cardio (Swissmedic 51795 aips-51795-0 ) se donne à 200 à 300 mg par voie orale écrasée ou intraveineuse aips-51795-4 . | aips-51795-4 (Aspirine Cardio = comprimés gastro-résistants, aips-51795-38 ; dose d'attaque IV ou forme orale non gastro-résistante seulement ; Aspirine Cardio  |
| Critique | 11 | Orale ou intraveineuse Dès le deuxième jour 100 mg | aips-51795-4 |
| Critique | 11 | Voir information professionnelle aips-40558-3 | aips-40558-5, aips-40558-6 (CI présentes dans le corpus ; renvoi = texte adouci) |
| Grave | 11 | Cas non très sévères hors hôpital aips-58253-3 | aips-58253-7 |
| Grave | 11 | Selon la maladie aips-66994-7 | aips-66994-17 |
| Moyen | 11 | Anurie, hypokaliémie sévère aips-30630-3 | aips-30630-8 (citation erronée -3 ; coma/précoma hépatique omis) |
| Moyen | 11 | Bronchospasme après anti-inflammatoire aips-51795-4 | aips-51795-5 (citation erronée -4) |
| Moyen | 11 | Grossesse, allaitement aips-58728-5 | aips-58728-24 (citation erronée -5) |
| Grave | 11 | Dans l'asthme aigu modéré ou sévère, elle propose cinquante milligrammes par voie orale pendant 5 jours w11618b-7 . | w11618b-7, aips-66994-7 (nombre en lettres = contournement LV3/LV6) |
| Grave | 11 | Ainsi, la dose est de quinze milligrammes deux fois par jour pendant vingt et un jours, puis de vingt milligrammes une fois par jour aips-58728-5 . | aips-58728-5 (lettres) |
| Grave | 11 | Quinze milligrammes deux fois par jour, puis vingt milligrammes aips-58728-5 | aips-58728-5 |
| Grave | 11 | À vingt minutes d'une première injection de furosémide dans l'œdème pulmonaire aigu, une nouvelle injection de 20 à 40 mg peut être faite si l'état le nécessite aips-30630-3 . | aips-30630-3 (lettres) |
| Grave | 11 | À soixante minutes d'une crise d'asthme, l'évaluation décide du retour à domicile ou de l'hospitalisation w11618b-55 . | w11618b-55 (lettres) |
| Grave | 11 | Dans l'asthme aigu, l'algorithme genevois associe l'ipratropium au salbutamol nébulisé, à répéter toutes les vingt minutes w11618b-7 . | w11618b-7 (lettres) |
| Grave | 8 | Ainsi, il repose aussi sur une variabilité du volume expiratoire d'au moins deux cents millilitres et 12 %, ou sur une variation du débit de pointe d'au moins 20 % w11618b-25 . | w11618b-25 (lettres ; « Ainsi » sans lien logique) |
| Grave | 4 | Si l'insuffisance cardiaque est possible, un peptide natriurétique normal rend le diagnostic improbable w149687-30 . | w149687-30 (seuils non aigus appliqués à la dyspnée aiguë ; seuils aigus ESC à ajouter au paquet, voir HELP) |
| Grave | 9 | BNP (valeur normale inférieure à 35 ng/l) Inférieur à 35 ng/l Insuffisance cardiaque improbable Chercher une autre cause | w149687-30 |
| Moyen | 9 | Saturation en oxygène (normale d'au moins 92 %) | w18c561-65 (92 % n'est pas une norme ; c'est un seuil de sévérité) |
| Léger | 9 | CRP (normale inférieure à 10 mg/l) | w18c561-65 |
| Moyen | 10 | Si l'électrocardiogramme est anormal, alors il est obtenu dans les 10 minutes après le premier contact médical, puis répété si nécessaire w480b78-96 . | w480b78-96 (condition illogique : l'ECG est anormal avant d'être obtenu) |
| Grave | 10 | Si le patient est instable, alors l'héparine non fractionnée intraveineuse est débutée sans délai, car l'embolie à haut risque est suspectée wa6f758-110 . | wa6f758-110 ; ajouter au paquet la recommandation 6.6 ESC/ERS 2019 (thrombolyse systémique de l'EP à haut risque) — absente du P10 et du P11 |

Corrections exactes (avant/après) : `LOT_046_Phase_A_V0.audit.json`.

**Ce qui manque :**
- Ajouter au paquet PA les seuils d'exclusion aigus ESC (BNP < 100, NT-proBNP < 300 pg/ml) depuis le texte ESC 2026 de l'insuffisance cardiaque (doi 10.1093/eurheartj/ehag100, publié le 28.08.2026), non depuis une revue.
- Ajouter la recommandation ESC/ERS 2019 6.6 (thrombolyse de l'EP à haut risque) ; vérifiée comme version ESC en vigueur (aucune ESC EP 2026 trouvée ; AHA/ACC 2026 exclue, LV5).
- Pneumothorax compressif (décompression immédiate) et oxygène contrôlé 88-92 % dans la BPCO hypercapnique : absents des points 4, 10 et 11 de la PA.
- Fibrillation auriculaire : HUG 2023 antérieure à l'ESC 2024 ; vérifier la cohérence (LV8).
