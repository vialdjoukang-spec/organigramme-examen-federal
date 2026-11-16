import re
D='fragments/'
def c(i): return '<sup class="r"><a href="#sb-%s">%s</a></sup>'%(i,i)
def sub(f,a,b):
    t=open(D+f,encoding='utf-8').read()
    assert t.count(a)==1,(f,a[:60],t.count(a))
    open(D+f,'w',encoding='utf-8').write(t.replace(a,b))
sub('p11.html',"Aucune monopréparation suisse n'a été lue pour l'association amoxicilline-acide clavulanique, donc la classe et la conduite sont enseignées sans dose (voir HELP).",
 "Chez l'adulte, la ceftriaxone (Rocephin®, n° 44625) se donne en général à 1 à 2 g une fois par jour"+c('aips-44625-4')+". Lors d'infection sévère ou de germes moyennement sensibles, cette dose quotidienne unique peut atteindre 4 g"+c('aips-44625-4')+". Rocephin est contre-indiqué en cas d'hypersensibilité à toute céphalosporine, et la préparation ne doit pas être utilisée pendant l'allaitement"+c('aips-44625-11')+c('aips-44625-40')+". Pendant la grossesse, Rocephin ne s'administre que lorsqu'il est formellement indiqué"+c('aips-44625-38')+".</div>\n"
 "<div class=\"p\">L'association amoxicilline-acide clavulanique (Co-Amoxi-Mepha® i.v., n° 56758) se donne chez l'adulte à 1200 mg 3 à 4 fois par jour en injection intraveineuse lente dans les infections de gravité modérée"+c('aips-56758-5')+". Dans les infections graves, la dose est de 2200 mg 3 à 4 fois par jour en perfusion brève d'au moins 30 minutes"+c('aips-56758-5')+". L'hypersensibilité aux pénicillines et aux céphalosporines contre-indique ce traitement"+c('aips-56758-9')+". Pendant la grossesse, il ne devrait être utilisé qu'en cas de nécessité absolue, et il ne faudrait pas allaiter pendant le traitement"+c('aips-56758-17')+c('aips-56758-18')+".")
sub('p11.html',"<tr><td>Amoxicilline + acide clavulanique</td><td>Pneumonie associée à l'AVC</td><td>IV, selon protocole local (sans dose ici)</td><td>Non lu (HELP)</td></tr>",
 "<tr><td>Co-Amoxi-Mepha® i.v. (amoxicilline-acide clavulanique)</td><td>Pneumonie associée à l'AVC</td><td>IV, 1200 mg 3 à 4 fois par jour ; infection grave 2200 mg 3 à 4 fois par jour"+c('aips-56758-5')+"</td><td>56758</td></tr>")
sub('p11.html',"<tr><td>Ceftriaxone, céfotaxime</td><td>Alternatives de première ligne</td><td>IV, selon protocole local (sans dose ici)</td><td>Non lu (HELP)</td></tr>",
 "<tr><td>Rocephin® (ceftriaxone)</td><td>Première ligne</td><td>IV, 1 à 2 g une fois par jour"+c('aips-44625-4')+"</td><td>44625</td></tr>")
sub('p11.html',"L'AIPS compte un NIHSS supérieur à 25 parmi les contre-indications, ainsi qu'une héparine reçue dans les 48 heures avant les symptômes","L'AIPS compte parmi les contre-indications un NIHSS supérieur à 25 et une héparine reçue dans les 48 heures avec un aPTT élevé à l'admission")
sub('p11.html',"Aucun médicament n'est validé pour améliorer directement la déglutition après AVC dans les sources lues.","Aucun médicament n'améliore la déglutition après AVC avec une certitude suffisante, car les essais disponibles restent rares et de certitude très faible"+c('we52567-6')+".")
sub('p11.html'," Par ailleurs, la couverture assurantielle précise des soins de déglutition n'est pas établie par les sources lues (voir HELP).","")
sub('p08.html',"Le résumé lu de la recommandation ESO/ESSD de 2021 pose une démarche en deux temps, sans critères diagnostiques chiffrés","La recommandation ESO/ESSD de 2021 pose une démarche en deux temps, dépistage puis évaluation, sans critères diagnostiques chiffrés")
