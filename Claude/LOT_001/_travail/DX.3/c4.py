from h import *

def p11():
    p = Pt(11)
    o = []
    o.append(H4("11.A But"))
    o.append(p.P(
        S("Le traitement vise à éradiquer le germe de la végétation, à contrôler le foyer et à traiter les complications", 'w37576c-4'), S("La mortalité hospitalière reste élevée, entre 15 % et 30 %", 'w37576c-4'),
        S("Par ailleurs, l'équipe d'endocardite, composée de cardiologues, de chirurgiens cardiaques, d'infectiologues et de microbiologistes, discute chaque cas, notamment l'indication d'un passage à la voie orale", 'w37576c-33')))
    o.append(H4("11.B Moyens"))
    o.append(H4("Urgences, dans l'ordre chronologique"))
    o.append(p.P(
        S("La " + p.w("conduite chronologique d'urgence", fp(
            S("La première étape consiste à prélever deux paires d'hémocultures, puis les répéter au moins une heure plus tard, avant de débuter les antibiotiques", 'wdb992c-11'),
            S("En cas de choc septique, le délai de prélèvement reste très court", 'wdb992c-6'),
            S("La deuxième étape consiste à réaliser l'échographie, transthoracique puis transœsophagienne selon le contexte", 'wb6a5b9-8'),
            S("La troisième étape consiste à débuter l'antibiothérapie empirique adaptée à la valve, native ou prothétique, et à l'origine de l'infection, communautaire ou associée aux soins", 'wf45fc8-13'),
            S("La quatrième étape consiste à adapter le traitement au germe dans les 24 à 48 h, dès que les résultats de sensibilité sont connus", 'wf45fc8-14'))) +
          " est donc d'abord fondée sur les hémocultures", 'wdb992c-6'),
        S("Dans une cohorte multicentrique de 470 patients, le traitement empirique comportait de la vancomycine dans 45,7 % des cas et une céphalosporine de troisième génération dans 36,9 %", 'wf45fc8-37', 'wf45fc8-20'),
        S("Il n'était approprié que dans 51,2 % des cas et inapproprié dans 40,3 %, ce qui souligne la nécessité d'un schéma adapté au germe et aux résistances locales", 'wf45fc8-37')))
    o.append(p.P(
        S("Les schémas empiriques dépendent de la situation : pour une valve native ou une prothèse tardive, ils ciblent les staphylocoques, les streptocoques et les entérocoques", 'wf45fc8-13'), S("Ils ajoutent les staphylocoques à coagulase négative sur prothèse", 'wf45fc8-13'),
        S("En revanche, pour une prothèse précoce ou une infection associée aux soins, le spectre s'élargit aux staphylocoques résistants à la méthicilline, aux entérocoques et aux bacilles à Gram négatif hors HACEK", 'wf45fc8-13')))
    o.append(H4("Ordre du traitement et pharmacologie suisse"))
    o.append(p.P(
        S("La pharmacologie suit l'information professionnelle suisse publiée par Swissmedic, lue dans l'AIPS", 'aips-57236-79'),
        S("Vancomycine Sandoz i.v. (autorisation Swissmedic 57236) est indiquée dans l'endocardite infectieuse", 'aips-57236-2', 'aips-57236-79'),
        S("L'adulte reçoit 15 à 20 mg/kg toutes les 8 à 12 heures, avec une dose individuelle maximale de 2 g", 'aips-57236-5'), S("Une dose de charge de 25 à 30 mg/kg est possible chez les patients gravement malades", 'aips-57236-5'),
        S("Par ailleurs, dans l'endocardite à entérocoques, la vancomycine est efficace seulement en association avec un aminoside", 'aips-57236-3'),
        S("Elle est efficace sur l'endocardite précoce de prothèse à S. epidermidis en association avec la rifampicine ou un aminoside, pendant 4 à 6 semaines", 'aips-57236-3')))
    o.append(p.P(
        S("Flucloxacilline Stragen (autorisation Swissmedic 60092) comprend l'endocardite parmi ses indications, avec une voie parentérale pour les infections sévères", 'aips-60092-1', 'aips-60092-2', 'aips-60092-38'),
        S("L'endocardite à staphylocoques résistants à la pénicilline G reçoit 12 g par jour, associés à un antibiotique de la classe des aminosides", 'aips-60092-4'),
        S("En effet, la flucloxacilline est réservée aux staphylocoques producteurs de pénicillinase sensibles, avec exception des souches résistantes à la méthicilline", 'aips-60092-1')))
    o.append(p.P(
        S("Amoxicillin Delbert (autorisation Swissmedic 40712) comprend l'endocardite parmi les infections sévères", 'aips-40712-2', 'aips-40712-47'),
        S("Si l'infection est sévère, l'adulte reçoit 2 g en perfusion brève de 30 min, 3 à 6 fois par jour", 'aips-40712-4'),
        S("Ceftriaxon Labatec (autorisation Swissmedic 59876) se dose à 1 à 2 g une fois par jour, jusqu'à 4 g dans les infections sévères, mais ses indications citées ne nomment pas l'endocardite", 'aips-59876-4', 'aips-59876-1', 'aips-59876-67')))
    o.append(p.P(
        S("Gentamicine AApot (autorisation Swissmedic 33380) a une efficacité clinique prouvée dans l'endocardite à entérocoques et à streptocoques, en association avec la pénicilline et en l'absence de résistance de haut niveau", 'aips-33380-48', 'aips-33380-57'),
        S("La dose usuelle dans les infections sévères est de 3 mg/kg/jour en 3 doses égales, toutes les 8 heures, et elle peut aller jusqu'à 5 mg/kg/jour en cas de menace vitale", 'aips-33380-5'),
        S("Les pics ne doivent pas dépasser 10 à 12 mg/L, les concentrations résiduelles 2 mg/L, et la durée ne doit pas dépasser 7 à 10 jours si possible", 'aips-33380-20')))
    o.append(p.P("Le tableau suivant résume les cinq médicaments avec leur dose, leur voie et leur point de vigilance, tels que l'AIPS les décrit."))
    o.append(T(["Spécialité", "Dose AIPS", "Voie", "Vigilance"], [
        ["Vancomycine Sandoz i.v., 57236" + c('aips-57236-79'), "15 à 20 mg/kg toutes les 8 à 12 heures, maximum 2 g" + c('aips-57236-5'), "Intraveineuse", "Néphrotoxicité et ototoxicité" + c('aips-57236-25')],
        ["Flucloxacilline Stragen, 60092" + c('aips-60092-38'), "12 g par jour avec un aminoside" + c('aips-60092-4'), "Parentérale", "Contrôle hépatique et rénal" + c('aips-60092-12')],
        ["Amoxicillin Delbert, 40712" + c('aips-40712-47'), "2 g, 3 à 6 fois par jour" + c('aips-40712-4'), "Perfusion brève", "Hypersensibilité aux pénicillines" + c('aips-40712-9')],
        ["Ceftriaxon Labatec, 59876" + c('aips-59876-67'), "1 à 2 g par jour, jusqu'à 4 g" + c('aips-59876-4'), "Intraveineuse ou intramusculaire", "Solutions calciques chez le nouveau-né" + c('aips-59876-12')],
        ["Gentamicine AApot, 33380" + c('aips-33380-57'), "3 mg/kg/jour en 3 doses" + c('aips-33380-5'), "Intraveineuse lente ou intramusculaire", "Oto- et néphrotoxicité" + c('aips-33380-20')],
    ]))
    o.append(p.P(
        S("Plusieurs risques imposent de la prudence : la vancomycine est potentiellement néphrotoxique et ototoxique, et le risque augmente avec les doses élevées, la durée ou la prise d'autres médicaments toxiques", 'aips-57236-25'),
        S("La gentamicine est contre-indiquée en cas de myasthénie ou d'hypersensibilité aux aminosides", 'aips-33380-15'),
        S("La vancomycine et la gentamicine se potentialisent mutuellement sur les reins et l'oreille, ce qui impose une surveillance étroite si on les associe", 'aips-33380-26', 'aips-57236-38'),
        S("Les pénicillines sont contre-indiquées chez les patients hypersensibles aux pénicillines ou aux céphalosporines", 'aips-40712-9', 'aips-60092-5')))
    o.append(p.P(
        S("Pendant la grossesse, la gentamicine ne s'emploie qu'en cas d'indication menaçant le pronostic vital sans autre option, car elle franchit le placenta et une surdité congénitale a été rapportée", 'aips-33380-31'),
        S("La vancomycine peut être administrée à la femme enceinte seulement en cas de nécessité absolue", 'aips-57236-42'),
        S("Amoxicillin Delbert impose la prudence pendant la grossesse et ne doit pas être administré pendant l'allaitement, car il passe dans le lait", 'aips-40712-21', 'aips-40712-22')))
    o.append(H4("Traitements non pharmacologiques et chirurgie"))
    o.append(p.P(
        S("La chirurgie peut sauver la vie dans l'endocardite gauche : elle est discutée en cas d'insuffisance cardiaque, de prothèse valvulaire, d'infection récidivante, d'embolies répétées ou de complication locale comme un abcès", 'wa35a53-5'),
        S("En effet, une étude multicentrique a associé la chirurgie à une mortalité plus basse à six mois dans l'endocardite native gauche compliquée", 'wa35a53-6'),
        S("Après une valve aortique percutanée, une méta-analyse de 1557 patients n'a pas trouvé de différence de mortalité à court terme entre chirurgie et traitement médical, soit 9,7 % contre 8,4 %", 'wbea7b0-31')))
    o.append(p.P(
        S("Les dispositifs cardiaques infectés demandent en principe une extraction complète, car la rétention du matériel infecté est associée à une infection persistante et à des rechutes", 'wbea7b0-36', 'w37576c-42'),
        S("Les cathéters intravasculaires infectés sont retirés rapidement, car leur rétention augmente le risque de complications hématogènes, avec un risque relatif de 2,28", 'w318a1c-32')))
    o.append(H4("Relais oral partiel"))
    o.append(p.P(
        S("L'essai POET a randomisé 400 patients avec endocardite gauche à streptocoques, à E. faecalis, à S. aureus ou à staphylocoques à coagulase négative", 'w37576c-17'),
        S("Après au moins 10 jours d'antibiotiques intraveineux, 201 patients sont passés à la voie orale, et le critère composite est survenu chez 12,1 % d'entre eux contre 12,6 % sous traitement intraveineux", 'w37576c-17'),
        S("Par ailleurs, le suivi moyen de 5,4 ans a montré une mortalité de 23,4 % dans le groupe oral contre 35,2 % dans le groupe intraveineux", 'w37576c-20'), S("Une sélection des patients stables reste possible", 'w37576c-20')))
    o.append(p.P(
        S("Les recommandations européennes de 2023 admettent ce relais pour S. aureus, les streptocoques, E. faecalis et les staphylocoques à coagulase négative, dans un cadre précis", 'w37576c-33'),
        S("Les critères comprennent au moins 10 jours de traitement intraveineux, ou 7 jours après chirurgie", 'w37576c-34'), S("Ils exigent aussi l'absence d'indication chirurgicale à l'échographie transœsophagienne, un indice de masse corporelle inférieur à 40 kg/m2 et une absorption digestive normale", 'w37576c-34'),
        S("Les schémas oraux associent deux agents de classes différentes, par exemple la dicloxacilline avec la rifampicine pour S. aureus sensible", 'w37576c-19', 'w37576c-31'),
        S("La rifampicine ne doit pas être associée au linézolide, car elle réduit ses concentrations sériques", 'w37576c-32')))
    o.append(H4("Situations spéciales et aspects sociaux"))
    o.append(p.P(
        S("Chez les personnes qui s'injectent des drogues, l'accès veineux est difficile, ce qui rend le relais oral particulièrement utile, avec l'appui de l'addictologie", 'w37576c-41'),
        S("Les données en endocardite droite restent limitées", 'w37576c-41'),
        S("Après valve percutanée, la décision chirurgicale s'individualise selon l'expertise locale, le risque opératoire et le pronostic sous traitement médical", 'wbea7b0-31')))
    o.append(H4("11.C Surveillance"))
    o.append(p.P(
        S("Les hémocultures de contrôle se font une fois par jour pour documenter l'efficacité du traitement", 'wdb992c-11'),
        S("Les taux sanguins de vancomycine se contrôlent en cas de traitement à haute dose ou prolongé, surtout chez l'insuffisant rénal ou le malentendant", 'aips-57236-28'),
        S("Sous gentamicine, la fonction rénale se surveille avant, pendant et après le traitement, avec un contrôle de l'audition et de l'équilibre", 'aips-33380-20', 'aips-33380-16'),
        S("Après un relais oral, le suivi comprend une évaluation clinique régulière, des hémocultures si la fièvre revient, le dosage des marqueurs inflammatoires et une échographie si l'état se dégrade", 'w37576c-35')))
    o.append(H4("11.D Pronostic, guérison, critères de sortie"))
    o.append(p.P(
        S("Dans la cohorte de 470 patients, la mortalité hospitalière augmentait avec l'âge, l'endocardite associée aux soins et les végétations mobiles", 'wf45fc8-31', 'wf45fc8-20'),
        S("En effet, les patients décédés avaient des complications plus fréquentes : sepsis dans 46,0 % des cas contre 11,8 %", 'wf45fc8-30'), S("L'embolie septique touchait 52,4 % des décédés contre 15,3 %, et l'insuffisance rénale aiguë 34,7 % contre 5,8 %", 'wf45fc8-30'),
        S("Les critères de stabilité avant un relais oral comprennent une apyrexie d'au moins 48 h, une CRP inférieure à 20 mg/L ou à 25 % du pic", 'w37576c-37'), S("Il faut aussi des leucocytes inférieurs à 15 G/L et une échographie transœsophagienne sans indication chirurgicale", 'w37576c-37')))
    return ''.join(o)


def p12():
    p = Pt(12)
    o = []
    o.append(p.P(
        S("Le groupe d'experts suisse sur la prévention de l'endocardite a révisé ses recommandations en 2021, puis publié en 2025 un bilan de leur application", 'w32d770-3', 'w32d770-1'),
        S("La prévention repose sur deux piliers : un petit nombre de patients à haut risque reçoit une prophylaxie antibiotique, et tous les patients à risque reçoivent une éducation", 'w32d770-8', 'w32d770-10')))
    o.append(H4("12.a Prévention primaire"))
    o.append(p.P(
        S("Une feuille d'information pour tous les patients à risque a été publiée en 2021, avec la Fondation suisse de cardiologie", 'w32d770-8'), S("Elle vise à promouvoir l'hygiène dentaire et cutanée et de faire reconnaître les symptômes", 'w32d770-8', 'w32d770-9'),
        S("Une carte de prophylaxie est remise aux patients à haut risque", 'w32d770-7'),
        S("Une bonne santé bucco-dentaire importe plus qu'une dose d'antibiotique isolée, et les soins dentaires réguliers sont prioritaires", 'wd98409-14'),
        S("Une parodontite non traitée expose le patient à plus de bactériémies que les rendez-vous dentaires eux-mêmes, donc la traiter a plus de poids que la couverture antibiotique", 'wd98409-18')))
    o.append(p.P(
        S("Les conditions à haut risque comprennent une prothèse valvulaire ou un matériel prothétique de réparation, une endocardite antérieure et certaines cardiopathies congénitales, notamment cyanogènes non corrigées", 'wd98409-13'),
        S("Ainsi, les recommandations européennes de 2023 ont fait passer la prophylaxie de la classe IIa à la classe I pour ces patients", 'w32d770-11'),
        S("Elles recommandent la prophylaxie pour un dispositif d'assistance ventriculaire gauche en traitement définitif", 'w32d770-11'), S("Elles la proposent aussi pour les receveurs de greffe cardiaque et jusqu'à six mois après une réparation bord à bord transcatheter", 'w32d770-11')))
    o.append(p.P(
        S("La prophylaxie dentaire vise les actes qui manipulent la gencive ou la région périapicale, ou qui perforent la muqueuse buccale", 'wd98409-14'),
        S("Ensuite, le schéma consiste en une dose orale unique donnée peu avant l'acte, l'amoxicilline étant l'agent standard en l'absence d'allergie à la pénicilline", 'wd98409-30'),
        S("La posologie se lit dans l'information professionnelle suisse de l'amoxicilline avant toute prescription")))
    o.append(p.P(
        S("Pour les actes non dentaires, des études suédoise et anglaise ont lié l'endocardite à la chirurgie coronarienne, aux gestes cutanés, à la dialyse, aux endoscopies", 'w32d770-12'), S("Elles l'ont aussi liée à la pose de stimulateurs et de défibrillateurs", 'w32d770-12'),
        S("Par ailleurs, les recommandations pour ces actes figurent dans des publications destinées aux professionnels", 'w32d770-7')))
    o.append(p.P(
        S("Les sociétés savantes divergent : l'ESC et l'AHA réservent la prophylaxie aux patients à plus haut risque, alors que le NICE britannique la déconseille en pratique courante", 'wd98409-3', 'wd98409-22'),
        S("Aucun essai randomisé n'a testé la prophylaxie, ce qui explique le désaccord", 'wd98409-26')))
    o.append(H4("12.b Prévention secondaire et tertiaire"))
    o.append(p.P(
        S("Le retrait rapide des cathéters intravasculaires infectés prévient les complications hématogènes comme l'endocardite", 'w318a1c-32'),
        S("Chez les personnes qui s'injectent des drogues, la poursuite de la consommation entraîne des récidives, et l'addictologie doit s'intégrer au traitement", 'wbea7b0-24', 'w37576c-41'),
        S("Le patient guéri garde un risque de récidive, ce qui le fait entrer dans la catégorie à haut risque avec éducation et carte de prophylaxie", 'wd98409-13', 'w32d770-8')))
    return ''.join(o)


def p13():
    p = Pt(13)
    o = []
    o.append(UL(
        S("Une fièvre avec sueurs chez un patient porteur de prothèse, de dispositif ou de cardiopathie doit faire chercher une endocardite avant tout autre diagnostic", 'w0c22e5-27'),
        S("Les hémocultures, deux paires correctement remplies, précèdent toujours l'antibiothérapie", 'wdb992c-1', 'wdb992c-7'),
        S("Une échographie transthoracique négative n'exclut pas la maladie, et l'échographie transœsophagienne ou une imagerie complémentaire peut prendre le relais", 'w0c22e5-13'),
        S("Les équipes d'endocardite décident ensemble de la chirurgie et du relais oral", 'w37576c-33'),
        S("La prophylaxie antibiotique ne concerne que les patients à haut risque avant des actes dentaires précis", 'w32d770-8', 'wd98409-14')))
    return ''.join(o)


def p14():
    p = Pt(14)
    o = []
    o.append(p.P(
        S("Les questions d'examen fédéral portent surtout sur le tri des urgences, l'ordre des examens et le choix des médicaments", 'wdb992c-6'),
        "Le tableau suivant permet de présenter chaque piège sous forme de question, de réponse et de raison."))
    o.append(T(["Question", "Réponse", "Raison"], [
        ["Faut-il débuter l'antibiotique avant les hémocultures dans un état stable ?" + c('wdb992c-6'), "Non, les hémocultures passent d'abord", "Un antibiotique préalable stérilise le sang" + c('wc68439-16')],
        ["Une seule paire d'hémocultures suffit-elle ?" + c('wdb992c-7'), "Non, deux paires", "Une seule paire a un mauvais rendement diagnostique" + c('wdb992c-7')],
        ["Une échographie transthoracique normale exclut-elle l'endocardite ?" + c('w0c22e5-11'), "Non", "Sa sensibilité pour les végétations est de 40 % à 63 %" + c('w0c22e5-11')],
        ["Répéter l'échographie transthoracique suffit-il ?" + c('w0c22e5-6'), "Non, préférer une imagerie plus sensible", "Elle n'a reclassé que 1 % des cas" + c('w0c22e5-6')],
        ["Une bactériémie à S. aureus exige-t-elle une échographie ?" + c('w318a1c-18'), "Oui, chez tous", "Environ 12 % développent une endocardite" + c('w318a1c-18')],
        ["Un porteur de dispositif avec hémocultures positives a-t-il une endocardite ?" + c('wbea7b0-34'), "Pas forcément", "Le risque dépend du germe, de la durée et de la source" + c('wbea7b0-34')],
        ["La gentamicine seule traite-t-elle l'endocardite ?" + c('aips-33380-1'), "Non, jamais seule", "Elle s'emploie en combinaison, notamment avec la pénicilline" + c('aips-33380-48')],
        ["La vancomycine suffit-elle contre un entérocoque ?" + c('aips-57236-3'), "Non", "Elle n'est efficace qu'avec un aminoside" + c('aips-57236-3')],
        ["Faut-il une prophylaxie pour tout cardiaque ?" + c('w32d770-8'), "Non", "Elle est réservée aux patients à haut risque" + c('w32d770-8')],
    ]))
    o.append(p.P(
        S("Un autre piège vient de la fièvre qui baisse : la disparition de la fièvre ne prouve pas la guérison, car l'abcès peut progresser, et le suivi repose sur les hémocultures quotidiennes", 'wdb992c-11'),
        S("Enfin, l'âge ne protège pas : chez la personne âgée, la maladie se présente de façon atypique, avec un tableau général peu spécifique", 'wbea7b0-6')))
    return ''.join(o)
