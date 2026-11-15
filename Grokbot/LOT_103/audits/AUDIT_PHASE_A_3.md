# Audit médical 3 — LOT_103 Phase A (S7.9 Troubles de la sensibilité)

- Date : 15.11.2026. Auditeur neuf, lecture seule. Base : `5f41e6a215f2784669339e62d84a9874be6b4391`.
- Fichier : `Grokbot/LOT_103/LOT_103_Phase_A_V0.html`, 105 394 octets, SHA-256 `17e78f3db20d2ed2fc1904e1165f4aa8f8cdbec9881619597bd69ffb87bdcfca`.
- Liste non gelée. Question finale : **non**. Gel : **non**.
- **Verdict : NON CONFORME. Score : 68/100.** Critiques : 0. Graves : 5. Mineurs : 4.
- Grille Θ3 (2, 1 ou 0) : p1=1, p2=2, p3=2, p4=1, p5=2, p6=2, p7=1, p8=2, p9=1, p10=1, p11=1, p12=2, p13=2, p14=1. Somme 19/28. La finale « non » n'entre pas dans ce dénominateur.

## Portes

`controle3.py --script-ok` : VERT, 391 phrases, connecteur 32 %, paragraphes sans connecteur 0, aucun défaut. `verif_aips.py` : OK, 0 AIPS citée. `aips_fiche.py verifier` : 0 défaut bloquant. `abreviations.py` : 0 sigle non développé. Les 375 phrases de `div.p` tiennent dans 12 à 28 mots. « car » : 0. « parce que » relie une raison à un geste. Ce n'est ni le « car » plaqué des versions refusées, ni le style télégraphique. Le connecteur reste sous la cible de 35 % : ne pas ajouter de cheville pour la franchir.

## Ce que l'audit 2 avait demandé

1. **Corrigé.** La phrase ne prétend plus que les rangs 3 à 10 suivent l'ordre étiologique de la revue de 2019. Le nouvel ordre est jugé aux graves 2 et 3.
2. **Corrigé pour la fausse attribution, trou maintenu.** Les phrases « on lève la compression » ont disparu. Le cours s'arrête à l'attelle et aux infiltrations. Grave 4.
3. **Corrigé.** Déficit moteur brusque ou progressif, douleur résistante six à huit mois, antalgie ou corticoïde en premier choix, myélo-scanner si l'IRM est impossible : les trois phrases sont dans le cours.
4. Mineurs 1, 3 et 4 de l'audit 2 : **corrigés** (point 13 « avancée et concordante », E4 provisoire faute de létalité lue, rapport 1,6 pour 1 retiré).
5. Mineur 2 : les dates 1865 et 1913 et la phrase des milligrammes au point 13 sont retirées. Des chevilles AIPS restent (mineur 2).
6. Mineur 5 : la phrase demandée est en place, et elle laisse une formule de lacune dans le cours (mineur 2).

## Chiffres ouverts et conformes

IASP Terminology, 15.11.2026 : hypoesthésie, hyperesthésie, paresthésie, dysesthésie, hyperalgésie et hypoalgésie, au point 8, conformes. MonAM diabète 2022 : 6,2 % (5,8 à 6,6), n = 21 906, femmes 5,6 %, hommes 6,9 %, 2017 : 4,8 %, 75 ans et plus tous sexes : 15,4 %. OFS, asset 34027818 : 22 517 attaques en 2023 (12 132 hommes, 10 385 femmes) et 2 580 décès. Obsan 2019-2023, I60-I64 : 249,4 (247,9 à 251,0), brut 249,5, moyenne 21 729, létalité 12,2 % (12,0 à 12,4), 2 651 décès. Atroshi, JAMA 1999 : 14,4 % (13,0 à 15,8), clinique 3,8 % (3,1 à 4,6), électrique symptomatique 4,9 % (4,1 à 5,8), clinique et électrique 2,7 % (2,1 à 3,4), 18,4 % (12,0 à 26,3) sur 125 témoins, 2 466/3 000, 83 %, région de 170 000. Société suisse SEP, 27.01.2024 : 18 000 (17 400 à 18 700), 2,7 pour 1, 15 000 en 2016, hausse d'environ 20 %, un cinquième lié à la population. Eur J Neurol 2024 : 1,78, 1,71, 1,41, 1,66, moyenne 1,67, ventilation 11 %, hommes 63,9 %, âge 53,2 ans, 2,18 et 1,18, pic 3,26 entre 70 et 79 ans. Keddie, Brain : 1,65 à 1,88 pour 100 000, Royaume-Uni, 2016-2019. Spijker-Huiges 2015 : incidence 9,4 et prévalence 17,2 pour 1 000 personnes-année, et 53 diagnostics initiaux de radiculopathie sur 103 dossiers. Vignette, diapason, alcool > 30 g/jour, 53 %, chimiothérapie 60 % puis 30 %, 90 % et 70 %, cohorte 2 290 et 42 %, compression 30 s à 87 % et 90 % : conformes aux extraits RMS ou au cours de Liège. Image Wikimedia `1313_Spinal_Cord_Cross_Section.jpg`, CC BY 4.0, OpenStax 18.05.2016, lame du Michigan 2012 au grossissement 40. Pas de SVG, pas d'image générée. Aucun milligramme. Les seuils 150 mg/j et > 1 200 mg/j de la revue ne sont pas recopiés.

## Critique

Aucun. Aucune dose, aucune voie et aucune contre-indication contraire à une fiche AIPS. Le corpus AIPS n'est pas cité, et le cours ne donne pas de milligramme.

## Grave

1. **Point 1 : définition que l'IASP ne publie pas.** « En 2011, l'International Association for the Study of Pain range dans ce motif une sensation anormale ou une sensibilité au stimulus modifiée, hors les sens spéciaux. » La page Terminology définit la paresthésie comme une sensation anormale, spontanée ou provoquée, et réserve « excluding the special senses » à l'hypoesthésie et à l'hyperesthésie. Elle ne définit pas l'entité « trouble de la sensibilité ». Correction : « En 2011, l'IASP définit la paresthésie comme une sensation anormale, et l'hypoesthésie comme une sensibilité diminuée hors les sens spéciaux. »

2. **La SEP sort du raisonnement, pas seulement du mauvais classement.** « La sclérose en plaques ne figure pas devant l'attaque par un simple stock de personnes, faute de cohorte commune. » Refuser de placer 18 000 personnes devant 22 517 cas annuels est juste. Le cours n'enseigne ensuite ni le sujet jeune, ni le trouble migrateur, ni le niveau sans compression. Pour l'examen fédéral, ce motif sensitif central disparaît. Les huit syndromes du point 7 ne la nomment pas. Correction : « Chez l'adulte jeune, un trouble sensitif migrateur ou un niveau sans compression fait chercher la sclérose en plaques, sans la classer par un stock. » La remettre dans les dix, sans rang de fréquence inventé.

3. **Les rangs 3 à 10 ne sont pas un ordre de fréquence, et le cours le dit.** « La radiculopathie lombaire entre au rang 3, parce que la lombalgie irradiée est fréquente en médecine générale néerlandaise. » Puis : « Ces deux taux ne sont pas ceux de la radiculopathie, et le code néerlandais mélange les douleurs irradiées. » Spijker-Huiges mesure 9,4 et 17,2 pour 1 000 personnes-année de lombalgie irradiée, dont 53 dossiers sur 103 appelés radiculopathie. Ce taux ne se compare pas aux 3,3 pour 1 000 de la radiculopathie cervicale vraie (RMS 2015), qui a perdu sa place alors que le point 7 enseigne encore la racine cervicale. La neuropathie des chimiothérapies (60 % des patients traités) passe devant l'attaque, sans dénominateur commun. Correction : ne pas geler. Ne pas appeler rang 3 une maladie dont la source dit qu'elle ne mesure pas le taux. Aligner le point 7 sur la liste retenue.

4. **Trou de prise en charge du rang 1.** « Ces infiltrations sont espacées de 3 à 6 mois, et le cours ne fixe pas le seuil opératoire. » Le point 13 s'arrête à : « Pour le canal carpien, le cours de Liège retient d'abord l'attelle de nuit, avant l'infiltration. » Retirer la libération faussement attribuée à Liège était juste : l'extrait s'arrête à l'attelle de trois mois, à une ou deux infiltrations, puis à la date de 1933. L'amyotrophie thénarienne reste décrite comme forme sévère, sans geste. L'indication est seulement dans HELP.md. Le cours, lu seul, ne dit pas quand adresser le rang 1. Correction : écrire l'indication depuis une source suisse lue. Tant qu'elle manque, la phase ne suffit pas à traiter la forme sévère.

5. **Le Guillain-Barré E2 n'a pas de traitement de fond.** « On hospitalise le patient, parce que l'assistance ventilatoire concerne une part de la série espagnole. » L'hôpital et la ventilation sont justes, et ils ne traitent pas la maladie. La série britannique déjà citée (Keddie, Brain) dit que les cas hospitalisés reçoivent des immunoglobulines et que les échanges plasmatiques sont rares. Le cours ne nomme ni les unes ni les autres. Correction : « Au Royaume-Uni, les formes hospitalisées reçoivent des immunoglobulines, tandis que les échanges plasmatiques restent rares. » Aucun milligramme.

## Mineur

1. **« Des deux côtés » ne veut pas dire les deux méthodes.** « L'intervalle de cette mesure électrique allait de 4,1 à 5,8 %, au-dessus de la forme confirmée des deux côtés. » Atroshi décrit 4,9 % (4,1 à 5,8) de neuropathie électrique symptomatique, et 2,7 % confirmés par la clinique et l'électricité, pas une forme bilatérale. La phrase suivante le dit juste. Correction : « L'intervalle de la neuropathie électrique symptomatique allait de 4,1 à 5,8 %, au-dessus du 2,7 % confirmé par les deux méthodes. »

2. **Formule de lacune et chevilles sur la leçon.** « La hernie discale est la compression lue dans la revue, et les autres causes de cet étage restent à vérifier. » HELP.md porte déjà la lacune. « Cette leçon ne contient aucun milligramme, et la dose exacte se lit sur l'information professionnelle en vigueur. » Les questions sur la prégabaline et la gabapentine demandent de ne pas recopier une dose absente de la leçon, non un piège clinique. Correction : « La hernie discale est la compression que la revue de 2015 décrit à l'étage cervical. » Remplacer les deux questions de dose par un piège de conduite déjà sourcé, par exemple l'arrêt d'un symptomatique qui provoque une chute chez la personne âgée.

3. **L'image explique la moelle, elle ne sépare pas E1 de E2.** La licence CC BY 4.0 est réelle, le fichier n'est ni généré ni un SVG, et le cours dit que la coupe ne montre pas le cerveau. HELP.md ne motive pas l'absence d'un cliché qui séparerait l'ischémie cérébrale du Guillain-Barré. Correction : une phrase dans HELP.md, pas un dessin nouveau.

4. **La série britannique est citée pour l'infection antécédente.** « On demande une infection récente, puisque ce syndrome suit souvent un épisode infectieux dans les séries européennes. » L'article démontre surtout l'absence de lien avec la covid, et il cite Campylobacter parmi les pathogènes dont le confinement a réduit la transmission. Correction : « On demande une infection récente, parce que le confinement a réduit des pathogènes qui précèdent le syndrome, comme Campylobacter. »

## Sources ouvertes

IASP Terminology. MonAM, diabète, 15 ans et plus, enquête 2022. Obsan, attaques cérébrales, moyenne 2019-2023. OFS, asset 34027818. Société suisse de la SEP, 27.01.2024. Atroshi et coll., JAMA 1999. Blanco-Ruiz et coll., European Journal of Neurology, 2024, doi 10.1111/ene.16439. Keddie et coll., Brain, incidence britannique 2016-2019. Spijker-Huiges et coll., Scandinavian Journal of Primary Health Care, 2015, doi 10.3109/02813432.2015.1006462. Wikimedia, fichier OpenStax CC BY 4.0. Extraits locaux relus : RMS 25.11.2015, RMS 20.11.2019, RMS 2019 sujet âgé, cours de Liège.

Prompt L1 lu et appliqué.
