import gzip
from html import escape
from format_lecon import R,paras
def ciproxin_hc(l):
 t=gzip.open(R/'ressources_ia/aips/fi_fr/54807.txt.gz','rt').read()
 qs=[
 "Traitement des inflammations bactériennes aiguës de l'oreille externe, dues à des micro-organismes sensibles à la ciprofloxacine.",
 "Il convient d'effectuer un test de sensibilité avant le début du traitement.",
 "Chez les enfants (dès deux ans), les adolescents et les adultes, instiller pendant sept jours, trois gouttes de suspension dans l'oreille atteinte, deux fois par jour. Bien agiter le flacon immédiatement avant l'emploi.",
 "Pour administrer les gouttes, le patient devra se coucher, l'oreille atteinte dirigée vers le haut. Cette position devra être maintenue pendant 30 à 60 secondes, afin de faciliter la pénétration des gouttes dans le conduit auditif externe. Si nécessaire, traiter ensuite également l'autre oreille.",
 "· Hypersensibilité à un principe actif, à un antibiotique du groupe des quinolones ou à l'un des excipients.\n· Patients présentant une perforation connue ou supposée du tympan.\n· Infections virales du conduit auditif externe\n· Infections fongiques\n· Ciproxin HC Suspension auriculaire en gouttes n'est pas indiqué pour le traitement d'une otite moyenne.",
 "C'est pourquoi Ciproxin HC Suspension auriculaire en gouttes ne doit pas être utilisé pendant la grossesse, ou uniquement en cas d'absolue nécessité.",
 "C'est pourquoi Ciproxin HC Suspension auriculaire en gouttes ne doit pas être utilisé pendant l'allaitement, ou uniquement en cas d'absolue nécessité.",
 "Aucune interaction cliniquement significative n'a été observée lors de l'administration locale de ciprofloxacine dans le conduit auditif externe. Toute association avec un autre médicament devrait malgré tout être évitée."]
 for q in qs:assert q in t,q
 detail=paras('Ciproxin HC est une suspension auriculaire associant ciprofloxacine et hydrocortisone. Les extraits suivants proviennent de l’information professionnelle suisse, mars 2024. Ils concernent cette préparation précise et un tympan non perforé.')+''.join('<blockquote><p>« '+escape(q)+' »</p></blockquote>' for q in qs)+paras('Ne pas extrapoler le schéma aux moins de deux ans, à une otite moyenne ou à un tympan possiblement perforé. Le test de sensibilité mentionné dans l’information professionnelle doit être pris en compte avant ce choix.', 'Arrêter et réévaluer en cas de réaction d’hypersensibilité ou de signes de tendinite. L’usage prolongé peut favoriser une surinfection ; le capuchon contient du latex et la suspension de l’alcool benzylique. La présence du corticoïde peut masquer une réaction allergique.', 'Une absence d’amélioration en 48 à 72 heures nécessite une réévaluation clinique sans attendre la fin de la durée prescrite. Une aggravation ou un signe de gravité impose un contrôle immédiat.')
 return l.subwindow('ciproxin','Ciproxin HC : indication, dose et limites suisses',detail,(7,13))
def amoxicilline(l):
 t=gzip.open(R/'ressources_ia/aips/fi_fr/44911.txt.gz','rt').read()
 qs=[
 'Otite moyenne, sinusite, amygdalite, pharyngite (due aux streptocoques).',
 "La posologie dépend du mode d'utilisation, de l'âge, du poids corporel et de la fonction rénale du patient, de même que du degré de gravité de l'infection et de la sensibilité du germe en cause.",
 "Adultes et enfants de plus de 40 kg\nInfections légères à moyennes\nConsignes générales: 1500 mg – 3000 mg d'amoxicilline/jour en 3 à 4 doses individuelles.",
 "Enfants jusqu'à 40 kg inclus\nIndications générales: 50 à 100 mg/kg/jour, répartis en 3 à 4 prises.\nDose journalière maximale: 2000 mg répartis en 3 à 4 prises.\nDose unitaire maximale: 50 mg/kg.",
 "Les nouveau-nés et les prématurés devraient en règle générale être traités par voie parentérale, en raison d'une absorption incertaine (transport actif). Traitement par voie orale au plus tôt à partir de 8 jours.",
 "Adultes et enfants de plus de 40 kg\nClairance de la créatinine (ClCr) (ml/min)\nDose orale au maximum\n10-30\n500 mg toutes les 12 heures au maximum\n<10\n500 mg toutes les 24 heures au maximum\nLors d'une clairance de la créatinine supérieure à 30 ml/min, aucun ajustement posologique n'est requis.",
 "Les enfants jusqu'à 40 kg inclus souffrant d'insuffisance rénale: doivent être traités par une forme d'amoxicilline parentérale.",
 "Hypersensibilité envers le principe actif ou l'un des excipients selon la composition: Amoxi-Mepha ne doit pas être administré aux patients présentant une hypersensibilité aux pénicillines ou aux céphalosporines.\nMononucléose infectieuse, leucémie lymphoïde: les patients souffrant de ces maladies et traités par l'amoxicilline sont particulièrement prédisposés à développer un exanthème (>90%).",
 "Les études expérimentales effectuées sur l'animal n'ont révélé aucune influence du produit sur la fertilité ni sur le développement embryonnaire et foetal. Toutefois, aucune étude contrôlée n'a été réalisée chez la femme enceinte. La prudence est donc de rigueur lors de l'emploi d'Amoxi-Mepha au cours de la grossesse.",
 "Amoxi-Mepha diffuse dans le lait maternel et pourrait, de ce fait, provoquer des effets secondaires chez le nouveau-né (p.ex. sensibilisation, diarrhées). La substance ne doit donc pas être administrée pendant la période d'allaitement ou, si nécessaire, il faut procéder au sevrage de l'enfant.",
 "Bien agiter la suspension avant chaque emploi."]
 for q in qs:assert q in t,q
 detail=paras('Amoxi-Mepha : extraits exacts de l’information professionnelle suisse de septembre 2026. Les repères ci-dessous sont généraux ; la prescription d’une otite doit être conciliée avec les recommandations cliniques, le poids, les reins et la spécialité effectivement délivrée.')+''.join('<blockquote><p>« '+escape(q)+' »</p></blockquote>' for q in qs)+paras('La directive suisse d’infectiologie utilise un schéma pédiatrique en deux prises, tandis que cette information professionnelle décrit trois à quatre prises. Ne pas présenter ces deux schémas comme identiques : la fréquence en deux prises est hors du schéma de cette information professionnelle et doit être explicitement validée par le prescripteur.', 'Chez l’enfant avec perforation, la directive suisse prévoit dix jours de traitement lorsqu’une antibiothérapie est retenue. Cette durée clinique ne remplace pas l’adaptation individuelle ni la réévaluation de l’évolution.', 'Les restrictions citées pendant l’allaitement sont celles de cette spécialité. Le choix thérapeutique doit être discuté avec le prescripteur et le pharmacien ; ne pas interrompre l’allaitement de sa propre initiative.', 'Vérifier concentration, dose en milligrammes et volume avant administration. Ne pas appliquer un schéma standard à un nouveau-né, un prématuré, une insuffisance rénale ou une infection grave.')
 return l.subwindow('amoxicilline','Amoxicilline : repères AIPS et limites d’application',detail,(2,18))
def canesten(l):
 t=gzip.open(R/'ressources_ia/aips/fi_fr/37510.txt.gz','rt').read()
 qs=[
 'Crème: clotrimazolum 10 mg/g.',
 'Pour traiter une mycose du conduit auditif, le tympan étant intact, badigeonner une mèche de gaze de Canesten Crème et la placer dans le conduit auditif en tamponnant légèrement.',
 'Enfants de moins de 2 ans\nChez les enfants de moins de 2 ans, Canesten Crème doit être utilisé uniquement sur prescription médicale.\nLa recommandation posologique correspond à celle préconisée pour les enfants plus âgés.',
 "Hypersensibilité au principe actif ou à l'un des excipients selon la composition.\nCanesten Crème/Spray ne doit pas être utilisé en cas d'hypersensibilité à d'autres antimycosiques de type imidazole.",
 "Ce médicament contient 10 mg d'alcool cétostéarylique pour 100 mg de crème équivalent à 100 mg/g. L'alcool cétostéarylique peut provoquer des réactions cutanées locales (p.ex. dermatite de contact).",
 "Le clotrimazole peut avoir un effet antagoniste contre l'amphotéricine et d'autres antibiotiques polyènes en application topique.",
 'Canesten doit être utilisé pendant la grossesse uniquement sous contrôle médical et seulement en cas d\'indication absolue.',
 "Le clotrimazole peut être utilisé pendant l'allaitement. Toutefois, pendant la période d'allaitement, Canesten Crème/Spray ne doit en aucun cas être appliqué directement sur le sein; si un traitement du sein est nécessaire, l'allaitement doit être (temporairement) arrêté."]
 for q in qs:assert q in t,q
 detail=paras('L’information suisse de Canesten Crème/Spray, août 2024, distingue les formulations. La méthode auriculaire qu’elle décrit concerne la crème et un tympan intact, avec une mèche posée et suivie par un professionnel.')+''.join('<blockquote><p>« '+escape(q)+' »</p></blockquote>' for q in qs)+paras('Le passage auriculaire ne donne pas de fréquence propre de remplacement de la mèche ni de durée spécifique. Elles doivent être prescrites et organisées par le professionnel ; ne pas transformer la fréquence d’application cutanée en règle de renouvellement auriculaire.', 'Le spray contient notamment de l’alcool isopropylique. Ne pas le substituer à la crème dans le conduit et ne pas extrapoler cette méthode à un tympan ouvert.', 'La crème contient aussi de l’alcool benzylique, susceptible d’irriter. En cas de réaction locale, arrêter et faire réévaluer plutôt que remplacer soi-même par le spray.')
 return l.subwindow('canesten','Canesten Crème : méthode auriculaire et précautions AIPS',detail,(27,))
