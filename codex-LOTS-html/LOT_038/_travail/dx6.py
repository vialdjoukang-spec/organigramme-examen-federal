from format_lecon import Lesson,paras,table,steps
from coamoxicilline_orale import adulte,enfant
l=Lesson('Cellulite préseptale',6)
adult=adulte(l);ped=enfant(l)
l.add('La {cellulite préseptale} est une infection des tissus palpébraux situés en avant du septum orbitaire. Elle donne une rougeur et un gonflement souvent unilatéraux. Le diagnostic exige de rechercher une atteinte plus profonde de l’orbite.',paras(
 'Le terme cellulite désigne ici une infection de peau et de tissus mous, sans rapport avec un aspect esthétique de la peau. La localisation préseptale s’oppose à l’atteinte orbitaire postseptale, qui expose à des complications visuelles et intracrâniennes.',
 'Une forme préseptale peut être sensible au toucher et s’accompagner de fièvre. En revanche, douleur aux mouvements oculaires, limitation de motilité, exophtalmie et baisse visuelle font suspecter une extension orbitaire.',
 'La distinction ne se fait pas sur une photographie isolée ni sur l’intensité apparente de l’œdème. Si l’œil ne peut pas être examiné, la sécurité d’une localisation superficielle n’est pas établie. Une évaluation hospitalière urgente est alors nécessaire.'),(9,36,37,41))
l.add('Le {contexte infectieux} recherche une porte d’entrée et un foyer voisin. Une lésion cutanée ou une infection palpébrale peut précéder le gonflement. Une sinusite associée augmente l’attention portée aux structures profondes.',paras(
 'Une plaie, une piqûre surinfectée, un orgelet ou une infection lacrymale peut être à l’origine de l’inflammation. Rechercher aussi une infection sinusienne ou dentaire selon la localisation et les symptômes.',
 'Une réaction inflammatoire après piqûre n’est pas toujours infectieuse. Une tuméfaction prurigineuse sans chaleur douloureuse ni signe général peut avoir un autre mécanisme, mais l’examen oculaire reste nécessaire si la présentation est inquiétante.',
 'Le terrain modifie le risque et l’orientation : très jeune âge, immunodépression, fragilité, diabète, traitements antérieurs et impossibilité de suivi fiable. Le statut vaccinal de l’enfant fait partie de l’histoire clinique.',
 'Aucune fréquence suisse chiffrée ni classement microbiologique local n’est inventé ici. La porte d’entrée, les expositions et les données de résistance du lieu de soins déterminent le traitement probabiliste.'),(9,36,37,38))
l.add('Les {bases anatomiques et microbiologiques} expliquent le risque d’extension. Le septum orbitaire sert de repère entre paupière et orbite. L’origine de l’infection aide à anticiper les germes et les complications.',paras(
 'La peau et le tissu sous-cutané palpébral se situent en avant du septum. Les tissus orbitaires comprennent notamment graisse, muscles et structures neurovasculaires. Une atteinte postseptale peut gêner les mouvements ou menacer le nerf optique.',
 'Les sinus, particulièrement l’ethmoïde, sont proches de l’orbite. La présentation HUG décrit l’extension depuis les cellules ethmoïdales à travers la région de la lame papyracée. Des complications intracrâniennes sont possibles en cas d’infection profonde.',
 'Les infections de peau impliquent notamment staphylocoques et streptocoques, tandis qu’une origine sinusienne élargit les hypothèses. Le choix antibiotique ne peut pas être identique pour toute porte d’entrée ou tout terrain.',
 'L’amoxicilline agit sur la synthèse de paroi ; le clavulanate inhibe certaines bêta-lactamases. Cette association ne couvre pas automatiquement toutes les résistances. Une culture pertinente et l’évolution clinique permettent de réviser le traitement.'),(9,37,38,39))
l.add('La démarche identifie les {situations à hospitaliser}. Une atteinte visuelle ou motrice fait suspecter une cellulite orbitaire. L’impossibilité d’examiner l’œil est elle-même une raison d’escalader la prise en charge.',table(['Constat','Risque','Conduite'],[
 ['Douleur aux mouvements, limitation, diplopie ou exophtalmie','Atteinte postseptale.','Évaluation hospitalière immédiate avec ophtalmologie et ORL.'],
 ['Baisse visuelle, couleur perçue différemment ou anomalie pupillaire','Atteinte du nerf optique ou du globe.','Urgence hospitalière, sans attendre la fin d’un traitement oral.'],
 ['Œil fermé impossible à examiner','Extension profonde non exclue.','Évaluation urgente et imagerie selon l’équipe.'],
 ['Altération générale, mauvaise perfusion, progression rapide','Sepsis ou infection invasive.','Prise en charge urgente ; appel 144 si instabilité.'],
 ['Céphalée intense, vomissements persistants, somnolence ou signe neurologique','Complication intracrânienne.','Évaluation urgente multidisciplinaire.'],
 ['Nourrisson très jeune, immunodépression ou voie orale impossible','Risque accru et traitement ambulatoire peu sûr.','Évaluation pédiatrique/hospitalière et traitement adapté.']
 ]),(9,36,37,39,41))
l.add('L’{anamnèse ciblée} précise la progression et la porte d’entrée. Elle recherche les symptômes orbitaires et généraux. Les traitements déjà pris doivent être documentés avec dose et durée.',steps(
 'Noter le début de la rougeur, la vitesse d’extension, la douleur et la fièvre.',
 'Demander douleur à la mobilisation du regard, diplopie, vision floue et céphalées.',
 'Rechercher rhinite ou sinusite récente, douleur dentaire, écoulement lacrymal, orgelet, plaie et piqûre.',
 'Identifier chirurgie ou traumatisme récent, corps étranger possible, morsure et expositions particulières.',
 'Préciser âge, poids de l’enfant, statut vaccinal, immunodépression et maladies associées.',
 'Reconstituer antibiotiques antérieurs, allergies avec description de la réaction, fonction rénale/hépatique et autres médicaments.',
 'Vérifier possibilité de boire, prendre le traitement, revenir rapidement et bénéficier d’une surveillance fiable.'),(9,36,38,39,41))
l.add('L’{examen} documente séparément la paupière et le globe. La vision et les mouvements oculaires doivent être réellement évalués. L’état général peut imposer une hospitalisation même sans signe orbitaire évident.',paras(
 'Mesurer température et paramètres vitaux selon l’âge. Apprécier vigilance, hydratation, perfusion et douleur. Une tachycardie ou tachypnée persistante avec fièvre et altération générale renforce la gravité.',
 'Décrire l’étendue de la rougeur, la chaleur, la sensibilité, les plaies et une éventuelle collection. Éviter de presser ou percer une lésion palpébrale. Un foyer au canthus interne suggère une atteinte du sac lacrymal.',
 'Comparer l’acuité visuelle, les pupilles, la position des globes et la motilité. Demander si les mouvements provoquent une douleur et rechercher une diplopie. Évaluer la perception des couleurs lorsque cela est possible et pertinent.',
 'Examiner les territoires voisins selon la clinique : sinus, nez, bouche et dents. Une atteinte neurologique exige un examen adapté. Une coopération insuffisante ou un œdème majeur doit être écrit comme limite, jamais converti en examen normal.'),(9,36,37,41))
l.add('L’{approche syndromique} sépare infection diffuse, lésion focale et inflammation non infectieuse. La fièvre aide sans être obligatoire. Le diagnostic le plus dangereux à exclure reste l’atteinte orbitaire.',table(['Hypothèse','Indices utiles','Décision'],[
 ['Cellulite préseptale','Rougeur chaude et sensible de la paupière, œil examinable normal.','Antibiothérapie systémique et suivi selon gravité.'],
 ['Cellulite orbitaire','Motilité douloureuse ou limitée, exophtalmie, vision atteinte.','Hospitalisation urgente.'],
 ['Orgelet avec inflammation locale','Nodule douloureux focal au bord ou dans la paupière.','Rechercher extension diffuse avant de rester aux soins locaux.'],
 ['Dacryocystite','Douleur et gonflement au canthus interne inférieur.','Prise en charge du foyer lacrymal.'],
 ['Dermatite ou allergie','Prurit, exposition, lésions cutanées ou atteinte bilatérale.','Démarche allergique après exclusion d’infection.'],
 ['Réaction inflammatoire à une piqûre','Chronologie de piqûre et signes locaux sans infection démontrée.','Ne pas prescrire automatiquement un antibiotique.'],
 ['Tumeur ou inflammation orbitaire non infectieuse','Évolution atypique ou persistante.','Exploration spécialisée.']
 ]),(1,4,6,9,36))
l.add('Le {diagnostic positif} d’une forme préseptale repose sur une infection palpébrale compatible et un examen oculaire rassurant. Il reste réévalué avec l’évolution. Une atteinte profonde ne se trouve pas exclue par la seule absence de fièvre.',paras(
 'Une vision préservée, des pupilles normales, des mouvements libres non douloureux et l’absence d’exophtalmie soutiennent la localisation antérieure. Ces observations doivent être accessibles à l’examen et documentées.',
 'Les signes orbitaires ne sont pas toujours tous présents. Une douleur nouvelle, une progression sous traitement ou une difficulté croissante à examiner l’œil impose de reprendre le classement de gravité.',
 'L’imagerie ne se justifie pas automatiquement pour toute forme légère bien examinée. Elle devient importante si le diagnostic de localisation est douteux, si l’évolution est défavorable ou si une complication est suspectée.'),(9,37,41))
l.add('Les {examens complémentaires} dépendent de la gravité et de la certitude de localisation. Une forme légère avec examen oculaire normal peut ne pas nécessiter de bilan systématique. Une suspicion orbitaire exige une évaluation urgente.',
 '<h3>9.a — Examen de référence</h3>'+paras('Le diagnostic initial est clinique. Une TDM avec contraste des orbites et des sinus recherche une atteinte profonde ou une collection lorsque les signes le justifient. Le bilan cérébral et le choix d’une autre imagerie dépendent des signes neurologiques et de l’équipe spécialisée.')+
 '<h3>9.b — Première intention</h3>'+paras('Documenter vision, pupilles, motilité et état général. Le parcours pédiatrique BSAC ne demande pas de biologie systématique pour une forme préseptale légère ou modérée sans autres critères. Un prélèvement n’est utile que s’il répond à une question clinique et peut modifier le traitement.')+
 '<h3>9.c — Gravité ou doute</h3>'+paras('En cas de gravité accrue, le parcours prévoit numération, marqueurs inflammatoires et hémocultures. Les prélèvements ne doivent pas retarder une antibiothérapie urgente. Un drainage ou une exploration sinusienne permet des prélèvements ciblés si indiqué.',
 'Une imagerie est discutée si l’œil ne peut pas être examiné, si des signes postseptaux apparaissent, si l’état progresse malgré le traitement ou si l’amélioration attendue manque. L’antibiothérapie urgente ne doit pas attendre l’organisation de l’imagerie.')+
 '<h3>9.d — Réévaluation</h3>'+paras('Une biologie initialement peu modifiée ne suffit pas à écarter une complication. Reprendre l’examen, les doses, la tolérance et la porte d’entrée en cas d’échec. Un abcès, un corps étranger ou une résistance peut exiger une autre stratégie.'),(9,37,41))
l.add('L’{arbre décisionnel} conditionne la voie orale à une évaluation fiable. Le suivi est organisé avant la sortie. Une aggravation provoque une réévaluation immédiate, indépendamment du nombre de prises déjà reçues.',steps(
 'Si signe orbitaire, neurologique, sepsis ou examen impossible, alors adresser immédiatement à l’hôpital.',
 'Si terrain à risque, très jeune âge, progression rapide ou voie orale impossible, alors demander une évaluation hospitalière même sans signe orbitaire établi.',
 'Si forme légère, patient en bon état général, examen oculaire normal et suivi fiable, alors envisager le traitement ambulatoire après décision médicale.',
 'Choisir l’antibiotique selon la porte d’entrée, les résistances locales, l’allergie et la notice de la présentation.',
 'Prévoir un contrôle précoce, généralement dans les vingt-quatre à quarante-huit heures, et donner des consignes de retour immédiat.',
 'Si progression ou absence d’amélioration au contrôle, alors réévaluer la localisation, la voie de traitement et l’indication d’imagerie ou drainage.'),(9,36,38,39,41))
l.add('La {prise en charge suisse} repose sur un antibiotique systémique adapté et une surveillance rapprochée. Un traitement local seul ne suffit pas à une infection diffuse des tissus palpébraux. Le choix ambulatoire exige un œil examinable et l’absence de gravité.',
 '<h3>11.A — But</h3>'+paras('Contrôler l’infection, traiter sa porte d’entrée et empêcher une extension profonde. Reconnaître rapidement une complication sans attendre une cure complète. Adapter la voie et le spectre à la situation réelle.')+
 '<h3>11.B — Moyens</h3>'+paras('Une association amoxicilline–clavulanate peut être retenue pour une forme légère sélectionnée lorsque les germes attendus sont sensibles. Le choix n’est pas automatique en cas d’allergie, de portage résistant, d’immunodépression ou d’exposition particulière. Les formes suisses et leurs restrictions sont détaillées ici :')+adult+ped+paras(
 'Chez l’adulte sélectionné, le repère cité est 500/125 mg par voie orale trois fois par jour pendant sept jours, avec adaptation rénale et réévaluation précoce. La dose provient de l’AIPS ; la durée est un repère européen, non une prescription universelle ni une durée fournie par l’AIPS.',
 'Chez l’enfant, utiliser la notice et le calcul de la suspension choisie, sans transposer les concentrations ou doses de documents étrangers. La décision de traiter à domicile dépend de l’examen et du suivi, pas seulement de l’existence d’une dose orale.',
 'Une forme sévère ou une atteinte orbitaire possible exige une antibiothérapie hospitalière, généralement intraveineuse initialement, et des avis ophtalmologique et ORL. Les schémas d’allergie et d’infection résistante sont définis avec l’infectiologie selon le contexte.',
 'Traiter un foyer sinusien, dentaire ou lacrymal lorsque nécessaire. Une collection peut demander un drainage spécialisé. Ni pression sur la paupière, ni incision domestique, ni corticoïde local empirique. Les pommades du chapitre orgelet ne remplacent pas l’antibiothérapie systémique.')+
 '<h3>11.C — Surveillance</h3>'+paras('Contrôler précocement l’état général, la fièvre, la douleur, l’étendue locale, la vision et la motilité. Vérifier chaque prise, la concentration du flacon, les vomissements éventuels et la fonction rénale si pertinente.',
 'Donner des consignes écrites : retour immédiat si douleur aux mouvements, diplopie, vision modifiée, œil impossible à ouvrir, céphalée importante, somnolence ou aggravation générale. Une photo peut documenter l’évolution cutanée mais ne remplace pas l’examen du globe.',
 'Le parcours BSAC prévoit une escalade en cas de progression après vingt-quatre heures ou d’absence d’amélioration après quarante-huit heures. Ces repères n’autorisent jamais à attendre en présence d’une alarme.')+
 '<h3>11.D — Pronostic et suivi</h3>'+paras('Une forme préseptale correctement traitée peut évoluer favorablement sans atteinte visuelle. Le suivi confirme cette évolution et permet d’ajuster la durée. Une persistance impose de rechercher foyer non contrôlé, collection, mauvaise absorption, résistance ou erreur diagnostique.',
 'La guérison ne se juge pas seulement à la fièvre. Le retour à une vision et une motilité normales, déjà attendues au départ, doit être confirmé. L’apparition de leur anomalie transforme la conduite à tenir.'),(9,36,37,38,39,40,41))
l.add('La {prévention} comprend les soins des portes d’entrée et la connaissance des alarmes. Elle évite l’automédication par une ancienne ordonnance. Les mesures sont adaptées à l’âge et au contexte.',paras(
 'Traiter correctement les lésions cutanées et les foyers dentaires ou lacrymaux. Ne pas manipuler un orgelet ni appliquer un désinfectant cutané irritant dans l’œil. Les soins généraux de plaie ne se transposent pas sans précaution à la surface oculaire.',
 'Vérifier le statut vaccinal selon les recommandations suisses adaptées à l’âge. Après une morsure ou un traumatisme, évaluer spécifiquement la plaie, un éventuel corps étranger et la protection antitétanique.',
 'Expliquer concentration, seringue, durée prescrite, conservation et signes de réaction au médicament. Ne pas partager les antibiotiques, garder des restes pour un épisode futur ou interrompre sans avis au seul motif d’une amélioration précoce.',
 'Organiser le lieu et l’heure du contrôle avant la sortie. Un traitement ambulatoire ne reste sûr que si le patient ou les proches peuvent reconnaître une aggravation et revenir rapidement.'),(9,36,38,39))
l.add('Les {points clés} placent l’examen du globe avant l’étiquette de cellulite superficielle. L’antibiothérapie doit correspondre à la forme suisse choisie. Le suivi précoce est une composante du traitement.',steps(
 'Examen impossible signifie localisation profonde non exclue.',
 'Douleur aux mouvements, diplopie, exophtalmie ou vision atteinte imposent l’hôpital.',
 'Une forme légère ambulatoire exige état général rassurant et retour fiable.',
 'Une pommade antibiotique ne suffit pas à une cellulite diffuse.',
 'Pour les suspensions, distinguer composant amoxicilline, somme des composants et dose quotidienne.',
 'Ne pas attendre vingt-quatre ou quarante-huit heures devant une aggravation ou une alarme.'),(9,36,38,39,41))
l.quiz([
 ('Où se situe une cellulite préseptale ?','Dans les tissus en avant du septum orbitaire.'),
 ('La douleur cutanée à la palpation prouve-t-elle une atteinte orbitaire ?','Non. La douleur aux mouvements oculaires et les autres signes orbitaires sont particulièrement préoccupants.'),
 ('Quel examen est nécessaire avant de retenir une forme légère ambulatoire ?','Un examen oculaire fiable, notamment vision, pupilles et motilité, avec état général rassurant.'),
 ('Que faire si l’œdème empêche l’examen du globe ?','Organiser une évaluation hospitalière urgente, car une atteinte profonde ne peut pas être exclue.'),
 ('L’absence de fièvre exclut-elle une cellulite orbitaire ?','Non. Les signes oculaires et l’évolution gardent leur importance.'),
 ('Une piqûre rouge nécessite-t-elle toujours un antibiotique ?','Non. Une réaction inflammatoire non infectieuse est possible ; la clinique guide la distinction.'),
 ('Une TDM est-elle obligatoire pour toute forme préseptale légère ?','Non. Elle est guidée par le doute, la gravité, les signes orbitaires ou l’évolution défavorable.'),
 ('Que contient un comprimé Augmentin 625 mg ?','500 mg d’amoxicilline et 125 mg d’acide clavulanique.'),
 ('La durée de sept jours citée est-elle une dose AIPS ?','Non. La dose est issue de l’AIPS ; la durée est un repère de guide à adapter à l’évolution.'),
 ('Peut-on remplacer une suspension 312,5 par 457 au même volume ?','Non. Concentration, rapport des composants, fréquence et indications diffèrent.'),
 ('Les mg/kg/jour de la notice doivent-ils être donnés à chaque prise ?','Non. Ils constituent une dose quotidienne à répartir selon la présentation.'),
 ('La barre du comprimé Augmentin à 1 g définit-elle une demi-dose validée ?','Non. La notice précise qu’elle facilite la prise, sans servir à réduire la dose de moitié.'),
 ('Une photo montrant moins de rougeur suffit-elle au contrôle ?','Non. Il faut aussi apprécier état général, vision, pupilles, motilité et tolérance.'),
 ('Faut-il attendre deux jours si une diplopie apparaît après la première prise ?','Non. Une alarme orbitaire impose une réévaluation hospitalière immédiate.')
 ],(9,36,38,39,40,41))
l.write()
