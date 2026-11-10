S='/home/user/wt/lot-054/Claude/LOT_054/_travail/DX.3/src/'
def sub(f,old,new):
    s=open(S+f).read()
    if old not in s: print('ABSENT',f,old[:70]); return
    open(S+f,'w').write(s.replace(old,new,1))
sub('p07.html',"qui sont des indications opératoires absolues.[[DM-247]]","qui constituent donc des indications opératoires absolues.[[DM-247]]")
sub('p08.html',"notamment s'il existe un risque d'atteinte","notamment lorsqu'il existe un risque d'atteinte")
sub('p11.html',"La voie transurétrale est privilégiée, et l'HBP,","La voie transurétrale est privilégiée, puisque l'HBP,")
sub('p11.html',"à cause du risque de caillotage vésical.[[R541-26]]","car le risque de caillotage vésical est élevé.[[R541-26]]")
sub('p11.html',"a besoin d'un apprentissage et d'un soutien. L'EAU demande d'instruire le patient sur la technique et les risques du cathétérisme intermittent.[[NU-95]] Elle note aussi que la dextérité manuelle conditionne la poursuite du geste.[[NU-88]]","a besoin d'un apprentissage et d'un soutien, car la dextérité manuelle conditionne la poursuite du geste.[[NU-88]] L'EAU demande d'instruire le patient sur la technique et les risques du cathétérisme intermittent.[[NU-95]]")
