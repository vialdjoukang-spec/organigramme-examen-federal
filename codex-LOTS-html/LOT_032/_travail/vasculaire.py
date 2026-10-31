from format_lecon import paras
from medicaments import q,line,segment
def nimodipine(l):
 t=paras('Nimotop comprimés pelliculés, nimodipine, information professionnelle suisse n°45839. La voie orale de cette notice est un relais après perfusion dans l’hémorragie sous-arachnoïdienne anévrismale. Cette portée précise diffère de la recommandation NICE qui propose de considérer d’emblée la voie entérale ; une stratégie différente du libellé suisse relève d’une décision spécialisée explicitement documentée.')
 t+=q('45839',segment('45839','Application orale consécutive','Recommandations spéciales'))
 t+=paras('Ces citations conservent le schéma exact de la notice : elles ne décrivent pas un traitement oral universel de vingt et un jours. La perfusion est une autre formulation et sa prescription exige sa propre vérification. Ne jamais injecter une préparation orale.', 'La nimodipine réduit le risque de déficit ischémique secondaire ; elle ne ferme pas l’anévrisme et ne remplace pas sa sécurisation. L’adaptation tensionnelle relève de l’équipe neurovasculaire.')
 t+=q('45839',segment('45839','La présence d’une insuffisance rénale','Mises en garde et précautions'))
 t+=q('45839',line('45839','La prudence est recommandée chez les patients présentant une hypotension'))
 t+=q('45839',segment('45839','Des études menées sur l’animal ont montré','Effet sur l’aptitude'))
 t+=paras('Surveiller pression artérielle, fréquence cardiaque, fonction hépatique et rénale selon le terrain. Une hypotension peut compromettre la perfusion cérébrale. Vérifier les inhibiteurs ou inducteurs enzymatiques, les autres antihypertenseurs et les médicaments néphrotoxiques.', 'Rifampicine, phénytoïne, carbamazépine et phénobarbital sont contre-indiqués en association selon les lignes citées. Éviter le pamplemousse. Les interactions peuvent persister après la dernière consommation. L’efficacité et la sécurité avant dix-huit ans ne sont pas établies ; aucune extrapolation pédiatrique n’est proposée.')
 return l.subwindow('nimodipine','Nimodipine orale : schéma suisse et différence de recommandation',t,(20,21))
