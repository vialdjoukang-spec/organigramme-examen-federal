import glob,re
A={
"P: Le vocabulaire temporel suit":" Ces seuils comptent, car ils déterminent la durée du traitement.",
"P: L'inflammation aiguë est aussi un déclencheur":" Cette arythmie peut donc révéler une atteinte du myocarde.",
"P: Le sus-décalage du segment ST pose":" Cette différence est donc la première clé de lecture du tracé.",
"P: Trois diagnostics se jouent":" Cette hiérarchie compte, car l'atteinte du myocarde change la surveillance.",
"P: La douleur thoracique est le symptôme le plus fréquent":" La douleur seule ne suffit donc pas à poser le diagnostic.",
"P: Les déclencheurs se cherchent":" Ces antécédents orientent donc le bilan étiologique.",
"P: L'auscultation pulmonaire reste claire":" Ce signe est donc utile, car il oriente vers une cause cardiaque.",
"P: L'approche syndromique regroupe":" Cet ordre permet de ne pas manquer l'urgence, car la tamponnade menace la vie.",
"P: La tamponnade associe hypotension":" L'examen doit donc être répété, car l'état peut se dégrader vite.",
"P: Ce syndrome associe un tableau péricardique":" Ce syndrome est donc plus grave, car le myocarde est touché.",
"P: Le diagnostic positif de péricardite aiguë repose":" Cette règle est simple, car elle repose sur des signes objectifs.",
"P: Les marqueurs inflammatoires sont des critères":" Un taux normal ne doit donc pas faire écarter le diagnostic.",
"P: La forme incessante persiste":" Ainsi, la durée des symptômes dicte le choix du traitement.",
"P: Le diagnostic de péricardite aiguë est un diagnostic clinique":" L'imagerie sert donc à confirmer et à mesurer, mais non à remplacer la clinique.",
"P: Pour la myocardite, la biopsie":" Cette réserve s'explique car le geste est invasif.",
"P: Tous les patients suspects de péricardite aiguë réalisent":" Ainsi, un bilan simple suffit à orienter la plupart des patients.",
"P: Le deuxième niveau est réservé":" Cette sélection évite donc les examens inutiles.",
"P: La tomographie par émission":" Ces examens restent donc exceptionnels, car ils ne sont pas nécessaires dans la majorité des cas.",
"P: Le traitement vise trois buts":" Ces critères permettent donc de décider de la décroissance du traitement.",
"P: La tamponnade avec compromis hémodynamique exige":" Ainsi, le patient instable ne doit jamais attendre le bilan.",
"P: Le troisième palier associe":" Ainsi, l'escalade reste progressive, car chaque palier a ses risques.",
"P: En cas d'atteinte myocardique, le retour":" Cette prudence est donc justifiée, car le myocarde cicatrise lentement.",
"P: En cas d'insuffisance rénale, la dose":" Cette adaptation est donc indispensable, car la colchicine s'accumule.",
"P: Les corticoïdes peuvent être le premier choix":" Ces exceptions restent donc limitées, car le risque de rechute demeure.",
"P: Preuve. Le rilonacept":" Ces résultats expliquent donc la place croissante de ces médicaments.",
"P: Le pronostic est généralement favorable":" Ainsi, le suivi reste nécessaire, car la rechute est fréquente.",
"P: Il n'existe pas de mesure établie":" Cette absence de mesure explique donc l'importance du traitement des rechutes.",
"P: La colchicine est la mesure la plus efficace":" Ainsi, une prise régulière est donc essentielle.",
}
for f in glob.glob('t/p*.txt'):
    L=open(f,encoding='utf8').read().split('\n'); ch=False
    for i,l in enumerate(L):
        for k,v in A.items():
            if l.startswith(k) and v not in l: L[i]=l+v; ch=True
    if ch: open(f,'w',encoding='utf8').write('\n'.join(L))
