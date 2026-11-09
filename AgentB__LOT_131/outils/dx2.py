# -*- coding: utf-8 -*-
"""DX.2 Varicocèle — texte rédigé, pas un gabarit."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from dx_lib import b, w, ilot, tableau

DX = 2

def body() -> str:
    from dx2_extra import extra
    from dx2_extra2 import extra2
    plus = extra()
    for k, v in extra2().items():
        plus[k] = plus.get(k, "") + v
    parts = []
    parts.append(ilot(DX, 1, "Définition et sémantique", f"""
<p>La {b('dx2-p1-def','varicocèle')} est, pour l’Association européenne d’urologie dans le chapitre pédiatrique relu le 9 novembre 2026, une dilatation anormale des veines testiculaires du plexus pampiniforme, produite par un reflux veineux. [S1]</p>
{w('dx2-p1-def',
'Le mot désigne donc un fait hémodynamique, et non une simple veine visible.',
'Le mécanisme commence par une valve ou un drainage incompétent, le sang redescend dans le plexus, la veine se dilate, et le scrotum devient plus chaud.',
'Exemple chiffré : chez l’adolescent, la forme clinique concerne 14 à 20 % des garçons, presque toujours à gauche. [S1]',
'Le piège est d’appeler varicocèle un reflux qui n’existe qu’à l’échographie : ce reflux isolé est une forme infraclinique, et il ne se traite pas comme un grade palpable. [S1]',
'Source [S1].')}
<p>Cette définition se distingue de l’hydrocèle, qui est une collection liquidienne de la vaginale, et de la torsion, qui est une ischémie aiguë du cordon. Elle se distingue aussi du varicocèle secondaire, dans lequel un obstacle rétro-péritonéal bloque le retour veineux. Le terme « sac de vers » décrit le signe, il ne remplace pas le diagnostic. [S1] [S2]</p>
<p>On réserve « varicocèle clinique » aux formes palpables ou visibles debout, et « varicocèle infraclinique » au reflux doppler sans veine palpable. Les grades I, II et III, au sens de l’EAU, classent seulement la forme clinique. [S1]</p>
"""))
    parts.append(ilot(DX, 2, "Épidémiologie (Suisse, puis Europe)", f"""
<p>La page suisse ouverte, la Revue Médicale Suisse de 2015, situe l’incidence dans la population générale autour de 15 %, surtout à gauche, et elle double chez les hommes infertiles. [S2]</p>
<p>Le chapitre européen, plus précis sur l’âge, dit que la varicocèle est rare avant dix ans, qu’elle apparaît au début de la puberté, et qu’elle touche 14 à 20 % des adolescents, avec une incidence semblable à l’âge adulte. Le côté gauche représente 78 à 93 % des cas. Le côté droit isolé est rare et s’observe d’ordinaire quand la forme est bilatérale. [S1]</p>
<p>Aucun registre OFS ou Obsan de la varicocèle n’a été ouvert le 9 novembre 2026 : la part suisse chiffrée reste donc celle de la revue romande, et non un taux national. La douleur est présente dans 2 à 10 % des varicocèles. Des problèmes de fertilité surviennent chez environ 20 % des adolescents qui en sont porteurs, et l’effet défavorable augmente avec le temps. [S1]</p>
{w('dx2-p2-age',
'La rareté avant dix ans change la conduite : une varicocèle prépubère n’est pas une variante banale de la puberté.',
'Le plexus se dilate quand la croissance et le débit testiculaire augmentent, par un mécanisme qui reste mal compris, avec une possible part génétique. [S1]',
'Exemple : un garçon de huit ans avec une bourse gauche pleine doit recevoir une échographie abdominale, parce que le chapitre demande cette recherche chez tout prépubère. [S1]',
'Le piège est de rassurer avec le chiffre de 14 à 20 %, qui ne s’applique pas avant la puberté.',
'Source [S1].')}
<p>L’enjeu de santé n’est pas la mortalité, qui n’est pas attribuée à la varicocèle dans les pages lues. L’enjeu est la fonction testiculaire future, le recours éventuel à une cure, et le fait qu’un dépistage pubertaire systématique suivi d’un traitement n’a pas un bénéfice démontré sur la paternité. [S1]</p>
"""))
    parts.append(ilot(DX, 3, "Physiopathologie", f"""
<p>L’amorce est anatomique. La veine spermatique interne gauche se jette dans la veine rénale gauche, alors que la droite rejoint en général la veine cave : ce trajet explique la forte prédominance gauche. Le développement suit l’accélération staturale et l’augmentation du flux testiculaire. L’installation se voit quand le reflux dilate le plexus. Le maintien vient de la chaleur, de la baisse des androgènes locaux et de l’accumulation de métabolites, qui ouvrent des voies d’apoptose. [S1] [S2]</p>
{w('dx2-p3-chaleur',
'La chaleur scrotale n’est pas une image : le testicule fonctionne plus bas que la température centrale.',
'Le reflux apporte du sang plus chaud que le scrotum, le parenchyme chauffe, les cellules germinales entrent en apoptose, le volume baisse, puis le spermogramme se dégrade chez l’adolescent plus âgé.',
'Exemple : une perte de volume gauche est trouvée chez 70 % des grades II et III. [S1]',
'Le piège est de croire que toute asymétrie pubertaire est déjà une lésion fixée : une croissance asynchrone peut être transitoire, d’où le contrôle à six mois. [S1]',
'Source [S1].')}
<p>Chez 70 % des patients de grade II ou III, le testicule gauche perd du volume. Des taux de FSH et de LH augmentés et une inhibine B diminuée ont été rapportés, en lien direct avec la sévérité. L’histologie est sévèrement altérée chez 20 % des adolescents atteints, et anormale chez 46 %. Ces lésions ressemblent à celles des hommes infertiles. [S1]</p>
<p>La Revue Médicale Suisse relie le même tableau à la stase, à l’hypoxie, à la température scrotale et au reflux de métabolites rénaux. Elle rappelle qu’un thrombus tumoral rénal gauche peut bloquer la veine spermatique et créer un varicocèle secondaire. [S2]</p>
{tableau([
('Lésion ou perturbation','Exploration qui la montre','Thérapeutique qui la corrige'),
('Le reflux dans le plexus pampiniforme dilate les veines.','Le Doppler, couché puis debout, avec Valsalva, objective le reflux.','La ligature ou l’occlusion des veines spermatiques internes interrompt le reflux. [S1]'),
('La chaleur et l’apoptose réduisent le volume testiculaire.','L’échographie ou l’orchidomètre chiffre une différence supérieure à 2 mL ou à 20 %.','On propose la cure si cette hypotrophie persiste sur deux examens espacés de six mois. [S1]'),
('La section des lymphatiques laisse filer le liquide et gonfle la vaginale.','L’hydrocèle postopératoire se voit à l’examen et à l’échographie.','La technique qui épargne les lymphatiques abaisse ce risque. [S1]'),
('Un obstacle rénal gauche retient le sang spermatique.','L’échographie abdominale cherche une masse rétro-péritonéale.','On traite la cause, et non le plexus, quand le varicocèle est secondaire. [S1] [S2]'),
])}
"""))
    parts.append(ilot(DX, 4, "Démarche diagnostique", f"""
<p>L’ordre est d’abord celui de la gravité, puis celui de la fréquence. On écarte le varicocèle secondaire et la douleur aiguë qui pourrait être une torsion, avant de classer la varicocèle pubertaire banale.</p>
<p>Le premier concurrent grave est la masse rétro-péritonéale, en particulier la tumeur rénale gauche dont le thrombus bloque la veine spermatique. Le signe qui tranche est le côté : tout varicocèle droit isolé, et toute forme chez un garçon prépubère, impose une échographie abdominale. Le piège est de programmer une cure veineuse sans avoir cherché l’obstacle. La conduite immédiate est l’imagerie abdominale, pas l’embolisation. [S1] [S2]</p>
<p>Le deuxième concurrent, quand la douleur est brutale, est la torsion du testicule. Le signe qui tranche est le temps : une douleur soudaine avec nausée n’est pas expliquée par une varicocèle, dont la gêne est plutôt vespérale et orthostatique. Le piège est de se rassurer parce qu’un varicocèle était déjà connu. La conduite est l’exploration urgente si la torsion reste plausible, selon le chapitre de la bourse aiguë, sans attendre un spermogramme. [S1] [S2]</p>
<p>Viennent ensuite les autres tuméfactions que la revue romande place à côté de la varicocèle, notamment l’hydrocèle et la spermatocèle, sans que la page ouverte ne détaille leur signe distinctif au-delà du sac de vers propre au plexus. L’orchi-épididymite fait partie de la même liste de diagnostics fréquents de bourse. Le piège commun est de ranger une douleur aiguë dans la gêne veineuse du soir. [S2]</p>
{w('dx2-p4-secondaire',
'Le varicocèle secondaire n’a pas le même âge ni le même côté que la forme pubertaire.',
'Une masse ou un thrombus de la veine rénale gauche comprime l’abouchement de la veine spermatique, le plexus gonfle, parfois rapidement, parfois à droite si l’obstacle est cave.',
'Exemple : la revue romande demande de chercher une tumeur rénale gauche devant ce drainage. [S2] L’EAU étend la règle à tout prépubère et à tout côté droit isolé. [S1]',
'Le piège d’examen est de citer le chiffre de 15 % pour un enfant de sept ans ou pour un côté droit seul.',
'Source [S1] [S2].')}
"""))
    parts.append(ilot(DX, 5, "Anamnèse ciblée et drapeaux rouges", f"""
<p>On demande l’âge des premiers signes, parce qu’une apparition avant dix ans sort de l’histoire naturelle pubertaire et déclenche la recherche d’un obstacle. [S1]</p>
<p>On demande le côté et si la bourse controlatérale est aussi pleine, parce qu’un côté droit isolé n’est presque jamais une forme primitive. [S1]</p>
<p>On demande si la gêne augmente le soir et debout, puis cède allongé, parce que ce rythme suit le reflux et distingue la varicocèle d’une douleur inflammatoire continue. [S2]</p>
<p>On demande une douleur brutale, des vomissements ou un traumatisme récent, parce que ces éléments font chercher une torsion ou un hématome avant toute discussion de fertilité. [S1]</p>
<p>On demande une lourdeur, une gêne esthétique et, chez l’adolescent plus âgé qui le peut, un projet de fertilité, parce que la douleur ne concerne que 2 à 10 % des porteurs et parce que le spermogramme n’est pertinent que plus tard. [S1]</p>
{w('dx2-p5-douleur',
'La douleur de varicocèle est un argument faible, pas une urgence en soi.',
'Le reflux maximal debout distend le plexus, la lourdeur vient le soir, et elle peut manquer complètement.',
'Exemple chiffré : la douleur persiste après cure dans 20 % des cas douloureux, donc la promesse de guérison antalgique est fausse une fois sur cinq dans les séries citées. [S1]',
'Le piège est d’opérer seulement pour une gêne vague sans avoir dit ce chiffre.',
'Source [S1].')}
<p>Les drapeaux qui imposent un geste le jour même sont le malaise aigu de la bourse, qui oriente vers le 144 et l’urologie d’urgence, et le varicocèle prépubère ou droit isolé, qui impose l’échographie abdominale avant tout geste veineux. Une asymétrie de volume ne se décide pas sur une seule mesure. [S1]</p>
"""))
    parts.append(ilot(DX, 6, "Examen physique ciblé, région par région", f"""
<p>On examine d’abord debout, parce que le diagnostic clinique dépend de cette position et que le plexus se vide souvent allongé. Le normal, avant la puberté, est un cordon sans veine palpable au Valsalva, et deux testicules de volume proche. [S1] [S2]</p>
<p>Région inguinal et cordon. Le normal est l’absence de turgescence à la toux. Le pathologique est un cordon qui s’épaissit au Valsalva. On pose les doigts sur le cordon, on demande une poussée abdominale, et on sent l’impulsion veineuse. Ce signe sépare le grade I, palpable seulement au Valsalva, du grade II, palpable sans Valsalva. [S1]</p>
<p>Région scrotale. Le normal est une peau souple et un testicule lisse dont le volume se compare au côté opposé, à l’orchidomètre ou plus tard à l’échographie. Le pathologique du grade III se voit à distance, sans palper. Le sac de vers siège en postéro-supérieur, roule sous les doigts, et diminue ou disparaît allongé. [S1] [S2]</p>
{w('dx2-p6-grades',
'Les trois grades de l’EAU sont cliniques, pas doppler.',
'Grade I : la veine n’existe sous le doigt que pendant le Valsalva. Grade II : elle est palpable au repos, debout. Grade III : elle se voit.',
'Exemple : un reflux doppler sans rien à la palpation n’est pas un grade I, c’est une forme infraclinique. [S1]',
'Le piège est de grader un patient couché, quand le plexus s’est vidé.',
'Source [S1].')}
<p>La valeur du signe est qualitative dans les pages lues : la recommandation de classer debout en trois grades est forte, mais aucune sensibilité chiffrée de la palpation n’y est donnée. Le piège d’interprétation est de prendre une croissance pubertaire décalée pour une hypotrophie définitive. Une différence supérieure à 2 mL ou à 20 % ne compte comme hypotrophie qu’après un second contrôle six mois plus tard. [S1]</p>
<p>Calcul dérivé, pour fixer la règle : si le testicule droit mesure 12 mL et le gauche 8 mL, la différence est de 4 mL, donc supérieure à 2 mL, et 4 divisé par 12 égale 0,33, soit 33 %, donc supérieur à 20 %. Les deux seuils sont franchis. On ne propose pas encore la chirurgie : on revérifie six mois plus tard. [S1]</p>
"""))
    parts.append(ilot(DX, 7, "Approche syndromique", f"""
<p><em>7.1 Syndrome de reflux pampiniforme</em></p>
<p>Les signes fonctionnels sont la lourdeur vespérale, la gêne debout et, rarement, une douleur vraie. Chaque terme désigne une sensation, pas une lésion : la lourdeur est un poids sans défense, la douleur est une souffrance qui peut manquer. On les recherche par l’horaire et par la position. Leur mécanisme est la distension veineuse quand la colonne hydrostatique est maximale. [S1] [S2]</p>
<p>Les signes physiques sont le sac de vers, l’impulsion au Valsalva et la diminution en décubitus. Le sac de vers est un amas de veines tortueuses que l’on fait rouler. On le cherche debout, en arrière et au-dessus du testicule. Le mécanisme est la dilatation du plexus par le reflux. [S2]</p>
{w('dx2-p7-sac',
'Le sac de vers est un signe, pas une maladie séparée.',
'Les veines du plexus se remplissent, deviennent tortueuses, et donnent sous les doigts la sensation de vers dans un sac.',
'Exemple : le signe s’efface souvent allongé, ce qui manque dans une tumeur solide. [S2]',
'Le piège est de transilluminer et de conclure à une hydrocèle alors que les veines roulent encore.',
'Source [S2].')}
<p><em>7.2 Syndrome d’hypotrophie testiculaire</em></p>
<p>Le signe fonctionnel peut manquer : l’adolescent ne sent pas toujours le volume perdu. Le signe physique est un testicule gauche plus petit, mou ou non, comparé au droit. On le mesure, on ne se fie pas au coup d'œil. Le mécanisme est l’apoptose liée à la chaleur, au déficit androgénique local et aux toxiques refluxés. Une différence supérieure à 2 mL ou à 20 %, confirmée, relie ce syndrome à l’offre de chirurgie. [S1]</p>
<p><em>7.3 Syndrome de varicocèle secondaire</em></p>
<p>Le signe fonctionnel peut être une apparition rapide, hors puberté, ou à droite. Le signe physique est le même plexus dilaté, parfois sans le profil gauche classique. On palpe l’abdomen et on demande l’échographie rénale. Le mécanisme est l’obstacle sur la veine de drainage, pas l’incompétence primitive. [S1] [S2]</p>
"""))
    parts.append(ilot(DX, 8, "Diagnostic positif et critères", f"""
<p>Le diagnostic positif d’une varicocèle clinique, selon l’EAU dans le chapitre relu, repose sur l’examen debout : un paquet veineux tortueux, plus net au Valsalva, classé en trois grades. Cette recommandation est forte. L’échographie scrotale est recommandée avec une force égale pour le volume et pour le reflux, couché, debout et au Valsalva. Elle ne remplace pas la palpation pour décider qu’il existe une forme clinique. [S1]</p>
{w('dx2-p8-critere',
'Il suffit, pour nommer la maladie clinique, de palper ou de voir le plexus debout.',
'Il ne suffit pas d’un reflux doppler isolé, ni d’une seule mesure de volume, ni d’un spermogramme chez l’enfant.',
'Exemple : grade III visible, volumes encore égaux : le diagnostic de varicocèle est posé, l’indication opératoire ne l’est pas. [S1]',
'Le piège d’examen est de confondre le diagnostic et l’indication.',
'Source [S1].')}
<p>Ce qui ne suffit pas : un reflux seulement échographique, qui définit la forme infraclinique ; une asymétrie vue une seule fois, parce que la croissance pubertaire peut être décalée ; un spermogramme chez le prépubère, parce que les paramètres de l’OMS ne sont pas faits pour cet âge, que des améliorations spontanées ont été observées, et que des barrières culturelles existent. Le spermogramme n’est en général proposé qu’à l’adolescent plus âgé. [S1]</p>
<p>L’indication opératoire forte est séparée du diagnostic. On informe et on offre la chirurgie quand un testicule reste plus petit de plus de 2 mL ou de 20 % sur deux visites espacées de six mois. Les autres situations, douleur, testicule controlatéral déjà compromis, forme bilatérale palpable, sperme pathologique chez l’adolescent plus âgé, gêne esthétique, sont des considérations au cas par cas, de force faible. [S1]</p>
<p>La classification de Dubin et Amelar est citée par la Revue Médicale Suisse de 2015, mais le tableau des stades n’était pas lisible dans la page ouverte. On n’invente donc pas une correspondance chiffrée au-delà des trois grades explicitement écrits par l’EAU. [S2] [S1]</p>
"""))
    parts.append(ilot(DX, 9, "Examens complémentaires", f"""
<p><em>9.a Gold standard</em></p>
<p>Le gold standard de la forme clinique est l’examen debout en trois grades. Il est clinique, et le chapitre le place avant l’image. Aucune sensibilité numérique de cette palpation n’est donnée dans la page lue. [S1]</p>
<p><em>9.b 1<sup>re</sup> intention</em></p>
<p>L’examen de première intention qui complète la clinique est l’échographie scrotale avec Doppler. On la prescrit pour mesurer les deux volumes et pour chercher le reflux couché, debout et pendant le Valsalva. On ajoute une échographie abdominale, le jour de la consultation, chez tout prépubère et devant tout côté droit isolé. [S1]</p>
<p>L’image utile est décrite avec les termes de la modalité. La revue romande parle d’images {b('dx2-p9-hypo','hypoéchogènes')} rétro-testiculaires et intrafuniculaires, dont le diamètre augmente au Valsalva, et d’un Doppler qui objective le reflux. [S2]</p>
{w('dx2-p9-hypo',
'Hypoéchogène signifie que la zone renvoie moins d’ultrasons que le tissu de référence, ici souvent le parenchyme voisin.',
'Les veines dilatées, remplies de sang lent, apparaissent sombres derrière et au-dessus du testicule, puis s’élargissent quand la pression abdominale pousse le reflux.',
'Exemple : le diamètre augmente au Valsalva ; la page lue ne fixe pas un seuil millimétrique unique, donc on n’en invente pas. [S2]',
'Le piège est d’écrire « tache » ou « anomalie » sans dire hypoéchogène ni reflux.',
'Source [S2].')}
<figure>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 360 210" role="img" aria-label="Schéma didactique d’une varicocèle gauche">
<rect width="360" height="210" fill="#fbfaf7"/>
<ellipse cx="210" cy="120" rx="46" ry="62" fill="#f3e6d4" stroke="#6b4f32" stroke-width="2"/>
<text x="198" y="124" font-size="14" fill="#3b2a1a">2</text>
<ellipse cx="168" cy="78" rx="38" ry="22" fill="none" stroke="#b45309" stroke-width="3" stroke-dasharray="5 4"/>
<text x="150" y="70" font-size="14" fill="#9a3412">1</text>
<path d="M168 78 C150 40 120 30 100 48" fill="none" stroke="#9a3412" stroke-width="3"/>
<text x="16" y="28" font-size="13" fill="#3b2a1a">Schéma didactique, pas une échographie de patient</text>
</svg>
<figcaption>Le dessin est original et didactique. Aucune photographie clinique libre n’a été retenue ni embarquée le 9 novembre 2026.</figcaption>
<ol>
<li>Le contour pointillé marque les veines du plexus, en situation rétro-testiculaire, là où l’image hypoéchogène et le reflux sont cherchés.</li>
<li>Le testicule est dessiné pour rappeler la comparaison de volume, sans prétendre représenter une coupe réelle.</li>
</ol>
</figure>
{tableau([
('Résultat possible','Interprétation','Hypothèse'),
('La palpation debout est normale et le Doppler montre un reflux.','La forme est infraclinique.','On ne pose pas d’indication opératoire sur cette seule image. [S1]'),
('Le grade est II ou III et le volume gauche reste inférieur de plus de 2 mL ou de 20 % à six mois.','L’hypotrophie est persistante.','On informe et on offre la chirurgie. [S1]'),
('Le volume diffère aujourd hui, mais une seule mesure existe.','La croissance peut être simplement décalée.','On revoit à six mois avant de décider. [S1]'),
('Le côté droit est isolé, ou le garçon est prépubère.','Le reflux peut être bloqué par une masse.','L’hypothèse prioritaire est le varicocèle secondaire, et l’échographie abdominale vient tout de suite. [S1] [S2]'),
('La douleur scrotale est brutale, avec nausée, et non une lourdeur du soir.','Ce récit ne correspond pas à l’histoire naturelle lue pour la varicocèle.','On suspend le bilan de fertilité et on oriente vers une prise en charge de bourse aiguë. [S1] [S2]'),
])}
<p><em>9.c’Alternatives</em></p>
<p>Si l’échographie scrotale n’est pas disponible, l’orchidomètre estime encore le volume, et l’examen debout reste le diagnostic. Cette substitution ne dispense pas de l’échographie abdominale quand le côté ou l’âge l’exigent. Aucune adaptation propre à la grossesse n’existe ici, le sujet étant un garçon ou un homme. Chez l’insuffisant rénal, le chapitre lu ne modifie pas l’écho-Doppler scrotal. L’allergie à l’iode et l’IRM ne concernent pas cet examen de première intention. [S1]</p>
<p><em>9.d 2<sup>e</sup> intention</em></p>
<p>Le spermogramme est un examen de deuxième temps, réservé à l’adolescent plus âgé. Le test de stimulation à la LHRH, avec une réponse supranormale de FSH et de LH, a été utilisé comme marqueur de souffrance, parce que des lésions histologiques ont été trouvées chez ces patients. La page lue ne donne ni le protocole de stimulation ni un seuil chiffré de FSH : on ne les invente pas. On passe à ces tests quand la décision de fertilité ne peut plus reposer sur le seul volume, pas chez le prépubère. [S1]</p>
{w('dx2-p9-lhrh',
'La LHRH, ou GnRH, libère LH et FSH quand l’hypophyse est sollicitée.',
'Si le testicule répond mal, la rétrocontrôle lâche, et la réponse hypophysaire devient excessive.',
'Exemple : le chapitre qualifie cette réponse supranormale de fiable pour dépister une atteinte, sans publier dans le passage lu le pic en UI/L. [S1]',
'Le piège est de traiter un enfant sur un dosage unique de FSH fait au hasard de la journée.',
'Source [S1].')}
"""))
    parts.append(ilot(DX, 10, "Arbre décisionnel", f"""
<p>Si la douleur est brutale, avec nausée ou vomissement, alors on sort de cet arbre et on traite comme une bourse aiguë, jusqu’à preuve contraire de torsion.</p>
<p>Si le garçon est prépubère ou si le varicocèle est droit et isolé, alors on fait une échographie abdominale avant toute ligature.</p>
<p>Si l’examen debout est normal, alors on ne traite pas un reflux seulement doppler.</p>
<p>Si la varicocèle est clinique et que la différence de volume dépasse 2 mL ou 20 % sur deux visites à six mois d’intervalle, alors on informe et on offre une cure qui épargne les lymphatiques, sous grossissement optique.</p>
<p>Si le volume est conservé, alors on discute au cas par cas la douleur, la bilatéralité palpable, un testicule controlatéral déjà lésé, un sperme pathologique chez l’adolescent plus âgé, ou la gêne esthétique. Sinon on surveille jusqu’à un spermogramme interprétable. [S1]</p>
{w('dx2-p10-arbre',
'Chaque flèche de cet arbre correspond à une phrase du chapitre, pas à une préférence locale.',
'La chirurgie précoce n’a pas montré un meilleur résultat andrologique qu’une chirurgie plus tardive : le diagnostic précoce n’accélère donc pas, à lui seul, l’indication. [S1]',
'Exemple : grade III, volumes égaux, aucune douleur : la surveillance est cohérente avec le texte.',
'Le piège est d’opérer tout grade III le jour du diagnostic.',
'Source [S1].')}
"""))
    parts.append(ilot(DX, 11, "Prise en charge selon les recommandations suisses", f"""
<p><em>11.A But</em></p>
<p>Le but, quand on opère, est de faire disparaître le reflux clinique, de laisser le testicule rattraper du volume et, chez l’adolescent plus âgé, d’améliorer la concentration spermatique. La méta-analyse citée par l’EAU trouve une différence moyenne de volume de 1,52 mL (intervalle de confiance à 95 % : 0,73 à 2,31) et une différence moyenne de concentration spermatique de 25,54 (intervalle de confiance à 95 % : 12,84 à 38,25) en faveur du traitement contre l’observation. L’unité exacte de cette concentration n’est pas réécrite dans le paragraphe lu : on ne la devine pas. Le but n’est pas une paternité garantie : l’effet ultime sur la paternité reste inconnu, et traiter plus tôt n’a pas montré de meilleur résultat andrologique qu’opérer plus tard. [S1]</p>
<p><em>11.B Moyens</em></p>
<p>Il n’y a pas de minute urgente propre à la varicocèle non compliquée. La gêne simple attend la consultation. L’urgence chronologique concerne deux situations voisines : la douleur scrotale brutale, que l’on oriente vers le 144 sans perdre de temps en spermogramme, et le varicocèle prépubère ou droit isolé, dont l’échographie abdominale précède tout geste sur la veine.</p>
{w('dx2-p11-urgence',
'Urgence, conduite chronologique, quand la bourse devient aiguë chez un porteur de varicocèle.',
'À la première minute, on croit à la torsion tant que le temps et l’examen ne l’ont pas écartée. Dans l’heure, on joint l’urologie et, si le garçon est loin d’un bloc, le 144. On ne demande pas un spermogramme. On n’attend pas six mois.',
'Exemple : une douleur apparue depuis trois heures avec vomissement ne se range pas dans les 2 à 10 % de douleurs de varicocèle. [S1]',
'Le piège est de donner un anti-inflammatoire et un rendez-vous électif.',
'Source [S1]. Aucune dose antalgique n’est écrite ici, parce que l’information professionnelle suisse correspondante n’a pas été relue le 9 novembre 2026.')}
<p>L’ordre électif est le suivant. On confirme le grade debout. On mesure les volumes. On écarte la forme secondaire. On n’opère pas sur une asymétrie unique. Si l’indication forte est là, on choisit une ligature des veines spermatiques internes avec un grossissement, microscope ou cœlioscopie, parce que l’artère spermatique interne ne mesure qu’environ 0,5 mm à l’anneau inguinal. On épargne les lymphatiques. [S1]</p>
<p>Deux familles techniques existent. La ligature inguinale ou sous-inguinale microchirurgicale est moins invasive dans son abord, mais elle rencontre davantage de veines. La ligature supra-inguinale, ouverte ou cœlioscopique, lie moins de veines, et la section accidentelle de l’artère à cet étage n’apporte pas d’avantage démontré sur le rattrapage ; l’épargne artérielle supra-inguinale s’associe même à plus de récidives. Aucune technique n’est supérieure pour le succès dans la méta-analyse : l’odds ratio entre chirurgie ouverte et cœlioscopie allait de 0,13 à 2,84. Le succès, défini par la disparition du varicocèle, allait de 85,1 % à 100 %, et les complications de 0 % à 29 %, l’hydrocèle étant la plus citée. [S1]</p>
{w('dx2-p11-lymph',
'Les lymphatiques testiculaires remontent avec les veines. Si on les lie, la lymphe stagne.',
'La vaginale se remplit, l’hydrocèle apparaît, et le testicule peut gonfler par œdème, ce qui fausse le rattrapage de croissance.',
'Exemple : la section lymphatique mène à une hydrocèle dans jusqu à 40 % des cas. L’épargne lymphatique abaisse ce risque, avec un odds ratio de 0,08 (intervalle de confiance à 95 % : 0,01 à 0,67) et une valeur p de 0,02. [S1]',
'Le piège est de prendre cet œdème pour une preuve que le testicule a repoussé.',
'Source [S1].')}
<p>L’occlusion radiologique, par sclérose rétrograde ou antérograde, épargne aussi les lymphatiques et peut éviter une anesthésie générale. Son coût est l’irradiation, moins maîtrisable dans la technique antérograde. Le rattrapage moyen de croissance après cure, dans une méta-analyse, est de 76,4 %, avec une fourchette de 52,6 % à 93,8 %, en partie attribuable à l'œdème si les lymphatiques ont été coupés. La douleur disparaît dans plus de 90 % des séries rapportées, mais le chapitre dit par ailleurs qu’elle peut persister dans 20 % des cas : ces deux phrases ne décrivent pas la même sélection de patients, et on les cite toutes les deux plutôt que d’en effacer une. [S1]</p>
<p>Aucun médicament de fond n’est recommandé dans le chapitre relu. Le corpus AIPS local du 8 octobre 2026 n’était pas présent dans l’environnement, et aucune spécialité veino-active n’a été relue sur swissmedicinfo pour cette indication. On n’écrit donc ni nom commercial, ni numéro d’autorisation, ni dose. La cure est mécanique. [S1]</p>
<p>Situations particulières. Il n’y a pas de grossesse chez le patient. Le prépubère n’est pas opéré selon le schéma de l’adolescent : on cherche d’abord la masse. L’insuffisance rénale ou hépatique ne modifie pas, dans la page lue, le choix entre ligature et surveillance. L’enfant très jeune relève de l’arbre du varicocèle secondaire. [S1]</p>
<p>Le versant social est la compréhension de la famille : on dit que la plupart des adolescents porteurs ne deviendront pas infertiles, puisque des problèmes de fertilité sont attendus chez environ 20 %, et que la paternité après cure n’est pas un résultat acquis. L’arrêt de travail ou de sport dépend du geste choisi ; la page lue ne fixe pas un nombre de jours. L’aptitude scolaire n’est pas en cause. [S1]</p>
<p><em>11.C Surveillance</em></p>
<p>Sans indication forte, on revoit le volume jusqu’à pouvoir interpréter un spermogramme. Avec une asymétrie limite, le prochain point est fixé à six mois, pas avant, pour ne pas confondre un décalage de puberté et une perte vraie. Après cure, on cherche la disparition clinique, l’hydrocèle et le volume. Une récidive ne se réopère que si elle est clinique et que l’asymétrie ne s’améliore pas, ou que les symptômes restent. On choisit alors une autre technique, pour travailler en terrain non ouvert. La cause habituelle de récidive est une veine branchée laissée en place. [S1]</p>
<p><em>11.D Pronostic</em></p>
<p>La varicocèle clinique peut régresser comme signe après une cure réussie, dans la fourchette de succès de 85,1 % à 100 % des études incluses. La guérison de la fertilité n’a pas de critère définitif dans le chapitre : le volume et la concentration spermatique s’améliorent à un niveau de preuve modéré, la paternité reste un résultat inconnu à long terme. Une étude de cure microchirurgicale chez l’adolescent a rapporté plus de paternités et un délai de conception plus court, mais le panel demande une confirmation. [S1]</p>
"""))
    parts.append(ilot(DX, 12, "Prévention", f"""
<p>La prévention primaire d’un reflux primitif n’existe pas dans les pages lues : ni vaccin, ni médicament, ni geste scolaire n’empêche la varicocèle pubertaire. Le dépistage systématique à la puberté, suivi d’un traitement, a un effet controversé sur la fertilité et sur la chance finale de paternité. On ne transforme donc pas chaque visite de contrôle en campagne de chirurgie. [S1]</p>
<p>La prévention secondaire consiste à ne pas manquer la forme secondaire et à ne pas laisser passer une hypotrophie confirmée. Le geste concret est l’examen debout des deux bourses à la visite du médecin de l’adolescent, puis l’échographie abdominale si l’âge ou le côté sort de l’ordinaire. [S1] [S2]</p>
<p>La prévention tertiaire est l’épargne lymphatique, qui évite l’hydrocèle, et l’information sur la persistance possible de la douleur. Aucune recommandation OFSP spécifique à la varicocèle n’a été ouverte le 9 novembre 2026. [S1]</p>
"""))
    parts.append(ilot(DX, 13, "Points clés", f"""
<p>La varicocèle clinique se diagnostique debout, et le reflux seulement doppler ne suffit pas à l’opérer.</p>
<p>Avant dix ans, ou à droite seule, on cherche une masse abdominale avant de lier une veine.</p>
<p>On n’offre la chirurgie pour hypotrophie que si la différence dépasse 2 mL ou 20 % sur deux visites espacées de six mois.</p>
<p>La cure utilise un grossissement et épargne les lymphatiques, parce que leur section provoque une hydrocèle dans jusqu’à 40 % des cas.</p>
<p>Traiter plus tôt n’a pas prouvé un meilleur avenir andrologique qu’opérer plus tard, et la paternité reste un résultat non démontré.</p>
<p>Une douleur scrotale brutale chez un porteur connu se gère comme une torsion possible, et non comme une gêne veineuse.</p>
"""))
    parts.append(ilot(DX, 14, "Pièges et questions fréquentes à l’examen fédéral suisse", f"""
<p>Question : un reflux doppler sans veine palpable chez un adolescent de quatorze ans impose-t-il une cure ? Réponse : non, c’est une forme infraclinique, et l’indication ne repose pas sur elle. [S1]</p>
<p>Question : une différence de 4 mL, soit 33 % si l’autre testicule fait 12 mL, vue aujourd’hui pour la première fois, est-elle une indication forte ? Réponse : pas encore, il faut la confirmer six mois plus tard. [S1]</p>
<p>Question : pourquoi le côté gauche domine-t-il ? Réponse : la veine spermatique gauche se jette dans la veine rénale, et ce trajet rend le reflux plus fréquent. [S1] [S2]</p>
<p>Question : un garçon de huit ans a un plexus gauche dilaté. Quelle est la prochaine étape ? Réponse : l’échographie abdominale, parce qu’il est prépubère. [S1]</p>
<p>Question : la douleur garantit-elle le bénéfice de la chirurgie ? Réponse : non, elle peut persister dans 20 % des cas, et elle n’est présente au départ que dans 2 à 10 % des varicocèles. [S1]</p>
<p>Question : quelle technique a prouvé sa supériorité sur les autres ? Réponse : aucune, dans la méta-analyse du panel. Ce qui est recommandé fort, c’est le grossissement optique et l’épargne lymphatique. [S1]</p>
<p>Question : le rattrapage de volume prouve-t-il à lui seul que le parenchyme a repoussé ? Réponse : non, une partie du gonflement peut être un œdème après section des lymphatiques. [S1]</p>
<p>Question : faut-il un spermogramme à onze ans ? Réponse : non, les paramètres de l’OMS ne visent pas le prépubère, et l’examen est en général réservé à l’adolescent plus âgé. [S1]</p>
<p>Question : un anti-inflammatoire règle-t-il une bourse douloureuse depuis deux heures ? Réponse : non, on écarte d’abord la torsion. Aucune dose n’est citée, faute d’information professionnelle suisse relue.</p>
<p>Question : la Revue Médicale Suisse et l’EAU donnent-elles le même ordre de grandeur ? Réponse : oui pour la fréquence, autour de 15 % d’un côté et 14 à 20 % de l’autre, avec un doublement chez les infertiles dans la revue romande. [S1] [S2]</p>
"""))
    parts.append(f"""
<section class="ilot sources">
<h3>Sources</h3>
<p>[S1] Association européenne d’urologie, Guidelines on Paediatric Urology, chapitre « Varicocele in children and adolescents », texte en ligne consulté le 9 novembre 2026. https://uroweb.org/guidelines/paediatric-urology/chapter/varicocele-in-children-and-adolescents</p>
<p>[S2] Revue Médicale Suisse 2015, numéro 497, « Douleurs et tuméfactions scrotales : prise en charge initiale diagnostique et thérapeutique par le généraliste », page consultée le 9 novembre 2026. https://www.revmed.ch/revue-medicale-suisse/2015/revue-medicale-suisse-497/douleurs-et-tumefactions-scrotales-prise-en-charge-initiale-diagnostique-et-therapeutique-par-le-generaliste</p>
<p>Les sources citées fondent cette monographie de la varicocèle, qui reste non validé cliniquement par un médecin.</p>
<p>Limite : le corpus AIPS local était absent, et aucun numéro d’autorisation Swissmedic n’est donc avancé. Le chapitre adulte de médecine sexuelle et reproductive de l’EAU n’a pas été la page ouverte pour les critères du couple infertile.</p>
</section>
""")
    html = "\n".join(parts)
    for n, block in plus.items():
        token = f'id="dx{DX}-i{n}"'
        start = html.find(token)
        if start < 0:
            raise SystemExit(f"ilot {n} introuvable")
        end = html.find("</section>", start)
        html = html[:end] + block + html[end:]
    return html

if __name__ == "__main__":
    sys.path.insert(0, str(Path(__file__).resolve().parents[0]))
    from assembler import ecrire
    ecrire(2, "Varicocèle", body())
