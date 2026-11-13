import json
S=lambda i:f'<sup class="r"><a href="#sb-{i}">{i}</a></sup>'
C=[
("Par ailleurs, il est contre-indiqué en cas de déficit complet avéré en dihydropyrimidine déshydrogénase, et un déficit complet touche 0,01 à 0,5 % de la population caucasienne"+S('aips-66825-8')+S('aips-66825-16')+".",
 "Par ailleurs, il est contre-indiqué en cas de myélosuppression, de modifications sévères de l'hémogramme, de troubles hépatiques sévères ou d'infections sévères"+S('aips-66825-7')+". Il l'est aussi en cas de déficit complet avéré en dihydropyrimidine déshydrogénase, rare avec 0,01 à 0,5 % de la population caucasienne"+S('aips-66825-8')+S('aips-66825-16')+"."),
("Le fluorouracile est contre-indiqué pendant l'allaitement"+S('aips-66825-8')+".",
 "Le fluorouracile est contre-indiqué pendant l'allaitement"+S('aips-66825-8')+". Pendant la grossesse, il n'est utilisable que s'il n'existe pas d'alternative plus sûre et s'il est impossible de reporter le traitement"+S('aips-66825-33')+". La contraception se poursuit pendant au moins 6 mois après le traitement"+S('aips-66825-32')+"."),
("Le fluorouracile suit à 750 mg/m² par jour en perfusion continue pendant 5 jours, toutes les 3 semaines"+S('aips-62537-12')+".",
 "Le fluorouracile suit à 750 mg/m² par jour en perfusion continue pendant 5 jours, toutes les 3 semaines"+S('aips-62537-12')+". Cette dose dépasse le plafond journalier de 1 g de l'AIPS du fluorouracile, et les deux textes ne sont pas conciliés"+S('aips-66825-3')+"."),
("On stadifie la maladie selon la classification de l'Union internationale contre le cancer et de l'American Joint Committee on Cancer de 2017, c'est-à-dire la 8e édition"+S('wf7ceda-11')+".",
 "On stadifie la maladie selon la classification TNM de l'Union internationale contre le cancer et de l'American Joint Committee on Cancer de 2017, c'est-à-dire la 8e édition"+S('wf7ceda-11')+". Les critères œsophagiens de cette édition restent en vigueur."),
]
json.dump([{"avant":a,"apres":b} for a,b in C],open('Claude/LOT_048/_travail/DX.7/corrections.json','w'),ensure_ascii=False)
