# Audit médical 2 — LOT_103 Phase A (S7.9 Troubles de la sensibilité)

- Date : 15.11.2026. Contre-auditeur neuf, lecture seule. Base : `29e1421260c436f13e056c2f665a9a5ece9b851d`.
- Fichier : `Grokbot/LOT_103/LOT_103_Phase_A_V0.html`, 108 376 octets. Liste non gelée.
- **Verdict : NON CONFORME. Score : 75/100.** Critiques : 0. Graves : 3. Mineurs : 5.
- Question finale : **non**. Gel : **non**.
- Grille Θ3 (2, 1 ou 0) : p1=2, p2=1, p3=2, p4=1, p5=2, p6=2, p7=2, p8=2, p9=1, p10=1, p11=1, p12=1, p13=1, p14=2. Somme 21/28.

## Portes

`controle3.py --script-ok` : VERT, 390 phrases, connecteur 31 %, aucun défaut. `verif_aips.py` : OK, 0 AIPS. `aips_fiche.py verifier` : 0. `abreviations.py` : 0. « car » : 0. La v3 n'est ni télégraphique ni allongée par un « car » plaqué. Elle reste allongée par des reprises paraphrasées (mineur 2).

## Chiffres ouverts et conformes

IASP, page Terminology lue le 15.11.2026 : hypoesthésie, hyperesthésie (seuil abaissé ou réponse plus forte), paresthésie, dysesthésie, hyperalgésie (même mode), hypoalgésie. MonAM 2022 : 6,2 % (5,8 à 6,6), n = 21 906, femmes 5,6 %, hommes 6,9 %, 2017 : 4,8 %, 75 ans et plus tous sexes : 15,4 % (hommes de cet âge : 19,9 %, non utilisé). OFS, asset 34027818 : 22 517 attaques en 2023 (12 132 hommes, 10 385 femmes) et 2 580 décès. Obsan 2019-2023, population européenne 2010, codes I60-I64 : 249,4 (247,9 à 251,0), brut 249,5, moyenne 21 729, létalité 12,2 % (12,0 à 12,4), 2 651 décès. Atroshi, JAMA 1999 : 14,4 % (13,0 à 15,8), clinique 3,8 % (3,1 à 4,6), électrique symptomatique 4,9 % (4,1 à 5,8), clinique et électrique 2,7 % (2,1 à 3,4), 18,4 % (12,0 à 26,3) sur 125 témoins sans plainte, 2 466/3 000, région de 170 000, enquête 1997. Société suisse SEP, 27.01.2024 : 18 000 (17 400 à 18 700) en 2021, 2,7 pour 1, 15 000 en 2016, hausse d'environ 20 %, un cinquième lié à la population. Eur J Neurol 2024 : 1,78, 1,71, 1,41, 1,66, moyenne 1,67, ventilation 11 %, hommes 63,9 %, âge 53,2 ans, 2,18 et 1,18, pic 3,26 entre 70 et 79 ans. EAN : 1,65 à 1,88 pour 100 000, Royaume-Uni, 2016-2019. Vignette RMS sujet âgé, diapason 6,9/5,5 et 6,2/4,7, alcool > 30 g/jour, 53 %, chimiothérapie 60 % puis 30 %, 90 % et 70 %, cohorte 2 290 et 42 %, compression 30 s à 87 % et 90 % : conformes aux extraits lus. Image Wikimedia `1313_Spinal_Cord_Cross_Section.jpg`, CC BY 4.0, OpenStax 18.05.2016, lame Michigan © 2012 au grossissement 40 : description des couleurs exacte. Pas de SVG, pas d'image générée. Aucun milligramme.

## Les 12 défauts de l'audit 1

1. **Corrigé.** Le point 1 est une seule phrase. Les six termes IASP sont au point 8.
2. **Corrigé.** 15 % par an et 23,1 pour 1 000 sont séparés, sans « soit ».
3. **Partiel.** 83,2/100 000 est retiré. Le rapport 1,6 pour 1 reste (mineur 4).
4. **Corrigé.** Les décomptes 2022 et la fourchette SEP 2016 absente de la page sont retirés.
5. **Corrigé.** L'image suit l'étage, le thorax et le périnée. La queue de cheval est dans E3. La phrase des quatre causes n'a pas de source (mineur 5).
6. **Corrigé.** E1 attaque, E2 Guillain-Barré, E3 compression, E4 vasculite.
7. **Corrigé.** Le rang 1 dit « seule prévalence de population lue ». Le rang 2 dit « part des polyneuropathies ».
8. **Partiel.** « Avancée et concordante » est aux points 5 et 14. Le point 13 garde « forme symptomatique » (mineur 1).
9. **Corrigé.** 2,7 pour 1 est gardé. 15,4 % vise les 75 ans et plus, tous sexes.
10. **Corrigé.** La légende anglaise est dite telle quelle. Le point 13 a six phrases.
11. **Partiel.** 12,2 % une fois ; 11 %, 53 % et 85 % au chiffre et au geste. D'autres reprises restent (mineur 2).
12. **Corrigé.** La question méta est retirée, DN4 n'est pas nommé, le tableau du point 7 a les huit syndromes. Une cheville sur les milligrammes occupe le point 13 (mineur 2).

## Critique

Aucun. Aucune dose, voie ou contre-indication contraire à une fiche AIPS. Les seuils 150 mg/j et > 1 200 mg/j de la revue ne sont pas recopiés.

## Grave

1. **L'ordre des rangs 3 à 10 n'est pas celui que la phrase affirme.** « Les rangs suivants sans prévalence de population suivent l'ordre étiologique de la Revue médicale suisse, non une cohorte. » La mise au point du 20.11.2019 écrit, après le diabète : « Suivent les causes toxiques, immunitaires et infectieuses, ainsi que métaboliques et carentielles », et « dans environ 30 % des cas de neuropathie chronique, aucune étiologie spécifique n'est retrouvée ». Les causes fréquentes qu'elle nomme sont l'alcool, le diabète, la cobalamine, la chimiothérapie et les paraprotéinémies. La radiculopathie cervicale, la SEP, l'attaque et la compression n'appartiennent pas à cet ordre. La chimiothérapie, nommée fréquente, n'est pas un des dix diagnostics. La radiculopathie lombaire non plus : en médecine générale néerlandaise, la lombalgie irradiée a une prévalence de 17,2 pour 1 000 personnes-année et une incidence de 9,4, et la moitié d'un sous-échantillon de 103 épisodes était une radiculopathie (Spijker-Huiges et coll., Scandinavian Journal of Primary Health Care, 2015), au-dessus des 3,3 pour 1 000 de la radiculopathie cervicale vraie (RMS 2015). « La SEP, avec 18 000 personnes en 2021, précède l'attaque cérébrale dans ce classement de stock » place un stock de 18 000 avant 22 517 cas annuels. Correction : remplacer la phrase d'ordre par « Les rangs 3 à 10 n'ont pas de cohorte commune, et ils ne recopient pas l'ordre étiologique de la revue de 2019. » Faire entrer la radiculopathie lombaire et la neuropathie des chimiothérapies, et ne plus faire précéder l'attaque par la SEP sur ce stock. Retirer en échange la phrase du « classement de stock ».

2. **La libération du canal carpien est attribuée à un cours qui ne la formule pas, et le traitement que ce cours écrit est absent.** « On lève la compression lorsque le déficit moteur ou l'amyotrophie thénarienne s'installe. » Le tableau répète : « On lève la compression si le déficit s'installe, et ce diagnostic n'a pas de rang E. » Les deux renvoient au cours de Liège. L'extrait lu se termine par : aménagement du poste, « attelle à porter la nuit (3 mois) », « 1 à 2 infiltrations espacées de 3 à 6 mois », puis « chirurgie : première intervention en 1933 ». Il ne pose pas la libération au déficit moteur ni à l'amyotrophie. Correction : « Le cours de Liège retient l'attelle nocturne pendant trois mois et une ou deux infiltrations avant la chirurgie. » Retirer les deux phrases de libération. Toute indication opératoire précise reste « À vérifier » tant qu'une source suisse ne l'a pas portée.

3. **Le déficit moteur brusque et le traitement conservateur de la hernie cervicale manquent, alors que la revue les écrit.** « On opère si le déficit progresse, ou si la douleur résiste encore après 6 à 8 mois. » « Plus de 90 % des patients qui ont une radiculopathie par hernie guérissent sans chirurgie lorsque le déficit moteur ne progresse pas. » La RMS du 25.11.2015 recommande la chirurgie si le déficit moteur apparaît de manière brusque ou progresse, ou si la douleur résiste six à huit mois au traitement non chirurgical, et elle place en premier choix « une antalgie et un traitement anti-inflammatoire adapté ou des corticostéroïdes ». Le même article fait le myélo-scanner lorsqu'il y a une contre-indication à l'IRM ou que l'IRM est peu conclusive : la leçon ne le dit pas. Correction : « On opère si un déficit moteur apparaît brusquement ou progresse, ou si la douleur résiste six à huit mois. » « Le premier choix est une antalgie, un anti-inflammatoire ou un corticoïde, puisque plus de 90 % guérissent sans chirurgie. » « Le myélo-scanner remplace l'IRM lorsqu'elle est contre-indiquée ou peu conclusive. » Retirer en échange une des reprises du seul « 90 % ».

## Mineur

1. **Le point 13 élargit encore l'indication que l'audit 1 avait resserrée.** « Un niveau sensitif ou un signe pyramidal ouvre l'imagerie de la moelle, et la forme symptomatique indique la chirurgie. » Les points 5 et 14 disent « lorsqu'elle est avancée et concordante avec le rétrécissement ». Les deux lectures existent dans la RMS 2015 (introduction « per se » ; corps « lorsqu'elle est avancée »). Le point mémorisé doit garder la phrase complète. Correction : « Un niveau sensitif ou un signe pyramidal ouvre l'imagerie, et la chirurgie vise la forme avancée et concordante. »

2. **Des chevilles et des reprises paraphrasées allongent encore la leçon.** « Aucune dose en milligrammes ne figure dans cette leçon, et toute posologie se lit sur l'AIPS en vigueur » occupe un des six points clés, et la formule « hors AIPS » revient dans chaque ligne du tableau des molécules. « Le cours rappelle que la compression est le plus souvent idiopathique, connue cliniquement depuis 1865. » « La description anatomique date de 1913, et ces dates ne changent pas la conduite actuelle au lit. » Le tableau du point 2 redit 3,8 %, 18 000, 249,4 et 1,67 déjà posés au-dessus. Correction : garder chaque chiffre au point 2 et au seul geste qui l'utilise. Retirer les deux phrases de 1865 et de 1913. Au point 13, remplacer la phrase des milligrammes par un fait de conduite qui n'est pas déjà au point 4.

3. **Le rang E4 est justifié par la fréquence.** « La mononévrite multiple des vasculites est le rang d'exclusion E4, en dernier par la fréquence. » Le rang E mesure la létalité et le délai, et la liste dit que la létalité de cette vasculite n'est pas lue. Correction : « Le rang E4 reste provisoire, parce que la létalité de cette vasculite n'est pas lue dans la revue. »

4. **Le rapport 1,6 pour 1 a été gardé et réattribué.** « Les hommes sont plus touchés que les femmes dans la hernie discale cervicale, dans un rapport de 1,6 pour 1. » L'audit 1 demandait de retirer la phrase qui liait ce rapport au 83,2/100 000. Dans la RMS 2015, le rapport suit les phrases sur les cervicobrachialgies et porte la référence 6, distincte de la hernie. Correction : retirer la phrase.

5. **Quatre causes compressives sont nommées sans source.** « Une compression aiguë à l'étage du niveau peut être une hernie, une métastase, un abcès ou un hématome. » Aucun appel de bibliographie. La hernie est dans la RMS 2015. La métastase, l'abcès et l'hématome n'y sont pas lus. Correction : « La hernie discale est la compression lue dans la revue, et les autres causes de cet étage restent à vérifier. »

## Sources ouvertes pour cet audit

IASP Terminology, 15.11.2026. MonAM diabète, 15 ans et plus, enquête 2022. Obsan, attaque cérébrale, moyenne 2019-2023, y compris I60-I64. OFS, asset 34027818, Santé, chiffres 2023. Société suisse de la SEP, 27.01.2024. Atroshi et coll., JAMA 1999. Blanco-Ruiz et coll., European Journal of Neurology, 2024, doi 10.1111/ene.16439. Fiche EAN, incidence britannique 2016-2019. Wikimedia, fichier OpenStax CC BY 4.0. Spijker-Huiges et coll., Scandinavian Journal of Primary Health Care, 2015, doi 10.3109/02813432.2015.1006462. Extraits locaux relus : RMS 25.11.2015, RMS 20.11.2019, RMS 2019 sujet âgé, cours de Liège (orbi.uliege.be, consulté le 10.11.2026).

Prompt L1 lu et appliqué.
