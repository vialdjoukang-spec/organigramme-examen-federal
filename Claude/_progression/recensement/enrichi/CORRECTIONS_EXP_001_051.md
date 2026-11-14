# Corrections : EXP-001 à EXP-051 (`enrichi/EXP_a.json`), 14.11.2026

Ces corrections répondent à `AUDIT_EXP_001_051.md`. Le JSON a été validé avec `json.load` et contient toujours 51 entrées. Les citations AIPS ont été relues par URL refdata, avec `aips_fiche.py` et le cache local.

| # | Statut | Correction appliquée |
|---|---|---|
| C1 | Fait | **007** : l'EEG est retiré des examens admis par l'ASSM ; il sert seulement à explorer un facteur confondant. Le seuil de 2 µV est attribué à l'ACNS (source américaine). L'examen de perfusion devient obligatoire dans les 4 situations ASSM. Les examens admis sont l'angio-TDM avec perfusion, l'angiographie numérique soustraite (ASN), l'angio-IRM avec perfusion et le duplex transcrânien codé couleur (déconseillé chez l'enfant). Les traces et la lecture ont été réécrites. |
| C2 | Fait | **007** : source ASSM 2017 datée (approuvée le 16.05.2017, en vigueur depuis le 15.11.2017). Le projet 2025 est signalé (consultation du 16.06 au 19.09.2025, non adopté). Le gold précise le principe des quatre yeux et le test d'apnée jusqu'à une PaCO2 ≥ 60 mmHg (8 kPa). |
| C3 | Fait | **002** : citation mot pour mot de Rivotril i.v. (AIPS n° 37756, octobre 2023) : « 1-4 mg suffisent », vitesse 0,25–0,5 mg/min, dose totale ≤ 10 mg. Lorazepam Xilmac est noté sans indication d'état de mal et destiné à l'étranger. |
| C4 | Fait | **001 et 006** : restriction du valproate citée mot pour mot (posologie et contre-indication), d'après l'AIPS Depakine n° 34734, septembre 2025. L'éthosuximide reste « AIPS absente (À vérifier) ». |
| C5 | Fait | **016** : pénalisation par atropine collyre 0,5 %, « 1 goutte 1 à 3 fois par jour », avec surveillance et compression du canal lacrymal (AIPS Atropine SDU Faure n° 46994, novembre 2025). |
| G1 | Fait | **008** : McDonald 2024. Le nerf optique devient la 5e localisation, prouvée par IRM, OCT ou PEV. Sources : Montalban et Saidha 2025 (résumés). |
| G2 | Fait | **009** : ERC-ESICM 2025, prévention de la fièvre ≤ 37,5 °C pendant 36 à 72 h, prédicteurs de bon pronostic (NSE < 17 µg/l). Le Swiss Resuscitation Council est noté « À vérifier ». |
| G3 | Fait | **048 et 049** : ERC 2025 ALS cité, avec l'algorithme bradycardie pour 049. |
| G4 | Fait | **025** : règle INFARCT exacte (un seul signe suffit) ; le HINTS est limité au syndrome vestibulaire aigu continu. |
| G5 | Fait | **016** : PEDIG est désormais étiqueté « Source américaine ». Source suisse cherchée mais non trouvée, notée « À vérifier ». |
| G6 | Fait | **006** : Synacthen (AIPS n° 31723) indique bien le syndrome de West, mais **aucune posologie pédiatrique** n'y figure ; la dose n'est donc pas citée. L'ACTH est placée au même rang que la vigabatrine. **013** : citations mot pour mot de Vabysmo 6 mg (n° 68395) et d'Eylea 2 mg (n° 62393). |
| G7 | Fait | **035** : la mise en garde Prednisone et myasthénie est citée mot pour mot, avec l'arrêt des anticholinestérasiques 24 h avant. |
| M1 | Fait | **001** : citation de la forme orale (Levetiracetam DESITIN cpr n° 65154, février 2025), avec les doses de 500 et 250 mg deux fois par jour. |
| M2 | Fait | **004** : première intention = IRM puis PL, aciclovir sans attendre. **046** : première intention passée à `null`. |
| M3 | Fait | **051** : seuil FC max < 85 % de la FMP ou indice chronotrope < 0,8. L'exemple montre une réserve de 56 %. |
| M4 | Fait | **037** : Gold Coast exige au moins 2 régions. |
| M5 | Fait | **010** : EGS 6e éd. 2025. |
| M6 | Fait | **037** : EAN/ERN 2024 (À vérifier). **033** : NeuPSIG 2025 (À vérifier). |
| M7 | Fait | **005** : OFSP et NRPE Zurich ; CDC étiqueté « source américaine » ; Hermann 2021 (À vérifier). |
| M8 | Fait | **023, 041, 044** : sources étiquetées « source américaine ». **041 et 044** : aucune source européenne trouvée, notée « À vérifier ». **027** : IGHG 2019 ajouté (À vérifier). |
| M9 | Fait | **002, 004, 005** : gabarit de lecture EEG du patient comateux (réactivité aux stimuli, pas d'hyperpnée). |
| L1 | Fait | **006** : sensibilité de 10 µV/mm chez l'enfant, unifiée. |
| L2 | Fait | **033 et 034** : température cutanée ≥ 30 °C aux membres inférieurs. |
| L3 | Fait | **018 à 021 et 026** : seuil normal < 20 dB HL. |
| L4 | Fait | **019** : otospongiose de type A ou As. |
| L5 | Partiellement | **045** : critère « AVC, AIT ou embolie systémique » corrigé. **Réduction d'apixaban si clairance 15–29 ml/min non appliquée** : l'AIPS suisse Eliquis n° 61549 ne la prévoit pas dans la fibrillation auriculaire non valvulaire (seulement 2 critères sur 3 parmi âge, poids et créatinine). J'ai ajouté « non recommandé si clairance < 15 ml/min ou dialyse », comme l'indique l'AIPS. |
| L6 | Fait | **002** : ESETT étiqueté « source américaine ». **011** : Pituitary Society 2023. |
| L7 | Fait | **029** : la référence Vogt est remplacée par le consensus RIGA, Rhinology 2018;56:133 (À vérifier). |
| L8 | Partiellement | J'ai cherché sur le web le 14.11.2026 et ajouté deux sources suisses : Ligue suisse contre l'épilepsie (« Épilepsie et conduite » 2019, flyer epi.ch 2026, en 001) et Suva (audiomobile, feuillet 1909, en 021). **SSC (adoption ESC) et SGKN restent « non lu, À vérifier ».** |

Restent « À vérifier » : AIPS éthosuximide, endossement des recommandations ESC par la SSC, normes ENMG suisses, Swiss Resuscitation Council, source suisse du dépistage visuel.
