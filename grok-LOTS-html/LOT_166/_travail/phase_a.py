#!/usr/bin/env python3
"""Phase A LOT_166."""
import sys
from pathlib import Path

ICI = Path(__file__).resolve().parent
sys.path.insert(0, str(ICI))
sys.path.insert(0, str(ICI.parents[1] / "outils/dessinateur"))
import dessinateur
import figurer
from gabarit import btn, fen, p, page, table
from plus_a import etendre

LOT = ICI.parent
POLICE = "../outils/dessinateur/polices/AtkinsonHyperlegible-Regular.ttf"

A = '<abbr title="information professionnelle suisse">AIPS</abbr>'
EASL = '<abbr title="European Association for the Study of the Liver">EASL</abbr>'
BTS = '<abbr title="British Thoracic Society">BTS</abbr>'
ESC = '<abbr title="European Society of Cardiology">ESC</abbr>'
FAST = '<abbr title="focused assessment with sonography for trauma">FAST</abbr>'
EFAST = '<abbr title="extended focused assessment with sonography for trauma">eFAST</abbr>'
BLUE = '<abbr title="bedside lung ultrasound in emergency">BLUE</abbr>'
LDH = '<abbr title="lactate déshydrogénase">LDH</abbr>'
SAAG = '<abbr title="gradient d&#x27;albumine entre le sérum et l&#x27;ascite">SAAG</abbr>'
PNN = '<abbr title="polynucléaires neutrophiles">PNN</abbr>'
RAPID = '<abbr title="renal, age, purulence, infection source, dietary factors">RAPID</abbr>'
WINFOCUS = '<abbr title="World Interactive Network Focused on Critical Ultrasound">WINFOCUS</abbr>'


def fig_html(desc):
    for n in desc["niveaux"]:
        n.pop("cliche", None)
    frag = dessinateur.rendre(desc, POLICE)
    import re
    frag = re.sub(r"<script>.*?</script>", "", frag, flags=re.S)
    return frag


def sources():
    lignes = (LOT / "evidence/INDEX.md").read_text(encoding="utf-8").splitlines()
    items = []
    for ligne in lignes:
        ligne = ligne.strip()
        if not ligne:
            continue
        items.append(f"<li>{ligne.split('. ', 1)[1]}</li>")
    return "<ol class=\"sources\">\n" + "\n".join(items) + "\n</ol>"


def construire():
    glossaire = fen("w-glossaire", "Sigles", "".join([
        p(f"{A} : information professionnelle suisse. Les doses chiffrées des spécialités viennent de ce texte, avec le numéro Swissmedic."),
        p(f"{EASL} 2018 : recommandations sur la cirrhose décompensée, l'ascite et la péritonite bactérienne spontanée."),
        p(f"{BTS} 2023 : recommandation sur la maladie pleurale, critères de Light, drainage et score {RAPID}."),
        p(f"{ESC} 2015 et {ESC} 2025 : épanchement péricardique et tamponnade."),
        p(f"{FAST} puis {EFAST} : quatre fenêtres abdominales et péricardique, puis les coupes thoraciques."),
        p(f"{BLUE} : profils échographiques de la détresse respiratoire aiguë, Lichtenstein et Mezière, 2008."),
        p(f"{SAAG}, {PNN}, {LDH}, {WINFOCUS}."),
        p('<abbr title="électrocardiogramme">ECG</abbr>, <abbr title="tomodensitométrie">TDM</abbr>, <abbr title="imagerie par résonance magnétique">IRM</abbr>, <abbr title="anti-inflammatoires non stéroïdiens">AINS</abbr>, <abbr title="rapport international normalisé">INR</abbr>, <abbr title="peptide natriurétique de type B">BNP</abbr>, <abbr title="New York Heart Association">NYHA</abbr>.'),
    ]))
    essentiel = "".join([
        p(f"Un liquide anéchogène vu à l'échographie est un épanchement jusqu'à preuve du contraire. Il peut être pleural, péritonéal ou péricardique. La nature, sang, pus, transsudat ou exsudat, ne se lit pas sur le noir de l'image."),
        p(f"Trois gestes ne se retardent pas : la recherche d'une tamponnade, la recherche d'un sang libre après un trauma, et la ponction d'une ascite fébrile pour compter les {PNN}."),
        p(f"Le liquide pleural est un exsudat si un critère de Light est rempli. L'ascite avec {SAAG} d'au moins 1,1 g/dl, soit 11 g/l, implique une hypertension portale. Les {PNN} au-dessus de 250 par mm³ définissent la péritonite bactérienne spontanée selon l'{EASL} 2018.", "2"),
        p(f"Les seuils, le score {RAPID} entier, les protocoles et les doses suisses sont dans les fenêtres. Les schémas de Morison, du signe de la colonne et du péricarde s'ouvrent au point 6.", "1"),
        glossaire,
    ])
    ilots = {}
    ilots["p1"] = (
        "".join([
            p(f"La situation F2.18 est la découverte d'un épanchement abdominal ou pleural à l'échographie. Le liquide libre péritonéal s'appelle ascite quand il est diffus. Une collection cloisonnée, un urinome ou un bilome ne sont pas une ascite libre."),
            p(f"Le même examen peut montrer un épanchement pleural, au-dessus du diaphragme, ou un épanchement péricardique. Ces trois liquides se cherchent parce que l'{EFAST} et l'échographie cardiaque passent par les mêmes fenêtres.", "6"),
            p("Les dix diagnostics de la leçon sont des causes, pas dix images différentes. " + btn("w-termes", "le vocabulaire") + " fixe les mots avant les seuils."),
        ]),
        [fen("w-termes", "Vocabulaire", "".join([
            p("Ascite : liquide libre dans la cavité péritonéale. Grade 1 seulement à l'échographie, grade 2 distension modérée, grade 3 grosse ascite, selon l'EASL 2018.", "2"),
            p("Épanchement pleural : liquide dans l'espace pleural. Transsudat ou exsudat selon les trois critères de Light repris par la BTS en 2023.", "1"),
            p("Épanchement parapneumonique : liquide au contact d'une pneumonie. Il est simple, compliqué, ou empyème si le pus est macroscopique.", "1"),
            p("Péritonite bactérienne spontanée : infection d'une ascite sans perforation. Le seuil lu est un compte de neutrophiles au-dessus de 250 par microlitre.", "2"),
            p("Hémopéritoine et hémothorax : sang libre. Au début il est souvent aussi noir qu'une ascite."),
            p("Épanchement péricardique : liquide dans le sac. La tamponnade est la compression des cavités, pas la simple lame.", "3"),
            p("Ascite maligne et épanchement pleural malin : deux maladies distinctes, souvent exsudatives ou à gradient bas pour le péritoine."),
            p("Pleurésie tuberculeuse : exsudat souvent lymphocytaire, avec cloisons fréquentes.", "1"),
            p("Ascite par hypoalbuminémie : le nephrotique et la dénutrition font partie des transsudats à gradient bas ou à protéine basse. Le classement exact se fait sur le gradient et la protéine, pas sur le seul diagnostic clinique.", "2"),
        ]))],
    )
    ilots["p2"] = (
        "".join([
            p("Aucune série suisse lue ne classe ces dix causes par prévalence. Le rang E de l'algorithme est l'ordre d'exclusion, pas un rang de fréquence."),
            p("En Occident, la cirrhose explique environ 80 % des ascites. Le reste se partage entre malignité, insuffisance cardiaque, tuberculose, maladie pancréatique et causes plus rares.", "2"),
            p("Cinq à 10 % des cirrhoses compensées décompensent par une ascite chaque année. Après la décompensation, la survie médiane tombe vers deux ans dans la synthèse de l'EASL.", "2"),
            p(btn("w-epi", "ce que ces chiffres changent") + " au lit, et " + btn("w-pleural-freq", "côté pleural") + "."),
        ]),
        [
            fen("w-epi", "Fréquence et conséquence", "".join([
                p("Le grade 1 n'est vu qu'à l'échographie. Il ne se traite pas comme une ascite tendue, mais il compte dans le suivi d'une cirrhose connue.", "2"),
                p("Une ascite nouvelle de grade 2 ou 3, ou toute ascite chez un patient hospitalisé pour une complication de cirrhose, impose une ponction diagnostique avant de conclure à une simple poussée de sel.", "2"),
                p("La péritonite bactérienne spontanée peut être peu bruyante. Dans une série observationnelle citée par l'EASL, une ponction retardée de plus de 12 heures après l'admission multipliait la mortalité par 2,7.", "2"),
                p("Le retard tue plus souvent que la rareté. Le médecin qui voit un liquide noir cherche d'abord ce qui compresse ou ce qui infecte."),
            ])),
            fen("w-pleural-freq", "Causes pleurales fréquentes", "".join([
                p("La BTS 2023 place l'insuffisance cardiaque congestive, la cirrhose et l'hypoalbuminémie parmi les transsudats, et la malignité, l'infection pleurale, l'embolie pulmonaire et la pleurite auto-immune parmi les exsudats fréquents.", "1"),
                p("L'embolie pulmonaire donne souvent un petit épanchement. Il ne doit pas faire oublier le diagnostic si le liquide est un exsudat peu abondant et la clinique évocatrice.", "1"),
                p("La sensibilité des signes cliniques de l'épanchement est basse, de 0,20 à 0,48 dans la synthèse de la BTS : l'échographie et la ponction expliquent le liquide, pas la percussion seule.", "1"),
            ])),
        ],
    )
    ilots["p3"] = (
        "".join([
            p("Le liquide s'accumule quand la formation dépasse la résorption. Pour la plèvre, la BTS rappelle que le mécanisme change avec la cause : pression hydrostatique, pression oncotique, perméabilité ou blocage lymphatique.", "1"),
            p("Pour l'ascite cirrhotique, l'EASL décrit la rétention rénale de sodium, le système rénine-angiotensine-aldostérone, la vasodilatation splanchnique et l'hypertension portale qui compartimente le volume.", "2"),
            p(btn("w-starling", "ce que cela change sur le liquide") + " puis " + btn("w-echo-phys", "pourquoi le liquide est noir") + "."),
        ]),
        [
            fen("w-starling", "Du mécanisme au type de liquide", "".join([
                p("Hypertension portale : le gradient d'albumine sérum-ascite est d'au moins 1,1 g/dl, soit 11 g/l, avec une exactitude d'environ 97 % pour dire que l'hypertension portale participe, selon l'EASL.", "2"),
                p("La protéine de l'ascite inférieure à 1,5 g/dl marque un risque plus élevé de péritonite bactérienne spontanée. Ce n'est pas, à lui seul, le diagnostic d'infection.", "2"),
                p("Insuffisance cardiaque : le liquide pleural est en général un transsudat bilatéral. L'ascite cardiaque garde un gradient élevé, parce que l'hypertension veineuse hépatique est une forme d'hypertension portale. La protéine d'ascite n'est pas celle, très basse, de la cirrhose évoluée. Le chiffre de partage protéique cardiaque n'est pas recopié : il n'était pas dans l'extrait EASL ouvert."),
                p("Inflammation pleurale, infection, cancer, tuberculose : la plèvre laisse passer les protéines et la lactate déshydrogénase. Un seul des trois critères de Light suffit à parler d'exsudat.", "1"),
                p("Sang et pus : le liquide peut commencer anéchogène. Les cloisons et les particules mobiles viennent ensuite. Ils orientent vers un exsudat riche, pas vers un transsudat libre.", "1"),
            ])),
            fen("w-echo-phys", "Image et physique du faisceau", "".join([
                p("L'eau libre ne renvoie pas d'écho : elle est noire. L'air arrête le faisceau. C'est pourquoi, sans épanchement, la colonne thoracique disparaît au diaphragme, et pourquoi elle réapparaît au-dessus du diaphragme quand un liquide conduit les ultrasons.", "7"),
                p("Le foie et la rate sont des fenêtres. L'espace de Morison est le récessus entre le foie et le rein droit. L'espace spléno-rénal est son symétrique gauche. Le cul-de-sac de Douglas est le point le plus déclive du péritoine pelvien. Le péricarde se regarde sous l'appendice xiphoïde, à travers le foie."),
                p("Une bande noire n'a pas de spécificité étiologique. Le même noir peut être de l'ascite, de l'urine, de la bile ou du sang frais."),
            ])),
        ],
    )
    ilots["p4"] = (
        "".join([
            p("La démarche tient en quatre questions, dans cet ordre : le patient est-il en train de se comprimer ou de saigner, le liquide est-il infecté, de quel côté de la membrane est-il, quelle est la cause."),
            p("On ne classe pas un liquide pleural sans les critères de Light, ni une ascite de cause incertaine sans le gradient d'albumine. On ne pose pas un drain parapneumonique sur une impression : le pH, le pus, le glucose et la lactate déshydrogénase ont des seuils.", "1"),
            p(btn("w-pas", "les pas, avec les seuils") + "."),
        ]),
        [fen("w-pas", "Démarche pas à pas", "".join([
            p("Pas 1. Constantes, pression artérielle, fréquence, saturation, température, jugulaires, pouls paradoxal. Une hypotension avec jugulaires tendues et cœur inaudible fait traiter la tamponnade sans attendre la taille de la lame.", "3"),
            p("Pas 2. Trauma ou douleur abdominale brutale avec liquide déclive : chercher le sang dans les quatre fenêtres, puis le thorax. L'instabilité ouvre le bloc, pas une ponction diagnostique différée."),
            p("Pas 3. Ascite et fièvre, douleur, encéphalopathie, insuffisance rénale ou hémorragie digestive : ponction avant les diurétiques. Neutrophiles au-dessus de 250 par mm³ : traiter comme une péritonite bactérienne spontanée sans attendre la culture.", "2"),
            p("Pas 4. Plèvre : échographie immédiate pour ponctionner. Un critère de Light positif : exsudat. Les trois doivent manquer pour parler de transsudat.", "1"),
            p("Pas 5. Pneumonie et liquide : pus macroscopique, drain. Sinon pH tout de suite. pH ≤ 7,2 : drain si le volume est ponctionnable sans danger. pH ≥ 7,4 : pas de drain immédiat. Entre les deux : lactate déshydrogénase, et drain à discuter au-dessus de 900 UI/l, surtout si fièvre, gros volume, glucose bas, rehaussement pleural ou cloisons.", "1"),
            p("Pas 6. Si le pH n'est pas disponible tout de suite, un glucose pleural inférieur à 3,3 mmol/l indique une forte probabilité d'épanchement parapneumonique compliqué.", "1"),
            p("Pas 7. Volume pleural chez le patient ventilé, hors hémothorax et hors empyème : séparation maximale en fin d'expiration, en millimètres, multipliée par vingt. L'erreur moyenne publiée est de 158 ml.", "5"),
        ]))],
    )
    ilots["p5"] = (
        "".join([
            p("L'anamnèse cherche le trauma, la cirrhose, l'alcool, l'hépatite, une cardiopathie, une fièvre, une toux, un cancer, une tuberculose, une dialyse, un syndrome néphrotique, une grossesse extra-utérine, un traitement anticoagulant."),
            p("Drapeaux rouges : hypotension, marbrures, silence auscultatoire avec turgescence jugulaire, douleur thoracique syncopale, défense abdominale, fièvre sur ascite, vomissements fécaloïdes, hématémèse.", "2"),
            p(btn("w-questions", "questions utiles") + "."),
        ]),
        [fen("w-questions", "Questions et ce qu'elles changent", "".join([
            p("Début en minutes après un choc ou une douleur scapulaire : penser à l'hémopéritoine, rate, foie, grossesse extra-utérine, anévrisme."),
            p("Orthopnée, prise de poids, œdèmes mous : transsudat cardiaque. Le liquide pleural est souvent bilatéral, plus à droite.", "1"),
            p("Fièvre et toux : parapneumonique. La purulence macroscopique nomme l'empyème et indique le drain, avant le pH.", "1"),
            p("Ascite connue et confusion : ponction le jour même. Le délai supérieur à 12 heures est associé à plus de morts dans la série citée par l'EASL.", "2"),
            p("Amaigrissement, antécédent de cancer, liquide unilatéral : exsudat jusqu'à preuve du contraire, cytologie sur 25 à 50 ml.", "1"),
            p("Origine à haute endémie, sueurs, liquide lymphocytaire cloisonné : tuberculose pleurale ou péritonéale. Les cloisons complexes orientent vers la tuberculose plus que vers le cancer dans la synthèse de la BTS, sans la prouver seules.", "1"),
        ]))],
    )
    ilots["p6"] = (
        "".join([
            p("L'examen commence par le choc et la respiration, pas par la mesure du liquide. Jugulaires, pouls paradoxal, matité déclive, murmure aboli, souffle aboli, défense, orifices herniaires, signes de cirrhose."),
            p("Trois figures d'examen : " + btn("w-fig-morison", "hypocondre droit") + ", " + btn("w-fig-pleural", "signe de la colonne") + ", " + btn("w-fig-peri", "sous-xiphoïdien") + ". Les pages avec cliché source sont liées dans chaque fenêtre."),
            p("Le pouls paradoxal est une baisse inspiratoire de la pression artérielle systolique de plus de 10 mmHg en respiration calme. Il manque souvent. Son absence n'écarte pas une tamponnade.", "3"),
        ]),
        [
            fen("w-fig-morison", "Figure. Espace de Morison", fig_html(figurer.morison()) + p('<a href="figures/f-morison.htm">Ouvrir la figure avec le cliché source et le survol actif</a>. James Heilman, Wikimedia Commons, licence Creative Commons attribution, partage dans les mêmes conditions, 3.0.')),
            fen("w-fig-pleural", "Figure. Signe de la colonne", fig_html(figurer.pleural()) + p('<a href="figures/f-pleural.htm">Ouvrir la figure avec le cliché source</a>. L’en-tête nominatif du fichier d’origine a été recadré.')),
            fen("w-fig-peri", "Figure. Péricarde sous-xiphoïdien", fig_html(figurer.peri()) + p('<a href="figures/f-peri.htm">Ouvrir la figure avec le secteur échocardiographique source</a>. AMC Echolab, CardioNetworks.')),
        ],
    )
    ilots["p7"] = (
        "".join([
            p(f"Trois syndromes se séparent sur l'image et sur le liquide : le syndrome de liquide libre traumatique, le syndrome d'ascite portale, le syndrome d'exsudat pleural. Le péricarde est un quatrième compartiment, lu avec l'{ESC}.", "3"),
            p(btn("w-fenetres", "les fenêtres FAST et eFAST") + ", " + btn("w-blue", "les profils BLUE lus dans le résumé de 2008") + ", " + btn("w-signes", "signes échographiques à ne pas amputer") + "."),
        ]),
        [
            fen("w-fenetres", "FAST et eFAST", "".join([
                p(f"Le {FAST} regarde quatre fenêtres : l'espace de Morison, l'espace spléno-rénal, le cul-de-sac de Douglas, la fenêtre péricardique sous-xiphoïdienne. L'{EFAST} ajoute les coupes pleurales, antérieures pour l'air et postérieures pour le liquide."),
                p("Le texte intégral du cours avancé de trauma n'est pas recopié. Les quatre fenêtres sont celles de l'examen nommé eFAST dans le travail de 2021 sur le signe de la colonne, et celles que les schémas de cette leçon montrent.", "7"),
                p("Une fenêtre positive veut dire liquide, pas « laparotomie automatique ». L'instabilité hémodynamique avec liquide libre après un trauma est une indication opératoire dans la logique de ce protocole. Un patient stable va au scanner."),
                p("Le péricarde fait partie du FAST. Une lame péricardique après un trauma pénétrant se draine. Une lame chronique connue ne se draine pas au seul motif qu'elle est vue."),
            ])),
            fen("w-blue", "Profils du protocole BLUE, résumé de 2008", "".join([
                p(f"L'article de Lichtenstein et Mezière, Chest 2008, groupe les signes en profils. Le résumé consulté donne cinq résultats, tous repris ici. Le nom {BLUE} désigne cet ensemble. Les lettres isolées ne sont pas listées à la place de ces résultats, pour ne pas couper la série.", "6"),
                p("Lignes A antérieures prédominantes et glissement présent : asthme ou bronchopneumopathie chronique obstructive, sensibilité 89 %, spécificité 97 %.", "6"),
                p("Lignes B antérieures diffuses et multiples, avec glissement : œdème pulmonaire, sensibilité 97 %, spécificité 95 %.", "6"),
                p("Profil antérieur normal et thrombose veineuse profonde : embolie pulmonaire, sensibilité 81 %, spécificité 99 %.", "6"),
                p("Glissement aboli, lignes A et point pulmonaire : pneumothorax, sensibilité 81 %, spécificité 100 %.", "6"),
                p("Condensations alvéolaires antérieures, lignes B diffuses sans glissement, syndrome interstitiel asymétrique, ou condensations et épanchements postérieurs sans lignes B antérieures diffuses : pneumonie, sensibilité 89 %, spécificité 94 %.", "6"),
                p("L'ensemble de ces profils aurait donné le bon diagnostic dans 90,5 % des cas de la série. L'épanchement pleural entre dans le groupe pneumonie quand il est postérieur, sans lignes B antérieures diffuses. Ce n'est pas un profil à part dans le résumé.", "6"),
                p(f"Le consensus {WINFOCUS} de 2012 a produit des recommandations fortes pour 65 énoncés d'échographie pulmonaire au lit. La liste intégrale des 73 énoncés n'a pas été retranscrite depuis le seul résumé.", "9"),
            ])),
            fen("w-signes", "Signes échographiques", "".join([
                table("Signes à reconnaître, sans en retirer un", ["Signe", "Ce qu'on voit", "Ce qu'on n'en conclut pas"], [
                    ["Espace de Morison", "Bande noire entre foie et rein droit", "La nature du liquide"],
                    ["Espace spléno-rénal", "Bande noire entre rate et rein gauche", "Une rate intacte si la fenêtre est vide"],
                    ["Cul-de-sac de Douglas", "Liquide déclive derrière l'utérus ou la vessie", "Le volume exact en millilitres"],
                    ["Signe de la colonne", "La colonne se prolonge au-dessus du diaphragme", "À lui seul, du sang plutôt que du transsudat"],
                    ["Signe du plancton", "Particules échogènes qui bougent dans le liquide", "Une sensibilité, le résumé de 2018 n'en donne pas"],
                    ["Cloisons", "Septa dans le liquide", "Un transsudat simple"],
                    ["Liseré péricardique", "Noir autour du cœur, mesuré en fin de diastole", "Une tamponnade, qui est clinique"],
                ]),
                p("Signe de la colonne en trauma, contre le scanner : sensibilité 78,7 %, spécificité 92,6 %, valeur prédictive positive 65 %, valeur prédictive négative 97,8 %. Le signe sert surtout à dire qu'il n'y a pas d'épanchement quand il manque.", "7"),
                p("Le signe du plancton est nommé pour l'épanchement pleural dans le Journal of Medical Imaging and Radiation Oncology en 2018. Aucun chiffre de performance n'était dans le résumé consulté. Le signe reste enseigné : particules mobiles, liquide riche.", "8"),
                p("Les cloisons, dans l'infection pleurale, s'associent à un séjour plus long et à plus de chirurgie dans la synthèse de la BTS. Elles ne sont pas, à elles seules, l'indication du drain : le pus, le pH et le glucose décident.", "1"),
            ])),
        ],
    )
    ilots["p8"] = (
        "".join([
            p("Le diagnostic positif de l'épanchement est l'image : liquide anéchogène dans un espace qui n'en contient pas. Le diagnostic de la cause est biologique et clinique."),
            p(btn("w-light", "les trois critères de Light") + " et " + btn("w-saag", "le gradient d'albumine, entier") + "."),
        ]),
        [
            fen("w-light", "Critères de Light, BTS 2023", "".join([
                p("Le liquide pleural est un exsudat si un ou plusieurs des critères suivants sont remplis. Il faut les trois négatifs pour un transsudat. En enseigner deux seulement serait une classification coupée.", "1"),
                table("Les trois critères, tous requis dans la leçon", ["Critère", "Seuil d'exsudat"], [
                    ["Protéine pleurale / protéine sérique", "Supérieur à 0,5"],
                    [f"{LDH} pleurale / {LDH} sérique", "Supérieur à 0,6"],
                    [f"{LDH} pleurale", "Supérieure aux deux tiers de la limite supérieure de la normale du laboratoire pour la lactate déshydrogénase sérique"],
                ]),
                p("On dose la lactate déshydrogénase et la protéine dans le liquide et dans le sang le même jour. Un seul ratio, sans le sang, ne calcule pas Light.", "1"),
                p("Un transsudat traité comme un exsudat multiplie les biopsies. Un exsudat étiqueté cardiaque retarde un cancer ou un empyème."),
            ])),
            fen("w-saag", "Gradient d'albumine sérum-ascite", "".join([
                p("Le gradient est l'albumine sérique moins l'albumine de l'ascite, prélevées le même jour. L'EASL retient un gradient d'au moins 1,1 g/dl, c'est-à-dire 11 g/l, comme signe que l'hypertension portale participe, exactitude d'environ 97 %.", "2"),
                p("Au-dessus de ce seuil : cirrhose, ascite cardiaque, obstacle veineux sus-hépatique. En dessous : carcinose péritonéale, tuberculose péritonéale, pancréatite, syndrome néphrotique, fuite biliaire. Cette liste n'est pas un rang de fréquence suisse."),
                p("L'EASL demande le gradient quand la cause n'est pas évidente ou quand une autre maladie que la cirrhose est possible. La cirrhose déjà prouvée ne dispense pas de la ponction si une infection est possible.", "2"),
                p("Protéine d'ascite inférieure à 1,5 g/dl : risque accru de péritonite bactérienne spontanée. Ce seuil n'est pas le seuil diagnostique de l'infection. L'infection se définit par les neutrophiles.", "2"),
            ])),
        ],
    )
    ilots["p9"] = (
        "".join([
            p("Tout liquide ponctionné part au laboratoire avec une question. Plèvre : protéine, lactate déshydrogénase, pH sur seringue adaptée, glucose, cytologie, culture en flacons d'hémoculture si infection suspecte.", "1"),
            p("Ascite : neutrophiles, protéine, albumine, culture au lit d'au moins 10 ml dans des flacons d'hémoculture. Amylase, cytologie ou mycobactéries selon la clinique.", "2"),
            p(btn("w-volume", "estimer le volume pleural") + " et " + btn("w-ponction", "indications et contre-indications de la ponction") + "."),
        ]),
        [
            fen("w-volume", "Formule de Balik, 2006", "".join([
                p("Chez le patient ventilé, allongé, tronc relevé d'environ 15 degrés, sonde sur la ligne axillaire postérieure, coupe transverse à la base : on mesure la séparation maximale entre plèvre pariétale et plèvre viscérale, en fin d'expiration, en millimètres.", "5"),
                p("Volume approximatif en millilitres = 20 fois cette séparation. La formule de régression publiée était 18,3 fois la séparation plus 19,4. La forme simplifiée est celle qu'on retient au lit.", "5"),
                p("Erreur moyenne de prédiction : 158,4 ml, écart-type 160,6 ml. Corrélation r = 0,72. Ce n'est pas une balance."),
                p("Exclus de la dérivation : déformation thoracique, chirurgie pulmonaire, maladie du diaphragme, hémothorax, empyème, évacuation incomplète. On n'utilise pas vingt fois la séparation pour coter un hémothorax ou un empyème.", "5"),
                p("Quatre-vingt-une personnes, 92 épanchements, 11 exclus pour aspiration incomplète. Aucun pneumothorax ni saignement dans cette série. Le succès de ramener du liquide sous échographie était de 100 %.", "5"),
            ])),
            fen("w-ponction", "Ponction : quand, et quand s'abstenir", "".join([
                p("Plèvre : la BTS recommande la ponction guidée par l'image, tout de suite, pour réduire le pneumothorax et rater moins souvent le liquide. La marque cutanée faite plus tôt, dans une autre pièce, n'est pas un guidage.", "1"),
                p("Ascite nouvelle grade 2 ou 3, et toute hospitalisation pour complication de cirrhose : ponction diagnostique.", "2"),
                p("Contre-indication lue pour la grande évacuation : coagulation intravasculaire disséminée. L'EASL écrit qu'il n'y a pas de donnée pour transfuser du plasma ou des plaquettes de façon prophylactique, même quand beaucoup de centres le font sous 40 % d'activité de prothrombine ou 40 000 plaquettes.", "2"),
                p("Dans une série citée, avec INR supérieur à 1,5 et plaquettes inférieures à 50 000, deux saignements mineurs au point de ponction sur 142 paracentèses. Le risque hémorragique ne justifie pas, à lui seul, de retarder une ponction diagnostique urgente.", "2"),
                p("On ne ponctionne pas à travers une infection de peau. On ne vide pas une ascite sous anticoagulant efficace sans peser le geste. Le patient qui ne tient pas en place est une contre-indication pratique."),
                p("Cytologie d'un épanchement pleural suspect de cancer : envoyer 25 à 50 ml. Infection pleurale suspecte : tube sec et flacon d'hémoculture.", "1"),
                p("Le pH pleural ne doit pas être souillé par l'anesthésique local ni par l'héparine résiduelle d'une seringue de gaz du sang : le pH baisse. Un délai avant la mesure le fait monter. Les deux erreurs inversent la décision de drain.", "1"),
            ])),
        ],
    )
    ilots["p10"] = (
        "".join([
            p("L'arbre exclut d'abord ce qui tue dans l'heure, puis ce qui tue dans la journée. Le numéro DX n'est pas le rang E."),
            p(btn("w-algo", "algorithme") + " et " + btn("w-drain", "drainage parapneumonique, critères complets") + " et " + btn("w-rapid", "score RAPID entier") + "."),
        ]),
        [
            fen("w-algo", "Ordre d'exclusion", "".join([
                p("E1. Épanchement péricardique et tamponnade. Instabilité et signes de compression : remplissage prudent et drainage. La taille seule ne décide pas."),
                p("E2. Hémopéritoine et hémothorax. Trauma, grossesse extra-utérine, rupture vasculaire. Liquide libre et choc : hémostase chirurgicale ou radiologique."),
                p("E3. Épanchement parapneumonique et empyème. Pus, ou pH, ou glucose, selon les seuils de la BTS 2023."),
                p("E4. Péritonite bactérienne spontanée. Neutrophiles au-dessus de 250 par mm³ dans une ascite."),
                p("E5. Ascite de l'hypertension portale. Gradient d'au moins 11 g/l, cirrhose le plus souvent."),
                p("E6. Épanchements de l'insuffisance cardiaque. Transsudat, souvent bilatéral, ascite à gradient élevé possible."),
                p("E7. Épanchement pleural malin. Exsudat unilatéral, cytologie."),
                p("E8. Ascite maligne. Gradient bas, cytologie."),
                p("E9. Pleurésie tuberculeuse. Exsudat lymphocytaire, cloisons, biopsie si la culture tarde."),
                p("E10. Ascite par hypoalbuminémie. Syndrome néphrotique, dénutrition, entéropathie. Le gradient et la protéine séparent cette cause de la cirrhose."),
            ])),
            fen("w-drain", "Quand drainer un parapneumonique", "".join([
                p("Le pus macroscopique est un empyème. Il se draine. Ce critère ne dépend pas du pH.", "1"),
                p("Sans pus, le pH se mesure tout de suite.", "1"),
                p("pH ≤ 7,2 : haut risque d'épanchement compliqué. Drain intercostal si l'échographie montre un volume accessible sans danger.", "1"),
                p("pH strictement supérieur à 7,2 et strictement inférieur à 7,4 : risque intermédiaire. On dose la lactate déshydrogénase. Au-dessus de 900 UI/l, le drain se discute, surtout s'il reste de la fièvre, un gros volume, un glucose bas, un rehaussement pleural au scanner ou des cloisons.", "1"),
                p("La BTS écrit le glucose bas de cette zone intermédiaire comme 72 mg/dl, soit au plus 4,0 mmol/l. Ce n'est pas le même seuil que le glucose de remplacement du pH.", "1"),
                p("pH ≥ 7,4 : bas risque. Pas de drain immédiat.", "1"),
                p("Sans pH disponible : glucose pleural inférieur à 3,3 mmol/l, forte probabilité de forme compliquée, et ce chiffre peut décider du drain dans le bon contexte.", "1"),
                p("Pièges de pH bas qui ne sont pas une infection : pleurésie rhumatoïde, cancer évolué, mésothéliome. La BTS le rappelle.", "1"),
                p("Drain initial de l'infection pleurale : petit calibre, 14 French ou moins. La chirurgie d'emblée n'est pas supérieure sur les données lues. La thoracoscopie médicale n'est pas le traitement initial recommandé.", "1"),
                p("Si l'on décide de ne pas drainer, on revoit le patient et l'on répète la ponction pour ne pas manquer le passage à la forme compliquée.", "1"),
            ])),
            fen("w-rapid", "Score RAPID, barème complet", "".join([
                p(f"Le score {RAPID} stratifie l'adulte qui a une infection pleurale. La BTS 2023 en fait une recommandation conditionnelle pour parler du pronostic avec le patient. Il ne remplace pas le pH pour décider du drain.", "1"),
                p("Le pus vaut 0 point et le liquide non purulent vaut 1 point. C'est l'inverse de l'intuition. Dans la dérivation, la non-purulence prédisait le mauvais pronostic. Rahman, Chest 2014, et le tableau 18 de la BTS.", "1"),
                table("Barème entier, 0 à 7", ["Lettre", "Mesure", "Points"], [
                    ["R rein", "Urée inférieure à 5,0 mmol/l", "0"],
                    ["R rein", "Urée de 5,0 à 8,0 mmol/l", "1"],
                    ["R rein", "Urée supérieure à 8,0 mmol/l", "2"],
                    ["A âge", "Moins de 50 ans", "0"],
                    ["A âge", "De 50 à 70 ans", "1"],
                    ["A âge", "Plus de 70 ans", "0".replace("0", "2")],
                    ["P pus", "Liquide purulent", "0"],
                    ["P pus", "Liquide non purulent", "1"],
                    ["I infection", "Acquise en ville", "0"],
                    ["I infection", "Acquise à l'hôpital", "1"],
                    ["D albumine", "Albumine supérieure à 27,0 g/l", "0"],
                    ["D albumine", "Albumine inférieure à 27,0 g/l", "1"],
                ]),
                p("Catégories : 0 à 2, risque bas. 3 à 4, risque moyen. 5 à 7, risque haut. Dans la validation prospective PILOT citée par les travaux ultérieurs, les morts à trois mois étaient d'environ 3 %, 9 % et 31 % selon ces trois bandes dans la cohorte de dérivation rappelée par l'article.", "17"),
                p("Dans MIST2, un score haut restait associé à la mort (rapport de cotes 14,1, intervalle 3,5 à 56,8). Le score moyen n'était pas significatif dans cette validation.", "17"),
                p("Les cloisons échographiques ne font pas partie du score : elles n'étaient pas dans les bases de dérivation. Leur présence diminue la performance du score, sans le remplacer.", "17"),
            ])),
        ],
    )
    # fix the silly replace - I need age >70 to be 2. Let me check I didn't leave a bug.
    # I wrote "Plus de 70 ans", "0".replace which is pointless and returns "2" because "0".replace("0","2") is "2". OK it works but ugly. Leave it, it evaluates to "2".
    ilots["p11"] = (
        "".join([
            p(f"Les doses suisses sont celles de l'{A}. Une conduite européenne qui n'est pas l'indication de l'information professionnelle est écrite comme telle."),
            p(f"Ascite cirrhotique : {btn('w-diur', 'spironolactone et furosémide')}. Infection de l'ascite : {btn('w-atb', 'ceftriaxone et albumine')}. Péricardite sans ascite : {btn('w-peri-ttt', 'anti-inflammatoire et colchicine')}. Hémorragie variqueuse : {btn('w-gly', 'terlipressine')}."),
            p("Numéros Swissmedic lus : 27257, 30629, 59876, 62660, 48164, 67974, 44470."),
        ]),
        [
            fen("w-diur", "Diurétiques de l'ascite", "".join([
                p("« Avec un quotient urinaire Na/K supérieur à 1.0: 100 mg/jour. Lorsque ce rapport est inférieur à 1.0: 200 à 400 mg/jour. » Information professionnelle d'Aldactone, cirrhose avec ascite, n° 27257.", "10"),
                p("Aldactone n'a pas son plein effet avant le troisième jour. La dose d'entretien est la plus basse qui stabilise le poids.", "10"),
                p("L'EASL, pour un premier épisode d'ascite modérée, commence par l'antiminéralocorticoïde seul, 100 mg par jour, paliers de 100 mg toutes les 72 heures, maximum 400 mg par jour. Ce maximum rejoint le plafond suisse de 400 mg par jour lu pour la cirrhose avec ascite.", "2"),
                p("En l'absence de réponse, perte de poids inférieure à 2 kg par semaine, ou en cas d'hyperkaliémie, l'EASL ajoute le furosémide, de 40 mg par jour jusqu'à cent soixante milligrammes par jour, par paliers de 40 mg. Le plafond de cent soixante milligrammes est celui de l'EASL 2018. L'information professionnelle du Lasix 40 mg, n° 30629, fait débuter l'adulte par un demi à deux comprimés par jour et fixe la dose maximale lue à 1'500 mg par jour, orale ou intraveineuse.", "11"),
                p("Chez l'enfant, Lasix oral : 2 mg de furosémide par kg, au plus 40 mg par jour. Aldactone chez l'enfant : 1.5-3.0 mg/kg. Ces phrases sont pédiatriques, pas le schéma de l'ascite adulte.", "11"),
                p("Perte de poids maximale sous diurétique, EASL : 0,5 kg par jour sans œdème, 1 kg par jour avec œdèmes. Au-delà, le volume plasmatique chute.", "2"),
                p("On arrête ou l'on baisse devant une encéphalopathie, une natrémie qui tombe, une créatinine qui monte, un potassium sous 3 mmol/l ou au-dessus de 6 mmol/l. Les définitions précises de l'ascite réfractaire sont dans le tableau de l'EASL : spironolactone 400 mg par jour et furosémide cent soixante milligrammes par jour depuis au moins une semaine, sel sous 90 mmol par jour, perte de poids insuffisante.", "2"),
                p("Les anti-inflammatoires non stéroïdiens sont contre-indiqués dans la cirrhose avec ascite, EASL, parce qu'ils bloquent les prostaglandines rénales. L'information professionnelle de l'ibuprofène, n° 48164, contre-indique les troubles hépatiques graves, cirrhose du foie ou ascite.", "14"),
            ])),
            fen("w-atb", "Infection de l'ascite et albumine", "".join([
                p("« En général, 1 - 2 g de Ceftriaxon Labatec une fois par jour (toutes les 24 heures). Lors d'infections sévères ou en présence de germes moyennement sensibles, la dose quotidienne unique peut être augmentée jusqu'à 4 g. » n° 59876.", "12"),
                p("L'information professionnelle lue ne nomme pas la péritonite bactérienne spontanée. L'EASL 2018 demande une antibiothérapie couvrant les bactéries du liquide, sans que la phrase suisse ci-dessus soit une indication nominative. On reste dans la fourchette 1 à 2 g par jour, jusqu'à 4 g si l'infection est sévère, et l'on documente que l'indication précise n'est pas dans l'extrait."),
                p("Albumine dans la péritonite bactérienne spontanée, EASL : 1,5 gramme par kilogramme au diagnostic et 1 gramme par kilogramme le troisième jour. L'information professionnelle d'Albunorm, n° 62660, adapte la dose au patient et ne fixe pas ce schéma. Le schéma est donc celui de l'EASL 2018, pas une posologie recopiée d'Albunorm.", "2"),
                p("L'effet sur le syndrome hépatorénal et la mort était net chez les patients dont la bilirubine était d'au moins 68 micromoles par litre ou la créatinine d'au moins 88 micromoles par litre dans l'essai cité par l'EASL.", "2"),
                p("Grande évacuation de plus de 5 litres : 8 g/l d'ascite retirée, en albumine, à la fin du geste. En dessous de 5 litres le risque de dysfonction circulatoire est bas, mais l'EASL garde l'albumine.", "2"),
                p("Albunorm ne s'utilise pas pour « normaliser un chiffre d'albumine ». La notice dit d'adapter la perfusion au volume circulant, pas à l'albuminémie seule.", "13"),
            ])),
            fen("w-peri-ttt", "Péricarde, doses et limites", "".join([
                p("Tamponnade : drainage écho-guidé, remplissage, pas d'attente d'un bilan étiologique. La lame large, plus de 20 mm en fin de diastole, est un critère de haut risque dans l'ESC 2015 et reste le seuil de lame large dans l'ESC 2025. Les trois classes sont : moins de 10 mm, de 10 à 20 mm, plus de 20 mm.", "3"),
                p("Péricardite aiguë sans ascite et sans cirrhose : l'ESC ajoute la colchicine à l'aspirine ou à un anti-inflammatoire. Pour la récidive, dose lue : 0,5 mg une fois par jour si le poids est inférieur à 70 kg, ou 0,5 mg deux fois par jour si le poids est d'au moins 70 kg, pendant au moins six mois, sans dose de charge.", "3"),
                p("COLCTAB, n° 67974, concerne la crise de goutte dans l'extrait lu : 1 mg puis 0,5 mg, au plus 2 mg par 24 heures, et au plus 6 mg par crise. Cette information professionnelle ne nomme pas la péricardite. On ne recopie pas le schéma de la goutte comme s'il était celui de la péricardite.", "15"),
                p("Ibuprofène Sandoz, n° 48164, affections rhumatismales : 1200 à 1800 mg par jour, jusqu'à 2400 mg par jour dans certains cas. Contre-indication lue : cirrhose ou ascite. On ne le donne donc pas à un patient qui a une ascite, même si l'ESC parle d'ibuprofène dans la péricardite.", "14"),
                p("Le sac normal contient 10 à 50 ml. Une lame idiopathique de moins de 10 mm, sans symptôme, n'exige pas de surveillance serrée selon l'ESC 2015. Au-delà de 10 mm, le contrôle se rapproche.", "3"),
            ])),
            fen("w-gly", "Terlipressine de l'hémorragie variqueuse", "".join([
                p("Glypressine, n° 44470, indication lue : traitement aigu des varices œsophagiennes hémorragiques. Poids supérieur à 50 kg : 1 à 2 mg intraveineux toutes les 4 à 6 heures. Poids inférieur à 50 kg : 1 mg selon le même rythme.", "16"),
                p("Maximum lu : 12 mg par jour, soit 2 mg toutes les 4 heures, pendant 36 heures au plus, puis 6 mg. Durée au plus 5 jours. Pression et électrocardiogramme pendant le traitement.", "16"),
                p("Ce n'est pas le traitement de l'épanchement. C'est le traitement de l'hémorragie qui décompense la cirrhose et qui oblige, le même jour, à ponctionner l'ascite.", "2"),
            ])),
        ],
    )
    ilots["p12"] = (
        "".join([
            p("Prévenir la ponction inutile et la ponction trop tardive. Toute ascite de cirrhose hospitalisée est ponctionnée. Tout épanchement pleural inexpliqué est ponctionné sous échographie.", "1"),
            p("Restriction sodée et dose minimale de diurétique après une grande évacuation, pour que l'ascite ne se reforme pas le lendemain. Vaccinations et sevrage alcoolique font partie du traitement de la cirrhose, pas du liquide seul.", "2"),
            p("Le patient apprend les signes qui ramènent : fièvre, confusion, ventre qui se retend, essoufflement brutal, syncope."),
        ]),
        [fen("w-prev", "Ce qui évite la récidive grave", "".join([
            p("Albumine après une évacuation de plus de 5 litres : 8 g/l retirés. Sans elle, la dysfonction circulatoire post-paracentèse fait chuter le rein et la natrémie.", "2"),
            p("Ne pas prescrire d'anti-inflammatoire non stéroïdien à un patient avec ascite. La notice suisse de l'ibuprofène et l'EASL se rejoignent.", "14"),
            p("Contrôler le potassium sous spironolactone. L'effet commence après le troisième jour : une kaliémie du lendemain ne dit pas encore la dose d'entretien.", "10"),
            p("Revoir un parapneumonique non drainé. Le passage au pH bas se fait en heures, pas en semaines.", "1"),
        ]))],
    )
    ilots["p13"] = (
        "".join([
            p("Liquide noir : compartiment, puis gravité, puis laboratoire. Morison, Douglas, rate, colonne, péricarde."),
            p("Light : trois critères, un suffit pour l'exsudat. Gradient d'albumine : 11 g/l. Neutrophiles : au-dessus de 250 par mm³. pH pleural : 7,2 et 7,4, glucose 3,3 mmol/l, pus. Score RAPID : le pus vaut 0.", "1"),
            p("Balik : vingt fois les millimètres, pas pour le sang ni le pus. Tamponnade : clinique, lame en trois classes, 10 et 20 mm."),
            p("Les diurétiques de l'ascite et leurs numéros d'autorisation sont dans la fenêtre dédiée, séparés des grammes de la céphalosporine."),
                p("Ceftriaxon Labatec, n° 59876 : en général 1 à 2 g une fois par jour, jusqu'à 4 g si l'infection est sévère. L'albumine de la péritonite suit l'EASL, en grammes par kilogramme, et n'est pas la posologie d'Albunorm. L'ibuprofène est interdit en cas d'ascite."),
        ]),
        [fen("w-cles", "À restituer à l'examen", "".join([
            p("Citer les trois critères de Light avec 0,5, 0,6 et les deux tiers."),
            p("Citer le gradient 1,1 g/dl et les neutrophiles au-dessus de 250."),
            p("Citer le barème RAPID jusqu'au bout, y compris pus = 0 et non purulent = 1, urée, âge, lieu, albumine 27 g/l, bandes 0-2, 3-4, 5-7."),
            p("Citer les quatre fenêtres et le signe de la colonne avec sa valeur prédictive négative de 97,8 % dans la série de trauma de 2021.", "7"),
            p("Ne pas appeler tamponnade une lame de 12 mm chez un patient stable."),
        ]))],
    )
    ilots["p14"] = (
        "".join([
            p("Le piège central est de croire que l'image noire a une cause. Le deuxième est de retarder la ponction d'une ascite fébrile. Le troisième est d'inverser le score RAPID en donnant un point au pus."),
            p(btn("w-cas", "cas corrigé") + " et " + btn("w-pieges", "autres pièges") + "."),
        ]),
        [
            fen("w-cas", "Cas type, corrigé", "".join([
                p("Homme de 58 ans, cirrhose alcoolique connue, admis pour fièvre à 38,6 °C et douleur diffuse du ventre. Pression artérielle 102/64 mmHg, fréquence 104 par minute, pas de défense localisée. L'échographie montre une ascite libre, espace de Morison et Douglas. Pas de lame péricardique."),
                p("La bonne première décision est la ponction avant le scanner et avant d'augmenter le diurétique. Le laboratoire ramène 1 800 neutrophiles par mm³, protéine 12 g/l, gradient d'albumine 18 g/l. La culture est ensemencée au lit."),
                p("Correction. Gradient au-dessus de 11 g/l : hypertension portale, cohérente avec la cirrhose. Neutrophiles au-dessus de 250 : péritonite bactérienne spontanée, même si la culture revient négative, ce qui arrive souvent. Ceftriaxon dans la fourchette suisse de 1 à 2 g par jour, jusqu'à 4 g si l'infection est jugée sévère, n° 59876, en disant que l'indication nominative n'est pas dans l'extrait. Albumine 1,5 gramme par kilogramme le jour même et 1 gramme par kilogramme à J3, schéma EASL, pas la notice d'Albunorm. Pas d'ibuprofène. Pas de drain pleural : il n'y a pas de plèvre dans l'énoncé."),
                p("Ce qui ferait faux : attendre la culture, donner un aminoside sans lire la fonction rénale, calculer un score RAPID sur une ascite, appeler cela un hémopéritoine parce que le liquide est noir."),
            ])),
            fen("w-pieges", "Pièges d'examen", "".join([
                p("Appeler exsudat un liquide dont un seul prélèvement de lactate déshydrogénase est haut, sans le sang du jour. Light exige les ratios ou le seuil des deux tiers de la normale sérique.", "1"),
                p("Oublier que le pH monte avec le délai et baisse avec la lidocaïne ou l'héparine.", "1"),
                p("Drainer tout épanchement parapneumonique, y compris celui dont le pH est d'au moins 7,4 et qui n'est pas du pus.", "1"),
                p("Utiliser vingt fois la séparation pour un empyème cloisonné. Balik a exclu ces liquides.", "5"),
                p("Donner 400 mg de spironolactone d'emblée quand le rapport sodium sur potassium urinaire est supérieur à 1. La notice commence alors à 100 mg par jour.", "10"),
                p("Confondre la dose de goutte de la colchicine et la dose de péricardite de l'ESC.", "15"),
                p("Poser un diagnostic de tamponnade sur une lame de 8 mm. La classe légère est inférieure à 10 mm et, sans symptôme, elle n'est pas une urgence de drainage.", "3"),
            ])),
        ],
    )
    etendre(ilots, fen, p, table)
    html = page(
        "LOT_166_Phase_A_V0.html",
        "Épanchement abdominal ou pleural détecté à l’échographie",
        "Situation de départ F2.18. Phase A. Texte du 31 octobre 2026. Dix diagnostics, rang E distinct du numéro DX.",
        essentiel,
        ilots,
        sources(),
    )
    out = LOT / "LOT_166_Phase_A_V0.html"
    out.write_text(html, encoding="utf-8")
    print(out, len(html.encode()))


if __name__ == "__main__":
    construire()
