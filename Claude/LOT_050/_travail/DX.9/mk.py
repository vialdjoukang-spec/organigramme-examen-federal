import json
t=open('fragments/p11.html').read()
S=lambda *ids:''.join(f'<sup class="r"><a href="#sb-{i}">{i}</a></sup>' for i in ids)
C=[]
# table rows
a=t.find('<tr><td>Amiodarone</td>'); b=t.find('</tbody>',a)
old_rows=t[a:b]
rows=(
"<tr><td>Cordarone® i.v. et Amiodarone Labatec® i.v. (amiodarone)</td><td>41060 ; 59528</td>"
"<td>Arythmies ventriculaires gravement symptomatiques et invalidantes, lorsque d'autres traitements ont échoué"+S('aips-59528-1','aips-41060-1')+"</td>"
"<td>Charge : en moyenne 5 mg/kg dans 250 ml de glucose à 5 % en 20 minutes à 2 heures, renouvelable 2 à 3 fois par 24 heures ; entretien 10 à 20 mg/kg/24 h"+S('aips-59528-2','aips-41060-2')+"</td>"
"<td>Bradycardie sinusale, bloc AV non appareillé, affection thyroïdienne, QT allongé, hypokaliémie ; grossesse sauf indication vitale ; allaitement"+S('aips-59528-4')+"</td></tr>"
"<tr><td>Rapidocain® ad usum cardiologicum (lidocaïne)</td><td>46461</td>"
"<td>Arythmies ventriculaires symptomatiques, invalidantes et menaçantes pour la vie"+S('aips-46461-1')+"</td>"
"<td>100 mg en injection intraveineuse lente de 2 à 4 minutes, répétée 20 minutes plus tard, puis perfusion de 1 à 4 mg/min"+S('aips-46461-2')+"</td>"
"<td>Bloc AV, troubles sévères de la conduction, bradycardies, insuffisance hépatique"+S('aips-46461-4')+"</td></tr>"
"<tr><td>Beloc® i.v. (métoprolol)</td><td>56191</td>"
"<td>Troubles du rythme cardiaque, surtout tachyarythmies supraventriculaires"+S('aips-56191-1')+"</td>"
"<td>Au début jusqu'à 5 mg en injection lente (1 à 2 mg/min), répétable toutes les 5 minutes ; 10 à 15 mg suffisent en général"+S('aips-56191-2')+"</td>"
"<td>Bloc AV de degrés 2 et 3, insuffisance cardiaque décompensée, choc cardiogénique, bradycardie sinusale patente"+S('aips-56191-6')+"</td></tr>"
"<tr><td>Brevibloc® (esmolol)</td><td>49576</td>"
"<td>Fibrillation et flutter auriculaires, tachycardie sinusale ou supraventriculaire ; la tachycardie ventriculaire n'est pas citée"+S('aips-49576-1')+"</td>"
"<td>Saturation 500 µg/kg/min pendant 1 minute, puis 50 µg/kg/min pendant 4 minutes"+S('aips-49576-2')+"</td>"
"<td>Traitement d'urgence, à ne pas prolonger au-delà de 24 heures"+S('aips-49576-6')+"</td></tr>"
"<tr><td>Inderal® (propranolol, voie orale)</td><td>31706</td>"
"<td>Troubles du rythme cardiaque"+S('aips-31706-1')+"</td>"
"<td>10 à 40 mg, 3 à 4 fois par jour"+S('aips-31706-4')+"</td>"
"<td>Asthme ou bronchospasme"+S('aips-31706-7')+"</td></tr>"
"<tr><td>Sotalol-Mepha® 80/160 (sotalol, comprimés)</td><td>54553</td>"
"<td>Arythmies ventriculaires potentiellement fatales, si l'efficacité est prouvée par stimulation électrophysiologique ou Holter"+S('aips-54553-1')+"</td>"
"<td>80 à 160 mg par jour au départ, optimum 160 à 320 mg par jour, en 2 à 3 prises"+S('aips-54553-2','aips-54553-3')+"</td>"
"<td>Dose réduite de moitié si la clairance de la créatinine est de 30 à 60 ml/min"+S('aips-54553-6')+"</td></tr>"
)
C.append({"avant":old_rows,"apres":rows})
C.append({"avant":"L'information professionnelle suisse (AIPS) fournit les données de deux bêtabloquants cardiosélectifs, que le tableau récapitule.","apres":"L'information professionnelle suisse (AIPS) fournit les données des antiarythmiques et des bêtabloquants utilisables dans la tachycardie ventriculaire, que le tableau récapitule."})
i=t.find("<div class=\"p\">Aucune dose d'amiodarone"); j=t.find('</div>',i)+6
old=t[i:j]
new=(
'<div class="p">L\'amiodarone (Cordarone® 41060, Amiodarone Labatec® 59528) et la lidocaïne (Rapidocain® 46461) disposent d\'une information professionnelle suisse'+S('aips-41060-0','aips-59528-0','aips-46461-0')+'. '
"En revanche, la seule information lue pour le sotalol (Sotalol-Mepha® 54553) concerne les comprimés, et la procaïnamide n'a aucune information professionnelle suisse relue ici"+S('aips-54553-0')+'.</div>'
'<h4><em>11.B.2 bis Conduite intraveineuse de la tachycardie ventriculaire stable selon l\'AIPS</em></h4>'
'<div class="p">L\'AIPS réserve l\'amiodarone injectable aux arythmies ventriculaires gravement symptomatiques et invalidantes, lorsque d\'autres traitements ont échoué'+S('aips-59528-1','aips-41060-1')+'. '
"Elle ne s'administre qu'en milieu hospitalier spécialisé, sous surveillance permanente de l'ECG et de la tension artérielle"+S('aips-59528-2')+'. '
'La charge est en moyenne de 5 mg/kg dans 250 ml de glucose à 5 % exclusivement, passés en 20 minutes à 2 heures'+S('aips-59528-2')+'. '
'Cette charge est renouvelable 2 à 3 fois par 24 heures, puis un entretien de 10 à 20 mg/kg/24 h prend le relais, avec un passage à la voie orale dès le premier jour'+S('aips-59528-2')+'. '
'Cordarone® prévoit la même charge de 5 mg/kg et le même entretien de 10 à 20 mg/kg/24 h'+S('aips-41060-2')+'.</div>'
'<div class="p">L\'injection directe de 5 mg/kg, qui dure au moins 3 minutes, existe aussi'+S('aips-59528-3')+'. '
"Elle est cependant contre-indiquée en cas d'hypotension, d'insuffisance respiratoire sévère, de myocardiopathie ou d'insuffisance cardiaque, car ces situations risquent de s'aggraver"+S('aips-59528-6')+'. '
"Dans une cardiopathie structurelle avec dysfonction ventriculaire, la perfusion est donc la voie à retenir"+S('aips-59528-6')+'. '
"La notice contre-indique aussi la bradycardie sinusale, le bloc auriculo-ventriculaire non appareillé, les affections thyroïdiennes, l'allongement du QT et l'hypokaliémie"+S('aips-59528-4')+'. '
"La grossesse est contre-indiquée sauf indication vitale pour la mère, et l'allaitement l'est également"+S('aips-59528-45','aips-59528-47')+'.</div>'
'<div class="p">La lidocaïne est indiquée dans les arythmies ventriculaires symptomatiques, invalidantes et menaçantes pour la vie, de préférence sous contrôle ECG'+S('aips-46461-1')+'. '
"La dose est de 100 mg en injection intraveineuse lente de 2 à 4 minutes, répétée 20 minutes plus tard, puis une perfusion de 1 à 4 mg/min poursuit le traitement"+S('aips-46461-2')+'. '
"Une réduction des doses jusqu'à 50 % s'impose en cas d'insuffisance cardiaque, et le traitement dure 24 à 48 heures pour éviter les récidives"+S('aips-46461-3')+'. '
"La solution à 10 % doit être diluée avant l'administration, car elle ne s'injecte jamais directement"+S('aips-46461-5')+'. '
"Le bloc auriculo-ventriculaire, les troubles sévères de la conduction, les bradycardies et l'insuffisance hépatique contre-indiquent la lidocaïne, et la grossesse l'exclut sauf nécessité absolue"+S('aips-46461-4','aips-46461-10')+'.</div>'
'<div class="p">Le métoprolol intraveineux (Beloc® i.v.) se donne au début jusqu\'à 5 mg en injection lente de 1 à 2 mg/min, répétable toutes les 5 minutes'+S('aips-56191-2')+'. '
"Ainsi, 10 à 15 mg suffisent en général, et une dose de 20 mg ou davantage n'améliore pas les résultats"+S('aips-56191-2')+'. '
"Son indication AIPS vise surtout les tachyarythmies supraventriculaires, de sorte que l'usage dans la tachycardie ventriculaire suit la ligne directrice"+S('aips-56191-1','w2042c8-19')+'. '
"Il est contre-indiqué en cas de bloc auriculo-ventriculaire de degrés 2 et 3, d'insuffisance cardiaque décompensée, de choc cardiogénique et de bradycardie sinusale patente"+S('aips-56191-6')+'.</div>'
'<div class="p">Le Brevibloc® (esmolol) a pour indications aiguës la fibrillation et le flutter auriculaires, la tachycardie sinusale et la tachycardie supraventriculaire, mais la notice ne cite pas la tachycardie ventriculaire'+S('aips-49576-1')+'. '
"La saturation est de 500 µg/kg/min pendant 1 minute, suivie de 50 µg/kg/min pendant 4 minutes"+S('aips-49576-2')+'. '
"Son emploi est réservé à l'urgence, car la perfusion ne devrait pas dépasser 24 heures et doit céder la place à un bêtabloquant oral ou à un autre antiarythmique"+S('aips-49576-6')+'.</div>'
'<div class="p">Le propranolol (Inderal®) n\'est décrit qu\'en voie orale, avec 10 à 40 mg 3 à 4 fois par jour dans les troubles du rythme'+S('aips-31706-4')+'. '
"Il est contre-indiqué en cas d'asthme ou d'antécédent de bronchospasme"+S('aips-31706-7')+'. '
"Le sotalol (Sotalol-Mepha®) traite et prévient les arythmies ventriculaires potentiellement fatales, si l'efficacité a été prouvée par stimulation électrophysiologique ou Holter"+S('aips-54553-1')+'. '
"La dose initiale est de 80 à 160 mg par jour, l'optimum se situe entre 160 et 320 mg par jour, et la clairance de 30 à 60 ml/min impose de réduire la dose de moitié"+S('aips-54553-3','aips-54553-6')+'. '
"Le médecin applique ensuite la logique de classe et de surveillance décrite dans les paragraphes précédents"+S('w2f28eb-30')+'.</div>'
)
C.append({"avant":old,"apres":new})
C.append({"avant":"Le bénéfice porte sur les patients de 70 ans ou moins","apres":"Le bénéfice sur la mort subite porte sur les patients de 70 ans ou moins"})
json.dump(C,open('corrections.json','w'),ensure_ascii=False,indent=1)
# p10
t10=open('fragments/p10.html').read()
C=[]
C.append({"avant":"Si les épisodes se répètent en 24 heures, il s'agit d'un orage","apres":"Si trois arythmies soutenues ou plus surviennent en 24 heures, chacune nécessitant une intervention, il s'agit d'un orage"})
x="<li>On choisit alors la cardioversion électrique si le risque de sédation est faible, sinon un antiarythmique"+S('w2f28eb-26')+".</li>"
assert x in t10
C.append({"avant":x,"apres":x+"<li>Si l'on choisit l'amiodarone, alors la charge est de 5 mg/kg en perfusion de 20 minutes à 2 heures, selon l'AIPS"+S('aips-59528-2')+".</li><li>Si l'on choisit la lidocaïne, alors la dose est de 100 mg en injection intraveineuse lente de 2 à 4 minutes, selon l'AIPS"+S('aips-46461-2')+".</li>"})
json.dump(C,open('corrections10.json','w'),ensure_ascii=False,indent=1)
