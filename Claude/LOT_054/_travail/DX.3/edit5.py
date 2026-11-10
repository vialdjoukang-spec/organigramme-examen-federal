S='/home/user/wt/lot-054/Claude/LOT_054/_travail/DX.3/src/'
def sub(f,old,new):
    s=open(S+f).read()
    if old not in s: print('ABSENT',f,old[:70]); return
    open(S+f,'w').write(s.replace(old,new,1))
sub('p01.html',"Cette distinction compte, car une vessie à haute pression menace les reins, alors qu'une vessie hypotonique expose surtout aux infections et au regorgement.[[NU-58,R541-13]]","Cette distinction compte, car il faut maintenir la pression du détrusor dans des limites sûres pour protéger les reins.[[NU-58]]")
sub('p03.html'," Il protège la continence pendant le remplissage.</div>","</div>")
sub('p07.html',"Le mécanisme est une pression élevée qui se transmet au rein ou une stase qui favorise la lithiase et l'infection.[[NU-55,R541-28]]","Le mécanisme est une pression élevée qui se transmet au rein ou une vidange incomplète qui favorise l'infection.[[NU-55,NU-60]]")
sub('p09.html',"L'EAU la réalise par échographie transabdominale, par bladder scan (échographe portable de la vessie) ou par sondage.[[DX-30]]","Selon l'EAU, elle se réalise par échographie transabdominale, par bladder scan (échographe portable de la vessie) ou par sondage.[[DX-30]]")
sub('p11.html',"Le cathétérisme intermittent s'impose dès que le résidu dépasse 300 mL ou que le haut appareil est menacé.[[DM-406]]","Le cathétérisme intermittent est recommandé, avec un grade faible, dès que le haut appareil est menacé ou que le résidu dépasse 300 mL.[[DM-406]]")
sub('p11.html',"Le cathétérisme intermittent est le traitement de première intention de l'homme dont le résidu dépasse 300 mL ou dont le haut appareil est menacé.[[DM-406]]","Le cathétérisme intermittent est le traitement de première intention de l'homme atteint de vessie hypoactive dont le résidu dépasse 300 mL.[[DM-406]] Il est aussi recommandé, avec un grade faible, si le haut appareil est menacé.[[DM-406]]")
sub('p11.html',"Le patient peut sortir lorsque la reprise mictionnelle est obtenue, ou lorsqu'un mode de drainage sûr est organisé. La Revue","Le patient peut sortir lorsque la reprise mictionnelle est obtenue, ou lorsqu'un mode de drainage sûr est organisé, car un traitement ambulatoire est possible en l'absence de complication.[[R541-29]] La Revue")
sub('p12.html',"Une revue de pharmacovigilance note que","Une revue sur les rétentions d'origine médicamenteuse note que")
sub('p12.html',"La surveillance du haut appareil par échographie tous les six mois pour les patients à haut risque évite l'insuffisance rénale.[[NU-170]]","La surveillance du haut appareil par échographie, environ tous les six mois chez les patients à haut risque, vise à prévenir l'insuffisance rénale.[[NU-170]]")
