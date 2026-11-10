R=[
('p01',"P La Société européenne","P La Société européenne"),
('p01',"La plateforme suisse des guides de pratique la recense","Ainsi, la plateforme suisse des guides de pratique la recense"),
('p01',"Le terme d'infarctus du myocarde se définit par la définition universelle","Le terme d'infarctus du myocarde se définit donc par la définition universelle"),
('p02',"Ce registre inclut des patients","Ainsi, ce registre inclut des patients"),
('p02',"L'hypertension, l'hyperlipidémie, le diabète,","Ainsi, l'hypertension, l'hyperlipidémie, le diabète,"),
('p02',"Entre 2007-2012 et 2019-2024, la différence","Ainsi, entre 2007-2012 et 2019-2024, la différence"),
('p03',"permet de reconnaître la plupart des ruptures","permet donc de reconnaître la plupart des ruptures"),
('p03',"P Deux causes particulières méritent d'être reconnues.","P Deux causes particulières méritent d'être reconnues lorsque les coronaires sont peu atteintes."),
('p04',"P La troponine élevée ne tranche pas à elle seule.","P La troponine élevée ne tranche donc pas à elle seule."),
('p05',"P Les symptômes associés renforcent la suspicion.","P Les symptômes associés renforcent donc la suspicion."),
('p06',"P Les signes vitaux ouvrent l'examen.","P Les signes vitaux ouvrent donc l'examen."),
('p06',"Signes pathologiques. Le souffle","Signes pathologiques. Ainsi, le souffle"),
('p07',"Chaque syndrome combine des signes fonctionnels","Ainsi, chaque syndrome combine des signes fonctionnels"),
('p08',"repose sur trois piliers","repose donc sur trois piliers"),
('p08',"Pour le STEMI, le critère ECG comprend","Pour le STEMI, le critère ECG comprend donc"),
('p08',"Le NSTEMI se définit par","Le NSTEMI se définit donc par"),
('p08',"L'angor instable se définit comme","L'angor instable se définit donc comme"),
('p08',"Les types d'infarctus se distinguent selon","Les types d'infarctus se distinguent donc selon"),
('p09',"Les examens complémentaires confirment le diagnostic","Les examens complémentaires confirment donc le diagnostic"),
('p09',"P La coronarographie précise l'anatomie","P La coronarographie précise donc l'anatomie"),
('p09',"L'algorithme 0/2h améliore cette efficacité à 58,4 %.","L'algorithme 0/2h atteint une efficacité de 58,4 %."),
('p11',"P Le traitement vise à rétablir","P Le traitement vise donc à rétablir"),
('p11',"P Les situations spéciales exigent","P Les situations spéciales exigent donc"),
('p11',"P Le traitement non pharmacologique comprend","P Le traitement non pharmacologique comprend donc"),
('p12',"repose sur le contrôle des facteurs de risque","repose donc sur le contrôle des facteurs de risque"),
('p12',"P L'imagerie peut préciser","P L'imagerie peut donc préciser"),
('p12',"P Une cause fréquente de récidive est","P Une cause fréquente de récidive est donc"),
('p12',"L'érosion de plaque, fréquente chez les jeunes femmes et chez les fumeurs, n'a pas encore de stratégie de prévention consensuelle, hormis un mode de vie sain.[[wc88660-61]]","Il n'existe pas encore de stratégie de prévention consensuelle pour l'érosion de plaque, fréquente chez les jeunes femmes et chez les fumeurs, hormis un mode de vie sain.[[wc88660-61]]"),
('p02',"qui est prescrite à plus de 90 % des patients après STEMI ou NSTEMI. Un écart","qui est prescrite à plus de 90 % des patients après STEMI ou NSTEMI.[[wf96e5f-26]] Un écart"),
('p11',"avec un maximum de 5 000 U.I. Elle prévoit","avec un maximum de 5 000 U.I.[[aips-46613-5]] Elle prévoit"),
('p11',"ou en cas d'infarctus droit. Ils le sont","ou en cas d'infarctus droit.[[w8db60a-6]] Ils le sont"),
]
for f,o,n in R:
    path=f'src/{f}.txt'
    s=open(path).read()
    if o not in s: print('MISS',f,o[:70]); continue
    open(path,'w').write(s.replace(o,n,1))
