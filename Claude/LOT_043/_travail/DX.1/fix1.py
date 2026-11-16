import re
R=[
('p01',"Le tableau suivant résume les entités voisines et la façon de les séparer du syndrome de la paroi thoracique de topographie banale.","Le tableau suivant permet de séparer les entités voisines du syndrome de la paroi thoracique de topographie banale."),
('p02',"La revue suisse de 2007 situe la douleur d'origine pariétale entre 28 et 49 % des douleurs thoraciques vues en médecine de premier recours.","La revue suisse de 2007 indique que la douleur d'origine pariétale est retrouvée dans 28 à 49 % des douleurs thoraciques vues en médecine de premier recours."),
('p02',"Le même syndrome pèse moins dans les services d'urgence et en préhospitalier, où la douleur d'origine cardiaque domine.","Le même syndrome est moins fréquent dans les services d'urgence et en préhospitalier, car la douleur d'origine cardiaque y domine."),
('p02',"La revue suisse de 2007 résume l'opposition en soulignant une prédominance de douleurs d'origine pariétale en médecine ambulatoire, contre une prédominance cardiaque aux urgences.","La revue suisse de 2007 montre que la prédominance est pariétale en médecine ambulatoire, alors qu'elle est cardiaque aux urgences."),
('p02',"Le médecin s'inquiète lui aussi dans 10 % des douleurs modérées et dans 26 % des douleurs aiguës.","Le médecin est lui aussi inquiet dans 10 % des douleurs modérées et dans 26 % des douleurs aiguës."),
('p03',"Le geste sportif ou professionnel répétitif joue le même rôle : une douleur musculaire d'effort ou post-traumatique figure dans le diagnostic différentiel des affections de la paroi.","Le geste sportif ou professionnel répétitif peut jouer le même rôle, car une douleur musculaire d'effort ou post-traumatique est un diagnostic différentiel des affections de la paroi."),
('p03',"Poser un diagnostic précis de syndrome de la paroi thoracique rassure davantage que la seule exclusion d'une maladie grave sans diagnostic précis.","Un diagnostic précis de syndrome de la paroi thoracique est plus rassurant que la seule exclusion d'une maladie grave sans diagnostic précis."),
('p03',"Le pneumothorax donne une douleur à début aigu associée à une dyspnée.","Le pneumothorax peut donner une douleur à début aigu associée à une dyspnée."),
('p04',"Le syndrome de la paroi thoracique n'est donc retenu qu'après cette première étape.","Le diagnostic de paroi est donc retenu seulement après cette première étape."),
('p04',"À l'inverse, la douleur continue ou très prolongée, sans lien avec l'activité, déclenchée par l'inspiration ou accompagnée de vertiges, de palpitations, de fourmillements ou de dysphagie rend l'angor stable peu probable.","À l'inverse, l'angor stable est peu probable lorsque la douleur est continue ou très prolongée, sans lien avec l'activité, déclenchée par l'inspiration ou accompagnée de vertiges, de palpitations, de fourmillements ou de dysphagie."),
('p05',"Le guide NICE demande ensuite de chercher","Le guide NICE recommande ensuite de chercher"),
('p05',"Le guide NICE ajoute à la liste l'âge, le sexe masculin,","Le guide NICE précise aussi les éléments qui augmentent la probabilité d'angor : l'âge, le sexe masculin,"),
('p05',"Le tableau suivant relie chaque drapeau rouge à sa signification et à l'action immédiate.","Le tableau suivant permet de relier chaque drapeau rouge à sa signification et à l'action immédiate."),
('p06',"La douleur reproduite par la palpation entre dans la règle de prédiction du syndrome de la paroi,","La douleur reproduite par la palpation fait partie de la règle de prédiction du syndrome de la paroi,"),
('p06',"Le tableau suivant résume la valeur et le piège de chaque geste.","Le tableau suivant permet de comparer la valeur et le piège de chaque geste."),
('p07',"Le tableau suivant regroupe les syndromes avec leurs signes.","Le tableau suivant permet de comparer les syndromes et leurs signes."),
('p08',"La règle de Ronga situe la probabilité du syndrome en dessous de 10 % pour 0 à 1 point,","La règle de Ronga indique une probabilité du syndrome inférieure à 10 % pour 0 à 1 point,"),
('p08',"La définition de la douleur angineuse du guide NICE aide à ne pas confondre les deux situations.","La définition de la douleur angineuse du guide NICE permet de ne pas confondre les deux situations."),
('p09',"Le guide NICE demande de le réaliser dès que possible","Le guide NICE recommande de le réaliser dès que possible"),
('p09',"Le guide NICE la réserve à la suspicion d'une autre maladie, comme une tumeur pulmonaire.","Le guide NICE recommande de la réserver à la suspicion d'une autre maladie, comme une tumeur pulmonaire."),
('p09',"En l'absence de situation aiguë, le médecin demande l'ergométrie,","En l'absence de situation aiguë, le médecin peut demander l'ergométrie,"),
('p09',"Pour une douleur d'origine digestive suspectée, un inhibiteur de la pompe à protons pendant un à deux mois sert de test diagnostique, et l'endoscopie n'est indiquée qu'en cas de non-réponse ou de symptômes d'alarme.","Pour une douleur digestive suspectée, un inhibiteur de la pompe à protons donné pendant un à deux mois est un test diagnostique, et l'endoscopie est indiquée seulement en cas de non-réponse ou de symptômes d'alarme."),
('p09',"Le seuil de 500 s'applique aux D-dimères dosés au cabinet.","Le seuil de 500 est celui des D-dimères dosés au cabinet."),
('p11',"Quatrième temps, avant l'arrivée de l'ambulance : poser une voie veineuse, donner de l'oxygène, de l'acide acétylsalicylique par voie intraveineuse et de la nitroglycérine par voie sublinguale, puis enregistrer un électrocardiogramme, selon l'atelier des HUG sur les douleurs thoraciques en ambulatoire.","Quatrième temps, avant l'arrivée de l'ambulance : le médecin pose une voie veineuse, donne de l'oxygène, de l'acide acétylsalicylique par voie intraveineuse et de la nitroglycérine par voie sublinguale, puis enregistre un électrocardiogramme, selon l'atelier des HUG."),
('p11',"La réponse à la trinitrine ne sert pas à poser le diagnostic.","La réponse à la trinitrine ne permet pas de poser le diagnostic."),
('p11',"La surveillance combine la réévaluation de la douleur et la vigilance sur les effets indésirables.","La surveillance comprend la réévaluation de la douleur et la vigilance sur les effets indésirables."),
('p12',"La prévention secondaire inclut la prévention des complications médicamenteuses.","La prévention secondaire comprend aussi la prévention des complications médicamenteuses."),
('p14',"Le résumé de 2008 donne 43 %","Le résumé de 2008 indique 43 %"),
]
for p,a,b in R:
    f=f'src/{p}.txt'; t=open(f).read()
    if a not in t: print('MISS',p,a[:60]); continue
    open(f,'w').write(t.replace(a,b,1))
