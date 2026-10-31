from html import escape
from pathlib import Path
from format_lecon import paras, table

D = Path(__file__).resolve().parents[1]

def citation(numero, extrait):
    original = (D / f'evidence/AIPS_{numero}.txt').read_text()
    assert extrait in original, (numero, extrait)
    return '<blockquote><p>« ' + escape(extrait) + ' »</p></blockquote>'

def passage(numero, debut, fin):
    lignes = (D / f'evidence/AIPS_{numero}.txt').read_text().splitlines()
    a = lignes.index(debut)
    b = lignes.index(fin, a + 1)
    return citation(numero, '\n'.join(lignes[a:b]).strip()).replace('\n', ' ')

def coamoxi(l):
    d = paras(
        'L’amoxicilline inhibe la synthèse de la paroi bactérienne. L’acide clavulanique inhibe certaines bêta-lactamases et protège l’amoxicilline contre leur action. L’association ne couvre pas toutes les résistances et ne remplace pas le contrôle chirurgical du foyer.',
        'La spécialité décrite est Co-Amoxi-Mepha i.v., autorisation 56758, notice de septembre 2026. Les flacons adultes contiennent 1000/200 mg ou 2000/200 mg ; les présentations pédiatriques habituelles contiennent 500/50 mg ou 1000/100 mg. Les rapports des deux substances diffèrent : une masse totale identique ne suffit pas à établir une équivalence.',
        'La notice vise notamment des infections ORL, des tissus mous et des septicémies à germes sensibles. Elle impose les recommandations et sensibilités locales. L’infection cervicale profonde n’est pas individualisée comme une rubrique posologique propre : le choix hospitalier s’appuie sur le siège, la gravité et le protocole infectiologique.'
    )
    d += passage('56758', 'Adultes et enfants de plus de 40 kg', 'Enfants de 3 mois à 12 ans env. (40 kg)')
    d += paras('Ces doses sont celles de la notice pour des infections modérées ou graves. Une infection profonde ne reçoit pas automatiquement le schéma modéré. La sélection du schéma grave et toute augmentation relèvent du prescripteur hospitalier après vérification des reins, des allergies et du foyer. La perfusion à 2200 mg dure au moins 30 minutes ; aucune administration ne doit être plus fréquente que toutes les quatre heures.')
    d += passage('56758', 'Enfants de 3 mois à 12 ans env. (40 kg)', 'Instructions posologiques particulières')
    d += paras('Les doses pédiatriques citées sont des doses par administration de l’association, avec leurs deux composantes. Elles ne sont pas des doses quotidiennes. Les flacons pédiatriques et l’intervalle propre au nouveau-né doivent être respectés. Une prescription néonatale ou une insuffisance rénale de l’enfant nécessite une vérification spécialisée, sans copier les doses adultes ou une suspension orale.')
    d += citation('56758', "En cas d'insuffisance rénale (clairance de la créatinine inférieure à 30 ml/min), ne pas utiliser la perfusion à 2200 mg (2000/200). La dose doit être réduite comme ci-dessous:")
    lignes = (D / 'evidence/AIPS_56758.txt').read_text().splitlines()
    a = lignes.index('Clairance de'); b = lignes.index("Insuffisance rénale chez l'enfant de plus de 4 semaines", a)
    d += '<p>Tableau rénal adulte original :</p>' + citation('56758', '\n'.join(lignes[a:b]).strip()).replace('\n', ' ')
    d += paras('La notice donne pour une clairance de 10 à 30 ml/min une dose initiale de 1,2 g puis 600 mg toutes les douze heures. Sous 10 ml/min, l’entretien est de 600 mg toutes les vingt-quatre heures. Ces masses sont celles de l’association. La préparation d’une fraction de flacon et l’adaptation à une infection grave doivent être validées par l’équipe. Ce tableau adulte ne se transpose pas à l’enfant.',
        'Chez l’enfant insuffisant rénal de plus de quatre semaines, la notice demande le rapport 5:1 du flacon adulte à 1200 mg pour assurer l’exposition au clavulanate. Ce cas déroge aux présentations pédiatriques habituelles et nécessite une prescription et une préparation spécialisées. Sous quatre semaines avec insuffisance rénale, la notice ne fournit pas de directives précises. Une dialyse nécessite aussi une adaptation et une dose supplémentaire selon la notice complète.')
    d += citation('56758', "L'usage de Co-Amoxi-Mepha i.v. est contre-indiqué en cas d'hypersensibilité connue aux pénicillines et céphalosporines ou à l'acide clavulanique, de même que chez les patients qui ont présenté un ictère ou des troubles de la fonction hépatique pendant un traitement antérieur par Co-Amoxi-Mepha i.v.")
    d += citation('56758', "Co-Amoxi-Mepha i.v. ne devrait donc être utilisé pendant la grossesse qu'en cas de nécessité absolue.")
    d += citation('56758', 'Il ne faudrait donc pas allaiter pendant le traitement par Co-Amoxi-Mepha i.v.')
    d += paras('La restriction d’allaitement ci-dessus est celle de cette notice précise. La grossesse nécessite une décision médicale ; l’observation en prophylaxie après rupture prématurée des membranes ne doit pas être transformée en interdiction de traiter une infection maternelle grave. L’avis obstétrical et le traitement urgent sont coordonnés.',
        'Arrêter l’administration et traiter immédiatement une réaction allergique grave ou une réaction cutanée sévère. Une diarrhée sévère, persistante ou sanglante impose de rechercher une infection à Clostridioides difficile ; un ralentisseur du transit est à éviter dans ce contexte. Surveiller aussi foie, reins, diurèse et hémogramme selon durée et terrain. Des vomissements persistants retardés avec malaise chez l’enfant peuvent correspondre à une entérocolite médicamenteuse et exigent une évaluation urgente.',
        'Rechercher en particulier méthotrexate, anticoagulants antivitamine K, probénécide, allopurinol et mycophénolate. Les interactions et la fonction hépatique peuvent modifier la surveillance ou le choix. Les modalités de reconstitution, compatibilité et conservation sont celles du flacon disponible ; ne pas improviser un mélange.',
        'Les schémas pondéraux français et les doses de cette spécialité suisse ne sont pas interchangeables sans vérifier le rapport amoxicilline/clavulanate, les plafonds, la fonction rénale et le protocole local. La durée totale n’est pas fixée par ce tableau de doses ; elle dépend du drainage, de l’évolution et des complications.'
    )
    return l.subwindow('coamoxi', 'Amoxicilline–clavulanate : doses parentérales suisses', d, (38,35,37))

def clindamycine(l):
    d = paras('La clindamycine inhibe la synthèse protéique bactérienne. Son spectre vise des bactéries Gram positif et des anaérobies sensibles. Une résistance, notamment inductible, peut compromettre son efficacité ; la seule mention d’allergie à une pénicilline ne garantit pas qu’elle convienne à une infection profonde.',
        'Clindamycin [Phosphat]-Mepha i.v./i.m., autorisation 62980, notice d’août 2025, contient 600 mg dans une ampoule de 4 ml. La solution contient de l’alcool benzylique. Les doses parentérales ne se déduisent pas du schéma oral d’une pharyngite simple.',
        'La clindamycine peut constituer une option adaptée à un germe sensible ou une composante d’un traitement spécialisé. Elle n’est pas présentée comme une monothérapie probabiliste universelle des cellulites extensives, de la médiastinite ou du choc. L’antibiogramme et l’avis infectiologique déterminent sa place.'
    )
    lignes = (D / 'evidence/AIPS_62980.txt').read_text().splitlines()
    a = lignes.index("Degré de l'infection"); b = next(i for i in range(a+1,len(lignes)) if lignes[i].startswith('Le dosage peut être augmenté'))
    d += '<p>Tableau parentéral original ; les doses sont quotidiennes et sont réparties en deux à quatre administrations :</p>' + citation('62980', '\n'.join(lignes[a:b]).strip()).replace('\n', ' ')
    d += citation('62980', "Clindamycin [Phosphat]-Mepha i.v./i.m. peut être utilisé chez les enfants à partir de l'âge de 1 mois. Chez les enfants, la clindamycine doit être dosée sur la base du poids corporel total, indépendamment de la présence d'une obésité. La dose maximale autorisée chez l'adulte ne doit toutefois pas être dépassée.")
    d += citation('62980', "En cas d'administration intraveineuse (i.v.), Clindamycin [Phosphat]-Mepha doit être utilisé sous forme diluée (voir «Mises en garde et précautions»). La concentration de clindamycine dans la solution pour perfusion ne doit pas dépasser 12 mg par ml et la vitesse de perfusion ne doit pas excéder 30 mg par min. Les vitesses de perfusion suivantes sont habituelles:")
    d += passage('62980', 'Dose', "L'administration de plus de 1200 mg en une perfusion unique d'une heure n'est pas recommandée.")
    d += citation('62980', "L'administration de plus de 1200 mg en une perfusion unique d'une heure n'est pas recommandée.")
    d += paras('La solution concentrée ne s’injecte jamais en bolus intraveineux. Le tableau donne notamment 600 mg dans 50 ml en vingt minutes et 900 mg dans 100 ml en trente minutes. Il décrit l’administration d’une dose choisie par le prescripteur, pas la fréquence ni la durée totale à appliquer à tout abcès. Une perfusion trop rapide peut provoquer hypotension ou arrêt cardiorespiratoire.')
    d += citation('62980', 'Hypersensibilité connue envers la clindamycine ou la lincomycine.')
    d += citation('62980', "Clindamycin [Phosphat]-Mepha i.v./i.m. solution injectable ne doit pas être administré aux nouveau-nés et aux prématurés, car cette préparation contient de l'alcool benzylique (voir «Mises en garde et précautions»).")
    d += citation('62980', "La clindamycine ne doit être administrée pendant la grossesse qu'en cas de nécessité absolue.")
    d += citation('62980', "L'administration orale ou parentérale de clindamycine n'est pas recommandée lors de l'allaitement. Si un traitement par la clindamycine est nécessaire, l'allaitement doit être arrêté.")
    d += citation('62980', "Lors de l'apparition d'une diarrhée persistante sous clindamycine, le traitement doit être arrêté et un traitement adapté doit être instauré.")
    d += paras('Une diarrhée sous traitement ou même après son arrêt peut signaler une infection à Clostridioides difficile, parfois grave. Faire évaluer sans délai une diarrhée persistante, sanglante ou accompagnée de douleurs importantes. Ne pas prendre de ralentisseur du transit si cette complication est suspectée. Les anciennes propositions de traitement de cette complication dans la notice ne sont pas reprises comme un protocole actuel.',
        'Arrêter et traiter une hypersensibilité grave ou une réaction cutanée sévère. En insuffisance rénale ou hépatique légère à modérée, la notice ne demande pas d’adaptation systématique. Dans les formes sévères sous hautes doses, elle demande une surveillance des concentrations ; les reins, le foie et l’hémogramme sont surveillés selon le terrain et la durée. Une atteinte rénale aiguë est possible.',
        'Revoir les inhibiteurs ou inducteurs enzymatiques, notamment la rifampicine, les anticoagulants antivitamine K et les curares. L’effet de blocage neuromusculaire peut être potentialisé, ce qui importe lors d’un geste sur les voies aériennes. La clindamycine ne constitue pas un traitement de la méningite.',
        'Un nourrisson de moins d’un mois ne doit pas recevoir cette spécialité injectable. Chez les autres jeunes enfants et pendant la grossesse, l’exposition totale à l’alcool benzylique doit être appréciée. L’allaitement suit la restriction de cette notice ; ne pas la généraliser silencieusement à toutes les situations ou spécialités.'
    )
    return l.subwindow('clindamycine', 'Clindamycine : place limitée, perfusion et sécurité', d, (39,35))
