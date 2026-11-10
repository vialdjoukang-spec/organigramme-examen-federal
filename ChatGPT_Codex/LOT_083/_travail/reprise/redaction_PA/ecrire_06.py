from rendu import Point
p=Point(6)
p.h('Observer puis comparer les deux côtés')
p.p('L’examen d’une douleur musculaire localisée est bilatéral et comparatif : inspection, palpation, amplitudes, douleur à l’étirement ou à la contraction et examen neurologique local.', 'rms-clinique')
p.p('À l’inspection, rechercher une encoche, une voussure, un hématome ou une ecchymose ; leur répartition doit être confrontée au mécanisme décrit.', 'rms-clinique')
p.p('À la palpation, relever une contracture, une perte du ballant musculaire ou une douleur provoquée ; la localisation précise évite de réduire l’examen au seul mot « myalgie ».', 'rms-clinique')
p.p('Mesurer les amplitudes et rechercher les raideurs musculo-tendineuses, puis comparer les réponses à l’étirement et à la contraction.', 'rms-clinique')
p.p('Le testing passif et actif et l’examen neurologique local complètent la description ; une douleur régionale peut aussi relever d’une atteinte tendineuse ou d’un autre diagnostic concurrent.', 'rms-clinique')
p.h('La force : un résultat distinct de la douleur')
p.p('La force normale correspond à la possibilité de s’opposer à une résistance extérieure importante ; la cotation documente ensuite les degrés de déficit.', 's103')
p.p('Une diminution de force peut accompagner une synovite, une arthropathie, un problème musculo-tendineux, une radiculopathie ou une neuropathie ; le déficit mesuré ne désigne donc pas à lui seul une myopathie.', 's103')
p.tableau(['Cotation','Observation pendant le geste','Lecture du résultat'],[
 [('5', 's103'),('Le patient s’oppose à une résistance extérieure importante.', 's103'),('La force est normale selon la cotation HUG/USZ.', 's103')],
 [('4', 's103'),('Le mouvement reste possible contre la pesanteur et une résistance extérieure.', 's103'),('La résistance est possible sans atteindre la force normale décrite au grade supérieur.', 's103')],
 [('3', 's103'),('Le mouvement est possible contre la pesanteur.', 's103'),('Le geste est documenté par la capacité à vaincre la pesanteur.', 's103')],
 [('2', 's103'),('Le mouvement est possible seulement en absence de pesanteur.', 's103'),('L’examen doit distinguer ce résultat d’un mouvement réalisé contre la pesanteur.', 's103')],
 [('1', 's103'),('Une contraction est visible ou palpable sans mouvement articulaire.', 's103'),('La contraction existe mais ne produit pas de mouvement.', 's103')],
 [('0', 's103'),('Aucune contraction n’est visible.', 's103'),('Le résultat décrit une absence de contraction observable dans ce testing.', 's103')]
])
p.p('Cette cotation provient du document HUG/USZ de septembre 2000 ; une évaluation fonctionnelle, notamment de la préhension, peut être plus appropriée pour les petites articulations des mains.', 's103')
p.fenetre('Palper un point gâchette',[
 ('Le syndrome myofascial se recherche dans une bande musculaire tendue : la pression identifie une sensibilité douloureuse locale maximale.', 'p83-myofascial-fibro'),
 ('La palpation peut provoquer une contraction musculaire visible et une douleur propagée à distance du point pressé.', 'p83-myofascial-fibro'),
 ('La DGN décrit un diagnostic clinique ; un examen manuel entraîné ou un algomètre étalonné peut servir à apprécier la douleur à la pression.', ['p83-myofascial-fibro','p83-phenotype']),
 ('Une douleur diffuse avec fatigue et sommeil peu réparateur correspond à une autre constellation clinique ; les anomalies de nocicepteurs observées dans certains sous-groupes ne remplacent pas cette évaluation.', 'p83-myofascial-fibro')
])
p.h('Membres : le geste douloureux qui change l’orientation')
p.p('Après une atteinte traumatique, rechercher une douleur hors de proportion avec la lésion attendue et une douleur lors de la mobilisation passive des muscles du compartiment concerné.', 'p83-boast-loges-0')
p.p('Ces signes font évoquer un syndrome compartimental aigu ; une fois le diagnostic établi, la conduite est une décompression immédiate.', ['p83-boast-loges-0','p83-boast-loges-3'])
p.p('Un hématome ou une ecchymose n’épuise pas l’examen : la fonction, l’étirement, la contraction et l’examen neurologique local restent nécessaires.', 'rms-clinique')
p.h('Peau, mouvement et ceintures')
p.p('L’examen recherche les signes cutanés qui accompagnent certaines myopathies, notamment l’érythème héliotrope et les signes de Gottron décrits dans la dermatomyosite aiguë.', 'p83-phenotype')
p.p('Une faiblesse rapportée doit être vérifiée ; l’examen recherche aussi spasticité, rigidité et dystonie, qui peuvent accompagner des douleurs musculaires par un autre mécanisme.', 'p83-phenotype')
p.p('Devant une douleur des ceintures compatible avec une pseudopolyarthrite rhizomélique, rechercher les manifestations d’artérite : céphalée, sensibilité du cuir chevelu, anomalie temporale, claudication de la mâchoire ou trouble visuel.', 'p83-eular26-signes-urgence')
p.p('Les manifestations crâniennes orientent vers une évaluation immédiate ; la recherche de confirmation ne doit pas différer les glucocorticoïdes lorsque la suspicion d’artérite est forte.', ['p83-eular26-orientation','p83-eular26-urgence'])
p.h('État général et organes : ne pas limiter l’examen au muscle')
p.p('La suspicion de rhabdomyolyse impose de rechercher les signes vitaux anormaux, les manifestations rénales et les complications compartimentales ou métaboliques.', 'e13')
p.p('Chez l’adulte avec suspicion de grippe, la SSI 2026 propose de considérer l’hospitalisation notamment si la pression systolique est inférieure à 90 mmHg, la fréquence respiratoire atteint 30 par minute ou plus, ou la SpO₂ est inférieure à 92 %.', 'flu-ssi-alarmes')
p.p('Ces seuils appartiennent à la recommandation adulte : ils ne doivent pas être appliqués automatiquement à l’enfant.', 'flu-ssi-alarmes')
p.p('Dans les myopathies inflammatoires, une dysphagie, une insuffisance cardiaque, un trouble du rythme, une pneumopathie interstitielle ou une dysfonction diaphragmatique peuvent déterminer le pronostic.', 'p83-myopathies-gravite')
p.fenetre('Ce que l’examen normal ne peut pas prouver seul',[
 ('L’absence d’un marqueur diagnostique spécifique de fibromyalgie impose une évaluation clinique et différentielle ; un examen ne se résume pas à chercher des anomalies biologiques.', 'p83-myofascial-fibro'),
 ('Des CK normales peuvent être observées dans certaines myosites ; la biologie ne remplace donc pas la vérification de la force et des manifestations associées.', ['pa83-biologie','p83-phenotype']),
 ('Une cause thyroïdienne peut également s’accompagner de CK normales ; l’examen et le contexte hormonal guident la suite du bilan.', 'p83-hypothyroidie')
])
p.sauver()
