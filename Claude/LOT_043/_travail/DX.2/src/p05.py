from lib import *
P = Pt(5)
P.p("L'anamnèse sert à deux tâches simultanées : écarter une urgence cardiovasculaire, puis reconnaître la panique de façon positive grâce à l'écoute d'une histoire précise [wd8c882-37]. "
    "Une anamnèse attentive, à la recherche d'un facteur anxiogène déclenchant, constitue un élément déterminant du diagnostic [wd8c882-37]. "
    "La connaissance du patient par le médecin de premier recours favorise le diagnostic, mais elle peut aussi induire en erreur si le clinicien néglige les signes non psychogènes [wd8c882-37]. "
    "Chaque question ci-dessous porte donc sa raison physiopathologique et sa conséquence sur la conduite.")
P.h("5.a Questions sur la douleur et sur l'attaque")
P.table(["Question", "Raison physiopathologique", "Ce que la réponse change"], [
 ["La douleur survient-elle à l'effort, et cède-t-elle au repos ?", "La douleur ischémique peut être déclenchée ou aggravée par l'effort [wd8c882-25]", "Une douleur d'effort impose une évaluation coronarienne avant de parler de panique [w31b8bf-20]"],
 ["Quelle est la qualité de la douleur : pression, brûlure, coup de poignard ?", "La probabilité d'infarctus varie avec la description de la douleur [wfba9d7-5]", "Aucune description n'exclut le syndrome coronarien à elle seule [wfba9d7-13]"],
 ["La douleur augmente-t-elle à la respiration ou à la mobilisation ?", "La douleur de paroi est mécanique, en relation avec la mobilisation de la paroi thoracique [wd8c882-20]", "Une douleur reproductible oriente vers la paroi thoracique [wd8c882-20]"],
 ["Quelle est la durée de l'épisode et son pic ?", "L'attaque de panique atteint son acmé en quelques minutes [we22718-33]", "Une durée de 15 à 30 minutes s'accorde avec une attaque de panique [w85c0ac-10]"],
 ["Existe-t-il un déclencheur évident ?", "L'attaque survient souvent sans déclencheur évident [we22718-31]", "L'absence de déclencheur oriente vers un trouble panique plutôt que vers une phobie [we22718-31]"],
 ["Le patient craint-il de mourir ou de perdre le contrôle ?", "Les cognitions catastrophiques entretiennent le cercle vicieux de la panique [wb1bfcb-36]", "La peur de mourir aide à différencier la panique des symptômes coronariens [wf778c1-38]"],
 ["Existe-t-il vertiges, frissons, bouffées de chaleur ?", "L'hyperventilation produit des vertiges et des picotements [w85c0ac-4]", "Ils n'apparaissent pas d'ordinaire avec les symptômes cardiaques [wf778c1-35]"]])
P.p("La première question porte sur l'effort, car l'ischémie myocardique est déclenchée ou aggravée par celui-ci, même si elle peut aussi survenir la nuit et sans lien avec l'effort [wd8c882-25]. "
    "La deuxième porte sur la qualité de la douleur, car la probabilité d'infarctus varie avec elle [wfba9d7-5]. Elle atteint 24 % pour une pression ou un serrement, 23 % pour une brûlure et 8 % pour une douleur pleurétique [wfba9d7-5]. "
    "Cette série date de 1993 et ne permet pas d'exclure l'infarctus, car la clinique du syndrome coronarien aigu est variable [wfba9d7-5][wfba9d7-13]. "
    "Une douleur pleurétique ou entièrement reproductible, sans antécédent d'angor ni d'infarctus, fait tomber la probabilité d'infarctus à 0 % dans cette combinaison [wfba9d7-5].",
    ("probabilité d'infarctus selon la description de la douleur", [
     "Dans une étude genevoise de 1993, la probabilité d'infarctus atteint 24 % pour une douleur décrite comme pression, serrement ou écrasement [wfba9d7-5].",
     "Elle est de 23 % pour une brûlure ou une indigestion, de 13 % pour une douleur sourde et de 5 % pour une douleur aiguë en coup de poignard [wfba9d7-5].",
     "Une douleur pleurétique et positionnelle correspond à 8 %, une douleur partiellement reproductible à 6 % et une douleur pleinement reproductible à 5 % [wfba9d7-5].",
     "La combinaison d'une douleur pleurétique ou reproductible, sans passé d'angor ni d'infarctus, est associée à une probabilité d'infarctus de 0 % [wfba9d7-5].",
     "Piège d'examen : ces probabilités concernent des patients suspects de syndrome coronarien aigu aux urgences, si bien qu'elles ne s'appliquent pas à tout patient anxieux [wfba9d7-3]."]))
P.h("5.b Contexte, comorbidités et médicaments")
P.table(["Question", "Raison physiopathologique", "Ce que la réponse change"], [
 ["Quels événements de vie ou stress récents ?", "Le stress lié aux événements de vie prédit l'apparition du trouble panique [w29cff0-4]", "Un facteur anxiogène déclenchant oriente le diagnostic [wd8c882-37]"],
 ["Quelle consommation de café, tabac, alcool, drogues ?", "Les patients paniques réagissent davantage à la caféine, à la nicotine et à l'alcool [wb1bfcb-16]", "L'éviction des toxiques fait partie de l'hygiène de vie [we22718-58]"],
 ["Quels médicaments, y compris psychostimulants et benzodiazépines ?", "Un sevrage ou un psychostimulant peut produire des symptômes anxieux [we22718-22]", "La dépendance aux benzodiazépines impose l'avis d'un spécialiste [we22718-23]"],
 ["Existe-t-il une dépression ou un autre trouble anxieux ?", "Une dépression s'associe dans 60 % des cas et un autre trouble anxieux dans 50 % [we22718-9]", "Les comorbidités se recherchent et se traitent [we22718-3]"],
 ["Le patient évite-t-il certaines situations ?", "L'évitement et les comportements de sécurité maintiennent le trouble [wb1bfcb-39]", "Un évitement suggère une agoraphobie associée [we22718-35]"],
 ["Quelle est l'histoire cardiovasculaire et quels sont les facteurs de risque ?", "Le trouble panique est associé à une coronaropathie incidente [w72a488-3]", "La recherche des facteurs de risque cardiovasculaire reste nécessaire [we22718-5]"],
 ["Le patient consulte-t-il de façon répétée avec des examens normaux ?", "La non-reconnaissance mène à des consultations répétées et à des coûts importants [wd8c882-36]", "Le trouble anxieux doit être envisagé lorsque les symptômes restent inexpliqués [we22718-19]"]])
P.p("Le médecin explore l'exposition aux substances, car la consommation de café, de tabac, d'alcool ou de drogues peut être l'expression d'un trouble anxieux [we22718-3]. "
    "Il vérifie aussi l'usage de cocaïne avant de prescrire un inhibiteur de la recapture de la sérotonine, à cause des interactions entre médicaments [wb6b3cd-37]. "
    "La demande de prescription de benzodiazépine, de zolpidem ou de zopiclone exige de rechercher l'indication initiale [we22718-23]. "
    "Une dépendance aux benzodiazépines impose l'avis d'un spécialiste [we22718-23].")
P.p("Une vignette clinique des HUG décrit un homme de 46 ans, fumeur de 30 unités paquet-année [w85c0ac-1]. Il consulte de façon répétée avec une oppression thoracique, une dyspnée et des palpitations, car ces symptômes persistent [w85c0ac-1]. "
    "L'examen physique est sans particularité, le bilan urgent avec ECG et troponine est négatif plusieurs fois, et la découverte d'un cancer du sein chez son épouse l'inquiète beaucoup [w85c0ac-1][w85c0ac-2]. "
    "La vignette pose alors la question d'un trouble anxieux et celle des propositions thérapeutiques [w85c0ac-2].",
    ("vignette de Monsieur D. aux HUG", [
     "Un patient de 46 ans, fumeur de 30 unités paquet-année, consulte depuis 6 semaines au cabinet et aux urgences avec une oppression thoracique, une dyspnée et des palpitations [w85c0ac-1].",
     "L'examen physique est chaque fois sans particularité, et le bilan en urgence avec ECG et troponine est plusieurs fois négatif [w85c0ac-1][w85c0ac-2].",
     "Le contexte comprend la découverte d'un cancer du sein chez son épouse, qui l'inquiète beaucoup [w85c0ac-2].",
     "Les questions posées sont : ce patient souffre-t-il d'un trouble anxieux, et quelles propositions thérapeutiques faire [w85c0ac-2] ?",
     "Piège d'examen : un tabagisme de 30 unités paquet-année reste un facteur de risque cardiovasculaire, si bien qu'un bilan cardiaque complet est justifié avant de conclure [w85c0ac-1]."]))
P.h("5.c Drapeaux rouges")
P.table(["Drapeau rouge", "Signification", "Action immédiate"], [
 ["Douleur rétrosternale, en barre, irradiant vers les bras ou la mâchoire, déclenchée par l'effort", "Douleur ischémique typique [wd8c882-25]", "ECG et filière du syndrome coronarien aigu [wbd75ff-11]"],
 ["Hypotension ou tachycardie", "Signal d'alarme d'une situation critique [wbd75ff-11]", "Bilan complet, ECG, biomarqueurs et imagerie [wbd75ff-11]"],
 ["Douleur brutale, intense ou déchirante, thoracique, dorsale ou abdominale", "Haut risque de syndrome aortique aigu [wc15f7c-13]", "Imagerie de l'aorte selon le score de risque [wc15f7c-13]"],
 ["Douleur constrictive irradiant dans le dos, augmentée à la respiration, avec essoufflement", "Diagnostics graves : péricardite, embolie, pneumothorax, dissection [wfba9d7-2]", "Prise en charge urgente [wfba9d7-1]"],
 ["Palpitations, syncope ou douleur thoracique", "Symptôme cardiaque nécessitant un ECG [we22718-25]", "ECG avec recherche d'un intervalle QT corrigé (QTc) allongé [we22718-25]"],
 ["Idées suicidaires ou antécédent de tentative", "Risque accru lors d'un traitement antidépresseur [aips-55391-21]", "Surveillance particulière [aips-55391-21]"],
 ["Sevrage d'alcool ou de benzodiazépines, usage de psychostimulants", "Cause iatrogène ou toxique d'anxiété [we22718-22]", "Rechercher la cause avant de poser le diagnostic [we22718-22]"],
 ["Paresthésies avec suspicion d'épilepsie", "Une épilepsie peut produire une paresthésie comme la panique [wf778c1-5]", "Avis neurologique selon le contexte [we22718-21]"]])
P.p("Aucune réponse réconfortante ne suffit à lever un drapeau rouge, car le trouble panique peut coexister avec une coronaropathie ou une autre maladie cardiaque [wf778c1-36]. "
    "Chez les patients coronariens, la panique associée augmente le risque d'événements cardiaques majeurs, le handicap et la détresse psychique [wf778c1-36]. "
    "Le médecin répète donc la réévaluation si les symptômes changent, car aucune règle ne garantit une exclusion définitive des causes cardiaques d'une douleur persistante [w1a9f59-13].")
P.save()
