# Auto-audit — prototype Urgences cardio (17.11.2026)

Le détail ligne par ligne se trouve dans `docs/AUDIT-donnees.md` (généré par `node tests/audit.js`).

## 1. Sources suisses lues

| Id | Source | Ce qui a été lu |
|---|---|---|
| hug-smur-sca | HUG, Brigade sanitaire cantonale — Protocole SMUR 5.1.1 SCA v1.7b (15.12.2023), réf. ESC 2023 | PDF intégral |
| hug-smur-liste | HUG — page des protocoles SMUR (journal des modifications) | page |
| bs-algo-2026 | Algorithmen für die präklinische Notfallmedizin v2.0 (01.11.2026) — RD KSBL, RD NordWestSchweiz, Sanität Basel, RD Winterthur, RD Einsiedeln (PDF publié par Bâle-Ville) | C6 SCA, C7 Aortendissektion, fiches ASS et héparine |
| kssg-acs | Kantonsspital St.Gallen (hôpital cantonal, source complémentaire) — Kardiovaskuläres Manual 2023, ACS (fondé sur ESC 2017/2018/2020) | chapitre + algorithme 0/1 h |
| kssg-aorte | KSSG — Akutes Aortensyndrom | chapitre + algorithme |
| kssg-le | KSSG — TVT et embolie pulmonaire | partie EP |
| rms-pericarde-2016 | Rev Med Suisse 2016;12:1475-8 (Hôpital du Valais) | PDF |
| unige-daa-2009 | Thèse UNIGE 2009, dissection aortique aux urgences | thèse |
| rms-sca-2024 | Rev Med Suisse 2024;20:1026-31 (HUG), ESC 2023 | résumé seul (payant) — non utilisé dans les cartes |

Pharmacologie (autorisé) : OpenStax *Pharmacology for Nurses* (20.2, 20.3, 18.4, 18.7, 14.3) ; StatPearls « Troponin Testing » (résumé via Europe PMC ; NCBI bloque la lecture automatisée par reCAPTCHA, non contourné).

## 2. Affirmations sans source suisse (« À vérifier » visibles)

- **Règle « pas d’antithrombotique avant exclusion d’une dissection suspectée »** : recherche ciblée de 15 min (17.11.2026) dans des sources CHUV, Inselspital, USZ et sociétés suisses : aucune formulation explicite trouvée. Lus sans résultat : page Herzchirurgie de l’Inselspital, *Précis d’anesthésie cardiaque* (pac6.ch), algorithmes préhospitaliers bâlois v2.0 (C6 SCA : aspirine et héparine sans mention de la dissection ; fiches ASS et héparine : la dissection ne figure pas dans les contre-indications ; C7 : aucun antithrombotique dans l’algorithme). Appui indirect : KSSG (hôpital cantonal ; imagerie d’abord, traitement initial sans antithrombotique) et thèse UNIGE (décès après aspirine, clopidogrel et énoxaparine). La règle reste « À vérifier » sur les fiches Dissection, Aspirine, HNF et P2Y12.
- **Correction 1 (hypotension / bradycardie)** : sourcée. L’algorithme bâlois C7 baisse la TA seulement si TAS > 120 mmHg et réserve le bêtabloquant à FC > 60/min ; la thèse UNIGE et le KSSG relient hypotension, tamponnade et rupture ; le KSSG oriente le type A vers la chirurgie urgente. Le duel 1 sanctionne désormais le bêtabloquant (TA 82/50, FC 58).
- **Correction 2 (dossier)** : l’angio-CT s’affiche « Négatif : pas de dissection » avant le duel 2 ; la consigne rappelle que le type A peut atteindre la coronaire droite et mimer un STEMI inférieur (UNIGE ; bâlois C7 : « STEMI-Äquivalente »).
- **Infarctus du VD** : mécanisme (occlusion proximale de la coronaire droite) et sémiologie (hypotension, poumons clairs) non lus dans une source suisse.
- **STEMI** : le mécanisme thrombotique n’a pas de source lue (science fondamentale ; à sourcer en physiopathologie).
- **Oxygène** : absence de bénéfice sans hypoxémie non lue ; le seuil « SpO₂ < 90 % » est sourcé (KSSG ; HUG écrit « FiO₂ < 90 % », coquille probable signalée dans la fiche).
- **Opioïdes** : contre-indications détaillées non lues.
- **Péricardite** : la source suisse date de 2016 (ESC 2015) ; une mise à jour européenne récente existe — à vérifier.
- **Raretés** : seules Dissection (≈ 6/100 000/an, KSSG), Péricardite (≈ 5 % des douleurs thoraciques aux urgences, RMS 2016), ECG, Troponine, Aspirine et HNF ont une justification sourcée ; les autres raretés sont des choix pédagogiques marqués « À vérifier ». Aucun poids d’examen PROFILES n’est affirmé.
- Divergence signalée : **P2Y12** — le KSSG (ESC 2017/2020) prévoit le ticagrélor dès le STEMI ; les HUG ont retiré la double antiagrégation préhospitalière (déc. 2023). Le jeu donne un verdict « Info » et renvoie au cardiologue.

## 3. Doses

Aucune dose n’est affichée. Les sources lues contiennent des doses (HUG : ASA, héparine, fentanyl ; KSSG : ASA, ticagrélor, prasugrel, clopidogrel, HNF, énoxaparine, métoprolol, morphine, nitroglycérine, alteplase, tirofiban, cangrelor, argatroban). Elles **n’ont pas été reprises** : ce sont des doses de protocole, pas des extraits de l’information professionnelle suisse (swissmedicinfo.ch). Chaque fiche médicament affiche « Posologie : À vérifier ».

## 4. Écarts avec les skills chargés

- `ssp-chaine-clinique` : le gabarit (geste → sémiologie → exploration → prise en charge) structure les fiches pathologie, mais les champs G8 complets (`mecanisme`, `principe`, `pourquoi_ce_choix`, `precautions`, `alternative` pour chaque examen et chaque moyen) ne sont pas tous remplis ; les fichiers `data/ck/*.json` du projet SSP ne s’appliquent pas à ce dépôt. Le brief (prototype de jeu) a primé.
- `ssp-chaine-clinique` admet une source européenne à défaut de suisse ; le brief l’interdit sauf renvoi suisse : le brief a primé.
- `ssp-verite` : chaque affirmation cite URL et date ; le numéro de paragraphe n’est pas noté.
- `ssp-posologie-suisse` : aucune dose, donc aucune extraction AIPS nécessaire. Les doses restent non validées par un médecin.

## 5. Validation humaine requise

La relecture médicale relève de Dr Vial Djoukang (médecin). Le contenu est pédagogique, pas un protocole.

Tout le contenu clinique doit être relu par un médecin avant usage. Les tests automatiques vérifient la mécanique et la présence des sources, pas l’exactitude médicale.
