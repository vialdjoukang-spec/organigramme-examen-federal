from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parent.parent))
from rendu import outils

B,p,c,h,w,table,liste,save=outils(1,6)
t=h('6.a — La référence normale précède la description des anomalies')
t+=p('L’examen de la force commence par une référence explicite : dans le support clinique des HUG, une force cotée5 s’oppose normalement à une résistance extérieure importante. Une limitation douloureuse du mouvement et une faiblesse motrice objectivée sont donc décrites séparément.','oa82-hug-force','c83-15')
t+=p('Une personne sans plainte peut présenter des points latents à la palpation. Le clinicien confronte ainsi chaque point découvert à la fonction et à la reconnaissance des symptômes, plutôt que considérer la sensibilité provoquée comme une anomalie suffisante.','eu83-phenotypes','eu83-latent')
t+=p('La référence fonctionnelle porte sur l’activité habituelle et sur le mouvement qui pose problème. L’entretien précise ce que le patient peut faire, ce qu’il évite et comment la douleur affecte sa vie, afin de donner un sens aux observations régionales.','nice83-vie','c83-15')
a=w('Force musculaire : normalité, limitation et échelle clinique',[
('La cotation va de0 à5 : le grade0 correspond à l’absence de contraction visible ; le grade1 à une contraction visible ou palpable sans mouvement articulaire.',['oa82-hug-force']),
('Le grade2 correspond au mouvement lorsque la pesanteur est éliminée, le grade3 au mouvement contre la pesanteur et le grade4 au mouvement contre une résistance extérieure. Le grade5 constitue la référence de force normale.',['oa82-hug-force']),
('Une réduction de force peut provenir d’une synovite, d’une arthropathie, d’un problème musculotendineux ou d’une atteinte nerveuse. La cotation décrit donc un résultat qui demande une interprétation clinique.',['oa82-hug-force']),
('Le patient peut décrire comme une faiblesse la sous-utilisation d’un muscle dont la contraction provoque la douleur. Cette explication reste confrontée à l’examen neurologique et aux autres signes objectifs.',['c83-15','c83-30'])])
t+=p('La fenêtre '+a+' aide à consigner le mouvement testé et le niveau de fonction. La description clinique reste ainsi plus précise qu’une simple mention de contracture ou de faiblesse.','oa82-hug-force','c83-15')
t+=h('6.b — La palpation construit une concordance anatomoclinique')
t+=p('Le clinicien recherche d’abord la bande tendue dans le muscle concerné, puis sa zone la plus hypersensible. La bande suit l’organisation du faisceau musculaire ; le point recherché se situe dans cette structure et non dans toute la région où la douleur est ressentie.','p83-myofascial-fibro','c83-7')
t+=p('Une stimulation du point précise la douleur locale, la sensation à distance et sa familiarité. Le patient indique si la sensation ressemble à celle qui motive la consultation, car cette reconnaissance distingue notamment le point actif d’un point latent.','eu83-actif','eu83-latent')
a=w('Trois observations pendant la recherche du point',[
('La bande tendue se décrit comme un faisceau ferme et raccourci accessible à la palpation. Le clinicien repère ensuite le foyer hypersensible au sein de ce faisceau.',['p83-myofascial-fibro','iasp83-criteres']),
('La douleur référée apparaît dans une zone différente du point stimulé. L’examinateur demande au patient de la localiser et d’en décrire la sensation, puis confronte le résultat à la plainte habituelle.',['c83-1','eu83-latent']),
('La secousse locale est une contraction brève du faisceau stimulé. Elle s’observe pendant la palpation et se distingue du mouvement global de retrait ou de sursaut du patient.',['c83-7','iasp83-criteres'])])
t+=p('La fenêtre '+a+' sépare le constat tissulaire, la réponse sensorielle et la réponse motrice. Cette séparation améliore la description sans imposer qu’une réaction observée résume à elle seule le diagnostic.','iasp83-criteres','c83-25')
t+=p('Les symptômes provoqués peuvent comprendre une douleur profonde, une brûlure ou des picotements. Toutefois, le territoire d’une douleur référée ne correspond pas nécessairement à celui d’un nerf ou d’une racine ; l’examen neurologique complète donc la palpation.','eu83-latent','c83-9','c83-30')
t+=h('6.c — Mouvement, étirement et usage du muscle')
t+=p('La douleur à la contraction ou à l’étirement du muscle atteint fait partie des éléments cliniques confirmatoires décrits par l’IASP. L’examinateur note donc le geste qui provoque la plainte et le distingue de la douleur obtenue par pression directe.','iasp83-criteres')
t+=p('La fatigue musculaire et les adaptations du recrutement peuvent limiter la fonction. L’examen apprécie ainsi la tâche et le contrôle moteur, en complément du repérage du point sensible.','eu83-moteur','nice83-vie')
t+=p('Une augmentation compensatoire de l’activité de muscles voisins peut rendre le tableau plus complexe. Le clinicien examine alors les muscles impliqués dans le geste et recherche les facteurs mécaniques qui continuent d’agir.','c83-16','c83-22')
t+=h('6.d — Régions cervicale et du membre supérieur : garder l’examen neurologique')
t+=p('Dans une douleur cervicale ou irradiant vers le membre supérieur, le dessin de la douleur ne suffit pas à départager un mécanisme musculaire et radiculaire. Le bilan confronte la topographie aux réflexes, à la force et à la sensibilité.','c83-9','c83-30')
t+=p('Les circonstances d’accentuation, dont les mouvements du rachis, participent aussi au différentiel avec une douleur facettaire. La recherche de zones gâchettes par un examinateur expérimenté apporte donc un élément supplémentaire, dans l’ensemble de l’évaluation.','c83-31')
t+=p('Une compression d’un nerf voisin peut parfois accompagner la modification musculaire. Dans ce cas, la topographie neurologique est distinguée de la sensation référée, et le bilan ne se réduit pas à l’étiquette myofasciale.','c83-13')
t+=h('6.e — Région lombopelvienne et membre inférieur : raisonner sur la concordance')
t+=p('Des douleurs myofasciales du petit fessier ou du piriforme peuvent évoquer une radiculopathie. La distinction demande la convergence du récit, de l’examen neurologique et des examens ciblés, plutôt que la seule présence d’une irradiation vers le membre inférieur.','c83-30')
t+=p('Le contexte mécanique recherche également une différence de longueur des membres, un trouble postural ou une affection articulaire associée. Ces éléments peuvent participer au maintien des symptômes et orienter l’adaptation du programme fonctionnel.','c83-22')
t+=p('Un déficit moteur ou des signes sphinctériens nouveaux avec symptômes rachidiens changent la priorité. Les HUG demandent alors une imagerie sans attendre et un avis neurochirurgical, au lieu de poursuivre uniquement des techniques locales.','pa17-lomb22-queue','pa17-lomb22-urgence')
t+=h('6.f — Après traumatisme ou avant needling : les tissus à risque sont examinés')
t+=p('Après un choc direct, l’examen décrit la douleur immédiate, l’hématome et la limitation active. Une douleur disproportionnée ou déclenchée par le mouvement passif des muscles concernés ouvre toutefois la recherche urgente d’un syndrome des loges.','p83-doms-contusion-clinique','p83-boast-loges-0')
t+=p('Avant un dry needling, le guide suisse demande une recherche de signes de saignement cutané ou d’hématomes et une vérification des zones à risque. Une altération cutanée, une infection locale ou la proximité d’un implant modifie donc la sécurité du geste.','dvs83-coagulation','dvs83-locaux')
t+=p('Le dossier consigne les constatations, les symptômes reproduits et la réponse fonctionnelle. Le guide suisse insiste sur une histoire complète, le consentement et le suivi des réactions au traitement, ce qui facilite une réévaluation cohérente.','dvs83-competences')
save(t)

B,p,c,h,w,table,liste,save=outils(1,7)
t=h('7.1 — Tableau régional avec point gâchette actif')
t+=p('Les signes fonctionnels sont une douleur régionale et une gêne à l’usage du muscle ; les signes physiques sont une bande tendue et un foyer hypersensible. La stimulation du foyer reproduit alors une partie ou l’ensemble des symptômes familiers.','c83-1','c83-7','eu83-actif')
a=w('Définition clinique du point actif et geste de recherche',[
('Le point actif se définit par sa contribution à la plainte vécue, plutôt que par la seule intensité de la pression douloureuse. Le clinicien recherche donc une sensation reconnue comme familière.',['eu83-actif','eu83-latent']),
('La palpation repère la bande tendue puis son point hypersensible ; la stimulation précise la douleur locale et les sensations à distance. Cette séquence relie un constat physique à une expérience sensorielle.',['iasp83-criteres','c83-7']),
('La bande ferme et la sensibilité locale constituent les éléments tissulaires observables ; les médiateurs et la sensibilisation sont des mécanismes proposés expliquant la réponse. Les deux niveaux d’analyse restent ainsi distincts.',['iasp83-physio','eu83-milieu'])])
t+=p('La fenêtre '+a+' détaille les éléments du tableau. L’existence d’un point latent chez une personne sans plainte conduit toutefois à exiger une concordance avec les symptômes et le retentissement.','eu83-phenotypes','barbero83-resume')
t+=h('7.2 — Tableau de sensation référée et d’hypersensibilité')
t+=p('Le signe fonctionnel est une sensation perçue à distance du foyer musculaire ; elle peut être profonde, brûlante ou décrite comme des picotements. Le signe physique est sa reproduction pendant la stimulation du point identifié.','eu83-latent','iasp83-clinique')
a=w('Sensation référée : définition, topographie et mécanisme',[
('Le terme référé indique une perception située ailleurs que le foyer stimulé. Le clinicien demande au patient de préciser le territoire et le caractère de la sensation obtenue.',['c83-1','eu83-latent']),
('Le dessin peut évoquer une radiculopathie sans correspondre exactement à l’innervation d’une racine ou d’un tronc nerveux. Les réflexes, la force et la sensibilité apportent donc des informations différentes.',['c83-9','c83-30']),
('Les modèles décrivent une contribution des entrées périphériques à la sensibilisation de neurones spinaux et supraspinaux. Cette explication aide à relier la stimulation locale et l’extension de la perception.',['eu83-milieu','eu83-neurophysio'])])
t+=p('La fenêtre '+a+' n’efface pas le bilan d’une atteinte neurologique associée. Une faiblesse objective, des troubles de sensibilité organisés ou une alarme sphinctérienne sont donc examinés selon leur propre portée.','c83-30','pa17-lomb22-queue','pa17-lomb22-urgence')
t+=p('Une hypersensibilité aux stimulations douloureuses correspond à l’hyperalgie, tandis que l’allodynie concerne des stimulations non nociceptives. La description du stimulus utilisé fait ainsi partie du compte rendu du signe.','iasp83-physio')
t+=h('7.3 — Tableau moteur douloureux et adaptations fonctionnelles')
t+=p('Les signes fonctionnels comprennent une fatigabilité, une gêne à la contraction ou une activité réduite. L’examen décrit la force, la tâche limitée et les adaptations du recrutement musculaire, en séparant la limitation douloureuse d’un déficit neurologique.','c83-15','eu83-moteur','oa82-hug-force')
a=w('Faiblesse ressentie et faiblesse objectivée',[
('La douleur peut réduire l’utilisation du muscle et être décrite par le patient comme une faiblesse. Le clinicien précise donc le mouvement empêché, la provocation douloureuse et les capacités conservées.',['c83-15','nice83-vie']),
('La force peut être cotée sur l’échelle clinique des HUG ; une force normale oppose une résistance extérieure importante. Une diminution de cotation demande une interprétation qui inclut les causes articulaires, musculotendineuses et nerveuses.',['oa82-hug-force']),
('Les modèles moteurs associent points gâchettes, activation musculaire modifiée, fatigabilité et coactivation antagoniste. L’exercice adapté vise ainsi la fonction et le contrôle du geste, pas seulement la disparition d’une douleur à la pression.',['eu83-moteur','eu83-multimodal'])])
t+=p('La fenêtre '+a+' précise la place du testing. Une faiblesse proximale progressive ou une dysphagie sous statine évoque toutefois un autre niveau de maladie musculaire et conduit à un bilan spécifique.','p83-statine-imnm')
t+=p('Les muscles voisins peuvent augmenter leur activité compensatoire et participer à la persistance régionale. L’analyse fonctionnelle recherche donc les relations entre le muscle douloureux, le geste et les autres facteurs mécaniques.','c83-16','c83-22')
t+=h('7.4 — Tableau persistant avec retentissement biopsychosocial')
t+=p('Les signes fonctionnels comprennent une douleur durable, des difficultés d’activité, un sommeil perturbé ou une inquiétude liée aux limitations. Le bilan clinique garde la carte de la douleur et les constatations régionales, en appréciant également le retentissement sur la vie.','c83-20','c83-23','nice83-vie')
a=w('Persistance et sensibilisation : ce que le modèle change dans la conduite',[
('La persistance peut dépasser la résolution de l’événement initial ; les facteurs de maintien deviennent alors une cible de l’entretien et du programme de soins. Le clinicien distingue ainsi ce qui a déclenché la douleur de ce qui continue à l’entretenir.',['c83-20','c83-21','c83-22']),
('Une interaction bidirectionnelle entre nociception périphérique et sensibilisation centrale est proposée. Elle soutient une prise en charge combinant moyens locaux et stratégies actives d’autogestion.',['eu83-nociplastic','eu83-multimodal']),
('Une amélioration après une technique passive à court terme ne démontre pas la correction durable de tous les mécanismes. Le suivi porte donc aussi sur l’activité, l’autonomie et les facteurs personnels associés.',['eu83-limite-effet','eu83-multimodal','nice83-vie'])])
t+=p('La fenêtre '+a+' aide à organiser le suivi d’un tableau chronique. Si la présentation devient plus diffuse ou change, le diagnostic est réévalué plutôt que conservé automatiquement.','nice83-vie','p83-myofascial-fibro')
t+=h('7.5 — Tableau associé qui impose une bifurcation')
t+=p('Une douleur référée musculaire peut coexister avec une autre affection. Une hypothyroïdie, une atteinte nerveuse, une pathologie articulaire ou une autre douleur chronique ne sont donc pas éliminées par le seul constat d’un point sensible.','c83-22','p83-hypothyroidie','nice83-vie')
t+=p('Le tableau aigu d’effort ou traumatique reste analysé pour lui-même : la rhabdomyolyse et le syndrome des loges possèdent leurs menaces propres. Cette bifurcation maintient la priorité de sécurité même si une sensibilité musculaire est également présente.','p83-rhabdo-menace','p83-boast-loges-0','p83-boast-loges-3')
t+=table(['Regroupement clinique','Signes fonctionnels','Signes physiques utiles'],[
[p('Régional avec point actif.','eu83-actif'),p('La plainte habituelle est reproduite.','eu83-actif'),p('Une bande tendue et un foyer hypersensible sont recherchés.','iasp83-criteres')],
[p('Sensation référée.','eu83-latent'),p('Une perception douloureuse ou sensorielle se projette à distance.','eu83-latent'),p('La stimulation précise la topographie ; l’examen neurologique caractérise les anomalies associées.','c83-30')],
[p('Moteur douloureux.','eu83-moteur'),p('La contraction, la fatigue et les activités sont décrites.','iasp83-criteres','nice83-vie'),p('La force et la fonction distinguent limitation et déficit.','oa82-hug-force')],
[p('Persistant et invalidant.','c83-20'),p('Le sommeil, le travail et les relations peuvent être touchés.','nice83-vie'),p('L’examen régional est confronté à une réévaluation globale.','nice83-evaluation','nice83-vie')]])
save(t)
