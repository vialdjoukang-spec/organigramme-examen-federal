# Audit médical 4 — LOT_103 Phase A (S7.9 Troubles de la sensibilité)

- Date : 15.11.2026. Contre-auditeur neuf, lecture seule. Base : `5d72ec4c6c73961c55891d41bff536b7185f349d`.
- Fichier : `Grokbot/LOT_103/LOT_103_Phase_A_V0.html`, 106 599 octets, SHA-256 `d3bc6698d9b0d38900ffe17779a90074e6e514dad6dfa93293ea1e4298448452`.
- Liste : `LISTE_DX_CANONIQUE.md`, non gelée. Question finale : **non**. Gel : **non**.
- **Verdict : NON CONFORME. Score : 82/100.** Critiques : 0. Graves : 3. Mineurs : 5.
- Grille Θ3 (2, 1 ou 0) : p1=1, p2=2, p3=2, p4=1, p5=2, p6=2, p7=2, p8=2, p9=1, p10=1, p11=1, p12=2, p13=2, p14=2. Somme 23/28.

## Portes

`controle3.py --script-ok` : VERT, 106 599 octets, 391 phrases, connecteur 32 %, paragraphes sans connecteur 0, aucun défaut. `verif_aips.py` : OK, 0 AIPS citée. `aips_fiche.py verifier` : 0 défaut bloquant. `abreviations.py` : 0 sigle non développé. Les phrases des `div.p` tiennent dans 12 à 28 mots. « car » : 0. Ce n'est ni le « car » plaqué des versions refusées, ni le style télégraphique. Ne pas ajouter de connecteur pour franchir 35 %.

## Liste

Les dix noms sont des maladies. L'attaque (E1), le Guillain-Barré (E2, ventilation 11 %), la compression avec la myélopathie (E3) et la mononévrite des vasculites (E4, provisoire, létalité non lue) sont nommés. Le rang 1 (canal carpien, 3,8 %) et le rang 2 (30 à 40 % des polyneuropathies, pas une prévalence) disent leur dénominateur. Le rang 3 (radiculopathie cervicale vraie, 3,3/1 000) ne reprend plus le code néerlandais. Les rangs 4 à 6 et 8 à 10 restent numérotés sans cohorte : le texte le dit, donc le gel reste fermé, sans chiffre inventé. La lombalgie irradiée (9,4 et 17,2/1 000) et la neuropathie des chimiothérapies ne sont pas numérotées.

## Ce qui a été ouvert et qui tient

IASP Terminology, liste 2011 : paresthésie = sensation anormale, spontanée ou provoquée, et note « non désagréable » ; hypoesthésie, hyperesthésie, dysesthésie, hyperalgésie (même mode) et hypoalgésie conformes au point 8. MonAM 2022 : 6,2 % (5,8 à 6,6), n = 21 906, femmes 5,6 %, hommes 6,9 %, 2017 : 4,8 %, femmes 4,5 à 5,6 %, hommes 5,1 à 6,9 %, 75 ans et plus tous sexes : 15,4 % (femmes de cet âge : 11,7 %). OFS, asset 34027818 : 22 517 attaques en 2023, 12 132 hommes, 10 385 femmes, 2 580 décès. Obsan 2019-2023 : 249,4 (247,9 à 251,0), brut 249,5, moyenne 21 729, létalité 12,2 % (12,0 à 12,4), 2 651 décès. Atroshi, JAMA 1999 : 14,4 % (13,0 à 15,8), clinique 3,8 % (3,1 à 4,6), électrique symptomatique 4,9 % (4,1 à 5,8), clinique et électrique 2,7 % (2,1 à 3,4), 18,4 % (12,0 à 26,3) sur 125 témoins, région de 170 000, enquête 1997. Société suisse SEP, 27.01.2024 : 18 000 (17 400 à 18 700), 2,7 pour 1, 15 000 en 2016, hausse d'environ 20 %, un cinquième lié à la population. Du Pasquier, RMS 28.01.2015 : début 20-30 ans, deux poussées dans le temps et le territoire, syndrome clinique isolé, IRM dès la première manifestation, immunomodulateurs plus efficaces tôt et ralentissement du handicap. Eur J Neurol 2024 : 1,78, 1,71, 1,41, 1,66, moyenne 1,67, ventilation mécanique 11 %, hommes 63,9 %, âge 53,2 ans, 2,18 et 1,18, pic 3,26 entre 70 et 79 ans. Keddie, Brain 2021 : incidence hospitalière 1,65 à 1,88/100 000 (2016-2019) ; immunoglobulines chez les formes hospitalisées, échanges rares. EAN/PNS 2023 (van Doorn) : immunoglobulines ou échanges si le patient ne marche plus sans aide ; compte jusqu'à 20 en une expiration vers les soins intensifs ; chute de la capacité vitale de plus de 30 % en 24 heures. mediX, révision août 2022 : chirurgie après échec du conservateur, ou lésion grave avec atrophie thénarienne ou déficit moteur ; amélioration souvent après l'accouchement. HAS, septembre 2012 : chirurgie d'emblée possible si signes de gravité, dont la perte axonale. RMS 2015, RMS 20.11.2019 et RMS sujet âgé : diapason 6,9/5,5 et 6,2/4,7, alcool > 30 g/jour et 3 verres / 2 verres, 53 %, chimiothérapie 60 % puis 30 %, urémie 90 %, dialyse ou transplantation, cohorte 2 290 et 42 % puis 70 %, DFG < 60 et < 15 mL/min, vignette (108 g/L, 101 fL, 35 G/L, 100 pmol/L, 8 %, 49 mL/min), 77 %, biopsie 17,5 %, prégabaline et gabapentine sans recopier 150 mg/j ni > 1 200 mg/j, C7 puis C6, plus de 90 % des espaces C5-C6 et C6-C7, plus de 90 % sans chirurgie, déficit brusque ou progressif, 6 à 8 mois, antalgie ou corticoïde, myélo-scanner, 85 %, cytokines et NGF. Cours de Liège : compression 30 s, 87 % et 90 %, déficit tactile absent chez 20 à 50 %, attelle 3 mois, une ou deux infiltrations. Image Wikimedia `1313_Spinal_Cord_Cross_Section.jpg` : CC BY 4.0, OpenStax 18.05.2016, corne latérale (thoracique), pas un SVG, pas une image générée. Aucun milligramme.

## Anciens défauts (audits 1 à 3)

Aucun grave ancien n'est revenu dans sa phrase. Corrigés et tenus : point 1 réduit à la paresthésie IASP exacte ; 15 % et 23,1/1 000 séparés ; 83,2/100 000, rapport 1,6, décomptes 2022 et fourchette SEP 2016 absents ; rangs E1 à E4 dans l'ordre de létalité lu ; « avancée et concordante » au point 13 ; 15,4 % pour les 75 ans et plus, tous sexes ; indication opératoire du canal carpien portée par mediX et la HAS, plus par Liège ; Guillain-Barré nommé avec immunoglobulines et échanges, sans dose ; SEP dans les dix, sans stock devant les 22 517 cas ; code néerlandais hors rang ; « des deux méthodes » ; Campylobacter et le confinement ; phrase HELP sur l'image. La v3 n'a pas été rallongée par un « car » ni par une formule de milligrammes.

## Critique

Aucun. Aucune dose, voie ou contre-indication. Les seuils 150 mg/j, > 1 200 mg/j, 0,4 g/kg sur 5 jours et 20 à 40 mg de méthylprednisolone restent hors du cours.

## Grave

1. **La létalité est le décompte des cas.** « Cette létalité mesure toutes les attaques de la période, et non la seule forme qui est sensitive. » La phrase précédente est le décompte OFS de 22 517 cas en 2023. La létalité Obsan est 12,2 %, et les décès de 2023 sont 2 580. Correction : « Ce décompte de 22 517 cas et la létalité de 12,2 % portent sur toutes les attaques, pas sur la seule forme sensitive. »

2. **La queue de cheval est citée dans un article de hernie cervicale.** « Si le périnée est pris, l'image doit voir la queue de cheval, et non seulement le rachis cervical. » Même attribution pour « y compris la queue de cheval » et pour « l'image doit voir l'étage du niveau, et la queue de cheval si le périnée est pris ». Schaller, RMS 25.11.2015, décrit la hernie cervicale, la myélopathie cervicale et des troubles de la miction de cette myélopathie. Il ne décrit ni la queue de cheval ni un niveau thoracique. Correction : « Un trouble de la miction avec un signe de moelle cervicale impose l'IRM cervicale, parce que la revue de 2015 le décrit dans la myélopathie. » Retirer la queue de cheval de toute phrase citée `rmshdc`. La nommer seulement avec une source qui la traite.

3. **Conduite de grossesse absente de la source, et elle peut retarder l'IRM.** « Chez la personne enceinte, on évite d'abord l'irradiation et l'on s'appuie sur l'examen clinique répété. » La mise au point du 20.11.2019 ne parle pas de grossesse. L'IRM n'irradie pas. Un niveau ou un hémicorps aigu ne se règle pas par un examen répété. Correction : retirer la phrase. Garder, sous mediX, l'amélioration fréquente du canal carpien après l'accouchement.

## Mineur

1. **83 % n'est pas 2 466/3 000.** « L'enquête a obtenu 2 466 réponses sur 3 000 adultes, soit 83 %. » Atroshi : 2 466 réponses sur 2 960 personnes joignables, soit 83 % ; 40 des 3 000 étaient hors champ. Correction : « L'enquête a obtenu 2 466 réponses parmi 2 960 adultes joignables, soit 83 %, sur 3 000 tirés au sort. »

2. **La seconde poussée est un critère, pas un fait constant.** « Le premier épisode sensitif évoque une atteinte médullaire cervicale, et une autre poussée survient dans un autre territoire. » Du Pasquier décrit un exemple, puis le critère : deux poussées séparées dans le temps et le territoire. Correction : « Le premier épisode sensitif peut évoquer la moelle cervicale, et une seconde poussée dans un autre territoire permet le diagnostic clinique. »

3. **La HAS autorise, elle n'impose pas la seule perte axonale.** « La Haute Autorité de santé indique la chirurgie d'emblée devant une perte axonale à l'ENMG. » Le rapport de septembre 2012 dit que la chirurgie peut être proposée d'emblée si un signe de gravité est présent : déficit moteur, amyotrophie, ou signe électrique dont la perte axonale. Correction : « La HAS peut proposer la chirurgie d'emblée si l'ENMG montre une perte axonale, au même titre qu'un déficit moteur ou une amyotrophie. »

4. **La chute n'est pas l'effet indésirable écrit.** « On arrête un symptomatique qui provoque des chutes, une confusion ou une ataxie. » La revue du sujet âgé nomme vertiges, ataxie, troubles visuels et confusion sous prégabaline, et le passage à l'amitriptyline en cas d'intolérance. Les 3 chutes de la vignette précèdent le traitement. Correction : « On arrête un symptomatique qui provoque une ataxie, des vertiges ou une confusion, puis l'on peut passer à un tricyclique. »

5. **Reprises, sans cheville.** 87 % et 90 %, 18,4 %, 6 semaines à 3 mois et 22 517 reviennent dans des phrases neuves. Le connecteur mesuré est à 32 %. L'image thoracique ne sépare pas E1 et E2 : HELP.md le dit, et aucune fenêtre ne donne un lien de cas. Le nerf ulnaire n'est pas nommé, alors que la coupure de l'annulaire est enseignée. Correction : garder chaque chiffre au point 2 et au geste qui l'utilise. Nommer le nerf ulnaire là où le cinquième doigt est pris. Ne pas ajouter de « car ».

Prompt L1 lu et appliqué.
