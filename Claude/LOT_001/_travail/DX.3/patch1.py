import glob
R=[
# nombres
("S(\"L'anamnèse cherche d'abord une fièvre, car elle reste le symptôme d'appel le plus fréquent, présente chez 61,5 % des patients d'une cohorte de 470 cas\", 'wf45fc8-23')","S(\"L'anamnèse cherche d'abord une fièvre, car elle reste le symptôme d'appel le plus fréquent, présente chez 61,5 % des patients d'une cohorte de 470 cas\", 'wf45fc8-23', 'wf45fc8-20')"),
("Hémocultures en moins de 30 minutes puis antibiotiques","Hémocultures sans délai puis antibiotiques"),
("deux paires, remplies chacune de 8 à 10 ml, et répétées","deux paires correctement remplies, et répétées"),
("de 8 à 10 ml par flacon, et du nombre de flacons","du remplissage correct des flacons et de leur nombre"),
("avec un délai inférieur à 30 min en cas de choc septique","avec un délai très court en cas de choc septique"),
("et jamais plus de 3 paires par 24 h","et jamais plus de 3 paires par jour"),
("alors les hémocultures sont prélevées en moins de 30 min, puis","alors les hémocultures sont prélevées sans délai, puis"),
("En cas de choc septique, le délai de prélèvement reste inférieur à 30 min.","En cas de choc septique, le délai de prélèvement reste très court."),
("Dans une cohorte multicentrique de 470 patients, le traitement empirique comportait de la vancomycine dans 45,7 % des cas et une céphalosporine de troisième génération dans 36,9 %\", 'wf45fc8-37')","Dans une cohorte multicentrique de 470 patients, le traitement empirique comportait de la vancomycine dans 45,7 % des cas et une céphalosporine de troisième génération dans 36,9 %\", 'wf45fc8-37', 'wf45fc8-20')"),
("S(\"Dans la cohorte de 470 patients, la mortalité hospitalière augmentait avec l'âge, l'endocardite associée aux soins et les végétations mobiles\", 'wf45fc8-31')","S(\"Dans la cohorte de 470 patients, la mortalité hospitalière augmentait avec l'âge, l'endocardite associée aux soins et les végétations mobiles\", 'wf45fc8-31', 'wf45fc8-20')"),
("puis publié en 2025 un bilan de leur application\", 'w32d770-3')","puis publié en 2025 un bilan de leur application\", 'w32d770-3', 'w32d770-1')"),
("jusqu'à 6 mois après","jusqu'à six mois après"),
("deux paires remplies chacune de 8 à 10 ml, précèdent","deux paires correctement remplies, précèdent"),
# longues
("n'a pas forcément une infection de sonde, car le risque dépend","n'a pas forcément une infection de sonde\", 'wbea7b0-34'), S(\"Le risque dépend"),
(", ou lorsqu'elle est diagnostiquée dans les 48 h chez",
 "\", 'wf45fc8-9'), S(\"Elle l'est aussi lorsqu'elle est diagnostiquée dans les 48 h chez"),
("créent d'autres portes d'entrée : une étude suédoise","créent d'autres portes d'entrée\", 'w32d770-12'), S(\"Une étude suédoise"),
("dans 51,1 % des cas, des fuites paravalvulaires","dans 51,1 % des cas\", 'wf45fc8-23'), S(\"Elle provoque aussi des fuites paravalvulaires"),
("les diagnostics graves : l'endocardite en fait partie lorsque","les diagnostics graves\", 'w0c22e5-26'), S(\"L'endocardite en fait partie lorsque"),
("ou de l'autopsie : culture de la végétation","ou de l'autopsie\", 'w0c22e5-30'), S(\"Il comprend la culture de la végétation"),
("avant les antibiotiques, puis d'un suivi une fois par jour pour documenter","avant les antibiotiques\", 'wdb992c-11'), S(\"Un suivi quotidien documente ensuite"),
("dans 61,9 % des cas, des microsaignements dans","dans 61,9 % des cas\", 'wb6a5b9-15'), S(\"Elle a aussi trouvé des microsaignements dans"),
(" par les Européens, alors que les Américains conseillent"," par les Européens\", 'w0c22e5-15'), S(\"Les Américains conseillent"),
(" dans 3 %, et la sensibilité pour les végétations est passée"," dans 3 %\", 'w0c22e5-6'), S(\"La sensibilité pour les végétations est passée"),
("dans la bactériémie à S. aureus : l'échographie est faite","dans la bactériémie à S. aureus\", 'w318a1c-18'), S(\"L'échographie est faite"),
("et à traiter les complications, car la mortalité hospitalière de l'endocardite se situe","et à traiter les complications\", 'w37576c-4'), S(\"La mortalité hospitalière de l'endocardite se situe"),
("entérocoques, avec en plus les staphylocoques à coagulase négative sur prothèse","entérocoques\", 'wf45fc8-13'), S(\"Ils ajoutent les staphylocoques à coagulase négative sur prothèse"),
(", et une dose de charge de 25 à 30 mg/kg chez les patients gravement malades","\", 'aips-57236-5'), S(\"Une dose de charge de 25 à 30 mg/kg est possible chez les patients gravement malades"),
(", l'absence d'indication chirurgicale à l'échographie transœsophagienne, un indice",
 "\", 'w37576c-34'), S(\"Ils exigent aussi l'absence d'indication chirurgicale à l'échographie transœsophagienne, un indice"),
(", embolie septique dans 52,4 % contre 15,3 % et insuffisance rénale aiguë dans 34,7 % contre 5,8 %","\", 'wf45fc8-30'), S(\"L'embolie septique touchait 52,4 % des décédés contre 15,3 %, et l'insuffisance rénale aiguë 34,7 % contre 5,8 %"),
(", des leucocytes inférieurs à 15 G/L et une échographie",
 "\", 'w37576c-37'), S(\"Il faut aussi des leucocytes inférieurs à 15 G/L et une échographie"),
(", afin de promouvoir l'hygiène dentaire",
 "\", 'w32d770-8'), S(\"Elle vise à promouvoir l'hygiène dentaire"),
(", et la proposent pour les receveurs de greffe cardiaque et jusqu'à six mois après",
 "\", 'w32d770-11'), S(\"Elles la proposent aussi pour les receveurs de greffe cardiaque et jusqu'à six mois après"),
(", ainsi qu'à la pose de stimulateurs","\", 'w32d770-12'), S(\"Elles l'ont aussi liée à la pose de stimulateurs"),
# nominales
("La végétation naît d'une lésion","La végétation est issue d'une lésion"),
("Le tableau suivant rassemble les chiffres à retenir","Le tableau suivant permet de retenir les chiffres"),
("Le tableau suivant relie chaque drapeau rouge","Le tableau suivant permet de relier chaque drapeau rouge"),
("Le tableau suivant résume les syndromes","Le tableau suivant permet de résumer les syndromes"),
("Le tableau suivant liste les critères avec leur usage.","Le tableau suivant permet de classer les critères selon leur usage."),
("Le tableau suivant relie le résultat à sa signification","Le tableau suivant permet de relier le résultat à sa signification"),
("Le tableau suivant présente chaque piège","Le tableau suivant permet de présenter chaque piège"),
("Le score VIRSTA attribue des points aux","Le score VIRSTA comprend des points pour les"),
("Deuxième différentiel : une autre infection","Le deuxième différentiel est une autre infection"),
("Cinquième différentiel : une lésion","Le cinquième différentiel est une lésion"),
("Cette pratique élève le risque","Cette pratique peut élever le risque"),
("L'arbre décisionnel commence par l'exclusion des urgences, puis discrimine les diagnostics fréquents","L'arbre décisionnel est organisé ainsi : exclusion des urgences d'abord, puis discrimination des diagnostics fréquents"),
('" commence donc par les hémocultures"','" est donc d\'abord fondée sur les hémocultures"'),
("Première étape : prélever","La première étape consiste à prélever"),
("Deuxième étape : réaliser","La deuxième étape consiste à réaliser"),
("Troisième étape : débuter","La troisième étape consiste à débuter"),
("Quatrième étape : adapter","La quatrième étape consiste à adapter"),
("Dans l'endocardite à entérocoques, la vancomycine n'est efficace qu'en association avec un aminoside","Dans l'endocardite à entérocoques, la vancomycine est efficace seulement en association avec un aminoside"),
("La vancomycine ne s'administre à la femme enceinte qu'en cas de nécessité absolue","La vancomycine peut être administrée à la femme enceinte seulement en cas de nécessité absolue"),
("Flucloxacilline Stragen (autorisation Swissmedic 60092) cite l'endocardite parmi ses indications","Flucloxacilline Stragen (autorisation Swissmedic 60092) comprend l'endocardite parmi ses indications"),
("Amoxicillin Delbert (autorisation Swissmedic 40712) cite l'endocardite","Amoxicillin Delbert (autorisation Swissmedic 40712) comprend l'endocardite"),
("transœsophagienne ou une imagerie complémentaire prend le relais","transœsophagienne ou une imagerie complémentaire peut prendre le relais"),
]
fs=['c1.py','c2.py','c3.py','c4.py']
T={f:open(f).read() for f in fs}
for old,new in R:
    n=sum(t.count(old) for t in T.values())
    if n!=1: print('!!',n,old[:70]); continue
    for f in fs:
        if old in T[f]: T[f]=T[f].replace(old,new)
for f in fs: open(f,'w').write(T[f])
