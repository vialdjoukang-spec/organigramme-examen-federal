# Audit médical de niveau 2 (Galien) · TIP champ 5 (PR #33, d253d06) et urgences CK lots 1 et 2 (PR #35, 49aef17 ; PR #38, c08236e) · fichiers data/ck/hyp.json, data/ck/syn.json, data/ck/glo.json

**Relecteur** : Galien, indépendant des auteurs (Asclépios, Podalire). **Date** : 17.10.2026, Europe/Zurich.

## TIP champ 5 (PR #33)
Relu : les 15 champs écrits (tools/asclepios/tip_nouveaux.py) et les 113 blocs « Autres éléments ciblés » (tip_autres_a, b et c).
Verdict : à corriger, puis accepté. 16 fautes (4 majeures, 12 mineures, aucune critique) sont corrigées par tools/galien/tip_corr01.py et inscrites dans qa/audit/fautes.jsonl.
Sources relues le 17.10.2026 : ERC 2025 First Aid (fig. 5) et ERC 2025 BLS (compressions de 5 à 6 cm, 100 à 120 par minute, respiration agonique : G14 accepté) ; Undén 2013 (recommandations 1.1 et 1.2) ; ESC 2025 myocardite et péricardite (§ 3.3.2) ; GLIM 2019 (tableau 3).
Note : le seuil de S100B s’écrit « 0,10 microgramme par litre » ; c’est un seuil biologique et non une dose, mais G1 l’aurait lu comme une dose.
À vérifier : technique des tests du fléchisseur profond et de la secousse palpébrale de la myasthénie ; seuils de la dynamique utérine ; les nombres tirés de la S3 Polytrauma (20 %, 11 %, 16,4 et 7,6, VPP > 66 %), qui n’ont pas été recontrôlés.
Termes encore à définir : environ 85 (journal/nerfs-ck.md, l. 132 et 180) ; S100B est créé.

## Urgences CK, lots 1 et 2 (20 hypothèses)
Relu : pour chaque hypothèse, les lignes d’examen, la confirmation, les moyens spécifiques et leurs limites (diff de data/ck/hyp.json). Verdict : accepté. Aucune faute n’a été trouvée sur l’indication, l’ordre des lignes ou les limites, d’après les sources déjà citées : ESC 2023 SCA, ESC 2019 EP, ESC 2024 aorte, ESC 2021 IC, SSC 2021, EAACI 2021, ESCMID 2016, DGN état de mal, JBDS 2023, ESE 2014 hyponatrémie, ESGE 2021, ERS/ATS 2017, guide européen du traumatisé grave 2023. Toutes les posologies restent « À vérifier ».
Glossaire : 27 entrées restent au statut « À vérifier » (marbrures, temps de recoloration, urticaire, angio-œdème, stridor, sibilants, dyspnée, tachycardie, bradycardie, tachypnée, fièvre, purpura, altération de la conscience, crise tonico-clonique, respiration de Kussmaul, angioscanner, cristalloïde, échelle de Glasgow, méta-analyse, tirage, expectoration purulente, crépitants, reflux hépato-jugulaire, œdèmes des membres inférieurs, bruit de galop, pli cutané persistant, natrémie). Leurs définitions relues sont justes, mais aucune source n’a été lue pour elles : elles restent non validées.
