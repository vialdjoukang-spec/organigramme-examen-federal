from lib import *
P = Pt(13)
P.raw('<ul>')
for t in ["Une douleur thoracique aiguë impose d'abord l'ECG et la recherche d'une cause grave, car la panique ne se diagnostique pas sans exclure le syndrome coronarien aigu [wf778c1-37].",
 "Le trouble panique associe des attaques inattendues, dont l'acmé survient en quelques minutes, à au moins un mois de crainte persistante ou d'évitement [we22718-33].",
 "Une attaque isolée ne suffit pas, car environ une personne sur cinq en vit une au cours de sa vie [we22718-31].",
 "Un ISRS ou une thérapie cognitivo-comportementale, seuls ou associés, constituent le traitement de première intention, et l'efficacité se juge après au moins 12 semaines [we22718-65][we22718-62].",
 "Le NICE déconseille les benzodiazépines dans le trouble panique, car elles sont associées à une moins bonne évolution à long terme [wb6b3cd-44].",
 "La panique n'exclut jamais une maladie cardiaque, car elle coexiste avec la coronaropathie et augmente le risque d'événements cardiaques majeurs chez le coronarien [wf778c1-36]."]:
    P.out.append(f'<li>{c(t)}</li>')
P.raw('</ul>')
P.save()
