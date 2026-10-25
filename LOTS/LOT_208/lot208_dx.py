# -*- coding: utf-8 -*-
"""Monographies DX.5 à DX.10 du LOT_208. Importé par gen_lot208_b.py."""
from gen_lot208_b import (
    block, e, inline, p, point, src, table, td, wrap_dx, NB,
)

RANG5 = f"5e rang — fréquence non quantifiée (Suisse)"
RANG6 = f"6e rang — fréquence non quantifiée (Suisse)"
BADGE7 = f"16,4{NB}% en 2022 [S508]"
RANG8 = f"8e rang — fréquence non quantifiée (Suisse)"
RANG9 = f"9e rang — fréquence non quantifiée (Suisse)"
RANG10 = f"10e rang — fréquence non quantifiée (Suisse)"


def badge(text):
    return f" <span style='font-size:0.8em;color:#2e8b57;'>{e(text)}</span>"


def corr_table():
    return table(
        ["Lésion ou perturbation", "Exploration qui la montre", "Conduite qui la corrige"],
        [
            [td("Le LDL et la pression restent élevés pendant des décennies, et le risque cumulé dépasse le risque à dix ans."),
             td("Le médecin calcule SCORE2 ou le score AGLA, puis il demande le bénéfice vie entière sur un outil qui l'affiche."),
             td("Il agit d'abord sur le tabac et le mode de vie. Il ne donne pas de dose ici, parce que l'information professionnelle n'a pas été ouverte.")],
            [td("Le calcium coronaire dépasse ce qui est attendu pour l'âge et le sexe."),
             td("Le score calcique sans injection, réservé au voisinage d'un seuil de décision."),
             td("Il reclasse le risque. Il ne traite pas le calcium lui-même.")],
            [td("L'éthanol lèse le foie, favorise des cancers et provoque des blessures."),
             td("L'anamnèse en grammes et en verres, selon les seuils Obsan."),
             td("Il propose l'intervention brève et l'orientation. Il ne recopie aucune dose de médicament de l'alcoolodépendance.")],
            [td("Le stress psychosocial et le revenu bas accompagnent la maladie athéromateuse."),
             td("Les questions de l'ESC sur le travail, l'argent, la famille et la solitude."),
             td("Il traite la détresse et les obstacles d'observance. Il ne multiplie pas le score par un coefficient britannique.")],
            [td("Les descendants solides du radon irradient le poumon."),
             td("La mesure agréée du logement, en becquerels par mètre cube."),
             td("Le propriétaire assainit selon l'ORaP. Le médecin ajoute l'arrêt du tabac.")],
            [td("Une maladie monogénique ou un agrégat familial change la catégorie avant tout calcul."),
             td("L'arbre familial, puis une analyse seulement après conseil LAGH."),
             td("Il oriente. Il ne prescrit pas un test présymptomatique sans conseil ni délai de réflexion.")],
        ],
    )


def dx5():
    t = inline(
        "risque vie entière",
        "L'ESC 2021 définit ce risque comme l'âge auquel la probabilité atteint 50 % qu'une personne ait déjà eu un événement cardiovasculaire ou soit morte.",
        "Le bénéfice vie entière est la différence, en années, entre cet âge avec le traitement envisagé et le même âge sans ce traitement.",
        "Il n'existe pas, dans ce texte, de seuil formel de traitement fondé sur le seul bénéfice vie entière.",
        "Piège : annoncer une réduction relative de 25 % à un adulte jeune dont le risque à dix ans est bas. L'ESC demande le risque absolu."
        + src("S501"),
    )
    inner = []
    inner.append(point("1", "Définition et sémantique", "".join([
        p(f"Le {t} n'est pas une maladie, et il ne remplace pas le risque à dix ans."),
        p("SCORE2 estime, chez une personne apparemment en bonne santé de 40 à 69 ans, le risque à dix ans d'infarctus ou d'accident vasculaire cérébral, fatal ou non."),
        p("Le calculateur AGLA, lui, estime un événement coronarien fatal ou un infarctus non fatal, de 20 à 69 ans, sans diabète."),
        p("Ces deux outils ne mesurent donc pas le même événement. Le médecin nomme l'outil avant de citer un pourcentage."),
        block("Fenêtre 1.1 — Trois horizons que l'étudiant mélange", "".join([
            p("L'horizon de dix ans répond à la question : quel événement peut survenir pendant la décennie qui vient ?"),
            p("L'horizon vie entière répond à une autre question : à quel âge le risque cumulé atteint-il une chance sur deux ?"),
            p("Le bénéfice vie entière répond à une troisième question : combien d'années sans événement le traitement ajoute-t-il, en moyenne ?"),
            p("Piège d'examen : traiter ces trois nombres comme s'ils étaient interchangeables."),
            p("Source : [S501]."),
        ])),
    ])))
    inner.append(point("2", "Épidémiologie (Suisse, puis Europe)", "".join([
        p("L'ESC place la Suisse dans la liste des pays à faible risque des abaques SCORE2, avec la Belgique, le Danemark, la France, Israël, le Luxembourg, la Norvège, l'Espagne, les Pays-Bas et le Royaume-Uni."),
        p("Les femmes de moins de 50 ans et les hommes de moins de 40 ans ont presque toujours un risque à dix ans bas, même lorsque les facteurs modifiables sont défavorables."),
        p("Leur risque sur la vie entière peut néanmoins être très élevé. C'est le fait qui justifie ce DX."),
        p("La fréquence suisse des adultes jeunes ainsi reclassés n'a pas été trouvée dans les sources ouvertes aujourd'hui. Le badge reste donc un rang, et non un pourcentage."),
        p("SCORE2 a été construit pour l'Europe de 40 à 69 ans, sans antécédent cardiovasculaire ni diabète. Le risque absolu d'un même profil varie fortement d'une région à l'autre."),
        block("Fenêtre 2.1 — Pourquoi un pourcentage suisse manque", "".join([
            p("Aucune page OFS ou Obsan lue aujourd'hui ne donne la part des moins de 50 ans dont le risque à dix ans est bas et le risque vie entière élevé."),
            p("Inventer ce pourcentage serait plus dangereux qu'un rang honnête."),
            p("L'enjeu de santé publique reste lisible : un adulte jeune traité trop tôt reçoit des années de médicament pour un bénéfice absolu faible, et un adulte jeune rassuré à tort accumule l'exposition."),
            p("Source : [S501], [S502]."),
        ])),
    ])))
    inner.append(point("3", "Physiopathologie", "".join([
        p("L'âge domine le risque à dix ans, parce que l'athérome a eu le temps de se constituer."),
        p("Chez le sujet jeune, le même LDL et la même pression agissent plus longtemps. L'ESC rappelle que de petites différences de LDL ou de pression systolique, maintenues toute la vie, changent fortement le risque, d'après les études de randomisation mendélienne qu'elle cite."),
        p("Le traitement corrige donc une exposition, et non un score. Le tabac, le LDL et la pression sont les trois leviers nommés pour le bénéfice vie entière dans les calculateurs que l'ESC indique."),
        corr_table(),
        p("Le tableau relie la perturbation, l'exploration et la conduite. Il ne donne aucune dose."),
        block("Fenêtre 3.1 — De l'exposition au signe, sans sauter d'étape", "".join([
            p("Les lipoprotéines qui contiennent l'apolipoprotéine B traversent l'intima et y restent d'autant plus que la concentration et la durée augmentent."),
            p("La pression élevée épaissit la paroi et favorise la plaque. Le tabac ajoute l'inflammation, la dysfonction endothéliale et la thrombose."),
            p("Le score à dix ans comprime cette histoire en une probabilité de décennie. Il devient bas lorsque l'âge est bas, même si la pente future est forte."),
            p("Piège : croire que le mécanisme s'arrête parce que le chiffre à dix ans est rassurant."),
            p("Source : [S501]."),
        ])),
    ])))
    inner.append(point("4", "Démarche diagnostique", "".join([
        p("Le médecin exclut d'abord les situations où l'on ne calcule pas un score de personne apparemment saine."),
        p("La maladie athéromateuse déjà établie, le diabète avec atteinte d'organe sévère, l'insuffisance rénale sévère et l'hypercholestérolémie familiale avec un facteur majeur classent d'emblée en risque très élevé sur la page AGLA."),
        p("Viennent ensuite les hypothèses fréquentes : risque à dix ans vraiment bas, risque intermédiaire que les modificateurs font bouger, et risque vie entière élevé chez un fumeur jeune."),
        table(
            ["Hypothèse à ne pas manquer", "Ce qui tranche", "Piège"],
            [
                [td("Maladie athéromateuse déjà constituée."), td("L'anamnèse d'infarctus, d'accident vasculaire, d'artériopathie ou une plaque déjà prouvée."), td("Calculer un SCORE2 de prévention primaire.")],
                [td("Hypercholestérolémie familiale."), td("Le LDL très élevé et l'histoire familiale, puis un avis spécialisé. Les points complets d'un score clinique n'ont pas été recopiés ici."), td("Rassurer parce que le risque à dix ans est bas.")],
                [td("Diabète ou maladie rénale qui change la catégorie."), td("La page AGLA donne les seuils de DFGe et d'albuminurie."), td("Utiliser le calculateur des personnes saines.")],
                [td("Sujet jeune à risque vie entière élevé."), td("Les facteurs modifiables persistent, et l'outil vie entière montre un bénéfice."), td("Citer seulement la réduction relative.")],
            ],
        ),
    ])))
    inner.append(point("5", "Anamnèse ciblée et drapeaux rouges", "".join([
        p("Chaque question cherche une variable du score ou un modificateur que le score ignore."),
        p("Le médecin demande le tabac, parce que l'arrêt est le levier dont l'ESC affiche le bénéfice vie entière, et parce qu'un fumeur de moins de 40 ans peut avoir un risque à dix ans bas."),
        p("Il demande les événements coronariens ou vasculaires précoces au premier degré, parce que cette information déclenche une évaluation complète même si elle n'améliore que marginalement la prédiction."),
        p("Il demande la prééclampsie, la ménopause précoce et les maladies inflammatoires, parce que l'ESC les compte parmi les modificateurs, surtout près d'un seuil."),
        block("Fenêtre 5.1 — Drapeaux qui interdisent la reassurance", "".join([
            p("Une douleur thoracique d'effort, un déficit neurologique transitoire ou une claudication font sortir de la prévention primaire."),
            p("Un xanthome tendineux ou un arc cornéen précoce oriente vers une hypercholestérolémie familiale, et non vers un simple conseil de mode de vie."),
            p("Une grossesse actuelle change les examens et les médicaments. Aucune dose n'est donnée ici."),
            p("Source : [S501], [S505], [S506]."),
        ])),
    ])))
    inner.append(point("6", "Examen physique ciblé, région par région", "".join([
        p("Le médecin décrit d'abord le normal. Une pression répétée et concordante, des pouls présents, l'absence de souffle et l'absence de xanthome ne prouvent pas que le risque vie entière est bas."),
        p("Il mesure la pression au bras, après repos, aux deux bras si les chiffres divergent, parce que la pression systolique entre dans AGLA et dans SCORE2."),
        p("Il palpe les pouls et il ausculte les trajets artériels, parce qu'un souffle ou un pouls aboli signe une maladie déjà constituée."),
        p("Il cherche les xanthomes tendineux et l'arc cornéen avant 45 ans, parce que ces signes orientent vers une maladie monogénique du LDL."),
        p("La technique et la valeur de chaque signe sont reprises dans la fenêtre."),
        block("Fenêtre 6.1 — Technique et valeur", table(
            ["Signe", "Comment on le cherche", "Ce qu'il vaut"],
            [
                [td("Pression systolique."), td("Le patient est assis, le bras est à hauteur du cœur, et la mesure est répétée."), td("Elle alimente le score. Une seule mesure de cabinet ne pose pas l'étiquette.")],
                [td("Souffle carotidien ou fémoral."), td("L'auscultation précède la décision d'imagerie."), td("Il suggère une plaque. Il ne quantifie pas le risque vie entière.")],
                [td("Xanthome."), td("Le médecin palpe le tendon d'Achille et les extenseurs des doigts."), td("Il oriente vers l'hypercholestérolémie familiale. Son absence ne l'exclut pas.")],
                [td("Poids et tour de taille."), td("La mesure est faite, puis elle est interprétée avec le contexte."), td("L'obésité est un modificateur clinique sur la page EAS. Elle ne remplace pas le score.")],
            ],
        ) + p("Source : [S501], [S505], [S506].")),
    ])))
    inner.append(point("7", "Approche syndromique", "".join([
        p("Trois situations reviennent en consultation de prévention."),
        block("7.1 Adulte jeune dont le chiffre à dix ans rassure", "".join([
            p("Signes fonctionnels : il ne se plaint de rien, ou il dit qu'un précédent calcul l'a rassuré."),
            p("Signes physiques : la pression peut déjà être élevée, et le reste de l'examen peut être normal."),
            p("Mécanisme : l'âge abaisse le risque à dix ans alors que l'exposition continue."),
            p("Le médecin explique l'âge vasculaire ou les années gagnées, sans inventer le pourcentage."),
        ])),
        block("7.2 Femme après une prééclampsie", "".join([
            p("Signes fonctionnels : la grossesse est terminée, et la patiente se croit revenue au risque de base."),
            p("Signes physiques : la pression peut être normale ce jour-là."),
            p("Mécanisme : l'ESC compte les désordres hypertensifs de la grossesse parmi les modificateurs."),
            p("Le médecin les écrit dans le dossier et il recalcule plus tard, parce que le score seul les ignore."),
        ])),
        block("7.3 Personne déjà malade que l'on score à tort", "".join([
            p("Signes fonctionnels : angor, claudication ou déficit déjà résolu."),
            p("Signes physiques : souffle, pouls aboli ou cicatrice de sternotomie."),
            p("Mécanisme : la plaque est déjà là. Le score de personne saine ne s'applique plus."),
            p("Conduite : prévention secondaire, sans nouveau calcul de SCORE2 primaire."),
        ])),
    ])))
    inner.append(point("8", "Diagnostic positif et critères", "".join([
        p("Il n'existe pas de critère de société savante qui « pose » le risque vie entière comme une maladie."),
        p("L'ESC dit quand cet horizon devient utile : la personne est apparemment en bonne santé et a moins de 50 ans, ou le risque à dix ans est bas malgré des facteurs défavorables."),
        p("Avant 50 ans, un risque SCORE2 d'au moins 7,5 % est en général un risque très élevé, et le traitement des facteurs est recommandé."),
        p("Un risque de 2,5 % à moins de 7,5 % est élevé : le traitement est envisagé avec les modificateurs, le bénéfice vie entière et la préférence de la personne."),
        p("Un risque inférieur à 2,5 % est faible à modéré : on ne traite pas les facteurs par médicament, sauf modificateur ou bénéfice vie entière jugé substantiel."),
        p("En dessous de 40 ans, les prédictions deviennent imprécises. L'ESC n'envisage en général ni hypolipémiant ni antihypertenseur, sauf hypercholestérolémie familiale ou trouble tensionnel spécifique. Le mode de vie maintenu toute la vie prime."),
        p("La page AGLA reprend les mêmes seuils d'âge pour son propre score et pour SCORE2. Elle ne republie pas les anciennes bandes uniques de 10 % et 20 %."),
        block("Fenêtre 8.1 — Ce qui ne suffit pas", "".join([
            p("Un LDL isolé ne suffit pas. Un parent malade sans âge de survenue ne suffit pas. Une application téléphonique dont la région n'est pas la Suisse ne suffit pas."),
            p("Le médecin écrit le nom de l'outil, l'âge, le statut diabétique et la région de risque."),
            p("Source : [S501], [S505]."),
        ])),
    ])))
    inner.append(point("9", "Examens complémentaires", "".join([
        p("Le gold standard du risque vie entière n'est pas une imagerie. C'est une estimation, et l'ESC dit qu'elle peut être approchée par l'expérience clinique ou par un score de vie entière."),
        p("En première intention, le médecin utilise AGLA entre 20 et 69 ans sans diabète, ou SCORE2 entre 40 et 69 ans sans diabète. À partir de 70 ans, AGLA renvoie à SCORE2-OP."),
        p("Le passage au bénéfice vie entière se fait lorsque le risque à dix ans est bas ou proche d'un seuil, surtout avant 50 ans. L'ESC cite des calculateurs en ligne, dont son application et U-Prevent, pour les années gagnées par l'arrêt du tabac, la baisse du LDL ou la baisse de la pression."),
        p("Le score calcique n'est pas l'examen du risque vie entière. Il est traité au DX.6, et seulement près d'un seuil."),
        table(
            ["Résultat", "Lecture", "Conduite"],
            [
                [td("SCORE2 inférieur à 2,5 % avant 50 ans."), td("Catégorie faible à modérée sur la page AGLA et dans l'ESC."), td("Mode de vie. Médicament seulement si modificateur ou bénéfice substantiel.")],
                [td("SCORE2 de 2,5 % à moins de 7,5 % avant 50 ans."), td("Catégorie élevée."), td("Discuter le traitement avec les modificateurs et le bénéfice vie entière.")],
                [td("SCORE2 d'au moins 7,5 % avant 50 ans."), td("Catégorie très élevée, parce que ce chiffre annonce un risque vie entière haut."), td("Traiter les facteurs. Le texte ESC le recommande.")],
                [td("Âge inférieur à 40 ans."), td("La prédiction est imprécise."), td("Mode de vie, sauf hypercholestérolémie familiale ou trouble tensionnel spécifique.")],
                [td("Diabète de type 2."), td("Le calculateur des personnes saines ne s'applique pas."), td("SCORE2-Diabète de 40 à 69 ans, si l'atteinte d'organe ne classe pas déjà en risque très élevé.")],
            ],
        ),
        p("Grossesse : on ne demande pas un score calcique ni un scanner pour « préciser » ce risque. L'estimation clinique et le report des examens irradiants priment."),
        p("DFGe inférieur à 30 mL/min/1,73 m² : la page AGLA classe déjà en risque très élevé, sans score de personne saine."),
        p("Allergie à l'iode et pacemaker : ils ne concernent pas le calculateur. Ils concernent le DX.6 si un scanner était envisagé."),
        block("Fenêtre 9.1 — Comment prescrire le calcul", "".join([
            p("Le médecin recueille l'âge, le sexe, le tabac, la pression systolique, le cholestérol total et le HDL pour SCORE2."),
            p("Pour AGLA, la page demande l'âge, la pression, le LDL, le HDL et les triglycérides, dans les fourchettes que le calculateur accepte."),
            p("Il note que les deux outils ne prédisent pas le même événement."),
            p("Source : [S503], [S504], [S501]."),
        ])),
    ])))
    inner.append(point("10", "Arbre décisionnel", "".join([
        p("Chaque branche nomme le signe ou le résultat qui fait choisir."),
        p("Si un événement athéromateux, une plaque prouvée, une maladie rénale sévère ou une hypercholestérolémie familiale avec facteur majeur est présent, le médecin ne calcule pas le score des personnes saines et il entre en risque très élevé."),
        p("Si la personne a un diabète de type 2, il utilise la voie diabète de la page AGLA."),
        p("Si la personne est apparemment saine et a moins de 40 ans, il priorise le mode de vie et il cherche l'exception familiale ou tensionnelle."),
        p("Si elle a de 40 à 69 ans, il calcule SCORE2 en région à faible risque pour la Suisse, puis il lit le seuil selon l'âge."),
        p("Si le résultat est proche d'un seuil ou si la personne a moins de 50 ans avec des facteurs lourds, il ajoute les modificateurs et le bénéfice vie entière."),
        p("Si le résultat est très bas et qu'aucun modificateur n'est présent, il explique, il fixe un délai de recalcul, et il n'ouvre pas un médicament pour « faire un chiffre »."),
    ])))
    inner.append(point("11", "Prise en charge selon les recommandations suisses", "".join([
        p("Le but n'est pas un pourcentage décoratif. Le but est d'éviter un événement cliniquement important, en commençant par les leviers dont le bénéfice absolu est le plus clair."),
        p("L'ordre est le suivant. Le médecin écarte d'abord la maladie déjà constituée. Il calcule ensuite l'outil valide. Il corrige par les modificateurs. Il traduit en années ou en fréquences naturelles. Il décide avec la personne. Il ne commence pas par une ordonnance."),
        block("Fenêtre 11.A — But", "".join([
            p("Avant 50 ans, un risque à dix ans d'au moins 7,5 % justifie le traitement des facteurs, parce que l'ESC le relie à un risque vie entière haut."),
            p("En dessous, le but est de ne pas médicaliser une exposition que le mode de vie peut réduire, tout en n'effaçant pas l'exposition cumulée."),
            p("Source : [S501]."),
        ])),
        block("Fenêtre 11.B — Moyens", "".join([
            p("Mesures générales : arrêt du tabac, activité, alimentation, poids, et pression confirmée hors du cabinet. Elles viennent en premier parce qu'elles agissent sur plusieurs maladies qui engagent le pronostic, pas seulement sur le cœur."),
            p("Médicaments : les classes possibles sont un hypolipémiant, un antihypertenseur, et un aide à l'arrêt du tabac. La classe se choisit selon la catégorie de risque et les comorbidités. Aucune spécialité, aucune dose, aucun schéma n'est écrit ici, parce qu'aucune information professionnelle suisse n'a été ouverte."),
            p("Le médecin dit au patient les effets qui comptent pour lui : douleurs musculaires sous statine, toux sous inhibiteur de l'enzyme de conversion, hypotension. Il vérifie ces effets dans l'information professionnelle au moment de la prescription réelle."),
            p("Volet social : le travail de nuit, le revenu et la solitude changent l'observance. L'ESC donne un risque relatif d'environ 1,76 pour le bas revenu et la mortalité cardiovasculaire, avec un intervalle de 1,45 à 2,14. Ce chiffre ne se transforme pas en pourcentage individuel."),
            p("Aptitude : un traitement préventif n'interdit pas la conduite. L'alcool et la somnolence, traités aux autres DX, le peuvent."),
            p("Source : [S501], [S505]."),
        ])),
        block("Fenêtre 11.C — Forme compliquée, minute par minute", "".join([
            p("La complication de ce DX n'est pas le risque vie entière lui-même. C'est la découverte, pendant la consultation, d'une urgence que le score ne doit pas retarder."),
            p("Minute 0 : douleur thoracique actuelle, déficit neurologique ou pression très élevée avec souffrance d'organe. Le médecin arrête le calcul et il traite l'urgence."),
            p("Heure 1 : si le symptôme a cédé et que l'examen est rassurant, il documente, il organise le bilan de la maladie suspectée, et il ne renvoie pas la personne avec un seul conseil de mode de vie."),
            p("Le lendemain : il reprend la prévention seulement lorsque l'urgence est écartée."),
        ])),
        block("Fenêtre 11.D — Situations spéciales, surveillance, sortie, pronostic", "".join([
            p("Grossesse et allaitement : le médecin ne commence pas un hypolipémiant « parce que le risque vie entière est haut ». Il reporte la décision médicamenteuse et il agit sur le tabac et la pression selon les filières obstétricales. Les doses ne sont pas ici."),
            p("Sujet âgé : l'horizon vie entière se raccourcit, et SCORE2-OP à partir de 70 ans intègre la mortalité concurrente. Un bénéfice qui demande de nombreuses années ne justifie pas d'ajouter un médicament à une personne fragile."),
            p("Enfant : ce DX ne se calcule pas avec SCORE2. Une histoire familiale lourde ou un LDL très élevé ouvre la voie du DX.10, pas un score d'adulte."),
            p("Foie et rein : une maladie hépatique active change le choix de l'hypolipémiant. Un DFGe inférieur à 30 mL/min/1,73 m² classe en risque très élevé sur la page AGLA, et les doses, non écrites ici, se réduisent selon l'information professionnelle."),
            p("Surveillance : le médecin recalcule lorsque l'âge, le tabac ou le traitement change. Il ne répète pas un scanner pour « suivre » le risque vie entière."),
            p("Fin de consultation : la personne peut partir lorsqu'elle a compris l'outil, le chiffre ou son absence, les modificateurs, la décision, et le délai de revue. Un symptôme d'alerte non exploré retient la sortie."),
            p("Pronostic : il n'y a pas de guérison d'un risque. Il y a une exposition qui baisse. Aucun essai de 2026 n'a été ouvert aujourd'hui sur un nouveau seuil suisse."),
            p("Source : [S501], [S504], [S505]."),
        ])),
    ])))
    inner.append(point("12", "Prévention", "".join([
        p("Primaire : ne pas fumer, confirmer la pression, et calculer avant de médicaliser. La Suisse étant en région à faible risque, un modèle d'une région à haut risque surestime le bénéfice."),
        p("Secondaire : si la maladie est déjà là, les cibles se durcissent et le score primaire sort du raisonnement."),
        p("Tertiaire : après un événement, la réadaptation et l'observance empêchent la récidive. Ce DX ne les décrit pas en détail."),
        p("Le vaccin, le dépistage des cancers et le radon ne se déduisent pas du SCORE2. Ils appartiennent aux autres facteurs de ce SSP, notamment le DX.9."),
    ])))
    inner.append(point("13", "Points clés", "".join([
        p("Le médecin nomme l'outil, parce qu'AGLA et SCORE2 ne prédisent pas le même événement."),
        p("Il refuse de rassurer un adulte jeune sur le seul risque à dix ans."),
        p("Il connaît les seuils avant 50 ans : moins de 2,5 %, de 2,5 % à moins de 7,5 %, et au moins 7,5 %."),
        p("Il n'ouvre en général pas un hypolipémiant ni un antihypertenseur avant 40 ans, hors exception familiale ou tensionnelle."),
        p("Il parle en risque absolu et en années gagnées, et il n'invente ni dose ni pourcentage non calculé."),
    ])))
    inner.append(point("14", "Pièges et questions fréquentes à l'examen fédéral suisse", "".join([
        p("Piège : appliquer les anciennes bandes AGLA de 10 % et 20 % à tout âge. La page lue le 24.10.2026 stratifie par âge. Bonne réponse : utiliser les seuils de la tranche d'âge."),
        p("Piège : multiplier le risque suisse par les coefficients ethniques britanniques de QRISK3. L'ESC les cite comme données du Royaume-Uni et souhaite des rapports propres au pays. Bonne réponse : ne pas les plaquer."),
        p("Piège : demander un score calcique parce que le sujet est jeune et inquiet. Bonne réponse : le réserver au voisinage d'un seuil, au DX.6."),
        p("Piège : citer un seuil Agatston de 100 comme s'il était dans l'ESC 2021. Bonne réponse : l'ESC compare le score à ce qui est attendu pour l'âge et le sexe."),
        p("Question : une femme de 36 ans fume et sa pression est haute. Son risque à dix ans est bas. Que fait-on ? Réponse : mode de vie en priorité, recherche d'une exception, et pas de médicament par réflexe."),
    ])))
    inner.append(atelier())
    inner.append(p("<strong>Question finale.</strong> Ces fenêtres permettent de choisir l'outil, de lire les seuils suisses et européens, et de ne pas médicaliser ni rassurer à tort. Elles ne remplacent pas le calcul réel ni l'information professionnelle au moment d'une ordonnance."))
    summary = "DX.5 — Risque cardiovasculaire vie entière du sujet jeune" + badge(RANG5)
    return wrap_dx(summary, "".join(inner))


def atelier():
    cases = [
        ("Un homme de 38 ans fume encore.", "Sa pression de repos est élevée, et il n'a pas de diabète.", "SCORE2 ne couvre pas cet âge avec la même validité que la tranche 40 à 69 ans.", "L'ESC juge les prédictions imprécises avant 40 ans et il place le mode de vie au premier plan.", "Le médecin cherche une hypercholestérolémie familiale avant de conclure que tout va bien."),
        ("Une femme de 44 ans ne fume plus depuis un an.", "Le calcul SCORE2, saisi dans l'outil et non de mémoire, tombe sous 2,5 %.", "Avant 50 ans, ce résultat est faible à modéré.", "Un médicament n'est pas la suite automatique.", "Le bénéfice vie entière n'est discuté que s'il paraît substantiel."),
        ("Un homme de 48 ans a un SCORE2 à 8 % en région suisse.", "Avant 50 ans, 7,5 % ou plus est un risque très élevé dans le texte ESC.", "Le traitement des facteurs est alors recommandé.", "Le médecin ne dit pas que le pourcentage est « seulement » un risque intermédiaire des anciennes bandes.", "Il vérifie qu'aucun symptôme ne fait sortir de la prévention primaire."),
        ("Une femme de 52 ans a un SCORE2 à 6 %.", "Entre 50 et 69 ans, la page AGLA place le risque élevé entre 5 % et moins de 10 %.", "Le seuil n'est donc pas celui des moins de 50 ans.", "Le médecin cite la tranche d'âge en même temps que le chiffre.", "Il ajoute les modificateurs seulement parce que le résultat est près d'une décision."),
        ("Un homme de 72 ans demande le même calcul que son fils.", "AGLA renvoie, à partir de 70 ans, vers SCORE2-OP.", "Le risque très élevé commence alors à 15 %, et le risque élevé à 7,5 %.", "Le bénéfice en années gagnées est plus court.", "La fragilité et les médicaments déjà pris entrent dans la décision."),
        ("Une femme de 61 ans a un diabète de type 2 sans atteinte d'organe connue.", "Le calculateur des personnes saines ne s'applique pas.", "La page AGLA ouvre SCORE2-Diabète entre 40 et 69 ans.", "Si une atteinte sévère existe déjà, la catégorie très élevée est posée sans ce calcul.", "Le médecin lit la définition d'atteinte d'organe sur la page avant de rassurer."),
        ("Un homme de 46 ans a un DFGe à 28 mL/min/1,73 m².", "La page AGLA classe la maladie rénale sévère en risque très élevé.", "Aucun SCORE2 de personne saine n'est nécessaire pour « adoucir » ce classement.", "Le médecin adapte les médicaments au rein au moment de la prescription, avec l'information professionnelle.", "Il n'invente pas la dose dans ce cours."),
        ("Une femme de 33 ans a un LDL très élevé et un père infarctus à 48 ans.", "Le risque à dix ans sera mécaniquement bas.", "Cette constellation oriente vers l'hypercholestérolémie familiale, pas vers la reassurance.", "L'exception avant 40 ans existe précisément pour cette maladie et pour certains troubles tensionnels.", "Le DX.10 reprend le conseil génétique si un test est envisagé."),
        ("Un homme de 57 ans a déjà une artériopathie.", "Le score primaire ne se calcule plus.", "La prévention devient secondaire.", "Intensifier les facteurs se discute avec la préférence et la fragilité, selon l'ESC.", "Un chiffre de personne saine serait une erreur de catégorie."),
        ("Une femme enceinte de 30 ans demande un « bilan de risque complet avec scanner ».", "Le risque vie entière ne se règle pas par un scanner.", "L'irradiation et les médicaments se reportent.", "Le tabac et la pression se prennent en charge dans la filière de grossesse.", "Aucune dose n'est écrite ici."),
        ("Un homme de 49 ans apporte un risque calculé avec un modèle américain.", "L'ESC et l'AGLA fournissent les outils valables pour cette consultation suisse.", "Le médecin refait le calcul avec SCORE2 en région à faible risque ou avec AGLA.", "Il n'additionne pas les deux pourcentages.", "Il explique la différence d'événement prédit."),
        ("Une femme de 66 ans a un risque SCORE2 juste sous le seuil de sa tranche.", "Les modificateurs peuvent encore changer la décision, parce que le résultat est proche du seuil.", "Un modificateur favorable doit pouvoir abaisser le risque, et pas seulement l'élever.", "L'ESC insiste sur cette symétrie.", "Le médecin ne collectionne pas les modificateurs si le risque est déjà très haut ou très bas."),
    ]
    blocks = []
    for i, (a, b, c, d, f) in enumerate(cases, 1):
        blocks.append(block(
            f"Atelier {i} — cas chiffré sans pourcentage inventé",
            "".join([p(a), p(b), p(c), p(d), p(f), p("Le pourcentage individuel, lorsqu'il dépend de lipides non donnés ici, se saisit dans l'outil. Il ne se devine pas.")]),
        ))
    return "<div style='margin:16px 0 10px;'><strong>Atelier — douze consultations</strong><br>" + "".join(blocks) + "</div>"


def dx6():
    term = inline(
        "score calcique coronaire",
        "L'ESC 2021 le décrit comme un modificateur qui peut faire monter ou descendre le risque, en plus des facteurs classiques.",
        "La recommandation lue dans le tableau est de classe IIb, niveau B : il peut être envisagé pour améliorer la classification autour des seuils de décision.",
        "S'il est présent, on le compare à ce qui est attendu pour le sexe et l'âge. Plus haut que prévu, le risque calculé augmente. Absent ou plus bas que prévu, le risque calculé diminue.",
        "Il ne dit ni la charge totale de plaque ni le degré de sténose, et il peut être nul chez un adulte d'âge moyen qui a une plaque molle non calcifiée."
        + src("S501"),
    )
    parts = []
    parts.append(point("1", "Définition et sémantique", "".join([
        p(f"Le {term} n'est pas un diagnostic d'angor, et il n'est pas un dépistage de masse."),
        p("Il quantifie le calcium des artères coronaires sur un scanner sans injection. Le nombre d'Agatston est l'unité historique de cette mesure. L'ESC 2021 ouvert aujourd'hui ne fixe pas un seuil unique, du type 100, pour reclasser."),
        p("La page de l'EAS, lue le même jour, affiche une ligne de classe IIa pour l'athérome infraclinique ou un score calcique augmenté, comme modificateur."),
        p("Les deux textes ne sont pas copiés l'un sur l'autre. Le cours suit la classe IIb du guide de prévention 2021, et il signale l'écart de la page EAS sans le transformer en nouvelle règle."),
    ])))
    parts.append(point("2", "Épidémiologie (Suisse, puis Europe)", "".join([
        p("La fréquence suisse des scores calciques réalisés en prévention n'a pas été trouvée dans les sources ouvertes aujourd'hui."),
        p("L'ESC rappelle que beaucoup de personnes se trouvent dans la zone grise autour des seuils, mais que la faisabilité et le coût limitent un modificateur dès qu'il devient un scanner."),
        p("Le bénéfice d'un programme systématique de scores calciques n'est pas établi par les pages lues. L'indication reste individuelle, près d'une décision."),
        p("La Suisse est un pays à faible risque sur les abaques SCORE2. Un scanner importé d'une stratégie de pays à haut risque ne se transpose pas tel quel."),
    ])))
    parts.append(point("3", "Physiopathologie", "".join([
        p("La plaque athéromateuse se calcifie lorsqu'elle vieillit. Le calcium vu au scanner est donc un témoin de plaque, et non la cause que l'on dissout."),
        p("Une plaque jeune, riche en lipides et pauvre en calcium, peut rompre alors que le score est encore nul. C'est le mécanisme du piège du zéro."),
        p("Le traitement qui réduit les événements agit sur le LDL, la pression et le tabac. Il ne « décalcifie » pas à titre de but."),
        table(
            ["Perturbation", "Exploration", "Conduite"],
            [
                [td("Plaque calcifiée plus abondante que pour l'âge et le sexe."), td("Score calcique comparé à la référence d'âge et de sexe."), td("Le risque calculé monte. Le traitement des facteurs se rediscute.")],
                [td("Absence de calcium alors qu'une plaque molle est possible."), td("Le zéro ne voit pas la plaque non calcifiée."), td("On ne blanchit pas un fumeur ou une personne déjà malade sur ce seul zéro.")],
                [td("Sténose et ischémie, que le score ne mesure pas."), td("Le scanner injecté ou une épreuve d'ischémie, seulement si la clinique le demande."), td("Une douleur d'effort ne se rassure pas par un score.")],
            ],
        ),
    ])))
    parts.append(point("4", "Démarche diagnostique", "".join([
        p("Avant le scanner, le médecin classe le risque par AGLA ou SCORE2 et il vérifie que la décision hésite vraiment."),
        p("Il exclut d'abord la maladie déjà symptomatique, le risque déjà très élevé et le risque déjà très bas sans modificateur, parce que le résultat ne changerait pas la conduite."),
        table(
            ["Situation", "Examen qui tranche", "Piège"],
            [
                [td("Douleur d'effort."), td("La filière de la douleur thoracique, pas le score de prévention."), td("Rassurer avec un score nul.")],
                [td("Risque déjà très élevé ou maladie établie."), td("La clinique et la page AGLA."), td("Ajouter un scanner qui ne change rien.")],
                [td("Risque près du seuil, personne asymptomatique."), td("Le score calcique peut être envisagé, classe IIb."), td("Le demander par routine.")],
                [td("Score impossible ou non souhaité."), td("La plaque carotidienne en échographie peut être envisagée, avec une définition précise de la plaque."), td("Utiliser l'épaisseur intima-média isolée, que l'ESC ne recommande pas.")],
            ],
        ),
    ])))
    parts.append(point("5", "Anamnèse ciblée et drapeaux rouges", "".join([
        p("Le médecin demande les symptômes, parce qu'un score de personne asymptomatique ne s'applique pas à une douleur."),
        p("Il demande le tabac, le diabète et l'histoire familiale, parce que le zéro calcique est moins rassurant lorsque ces facteurs existent. L'ESC ne donne pas la liste d'exclusion américaine. Il dit seulement que le zéro peut manquer une plaque molle."),
        p("Il demande si la personne peut rester allongée et si elle est enceinte, parce que le scanner irradie."),
        p("Drapeau rouge : douleur actuelle, dyspnée d'effort nouvelle, ou syncope. Le calculateur s'arrête."),
    ])))
    parts.append(point("6", "Examen physique ciblé, région par région", "".join([
        p("L'examen normal précède le scanner. Une auscultation sans souffle et des pouls présents n'excluent pas le calcium coronaire."),
        p("Le médecin prend la pression et il cherche les signes d'artériopathie, parce qu'ils peuvent classer la personne sans imagerie."),
        p("Il n'y a pas de manœuvre au lit qui mesure le score d'Agatston. Promettre le contraire est une erreur."),
    ])))
    parts.append(point("7", "Approche syndromique", "".join([
        block("7.1 Zone grise asymptomatique", "".join([
            p("Signes fonctionnels : aucun symptôme ischémique."),
            p("Signes physiques : examen sans signe d'artériopathie constituée."),
            p("Mécanisme : les facteurs placent le risque près d'un seuil, et le calcium peut départager."),
        ])),
        block("7.2 Zéro faussement blanc", "".join([
            p("Signes fonctionnels : le patient dit qu'on lui a promis un cœur normal."),
            p("Signes physiques : il peut fumer ou avoir un LDL haut."),
            p("Mécanisme : la plaque molle n'est pas calcaire. Le zéro ne la voit pas."),
        ])),
        block("7.3 Douleur que l'on déguise en prévention", "".join([
            p("Signes fonctionnels : oppression à l'effort."),
            p("Signes physiques : parfois aucun, au repos."),
            p("Mécanisme : la sténose et l'ischémie ne se lisent pas sur le calcium. La filière diagnostique de la douleur s'ouvre."),
        ])),
    ])))
    parts.append(point("8", "Diagnostic positif et critères", "".join([
        p("Le critère n'est pas un nombre d'Agatston unique dans l'ESC 2021. Le critère est la comparaison à ce qui est attendu pour l'âge et le sexe, chez une personne dont le risque calculé est autour d'un seuil."),
        p("Un score plus haut que prévu augmente le risque calculé. Un score absent ou plus bas que prévu le diminue."),
        p("Ce résultat ne pose pas le diagnostic de maladie coronaire sténosante. Il modifie une probabilité."),
        p("La collecte routinière d'autres imageries, en dehors du score calcique et de l'échographie de plaque carotidienne, est non recommandée dans le tableau ESC lu, en classe III."),
    ])))
    parts.append(point("9", "Examens complémentaires", "".join([
        p("Le gold standard de la sténose n'est pas le score calcique. Le texte ESC dit que le scanner injecté voit les sténoses, mais qu'on ne sait pas s'il classe mieux le risque que le calcium seul."),
        p("Première intention du reclassement : score calcique sans produit, si la décision hésite et si l'examen est disponible."),
        p("Alternative : plaque carotidienne, définie comme un épaississement focal d'au moins 50 % par rapport à la paroi voisine, ou une épaisseur focale d'au moins 1,5 mm qui entre dans la lumière."),
        p("L'épaisseur intima-média systématique n'est pas recommandée, faute de standard et de valeur ajoutée."),
        table(
            ["Résultat", "Signification selon l'ESC 2021", "Conduite"],
            [
                [td("Calcium absent ou plus bas que pour l'âge et le sexe."), td("Risque calculé plus bas."), td("On peut éviter d'intensifier, si le contexte clinique ne contredit pas le zéro.")],
                [td("Calcium plus haut que pour l'âge et le sexe."), td("Risque calculé plus haut."), td("On rediscute le traitement des facteurs.")],
                [td("Douleur d'effort."), td("Le score ne décrit pas la sténose."), td("On quitte cet examen de prévention.")],
                [td("Grossesse."), td("Irradiation sans bénéfice pour une décision qui peut attendre."), td("On ne prescrit pas le scanner.")],
                [td("Diabète de type 2."), td("La page AGLA écrit qu'il n'y a pas de preuve suffisante pour utiliser le score calcique ou l'épaisseur intima-média comme facteurs de risque dans le diabète de type 2."), td("On ne s'appuie pas sur cet examen pour classer ce diabète.")],
            ],
        ),
        p("Allergie à l'iode : elle concerne le scanner injecté, pas le score sans injection. Un pacemaker n'interdit pas, à lui seul, un scanner non injecté du calcium. La page lue ne détaille pas les incompatibilités d'appareil."),
    ])))
    parts.append(point("10", "Arbre décisionnel", "".join([
        p("Si la personne a une douleur d'effort, le médecin ouvre la filière clinique et il ne coche pas un score de prévention."),
        p("Si la catégorie est déjà très élevée ou déjà basse et stable, il n'ajoute pas le scanner."),
        p("Si la catégorie est au seuil, chez une personne asymptomatique, il peut envisager le score, classe IIb, après avoir dit l'irradiation et l'incertitude sur la plaque molle."),
        p("Si le score est impossible, il peut envisager la plaque carotidienne, et il ne mesure pas l'intima-média pour décider."),
        p("Si le résultat est plus haut ou plus bas que l'attendu, il monte ou il baisse le risque calculé, puis il rediscute. Il ne livre pas le nombre d'Agatston seul."),
    ])))
    parts.append(point("11", "Prise en charge selon les recommandations suisses", "".join([
        p("Le but du score est une meilleure décision, pas une image. Si l'image ne peut pas changer l'ordonnance ou le mode de vie, elle ne se demande pas."),
        p("L'ordre est clinique, puis calculateur, puis seulement ensuite le scanner."),
        block("Urgence chronologique", "".join([
            p("Minute 0 : douleur persistante, malaise ou signe neurologique. Le médecin n'envoie pas au score calcique."),
            p("Heure 1 : il sécurise la filière d'urgence habituelle."),
            p("Plus tard : le score de prévention ne se rattrape qu'une fois la personne asymptomatique et la décision vraiment indécise."),
        ])),
        p("Moyens non médicamenteux : expliquer le zéro, le tabac, l'activité. Moyens médicamenteux : ceux de la catégorie de risque enfin reclassée. Aucune dose n'est écrite."),
        p("Grossesse : pas de scanner. Sujet âgé : le calcium est fréquent, et la comparaison à l'âge devient indispensable pour ne pas tout classer en maladie. Enfant : examen hors sujet. Foie et rein : le produit iodé n'est pas nécessaire pour le score sans injection. La fonction rénale compte si l'on glisse vers un scanner injecté."),
        p("Surveillance : l'ESC lu aujourd'hui ne fixe pas un délai suisse de répétition. Le médecin ne reprend pas l'examen chaque année par habitude."),
        p("Sortie : la personne part avec une phrase claire. Soit l'examen n'est pas indiqué. Soit il est indiqué, avec son but. Soit le résultat a changé la catégorie, et la suite est nommée."),
        p("Pronostic : un zéro associé à un risque bas prédit moins d'événements que le calcul seul, dans le texte ESC, sans que ce cours recopie un pourcentage d'étude américaine."),
    ])))
    parts.append(point("12", "Prévention", "".join([
        p("Primaire : le score n'est pas un dépistage organisé. Secondaire : la maladie établie n'a pas besoin de lui pour être crue. Tertiaire : après un infarctus, la réadaptation ne passe pas par un score de calcium de routine."),
    ])))
    parts.append(point("13", "Points clés", "".join([
        p("Le médecin réserve le score au voisinage d'un seuil, chez une personne asymptomatique."),
        p("Il compare le résultat à l'âge et au sexe, et il ne récite pas un seuil américain de 100."),
        p("Il se souvient que zéro n'exclut pas une plaque molle."),
        p("Il connaît la classe IIb de l'ESC 2021, et il sait que la page EAS affiche une classe IIa qu'il ne substitue pas sans texte complet."),
        p("Il n'utilise pas l'intima-média isolée, et il n'utilise pas le score pour classer un diabète de type 2 selon la page AGLA."),
    ])))
    parts.append(point("14", "Pièges et questions fréquentes à l'examen fédéral suisse", "".join([
        p("Piège : scanner de tout homme de 50 ans. Bonne réponse : seulement si la décision hésite."),
        p("Piège : seuil d'Agatston 0 / 100 pris dans une recommandation américaine. Bonne réponse : comparaison à l'attendu, texte ESC 2021."),
        p("Piège : rassurer une douleur d'effort par un score nul. Bonne réponse : filière de la douleur."),
        p("Piège : mesurer l'intima-média pour reclasser. Bonne réponse : plaque carotidienne définie, ou score calcique."),
        p("Question : quelle classe dans le guide de prévention 2021 ? Réponse : IIb, niveau B."),
    ])))
    parts.append(p("<strong>Question finale.</strong> Le candidat sait quand ne pas demander l'examen, comment lire un résultat sans seuil américain, et comment ne pas manquer une douleur. Il prescrit encore la dose réelle dans l'information professionnelle, hors de ce texte."))
    return wrap_dx("DX.6 — Score calcique coronaire comme modificateur de risque" + badge(RANG6), "".join(parts))


def dx7():
    term = inline(
        "consommation d'alcool à risque",
        "Obsan la définit, à partir de 15 ans, comme une consommation chronique au-dessus des seuils, ou une consommation ponctuelle excessive, ou les deux.",
        "En 2022, 16,4 % de la population vivant en ménage privé était dans ce cas, contre 18,1 % en 2017.",
        "Les hommes étaient à 20,7 % et les femmes à 12,1 %. Les 20 à 24 ans étaient à 31,0 %, et les personnes au diplôme tertiaire à 17,1 %.",
        "Le chiffre vient de l'enquête suisse sur la santé, environ 22 000 personnes en 2022."
        + src("S508"),
    )
    parts = []
    parts.append(point("1", "Définition et sémantique", "".join([
        p(f"La {term} n'est pas synonyme d'alcoolodépendance."),
        p("Le risque chronique moyen va, par jour, de 20 à 40 g d'alcool pur chez la femme, soit 2 à 4 verres standard, et de 40 à 60 g chez l'homme, soit 4 à 6 verres."),
        p("Le risque chronique élevé dépasse 40 g chez la femme, soit plus de 4 verres, et 60 g chez l'homme, soit plus de 6 verres."),
        p("La lecture du texte Obsan donne 10 g par verre standard, puisque 20 g correspondent à 2 verres. Ce n'est pas une nouvelle norme inventée."),
        p("L'OFSP décrit en outre la consommation épisodique à risque : au moins 4 verres chez la femme ou 5 chez l'homme, au moins une fois par mois."),
        p("L'OFSP écrit qu'aucune quantité sans danger pour la santé et sans effet sur les cancers n'a été établie, et qu'un effet cardiovasculaire protecteur d'une consommation modérée n'est pas démontré de façon fiable."),
    ])))
    parts.append(point("2", "Épidémiologie (Suisse, puis Europe)", "".join([
        p("En 2022, 83 % de la population avait consommé de l'alcool, et environ 9 % au moins une fois par jour. Chez les plus de 65 ans, 21,4 % buvaient chaque jour."),
        p("En 2024, la consommation moyenne était de 7,6 litres d'alcool pur par personne de 15 ans et plus, contre 10,6 litres en 2001."),
        p("Près de 4 % ont une consommation chronique à risque, et près de 15 % une consommation épisodique à risque, soit 10,7 % des femmes et 18,9 % des hommes. Les hommes de 20 à 24 ans atteignent 35 % pour l'épisode."),
        p("L'OFSP estime que 250 000 à 300 000 personnes sont alcoolodépendantes, d'après le rapport de Kuendig de 2010 qu'il cite encore. Ce n'est pas une mesure de 2026."),
        p("En 2017, l'alcool a causé 1 553 décès entre 15 et 74 ans. Parmi eux, 36 % venaient de cancers, 21 % de troubles digestifs et hépatiques, et 21 % de blessures et d'accidents."),
        p("Les coûts directs de santé étaient de 447 millions de francs en 2017, et une étude citée par l'OFSP les estime à 513 millions en 2022. Le coût social annuel problématique est d'environ 2,8 milliards, dont 2,1 milliards de pertes de productivité."),
        p("En 2022, l'alcool était impliqué dans 13 % des accidents graves ou mortels de la route."),
    ])))
    parts.append(point("3", "Physiopathologie", "".join([
        p("L'éthanol et son métabolite, l'acétaldéhyde, lésent l'ADN et expliquent le lien avec les cancers. L'OFSP relie l'alcool à plus de 200 maladies et troubles, d'après l'OMS 2024 qu'il cite."),
        p("La consommation chronique détruit le foie, du foie gras jusqu'à la cirrhose, et elle favorise l'hypertension et les hémorragies."),
        p("La consommation ponctuelle massive déprime la vigilance et provoque les accidents, les violences et une part des suicides. Chez le jeune, les décès liés à l'alcool passent surtout par les blessures."),
        p("Il n'y a pas, dans les pages lues, un seuil « cardioprotecteur » à enseigner. L'OFSP attribue les anciens résultats favorables à des biais, notamment la comparaison avec d'anciens buveurs déjà malades."),
        table(
            ["Lésion", "Comment on la voit", "Ce qui la corrige"],
            [
                [td("Exposition répétée de la muqueuse et du foie."), td("Grammes par jour, enzymes et clinique hépatique si le contexte le demande."), td("Baisse ou arrêt. Pas de dose de médicament dans ce cours.")],
                [td("Ivresse aiguë et trauma."), td("Heure, quantité, traumatisme, hypoglycémie possible."), td("Sécuriser d'abord, puis l'entretien."),
                ],
                [td("Dépendance."), td("Perte de contrôle, sevrage, poursuite malgré les dommages."), td("Orientation spécialisée. Les médicaments existent en Suisse, mais leurs doses ne sont pas recopiées.")],
            ],
        ),
    ])))
    parts.append(point("4", "Démarche diagnostique", "".join([
        p("Le médecin cherche d'abord le danger immédiat : trauma, agitation, idée suicidaire, grossesse exposée, conduite imminente."),
        p("Il distingue ensuite l'épisode, le risque chronique et la dépendance, parce que les conduites diffèrent."),
        table(
            ["Hypothèse", "Ce qui tranche", "Piège"],
            [
                [td("Ivresse compliquée."), td("Conscience, glycémie, trauma, aspiration."), td("Laisser partir une personne qui va conduire.")],
                [td("Risque chronique sans dépendance."), td("Les grammes et les verres sur une semaine typique."), td("Parler d'un verre « bon pour le cœur ».")],
                [td("Dépendance."), td("Le contrôle perdu et le sevrage."), td("Se contenter d'un conseil unique.")],
                [td("Consommation cachée chez la personne âgée."), td("Chutes, confusion, interaction avec les médicaments."), td("Attribuer tout au grand âge.")],
            ],
        ),
    ])))
    parts.append(point("5", "Anamnèse ciblée et drapeaux rouges", "".join([
        p("Le médecin demande la quantité sur une semaine ordinaire et la quantité sur une occasion, parce que les deux seuils suisses ne se recouvrent pas."),
        p("Il demande la grossesse, l'allaitement, la conduite, le travail à risque et les médicaments sédatifs, parce que l'OFSP compte ces situations comme inappropriées même à plus faible dose."),
        p("Il demande le sevrage : tremblement matinal, sueurs, crise comitiale. Ces signes imposent une filière de sevrage, et non un conseil différé."),
        p("Drapeaux : idée suicidaire, violence, vomissements sanglants, jaunisse, confusion."),
    ])))
    parts.append(point("6", "Examen physique ciblé, région par région", "".join([
        p("Le normal existe : une personne peut boire au-dessus du seuil et n'avoir encore aucun signe. L'absence de signe ne innocente pas la quantité."),
        p("Le médecin cherche l'haleine, la coordination, les tremblements et les stigmates hépatiques, après avoir regardé l'état général."),
        p("Il palpe l'abdomen et il cherche une ascite ou une hépatomégalie, parce que ces signes déplacent la personne vers la maladie constituée."),
        p("Il inspecte les traumatismes, parce que l'épisode massif tue d'abord par la blessure."),
        block("Technique", "".join([
            p("Le tremblement de sevrage se cherche mains tendues, au repos, le matin ou à distance du dernier verre."),
            p("L'astérixis se cherche poignets en extension, et il oriente vers l'encéphalopathie, pas vers une simple ivresse."),
            p("La pression se mesure, parce que l'alcool chronique l'élève. La valeur ne se devine pas."),
        ])),
    ])))
    parts.append(point("7", "Approche syndromique", "".join([
        block("7.1 Épisode du week-end", "".join([
            p("Signes fonctionnels : quantité brève, amnésie, regret."),
            p("Signes physiques : souvent aucun le lundi."),
            p("Mécanisme : toxicité aiguë et trauma, plus que cirrhose."),
        ])),
        block("7.2 Usage quotidien du sujet âgé", "".join([
            p("Signes fonctionnels : verre quotidien, chutes, sommeil fractionné."),
            p("Signes physiques : tremblement fin, hygiène qui se dégrade."),
            p("Mécanisme : le cerveau âgé et les médicaments abaissent la tolérance. 21,4 % des plus de 65 ans boivent chaque jour."),
        ])),
        block("7.3 Maladie hépatique", "".join([
            p("Signes fonctionnels : fatigue, ventre qui gonfle."),
            p("Signes physiques : ictère, angiomes, ascite."),
            p("Mécanisme : fibrose puis hypertension portale. L'arrêt reste utile, et la filière hépatologique s'ouvre."),
        ])),
    ])))
    parts.append(point("8", "Diagnostic positif et critères", "".join([
        p("Le critère suisse de la consommation à risque est celui d'Obsan et de l'OFSP, en grammes et en verres, et non un score américain."),
        p("Le seuil d'un questionnaire de type AUDIT n'a pas été relu dans une recommandation suisse aujourd'hui. Il n'est donc pas donné."),
        p("La dépendance ne se résume pas au dépassement des grammes. Elle ajoute la perte de contrôle et la poursuite malgré le dommage. Le chiffre de 250 000 à 300 000 personnes date du rapport de 2010 cité par l'OFSP."),
        p("Aucun seuil n'est présenté comme protecteur pour le cœur ou comme sans effet sur le cancer."),
    ])))
    parts.append(point("9", "Examens complémentaires", "".join([
        p("Il n'existe pas de gold standard biologique de la consommation déclarée. L'entretien structuré reste premier."),
        p("En première intention, si la clinique hépatique ou le dépassement chronique est là, le médecin demande les enzymes, la bilirubine et la numération, pour voir le retentissement et non pour « prouver » les verres."),
        p("Un résultat normal n'innocente pas. Un gamma-GT élevé n'est pas spécifique."),
        table(
            ["Résultat", "Lecture", "Conduite"],
            [
                [td("Enzymes normales et quantité au-dessus du seuil."), td("La biologie ne blanchit pas l'anamnèse."), td("L'intervention brève reste indiquée.")],
                [td("Cytolyse et consommation élevée."), td("Retentissement possible."), td("Arrêt, contrôle, et avis si les signes d'hépatopathie sont là.")],
                [td("Macrocytose isolée."), td("Elle est compatible avec l'alcool et avec d'autres causes."), td("On ne pose pas l'étiquette sur ce seul chiffre.")],
                [td("Grossesse."), td("Toute exposition compte, selon la page OFSP."), td("Orientation, sans culpabiliser, et sans dose de médicament ici.")],
            ],
        ),
        p("Le scanner et la biopsie ne sont pas des examens de première intention d'un repérage. Ils viennent avec une maladie d'organe."),
    ])))
    parts.append(point("10", "Arbre décisionnel", "".join([
        p("Si la personne est instable, blessée, suicidaire ou sur le point de conduire, le médecin sécurise avant de conseiller."),
        p("Si elle est stable et au-dessus du seuil sans dépendance, il fait l'intervention brève, il fixe un objectif de verres, et il revoit."),
        p("Si la dépendance ou le sevrage est présent, il oriente vers une filière compétente et il ne se contente pas d'un dépliant."),
        p("Si une grossesse est en cours, il annonce l'arrêt comme objectif et il accompagne."),
        p("S'il est tenté de dire qu'un verre protège le cœur, il s'arrête. La page OFSP ne retient pas ce bénéfice."),
    ])))
    parts.append(point("11", "Prise en charge selon les recommandations suisses", "".join([
        p("Le but est de faire descendre la consommation sous les seuils de risque, et de viser l'arrêt lorsqu'il y a dépendance, grossesse, ou maladie d'organe."),
        p("L'ordre est la sécurité, puis l'entretien, puis l'objectif, puis le suivi. Le médicament vient après, s'il est indiqué, et sa dose se lit dans l'information professionnelle, qui n'a pas été ouverte pour ce fichier."),
        block("Urgence", "".join([
            p("Minute 0 : conscience, glycémie, protection des voies aériennes, trauma."),
            p("Heure 1 : le sevrage sévère, la crise ou le délirium ne se renvoient pas au lendemain avec une brochure."),
            p("Le médecin ne donne pas ici de schéma de benzodiazépine, faute d'information professionnelle ouverte."),
        ])),
        p("Moyens non médicamenteux : intervention brève, journal de verres, entourage, groupes, arrêt de la conduite tant que l'alcoolémie n'est pas compatible avec la route. Le seuil légal suisse de l'air expiré n'a pas été relu sur Fedlex aujourd'hui : il n'est pas inventé."),
        p("Classes possibles, sans dose : accompagnement du sevrage en milieu adapté, et médicaments de maintien de l'abstinence ou de la réduction autorisés en Suisse. Le nom commercial et la dose attendent l'information professionnelle."),
        p("Travail : l'OFSP chiffre 2,1 milliards de francs de pertes de productivité. L'incapacité se juge sur la fonction, pas sur l'étiquette."),
        p("Grossesse et allaitement : l'OFSP les place parmi les situations inappropriées. Sujet âgé : interactions et chutes. Enfant et adolescent : 22 % des 15 à 19 ans déclarent un épisode excessif au moins une fois par mois, et la réponse est la protection, pas un score d'adulte. Foie : l'arrêt est le traitement de fond. Rein : l'adaptation des médicaments se fait plus tard, sur l'information professionnelle."),
        p("Surveillance : nouveau décompte des verres à une date fixée, enzymes si elles étaient anormales, recherche de rechute."),
        p("Sortie : la personne stable part avec un objectif chiffré en verres, un conseil de ne pas conduire si elle a bu, et un recours si le sevrage commence. Elle ne part pas si elle est confuse ou suicidaire."),
        p("Pronostic : la mortalité attribuable baisse lorsque la consommation baisse. Le cours ne promet pas un chiffre individuel de guérison."),
    ])))
    parts.append(point("12", "Prévention", "".join([
        p("Primaire : dire qu'il n'y a pas de quantité enseignée comme sans danger, et retarder l'entrée chez l'adolescent."),
        p("Secondaire : repérer les 16,4 % au-dessus du seuil à chaque occasion utile, sans attendre une demande."),
        p("Tertiaire : après une cirrhose, un cancer ou un accident, l'arrêt prévient la récidive et le deuxième trauma."),
    ])))
    parts.append(point("13", "Points clés", "".join([
        p("Le médecin connaît 16,4 % en 2022, les seuils en grammes, et les 4 et 5 verres de l'épisode."),
        p("Il sépare l'épisode, le risque chronique et la dépendance."),
        p("Il ne vend pas le verre cardioprotecteur."),
        p("Il cite 1 553 décès en 2017 entre 15 et 74 ans, sans les transformer en incidence actuelle inventée."),
        p("Il ne prescrit aucune dose tant que l'information professionnelle n'est pas ouverte."),
    ])))
    parts.append(point("14", "Pièges et questions fréquentes à l'examen fédéral suisse", "".join([
        p("Piège : un verre de vin protège le cœur. Bonne réponse : l'OFSP ne retient pas ce bénéfice."),
        p("Piège : mêmes seuils en grammes pour les deux sexes. Bonne réponse : 20 à 40 g chez la femme et 40 à 60 g chez l'homme pour le risque moyen."),
        p("Piège : enzymes normales, donc consommation sans risque. Bonne réponse : l'anamnèse tranche."),
        p("Piège : donner une dose de naltrexone ou d'acamprosate de mémoire. Bonne réponse : information professionnelle suisse, non ouverte ici."),
        p("Question : que répond-on à un homme de 22 ans qui boit 6 verres chaque samedi ? Réponse : c'est un épisode à risque, fréquent dans sa tranche d'âge, et l'intervention brève commence maintenant."),
    ])))
    parts.append(p("<strong>Question finale.</strong> Le candidat dépiste, quantifie en verres suisses, sécurise l'urgence et n'invente ni bénéfice cardiovasculaire ni dose."))
    return wrap_dx("DX.7 — Alcool : risque, épisode et dépendance" + badge(BADGE7), "".join(parts))


def dx8():
    term = inline(
        "stress psychosocial",
        "L'ESC 2021 l'associe, selon une relation dose-réponse, à l'apparition et à l'aggravation de la maladie athéromateuse, indépendamment des facteurs classiques et du sexe.",
        "Il inclut les symptômes de trouble psychique et les stresseurs : solitude, événements de vie, travail, argent, famille.",
        "Les risques relatifs usuels se situent entre 1,2 et 2,0.",
        "Malgré cette association, seul l'« épuisement vital » a montré, dans les travaux cités par l'ESC, qu'il améliorait la reclassification du risque."
        + src("S501"),
    )
    parts = []
    parts.append(point("1", "Définition et sémantique", "".join([
        p(f"Le {term} n'est pas un score, et il n'est pas une faiblesse morale."),
        p("L'ESC distingue le symptôme psychique, le stresseur, et le statut socio-économique. Le revenu bas porte l'association la plus forte avec la mortalité cardiovasculaire, avec un risque relatif de 1,76 et un intervalle de 1,45 à 2,14."),
        p("Le strain professionnel est la combinaison d'exigences hautes et de contrôle bas, à laquelle s'ajoute le déséquilibre effort-récompense."),
        p("Ces éléments ne sont pas des variables de SCORE2. Les ignorer parce qu'ils ne sont pas dans le calculateur est le piège de ce DX."),
    ])))
    parts.append(point("2", "Épidémiologie (Suisse, puis Europe)", "".join([
        p("Une prévalence suisse unique du stress psychosocial, mesurée comme le fait l'ESC, n'a pas été trouvée dans les pages ouvertes aujourd'hui. Le badge reste un rang."),
        p("L'ESC écrit qu'au moins un patient sur cinq porte un diagnostic de trouble psychique, souvent exprimé par un symptôme corporel. Ce ratio n'est pas une prévalence suisse de cabinet."),
        p("L'enjeu est double : le risque vasculaire, et le risque de passer à côté d'une dépression ou d'une idée suicidaire derrière une demande de « bilan »."),
        p("Le gradient social du SSP, tel qu'il figure dans la fiche locale, n'est pas repris comme chiffre, parce que sa source primaire n'a pas été rouverte aujourd'hui."),
    ])))
    parts.append(point("3", "Physiopathologie", "".join([
        p("L'ESC retient des effets biologiques directs et, en même temps, une forte corrélation avec le tabac, le revenu et la mauvaise observance."),
        p("Le cours ne transforme pas cette phrase en cascade moléculaire inventée. Le mécanisme utile est celui-ci : le stresseur entretient les comportements, l'observance chute, et la plaque progresse."),
        p("Les cibles de correction sont donc le symptôme psychique, l'obstacle social et les facteurs classiques, ensemble."),
        table(
            ["Perturbation", "Exploration", "Conduite"],
            [
                [td("Symptôme dépressif ou anxieux."), td("Questions directes, et un outil de repérage si le médecin en utilise un."), td("Soin psychique. Pas de dose dans ce fichier.")],
                [td("Stresseur de travail ou d'argent."), td("La question ouverte de l'ESC."), td("Adapter le plan, et non répéter la même ordonnance.")],
                [td("Bas revenu."), td("L'histoire sociale."), td("Tenir compte du coût et de l'accès. Ne pas convertir 1,76 en risque individuel.")],
            ],
        ),
    ])))
    parts.append(point("4", "Démarche diagnostique", "".join([
        p("Le médecin exclut d'abord l'urgence psychiatrique et l'urgence coronaire, parce que les deux peuvent se présenter comme une oppression thoracique."),
        p("Il cherche ensuite un trouble psychique constitué, puis un stresseur sans trouble, puis un simple modificateur vasculaire."),
        table(
            ["Hypothèse grave", "Ce qui tranche", "Piège"],
            [
                [td("Idée suicidaire."), td("La question directe."), td("Parler seulement de cholestérol.")],
                [td("Syndrome coronarien que l'anxiété imite."), td("La clinique ischémique et l'électrocardiogramme si la douleur est évocatrice."), td("Attribuer toute oppression au stress.")],
                [td("Dépression."), td("Humeur, anhédonie, durée."), td("Un conseil de « se détendre » seul.")],
                [td("Modificateur vasculaire isolé."), td("Stresseur présent, score près d'un seuil."), td("Multiplier le SCORE2 par 1,5 de mémoire.")],
            ],
        ),
    ])))
    parts.append(point("5", "Anamnèse ciblée et drapeaux rouges", "".join([
        p("L'ESC propose une question simple : la personne est-elle gênée par le stress au travail, les problèmes d'argent, les difficultés familiales, la solitude ou un événement ?"),
        p("Cette question a une raison : ces stresseurs portent un risque relatif du même ordre que plusieurs facteurs biologiques, et ils expliquent l'échec d'un plan trop technique."),
        p("Le médecin demande ensuite l'humeur et l'idée de mort, parce que le modificateur vasculaire ne doit pas cacher une crise."),
        p("Drapeaux : idée suicidaire, violence subie, douleur thoracique actuelle, sevrage ou alcool massif associé au DX.7."),
    ])))
    parts.append(point("6", "Examen physique ciblé, région par région", "".join([
        p("L'examen normal d'une personne anxieuse est un thorax souple, une pression parfois haute, et un cœur rapide qui ralentit au repos."),
        p("Le pathologique vasculaire se cherche quand même : pression aux deux bras, pouls, souffle, œdème. Le stress ne donne pas un permis de sauter l'examen."),
        p("Le médecin observe le contact, le ralentissement et l'agitation, parce que ces signes orientent vers un trouble de l'humeur plutôt que vers un simple modificateur."),
        p("Il n'existe pas de signe physique qui mesure le risque relatif de 1,2 à 2,0."),
    ])))
    parts.append(point("7", "Approche syndromique", "".join([
        block("7.1 Oppression et anxiété", "".join([
            p("Signes fonctionnels : serrement, soupirs, peur de mourir."),
            p("Signes physiques : tachycardie, thorax normal, électrocardiogramme à discuter si le doute ischémique existe."),
            p("Mécanisme : le symptôme corporel est fréquent dans le trouble psychique, et il peut coexister avec une plaque."),
        ])),
        block("7.2 Épuisement au travail", "".join([
            p("Signes fonctionnels : exigences hautes, contrôle bas, sommeil cassé."),
            p("Signes physiques : souvent pauvres."),
            p("Mécanisme : le strain est un stresseur vasculaire dans le texte ESC, distinct du burnout comme maladie administrative."),
        ])),
        block("7.3 Isolement du sujet âgé", "".join([
            p("Signes fonctionnels : repas seul, ordonnance non prise."),
            p("Signes physiques : hygiène, poids, pression non suivie."),
            p("Mécanisme : la solitude est un stresseur, et elle casse l'observance."),
        ])),
    ])))
    parts.append(point("8", "Diagnostic positif et critères", "".join([
        p("Il n'y a pas de score suisse obligatoire qui « positive » ce modificateur."),
        p("L'ESC recommande des instruments de repérage de la dépression, de l'anxiété et de l'insomnie, et il cite en exemple le Patient Health Questionnaire. Le seuil chiffré de ce questionnaire n'a pas été relu dans sa notice aujourd'hui : il n'est pas inventé."),
        p("Un stresseur nommé par la personne suffit pour adapter le plan. Il ne suffit pas pour multiplier le SCORE2 par un coefficient."),
        p("Seul l'épuisement vital est présenté par l'ESC comme ayant amélioré la reclassification. Le médecin ne prétend pas la même performance pour chaque contrariété."),
    ])))
    parts.append(point("9", "Examens complémentaires", "".join([
        p("Le gold standard est clinique. Aucune prise de sang ne mesure le stress utilement pour reclasser."),
        p("Première intention : l'entretien de l'ESC, et un repérage de la dépression si le symptôme est là."),
        p("Deuxième intention : avis psychiatrique ou psychothérapeutique si le trouble est constitué ou si le risque suicidaire existe."),
        p("Le score calcique ne se demande pas pour « objectiver » un stress."),
        table(
            ["Situation", "Examen", "Conduite"],
            [
                [td("Stresseur sans symptôme ischémique."), td("Entretien seul."), td("Adapter le plan de prévention.")],
                [td("Suspicion de dépression."), td("Repérage clinique."), td("Soin psychique, et poursuite de la prévention vasculaire.")],
                [td("Douleur thoracique douteuse."), td("Électrocardiogramme et filière habituelle."), td("Ne pas choisir entre le cœur et l'esprit : les deux peuvent être vrais.")],
                [td("Idée suicidaire."), td("Évaluation du danger immédiat."), td("Ne pas laisser partir sans un plan de sécurité.")],
            ],
        ),
    ])))
    parts.append(point("10", "Arbre décisionnel", "".join([
        p("Si une idée suicidaire ou une douleur ischémique est présente, cette urgence passe avant le modificateur."),
        p("Si un trouble psychique est probable, le médecin le fait soigner et il maintient la prévention vasculaire."),
        p("Si seul un stresseur est présent et que le risque vasculaire est près d'un seuil, il en tient compte dans la décision partagée, sans coefficient magique."),
        p("Si le risque est déjà très haut ou très bas, il ne collectionne pas le stress pour changer un chiffre, mais il le traite quand même s'il fait souffrir."),
    ])))
    parts.append(point("11", "Prise en charge selon les recommandations suisses", "".join([
        p("Le but est double : réduire la souffrance psychique, et ne pas laisser les facteurs vasculaires dériver pendant cette souffrance."),
        p("L'ordre est la sécurité, l'écoute, le plan vasculaire simplifié, puis le suivi. Un plan de vingt mesures échoue lorsque la personne est épuisée."),
        block("Urgence", "".join([
            p("Minute 0 : question sur l'idée de mort, et question sur la douleur thoracique actuelle."),
            p("Si le danger est immédiat, le médecin ne renvoie pas à un calculateur."),
            p("Il organise la protection et la filière d'urgence. Les numéros et les gardes locales se vérifient au moment du soin, et ils ne sont pas inventés ici."),
        ])),
        p("Moyens non médicamenteux : entretien, psychothérapie, adaptation du travail, aide sociale si le revenu bloque les soins. Moyens médicamenteux : un antidépresseur peut être indiqué. Sa classe, sa spécialité suisse et sa dose se lisent dans l'information professionnelle, non ouverte aujourd'hui."),
        p("Travail et assurances : le strain peut justifier un aménagement. L'incapacité se décrit par la fonction. La conduite est limitée si la sédation ou l'idée suicidaire existe."),
        p("Grossesse : les stresseurs et la dépression périnatale se recherchent, et les médicaments psychotropes se décident avec l'information professionnelle. Sujet âgé : solitude et ordonnances multiples. Enfant : ce DX adulte ne se plaque pas. Une souffrance d'enfant ouvre une protection, pas un SCORE2. Foie et rein : ils changent le choix ultérieur du psychotrope, sans dose ici."),
        p("Surveillance : humeur, observance des traitements vasculaires, tension, et non un dosage de « cortisol de stress »."),
        p("Sortie : la personne peut partir si le danger suicidaire est écarté, si la douleur cardiaque l'est aussi, et si elle a un prochain contact. Sinon elle reste dans une filière."),
        p("Pronostic : traiter la dépression et les stresseurs améliore la vie. L'ESC cite une cohorte où le dépistage de la dépression a été suivi d'un effet favorable sur les événements majeurs, avec un suivi médian de 8,4 ans. Ce n'est pas une garantie individuelle."),
    ])))
    parts.append(point("12", "Prévention", "".join([
        p("Primaire : poser la question des stresseurs avant que la plaque ne soit symptomatique."),
        p("Secondaire : chez la personne déjà malade, l'ESC juge le dépistage du stress psychologique important."),
        p("Tertiaire : après l'événement, la réadaptation inclut le psychique, sinon l'observance s'effondre."),
    ])))
    parts.append(point("13", "Points clés", "".join([
        p("Le médecin pose la question du travail, de l'argent, de la famille et de la solitude."),
        p("Il retient un risque relatif d'environ 1,2 à 2,0, et 1,76 pour le bas revenu, sans en faire un pourcentage personnel."),
        p("Il ne multiplie pas SCORE2 par un coefficient psychosocial."),
        p("Il cherche l'idée suicidaire et la douleur ischémique avant de parler de modificateur."),
        p("Il ne donne aucune dose d'antidépresseur dans ce fichier."),
    ])))
    parts.append(point("14", "Pièges et questions fréquentes à l'examen fédéral suisse", "".join([
        p("Piège : « c'est le stress » devant une oppression d'effort. Bonne réponse : écarter l'ischémie."),
        p("Piège : ignorer le psychique parce qu'il n'est pas dans SCORE2. Bonne réponse : le traiter, et ne l'utiliser comme modificateur que près d'un seuil."),
        p("Piège : croire que tout stresseur reclassifie aussi bien que l'épuisement vital. Bonne réponse : l'ESC limite cette preuve à l'épuisement vital."),
        p("Question : citez la question d'entretien. Réponse : travail, argent, famille, solitude, événement stressant."),
    ])))
    parts.append(p("<strong>Question finale.</strong> Le candidat tient ensemble le cœur et le psychisme, sans coefficient inventé et sans dose inventée."))
    return wrap_dx("DX.8 — Stress psychosocial et position sociale" + badge(RANG8), "".join(parts))


def dx9():
    term = inline(
        "radon",
        "L'OFSP le décrit comme un gaz rare naturel, issu de la désintégration de l'uranium du sol, qui entre dans les bâtiments par les défauts d'étanchéité.",
        "Ses produits de désintégration s'accumulent dans le poumon et l'irradient.",
        "Il est, après le tabac, la principale cause de cancer du poumon en Suisse, et il tue 200 à 300 personnes par an.",
        "Le cancer du poumon cause environ 3 200 décès par an dans le pays, chiffre OFS 2023 cité par l'OFSP. L'estimation de 200 à 300 vient de Menzler et collaborateurs, 2005, que l'OFSP cite encore."
        + src("S509"),
    )
    parts = []
    parts.append(point("1", "Définition et sémantique", "".join([
        p(f"Le {term} n'est pas une « pollution chimique » ordinaire, et il n'est pas visible ni odorant."),
        p("Le niveau de référence suisse est 300 Bq/m³ en moyenne annuelle, pour les locaux où l'on séjourne régulièrement plusieurs heures par jour."),
        p("Les lignes directrices du 2 février 2023 précisent ce séjour : au moins quinze heures par semaine. En dessous, des mesures de protection ne sont pas exigées pour ce local."),
        p("Depuis le 1.1.2018, ce niveau de référence a remplacé l'ancienne valeur limite de 1 000 Bq/m³. Une valeur seuil de 1 000 Bq/m³ demeure pour la concentration annuelle moyenne aux postes de travail exposés."),
        p("Le médecin ne confond pas le becquerel par mètre cube de l'air avec une dose en millisievert. Les lignes directrices visent à éviter, après un dépassement, une dose efficace cumulée d'environ 100 mSv, en accord avec la CIPR qu'elles citent."),
    ])))
    parts.append(point("2", "Épidémiologie (Suisse, puis Europe)", "".join([
        p("Deux cents à trois cents décès par an ne sont pas une prévalence. Le badge reste un rang. Le poids de gravité est néanmoins haut, parce que la maladie est un cancer du poumon."),
        p("Parmi environ 3 200 décès annuels par cancer du poumon, 200 à 300 sont imputés au radon par la source que l'OFSP affiche."),
        p("Le risque croît avec la concentration et avec la durée. Des années ou des décennies séparent l'irradiation et le cancer."),
        p("La carte communale et les services de mesure agréés existent. Leur liste, mise à jour en 2026 sur la page OFSP, ne se récite pas de mémoire."),
        p("Une proportion européenne unique n'a pas été relue dans une page du Centre européen aujourd'hui. Elle n'est pas inventée."),
    ])))
    parts.append(point("3", "Physiopathologie", "".join([
        p("L'uranium du sol produit le radon, gaz radioactif. Le gaz entre par la cave, les fissures et les passages de gaines. Il se dilue mal lorsque le bâtiment est fermé."),
        p("Les descendants solides, une fois inhalés, se déposent dans le poumon et émettent un rayonnement qui casse l'ADN des cellules bronchiques."),
        p("Le tabac multiplie ce risque. L'OFSP place le radon juste derrière le tabac. Le médecin ne sépare donc pas les deux messages."),
        p("Il n'y a pas de médicament qui « détoxique » le radon. La correction est le bâtiment, puis l'arrêt du tabac."),
        table(
            ["Lésion", "Exploration", "Correction"],
            [
                [td("Irradiation bronchique cumulée."), td("Dosimétrie du local en Bq/m³, par un service agréé."), td("Assainissement du bâtiment par le propriétaire.")],
                [td("Synergie avec le tabac."), td("Anamnèse tabagique chez tout cancer du poumon, fumeur ou non."), td("Arrêt du tabac, qui reste le premier levier personnel.")],
                [td("Cancer constitué."), td("Filière oncologique respiratoire."), td("Le traitement du cancer n'est pas une mesure de radon. Les doses ne sont pas ici.")],
            ],
        ),
    ])))
    parts.append(point("4", "Démarche diagnostique", "".join([
        p("Devant un cancer du poumon, le médecin cherche le tabac et le radon, y compris chez une personne qui n'a jamais fumé."),
        p("Devant une demande de prévention, il ne promet pas un risque individuel précis. Il propose la mesure du logement si le séjour atteint quinze heures par semaine."),
        table(
            ["Hypothèse", "Ce qui tranche", "Piège"],
            [
                [td("Cancer du poumon lié au radon chez un non-fumeur."), td("L'histologie ne signe pas le radon. L'histoire du logement et la mesure comptent."), td("Dire que le non-fumeur exclut le radon.")],
                [td("Dépassement dans une chambre."), td("Mesure agréée, pas un détecteur de fortune non reconnu."), td("Rassurer sur une mesure de quelques minutes.")],
                [td("Poste de travail au-dessus de 1 000 Bq/m³."), td("La valeur seuil des lignes directrices, article 167 de l'ORaP."), td("Appliquer seulement le niveau de 300 et ignorer le droit du travail.")],
                [td("Symptôme respiratoire aigu."), td("La clinique infectieuse ou embolique."), td("Attribuer une dyspnée du jour au radon de la cave.")],
            ],
        ),
    ])))
    parts.append(point("5", "Anamnèse ciblée et drapeaux rouges", "".join([
        p("Le médecin demande l'étage, la cave en terre, les fissures et le temps passé dans chaque pièce, parce que le radon vient du sol et que le séjour de quinze heures décide de l'exigence."),
        p("Il demande le tabac, parce que la synergie change le message."),
        p("Il demande si des enfants ou une école occupent le local. Pour les écoles et les jardins d'enfants, la durée de séjour additionne tous les occupants, et les délais longs sont recommandés même si l'usage réel est plus court."),
        p("Drapeaux cliniques : hémoptysie, amaigrissement, toux persistante. Ils ouvrent la filière du cancer, pas seulement un dosimètre."),
    ])))
    parts.append(point("6", "Examen physique ciblé, région par région", "".join([
        p("L'examen normal est la règle chez une personne exposée qui n'a pas encore de cancer. Un thorax clair n'exclut pas une concentration haute à la maison."),
        p("Le médecin ausculte les poumons, cherche un hippocratisme et une masse sus-claviculaire seulement lorsqu'un symptôme de cancer existe."),
        p("Il ne « sent » pas le radon. L'absence d'odeur ne rassure pas."),
        p("La technique utile est administrative autant que clinique : identifier le local à séjour prolongé, au-delà de trente heures par semaine, le local court entre quinze et trente heures, et le local sans séjour durable en dessous de quinze heures."),
    ])))
    parts.append(point("7", "Approche syndromique", "".join([
        block("7.1 Maison fermée en hiver", "".join([
            p("Signes fonctionnels : aucun."),
            p("Signes physiques : aucun."),
            p("Mécanisme : le gaz s'accumule lorsque l'aération baisse et que la dépression du bâtiment aspire le sol."),
        ])),
        block("7.2 Non-fumeur avec cancer du poumon", "".join([
            p("Signes fonctionnels : toux, essoufflement, parfois hémoptysie."),
            p("Signes physiques : ceux de la tumeur, ou aucun au début."),
            p("Mécanisme : l'irradiation ancienne. Le médecin pose la question du logement."),
        ])),
        block("7.3 École ou jardin d'enfants", "".join([
            p("Signes fonctionnels : aucun chez l'enfant."),
            p("Signes physiques : aucun."),
            p("Mécanisme : la durée s'additionne pour toute la classe. Le délai d'assainissement recommandé est celui du séjour prolongé."),
        ])),
    ])))
    parts.append(point("8", "Diagnostic positif et critères", "".join([
        p("Le critère d'action dans l'habitat est le dépassement de 300 Bq/m³ dans un local occupé au moins quinze heures par semaine, d'après les lignes directrices qui explicitent l'article 155 de l'ordonnance sur la radioprotection."),
        p("Ce niveau est une référence, et non une preuve que le risque est nul en dessous. L'OFSP dit que le risque augmente avec la concentration et la durée."),
        p("Au poste de travail, le dépassement de 1 000 Bq/m³ fait considérer le poste comme exposé au radon, article 167."),
        p("Une mesure antérieure à 2018 peut rester enregistrée et dépasser le nouveau niveau. Les lignes directrices recommandent alors vivement une nouvelle mesure si le séjour atteint quinze heures, ou un assainissement."),
    ])))
    parts.append(point("9", "Examens complémentaires", "".join([
        p("Le gold standard pratique est la mesure par un service agréé, en moyenne, et non une estimation d'après le code postal seul. La carte indique une priorité. Elle ne remplace pas la mesure du bâtiment."),
        p("Première intention : dosimètre du local à séjour prolongé. La page de protection décrit une mesure facile. La durée exacte de trois mois en hiver, souvent citée, n'a pas été relue dans le PDF des lignes directrices ouvert aujourd'hui : elle n'est pas affirmée ici."),
        p("Deuxième intention : la filière du cancer du poumon si un symptôme existe. Le scanner thoracique ne mesure pas le radon."),
        table(
            ["Concentration et séjour", "Lecture selon le tableau 4, ligne lue sans ambiguïté", "Conduite"],
            [
                [td("300 à 600 Bq/m³, séjour prolongé."), td("Délai maximal d'assainissement de 10 ans."), td("Le propriétaire planifie. Le canton peut ordonner s'il reste inactif.")],
                [td("300 à 600 Bq/m³, séjour court."), td("Délai maximal de 30 ans."), td("Si une transformation majeure a lieu avant, l'assainissement radon se fait en même temps.")],
                [td("Moins de 15 heures par semaine."), td("Pas de mesure exigée pour ce local."), td("Réévaluer si la pièce devient une chambre.")],
                [td("Au-dessus de 600 Bq/m³."), td("Le tableau 4 existe, mais son extraction était ambiguë."), td("Le médecin lit le tableau officiel plutôt que de réciter une cellule douteuse.")],
                [td("Poste de travail au-dessus de 1 000 Bq/m³."), td("Poste exposé, article 167."), td("Droit de la radioprotection au travail, pas seulement un conseil d'aération.")],
            ],
        ),
        p("Grossesse : la mesure du logement est d'autant plus utile que le séjour est long. Elle n'irradie pas la personne. Enfant : même logique, avec la règle de l'école. Rein et foie : sans objet pour la mesure de l'air."),
    ])))
    parts.append(point("10", "Arbre décisionnel", "".join([
        p("Si un symptôme de cancer existe, le médecin ouvre cette filière le jour même et il ajoute la question du radon, sans la substituer au diagnostic."),
        p("Si la personne séjourne au moins quinze heures dans un local en contact avec le sol, il propose la mesure agréée."),
        p("Si le résultat dépasse 300 Bq/m³, il explique que le propriétaire assume l'assainissement, article 166, et il donne le délai de la ligne qu'il a lue, ou il renvoie au tableau 4."),
        p("S'il y a du tabac, il place l'arrêt au même rang d'urgence que les travaux, parce que les deux risques se multiplient."),
        p("Si le local est un poste de travail au-dessus de 1 000 Bq/m³, il ne s'arrête pas au conseil domestique."),
    ])))
    parts.append(point("11", "Prise en charge selon les recommandations suisses", "".join([
        p("Le but est une concentration sous 300 Bq/m³ dans les locaux occupés, et l'arrêt du tabac chez la personne exposée."),
        p("L'ordre est le suivant. Protéger si un symptôme de cancer est là. Mesurer sinon. Expliquer le devoir du propriétaire. Accompagner l'arrêt du tabac. Ne pas promettre un risque individuel chiffré au-delà des sources."),
        block("Urgence", "".join([
            p("Le radon domestique n'est presque jamais une urgence à la minute, sauf si un symptôme de cancer ou une détresse respiratoire est présent."),
            p("Minute 0 de cette détresse : oxygène et filière d'urgence habituelle, pas un dosimètre."),
            p("Les jours suivants : la question du logement vient après la stabilité clinique."),
        ])),
        p("Moyens : étanchéité du sol, ventilation du vide sanitaire, aspiration sous dalle, aération. Ce sont des moyens du bâtiment, décrits comme l'état de la technique dans les lignes directrices, avec les normes SIA. Le médecin n'improvise pas le chantier."),
        p("Médicament : aucun n'abaisse le radon. Les traitements du cancer du poumon ont leurs informations professionnelles, non ouvertes ici."),
        p("Droit : le propriétaire ou le maître d'ouvrage veille aux mesures préventives dans le neuf et le transformé, article 163. Le canton exécute en général, article 158 cité par les lignes directrices. Le propriétaire paie l'assainissement nécessaire, article 166, et le canton peut l'ordonner."),
        p("Grossesse, enfant, sujet âgé : la physique du gaz est la même. Le séjour de l'enfant à l'école s'additionne. Le sujet âgé qui reste toute la journée dans une cave aménagée cumule l'exposition. Foie et rein : sans effet sur la décision de mesurer."),
        p("Surveillance : nouvelle mesure après travaux. Une mesure d'avant 2018 qui dépasse 300 Bq/m³ se refait si le séjour est suffisant."),
        p("Sortie de consultation : la personne part avec l'adresse d'un service agréé ou la carte, la phrase sur les quinze heures, et l'arrêt du tabac si elle fume. Elle ne part pas sans filière si un symptôme de cancer est présent."),
        p("Pronostic : abaisser la concentration abaisse le risque. Le cancer déjà constitué suit sa propre filière. Aucune guérison spontanée de l'irradiation passée n'est promise."),
    ])))
    parts.append(point("12", "Prévention", "".join([
        p("Primaire : construire selon l'état de la technique pour rester sous 300 Bq/m³, et ne pas fumer."),
        p("Secondaire : mesurer les locaux occupés, surtout avant une rénovation qui pourrait enfermer le gaz."),
        p("Tertiaire : après un cancer du poumon, réduire l'exposition restante et le tabac, sans accuser la personne."),
    ])))
    parts.append(point("13", "Points clés", "".join([
        p("Le médecin retient 200 à 300 décès par an et la deuxième place derrière le tabac."),
        p("Il retient 300 Bq/m³ et quinze heures par semaine."),
        p("Il retient 1 000 Bq/m³ comme seuil du poste de travail exposé."),
        p("Il connaît le délai de 10 ans et de 30 ans pour la bande 300 à 600 Bq/m³, et il ouvre le tableau 4 pour le reste."),
        p("Il associe toujours le tabac, et il n'invente pas de médicament anti-radon."),
    ])))
    parts.append(point("14", "Pièges et questions fréquentes à l'examen fédéral suisse", "".join([
        p("Piège : le non-fumeur ne peut pas avoir un cancer du poumon lié au radon. Bonne réponse : le radon est la cause suivante après le tabac, et il touche aussi les non-fumeurs."),
        p("Piège : 1 000 Bq/m³ est encore la limite des logements. Bonne réponse : depuis 2018, la référence des locaux occupés est 300, et 1 000 reste le seuil des postes exposés."),
        p("Piège : la carte communale remplace la mesure. Bonne réponse : elle priorise, elle ne mesure pas le salon."),
        p("Piège : réciter tous les délais du tableau 4 de mémoire si l'on n'a pas la cellule sous les yeux. Bonne réponse : citer la ligne sûre et ouvrir le document."),
        p("Question : qui paie l'assainissement ? Réponse : en principe le propriétaire, article 166 de l'ordonnance, et le canton peut ordonner."),
    ])))
    parts.append(p("<strong>Question finale.</strong> Le candidat relie le gaz, la loi suisse et le tabac, et il n'envoie pas un dyspnéique aigu chercher un dosimètre à la place des urgences."))
    return wrap_dx("DX.9 — Radon domiciliaire et cancer du poumon" + badge(RANG9), "".join(parts))


def dx10():
    term = inline(
        "antécédent familial de maladie cardiovasculaire précoce",
        "L'ESC 2021 le décrit comme un indicateur simple, qui mélange héritage génétique et milieu partagé.",
        "Il améliore peu la prédiction au-delà des facteurs classiques, mais il déclenche une évaluation complète.",
        "La page de l'EAS, lue le 24.10.2026, chiffre la précocité : avant 55 ans chez l'homme et avant 60 ans chez la femme, au premier degré.",
        "Ce seuil n'autorise pas, à lui seul, une analyse génétique."
        + src("S501") + src("S506"),
    )
    parts = []
    parts.append(point("1", "Définition et sémantique", "".join([
        p(f"L'{term} n'est pas un test, et il n'est pas une condamnation."),
        p("L'ESC distingue cette histoire clinique du score polygénique. Il juge le gain prédictif des scores polygéniques encore modeste, et son tableau classe en III la collecte routinière des scores de risque génétique."),
        p("L'hypercholestérolémie familiale est une autre entité : elle peut classer d'emblée en risque haut ou très haut sur la page AGLA, avant tout calcul de personne saine."),
        p("Le conseil génétique suisse est défini par la LAGH, pas par une habitude de service. Le médecin qui prescrit veille à un conseil non directif, par une personne qualifiée, consigné, limité à la situation individuelle et familiale."),
    ])))
    parts.append(point("2", "Épidémiologie (Suisse, puis Europe)", "".join([
        p("La prévalence suisse des antécédents familiaux précoces en consultation de premier recours n'a pas été trouvée aujourd'hui. Le badge reste un rang."),
        p("L'enjeu n'est pas ce pourcentage manquant. L'enjeu est de ne pas rater une maladie monogénique actionnable, et de ne pas tester sans droit."),
        p("L'ESC note que l'histoire familiale reste associée aux événements même après ajustement sur des scores génétiques, dans les quelques études qu'il cite, tout en n'ajoutant que peu à la prédiction usuelle."),
        p("Aucune incidence suisse des tests prescrits hors conseil n'a été lue. Elle n'est pas inventée."),
    ])))
    parts.append(point("3", "Physiopathologie", "".join([
        p("Une partie du risque se transmet par des variants rares à fort effet, comme dans l'hypercholestérolémie familiale, où le LDL reste haut dès l'enfance."),
        p("Une autre partie se transmet par de nombreux variants faibles et par les habitudes de la maison : tabac, cuisine, tension non mesurée."),
        p("C'est pourquoi l'histoire familiale ne disparaît pas entièrement derrière un score polygénique, et pourquoi elle ne remplace pas non plus la mesure du LDL et de la pression."),
        p("Le traitement corrige le LDL, la pression et le tabac. Le test ne soigne personne s'il n'est pas suivi d'une mesure."),
        table(
            ["Perturbation", "Exploration", "Conduite"],
            [
                [td("LDL très élevé et histoire précoce."), td("Bilan lipidique, examen des xanthomes, avis spécialisé."), td("Catégorie AGLA de l'hypercholestérolémie familiale. Dose selon l'information professionnelle, non ouverte ici.")],
                [td("Agrégat familial sans anomalie lipidique claire."), td("Arbre à trois générations, âges d'événement."), td("Évaluation du risque, et test seulement si une question génétique précise existe.")],
                [td("Information excédentaire d'un génome large."), td("L'article 9 de la LAGH demande de l'éviter autant que possible."), td("Conseil avant, et droit de ne pas savoir.")],
            ],
        ),
    ])))
    parts.append(point("4", "Démarche diagnostique", "".join([
        p("Le médecin dessine d'abord l'arbre. Il ne prescrit pas un kit."),
        p("Il exclut l'urgence familiale réelle : un apparenté jeune symptomatique maintenant, qui a besoin de soins, pas d'un cours de droit."),
        table(
            ["Hypothèse", "Ce qui tranche", "Piège"],
            [
                [td("Hypercholestérolémie familiale."), td("LDL, signes, histoire. La page AGLA la classe sans score de personne saine."), td("Calculer un SCORE2 rassurant.")],
                [td("Histoire précoce sans maladie monogénique."), td("Âges précis : avant 55 ans chez l'homme et avant 60 ans chez la femme, selon la page EAS."), td("Compter un infarctus à 80 ans comme précoce.")],
                [td("Demande de test présymptomatique."), td("La LAGH impose le conseil avant et après."), td("Prélever le jour de la demande.")],
                [td("Parent qui veut tester un enfant incapable de discernement."), td("L'article 5 exige le représentant, et l'intégration de l'enfant autant que possible."), td("Tester pour rassurer les parents.")],
            ],
        ),
    ])))
    parts.append(point("5", "Anamnèse ciblée et drapeaux rouges", "".join([
        p("Le médecin demande qui a été malade, à quel âge, et de quoi, parce que la précocité se juge sur l'âge et le degré de parenté."),
        p("Il demande les xanthomes familiaux et les LDL déjà mesurés, parce qu'ils orientent vers l'hypercholestérolémie familiale plutôt que vers un score polygénique."),
        p("Il demande ce que la personne veut savoir, et ce qu'elle ne veut pas savoir, parce que l'article 8 de la LAGH protège le refus de tout ou partie de l'information."),
        p("Drapeaux : symptôme actuel chez le consultant, LDL extrême, ou demande de tester un tiers sans son consentement."),
    ])))
    parts.append(point("6", "Examen physique ciblé, région par région", "".join([
        p("L'examen normal n'exclut pas un risque familial. Beaucoup de porteurs n'ont aucun signe cutané."),
        p("Le médecin cherche quand même les xanthomes tendineux, l'arc cornéen précoce et les dépôts, parce que leur présence renforce l'hypothèse monogénique."),
        p("Il mesure la pression et les pouls, parce que l'histoire familiale ne dispense pas de l'examen vasculaire."),
        p("La technique du xanthome est la palpation du tendon d'Achille et des extenseurs. Un tendon épais et nodulaire est pathologique. Un tendon fin ne blanchit pas le LDL."),
    ])))
    parts.append(point("7", "Approche syndromique", "".join([
        block("7.1 Parent précoce, lipides inconnus", "".join([
            p("Signes fonctionnels : inquiétude, aucun symptôme."),
            p("Signes physiques : souvent aucun."),
            p("Mécanisme : milieu partagé et possible variant. Le premier examen est le bilan lipidique, pas le génome entier."),
        ])),
        block("7.2 Hypercholestérolémie familiale probable", "".join([
            p("Signes fonctionnels : parfois aucun jusqu'à l'événement."),
            p("Signes physiques : xanthome possible, souvent absent."),
            p("Mécanisme : LDL haut depuis l'enfance. La page AGLA sort du score de personne saine."),
        ])),
        block("7.3 Demande de savoir pour les enfants", "".join([
            p("Signes fonctionnels : la demande vient du parent."),
            p("Signes physiques : l'enfant peut être asymptomatique."),
            p("Mécanisme juridique : consentement, information, et intérêt de la personne concernée. Le test n'est pas un outil de curiosité."),
        ])),
    ])))
    parts.append(point("8", "Diagnostic positif et critères", "".join([
        p("Le critère qui déclenche l'évaluation est l'histoire de maladie cardiovasculaire précoce au premier degré, avant 55 ans chez l'homme et avant 60 ans chez la femme, telle que la page EAS la publie."),
        p("Ce critère ne pose pas le diagnostic d'hypercholestérolémie familiale. Il l'évoque si le LDL est très élevé ou si des signes existent."),
        p("Le critère d'un test présymptomatique, prénatal ou de planning familial est juridique : conseil génétique obligatoire avant et après, article 21 alinéa 1 lettre b. Pour un test diagnostique, la personne doit pouvoir bénéficier du conseil, lettre a."),
        p("Un temps de réflexion adéquat sépare le conseil et le prélèvement, article 21 alinéa 4. Le prélèvement le jour même de l'annonce est un manquement."),
        p("Un score polygénique commercial ne constitue pas ce diagnostic. L'ESC ne le retient pas en collecte routinière."),
    ])))
    parts.append(point("9", "Examens complémentaires", "".join([
        p("Le gold standard de l'histoire familiale est l'arbre bien daté, pas une puce. Le gold standard de l'hypercholestérolémie familiale moléculaire est l'analyse ciblée après conseil, lorsque le clinicien a une question précise."),
        p("Première intention : profil lipidique du consultant, pression, et calcul du risque seulement si la page AGLA ne l'a pas déjà classé."),
        p("Deuxième intention : avis lipidologique ou génétique si l'hypothèse monogénique tient."),
        p("Le médecin prescrit l'analyse seulement s'il est habilité, article 20 : titre postgrade fédéral du domaine ou qualification particulière en génétique humaine."),
        table(
            ["Situation", "Examen juste", "Conduite"],
            [
                [td("Histoire précoce, personne asymptomatique."), td("Lipides, pression, arbre."), td("Évaluation complète. Pas de génome le jour même.")],
                [td("LDL très élevé."), td("Filière de l'hypercholestérolémie familiale."), td("Catégorie AGLA dédiée. Pas de SCORE2 rassurant.")],
                [td("Test présymptomatique accepté."), td("Conseil avant et après, délai, consentement écrit au sens de l'article 5."), td("Documenter le conseil.")],
                [td("La personne refuse de savoir."), td("Aucun examen de plus."), td("Article 8. Le refus n'a pas à être justifié.")],
                [td("Grossesse et test prénatal."), td("Article 22 : information spécifique, y compris si aucun traitement n'est possible."), td("Ne pas diriger vers une seule issue.")],
            ],
        ),
    ])))
    parts.append(point("10", "Arbre décisionnel", "".join([
        p("Si un symptôme vasculaire est actuel, le médecin soigne la personne et il remet l'arbre à plus tard dans la journée, pas à l'année suivante."),
        p("Si l'arbre montre une maladie précoce au premier degré, il mesure les lipides et la pression et il cherche l'hypercholestérolémie familiale."),
        p("Si cette maladie est probable, il classe selon AGLA et il adresse. Il n'utilise pas le calculateur des personnes saines pour minimiser."),
        p("Si un test génétique est vraiment utile, il organise le conseil, le délai et le consentement. Il ne prélève pas avant."),
        p("Si la personne refuse d'être informée, il respecte le refus et il informe quand même des conséquences médicales de ne pas savoir, dans le conseil, sans forcer le résultat."),
        p("S'il s'agit d'un parent, d'un assureur ou d'un employeur qui demande le résultat, il ne communique rien sans le consentement de la personne, article 7."),
    ])))
    parts.append(point("11", "Prise en charge selon les recommandations suisses", "".join([
        p("Le but est de protéger la personne et ses apparentés d'un risque actionnable, sans violer l'autodétermination."),
        p("L'ordre est clinique, puis juridique, puis biologique. Inverser cet ordre produit des tests que personne ne peut interpréter sereinement."),
        block("Conseil, pas à pas", "".join([
            p("Étape 1 : dire le but, la nature, la pertinence, les risques psychiques, le sort des échantillons, la possibilité d'informations excédentaires, et le droit de refuser, article 6."),
            p("Étape 2 : le conseil qualifié ajoute la fréquence de l'anomalie, les conséquences médicales, psychiques et sociales du test et du refus, le coût, les mesures possibles, le soutien, et ce que les assurances peuvent demander, article 21 alinéa 3."),
            p("Étape 3 : laisser un délai, puis ne prélever que si le consentement libre et exprès demeure."),
            p("Étape 4 : rendre le résultat à la personne seule, sauf consentement contraire, et respecter un refus partiel."),
            p("Le conseil ne sert pas l'intérêt général de la société. Il est individuel et familial, et il est consigné."),
        ])),
        p("Moyens cliniques : traitement des facteurs selon la catégorie, suivi des apparentés qui le demandent, et pas de pression sur ceux qui invoquent leur droit de ne pas savoir. Le PDF de l'OFSP de février 2025 rappelle que ce droit vaut aussi pour les membres de la famille."),
        p("Médicaments : ceux de l'hypercholestérolémie ou du risque élevé. Aucune dose ni aucun nom commercial n'est écrit, faute d'information professionnelle ouverte."),
        p("Assurances : le conseil doit expliquer dans quelles conditions un assureur peut demander des données. Le médecin ne transmet pas un résultat « pour aider le dossier »."),
        p("Grossesse : article 22, information sur l'autodétermination, et avertissement si aucun traitement n'est possible après le test. Le partenaire est associé si c'est possible. La note Fedlex indique une modification de cet alinéa en vigueur depuis le 1er août 2025."),
        p("Enfant incapable de discernement : le représentant consent, et l'enfant est associé autant que possible, article 5. Le test d'un enfant sain pour rassurer un parent n'est pas une indication."),
        p("Sujet âgé : un test présymptomatique n'a de sens que s'il change encore une décision. Foie et rein : ils influencent le médicament ultérieur, pas le droit au conseil."),
        p("Surveillance : LDL et clinique selon la maladie trouvée. Le test ne se répète pas pour voir."),
        p("Sortie : la personne part seulement si elle a compris s'il y aura ou non un test, quand, et qu'elle peut encore refuser. Un apparenté symptomatique n'est pas « réglé » par le conseil du consultant."),
        p("Pronostic : traiter une hypercholestérolémie familiale change le risque. Un test sans suite ne le change pas. Aucune série suisse nouvelle n'a été ouverte aujourd'hui."),
    ])))
    parts.append(point("12", "Prévention", "".join([
        p("Primaire : dessiner l'arbre au moment du premier bilan, et mesurer le LDL une fois lorsqu'il n'est pas connu."),
        p("Secondaire : si la maladie familiale est confirmée, dépister les apparentés qui consentent, dans le cadre du conseil."),
        p("Tertiaire : après un infarctus précoce, l'arbre protège les enfants mieux qu'un discours général."),
    ])))
    parts.append(point("13", "Points clés", "".join([
        p("Le médecin retient avant 55 ans chez l'homme et avant 60 ans chez la femme, au premier degré, comme seuil de la page EAS."),
        p("Il sait que cette histoire déclenche l'évaluation et qu'elle prédit peu au-delà des facteurs classiques."),
        p("Il classe l'hypercholestérolémie familiale avec AGLA, sans SCORE2 de complaisance."),
        p("Il n'ordonne pas un test présymptomatique sans conseil, sans délai et sans consentement."),
        p("Il respecte le droit de ne pas savoir, y compris pour la famille."),
    ])))
    parts.append(point("14", "Pièges et questions fréquentes à l'examen fédéral suisse", "".join([
        p("Piège : prélever le jour de la demande de test présymptomatique. Bonne réponse : conseil, puis délai, article 21."),
        p("Piège : communiquer le résultat au frère qui s'inquiète, sans accord. Bonne réponse : article 7, consentement."),
        p("Piège : score polygénique commercial à tout patient intermédiaire. Bonne réponse : classe III pour la collecte routinière dans le tableau ESC 2021."),
        p("Piège : un père mort à 78 ans « compte comme précoce ». Bonne réponse : non, selon le seuil de 55 et 60 ans de la page EAS."),
        p("Question : que contient au minimum le conseil de l'article 21 alinéa 3 ? Réponse : fréquence et nature, conséquences du test et du refus, coûts, importance et mesures, soutien, et demandes possibles des assurances."),
    ])))
    parts.append(p("<strong>Question finale.</strong> Le candidat protège à la fois l'artère et le droit. Il n'invente ni une puce utile à tous ni une dose de statine."))
    return wrap_dx("DX.10 — Histoire familiale précoce et conseil génétique" + badge(RANG10), "".join(parts))


def all_bodies():
    return dx5(), dx6(), dx7(), dx8(), dx9(), dx10()
