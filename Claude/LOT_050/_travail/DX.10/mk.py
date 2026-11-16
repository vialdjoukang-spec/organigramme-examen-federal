import json
S=lambda *ids:''.join(f'<sup class="r"><a href="#sb-{i}">{i}</a></sup>' for i in ids)
C=[]
def add(a,b): C.append({"avant":a,"apres":b})
add("Un voltage de Sokolow-Lyon d'au moins 50 mV indique une maladie de surcharge comme la maladie de Pompe ou de Danon"+S('wb0f12f-32')+".",
    "Un indice de Sokolow-Lyon très élevé, signe d'une hypertrophie massive, oriente vers une maladie de surcharge comme la maladie de Pompe ou de Danon"+S('wb0f12f-32')+".")
add("<tr><td>Bisoprolol</td><td>Dose maximale tolérée (recommandation ESC)</td><td>Orale</td><td>Long cours</td><td>Bloc auriculoventriculaire, bradycardie, hypotension (classe)</td><td>"+S('wb0f12f-76')+"</td></tr>",
    "<tr><td>Bisoprolol : Concor® (47311), Bisoprolol Stada® (67675), sans indication de CMH dans l'AIPS</td><td>Dose maximale tolérée selon l'ESC"+S('wb0f12f-76')+", au plus 10 mg une fois par jour"+S('aips-67675-5','aips-47311-4')+"</td><td>Orale</td><td>Long cours</td><td>Bloc AV du 2e ou 3e degré non appareillé, bradycardie symptomatique sous 60/min, hypotension symptomatique sous 100 mm Hg</td><td>"+S('aips-67675-9','aips-47311-8')+"</td></tr>")
add("<li>Si le risque est inférieur à 4 %, alors un rehaussement tardif étendu peut modifier la décision (IIb B)"+S('wa4c20a-45')+".</li>",
    "<li>Si le risque est de 4 à 6 %, alors un défibrillateur peut être envisagé"+S('wa4c20a-45')+".</li><li>Si le risque est inférieur à 4 %, alors un rehaussement tardif de 15 % ou une FEVG inférieure à 50 % peuvent modifier la décision (IIb B)"+S('wa4c20a-45')+".</li>")
add("Si l'épaisseur est inférieure à 15 mm, alors on évalue les autres phénotypes, dont l'hypertension, le cœur d'athlète et les autres cardiomyopathies"+S('wb0f12f-60')+".",
    "Si l'épaisseur est inférieure à 15 mm, alors on évalue les autres phénotypes, dont l'hypertension, le cœur d'athlète et les autres cardiomyopathies"+S('wb0f12f-60')+", sauf chez l'apparenté ou le porteur d'un variant causal, pour qui 13 mm suffisent"+S('wb0f12f-3')+".")
add("Le contrôle du rythme est souvent préféré, car la fibrillation auriculaire est mal tolérée ; le dofétilide et le sotalol peuvent prévenir les récidives"+S('wb0f12f-70')+".",
    "Le contrôle du rythme est souvent préféré, car la fibrillation auriculaire est mal tolérée, et le sotalol peut prévenir les récidives ; le dofétilide cité par la source n'a pas d'information professionnelle suisse"+S('wb0f12f-70')+".")
add("Les résultats génétiques ne servent pas à la stratification du risque rythmique dans les recommandations actuelles",
    "Dans la CMH, les résultats génétiques ne servent pas à la stratification du risque rythmique selon les recommandations actuelles")
add("Étape 2, immédiatement : on choisit la noradrénaline et un bêtabloquant intraveineux, et l'on évite l'adrénaline, dont l'effet inotrope positif augmente le gradient"+S('wb0f12f-77')+".",
    "Étape 2, immédiatement : l'ESC recommande la noradrénaline et un bêtabloquant intraveineux, et l'on évite l'adrénaline, dont l'effet inotrope positif augmente le gradient"+S('wb0f12f-77')+". "
    "Cependant, l'AIPS de Beloc® i.v. (56191) contre-indique le choc cardiogénique et l'insuffisance cardiaque décompensée, et son indication vise les troubles du rythme et l'infarctus, non la CMH"+S('aips-56191-1','aips-56191-6')+". "
    "Si un cardiologue retient le métoprolol, la dose est de 5 mg au début en injection lente de 1 à 2 mg/min, répétable toutes les 5 minutes"+S('aips-56191-2')+". "
    "L'AIPS de Brevibloc® (49576) contre-indique aussi le choc cardiogénique et l'hypotension sévère"+S('aips-49576-10')+". "
    "Si l'esmolol est choisi, la saturation est de 500 µg/kg/min pendant 1 minute, suivie de 50 µg/kg/min pendant 4 minutes"+S('aips-49576-2')+".")
json.dump(C,open('corrections.json','w'),ensure_ascii=False,indent=1)
