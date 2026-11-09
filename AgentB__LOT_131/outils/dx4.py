# -*- coding: utf-8 -*-
"""DX.4 Hypospadias — chapitre EAU pédiatrique relu le 9 novembre 2026."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from dx_lib import b, w, ilot, tableau
DX = 4

def body() -> str:
    P = []
    P.append(ilot(DX, 1, "Définition et sémantique", """
<p>L’hypospadias est, dans le chapitre homonyme des recommandations européennes d’urologie pédiatrique relu le 9 novembre 2026, une malformation dans laquelle le méat urétral s’ouvre sur la face ventrale, plus ou moins loin du sommet du gland, avec souvent un prépuce en capuchon et une courbure. [S1]</p>
""" + w("dx4-p1-def",
"Le méat est l’orifice par lequel l’urine sort. Dans l’hypospadias il n’est pas au sommet.",
"Le plateau urétral ne se ferme pas jusqu’au bout, l’orifice reste ventral, la peau dorsale du prépuce est en excès et la face ventrale est courte.",
"Exemple : la prévalence européenne citée est de 18,6 nouveaux cas pour 10 000 naissances masculines, fourchette 5,1 à 36,8, d’après EUROCAT. [S1]",
"Le piège est d’appeler hypospadias toute courbure du pénis sans regarder où s’ouvre le méat.",
"Source [S1].") + """
<p>Le chapitre classe selon le siège : forme distale-antérieure, sur le gland ou la verge distale ; forme moyenne ; forme proximale-postérieure. Ce siège ne résume pas la gravité. La longueur de la verge, la courbure, la taille du gland et la qualité du plateau urétral comptent aussi, et l’aspect peut être reclassé après libération de la peau. [S1]</p>
<p>Le mégameatus à prépuce intact se voit seulement quand on rétracte le prépuce. Il ne se diagnostique donc pas toujours à la première inspection du nouveau-né. Ce n’est pas un phimosis. [S1]</p>
<p>L’hypospadias proximal avec deux testicules non palpables n’est pas « un petit hypospadias ». C’est une situation où le chapitre demande un bilan génétique et endocrinien rapide pour écarter une variation du développement sexuel, en particulier l’hyperplasie congénitale des surrénales. [S1]</p>
"""))
    P.append(ilot(DX, 2, "Épidémiologie (Suisse, puis Europe)", """
<p>Aucun taux OFS ou Obsan de l’hypospadias n’a été ouvert le 9 novembre 2026. On ne fabrique pas un chiffre cantonal. L’ancrage chiffré lu est européen. [S1]</p>
<p>EUROCAT, cité par l’EAU, donne 18,6 nouveaux cas pour 10 000 naissances de garçons en Europe, avec une fourchette de 5,1 à 36,8. Une revue élargie citée dans le même chapitre situe l’Europe à 19,9 pour 10 000, fourchette très large de 1 à 464, ce qui montre surtout l’hétérogénéité des registres. On retient l’ordre de grandeur d’environ 2 pour 1 000 naissances masculines, calcul dérivé de 18,6 pour 10 000, et l’on dit la fourchette. [S1]</p>
""" + w("dx4-p2-famille",
"Le risque familial est écrit en pourcentage de familles, pas en risque relatif inventé.",
"Un autre membre de la famille est atteint dans 7 à 12,9 % des familles, surtout dans les formes antérieures et moyennes.",
"Exemple : un frère déjà opéré augmente l’attention à la naissance, il ne change pas la classification anatomique. [S1]",
"Le piège est de rassurer parce que « personne dans la famille » : la plupart des cas sont sporadiques.",
"Source [S1].") + """
<p>Les facteurs associés lus sont le petit poids de naissance ou le retard de croissance intra-utérin, l’hypertension maternelle et la prééclampsie, probablement via le placenta, et le diabète avant ou pendant la grossesse. Le petit poids pourrait aussi augmenter le taux de réintervention dans les formes proximales. Les perturbateurs endocriniens sont discutés comme interaction avec la génétique, sans qu’un seuil d’exposition ne soit donné. [S1]</p>
<p>L’histoire naturelle sans opération est mal documentée. D’anciennes séries d’hommes non opérés, surtout distaux, décrivaient une miction et une sexualité satisfaisantes. Des études plus récentes décrivent un jet qui éclabousse, une obstruction, une courbure, une douleur coïtale et une insatisfaction. Plus de la moitié de ces hommes ont ensuite demandé une correction. [S1]</p>
"""))
    P.append(ilot(DX, 3, "Physiopathologie", """
<p>L’amorce est embryonnaire : la fermeture ventrale de l’urètre s’arrête trop tôt. Le développement laisse un méat ectopique, un plateau urétral, un prépuce dorsal et souvent un tissu fibreux ventral. L’installation clinique est visible à la naissance, sauf dans le mégameatus à prépuce intact. Le maintien est mécanique : la verge courbe au moment de l’érection, le jet part vers le bas, et la peau manque en ventral. [S1]</p>
<p>La courbure n’a pas une seule cause. Elle peut venir de la peau, du tissu conjonctif ventral, d’une charnière du plateau, ou d’une disproportion des corps caverneux. C’est pourquoi le chapitre corrige par étapes : déganter, exciser le tissu ventral, puis seulement ensuite raccourcir le dos ou allonger le ventre. [S1]</p>
""" + w("dx4-p3-30",
"Trente degrés est le seuil à partir duquel le chapitre juge en général la courbure à corriger.",
"On la mesure au bloc par un test d’érection, mieux avec un goniomètre ou une application qu’à l’œil.",
"Exemple : une coudure de 20 degrés après dégantage peut ne pas justifier une corporoplastie. Une coudure qui reste à 40 degrés, si. [S1]",
"Le piège est de promettre la rectitude avant d’avoir libéré la peau.",
"Source [S1].") + """
<p>La stratégie qui corrige n’est pas une hormone de routine. Le traitement hormonal préopératoire a des preuves non concluantes. Le chapitre le limite d’ordinaire aux formes proximales avec petite verge, gland de faible circonférence ou plateau étroit. Aucune dose, aucune spécialité et aucun schéma ne sont dans la page lue : on n’en écrit pas. La correction de fond est chirurgicale. [S1]</p>
""" + tableau([
("Lésion ou perturbation", "Exploration qui la montre", "Ce qui la corrige"),
("Le méat s’ouvre trop bas et le jet éclabousse.", "L’inspection à la naissance, ou après rétraction si le prépuce est fermé.", "Une urétroplastie qui ramène un méat glandulaire, quand l’indication fonctionnelle est là. [S1]"),
("La peau et le tissu ventral courbent la verge.", "Le test d’érection au bloc, après dégantage.", "L’excision du tissu ventral, puis une corporoplastie si 30 degrés ou plus persistent. [S1]"),
("Le plateau est trop étroit pour être tubulisé.", "L’inspection sous grossissement au bloc.", "Une incision médiane type TIP, parfois avec un greffon d’incrustation si l’incision est profonde. [S1]"),
("Deux testicules manquent et le méat est proximal.", "L’examen du scrotum et de l’aine à la naissance.", "Le bilan génétique et endocrinien rapide, avant toute chirurgie de conformation. [S1]"),
]) + """
"""))
    P.append(ilot(DX, 4, "Démarche diagnostique", """
<p>L’ordre commence par ce qui peut mettre en danger un nouveau-né, pas par l’esthétique du prépuce. Devant un hypospadias proximal et deux gonades non palpables, on écarte d’abord une hyperplasie congénitale des surrénales et les autres variations du développement sexuel. Le signe qui tranche est l’association méat proximal et gonades absentes. Le piège est d’annoncer « un garçon avec un hypospadias » et de programmer la chirurgie. La conduite est le bilan endocrinien et génétique sans délai, et le 144 si apparaissent vomissements, déshydratation ou malaise, parce que la perte de sel de l’hyperplasie n’est pas décrite en doses dans ce chapitre : on ne les invente pas. [S1]</p>
<p>Vient ensuite la sténose du méat, suspectée si l’urine goutte ou si l’urètre ballonne. Le piège est de la laisser jusqu’à l’âge de l’urétroplastie. On l’écarte tôt. [S1]</p>
<p>La courbure congénitale sans hypospadias et l’épispadias, méat dorsal, ne sont pas cette entité. Le chapitre de la courbure congénitale est distinct. On ne les opère pas avec le même plan sans avoir vu où s’ouvre le méat. [S1]</p>
<p>Le consensus du panel est de ne pas faire d’imagerie systématique à la recherche d’une malformation urinaire associée. On n’ajoute donc pas une échographie rénale « par principe » chez un hypospadias distal isolé. [S1]</p>
"""))
    P.append(ilot(DX, 5, "Anamnèse ciblée et drapeaux rouges", """
<p>On demande le poids de naissance et le terme, parce que le retard de croissance est associé à l’hypospadias et peut augmenter la réintervention des formes proximales. [S1]</p>
<p>On demande le diabète et l’hypertension de la grossesse, parce qu’ils figurent parmi les facteurs associés, via le placenta pour l’hypertension. [S1]</p>
<p>On demande si un frère, un père ou un cousin est atteint, parce que 7 à 12,9 % des familles ont un autre cas, surtout en distal et en moyen. [S1]</p>
<p>On demande comment l’enfant urine : jet unique, éclaboussure, goutte à goutte, ballonnement de l’urètre. Ces détails séparent une forme seulement cutanée d’une sténose ou d’un méat qui dévie le jet, lesquelles comptent parmi les indications opératoires. [S1]</p>
<p>On demande, chez l’adolescent non opéré, la douleur à l’érection, la gêne coïtale et le regard sur l’aspect. Les études récentes citées montrent que ces plaintes existent et que plus de la moitié des hommes concernés ont choisi l’opération. [S1]</p>
""" + w("dx4-p5-drapeau",
"Le drapeau rouge néonatal n’est pas le prépuce en capuchon.",
"C’est l’hypospadias proximal avec deux testicules non palpables, parce qu’il peut s’agir d’une fille virilisée par une hyperplasie des surrénales, exposée à une crise de perte de sel.",
"Exemple : nouveau-né étiqueté garçon, méat à la base, bourses vides. On n’attend pas six mois. [S1]",
"Le piège est un bilan « en ville la semaine prochaine ».",
"Source [S1].") + """
<p>Les drapeaux qui imposent une action immédiate sont donc cette association anatomique, et tout signe de malaise néonatal qui ferait appeler le 144. Une courbure isolée chez un nourrisson stable n’est pas une urgence de la nuit. [S1]</p>
"""))
    P.append(ilot(DX, 6, "Examen physique ciblé, région par région", """
<p>Le normal du nouveau-né est un méat au sommet du gland, un prépuce qui fait le tour, une verge droite au repos, et deux testicules dans le scrotum. On regarde cela avant de décrire l’anormal. [S1]</p>
<p>Région du méat. On note le siège : gland, verge distale, verge moyenne, pénoscrotal ou plus proximal. On regarde si l’urine, quand on la voit, sort en jet ou en gouttes, et si l’urètre se dilate. Le pathologique fonctionnel est le jet dévié, l’éclaboussure ou la sténose. [S1]</p>
<p>Région du prépuce et de la peau. Le pathologique classique est le capuchon dorsal, avec une face ventrale pauvre. On ne rétracte pas de force un prépuce serré chez un nouveau-né pour « classer » : le mégameatus, lui, ne se voit qu’après rétraction, ce qui se fait quand c’est possible sans déchirer. [S1]</p>
<p>Région de la verge. On décrit une courbure visible, sans prétendre la mesurer en degrés au lit : le chapitre mesure au bloc, par test d’érection, de préférence avec un outil plutôt qu’à l’œil. Trente degrés ou plus justifient en général une correction. [S1]</p>
<p>Région du scrotum et des gonades. On palpe les deux testicules. Deux absences plus un méat proximal changent le diagnostic de travail. Une transposition pénoscrotale se note, parce qu’elle figure parmi les indications possibles de correction. [S1]</p>
"""))
    P.append(ilot(DX, 7, "Approche syndromique", """
<p><em>7.1 Forme distale</em></p>
<p>Le signe fonctionnel peut être discret : un jet un peu ventral, ou aucun symptôme. Le signe physique est un méat glandulaire ou distal, un capuchon, une courbure souvent modeste. Le geste est l’inspection. Le mécanisme est un défaut de fermeture limité à l’extrémité. Le succès des réparations primaires distales est cité entre 85 et 90 %. [S1]</p>
<p><em>7.2 Forme proximale</em></p>
<p>Le signe fonctionnel est plus souvent un jet très dévié. Le signe physique est un méat postérieur, une courbure forte, parfois une transposition. Le mécanisme ajoute le tissu ventral et parfois une disproportion des corps. Les complications vont de 14 à 68 % selon les séries citées. [S1]</p>
<p><em>7.3 Forme associée à une variation du développement sexuel</em></p>
<p>Le signe fonctionnel néonatal peut être un malaise, qui n’appartient pas à l’hypospadias isolé. Le signe physique est le couple méat proximal et gonades non palpables. Le mécanisme peut être une virilisation d’un fœtus 46,XX ou un autre trouble, que le chapitre demande d’écarter par la biologie et la génétique, sans donner ici les seuils hormonaux. [S1]</p>
"""))
    P.append(ilot(DX, 8, "Diagnostic positif et critères", """
<p>Le diagnostic positif est clinique, à la naissance dans la grande majorité des cas. Il suffit de voir un méat ventral. Il ne suffit pas d’un prépuce incomplet si le méat est au sommet, ni d’une courbure si le méat est normal : ce sont alors d’autres entités. L’année et la société sont celles du chapitre EAU relu le 9 novembre 2026. Il n’y a pas de score majeur et mineur. [S1]</p>
<p>La sévérité, elle, ne se fige pas sur le seul siège. Après libération cutanée, on reclasse. Au bloc, une courbure de 30 degrés ou plus devient un critère de correction. Une indication opératoire reconnue est un méat proximal qui dévie ou éclabousse, une sténose, une courbure ventrale, un capuchon, ou une transposition pénoscrotale. L’esthétique seule se discute à part de la nécessité fonctionnelle. [S1]</p>
""" + w("dx4-p8-age",
"L’âge habituel de la réparation primaire est de 6 à 18 mois.",
"Avant, la verge est petite. Beaucoup plus tard, chez l’adulte, une étude prospective contrôlée a trouvé un taux de complications après TIP 2,5 fois plus haut que chez l’enfant. Chez l’enfant prépubère, l’âge n’était pas un facteur de complication du TIP.",
"Exemple : on ne repousse pas « à l’adolescence pour qu’il décide », si l’indication fonctionnelle est déjà claire, parce que la chirurgie adulte paie plus de complications dans cette étude. [S1]",
"Le piège est d’opérer un nouveau-né de trois semaines pour une forme distale mineure.",
"Source [S1].") + """
"""))
    P.append(ilot(DX, 9, "Examens complémentaires", """
<p><em>9.a Gold standard</em></p>
<p>Le gold standard du diagnostic est l’examen clinique. Il n’y a pas d’imagerie qui « confirme » un hypospadias distal. Le panel conseille même de ne pas imager systématiquement le haut appareil. [S1]</p>
<p><em>9.b 1<sup>re</sup> intention</em></p>
<p>L’examen de première intention, quand la forme est proximale et les deux gonades absentes, est le bilan génétique et endocrinien, fait tôt. La page ne liste ni le caryotype en cases ni le seuil de 17-hydroxyprogestérone. On écrit donc « bilan endocrinien et génétique pour écarter l’hyperplasie congénitale des surrénales », et l’on n’invente pas le chiffre qui tranche. [S1]</p>
<p>Au bloc, le test d’érection est l’examen qui mesure la courbure. Le terme juste est la courbure en degrés, pas une « verge tordue ». Trente degrés est le seuil lu. [S1]</p>
""" + tableau([
("Résultat possible", "Interprétation", "Hypothèse"),
("Méat au sommet, prépuce en capuchon seulement.", "Ce n’est pas un hypospadias au sens du méat ectopique.", "On ne planifie pas une urétroplastie sur ce seul aspect."),
("Méat distal, jet correct, pas de sténose, courbure absente.", "Forme mineure.", "La chirurgie peut être surtout de convenance, à discuter, pas une urgence. [S1]"),
("Méat proximal, jet qui éclabousse, courbure visible.", "Forme fonctionnellement significative.", "L’indication opératoire entre dans la liste du chapitre. [S1]"),
("Méat proximal et deux testicules non palpables.", "Le sexe et la surrénale ne sont pas réglés.", "On suspend la chirurgie de conformation et l’on fait le bilan néonatal. [S1]"),
("Au bloc, après dégantage, la courbure reste d’au moins 30 degrés.", "La peau ne suffisait pas à expliquer la coudure.", "Une corporoplastie est en général justifiée. [S1]"),
]) + """
<figure>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 360 180" role="img" aria-label="Schéma didactique d un méat ventral">
<rect width="360" height="180" fill="#fbfaf7"/>
<path d="M40 100 C120 40 240 40 320 100" fill="none" stroke="#6b4f32" stroke-width="8"/>
<circle cx="300" cy="112" r="10" fill="none" stroke="#9f1239" stroke-width="3" stroke-dasharray="3 2"/>
<text x="286" y="140" font-size="14" fill="#9f1239">1</text>
<text x="12" y="28" font-size="13">Schéma didactique, pas une photo clinique</text>
</svg>
<figcaption>Aucune photographie d’enfant n’a été embarquée le 9 novembre 2026.</figcaption>
<ol>
<li>Le cercle pointillé marque un méat ventral schématique, pour rappeler que le diagnostic se fait en voyant l’orifice, pas sur une image.</li>
</ol>
</figure>
<p><em>9.c Alternatives</em></p>
<p>Si le bilan endocrinien spécialisé n’est pas sur place, on transfert le nouveau-né à risque plutôt que d’attendre un résultat incomplet. L’échographie rénale n’est pas l’alternative recommandée en routine. Il n’y a pas de produit de contraste dans le parcours distal simple. [S1]</p>
<p><em>9.d 2<sup>e</sup> intention</em></p>
<p>Il n’y a pas d’examen de deuxième intention de routine. Le spermogramme ou l’IRM n’appartiennent pas au chapitre lu. On ne les ajoute pas pour faire nombre. [S1]</p>
"""))
    P.append(ilot(DX, 10, "Arbre décisionnel", """
<p>Si le nouveau-né a un méat proximal et deux gonades non palpables, alors bilan endocrinien et génétique immédiat, pas de chirurgie de forme.</p>
<p>Si l’urine goutte ou l’urètre ballonne, alors on cherche une sténose du méat sans attendre l’âge de l’urétroplastie.</p>
<p>Si la forme est distale, le jet correct, la verge droite et la famille informée, alors on peut ne pas opérer, ou discuter une correction surtout cutanée.</p>
<p>Si le méat dévie le jet, si une sténose, une courbure ou une transposition existe, alors on propose une réparation, en général entre 6 et 18 mois.</p>
<p>Si au bloc la courbure reste d’au moins 30 degrés après dégantage et excision du tissu ventral, alors on redresse les corps, de préférence en allongeant le ventre quand la coudure est sévère, parce que la récidive de courbure était de 5 % après allongement ventral contre 25 % après plicature dorsale dans les travaux cités. [S1]</p>
<p>Si le plateau doit être sectionné, alors on n’impose pas un TIP proximal : cette technique a montré 26 % de récidive de courbure ventrale. Les réparations en plusieurs temps sont devenues préférées dans beaucoup de formes sévères. [S1]</p>
"""))
    P.append(ilot(DX, 11, "Prise en charge selon les recommandations suisses", """
<p><em>11.A But</em></p>
<p>Le but est un méat glandulaire, une verge droite, une peau qui couvre, une miction en jet et, plus tard, une fonction sexuelle sans douleur. Le chapitre ne donne pas un score de satisfaction chiffré unique. Il donne des taux : 85 à 90 % de succès des réparations distales primaires, 14 à 68 % de complications dans les formes proximales. [S1]</p>
<p><em>11.B Moyens</em></p>
<p>Il n’y a pas de minute urgente hors le nouveau-né à risque de perte de sel, que l’on oriente tout de suite, 144 compris si le malaise est là. La forme isolée attend l’âge de 6 à 18 mois. [S1]</p>
""" + w("dx4-p11-bloc",
"Urgence seulement pour le nouveau-né ambigu ou en malaise. Le bloc de l’hypospadias isolé est programmé.",
"Au bloc : grossissement, fils résorbables fins 6-0 ou 7-0, bistouri bipolaire plutôt qu’une coagulation large. Test d’érection. Dégantage. Excision du tissu ventral. Mesure. Puis urétroplastie adaptée au plateau.",
"Exemple : plateau large, forme distale, courbure qui disparaît au dégantage. Un TIP est le choix habituel du chapitre pour le distal et le moyen. [S1]",
"Le piège est un TIP proximal « parce qu’on le maîtrise », malgré 26 % de récidive de courbure.",
"Source [S1].") + """
<p>L’urétroplastie conserve le plateau quand il est sain. S’il est large, on le tubulise. S’il est étroit, l’incision médiane du TIP, décrite par Snodgrass, est devenue le choix des formes distales et moyennes. Une incision profonde peut recevoir un greffon d’incrustation pour limiter la sténose. Si le plateau ne peut pas servir, les techniques en un temps existent, mais les réparations en plusieurs temps sont souvent préférées aujourd’hui, avec moins de récidive de courbure. [S1]</p>
<p>Sectionner le plateau sans le faire, dans une forme sévère, exposait à 20 % de récidive de courbure et 17 % de sténose. L’allongement ventral récidive moins que la plicature dorsale, 5 % contre 25 %, et la plicature raccourcit la verge, motif fréquent d’insatisfaction. On évite de poser en même temps un greffon de corps caverneux et un greffon urétral, selon les données croissantes citées. [S1]</p>
<p>Le prépuce peut être reconstruit s’il ne sert pas à l’urètre ni à couvrir le ventre, sans augmenter les fistules dans les données citées. La désunion du prépuce va de 7 à 17 %, le phimosis secondaire à 1,5 %. Dans les formes mineures, reconstruire seulement le prépuce peut cacher la malformation sans prendre le risque de l’urétroplastie. [S1]</p>
<p>Le drainage urinaire peut être une sonde qui goutte, un cathéter sus-pubien, ou rien après une forme distale. Ni le matériau de la sonde, ni le pansement, ni la durée n’ont de consensus fort. L’antibioprophylaxie n’a pas montré de baisse des infections du site ou des urines, surtout d’après des séries distales. On n’écrit donc pas une durée d’antibiotique. [S1]</p>
<p>L’analgésie par bloc caudal ou par bloc pénien est efficace dans les travaux cités, et le type de bloc n’a pas été lié aux complications de la réparation primaire. Le chapitre ne nomme aucun anesthésique, donc aucune notice n’est recopiée. [S1]</p>
<p>Le traitement hormonal préopératoire ne reçoit ni nom de marque ni dose. Preuves non concluantes, usage habituel limité au proximal avec petit gland ou plateau étroit. [S1]</p>
<p>Situations particulières. Le nouveau-né à gonades absentes : pas de chirurgie de forme avant le bilan. L’adulte : plus de complications après TIP dans l’étude citée, facteur 2,5. L’enfant prépubère : l’âge précis entre les bornes habituelles n’était pas un facteur de complication du TIP. Il n’y a pas de grossesse du patient. L’insuffisance rénale ou hépatique n’est pas discutée dans la page. [S1]</p>
<p><em>11.C Surveillance</em></p>
<p>Le suivi est long, fonctionnel et esthétique. On regarde le jet, la fistule, la sténose, la courbure qui revient, le prépuce s’il a été reconstruit. Le chapitre ne fixe pas un calendrier en mois. Il dit que le suivi au long cours est indispensable, surtout dans le proximal où les complications atteignent 14 à 68 %, et que l’expérience du chirurgien pèse. [S1]</p>
<p><em>11.D Pronostic</em></p>
<p>La « guérison » distale approche 85 à 90 % de succès primaire. Elle n’est pas un méat parfait garanti à vie : des plaintes adultes existent même sans opération, et la moitié et plus de ces hommes ont demandé une chirurgie. Le proximal reste le secteur incertain. Aucune piste médicamenteuse de 2026 n’est dans le chapitre. [S1]</p>
<p>Sortie après chirurgie programmée : l’enfant urine selon le mode choisi avec l’équipe, la famille sait reconnaître une rétention, un saignement ou une fièvre, et la date de contrôle est écrite. Le chapitre ne donne pas d’autres items chiffrés. [S1]</p>
"""))
    P.append(ilot(DX, 12, "Prévention", """
<p>Il n’existe pas, dans la page lue, de prévention primaire efficace à prescrire : pas de vitamine, pas de vaccin, pas de seuil de diabète gestationnel qui éviterait l’hypospadias. Le diabète et l’hypertension sont des associations, pas un programme de prévention chiffré. [S1]</p>
<p>La prévention secondaire est l’examen de tout nouveau-né : voir le méat, palper les deux testicules, ne pas manquer la forme qui exige un bilan de développement sexuel. [S1]</p>
<p>La prévention tertiaire est le choix technique qui limite fistule, sténose et courbure récidivante, et le suivi long. Le plan de vaccination suisse lu pour d’autres sujets ne contient pas de mesure visant l’hypospadias. [S1]</p>
"""))
    P.append(ilot(DX, 13, "Points clés", """
<p>Le diagnostic se voit : méat ventral. Le prépuce en capuchon ne suffit pas si le méat est normal.</p>
<p>Méat proximal et deux testicules absents : bilan endocrinien et génétique tout de suite, pas une chirurgie esthétique.</p>
<p>L’âge habituel de réparation est 6 à 18 mois, et le TIP de l’adulte s’est compliqué 2,5 fois plus dans l’étude citée.</p>
<p>Une courbure qui reste d’au moins 30 degrés après dégantage se corrige, de préférence sans raccourcir le dos si elle est sévère.</p>
<p>Le TIP est le choix courant du distal et du moyen, pas du proximal sévère, où il récidive la courbure dans 26 % des cas cités.</p>
<p>Les antibiotiques péri-opératoires n’ont pas montré de bénéfice clair, surtout dans les séries distales : on n’invente pas une durée.</p>
"""))
    P.append(ilot(DX, 14, "Pièges et questions fréquentes à l'examen fédéral suisse", """
<p>Question : 18,6 pour 10 000 signifie-t-il 18,6 % ? Réponse : non. C’est 18,6 naissances masculines atteintes pour 10 000, soit environ 0,186 %, calcul dérivé. [S1]</p>
<p>Question : faut-il une échographie rénale à tout hypospadias ? Réponse : non. Le consensus du panel est de ne pas imager systématiquement. [S1]</p>
<p>Question : à partir de quelle courbure corrige-t-on en général ? Réponse : 30 degrés ou plus, mesurés au mieux avec un outil pendant le test d’érection. [S1]</p>
<p>Question : pourquoi éviter la plicature dorsale dans une forte coudure ? Réponse : elle raccourcit la verge et la courbure revenait dans 25 % des cas contre 5 % après allongement ventral. [S1]</p>
<p>Question : le traitement hormonal préopératoire est-il standard ? Réponse : non. Les preuves sont non concluantes, et l’usage habituel vise le proximal avec petit gland ou plateau étroit, sans dose écrite ici. [S1]</p>
<p>Question : 85 à 90 % de succès concernent quelle forme ? Réponse : les réparations distales primaires, pas le proximal, dont les complications vont de 14 à 68 %. [S1]</p>
<p>Question : reconstruire le prépuce augmente-t-il les fistules ? Réponse : non dans les données citées, si le prépuce n’est pas nécessaire à l’urètre. La désunion propre du prépuce va de 7 à 17 %. [S1]</p>
<p>Question : l’antibioprophylaxie est-elle obligatoire ? Réponse : elle n’a pas réduit les infections du site ni les infections urinaires dans les preuves rassemblées, surtout distales. [S1]</p>
<p>Question : un homme adulte non opéré est-il toujours satisfait ? Réponse : non. Des études récentes décrivent l’éclaboussure, l’obstruction, la courbure et la douleur, et plus de la moitié ont demandé une correction. [S1]</p>
<p>Question : quelle dose de testostérone donne-t-on avant un hypospadias proximal ? Réponse : aucune dans cette monographie. Le chapitre ne donne pas de schéma, et les notices suisses lues n’ont pas cette indication. [S1]</p>
"""))
    P.append("""
<section class="ilot sources">
<h3>Sources</h3>
<p>[S1] Association européenne d’urologie, Guidelines on Paediatric Urology, chapitre « Hypospadias », texte en ligne consulté le 9 novembre 2026. https://uroweb.org/guidelines/paediatric-urology/chapter/hypospadias</p>
<p>La monographie de l’hypospadias repose sur cette page et reste non validé cliniquement.</p>
<p>Limite : pas de taux suisse ouvert le 9 novembre 2026. Pas de dose de testostérone, d’anesthésique ou d’antibiotique : le chapitre n’en nomme pas, et les notices de testostérone du corpus du 8.10.2026 n’indiquent pas l’hypospadias.</p>
</section>
""")
    html = "\n".join(P)
    from dx4_extra import extra
    from dx4_extra2 import extra2
    from dx4_extra3 import extra3
    from dx4_extra4 import extra4
    from dx4_extra5 import extra5
    from dx4_extra6 import extra6
    plus = extra()
    for src in (extra2(), extra3(), extra4(), extra5(), extra6()):
        for k, v in src.items():
            plus[k] = plus.get(k, "") + v
    for n, block in plus.items():
        start = html.find(f'id="dx{DX}-i{n}"')
        if start < 0:
            raise SystemExit(n)
        end = html.find("</section>", start)
        html = html[:end] + block + html[end:]
    return html

if __name__ == "__main__":
    from assembler import ecrire
    ecrire(4, "Hypospadias", body())
