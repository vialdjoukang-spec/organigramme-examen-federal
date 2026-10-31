from format_lecon import paras, table
from antibiotiques_parenteraux import citation, passage, D

def enoxaparine(l):
    lignes=(D/'evidence/AIPS_49456.txt').read_text().splitlines()
    def ligne(debut):
        trouve=[x for x in lignes if x.startswith(debut)]
        assert len(trouve)==1,(debut,len(trouve))
        return citation('49456',trouve[0])
    d=paras(
        'L’énoxaparine potentialise l’antithrombine et inhibe principalement le facteur Xa. Elle limite la progression thrombotique ; elle ne dissout pas immédiatement le caillot et ne traite pas une compression tumorale pure. L’anticoagulation exige une indication et une évaluation hémorragique.',
        'Clexane/-multi, autorisation 49456, notice de février 2026, mentionne la thrombose veineuse profonde avec ou sans embolie pulmonaire. Le syndrome cave supérieur n’y possède pas de schéma individualisé. L’application à une thrombose centrale est décidée dans cette indication et selon le contexte spécialisé ; ce tableau ne justifie pas de traiter toute obstruction.',
        'Les seringues préremplies existent notamment à 20 mg/0,2 ml, 40 mg/0,4 ml, 60 mg/0,6 ml, 80 mg/0,8 ml et 100 mg/1 ml. Les présentations à 120 mg/0,8 ml et 150 mg/1 ml sont plus concentrées. Vérifier dose en mg, volume et concentration ; les héparines de bas poids moléculaire ne sont pas interchangeables.',
        'Les doses suivantes concernent un adulte pour lequel cette molécule a été retenue. La voie SC signifie sous-cutanée. Elles ne constituent ni une ordonnance pédiatrique ni un schéma de thrombolyse. Les situations hémorragiques, l’instabilité ou un geste urgent peuvent imposer une autre stratégie hospitalière.'
    )
    d+=ligne("L'énoxaparine s'administre par voie sous cutanée, en deux injections")
    d+=ligne('Chez les patients obèses ou souffrants d\'un cancer, il a été montré')
    d+=paras('La dose curative usuelle citée est de 1 mg/kg par injection sous-cutanée deux fois par jour. Le schéma de 1,5 mg/kg une fois par jour n’est prévu que pour les situations non compliquées ; la notice privilégie deux injections en cas de cancer ou d’obésité. Une dose de prophylaxie ne remplace pas la dose de traitement.',
        'La notice décrit une phase initiale moyenne d’environ dix jours et un relais antivitamine K. Elle ne fixe pas ainsi la durée totale d’une thrombose associée au cancer ou à un cathéter. Le choix du relais et la durée sont réévalués selon cause persistante, risque de récidive, saignement et procédure prévue.')
    d+=ligne("Une surveillance soigneuse est indiquée en cas d'insuffisance rénale faible")
    d+=table(['Clairance de la créatinine adulte','Dose de traitement citée','Action'],[
        ['30 à 80 ml/min','Pas de réduction systématique dans la notice.','Surveillance soigneuse de l’exposition clinique et du saignement.'],
        ['Inférieure à 30 ml/min','1 mg/kg sous-cutané une fois par jour.','Réduction spécifique de la dose thérapeutique ; faire valider le choix en insuffisance sévère et avant un geste.']
    ])
    a=lignes.index('Doses thérapeutiques');b=lignes.index('Pour le traitement de STEMI aigu chez les patients âgés de moins de 75 ans:',a)
    d+=citation('49456','\n'.join(lignes[a:b])).replace('\n',' ')
    d+=paras('Le tableau rénal porte sur la clairance de la créatinine et sur la dose thérapeutique. Il ne faut pas utiliser la réduction d’une dose prophylactique ni les bolus d’infarctus pour cette indication. Dialyse, extrêmes de poids et altération rénale instable nécessitent un choix expert.')
    d+=passage('49456','Contre-indications','Mises en garde et précautions')
    d+=paras('Ces contre-indications sont celles de Clexane. Rechercher particulièrement une hémorragie active et un antécédent de thrombopénie immunitaire liée à l’héparine. Une suspicion de cette complication impose l’arrêt de l’héparine et un anticoagulant non héparinique choisi par l’équipe. Une insuffisance rénale ou un geste invasif modifie le risque même sans contre-indication absolue.')
    d+=citation('49456',"L'énoxaparine ne doit pas être administrée par voie intramusculaire.")
    d+=citation('49456',"L'efficacité et la sécurité de l'énoxaparine chez l'enfant n'ont pas été étudiées de façon suffisante.")
    d+=citation('49456',"l'énoxaparine ne doit être utilisée pendant la grossesse que si le médecin a établi un réel besoin clinique.")
    d+=citation('49456',"Cependant, par mesure de précaution et étant donné que de nombreux médicaments sont excrétés dans le lait maternel, l'allaitement n'est pas recommandé.")
    d+=paras('La restriction d’allaitement est celle de cette notice précise ; elle ne doit pas être remplacée par une affirmation générale de compatibilité de toutes les héparines. Pendant grossesse et autour de l’accouchement, coordonner avec obstétrique et anesthésie. Une valve mécanique constitue un terrain particulier à haut risque qui ne suit pas un schéma simplifié.',
        'L’enfant nécessite un protocole pédiatrique spécialisé et une vérification de la formulation. Le flacon multi contient de l’alcool benzylique et ne doit pas être utilisé chez le nouveau-né. Ne pas extrapoler le tableau adulte au poids de l’enfant.',
        'Les effets majeurs à surveiller sont saignement, anémie, thrombopénie et lésions cutanées graves. Contrôler hémogramme, plaquettes et fonction rénale avant puis pendant le traitement selon le terrain. Les tests globaux de coagulation ne permettent pas de mesurer de manière fiable l’effet de l’énoxaparine. Un dosage anti-Xa éventuel est discuté dans les situations particulières, sans cible universelle ici.')
    d+=ligne('Il est donc recommandé de réaliser une numération plaquettaire')
    d+=ligne('En pratique, si une diminution significative confirmée de la numération plaquettaire')
    d+=paras('Revoir les autres anticoagulants, antiagrégants, anti-inflammatoires non stéroïdiens et corticoïdes systémiques qui augmentent le risque hémorragique. Une association n’est maintenue que pour une indication vérifiée et sous surveillance. Coordonner biopsie, intervention et anesthésie neuraxiale ; les délais dépendent de la dose et des reins et ne doivent pas être improvisés par le patient.',
        'La seringue préremplie ne se purge pas avant injection ; ne pas masser le site ensuite. Une injection ne doit pas obliger un patient intolérant au décubitus à s’allonger sans évaluation de sécurité. L’équipe adapte les conditions du soin à la compression thoracique et vérifie la technique complète de la présentation utilisée.')
    d=d.replace('</blockquote><','</blockquote>\n<')
    return l.subwindow('enoxaparine','Énoxaparine : exemple conditionnel de traitement d’une thrombose',d,(61,58,60))
