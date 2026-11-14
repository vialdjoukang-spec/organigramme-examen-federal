# Audit médical agressif : A-MOT-26 à A-MOT-60 (anamnèse orientée par motif)

Auditeur indépendant (je n'ai rien rédigé), 14.11.2026. Objet : 35 fiches JSON (212 Ko). Schéma : `SCHEMA_A_M_KK.md`.

## 1. Ce que j'ai fait

| Contrôle | Méthode | Résultat |
|---|---|---|
| Numéros SSP (35 fiches) | Comparaison avec la liste SSP 1-265 de PROFILES 2017 (texte extrait du PDF) | 35/35 corrects |
| Axes ASSM | Lecture du guide ASSM 2022 § 3.2 (Zenodo 7148494, PDF téléchargé) ; script de présence des axes | Axes conformes. « Lieu » ou « Facteurs d'influence » manquent dans 22 fiches (justifié pour 52, 55, 59, 60, discutable pour 28, 39) |
| Renvois S/SY/IMG | Script : existence des identifiants dans `status/`, `syndromes/`, `recensement.json` | Aucun lien cassé. 3 renvois cités dans le texte manquent dans `liens` (40 : SY-11 ; 54 : SY-12 ; 58 : S-35). 33 renvoie à IMG-046 (cellulite orbitaire), absente de la fiche |
| « Lu » HUG | Téléchargement et lecture de 11 stratégies HUG (Céphalées 2022, IVRS 2021, Dépression 2022, Alcool 2021, Fièvre au retour 2026, Œil rouge 2025, Monoarthrite 2024, Entorse 2024, Troubles anxieux 2023, Lombalgie 2022, Otite externe 2022) et 3 copies locales (Vertiges 2024, Personne âgée 2026, Dépistage 2026) | 14 stratégies vérifiées. Les extraits cités sont fidèles (Centor, RUD, PHQ-2, ACME, paludisme, Ottawa, « 3 C », StartBack, timing/trigger). Je n'ai pas vérifié : protocole HUG « Vertige isolé aigu » 2020, Anémie 2022, Carences vitaminiques 2025, Urticaire 2023, Vaccination 2025, SMC 2024, Gardier RMS 2018 |
| ASSM § 3.6 (alcool) | Lecture du PDF ASSM | Seuil « plus de 4 / plus de 2 verres » bien présent dans l'ASSM, mais contredit par HUG 2021 (voir M-6) |
| Synthèses orales | Script : nombre de phrases | 35/35 en 2 phrases |

## 2. Score (§ 12.2 : 2 = conforme, 1 = partiel, 0 = absent)

| Critère | Score | Raison |
|---|---|---|
| Questions (axes ASSM) | 1 | Questions justes et en langage du patient ; axes incomplets en 28 et 39 |
| Drapeaux rouges | 1 | Lacunes graves en 26 (SNNOOP10), 27 (chute), 31 (AVC) |
| Hypothèses VITE DIT CAFé | 2 | Classement gravité puis fréquence respecté, sauf 57 (Léger) |
| Questions discriminantes | 2 | Pertinentes et verbales |
| ICE | 1 | Triplet générique identique dans 21 fiches sur 35 |
| Synthèse orale | 2 | Deux phrases, décision explicite |
| Renvois S/SY/IMG | 2 | Aucun lien cassé ; 4 oublis légers |
| Numéros SSP | 2 | 35/35 vérifiés |
| Sources et étiquetage | 1 | « Lu » fidèle là où je l'ai vérifié ; conduites mal étiquetées en 26 et 28, seuil d'alcool périmé en 55 |
| Phrases verbales | 2 | Respectées ; quelques pièges restent nominaux (36 : Centor) |

## 3. Défauts et PATCH exacts

| # | Grav. | Fiche, champ | Extrait fautif (≤ 200 car.) | PATCH exact | Source |
|---|---|---|---|---|---|
| G-1 | **Grave** | 26 `drapeaux_rouges` | 6 drapeaux seulement, alors que la source citée « lu : tableau 2 SNNOOP10 » en compte 15 | Ajouter 4 objets : ① `{"question":"Avez-vous eu un cancer, ou une maladie ou un traitement qui affaiblit vos défenses (VIH, greffe, chimiothérapie) ?","si_oui":"Céphalée nouvelle sur néoplasie ou immunodépression : chercher une métastase ou une infection opportuniste par imagerie cérébrale rapide (HUG 2022, tableau 2)."}` ② `{"question":"Le mal de tête change-t-il avec la position, ou la toux, l'éternuement ou l'effort le déclenchent-ils ?","si_oui":"Céphalée positionnelle ou d'effort : chercher une hypo- ou hypertension du LCR, une masse de la fosse postérieure ou une thrombose veineuse ; demander une imagerie (HUG 2022, tableau 2)."}` ③ `{"question":"Ce mal de tête date-t-il de moins de 3 mois, a-t-il changé de caractère, ou s'aggrave-t-il de jour en jour ?","si_oui":"Céphalée récente ou progressive : examiner le fond d'œil (œdème papillaire) et demander une imagerie (HUG 2022, tableau 2)."}` ④ `{"question":"Avez-vous mal autour d'un œil, avec l'œil rouge qui larmoie ou une paupière tombante ?","si_oui":"Œil douloureux avec signes autonomes : algie vasculaire, mais aussi lésion hypophysaire ou du sinus caverneux, ou glaucome aigu ; demander une imagerie ou un avis ophtalmologique (HUG 2022, tableau 2)."}` | HUG Céphalées 2022, tableau 2 (lu) |
| G-2 | **Grave** | 27 `drapeaux_rouges` (titre « … chutes », SSP 96) | Aucun drapeau sur la chute | Ajouter `{"question":"Êtes-vous tombé, vous êtes-vous cogné la tête sous anticoagulant, ou êtes-vous resté longtemps au sol ?","si_oui":"Chute à risque : chercher un hématome sous-dural (TDM au moindre doute sous anticoagulant), une fracture, une rhabdomyolyse, puis évaluer le risque de chute de manière multifactorielle (HUG, Personne âgée 2026, § 4.3 ; A-MOT-58)."}` | HUG Personne âgée 2026 § 4.3 (lu, copie locale) |
| G-3 | **Grave** | 31 `drapeaux_rouges`, `hypotheses[V]`, `liens` | Aucun déficit sensitif brutal unilatéral → filière AVC | Ajouter `{"question":"L'engourdissement est-il apparu d'un coup, d'un seul côté du corps (visage, bras, jambe) ?","si_oui":"Déficit sensitif brutal et unilatéral : AVC ou AIT jusqu'à preuve du contraire ; appeler le 144 et activer la filière AVC (A-MOT-28, SY-12)."}` ; placer « AVC ou AIT (déficit hémicorporel brutal) » en tête de `hypotheses[V].diagnostics` ; ajouter `SY-12` et `IMG-001` aux `liens` | Déduction (non vérifié CH) |
| M-1 | Moyen | 26 `drapeaux_rouges[0].si_oui` | « …TDM cérébrale sans injection immédiate, puis une ponction lombaire si la TDM est normale (déduction, non vérifié CH). » | « …adresser aux urgences : une angio-TDM faite dans les 6 heures est très sensible ; au-delà de 6 heures et avec une imagerie normale, la ponction lombaire est indiquée (HUG 2022, tableau 7 et § 5.3). » | HUG Céphalées 2022 (lu) |
| M-2 | Moyen | 28 `drapeaux_rouges[0]` et `[3]` | « …commencé brutalement il y a moins de 24 heures ? » ; « Avez-vous eu de la fièvre ou êtes-vous diabétique sous insuline ? » → glycémie | [0] question : « Le déficit a-t-il commencé brutalement ? » ; si_oui : « AVC jusqu'à preuve du contraire, quel que soit le délai : appeler le 144 et activer la filière AVC ; l'heure de dernière vue normale décide de la thrombolyse ou de la thrombectomie (délais : Swiss Stroke Society, À vérifier). » [3] question : « Êtes-vous diabétique, sous insuline ou sulfonylurée ? » ; si_oui : « Mesurer la glycémie capillaire chez tout patient : une hypoglycémie imite un AVC (SY-55) ; la mesure ne retarde pas la filière AVC. » | Déduction ; source suisse non lue |
| M-3 | Moyen | 32 `drapeaux_rouges[3].si_oui` | « AIT rétinien : bilan neurovasculaire rapide (carotides). » | « AIT rétinien : urgence neurovasculaire le jour même, par la filière AVC comme tout AIT ; imagerie des carotides (A-MOT-28). » | Déduction (non vérifié CH) |
| M-4 | Moyen | 33 `drapeaux_rouges`, `hypotheses[I]` | IMG-046 (cellulite orbitaire) liée, mais la cellulite orbitaire ne figure nulle part | Ajouter `{"question":"Avez-vous de la fièvre, la paupière gonflée, l'œil qui avance, ou mal en bougeant l'œil ?","si_oui":"Cellulite orbitaire : urgence (cécité, thrombose du sinus caverneux) ; hospitaliser et demander une imagerie orbitaire (IMG-046)."}` ; ajouter « cellulite orbitaire » en tête de `hypotheses[I]` | Déduction (non vérifié CH) |
| M-5 | Moyen | 36 `hypotheses` | Aucun diagnostic vasculaire ; Lemierre absent | Ajouter `{"lettre":"V (vasculaire)","diagnostics":["syndrome coronarien aigu (douleur projetée à la gorge)"],"question_discriminante":"La gêne arrive-t-elle à l'effort et cède-t-elle au repos, sans fièvre ni douleur en avalant ?"}` ; ajouter « syndrome de Lemierre » après « abcès… rétropharyngé » | Déduction (non vérifié CH) |
| M-6 | Moyen | 55 `pieges[1]` | « Consommation à risque : plus de 4 verres standard par jour chez l'homme, plus de 2 chez la femme ; … (ASSM § 3.6 ; HUG 2021 : 10 g). » | « Faible risque (Addiction Suisse, repris par HUG 2021) : 2 verres standard par jour au plus chez l'homme, 1 chez la femme, et 2 jours sans alcool par semaine. Consommation chronique à risque : plus de 30 g (3 verres) chez l'homme, plus de 20 g (2 verres) chez la femme ; 1 verre = 10 g (HUG 2021). L'ASSM 2022 (§ 3.6) cite encore l'ancien seuil de 4 et 2 verres. » | HUG Alcool 2021 § 2.1 et 2.4 (lu) ; ASSM § 3.6 (lu) |
| M-7 | Moyen | 38 `pieges[2]` | « Ne pas prescrire d'antibiotique avant la ponction. » | « Ponctionner avant l'antibiotique, sauf en cas de sepsis : prélever alors les hémocultures et débuter l'antibiotique sans attendre (HUG 2024). » | HUG Monoarthrite 2024 (lu) |
| M-8 | Moyen | 51 `drapeaux_rouges[0].si_oui` | « …tout patient à risque doit être référé en urgence au psychiatre (HUG 2022 ; A-MOT-52). » | « Évaluer immédiatement par le RUD, puis grader le risque : s'il est faible, suivi ambulatoire ; s'il est moyen, suivi psychiatrique ambulatoire ou hospitalisation ; s'il est élevé, urgences psychiatriques (HUG 2022, tableau 4b ; A-MOT-52). » | HUG Dépression 2022, tableau 4b (lu) |
| M-9 | Moyen | 52 `questions[].axe`, `drapeaux_rouges[0]` | « Idées (R : risque) » ; « Antécédents » séparés de R ; pas de 144 | Renommer : « Idées suicidaires » ; « Plan et imminence (U : urgence) » ; « Moyens et létalité (D : dangerosité) » ; « Antécédents » devient « Facteurs de risque (R : risque) ». Ajouter à [0].si_oui : « En cas de danger immédiat, appeler le 144. » | RUD selon HUG 2022 § 3.1 (lu) ; correspondance R, U, D : déduction |
| M-10 | Moyen | ICE de 27, 29, 31-35, 38, 40-44, 46-50, 53, 56 | Le triplet « Qu'est-ce qui, à votre avis, provoque… / …inquiète le plus ? / …consultation d'aujourd'hui ? » est identique dans 21 fiches | Remplacer la 2e question par une crainte propre au motif. Exemples : 27 « Avez-vous peur d'une attaque cérébrale ou de tomber ? » ; 31 « Craignez-vous une sclérose en plaques ou de perdre l'usage de la main ? » ; 46 « Avez-vous peur d'un cancer ? » | ASSM § 3.2 (lu) |
| M-11 | Moyen | 35 fiches, `sources[-1]` | Ligne générique « Éléments cliniques non couverts… déduction d'expert » | Garder la ligne, mais étiqueter chaque conduite non sourcée dans son champ (« déduction, non vérifié CH »). Exemples : 31 DR, 36 DR 1-3, 37 DR 2-6, 46 DR 1-2 | Prompt V0 § 23 |
| L-1 | Léger | 26 `hypotheses` | Thunderclap sans SVCR ni apoplexie hypophysaire ; CO absent | V : ajouter « syndrome de vasoconstriction cérébrale réversible ; apoplexie hypophysaire » ; I (iatrogène) : renommer en « I (iatrogène, toxique) » et ajouter « intoxication au monoxyde de carbone » | HUG Céphalées 2022 (lu) |
| L-2 | Léger | 39 `synthese_cs` | « …douleur à la palpation de la malléole latérale. » | « …douleur à la palpation du bord postérieur et de la pointe de la malléole latérale (sur 6 cm). » | HUG Entorse 2024 (lu) |
| L-3 | Léger | 28, 39 `questions` | Axe « Facteurs d'influence » absent | 28 : « Le trouble a-t-il commencé après un effort, un mouvement brusque ou une manipulation du cou ? » ; 39 : « Qu'est-ce qui aggrave ou soulage la douleur : l'appui, le mouvement, la glace ? » | ASSM § 3.2 (lu) |
| L-4 | Léger | 40, 54, 58 `liens` | SY-11, SY-12, S-35 cités dans le texte, mais absents des liens | Ajouter `SY-11` (40), `SY-12` (54), `S-35` (58) | Script |
| L-5 | Léger | 57 `hypotheses[C]` | « sténose du pylore ; malrotation… » | Placer « malrotation (volvulus) » en premier, car elle est plus grave | Gravité puis fréquence |
| L-6 | Léger | 29 `hypotheses[C]` | « épilepsie focale structurelle » classée congénitale | Remplacer par « malformation du développement cortical » | Déduction |
| L-7 | Léger | 42 `drapeaux_rouges[4]` | « évaluer le qSOFA » sans étiquette | Ajouter « (source internationale, Sepsis-3 ; non vérifié CH) » | Règle Vial |
| L-8 | Léger | 49 et 59 `sources` | 49 « (résumé : points à retenir) » ; 59 sans DOI | 49 : « (lu partiellement : points à retenir) » ; 59 : ajouter « DOI 10.53738/REVMED.2026.22.976.49183 » | Copie locale HUG Dépistage 2026 |
| L-9 | Léger | 54 `pieges[0]` | « (SMC 2024 cite le status après état confusionnel parmi les drapeaux rouges cognitifs) » est incompréhensible | Reformuler : « La SMC classe un trouble cognitif après un état confusionnel parmi les drapeaux rouges (SMC 2024, à vérifier). » | SMC non vérifiée par moi |
| L-10 | Léger | 55 `questions[0][2]` | « 4 verres ou plus (femme), 5 verres ou plus (homme) » | « plus de 4 verres (femme), plus de 5 (homme) », pour suivre le seuil HUG 2021 § 2.4 | HUG Alcool 2021 (lu) |

## 4. Points conformes vérifiés

Ces points sont justes : le Centor et sa conduite (36), la répétition de la recherche de paludisme et l'incubation de 7 jours ou plus (42), le PHQ-2 positif dès une réponse « oui » (41, 51), l'ACME dès une réponse positive puis l'AUDIT (55), le timing et le trigger, puis le HINTS (27), les « 3 C » (38), Ottawa et le contrôle à 7-10 jours (39), StartBack et l'absence d'imagerie (37), la douleur parfois absente chez le diabétique (33), les gouttes ototoxiques en cas de perforation (34), les trois questions sur les chutes et STOPP/START (58), la décision partagée pour le dépistage (59). Les 35 numéros SSP sont corrects. Les étiquettes non suisses (HAS, NEXUS, CAM, Wessel, McIsaac) sont présentes.

## 5. Verdict

| Question | Réponse |
|---|---|
| Les fiches A-MOT-26 à 60 peuvent-elles recevoir `audit-ok` en l'état ? | **Non** |
| Ce qui manque | G-1 à G-3 (SNNOOP10 incomplet, chute absente de 27, filière AVC absente de 31) et M-1 à M-11. Après application des PATCH, une contre-vérification courte suffit |
| Limites de l'audit | Je n'ai pas vérifié 7 sources citées « lu » (voir § 1). Les recommandations de la Swiss Stroke Society, de la Ligue contre l'épilepsie et du CEMV restent non lues dans les fiches comme dans cet audit |
