# -*- coding: utf-8 -*-
"""
Questions expertes de niveau Examen fédéral suisse (Session 2027).
Format unifié :
- type: "A" (1 meilleure réponse parmi 5 options A-E), "K" (4 propositions Vrai/Faux +/-), "M" (Menu Long 10-14 options)
- stem: vignette clinique ou question précise
- options: liste des choix (5 pour A, 4 pour K, 10-14 pour M)
- answer: index int (0-4) pour A, liste de 4 booléens [True, False, ...] pour K, index int pour M
- justification_options: liste expliquant chaque option une par une (pourquoi choisie ou rejetée)
- rappel_base: rappel concis de sciences fondamentales (anatomie, physiologie, pharmacologie)
- explication_specifique: raisonnement clinique ciblé, pièges d'examen, prise en charge suisse
- source: référence datée CH/UE
"""

EXPERT_QUESTIONS = {
    "G1": [
        {
            "id": "G1-EXP-A01",
            "type": "A",
            "theme": "Hyperhidrose primaire · Critères diagnostiques",
            "stem": "Un étudiant de 22 ans consulte pour une sudation axillaire et palmaire bilatérale excessive depuis l'âge de 15 ans, survenant 4 à 5 fois par semaine lorsqu'il écrit ou serre la main, mais absente la nuit. Son père présentait le même trouble. L'examen clinique est normal. Quelle est l'attitude diagnostique la plus appropriée ?",
            "options": [
                "Poser le diagnostic clinique d'hyperhidrose primaire focale sans bilan biologique systématique",
                "Prescrire d'emblée un dosage de TSH, T4 libre, glycémie à jeun et métanéphrines plasmatiques",
                "Exclure une hyperhidrose primaire car la sudation ne survient pas quotidiennement",
                "Réaliser une gravimétrie sur papier filtre pour confirmer le diagnostic avant tout traitement",
                "Demander une IRM thoracique à la recherche d'une compression de la chaîne sympathique"
            ],
            "answer": 0,
            "justification_options": [
                "A (Exacte) : Le patient remplit 6 des 7 critères RMS 2017 (sudation focale > 6 mois + localisation axillo-palmaire, bilatérale et symétrique, ≥ hebdomadaire, absente la nuit, début < 25 ans, anamnèse familiale). Le diagnostic est purement clinique.",
                "B (Fausse) : Aucun bilan hormonal ou biologique de routine n'est indiqué devant une forme focale primaire typique sans drapeau rouge.",
                "C (Fausse) : Les critères exigent une fréquence au moins hebdomadaire (≥ 1x/semaine), et non quotidienne.",
                "D (Fausse) : La gravimétrie sert surtout à la recherche clinique ; elle n'est pas requise pour le diagnostic courant.",
                "E (Fausse) : Une lésion de la chaîne sympathique donne une atteinte focale secondaire souvent unilatérale ou asymétrique, pas un tableau familial symétrique débutant à l'adolescence."
            ],
            "rappel_base": "Les glandes sudoripares eccrines (~3 millions) assurent la thermorégulation. Par exception anatomo-physiologique, leurs fibres sympathiques postganglionnaires sont cholinergiques (récepteurs muscariniques M3).",
            "explication_specifique": "Selon la RMS 2017, une sudation focale excessive > 6 mois avec ≥ 4/7 critères (aisselles/paumes/plantes/visage, bilatérale-symétrique, ≥ hebdomadaire, absente la nuit, début < 25 ans, histoire familiale, gêne quotidienne) évoque une hyperhidrose primaire (Se 99 %, Sp 82 %). Aucun critère pris isolément n'est obligatoire, mais l'absence de sueurs nocturnes et le début < 25 ans orientent fortement vers une cause primaire.",
            "source": "Menzinger S, Quenan S. Rev Med Suisse 2017;13:710-714."
        },
        {
            "id": "G1-EXP-A02",
            "type": "A",
            "theme": "Phéochromocytome · Piège thérapeutique majeur",
            "stem": "Une femme de 41 ans présente des accès paroxystiques associant céphalées pulsatiles, palpitations et sueurs profuses, avec une pression artérielle à 210/115 mmHg lors des crises. Les métanéphrines libres plasmatiques prélevées après 25 minutes de décubitus reviennent nettement élevées. Quel principe thérapeutique initial est impératif avant toute chirurgie ?",
            "options": [
                "Instaurer un alphabloquant (ex. phénoxybenzamine ou doxazosine) au moins 7 à 14 jours avant d'introduire un éventuel bêtabloquant",
                "Administrer immédiatement un bêtabloquant non cardiosélectif (propranolol) pour contrôler la tachycardie réflexe",
                "Réaliser une biopsie surrénalienne percutanée sous contrôle TDM avant de débuter le traitement médicamenteux",
                "Associer d'emblée un inhibiteur de l'ECA et un diurétique thiazidique sans blocage alpha",
                "Opérer en urgence dans les 24 heures sans préparation pharmacologique préalable"
            ],
            "answer": 0,
            "justification_options": [
                "A (Exacte) : Le blocage alpha-adrénergique (7–14 jours avant chirurgie, avec apport sodé) est obligatoire en premier pour éviter une vasoconstriction alpha non opposée.",
                "B (Fausse) : Piège mortel classique ! Un bêtabloquant donné avant l'alphabloquant bloque la vasodilatation bêta-2 et laisse les récepteurs alpha-1 sans opposition, déclenchant une crise hypertensive majeure.",
                "C (Fausse) : La biopsie d'un phéochromocytome est formellement contre-indiquée (risque de crise catécholaminergique fatale et d'hémorragie).",
                "D (Fausse) : Les diurétiques aggravent l'hypovolémie relative des patients porteurs d'un phéochromocytome et favorisent le collapsus.",
                "E (Fausse) : Une chirurgie sans préparation alpha-bloquante expose à des pics hypertensifs peropératoires et un collapsus post-exérèse."
            ],
            "rappel_base": "Les catécholamines (adrénaline, noradrénaline) stimulent à la fois les récepteurs α1 (vasoconstriction) et β2 (vasodilatation musculaire/splanchnique) ainsi que β1 (chronotropisme/inotropisme).",
            "explication_specifique": "La triade céphalées (60 %), palpitations (59 %), sudation (52 %) avec HTA évoque un phéochromocytome (mutation germinale jusqu'à 40 %). Après confirmation biochimique (métanéphrines plasmatiques après ≥ 20 min de décubitus, ou urinaires de 24 h), on réalise l'imagerie (TDM/IRM) puis une préparation par α-bloquant + expansion volémique/sodée pendant 7–14 jours. Le β-bloquant n'est ajouté qu'après blocage alpha si tachycardie persistante.",
            "source": "Meyer P. Rev Med Suisse 2009;5:15-18 ; ESH Working Group 2020."
        },
        {
            "id": "G1-EXP-A03",
            "type": "A",
            "theme": "Hypoglycémie · Bêtabloquants et sémiologie",
            "stem": "Un homme de 64 ans, diabétique de type 2 sous insuline glargine et metformine, suivi pour une cardiopathie ischémique traitée par bisoprolol 5 mg/j, est amené aux urgences pour confusion aiguë et sueurs profuses froides. Il ne présente aucun tremblement ni palpitation. Quel énoncé explique le mieux ce tableau ?",
            "options": [
                "Les bêtabloquants masquent les signes adrénergiques (tremblements, tachycardie) mais laissent persister les sueurs car elles sont médiées par l'acétylcholine",
                "Le bisoprolol bloque la sécrétion sudorale eccrine, ce qui indique que ces sueurs sont d'origine ischémique pure",
                "Chez le patient diabétique traité, le seuil biologique d'hypoglycémie est fixé à < 2,2 mmol/L",
                "En cas d'hypoglycémie avec confusion, il faut administrer 15 g de glucose per os avant toute mesure glycémique",
                "La metformine en monothérapie est la cause la plus fréquente d'hypoglycémie sévère nocturne"
            ],
            "answer": 0,
            "justification_options": [
                "A (Exacte) : La sudation hypoglycémique est médiée par le système sympathique cholinergique (ACh sur M3) et persiste donc sous bêtabloquant, contrairement aux tremblements et à la tachycardie (β-adrénergiques).",
                "B (Fausse) : Les bêtabloquants ne bloquent pas les récepteurs muscariniques M3 des glandes eccrines ; la sudation reste un signal d'alerte précieux.",
                "C (Fausse) : Chez le diabétique traité, le seuil d'hypoglycémie est < 4,0 mmol/L (hors diabète : < 2,85 mmol/L veineux).",
                "D (Fausse) : Un patient confus/troubles de la conscience présente un risque d'inhalation : privilégier le glucose IV (30 %) ou le glucagon 1 mg IM/SC, jamais la voie orale.",
                "E (Fausse) : La metformine ne provoque pas d'hypoglycémie en monothérapie ; c'est l'insuline (ou les sulfonylurées) qui est responsable."
            ],
            "rappel_base": "Bien qu'appartenant anatomiquement au système sympathique, les fibres postganglionnaires des glandes sudoripares eccrines libèrent de l'acétylcholine (récepteurs M3), et non de la noradrénaline.",
            "explication_specifique": "Devant sueurs + confusion sous traitement hypoglycémiant : glycémie capillaire/veineuse immédiate (< 4 mmol/L chez le diabétique). Chez un patient sous β-bloquant, l'absence de tachycardie ou de tremblement ne doit jamais rassurer : les sueurs cholinergiques restent le dernier signe d'alarme adrénergique/autonome avant la neuroglucopénie sévère.",
            "source": "Data/tip G1 · Triade de Whipple et seuils d'hypoglycémie."
        },
        {
            "id": "G1-EXP-A04",
            "type": "A",
            "theme": "Syndrome sérotoninergique · Critères de Hunter",
            "stem": "Une patiente de 34 ans traitée par venlafaxine (IRSN) débute du tramadol pour une lombalgie aiguë. Douze heures plus tard, elle consulte pour une diaphorèse profuse, une agitation, une tachycardie à 124/min, une température à 38,8 °C, une mydriase et un clonus spontané des membres inférieurs. Quelle est la prise en charge la plus adaptée ?",
            "options": [
                "Arrêt immédiat de la venlafaxine et du tramadol, hydratation et administration de benzodiazépines",
                "Administration urgente de paracétamol IV et d'ibuprofène pour abaisser la température corporelle",
                "Introduction de dantrolène IV en première intention comme antidote spécifique",
                "Ajout d'un triptan pour prévenir les céphalées vasculaires associées",
                "Poursuite de la venlafaxine à demi-dose pour éviter un syndrome de sevrage"
            ],
            "answer": 0,
            "justification_options": [
                "A (Exacte) : Elle remplit les critères de Hunter (agent sérotoninergique + clonus spontané). Le traitement repose sur l'arrêt des agents causaux, les soins de support et les benzodiazépines (agitation, rigidité, hyperthermie).",
                "B (Fausse) : Les antipyrétiques sont inefficaces dans le syndrome sérotoninergique car l'hyperthermie est due à l'hyperactivité musculaire et non à un dérèglement du thermostat hypothalamique.",
                "C (Fausse) : Le dantrolène est le traitement de l'hyperthermie maligne anesthésique (et parfois discuté dans le syndrome malin des neuroleptiques), pas du syndrome sérotoninergique.",
                "D (Fausse) : Les triptans sont eux-mêmes sérotoninergiques et aggraveraient la toxicité.",
                "E (Fausse) : La poursuite de l'agent causal met le pronostic vital en jeu ; la résolution survient souvent en 24 h après l'arrêt."
            ],
            "rappel_base": "L'hyperstimulation des récepteurs sérotoninergiques 5-HT2A et 5-HT1A centraux et périphériques provoque une triade : dysautonomie (diaphorèse, tachycardie, mydriase), altération mentale et hyperexcitabilité neuromusculaire (clonus, hyperréflexie).",
            "explication_specifique": "Début rapide (< 24 h) après ajout/augmentation d'un agent sérotoninergique (ISRS, IRSN, tramadol, IMAO, triptans). Critères de Hunter : agent sérotoninergique + clonus spontané (ou clonus inductible/oculaire + agitation/diaphorèse, etc.). Si T > 41 °C : sédation profonde, curarisation et intubation.",
            "source": "Rev Med Suisse 2012;8:2086-2090 · Syndrome sérotoninergique en Suisse."
        },
        {
            "id": "G1-EXP-A05",
            "type": "A",
            "theme": "Symptômes B & Lymphome · Diagnostic de certitude",
            "stem": "Un homme de 29 ans consulte pour des sueurs nocturnes profuses nécessitant de changer ses draps, une fièvre vespérale à 38,4 °C et un amaigrissement de 9 kg (poids initial 75 kg) en 4 mois. L'examen révèle une adénopathie sus-claviculaire gauche ferme, indolore, de 3 cm. Quel examen établit le diagnostic de certitude ?",
            "options": [
                "Biopsie-exérèse chirurgicale complète du ganglion sus-claviculaire",
                "Ponction-aspiration à l'aiguille fine (cytoponction) du ganglion",
                "TEP-TDM au 18F-FDG corps entier avant tout prélèvement tissulaire",
                "Dosage sérique de la LDH, de la VS et de la bêta-2-microglobuline",
                "Test de libération d'interféron gamma (IGRA) et intradermoréaction à la tuberculine"
            ],
            "answer": 0,
            "justification_options": [
                "A (Exacte) : Le diagnostic histologique d'un lymphome (classification OMS) exige une biopsie-exérèse ganglionnaire entière (ou prélèvement chirurgical suffisant) pour préserver l'architecture ganglionnaire.",
                "B (Fausse) : La cytoponction à l'aiguille fine détruit l'architecture tissulaire et est insuffisante pour typer et classer un lymphome.",
                "C (Fausse) : Le TEP-TDM sert au bilan d'extension (stadification Ann Arbor), jamais à remplacer la preuve histologique.",
                "D (Fausse) : La VS (> 50 mm/h ou > 30 avec symptômes B) et la LDH ont une valeur pronostique, pas diagnostique.",
                "E (Fausse) : L'IGRA ne distingue pas infection latente et tuberculose maladie et ne diagnostique pas un lymphome."
            ],
            "rappel_base": "Les symptômes B traduisent la libération systémique de cytokines inflammatoires (IL-6, TNF-α) par les cellules tumorales et le micro-environnement : fièvre > 38 °C, sueurs nocturnes profuses, perte pondérale inexpliquée > 10 % en 6 mois (ici 12 % en 4 mois).",
            "explication_specifique": "Devant des sueurs nocturnes avec symptômes B et adénopathie suspecte, les hypothèses graves incluent lymphome, tuberculose, VIH et endocardite. Pour le lymphome, seule la biopsie-exérèse ganglionnaire permet l'analyse morphologique et immunohistochimique indispensable selon ESMO 2018.",
            "source": "Eichenauer DA et al. Hodgkin lymphoma: ESMO Guidelines, Ann Oncol 2018."
        },
        {
            "id": "G1-EXP-A06",
            "type": "A",
            "theme": "Endocardite infectieuse · Priorité du bilan microbiologique",
            "stem": "Un homme de 68 ans porteur d'une prothèse valvulaire aortique consulte pour une fièvre à 38,7 °C évoluant depuis 10 jours avec sueurs nocturnes et asthénie. Il est hémodynamiquement stable sans signe de choc septique. L'auscultation note un souffle diastolique nouveau. Quelle est la priorité microbiologique immédiate ?",
            "options": [
                "Prélever au moins 3 paires d'hémocultures (aérobie/anaérobie, 10 mL chacune) à 30 minutes d'intervalle avant toute antibiothérapie",
                "Débuter immédiatement une antibiothérapie empirique IV puis prélever une paire d'hémocultures le lendemain",
                "Réaliser une sérologie Coxiella burnetii et Bartonella avant de prélever des hémocultures",
                "Faire une échocardiographie transœsophagienne en première intention sans hémocultures préalables",
                "Se contenter d'une seule paire d'hémocultures périphériques si le patient est fébrile au moment du prélèvement"
            ],
            "answer": 0,
            "justification_options": [
                "A (Exacte) : Chez un patient stable suspect d'endocardite infectieuse, prélever ≥ 3 paires d'hémocultures (10 mL par flacon) espacées d'au moins 30 min avant tout antibiotique est un critère majeur de Duke-ESC 2023.",
                "B (Fausse) : Débuter une antibiothérapie avant les hémocultures chez un patient stable négative les cultures et compromet l'identification du germe et l'antibiogramme.",
                "C (Fausse) : Les sérologies des germes intracellulaires ne sont demandées qu'en cas d'endocardite à hémocultures négatives.",
                "D (Fausse) : L'échocardiographie (ETT puis ETO) est indispensable, mais ne remplace jamais les hémocultures.",
                "E (Fausse) : Une seule paire est insuffisante pour documenter une bactériémie continue et exclure une contamination."
            ],
            "rappel_base": "La bactériémie de l'endocardite infectieuse est typiquement continue et de faible inoculum ; le prélèvement de ≥ 3 paires augmente la sensibilité à > 95 % et permet de distinguer un vrai pathogène d'un contaminant cutané.",
            "explication_specifique": "Selon les critères de Duke modifiés ESC 2023, les hémocultures positives et l'imagerie (ETT/ETO) sont les deux critères majeurs. Chez le patient instable/septique, on prélève rapidement 2–3 paires sans retarder l'antibiothérapie urgente ; chez le patient stable, on respecte les prélèvements avant antibiotiques et on réfère à l'Endocarditis Team.",
            "source": "ESC 2023 Guidelines for the management of endocarditis."
        },
        {
            "id": "G1-EXP-A07",
            "type": "A",
            "theme": "Hyperhidrose focale · Prise en charge graduée et sympathectomie",
            "stem": "Une patiente de 26 ans souffre d'une hyperhidrose axillaire primaire sévère (HDSS 4/4) résistante aux antiperspirants topiques à base de chlorure d'aluminium. Avant d'envisager une sympathectomie thoracique endoscopique, quelle option thérapeutique de deuxième ligne présente le meilleur rapport efficacité/tolérance et de quelle complication majeure faut-il l'informer si la chirurgie était finalement discutée ?",
            "options": [
                "Toxine botulique A intradermique (après repérage par test de Minor) ; complication chirurgicale majeure : hyperhidrose compensatrice",
                "Anticholinergique oral à vie d'emblée ; complication chirurgicale : syndrome de Frey systématique",
                "Ionophorèse axillaire quotidienne ; complication chirurgicale : anhidrose complète du visage dans 80 % des cas",
                "Excision chirurgicale des glandes apocrines uniquement ; complication : paralysie phrénique définitive",
                "Bêtabloquant oral continu ; complication chirurgicale : pneumothorax bilatéral irréversible"
            ],
            "answer": 0,
            "justification_options": [
                "A (Exacte) : La toxine botulique A intradermique bloque l'ACh au niveau des glandes eccrines pendant 6–12 mois (cartographie par test de Minor iode-amidon). La sympathectomie est le dernier recours en raison d'une hyperhidrose compensatrice sévère (10–40 % des cas).",
                "B (Fausse) : Les anticholinergiques oraux (ex. oxybutynine) entraînent des effets atropiniques systémiques (xérostomie, troubles visuels) et sont plutôt réservés aux formes diffuses ou échecs.",
                "C (Fausse) : L'ionophorèse (15–20 mA) est surtout adaptée aux paumes et aux plantes, difficilement aux aisselles.",
                "D (Fausse) : Les glandes impliquées dans l'hyperhidrose primaire sont les glandes eccrines (et non apocrines qui produisent l'odeur).",
                "E (Fausse) : Les bêtabloquants ne bloquent pas les récepteurs cholinergiques M3 des glandes eccrines."
            ],
            "rappel_base": "La toxine botulique A clive la protéine SNAP-25 du complexe SNARE dans la terminaison nerveuse cholinergique sympathique, empêchant l'exocytose des vésicules d'acétylcholine vers les glandes eccrines.",
            "explication_specifique": "Le test de Minor (solution iodée puis amidon) colore en bleu-noir les zones d'hyperhidrose pour guider les injections intradermiques. La sympathectomie thoracique expose à une hyperhidrose compensatrice (tronc, fesses, aines) dans 10–40 % des cas (souvent irréversible) et plus rarement à un syndrome de Claude Bernard-Horner.",
            "source": "Menzinger S, Quenan S. Rev Med Suisse 2017;13:710-714 ; AWMF S1 013-059 (2023)."
        },
        {
            "id": "G1-EXP-K01",
            "type": "K",
            "theme": "Hyperhidrose · Sémiologie, critères et drapeaux rouges",
            "stem": "Concernant l'évaluation clinique d'une sudation anormale (SSP G1), indiquez pour chacune des propositions suivantes si elle est vraie (+) ou fausse (-).",
            "options": [
                "Une sudation nocturne profuse, généralisée ou débutant après 25 ans oriente fortement vers une cause secondaire.",
                "Dans les critères RMS 2017 de l'hyperhidrose primaire, l'absence de sudation nocturne est un critère obligatoire à lui seul.",
                "Le test de Minor à l'iode et à l'amidon permet de quantifier précisément le débit sudoral en mg/min.",
                "Une sudation aiguë accompagnée d'une douleur thoracique impose un ECG interprété dans les 10 minutes et un dosage de troponine hypersensible."
            ],
            "answer": [True, False, False, True],
            "justification_options": [
                "a (+ Vrai) : La forme primaire est typiquement focale, symétrique, diurne et débute avant 25 ans ; les caractéristiques inverses imposent la recherche d'une cause secondaire.",
                "b (- Faux) : Piège d'examen ! La règle demande ≥ 4 critères sur 7 ; ni l'absence de sueurs nocturnes ni le début < 25 ans ne sont chacun obligatoires isolément dans le score combiné.",
                "c (- Faux) : Le test de Minor est qualitatif (cartographie topographique en noir/bleu) ; c'est la gravimétrie sur papier filtre qui quantifie le débit.",
                "d (+ Vrai) : Sueurs + douleur thoracique = drapeau rouge de syndrome coronarien aigu (ECG < 10 min dès le premier contact médical)."
            ],
            "rappel_base": "Les glandes eccrines sont diffuses et thermorégulatrices (ACh/M3), tandis que les glandes apocrines (aisselles, région génitale) sont androgéno-dépendantes et responsables de la bromhidrose après dégradation bactérienne.",
            "explication_specifique": "Le tri clinique distingue d'abord l'urgence vitale (SCA, hypoglycémie, sevrage sévère, crise thyrotoxique, syndrome sérotoninergique), puis différencie forme primaire (clinique) et secondaire (médicaments, endocrinopathies, infections, néoplasies).",
            "source": "Menzinger S, Quenan S. Rev Med Suisse 2017 ; Data/tip G1."
        },
        {
            "id": "G1-EXP-K02",
            "type": "K",
            "theme": "Causes secondaires de sudation · Endocrinologie et toxiques",
            "stem": "À propos des causes secondaires d'hyperhidrose et de leur prise en charge, indiquez si chaque proposition est vraie (+) ou fausse (-).",
            "options": [
                "Chez une femme de 51 ans présentant des bouffées de chaleur, des sueurs nocturnes et une aménorrhée depuis 14 mois, le diagnostic de ménopause est clinique sans dosage de FSH.",
                "En cas de suspicion de primo-infection à VIH devant des sueurs nocturnes et un syndrome grippal, un test rapide négatif à 10 jours du rapport à risque exclut l'infection.",
                "Un sevrage alcoolique avec score CIWA-Ar élevé nécessite notamment une supplémentation en vitamine B1 (thiamine) et un traitement par benzodiazépine (ex. oxazépam).",
                "Un patient présentant un syndrome d'apnées obstructives du sommeil (SAOS) non traité rapporte fréquemment des sueurs nocturnes, qui diminuent sous CPAP."
            ],
            "answer": [True, False, True, True],
            "justification_options": [
                "a (+ Vrai) : Dès 45 ans, le diagnostic de ménopause est clinique (aménorrhée ≥ 12 mois sans contraception hormonale) ; la FSH n'est dosée qu'entre 40–45 ans avec symptômes ou < 40 ans (insuffisance ovarienne prématurée).",
                "b (- Faux) : Un test rapide de 4e génération ne détecte l'infection qu'à partir de 2 semaines et ne l'exclut qu'à 6 semaines après l'exposition. En primo-infection précoce, privilégier un test de laboratoire sensible.",
                "c (+ Vrai) : Protocole suisse du sevrage alcoolique : vitamine B1 (300 mg/j) pour prévenir l'encéphalopathie de Gayet-Wernicke + benzodiazépines (oxazépam 60–200 mg/j guidé par CIWA-Ar).",
                "d (+ Vrai) : Les sueurs nocturnes (≥ 3 nuits/semaine) touchent ~1/3 des patients avec SAOS non traité et régressent sous pression positive continue (CPAP)."
            ],
            "rappel_base": "Les sueurs nocturnes du SAOS résultent de décharges sympathiques répétées lors des micro-éveils et de l'hypoxémie intermittente induits par les apnées obstructives.",
            "explication_specifique": "Ne pas réduire les sueurs nocturnes aux seules causes infectieuses ou néoplasiques : toujours intégrer la revue médicamenteuse (ISRS, opiacés, cholinergiques), la ménopause, les troubles anxieux et le SAOS.",
            "source": "Data/tip G1 · NICE Menopause, BAG/OFSP VIH, Rev Med Suisse."
        },
        {
            "id": "G1-EXP-K03",
            "type": "K",
            "theme": "Tuberculose, thyrotoxicose et physiologie sudorale",
            "stem": "Concernant la tuberculose, la thyrotoxicose et la physiologie de la sudation, indiquez si chaque proposition est vraie (+) ou fausse (-).",
            "options": [
                "En Suisse, la tuberculose pulmonaire active confirmée est une maladie à déclaration obligatoire au médecin cantonal et nécessite un test VIH systématique.",
                "Un test IGRA (Quantiféron) positif permet à lui seul de confirmer une tuberculose pulmonaire active contagieuse.",
                "Chez le sujet âgé, une thyrotoxicose peut se présenter sous une forme apathique avec fibrillation auriculaire sans tremblement marqué.",
                "La sueur primaire produite dans le glomérule de la glande eccrine est hypertonique, puis devient isotonique dans le canal excréteur."
            ],
            "answer": [True, False, True, False],
            "justification_options": [
                "a (+ Vrai) : Déclaration obligatoire au médecin cantonal en Suisse, schéma standard 2 HRZE / 4 HR et dépistage VIH systématique.",
                "b (- Faux) : Ni l'IGRA ni le test tuberculinique ne distinguent l'infection tuberculeuse latente de la tuberculose maladie active (qui requiert imagerie + PCR Xpert MTB/RIF + culture).",
                "c (+ Vrai) : La thyrotoxicose du sujet âgé est volontiers pauci-symptomatique (« apathique ») et dominée par les signes cardiovasculaires (FA) et l'amaigrissement.",
                "d (- Faux) : C'est l'inverse : la sueur primaire est quasi isotonique, puis le canal excréteur réabsorbe le NaCl (via CFTR) pour émettre une sueur finale hypotonique."
            ],
            "rappel_base": "À débit sudoral élevé, le temps de transit dans le canal excréteur diminue, réduisant la réabsorption de NaCl : la sueur devient plus salée (et dans la mucoviscidose, le défaut de CFTR empêche cette réabsorption, d'où le test à la sueur positif).",
            "explication_specifique": "La combinaison fièvre + sueurs nocturnes + perte de poids impose d'écarter tuberculose (RX thorax, Xpert/culture) et VIH. Pour la thyrotoxicose, doser TSH + T4L/T3L et rechercher une crise thyrotoxique (score Burch-Wartofsky ≥ 45).",
            "source": "OFSP Tuberculose ; ETA 2018 Graves' Hyperthyroidism ; Data/tip G1."
        },
        {
            "id": "G1-EXP-M01",
            "type": "M",
            "theme": "Menu Long · Diagnostic différentiel ciblé de la sudation",
            "stem": "Un homme de 52 ans, opéré 18 mois plus tôt d'une parotidectomie pour adénome pléomorphe, consulte car chaque fois qu'il mange un aliment acide ou épicé, la peau de sa joue droite devient érythémateuse et se couvre de sueur abondante. Quel diagnostic précis explique ce tableau ?",
            "options": [
                "Hyperhidrose primaire focale",
                "Hyperhidrose médicamenteuse",
                "Thyrotoxicose",
                "Phéochromocytome",
                "Hypoglycémie réactionnelle",
                "Lymphome hodgkinien",
                "Tuberculose extrapulmonaire",
                "Endocardite infectieuse",
                "Syndrome sérotoninergique",
                "Syndrome de Frey (sudation gustative)",
                "Syndrome d'apnées obstructives du sommeil",
                "Attaque de panique"
            ],
            "answer": 9,
            "justification_options": [
                "J (Exacte · Syndrome de Frey) : Repousse aberrante des fibres parasympathiques sécrétomotrices du nerf auriculo-temporal (destinées initialement à la parotide) vers les glandes sudoripares eccrines cutanées (toutes deux cholinergiques !). La mastication déclenche ainsi une sudation gustative localisée.",
                "Options A–I, K–L (Fausses) : Aucune autre entité ne provoque une sudation strictement unilatérale de la joue déclenchée par la prise alimentaire après chirurgie parotidienne."
            ],
            "rappel_base": "La réinnervation aberrante est possible parce que les fibres parasympathiques parotidiennes et les fibres sympathiques sudorales eccrines utilisent toutes deux l'acétylcholine comme neurotransmetteur.",
            "explication_specifique": "Le syndrome de Frey survient typiquement après parotidectomie ou traumatisme parotidien. Le traitement de référence en cas de gêne importante est l'injection intradermique locale de toxine botulique A.",
            "source": "Data/tip G1 · Syndrome de Frey et étiologies neurologiques focales."
        },
        {
            "id": "G1-EXP-M02",
            "type": "M",
            "theme": "Menu Long · Urgence sudorale chez un patient psychiatrique",
            "stem": "Un patient de 46 ans suivi pour dépression résistante est amené aux urgences après avoir associé de sa propre initiative du millepertuis et du moclobémide à son traitement de sertraline. Il présente une diaphorèse majeure, une température à 39,4 °C, une diarrhée aqueuse, des myoclonies et un clonus oculaire bilatéral. Quel diagnostic retenez-vous en priorité ?",
            "options": [
                "Hyperhidrose primaire focale",
                "Hyperhidrose médicamenteuse bénigne",
                "Crise thyrotoxique",
                "Phéochromocytome",
                "Hypoglycémie sévère",
                "Lymphome agressif",
                "Tuberculose miliaire",
                "Endocardite aiguë",
                "Primo-infection VIH",
                "Sevrage alcoolique compliqué",
                "Syndrome sérotoninergique",
                "Attaque de panique"
            ],
            "answer": 10,
            "justification_options": [
                "K (Exacte · Syndrome sérotoninergique) : Association explosive de trois agents sérotoninergiques (ISRS + IMAO + millepertuis) avec triade dysautonomique (diaphorèse, hyperthermie, diarrhée) et clonus oculaire remplissant les critères de Hunter.",
                "Options A–J, L (Fausses) : Le clonus oculaire et les myoclonies dans un contexte de poly-exposition sérotoninergique écartent le sevrage alcoolique, le phéochromocytome ou la crise thyrotoxique."
            ],
            "rappel_base": "Les IMAO (moclobémide) bloquent la dégradation de la sérotonine tandis que les ISRS (sertraline) et le millepertuis bloquent sa recapture synaptique, provoquant une accumulation massive de 5-HT.",
            "explication_specifique": "Urgence toxicologique : arrêt immédiat de tous les agents sérotoninergiques, benzodiazépines IV, refroidissement actif et réhydratation. Les antipyrétiques sont inefficaces.",
            "source": "Rev Med Suisse 2012;8:2086-2090."
        }
    ]
}
