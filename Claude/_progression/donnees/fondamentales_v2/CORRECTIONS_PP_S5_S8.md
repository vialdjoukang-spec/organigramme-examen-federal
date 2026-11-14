# Corrections PP-S5 à PP-S8, suite à AUDIT_PP_S5_S8.md

Date : 14.11.2026. Les 36 fiches ont été régénérées, puis corrigées par script, et revalidées : JSON valides, tous les renvois SY, S, IMG, EX, PHY, PH, SF et PP résolus, aucune dose chiffrée. Les affections passent de 143 à 172. Le statut des fiches est « brouillon corrigé après audit, à réauditer ». Ni commit ni push.

## Graves

| Point | Correction |
|---|---|
| E1, PP-S5-C, sténose du pylore | L'hypokaliémie est désormais d'origine rénale : l'aldostérone et la bicarbonaturie entraînent le potassium, puis apparaît l'acidurie paradoxale (texte de l'audit). |
| M1, PP-S8-T | Ajout du syndrome de Cushing (formes hypophysaire, ectopique et surrénalienne ; cortisol libre urinaire, freinage, ACTH ; chirurgie, inhibiteur de la stéroïdogenèse) et de l'acromégalie (IGF-1, HGPO avec GH, IRM ; chirurgie, analogue de la somatostatine, pegvisomant). |
| M2, PP-S8-Ia | Ajout du Cushing iatrogène, placé en tête, et des endocrinopathies des anti-CTLA-4 et anti-PD-1 (hypophysite, thyroïdite, diabète). |
| M3, PP-S7-V | Ajout de l'hématome rétroplacentaire (décollement, hypertonie, CIVD ; extraction fœtale urgente) et du placenta prævia. |
| S1, PP-S7-F | Le méthotrexate est marqué « hors indication AIPS » dans la cible ; la source AIPS précise que la GEU est hors indication autorisée. |
| S2, PP-S7-C, -D, -Ia, -T | Les fiches S-xx portent `origine: dépôt interne (non opposable)`. Chaque fiche a reçu des sources externes au statut « non lu » : SGGG (référence précise à identifier), Gravholt 2017, EMAS, EMA/PRAC 2018, Swissmedic, ESMO et ESGO. |

## Moyens

| Point | Correction |
|---|---|
| E2 | Kehr : épaule gauche pour la rate, épaule droite pour le foie. |
| E3 | Correction trop rapide : myélinolyse pour l'hyponatrémie chronique, œdème cérébral pour l'hypernatrémie. |
| E4 | État hyperosmolaire : l'insuline résiduelle bloque la cétogenèse, mais pas la production hépatique de glucose. |
| E5 | L'herpès est retiré des infections transplacentaires (transmission au passage dans la filière). L'affection est renommée « TORCH (transplacentaires) ». |
| E6 | Acide folique : il réduit le risque de base, pas le risque propre au valproate (déduction, à vérifier dans l'AIPS). |
| E7 | SY-36 est retiré du cancer de l'ovaire. |
| M4 | Ajout de l'infection materno-fœtale bactérienne (streptocoque du groupe B, Listeria, chorioamniotite, endométrite) dans PP-S7-I. |
| M5 | Ajouts dans S5 : péritonite bactérienne spontanée (I) ; atrésie des voies biliaires et malrotation avec volvulus (C) ; achalasie (F) ; cholangite sclérosante primitive (A) ; syndrome de Boerhaave et ingestion de caustiques (Tr) ; thrombose porte et Budd-Chiari (V). |
| M6 | Ajouts dans S6 : maladie anti-MBG (A) ; jonction pyélo-urétérale et syndrome d'Alport (C) ; lithium, néphrite interstitielle médicamenteuse et cristallurie (Ia) ; néphropathie diabétique (D). |
| M7 | Ajouts dans S8 : dénutrition, syndrome de renutrition inappropriée et goutte (F) ; phénylcétonurie (C). |
| M8 | Ajouts dans S7 : hyperstimulation ovarienne (Ia), maladie trophoblastique (T), cryptorchidie (C). L'ostéoporose est renvoyée vers PP-S8-D par une passerelle et par `honnetete` de PP-S7-D. |
| S3 | La mention « lu » héritée devient « lu (ou résumé lu) par la fiche SY-xx, non relu ici ». |
| S4 | Les sources hors sujet sont retirées de S6-T, S6-Tr, S6-C, S8-Tr et S5-Tr. Sont ajoutées : EAU (année non vérifiée), KDIGO ADPKD, Christ-Crain 2019, ATLS, et Ferrari ASCO/SVGO 2020 pour PP-S8-D. Toutes sont au statut « non lu ». |
| S5 | `international` devient « international, non européen (dernier recours) ». |
| S6 | Les sources RMS de 2014 ou avant portent `recence: à vérifier (plus de 12 ans)`. |
| R1 | Les passerelles PHY sont désormais propres à chaque lettre, selon la liste de l'audit, complétée. |
| R2 | Doublons réduits à un renvoi : colite post-antibiotique vers PP-S5-I, urétrite vers PP-S7-I, HCS de PP-S7-C vers PP-S8-C. Des passerelles PP croisées sont ajoutées. |
| Cascades | 33 cascades sont réécrites avec des maillons verbaux. Les cascades de S5-I, S5-V et S8-Tr étaient déjà verbales. |

## Légers

| Point | Correction |
|---|---|
| E8 | « Résine fixatrice des acides biliaires » remplace « résine chélatrice ». |
| E9 | Urétrite : PCR sur premier jet chez l'homme, prélèvement vaginal ou cervical chez la femme. |
| E10 | Une note dans `honnetete` de PP-S5-F justifie le classement de la pancréatite en F. |
| S7 | EAU Urolithiasis : « année non vérifiée ». |
| R3 | Une passerelle `cours` est ajoutée partout. Son identifiant reste à résoudre (« LOT correspondant »), car il n'a pas été vérifié. |
| L4 | Les qualificatifs posologiques sont retirés ou renvoyés à l'AIPS (aminosides, stress cortisolique, Solu-Cortef, aspirine, tricyclique). |
| L5 | Tamsulosine, létrozole, misoprostol et amiloride portent la mention « statut AIPS à vérifier » ou « hors indication ». La même mention est ajoutée aux inhibiteurs de la stéroïdogenèse et au méthotrexate de la môle. |
| L6 | Mnémotechniques anglais traduits : « triple peine » et « calculs, os, ventre, tête » ; « I GET SMASHED » est remplacé par une liste française. |

## Restes honnêtes

- Les sources ajoutées n'ont pas été lues ; plusieurs références SGGG et Swissmedic restent à identifier précisément.
- L'identifiant LOT des passerelles `cours` n'est pas résolu.
- Les mécanismes des affections ajoutées relèvent de la déduction d'expert, sans relecture suisse.
- Scripts : scratchpad `pp/` (s5–s8.py puis corrections.py, valider.py).
