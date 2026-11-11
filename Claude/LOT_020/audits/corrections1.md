# LOT_020 — corrections de l'audit 1 (audit1_A, audit1_B), 11.11.2026

Vérification préalable : AIPS lues sur refdata le 11.11.2026 — Doxycyclin-Mepha 65952 (« Maladie de Lyme, stades 1 et 2 : 100 mg … deux fois par jour pendant 10-60 jours ») ; Firazyr 58178 (tableau 1 : 51–65 kg 25 mg, > 65 kg 30 mg ; 2e puis 3e injection à 6 h, au plus 3 en 24 h). Page Suva « Piqûre de tique : quelle prise en charge par l'assurance ? » (07.04.2022) lue. PNDS AOH 2024 (S3 de DX.9) lu : localisations « visage (lèvres, paupières) », langue.

Contrôles finaux : `controle3 --script-ok` VERT sur les 11 fichiers ; `verif_aips` OK, aucun BLOQUANT ; `forme.py` conforme ; tous entre 127 et 148 Ko.

| # | Fichier | Défaut | Décision |
|---|---|---|---|
| A0 | Phase A | Doxycycline 14 j « hors AIPS » | **Appliqué** (vrai : 14 j ∈ 10–60 j). La phrase vivait dans la fiche supprimée (A4) ; le tableau des médicaments écrit désormais « compris dans l'intervalle de 10 à 60 jours de l'AIPS » [S22][S3]. HELP corrigé. |
| A1 | Phase A | Icatibant enfant sans paliers 51–65 kg et > 65 kg | **Sans objet / résolu** : fiche f-ssp-m-icatibant supprimée ; la fiche f-dx9-m-icatibant porte les cinq paliers (vérifiés sur l'AIPS). |
| A2–A6 | Phase A | 5 fiches `.mb` doublées | **Appliqué** : liens vers f-dx1-m-prednisone, f-dx1-m-valaciclovir, f-dx4-m-doxycycline, f-dx9-m-adrenaline, f-dx9-m-icatibant ; sections supprimées. Faits uniques reportés dans le tableau f-ssp-p11-medic : RMS 5–10 j (prednisone) ; site cuisse antérolatérale, fesse évitée (nécrose), aiguille assez longue, contre-indications systémiques cédant devant l'indication vitale dont tachycardie paroxystique (adrénaline) ; amoxicilline avant 8 ans selon la RMS (doxycycline). Non repris : indications AIPS de l'adrénaline sans lien avec le LOT (crise d'asthme, réanimation). |
| A7 | Phase A | House-Brackmann doublée | **Appliqué** : lien vers DX.1 f-dx1-r-hb, section supprimée ; « IV–VI : antiviral et neurologie au 10e jour » reste dans DX.1. |
| A8 | DX.4 | House-Brackmann doublée | **Appliqué** : lien vers DX.1, section supprimée ; « grades IV–VI = atteinte sévère (HUG) » reste dans DX.4 (indication de l'ENMG, suivi). |
| A9 | DX.3 | House-Brackmann doublée | **Appliqué** (retrait seul) : lien vers DX.1, section supprimée ; frontière III/IV et suivi spécialisé restent dans DX.3. |
| A10 | DX.2 | Point 1 : 80/20 % HUG | **Appliqué** : phrase retirée du point 1 et déplacée en ligne du tableau f-dx2-p2-chiffres [S1] (aucun fait perdu). |
| A11 | DX.2 | Volet social et assurances absent | **Refusé** : aucune source suisse lue ne donne les règles d'aptitude à la conduite après AVC/AIT (Leitfaden Fahreignung asa 2020 lu : AVC seulement cité comme indicateur d'évaluation, sans délai). Phrase française de mortalité conservée (l'échange proposé n'a pas lieu). Lacune maintenue dans HELP. |
| A12 | DX.4 | Volet assurances (LAA) absent | **Appliqué** : 2 phrases avant 11.C, sur la page Suva lue (piqûre = accident, annonce si soins, prise en charge seulement si lien de causalité prépondérant démontré) ; nouvelle source S16. La formule « borréliose prise en charge à ce titre » de l'auditeur n'est pas reprise telle quelle (la Suva exige la preuve du lien). Ligne HELP supprimée. |
| A13 | DX.4 | Point 1 : forme tardive | **Appliqué** : phrase supprimée ; f-dx4-p8-class la porte déjà [S6]. |
| A14 | Phase A | Point 1 : asymétrie constitutionnelle | **Appliqué** : phrase supprimée ; le point 6 la porte déjà [S4]. |
| A15 | Phase A / HELP | « DGN illisible » | **Appliqué** dans HELP : DGN S3 2024 lisible (PMC12584707), faits portés par DX.4 (f-dx4-p11-choix). |
| A16 | DX.2 | Point 9 sans « 9.a » | **Appliqué**. |
| A17 | Phase A, DX.2–4 | Images manquantes | Aucune correction exigée ; non traité. |
| B0 | DX.6 | Point 1 : terme du Swiss Dental Journal | **Appliqué** (retrait, avec son appel S28 ; S28 reste citée ailleurs). |
| B1 | DX.6 | « anciennement fracture du malaire » | **Appliqué**. |
| B2 | DX.8 | « ce cours n'en donne aucune dose » | **Appliqué** en version courte (retrait seul, fichier > 145 Ko) : « L'oncologue fixe le schéma et la dose … » ; la mention RCP, plus longue, non ajoutée. |
| B3–B6 | DX.10 | Redites (voies aériennes, maternité type 3, échographie T2, polysomnographie, 42–83 %) | **Appliqué** (5 retraits ; chaque fait reste à l'endroit indiqué par l'audit). |
| B8 | DX.10 | ERN CRANIO « ensuite … recommande » | **Appliqué** (chronologie vérifiée : S3 2020, S1 2021). |
| B9 | DX.10 | « quitte ce fichier » | **Appliqué** : « cherche une cause acquise ». |
| B10 | DX.9 | Point 1 sans citation | **Appliqué** : appel S3 ajouté (PNDS lu : lèvres, paupières, langue). |
| B11 | DX.7 | Origine de la recommandation gentamicine | **Appliqué** (intitulé vérifié en bibliographie S14). |
| B12 | DX.7 | Série israélienne | **Appliqué** (S19 : Tel-Aviv). |
| B13 | DX.6 | Énophtalmie redite | **Appliqué** : « tardive (point 7.4) ». |
| B14 | DX.6–10 | Images manquantes | Aucune correction exigée ; non traité. |
| B15 | Phase A | Icatibant « en dose unique » | **Appliqué** (vrai selon AIPS 58178) : « 2e puis 3e injection possibles à 6 h d'intervalle, au plus 3 en 24 h » [S23]. |

Tailles (octets, avant → après) : Phase A 147 079 → 136 169 ; DX.2 130 047 → 130 021 ; DX.3 149 638 → 147 859 ; DX.4 132 179 → 131 353 ; DX.6 147 207 → 146 960 ; DX.7 133 024 → 133 098 ; DX.8 145 257 → 145 229 ; DX.9 136 504 → 136 548 ; DX.10 145 540 → 145 000. Fichiers > 145 Ko (DX.3, DX.6, DX.8, DX.10) : retraits nets seulement.
