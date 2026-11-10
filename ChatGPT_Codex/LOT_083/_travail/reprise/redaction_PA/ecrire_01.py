from rendu import Point
p=Point(1)
p.h('Une plainte musculaire à caractériser')
p.p('La Deutsche Gesellschaft für Neurologie définit les myalgies comme des sensations douloureuses dans la musculature ; elles peuvent être localisées ou diffuses.', 'p83-definition')
p.p('Cette définition figure dans sa recommandation de 2025, élaborée avec la participation de la Société suisse de neurologie.', ['pa83-date-dgn','pa83-dgn-organismes'])
p.p('Le mot décrit donc une plainte, tandis que la recherche clinique précise son contexte et ses manifestations associées.', ['p83-definition','pa83-anamnese','p83-phenotype'])
p.p('Une douleur musculaire peut accompagner un trouble régional, un syndrome diffus, une exposition médicamenteuse ou une maladie musculaire identifiée.', ['p83-myofascial-fibro','p83-statine-frequence','p83-myopathies-inflammatoires'])
p.p('La localisation ne démontre pas à elle seule une destruction des fibres ; la faiblesse, les signes cutanés et les résultats ciblés orientent la suite.', ['p83-myofascial-fibro','p83-phenotype','pa83-biologie'])
p.fenetre('Localisé ou généralisé : deux cadres de départ',[
 ('L’interrogatoire fait préciser les régions douloureuses, leur répartition, leur irradiation et la sensation superficielle ou profonde.', 'pa83-anamnese'),
 ('Un schéma corporel aide à distinguer une plainte focale d’une atteinte généralisée ; il rend la description plus précise.', 'pa83-anamnese'),
 ('Dans le cadre localisé, le syndrome myofascial se recherche par ses points gâchettes et la douleur qu’ils reproduisent.', ['p83-myofascial-fibro','p83-phenotype']),
 ('Dans un tableau diffus chronique, la fibromyalgie associe la douleur à d’autres symptômes, notamment la fatigue et les troubles du sommeil.', 'p83-myofascial-fibro'),
 ('Ces présentations guident l’enquête ; des signes de myopathie ou une autre évolution imposent de compléter l’évaluation.', ['p83-myofascial-fibro','pa83-biologie'])
])
p.h('Douleur, faiblesse et inflammation ne sont pas synonymes')
p.p('L’examinateur recherche une faiblesse accompagnant la douleur et la vérifie cliniquement, car les deux symptômes apportent des informations différentes.', 'p83-phenotype')
p.p('La force se mesure par une cotation ou une évaluation fonctionnelle ; sa diminution peut aussi accompagner une affection articulaire, tendineuse ou neurologique.', 's103')
p.p('Une myopathie inflammatoire immunomédiée appartient à un groupe distinct, dans lequel la faiblesse musculaire et l’atteinte immunitaire guident le diagnostic.', 'p83-myopathies-inflammatoires')
p.p('Les CK peuvent orienter vers une atteinte musculaire, mais certaines myosites ont des valeurs normales et un effort important peut les augmenter chez une personne saine.', 'pa83-biologie')
p.fenetre('Trois confusions qui modifient la conduite',[
 ('Les courbatures apparaissent après l’activité ; la contusion associe au contraire un choc direct et une douleur immédiate.', 'p83-doms-contusion-clinique'),
 ('Une élévation des CK après exercice se distingue d’un épisode pathologique par la présentation clinique et les complications éventuelles.', 'e13'),
 ('Le consensus ENMC associe au diagnostic de rhabdomyolyse une symptomatologie musculaire et une augmentation des CK replacée dans son évolution.', 'e12'),
 ('La pseudopolyarthrite rhizomélique se reconnaît dans un ensemble de signes et de symptômes compatibles, après recherche des affections qui peuvent l’imiter.', 'p83-eular26-diagnostic'),
 ('Une amélioration sous glucocorticoïdes ne constitue pas un essai diagnostique recommandé pour cette dernière affection.', 'p83-eular26-pas-test-gc')
])
p.h('Qualifier le contexte sans attribuer trop vite la cause')
p.p('Le terme « symptômes musculaires associés aux statines » conserve la question du lien causal ; la présence du médicament ne remplace pas l’évaluation des autres explications.', 'p83-statine-frequence')
p.p('Une hypothyroïdie peut elle-même provoquer douleur, fatigabilité ou faiblesse proximale, avec des CK normales ou augmentées.', 'p83-hypothyroidie')
p.p('Une faiblesse progressive ou une dysphagie dans ce contexte ouvre notamment la recherche d’une myopathie nécrosante immunomédiée.', 'p83-statine-imnm')
p.p('Enfin, l’orientation urgente repose sur les menaces observées : constantes anormales, anurie, syndrome des loges ou complications métaboliques.', 'e13')
p.p('La recherche de symptômes crâniens et visuels est immédiate lorsqu’une artérite à cellules géantes est suspectée, car elle peut entraîner une perte visuelle irréversible.', 'p83-eular26-orientation')
p.sauver()
