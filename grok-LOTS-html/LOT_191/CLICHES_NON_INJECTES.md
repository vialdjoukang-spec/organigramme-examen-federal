# LOT_191 — 5 clichés non injectés : blocage documenté · 01.11.2026 17:35 (Europe/Zurich)

Ordre de Vial « Corrige ce qu'il faut » (alerte 3 de l'état des lieux). Règle : injecter seulement une paire PRET
(brute + annotée, même cadrage, licence libre vérifiée) ; **ne pas inventer d'image**.

Contrôle refait : `injecter_cliches.py --simuler --lot LOT_191` sur origin/grok/lots @ 96bbfb49
→ PRET 9 (déjà injectés, ce1fbb4) · A_RENDRE_WEB 2 · A_SOURCER 2 · A_RENDRE_BIO 1. Rapport : `rapports/simulation_LOT_191_20261101_1734.md`.
Inventaire `/workspace/LOT_Tunder/images_cliches_queue/LOT_191/IMG-0xx_*/` : pour les 5, seulement `candidat_Phase_B_V0_DX.n_n1|n3.png`
(captures de la leçon elle-même, pas des clichés) ; aucun `brute/IMG-xxx_brute.*`, aucun `annotee/IMG-xxx_annotee.*`, aucun `SOURCES.json`.
DISPOSITION (`/workspace/LOT_Tunder/DISPOSITION_IMAGES_LOTS.json`) : `injection = "NON FAITE"` pour les 5 (inchangé).

| IMG | Leçon / ancre | Signe | Statut | Blocage précis | Ce qui débloquerait |
|---|---|---|---|---|---|
| 052 | DX.2 #p8 (RGO du nourrisson) | Œsophagite érosive (endoscopie) | A_RENDRE_WEB | URL de la disposition = PDF (Rabeprazole.pdf), pas une image. Aucune endoscopie d'œsophagite peptique érosive sous licence libre trouvée (seulement lymphocytaire, éosinophile, histologie). | Une image endoscopique libre (CC0/BY/BY-SA/PD) d'œsophagite érosive, ou une image fournie par Vial avec droits. |
| 053 | DX.2 #p9 | Malrotation / sténose (transit) | A_SOURCER | Aucun transit œso-gastro-duodénal pédiatrique libre ; seul un schéma de bride de Ladd existe. | Un TOGD pédiatrique libre, ou accord de Vial pour un schéma pédagogique (marqué « schéma »). |
| 054 | DX.4 #p9 | Bandelette leucocytes / nitrites | A_RENDRE_BIO | Seule photo libre (Comp.Urine.Test.Strip.jpg, CC BY-SA 3.0) montre leucocytes et nitrites **négatifs** : ne montre pas le signe. | Accord de Vial pour un schéma original de bandelette (comme IMG-064), ou photo libre positive. |
| 059 | DX.6 #p8 | Volvulus du grêle sur malrotation (tourbillon) | A_SOURCER | Seulement volvulus sigmoïde adulte (TDM) ou animal : hors sujet. | Image libre d'un tourbillon mésentérique pédiatrique (écho-Doppler ou TDM). |
| 062 | DX.9 #p8 | Dysfonction ventriculaire (échocardiographie) | A_RENDRE_WEB | URL de la disposition = PDF hors sujet. Candidat ECHOpedia E00473 (PLAX, CMD, CC BY-SA 3.0) : contours du VG pas assez sûrs sur image fixe ; « Dilated cardiomyopathy B-Mode.jpg » = chien, exclu. | Relecture d'un cardiologue sur la frame E00473, ou autre écho libre humaine. |

Aucune injection, aucun commit d'image, aucune capture QC (pas d'injection réelle). Les 9 paires de ce1fbb4 restent en place.
