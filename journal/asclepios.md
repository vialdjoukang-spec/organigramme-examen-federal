# Journal Asclépios
## 17.10.2026 — Étape 1 (audit examen physique, sans modification de app_v2.html)
- Extraits : GES, PHT, NOT, TIP via tools/json_inject.py (non commités).
- Scripts réutilisables : tools/audit_examen/analyse.py (stats, matrice auto, signaux d'ordre, doublons ; lancer depuis la racine), render.py (MD → PDF Chrome headless), sk.py (licences Wikimedia via API).
- Livrables : /workspace/ssp/audit_examen/AUDIT_examen_physique.{md,pdf}.
- Résultat : 308 gestes / 20 régions (3 axes mélangés) ; 7 lacunes, 12 doublons, 9 violations d'ordre confirmées (48 signaux auto) ; TIP champ 5 : 15 vides, 6/233 structurés par région.
- Étape 2 bloquée en attente de validation par Vial.

## 17.10.2026 — Étape 2 (validée par Vial)
- tools/asclepios/ges_v2.py : 3 axes, sous-régions (tête-cou 6, TR-OGE 4, rachis 5, coude-main 2), module Vaisseaux périphériques (8 gestes déplacés du cœur), module Relevé ganglionnaire (3 gestes nouveaux), ATM, globe vésical, neuro-vasculaire distal épaule et genou ; 9 violations d’ordre corrigées ; 12 doublons → 23 paires de renvois.
- tools/asclepios/tip_exam.py : champ 5 de 198 SSP réparti par région puis par phase, éléments d’origine verbatim (0 perdu, 196 intertitres conservés en italique), 728 puces vers les gestes ; 15 vides « À compléter » ; 35 laissés (moins de 25 % d’éléments anatomiques).
- Croquis : 19 intégrés ; écartés : photo de mesure tensionnelle (personne identifiable), Gray1218 (montre le cœur, pas les poumons) remplacé par Gray965.
- Tests : 72/72 (dont test_examen 16/16), gardes 5/5.

## 17.10.2026 — Étape 3 (champ 5 de TIP : 15 champs écrits, 113 blocs « Autres éléments ciblés » revus)
- Scripts rejouables : tools/asclepios/tip_revue.py applique tip_nouveaux.py (15 champs), tip_sources.py (sources) et tip_autres_a/b/c.py (113 blocs) à data/TIP.json extrait de main ; un élément rattaché à une région rejoint le bloc de cette région (doublons exacts retirés).
- Sources lues le 17.10.2026 : S3 Polytrauma AWMF 187-023 v5.0 (DGU) ; S2k brûlures AWMF 044-001 v8.0 (DGV) ; S3 Müdigkeit AWMF 053-002 (DEGAM) ; ERC 2021 BLS et circonstances particulières (Notf Rett Med) ; lignes directrices scandinaves TCC 2013 ; ESVS 2025 traumatismes vasculaires (recommandations 82 à 84) ; ESGE 2016 corps étrangers (résumé) ; Refardt et Christ-Crain, SMW 2020 (déjà citée en G3).
- Non lues (bloquées ou non trouvées) : ESC 2022 mort subite (academic.oup.com refuse) ; SOSORT ; plan suisse de vaccination ; points marqués « À vérifier » dans le texte.
- Corrections notables : Weber/Rinne (sens de latéralisation et Rinne négatif), angle d’Adams « 5–77° » → 5 à 7° (À vérifier), Epworth (seuil sévère À vérifier), test ABO au lit (il détermine le groupe du receveur), Prehn (n’exclut pas une torsion), HINTS (impulsion normale = cause centrale), ROR adulte (né après 1963, À vérifier), index de pression systolique non indiqué en traumatisme de membre (ESVS 83), apostrophes et « l’+A+' » corrigés, phrases tronquées réécrites.
- Glossaire : ESVS, ESGE (abréviations, sourcées) ; 3 éponymes décrits sans nom en attendant Galien (Cogan, Hoffmann, Lasègue) ; liste dans journal/nerfs-ck.md.
- Reste hors périmètre, signalé : les blocs régionaux du champ 5 gardent des fragments d’origine (ex. S1.12 « Otoscopie », « tympan normal (perception) ») ; le champ 12 (Points clés) de S8.1 à S8.12 est corrompu (« &lt;• p• &gt;• … »).
- Tests : 199/199, gardes 5/5, test_examen avec 2 contrôles nouveaux (tip_sans_a_completer, tip_autres_rediges).

## 17.10.2026 — Étape 4 (bloc trauma S8.1–S8.12)
- Scripts rejouables : tools/asclepios/s8_a.py, s8_b.py (contenu), s8_apply.py (applique à data/TIP.json et data/NOT.json extraits de main).
- 60 diagnostics différentiels (5 par SSP, format « Ce que c’est · Ce qui la distingue · Délai · Conduite · Piège »), dont 42 sourcés (v.d « complété ») ; les 18 autres portent « À vérifier » dans le texte.
- Rubriques réécrites : 3 (démarche), 4 (anamnèse et drapeaux rouges), 12 (points clés, ex-« &lt;• p• &gt; »), 13 (pièges) pour les 12 SSP ; rubrique 6 écrite pour S8.8–S8.12 (vide) et 7 puces tronquées remplacées pour S8.1, S8.2, S8.4–S8.7.
- Retirés car non sourcés ou faux : « céfazoline 2 g » (dose inventée), « PAS 120/min », « RR × 8 », « 20–50 % » de l’intervalle libre, « 6 P de Pratt ».
- Sources (lues le 17.10.2026) : S3 Polytrauma 187-023 (1.1, 1.5, 1.7, 1.8, 2.6 à 2.11, 2.13, 2.14, 2.17) ; S2k brûlures 044-001 (recommandations 2 à 30) ; ERC 2021 circonstances particulières (noyade, hypothermie) et réanimation de base (obstruction) ; ESGE 2016 (recommandations 1 à 10, résumé Europe PMC) ; lignes scandinaves 2013 (recommandation 1) ; ESVS 2025 (recommandation 83).
- À vérifier : gelure (aucune source lue) ; signalement de maltraitance (règles cantonales) ; nerf axillaire ; luxation postérieure de l’épaule ; signes de fracture de la base du crâne ; signes de perforation de l’œsophage ; inhalation d’un corps étranger chez l’enfant ; scaphoïde ; corps étranger de plaie ; tétanos (plan suisse) ; doses d’antibiotiques (Compendium) ; choc neurogène ; queue de cheval ; rachis rigide ; lésion veineuse majeure ; DD sans source (hématome sous anticoagulant, rachis du plongeur, cause de la noyade, os pathologique, tendon, infection de plaie).
- Termes pour Galien (non relevés par Lyncée) : FAST, eFAST, tamponnade, volet thoracique, carboxyhémoglobine, choc neurogène, syndrome centromédullaire, syndrome de Brown-Séquard, syndrome de Claude Bernard-Horner, queue de cheval, faux anévrisme, fistule artérioveineuse, intervalle libre, engagement cérébral, pile bouton, tabatière anatomique.
- Constats hors bloc S8 : rubriques 0 à 2 et 7 à 11 de S8 gardent des phrases tronquées d’origine ; 2 champs de S9.13 (4 et 7) découpés lettre par lettre ; app_v2.html à 5,91 Mo pour un budget de 6 Mo.
