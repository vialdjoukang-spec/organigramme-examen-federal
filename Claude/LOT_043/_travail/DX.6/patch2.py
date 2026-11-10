R=[
('p01',"Le cours admet comme synonymes « syndrome coronarien aigu », « SCA » et « angor instable », selon le tableau clinique. Il admet aussi « infarctus du myocarde avec ou sans sus-décalage du segment ST ».[[w29ae2f-3 w512b09-2]]","Les synonymes admis sont « syndrome coronarien aigu » et « SCA », car ils désignent le même spectre.[[w29ae2f-3]] L'expression « infarctus du myocarde avec ou sans sus-décalage du segment ST » est aussi admise, selon le tableau clinique.[[w512b09-2]]"),
('p02',"Une étude de médecine générale de l'équipe de Bösner retrouve 3,6 %.","Une étude de médecine générale de l'équipe de Bösner montre une proportion de 3,6 %."),
('p02',"L'histoire naturelle dépend du temps d'occlusion, car la nécrose progresse avec lui.","L'histoire naturelle est liée au temps d'occlusion, car la nécrose progresse avec lui."),
('p02',"Les enjeux de santé publique concernent d'abord l'aspirine, qui est prescrite à plus de 90 % des patients après STEMI ou NSTEMI dans les registres suisses, avec un écart persistant entre hommes et femmes.","Les enjeux de santé publique concernent d'abord l'aspirine, qui est prescrite à plus de 90 % des patients après STEMI ou NSTEMI. Un écart persiste cependant entre hommes et femmes."),
('p05',"Le caractère reproductible ou positionnel rend l'infarctus moins probable, sans l'exclure.","L'infarctus est moins probable si la douleur est reproductible ou positionnelle, mais il n'est pas exclu."),
('p07',"met en regard les signes fonctionnels et les signes physiques de chacun.","indique les signes fonctionnels et les signes physiques de chacun."),
('p08',"La recommandation de l'ESC propose une stratégie invasive précoce dans les 24 heures dans quatre situations.","La recommandation de l'ESC recommande une stratégie invasive précoce dans les 24 heures dans quatre situations."),
('p08',"sert donc de seuil de risque pour l'angiographie.","constitue donc un seuil de risque pour l'angiographie."),
('p08',"L'algorithme 0/2h améliore cette efficacité à 58,4 %.","L'algorithme 0/2h atteint une efficacité de 58,4 %."),
('p11',"la recommandation de l'ESC propose une stratégie invasive dans les 24 heures.","la recommandation de l'ESC recommande une stratégie invasive dans les 24 heures."),
('p11',"Dans l'angine de poitrine instable ou le NSTEMI, l'information professionnelle suisse prévoit un bolus de 60 à 70 U.I./kg avec un maximum de 5 000 U.I., puis 12 à 15 U.I./kg par heure.","Dans l'angine instable ou le NSTEMI, l'information professionnelle suisse prévoit un bolus de 60 à 70 U.I./kg, avec un maximum de 5 000 U.I. Elle prévoit ensuite 12 à 15 U.I./kg par heure."),
('p11',"Ils sont contre-indiqués si la pression systolique est inférieure à 110 mmHg, en cas d'infarctus droit ou si le patient a pris un inhibiteur de la phosphodiestérase de type 5 dans les dernières 48h.","Ils sont contre-indiqués si la pression systolique est inférieure à 110 mmHg ou en cas d'infarctus droit. Ils le sont aussi si le patient a pris un inhibiteur de la phosphodiestérase de type 5 dans les dernières 48h."),
('p11',"s'administre avant l'angioplastie, à la dose de charge","est administré avant l'angioplastie, à la dose de charge"),
('p11',"s'instaure par une dose de charge de 300 mg dans le SCA sans sus-décalage, puis par 75 mg par jour avec l'aspirine.","est instauré par une dose de charge de 300 mg dans le SCA sans sus-décalage, puis par 75 mg par jour avec l'aspirine."),
('p11',"La recommandation de l'ESC le réserve aux situations où le prasugrel ou le ticagrelor est contre-indiqué ou indisponible, et elle le propose chez les patients de 70 ans ou plus à risque hémorragique.","La recommandation de l'ESC le réserve aux situations où le prasugrel ou le ticagrelor est contre-indiqué ou indisponible. Elle le propose aussi chez les patients de 70 ans ou plus à risque hémorragique."),
('p11',"débute à 10 mg une fois par jour, avec une dose maximale de 80 mg.","est débutée à 10 mg une fois par jour, avec une dose maximale de 80 mg."),
('p12',"La recommandation de l'ESC lui accorde la classe IIa, niveau de preuve B.","La classe de recommandation de l'ESC est IIa, avec un niveau de preuve B."),
('p12',"ne bénéficie pas encore d'une stratégie de prévention consensuelle, hormis un mode de vie sain.","n'a pas encore de stratégie de prévention consensuelle, hormis un mode de vie sain."),
]
for f,o,n in R:
    path=f'src/{f}.txt'
    s=open(path).read()
    if o not in s: print('MISS',f,o[:70]); continue
    open(path,'w').write(s.replace(o,n,1))
