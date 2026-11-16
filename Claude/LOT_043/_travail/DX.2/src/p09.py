from lib import *
P = Pt(9)
P.p("Aucun examen ne confirme à lui seul le trouble panique, car il n'existe pas de test diagnostique pour une cause psychogène [wd8c882-37]. "
    "Le bilan se limite donc aux examens minimaux nécessaires pour exclure un problème physique aigu, comme le recommande le guide NICE devant une attaque de panique [wb6b3cd-40].")
P.h("9.a Gold standard")
P.p("Le diagnostic de panique est clinique, puisqu'il repose sur les critères du DSM-5 après exclusion d'une cause médicale [we22718-20]. "
    "Les études utilisent le Mini International Neuropsychiatric Interview ou l'entretien Anxiety Disorders Interview Schedule (ADIS-IV) comme référence pour établir le diagnostic de trouble panique [wb34f75-3][w9a2f8f-13]. "
    "Pour exclure une coronaropathie, la coronarographie est discutée lorsque l'épreuve d'effort est positive ou lorsque l'angor est sévère [wfba9d7-12].")
P.h("9.b Première intention")
P.p("L'ECG est indiqué lors de douleurs thoraciques, de palpitations ou de syncope, et avant toute prescription d'antidépresseur, avec recherche systématique d'un QTc allongé [we22718-25]. "
    "Le bilan sanguin standard comprend la formule sanguine, la thyréostimuline (TSH), la créatinine, les électrolytes et la fonction hépatique [we22718-24]. "
    "Il comprend aussi la glycémie et le bilan lipidique lorsqu'un antidépresseur à profil métabolique défavorable est prescrit [we22718-24]. "
    "Lors d'une douleur thoracique aiguë, les biomarqueurs et l'imagerie complètent l'ECG selon les signaux d'alarme [wbd75ff-11].",
    ("QTc allongé", [
     "Le QTc désigne l'intervalle QT corrigé, et son allongement expose aux torsades de pointes selon l'information professionnelle suisse [aips-55391-14].",
     "L'information professionnelle suisse (AIPS) de la sertraline signale des cas d'allongement du QTc et de torsades de pointes, surtout chez les patients présentant d'autres facteurs de risque [aips-55391-14].",
     "L'AIPS de l'escitalopram contre-indique le médicament en cas d'allongement connu du QT ou de syndrome du QT long congénital [aips-62641-13].",
     "Piège d'examen : un ECG normal en dehors de l'attaque n'exclut pas une tachycardie supraventriculaire paroxystique, qui peut échapper à l'ECG réalisé après l'attaque [wf778c1-35]."]))
P.table(["Examen", "Indication et prescription", "Interprétation"], [
 ["ECG de repos", "Douleur thoracique, palpitations, syncope, avant antidépresseur [we22718-25]", "QTc allongé : contre-indication de l'escitalopram [aips-62641-13]"],
 ["Formule sanguine, TSH, créatinine, électrolytes, tests hépatiques", "Diagnostic différentiel et avant antidépresseur [we22718-24]", "Anémie ou hyperthyroïdie : cause traitable immédiatement [wfba9d7-9]"],
 ["Glycémie, lipides", "Avant antidépresseur à profil métabolique défavorable [we22718-24]", "Adapter le choix du médicament [we22718-24]"],
 ["Troponine et biomarqueurs", "Douleur thoracique aiguë avec signaux d'alarme [wbd75ff-11]", "Positifs : filière du syndrome coronarien aigu [wbd75ff-11]"]])
P.h("9.c Alternatives")
P.p("Lorsque l'épreuve d'effort est impossible, plusieurs alternatives existent : la scintigraphie, l'échographie de stress, l'imagerie par résonance magnétique (IRM) et la tomodensitométrie (CT) multicoupe [wfba9d7-13]. Leur sensibilité atteint 65 à 90 % et leur spécificité 90 à 95 % [wfba9d7-13]. "
    "L'ergométrie est contre-indiquée en cas d'infarctus ou d'angor instable, de sténose aortique sévère, de myopéricardite et de dissection aortique [wfba9d7-10]. "
    "Chez la femme, la sensibilité de l'ergométrie est de 61 % et sa spécificité de 70 %, contre 72 % et 77 % chez l'homme [wfba9d7-11].")
P.h("9.d Deuxième intention")
P.p("Le Holter ne joue qu'un rôle limité dans l'évaluation des palpitations, et il n'est indiqué que si les symptômes surviennent régulièrement chaque jour [wf778c1-10]. "
    "Le monitorage ambulatoire distingue une tachycardie supraventriculaire paroxystique de la panique, car l'ECG réalisé après l'attaque ne montre que des anomalies mineures [wf778c1-35]. "
    "L'échocardiographie bidimensionnelle recherche un prolapsus de la valve mitrale, et la spirométrie avec laryngoscopie recherche un dysfonctionnement des cordes vocales [wf778c1-11][wf778c1-27]. "
    "L'endoscopie digestive confirme le reflux gastro-œsophagien par la lésion de la muqueuse œsophagienne [wf778c1-34].")
P.table(["Résultat", "Signification", "Conduite"], [
 ["ECG, biomarqueurs et imagerie normaux, symptômes cognitifs dominants", "Absence de cause cardiaque probable [wf778c1-38]", "Aborder le diagnostic de trouble panique [wd8c882-37]"],
 ["ECG normal après l'attaque, palpitations persistantes", "Tachycardie supraventriculaire paroxystique possible [wf778c1-35]", "Monitorage ambulatoire [wf778c1-35]"],
 ["Ergométrie négative", "Probabilité post-test de 40 % pour l'exemple discuté [wfba9d7-11]", "Envisager un examen complémentaire si la probabilité post-test dépasse 15 % [wfba9d7-12]"],
 ["Ergométrie positive", "Probabilité post-test de 86 % pour l'exemple discuté [wfba9d7-11]", "Traitement antiangineux et discussion de la coronarographie [wfba9d7-11][wfba9d7-12]"],
 ["TSH ou hémoglobine anormale", "Cause secondaire traitable [wfba9d7-9]", "Traiter la cause avant de conclure à l'anxiété [we22718-21]"]])
P.p("Aucun résultat normal n'exclut définitivement une cause cardiaque, car il n'existe pas de règle établie pour exonérer de façon suffisante les causes cardiaques d'une douleur persistante [w1a9f59-13]. "
    "Des examens périodiques restent justifiés chez les patients dont le bilan antérieur est négatif, parce que certains développent une maladie cardiaque [w1a9f59-13].")
P.save()
