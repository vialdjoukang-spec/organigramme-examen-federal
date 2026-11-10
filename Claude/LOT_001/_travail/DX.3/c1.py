from h import *

def p01():
    p = Pt(1)
    o = []
    o.append(p.P(
        S("L'endocardite infectieuse est une infection microbienne de la surface endocardique, qui touche le plus souvent les valves natives et prothétiques du cœur", 'wc68439-2'),
        S("Elle se distingue d'une simple bactériémie, car les bactéries doivent se fixer sur l'endocarde ou sur un matériel intracardiaque pour y former une lésion infectée", 'wd98409-9'),
        S("Dans le LOT_001, une transpiration anormale n'évoque cette maladie que si elle s'associe à de la fièvre, à un terrain à risque ou à une bactériémie documentée")))
    o.append(p.P(
        S("La Société européenne de cardiologie a publié en 2023 ses recommandations pour la prise en charge de l'endocardite, dans l'European Heart Journal", 'w842342-1'),
        S("Ce texte a reçu des corrections publiées en 2023, en 2024 puis en 2025, de sorte qu'il faut lire la version corrigée", 'w842342-4'),
        S("Les critères diagnostiques de référence restent les critères de Duke, introduits en 1994 puis modifiés plusieurs fois pour intégrer les nouvelles techniques d'imagerie", 'wc68439-13'),
        S("La version actuelle porte le nom de critères Duke-ISCVID 2023, où ISCVID désigne la Société internationale des maladies infectieuses cardiovasculaires", 'w0e265d-5')))
    o.append(H4("1.a Lexique : ce que chaque terme décide"))
    o.append(p.P(
        S("Une " + p.w("végétation", fp(
            S("La végétation est issue d'une lésion endocardique stérile appelée endocardite thrombotique non bactérienne, faite de plaquettes et de fibrine", 'wd98409-9'),
            S("Lors d'une bactériémie, les microorganismes s'y fixent, s'y multiplient et s'entourent d'un biofilm de plaquettes et de fibrine", 'wd98409-9'),
            S("Ce biofilm protège les bactéries des défenses de l'hôte et des antibiotiques, ce qui explique la difficulté de traiter une infection installée", 'wd98409-9'))) +
          " est donc une lésion infectée, à la fois thrombotique et microbienne", 'wd98409-9'),
        S("L'image échographique seule ne prouve pas l'infection, car la lésion de départ est un thrombus stérile", 'wd98409-9')))
    o.append(p.P(
        S("Une endocardite sur valve native touche une valve sans prothèse, alors qu'une endocardite prothétique concerne un matériel implanté", 'wbea7b0-25'),
        S("Les formes liées à un dispositif comprennent l'endocardite après valve transcatheter, après valve pulmonaire percutanée et sur dispositif cardiaque implantable", 'wbea7b0-25'),
        S("Un patient porteur d'un dispositif et dont les hémocultures sont positives n'a pas forcément une infection de sonde", 'wbea7b0-34'), S("Le risque est lié à la durée et de la source de la bactériémie, du type de dispositif et du germe", 'wbea7b0-34')))
    o.append(p.P(
        S("Une endocardite à hémocultures négatives est diagnostiquée lorsque les autres critères sont remplis alors qu'aucun germe n'est identifié dans le sang", 'wc68439-16'),
        S("Une endocardite est dite nosocomiale lorsqu'elle apparaît au moins 48 h après l'admission", 'wf45fc8-9'), S("Elle l'est aussi lorsqu'elle est diagnostiquée dans les 48 h chez un patient exposé de façon notable aux soins, par exemple en hémodialyse", 'wf45fc8-9'),
        S("Le classement d'un épisode en rejeté, possible ou certain repose sur les critères Duke-ISCVID 2023", 'w0c22e5-19')))
    o.append(p.P(
        "Le tableau suivant relie chaque terme à la décision qu'il commande."))
    o.append(T(["Terme", "Définition utile", "Décision qui en découle"], [
        ["Végétation", "Masse infectée de plaquettes, de fibrine et de bactéries" + c('wd98409-9'), "Imagerie cardiaque, risque d'embolie"],
        ["Endocardite sur valve native", "Valve sans prothèse" + c('wbea7b0-25'), "Échographie transthoracique puis transœsophagienne"],
        ["Endocardite prothétique ou sur dispositif", "Infection d'un matériel intracardiaque" + c('wbea7b0-25'), "Imagerie complémentaire, discussion d'extraction"],
        ["Hémocultures négatives", "Endocardite sans germe isolé dans le sang" + c('wc68439-16'), "Sérologies et recherche de germes rares"],
        ["Endocardite nosocomiale", "Début au moins 48 h après l'admission" + c('wf45fc8-9'), "Résistances à anticiper, pronostic plus sombre"],
    ]))
    o.append(p.P(
        S("Le lecteur retient que la bactériémie signale un risque, alors que la lésion endocardique ou intracardiaque fait le diagnostic d'endocardite", 'wc68439-13', 'wd98409-9')))
    return ''.join(o)


def p02():
    p = Pt(2)
    o = []
    o.append(p.P(
        S("Une cohorte nationale suisse a analysé 15 255 hospitalisations pour endocardite entre 2012 et 2021 dans les données de facturation hospitalière", 'w6185e6-3', 'w6185e6-4'),
        S("Le nombre annuel de cas est passé de 1361 en 2012 à 1636 en 2021", 'w6185e6-4'),
        S("Ces chiffres comptent des hospitalisations et non des personnes, donc ils ne donnent pas une incidence par habitant", 'w6185e6-3')))
    o.append(p.P(
        S("Dans la même cohorte, la part de Staphylococcus aureus est passée de 19,8 % à 30,0 %, et celle des streptocoques de 17,6 % à 24,4 %", 'w6185e6-4'),
        S("Par ailleurs, l'endocardite à S. aureus a donné la mortalité hospitalière la plus élevée, soit 19,9 %, avec 30,3 % de décès à six mois et 44,2 % d'admissions aux soins intensifs", 'w6185e6-4'),
        S("Les séjours les plus longs concernaient les entérocoques, avec 23,9 jours en moyenne, et S. aureus, avec 23,8 jours", 'w6185e6-4'),
        S("Les auteurs relient cette évolution au vieillissement de la population et à l'usage croissant de dispositifs endovasculaires", 'w6185e6-2')))
    o.append(p.P(
        S("Aucune source lue ne donne la fréquence de l'endocardite parmi les personnes qui consultent pour une transpiration anormale, ce qui interdit d'estimer une probabilité prétest chiffrée")))
    o.append(H4("2.a Le terrain a changé"))
    o.append(p.P(
        S("Dans les pays à revenu élevé, l'endocardite sur valve native touche surtout des patients âgés, avec une valvulopathie dégénérative et de multiples comorbidités", 'wbea7b0-2'),
        S("Les cas associés aux soins représentent jusqu'à 47 % des endocardites", 'wbea7b0-2'),
        S("En outre, le risque est multiplié jusqu'à cinq fois chez les personnes âgées par rapport à la population générale", 'wbea7b0-5'),
        S("Dans ce groupe, la maladie se manifeste souvent de façon atypique, avec des symptômes généraux peu spécifiques, une fièvre atténuée ou une confusion", 'wbea7b0-6')))
    o.append(p.P(
        S("Les endocardites sur prothèse représentaient environ 5 % des cas dans les premières études, alors qu'elles atteignent aujourd'hui jusqu'à 30 % des cas", 'wbea7b0-25'),
        S("Leur mortalité hospitalière peut atteindre 27 %, et la mortalité à un an approche 37 %", 'wbea7b0-25'),
        S("Après remplacement valvulaire aortique percutané, l'incidence rapportée varie de 0,3 à 2 cas par 100 personnes-années", 'wbea7b0-26'),
        S("Dans le registre suisse SwissTAVI, elle culminait en période périprocédurale avec 2,59 cas par 100 personnes-années, puis diminuait à 0,71 et à 0,4", 'wbea7b0-27')))
    o.append(p.P(
        S("L'hémodialyse chronique est l'un des principaux facteurs liés aux soins, avec une incidence de 1,7 à 2 cas pour 1000 patients", 'wbea7b0-9'),
        S("En outre, les cathéters veineux centraux multiplient par 3,5 le taux observé avec une fistule artérioveineuse", 'wbea7b0-10'),
        S("Les personnes qui s'injectent des drogues ont un risque jusqu'à 100 fois supérieur à celui de la population générale", 'wbea7b0-20'),
        S("Cette population représentait 6,9 % des patients du registre européen EURO-ENDO, contre 22,2 % des cas dans une série américaine", 'wbea7b0-21')))
    o.append(p.P("Le tableau suivant permet de retenir les chiffres avec leur population et leur source."))
    o.append(T(["Chiffre", "Population", "Source"], [
        ["15 255 hospitalisations" + c('w6185e6-4'), "Suisse, 2012 à 2021", "Cohorte nationale, Clin Infect Dis"],
        ["S. aureus : 19,8 % à 30,0 %" + c('w6185e6-4'), "Hospitalisations suisses", "Cohorte nationale"],
        ["Mortalité hospitalière 19,9 %" + c('w6185e6-4'), "Endocardite à S. aureus, Suisse", "Cohorte nationale"],
        ["2,59 cas par 100 personnes-années" + c('wbea7b0-27'), "Période périprocédurale après valve percutanée", "Registre SwissTAVI"],
        ["Jusqu'à 47 %" + c('wbea7b0-2'), "Part des cas associés aux soins", "Revue épidémiologique 2026"],
    ]))
    o.append(p.P(
        S("Ce tableau montre que l'endocardite moderne survient souvent chez un patient exposé aux soins, ce qui change les questions à poser et les germes à craindre", 'wbea7b0-2', 'w6185e6-4')))
    o.append(H4("2.b Histoire naturelle et pronostic"))
    o.append(p.P(
        S("La mortalité hospitalière de l'endocardite se situe entre 15 % et 30 %", 'w37576c-4'),
        S("Elle varie de 25 % à 47 % lorsque S. aureus est en cause, alors qu'elle n'est que de 4 % à 9 % pour les streptocoques", 'w37576c-5'),
        S("Une durée des symptômes supérieure à un mois avant le diagnostic et la chirurgie, quand elle est indiquée, sont associées à une évolution plus favorable", 'w37576c-5'),
        S("Les valeurs de cohortes soignées ne décrivent pas l'évolution sans traitement, qui n'est pas chiffrée dans les sources lues")))
    o.append(p.P(
        S("Dans une cohorte de 470 adultes, 124 sont décédés, soit une mortalité de 26,4 %", 'wf45fc8-33'),
        S("En effet, les complications hospitalières comprenaient une insuffisance cardiaque nouvelle ou aggravée dans 27,9 % des cas, une embolie septique dans 25,1 % et une embolie cérébrale dans 18,9 %", 'wf45fc8-24')))
    return ''.join(o)


def p03():
    p = Pt(3)
    o = []
    o.append(p.P(
        S("La maladie commence par une lésion de l'endothélium ou un flux anormal sur une valve altérée, qui attire plaquettes et fibrine", 'wd98409-9'),
        S("Cette lésion stérile appelée endocardite thrombotique non bactérienne constitue le terrain où les bactéries circulantes vont se fixer", 'wd98409-9'),
        S("Les bactéries s'y multiplient ensuite et s'entourent d'un biofilm, ce qui forme la végétation mature", 'wd98409-9')))
    o.append(H4("3.a De la porte d'entrée à la bactériémie"))
    o.append(p.P(
        S("Les streptocoques oraux vivent dans la cavité buccale et la plaque dentaire, et leurs adhésines se lient aux plaquettes et à la fibrine", 'wd98409-10'),
        S("Le brossage, le passage du fil dentaire et la mastication produisent chaque jour des bactériémies transitoires, dont l'effet cumulé dépasse de plusieurs ordres de grandeur celui des actes dentaires occasionnels", 'wd98409-11'),
        S("Les staphylocoques, les entérocoques et les autres germes ne dépendent pas des soins dentaires et ne répondent donc pas à une prophylaxie dentaire", 'wd98409-10')))
    o.append(p.P(
        S("Les procédures invasives non dentaires créent d'autres portes d'entrée", 'w32d770-12'), S("Une étude suédoise a associé l'endocardite à la chirurgie coronarienne, aux gestes cutanés, aux transfusions, à la dialyse, à la ponction de moelle et à certaines endoscopies", 'w32d770-12'),
        S("Chez les patients dialysés, le type d'abord vasculaire peut influencer le risque de bactériémie, donc celui d'endocardite", 'wbea7b0-10')))
    o.append(H4("3.b Pourquoi S. aureus est si redoutable"))
    o.append(p.P(
        S("S. aureus adhère efficacement à l'endothélium lésé et au matériel prothétique, envahit et détruit rapidement les tissus, provoque des bactériémies persistantes, embolise souvent et forme un biofilm", 'w37576c-5'),
        S("Cette virulence explique que S. aureus prédise les embolies et une mortalité précoce élevée", 'w37576c-5'),
        S("Environ 12 % des patients atteints de bactériémie à S. aureus développent une endocardite, d'où l'intérêt d'une échographie systématique", 'w318a1c-18')))
    o.append(H4("3.c Pourquoi le traitement est long"))
    o.append(p.P(
        S("Les bactéries enfouies dans les végétations sont peu accessibles aux antibiotiques et à la réponse immunitaire de l'hôte", 'w37576c-7'),
        S("La forte densité bactérienne réduit l'efficacité de certains antibiotiques, ce que l'on appelle l'effet inoculum, et la végétation forme en outre une barrière à la pénétration des médicaments", 'w37576c-7'),
        S("Le traitement standard comporte donc plusieurs semaines d'antibiotiques par voie intraveineuse, soit de 2 à 6 semaines", 'w37576c-2', 'w37576c-1')))
    o.append(H4("3.d Conséquences cardiaques, emboliques et immunologiques"))
    o.append(p.P(
        S("En effet, la destruction valvulaire provoque une régurgitation modérée à sévère dans 51,1 % des cas", 'wf45fc8-23'), S("Elle provoque aussi des fuites paravalvulaires dans 20,0 %, des valves flottantes dans 12,1 % et des abcès paravalvulaires dans 6,4 %", 'wf45fc8-23'),
        S("Des fragments de végétation migrent dans la circulation : le système nerveux central est le site d'embolisation le plus fréquent, suivi des organes abdominaux, et la majorité des événements restent cliniquement muets", 'wa9c851-4'),
        S("Une végétation de plus de 10 mm augmente le risque d'embolie, avec un rapport de cotes de 2,28, et la mortalité, avec un rapport de cotes de 1,63", 'w2f62fb-10')))
    o.append(p.P(
        S("Des phénomènes immunologiques s'ajoutent : ils sont observés dans 11 % des épisodes d'endocardite contre 2 % des épisodes sans endocardite", 'w0c22e5-29'),
        S("Les complications immunologiques décrites comprennent la glomérulonéphrite par complexes immuns", 'wf45fc8-30')))
    o.append(p.P("Le tableau suivant relie chaque perturbation à l'examen qui la montre et à la thérapeutique qui la corrige."))
    o.append(T(["Perturbation", "Exploration", "Thérapeutique"], [
        ["Bactériémie continue", "Hémocultures répétées" + c('wdb992c-11'), "Antibiotiques après les hémocultures" + c('wdb992c-6')],
        ["Végétation", "Échographie transthoracique et transœsophagienne" + c('wb6a5b9-8'), "Antibiothérapie prolongée" + c('w37576c-2')],
        ["Destruction valvulaire ou abcès", "Échographie, scanner cardiaque" + c('wb6a5b9-11'), "Discussion chirurgicale" + c('wa35a53-5')],
        ["Embolie septique", "Imagerie cérébrale et abdominale" + c('wa9c851-4'), "Contrôle du foyer" + c('wa9c851-11')],
        ["Matériel infecté", "TEP-scanner au FDG" + c('w0c22e5-14'), "Extraction complète si possible" + c('wbea7b0-36')],
    ]))
    o.append(p.P(
        S("Chaque ligne du tableau montre qu'un mécanisme précis commande à la fois l'examen demandé et le geste thérapeutique", 'wd98409-9', 'w37576c-7')))
    return ''.join(o)
