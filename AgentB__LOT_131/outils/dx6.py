# -*- coding: utf-8 -*-
"""DX.6 Torsion du testicule. Phrases propres à ce fichier."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from dx_lib import b, w, ilot, tableau

DX = 6

def body() -> str:
    P = []
    P.append(ilot(DX, 1, "Définition et sémantique", """
<p>La torsion du testicule est, dans le chapitre « Acute scrotum » des recommandations européennes d’urologie pédiatrique relu le 9 novembre 2026, une urgence urologique : le cordon tourne, le flux chute, et le parenchyme évolue vers la nécrose si l’on attend. [S1]</p>
""" + w("dx6-p1-def",
"Le mot torsion désigne le vrillage du pédicule, pas toute douleur de bourse.",
"Le cordon se tord, les veines se ferment d’abord, l’artère suit, l’ischémie s’installe, puis la nécrose si le délai dépasse la fenêtre critique.",
"Exemple : cette fenêtre est d’environ quatre à six heures dans le chapitre. [S1]",
"Le piège de langage est d’appeler torsion une épididymite douloureuse ou une torsion d’hydatide.",
"Source [S1].") + """
<p>Deux mécanismes ne portent pas le même nom. La forme de la puberté est en règle intravaginale. La forme périnatale est le plus souvent extravaginal, survenue avant la naissance, et elle peut toucher les deux côtés dans 11 à 21 % des cas périnataux. [S1]</p>
<p>La bourse aiguë est le syndrome d’appel, pas le diagnostic. Elle regroupe la torsion du testicule, la torsion d’hydatide et l’épididymite ou l’orchi-épididymite, qui en sont les causes les plus communes. Confondre le syndrome et la torsion fait explorer trop tard, ou rassure à tort. [S1]</p>
"""))
    P.append(ilot(DX, 2, "Épidémiologie (Suisse, puis Europe)", """
<p>La Revue Médicale Suisse de 2015, lue pour le contexte suisse, place la torsion hors du circuit électif du généraliste : elle relève le plus souvent des urgences. Aucun taux OFS, Obsan ou cantonal n’a été ouvert le 9 novembre 2026. On ne fabrique donc pas une incidence suisse. [S2]</p>
<p>Le chapitre européen décrit deux pics plutôt qu’un taux pour 100 000 : la période néonatale et le voisinage de la puberté. La torsion d’hydatide s’étale sur un âge plus large. L’épididymite, elle, concerne surtout les moins d’un an et les douze à quinze ans. Une étude citée estime l’incidence annuelle de l’épididymite autour de 1,2 pour 1 000 enfants. [S1]</p>
""" + w("dx6-p2-pics",
"Deux âges concentrent la torsion du testicule, et ce n’est pas un hasard anatomique.",
"Chez le nouveau-né, la vaginale n’est pas encore fixée et la torsion est extravaginal. À la puberté, le testicule plus lourd tourne dans une vaginale large : c’est la forme intravaginale.",
"Exemple chiffré : 11 à 21 % des torsions périnatales sont bilatérales. [S1]",
"Le piège est d’appliquer le délai de la puberté à un nouveau-né déjà tordu in utero.",
"Source [S1].") + """
<p>Chez l’individu, l’histoire est dominée par l’horloge. Soixante-neuf pour cent des torsions du testicule arrivent aux soins dans les douze heures, contre 62 % des torsions d’hydatide et 31 % des épididymites. Après coup, jusqu’à la moitié des testicules jugés viables au bloc peuvent quand même s’atrophier. Une subfertilité est retrouvée chez 36 à 39 % des patients. Le sperme n’est normal, dans le suivi à distance cité, que dans 5 à 50 % des cas. [S1]</p>
<p>L’enjeu n’est pas un dépistage de masse. C’est le délai entre le premier cri de douleur et la détorsion, parce que ce délai et le nombre de tours décident du sauvetage. [S1]</p>
"""))
    P.append(ilot(DX, 3, "Physiopathologie", """
<p>L’amorce est mécanique. Le testicule tourne dans la vaginale, ou, chez le nouveau-né, le cordon tourne en dehors d’elle. Le développement est vasculaire : le retour veineux cesse, la pression monte, l’artère se ferme. L’installation est clinique en quelques heures. Le maintien, si l’on ne détord pas, est la nécrose, puis l’atrophie, puis la baisse de la spermatogenèse. [S1]</p>
<p>Le chapitre sépare deux dégâts. Le premier est l’ischémie directe. Le second apparaît au moment de la détorsion : la reperfusion libère des radicaux libres dans le parenchyme. Sauver le testicule ne signifie donc pas effacer toute lésion. [S1]</p>
""" + w("dx6-p3-tours",
"Le nombre de tours pèse autant que l’heure.",
"Une torsion incomplète, entre 180 et 360 degrés, n’a pas montré d’atrophie dans l’étude citée quand les symptômes duraient jusqu’à douze heures. Au-delà de 360 degrés, une atrophie sévère a été vue après seulement quatre heures. Au-delà de 360 degrés et de vingt-quatre heures de symptômes, tous les testicules de cette série étaient absents ou sévèrement atrophiés. [S1]",
"Exemple : quatre heures et un tour complet ne se rangent pas dans la même case que douze heures et un demi-tour.",
"Le piège d’examen est une seule règle « après six heures, tout est perdu ».",
"Source [S1].") + """
<p>La stratégie qui corrige l’ischémie est la détorsion chirurgicale, pas un vasodilatateur. Rien dans le chapitre ne propose une classe médicamenteuse pour rouvrir l’artère spermatique. L’orchidopexie controlatérale empêche la torsion de l’autre côté, elle ne répare pas le côté déjà ischémié. [S1]</p>
""" + tableau([
("Lésion ou perturbation", "Exploration qui la montre", "Thérapeutique qui la corrige"),
("Le cordon est tordu et le flux artériel est menacé.", "L’examen, puis au besoin le Doppler ou l’échographie haute résolution du cordon, sans retarder le bloc.", "La détorsion chirurgicale immédiate. [S1]"),
("La reperfusion libère des radicaux après la détorsion.", "Il n’existe pas, dans le chapitre, de dosage sanguin de ces radicaux pour décider.", "On détord quand même, parce que l’ischémie prolongée est pire, et l’on prévient la famille de l’atrophie possible. [S1]"),
("La vaginale large laisse le testicule controlatéral libre de tourner.", "Le risque est anatomique, pas visible sur une prise de sang.", "L’orchidopexie de l’autre côté se fait dans le même temps, pas à froid. [S1]"),
("Une hydatide tordue nécrose un appendice, pas le testicule.", "La douleur du pôle supérieur et, parfois, le point bleu.", "Le traitement conservateur, et le bloc seulement si le doute persiste. [S1]"),
]) + """
"""))
    P.append(ilot(DX, 4, "Démarche diagnostique", """
<p>L’ordre est imposé par le temps, pas par la fréquence des épididymites. On exclut d’abord la torsion du testicule, parce que la nécrose est liée à l’heure. Les causes fréquentes viennent après, une fois cette hypothèse tenue ou écartée par l’exploration. [S1]</p>
<p>Le concurrent le plus dangereux est donc la torsion elle-même, face à l’épididymite. Le signe qui oriente est un début soudain, avec nausée ou vomissement, un testicule douloureux plutôt qu’un épididyme, une position horizontale anormale, et un réflexe crémastérien absent. Ce réflexe absent a, dans les travaux cités, une sensibilité de 100 % et une spécificité de 66 % : son absence pousse fort vers la torsion, sa présence ne doit pas servir d’alibi unique si le reste crie à l’ischémie. Le piège est d’attendre un Doppler « pour être sûr ». La conduite est l’exploration dès que la torsion est plausible. [S1]</p>
""" + w("dx6-p4-cremaster",
"Le réflexe crémastérien relève le testicule quand on frôle la face interne de la cuisse.",
"Si le cordon est tordu, ce réflexe disparaît. La sensibilité citée est de 100 %, la spécificité de 66 % : beaucoup de garçons sans torsion n’ont pas non plus ce réflexe, surtout petits.",
"Exemple : réflexe absent, douleur depuis trois heures, vomissement. On n’attend pas la biologie. [S1]",
"Le piège est de croire qu’un réflexe présent élimine la torsion avec la même force.",
"Source [S1].") + """
<p>La torsion d’hydatide partage le début brutal et parfois la réaction vagale. Elle se distingue, quand l’examen le permet, par une douleur isolée du pôle supérieur et par un point bleu, vu seulement dans 10 à 23 % des cas. Le piège est de conclure à l’hydatide parce que le point bleu manque. La conduite, si le doute reste, est encore l’exploration. [S1]</p>
<p>L’épididymite est plus souvent fébrile (11 à 19 %), l’épididyme est sensible, et le début est en moyenne plus long : seulement 31 % consultent dans les douze heures. Élever la bourse peut calmer l’épididymite et non la torsion : c’est le signe de Prehn, qualitatif dans le chapitre. Une bandelette normale n’élimine pas l’épididymite. Une bandelette anormale n’élimine pas la torsion. [S1]</p>
<p>D’autres bourses aiguës existent dans le chapitre : œdème scrotal idiopathique, orchite ourlienne, hématome, hernie étranglée, appendicite, purpura d’Henoch-Schönlein, traumatisme. Aucune ne justifie de laisser une torsion probable au fond d’un couloir. [S1]</p>
"""))
    P.append(ilot(DX, 5, "Anamnèse ciblée et drapeaux rouges", """
<p>On demande l’heure exacte du début, parce que quatre heures, douze heures et vingt-quatre heures ne mènent pas au même pronostic tissulaire. [S1]</p>
<p>On demande si la douleur est apparue d’un coup et si l’enfant a vomi, parce que cette paire oriente vers la torsion du testicule ou de l’hydatide plutôt que vers une infection. [S1]</p>
<p>On demande la fièvre, parce qu’elle est plus fréquente dans l’épididymite, entre 11 et 19 %, sans être un certificat d’infection. [S1]</p>
<p>On demande un traumatisme récent, un testicule non descendu, et l’âge : la torsion existe aussi sur un testicule cryptorchide, et le nouveau-né n’exprime pas la douleur comme le pubère. [S1]</p>
<p>On demande si quelqu’un a déjà « détordu » manuellement et si la douleur a cessé, parce qu’une sédation des symptômes ne prouve pas que le cordon est droit : dans une série, 17 explorations sur 53 ont trouvé une torsion résiduelle, dont 11 chez des garçons qui se disaient soulagés. [S1]</p>
""" + w("dx6-p5-heure",
"L’heure de début est une donnée thérapeutique, pas administrative.",
"Elle se compare à la fenêtre de quatre à six heures, au seuil de douze heures des torsions incomplètes, et au seuil de vingt-quatre heures qui fait passer l’exploration d’urgente à semi-élective.",
"Exemple : douleur depuis cinq heures, début noté par la mère. Le bloc passe avant le dossier complet. [S1]",
"Le piège est d’écrire « depuis ce matin » sans heure, puis de croire qu’on est encore dans la fenêtre.",
"Source [S1].") + """
<p>Les drapeaux qui imposent le 144 ou le bloc sans détour sont : douleur scrotale brutale, vomissements, testicule haut ou horizontal, réflexe crémastérien absent, et tout doute persistant. Le score TWIST peut aider à trier, mais le chapitre interdit de s’y fier seul : il ne prouve ni n’élimine la torsion, et la preuve médicolégale d’une décision fondée seulement sur le score n’est pas acquise. Les points du score ne sont pas reproduits dans la page lue : on ne les reconstitue pas de mémoire. [S1]</p>
"""))
    P.append(ilot(DX, 6, "Examen physique ciblé, région par région", """
<p>Le normal, chez un garçon au repos, est un testicule en place, vertical, mobile, avec un réflexe crémastérien présent des deux côtés, un épididyme non sensible et une peau souple. On regarde les deux bourses avant de palper la douloureuse. [S1]</p>
<p>Région du testicule. Le pathologique de la torsion est une glande très sensible, souvent horizontale. On note la position, la hauteur et la sensibilité globale, pas seulement un point. La valeur de la position horizontale est qualitative : elle est plus fréquente dans la torsion que dans l’épididymite, sans pourcentage supplémentaire dans le passage lu. [S1]</p>
<p>Région de l’épididyme et du pôle supérieur. Le normal est un épididyme souple. Le pathologique de l’épididymite est un épididyme sensible. Le pathologique de l’hydatide est une douleur limitée au pôle supérieur, parfois avec un point bleu cutané. On cherche ce point en soulevant la peau, sans forcer si la douleur empêche l’examen : l’absence du point bleu, fréquente, ne change pas l’urgence si le testicule entier est pris. [S1]</p>
<p>Région de la cuisse. On cherche le réflexe crémastérien par un effleurement de la face interne. L’absence est le résultat pathologique le plus cité, avec la sensibilité et la spécificité déjà données. On compare à l’autre cuisse. [S1]</p>
<p>Signe de Prehn. On élève doucement la bourse. Le résultat qui va vers l’épididymite est un soulagement. Le résultat qui va vers la torsion est l’absence de soulagement. Ce signe ne remplace pas la décision d’explorer. [S1]</p>
"""))
    P.append(ilot(DX, 7, "Approche syndromique", """
<p><em>7.1 Syndrome d’ischémie testiculaire</em></p>
<p>Les signes fonctionnels sont la douleur d’apparition brutale, la nausée et le vomissement. La nausée est ici un reflet vagal, pas un trouble digestif primitif. On la date. Le mécanisme est l’ischémie du testicule et la traction du cordon. [S1]</p>
<p>Les signes physiques sont le testicule globalement sensible, haut ou horizontal, et le réflexe crémastérien absent. On les cherche comme décrit au point 6. Le mécanisme est le vrillage du pédicule, qui fixe la glande et coupe le réflexe. [S1]</p>
<p><em>7.2 Syndrome de l’hydatide</em></p>
<p>Le signe fonctionnel peut ressembler à la torsion vraie, y compris la réaction vagale. Le signe physique, quand il est présent, est le point bleu et la douleur du seul pôle supérieur. Le point bleu est une petite zone livide vue à travers la peau, correspondant à l’appendice nécrosé. Il manque dans la majorité des cas, puisque seulement 10 à 23 % le montrent. Le mécanisme est la torsion d’un reliquat embryonnaire, sans fermer l’artère du testicule. [S1]</p>
<p><em>7.3 Syndrome épididymaire</em></p>
<p>Le signe fonctionnel est une douleur plus progressive, parfois fébrile. Le signe physique est l’épididyme épaissi et sensible, et parfois un soulagement quand on soulève la bourse. Le mécanisme lu est l’inflammation de l’épididyme, bactérienne seulement dans une minorité de cultures. Chez le garçon prépubère, une anomalie urogénitale sous-jacente a été trouvée dans 29,1 % d’une série, et environ un quart des épididymites prépubères ont une pathologie sous-jacente dans une autre formulation du même chapitre. [S1]</p>
"""))
    P.append(ilot(DX, 8, "Diagnostic positif et critères", """
<p>Le chapitre est explicite : le diagnostic de torsion repose sur la présentation et l’examen, avec un niveau de preuve 3. Il n’existe pas de critère de société savante du type « deux majeurs et un mineur ». Ce qui suffit à décider l’exploration, c’est un tableau compatible, pas une image parfaite. Ce qui ne suffit pas à surseoir, c’est un Doppler rassurant, un score TWIST intermédiaire, une bandelette anormale ou un réflexe difficile à juger. [S1]</p>
""" + w("dx6-p8-assez",
"La décision d’ouvrir est clinique.",
"Douleur brutale, vomissement, testicule horizontal, réflexe absent : le faisceau suffit. Aucun de ces items n’est obligatoire à lui seul dans une formule chiffrée du chapitre.",
"Exemple : Doppler avec flux conservé et clinique de torsion. Le flux ne suffit pas à renvoyer l’enfant. [S1]",
"Le piège est d’attendre un critère biologique qui n’existe pas.",
"Source [S1].") + """
<p>La confirmation absolue est opératoire : on voit le tour du cordon. Avant le bloc, on parle de suspicion, et cette suspicion se traite comme la maladie. L’échographie ne pose pas le diagnostic à la place du chirurgien. [S1]</p>
"""))
    P.append(ilot(DX, 9, "Examens complémentaires", """
<p><em>9.a Gold standard</em></p>
<p>Le gold standard décisionnel est clinique, puis chirurgical. Le chapitre ne désigne pas le Doppler comme étalon. L’exploration qui montre le cordon tordu est la preuve. [S1]</p>
<p><em>9.b 1<sup>re</sup> intention</em></p>
<p>Si un examen d’image est fait, c’est l’échographie avec Doppler, et elle ne doit pas retarder le geste. La sensibilité citée va de 63,6 % à 100 %, la spécificité de 97 % à 100 %, la valeur prédictive positive de 100 % et la valeur prédictive négative de 97,5 %. Ces intervalles ne autorisent pas l’attente : dans une série multicentrique de 208 garçons tordus, 24 % avaient une vascularisation normale ou augmentée. Un flux qui persiste n’exclut donc pas la torsion. Il faut comparer au côté opposé. [S1]</p>
<p>Le terme doppler juste est l’absence ou la diminution du flux, ou au contraire un flux conservé qui n’innocente pas. Pour le cordon, l’échographie haute résolution cherche le {b("dx6-p9-tour","tour de spire")} du cordon, avec une sensibilité de 97,3 % et une spécificité de 99 % dans les travaux cités. On ne dit pas « image anormale du cordon » sans nommer ce tour. [S1]</p>
""" + w("dx6-p9-tour",
"Le tour de spire est la spire visible du cordon spermatique, enroulée sur elle-même.",
"L’échographie haute résolution le montre comme un enroulement, distinct d’un simple œdème.",
"Exemple : sensibilité 97,3 % et spécificité 99 % pour cette visualisation directe, à condition de ne pas perdre l’heure du bloc. [S1]",
"Le piège est de répéter l’examen jusqu’à « bien voir » alors que l’enfant est dans la fenêtre des quatre à six heures.",
"Source [S1].") + """
<figure>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 360 200" role="img" aria-label="Schéma didactique d un cordon tordu">
<rect width="360" height="200" fill="#fbfaf7"/>
<ellipse cx="200" cy="130" rx="40" ry="50" fill="#f3e6d4" stroke="#6b4f32"/>
<path d="M200 80 C220 60 180 40 200 20" fill="none" stroke="#9f1239" stroke-width="4" stroke-dasharray="4 3"/>
<text x="210" y="50" font-size="14" fill="#9f1239">1</text>
<text x="188" y="134" font-size="14">2</text>
<text x="12" y="24" font-size="13">Schéma didactique, pas une échographie de patient</text>
</svg>
<figcaption>Aucune photographie clinique libre n’a été embarquée le 9 novembre 2026. Le dessin situe seulement le cordon et le testicule.</figcaption>
<ol>
<li>Le contour pointillé marque l’enroulement du cordon, là où l’on cherche le tour de spire.</li>
<li>Le testicule est rappelé pour la comparaison de flux avec le côté opposé, sans prétendre à une coupe réelle.</li>
</ol>
</figure>
""" + tableau([
("Résultat possible", "Interprétation", "Hypothèse"),
("La clinique est typique et aucun Doppler n’est encore fait.", "Le diagnostic de travail est la torsion.", "On explore sans attendre l’image. [S1]"),
("Le Doppler ne montre plus de flux d’un côté, avec comparaison controlatérale.", "L’ischémie est probable.", "La torsion reste l’hypothèse, et le bloc est déjà indiqué. [S1]"),
("Le Doppler montre un flux normal ou augmenté, mais la douleur est brutale avec vomissement.", "Le résultat est discordant et connu : 24 % de 208 garçons tordus avaient encore un flux.", "On n’écarte pas la torsion. [S1]"),
("L’échographie haute résolution voit un tour de spire.", "La visualisation directe du cordon est très spécifique dans les chiffres cités.", "On opère, sans transformer cet examen en rendez-vous différé. [S1]"),
("La bandelette urinaire est positive.", "Ce résultat limite n’innocente pas le cordon.", "L’hypothèse torsion reste ouverte, et l’infection urinaire n’est pas le diagnostic de sortie. [S1]"),
]) + """
<p><em>9.c Alternatives</em></p>
<p>L’échographie au lit par le médecin urgentiste peut aider, selon une revue systématique citée, avec un risque de biais dans les études de départ. Elle ne remplace pas l’exploration si la clinique est forte. Il n’y a pas d’adaptation de grossesse chez le garçon. L’insuffisance rénale ne change pas l’indication opératoire. L’allergie iodée et l’IRM ne sont pas le chemin de cette urgence dans le chapitre. [S1]</p>
<p><em>9.d 2<sup>e</sup> intention</em></p>
<p>La bandelette et la culture d’urine viennent en appoint, surtout si l’on penche vers une épididymite. Elles ne sont pas le test qui autorise le retour à la maison. Le bilan hormonal et le spermogramme appartiennent au suivi, des mois plus tard, pas à la première heure. [S1]</p>
"""))
    P.append(ilot(DX, 10, "Arbre décisionnel", """
<p>Si la douleur scrotale est brutale et que la torsion est plausible, alors on appelle le 144 ou l’on monte au bloc selon le lieu, et l’on n’attend pas une preuve d’image.</p>
<p>Si un Doppler est déjà là et qu’il montre un flux, alors on explore quand même tant que la clinique n’a pas changé de camp.</p>
<p>Si les symptômes durent depuis moins de vingt-quatre heures, alors l’exploration est urgente. Si elles durent depuis plus de vingt-quatre heures, alors l’exploration devient semi-élective, sans devenir facultative. [S1]</p>
<p>Si l’on voit au bloc une torsion, alors on détord, on juge la vitalité, et l’on fixe l’autre testicule dans le même temps opératoire.</p>
<p>Si le tableau est celui d’une hydatide certaine, avec point bleu et testicule indolore, alors on peut surveiller, sous antalgiques anti-inflammatoires dont la dose suisse n’est pas écrite ici, et l’on opère si la douleur dure ou si le doute revient. [S1]</p>
<p>Si l’enfant est un nouveau-né avec une torsion périnatale, alors on fixe le côté controlatéral. Le moment exact, quand la torsion est prénatale, dépend de l’état clinique : la recommandation sur le timing est faible. [S1]</p>
"""))
    P.append(ilot(DX, 11, "Prise en charge selon les recommandations suisses", """
<p><em>11.A But</em></p>
<p>Le but chiffré est de détordre avant la nécrose. La fenêtre idéale citée est de quatre à six heures après le début des symptômes. Un délai moyen inférieur à treize heures a été associé à la préservation de la fertilité dans une étude. Au-delà, le but devient de limiter la perte, d’enlever ce qui est manifestement nécrosé, et de protéger l’autre testicule. [S1]</p>
<p><em>11.B Moyens</em></p>
<p>L’ordre est chronologique. À la première minute, on croit à la torsion. Dans l’heure, on rejoint un bloc capable d’explorer, par le 144 si l’on est loin. On peut tenter une détorsion manuelle en attendant, par rotation externe, sauf si la douleur augmente ou si l’on sent une résistance franche. Le succès manuel exige la disparition immédiate de tous les symptômes et un examen redevenu normal. Même alors, on opère : la manœuvre ne remplace pas le chirurgien, et un Doppler peut seulement guider. [S1]</p>
""" + w("dx6-p11-chrono",
"Urgence, conduite chronologique.",
"Minute 0 : heure de début notée, jeûne, voie veineuse selon l’équipe, appel du bloc. Pas de spermogramme. Pas de score utilisé seul.",
"Si le trajet dépasse l’heure locale, le 144 transporte. À l’arrivée, exploration. Au bloc : détorsion, attente de recoloration, fixation controlatérale dans le même temps.",
"Exemple : symptômes depuis trois heures à l’appel. On ne programme pas le lendemain matin. [S1]",
"Le piège est une détorsion manuelle « réussie » qui renvoie l’enfant chez lui.",
"Source [S1]. Aucune dose d’antalgique n’est citée : l’information professionnelle suisse n’a pas été relue.") + """
<p>Au bloc, si le testicule reprend une couleur viable, on le conserve, parce que des volumes plus grands ont été liés à une meilleure fonction et que le côté tordu peut encore contribuer à l’endocrine. Si la nécrose est évidente, l’orchidectomie se discute. Après plus de vingt-quatre heures, la controverse persiste entre conserver et enlever pour protéger la fertilité controlatérale. Une étude a trouvé un sperme préservé après les deux attitudes par rapport à des témoins, avec une morphologie meilleure après orchidectomie. Le chapitre ne tranche pas par une obligation d’enlever. [S1]</p>
<p>L’orchidopexie controlatérale se fait tout de suite après la détorsion, pas sur une liste d’attente. La récidive après fixation reste rare, 4,5 %, parfois des années plus tard. Aucun consensus du chapitre ne désigne le fil ou la technique de fixation. L’incision de l’albuginée avec greffe de vaginale a été proposée contre un syndrome de loge, mais l’effet immédiat sur la pression intratesticulaire est jugé vague et le bénéfice à long terme peu clair. [S1]</p>
<p>Forme non compliquée au sens d’une hydatide certaine : repos relatif, antalgique anti-inflammatoire, contrôle sur six semaines cliniquement et à l’échographie, sans atrophie dans la série citée. On n’écrit pas le nom commercial de l’antalgique. [S1]</p>
<p>L’épididymite du garçon prépubère ne reçoit pas d’antibiotique dans la plupart des cas. Le chapitre réserve l’antibiotique à une bandelette et une culture qui montrent une infection. La maladie est souvent spontanément résolutive avec le repos et l’antalgie. Un abcès ou un testicule nécrotique, rares, peuvent quand même mener au bloc. Aucune molécule ni aucune dose suisse n’est recopiée, faute d’information professionnelle relue le 9 novembre 2026. [S1]</p>
<p>Situations particulières. Le nouveau-né : torsion souvent déjà constituée, fixation de l’autre côté, timing guidé par l’état si la torsion est prénatale. L’enfant avec testicule non descendu : la torsion y existe, on n’attend pas de palper une bourse pleine. Il n’y a pas de grossesse du patient. L’insuffisance rénale ou hépatique ne modifie pas, dans la page lue, l’indication de détordre. [S1]</p>
<p>Le versant social est l’information des parents sur l’atrophie possible malgré un testicule « sauvé », sur la fertilité ultérieure, et sur le retour immédiat si la douleur revient. L’école et le sport n’ont pas de délai chiffré dans le chapitre. [S1]</p>
<p><em>11.C Surveillance</em></p>
<p>On revoit le volume, parce que jusqu’à la moitié des testicules jugés viables s’atrophient ensuite. On parle de fertilité à distance : la subfertilité concerne 36 à 39 % des patients, tandis qu’une étude de paternité a trouvé un taux de grossesses normal après torsion unilatérale, sans différence entre ceux qui avaient gardé le testicule et ceux qui l’avaient perdu. Les taux de FSH, de LH et de testostérone sont plus hauts que chez les témoins, mais restent dans l’intervalle normal selon les travaux cités. On n’invente pas de seuil d’arrêt médicamenteux : il n’y a pas de traitement au long cours. [S1]</p>
<p><em>11.D Pronostic</em></p>
<p>La guérison tissulaire n’est pas garantie par la recoloration au bloc. Le pronostic endocrinien immédiat reste le plus souvent dans la norme, le pronostic de sperme est incertain, et la paternité peut être conservée dans l’étude citée. Une détorsion précoce, délai moyen inférieur à treize heures, préservait la fertilité, alors qu’une torsion prolongée, délai moyen de soixante-dix heures, suivie d’orchidectomie, la mettait en jeu. [S1]</p>
<p>Sortie : douleur contrôlée sans tableau de re-torsion, parents capables de redater une douleur, côté controlatéral fixé si une torsion a été confirmée, et rendez-vous de volume annoncé. Le chapitre ne donne pas d’autre critère chiffré de retour à la maison. [S1]</p>
"""))
    P.append(ilot(DX, 12, "Prévention", """
<p>Il n’existe pas, dans les pages lues, de prévention primaire de la vaginale large : pas de vaccin, pas de médicament, pas de dépistage scolaire de la torsion. La prévention secondaire est la reconnaissance immédiate de la douleur brutale, par la famille et par le premier médecin, avec le 144 plutôt qu’un rendez-vous. [S1] [S2]</p>
<p>La prévention tertiaire est l’orchidopexie controlatérale dans le même temps, qui réduit le risque de torsion de l’autre côté sans l’annuler : la récidive après fixation est de 4,5 %. On le dit aux parents. Aucune recommandation OFSP spécifique n’a été ouverte. [S1]</p>
"""))
    P.append(ilot(DX, 13, "Points clés", """
<p>Une bourse douloureuse d’un coup, avec vomissement, s’explore sans attendre un Doppler parfait.</p>
<p>Un flux doppler conservé n’innocente pas : 24 % de 208 garçons tordus en avaient encore un.</p>
<p>La fenêtre tissulaire idéale citée est de quatre à six heures, et elle dépend aussi du nombre de tours.</p>
<p>La détorsion manuelle, même suivie d’un soulagement, ne dispense pas du bloc.</p>
<p>On fixe l’autre testicule dans le même temps opératoire, pas six semaines plus tard.</p>
<p>Jusqu’à un testicule sur deux jugé viable s’atrophie ensuite : il faut l’avoir dit.</p>
"""))
    P.append(ilot(DX, 14, "Pièges et questions fréquentes à l'examen fédéral suisse", """
<p>Question : un réflexe crémastérien absent a-t-il une spécificité de 100 % ? Réponse : non. La sensibilité citée est de 100 % et la spécificité de 66 %. [S1]</p>
<p>Question : à partir de quelle heure l’exploration cesse-t-elle d’être urgente ? Réponse : après vingt-quatre heures de symptômes elle devient semi-élective, mais elle reste indiquée. Avant cela, elle est urgente. [S1]</p>
<p>Question : une torsion de 200 degrés depuis dix heures condamne-t-elle le testicule dans l’étude citée ? Réponse : non. Entre 180 et 360 degrés et jusqu’à douze heures, cette étude n’a pas observé d’atrophie. [S1]</p>
<p>Question : le point bleu est-il nécessaire pour reconnaître une hydatide ? Réponse : non, il n’est vu que dans 10 à 23 % des cas. [S1]</p>
<p>Question : une bandelette positive autorise-t-elle le retour à la maison ? Réponse : non. Elle n’exclut pas la torsion, et une bandelette normale n’exclut pas l’épididymite. [S1]</p>
<p>Question : pourquoi 17 cas sur 53 comptent-ils ? Réponse : parce qu’une torsion résiduelle a été trouvée à l’exploration, y compris chez 11 garçons soulagés après manœuvre manuelle. [S1]</p>
<p>Question : l’antibiotique est-il systématique dans l’épididymite du petit garçon ? Réponse : non. Il est réservé à une infection montrée par la bandelette et la culture. [S1]</p>
<p>Question : la fixation empêche-t-elle toute récidive ? Réponse : non. Le chapitre cite 4,5 % de récidives, parfois des années plus tard, sans consensus sur le fil. [S1]</p>
<p>Question : FSH et LH élevées après torsion signifient-elles une insuffisance endocrine certaine ? Réponse : non. Elles sont plus hautes que chez les témoins, mais le chapitre les situe encore dans l’intervalle normal. [S1]</p>
<p>Question : où est la dose suisse de l’antalgique ? Réponse : elle n’est pas dans cette monographie, parce que l’information professionnelle correspondante n’a pas été relue. [S1]</p>
"""))
    P.append("""
<section class="ilot sources">
<h3>Sources</h3>
<p>[S1] Association européenne d’urologie, Guidelines on Paediatric Urology, chapitre « Acute scrotum », texte en ligne consulté le 9 novembre 2026. https://uroweb.org/guidelines/paediatric-urology/chapter/acute-scrotum</p>
<p>[S2] Revue Médicale Suisse 2015, numéro 497, « Douleurs et tuméfactions scrotales », page consultée le 9 novembre 2026, pour la place de la torsion aux urgences. https://www.revmed.ch/revue-medicale-suisse/2015/revue-medicale-suisse-497/douleurs-et-tumefactions-scrotales-prise-en-charge-initiale-diagnostique-et-therapeutique-par-le-generaliste</p>
<p>Ce chapitre sur la torsion du testicule s’appuie sur les sources citées et demeure non validé cliniquement.</p>
<p>Limite : corpus AIPS local absent le 9 novembre 2026, donc aucune dose antalgique ni antibiotique suisse n’est affirmée. Le score TWIST est nommé par le chapitre sans sa grille de points, qui n’est donc pas reconstituée.</p>
</section>
""")
    html = "\n".join(P)
    from dx6_extra import extra
    from dx6_extra2 import extra2
    from dx6_extra3 import extra3
    from dx6_extra4 import extra4
    plus = extra()
    for src in (extra2(), extra3(), extra4()):
        for k, v in src.items():
            plus[k] = plus.get(k, "") + v
    for n, block in plus.items():
        token = f'id="dx{DX}-i{n}"'
        start = html.find(token)
        if start < 0:
            raise SystemExit(n)
        end = html.find("</section>", start)
        html = html[:end] + block + html[end:]
    return html

if __name__ == "__main__":
    from assembler import ecrire
    ecrire(6, "Torsion du testicule", body())
