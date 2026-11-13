import sys
P={
'p01':[("Dans ces cas, une grande confiance dans le diagnostic est indispensable[[w2e975a-30]]","Dans ces cas, une grande confiance dans le diagnostic est indispensable, car ces gestes sont difficilement réversibles[[w2e975a-30]]"),
("se chevaucher, de sorte qu'un patient présente parfois les deux","se chevaucher, ce qui explique qu'un patient présente parfois les deux"),
("Le consensus de Lyon actualisé précise que les symptômes dyspeptiques","Le consensus de Lyon actualisé précise en outre que les symptômes dyspeptiques")],
'p02':[("Parmi les 102 études incluses, 66","Ainsi, parmi les 102 études incluses, 66"),
("L'obésité est le facteur le plus net : la prévalence atteint","L'obésité est le facteur le plus net, car la prévalence atteint"),
("Les boissons gazeuses et le café ou le thé sont aussi associés","En outre, les boissons gazeuses et le café ou le thé sont associés"),
("La sténose peptique reste la plus fréquente des sténoses bénignes de l'œsophage, mais son incidence","Ainsi, la sténose peptique reste la plus fréquente des sténoses bénignes de l'œsophage, mais son incidence"),
("Le RGO pèse aussi sur les coûts, qui sont","Par ailleurs, le RGO pèse sur les coûts, qui sont"),
("Pourtant, des affections","Cependant, des affections")],
'p03':[("Cette exposition résulte d'une barrière","Cette exposition résulte, en effet, d'une barrière"),
("Une compliance accrue de la jonction","Ainsi, une compliance accrue de la jonction"),
("Une fois actifs, ils inhibent","Ainsi, une fois actifs, ils inhibent")],
'p04':[("La réponse à la trinitrine ne doit pas servir au diagnostic","En effet, la réponse à la trinitrine ne doit pas servir au diagnostic"),
("Dans une série de 219 patients","Par ailleurs, dans une série de 219 patients"),
("Elle peut coexister avec le RGO, sans lien","Elle peut en outre coexister avec le RGO, sans lien"),
("Elle peut se manifester par des douleurs thoraciques ou des régurgitations[[rms2026rgo-19]]","Elle peut donc se manifester par des douleurs thoraciques ou des régurgitations, ce qui la rapproche du reflux[[rms2026rgo-19]]")],
'p05':[("Il se pratique au comptoir de la pharmacie, dans un espace de consultation séparé","Il se pratique, lorsque la patiente est dirigée vers la pharmacienne, dans un espace de consultation séparé"),
("Une douleur qui s'aggrave à l'effort, à la respiration ou au mouvement, ou qui siège à gauche, s'associe","Ainsi, une douleur qui s'aggrave à l'effort, à la respiration ou au mouvement, ou qui siège à gauche, s'associe"),
("Certaines positions, comme l'antéflexion","Par ailleurs, certaines positions, comme l'antéflexion"),
("Une douleur thoracique irradiante et des signes d'hémorragie digestive relèvent","Par ailleurs, une douleur thoracique irradiante et des signes d'hémorragie digestive relèvent")],
'p06':[("Une instabilité hémodynamique associée","Ainsi, une instabilité hémodynamique associée")],
'p07':[("en ensembles cliniques qui se distinguent par leurs signes","en ensembles cliniques, puisqu'ils se distinguent par leurs signes"),
("Ils s'expliquent par une hypersensibilité viscérale","Ils s'expliquent, en effet, par une hypersensibilité viscérale")],
'p08':[("Les patients qui remplissent ce seuil sur au moins 2 jours","En effet, les patients qui remplissent ce seuil sur au moins 2 jours"),
("La classification de Los Angeles, elle, est","Cependant, la classification de Los Angeles est")],
'p09':[("Elle est indispensable avant une prise en charge invasive, afin d'éliminer un trouble moteur comme l'achalasie","Elle est indispensable avant une prise en charge invasive, car elle permet d'éliminer un trouble moteur comme l'achalasie"),
("Son usage reste non standardisé","Cependant, son usage reste non standardisé")],
'p11':[("Il recommande aussi d'éviter la charcuterie","Il recommande en outre d'éviter la charcuterie"),
("Les patients dont l'œsophagite n'est pas totalement guérie ou dont les symptômes persistent peuvent être traités 4 semaines de plus[[aips-60574-4]]","Si l'œsophagite n'est pas totalement guérie ou si les symptômes persistent, les patients peuvent être traités 4 semaines de plus[[aips-60574-4]]"),
("En présence de méthotrexate à fortes doses, il est recommandé de suspendre l'IPP","Si le patient reçoit du méthotrexate à fortes doses, il est recommandé de suspendre l'IPP"),
("Les effets très rares comprennent","En revanche, les effets très rares comprennent"),
("L'ésoméprazole ne doit pas être utilisé pendant l'allaitement","Par ailleurs, l'ésoméprazole ne doit pas être utilisé pendant l'allaitement"),
("Il conclut qu'une limitation du remboursement","Par ailleurs, il conclut qu'une limitation du remboursement"),
("L'information professionnelle recommande une surveillance médicale régulière","En outre, l'information professionnelle recommande une surveillance médicale régulière"),
("La NICE rappelle que les risques de la surveillance","Cependant, la NICE rappelle que les risques de la surveillance")],
'p12':[("S'y ajoute la surélévation de la tête du lit","En outre, la surélévation de la tête du lit s'y ajoute"),
("Le pharmacien suisse limite cette co-prescription","Cependant, le pharmacien suisse limite cette co-prescription"),
("reste prescrit au long cours pour limiter la récidive[[w2082ec-11 w864e80-2]]","reste prescrit au long cours, afin de réduire le besoin de dilatations répétées[[w2082ec-11 w864e80-2]]"),
("La Société européenne d'endoscopie gastro-intestinale indique la technique","La Société européenne d'endoscopie gastro-intestinale indique en outre la technique")],
}
for k,L in P.items():
    f=f'src/{k}.txt'; t=open(f).read()
    for a,b in L:
        if a not in t: print('MISS',k,a[:50]); continue
        t=t.replace(a,b)
    open(f,'w').write(t)
