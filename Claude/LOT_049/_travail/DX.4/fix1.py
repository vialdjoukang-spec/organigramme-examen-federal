import glob,re
R=[
("En Suisse, la cohorte CAPNETZ renseigne la bactériologie","En Suisse, la cohorte CAPNETZ permet de décrire la bactériologie"),
("Streptococcus pneumoniae occupe la première place, suivi de Haemophilus influenzae","Streptococcus pneumoniae est le plus fréquent, suivi de Haemophilus influenzae"),
("L'empyème présente la plus forte proportion de ces signes.","L'empyème montre la plus forte proportion de ces signes."),
("Cette liste guide la première minute de l'évaluation, donc avant toute idée de pneumonie.","Cette liste permet de guider la première minute de l'évaluation, donc avant toute idée de pneumonie."),
("L'imagerie tranche donc entre l'air","L'imagerie permet donc de trancher entre l'air"),
("Un pneumothorax sous tension figure d'ailleurs parmi les douleurs thoraciques menaçant le pronostic vital.","Un pneumothorax sous tension est d'ailleurs l'une des causes de douleur thoracique menaçant le pronostic vital."),
("L'embolie pulmonaire figure parmi les diagnostics à exclure devant","L'embolie pulmonaire est l'un des diagnostics à exclure devant"),
("L'anamnèse sert à reconnaître la gravité, à préciser le germe probable et à repérer le terrain à risque.","L'anamnèse permet de reconnaître la gravité, de préciser le germe probable et de repérer le terrain à risque."),
("figure parmi les signes de détresse à rechercher chez l'enfant","fait partie des signes de détresse à rechercher chez l'enfant"),
("Mycoplasma pneumoniae prévaut chez","Mycoplasma pneumoniae est fréquent chez"),
("Le grunting résulte d'une fermeture","Le grunting est dû à une fermeture"),
("l'obstruction des voies aériennes, sert surtout de diagnostic différentiel.","l'obstruction des voies aériennes, est surtout un diagnostic différentiel."),
("Le médecin retrouve une abolition","Le médecin recherche une abolition"),
("mérite d'être cherché chez l'adulte","doit être cherché chez l'adulte"),
("Le syndrome de condensation désigne la perte","Le syndrome de condensation correspond à la perte"),
("Le choix de l'algorithme dépend donc du contexte clinique.","Le choix de l'algorithme varie donc selon le contexte clinique."),
("Le score RAPID stratifie le risque de décès à l'admission.","Le score RAPID permet de stratifier le risque de décès à l'admission."),
("L'échographie pulmonaire gagne du terrain comme imagerie de première intention.","L'échographie pulmonaire est de plus en plus utilisée comme imagerie de première intention."),
("La gazométrie n'est pas recommandée de routine, tout comme la CRP et la procalcitonine.","La gazométrie, la CRP et la procalcitonine ne sont pas recommandées de routine."),
("Une culture négative n'exclut donc pas l'infection pleurale.","Une culture négative ne permet donc pas d'exclure l'infection pleurale."),
("L'arbre décisionnel part de l'urgence vitale pour descendre vers l'infection pleurale.","L'arbre décisionnel va de l'urgence vitale à l'infection pleurale."),
("En revanche, un score élevé ne prouve pas qu'une escalade","En revanche, un score élevé ne permet pas de conclure qu'une escalade"),
("l'information professionnelle envisage une administration par voie intraveineuse","l'information professionnelle recommande d'envisager une administration par voie intraveineuse"),
("La durée de l'antibiothérapie dépend du germe et des complications.","La durée de l'antibiothérapie varie selon le germe et les complications."),
("La fibrinolyse intrapleurale s'adresse aux collections cloisonnées dont le drainage échoue.","La fibrinolyse intrapleurale est réservée aux collections cloisonnées dont le drainage échoue."),
("L'examen fédéral teste surtout les décisions à risque, pas la mémoire des chiffres.","L'examen fédéral porte surtout sur les décisions à risque, pas sur la mémoire des chiffres."),
("Non, car près d'un tiers des patients avec infection pleurale n'ont pas de pneumonie visible à l'imagerie.","Non, car près d'un tiers des patients avec infection pleurale ont une imagerie sans pneumonie visible."),
("L'imagerie départage les deux diagnostics.","L'imagerie permet de départager les deux diagnostics."),
# longues
("classent parmi les causes menaçant le pronostic vital le syndrome coronarien aigu, l'embolie pulmonaire, la dissection aortique, la myocardite, le pneumothorax sous tension et la péricardite.[[wfba9d7-2]]","listent les causes menaçant le pronostic vital.[[wfba9d7-2]] Elles citent le syndrome coronarien aigu, l'embolie pulmonaire, la dissection aortique, la myocardite, le pneumothorax sous tension et la péricardite.[[wfba9d7-2]]"),
("Ce score additionne la confusion, une fréquence respiratoire supérieure à 30 par minute, une pression artérielle systolique inférieure à 90 mmHg ou diastolique inférieure à 60 mmHg, et l'âge supérieur à 65 ans.[[w523b30-26]]","Ce score additionne la confusion et une fréquence respiratoire supérieure à 30 par minute.[[w523b30-26]] Il ajoute une pression artérielle systolique inférieure à 90 mmHg ou diastolique inférieure à 60 mmHg, et l'âge supérieur à 65 ans.[[w523b30-26]]"),
("Une cohorte adulte retient au moins un critère parmi le pus franc, un Gram ou une culture pleurale positifs, un pH pleural inférieur ou égal à 7.20, un glucose pleural inférieur ou égal à 40 mg/dL, ou un cloisonnement.[[w98dc10-10]]","Une cohorte adulte retient au moins un critère pleural, comme le pus franc, un Gram ou une culture positifs, ou un cloisonnement.[[w98dc10-10]] Elle retient aussi un pH pleural inférieur ou égal à 7.20 ou un glucose pleural inférieur ou égal à 40 mg/dL.[[w98dc10-10]]"),
("Les précautions de base s'appliquent à tout patient, et la prise en charge sociale comprend la déclaration des maladies à déclaration obligatoire comme la légionellose, la coxiellose ou une maladie invasive à Haemophilus.","Les précautions de base s'appliquent à tout patient. La prise en charge sociale comprend la déclaration des maladies à déclaration obligatoire, comme la légionellose, la coxiellose ou une maladie invasive à Haemophilus."),
("Le vaccin contre la coqueluche concerne tous les enfants, avec une primovaccination à 2 et 4 mois et des rappels à 12 mois, entre 4 et 7 ans, puis entre 11 et 15 ans.[[w523b30-57]]","Le vaccin contre la coqueluche concerne tous les enfants.[[w523b30-57]] La primovaccination se fait à 2 et 4 mois, puis des rappels sont donnés à 12 mois, entre 4 et 7 ans, puis entre 11 et 15 ans.[[w523b30-57]]"),
# nombres/cites
("Parmi 234 adultes inclus entre 2016 et 2021, le pneumocoque était identifié par les méthodes conventionnelles chez 37 patients, soit 15.8 %.[[w299098-6,w299098-3]]","Parmi 234 adultes inclus entre 2016 et 2021, le pneumocoque était identifié par les méthodes conventionnelles chez 37 patients, soit 15.8 %.[[w299098-6,w299098-4]]"),
("La gravité se mesure par le score CRB-65 et par le jugement clinique, qui l'emporte sur le score.[[w523b30-3]]","La gravité se mesure par le score CRB-65 et par le jugement clinique, qui l'emporte sur le score.[[w523b30-3,w523b30-26]]"),
("Une étude japonaise de 2026 a comparé","Une étude japonaise a comparé"),
("au plus tôt 6 mois après la dernière dose","au plus tôt six mois après la dernière dose"),
("Enfin, un échec du traitement à 48 heures doit remettre en question le diagnostic initial.","Enfin, un échec du traitement doit remettre en question le diagnostic initial."),
("L'examen se termine par l'évaluation de la gravité avec le score CRB-65.","L'examen se termine par l'évaluation de la gravité avec le score CRB-65.[[w523b30-26]]"),
("La gravité de la pneumonie se mesure avec des scores validés pour prédire la mortalité à 30 jours.[[w523b30-23]]","La gravité de la pneumonie se mesure avec des scores validés pour prédire la mortalité à 30 jours.[[w523b30-23]]"),
]
import collections
files={f:open(f).read() for f in glob.glob('src/p*.txt')}
for a,b in R:
    done=False
    for f,t in files.items():
        if a in t: files[f]=t.replace(a,b,1); done=True; break
    if not done: print('MISS',a[:60])
for f,t in files.items(): open(f,'w').write(t)
