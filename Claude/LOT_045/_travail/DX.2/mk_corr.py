import json
def s(i): return f'<sup class="r"><a href="#sb-{i}">{i}</a></sup>'
C=[]
def c(a,b): C.append({"avant":a,"apres":b})
c("La dose adulte de l'amoxicilline doit être lue dans l'information professionnelle suisse du comprimé choisi, car la fiche consultée pour ce cours concerne la suspension pédiatrique.",
  "Chez l'adulte, l'information suisse d'Amoxi-Mepha recommande 375 à 750 mg, 3 à 4 fois par jour "+s('aips-44911-7')+".")
c("<tr><td>Amoxicilline</td><td>Alternative NICE ; préférée en grossesse</td><td>Voir l'information du comprimé choisi</td><td>Allergie aux pénicillines</td></tr>",
  f"<tr><td>Amoxi-Mepha (amoxicilline), Swissmedic 44911</td><td>Alternative NICE ; préférée en grossesse</td><td>375 à 750 mg, 3 à 4 fois par jour{s('aips-44911-7')}</td><td>Allergie aux pénicillines</td></tr>")
c("<tr><td>Paracétamol</td><td>Antalgique et antipyrétique</td><td>Voir l'information du produit choisi</td><td>Dose maximale quotidienne</td></tr>",
  f"<tr><td>Dafalgan® (paracétamol), Swissmedic 46206</td><td>Antalgique et antipyrétique</td><td>Adulte de plus de 40 kg : jusqu'à 4 x 1 à 2 comprimés par jour, maximum 4000 mg par jour{s('aips-46206-3')}{s('aips-46206-4')}</td><td>Intervalle de 4 à 8 h entre les prises{s('aips-46206-3')}</td></tr>")
c("<td>Dose la plus faible, durée la plus courte"+s('aips-49156-3')+"</td>",
  "<td>Céphalées : dose simple de 400 mg, dose journalière maximale de 2400 mg, la plus faible possible"+s('aips-49156-4')+"</td>")
c("Il définit la bronchite aiguë par une infection aiguë des voies respiratoires inférieures, avec une toux dominante, d'une durée d'au plus 3 semaines"+s('wd1575e-4')+".",
  "La guideline européenne DEGAM retient une toux aiguë de moins de 8 semaines "+s('w08df78-1')+". À titre complémentaire, le CHEST, source américaine, définit la bronchite aiguë par une infection aiguë des voies respiratoires inférieures, avec une toux dominante, d'une durée d'au plus 3 semaines"+s('wd1575e-4')+".")
c('<div class="p">Ce tableau résume les médicaments utiles, et il montre que seule la doxycycline possède une dose lue dans l\'information suisse pour cette indication.</div>\n',"")
c("<tr><td>CRP nettement élevée</td><td>Inflammation marquée, pneumonie possible</td><td>Radiographie, discussion d'antibiotique</td></tr>\n","")
c(" Chez un patient allergique à l'iode, on évite les produits de contraste et l'on choisit un scanner sans injection ou une autre méthode.","")
json.dump(C,open('Claude/LOT_045/_travail/DX.2/corrections.json','w'),ensure_ascii=False,indent=1)
