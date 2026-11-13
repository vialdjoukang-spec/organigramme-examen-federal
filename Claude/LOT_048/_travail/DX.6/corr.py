import json
S=lambda i:f'<sup class="r"><a href="#sb-{i}">{i}</a></sup>'
C=[
("Le fluorouracile est contre-indiqué en cas de déficit complet en DPD, d'allaitement et d'association avec la brivudine, car ces situations exposent à une toxicité grave"+S('aips-66825-7')+S('aips-66825-8')+".",
 "Le fluorouracile est contre-indiqué en cas de myélosuppression, de modifications sévères de l'hémogramme, de troubles hépatiques sévères, d'infections sévères, de déficit complet en DPD, d'allaitement et avec la brivudine"+S('aips-66825-7')+S('aips-66825-8')+"."),
("Seulement si bénéfice supérieur au risque</td>",
 "Seulement si le bénéfice potentiel justifie le risque, sans alternative plus sûre et sans report possible ; contraception d'au moins 6 mois après"+S('aips-66825-33')+S('aips-66825-32')+"</td>"),
("La recommandation impose la huitième édition de la classification TNM de l'Union internationale contre le cancer"+S('w657eba-24')+".",
 "La recommandation retient la huitième édition de la classification TNM de l'Union internationale contre le cancer"+S('w657eba-24')+". La neuvième édition, applicable dès 2026, révise la stadification de l'oropharynx associé au papillomavirus"+S('wded061-17')+S('wded061-18')+"."),
("<tr><td>TNM huitième édition</td><td>À utiliser</td><td>Recommandation</td></tr>",
 "<tr><td>TNM huitième édition</td><td>Retenue par la recommandation ; neuvième édition applicable dès 2026</td><td>Recommandation</td></tr>"),
("Le cisplatine est contre-indiqué en cas de myélosuppression, d'atteinte rénale, de troubles sévères de l'ouïe, de grossesse et d'allaitement, car il est toxique pour ces organes"+S('aips-51077-6')+".",
 "Le cisplatine est contre-indiqué en cas de myélosuppression, de neuropathie due au cisplatine, de trouble de la fonction rénale, d'exsiccose, de troubles sévères de l'ouïe ou de la fonction hépatique, de grossesse et d'allaitement"+S('aips-51077-6')+"."),
("Un nouveau cycle ne peut commencer que si la créatinine est inférieure ou égale à 130 µmol/l"+S('aips-51077-8')+".",
 "Un nouveau cycle ne peut être envisagé que si la créatinine sérique est inférieure ou égale à 130 µmol/l et l'urée inférieure à 25 mg/dl"+S('aips-51077-8')+", après normalisation de la formule sanguine"+S('aips-51077-3')+"."),
("<tr><td>Créatinine ≤ 130 µmol/l</td><td>Cycle de cisplatine possible</td>",
 "<tr><td>Créatinine ≤ 130 µmol/l, urée &lt; 25 mg/dl, formule normalisée</td><td>Cycle de cisplatine envisageable</td>"),
("la survie médiane est de 14·9 mois sous pembrolizumab, alors qu'elle est de 10·7 mois sous cétuximab avec chimiothérapie (HR 0·61)",
 "la survie médiane est de 14,9 mois sous pembrolizumab, contre 10,7 mois sous cétuximab avec chimiothérapie (HR 0,61)"),
]
json.dump([{"avant":a,"apres":b} for a,b in C],open('Claude/LOT_048/_travail/DX.6/corrections.json','w'),ensure_ascii=False)
