from common import *
p=Pt(14)
p.P("""Les questions d'examen fédéral sur le syndrome d'Ogilvie testent trois réflexes : exclure l'obstacle, mesurer le cæcum et choisir la bonne étape thérapeutique. Chaque piège est présenté sous forme de question, avec sa réponse et sa raison.""")
p.H("14.a Les pièges diagnostiques")
p.P("""Première question : un patient de soixante-dix ans présente un ventre distendu cinq jours après une prothèse de hanche, avec arrêt des gaz. Faut-il poser le diagnostic de syndrome d'Ogilvie sur le contexte ? La réponse est non, car le diagnostic est un diagnostic d'exclusion et le profil de risque seul ne suffit pas{wd21b7d-178 wd21b7d-181}. Le scanner avec injection doit d'abord exclure l'obstruction mécanique{wd21b7d-179}.""")
p.P("""Deuxième question : la radiographie simple montre un signe du grain de café chez un patient hospitalisé. S'agit-il d'un Ogilvie ? La réponse est non : ce signe évoque un volvulus, dont la radiographie a une faible sensibilité, ce qui impose le scanner{wd21b7d-169}. La raison est qu'un volvulus du cæcum a déjà été pris pour un syndrome d'Ogilvie{wd21b7d-574}, alors qu'il relève de la chirurgie d'emblée{w1306ed-11}.""")
p.H("14.b Les pièges thérapeutiques")
p.P("""Troisième question : quel diamètre du cæcum fait craindre la perforation ? La réponse est 9 à 12 cm pour une perforation imminente{wd21b7d-181}. Un traitement conservateur reste possible de 48 à 72 heures tant que le diamètre est inférieur à 12 cm, car le patient est alors stable{wd21b7d-183}. La raison est que le risque de perforation augmente avec le diamètre, de 0 % sous 12 cm à 23 % au-dessus de 14 cm{wd5dad6-5}.""")
p.P("""Quatrième question : peut-on donner de la néostigmine à ce patient ? La réponse dépend de la preuve de l'absence d'obstacle mécanique, qui est une contre-indication{aips-49389-5}, de l'absence de bradycardie sévère ou de bronchospasme{aips-49389-6}, et d'un monitorage cardiaque{wd21b7d-186}. La raison est que le médicament stimule le système cholinergique, d'où la bradycardie{aips-49389-13}. De plus, la spécialité de l'AIPS est une association avec le glycopyrronium, indiquée pour la levée de curarisation{aips-49389-1}.""")
p.P("""Cinquième question : après la résolution de la dilatation, faut-il arrêter tout traitement ? La réponse est non, car le polyéthylèneglycol oral est recommandé pour prévenir la récidive{wd21b7d-187}. La raison est que la récidive touche 17,1 % des patients après une décompression réussie{wd24a99-5}.""")
p.T(["Question","Réponse","Raison"],[
["Ogilvie sur le seul contexte postopératoire ?","Non, scanner avec injection d'abord {wd21b7d-179}","Diagnostic d'exclusion {wd21b7d-178}"],
["Signe du grain de café ?","Volvulus, pas Ogilvie {wd21b7d-169}","Chirurgie d'emblée pour le cæcum {w1306ed-11}"],
["Cæcum à 12 cm ou plus ?","Intervenir : néostigmine ou endoscopie {wd21b7d-186}","Perforation imminente {wd21b7d-181}"],
["Néostigmine sans scanner ?","Non {aips-49389-5}","Obstruction mécanique contre-indiquée {aips-49389-5}"],
["Opiacés poursuivis ?","Non, les arrêter {wd21b7d-184}","Frein à la motricité colique {wd21b7d-184}"],
["Traitement arrêté après résolution ?","Non, polyéthylèneglycol {wd21b7d-187}","Récidive {wd24a99-5}"]])
p.P("""Le candidat qui retient ces six paires évite l'essentiel des pièges : il exclut l'obstacle, mesure le cæcum, respecte les contre-indications du médicament et prévient la récidive.""")
p.save()
