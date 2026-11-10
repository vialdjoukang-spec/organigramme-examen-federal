from rendu import Point
p=Point(3)
p.h('Relier le mécanisme aux observations')
p.p('Les myalgies réunissent plusieurs mécanismes : surcharge régionale, atteinte ultrastructurale liée à l’effort, trouble hormonal, inflammation ou destruction musculaire.', ['p83-myofascial-fibro','doms-mecanisme','p83-hypothyroidie','p83-myopathies-inflammatoires','pa83-rhabdo-mecanisme'])
p.p('Le contexte et les signes associés choisissent donc les explorations utiles ; les mêmes sensations douloureuses peuvent accompagner des atteintes différentes.', ['pa83-anamnese','p83-phenotype','pa83-biologie'])
p.p('Dans le syndrome myofascial primaire, une surcharge musculaire est impliquée, probablement par des microtraumatismes ; l’examen recherche une bande tendue et un point gâchette.', 'p83-myofascial-fibro')
p.p('La pression sur ce point peut produire une douleur locale, une contraction visible et une douleur propagée, ce qui donne au geste sa valeur clinique.', 'p83-myofascial-fibro')
p.p('Après une charge inhabituelle ou excentrique, les courbatures correspondent à une atteinte ultrastructurale suivie de réactions locales et de limitations fonctionnelles retardées.', 'doms-mecanisme')
p.p('Le gonflement, la réduction de force et la raideur s’inscrivent dans cette évolution ; la charge est alors ajustée plutôt que maintenue à son niveau déclenchant.', ['doms-mecanisme','doms-prevention'])
p.tableau(['Perturbation et traduction clinique','Exploration liée au mécanisme','Conséquence pour les soins'],[
 [('Une surcharge régionale peut faire apparaître un point gâchette douloureux dans une bande musculaire tendue.', 'p83-myofascial-fibro'),('La palpation recherche la reproduction locale et propagée de la douleur.', 'p83-myofascial-fibro'),('Le diagnostic clinique oriente une prise en charge multimodale.', 'p83-myofascial-fibro')],
 [('Les courbatures suivent une charge inhabituelle avec perturbations ultrastructurales.', 'doms-mecanisme'),('La chronologie et l’examen fonctionnel identifient le tableau ; l’imagerie se réserve aux cas peu clairs.', ['doms-mecanisme','doms-biologie-imagerie']),('Une réduction transitoire de charge précède une progression adaptée.', ['rms-doms','doms-prevention'])],
 [('Un choc direct s’associe à une douleur immédiate et à un hématome dont l’importance influence les symptômes.', 'p83-doms-contusion-clinique'),('L’examen compare les côtés, les amplitudes et la douleur à l’étirement ou à la contraction.', 'rms-clinique'),('Les signes de pression compartimentale imposent une évaluation urgente ; un syndrome des loges confirmé exige une décompression immédiate.', ['p83-boast-loges-0','p83-boast-loges-3'])],
 [('La destruction musculaire libère le contenu cellulaire et peut affecter la fonction rénale et les électrolytes.', 'pa83-rhabdo-mecanisme'),('Les CK et l’évaluation des complications replacent l’atteinte dans sa cinétique et sa gravité.', ['e12','e13']),('Le risque rénal et les comorbidités guident une prise en charge individualisée.', 'e13')],
 [('Les hormones thyroïdiennes participent au métabolisme et à la fonction mitochondriale musculaires.', 'p83-hypothyroidie'),('La clinique musculaire est reliée au bilan thyroïdien et aux CK, qui peuvent rester normales.', 'p83-hypothyroidie'),('L’identification du trouble hormonal oriente le traitement étiologique.', 'p83-hypothyroidie')],
 [('La dermatomyosite associe notamment une vasculopathie périmysiale et une atrophie périfasciculaire.', 'p83-dermato-histologie'),('La faiblesse et les signes cutanés orientent le bilan spécialisé ; les atteintes d’organes doivent être recherchées.', ['p83-phenotype','p83-myopathies-gravite']),('Le pronostic respiratoire, cardiaque et bulbaire participe à la priorité des soins.', 'p83-myopathies-gravite')]
])
p.fenetre('De l’énergie cellulaire à la rhabdomyolyse',[
 ('Une déplétion en ATP peut limiter la fonction de la pompe sodium-potassium et altérer le gradient nécessaire à la sortie du calcium du sarcoplasme.', 'pa83-rhabdo-mecanisme'),
 ('L’accumulation intracellulaire de calcium active des enzymes cytolytiques ; la cellule musculaire se détruit et libère son contenu dans la circulation.', 'pa83-rhabdo-mecanisme'),
 ('La myoglobine peut contribuer à une obstruction tubulaire et à des lésions oxydatives rénales, tandis que la séquestration liquidienne favorise une hypovolémie.', 'pa83-rhabdo-mecanisme'),
 ('La libération d’électrolytes intracellulaires explique notamment l’hyperkaliémie et l’hyperphosphatémie.', 'pa83-rhabdo-mecanisme'),
 ('Ces mécanismes donnent leur sens à la recherche d’anurie, de perturbations métaboliques et de signes généraux anormaux.', ['pa83-rhabdo-mecanisme','e13']),
 ('Une augmentation des CK isolée après exercice s’interprète avec les symptômes et le risque de complications ; elle ne commande pas à elle seule une réanimation hydrique agressive.', 'e13')
])
p.h('La pression compartimentale change l’urgence')
p.p('Un œdème musculaire dans un espace limité par les fascias peut augmenter la pression locale et conduire à un syndrome compartimental.', 'pa83-rhabdo-mecanisme')
p.p('Le syndrome des loges aigu provoque une ischémie tissulaire ; une douleur disproportionnée et une douleur lors de la mobilisation passive des muscles concernés doivent l’évoquer.', 'p83-boast-loges-0')
p.p('Une fois le diagnostic posé, la décompression chirurgicale doit être immédiate ; la prise en charge ne se réduit pas à traiter la douleur.', 'p83-boast-loges-3')
p.fenetre('Sous statine : toxicité et immunité correspondent à deux voies',[
 ('Les manifestations musculaires associées aux statines vont de plaintes sans faiblesse à des atteintes toxiques ou immunomédiées.', 'p83-statine-frequence'),
 ('Une faiblesse proximale ou axiale progressive, une dysphagie et des CK très élevées font rechercher une myopathie nécrosante immunomédiée.', 'p83-statine-imnm'),
 ('Les anticorps anti-HMGCR soutiennent ce diagnostic ; la biopsie décrit une nécrose et une régénération avec peu d’infiltrats lymphocytaires.', 'p83-statine-imnm'),
 ('Dans cette forme, le seul arrêt de la statine ne fait pas régresser les symptômes ; une immunosuppression est nécessaire chez la plupart des patients.', 'p83-statine-imnm'),
 ('Pour Sortis, la notice suisse demande un dosage des CPK devant douleurs, faiblesse ou crampes et l’arrêt lorsque leur taux dépasse cinq fois la limite supérieure de la normale.', 'aips-sortis-surveillance'),
 ('Des symptômes importants et durablement gênants peuvent aussi conduire à envisager l’arrêt malgré un taux inférieur à ce seuil.', 'aips-sortis-surveillance')
])
p.h('Douleur chronique diffuse : une autre organisation clinique')
p.p('Des signes de sensibilisation centrale et des anomalies de nocicepteurs périphériques sont décrits dans des sous-groupes de fibromyalgie ; ces observations ne constituent pas des marqueurs diagnostiques utilisables.', 'p83-myofascial-fibro')
p.p('Le tableau associe douleur étendue, sommeil peu réparateur et fatigabilité ; la prise en charge articule éducation, soins et autogestion.', ['p83-myofascial-fibro','pa83-fibro-soins'])
p.p('L’activité physique adaptée et la gestion des réserves d’énergie s’intègrent dans cette stratégie individuelle, avec une charge qui respecte les capacités de la personne.', 'pa83-fibro-activite')
p.p('La présence d’une faiblesse, d’une atrophie ou d’anomalies biologiques conduit à examiner une autre explication, même si un syndrome douloureux chronique est déjà reconnu.', 'p83-myofascial-fibro')
p.sauver()
