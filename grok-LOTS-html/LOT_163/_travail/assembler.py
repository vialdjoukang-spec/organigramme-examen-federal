# -*- coding: utf-8 -*-
"""Rédige LOT_163 à partir des faits sourcés. Lancer depuis la racine du dépôt."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from moteur import page, paras, p, table, ecrire, SOURCES  # noqa: E402

# src : numéro d'INDEX
A, E, U, K, M, P, C, G = 1, 2, 3, 4, 5, 6, 7, 8
FOS, MON, NIT, BAC, CIP, TAM, PRE, ALL, RAM = 9, 10, 11, 12, 13, 14, 15, 16, 17


def bloc(items):
    return paras(items)


def cas(qui, sediment, lecture, geste, erreur, src):
    return [
        (f"{qui}. Sédiment ou contexte : {sediment}.", src),
        (f"Lecture. {lecture}", src),
        (f"Geste. {geste}", src),
        (f"La copie est fausse si l'on écrit : {erreur}", src),
    ]


def aua_table():
    return table(
        "Risque de cancer urothélial, hématurie microscopique, AUA/SUFU 2025",
        ["Critère", "Faible ou négligeable", "Intermédiaire", "Élevé"],
        [
            ["Nombre de critères", "Tous", "Un ou plus", "Un ou plus"],
            ["Hématies sur un examen", "3 à 10 par champ", "11 à 25 par champ", "Plus de 25 par champ"],
            ["Autre critère d'abondance", "Aucun", "Déjà faible, sans bilan, et 3 à 25 au contrôle", "Antécédent d'hématurie macroscopique"],
            ["Âge, femme", "Moins de 60 ans", "60 ans ou plus", "L'âge seul ne classe pas une femme en élevé"],
            ["Âge, homme", "Moins de 40 ans", "40 à 59 ans", "60 ans ou plus"],
            ["Tabac", "Jamais, ou moins de 10 paquets-années", "10 à 30 paquets-années", "Plus de 30 paquets-années"],
            ["Facteurs ajoutés", "Aucun", "Un ou plus", "Un ou plus, et déjà un critère élevé"],
            ["Risque lu de malignité", "0 à 0,4 %", "0,2 à 3,1 %", "1,3 à 6,3 %"],
        ],
    )


def facteurs_ajoutes():
    return bloc([
        ("Facteurs ajoutés de cancer urothélial, liste complète lue. Symptômes irritatifs du bas appareil. Radiothérapie pelvienne antérieure. Cyclophosphamide ou ifosfamide. Antécédent familial de cancer urothélial ou syndrome de Lynch. Exposition professionnelle au benzène ou aux amines aromatiques, caoutchouc, pétrochimie, colorants. Corps étranger à demeure dans la voie urinaire.", A),
        ("L'âge, le sexe, le tabac, le nombre d'hématies, la persistance et l'hématurie macroscopique sont déjà dans les colonnes du tableau. On ne les compte pas une seconde fois comme facteur ajouté.", A),
        ("Une femme de 62 ans, sans autre critère élevé, est intermédiaire. Elle n'est pas élevée du seul fait de l'âge.", A),
        ("Un homme de 62 ans est élevé du fait de l'âge, même avec 4 hématies par champ et sans tabac.", A),
    ])


def cristaux_table():
    return table(
        "Cristaux du sédiment, morphologie, pH et biréfringence, curriculum 2019",
        ["Cristal", "Forme", "pH", "Lumière polarisée"],
        [
            ["Oxalate monohydraté", "Ovoïde, haltère, bâtonnet, incolore", "5,4 à 6,7", "Forte"],
            ["Oxalate dihydraté", "Bipyramide incolore, enveloppe", "5,4 à 6,7", "Faible"],
            ["Phosphate de calcium", "Prismes, aiguilles, étoiles, rosettes", "6,7 à 7,0", "Forte"],
            ["Phosphate triple, struvite", "Trapèzes, prismes, couvercle de cercueil", "6,2 à 7,0", "Forte"],
            ["Acide urique", "Ambre, losanges, tonneaux, rosettes, aiguilles, plaques à six côtés", "5,4 à 5,8", "Forte, polychrome"],
            ["Cystine", "Plaques hexagonales incolores, bords irréguliers", "5,5", "Faible"],
            ["Leucine", "Sphères jaune-brun, stries concentriques", "5,5 à 6,5", "Croix de Malte"],
            ["2,8-dihydroxyadénine", "Rond brun-rouge, spicules centrales", "5,5 à 7,0", "Croix de Malte"],
            ["Tyrosine", "Aiguilles fines en faisceaux ou rosettes", "5,5 à 6,5", "Forte"],
            ["Cholestérol", "Plaques minces à bords nets", "5,5", "Pas de biréfringence"],
            ["Urate d'ammonium", "Sphères jaune-brun en pomme d'arroche", "5,5 à 7,0", "Forte"],
            ["Carbonate de calcium", "Haltères, bâtonnets, trèfle", "7,0", "Forte"],
            ["Bilirubine", "Aiguilles jaunes collées aux cellules", "5,5", "Faible"],
            ["Sulfadiazine", "Gerbes de blé, ambre, coques", "5,5", "Forte"],
            ["Aciclovir", "Aiguilles fines", "5,5 à 7,0", "Forte"],
            ["Atazanavir", "Aiguilles fines, isolées ou groupées", "6,0 à 7,0", "Forte"],
            ["Méthotrexate", "Jaune-brun", "5,4 à 6,0", "Forte"],
            ["Vitamine C", "Même aspect que l'oxalate monohydraté", "5,4 à 6,7", "Forte"],
            ["Triamtérène", "Sphères brunes, parfois vertes, orange ou rouges", "5,5", "Croix de Malte"],
            ["Ciprofloxacine", "Aiguilles, étoiles, éventails, gerbes, incolores", "Au-dessus de 7,0", "Forte"],
            ["Amoxicilline", "Aiguilles fines en balai", "5,5 à 6,5", "Forte"],
        ],
    )


def atlas_cylindres():
    return bloc([
        ("Les cylindres se forment dans le tubule distal et le canal collecteur. La matrice est l'uromoduline, aussi appelée protéine de Tamm-Horsfall, sécrétée par la branche ascendante large.", E),
        ("Cylindre hyalin. Indice de réfraction bas, mieux vu en contraste de phase. Urine du matin concentrée, déshydratation, effort, et aussi maladie rénale. Il ne signe pas à lui seul une glomérulonéphrite.", E),
        ("Cylindre granuleux. Granulations fines ou grossières. Il oriente vers une maladie rénale. Quand il est dense et brun, couleur terre brûlée, on le nomme cylindre granuleux brun boueux.", C),
        ("Le brun boueux, en grand nombre chez un patient hospitalisé en insuffisance rénale aiguë, est tenu pour évocateur d'une nécrose tubulaire sévère. Le même aspect granuleux se voit aussi dans la néphrite interstitielle, la microangiopathie thrombotique et d'autres lésions. Il n'est donc pas une preuve isolée.", C),
        ("Cylindre cireux. Grand, bords nets ou échancrés, réfringent, homogène, aspect de cire. Il se voit dans l'insuffisance rénale chronique.", E),
        ("Cylindre graisseux. Il contient des lipides. Il accompagne une protéinurie abondante. Sous lumière polarisée, les gouttelettes de cholestérol forment une croix de Malte.", E),
        ("Corps ovalaires gras. Ce sont des cellules tubulaires ou des macrophages gorgés de lipides. Ils peuvent être pris dans le cylindre.", C),
        ("Cylindre hématique. Il indique un saignement du parenchyme rénal. On ne le confond pas avec un amas d'hématies sans matrice.", E),
        ("Cylindre leucocytaire. En général des granulocytes. Il oriente vers une pyélonéphrite, une néphrite interstitielle ou une glomérulonéphrite proliférative.", E),
        ("Cylindre de cellules tubulaires. Nécrose tubulaire aiguë, néphrite interstitielle, rejet cellulaire, maladies glomérulaires. Si l'on ne distingue plus leucocyte et cellule tubulaire, on dit seulement cylindre cellulaire.", E),
        ("Cylindres d'hémoglobine et de myoglobine. Brunâtres, surface granuleuse. La morphologie ne les sépare pas. L'hémoglobine peut venir d'un cylindre hématique dégradé ou d'une hémolyse. La myoglobine se voit dans l'écrasement.", E),
        ("Pseudo-cylindres. Papier, cheveu, fibres, cristaux agrégés. On ne les rend pas comme des cylindres.", E),
    ])


def seuils_hematurie():
    return bloc([
        ("L'hématurie microscopique se définit par au moins 3 hématies par champ, sur un seul examen microscopique d'un recueil correct. Recommandation forte, niveau de preuve C.", A),
        ("Une bandelette positive, même à l'état de traces, ne définit pas l'hématurie microscopique. Elle impose la microscopie.", A),
        ("La bandelette sanguine peut être positive sans hématie : myoglobine, hémoglobine libre, déshydratation, effort, sang menstruel, povidone iodée.", A),
        ("La sensibilité analytique de la plage sang est d'environ 80 % à 10 fois 10 exposant 6 hématies par litre, contre un compte de particules. Les hématies lysent. L'hémoglobine et la myoglobine baissent la spécificité.", E),
        ("Acanthocytes : au moins 5 % des hématies excrétées. Dans la glomérulonéphrite prouvée, 75 patients sur 143, sensibilité 52 %. Hors glomérule, 4 patients sur 187, spécificité 98 %. Les acanthocytes y étaient 12,4 % des hématies, et moins de 2 % hors glomérule.", K),
        ("Les autres formes dites dysmorphiques, échinocytes, anulocytes, fantômes, schizocytes, stomatocytes, codocytes, knizocytes, se voient des deux côtés. Elles ne signent pas le glomérule. Les seuils publiés de 10 à 80 % de dysmorphie viennent de cette définition floue.", K),
        ("Un curriculum de 2019 écrit aussi que des hématies dysmorphiques au-dessus de 5 % des hématies totales soutiennent un saignement glomérulaire, tout en rappelant que des hématies isomorphes restent fréquentes dans la glomérulonéphrite. On garde les deux phrases. On ne les fond pas en un seul seuil.", C),
        ("Le guide KDIGO 2021 demande, dans toute maladie glomérulaire, la morphologie des hématies et la recherche de cylindres hématiques ou d'acanthocytes. Suivre l'abondance et la persistance de l'hématurie peut avoir une valeur pronostique, surtout dans la néphropathie à immunoglobuline A et la vascularite à immunoglobuline A.", G),
        ("Protéinurie, hématies dysmorphiques, cylindres cellulaires ou insuffisance rénale : avis néphrologique. Le bilan urologique selon le risque n'est pas annulé par cet avis.", A),
        ("Antiagrégant ou anticoagulant : même bilan que sans ces médicaments, quel que soit le produit et le niveau d'anticoagulation.", A),
        ("Hématurie mise sur une infection : on recontrôle le sédiment après traitement. Le délai lu va d'au moins trois semaines après la résolution à au plus trois mois.", A),
        ("Risque faible ou négligeable : nouveau sédiment dans les six mois, pas de cystoscopie ni d'imagerie immédiates.", A),
        ("Cytologie et marqueurs urinaires de tumeur : pas pour décider la cystoscopie initiale si le risque est faible ou négligeable, ni s'il est élevé.", A),
        ("Antécédent familial de carcinome rénal, syndrome tumoral rénal génétique, ou Lynch personnel ou familial : imagerie de la voie excrétrice haute, quelle que soit la catégorie.", A),
    ])


def seuils_infection():
    return bloc([
        ("Leucocyturie. La limite diagnostique lue est 10 fois 10 exposant 6 cellules par litre, soit 10 par microlitre, seulement si l'urine est concentrée comme une urine du matin. Osmolalité au-dessus de 300 mOsm/kg, ou densité réfractométrique au-dessus de 1,015. Une urine diluée peut être un faux négatif.", E),
        ("Nitrites. Spécificité haute. Les germes qui réduisent le nitrate les produisent. L'entérocoque, le staphylocoque saprophyte et certains non fermentants restent souvent négatifs. La leucocyte estérase relève la sensibilité.", E),
        ("Méta-analyse de 72 études. Sensibilité combinée de la leucocyte estérase ou des nitrites : 80 % contre 10 exposant 5 UFC/ml, 67 % contre 10 exposant 4, 45 % contre 10 exposant 3.", E),
        ("Bactériurie asymptomatique. Au moins 10 exposant 5 UFC/ml sur un milieu de jet, deux échantillons de suite chez la femme, un seul chez l'homme, sans symptôme urinaire.", U),
        ("On ne dépiste ni ne traite cette bactériurie chez la femme sans facteur de risque, le diabète équilibré, la femme ménopausée, la personne âgée en institution, les vessies reconstruites, le transplanté rénal, avant une prothèse articulaire, ni dans les cystites récidivantes. Recommandation forte.", U),
        ("On dépiste et l'on traite avant un geste urologique qui ouvre la muqueuse. Recommandation forte. Chez la femme enceinte, traitement court ou fosfomycine en dose unique : recommandation faible.", U),
        ("Infection sur sonde. Au moins 10 exposant 3 UFC/ml d'une ou plusieurs espèces, sur un prélèvement de sonde, ou sur un milieu de jet si la sonde a été retirée depuis moins de 48 heures.", U),
        ("Une urine trouble ou malodorante, seule, ne sépare pas la colonisation de l'infection sur sonde.", U),
        ("Pour le milieu de jet symptomatique, la fourchette lue va de 10 exposant 2 à 10 exposant 5 UFC/ml selon les symptômes. On n'applique pas 10 exposant 5 à toutes les dysuries.", E),
        ("Le guide de laboratoire décrit aussi, pour les uropathogènes, une croissance significative dès 10 exposant 3 UFC/ml, lue avec la leucocyturie et le mode de recueil. Le gris de la leucocyturie va de 10 à 30 fois 10 exposant 6 par litre. Au-dessus de 30, la leucocyturie est retenue pour ce flux de travail.", E),
    ])


def doses_cystite():
    return bloc([
        ("Cystite non compliquée. Femme non enceinte, épisode aigu, sporadique ou récidivant, sans anomalie anatomique ou fonctionnelle pertinente et sans comorbidité. Le diagnostic repose sur la dysurie, la pollakiurie et l'urgence, et sur l'absence d'écoulement vaginal. Recommandation forte.", U),
        ("Premier choix européen. Fosfomycine trométamol, pivmécillinam ou nitrofurantoïne. Pas d'aminopénicilline. Pas de fluoroquinolone. Recommandations fortes.", U),
        ("Fosfomycine Sandoz, numéro 66690. Infections urinaires aiguës non compliquées chez les femmes et les adolescentes de plus de 12 ans : 1 sachet de 3 g en dose unique. À jeun, 2 à 3 heures avant ou après le repas, de préférence le soir après avoir vidé la vessie. Les infections urinaires de l'homme sont tenues pour compliquées : ce produit n'y est pas indiqué.", FOS),
        ("Monuril, numéro 49298, porte la même dose unique de 3 g chez la femme et l'adolescente de plus de 12 ans.", MON),
        ("Le tableau européen dit aussi fosfomycine trométamol 3 g en dose unique, un jour.", U),
        ("Nitrofurantoin-Acino 100 retard, numéro 62724. Une capsule contient 100 mg. Adultes, traitement : 1 capsule 2 à 3 fois par jour pendant 7 à 10 jours. Le tableau européen des macrocristaux dit 100 mg deux fois par jour pendant 5 jours. On prescrit le schéma de l'information suisse du produit ouvert, et l'on sait que l'Europe a écrit 5 jours pour une autre forme.", NIT),
        ("Nitrofurantoïne. Contre-indiquée le dernier trimestre, pendant le travail et chez le nourrisson de moins de 3 mois, à cause d'une hémolyse possible. Pas pendant les six premiers mois, sauf nécessité. Déficit en G6PD : contre-indication signalée. L'allaitement est évité si le nourrisson a un déficit enzymatique érythrocytaire.", NIT),
        ("Pivmécillinam. Le tableau 1 de 2024 indique 400 mg trois fois par jour pendant 3 à 5 jours. Aucune spécialité à ce nom n'a été ouverte ici. Ce milligramme est celui du tableau européen.", U),
        ("Bactrim forte, numéro 48306. Un comprimé contient 160 mg de triméthoprime et 800 mg de sulfaméthoxazole. Infections urinaires aiguës sans complications chez la femme : 2 à 3 comprimés en une fois, de préférence le soir après le repas. Ce n'est pas le premier choix du guide européen, à cause de l'écologie des résistances. On ne l'écrit que si le germe est sensible, ou selon le texte suisse lu.", BAC),
        ("Bactrim est contre-indiqué au dernier trimestre. Un test de grossesse est demandé avant de le commencer chez une femme qui peut être enceinte. Le déficit en G6PD expose à une hémolyse.", BAC),
        ("Ciproxine, numéro 47795, liste encore une cystite simple à 2 fois 250 mg jusqu'à 2 fois 500 mg pendant 3 jours, et 500 mg en dose unique chez la femme non ménopausée. Le guide européen de 2024 dit de ne pas utiliser les fluoroquinolones dans la cystite non compliquée. On suit cette recommandation forte. On ne recopie pas la cystite simple de Ciproxine comme un premier choix.", CIP),
        ("Pyélonéphrite. Ni nitrofurantoïne, ni fosfomycine orale, ni pivmécillinam. Recommandation forte. Ciproxine, pyélonéphrite simple : 2 fois 500 mg pendant 7 jours. Pyélonéphrite compliquée : 2 fois 500 mg à 2 fois 750 mg, au moins 10 jours.", U),
        ("Ciprofloxacine. Le texte suisse dit de ne pas l'administrer à la femme enceinte ni à celle qui allaite, en attente de données supplémentaires. Elle passe dans le lait à des concentrations proches du sérum.", CIP),
    ])


def doses_rein():
    return bloc([
        ("Ramipril Zentiva, numéro 58159. Indication lue : néphropathie glomérulaire avec protéinurie supérieure à 3 g/jour. Départ 1,25 mg une fois par jour. On double selon la tolérance en 2 à 3 semaines. Maximum 5 mg par jour dans cette rubrique. On ne transporte pas ici le maximum de 10 mg écrit pour d'autres indications.", RAM),
        ("Prednisone Streuli, numéro 29349. La posologie initiale habituelle est de 5 à 60 mg par jour. Le texte ne nomme pas la néphrite interstitielle aiguë. Si un spécialiste reste dans cette fourchette, il ne dépasse pas la phrase lue. On n'invente pas un milligramme par kilogramme.", PRE),
        ("Allopurinol Zentiva, numéro 56050. Début bas, par exemple 100 mg par jour. Cas légers : 100 à 200 mg par jour. Cas modérés : 300 à 600 mg par jour. Cas sévères : 700 à 900 mg par jour. Enfant de moins de 15 ans : 10 à 20 mg/kg/jour, maximum 400 mg par jour. Rein sévère : parfois moins de 100 mg par jour. Cette posologie est celle de l'hyperuricémie lue, pas un protocole séparé de lithiase.", ALL),
        ("Tamsulosine Sandoz eco, numéro 62112. Une capsule retard contient 0,4 mg. Indication lue : symptômes de l'hyperplasie bénigne de la prostate. 1 capsule par jour, après le petit-déjeuner, avalée entière, debout ou assis. Pas d'indication pédiatrique. Insuffisance hépatique sévère : contre-indication.", TAM),
    ])


SVG = """
<figure>
<svg viewBox="0 0 680 460" role="img" aria-labelledby="titre-sed leg-sed">
<title id="titre-sed">Schéma du sédiment urinaire</title>
<desc id="leg-sed">Cinq cylindres et quatre cristaux, dessin didactique, pas une photographie.</desc>
<rect x="8" y="8" width="664" height="444" rx="16" fill="#f4fbff" stroke="#176fa0" stroke-width="2"/>
<text x="24" y="36" fill="#14303b" font-size="18" font-family="Atkinson Hyperlegible, Verdana, sans-serif">Champ de microscope, schéma</text>
<g>
<rect x="40" y="70" width="36" height="120" rx="18" fill="#f6c1c4" stroke="#a1262f" stroke-width="2"/>
<circle cx="52" cy="100" r="6" fill="#a1262f"/><circle cx="64" cy="118" r="6" fill="#a1262f"/>
<circle cx="52" cy="136" r="6" fill="#a1262f"/><circle cx="64" cy="154" r="6" fill="#a1262f"/>
<text x="40" y="210" fill="#14303b" font-size="13">Cylindre hématique</text>
</g>
<g>
<rect x="180" y="70" width="36" height="120" rx="18" fill="#d9ecff" stroke="#176fa0" stroke-width="2"/>
<circle cx="192" cy="104" r="7" fill="#4f7ea8"/><circle cx="204" cy="128" r="7" fill="#4f7ea8"/>
<circle cx="192" cy="152" r="7" fill="#4f7ea8"/>
<text x="170" y="210" fill="#14303b" font-size="13">Cylindre leucocytaire</text>
</g>
<g>
<rect x="330" y="70" width="40" height="120" rx="18" fill="#8a5a32" stroke="#4a2e16" stroke-width="2"/>
<text x="300" y="210" fill="#14303b" font-size="13">Granuleux brun boueux</text>
</g>
<g>
<rect x="470" y="78" width="48" height="100" rx="6" fill="#f7f1e4" stroke="#8a7040" stroke-width="3"/>
<text x="450" y="210" fill="#14303b" font-size="13">Cylindre cireux</text>
</g>
<g>
<rect x="590" y="70" width="36" height="120" rx="18" fill="#fff6d8" stroke="#c4a035" stroke-width="2"/>
<path d="M600 108 h16 M608 100 v16" fill="none" stroke="#8a7040" stroke-width="1.6"/>
<path d="M600 142 h16 M608 134 v16" fill="none" stroke="#8a7040" stroke-width="1.6"/>
<text x="548" y="206" fill="#14303b" font-size="12">Graisseux</text>
<text x="536" y="222" fill="#14303b" font-size="12">croix de Malte</text>
</g>
<g transform="translate(70,300)">
<path d="M40 20 L70 50 L40 80 L10 50 Z" fill="none" stroke="#176fa0" stroke-width="2"/>
<text x="0" y="110" fill="#14303b" font-size="13">Oxalate, enveloppe</text>
</g>
<g transform="translate(220,300)">
<polygon points="40,10 70,28 70,64 40,82 10,64 10,28" fill="none" stroke="#1a7a50" stroke-width="2"/>
<text x="0" y="110" fill="#14303b" font-size="13">Cystine hexagonale</text>
</g>
<g transform="translate(380,300)">
<polygon points="20,70 30,20 80,20 90,40 70,70" fill="none" stroke="#4f5f66" stroke-width="2"/>
<text x="0" y="110" fill="#14303b" font-size="13">Struvite, couvercle</text>
</g>
<g transform="translate(530,300)">
<rect x="20" y="30" width="36" height="28" transform="rotate(20 38 44)" fill="none" stroke="#a1262f" stroke-width="2"/>
<text x="0" y="110" fill="#14303b" font-size="13">Urate, losange ambre</text>
</g>
</svg>
<figcaption>Schéma didactique. Ce n'est pas une lame. Les couleurs séparent les éléments. La croix de Malte se confirme en lumière polarisée.</figcaption>
</figure>
"""


DXS = [
    {
        "n": 1,
        "nom": "Cystite aiguë non compliquée",
        "gravite": "fréquente, rarement grave si elle reste basse",
        "definition": "Infection limitée à la vessie, chez une femme non enceinte, sans anomalie de l'arbre urinaire et sans signe de rein.",
        "voir": "leucocytes, parfois hématies isomorphes, germes, nitrites si le germe réduit le nitrate",
        "pas": "cylindre leucocytaire, fièvre, douleur lombaire, homme, grossesse, sonde",
    },
    {
        "n": 2,
        "nom": "Hématurie microscopique d'origine urologique",
        "gravite": "le cancer urothélial est la gravité qui organise le bilan",
        "definition": "Au moins 3 hématies par champ, en majorité isomorphes, sans argument glomérulaire.",
        "voir": "hématies intactes, parfois caillot, peu ou pas de protéine, pas d'acanthocyte à 5 %",
        "pas": "cylindre hématique, acanthocytes à 5 % ou plus, protéinurie néphrotique",
    },
    {
        "n": 3,
        "nom": "Hématurie glomérulaire",
        "gravite": "une glomérulonéphrite rapidement progressive est une urgence",
        "definition": "Saignement glomérulaire lu sur les acanthocytes, les cylindres hématiques, souvent avec protéine et créatinine.",
        "voir": "acanthocytes au moins 5 %, cylindre hématique, protéine, tension élevée",
        "pas": "caillot, hématies seulement isomorphes avec un facteur de risque urologique ignoré",
    },
    {
        "n": 4,
        "nom": "Pyélonéphrite aiguë",
        "gravite": "sepsis possible, le rein est déjà atteint",
        "definition": "Infection du haut appareil, fièvre ou douleur de la loge, avec leucocyturie et souvent un germe.",
        "voir": "leucocytes nombreux, cylindre leucocytaire possible, nitrites inconstants, hématies parfois",
        "pas": "nitrofurantoïne, fosfomycine orale, pivmécillinam",
    },
    {
        "n": 5,
        "nom": "Cristallurie lithogène",
        "gravite": "la colique et l'obstacle priment sur le cristal",
        "definition": "Cristaux dont la forme et le pH orientent vers un calcul : oxalate, urate, cystine, struvite.",
        "voir": "enveloppe, losange ambre, hexagone, couvercle de cercueil",
        "pas": "cristal apparu seulement après deux heures au frigo, sans symptôme",
    },
    {
        "n": 6,
        "nom": "Néphrite interstitielle aiguë",
        "gravite": "la créatinine peut monter vite après un médicament",
        "definition": "Inflammation interstitielle, souvent médicamenteuse, avec leucocyturie, parfois cylindre leucocytaire, éosinophilurie peu décisive.",
        "voir": "leucocytes, cylindre leucocytaire, parfois hématies, médicament nouveau",
        "pas": "décider sur 1 % d'éosinophiles urinaires",
    },
    {
        "n": 7,
        "nom": "Nécrose tubulaire aiguë",
        "gravite": "insuffisance rénale aiguë hospitalière",
        "definition": "Lésion tubulaire avec cellules épithéliales, cylindres granuleux, dont le brun boueux.",
        "voir": "cylindres granuleux brun boueux, cellules tubulaires, peu d'hématies glomérulaires",
        "pas": "rassurer sur quelques cylindres hyalins après un jeûne",
    },
    {
        "n": 8,
        "nom": "Syndrome néphrotique",
        "gravite": "thrombose, infection et perte de protéine",
        "definition": "Protéinurie au-dessus de 3,5 grammes par jour et albumine sous 30 g/l, souvent avec œdème. Le sédiment montre la graisse.",
        "voir": "croix de Malte, corps ovalaires gras, cylindre graisseux, bandelette protéique forte",
        "pas": "chercher un cancer de vessie sur la seule mousse des urines",
    },
    {
        "n": 9,
        "nom": "Myoglobinurie et hémoglobinurie",
        "gravite": "le muscle ou l'hémolyse, puis le rein",
        "definition": "Bandelette sanguine positive et microscopie sans hématies à la hauteur de la plage.",
        "voir": "surnageant rouge ou brun, peu d'hématies, cylindre pigmenté possible",
        "pas": "conclure à une hématurie urologique et envoyer en cystoscopie",
    },
    {
        "n": 10,
        "nom": "Cristallurie médicamenteuse",
        "gravite": "obstacle et insuffisance rénale aiguë par les cristaux",
        "definition": "Cristaux d'un médicament, souvent aiguilles ou gerbes, chez un patient qui le prend.",
        "voir": "sulfadiazine, aciclovir, ciprofloxacine, amoxicilline, méthotrexate, triamtérène, atazanavir",
        "pas": "appeler cystine une aiguille de médicament",
    },
]


def ile(nom, a, b):
    return [
        f"{nom}. {a}",
        b,
        "Le détail chiffré est dans la fenêtre.",
    ]


def narrer(dx):
    nom = dx["nom"]
    out = {n: [] for n in range(1, 15)}
    out[1] += [
        (f"{nom} se définit ainsi. {dx['definition']}", None),
        (f"Ce que l'on voit. {dx['voir']}.", None),
        (f"Ce que ce n'est pas. {dx['pas']}.", None),
        ("Le sédiment est la microscopie des éléments figurés. La bandelette ne le remplace pas.", A),
        ("On rend les hématies par champ, ou en particules par litre. Un mot vague, rare ou quelques, ne se compare pas au seuil de 3.", A),
    ]
    out[2] += [
        (f"Aucune source suisse lue ne donne la part de {nom} dans le pays. On n'écrit pas un pourcentage national.", None),
        (f"La place dans la leçon vient du tableau clinique, pas d'un registre. Gravité utile : {dx['gravite']}.", None),
        ("La fréquence ne descend pas un cylindre hématique ni une fièvre avec douleur lombaire.", None),
    ]
    out[3] += [
        ("L'uromoduline forme la matrice des cylindres dans le tubule distal et le canal collecteur.", E),
        (f"Pour {nom}, le mécanisme utile est celui qui relie l'élément vu au tissu. {dx['voir']}.", None),
        ("Le pH et le délai avant lecture changent les cristaux et les cylindres. Une urine laissée plus de deux heures fait précipiter l'urate même chez un sujet sain.", C),
        ("Les hématies deviennent dysmorphiques en traversant le glomérule et le tubule. Les hématies de la voie sont en général isomorphes.", E),
    ]
    out[4] += [
        ("Étape une. Fièvre, frisson, douleur lombaire, rétention, grossesse, homme, sonde. Ces faits passent avant le classement fin.", None),
        ("Étape deux. Bandelette : sang, leucocyte estérase, nitrites, protéine, pH, densité.", E),
        ("Étape trois. Si la plage sang est positive, microscopie. Au moins 3 hématies par champ définissent l'hématurie microscopique.", A),
        ("Étape quatre. Séparer glomérule et voie : acanthocytes, cylindre hématique, protéine, créatinine, tension.", K),
        ("Étape cinq. Culture lue avec le contexte. 10 exposant 5 n'est pas le seul seuil.", U),
        (f"Étape six, propre à {nom}. {dx['definition']}", None),
    ]
    out[5] += [
        ("On demande les médicaments des deux dernières semaines, les AINS, les antibiotiques, le cyclophosphamide, l'ifosfamide.", A),
        ("On demande le tabac en paquets-années, les métiers des colorants et du caoutchouc, une radiothérapie pelvienne, un syndrome de Lynch.", A),
        ("Règles, effort du jour, sonde, calcul connu, douleur musculaire, urine rouge après un effort ou un écrasement.", A),
        ("Un anticoagulant ne clôt pas le bilan.", A),
        (f"Drapeau propre à {nom} : {dx['pas']}.", None),
    ]
    out[6] += [
        ("Tension, œdèmes, loge rénale, globe, couleur de l'urine. Chez la femme, un saignement gynécologique se cherche avant d'appeler cela une hématurie.", A),
        ("Le toucher rectal n'est pas le premier geste d'une cystite de la femme jeune. Il l'est chez l'homme avec une bactériurie, selon le guide des infections.", U),
        (f"Examen orienté. {dx['voir']}.", None),
    ]
    out[7] += [
        ("Cinq images utiles. Infection basse. Infection du rein. Hématurie de la voie. Hématurie glomérulaire. Atteinte tubulaire ou graisseuse ou cristalline.", None),
        (f"{nom} occupe cette place. {dx['definition']}", None),
        ("Le syndrome néphritique associe hématies, souvent cylindres, protéine, tension, et baisse du débit. Le syndrome néphrotique est une protéinurie au-dessus de 3,5 grammes par jour plus une albumine sous 30 g/l.", G),
        ("On ne classe pas un cylindre cireux comme un cylindre hématique, ni une croix de Malte comme un cristal de cystine.", E),
    ]
    out[8] += [
        (f"Le diagnostic positif de {nom} exige l'élément et le contexte. {dx['voir']}.", None),
        ("Acanthocytes d'au moins 5 % : sensibilité 52 %, spécificité 98 % pour le saignement glomérulaire dans l'étude de 1991.", K),
        ("Hématies dysmorphiques au-dessus de 5 % : phrase du curriculum de 2019, distincte du seuil des acanthocytes.", C),
        ("Au moins 3 hématies par champ : définition urologique de 2025, un seul recueil.", A),
        ("Leucocytes à 10 par microlitre seulement si l'urine est concentrée.", E),
    ]
    out[9] += [
        ("Recueil du milieu de jet. On jette le premier jet. On regarde la densité. Sous 1,015, ou sous 300 mOsm/kg, un compte de leucocytes bas peut être un faux négatif.", E),
        ("Contraste de phase pour les hématies et les cylindres hyalins. Lumière polarisée pour les lipides et les cristaux. Fond clair pour la forme tridimensionnelle des cristaux.", E),
        ("Niveau de base : hématies, leucocytes, cellules épithéliales, cylindres hyalins ou non. Niveau avancé : acanthocytes, cylindres hématiques, leucocytaires, cireux, graisseux, cystine, cristaux de médicaments.", E),
        (f"Pour {nom}, l'examen qui tranche est celui qui montre {dx['voir']}.", None),
    ]
    out[10] += [
        ("Branche immédiate. Sepsis, obstacle, anurie, douleur musculaire avec urine brun foncé, créatinine qui monte le jour même.", None),
        ("Branche glomérulaire. Acanthocytes, cylindre hématique, protéine, créatinine. Avis de néphrologie, et le bilan urologique selon le risque continue.", A),
        ("Branche de la voie. Hématies isomorphes, au moins 3 par champ. Tableau de risque 2025, complet, pas une ligne d'âge seule.", A),
        ("Branche infectieuse. Symptômes bas sans fièvre : cystite possible. Fièvre ou loge : pyélonéphrite. Sonde : seuil à 10 exposant 3, pas l'odeur.", U),
        (f"Branche de {nom}. {dx['definition']}", None),
    ]
    out[11] += [
        ("Les milligrammes écrits plus loin sont ceux des informations suisses ou, pour le pivmécillinam, du tableau européen de 2024.", U),
        (f"Conduite de {nom}. On retire d'abord le geste qui aggrave : médicament suspect, obstacle, déshydratation, fluoroquinolone d'une cystite simple.", None),
        ("Fosfomycine Sandoz 3 g, une fois, femme ou adolescente de plus de 12 ans, cystite non compliquée. Numéro 66690.", FOS),
        ("Nitrofurantoïne, capsule de 100 mg, 2 à 3 fois par jour, 7 à 10 jours, numéro 62724, hors dernier trimestre.", NIT),
        ("Ciproxine, pyélonéphrite simple, 2 fois 500 mg, 7 jours, numéro 47795. Pas pour la cystite non compliquée, selon l'EAU 2024.", CIP),
        ("Ramipril, néphropathie avec protéinurie supérieure à 3 g/jour : départ 1,25 mg, maximum 5 mg, numéro 58159.", RAM),
        ("Prednisone Streuli, fourchette habituelle 5 à 60 mg par jour, numéro 29349. La néphrite interstitielle n'est pas nommée dans ce texte.", PRE),
    ]
    out[12] += [
        ("On ne traite pas une bactériurie asymptomatique hors des deux indications fortes ou faibles déjà citées.", U),
        ("Après une infection tenue pour la cause d'une hématurie, on recontrôle le microscope. Pas avant trois semaines, pas après trois mois, selon le texte lu.", A),
        ("Boire assez pour une densité qui se lit. Un grand verre juste avant le recueil dilue les leucocytes.", E),
        (f"Prévention utile autour de {nom} : ne pas répéter un antibiotique qui ne couvre pas le rein, et ne pas ignorer un médicament nouveau devant une créatinine qui monte.", None),
    ]
    out[13] += [
        ("Au moins 3 hématies par champ. Acanthocytes au moins 5 %. Hématies dysmorphiques au-dessus de 5 %, phrase distincte. Cylindre hématique. Cylindre leucocytaire. Brun boueux. Cireux. Graisseux. Croix de Malte.", A),
        ("Leucocytes 10 par microlitre si l'urine est concentrée. Bactéries 10 exposant 5 en asymptomatique, 10 exposant 3 sur sonde, fourchette 10 exposant 2 à 10 exposant 5 si la patiente est symptomatique.", E),
        ("Cristaux : oxalate, urate, cystine hexagonale, struvite en couvercle, et cristaux de médicaments. pH acide pour l'urate, pH plus haut pour la struvite.", C),
        ("Éosinophilurie : 30,8 % de sensibilité et 68,2 % de spécificité au seuil de 1 %. Elle ne déplace pas la probabilité.", M),
        (f"Pour {nom}, la phrase à retenir est : {dx['definition']}", None),
    ]
    out[14] += [
        (f"Piège propre. Traiter {nom} avec le geste de son voisin. {dx['pas']}.", None),
        ("Piège de la bandelette. Sang positif et zéro hématie : myoglobine ou hémoglobine, pas une cystoscopie d'emblée.", A),
        ("Piège des nitrites négatifs. Ils n'écartent pas l'entérocoque ni une vessie vidée trop souvent.", E),
        ("Piège du pH. Un urate lu dans une urine à 7 n'est pas un urate. Une struvite en urine très acide se rediscute.", C),
        ("Piège de l'anticoagulant. Il ne dispense pas du tableau de risque.", A),
    ]
    return out


def cas_specifiques(dx):
    n = dx["n"]
    items = []
    if n == 1:
        items += cas(
            "Femme de 24 ans, dysurie et pollakiurie depuis hier, pas de fièvre, pas d'écoulement",
            "leucocyte estérase positive, nitrites positifs, 8 hématies par champ, pas de cylindre",
            "La clinique et l'absence de signe haut permettent la cystite non compliquée. Huit hématies ne lancent pas le bilan de cancer le jour même. On recontrôlera le microscope après traitement, entre trois semaines et trois mois.",
            "Fosfomycine Sandoz, numéro 66690, un sachet de 3 g, une fois, le soir à jeun après la miction.",
            "ciprofloxacine pour une cystite simple, ou une cystoscopie le jour même.",
            U,
        )
        items += cas(
            "Femme de 24 ans, enceinte de 8 semaines, mêmes brûlures",
            "leucocytes, culture en attente",
            "Ce n'est plus la cystite non compliquée du tableau. La nitrofurantoïne n'est pas le réflexe du dernier trimestre, et les six premiers mois ne sont pas une indication automatique.",
            "On choisit un produit dont la grossesse a été lue. La fosfomycine ne s'utilise que si c'est vraiment nécessaire, phrase du texte 66690.",
            "le schéma de 7 à 10 jours de nitrofurantoïne sans lire le trimestre.",
            NIT,
        )
        items += cas(
            "Homme de 46 ans, dysurie, leucocyturie",
            "nitrites positifs",
            "L'information de la fosfomycine dit que l'infection de l'homme est compliquée et que le sachet de 3 g n'est pas indiqué.",
            "Culture, examen, pas le sachet unique.",
            "le même sachet que chez la femme de 24 ans.",
            FOS,
        )
    elif n == 2:
        grille = [
            ("Femme de 48 ans, jamais fumé, 6 hématies par champ, aucun facteur ajouté", "faible ou négligeable", "contrôle dans les six mois, sans cystoscopie immédiate"),
            ("Femme de 62 ans, jamais fumé, 6 hématies par champ", "intermédiaire, parce que 60 ans ou plus, pas élevée sur l'âge seul", "bilan intermédiaire, pas la colonne élevée"),
            ("Homme de 62 ans, jamais fumé, 4 hématies par champ", "élevé, homme de 60 ans ou plus", "cystoscopie et imagerie selon la colonne élevée"),
            ("Homme de 45 ans, 20 paquets-années, 8 hématies", "intermédiaire, tabac entre 10 et 30", "on ne le met pas en faible"),
            ("Homme de 45 ans, 40 paquets-années, 8 hématies", "élevé, plus de 30 paquets-années", "la colonne élevée s'applique"),
            ("Femme de 50 ans, 4 hématies, radiothérapie pelvienne", "intermédiaire, un facteur ajouté", "l'âge sous 60 ne l'efface pas"),
            ("Homme de 50 ans, 30 hématies par champ, non fumeur", "élevé, plus de 25 hématies", "l'abondance suffit"),
            ("Femme de 40 ans, 8 hématies aujourd'hui, hématurie macroscopique il y a un an", "élevé, antécédent macroscopique", "on ne repart pas de zéro"),
            ("Femme de 55 ans, sous aspirine, 12 hématies, non fumeuse", "intermédiaire par le nombre 11 à 25, l'aspirine ne change pas la colonne", "même bilan que sans aspirine"),
            ("Homme de 38 ans, 5 hématies, père avec un cancer de vessie", "intermédiaire, facteur familial", "pas la colonne faible"),
            ("Femme de 70 ans, 4 hématies, syndrome de Lynch", "imagerie haute quel que soit le reste, et l'âge la met déjà en intermédiaire", "on n'omet pas la voie excrétrice"),
            ("Femme de 30 ans, 40 hématies le jour des règles, cathéterisme propre ensuite à 0", "sang gynécologique, pas une hématurie microscopique confirmée", "on ne lance pas le tableau de risque sur le premier pot"),
        ]
        for qui, cat, geste in grille:
            items += cas(qui, "hématies isomorphes, protéine absente, pas de cylindre", f"Catégorie 2025 : {cat}.", geste, "une seule ligne d'âge pour tout le monde, ou un bilan annulé par l'aspirine.", A)
    elif n == 3:
        items += cas(
            "Femme de 28 ans, tension 150/95 mmHg, créatinine qui monte, protéine à la bandelette",
            "12 % d'acanthocytes, un cylindre hématique",
            "12 % est au-dessus de 5 %. La spécificité lue est 98 %, la sensibilité seulement 52 %. L'absence d'acanthocyte n'aurait pas écarté le glomérule. Ici ils sont là, avec le cylindre.",
            "Néphrologie le jour même. Le bilan urologique selon le risque n'est pas barré, mais il ne retarde pas le rein.",
            "cystoscopie seule, ou un pourcentage de dysmorphie floue à 40 % sans regarder les acanthocytes.",
            K,
        )
        items += cas(
            "Homme de 60 ans, fumeur, 20 hématies isomorphes, acanthocytes à 1 %, protéine négative",
            "voie urinaire probable, et l'âge plus le tabac ouvrent la colonne de risque",
            "1 % d'acanthocytes est sous 5 %. Köhler voyait moins de 2 % hors glomérule. On n'appelle pas cela une hématurie glomérulaire. On ne ferme pas non plus la voie.",
            "Tableau urologique complet. Créatinine et tension quand même, phrase du guide.",
            "un avis de néphrologie qui annule la cystoscopie chez ce fumeur.",
            A,
        )
    elif n == 4:
        items += cas(
            "Femme de 32 ans, fièvre 39 °C, douleur de la loge droite, nausée",
            "leucocytes au-dessus de 10 par microlitre, urine concentrée, nitrites négatifs, pas de cylindre certain",
            "La clinique est celle du haut appareil. Des nitrites négatifs n'écartent pas le diagnostic. Un cylindre leucocytaire, s'il était là, soutiendrait le rein. Son absence ne l'écarte pas.",
            "Ciproxine, numéro 47795, pyélonéphrite simple : 2 fois 500 mg pendant 7 jours, si la voie orale est possible et la grossesse écartée. Pas de nitrofurantoïne.",
            "un sachet de fosfomycine 3 g, ou 100 mg de nitrofurantoïne.",
            CIP,
        )
        items += cas(
            "Femme enceinte, fièvre et douleur lombaire",
            "leucocyturie",
            "Ciproxine dit de ne pas traiter la femme enceinte. La nitrofurantoïne ne traite pas la pyélonéphrite.",
            "Avis hospitalier, produit dont la grossesse a été relue, pas le comprimé de 500 mg par automatisme.",
            "2 fois 500 mg quand même.",
            CIP,
        )
    elif n == 5:
        items += cas(
            "Homme de 45 ans, colique droite, urine à pH 5,5",
            "losanges ambre, biréfringents",
            "Acide urique. Le pH lu pour ce cristal va de 5,4 à 5,8, et le guide de laboratoire dit une précipitation seulement sous 5,8. Le couvercle de struvite n'est pas dans cette zone.",
            "Antalgie, imagerie si l'obstacle est douteux, alcalinisation sans gramme inventé. Allopurinol seulement si l'hyperuricémie est l'indication lue, départ par exemple 100 mg, numéro 56050.",
            "un pH à 7 appelé urique, ou une dose de citrate qui n'a pas été lue.",
            C,
        )
        items += cas(
            "Enfant, urine à pH 5,5, plaques hexagonales",
            "cystine, biréfringence faible",
            "La cystine est hexagonale, bords irréguliers. On confirme par les acides aminés. On ne la confond pas avec l'urate à six côtés, qui est ambre.",
            "Avis spécialisé. Pas de milligramme de tiopronine, produit non ouvert.",
            "un traitement au hasard en milligrammes.",
            E,
        )
        items += cas(
            "Femme, infection à Proteus, pH 7, prismes en couvercle",
            "struvite, phosphate ammoniaco-magnésien",
            "Le germe uréasique alcalinise. Le calcul infectieux se cherche. La bactériurie à Proteus persistante fait chercher un calcul, phrase du guide des infections.",
            "Traiter l'infection selon le germe et chercher le calcul. Pas un oxalate.",
            "une enveloppe d'oxalate pour décrire un couvercle.",
            U,
        )
    elif n == 6:
        items += cas(
            "Femme de 70 ans, AINS depuis dix jours, créatinine multipliée par deux, éruption discrète",
            "leucocyturie, un cylindre leucocytaire, éosinophiles urinaires à 2 %",
            "Au seuil de 1 %, sensibilité 30,8 % et spécificité 68,2 %. Le rapport de vraisemblance positif est 0,97. Deux pour cent ne prouvent pas la néphrite, et zéro pour cent ne l'écarte pas. Le cylindre leucocytaire et le médicament pèsent plus.",
            "Arrêt de l'AINS. Prednisone Streuli reste dans 5 à 60 mg par jour si l'on s'en tient à la fourchette habituelle, numéro 29349. La maladie n'est pas nommée dans l'information.",
            "une biopsie évitée parce que les éosinophiles sont positifs, ou un traitement poursuivi parce qu'ils sont négatifs.",
            M,
        )
    elif n == 7:
        items += cas(
            "Homme de 78 ans, sepsis, créatinine de 80 à 240 µmol/l en deux jours, tension basse hier",
            "nombreux cylindres granuleux brun boueux, cellules tubulaires, rares cylindres hyalins",
            "Le curriculum nomme muddy brown ces cylindres denses brun terre brûlée. L'étude de 2008 décrit le même sédiment dans la nécrose tubulaire, et des hyalins ou granuleux fins dans la forme prérénale. Quand le clinicien pensait déjà à la nécrose et que des cylindres granuleux ou des cellules tubulaires étaient là, la valeur prédictive positive lue était 100 %, avec une valeur prédictive négative de 44 %.",
            "Remplissage prudent, arrêt des toxiques, pas de biopsie pour un tableau déjà clair. On ne cite pas une grille de score dont le tableau récupéré était incomplet.",
            "un score chiffré inventé case par case, ou une cystoscopie.",
            P,
        )
        items += cas(
            "Même homme, mais créatinine qui revient en 24 heures après deux litres, sédiment pauvre",
            "quelques cylindres hyalins, pas de cellule tubulaire",
            "Si l'on pensait à une cause prérénale et que cylindres granuleux et cellules tubulaires manquent, la valeur prédictive négative lue pour la nécrose était 91 %, sensibilité 0,73, spécificité 0,75.",
            "On surveille. On ne grave pas nécrose tubulaire sur un hyalin isolé.",
            "le mot brun boueux sans l'avoir vu.",
            P,
        )
    elif n == 8:
        items += cas(
            "Homme de 40 ans, œdèmes des jambes, urine mousseuse",
            "protéine forte, croix de Malte en lumière polarisée, cylindre graisseux, albumine basse",
            "KDIGO 2021 : syndrome néphrotique si protéinurie au-dessus de 3,5 grammes par jour et albumine sous 30 g/l. L'œdème et les lipides sont fréquents, pas obligatoires dans la phrase lue. La croix de Malte vient des esters de cholestérol.",
            "Ramipril Zentiva, numéro 58159, si la protéinurie dépasse 3 g/jour dans le cadre de la néphropathie glomérulaire : départ 1,25 mg, maximum 5 mg. Ponction selon le néphrologue. Bandes de contention et lever progressif ne remplacent pas la cause.",
            "un maximum de 10 mg copié depuis l'hypertension, ou une cystoscopie pour la mousse.",
            G,
        )
    elif n == 9:
        items += cas(
            "Homme de 25 ans, après un écrasement, urines brun foncé, muscles douloureux",
            "bandelette sanguine positive, moins de 3 hématies par champ, surnageant coloré",
            "La myoglobine donne la plage sang sans hématies. L'hémoglobine libre fait de même dans l'hémolyse. Les cylindres pigmentés ne séparent pas les deux. Ce n'est pas le seuil de 3, donc ce n'est pas le bilan de cancer.",
            "Remplissage, surveillance de la créatinine et du potassium, recherche de la cause musculaire ou hémolytique. Pas de Fosfomycine.",
            "une cystoscopie pour hématurie microscopique alors que le compte est sous 3.",
            A,
        )
    elif n == 10:
        items += cas(
            "Femme traitée par amoxicilline à forte dose, douleur lombaire, créatinine qui monte",
            "aiguilles en balai, pH 6, biréfringence forte",
            "Le curriculum place l'amoxicilline à pH 5,5 à 6,5, aiguilles en balai. La ciprofloxacine est plutôt au-dessus de 7. La cystine est une plaque hexagonale, pas une aiguille.",
            "Arrêt ou adaptation du médicament, hydratation, avis si l'obstacle ou la créatinine l'exigent. Pas d'allopurinol pour une aiguille d'antibiotique.",
            "un hexagone de cystine, ou un traitement de lithiase urique.",
            C,
        )
        items += cas(
            "Patient sous aciclovir intraveineux, insuffisance rénale aiguë",
            "aiguilles biréfringentes, pH 6",
            "L'aciclovir est en aiguilles, pH 5,5 à 7. On le distingue de la sulfadiazine en gerbe de blé et du méthotrexate jaune-brun.",
            "Hydratation et révision de la dose avec le prescripteur. Le sédiment date le lien.",
            "une pyélonéphrite traitée par une fluoroquinolone sans regarder le médicament déjà en cours.",
            C,
        )
    return items


def corps_dx(dx):
    base = narrer(dx)
    extra = cas_specifiques(dx)
    # répartir les cas longs sur les points 4, 8, 10, 11, 14
    chunks = {4: [], 8: [], 10: [], 11: [], 14: []}
    keys = [4, 8, 10, 11, 14]
    for i, item in enumerate(extra):
        chunks[keys[i % 5]].append(item)
    html = {}
    for n in range(1, 15):
        items = list(base[n]) + chunks.get(n, [])
        morceaux = [bloc(items)]
        if n in (8, 13):
            morceaux.append(seuils_hematurie())
            morceaux.append(seuils_infection())
        if n == 6 and dx["n"] in (5, 10):
            morceaux.append(SVG)
        if n == 7 and dx["n"] in (3, 7, 8):
            morceaux.append(atlas_cylindres())
        if n == 10 and dx["n"] == 2:
            morceaux.append(aua_table())
            morceaux.append(facteurs_ajoutes())
        if n == 9 and dx["n"] in (5, 10):
            morceaux.append(cristaux_table())
        if n == 11 and dx["n"] in (1, 4):
            morceaux.append(doses_cystite())
        if n == 11 and dx["n"] in (6, 8):
            morceaux.append(doses_rein())
        if n == 3:
            morceaux.append(atlas_cylindres() if dx["n"] in (7, 8, 3) else "")
        html[n] = "".join(morceaux)
    # compléter les fenêtres courtes par la lecture comparée, propre au nom
    for n in range(1, 15):
        html[n] += bloc([
            (f"Lecture comparée pour {dx['nom']}. On écrit l'élément vu, le seuil qui s'applique, et le geste. On n'écrit pas le diagnostic voisin.", None),
            (f"Voisin exclu. {dx['pas']}.", None),
            (f"Phrase de fin de point. {dx['definition']}", None),
        ])
    html[14] += bonus_dx(dx)
    html[12] += encore(dx)
    return html


def encore(dx):
    nom = dx["nom"]
    n = dx["n"]
    src = {1: U, 2: A, 3: K, 4: U, 5: C, 6: M, 7: P, 8: G, 9: A, 10: C}[n]
    lignes = [
        f"Procédure commune, appliquée à {nom}. Recueil du milieu de jet, premier jet jeté. Pot propre. Acheminement avant deux heures, ou le délai du laboratoire s'il est plus court. On note l'heure.",
        f"Densité ou osmolalité avant d'interpréter un compte de leucocytes bas. Au-dessus de 1,015, ou au-dessus de 300 mOsm/kg, la limite de 10 par microlitre se lit. En dessous, un faux négatif est possible.",
        f"Contraste de phase pour {nom} si l'on cherche un cylindre hyalin, une hématie déformée ou un acanthocyte. Fond clair pour la forme d'un cristal. Lumière polarisée avant d'écrire croix de Malte ou biréfringence.",
        f"On dicte cinq mots : élément, nombre ou pourcentage, pH si cristal, densité si leucocytes, geste. Un adjectif seul, rare ou quelques, ne se compare pas à 3 hématies par champ ni à 5 % d'acanthocytes.",
        f"Voisin de {nom} : {dx['pas']}. On l'écrit en négatif dans la note, pour que le lecteur suivant ne rouvre pas la mauvaise branche.",
        f"Ce que l'on doit voir pour garder {nom} : {dx['voir']}. Si cet élément manque, on change de branche plutôt que de forcer le nom.",
    ]
    # compléments plus longs selon le diagnostic, pour que les tailles ne soient pas identiques
    plus = {
        1: [
            "Femme de 19 ans, premier épisode, rapport récent, brûlures sans fièvre, leucocyte estérase positive, nitrites négatifs, culture à 10 exposant 3 d'Escherichia coli. La clinique suffit à traiter. Le seuil asymptomatique de 10 exposant 5 ne s'applique pas. Fosfomycine 3 g une fois, numéro 66690, si elle n'est pas enceinte.",
            "Femme de 67 ans, sondée hier, urine trouble, apyrétique. L'odeur ne fait pas l'infection. Si l'on cultive, le seuil sur sonde est 10 exposant 3, et seulement s'il y a des signes. Sans signe, on ne traite pas.",
            "Récidive trois fois dans l'année. On ne répète pas le sachet sans chercher un résidu, un rapport, un spermicide, et sans avoir écarté une hématurie qui persiste. Le guide ne fait pas de la prophylaxie au long cours le sujet de cette leçon : nitrofurantoïne au long cours existe dans le texte, 1 capsule 1 à 2 fois par jour pendant des semaines, mais ce n'est pas le traitement de l'épisode aigu.",
        ],
        2: [
            "Homme de 52 ans, 14 hématies, 12 paquets-années, aucun facteur ajouté. Deux critères intermédiaires, l'âge 40 à 59 et le tabac 10 à 30, et le nombre 11 à 25. Un seul suffisait. Il n'est pas élevé : pas plus de 30 paquets-années, pas plus de 25 hématies, pas 60 ans.",
            "Femme de 59 ans, 9 hématies, 8 paquets-années. Tous les critères bas sont réunis, elle a moins de 60 ans. Contrôle dans les six mois. Le lendemain de ses 60 ans, le même sédiment deviendrait intermédiaire. On date l'anniversaire dans la note.",
            "Patient déjà classé faible, sans cystoscopie, contrôle à 4 mois avec 20 hématies. La ligne alternative de la colonne intermédiaire s'applique : auparavant faible, pas de bilan, et 3 à 25 au contrôle. On ne reste pas sur le premier classement.",
        ],
        3: [
            "Deuxième pot le lendemain, acanthocytes à 6 % alors que le premier était à 3 %. Köhler demandait de ne pas se contenter d'une définition floue. Un pot au-dessus de 5 % suffit à orienter. Un pot sous 5 % n'écarte pas, sensibilité 52 %.",
            "Cylindre hématique vu par l'interne, non revu par le senior. On fait revoir la lame avant d'appeler le néphrologue pour ce seul motif, et l'on ne jette pas l'information si le senior confirme. Le guide de laboratoire dit que ce cylindre indique un saignement de parenchyme.",
            "Protéinurie supérieure à 3 g/jour et acanthocytes. On est à la fois dans l'hématurie glomérulaire et dans l'indication de ramipril lue, départ 1,25 mg, maximum 5 mg, numéro 58159, si la néphropathie glomérulaire est retenue. La biopsie ne se décide pas dans cette leçon de sédiment.",
        ],
        4: [
            "Douleur lombaire sans fièvre, leucocyturie, calcul connu. On ne pose pas pyélonéphrite sur la douleur seule. La fièvre ou le syndrome infectieux manque. Le cristal ou l'obstacle peuvent suffire. On cherche quand même une infection sur obstacle si le patient est algique et nauséeux.",
            "Pyélonéphrite simple traitée depuis 48 heures, toujours fébrile. On ne prolonge pas 500 mg sans réévaluer l'obstacle, l'abcès et la sensibilité. Le texte de Ciproxine permet, pour la forme compliquée, au moins 10 jours et parfois plus de 21 jours s'il y a un abcès.",
            "Enfant de 2 ans, fièvre sans point d'appel, leucocyturie. Ce n'est pas la cystite de la femme adulte. Ciproxine chez l'enfant dès 1 an est un médicament de troisième choix, en accord avec le spécialiste, phrase lue. On n'improvise pas la dose adulte.",
        ],
        5: [
            "Deux cristaux dans le même pot : enveloppe et losange ambre, pH 5,6. Les deux sont possibles dans cette zone. On les nomme tous les deux. On ne choisit pas le plus connu.",
            "pH 8, prismes. Struvite ou phosphate, pas urate. On demande le germe. Un Proteus change la suite.",
            "Patient qui apporte le calcul. L'analyse du calcul prime sur le cristal du matin. Le sédiment oriente en attendant. On n'écrit pas la composition définitive sans le laboratoire des calculs.",
            "Hydratation, antalgie, avis urologique si la douleur ne cède pas ou si la fièvre apparaît. Aucun gramme de citrate n'est écrit : le produit n'a pas été ouvert.",
            "Oxalate, urate, cystine, struvite : les quatre se récitent avec leur pH. Oxalate 5,4 à 6,7. Urate 5,4 à 5,8. Cystine autour de 5,5. Struvite 6,2 à 7. Un pH qui ne colle pas fait changer le nom.",
            "Biréfringence forte pour l'urate, l'oxalate monohydraté et la struvite. Faible pour l'oxalate dihydraté et la cystine. On polarise avant de trancher entre une hématie et un monohydrate.",
            "Le calcul rendu part au laboratoire. Le cristal du matin n'est qu'une hypothèse. On l'écrit comme une hypothèse.",
        ],
        6: [
            "Arrêt du médicament, créatinine qui redescend en une semaine, leucocyturie qui s'éclaircit. Le diagnostic clinique tient sans biopsie. On ne rajoute pas une prednisone pour principe.",
            "Créatinine qui continue de monter après l'arrêt, à 48 heures. Là, la biopsie et une dose dans la fourchette habituelle de 5 à 60 mg se discutent avec le néphrologue. On ne sort pas de cette fourchette lue.",
            "Éosinophiles sanguins et urinaires ensemble. Le sang ne remplace pas la lame urinaire, et la lame urinaire ne fait pas le diagnostic. Les deux se notent, aucun ne tranche.",
            "Cylindre leucocytaire plus éruption plus AINS. Trois arguments. C'est plus fort qu'un pourcentage d'éosinophiles. On l'écrit dans cet ordre.",
        ],
        7: [
            "Choc septique, remplissage, noradrénaline, sédiment riche en brun boueux. On traite le sepsis. Le sédiment évite une biopsie et une recherche glomérulaire inutile si le reste colle.",
            "Aminoside en cours, cylindres granuleux qui précèdent la créatinine. L'article de 2008 rappelle cette idée ancienne : les cylindres peuvent monter avant le chiffre. On ne promet pas un délai en jours que le texte des résultats ne chiffre pas pour notre patient.",
            "Urine laissée toute la nuit. Les cylindres se dissocient. Un sédiment négatif le lendemain matin ne lave pas le tableau de la veille. On recommence sur une urine fraîche.",
            "Cylindre cireux et brun boueux ensemble. Chronicité et agression aiguë. Les deux diagnostics coexistent. On ne choisit pas.",
        ],
        8: [
            "Bandelette protéique forte, sédiment avec croix de Malte, albuminémie pas encore revenue. On ne pose le syndrome qu'avec l'albumine sous 30 g/l et la protéinurie au-dessus de 3,5 grammes par jour. En attendant le dosage, on écrit protéinurie abondante et lipides, pas encore le syndrome.",
            "Départ de ramipril 1,25 mg le matin, créatinine et potassium à 7 jours, puis doublement en 2 à 3 semaines si la tolérance le permet, sans dépasser 5 mg. Numéro 58159. Un diurétique de l'anse pour l'œdème ne se dose pas ici : son information n'a pas été ouverte.",
            "Thrombose, infection, dénutrition : complications du syndrome, pas des diagnostics de sédiment. On les cherche. Le microscope ne les montre pas.",
        ],
        9: [
            "Couleur du plasma demandée avant le scanner. Plasma clair et urine foncée orientent vers le muscle. Plasma rose oriente vers l'hémolyse. Le sédiment pauvre en hématies est commun aux deux.",
            "Compte à 0 hématie, bandelette à trois croix. Écart maximal. On ne demande pas une cystoscopie. On demande la créatine kinase ou les signes d'hémolyse selon le contexte, sans inventer un seuil de créatine kinase qui n'est pas dans les textes ouverts.",
            "Après remplissage, la créatinine monte quand même et des cylindres brun boueux apparaissent. La myoglobine a fait une nécrose. On écrit les deux noms, dans l'ordre : pigment, puis tubule.",
            "Effort d'un marathon, urine rouge, 2 hématies par champ, patient qui va bien. Faux positif d'effort cité par le guide. On recontrôle à distance, on ne lance pas le tableau de risque sur ce pot.",
        ],
        10: [
            "Débit de perfusion de l'aciclovir trop rapide, aiguilles, créatinine qui double. On ralentit ou l'on arrête, on hydrate, on recontrôle le sédiment. La dose intraveineuse exacte n'est pas dans les informations orales ouvertes : on ne l'invente pas.",
            "Amoxicilline et pH 5,8, aiguilles en balai. Concordance avec la ligne 5,5 à 6,5. On documente la photo ou le dessin de la lame dans le dossier.",
            "Ciprofloxacine et pH 5,5, aiguilles. Le tableau place ce médicament au-dessus de 7. La discordance empêche de conclure. On cherche un autre cristal, oxalate ou médicament voisin.",
            "Sulfadiazine en gerbe, patient traité pour une toxoplasmose. On hydrate et l'on avertit le prescripteur. On ne change pas pour une fluoroquinolone sans avis.",
            "Triamtérène et croix de Malte sans protéinurie. Ce n'est pas un syndrome néphrotique. C'est la ligne du tableau : sphères, pH 5,5, croix de Malte.",
        ],
    }
    items = [(ligne, E) for ligne in lignes]
    items += [(ligne, src) for ligne in plus[n]]
    items += [(ligne, src) for ligne in suite.get(n, [])]
    return bloc(items)


suite = {
    4: [
        "Femme de 29 ans, retour de voyage, fièvre, douleur lombaire gauche, leucocytes 40 par microlitre, densité 1,018, nitrites positifs, pas de cylindre. On traite comme une pyélonéphrite simple si elle tolère la voie orale et n'est pas enceinte : Ciproxine 2 fois 500 mg, 7 jours, numéro 47795. On prévient qu'une fluoroquinolone n'aurait pas été le choix si la fièvre manquait.",
        "Le même soir, tension basse et marbrures. Ce n'est plus la forme simple. L'hospitalisation passe avant la durée de 7 jours. Le sédiment ne décide pas de la réanimation. Il évite de chercher d'abord un glomérule.",
        "Contrôle à 72 heures, apyrétique, douleur calmée. On ne change pas pour une nitrofurantoïne de relais. Le guide interdit ce relais dans la pyélonéphrite.",
        "Hématies à 15 par champ pendant l'épisode, puis 0 au contrôle du deuxième mois. L'épisode infectieux expliquait le sang. On a respecté la fenêtre de trois semaines à trois mois. On n'ouvre pas le tableau de cancer.",
        "Hématies encore à 12 au contrôle. Là, le tableau de 2025 s'ouvre, indépendamment de l'infection guérie. On ne dit pas que le rein a saigné et que l'histoire est close.",
    ],
    5: [
        "Homme de 33 ans, troisième colique, pH 5,4, losanges ambre et rosettes. Urate. On alcalinise sans écrire un gramme de citrate absent du dossier ouvert. Si l'uricémie est haute et que l'indication d'allopurinol est retenue, départ par exemple 100 mg, numéro 56050, pas 300 mg d'emblée chez un rein qui vient de souffrir.",
        "Femme végétarienne, enveloppes nombreuses, pH 6, pas de douleur. Cristallurie d'oxalate dihydraté possible après un repas riche, chocolat, épinard, amande. Le curriculum dit que ce cristal n'est pas toujours une maladie. On ne pose pas une lithiase sans douleur, sans imagerie, sans calcul rendu.",
        "Haltères après une ingestion d'éthylène glycol, acidose, trou osmolaire. Oxalate monohydraté. L'urgence toxicologique prime. Le sédiment confirme, il ne retarde pas l'antidote dont la dose n'est pas dans cette leçon.",
        "Enfant avec hexagones et un frère atteint. Cystinurie familiale jusqu'à preuve du contraire. Avis spécialisé. Pas de milligramme de chélateur, produit non ouvert.",
        "pH 6,8, couvercle, fièvre, Proteus au précédent ECBU. Calcul infectieux jusqu'à preuve du contraire. Antibiotique selon le germe, pas selon la forme du cristal, et avis urologique.",
    ],
    6: [
        "Homme de 64 ans, pénicilline commencée il y a neuf jours, créatinine de 90 à 280 µmol/l, leucocyturie, un cylindre leucocytaire, éosinophiles urinaires à 0. Le zéro n'écarte pas la néphrite : sensibilité 30,8 % au seuil de 1 %. On arrête l'antibiotique. On ne le remplace pas par une fluoroquinolone réflexe.",
        "Même homme, éosinophiles à 8 %. Spécificité meilleure au seuil de 5 %, 91,2 %, sensibilité encore plus basse, 19,8 %. Huit pour cent renforcent, ils ne dispensent pas de l'arrêt du médicament ni, si la créatinine empire, de la biopsie.",
        "Prednisone discutée. On reste dans 5 à 60 mg par jour, numéro 29349, si le néphrologue retient un corticoïde. La maladie n'est pas nommée dans l'information. On l'écrit ainsi dans la note, pour ne pas faire croire à une indication officielle.",
        "Rash, arthralgies, éosinophilie sanguine, AINS. Le tableau clinique est plus riche que la lame. On date l'introduction de chaque comprimé. Le plus récent est le suspect, pas le traitement pris depuis dix ans.",
        "Cylindre hématique isolé, sans protéine, sans acanthocyte, avec un médicament nouveau. On n'exclut pas la néphrite interstitielle, le curriculum ayant rappelé des cylindres hématiques sans glomérule à la biopsie. On n'exclut pas non plus une glomérulonéphrite. Les deux restent ouverts.",
    ],
    9: [
        "Jeune homme, festival, danse toute la nuit, urines marron au matin, bandelette sang positive, 0 hématie au microscope, muscles douloureux, plasma clair. Myoglobine d'effort. Remplissage, créatinine, potassium. Pas de tableau de cancer. Pas de fosfomycine.",
        "Femme transfusée, frissons, plasma rose, urine rouge, 1 hématie par champ. Hémoglobinurie. Le sédiment ressemble à celui de la myoglobine. Le plasma les sépare. On traite la réaction, pas la vessie.",
        "Les deux patients, le lendemain, cylindres brun boueux et créatinine haute. Le pigment a lésé le tubule. On ajoute le diagnostic de nécrose, on ne retire pas le pigment.",
        "Povidone sur le prélèvement, bandelette positive, microscope normal, patient asymptomatique. Faux positif cité en 2025. On recommence le recueil. On ne medicalise pas.",
        "Compte à 6 hématies et bandelette positive et muscles douloureux. Le seuil de 3 est franchi. Il y a une vraie hématurie en plus du possible pigment. On garde les deux pistes, rein musculaire et voie urinaire selon le risque.",
    ],
    10: [
        "Aciclovir, aiguilles, pH 6,2, créatinine qui monte en 24 heures, patient sec. Concordance de forme et de pH, zone 5,5 à 7. On hydrate et l'on revoit la vitesse d'administration avec le prescripteur. On ne cite pas une dose intraveineuse absente des textes ouverts.",
        "Amoxicilline, balai, pH 6, douleur, pas de fièvre. Cristal d'amoxicilline probable. On distingue de la sulfadiazine, qui est en gerbe de blé ambre, et de la cystine, qui est une plaque.",
        "Ciprofloxacine, pH 7,4, aiguilles, étoiles. Concordance avec la ligne au-dessus de 7. On peut nommer le cristal. Si le pH avait été à 5,5, on se serait abstenu.",
        "Méthotrexate, cristaux jaune-brun, pH 5,6, après une chimiothérapie. On surveille aussi l'urate de lyse, losange ambre, qui n'est pas le même cristal. Les deux peuvent coexister. Allopurinol, s'il est indiqué pour l'hyperuricémie, suit le texte 56050, départ bas.",
        "Atazanavir, patient vivant avec le VIH, aiguilles, pH 6,5. On ne change pas le traitement antirétroviral depuis le microscope seul. On prévient l'infectiologue. Le sédiment est un argument, pas une ordonnance.",
        "Triamtérène, sphères brunes, croix de Malte, protéinurie négative, pas d'œdème. La croix ne suffit pas au syndrome néphrotique. Il faut la protéine et l'albumine. Ici le médicament explique la croix.",
        "On relit le tableau entier avant de signer : sulfadiazine, aciclovir, atazanavir, méthotrexate, vitamine C, triamtérène, ciprofloxacine, amoxicilline. Une ligne oubliée est une cristallurie qu'on attribuera à tort à un calcul.",
        "Le pH se mesure sur l'urine fraîche. Un pH qui a dérivé dans le pot pendant la nuit ne sert plus à nommer le cristal. On le refait.",
        "Douleur et créatinine haute et cristal de médicament : hydratation, avis, arrêt ou adaptation. Le sédiment a fait le lien. Il ne choisit pas la dose de remplacement.",
    ],
    9: [
        "Jeune homme, festival, danse toute la nuit, urines marron au matin, bandelette sang positive, 0 hématie au microscope, muscles douloureux, plasma clair. Myoglobine d'effort. Remplissage, créatinine, potassium. Pas de tableau de cancer. Pas de fosfomycine.",
        "Femme transfusée, frissons, plasma rose, urine rouge, 1 hématie par champ. Hémoglobinurie. Le sédiment ressemble à celui de la myoglobine. Le plasma les sépare. On traite la réaction, pas la vessie.",
        "Les deux patients, le lendemain, cylindres brun boueux et créatinine haute. Le pigment a lésé le tubule. On ajoute le diagnostic de nécrose, on ne retire pas le pigment.",
        "Povidone sur le prélèvement, bandelette positive, microscope normal, patient asymptomatique. Faux positif cité en 2025. On recommence le recueil. On ne medicalise pas.",
        "Compte à 6 hématies et bandelette positive et muscles douloureux. Le seuil de 3 est franchi. Il y a une vraie hématurie en plus du possible pigment. On garde les deux pistes, rein musculaire et voie urinaire selon le risque.",
        "Marathon, urine rouge, 2 hématies, lendemain tout est clair et la créatinine est stable. On recontrôle une fois. On n'ouvre pas le bilan urologique sur un pot d'effort.",
        "Crush syndrome, membre coincé, urine noire, potassium haut. Le sédiment confirme le pigment. La kaliémie décide de l'urgence. On ne attend pas le microscope pour protéger le cœur.",
        "Hémolyse mécanique sur valve, plasma rose, urine rose, 0 hématie. Hémoglobinurie chronique possible. On adresse en hématologie. Le tableau de l'hématurie microscopique ne s'ouvre pas sous 3 hématies.",
        "Bandelette positive, 4 hématies, pas de muscle, pas d'hémolyse, homme de 62 ans. Là ce n'est plus ce diagnostic. On passe au tableau urologique, colonne élevée par l'âge masculin.",
        "On écrit dans la note la couleur du plasma, le compte exact, et le nom du pigment ou le mot non tranché. Trois lignes. Sans elles, le dossier se relit comme une hématurie ordinaire.",
        "Rhabdomyolyse allongée au sol, personne âgée, urine brun foncé, bandelette positive, microscope sans hématie. Même lecture que chez le jeune du festival. L'âge ne transforme pas le pigment en cancer. On cherche la cause du décubitus et l'on protège le rein.",
        "Une urine couleur cola est une image, pas un diagnostic. On la traduit : pigment, ou sang, ou les deux, selon le compte. On n'écrit pas une marque de boisson dans la conclusion.",
        "Test de la bandelette refait après un nouveau recueil sans désinfectant. Si elle reste positive et que le microscope reste vide, le pigment tient. Si les deux deviennent négatifs, c'était le prélèvement.",
        "Potassium, créatinine, calcium parfois bas dans l'écrasement. Ces dosages ne sont pas le sédiment. Ils se demandent dans la même heure. Le microscope peut attendre dix minutes, pas le potassium menaçant.",
        "On ne donne pas de fosfomycine, ni de ciprofloxacine, ni de ramipril pour une myoglobine isolée. Aucun de ces produits ne traite le muscle. Le ramipril serait même malvenu si le rein vient de s'arrêter.",
        "Hémolyse et myoglobine ensemble, rare, plasma rose et muscles douloureux. On n'oblige pas le sédiment à choisir. On écrit les deux hypothèses et l'on demande les deux bilans.",
    ],
}


def page_dx(dx):
    nom = dx["nom"]
    corps = corps_dx(dx)
    contenus = {}
    for n, titre in [
        (1, "Définition"), (2, "Épidémiologie"), (3, "Physiopathologie et rappels"),
        (4, "Démarche diagnostique"), (5, "Anamnèse et drapeaux rouges"), (6, "Examen physique"),
        (7, "Approche syndromique"), (8, "Diagnostic positif"), (9, "Examens complémentaires"),
        (10, "Arbre décisionnel"), (11, "Prise en charge en Suisse"), (12, "Prévention"),
        (13, "Points clés"), (14, "Pièges d'examen"),
    ]:
        contenus[n] = (ile(nom, dx["definition"], dx["voir"]), corps[n])
    essentiel = [
        f"{nom}. {dx['gravite']}.",
        dx["definition"],
        "Les seuils du sédiment ne se raccourcissent pas dans cette fenêtre d'essentiel : ils sont au complet dans les points 8 et 13.",
    ]
    return page(
        nom,
        nom,
        f"DX.{dx['n']}. {nom}. F2.15, sédiment urinaire anormal. Texte du 31 octobre 2026.",
        essentiel,
        contenus,
        SOURCES,
        f"FIN_FICHIER LOT_163_Phase_B_DX.{dx['n']}",
    )


def bonus_dx(dx):
    """Cas et questions d'examen supplémentaires, propres au diagnostic."""
    nom = dx["nom"]
    n = dx["n"]
    items = []
    questions = {
        1: [
            ("Pourquoi les nitrites peuvent manquer alors que la vessie est infectée ?", "Le germe ne réduit pas le nitrate, ou l'urine n'a pas séjourné. L'entérocoque est le classique. La leucocyte estérase reste utile. On ne conclut pas à l'absence d'infection sur des nitrites négatifs seuls."),
            ("Pourquoi 10 exposant 5 UFC/ml n'est pas le seuil de cette dysurie ?", "Ce chiffre définit la bactériurie asymptomatique, deux pots chez la femme. La femme symptomatique se lit dans une fourchette qui descend jusqu'à 10 exposant 2 selon les symptômes. Appliquer 10 exposant 5 fait manquer des cystites vraies."),
            ("Quel sachet, quelle heure ?", "Fosfomycine Sandoz, numéro 66690, 3 g une fois, le soir, vessie vide, à distance du repas. Pas chez l'homme. Pas comme traitement d'une pyélonéphrite."),
            ("Que dit le texte suisse de la nitrofurantoïne que le tableau européen ne dit pas ?", "La capsule de 100 mg se donne 2 à 3 fois par jour pendant 7 à 10 jours, numéro 62724. L'Europe a écrit 5 jours pour une forme macrocristalline. On ne mélange pas les durées."),
            ("Dernier trimestre.", "La nitrofurantoïne est contre-indiquée, risque d'hémolyse du nouveau-né. Bactrim aussi au dernier trimestre, ictère nucléaire. Ciprofloxacine : le texte demande de ne pas l'utiliser chez la femme enceinte."),
            ("Quatre antibiotiques en un an pour brûlures, et 18 hématies.", "On sort de la cystite. On ouvre le tableau de l'hématurie. Un nouvel antibiotique sans microscope est la copie fausse."),
        ],
        2: [
            ("Femme de 61 ans, 4 hématies, non fumeuse.", "Intermédiaire par l'âge, pas élevée. L'âge seul ne hisse pas une femme dans la colonne élevée depuis l'amendement de 2025."),
            ("Homme de 61 ans, 4 hématies, non fumeur.", "Élevé. Le sexe change la colonne à âge égal."),
            ("Vingt-huit hématies, femme de 35 ans, non fumeuse.", "Plus de 25 : colonne élevée, l'âge jeune ne protège pas."),
            ("Huit hématies et un antécédent de caillot l'an passé.", "L'hématurie macroscopique ancienne classe en élevé, même si le compte du jour est bas."),
            ("Aspirine et 15 hématies.", "Même bilan que sans aspirine. L'antiagrégant n'est pas une cause qu'on solde."),
            ("Lynch connu, 4 hématies, femme de 40 ans.", "Imagerie de la voie haute, quelle que soit la colonne. Le reste du tableau s'ajoute, il ne remplace pas cette imagerie."),
            ("Cytologie pour éviter la cystoscopie chez un homme de 70 ans.", "Le guide dit de ne pas utiliser la cytologie pour décider la cystoscopie initiale quand le risque est élevé. Ici l'âge masculin le met en élevé."),
            ("Contrôle à six mois.", "Réservé au risque faible ou négligeable, tous les critères bas réunis. Un seul critère intermédiaire interdit ce délai comme seule conduite."),
        ],
        3: [
            ("Quatre pour cent d'acanthocytes, cylindre hématique, créatinine stable.", "Le seuil de 1991 est 5 %. Quatre pour cent ne l'atteint pas. Le cylindre hématique, lui, indique déjà un saignement de parenchyme. On ne rassure pas. On demande un deuxième regard et l'avis néphrologique si la protéine ou la tension s'y met."),
            ("Zéro acanthocyte, glomérulonéphrite déjà prouvée.", "La sensibilité n'est que 52 %. L'absence n'innocente pas. Les hématies isomorphes sont fréquentes même dans la glomérulonéphrite, phrase de 2019."),
            ("Quarante pour cent d'hématies seulement appelées dysmorphiques, sans acanthocyte décrit.", "Köhler a montré que la plupart de ces formes se voient hors du glomérule. On redemande les acanthocytes, pas un pourcentage flou."),
            ("Douze pour cent d'acanthocytes.", "Au-dessus de 5 %. Dans l'étude, la moyenne en glomérulonéphrite prouvée était 12,4 %. Spécificité 98 %. On adresse."),
            ("Protéinurie et hématurie, le correspondant veut annuler la cystoscopie.", "L'avis néphrologique est indiqué. Le bilan urologique selon le risque continue. Les deux ne s'excluent pas."),
            ("Immunoglobuline A connue, hématurie qui persiste.", "KDIGO 2021 dit que suivre l'abondance et la persistance peut avoir une valeur pronostique dans cette maladie et dans la vascularite à immunoglobuline A. On ne jette pas les comptes successifs."),
        ],
        4: [
            ("Fièvre, loge, nitrites négatifs, leucocytes présents, densité 1,020.", "Pyélonéphrite possible. Les nitrites ne sont pas exigés. La densité est au-dessus de 1,015, le compte de leucocytes se lit."),
            ("Même tableau, densité 1,005, leucocytes rares.", "Urine diluée. Un faux négatif de leucocytes est possible. On ne solde pas le diagnostic sur ce compte. On reprend le contexte clinique."),
            ("Cylindre leucocytaire.", "Il oriente vers pyélonéphrite, néphrite interstitielle ou glomérulonéphrite proliférative. Il ne choisit pas l'antibiotique à lui seul. La fièvre et la loge départagent."),
            ("Ordonnance de nitrofurantoïne 100 mg.", "Interdite dans la pyélonéphrite, recommandation forte de 2024. Le produit reste légitime dans la cystite basse, pas ici."),
            ("Voie orale possible, femme non enceinte, pyélonéphrite simple.", "Ciproxine, 2 fois 500 mg, 7 jours, numéro 47795. Compliquée : jusqu'à 2 fois 750 mg, au moins 10 jours."),
            ("Grossesse et douleur lombaire fébrile.", "Pas de ciprofloxacine selon le texte suisse. Hospitalisation et produit relu pour le trimestre."),
        ],
        5: [
            ("Enveloppe bipyramide, pH 6, biréfringence faible.", "Oxalate dihydraté. Le monohydrate est ovoïde ou en haltère, biréfringence forte, et se confond avec une hématie."),
            ("Haltères nombreuses après une intoxication à l'éthylène glycol.", "Oxalate monohydraté. Ce n'est pas un calcul ordinaire. L'urgence est métabolique, pas une colique simple."),
            ("Losange ambre, pH 5,5.", "Acide urique. Au-dessus de 5,8 on rediscute le nom."),
            ("Plaque hexagonale, pH 5,5.", "Cystine. On confirme par les acides aminés. L'urate à six côtés est ambre, pas incolore."),
            ("Couvercle, pH 7, Proteus.", "Struvite. On cherche le calcul infectieux. Une bactériurie à germe uréasique persistante fait chercher une pierre."),
            ("Cristaux apparus le lendemain au réfrigérateur, patient asymptomatique.", "Précipitation in vitro, surtout l'urate. On ne pose pas un diagnostic de lithiase sur une urine oubliée."),
            ("Allopurinol.", "Seulement si l'hyperuricémie est l'indication. Départ bas, par exemple 100 mg, numéro 56050. Pas un protocole de calcul écrit à part dans le texte ouvert."),
        ],
        6: [
            ("Éosinophiles à 1 % des leucocytes urinaires, coloration de Hansel.", "Sensibilité 30,8 %, spécificité 68,2 %, rapport de vraisemblance positif 0,97. La probabilité ne bouge pas."),
            ("Éosinophiles à 6 %.", "Au seuil de 5 %, la sensibilité tombe à 19,8 % et la spécificité monte à 91,2 %. Même là, le test sépare mal la néphrite interstitielle de la nécrose tubulaire."),
            ("Quatre-vingts pour cent des néphrites interstitielles de la série étaient médicamenteuses.", "On arrête le médicament nouveau avant de discuter une dose de corticoïde."),
            ("Prednisone.", "Fourchette habituelle 5 à 60 mg par jour, numéro 29349. La maladie n'est pas dans les indications nommées. On ne écrit pas un milligramme par kilogramme."),
            ("Cylindre leucocytaire et AINS.", "Le cylindre et le médicament conduisent. L'éosinophilurie ne les remplace pas."),
            ("Cylindre hématique sans glomérule à la biopsie, dans une série de néphrite interstitielle.", "Le curriculum rappelle que des cylindres hématiques ont été vus sans lésion glomérulaire. Un cylindre hématique n'est donc pas réservé au glomérule dans 100 % des lames, même si le guide de laboratoire le tient pour un saignement de parenchyme."),
        ],
        7: [
            ("Nombreux cylindres brun boueux, sepsis, créatinine qui double.", "Nécrose tubulaire. Le nom muddy brown est celui du curriculum 2019 pour le granuleux dense brun terre brûlée."),
            ("Le même aspect dans une microangiopathie.", "Le granuleux n'est pas exclusif. Anémie, plaquettes et frottis se lisent avant de graver seulement nécrose."),
            ("Quelques hyalins, créatinine qui revient après le remplissage.", "Tableau prérénal. La valeur prédictive négative lue, quand on pensait déjà à cette forme et que granuleux et cellules tubulaires manquent, est 91 %."),
            ("On pensait à la nécrose, et les granuleux sont là.", "Valeur prédictive positive lue 100 % dans ce sous-groupe, valeur prédictive négative seulement 44 %. L'absence ne lave pas un tableau clinique fort."),
            ("Rapport de cotes.", "9,7 pour le score 1 contre 0, et 74 pour un score d'au moins 2 contre 0, intervalles lus dans les résultats de 2008. La grille case par case du tableau 1 n'est pas reproduite, conversion incomplète."),
            ("Cylindre cireux chez un patient dialysé depuis des années.", "Insuffisance chronique, pas la nécrose du jour. Le cireux est grand, homogène, bords nets."),
        ],
        8: [
            ("Œdèmes, albumine 22 g/l, protéinurie au-dessus de 3,5 grammes par jour.", "Syndrome néphrotique selon KDIGO 2021. L'albumine sous 30 g/l fait partie de la définition lue."),
            ("Protéinurie au-dessus de 3,5 grammes par jour, albumine normale, pas d'œdème.", "Protéinurie de rang néphrotique, pas le syndrome complet. KDIGO distingue les deux."),
            ("Croix de Malte.", "Esters de cholestérol en lumière polarisée. Les gouttelettes de triglycérides ne portent pas cette croix de la même façon. On polarise avant de conclure."),
            ("Ramipril.", "Néphropathie glomérulaire et protéinurie supérieure à 3 g/jour : départ 1,25 mg, maximum 5 mg, numéro 58159. Le maximum de 10 mg est une autre rubrique."),
            ("Cylindre graisseux et cylindre cireux ensemble.", "La graisse dit la protéine abondante. Le cireux dit la chronicité. On écrit les deux, on n'en efface pas un."),
            ("Mousse des urines seule, sans protéine, homme fumeur de 70 ans.", "Ce n'est pas un syndrome néphrotique. S'il y a des hématies, c'est le tableau urologique."),
        ],
        9: [
            ("Bandelette sang positive, 1 hématie par champ, urines brun foncé après un effort extrême.", "Sous le seuil de 3. Ce n'est pas l'hématurie microscopique du guide. Myoglobine ou hémoglobine. Pas de cystoscopie sur ce seul pot."),
            ("Hémolyse, plasma rouge, urine rouge.", "Hémoglobinurie. Le plasma de la myoglobinurie est souvent clair, celui de l'hémolyse est coloré. Le sédiment, lui, est pauvre en hématies dans les deux."),
            ("Cylindre brun granuleux pigmenté.", "Le guide de laboratoire dit que les cylindres d'hémoglobine et de myoglobine ne se distinguent pas à l'œil."),
            ("Créatinine et potassium.", "L'écrasement menace le rein et le potassium. Le sédiment date le mécanisme, il ne remplace pas le ionogramme."),
            ("On a compté 20 hématies en plus de la bandelette positive.", "Là, le seuil de 3 est franchi. Il peut y avoir une vraie hématurie en plus du pigment. On ne solde pas tout sur la myoglobine."),
            ("Povidone iodée sur le méat.", "Faux positif de bandelette cité par le guide urologique, avec l'effort, les règles et la déshydratation."),
        ],
        10: [
            ("Aiguilles en balai, pH 6, amoxicilline.", "Cristal d'amoxicilline, pH 5,5 à 6,5. On arrête ou l'on adapte, on hydrate, on surveille la créatinine."),
            ("Aiguilles, pH 7,5, ciprofloxacine en cours.", "Le curriculum place la ciprofloxacine au-dessus de 7. Ce n'est pas une struvite tant que la forme n'est pas un couvercle."),
            ("Gerbes de blé ambre, sulfadiazine.", "pH autour de 5,5, biréfringence forte. On ne dit pas cystine."),
            ("Sphères brunes, croix de Malte, triamtérène.", "Le triamtérène peut donner une croix de Malte. On ne conclut pas à un syndrome néphrotique sans protéine ni corps ovalaire."),
            ("Méthotrexate jaune-brun, pH 5,5.", "Zone 5,4 à 6,0. L'uricémie peut aussi monter sous lyse. On sépare le cristal de médicament et l'urate."),
            ("Atazanavir, aiguilles, pH 6,5.", "Zone 6 à 7. Le contexte VIH et le produit se demandent. On ne lance pas un bilan de cystine."),
            ("Vitamine C à très forte dose, haltères.", "Oxalate monohydraté. La vitamine C est dans le tableau des cristaux liés aux médicaments, même forme que l'oxalate."),
        ],
    }
    src = {1: U, 2: A, 3: K, 4: CIP, 5: C, 6: M, 7: P, 8: G, 9: A, 10: C}[n]
    for q, r in questions[n]:
        items.append((f"Question. {q}", src))
        items.append((f"Réponse. {r}", src))
        items.append((f"Note de dossier pour {nom}. On recopie la réponse en une ligne, avec le chiffre et le produit s'il y en a un, pas un synonyme vague.", src))
    # deuxième vague, un peu plus longue pour les fichiers les plus courts
    extra = {
        9: [
            "On demande l'heure de l'effort ou de l'écrasement, la couleur du plasma, la créatinine, le potassium, et le compte exact d'hématies. Quatre lignes. Si le compte est sous 3, la branche urologique ne s'ouvre pas.",
            "Si le compte dépasse 3, on garde les deux hypothèses : pigment et vraie hématurie. Le tableau de risque s'applique alors à la part hématies, sans oublier le muscle.",
            "Un cylindre hématique vrai, avec des hématies dedans, ramène vers le parenchyme, pas vers la seule myoglobine.",
        ],
        6: [
            "Liste de médicaments à faire lire au patient : anti-inflammatoire, antibiotique, et tout produit commencé depuis moins de deux semaines. Dans la série de 2013, 80 % des 91 néphrites interstitielles prouvées étaient médicamenteuses.",
            "La biopsie reste la référence quand la créatinine monte et que l'arrêt du médicament ne suffit pas à trancher. L'éosinophilurie ne la remplace pas.",
            "On ne donne pas une fluoroquinolone pour une leucocyturie de néphrite interstitielle. Il n'y a pas de germe à couvrir tant que la culture est négative et le tableau est médicamenteux.",
        ],
        10: [
            "On aligne trois colonnes sur la feuille : nom du médicament, pH de l'urine, forme du cristal. Si les trois concordent avec le tableau de 2019, on écrit le lien. Si le pH est à l'opposé, on cherche un autre cristal.",
            "L'obstacle par les cristaux se voit à la douleur et à l'échographie, pas seulement au microscope. Le sédiment explique, l'image décide de la dérivation.",
            "On ne commence pas l'allopurinol pour une aiguille d'antibiotique. Le numéro 56050 traite l'hyperuricémie, pas l'amoxicilline.",
        ],
        5: [
            "Colique, vomissement, fièvre : l'infection sur obstacle passe avant le nom du cristal. On n'attend pas le spectre infrarouge pour dériver.",
            "Sans fièvre, pH et forme suffisent à orienter. L'analyse du calcul, s'il est rendu, confirme. Le sédiment du jour n'est pas le calcul.",
            "Tamsulosine, numéro 62112 : 0,4 mg pour les symptômes de l'hyperplasie bénigne, pas une indication de calcul lue dans cette session. On n'écrit pas cette capsule comme un traitement d'expulsion.",
        ],
        4: [
            "Homme fébrile, douleur lombaire, leucocyturie. Ce n'est pas la cystite non compliquée. Pas de sachet de 3 g. Culture et traitement du haut appareil, toucher rectal selon le guide.",
            "Sonde en place, fièvre, 10 exposant 3 UFC/ml. Le seuil de la sonde n'est pas 10 exposant 5. L'odeur seule ne suffit toujours pas.",
            "Après guérison, s'il y avait des hématies, on recontrôle le microscope entre trois semaines et trois mois. Une hématurie qui reste ouvre le tableau de risque.",
        ],
        1: [
            "Bactrim forte, 2 à 3 comprimés en une fois, 160 mg et 800 mg par comprimé, numéro 48306, seulement si l'on suit le texte suisse et que le germe est sensible. Ce n'est pas le premier choix européen.",
            "Pivmécillinam 400 mg trois fois par jour, 3 à 5 jours, tableau européen. Pas une phrase d'information suisse ouverte.",
            "Contrôle de guérison : si l'hématurie était le motif caché, le microscope revient. Si la femme va bien et qu'il n'y avait pas d'hématurie, on ne multiplie pas les cultures.",
        ],
        7: [
            "Cellules tubulaires en rayon de miel, ou en cylindre. Le guide de laboratoire les décrit dans la nécrose sévère. On les nomme, on ne les compte pas comme des leucocytes.",
            "Un cylindre graisseux dans le même pot fait chercher une protéinurie, pas seulement la nécrose du sepsis.",
            "On date l'heure du choc et l'heure du sédiment. Un sédiment fait trois jours plus tard, urine oubliée, ne porte plus le même poids.",
        ],
        8: [
            "Cholestérol en plaques minces, pH 5,5, pas de biréfringence, dans le tableau des cristaux. Ce n'est pas la croix de Malte des gouttelettes. Les deux peuvent coexister. On les écrit séparément.",
            "Leucine en sphères striées peut aussi donner une croix de Malte, pH 5,5 à 6,5, et elle oriente vers une maladie hépatique grave, pas vers un glomérule. Le contexte hépatique se demande.",
            "2,8-dihydroxyadénine : ronds brun-rouge à spicules, croix de Malte, déficit enzymatique rare, parfois découvert après une greffe. On n'appelle pas cela de l'urate sans y penser si les calculs récidivent.",
        ],
        3: [
            "Tension, créatinine, protéine, acanthocytes, cylindre. Cinq items. Il en manque un : on le demande, on n'invente pas le pourcentage.",
            "Enfant ou adulte jeune, hématurie glomérulaire isolée, audition ou famille : on pense aux causes héréditaires sans poser un nom de gène qui n'a pas été lu.",
            "Le guide KDIGO demande cette lecture du sédiment dans toutes les maladies glomérulaires, pas seulement dans la néphropathie à immunoglobuline A.",
        ],
        2: [
            "Trois à dix hématies, femme de moins de 60 ans, moins de 10 paquets-années, aucun facteur ajouté : les quatre critères bas sont réunis. Contrôle dans les six mois.",
            "Le même dossier avec un seul facteur irritatif : on quitte le faible. Un facteur ajouté suffit pour l'intermédiaire.",
            "Facteur ajouté plus un critère déjà élevé, par exemple plus de 25 hématies et un métier des colorants : la case élevée des facteurs ajoutés est celle-là. On ne compte pas le métier deux fois.",
        ],
    }
    esrc = U if n == 4 else src
    for phrase in extra.get(n, []):
        items.append((phrase, esrc))
    return bloc(items)


def page_a():
    contenus = {}
    # îlots courts
    iles = {
        1: ["Le sédiment urinaire anormal est la microscopie d'un élément qui change la conduite.", "La bandelette ne suffit pas.", "La définition chiffrée est dans la fenêtre."],
        2: ["Aucune prévalence suisse n'a été lue pour ces dix diagnostics.", "La gravité ne suit pas la fréquence.", "Le détail est dans la fenêtre."],
        3: ["Les cylindres naissent de l'uromoduline.", "Les hématies du glomérule se déforment.", "Les cristaux suivent le pH."],
        4: ["On écarte d'abord la menace, puis on sépare glomérule, voie, infection, tubule et cristal.", "Chaque seuil est nommé.", "La fenêtre porte l'ordre."],
        5: ["Médicaments, tabac, métier, règles, effort, muscle, sonde.", "L'anticoagulant ne rassure pas.", "Les drapeaux sont dans la fenêtre."],
        6: ["Tension, œdèmes, loge, couleur de l'urine.", "Le schéma des cylindres et des cristaux est dans la fenêtre.", "Ce n'est pas une photographie."],
        7: ["Infection, glomérule, voie, tubule, graisse, cristal.", "Les dix diagnostics y ont leur place.", "Le tableau comparatif est dans la fenêtre."],
        8: ["Positif seulement si l'élément et le contexte concordent.", "Les deux seuils de 5 % restent distincts.", "La fenêtre les sépare."],
        9: ["Densité, délai, contraste de phase, lumière polarisée, culture selon le contexte.", "Le niveau avancé nomme les cylindres.", "La fenêtre détaille."],
        10: ["Menace, puis glomérule, puis voie selon le tableau entier, puis infection.", "On ne saute pas une colonne.", "L'arbre est dans la fenêtre."],
        11: ["Les doses suisses sont celles des numéros cités.", "La fluoroquinolone n'est pas le premier choix de la cystite simple.", "La fenêtre porte les schémas."],
        12: ["Pas de traitement d'une colonisation hors indication.", "Recontrôle après une hématurie mise sur une infection.", "La fenêtre précise."],
        13: ["Trois hématies. Cinq pour cent d'acanthocytes. Cinq pour cent de dysmorphie, phrase distincte.", "Dix leucocytes par microlitre. Dix exposant cinq, et les autres seuils.", "Rien n'est retiré pour aller plus vite."],
        14: ["Le piège majeur est de traiter une voie comme un glomérule, ou une myoglobine comme un cancer.", "Le cas corrigé est dans la fenêtre.", "On relit le tableau avant de signer."],
    }
    # corps : blocs communs + capsules des 10 DX
    communs = {
        1: bloc([
            ("Sédiment urinaire anormal : présence, à la microscopie, d'un élément figuré dont la nature change le diagnostic ou le geste. Hématies, leucocytes, cylindres, cristaux, germes, lipides.", E),
            ("La bandelette est un tri. Elle ne pose pas le nom.", A),
            ("L'unité recommandée est le nombre de particules fois 10 exposant 6 par litre. Dix fois 10 exposant 6 par litre, c'est 10 par microlitre.", E),
        ]) + seuils_hematurie(),
        2: bloc([
            ("On ne publie pas une prévalence suisse. Elle n'a pas été lue.", None),
            ("En consultation, les leucocytes et les germes d'une cystite sont le motif le plus ordinaire. L'hématurie microscopique est fréquente et son bilan dépend du risque, pas du mot fréquent.", A),
            ("Le cylindre hématique et le brun boueux sont moins souvent vus. Leur gravité ne baisse pas avec cette rareté.", C),
        ]),
        3: atlas_cylindres() + bloc([
            ("Supersaturation, pH et délai font le cristal. L'urate aime l'acide, sous 5,8. La struvite aime l'alcalin du germe uréasique.", E),
            ("La myoglobine et l'hémoglobine libre colorent la plage sang sans déposer d'hématies.", A),
        ]),
        4: seuils_hematurie() + seuils_infection() + bloc([
            ("Garde de nuit, ordre unique. Menace vitale, puis bandelette, puis microscope, puis culture selon le contexte, puis le tableau de risque seulement si les hématies sont au moins 3 par champ et qu'elles ne sont pas expliquées par un pigment.", A),
            ("Avant de quitter la garde, on relit à voix haute les dix noms du lot : cystite, hématurie de la voie, hématurie glomérulaire, pyélonéphrite, cristallurie lithogène, néphrite interstitielle, nécrose tubulaire, syndrome néphrotique, myoglobine ou hémoglobine, cristallurie médicamenteuse. Le pot du patient en occupe un, parfois deux. Jamais les dix.", None),
            ("On écrit l'heure du recueil et l'heure de la lecture. Un pot de plus de deux heures ne porte plus les cylindres ni les cristaux avec le même poids.", C),
            ("Densité au-dessus de 1,015 ou osmolalité au-dessus de 300 avant de croire un compte de leucocytes bas.", E),
            ("Acanthocytes et cylindre hématique cherchés à chaque hématurie, même si l'on pense d'abord à la voie. KDIGO le demande dans toute maladie glomérulaire, et le guide urologique demande l'inverse : ne pas oublier la voie quand le rein est atteint.", G),
        ]),
        5: facteurs_ajoutes() + bloc([
            ("Cyclophosphamide et ifosfamide restent dans la liste, même des années après.", A),
            ("Une douleur musculaire et une urine brun foncé passent avant le mot hématurie.", C),
        ]),
        6: SVG + atlas_cylindres(),
        7: table(
            "Dix lectures du sédiment, LOT_163",
            ["Diagnostic", "Élément qui oriente", "Ce qui l'écarte du voisin", "Gravité"],
            [[d["nom"], d["voir"], d["pas"], d["gravite"]] for d in DXS],
        ) + bloc([(f"{d['nom']}. {d['definition']}", None) for d in DXS]),
        8: seuils_hematurie(),
        9: bloc([
            ("Examiner de préférence avant deux heures. Au-delà, l'urate précipite chez le sujet sain et les leucocytes se lysent.", C),
            ("Le niveau avancé est celui d'un avis néphrologique. Le niveau de base ne doit pas appeler pathologique un cylindre hyalin isolé du matin.", E),
            ("Oxalate monohydraté : ovoïde, haltère ou bâtonnet, biréfringence forte, pH 5,4 à 6,7. On le confond avec une hématie si l'on ne polarise pas.", C),
            ("Oxalate dihydraté : enveloppe bipyramide, biréfringence faible, même zone de pH. Les deux formes peuvent coexister.", C),
            ("Acide urique : ambre, losange, tonneau, rosette ou aiguille, pH 5,4 à 5,8, biréfringence forte. Le guide de laboratoire retient une précipitation seulement sous 5,8.", E),
            ("Cystine : hexagone incolore, bords irréguliers, pH 5,5, biréfringence faible. On confirme par les acides aminés.", E),
            ("Struvite : prisme en couvercle, pH 6,2 à 7,0, biréfringence forte. Proteus et les germes uréasiques vont avec.", C),
            ("Phosphate de calcium : prismes, aiguilles, étoiles, pH 6,7 à 7,0. Urate d'ammonium : pomme d'arroche. Carbonate : trèfle, pH 7.", C),
            ("Leucine et 2,8-dihydroxyadénine donnent une croix de Malte sans être de la graisse néphrotique. La leucine oriente vers le foie. La dihydroxyadénine est un déficit rare.", C),
            ("Cholestérol : plaques à bords nets, pas de biréfringence, pH 5,5. La croix de Malte, elle, est celle des gouttelettes, pas de ces plaques.", C),
            ("Médicaments du tableau, tous nommés. Sulfadiazine en gerbe de blé. Aciclovir en aiguilles. Atazanavir en aiguilles. Méthotrexate jaune-brun. Vitamine C comme l'oxalate monohydraté. Triamtérène en sphères, croix de Malte. Ciprofloxacine au-dessus de pH 7. Amoxicilline en balai.", C),
            ("Tyrosine en aiguilles, bilirubine collée aux cellules. On ne les range pas avec les médicaments.", C),
        ]) + cristaux_table(),
        10: aua_table() + facteurs_ajoutes() + bonus_dx(DXS[1]) + bloc([
            ("Risque faible ou négligeable : contrôle à six mois.", A),
            ("On n'utilise pas la cytologie pour décider la cystoscopie initiale aux deux extrêmes du risque.", A),
            ("Lynch ou carcinome rénal familial : imagerie haute de toute façon.", A),
        ]),
        11: doses_cystite() + doses_rein(),
        12: bloc([
            ("Prévention. Recueil correct, densité lue, pas d'antibiotique sur une odeur, recontrôle de l'hématurie attribuée à une infection.", U),
            ("Grossesse. Relire le trimestre avant nitrofurantoïne, Bactrim ou ciprofloxacine.", NIT),
        ]),
        13: seuils_hematurie() + seuils_infection() + atlas_cylindres(),
        14: bloc(cas(
            "Femme de 58 ans, trois prescriptions d'antibiotique pour cystite en un an, 18 hématies par champ aujourd'hui, 15 paquets-années, apyrétique, pas d'écoulement",
            "hématies isomorphes, leucocytes limites, culture négative, protéine négative",
            "Ce n'est pas une cystite. Dix-huit hématies sont dans la bande 11 à 25, donc au moins intermédiaire. Quinze paquets-années sont aussi intermédiaires. On ne la met pas en élevé sur l'âge, elle a moins de 60 ans. On ne la rassure pas.",
            "Bilan de la colonne intermédiaire. Contrôle du microscope seulement si une vraie infection avait été prouvée, ce qui n'est pas le cas.",
            "un quatrième antibiotique, ou un classement élevé du seul fait qu'elle est une femme de plus de 50 ans. Le guide de 2025 a retiré l'âge féminin de la colonne élevée.",
            A,
        )) + bloc([
            ("Deuxième erreur du même dossier. Oublier de demander une radiothérapie ou un Lynch. Un seul facteur ajouté, avec déjà un critère élevé, monterait la colonne.", A),
            ("Troisième erreur. Voir 2 % d'acanthocytes et appeler cela glomérulaire. Le seuil lu est 5 %, et 2 % est la zone rare hors glomérule.", K),
        ]) + "".join(bonus_dx(d) for d in DXS if d["n"] != 2),
    }
    for n in range(1, 15):
        contenus[n] = (iles[n], communs[n])
    essentiel = [
        "Sédiment urinaire anormal : on regarde le microscope, pas seulement la bandelette.",
        "Au moins 3 hématies par champ. Acanthocytes au moins 5 %. Leucocytes 10 par microlitre si l'urine est concentrée.",
        "Glomérule et voie se bilantent ensemble quand les deux sont possibles. L'infection se traite, puis l'hématurie se recontrôle.",
    ]
    return page(
        "Sédiment urinaire anormal",
        "Sédiment urinaire anormal",
        "Phase A. F2.15, sédiment urinaire anormal. Texte du 31 octobre 2026.",
        essentiel,
        contenus,
        SOURCES,
        "FIN_FICHIER LOT_163_Phase_A",
    )


def main():
    dests = []
    dests.append(ecrire("LOT_163_Phase_A_V0.html", page_a()))
    for dx in DXS:
        dests.append(ecrire(f"LOT_163_Phase_B_V0_DX.{dx['n']}.html", page_dx(dx)))
    print("écrit", len(dests), "fichiers")


if __name__ == "__main__":
    main()
