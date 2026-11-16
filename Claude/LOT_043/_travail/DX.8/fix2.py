import glob
R=[
("jusqu'à 1 % des admissions. Ces chiffres sont probablement sous-estimés, car les formes légères restent en ambulatoire.{w8806c9-13}","jusqu'à 1 % des admissions.{w8806c9-13} Ces chiffres sont probablement sous-estimés, car les formes légères restent en ambulatoire.{w8806c9-13}"),
("récente étaient associés à un résultat défavorable à douze mois. La vaccination","récente étaient associés à un résultat défavorable à douze mois.{w737299-10} La vaccination"),
("Une dyspnée apparaît chez 19 à 49 % d'entre eux et une syncope chez 5 à 7 %. Des signes","Une dyspnée apparaît chez 19 à 49 % d'entre eux et une syncope chez 5 à 7 %.{PMC13057090-2} Des signes"),
("la protéine C-réactive médiane était de 33,3 mg/L. Cependant,","la protéine C-réactive médiane était de 33,3 mg/L.{w737299-29} Cependant,"),
("27,7 % des patients avaient une protéine C-réactive à 10 mg/L ou moins. Dans l'étude","27,7 % des patients avaient une protéine C-réactive à 10 mg/L ou moins.{w737299-29} Dans l'étude"),
("La dose est de 0,5 mg deux fois par jour chez l'adulte de plus de 70 kg. Elle","La dose est de 0,5 mg deux fois par jour chez l'adulte de plus de 70 kg.{aips-67974-4} Elle"),
("dans la phase de sevrage randomisée de l'essai RHAPSODY. L'anakinra l'a ramené à 18 % contre 90 % dans l'essai AIRTRIP.{wa67766-15}","dans la phase de sevrage randomisée de l'essai RHAPSODY.{wa67766-15} L'anakinra a ramené ce taux à 18 % contre 90 % dans l'essai AIRTRIP.{wa67766-15}"),
("</button> sert de repère pour tout le cours.","</button> est le repère de tout le cours."),
("La sérologie virale systématique n'est plus recommandée par les textes de 2025, sauf dans des situations choisies.","Les sérologies virales systématiques ne sont plus recommandées par les textes de 2025, sauf dans des situations choisies."),
("Non, car l'infarctus donne un décalage régional avec image en miroir, alors que la péricardite donne un décalage diffus","Non, car l'infarctus montre un décalage régional avec image en miroir, alors que la péricardite montre un décalage diffus"),
("Non, car cette catégorie regroupe myocardite","Non, car cette catégorie comprend myocardite"),
("Ce sont l'insuffisance rénale grave avec un débit de filtration glomérulaire estimé inférieur à 30 mL/min, l'atteinte hépatique sévère, la grossesse, l'allaitement et l'association avec des inhibiteurs de la glycoprotéine P ou du CYP3A4.","Ce sont l'insuffisance rénale grave avec un débit de filtration glomérulaire estimé inférieur à 30 mL/min et l'atteinte hépatique sévère. Ce sont aussi la grossesse, l'allaitement et l'association avec des inhibiteurs de la glycoprotéine P ou du CYP3A4.{aips-67974-7}"),
]
for f in glob.glob('t/p*.txt'):
    s=open(f,encoding='utf8').read(); o=s
    for a,b in R: s=s.replace(a,b)
    if s!=o: open(f,'w',encoding='utf8').write(s)
