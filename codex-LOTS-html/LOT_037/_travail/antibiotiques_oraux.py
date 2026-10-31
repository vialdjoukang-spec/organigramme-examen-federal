from format_lecon import paras
from antibiotiques_parenteraux import citation, passage, D

def prefixe(n, debut):
    lignes=(D/f'evidence/AIPS_{n}.txt').read_text().splitlines()
    choix=[x for x in lignes if x.startswith(debut)]
    assert len(choix)==1,(n,debut,len(choix))
    return citation(n,choix[0])

def coamoxi_oral(l):
    d=paras('L’amoxicilline inhibe la synthèse de la paroi bactérienne ; le clavulanate inhibe certaines bêta-lactamases. Le traitement s’emploie pour une infection bactérienne sensible avec une indication clinique. Il n’est pas utile pour une simple réaction ganglionnaire virale et ne remplace pas le drainage d’une collection qui le nécessite.',
        'Les comprimés Co-Amoxi-Mepha et Co-Amoxi-Mepha Dispersible relèvent de l’autorisation 53995, notice de mars 2026. Le comprimé à 625 mg contient 500 mg d’amoxicilline et 125 mg de clavulanate. Le comprimé à 1000 mg contient 875/125 mg. La notice ne réserve pas une rubrique posologique propre à l’adénite : il faut distinguer recommandation clinique et doses générales de la spécialité.')
    d+=prefixe('53995','Pour les infections légères, modérées et sévères, la posologie usuelle')
    d+=prefixe('53995','Co-Amoxi-Mepha comprimés pelliculés et comprimés dispersibles ne convient')
    d+=paras('Chez l’adulte ou l’enfant de plus de 40 kg avec fonction rénale appropriée, la dose usuelle citée est un comprimé à 625 mg trois fois par jour. Ce n’est pas une prescription automatique devant toute masse cervicale. Les schémas à 1000 mg deux fois par jour décrits pour certaines autres infections ne sont pas étendus ici à toute adénite.',
        'Prendre au début du repas selon la notice. La barre du comprimé pelliculé à 1000 mg facilite la déglutition des deux morceaux successifs ; elle ne valide pas une demi-dose. Les comprimés dispersibles ne sont pas substitués à une suspension pédiatrique pour calculer une fraction de comprimé.')
    d+=passage('53995','Adultes et enfants de plus de 40 kg:', 'Patients âgés')
    d+=paras('Vérifier la fonction rénale avant de choisir la présentation. Entre 10 et 30 ml/min, le tableau donne 625 mg toutes les douze heures ; sous 10 ml/min, toutes les vingt-quatre heures. Les comprimés pelliculés à 1000 mg sont réservés à une clairance supérieure à 30 ml/min. La dialyse nécessite une adaptation spécialisée et les doses supplémentaires décrites dans la notice.')
    d+=prefixe('53995',"Co-Amoxi-Mepha est contre-indiqué en cas d'hypersensibilité connue")
    d+=prefixe('53995','Co-Amoxi-Mepha ne devrait donc être utilisé pendant la grossesse')
    d+=citation('53995','Il ne faudrait donc pas allaiter pendant le traitement par Co-Amoxi-Mepha.')
    d+=prefixe('53995',"En cas d'apparition d'une réaction allergique, il faut arrêter")
    d+=paras('La restriction d’allaitement est celle de cette spécialité. Le prescripteur apprécie grossesse, besoin du traitement et alternatives. Un antécédent d’ictère ou d’atteinte hépatique sous cette association constitue une contre-indication, et non une simple indication de surveillance.',
        'Arrêter et faire évaluer une réaction allergique, une éruption grave ou une diarrhée sévère, persistante ou sanglante. Une atteinte liée à Clostridioides difficile est possible ; ne pas la masquer par un ralentisseur du transit. Surveiller reins, foie et hémogramme selon durée et terrain. Revoir notamment méthotrexate, anticoagulants antivitamine K, probénécide, allopurinol et mycophénolate.',
        'Une durée de sept jours est proposée pour l’adénite de l’adulte dans la synthèse SPILF2026. Elle n’est pas une durée imposée par cette notice pour tout foyer. Le traitement est réévalué selon réponse, microbiologie et drainage. Le patient ne doit ni prolonger ni interrompre seul l’antibiothérapie.')
    return l.subwindow('coamoxi-oral','Amoxicilline–clavulanate orale : adulte et reins',d,(45,35))

def coamoxi_enfant(l):
    d=paras('Co-Amoxi-Mepha suspension relève de l’autorisation 53982, notice d’août 2026. Les concentrations 156,25 mg pour 5 ml et 312,5 mg pour 5 ml correspondent respectivement à 125/31,25 mg et 250/62,5 mg. Ces deux suspensions ont un rapport amoxicilline/clavulanate de 4:1 et un rythme de trois prises par jour.',
        'La suspension à 457 mg pour 5 ml contient 400/57 mg avec un autre rapport et un rythme de deux prises par jour. Sa notice limite ses indications à certaines infections nommées. Elle ne doit pas être choisie automatiquement pour une adénite parce qu’elle est plus concentrée ou requiert moins de prises.')
    d+=passage('53982','Co-Amoxi-Mepha suspension 156,25 et 312,5','Co-Amoxi-Mepha suspension 457')
    d+=paras('Le tableau est exprimé en dose totale quotidienne de l’association, répartie en trois prises. Les composantes amoxicilline et clavulanate y sont explicites. Il ne faut pas lire ces valeurs comme une dose par prise ni comme une dose d’amoxicilline seule. La concentration du flacon, le poids et le volume calculé doivent être vérifiés avant de remettre l’ordonnance.',
        'Pour les enfants de plus de deux ans, la notice indique notamment 50 à 75 mg/kg/jour de l’association pour une infection sévère. Cela correspond à 40 à 60 mg/kg/jour d’amoxicilline et 10 à 15 mg/kg/jour de clavulanate. Ce tableau général ne justifie pas le maintien ambulatoire d’un enfant avec signes de gravité.',
        'Les doses françaises plus élevées et leurs rapports de substances ne correspondent pas forcément aux schémas de cette notice. Toute dose ou indication dépassant la spécialité suisse est hors information professionnelle et doit être justifiée et vérifiée par le prescripteur pédiatrique. Aucun volume issu d’une suspension étrangère n’est transposé ici.')
    d+=prefixe('53982',"Pour le traitement des infections chez les nouveau-nés et les nourrissons jusqu'à 3 mois")
    lignes=(D/'evidence/AIPS_53982.txt').read_text().splitlines();a=lignes.index("Enfants jusqu'à 40 kg:");b=lignes.index("Mode d'administration",a)
    d+='<p>Adaptation rénale pédiatrique originale :</p>'+citation('53982','\n'.join(lignes[a:b]).strip()).replace('\n',' ')
    d+=paras('Le tableau rénal donne les deux composantes séparées, avec plafonds et intervalle. Il ne se remplace pas par le tableau adulte. La suspension à 457 mg est exclue sous 30 ml/min dans la notice. Une insuffisance rénale pédiatrique, la dialyse ou un jeune nourrisson nécessite une prescription spécialisée.')
    d+=prefixe('53982',"L'usage de Co-Amoxi-Mepha est contre-indiqué en cas d'hypersensibilité connue")
    d+=prefixe('53982','Co-Amoxi-Mepha ne devrait donc être utilisé pendant la grossesse')
    d+=citation('53982','Il ne faudrait donc pas allaiter pendant le traitement par Co-Amoxi-Mepha.')
    d+=citation('53982',"Ne pas utiliser pendant plus d'une semaine chez les jeunes enfants (moins de 3 ans) en raison de l'accumulation, sauf avis contraire de votre médecin ou de votre pharmacien.")
    d+=paras('Les contre-indications d’hypersensibilité et d’atteinte hépatique antérieure sous l’association restent applicables. Les suspensions contiennent de l’alcool benzylique et de l’aspartame, source de phénylalanine. La phénylcétonurie et les risques d’accumulation des excipients doivent être vérifiés. La restriction au-delà d’une semaine chez le moins de trois ans est confrontée à toute durée clinique plus longue avant prescription. En cas de vomissements persistants, altération générale ou signes d’allergie, interrompre l’administration et demander une évaluation urgente.',
        'La suspension se prépare et se conserve selon sa notice ; le volume se mesure avec un dispositif adapté, jamais avec une cuillère domestique. Une nouvelle concentration nécessite un nouveau calcul, pas la conservation du même nombre de millilitres.',
        'Pour l’adénite de l’enfant, SPILF2026 propose dix jours, tandis que le parcours BSAC décrit sept jours dans les situations qu’il couvre. Cette différence de recommandations ne s’arbitre pas en mélangeant les doses. La durée retenue est écrite par le prescripteur selon protocole local, évolution et contrôle du foyer, avec réévaluation clinique.')
    return l.subwindow('coamoxi-enfant','Suspensions pédiatriques : concentration, dose et limites',d,(44,35,41))
