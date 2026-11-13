from lib import *
P = Pt(14)
P.p("Les pièges de l'examen portent sur la confusion entre douleur cardiaque et douleur anxieuse, car aucun test ne confirme le diagnostic [wd8c882-37]. Ils portent aussi sur les critères de durée et sur le choix du médicament [we22718-33].")
P.table(["Question", "Réponse", "Raison"], [
 ["Une douleur thoracique avec un examen normal et une anxiété évidente permet-elle de conclure à une panique sans ECG ?", "Non, l'ECG reste nécessaire [we22718-25]", "Le trouble panique coexiste avec des maladies cardiaques [wf778c1-36]"],
 ["Une attaque de panique unique suffit-elle pour le diagnostic de trouble panique ?", "Non [we22718-31]", "Environ une personne sur cinq en vit une, et il faut un mois de crainte persistante [we22718-33]"],
 ["La localisation de la douleur distingue-t-elle la panique de la coronaropathie ?", "Non [w587cc6-29]", "Toutes les étiologies siègent surtout à gauche en avant du thorax [w587cc6-29]"],
 ["Une douleur reproductible à la palpation exclut-elle un infarctus ?", "Non [wfba9d7-5]", "Une douleur pleinement reproductible correspond encore à 5 % d'infarctus [wfba9d7-5]"],
 ["Quelle est la dose initiale de la sertraline dans le trouble panique selon l'AIPS ?", "25 mg par jour pendant une semaine, puis 50 mg par jour [aips-55391-6]", "Une dose initiale faible limite les effets indésirables du début du traitement [wb6b3cd-49]"],
 ["Quelle est la dose maximale d'alprazolam dans le trouble panique ?", "6 mg par jour [aips-43216-6]", "Les doses élevées augmentent le risque de dépendance [aips-43216-10]"],
 ["Les benzodiazépines sont-elles recommandées au long cours dans la panique ?", "Non, selon le NICE [wb6b3cd-44]", "Elles sont associées à une moins bonne évolution à long terme [wb6b3cd-44]"],
 ["Quand juge-t-on l'efficacité d'un premier traitement ?", "Après au moins 12 semaines [w85c0ac-16]", "L'effet anxiolytique de l'antidépresseur commence après 2 à 8 semaines [w85c0ac-16]"],
 ["Qu'est-ce que la fausse alarme de suffocation ?", "Une hypersensibilité du détecteur de suffocation au CO2 [wb1bfcb-26]", "L'hyperventilation devient une défense contre l'alarme [wb1bfcb-26]"]])
P.save()
