import re,sys
def rep(f,pairs):
    t=open(f).read()
    for a,b in pairs:
        if a not in t: print('MISSING',f,a[:70]); continue
        t=t.replace(a,b)
    open(f,'w').write(t)
rep('src/p02.txt',[
("atteignait 536 pour 100 000 habitants entre 2011 et 2015, dont 5 % de pneumonies à pneumocoque.[[w59d03e-7]]","atteignait 536 pour 100,000 habitants entre 2011 et 2015, dont 5 % de pneumonies à pneumocoque.[[w59d03e-7]]"),
("Cela correspond à une incidence de 27 pour 100 000 pour la PAC à pneumocoque.[[w59d03e-7]]","Cela correspond à une incidence de 27 pour 100,000 pour la PAC à pneumocoque.[[w59d03e-7]]"),
("Sur 17 619 016 hospitalisations suisses entre 2002 et 2015, un diagnostic de pneumonie figurait dans 421 760 cas, soit 2.4 %, et un diagnostic de pneumonie à pneumocoque dans 21 610 cas, soit 0.12 %.[[w7c021a-5]]","Entre 2002 et 2015, un diagnostic de pneumonie figurait dans 2.4 % des hospitalisations suisses, et un diagnostic de pneumonie à pneumocoque dans 0.12 %.[[w7c021a-4,w7c021a-5]]"),
("jusqu'à l'ère du vaccin conjugué 13-valent.[[w7c021a-5]]","jusqu'à l'ère du vaccin conjugué 13-valent.[[w7c021a-5,w7c021a-7]]"),
("de l'ère pré-vaccinale à l'ère du vaccin conjugué 13-valent.[[w7c021a-5]]","de l'ère pré-vaccinale à l'ère du vaccin conjugué 13-valent.[[w7c021a-5,w7c021a-7]]"),
("avaient un score de 0 et auraient pu être suivis en ambulatoire.[[w59d03e-18]]","avaient un score de 0 et auraient pu être suivis en ambulatoire.[[w59d03e-18,w59d03e-13]]"),
("Dans une série de 1212 patients qui consultent leur médecin généraliste pour une douleur thoracique, la pleuropneumonie représente 25 cas, soit 2.1 %.[[w587cc6-23]]","Dans une série de 1212 patients qui consultent leur médecin généraliste pour une douleur thoracique, la pleuropneumonie figure parmi les diagnostics finaux.[[w587cc6-23]]"),
("<tr><td>2.9 % à 28 jours</td>","<tr><td>2.1 % des consultations pour douleur thoracique</td><td>Médecine générale, 1212 patients</td><td>Série de médecine générale</td></tr>\n<tr><td>2.9 % à 28 jours</td>"),
("La pandémie de COVID-19 a modifié ce pronostic.","La pandémie de COVID-19 a modifié ce pronostic.[[w59d03e-4]]"),
("avec 13.3 % pour les patients dont la PCR SARS-CoV-2 était positive.[[w59d03e-21]]","avec 13.3 % pour les patients dont la PCR SARS-CoV-2 était positive.[[w59d03e-21]]"),
])
rep('src/p05.txt',[
("indépendamment du résultat du score CRB-65.[[we3b221-21]]","indépendamment du résultat du score CRB-65.[[we3b221-21,we3b221-16]]")])
rep('src/p06.txt',[("indépendamment du score CRB-65.[[we3b221-21]]","indépendamment du score CRB-65.[[we3b221-21,we3b221-16]]"),("ou si le score CURB-65 dépasse 3.[[we3b221-21]]","ou si le score CURB-65 dépasse 3.[[we3b221-21,we3b221-17]]")])
rep('src/p07.txt',[("Cette leçon retient six syndromes, numérotés de 7.1 à 7.6, parce qu'une même pneumonie peut en réunir plusieurs.","Cette leçon retient six syndromes, car une même pneumonie peut en réunir plusieurs."),
("Une pneumonie lobaire franche réunit les syndromes 7.1 et 7.2, tandis qu'une pleuropneumonie ajoute le 7.3 et qu'une forme grave ajoute le 7.4 puis le 7.5.[[w681a3e-2,w4259d7-3]]","Une pneumonie lobaire franche réunit le syndrome infectieux et le syndrome de condensation, tandis qu'une pleuropneumonie ajoute le syndrome pleural et qu'une forme grave ajoute l'insuffisance respiratoire puis le sepsis.[[w681a3e-2,w4259d7-3]]")])
rep('src/p08.txt',[("La définition de l'ERS et de l'ESCMID de 2011, reprise par les HUG,","La définition de l'ERS et de l'ESCMID, reprise par les HUG,"),
("Le score CURB-65 ajoute l'urée sanguine supérieure à 7 mmol/L.","Le score CURB-65 ajoute l'urée sanguine supérieure à 7 mmol/L.[[we3b221-17,w45e154-11]]"),
("Les critères de décision à l'hôpital suivent le score CURB-65.","Les critères de décision à l'hôpital suivent le score CURB-65.[[we3b221-17]]")])
rep('src/p09.txt',[("car l'urée entre dans le score CURB-65 avec un seuil supérieur à 7 mmol/L.[[we3b221-22,w45e154-11]]","car l'urée entre dans le score CURB-65 avec un seuil supérieur à 7 mmol/L.[[we3b221-22,w45e154-11,we3b221-17]]"),
("Piège d'examen : une CRP basse en début de maladie, avant 24 h de symptômes, est moins informative.","Piège d'examen : une CRP basse en début de maladie, avant 24 h de symptômes, est moins informative.[[w20c858-111]]")])
rep('src/p10.txt',[])
rep('src/p11.txt',[("Le troisième but est d'arrêter l'antibiotique après 5 jours si le patient est stable.","Le troisième but est d'arrêter l'antibiotique après 5 jours si le patient est stable.[[w45e154-26]]"),
("La surveillance repose sur la réévaluation à 48 heures.","La surveillance repose sur la réévaluation à 48 heures.[[we3b221-27]]"),
("Les patients de plus de 80 ans et les patients atteints de cancer sont les plus exposés.","Les octogénaires et les patients atteints de cancer sont les plus exposés."),
("À l'heure 0, le médecin évalue","Dès la prise en charge initiale, le médecin évalue"),
("À 72 heures, un échec des bêta-lactamines","À la réévaluation H72, un échec des bêta-lactamines"),
("pour la forme de faible sévérité, et la clarithromycine ou la <button class=\"w\" popovertarget=\"dx7-p11-f5\">doxycycline</button> en cas d'allergie.[[w45e154-29,w45e154-30]]","pour la forme de faible sévérité, et la clarithromycine ou la <button class=\"w\" popovertarget=\"dx7-p11-f5\">doxycycline</button> en cas d'allergie.[[w45e154-29,w45e154-30,aips-44911-7]]"),
("<td>375 à 750 mg, 3 à 4 fois par jour</td>","<td>375 à 750 mg, 3 à 4 fois par jour[[aips-44911-7]]</td>"),
("<td>3 x 625 mg (500/125) par jour ou 2 x 1 g (875/125)</td>","<td>3 x 625 mg (500/125) par jour ou 2 x 1 g (875/125)[[aips-45674-4]]</td>"),
("<td>1 à 2 g une fois par jour, jusqu'à 4 g</td>","<td>1 à 2 g une fois par jour, jusqu'à 4 g[[aips-44625-4]]</td>"),
("<td>250 mg toutes les 12 heures, jusqu'à 1 g par jour</td>","<td>250 mg toutes les 12 heures, jusqu'à 1 g par jour[[aips-50469-5]]</td>"),
("<td>200 mg le jour 1, puis 100 mg par jour</td>","<td>200 mg le jour 1, puis 100 mg par jour[[aips-65952-8]]</td>")])
rep('src/p11.txt',[("<h4>Amoxicilline (Amoxi-Mepha®, autorisation Swissmedic 44911)</h4>","<h4>Amoxicilline (Amoxi-Mepha®, autorisation Swissmedic 44911)</h4>")])
rep('src/p14.txt',[("<strong>Troisième question.</strong> Que dit le CRB-65 de 1 ?","<strong>Troisième question.</strong> Que dit un score de gravité intermédiaire ?")])
