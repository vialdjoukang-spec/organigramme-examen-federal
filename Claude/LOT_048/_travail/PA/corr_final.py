import re,sys
D='fragments/'
def c(i): return '<sup class="r"><a href="#sb-%s">%s</a></sup>'%(i,i)
def sub(f,a,b):
    t=open(D+f,encoding='utf-8').read()
    assert t.count(a)==1,(f,a[:60],t.count(a))
    open(D+f,'w',encoding='utf-8').write(t.replace(a,b))
sub('p04.html',"La valeur prédictive positive de la dysphagie pour un cancer digestif haut atteint 66,7 % dans une grande cohorte"+c('wd122d9-3')+".",
 "En médecine de premier recours, la valeur prédictive positive de la dysphagie pour un cancer de l'œsophage atteint jusqu'à 5,5 %, ce qui justifie l'endoscopie rapide"+c('w2aac93-128')+". Une cohorte endoscopique de patients dyspeptiques a rapporté 66,7 % pour ce signe, mais ce chiffre vient d'un centre tertiaire et ne s'applique pas au premier recours"+c('wd122d9-3')+".")
sub('p05.html',"mais la dysphagie a une valeur prédictive positive de 66,7 %"+c('wd122d9-3')+".",
 "mais la dysphagie a une valeur prédictive positive allant jusqu'à 5,5 % pour le cancer de l'œsophage en premier recours"+c('w2aac93-128')+".")
sub('p14.html',"La valeur prédictive positive de la dysphagie atteint 66,7 % dans une cohorte"+c('wd122d9-3')+".",
 "En premier recours, la valeur prédictive positive de la dysphagie atteint jusqu'à 5,5 % pour le cancer de l'œsophage, ce qui suffit à justifier l'endoscopie rapide"+c('w2aac93-128')+".")
# p09
sub('p09.html',"inférieure à 2 mm²/mmHg indique une mauvaise distensibilité","inférieure ou égale à 2,0 mm²/mmHg indique une mauvaise distensibilité")
sub('p09.html',"<td>Distensibilité inférieure à 2 mm²/mmHg</td>","<td>Distensibilité inférieure ou égale à 2,0 mm²/mmHg</td>")
# p10
sub('p10.html',"<li>Le consensus cite une endoscopie en accès direct dans les 2 semaines pour tout patient dysphagique","<li>Le consensus cite la recommandation britannique NICE, qui offre une endoscopie en accès direct dans les 2 semaines à tout patient dysphagique")
# p11
sub('p11.html',"avec 40 mg en cas de réponse insuffisante"+c('aips-56313-5'),"et à 40 mg après réponse insuffisante à d'autres traitements"+c('aips-56313-5'))
sub('p11.html',"<td>20 mg une fois par jour, 40 mg si réponse insuffisante "+c('aips-56313-5')+"</td>","<td>20 mg une fois par jour ; 40 mg si réponse insuffisante à d'autres traitements "+c('aips-56313-5')+"</td>")
sub('p11.html',"La grossesse doit être évitée sans argument solide, et les candidoses buccales et œsophagiennes sont fréquentes sous traitement","Pendant la grossesse, l'administration doit être évitée sauf arguments solides, et les candidoses buccales, oropharyngées et œsophagiennes sont fréquentes sous traitement")
sub('p11.html',"Le comprimé se prend après un repas, posé sur la langue"+c('aips-66999-4')+".","Le comprimé se prend après un repas, posé sur la langue"+c('aips-66999-4')+". Les patients atteints de troubles de la fonction hépatique ne doivent pas être traités"+c('aips-66999-4')+".")
sub('p11.html',"et il est à éviter pendant la grossesse sans infection sévère","et il est évité pendant la grossesse sauf infection fongique sévère ou potentiellement létale")
sub('p11.html',"Les bisphosphonates se prennent debout avec un grand verre d'eau, et le patient reste assis ou debout au moins 30 minutes","Les bisphosphonates s'avalent après le lever avec un grand verre d'eau, et le patient ne se recouche qu'après 30 minutes au moins et après le premier repas")
sub('p11.html',"Par ailleurs, le traitement de l'œsophagite à herpès ou à cytomégalovirus se décide avec un infectiologue, sans dose enseignée ici.</div>",
 "Par ailleurs, l'aciclovir intraveineux (Zovirax® i.v., n° 44772) se perfuse lentement, en une heure, à 5 mg/kg toutes les 8 heures dans l'infection à Herpes simplex, et le traitement dure habituellement 5 jours"+c('aips-44772-4')+". Pendant la grossesse, le traitement intraveineux et oral n'est indiqué qu'en cas de nécessité impérieuse, et il ne faut pas allaiter pendant un traitement par Zovirax"+c('aips-44772-21')+c('aips-44772-23')+".</div>\n"
 "<div class=\"p\">Pour l'infection à cytomégalovirus de l'immunodéprimé, le ganciclovir (Cymevene®, n° 49188) se donne en perfusion intraveineuse d'une heure à 5 mg/kg toutes les 12 heures pendant 14 à 21 jours, si la fonction rénale est normale"+c('aips-49188-4')+". Cymevene est contre-indiqué pendant la grossesse et l'allaitement"+c('aips-49188-8')+". Cependant, il ne doit pas être administré pendant la grossesse sauf si le bénéfice thérapeutique pour la mère l'emporte sur le risque tératogène potentiel, et il convient de ne pas allaiter"+c('aips-49188-27')+c('aips-49188-28')+".</div>")
old=re.search(r"<tr><td>Acyclovir-Mepha® \(aciclovir\)</td>.*?</tr>",open(D+'p11.html',encoding='utf-8').read()).group(0)
new=("<tr><td>Zovirax® i.v. (aciclovir)</td><td>Infections herpétiques des muqueuses</td><td>5 mg/kg i.v. en une heure toutes les 8 heures, habituellement 5 jours "+c('aips-44772-4')+"</td><td>Nécessité impérieuse ; ne pas allaiter "+c('aips-44772-21')+"</td><td>44772</td></tr>\n"
 "<tr><td>Cymevene® (ganciclovir)</td><td>Infection à cytomégalovirus de l'immunodéprimé</td><td>5 mg/kg i.v. en une heure toutes les 12 heures, 14 à 21 jours "+c('aips-49188-4')+"</td><td>Contre-indiqué ; ne pas allaiter "+c('aips-49188-8')+"</td><td>49188</td></tr>")
sub('p11.html',old,new)
# capitales fautives après connecteur
for f in ['p01','p02','p05','p08','p09','p11','p12']:
    t=open(D+f+'.html',encoding='utf-8').read()
    t2=re.sub(r"(Ensuite|En outre|Par ailleurs), (L'|Elles|Entre|Il |Le |La |Les |Un |Une |Ce |Cet )",lambda m:m.group(1)+', '+m.group(2)[0].lower()+m.group(2)[1:],t)
    open(D+f+'.html','w',encoding='utf-8').write(t2)
