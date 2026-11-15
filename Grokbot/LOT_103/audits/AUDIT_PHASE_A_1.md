# Audit médical 1 — LOT_103 Phase A (S7.9 Troubles de la sensibilité)

- Date : 15.11.2026. Auditeur neuf, lecture seule. Base : `4f3596ee1abc644643b405906eeba8e941ceb229`.
- Fichier : `Grokbot/LOT_103/LOT_103_Phase_A_V0.html`, 108 692 octets, SHA-256 `72a6f6c79eb6bb9912be108b3158f8a364c603b4b88211eb30f545a02c698413`.
- Liste : `LISTE_DX_CANONIQUE.md`, non gelée. Verdict de liste : **CORRIGER**. Question finale : **non**.
- **Verdict : NON CONFORME. Score : 71/100.** Critiques : 0. Graves : 6. Mineurs : 6.
- Grille Θ3 (2, 1 ou 0) : p1=1, p2=1, p3=2, p4=1, p5=2, p6=2, p7=2, p8=1, p9=1, p10=2, p11=1, p12=2, p13=1, p14=1. Somme 20/28. La finale « non » n'entre pas dans ce dénominateur.

## Portes relancées

`controle3.py --script-ok` : VERT, 402 phrases hors cellules, connecteur 31 %, paragraphes sans connecteur 0, aucun défaut. `verif_aips.py` : OK, 0 AIPS citée. `aips_fiche.py verifier` : 0 défaut bloquant. `abreviations.py` : 0 sigle non développé. Les 551 phrases d'au moins 4 mots des blocs tiennent dans 12 à 28 mots. « car » : 0 occurrence. « parce que » : 28, chacune relie une raison à un geste.

## Ce qui a été relu et qui tient

Définitions IASP (hypoesthésie, hyperesthésie, paresthésie, dysesthésie, hyperalgésie, hypoalgésie) conformes à la page Terminology consultée le 15.11.2026. MonAM 2022 : 6,2 % (5,8 à 6,6), n = 21 906, femmes 5,6 %, hommes 6,9 %, 2017 : 4,8 %, 75 ans et plus : 15,4 %. OFS, asset 34027818 : 22 517 attaques en 2023 (12 132 hommes, 10 385 femmes) et 2 580 décès. Obsan 2019-2023 : incidence standardisée 249,4 (247,9 à 251,0), taux brut 249,5, moyenne 21 729, létalité 12,2 % (12,0 à 12,4), 2 651 décès. Atroshi, JAMA 1999 : 14,4 % (13,0 à 15,8), clinique 3,8 % (3,1 à 4,6), électrique symptomatique 4,9 % (4,1 à 5,8), clinique et électrique 2,7 % (2,1 à 3,4), témoins 18,4 % (12,0 à 26,3) sur 125, 2 466/3 000, région de 170 000, enquête 1997. Société suisse SEP, 27.01.2024 : 18 000 (17 400 à 18 700) en 2021, 2,7 femmes pour 1 homme, 15 000 en 2016, hausse d'environ 20 %, un cinquième lié à la population. Guillain-Barré, Eur J Neurol 2024 : 1,78, 1,71, 1,41, 1,66, moyenne 1,67, ventilation 11 %, hommes 63,9 %, âge 53,2 ans, incidences 2,18 et 1,18, pic 3,26 entre 70 et 79 ans. EAN : 1,65 à 1,88 pour 100 000 au Royaume-Uni, 2016-2019. Vignette RMS sujet âgé : 77 ans, 3 chutes, Hb 108 g/L, VGM 101 fL, réticulocytes 35 G/L, cobalamine 100 pmol/L, HbA1c 8 %, DFG 49 mL/min. Normes du diapason 6,9/5,5 et 6,2/4,7, seuil d'alcool > 30 g/jour, 53 %, 60 % puis 30 % sous chimiothérapie, 90 % et 70 % d'insuffisance terminale, cohorte 2 290 et 42 %, compression 30 s à 87 % et 90 % : présents dans les extraits RMS 2019 ou le cours de Liège. Aucun milligramme. Image : fichier Wikimedia `1313_Spinal_Cord_Cross_Section.jpg`, CC BY 4.0, OpenStax 18.05.2016 ; lame Michigan © 2012, grossissement 40, comme la légende OpenStax. Pas de SVG, pas d'image générée.

## Liste DX — arbitrage

Les dix noms sont des maladies, pas des symptômes. L'attaque, le Guillain-Barré, la myélopathie cervicale et la vasculite sont nommés. La compression médullaire d'un autre étage et le syndrome de la queue de cheval ne le sont pas. L'ordre mélange une part des polyneuropathies, une prévalence de population et une incidence annuelle : le brouillon le dit, et ce mélange empêche le gel.

Rang de fréquence proposé, sans pourcentage inventé : le canal carpien reste le seul motif dont la prévalence de population est mesurée (3,8 %). La neuropathie diabétique reste la cause la plus commune des polyneuropathies (30 à 40 % des cas, RMS 2019), sans prévalence de population lue au-dessus de 3,8 %. Le gel exige que la leçon choisisse un seul dénominateur et l'écrive dans la phrase de rang. Les rangs 3 à 10 peuvent rester dans l'ordre actuel si la phrase de chaque rang sans prévalence dit qu'elle suit l'ordre étiologique RMS, pas une cohorte. Rangs E proposés selon la létalité et le délai lus : E1 infarctus ou accident ischémique transitoire sensitif ; E2 syndrome de Guillain-Barré ; E3 compression médullaire, étage compris, dont la myélopathie cervicale symptomatique ; E4 mononévrite multiple des vasculites, tant que sa létalité n'est pas lue.

## Défauts

### Critique

Aucun. Aucune dose en milligrammes, aucune voie contraire à une fiche AIPS ouverte. Les phrases de dose disent « hors AIPS » et ne recopient pas les seuils 150 mg/j ni > 1 200 mg/j de la revue.

### Grave

1. **Point 1, notions voisines (L1-3).** « Un trouble de la sensibilité est présent lorsqu'un des phénomènes définis par cette taxonomie de 2011 est constaté. L'hypoesthésie est une sensibilité diminuée… » Le point enchaîne six termes voisins. L'IASP ne définit pas l'entité « trouble de la sensibilité ». Correction : une seule phrase, la définition du motif, société et année nommées ; les six termes passent au point 8, chacun une fois.

2. **Fausse identité 15 % = 23,1/1 000.** « L'incidence des cervicalgies est de 15 % par an, soit 23,1 cas pour 1 000 personnes-année. » 15 % valent 150 pour 1 000, pas 23,1. La RMS 2015 juxtapose les deux chiffres par un point-virgule (« est de 15 % par an ; elle s'élève à 23,1 ») et ne démontre pas l'égalité. Correction : retirer « soit » ; ne garder un chiffre que s'il est qualifié de la mesure exacte de la revue, sans conversion.

3. **83,2/100 000 n'est pas une prévalence de cervicobrachialgie.** « Les cervicobrachialgies ont une prévalence de 83,2 pour 100 000, et les hommes sont touchés dans un rapport de 1,6 pour 1. » La RMS 2015 écrit déjà « prévalence ». Le chiffre 83,2 est l'incidence annuelle ajustée de la radiculopathie cervicale à Rochester, Minnesota, 1976-1990 (Radhakrishnan, Brain 1994), source américaine. Correction : retirer la phrase. Ne pas la remplacer par ce chiffre.

4. **Nombres absents de la page citée.** « En 2022 le décompte était de 21 797 attaques, dont 11 821 chez les hommes et 9 976 chez les femmes. » et « Les décès par attaque cérébrale étaient de 2 535 en 2022. » L'asset OFS 34027818, ouvert, donne 2023 (22 517 et 2 580) et ne contient pas ces quatre nombres. « Le registre situait en 2016 entre 14 650 et 15 700 personnes, soit 174 à 187 pour 100 000. » La page de la Société du 27.01.2024 dit 15 000 en 2016 et ne donne ni la fourchette ni le taux. Ces taux sont ceux de Kaufmann et coll., Frontiers in Neurology 2019. Correction : citer cette étude, ou retirer les nombres. Garder 18 000, 17 400 à 18 700, 2,7 pour 1 et la hausse d'environ 20 %, qui sont sur la page.

5. **Compression médullaire réduite au rachis cervical.** « L'imagerie du rachis cervical passe devant l'électricité lorsqu'un niveau ou un signe pyramidal est présent. » Un niveau tronculaire ou un trouble sphinctérien peut siéger sous le cou. La leçon ne nomme ni la compression métastatique, ni l'abcès, ni l'hématome, ni la queue de cheval. Le drapeau « imagerie de la moelle le jour même » est juste, puis le point 9 le rétrécit. Correction : « On image la moelle à l'étage du niveau, le jour même, et le rachis cervical ne suffit pas si le niveau est thoracique ou si le périnée est pris. » Ajouter la compression médullaire et la queue de cheval au rang E3, à la place du seul intitulé « myélopathie cervicale compressive ».

6. **E2 avant le Guillain-Barré, malgré la létalité écrite dans la leçon.** « La myélopathie cervicale compressive est le rang E2, parce qu'une forme symptomatique indique déjà la chirurgie. » Plus loin : « Un syndrome de Guillain-Barré ou une attaque cérébrale peuvent les emporter dans les heures ou les jours. » La ventilation espagnole est de 11 %. La RMS 2015 indique la chirurgie de la myélopathie symptomatique ; elle n'en fait pas une maladie qui tue dans les heures. Correction : E1 attaque, E2 Guillain-Barré, E3 compression médullaire, E4 vasculite. La myélopathie cervicale garde son rang de fréquence et la mention chirurgicale, sans passer devant la ventilation.

### Mineur

1. **Rang 1 non démontré pour le motif.** Le diabète explique 30 à 40 % des polyneuropathies. Le canal carpien clinique atteint 3,8 % des adultes suédois de 25 à 74 ans. Aucune prévalence suisse de la neuropathie diabétique n'est lue au-dessus de ce taux. Correction : la phrase de rang dit le dénominateur (part des polyneuropathies, ou prévalence du motif).

2. **Seuil chirurgical incomplet.** La RMS 2015 écrit aussi : « La myélopathie cervicale symptomatique, corrélée au rétrécissement canalaire radiologique, pose l'indication chirurgicale lorsqu'elle est avancée. » La leçon ne garde que « per se ». Correction : ajouter « lorsqu'elle est avancée et concordante avec le rétrécissement ».

3. **Deux conversions collées.** « Le même décompte retient 73 % de femmes et 27 % d'hommes » : la page donne 2,7 pour 1, pas ces pourcentages. « Chez les hommes le taux est passé de 5,1 à 6,9 %, et après 75 ans 15,4 % déclaraient un diabète » : 15,4 % est le total des 75 ans et plus (MonAM 2022), pas le taux masculin (19,9 %). Correction : garder 2,7 pour 1 ; écrire « chez les 75 ans et plus, 15,4 % ».

4. **Image et point 13.** « Aucune flèche ne figure sur le fichier, et l'original d'OpenStax reste intact, sans œuvre dérivée. » Le fichier porte des traits de rappel et des légendes anglaises (cornes, colonnes, canal central). Le point 13 compte sept phrases ; le contrat en demande trois à six. Correction : « Le fichier OpenStax est déjà légendé en anglais ; cette leçon n'ajoute pas de repère. » Retirer une des sept phrases, de préférence la reprise du 3,8 %.

5. **Répétitions, sans cheville « car ».** 11 %, 12,2 %, 53 % et 85 % reviennent dans les points 2, 4, 5, 10, 11, 13 et 14, en phrases neuves de 12 à 28 mots. Ce n'est pas le « car » mécanique des versions refusées, ni le style télégraphique. Le connecteur mesuré est à 31 %, sous la cible de 35 % du prompt, et le script reste VERT. Correction : garder le chiffre au point 2 et au seul geste qui l'utilise ; ne pas ajouter de connecteur décoratif pour franchir 35 %.

6. **Méta-commentaire, score sans cotation, tableau incomplet.** « Ce cours, lu seul avec ses fenêtres, permet-il de reconnaître le motif… Oui pour cette phase, sous réserve de l'audit. » L'échelle de douleur neuropathique est citée et sa cotation est refusée dans la leçon. Le tableau du point 7 ne reprend que quatre des huit syndromes. Correction : remplacer la question méta par un piège de conduite ; ouvrir la cotation DN4 depuis la source qui la publie, ou ne pas nommer l'échelle ; compléter le tableau avec l'ischémie, la mononévrite, la sclérose combinée et la racine cervicale.

## Sources ouvertes pour cet audit

IASP Terminology ; MonAM diabète ; Obsan attaque cérébrale ; OFS asset 34027818 ; Société suisse de la SEP, 27.01.2024 ; Atroshi, JAMA 1999 ; Eur J Neurol 2024 (Guillain-Barré, Espagne) ; fiche EAN 2016-2019 ; Wikimedia, fichier OpenStax ; extraits locaux RMS 2015, RMS 2019 médecine interne, RMS 2019 sujet âgé, cours de Liège, relus puis confrontés aux pages ci-dessus. Radhakrishnan, Brain 1994, et Kaufmann, Frontiers in Neurology 2019, ouverts parce que les pages citées ne portaient pas le chiffre.
