import re,glob
R=[
# p01
("ou maladie ulcéreuse peptique, désigne les ulcères","ou maladie ulcéreuse peptique, correspond aux ulcères"),
("le reflux gastro-œsophagien désigne une œsophagite","le reflux gastro-œsophagien correspond à une œsophagite"),
("Un ulcère n'est pas toujours dû à <em>H. pylori</em> ou aux AINS.","Un ulcère n'est pas toujours dû à <em>H. pylori</em> ou aux AINS, car d'autres causes existent."),
("figure dans la CIM-11, la Classification internationale des maladies<sup class=\"r\"><a href=\"#sb-wa677e9-5\">wa677e9-5</a></sup>","figure dans la CIM-11, la Classification internationale des maladies<sup class=\"r\"><a href=\"#sb-wa677e9-5\">wa677e9-5</a></sup><sup class=\"r\"><a href=\"#sb-wa677e9-6\">wa677e9-6</a></sup>"),
("Le consensus a réuni 41 experts","Le consensus a réuni quarante et un experts"),
("Le consensus de Maastricht VI, publié en 2022 par l'European Helicobacter and Microbiota Study group, définit","Le consensus de Maastricht VI, publié par l'European Helicobacter and Microbiota Study group, définit"),
# p02
("La WSES estime sa prévalence","La WSES indique une prévalence"),
("Une revue de 2026 donne une prévalence mondiale de 5–14 %,","Une revue récente indique une prévalence mondiale de 5–14 %,"),
("Une étude sur 36 pays de l'OCDE, entre 2000 et 2019, rapporte un taux","Une étude sur 36 pays de l'OCDE, entre 2000 et 2019, indique un taux"),
("Dans cette cohorte, 13 % des patients ont présenté un ulcère récidivant en 1 an.","Dans cette cohorte, 13 % des patients ont présenté un ulcère récidivant au cours de la première année."),
("Le tableau suivant résume les chiffres retenus,","Le tableau suivant montre les chiffres retenus,"),
("Le taux de récidive de l'ulcère passe de","Le taux de récidive de l'ulcère diminue de"),
("Un ulcère gastrique ancien garde un risque de cancer de l'estomac, même après éradication","Un ulcère gastrique ancien reste associé à un risque de cancer de l'estomac, même après éradication"),
("De plus, la résistance croissante aux antibiotiques menace l'éradication","De plus, la résistance croissante aux antibiotiques fait peser une menace sur l'éradication"),
("Ce point justifie un suivi à long terme, et il explique la biopsie","Ce point justifie un suivi à long terme, et il explique ainsi la biopsie"),
# p03
("L'hypersécrétion d'acide, surtout dans l'ulcère duodénal, accroît l'exposition","L'hypersécrétion d'acide, surtout dans l'ulcère duodénal, augmente l'exposition"),
("La prostaglandine E2 joue un rôle central dans cette défense","La prostaglandine E2 a un rôle central dans cette défense"),
("Le stress oxydatif lèse les membranes, les protéines et l'ADN, et contribue","Le stress oxydatif provoque des lésions des membranes, des protéines et de l'ADN, et contribue"),
# p04
("La NICE demande de penser à une origine cardiaque ou biliaire dans le diagnostic différentiel","La NICE recommande de penser à une origine cardiaque ou biliaire dans le diagnostic différentiel"),
("La péritonite n'existe pourtant que chez deux tiers des patients, donc un examen","La péritonite est pourtant présente chez deux tiers des patients seulement, donc un examen"),
("L'endoscopie avec biopsie différencie le bénin du malin","L'endoscopie avec biopsie permet de distinguer le bénin du malin"),
("La NICE gère d'abord les symptômes de type reflux comme une dyspepsie non investiguée","La NICE recommande de traiter d'abord les symptômes de type reflux comme une dyspepsie non investiguée"),
# p05
("L'outil d'anamnèse du pharmacien explore la localisation","L'outil d'anamnèse du pharmacien permet d'explorer la localisation"),
("La NICE demande de revoir les médicaments susceptibles","La NICE recommande de revoir les médicaments susceptibles"),
("Le recours à une <button","Le recours à une <button"),
("aide à décider de l'urgence","permet de décider de l'urgence"),
("Le score de Rockall identifie les patients à risque","Le score de Rockall permet d'identifier les patients à risque"),
# p06
("L'examen cherche donc surtout l'instabilité","L'examen recherche donc surtout l'instabilité"),
("À l'abdomen, la perforation donne une péritonite","À l'abdomen, la perforation provoque une péritonite"),
("L'examen sert donc à repérer l'urgence, puis l'endoscopie tranche","L'examen permet donc de repérer l'urgence, puis l'endoscopie tranche"),
# p07
("L'approche syndromique regroupe les signes","L'approche syndromique associe les signes"),
# p08
("Dans la perforation, la WSES suggère les scores de Boey, PULP et ASA pour stratifier le risque","Dans la perforation, les scores de Boey, PULP et ASA sont suggérés par la WSES pour stratifier le risque"),
("Le consensus de Maastricht VI de 2022 fonde l'indication","Le consensus de Maastricht VI fonde l'indication"),
("La NICE de 2019 recommande l'éradication","La NICE recommande l'éradication"),
("La WSES de 2020 recommande de tester","La WSES recommande de tester"),
# p09
("Le choix des examens dépend de l'urgence.","Le choix des examens est fonction de l'urgence."),
("la sécurité prime sur la précision","la sécurité doit primer sur la précision"),
("L'embolisation comporte des risques","L'embolisation a des risques"),
# p11
("Dans l'hémorragie comme dans la perforation, la <button class=\"w\" popovertarget=\"dx6-p11-f1\">conduite chronologique de l'urgence</button> commence par l'évaluation","Dans l'hémorragie comme dans la perforation, la <button class=\"w\" popovertarget=\"dx6-p11-f1\">conduite chronologique de l'urgence</button> doit commencer par l'évaluation"),
("Urgence — conduite chronologique : hémorragie digestive haute d'origine ulcéreuse.","Urgence — conduite chronologique : cette liste concerne l'hémorragie digestive haute d'origine ulcéreuse."),
("<li>Maintenir l'hémoglobine","<li>Il faut maintenir l'hémoglobine"),
("<li>Stratifier le risque","<li>Il faut stratifier le risque"),
("<li>Traiter les stigmates","<li>Il faut traiter les stigmates"),
("<li>Poursuivre par un inhibiteur","<li>Il faut poursuivre par un inhibiteur"),
("<li>Évaluer les voies aériennes","<li>Il faut évaluer les voies aériennes"),
("<li>Viser une pression","<li>Il faut viser une pression"),
("<li>Réaliser l'endoscopie","<li>Il faut réaliser l'endoscopie"),
("En 2026, l'ESGE suggère aussi les clips hors endoscope en monothérapie comme alternative","L'ESGE suggère aussi, dans sa mise à jour, les clips hors endoscope en monothérapie comme alternative"),
("La NICE déconseille l'adrénaline seule","La NICE ne recommande pas l'adrénaline seule"),
("Avant l'endoscopie, la NICE ne propose aucun inhibiteur de la pompe ni antihistaminique","Avant l'endoscopie, la NICE ne recommande aucun inhibiteur de la pompe ni antihistaminique"),
("L'ESGE 2026 suggère au contraire d'envisager un inhibiteur intraveineux à haute dose, sans retarder l'endoscopie","La mise à jour de l'ESGE suggère au contraire d'envisager un inhibiteur intraveineux à haute dose, ce qui ne doit pas retarder l'endoscopie"),
("Par ailleurs, la WSES suggère l'érythromycine avant l'endoscopie pour améliorer la visualisation","Par ailleurs, l'érythromycine avant l'endoscopie est suggérée par la WSES pour améliorer la visualisation"),
("D'abord, le médecin arrête l'AINS si possible et teste","D'abord, le médecin doit arrêter l'AINS si possible et tester"),
("Pour l'éradication, l'AIPS cite 20 mg","Pour l'éradication, l'AIPS indique 20 mg"),
("s'emploie avec un inhibiteur de la pompe et un autre antibiotique en cas d'ulcère","est indiquée avec un inhibiteur de la pompe et un autre antibiotique en cas d'ulcère"),
("s'emploie à 2 fois 500 mg par jour","est indiquée à 2 fois 500 mg par jour"),
("Pylera (Swissmedic 66366) s'emploie après","Pylera (Swissmedic 66366) est indiqué après"),
("Chaque dose comprend 3 gélules, 4 fois par jour,","Chaque dose comprend 3 gélules, quatre fois par jour,"),
("traite l'ulcère duodénal associé à <em>H. pylori</em> par 20 mg deux fois par jour, avec 1 g","traite l'ulcère duodénal associé à <em>H. pylori</em> par une prise biquotidienne de 20 mg, avec 1 g"),
("<td>20 mg 2 fois par jour, 7 jours <sup","<td>20 mg par prise biquotidienne, 7 jours <sup"),
("<td>Pantoprazol-Mepha Teva 40 mg (59834)</td><td>40 mg par jour ; éradication 40 mg 2 fois par jour, 7 jours <sup class=\"r\"><a href=\"#sb-aips-59834-6\">aips-59834-6</a></sup>","<td>Pantoprazol-Mepha Teva (59834)</td><td>40 mg par jour ; éradication 40 mg 2 fois par jour, 7 jours <sup class=\"r\"><a href=\"#sb-aips-59834-6\">aips-59834-6</a></sup><sup class=\"r\"><a href=\"#sb-aips-59834-7\">aips-59834-7</a></sup>"),
("<td>Pylera (66366)</td><td>12 gélules par jour, 10 jours","<td>Pylera (66366)</td><td>12 gélules par jour, 10 jours"),
# p14
("<strong>Question 1.</strong>","<strong>Q1.</strong>"),("<strong>Question 2.</strong>","<strong>Q2.</strong>"),("<strong>Question 3.</strong>","<strong>Q3.</strong>"),
("<strong>Question 4.</strong>","<strong>Q4.</strong>"),("<strong>Question 5.</strong>","<strong>Q5.</strong>"),("<strong>Question 6.</strong>","<strong>Q6.</strong>"),("<strong>Question 7.</strong>","<strong>Q7.</strong>"),
("Non, car la péritonite n'existe que chez deux tiers des patients<","Non, car la péritonite est présente chez deux tiers des patients seulement<"),
("car l'air libre n'apparaît que dans 30 à 85 % des cas","car l'air libre n'est visible que dans 30 à 85 % des cas"),
# p12/p11 years
("Aucune recommandation suisse officielle n'a été lue pour cette prévention ; la conduite suit le consensus européen de Maastricht VI de 2022 et la NICE de 2019.","La conduite enseignée suit le consensus européen de Maastricht VI<sup class=\"r\"><a href=\"#sb-wa677e9-6\">wa677e9-6</a></sup> et la NICE<sup class=\"r\"><a href=\"#sb-w2082ec-14\">w2082ec-14</a></sup>."),
("La conduite enseignée suit l'ESGE, la plus récente : endoscopie précoce dans les 24 h, immédiate si le patient reste instable.","La conduite enseignée suit l'ESGE, la plus récente : endoscopie précoce dans les 24 h, immédiate si le patient reste instable<sup class=\"r\"><a href=\"#sb-w5eb23b-7\">w5eb23b-7</a></sup>."),
("L'ESGE 2021 et la NICE recommandent","L'ESGE et la NICE recommandent"),
("La mise à jour ESGE de 2026 ne recommande","La mise à jour de l'ESGE ne recommande"),
# long sentences
("En cas d'hémorragie, l'anamnèse porte aussi sur les médicaments qui modifient la coagulation, comme les antiplaquettaires et les anticoagulants, sur les maladies cardiaques et pulmonaires qui aggravent l'anémie, et sur les maladies neurologiques exposant à l'aspiration","En cas d'hémorragie, l'anamnèse porte aussi sur les médicaments qui modifient la coagulation, comme les antiplaquettaires et les anticoagulants. Elle recherche les maladies cardiaques et pulmonaires qui aggravent l'anémie, et les maladies neurologiques qui exposent à l'aspiration"),
("Pour les médicaments de l'étape suivante, l'âge pèse : le pantoprazole ne s'utilise pas chez l'enfant de moins de 12 ans<sup class=\"r\"><a href=\"#sb-aips-59834-5\">aips-59834-5</a></sup>, et l'association Pylera est contre-indiquée chez l'enfant jusqu'à 12 ans, ainsi que pendant la grossesse","Pour les médicaments, l'âge pèse : le pantoprazole ne s'utilise pas chez l'enfant de moins de 12 ans<sup class=\"r\"><a href=\"#sb-aips-59834-5\">aips-59834-5</a></sup>. Pylera est contre-indiqué chez l'enfant jusqu'à 12 ans, ainsi que pendant la grossesse"),
("Si la plainte est une dyspepsie sans signe d'alarme, la NICE propose un inhibiteur de la pompe à protons à dose complète pendant 4 semaines et un test suivi d'un traitement de <em>H. pylori</em>","Si la plainte est une dyspepsie sans signe d'alarme, la NICE recommande un inhibiteur de la pompe à protons à dose complète pendant 4 semaines, puis un test avec traitement de <em>H. pylori</em>"),
]
files={f:open(f).read() for f in glob.glob('src/p*.txt')}
for old,new in R:
    hit=[f for f,s in files.items() if old in s]
    if not hit: print('MISS',old[:70]); continue
    for f in hit: files[f]=files[f].replace(old,new)
# Swissmedic numbers: add -0 cite
for f,s in files.items():
    s=re.sub(r'\(Swissmedic (59834|56313|62581|66366|56203|57129)\)(.*?)(</div>)',lambda m:f'(Swissmedic {m.group(1)}){m.group(2)}'+m.group(3),s,flags=re.S)
    files[f]=s
for f,s in files.items(): open(f,'w').write(s)
