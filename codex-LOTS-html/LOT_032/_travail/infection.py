from medicaments import q,line,segment
from format_lecon import paras
def traitements(l):
 t=paras('Rocephin, ceftriaxone, information professionnelle suisse n° 44625. Traitement hospitalier intraveineux dans un schéma méningé adapté à l’âge, au terrain et aux résistances. La dose usuelle basse d’autres infections n’est pas automatiquement une dose de méningite. La notice décrit chez l’adulte une augmentation pour infection sévère :')
 t+=q('44625',line('44625','En général, 1 - 2 g'))
 t+=paras('Chez l’enfant en bas âge et l’enfant, rubrique spécifique méningite :')+q('44625',line('44625','En cas de méningite bactérienne'))
 t+=paras('Les durées historiques associées à cette rubrique ne sont pas appliquées automatiquement : durée et désescalade suivent le germe, la sensibilité et l’évolution avec l’infectiologue.')
 for prefix in ['Rocephin est contre-indiqué chez les patients présentant une hypersensibilité','Rocephin est contre-indiqué chez les prématurés','Les nouveau-nés présentant une hyperbilirubinémie','Rocephin est contre-indiqué chez les nouveau-nés (≤28 jours) pour lesquels','Les solutions de ceftriaxone contenant de la lidocaïne']:
  t+=q('44625',line('44625',prefix))
 t+=q('44625',line('44625',"Aucun ajustement posologique n'est nécessaire à condition que la fonction hépatique"))
 t+=q('44625',line('44625',"La ceftriaxone n'est pas éliminée par dialyse"))
 for prefix in ['La ceftriaxone passe la barrière placentaire','Étant donné que la ceftriaxone']:
  t+=q('44625',line('44625',prefix))
 t+=paras('Vérifier les incompatibilités avec les solutions calciques ; ne pas mélanger ni administrer simultanément par la même ligne. Les restrictions néonatales sont plus fortes et interdisent de transposer le schéma de l’enfant au nouveau-né. La voie intraveineuse n’utilise jamais un solvant de lidocaïne.', 'Surveiller allergie, cytopénies, diarrhée sévère, complications biliaires et signes d’encéphalopathie. Une insuffisance rénale terminale ou associée à une atteinte hépatique exige une décision spécialisée permettant de maintenir une exposition adaptée à l’infection.')
 a=l.subwindow('ceftriaxone','Ceftriaxone : doses et restrictions suisses',t,(8,16,17))
 t=paras('Amoxicillin OrPha parentéral, information professionnelle n° 68815. Une couverture de Listeria est ajoutée selon âge et terrain, notamment grossesse ou immunodépression. La ceftriaxone seule ne couvre pas cette bactérie. L’extrait adulte ci-dessous est le schéma suisse des infections sévères, à sélectionner par l’équipe pour l’indication méningée.')
 t+=q('68815','2 g en perfusion brève (30 min) 3 à 6 fois par jour.')
 t+=paras('Ce schéma concerne adultes et enfants de plus de quarante kilogrammes avec fonction rénale appropriée. Pour les enfants de plus de trois mois, la notice précise :')
 t+=q('68815',line('68815',"En cas d'infection sévère chez l'enfant de plus de 3 mois"))
 t+=paras('Le nouveau-né et le nourrisson plus jeune suivent des doses et intervalles distincts, non transposés ici. L’adaptation rénale doit être individualisée avec l’équipe : la notice impose une réduction selon clairance et des dispositions propres à la dialyse ; ne pas maintenir le schéma de fonction normale sans vérification.')
 t+=q('68815',segment('68815','· Hypersensibilité envers','Mises en garde et précautions'))
 for prefix in ['Les études expérimentales effectuées','Amoxicillin OrPha diffuse dans le lait maternel']:
  t+=q('68815',line('68815',prefix))
 t+=paras('Vérifier allergie aux bêta-lactamines, charge sodée, hydratation, diurèse et interactions. De fortes doses, surtout en insuffisance rénale, peuvent provoquer des convulsions ; une diarrhée sévère impose une réévaluation. La durée de la listériose n’est pas celle d’une méningite à méningocoque.')
 b=l.subwindow('amoxicilline','Amoxicilline parentérale : couverture de Listeria',t,(8,16,18))
 t=paras('Dexaméthasone Galepharm Amp, information professionnelle n° 66710. La corticothérapie adjuvante est discutée dès le début, avant ou avec la première dose antibiotique si possible, sans jamais retarder l’antibiotique. La rubrique pédiatrique de la notice, sous œdème cérébral/encéphalite-méningite, comporte cet extrait exact :')
 t+=q('66710',line('66710','· encéphalite/méningite:'))
 t+=paras('Cette citation conserve sa portée pédiatrique et sa rubrique : elle n’est pas extrapolée à un schéma adulte. Le schéma adulte adjuvant des recommandations n’a pas été retrouvé tel quel dans les notices suisses consultées ; il relève d’un protocole hospitalier et n’est pas présenté ici comme une dose AIPS vérifiée. Ce décalage de posologie et d’indication doit être explicité lors de la prescription.', 'NICE propose la dexaméthasone pour les méningites bactériennes fortement suspectées ou confirmées au-delà de trois mois ; chez les plus jeunes, avis spécialisé. La poursuite dépend du germe et du contexte, sans attendre la disponibilité du corticoïde pour donner l’antibiotique.')
 for prefix in ['Dans des situations dans lesquelles','Ne pas utiliser ce médicam',"C'est pourquoi Dexaméthasone Galepharm",'La dexaméthasone, comme tous les autres glucocorticoïdes, se retrouve']:
  t+=q('66710',line('66710',prefix))
 t+=paras('Surveiller notamment glycémie, électrolytes, pression artérielle, complications digestives et infectieuses. Le corticoïde ne remplace ni antibiothérapie ni prise en charge du sepsis. Une dose destinée à un autre œdème cérébral ne devient pas une dose de méningite communautaire.')
 c=l.subwindow('dexamethasone','Dexaméthasone : place et limite de la vérification suisse',t,(8,16,19))
 return paras(a,b,c)
