from format_phase_b import aips, line, cite, paras, p, ref

def precautions(l,n,source,cle):
    a=aips(n)
    text=p('Contre-indications, citation de l’information professionnelle :')+cite(a['contre_indications'])
    text+=p('Grossesse et allaitement, citation de l’information professionnelle :')+cite(a['grossesse'])
    return l.window(cle,'contre-indications et situations particulières',text+ref(source),True)

def eylea(l,indication):
    a=aips('62393002');s=a['posologie']
    starts={
        'dmla':('Forme exsudative (humide) de la dégénérescence maculaire liée à l’âge (DMLAe)','Œdème maculaire secondaire à une occlusion de la veine centrale'),
        'rvo':('Œdème maculaire secondaire à une occlusion de la veine centrale','Œdème maculaire diabétique (OMD)'),
        'diabete':('Œdème maculaire diabétique (OMD)','NVC consécutive à une myopie pathologique'),
    }
    start,end=starts[indication]
    # Le texte AIPS emploie l’apostrophe droite dans « l'âge ».
    start=start.replace('l’âge',"l'âge")
    i=s.index(start);j=s.index(end,i+len(start));dose=s[i:j].strip()
    safety=precautions(l,'62393002',25,'anti-vegf-ci')
    arrest=a['precautions'].split('Suspension du traitement',1)[1].split('Déchirure de l’épithélium',1)[0].split("Déchirure de l'épithélium",1)[0].strip()
    details=paras('L’aflibercept est une protéine qui piège des facteurs proangiogéniques, dont le VEGF, pour réduire l’activité néovasculaire et la fuite vasculaire. La formulation présentée est Eylea® 2 mg/50 µl : Swissmedic 62393 pour la seringue préremplie, 62397 pour le flacon. Elle ne se confond pas avec la formulation à 8 mg.',
                 'Le traitement est réservé à un ophtalmologue expérimenté dans les injections intravitréennes. Vérifier la formulation et sa concentration avant chaque administration.')
    details+=cite(dose)+p('Avant chaque injection, vérifier les '+safety+'.')
    details+=paras('L’injection exige une asepsie adaptée, une anesthésie et un contrôle immédiat de la pression et de la perfusion papillaire. La seringue contient un excédent : son volume total ne doit pas être injecté. L’AIPS demande de ne pas injecter tant que la pression intraoculaire est ≥30 mmHg.',
                   'Informer sur les signes d’endophtalmie ou d’autre complication : douleur, rougeur, photophobie ou baisse visuelle imposent un contact immédiat. Un événement artériel récent, un glaucome insuffisamment contrôlé ou un risque de déchirure de l’épithélium pigmentaire modifie l’évaluation individuelle.',
                   'Aucune étude d’interactions n’a été réalisée selon l’AIPS ; cela ne prouve pas l’absence d’interaction. L’exposition systémique est faible, mais le risque systémique n’est pas nul. La décision d’une injection bilatérale ou d’une association à un autre anti-VEGF appartient au spécialiste.')
    details+=p('Suspension du traitement, citation AIPS :')+cite(arrest)
    details+=p('Populations particulières, citations AIPS :')+cite(line('62393002','posologie','Les données de sécurité et d’efficacité') if any(x.startswith('Les données de sécurité et d’efficacité') for x in s.splitlines()) else line('62393002','posologie',"Les données de sécurité et d'efficacité"))
    details+=cite(line('62393002','posologie',"Aucune étude spécifique n'a été menée"))
    details+=p('La dose de rétinopathie du prématuré est distincte et n’est pas extrapolée des schémas adultes présentés ici. Tracer le nom de la spécialité et le lot à chaque administration.'+ref(25))
    return l.window('aflibercept','aflibercept : schéma suisse pour cette indication',details,True)

def xalatan(l):
    a=aips('53675');s=a['posologie'];safety=precautions(l,'53675',24,'latanoprost-ci')
    detail=paras('Le latanoprost, analogue de prostaglandine, augmente l’évacuation de l’humeur aqueuse. Xalatan® collyre, Swissmedic 53675, est une option de traitement du glaucome à angle ouvert ou de l’hypertonie oculaire ; il ne remplace pas la prise en charge d’une fermeture aiguë de l’angle.')
    for start in ('Une goutte par jour',"En cas d'association",'Pour réduire une possible absorption systémique','En cas d’oubli'):
        candidates=[x for x in s.splitlines() if x.startswith(start) or x.startswith(start.replace('’',"'"))]
        if candidates: detail+=cite(candidates[0])
    detail+=p('Vérifier les '+safety+' avant prescription.')
    detail+=paras('Retirer les lentilles avant instillation et attendre au moins 15 minutes avant de les remettre. Ne pas contaminer l’embout. Observer le geste du patient, car l’efficacité dépend aussi de la technique et de l’observance.',
                  'Prévenir de la pigmentation irienne parfois définitive, des modifications des cils et de l’irritation locale. Rechercher un antécédent de kératite herpétique, un risque d’œdème maculaire et une chirurgie récente. Une baisse nouvelle ou une douleur impose un examen ; ne pas la considérer comme une simple intolérance.',
                  'L’association de deux analogues de prostaglandine est déconseillée : une élévation paradoxale de pression est rapportée. Les données ne permettent pas d’inventer un ajustement numérique rénal ou hépatique.')
    detail+=p('Enfants et adolescents, citation AIPS :')+cite(line('53675','posologie','Le collyre Xalatan peut'))
    detail+=p('Le glaucome congénital du petit enfant reste une prise en charge distincte, souvent chirurgicale. Contrôler pression, surface oculaire et progression selon l’objectif individuel.'+ref(24))
    return l.window('latanoprost','latanoprost : prescription et surveillance',detail,True)

def methylprednisolone(l,sep=False):
    a=aips('35112');safety=precautions(l,'35112',8,'methyl-ci')
    detail=paras('Solu-MEDROL® 500 mg ou 1 g, poudre et solvant, Swissmedic 35112. La méthylprednisolone réduit l’inflammation par ses effets glucocorticoïdes. La décision et la surveillance relèvent ici d’une équipe spécialisée.')
    if sep:
        detail+=p('Schéma AIPS des poussées aiguës de sclérose en plaques :')+cite(line('35112','posologie','Selon les données publiées'))
        detail+=p('Cette citation ne transforme pas toute névrite en poussée de SEP. L’étiologie, notamment AQP4 ou MOG, conditionne le protocole et les traitements de secours. Pour une névrite isolée, le schéma maladie-spécifique ne doit pas être présenté comme explicitement défini par cette rubrique.')
    else:
        detail+=p('Pour l’ACG avec perte visuelle aiguë sélectionnée, le protocole de bolus évoqué par EULAR relève d’une recommandation spécialisée. Il n’est pas une posologie spécifique de l’ACG dans l’extrait AIPS lu ; tout usage hors information professionnelle doit être documenté. L’incertitude du bénéfice visuel ne doit pas retarder le traitement glucocorticoïde nécessaire.'+ref(6))
    detail+=cite(next(x for x in a['posologie'].splitlines() if x.startswith("La durée d'administration") or x.startswith('La durée d’administration')))
    detail+=p('Consulter les '+safety+'.')
    detail+=paras('Surveiller pression artérielle, glycémie, électrolytes, infection et effets psychiatriques. Les risques augmentent avec dose et durée ; organiser le relais et éviter un arrêt non planifié après traitement prolongé.',
                  'Réviser les interactions : inducteurs ou inhibiteurs du CYP3A4, antidiabétiques, anticoagulants, anti-inflammatoires non stéroïdiens et autres immunosuppresseurs. L’hypokaliémie et les complications digestives ou infectieuses demandent une vigilance ciblée.',
                  'En insuffisance hépatique grave, une réduction peut être nécessaire ; l’AIPS indique la prudence rénale sans adaptation systématique. Le prématuré et le nouveau-né sont exclus pour ce produit ; ne pas extrapoler un bolus adulte à un enfant.'+ref(8))
    return l.window('methyl','méthylprednisolone : cadre suisse et précautions',detail,True)

def prednisone(l):
    safety=precautions(l,'29349',26,'pred-ci')
    detail=paras('Prednisone Streuli®, comprimés, Swissmedic 29349. L’artérite à cellules géantes figure dans les indications de cette information professionnelle. Le schéma maladie-spécifique se décide avec le spécialiste ; l’AIPS fournit une plage générale et des précautions.')
    detail+=cite(line('29349','posologie','La posologie initiale dépend'))
    detail+=p('EULAR 2025 propose une induction orale à 40–60 mg/jour en équivalent prednisone. Ce choix est une recommandation pour l’ACG, située dans la plage usuelle citée ; la plage AIPS de 5–60 mg ne justifie pas une faible dose pour une menace visuelle.'+ref(6,26))
    detail+=p('Les '+safety+' distinguent notamment l’urgence vitale des restrictions du traitement prolongé. Elles doivent être confrontées à la situation réelle, sans supprimer les réserves du texte.')
    detail+=cite(line('29349','posologie','Comme pour toute thérapie'))
    detail+=paras('La décroissance n’est pas un calendrier automatique : elle dépend de la rémission, des rechutes et du traitement associé. Une nouvelle atteinte visuelle pendant la décroissance impose une réévaluation urgente. Un syndrome de sevrage ou une insuffisance surrénale peuvent imiter une rechute systémique.',
                  'Organiser prévention osseuse, suivi tensionnel et glycémique, dépistage infectieux et révision des interactions. La liste des traitements doit rechercher notamment anticoagulants, anti-inflammatoires et inducteurs ou inhibiteurs enzymatiques. Une cirrhose ou une hypothyroïdie peut modifier l’exposition.',
                  'La pédiatrie de la spécialité ne constitue pas un protocole d’ACG de l’enfant. Une atteinte visuelle inflammatoire chez un enfant demande une autre démarche diagnostique.'+ref(6,26))
    return l.window('prednisone','prednisone : indication, plage AIPS et relais',detail,True)
