import re
D='fragments/'
def c(i): return '<sup class="r"><a href="#sb-%s">%s</a></sup>'%(i,i)
def sub(f,a,b):
    t=open(D+f,encoding='utf-8').read()
    assert t.count(a)==1,(f,a[:60],t.count(a))
    open(D+f,'w',encoding='utf-8').write(t.replace(a,b))
sub('p04.html',"La dysphagie est le seul signe d'alarme dont la valeur prédictive positive atteint 66,7 % pour un cancer digestif haut, dans une cohorte de dyspepsie"+c('wd122d9-3')+". Sa sensibilité reste basse,",
 "En médecine de premier recours, la valeur prédictive positive de la dysphagie pour un cancer de l'œsophage atteint jusqu'à 5,5 %, d'où l'endoscopie rapide"+c('w2aac93-128')+". Une cohorte endoscopique de patients dyspeptiques a rapporté 66,7 % pour ce signe, mais ce chiffre vient d'un centre tertiaire et ne s'applique pas au premier recours"+c('wd122d9-3')+". La sensibilité des signes d'alarme reste basse,")
sub('p04.html',"<td>Endoscopie normale chez 10 % des patients atteints</td>","<td>Au moins 10 % des patients dysphagiques aux solides ont une endoscopie d'apparence normale "+c('w2aac93-133')+"</td>")
sub('p08.html',"Une étude chinoise définit la sténose par un diamètre inférieur à 11 mm"+c('wf2638c-10')+". ","")
sub('p10.html',"Si le patient saigne, une endoscopie digestive haute en urgence est nécessaire"+c('aips-55609-13')+".","Si le patient présente une hématémèse ou un méléna, il faut exclure une malignité avant tout inhibiteur de la pompe à protons, car le traitement retarde le diagnostic"+c('aips-55609-13')+".")
sub('p10.html',"<li><div class=\"p\">Si une tumeur est prouvée, le patient quitte cet arbre pour la prise en charge du cancer de l'œsophage, qui relève d'une autre leçon.</div></li>\n","")
sub('p11.html',"Si besoin, la dose habituelle de 1 comprimé de 40 mg par jour peut être doublée dans certains cas d'œsophagite"+c('aips-59834-8')+".",
 "La dose de 40 mg par jour peut être doublée dans certains cas, notamment l'œsophagite de reflux non guérie par d'autres médicaments"+c('aips-59834-8')+". Chez le patient âgé ou insuffisant rénal, la dose journalière de 40 mg ne doit pas être dépassée"+c('aips-59834-11')+".")
sub('p11.html',"<td>20 mg par jour ; 40 mg si réponse insuffisante"+c('aips-56313-5')+"</td>","<td>20 mg par jour ; 40 mg si réponse insuffisante à d'autres traitements"+c('aips-56313-5')+"</td>")
sub('p11.html',"<td>Orale, matin, au moins 30 minutes avant le repas</td>","<td>Orale, matin, au moins 30 minutes avant le repas"+c('aips-57801-5')+"</td>")
sub('p11.html',"La guérison survient chez la plupart des patients au bout de quatre semaines"+c('aips-57801-9')+".","La guérison survient chez la plupart des patients au bout de quatre semaines, et une poursuite de deux semaines supplémentaires suffit dans la plupart des cas si ce délai est insuffisant"+c('aips-57801-9')+".")
sub('p11.html',"En cas d'insuffisance rénale, l'ésoméprazole ne nécessite aucun ajustement"+c('aips-55609-10')+".","En cas d'insuffisance rénale, l'ésoméprazole ne nécessite aucun ajustement, mais l'insuffisance rénale sévère impose la prudence faute d'expérience"+c('aips-55609-10')+".")
