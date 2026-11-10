from lib import *
P = Pt(4)
P.p("Toute douleur thoracique aiguë doit d'abord être évaluée pour une cause cardiaque, après l'anamnèse et l'examen clinique, au moyen d'un électrocardiogramme [wf778c1-37]. "
    "Les causes graves à écarter sont le syndrome coronarien aigu, le syndrome aortique aigu, l'embolie pulmonaire, la myopéricardite aiguë et la valvulopathie [wf778c1-37]. "
    "Les enseignants genevois ajoutent le pneumothorax sous tension et la péricardite à la liste des diagnostics menaçant le pronostic vital [wfba9d7-2]. "
    "Le diagnostic de panique ne s'obtient donc pas par exclusion pure, car l'anamnèse précise permet d'évoquer le diagnostic de façon positive [wd8c882-37].")
P.p("En pratique, le guide NICE demande de ne réaliser que les examens minimaux nécessaires pour exclure un problème physique aigu chez la personne qui présente une attaque de panique [wb6b3cd-40]. "
    "Les signaux d'alarme, comme l'hypotension et la tachycardie, orientent d'emblée vers une situation critique, tandis que le bilan comprend les antécédents, les signes vitaux, l'ECG, les biomarqueurs et l'imagerie [wbd75ff-11]. "
    "Un patient anxieux peut aussi avoir une maladie cardiaque, car les patients paniques présentent des taux élevés d'angor microvasculaire, d'hypertension et de cardiomyopathie [wf778c1-36].")
P.h("4.a Les diagnostics graves à écarter d'abord")
P.p("Le syndrome coronarien aigu est le premier diagnostic à écarter, car la douleur ischémique peut être atypique, nocturne, indépendante de l'effort et même silencieuse [wd8c882-25]. "
    "La localisation de la douleur ne permet pas de le distinguer des autres causes, car les douleurs de toutes les étiologies siègent surtout à gauche en avant du thorax [w587cc6-29]. "
    "Une règle de décision de médecine de premier recours repose sur cinq éléments, dont la douleur aggravée à l'effort et la douleur non reproductible à la palpation [w31b8bf-20]. "
    "Cette règle écarte une coronaropathie avec une sensibilité de 87,1 % pour un seuil de 3 points [w31b8bf-20]. "
    "L'un de ses éléments est la conviction du patient que la douleur est cardiaque, or les patients à douleur psychogène la supposent souvent [w31b8bf-20][w587cc6-36].",
    ("règle de prédiction de la coronaropathie en soins primaires", [
     "La règle contient cinq déterminants : âge et sexe, maladie vasculaire connue, patient persuadé que la douleur est cardiaque, douleur aggravée à l'effort et douleur non reproductible à la palpation [w31b8bf-20].",
     "Le score va de 0 à 5 points, et le seuil de 3 points donne une sensibilité de 87,1 % et une spécificité de 80,8 % [w31b8bf-20].",
     "La validation externe a utilisé des patients de 58 cabinets de Suisse occidentale, avec l'anxiété induite par la douleur comme variable de substitution [w31b8bf-33][w31b8bf-34].",
     "Avec un seuil de 3 points, environ un patient sur sept souffrant d'une douleur d'origine cardiaque serait manqué, d'où la nécessité d'une attente vigilante [w31b8bf-51].",
     "Piège d'examen : la conviction d'une origine cardiaque est fréquente dans la panique, si bien que cet élément du score peut perdre sa valeur discriminante [w587cc6-36][w31b8bf-34]."]))
P.p("Le syndrome aortique aigu est rare mais il met la vie en danger, et la mortalité augmente de 1 à 2 % par heure sans traitement [wc15f7c-5]. "
    "Un diagnostic de syndrome aortique manqué s'associe à des modifications ischémiques de l'ECG et à une suspicion initiale d'infarctus du myocarde [wc15f7c-4]. "
    "Les troponines et les D-dimères élevés ainsi que les anomalies de l'ECG peuvent égarer le clinicien vers un syndrome coronarien aigu ou une embolie pulmonaire au lieu du syndrome aortique [wc15f7c-7]. "
    "Les douleurs thoraciques, dorsales ou abdominales brutales, intenses ou déchirantes, ainsi que l'hypotension, constituent des éléments de haut risque [wc15f7c-13].")
P.p("Chez un patient aux douleurs constrictives irradiant dans le dos et augmentées à la respiration, il faut donc évoquer la péricardite, la myocardite, le pneumothorax sous tension et l'embolie pulmonaire [wfba9d7-2]. "
    "Dans une cohorte suisse de médecine de premier recours, l'embolie pulmonaire et les syndromes coronariens instables étaient rares, mais les affections graves ont représenté 20 % des cas [wfbafca-3][wfbafca-4]. "
    "La Société européenne de cardiologie a publié en 2019, avec la Société européenne de pneumologie, un guide sur l'embolie pulmonaire [wf4ca70-1].")
P.h("4.b Les diagnostics fréquents et discriminants")
P.p("Le syndrome de la paroi thoracique est la cause la plus fréquente, car il représente 24,5 à 49,8 % des douleurs thoraciques en soins primaires [w7a56a8-8]. Sa douleur est mécanique, liée à la mobilisation de la paroi ou de l'épaule, et reproductible à la palpation [wd8c882-20]. "
    "Le reflux gastro-œsophagien constitue la cause biologique la plus fréquente de douleur thoracique non cardiaque [wf778c1-34]. "
    "La tachycardie supraventriculaire paroxystique partage les symptômes de la panique et reste difficile à documenter par un ECG réalisé après l'attaque [wf778c1-35]. "
    "Le dosage de la thyréostimuline et de la glycémie, la créatinine et l'ECG permettent d'écarter les causes métaboliques et cardiaques traitables [we22718-24][wfba9d7-9].")
P.table(["Diagnostic", "Élément qui tranche", "Piège", "Conduite si positif"], [
 ["🚩 Syndrome coronarien aigu", "ECG et biomarqueurs [wbd75ff-11]", "Douleur atypique ou silencieuse ; siège identique à la panique [wd8c882-25][w587cc6-29]", "Prise en charge urgente [wfba9d7-1]"],
 ["🚩 Syndrome aortique aigu", "Douleur brutale ou déchirante, hypotension, déficit de perfusion [wc15f7c-13]", "Troponine et ECG égarent vers le syndrome coronarien [wc15f7c-7]", "Imagerie de l'aorte [wc15f7c-13]"],
 ["🚩 Embolie pulmonaire", "Évoquée devant des douleurs aggravées à la respiration [wfba9d7-2]", "Biomarqueurs élevés égarent vers une autre voie [wc15f7c-7]", "Filière diagnostique urgente [wfba9d7-1]"],
 ["Péricardite, myocardite", "Douleur augmentée à la respiration [wfba9d7-2]", "Myocardite : risque de mort subite chez le jeune [wfba9d7-2]", "Prise en charge urgente [wfba9d7-1]"],
 ["Syndrome de la paroi thoracique", "Douleur reproductible à la palpation [wd8c882-20]", "Siège gauche, identique à celui de la coronaropathie [w587cc6-29]", "Réassurance appuyée sur la palpation [wd8c882-20]"],
 ["Reflux gastro-œsophagien", "Brûlure, régurgitation, dysphagie [wf778c1-34]", "Reflux et panique coexistent [wf778c1-34]", "Essai d'un inhibiteur de la pompe à protons [w1a9f59-37]"],
 ["Tachycardie supraventriculaire paroxystique", "Monitorage ambulatoire [wf778c1-35]", "ECG normal après l'attaque [wf778c1-35]", "Distinguer de la panique par un monitorage prolongé [wf778c1-35]"],
 ["Trouble panique", "Symptômes cognitifs et autonomes de la panique [wf778c1-35][wf778c1-38]", "Les signes habituels ne distinguent pas [wb34f75-5]", "Thérapie cognitivo-comportementale et inhibiteur de la recapture de la sérotonine [we22718-65]"]])
P.p("Le tableau clinique de la panique associe plusieurs symptômes qui n'apparaissent pas d'ordinaire avec les symptômes cardiaques, comme les vertiges, les frissons, les bouffées de chaleur et la peur de mourir [wf778c1-35]. "
    "Les patients cardiaques rapportent surtout des symptômes physiques et rarement des symptômes cognitifs [wf778c1-38]. Les patients paniques décrivent en revanche des pensées catastrophiques, comme la peur de mourir ou de perdre le contrôle [wf778c1-38]. "
    "Une douleur thoracique inexpliquée avec une plainte cognitive dominante ou une forte anxiété cardiaque peut donc orienter vers l'absence de maladie cardiaque [wf778c1-38]. "
    "Néanmoins, la routine du bilan thoracique ne permet pas de distinguer à elle seule les patients avec et sans trouble panique [wb34f75-5].",
    ("critères cognitifs qui orientent vers la panique", [
     "Fraenkel et coll. ont comparé les symptômes de patients paniques, de patients avec une cardiopathie ischémique débutante et de patients douloureux avec angiographie normale [wf778c1-38].",
     "Les patients cardiaques rapportaient surtout des symptômes physiques, comme la dyspnée et la douleur thoracique, mais rarement des symptômes cognitifs [wf778c1-38].",
     "La douleur thoracique des patients paniques était dominée par des pensées catastrophiques, comme la peur de mourir ou de perdre le contrôle [wf778c1-38].",
     "Piège d'examen : la douleur thoracique n'indique pas une panique plus sévère, car elle est cotée moins sévère que l'étouffement, la peur de mourir et les paresthésies [wf778c1-35]."]))
P.p("Un modèle de détection utilise des questionnaires de panique, la qualité et la localisation de la douleur ainsi que le sexe [w3ce001-3]. Il classe correctement 84 % des patients consultant aux urgences pour douleur thoracique, car il combine ces variables [w3ce001-3]. "
    "Ce modèle présente une sensibilité de 59 % et une spécificité de 93 %, pour une prévalence du trouble panique de 26 % dans l'échantillon [w3ce001-3]. "
    "Le Panic Screening Score, qui comprend quatre éléments, présente une sensibilité de 63 % et une spécificité de 84 % dans la cohorte de dérivation [wf28a93-19][wf28a93-20]. "
    "Plus de 92 % des cas d'anxiété de type panique restent non diagnostiqués à la sortie des urgences [w89be42-2].",
    ("scores de dépistage de la panique aux urgences", [
     "Le Panic Screening Score compte quatre éléments, identifie les attaques de panique avec ou sans trouble panique et se montre huit fois plus sensible que l'évaluation clinique d'un médecin urgentiste [wf28a93-19].",
     "Dans la cohorte de dérivation, sa sensibilité atteint 63 % et sa spécificité 84 % ; dans la validation rétrospective, elles atteignent 53 % et 85 % [wf28a93-20].",
     "La sensibilité reste insuffisante, et les auteurs jugent qu'elle doit être améliorée [wf28a93-20].",
     "Piège d'examen : un score négatif n'exclut pas une panique, car la sensibilité reste limitée [wf28a93-20]. Un score positif n'exclut pas non plus une maladie cardiaque, puisque celle-ci coexiste avec la panique [wf778c1-36]."]))
P.save()
