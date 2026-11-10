from h import *

def p04():
    p = Pt(4)
    o = []
    o.append(p.P(
        S("Devant une fièvre avec sueurs, le médecin écarte d'abord les diagnostics graves", 'w0c22e5-26'), S("L'endocardite en fait partie lorsque le patient porte une valve prothétique, un dispositif ou une cardiopathie, ou lorsqu'une bactériémie est prouvée", 'w0c22e5-26'),
        S("Les hémocultures précèdent toujours l'antibiothérapie, car un traitement préalable stérilise le sang et masque le germe", 'wdb992c-6', 'wc68439-16')))
    o.append(H4("4.a Les différentiels discriminants, les graves d'abord"))
    o.append(p.P(
        S("Premier différentiel grave : la bactériémie à S. aureus sans endocardite, qui exige pourtant de chercher l'endocarde", 'w318a1c-18'),
        S("Ainsi, le score VIRSTA comprend des points pour les emboles, à la méningite, au dispositif intracardiaque, à l'endocardite antérieure, à l'usage de drogues, à la valvulopathie native et à la bactériémie persistante", 'w318a1c-102'),
        S("Un score inférieur à 3 a une valeur prédictive négative de 99,3 % pour l'endocardite, mais il classe environ 70 % des patients à haut risque", 'w318a1c-19')))
    o.append(p.P(
        S("Le deuxième différentiel est une autre infection métastatique ou un foyer primitif extracardiaque", 'wa9c851-7'),
        S("Parmi 289 épisodes où l'endocardite a été exclue, les diagnostics alternatifs les plus fréquents étaient les infections ostéo-articulaires, dans 23 % des cas, puis les bactériémies sur cathéter, dans 19 %", 'wa9c851-7'),
        S("La bactériémie à S. aureus provoque aussi une spondylodiscite et une arthrite septique, d'où la palpation du rachis et des articulations", 'w318a1c-2', 'w318a1c-13')))
    o.append(p.P(
        S("Troisième différentiel : l'infection d'un dispositif cardiaque, qui peut prendre la forme d'une infection de poche sans endocardite", 'wbea7b0-34'),
        S("Quatrième différentiel : l'endocardite à hémocultures négatives, souvent due à un antibiotique préalable, dans 35 % à 74 % des cas, ou à des germes à culture difficile", 'wc68439-16'),
        S("Le cinquième différentiel est une lésion thrombotique stérile, car la végétation débute comme un thrombus non infecté", 'wd98409-9')))
    o.append(p.P("Le tableau suivant résume pour chaque différentiel l'élément qui tranche, le piège et la conduite."))
    o.append(T(["Diagnostic", "Élément qui tranche", "Piège", "Conduite"], [
        ["Bactériémie à S. aureus sans endocardite" + c('w318a1c-19'), "Score VIRSTA, échographie", "Se fier à l'échographie transthoracique seule", "Échographie transœsophagienne selon le score"],
        ["Infection ostéo-articulaire ou sur cathéter" + c('wa9c851-7'), "Examen des articulations et du rachis, retrait du cathéter", "S'arrêter au premier foyer trouvé", "Traiter le foyer et chercher l'endocarde"],
        ["Infection de poche de dispositif" + c('wbea7b0-34'), "Hémocultures, imagerie de la sonde", "Dispositif porteur ne veut pas dire endocardite", "Extraction complète si infection prouvée" + c('wbea7b0-36')],
        ["Hémocultures négatives" + c('wc68439-16'), "Sérologies, PCR", "Antibiotique déjà donné", "Recherche de germes à culture difficile"],
    ]))
    o.append(p.P(
        S("Ce tableau rappelle qu'une imagerie négative n'exclut pas la maladie, car la sensibilité de l'échographie dépend de la taille de la lésion et du type de valve", 'w0c22e5-11', 'w0c22e5-13')))
    return ''.join(o)


def p05():
    p = Pt(5)
    o = []
    o.append(p.P(
        S("L'anamnèse cherche d'abord une fièvre, car elle reste le symptôme d'appel le plus fréquent, présente chez 61,5 % des patients d'une cohorte de 470 cas", 'wf45fc8-23', 'wf45fc8-20'),
        S("Les autres plaintes sont la dyspnée, dans 44,9 % des cas, les myalgies, dans 26,2 %, et les arthralgies, dans 21,9 %", 'wf45fc8-23'),
        S("Chaque question vise un mécanisme : la dyspnée évoque une insuffisance cardiaque par destruction valvulaire, et les douleurs articulaires une atteinte métastatique", 'wf45fc8-23', 'wf45fc8-24')))
    o.append(H4("5.a Questions ciblées et leur raison"))
    o.append(UL(
        S("Existe-t-il une valve prothétique, un dispositif cardiaque, une valve percutanée ou une endocardite antérieure ? Ces matériels et antécédents augmentent la probabilité de maladie", 'w0c22e5-26', 'w0c22e5-27'),
        S("Le patient est-il dialysé ou porteur d'un cathéter central ? Ces expositions aux soins constituent des portes d'entrée majeures", 'wbea7b0-9', 'wbea7b0-10'),
        S("Le patient s'injecte-t-il des drogues ? Cette pratique peut élever le risque jusqu'à 100 fois", 'wbea7b0-20'),
        S("Un acte invasif récent a-t-il eu lieu ? Chirurgie coronarienne, geste cutané, transfusion, dialyse, ponction de moelle ou bronchoscopie ont été associés à l'endocardite", 'w32d770-12'),
        S("Le patient a-t-il déjà reçu des antibiotiques ? Ils stérilisent les hémocultures et expliquent de nombreux cas sans germe isolé", 'wc68439-16'),
        S("Depuis quand dure la maladie ? Une évolution de plus d'un mois avant le diagnostic est associée à un meilleur pronostic", 'w37576c-5')))
    o.append(p.P(
        S("Chez la personne âgée, l'anamnèse doit rester large, car les symptômes généraux, la confusion ou une complication comme l'accident vasculaire peuvent masquer la fièvre", 'wbea7b0-6')))
    o.append(p.P("Le tableau suivant permet de relier chaque drapeau rouge à sa signification et à l'action immédiate."))
    o.append(T(["Drapeau rouge", "Signification", "Action immédiate"], [
        ["Fièvre avec prothèse valvulaire" + c('w0c22e5-27'), "Endocardite prothétique possible", "Hémocultures puis imagerie"],
        ["Bactériémie persistante à 48 h" + c('w318a1c-102'), "Foyer endovasculaire probable", "Échographie transœsophagienne"],
        ["Déficit neurologique" + c('wf45fc8-24'), "Embolie cérébrale, présente chez 18,9 % des patients", "Imagerie cérébrale urgente"],
        ["Dyspnée ou œdème" + c('wf45fc8-24'), "Insuffisance cardiaque valvulaire", "Avis cardiologique urgent"],
        ["Choc ou sepsis" + c('wf45fc8-24'), "Maladie grave, sepsis dans 20,9 % des cas", "Hémocultures sans délai puis antibiotiques" + c('wdb992c-6')],
    ]))
    o.append(p.P(
        S("Ces drapeaux orientent le tri : plus ils s'accumulent, plus l'endocardite doit passer devant les diagnostics fréquents", 'wf45fc8-24')))
    return ''.join(o)


def p06():
    p = Pt(6)
    o = []
    o.append(p.P(
        S("L'examen physique cherche à localiser l'infection et ses complications, car une bactériémie à S. aureus peut se manifester par une fièvre isolée ou par des signes à distance", 'w318a1c-10'),
        S("Le normal se définit d'abord : un cœur sain produit deux bruits sans souffle, et la ventilation normale est un murmure vésiculaire symétrique", 'w308a8c-11')))
    o.append(H4("6.a Cœur"))
    o.append(p.P(
        S("Un souffle holosystolique rectangulaire traduit une régurgitation mitrale ou tricuspidienne, et un souffle diastolique décroissant traduit une insuffisance aortique ou pulmonaire", 'w308a8c-6'),
        S("Les souffles diastoliques traduisent toujours une atteinte organique : ils débutent dès le bruit de fermeture de la valve, restent souvent doux et se recherchent avec la membrane du stéthoscope appuyée fermement", 'w308a8c-3'),
        S("Un souffle nouveau ou modifié doit donc faire évoquer une destruction valvulaire, qui s'observe dans 51,1 % des endocardites sous la forme d'une régurgitation modérée à sévère", 'wf45fc8-23')))
    o.append(p.P(
        S("Sur une prothèse aortique, un souffle diastolique de fuite signe en règle une fuite paravalvulaire par lâchage de sutures", 'w308a8c-10'),
        S("En revanche, sur une prothèse mitrale, un claquement d'ouverture assourdi ou l'apparition d'un roulement diastolique ou d'un souffle systolique évoque un dysfonctionnement", 'w308a8c-10')))
    o.append(H4("6.b Poumons, articulations, rachis et peau"))
    o.append(p.P(
        S("Des râles crépitants fins aux bases traduisent une insuffisance cardiaque gauche, et l'abolition du murmure vésiculaire évoque un épanchement pleural", 'w308a8c-11', 'w308a8c-12'),
        S("Ensuite, les articulations se recherchent pour une douleur, un érythème ou un épanchement, et le rachis pour une douleur à la palpation évoquant une ostéomyélite vertébrale", 'w318a1c-13'),
        S("Des manifestations cutanéomuqueuses sont présentes chez environ 18 % des patients atteints de bactériémie à S. aureus", 'w318a1c-10')))
    o.append(H4("6.c Neurologie, abords vasculaires et dispositifs"))
    o.append(p.P(
        S("Un examen neurologique soigneux s'impose, car l'embolie cérébrale touche 18,9 % des patients et le système nerveux central est le site d'embolisation le plus fréquent", 'wf45fc8-24', 'wa9c851-4'),
        S("Les sites de cathéter et les abords de dialyse sont inspectés, car un cathéter retenu augmente le risque de complications hématogènes comme l'endocardite", 'w318a1c-32'),
        S("La loge d'un stimulateur ou d'un défibrillateur est inspectée, car l'infection de poche peut coexister avec une endocardite sur sonde", 'wbea7b0-34')))
    o.append(p.P(
        S("Chez la personne âgée, les stigmates périphériques classiques manquent généralement, ce qui impose une vigilance accrue devant une bactériémie inexpliquée", 'wbea7b0-6')))
    return ''.join(o)


def p07():
    p = Pt(7)
    o = []
    o.append(p.P(
        S("L'approche syndromique regroupe les signes en six syndromes, car l'endocardite se présente tantôt comme une infection, tantôt comme une maladie valvulaire, embolique ou immunologique", 'wf45fc8-23', 'wf45fc8-24')))
    o.append(H4("7.1 Syndrome infectieux et bactériémique"))
    o.append(p.P(
        S("La fièvre touche 61,5 % des patients, avec des myalgies dans 26,2 % des cas et des arthralgies dans 21,9 %", 'wf45fc8-23'),
        S("Par ailleurs, un sepsis complique 20,9 % des épisodes", 'wf45fc8-24'),
        S("Le geste de recherche est l'hémoculture : deux paires correctement remplies, et répétées au moins une heure plus tard avant tout antibiotique", 'wdb992c-7', 'wdb992c-11')))
    o.append(H4("7.2 Syndrome valvulaire et insuffisance cardiaque"))
    o.append(p.P(
        S("La régurgitation modérée à sévère concerne 51,1 % des patients, et une insuffisance cardiaque nouvelle ou aggravée apparaît dans 27,9 % des cas", 'wf45fc8-23', 'wf45fc8-24'),
        S("Le geste de recherche est l'auscultation, puis l'échographie qui montre la fuite et la végétation", 'w308a8c-6', 'wb6a5b9-8')))
    o.append(H4("7.3 Syndrome embolique"))
    o.append(p.P(
        S("Les embolies septiques surviennent dans 25,1 % des cas et les embolies cérébrales dans 18,9 %", 'wf45fc8-24'),
        S("En effet, les événements emboliques sont présents dans 64 % des épisodes d'endocardite contre 17 % des épisodes sans endocardite", 'w0c22e5-29'),
        S("Le geste de recherche est l'examen neurologique, complété par une imagerie de l'encéphale et de l'abdomen", 'wa9c851-4', 'wb6a5b9-15')))
    o.append(H4("7.4 Syndrome immunologique"))
    o.append(p.P(
        S("Les phénomènes immunologiques s'observent dans 11 % des endocardites, et la glomérulonéphrite par complexes immuns en est une expression", 'w0c22e5-29', 'wf45fc8-30'),
        S("Le geste de recherche est l'analyse d'urine et le dosage de la créatinine, car l'atteinte rénale aggrave le pronostic", 'wf45fc8-28')))
    o.append(H4("7.5 Syndrome de dispositif"))
    o.append(p.P(
        S("Les infections de dispositifs vont de la poche à l'endocardite, et leur incidence se situe entre 0,5 % et 2,2 %", 'wbea7b0-34', 'wbea7b0-35'),
        S("Le geste de recherche est l'inspection de la loge, puis l'imagerie de la sonde, car l'échographie transœsophagienne perd de la sensibilité sur les dispositifs", 'wb6a5b9-9')))
    o.append(H4("7.6 Syndrome du cœur droit"))
    o.append(p.P(
        S("Chez la personne qui s'injecte des drogues, l'endocardite touche surtout la valve tricuspide native, mais la moitié des cas atteint aussi des valves gauches", 'wbea7b0-23'),
        S("La bactériémie à S. aureus peut donner des emboles pulmonaires septiques, ce qui fait rechercher toux, douleur thoracique et nodules pulmonaires", 'w318a1c-2')))
    o.append(p.P("Le tableau suivant permet de résumer les syndromes avec leurs signes fonctionnels et physiques."))
    o.append(T(["Syndrome", "Signes fonctionnels", "Signes physiques"], [
        ["Infectieux" + c('wf45fc8-23'), "Fièvre, myalgies, arthralgies", "Température élevée, signes de sepsis"],
        ["Valvulaire" + c('wf45fc8-23'), "Dyspnée", "Souffle nouveau, râles crépitants" + c('w308a8c-11')],
        ["Embolique" + c('wf45fc8-24'), "Déficit neurologique, douleur d'organe", "Signes neurologiques focaux"],
        ["Immunologique" + c('w0c22e5-29'), "Signes rénaux ou cutanés", "Atteinte cutanéomuqueuse" + c('w318a1c-10')],
        ["Dispositif" + c('wbea7b0-34'), "Douleur de poche", "Érythème ou écoulement de la loge"],
    ]))
    o.append(p.P(
        S("Un patient réunit souvent plusieurs syndromes, ce qui renforce la suspicion : une fièvre associée à une embolie cérébrale fait évoquer l'endocardite en priorité", 'w0c22e5-29')))
    return ''.join(o)
