#!/usr/bin/env python3
"""DX.3 Hypothyroïdie primaire."""
from rendre_dx import rendre, P, S
from dx3_plus import PLUS
from moteur import btn

ess = P(
    "L'hypothyroïdie primaire est un manque d'hormone par défaillance de la thyroïde : la thyréostimuline monte, la thyroxine libre baisse. "
    "On substitue par lévothyroxine orale, à jeun, en commençant bas si le cœur ou l'âge l'exigent. "
    "On écarte l'insuffisance surrénale avant la première dose. "
    "Le coma myxœdémateux est un autre chapitre.",
    S(1, 3, 9),
)
points = {f"p{i}": P("Voir la fenêtre.") for i in range(1, 15)}
# islands rewritten below
points.update({
"p1": P("La thyroïde ne fabrique plus assez. La thyréostimuline monte. Ce n'est pas le déficit hypophysaire. La ", btn("w-def", "définition"), " fixe la frontière.", S(1)),
"p2": P("Elle augmente avec l'âge. Les anticorps accélèrent le passage de la forme infraclinique à la forme franche. Les ", btn("w-epi", "chiffres"), " sont ceux de 2010.", S(1)),
"p3": P("Moins de thyroxine, moins de frein, plus de thyréostimuline. La ", btn("w-physio", "chaîne"), " explique aussi pourquoi l'hormone peut démasquer une surrénale.", S(1, 9)),
"p4": P("Confirmer le profil, chercher la cause, écarter la surrénale et le coma, puis substituer. Les ", btn("w-dem", "pas"), " évitent la dose d'emblée.", S(9)),
"p5": P("Fatigue, frilosité, prise de poids, constipation, règles. Les ", btn("w-ana", "questions"), " cherchent aussi le lithium, l'amiodarone et l'arrêt de la lévothyroxine.", S(1, 4)),
"p6": P("Peau sèche, voix, réflexes lents, bradycardie, goitre ou loge vide. L'", btn("w-ex", "examen"), " cherche surtout le froid et la conscience, pour ne pas rater le coma.", S(3)),
"p7": P("Thyréostimuline haute et thyroxine libre basse : le syndrome primaire. Le ", btn("w-syn", "profil"), " le sépare du central et de la forme infraclinique.", S(1)),
"p8": P("Le diagnostic positif est biologique plus le contexte. Le ", btn("w-pos", "seuil pratique"), " rappelle les bornes du laboratoire et le rôle des anticorps.", S(1)),
"p9": P("Anticorps anti-thyroperoxydase, parfois échographie, pas de scintigraphie en routine. Les ", btn("w-examens", "examens"), " restent courts.", S(1)),
"p10": P("Coma d'abord, surrénale ensuite, puis substitution. L'", btn("w-arbre", "arbre"), " ne commence pas par 100 µg chez un coronarien.", S(3, 9)),
"p11": P("Euthyrox, numéro 54949. Le ", btn("w-ttt", "schéma"), ", l'", btn("w-enf", "enfant"), " et les ", btn("w-plus", "autres situations"), " donnent les microgrammes lus, pas une dose intraveineuse.", S(9)),
"p12": P("À jeun, loin du calcium et du fer, contrôle après chaque changement. La ", btn("w-prev", "prévention"), " évite le surdosage et l'oubli.", S(1, 9)),
"p13": P("Primaire : thyréostimuline haute. Début à 25 µg si fragile. Surrénale d'abord. Le ", btn("w-cles", "rappel"), " tient ces trois phrases.", S(1, 9)),
"p14": P("Les pièges sont la dose pleine d'emblée, l'hormone avant le cortisol, et la confusion avec le centre. Les ", btn("w-pieges", "pièges"), " et le ", btn("w-cas", "cas"), " les fixent.", S(9)),
})

fens = []
def add(pid, wid, titre, *paras):
    fens.append((pid, wid, titre, "".join(paras)))

add("p1", "w-def", "Définition",
P("L'hypothyroïdie primaire est la baisse de production d'hormone par la thyroïde elle-même. La thyroxine libre baisse. L'hypophyse, privée de frein, augmente la thyréostimuline. La revue de 2010 dit que les valeurs dépassent habituellement 10 mU/l dans la forme franche. La forme infraclinique, thyréostimuline modérément haute et thyroxine libre normale, est un autre diagnostic de la leçon.", S(1)),
P("L'hypothyroïdie centrale fait l'inverse sur la thyréostimuline : elle reste basse ou normale alors que la thyroxine libre est basse. La confondre mène à rassurer parce que « la TSH n'est pas haute ». Ce n'est pas ce chapitre, mais c'est la frontière à nommer dès la définition.", S(1)),
P("Le coma myxœdémateux est l'extrême décompensé : hypothermie, hypoventilation, hyponatrémie, trouble de conscience. On ne le traite pas comme une hypothyroïdie de ville. La lévothyroxine y est intraveineuse dans la recommandation de 2014, après le glucocorticoïde. Ici, le patient parle, marche, a froid : la voie est orale.", S(3)),
P("Causes fréquentes : thyroïdite auto-immune, après chirurgie, après iode radioactif, iode en excès ou carence, amiodarone, lithium, phase basse d'une thyroïdite. Le mécanisme commun est le manque de fabrication ou la perte de glande, pas un blocage hypophysaire.", S(1, 4)),
)

add("p2", "w-epi", "Fréquence",
P("Dans NHANES III, cité par la revue lausannoise, l'hypothyroïdie franche était inférieure à 1 % chez des adultes sans maladie connue. Elle est rare chez l'adulte jeune et augmente avec l'âge. La forme infraclinique est estimée à environ 5 %. Ces chiffres dépendent des bornes.", S(1)),
P("Le passage à la forme franche est de 4,3 % par an si les anticorps anti-thyroperoxydase sont présents, et de 2,3 % par an s'ils sont absents. À dix ans, le risque passe de 23 % à 43 % quand les anticorps sont positifs. On dose donc ces anticorps quand la thyréostimuline est un peu haute et qu'on hésite à traiter : ils changent le risque, pas le diagnostic du jour si la thyroxine libre est déjà basse.", S(1)),
P("Aucune prévalence suisse classant cette cause parmi les dix diagnostics n'a été lue. On ne l'invente pas."),
)

add("p3", "w-physio", "Physiopathologie",
P("La thyroxine et la triiodothyronine freinent l'hypophyse. Quand la glande produit moins, la thyréostimuline monte. Ce rétrocontrôle est le test. Il suppose une hypophyse capable de répondre. Si l'hypophyse est détruite, la thyréostimuline ne monte pas et le test « TSH haute » manque le diagnostic.", S(1)),
P("L'hormone thyroïdienne accélère le cortisol nécessaire en situation de stress et peut précipiter une insuffisance surrénale latente, notamment dans les polyendocrinopathies. La revue de 2010 le met dans les implications pratiques. Euthyrox est contre-indiqué si la surrénale n'est pas traitée. D'où l'ordre : cortisol si le doute existe, puis seulement la lévothyroxine.", S(1, 9)),
P("Sous amiodarone, la thyréostimuline peut monter au début par l'effet de Wolff-Chaikoff, sans que la thyroxine libre soit basse. Ce n'est pas encore une hypothyroïdie primaire franche. La forme franche, elle, a la thyroxine libre basse et se traite par lévothyroxine sans obligation d'arrêter l'amiodarone si le cardiologue la maintient.", S(4)),
P("La triiodothyronine basse d'une réanimation n'est pas cette maladie. La recommandation de 2014 refuse la lévothyroxine pour le syndrome de basse T3 du patient qui n'était pas hypothyréodien. Le patient déjà substitué, lui, garde son traitement.", S(3)),
)

add("p4", "w-dem", "Démarche",
P("Pas 1. Conscience, température, respiration. Froid, lent, endormi : chapitre du coma, pas celui-ci. Patient stable : on continue.", S(3)),
P("Pas 2. Profil. Thyréostimuline haute et thyroxine libre basse : primaire. Thyréostimuline haute et thyroxine libre normale : infraclinique, autre fichier. Thyréostimuline non haute et thyroxine libre basse : central, autre fichier.", S(1)),
P("Pas 3. Cause. Anticorps anti-thyroperoxydase, chirurgie ou iode dans le passé, amiodarone, lithium, produit de contraste récent, thyroïdite récente. Un goitre dur et indolore oriente vers Hashimoto. Une loge vide oriente vers une thyroïdectomie.", S(1, 4)),
P("Pas 4. Surrénale. Hypotension, hyponatrémie, mélanodermie, autre maladie auto-immune : cortisol avant l'hormone. Sans aucun de ces signes, on peut commencer, en sachant que la contre-indication d'Euthyrox vise les troubles surrénaliens non traités.", S(9)),
P("Pas 5. Dose. Âge, cœur, ancienneté du manque. Début à 25 µg si âgé, hypothyroïdie ancienne ou cardiopathie. Sinon, début dans la zone 25 à 50 du tableau, entretien 100 à 200 µg. À jeun.", S(9)),
P("Pas 6. Contrôle à quatre à six semaines après un changement, pas à trois jours. Cible : thyréostimuline dans les bornes, en évitant une valeur trop basse. La revue cite 0,4 mU/l comme plancher à ne pas franchir vers le bas, à cause de l'os et de la fibrillation.", S(1)),
)

add("p5", "w-ana", "Anamnèse",
P("Fatigue, frilosité, prise de poids modérée, constipation, voix rauque, peau sèche, crampes, règles abondantes, dépression, bradycardie connue. Le début est en mois. Un début en jours avec douleur du cou est une thyroïdite, dont la phase basse est souvent transitoire : on ne promet pas un traitement à vie le premier jour.", S(1)),
P("Médicaments. Amiodarone, lithium, iode, contraste. Lévothyroxine déjà prescrite : heure de prise, jeûne, calcium, fer, observance. La revue liste calcium, fer, hydroxyde d'aluminium et cholestyramine comme freins à l'absorption, et phénytoïne, carbamazépine, phénobarbital, rifampicine comme accélérateurs du métabolisme.", S(1, 4)),
P("Grossesse ou projet. Avis spécialisé. Les besoins montent. Sans borne locale : environ 4,0 mU/l (ATA, 2017) ou 2,5 mU/l, 3,0 mU/l, 3,5 mU/l (ETA, 2014).", S(1)),
P("Antécédent d'infarctus récent, angor instable, myocardite. Euthyrox est contre-indiqué dans l'infarctus aigu, l'angine de poitrine, la myocardite aiguë, la pancardite, l'insuffisance cardiaque avec tachycardie. On ne « commence quand même à petite dose » dans l'infarctus de la nuit. On attend que l'épisode aigu soit passé, puis on commence à 25 µg si le manque doit être corrigé.", S(9)),
)

add("p6", "w-ex", "Examen",
P("Température et conscience d'abord. Un patient à 35 °C et somnolent n'est pas une hypothyroïdie de consultation. Fréquence cardiaque basse, pression parfois haute, poids. Peau sèche, cheveux, œdème des paupières, macroglossie discrète, réflexes lents au retour."),
P("Cou. Goitre ferme et indolore de Hashimoto, ou cicatrice, ou rien de palpable après un iode radioactif. Un nodule se classe à part, de TR1 à TR5, s'il existe. L'hypothyroïdie n'annule pas un nodule suspect.", S(6)),
P("Cœur. Bradycardie, parfois épanchement dans les formes longues. Électrocardiogramme si l'on commence chez un patient cardiaque, comme l'information d'Eltroxine le suggère avant le traitement quand on suspecte une cardiopathie. On ne retarde pas des semaines un patient jeune sans plainte cardiaque.", S(15)),
)

add("p7", "w-syn", "Profils",
P("Primaire franche : thyréostimuline haute, souvent au-dessus de 10 mU/l dans la phrase de 2010, thyroxine libre basse. Les bornes du Centre hospitalier universitaire vaudois publiées alors étaient 0,2 à 3,5 mU/l pour la thyréostimuline et 8 à 22 pmol/l pour la thyroxine libre. On utilise les bornes du compte rendu du jour.", S(1)),
P("Infraclinique : thyréostimuline entre la borne haute et des valeurs encore modérées, thyroxine libre normale. La revue parle de 3,5 à 20 mU/l. Ce n'est pas une indication automatique. Autre chapitre.", S(1)),
P("Centrale : thyroxine libre basse, thyréostimuline basse ou « normale ». On ne la range pas ici.", S(1)),
P("Amiodarone euthyroïdien : thyroxine libre haute ou limite haute, thyréostimuline revenue vers la normale après trois mois, triiodothyronine basse. L'hypothyroïdie induite franche, elle, a la thyroxine libre basse et la thyréostimuline au-dessus de 10 mU/l dans la définition européenne de 2018.", S(4)),
P("Basse T3 de réanimation : triiodothyronine basse, thyréostimuline basse ou normale, pas une thyréostimuline très haute. On ne commence pas Euthyrox pour cela.", S(3)),
)

add("p8", "w-pos", "Diagnostic positif",
P("Deux conditions. Thyroxine libre basse pour le laboratoire. Thyréostimuline haute, en pratique souvent au-dessus de 10 mU/l pour parler de forme franche selon la revue. L'une sans l'autre change le nom.", S(1)),
P("Les anticorps anti-thyroperoxydase confirment le mécanisme auto-immun et le risque évolutif. Ils ne sont pas requis pour commencer le traitement si la thyroxine libre est déjà basse : le manque est là, quelle qu'en soit la cause autoimmune ou post-chirurgicale.", S(1)),
P("On ne pose pas le diagnostic sur la fatigue seule. On ne le pose pas sur une thyréostimuline à peine au-dessus de la borne avec une thyroxine libre normale : c'est l'infraclinique, dont le traitement est controversé.", S(1)),
)

add("p9", "w-examens", "Examens",
P("Thyroxine libre et thyréostimuline suffisent au nom. Anticorps anti-thyroperoxydase pour le mécanisme et le pronostic de la forme limite. Numération et lipides si la clinique le suggère : la revue mentionne une dyslipidémie, cholestérol total au-dessus de 7 mmol/l, parmi les raisons de discuter un traitement de la forme infraclinique. Ce seuil-là concerne l'autre chapitre. Ici la forme est déjà franche.", S(1)),
P("Échographie si le cou est nodulaire. Classification complète, TR1 à TR5. Pas de scintigraphie pour une hypothyroïdie primaire typique : la glande ne fixe pas utilement la question diagnostique dans ce cadre, et l'examen irradie.", S(6)),
P("Cortisol si l'on suspecte la surrénale. Pas un scanner surrénalien systématique. Électrocardiogramme si cardiopathie suspectée.", S(9, 15)),
)

add("p10", "w-arbre", "Arbre",
P("Instable, froid, conscientiel : coma, autre fichier, glucocorticoïde puis lévothyroxine intraveineuse selon 2014, pas les comprimés dans la tubulure.", S(3)),
P("Stable, thyroxine libre basse, thyréostimuline haute. Chercher surrénale. Si oui, couvrir. Si non, Euthyrox. Début 25 µg si âgé, ancien ou cardiaque. Sinon début 25 à 50, entretien 100 à 200 µg, à jeun, contrôle dans quatre à six semaines.", S(9)),
P("Thyroxine libre normale : ne pas entrer dans cet arbre. C'est l'infraclinique. Thyroxine libre basse et thyréostimuline non haute : central, imagerie et autres axes, pas une dose de Hashimoto.", S(1)),
P("Cause réversible, phase basse de thyroïdite : on peut substituer transitoirement et réévaluer l'arrêt, plutôt que graver « à vie » le premier mois. Après thyroïdectomie ou iode radioactif, c'est à vie.", S(1, 9)),
)

add("p11", "w-ttt", "Lévothyroxine",
P("Euthyrox, numéro 54949. Hypothyroïdie : dose initiale souvent 25 à 50, augmentation toutes les 2 à 4 semaines, entretien 100 à 200 µg par jour. Personne âgée, hypothyroïdie de longue date, endocrinopathie ou cardiopathie : début à 25 µg, paliers prudents, entretien plus bas. La thyréostimuline du sujet âgé est naturellement un peu plus haute : une petite augmentation n'est pas à elle seule une indication, phrase lue dans la même notice.", S(9)),
P("Prise le matin. Eltroxine, numéro 29812, précise 30 minutes avant le petit-déjeuner, en une fois. Avant un an, Euthyrox : au moins une demi-heure avant le premier repas, comprimé délayé dans un peu d'eau, suspension faite juste avant. On n'écrase pas dans le biberon de lait du matin.", S(9, 15)),
P("Cible. Thyréostimuline dans les bornes du laboratoire, pas au-dessous de 0,4 mU/l selon la mise en garde de la revue, à cause de l'os et de la fibrillation. Contrôle trois mois après l'introduction dans la revue, et quatre à six semaines après chaque changement. Puis une fois par an, plus souvent si grossesse, œstrogènes ou variation de poids.", S(1)),
P("Contre-indications lues : insuffisance cardiaque avec tachycardie, pancardite aiguë, myocardite aiguë, infarctus aigu, angine de poitrine, troubles hypophysaires non traités, troubles surrénaliens non traités. Le début à 25 µg ne lève pas l'infarctus aigu.", S(9)),
P("Interactions. Calcium, fer, hydroxyde d'aluminium, cholestyramine : absorption moindre, à espacer. Inducteurs : recontrôle, on n'augmente pas de mémoire. La dose associée à un thionamide, dans le tableau d'Euthyrox, est 25 à 100 µg : ce n'est pas le schéma de l'hypothyroïdie primaire isolée.", S(1, 9)),
P("Il n'existe pas, dans l'index parcouru, de lévothyroxine intraveineuse. On ne présente pas les comprimés comme injectables. La dose de charge du coma, 200 à 400 microgrammes, reste dans le chapitre du coma et dans la recommandation de 2014.", S(3, 9)),
)

add("p11", "w-enf", "Enfant",
P("Dès 12 ans, posologie adulte. Avant 12 ans, la dose par kilogramme est plus haute et individuelle. Tableau lu : 0 à 6 mois, 25 à 75 µg, soit 10 µg par kilogramme. 6 à 12 mois, 50 à 75 µg, soit 8 µg par kilogramme. 1 à 5 ans, 75 à 100 µg, soit 5 à 6 µg par kilogramme. 6 à 12 ans, 100 à 150 µg, soit 4 à 5 µg par kilogramme. Paliers toutes les 2 à 4 semaines.", S(9)),
P("Le nourrisson se juge aussi sur la croissance, le pouls, les selles, pas seulement sur un chiffre. Eltroxine mentionne, pour le crétinisme, une adaptation clinique. On suit le tableau en microgrammes d'Euthyrox, qui est la spécialité dont les lignes sont claires, plutôt qu'une conversion depuis une autre notice.", S(9, 15)),
P("Un enfant sous lithium ou après une irradiation cervicale se surveille. On n'attend pas le retard scolaire pour doser si le contexte est là."),
)

add("p12", "w-prev", "Prévention du surdosage et de l'oubli",
P("La boîte du matin, à jeun, avant le café et loin du calcium du petit-déjeuner. Une thyréostimuline qui reste haute chez un patient « observant » est souvent une prise avec le fer ou le calcium. On corrige l'heure avant de monter la dose.", S(1, 9)),
P("Ordonnance renouvelée avant la fin. L'arrêt provoque le retour des symptômes en semaines, et chez le fragile un glissement vers le coma. On le dit."),
P("Contrôle après chaque changement de marque ou de dose, et en cas de grossesse. On évite la thyréostimuline trop basse. La revue cite le plancher de 0,4 mU/l.", S(1)),
P("Ne pas introduire l'hormone le jour où l'on découvre une hyponatrémie et une hypotension sans avoir pensé au cortisol. C'est la prévention de la crise surrénale, pas un luxe.", S(1, 9)),
)

add("p13", "w-cles", "Points d'examen",
P("Primaire : thyroxine libre basse, thyréostimuline haute, souvent au-dessus de 10 mU/l. Centrale : thyréostimuline qui ne monte pas. Infraclinique : thyroxine libre normale. Trois noms, trois conduites.", S(1)),
P("Euthyrox 54949. Début 25 µg si âgé, ancien ou cardiaque. Entretien 100 à 200 µg. À jeun. Enfant : tableau par âge, de 25 à 75 µg chez le tout-petit jusqu'à 100 à 150 µg entre 6 et 12 ans. Contre-indiqué si infarctus aigu ou surrénale non traitée.", S(9)),
P("Anticorps : 4,3 % par an de passage à la forme franche s'ils sont là, 2,3 % sinon. À dix ans, 43 % contre 23 %.", S(1)),
P("Pas de lévothyroxine pour une basse T3 de réanimation. Pas de dose intraveineuse inventée pour la forme de ville. Le coma est ailleurs.", S(3)),
)

add("p14", "w-pieges", "Pièges",
P("Rassurer parce que la thyréostimuline est à 2 mU/l alors que la thyroxine libre est à 6 pmol/l. C'est central ou un autre piège, pas une thyroïde saine.", S(1)),
P("Donner 100 µg le premier jour à un homme de 78 ans coronarien. La notice dit 25 µg.", S(9)),
P("Injecter les comprimés. Il n'y a pas de forme intraveineuse dans l'index.", S(9)),
P("Traiter une basse T3 de pneumonie. Recommandation contre.", S(3)),
P("Oublier le calcium du matin et monter la dose chaque mois. L'absorption est le problème.", S(1)),
P("Appeler primaire une thyréostimuline à 7 mU/l avec une thyroxine libre normale. C'est l'infraclinique, traitement controversé.", S(1)),
P("Commencer l'hormone devant une suspicion d'Addison. Contre-indication tant que la surrénale n'est pas traitée.", S(9)),
)

add("p14", "w-cas", "Cas corrigé",
P("Énoncé. Femme de 71 ans, fatigue et frilosité depuis six mois, poids plus 3 kg. Pouls 58. Température 36,4 °C. Elle répond, elle marche. Peau sèche. Thyroxine libre 7 pmol/l pour une borne basse à 9. Thyréostimuline 38 mU/l. Anticorps anti-thyroperoxydase positifs. Antécédent d'angor stable, pas de douleur ce jour. Natrémie normale, pression 138/82 mmHg. Que démarrez-vous, et que refusez-vous ?"),
P("Correction. Forme primaire franche : thyroxine libre basse, thyréostimuline très au-dessus de 10 mU/l, anticorps présents. Pas un coma : elle est réveillée, pas hypothermique au sens du chapitre du coma. Pas d'argument fort pour une surrénale aiguë : pression tenue, natrémie dite normale. On peut commencer l'oral. On ne commence pas à la dose d'entretien.", S(1, 3)),
P("Euthyrox, numéro 54949. Elle a 71 ans et un angor stable, pas un infarctus aigu. Le début lu pour la personne âgée ou cardiaque est 25 µg. On n'écrit pas 100 µg « pour aller plus vite ». On augmente plus tard, par paliers de plusieurs semaines, sous contrôle. Prise le matin à jeun, loin du calcium. Contrôle dans quatre à six semaines, pas dans trois jours. Cible : ramener la thyréostimuline vers les bornes sans passer sous 0,4 mU/l.", S(1, 9)),
P("On refuse une forme intraveineuse inexistante dans l'index. On refuse d'arrêter un éventuel bêtabloquant de l'angor pour « laisser le cœur accélérer ». On explique que l'amélioration clinique prend des semaines. On note les anticorps, qui ici confirment Hashimoto mais ne changent plus l'indication, déjà posée par la thyroxine libre basse. On donne un rendez-vous et une ordonnance assez longue pour ne pas qu'elle s'arrête.", S(1, 9)),
P("Si la pression avait été à 80 mmHg et le sodium à 124 mmol/l, on n'aurait pas commencé. On aurait dosé le cortisol et couvert avant. Ce n'est pas le cas écrit. On le dit pour montrer que le cas change avec deux chiffres, et que la contre-indication surrénalienne n'est pas théorique.", S(9)),
)

LONG = "".join([
P("Semaines 0 à 4. La patiente prend 25 µg chaque matin, à jeun. On ne juge pas l'échec sur une fatigue encore présente à dix jours : la thyréostimuline met du temps. On vérifie qu'elle n'a pas d'angor croissant. S'il apparaît, on suspend et on revoit, parce que l'angine de poitrine figure parmi les contre-indications de la notice quand elle est active.", S(9)),
P("Semaines 4 à 8. Dosage. Si la thyréostimuline est encore très haute et la clinique tolérée, on monte d'un palier, de l'ordre de 25 µg, pas d'un doublement agressif chez cette patiente cardiaque. La notice parle d'augmentations de 25 à 50 toutes les 2 à 4 semaines dans le schéma général, et de paliers plus lents chez le fragile. On choisit le lent.", S(9)),
P("Mois 3. La revue contrôle à trois mois après l'introduction. On vise une thyréostimuline dans les bornes, entretien souvent entre 100 et 200 µg chez l'adulte, mais chez elle l'entretien peut rester plus bas. On n'atteint pas 200 µg par principe. On s'arrête quand le chiffre et le cœur sont d'accord.", S(1, 9)),
P("Année suivante. Dosage annuel, plus tôt si le poids change beaucoup, si elle commence un œstrogène, si elle est enceinte ce qui est ici improbable, ou si un inducteur enzymatique est ajouté. On redit le calcium et le fer. Une thyréostimuline qui remonte après des mois stables fait chercher l'observance avant une maladie nouvelle.", S(1)),
P("Hashimoto et nodule. Si un nodule apparaît, on le classe. Un nodule solide très hypoéchogène, marge irrégulière, plus haut que large, foyers ponctués, dépasse 7 points : TR5, cytoponction dès 1 cm. L'hypothyroïdie auto-immune n'est pas un certificat de bénignité. On ne « surveille dans six mois » un TR5 de 14 mm.", S(6)),
P("Amiodarone chez un autre patient du même après-midi. Thyréostimuline 14 mU/l, thyroxine libre basse : hypothyroïdie induite franche. Lévothyroxine, amiodarone maintenue si le cardiologue la veut. Cible européenne : thyroxine libre et triiodothyronine libre normales, thyréostimuline dans le haut de la norme ou encore un peu haute mais sous 10 mU/l, pour éviter le surdosage chez un cœur malade. Ce n'est pas la cible de la femme de 71 ans sans amiodarone, dont on cherche une thyréostimuline dans les bornes.", S(4, 9)),
P("Phase basse après une thyroïdite. Homme de 40 ans, douleur cervicale il y a six semaines, maintenant fatigué, thyroxine libre basse, thyréostimuline haute. On peut substituer pour traverser la phase, à dose modérée, et prévoir un essai d'arrêt dans quelques mois. On ne grave pas « Hashimoto à vie » sans anticorps et sans recul. On ne donne pas non plus de carbimazole : la phase haute est passée.", S(1)),
P("Ce qu'on dit au patient. Le comprimé remplace ce que la glande ne fait plus. Il se prend à jeun, tous les jours, y compris quand on se sent bien. On augmente lentement à cause du cœur. Les effets d'un excès ressemblent à Basedow : palpitations, amaigrissement, tremblement. On les signale. On ne double pas la dose un jour où l'on a oublié la veille : on reprend le lendemain la dose habituelle.", S(9)),
P("Grossesse d'une autre patiente, 28 ans, déjà substituée à 100 µg. On l'adresse. Les besoins montent. On s'aligne sur la borne locale, ou à défaut sur environ 4,0 mU/l (ATA, 2017) ou sur 2,5 mU/l, 3,0 mU/l et 3,5 mU/l (ETA, 2014). On contrôle plus souvent, comme la revue le demande en cas de grossesse. On ne stoppe pas la lévothyroxine : le manque est pire.", S(1)),
P("Erreur de laboratoire à ne pas traiter. Thyroxine libre basse, thyréostimuline basse, patiente sous biotine ? La biotine baisse plutôt la thyréostimuline et monte les hormones libres. L'inverse n'est pas le piège classique. Devant un profil incohérent avec la clinique, on refait le dosage, on demande les compléments, on n'ajuste pas la dose sur un tube douteux.", S(7)),
])
fens.append(("p12", "w-sem", "Les semaines qui suivent", LONG))
fens.append(("p11", "w-plus", "L'année d'après et les autres patients", PLUS))

if __name__ == "__main__":
    # bouton déjà? ajouter dans p12 si besoin — le point p12 a w-prev. On ajoute le bouton dans l'île.
    points["p12"] = P("À jeun, loin du calcium et du fer, contrôle après chaque changement. La ", btn("w-prev", "prévention"), " et les ", btn("w-sem", "semaines"), " évitent le surdosage et l'oubli.", S(1, 9))
    print(rendre(3, "Hypothyroïdie primaire", ess, points, fens))
