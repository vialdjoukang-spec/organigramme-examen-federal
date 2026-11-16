import re,sys
def rep(f,start,new):
    p=f'src/{f}.html'; s=open(p).read()
    i=s.find(start)
    if i<0: print('NOT FOUND',f,start[:50]); return
    m=re.compile(r'[.?!](?:\[\[[^\]]*\]\])*').search(s,i+len(start)-1)
    # sentence ends at first sentence-final punctuation followed by optional cites AND then space/tag/end
    j=i
    while True:
        m=re.compile(r'[.?!](?:\[\[[^\]]*\]\])*').search(s,j)
        if not m: print('no end',f,start[:40]); return
        nxt=s[m.end():m.end()+1]
        if nxt in (' ','<','\n','') : break
        j=m.end()
    s=s[:i]+new+s[m.end():]
    open(p,'w').write(s)
R=[
('p01',"Elle définit le carcinome comme","Elle définit le carcinome comme une prolifération épithéliale néoplasique qui franchit la membrane basale pour atteindre le stroma de la muqueuse.[[DE.114]] Il peut ensuite atteindre la sous-muqueuse et les couches plus profondes.[[DE.114]]"),
('p01',"La Société européenne d'oncologie médicale (ESMO) a publié","La Société européenne d'oncologie médicale (ESMO) a publié en 2022 sa recommandation sur le diagnostic, le traitement et le suivi du cancer de l'œsophage.[[EM.1]]"),
('p01',"La classification TNM range","La classification TNM range parmi les cancers de l'œsophage toute tumeur dont le centre se situe à moins de 2 cm de la jonction œsogastrique.[[DE.116]]"),
('p01',"Les tumeurs de la jonction dont le centre","Les tumeurs de la jonction centrées dans les 2 premiers centimètres du cardia suivent le même schéma, ce sont les types I et II de Siewert.[[DE.116]]"),
('p01',"Dans l'épithélium épidermoïde, le risque de carcinome","Dans l'épithélium épidermoïde, le risque de carcinome augmente avec la gravité de la dysplasie.[[DE.109]] Il atteint 2,9 % pour la dysplasie de bas grade, 28,3 % pour celle de haut grade et 34,4 % pour le carcinome in situ.[[DE.109]]"),
('p01',"Le carcinome in situ ne diffère pas","Le carcinome in situ ne diffère pas de la dysplasie de haut grade par son comportement biologique.[[DE.109]] La classification de l'Organisation mondiale de la Santé les regroupe donc sous le même terme.[[DE.109]]"),
('p01',"Ce cancer ne résume pas la dysphagie","Ce cancer ne résume pas la dysphagie, car celle-ci a de nombreuses causes non tumorales.[[DE.69]] Ce sont le reflux œsophagien, la hernie hiatale, les anneaux, l'œsophagite à éosinophiles et les diverticules.[[DE.69]]"),
('p01',"L'incidence de l'Office fédéral de la statistique compte","L'incidence de l'Office fédéral de la statistique compte les nouveaux cas de cancer de l'œsophage.[[OF.116]] Elle ne mesure donc pas la fréquence de la dysphagie dans la population.[[OF.116]]"),
('p02',"Le carcinome épidermoïde prédomine","Le carcinome épidermoïde est plus fréquent dans la partie supérieure de l'œsophage, alors que l'adénocarcinome est plus fréquent dans la partie inférieure.[[OF.115]]"),
('p02',"La Suisse présente pourtant","La Suisse a pourtant le taux de survie le plus élevé parmi les pays européens comparés par l'Office fédéral de la statistique.[[OF.124]]"),
('p02',"Une analyse de 2022 retrouve","Une analyse de 2022 montre 82,6 % de carcinomes épidermoïdes et 16,0 % d'adénocarcinomes.[[NC.7]]"),
('p02',"Les boissons très chaudes augmentent le risque","Les boissons très chaudes augmentent le risque de carcinome épidermoïde.[[HT.21]] Le risque relatif atteint 1,79 pour qui préfère les boissons chaudes et 3,47 pour les boissons très chaudes, par rapport aux boissons tièdes.[[HT.21]]"),
('p02',"La recommandation allemande ajoute à l'adénocarcinome","La recommandation allemande associe à l'adénocarcinome l'obésité, le reflux et l'œsophage de Barrett.[[DE.65]] Elle associe au carcinome épidermoïde l'alcool, la radiothérapie cervicothoracique antérieure et les tumeurs de la tête et du cou.[[DE.65]]"),
('p03',"Le carcinome épidermoïde suit une progression","Le carcinome épidermoïde suit une progression par étapes, de l'épithélium normal à l'hyperplasie des cellules basales.[[GN.36]] Viennent ensuite les dysplasies légère, modérée et sévère, le carcinome in situ et le carcinome invasif.[[GN.36]]"),
('p03',"Sur le plan moléculaire, des mutations de TP53","Sur le plan moléculaire, des mutations de TP53, de NOTCH1, de CDKN2A, d'EP300 et de MLL2 apparaissent déjà dans l'hyperplasie basale.[[GN.38]] Elles persistent jusqu'au cancer invasif, ce qui en fait des événements clonaux probablement précoces.[[GN.38]]"),
('p03',"L'œsophage de Barrett est une réponse métaplasique","L'œsophage de Barrett est une réponse métaplasique à une agression acide chronique.[[EN.7]] Les cellules épidermoïdes normales sont alors remplacées par des cellules proches de celles de l'estomac et de l'intestin.[[EN.7]]"),
('p03',"La dysplasie qui s'y développe","La dysplasie qui s'y développe est le marqueur le plus valide du risque de cancer.[[DE.110]] La classification de l'Organisation mondiale de la Santé doit donc figurer dans tout compte rendu de Barrett.[[DE.110]]"),
('p03',"Le risque dépend du grade","Le risque dépend du grade de la dysplasie.[[DE.153]] Si un second pathologiste confirme une dysplasie de bas grade, l'évolution vers le haut grade ou le cancer atteint 13,4 % par patient et par an.[[DE.153]]"),
('p03',"Le pronostic dépend de la profondeur","Le pronostic est lié à la profondeur d'infiltration (catégorie T) et à l'atteinte ganglionnaire (catégorie N).[[DE.79]]"),
('p03',"Pour le carcinome épidermoïde précoce, le risque","Pour le carcinome épidermoïde précoce, le risque de métastase ganglionnaire augmente avec la couche atteinte.[[DE.121]] Il vaut 0 % pour m1, 3,3 % pour m2 et 12,2 % pour m3.[[DE.121]] Il atteint ensuite 26,5 %, 35,8 % et 45,9 % pour sm1, sm2 et sm3.[[DE.121]]"),
('p03',"La perte de poids traduit pourtant","La perte de poids traduit pourtant un changement de composition corporelle.[[DE.134]] Ce changement entraîne un risque métabolique, à prendre en compte avant et pendant le traitement, surtout avant la chirurgie.[[DE.134]]"),
('p03',"Le nivolumab, anticorps monoclonal","Le nivolumab, anticorps monoclonal de type IgG4, se lie au récepteur PD-1.[[OP.190]] Il empêche ainsi son interaction avec PD-L1 et PD-L2, ce qui lève le frein exercé sur les lymphocytes T.[[OP.190]]"),
('p03',"Le statut PD-L1, exprimé","Le statut PD-L1 guide l'immunothérapie, et il s'exprime en score positif combiné (CPS) ou en proportion tumorale (TPS).[[DE.47|SE.11]]"),
('p04',"Les premiers sont graves","Le premier est le cancer de la jonction œsogastrique de type III de Siewert, classé comme un cancer de l'estomac.[[DE.116]] Le deuxième est la compression extrinsèque par une tumeur, une adénopathie ou une structure vasculaire.[[AC.162]]"),
('p04',"Le quatrième regroupe","Le quatrième comprend les causes bénignes de sténose : œsophagite par reflux, hernie hiatale, anneaux, œsophagite à éosinophiles, diverticules et tumeurs sous-épithéliales.[[DE.69]]"),
('p04',"Dans un registre danois de blocages alimentaires","Dans un registre danois de blocages alimentaires, l'œsophagite à éosinophiles représentait 17,3 % des diagnostics.[[FB.23]] La sténose œsophagienne en représentait 15,3 %, le cancer de l'œsophage ou du cardia 5,3 % et l'anneau de Schatzki 4,0 %.[[FB.23]]"),
('p06',"Chez un sujet sain,","Chez un sujet sain, l'état général est conservé et le poids est stable.[[DE.134]] L'indice de masse corporelle reste au-dessus de 18,5 kg/m², limite critique de l'Organisation mondiale de la Santé.[[DE.134]]"),
('p06',"On pèse le patient","On pèse le patient, car la perte dépasse 5 % du poids habituel chez plus de la moitié des patients à l'admission pour chirurgie.[[DE.133]]"),
('p06',"On palpe les aires ganglionnaires","On palpe les aires ganglionnaires du cou, car des métastases cervicales touchent 10 à 28 % des patients.[[DE.88]] Elles sont plus fréquentes si la tumeur est cervicale ou haut située dans le thorax.[[DE.88]]"),
('p06',"On inspecte la cavité buccale","On inspecte la bouche et le pharynx, car des tumeurs synchrones ou métachrones de la tête et du cou figurent parmi les risques du carcinome épidermoïde.[[DE.65]]"),
('p06',"La recommandation allemande n'impose cependant","La recommandation allemande n'impose cependant pas de panendoscopie systématique, car aucune preuve ne la soutient.[[DE.104]]"),
('p07',"L'Union européenne de gastroentérologie","L'Union européenne de gastroentérologie et la Société européenne de neurogastroentérologie définissent la dysphagie œsophagienne comme une difficulté à avaler, causée par des anomalies anatomiques, mécaniques ou fonctionnelles.[[AC.27]] Cette difficulté est généralement ressentie derrière le sternum.[[AC.27]]"),
('p07',"La dysphagie oropharyngée se définit","La dysphagie oropharyngée se définit à l'inverse comme un trouble de la déglutition.[[AC.227]] Ce trouble empêche le bol alimentaire de passer de la bouche vers l'œsophage de façon sûre et efficace.[[AC.227]]"),
('p07',"En effet, l'irradiation de ces tumeurs","En effet, l'irradiation de ces tumeurs est associée à un risque élevé d'hémorragie massive ou de fistule.[[SE.42]]"),
('p08',"Le compte rendu doit préciser","Le compte rendu doit préciser le type de lésion néoplasique et le type histologique selon l'Organisation mondiale de la Santé.[[DE.112]] Il précise aussi le grade de différenciation pour l'adénocarcinome invasif.[[DE.112]]"),
('p08',"Le score de Becker distingue","Le score de Becker distingue la régression complète et la régression subtotale (1 à moins de 10 % de tumeur résiduelle).[[DE.128]] Il distingue aussi la régression partielle (10 à 50 %) et la régression faible ou nulle (plus de 50 %).[[DE.128]]"),
('p09',"Le compte rendu note la distance","Le compte rendu note la distance en centimètres entre les incisives et les limites supérieure et inférieure de la tumeur.[[DE.71]] Il décrit l'aspect endoscopique selon la classification de Paris et la position de la jonction œsogastrique.[[DE.71]]"),
('p09',"La recommandation espagnole demande","La recommandation espagnole recommande 6 à 8 biopsies.[[SE.9]]"),
('p09',"La société européenne d'endoscopie digestive demande au moins 1 minute","La société européenne d'endoscopie digestive exige au moins 1 minute d'inspection par centimètre de Barrett et une biopsie en quatre quadrants tous les 2 cm.[[GB.6|GB.7]]"),
('p09',"Le Lugol est utile surtout","Le Lugol est utile surtout chez les patients à haut risque, comme les alcooliques et les grands fumeurs.[[DE.73]] Il l'est aussi chez ceux qui ont déjà un carcinome épidermoïde de l'oropharynx.[[DE.73]]"),
('p09',"Tout patient qui vient de recevoir","Tout patient qui vient de recevoir le diagnostic doit bénéficier d'un scanner multibarrette du cou, du thorax et de l'abdomen.[[DE.91]] Ce scanner comporte une injection de produit de contraste et une distension de la paroi.[[DE.91]]"),
('p09',"Pour les ganglions, la sensibilité","Pour les ganglions, la sensibilité atteint 81 % et la spécificité 73 % avec ponction à l'aiguille fine.[[DE.97]] Ces valeurs atteignent 54 % et 87 % pour le scanner, et 52 % et 82 % pour la tomographie par émission de positons.[[DE.97]]"),
('p09',"Elle donne une précision comparable","Elle donne une précision comparable à celle du scanner pour la stadification TNM, surtout pour les tumeurs de la jonction.[[DE.99]] Elle est moins précise pour les lésions pulmonaires.[[DE.99]]"),
('p09',"Dans la maladie précoce destinée","Dans la maladie précoce destinée à une résection endoscopique, la société européenne d'endoscopie digestive ne recommande pas de pratiquer systématiquement d'autres examens.[[GD.5]] Il s'agit de l'échoendoscopie, du scanner, de l'imagerie par résonance magnétique et de la tomographie par émission de positons avant la résection.[[GD.5]]"),
('p09',"La tomographie par émission de positons couplée","La tomographie par émission de positons couplée au scanner peut compléter la stadification M des tumeurs localement avancées, de catégories T2 à T4 avec atteinte ganglionnaire.[[DE.10]] Elle se justifie si le patient reste curable ou si le résultat change la conduite.[[DE.10]]"),
('p09',"Avant un traitement par cisplatine, la créatinine","Avant un traitement par cisplatine, la créatinine sérique doit rester inférieure ou égale à 130 µmol/l.[[CI.8]] Les thrombocytes doivent dépasser 100 000 par µl et les leucocytes 4000 par µl.[[CI.9]]"),
('p10',"Si un patient présente une dysphagie récente","Si l'un de ces signes apparaît (dysphagie récente, saignement digestif, aspirations ou vomissements répétés, dyspepsie, perte de poids, inappétence), alors on organise une endoscopie précoce.[[DE.67]]"),
('p10',"Si un adénocarcinome exprime HER2","Si un adénocarcinome surexprime HER2, alors on ajoute le trastuzumab à la chimiothérapie à base de cisplatine et de fluoropyrimidine.[[DE.48]]"),
('p11',"En revanche, la chimiothérapie systémique","En revanche, la chimiothérapie systémique d'un adénocarcinome non curable vise à prolonger la survie et à maintenir la qualité de vie.[[DE.46]]"),
('p11',"Le FLOT désigne","Le FLOT est l'association de fluorouracile, de leucovorine, d'oxaliplatine et de docétaxel.[[EU.8]]"),
('p11',"Une élévation de la créatinine de grade 2","Une élévation de la créatinine de grade 2 ou 3 sous nivolumab impose de suspendre le traitement.[[OP.70]] On débute alors une corticothérapie de 0,5 à 1 mg/kg/jour de méthylprednisolone.[[OP.70]]"),
('p11',"Si la tumeur envahit l'aorte ou la trachée","Si la tumeur envahit l'aorte ou la trachée, la radiothérapie est associée à un risque élevé d'hémorragie massive ou de fistule.[[SE.42]] La chimiothérapie, avec ou sans immunothérapie, devient alors le meilleur choix.[[SE.42]]"),
('p11',"Selon l'information professionnelle suisse, le nivolumab","Selon l'information professionnelle suisse, le nivolumab s'utilise en première ligne pour le carcinome épidermoïde avancé dont l'expression de PD-L1 atteint au moins 1 %.[[OP.11]] Il s'associe alors à une chimiothérapie à base de fluoropyrimidine et de cisplatine, ou à l'ipilimumab.[[OP.11]]"),
('p11',"Avec une chimiothérapie à base de fluoropyrimidine et de cisplatine, la dose","Avec une chimiothérapie à base de fluoropyrimidine et de cisplatine, la dose est de 240 mg toutes les 2 semaines.[[OP.25]] L'association à l'ipilimumab comprend 3 mg/kg de nivolumab toutes les 2 semaines et 1 mg/kg d'ipilimumab toutes les 6 semaines.[[OP.21]]"),
('p11',"La dose usuelle en monothérapie","La dose usuelle en monothérapie est de 50 à 100 mg/m² en dose unique ou de 15 à 20 mg/m² par jour pendant 5 jours consécutifs.[[CI.3]] Une pause de 4 semaines après chaque cycle est indispensable.[[CI.3]]"),
('p11',"La dose est de 75 mg/m², suivie","La dose est de 75 mg/m², suivie de 75 mg/m² de cisplatine.[[DO.12]] Le fluorouracile suit à 750 mg/m² par jour en perfusion continue pendant 5 jours, toutes les 3 semaines.[[DO.12]]"),
('p11',"Le fluorouracile (Fluorouracil Accord","La dose du fluorouracile (Fluorouracil Accord®, Swissmedic 66825) est de 300 à 600 mg/m² par jour par voie intraveineuse, avec un maximum de 1 g par jour.[[FA.0|FA.3]]"),
('p11',"L'oxaliplatine (Oxaliplatine Sandoz","L'oxaliplatine (Oxaliplatine Sandoz®, Swissmedic 61663) est indiqué dans l'information suisse pour le cancer colorectal, à 85 mg/m² toutes les deux semaines avec le fluorouracile et l'acide folinique.[[OX.0|OX.1|OX.2]]"),
('p11',"L'abord de McKeown","L'abord de McKeown, avec anastomose cervicale, est utilisé pour les tumeurs du thorax supérieur.[[SE.27]]"),
('p11',"La Ligue suisse contre le cancer propose le service","Le service InfoCancer de la Ligue suisse contre le cancer est joignable au 0800 11 88 11 pour les personnes concernées et leurs proches.[[LI.16]]"),
('p11',"Après un traitement endoscopique d'une dysplasie","Après un traitement endoscopique d'une dysplasie de haut grade ou d'un cancer précoce, des endoscopies de contrôle sont réalisées à 3 mois.[[DE.24]] Elles se répètent ensuite tous les 6 mois pendant 2 ans, puis chaque année.[[DE.24]]"),
('p11',"Après une éradication d'un Barrett","Après une éradication du Barrett avec dysplasie de haut grade ou adénocarcinome, la société européenne recommande des contrôles à 1, 2, 3, 4, 5, 7 et 10 ans.[[GB.8]]"),
('p12',"La Ligue suisse contre le cancer ajoute le surpoids","Le surpoids est aussi un facteur de risque selon la Ligue suisse contre le cancer.[[LI.13]]"),
('p12',"La société européenne d'endoscopie digestive demande, pour chaque","La société européenne d'endoscopie digestive exige, pour chaque endoscopie de surveillance, au moins 1 minute d'inspection par centimètre de Barrett et des biopsies de toute anomalie visible.[[GB.6]]"),
('p12',"Dans un essai randomisé, la progression","Dans un essai randomisé, la progression est survenue chez 1,5 % des patients traités par radiofréquence.[[DE.155]] Elle est survenue chez 25 % des patients simplement surveillés, après un suivi médian de 21 mois.[[DE.155]]"),
('p12',"Pour le carcinome épidermoïde, la coloration au Lugol","Pour le carcinome épidermoïde, la coloration au Lugol ou l'imagerie numérique s'adressent aux patients à risque.[[DE.72]] Ce sont ceux qui ont déjà eu un carcinome épidermoïde de la bouche, du nez, du pharynx, des bronches ou de l'œsophage.[[DE.72]]"),
('p14',"Question : comment classe-t-on une tumeur","Question : comment classe-t-on une tumeur de la jonction dont le centre se trouve à plus de 2 cm sous la jonction ?[[DE.116]]"),
('p14',"Réponse : comme un cancer de l'estomac","Réponse : on la classe comme un cancer de l'estomac, car c'est un type III de Siewert.[[DE.116]]"),
('p14',"Question : quel examen stadifie le mieux","Question : quel examen est le plus précis pour la profondeur d'infiltration ?"),
('p14',"Piège : doser un marqueur tumoral","Le piège consiste à doser un marqueur tumoral pour suivre la maladie.[[DE.8]]"),
('p14',"Piège : opérer un carcinome épidermoïde cervical","Le piège consiste à opérer d'emblée un carcinome épidermoïde cervical.[[DE.40]]"),
('p14',"Piège : arrêter la démarche","Le piège consiste à arrêter la démarche devant un anneau ou une sténose bénigne.[[AK.84]]"),
('p14',"Piège : confondre l'incidence","Le piège consiste à confondre l'incidence du cancer et la fréquence de la dysphagie.[[OF.116]]"),
('p14',"Piège : appliquer le seuil de PD-L1","Le piège consiste à appliquer le seuil de PD-L1 de la recommandation allemande plutôt que celui de l'information suisse.[[DE.48]]"),
]
for f,a,b in R: rep(f,a,b)
