# -*- coding: utf-8 -*-
# Suite Phase A — exécutée dans le générateur (s, seul, fen, tableau, L, use).

use("p3")
s("Le sens épicritique comprend la pallesthésie, le sens de position et le toucher fin, car ces messages montent par les gros fibres puis les cordons postérieurs", "rmsnp")
s("Le sens protopathique comprend la douleur et la température, car ces messages montent par les petites fibres puis les voies spinothalamiques", "rmsnp")
s("Une " + L("f-moelle", "coupe de moelle") + " en couleur montre ces cordons, car la lésion d'une colonne n'a pas le territoire d'un nerf périphérique", "openstax", "rmsnp")
s("La fibre sensitive part du récepteur cutané, gagne le ganglion spinal puis la corne postérieure, car le premier relais dépend du type de fibre", "rmsnp")
s("La grosse fibre monte dans le cordon postérieur du même côté jusqu'au bulbe, car la décussation de ce canal est haute", "rmsnp")
s("La petite fibre synapse dans la corne postérieure et croise bas dans la moelle, car une lésion latérale de la moelle atteint déjà le côté opposé", "rmsnp")
s("Le thalamus puis le cortex pariétal reçoivent les deux canaux, car une lésion hémisphérique peut n'emporter que la sensibilité d'un hémicorps", "rmsnp")
s("Le nerf périphérique mélange les deux calibres de fibres sur une grande longueur, car une polyneuropathie distale touche d'abord les axones les plus longs", "rmsnp")
s("L'hyperglycémie chronique lèse ces axones longs, car le diabète explique trente à quarante pour cent des polyneuropathies et domine ce mécanisme", "rmsnp")
s("L'alcool lèse le nerf directement ou par carence en thiamine, car la revue suisse retient les deux mécanismes sans les opposer", "rmsnp")
s("La carence en cobalamine lèse surtout les grosses fibres et les cordons postérieurs, car l'ataxie de marche peut précéder l'anémie", "rmsnp")
s("Une hernie cervicale déforme la racine et l'irrite par des médiateurs, car la douleur ne se résume pas à la compression mécanique", "rmshdc")
s("La racine cervicale sept (C7) est la plus souvent touchée, suivie de la racine cervicale six (C6), car la revue suisse donne cet ordre", "rmshdc")
s("Plus de 90 % des maladies discales cervicales symptomatiques intéressent les espaces (C5)-(C6) et (C6)-(C7), car la revue suisse le chiffre", "rmshdc")
s("La myéline du nerf médian souffre quand la pression du canal carpien monte, car l'ischémie locale ralentit la conduction", "ulg")
s("Une atteinte aiguë, asymétrique ou non longueur-dépendante sort de ce schéma, car elle doit faire chercher une autre lésion", "rmsnp")

fen("p3", "f-moelle", "Coupe de moelle thoracique", [
    seul("Le schéma du haut est une coupe thoracique publiée par OpenStax le dix-huit mai deux mille seize, car la licence permet de la reproduire avec le crédit", "openstax"),
    seul("La matière grise est dessinée en jaune et forme les cornes, car la corne postérieure reçoit les fibres sensitives qui entrent par la racine", "openstax"),
    seul("La corne latérale et la corne antérieure sont nommées à part, car la corne antérieure porte les motoneurones et non le premier relais sensitif", "openstax"),
    seul("Les colonnes postérieures blanches sont légendées derrière la grisaille, car le tact fin et la pallesthésie y montent avant le bulbe", "openstax", "rmsnp"),
    seul("Les colonnes latérales et antérieures entourent le reste, car les voies spinothalamiques et les voies motrices y voisinent sans se confondre", "openstax", "rmsnp"),
    seul("Le canal central est le petit anneau au milieu, car il sert de repère et ne porte pas lui-même la sensibilité cutanée", "openstax"),
    seul("La lame du bas est une histologie au grossissement quarante, prêtée par l'université du Michigan en deux mille douze, car le papillon gris y reste visible", "openstax"),
    seul("Cette image sépare une lésion de cordon, qui suit un niveau, d'une lésion de nerf, qui suit un territoire distal", "openstax"),
    seul("Elle ne montre pas le cerveau, car l'infarctus sensitif se cherche au-dessus de cette coupe et non dans la moelle", "openstax", "ofsavc"),
    seul("Aucune flèche n'a été ajoutée, car le fichier original reste intact et les légendes anglaises suffisent à nommer les repères", "openstax"),
])

tableau("p3", "Perturbation, exploration qui la montre, traitement qui la corrige",
        ["Perturbation", "Exploration", "Thérapeutique"],
        [
            [seul("L'axone distal long dégénère dans le diabète, car les fibres les plus longues souffrent en premier", "rmsnp"),
             seul("Le diapason et le monofilament montrent cette perte, car le dépistage annuel des pieds repose sur ces deux gestes", "rmsage"),
             seul("Le contrôle de la glycémie réduit le risque dans le type un, car l'évidence est moindre quand l'atteinte du type deux est déjà là", "rmsnp")],
            [seul("La pression du canal carpien ischémie le nerf médian, car la conduction focale ralentit sous le ligament", "ulg"),
             seul("La compression carpienne pendant trente secondes aide au diagnostic, car sa sensibilité atteint 87 % et sa spécificité 90 %", "ulg"),
             seul("La levée de la compression traite la cause focale, car le cours liégeois décrit une compression chronique du médian", "ulg")],
            [seul("Le cordon postérieur se démyélinise quand la cobalamine manque, car la pallesthésie tombe avant l'anémie", "rmsnp"),
             seul("Le sens de position et la marche talonnante montrent cette colonne, car l'ataxie est le signe d'appel", "rmsage"),
             seul("La supplémentation en cobalamine vise la récupération, car elle s'observe entre six semaines et trois mois selon la durée du manque", "rmsnp")],
            [seul("La racine cervicale est déformée et enflammée par la hernie, car les deux mécanismes additionnent la douleur", "rmshdc"),
             seul("L'examen racine par racine puis l'image montrent la concordance, car une image sans signe clinique ne décide pas", "rmshdc"),
             seul("La chirurgie s'impose si le déficit progresse ou si la douleur résiste six à huit mois, car la revue fixe ces deux portes", "rmshdc")],
        ])

use("p4")
s("La démarche commence par les formes qui tuent ou paralysent vite, car le rang de fréquence ne protège pas d'une erreur d'heure", "ofsavc", "gbses", "rmshdc")
s("L'infarctus cérébral ou l'" + L("f-e1", "accident ischémique transitoire") + " sensitif est le rang d'exclusion un, car la létalité suisse des attaques est de 12,2 %", "obsanavc")
s("La myélopathie cervicale compressive est le rang d'exclusion deux, car une myélopathie symptomatique indique déjà la chirurgie", "rmshdc")
s("Le syndrome de Guillain-Barré est le rang d'exclusion trois, car onze pour cent des patients espagnols ont eu besoin d'une ventilation", "gbses")
s("La mononévrite multiple des vasculites est le rang d'exclusion quatre, car la suspicion impose des investigations rapides", "rmsnp")
s("Ensuite seulement viennent les maladies fréquentes, car le diabète reste la cause la plus commune des polyneuropathies distales", "rmsnp")
s("Le canal carpien vient après, car c'est la neuropathie tronculaire focale la plus fréquente et sa prévalence clinique suédoise est de 3,8 %", "ulg", "atroshi")
s("La radiculopathie cervicale suit, car 3,3 pour 1 000 dépasse les 174 à 187 pour 100 000 de la sclérose en plaques en deux mille seize", "rmshdc", "mssuisse")
s("La neuropathie alcoolique et la carence en cobalamine viennent ensuite, car les deux articles suisses les placent parmi les causes majeures à chercher d'emblée", "rmsnp", "rmsage")
s("La sclérose en plaques (SEP) précède l'attaque cérébrale dans ce rang de stock, car dix-huit mille personnes vivent avec elle alors que l'attaque est comptée en cas annuels", "mssuisse", "ofsavc")
s("Ce rang mélange des prévalences et des incidences, car aucune cohorte suisse n'a suivi un même motif sensitif jusqu'au diagnostic final", "rmsnp")
s("Le " + L("f-compar", "tableau comparatif") + " tient les dix maladies sur une ligne, car le signe qui tranche évite de les confondre", "rmsnp")

fen("p4", "f-e1", "Exclusion de l'ischémie cérébrale sensitive", [
    seul("Un trouble sensitif d'installation soudaine sur un hémicorps fait chercher l'attaque cérébrale avant la polyneuropathie, car le temps cérébral ne se rattrape pas", "ofsavc"),
    seul("L'Office fédéral de la statistique (OFS) a compté 22 517 attaques en deux mille vingt-trois, car le volume national interdit de traiter ce motif comme bénin par défaut", "ofsavc"),
    seul("La létalité de 12,2 % mesure toutes les attaques de la période, car la fraction seulement sensitive n'est pas publiée à part", "obsanavc"),
    seul("Un épisode qui régresse fait craindre l'accident ischémique transitoire (AIT), car la revue des attaques compte aussi les événements qui annoncent un infarctus", "ofsavc"),
    seul("La glycémie capillaire se mesure tout de suite si la vigilance baisse, car une confusion ne doit pas retarder la filière vasculaire ni masquer une autre urgence", "rmsage"),
])

# Comparatif : dix lignes, cinq colonnes, phrases verbales
rows = []
data = [
    ("Polyneuropathie diabétique distale symétrique",
     "Le patient décrit un territoire en chaussettes, car la longueur de l'axone décide du siège",
     "Le diapason et le monofilament confirment la perte distale, car le dépistage annuel repose sur eux",
     "L'hyperglycémie chronique lèse d'abord les axones les plus longs, car le diabète est la cause la plus commune",
     "On traite la glycémie et l'on protège le pied, car la douleur se discute sans dose recopiée ici",
     "rmsnp"),
    ("Syndrome du canal carpien",
     "Les paresthésies réveillent la main dans le territoire médian, car la plainte nocturne oriente vers le canal",
     "La compression du poignet pendant trente secondes atteint 87 % de sensibilité, car le cours liégeois donne aussi 90 % de spécificité",
     "La pression intracanalaire ischémie le médian, car la conduction focale ralentit sous le ligament",
     "On lève la compression quand le déficit s'installe, car la cause est mécanique et focale",
     "ulg"),
    ("Radiculopathie cervicale par hernie discale",
     "La douleur suit une racine et le cou la déclenche, car la toux peut l'augmenter",
     "La concordance entre la racine clinique et l'image tranche, car une image isolée ne suffit pas",
     "La hernie déforme la racine et l'enflamme, car plus de 90 % des formes symptomatiques siègent sur deux espaces",
     "On opère si le déficit progresse ou si la douleur dure six à huit mois, car la plupart guérissent sans chirurgie",
     "rmshdc"),
    ("Polyneuropathie alcoolique",
     "La douleur distale domine chez une personne qui boit au-delà du seuil, car la revue fixe ce seuil à plus de 30 grammes par jour",
     "L'anamnèse de consommation et le déficit cérébelleux associé orientent, car la carence en thiamine peut s'y ajouter",
     "La toxicité directe et la carence vitaminique coexistent, car la revue suisse retient les deux",
     "L'arrêt de l'alcool et la vitamine précoce améliorent surtout les formes récentes, car le délai compte",
     "rmsnp"),
    ("Sclérose combinée de la moelle par carence en cobalamine",
     "L'ataxie et la chute de la pallesthésie peuvent exister sans anémie, car le signe neurologique ne dépend pas de l'hémogramme",
     "La cobalamine basse, ou l'homocystéine et l'acide méthylmalonique si la valeur est limite, confirment le manque",
     "Les cordons postérieurs et les grosses fibres manquent de cobalamine, car la marche se dégrade",
     "On supplémente, par voie intramusculaire si le manque est sévère ou l'absorption rompue, car la récupération prend six semaines à trois mois",
     "rmsnp"),
    ("Sclérose en plaques",
     "Des poussées sensitives disseminées dans le temps frappent souvent un adulte jeune, car la société suisse compte 18 000 personnes atteintes",
     "L'imagerie par résonance magnétique (IRM) cherche des lésions disséminées, car le diagnostic de maladie ne se pose pas sur un picotement isolé",
     "L'inflammation démyélinise le système nerveux central par poussées, car le rapport est de 2,7 femmes pour un homme",
     "La filière spécialisée décide du traitement de fond, car cette leçon ne recopie aucune dose",
     "mssuisse"),
    ("Infarctus cérébral ou accident ischémique transitoire sensitif",
     "Le déficit sensitif s'installe en minutes sur un hémicorps, car cette cinétique n'est pas celle d'une chaussette chronique",
     "La filière neurovasculaire et l'imagerie cérébrale tranchent, car attendre un électroneuromyogramme ferait perdre la fenêtre",
     "L'ischémie d'un territoire cérébral coupe la voie sensitive après le thalamus ou le cortex, car la létalité globale est de 12,2 %",
     "On active la filière d'attaque sans retard, car l'incidence standardisée atteint 249,4 pour 100 000",
     "obsanavc"),
    ("Myélopathie cervicale compressive",
     "Un niveau sensitif, une maladresse des mains et des signes pyramidaux définissent la moelle, car la douleur seule ne suffit pas",
     "L'imagerie du canal cervical corrélée au signe clinique tranche, car 85 % des gens âgés ont une image et restent sans symptôme",
     "Le rétrécissement du canal comprime les cordons, car la myélopathie symptomatique indique la chirurgie par elle-même",
     "On adresse en neurochirurgie sans attendre six mois, car ce délai concerne la radiculopathie douloureuse et non la moelle symptomatique",
     "rmshdc"),
    ("Syndrome de Guillain-Barré",
     "Les paresthésies montent en jours avec une aréflexie, car la faiblesse peut suivre de quelques heures",
     "Le liquide et la conduction nerveuse aident, car la surveillance respiratoire ne doit pas attendre leur résultat",
     "L'inflammation aiguë des racines suit souvent une infection, car l'incidence espagnole moyenne est de 1,67 pour 100 000",
     "On surveille la ventilation et l'on hospitalise, car onze pour cent des patients de la série espagnole ont été ventilés",
     "gbses"),
    ("Mononévrite multiple des vasculites",
     "Des déficits douloureux de plusieurs nerfs s'additionnent en jours ou en semaines, car le tableau n'est pas longueur-dépendant",
     "Le bilan inflammatoire et la biopsie ciblée tranchent, car le sang peut rester normal quand la vasculite est limitée au nerf",
     "L'ischémie focale du nerf par vascularite explique les étapes, car 77 % de ces vasculites touchent le nerf",
     "On lance les investigations sans délai, car la revue suisse en fait une consigne et non une option",
     "rmsage"),
]
for nom, a, b, c3, d, src in data:
    rows.append([
        seul(f"Le diagnostic retenu est {nom}, car il concurrence réellement un trouble de la sensibilité", src),
        seul(a, src), seul(b, src), seul(c3, src), seul(d, src),
    ])
tableau("p4", "Dix diagnostics : signe clé, examen qui tranche, mécanisme, conduite immédiate",
        ["Diagnostic", "Signe clé", "Examen qui tranche", "Mécanisme", "Conduite immédiate"],
        rows)
fen("p4", "f-compar", "Comment lire le tableau des dix diagnostics", [
    seul("Chaque ligne est une maladie et non un symptôme, car un fourmillement ou un terrain ne constituent pas un diagnostic différentiel", "rmsnp"),
    seul("Le diabète reste en tête des polyneuropathies, car il explique 30 à 40 % des cas dans la mise au point de médecine interne", "rmsnp"),
    seul("Le canal carpien n'est pas une polyneuropathie, car c'est une compression focale du médian dont la prévalence clinique européenne atteint 3,8 %", "atroshi"),
    seul("Les quatre dernières lignes portent un rang d'exclusion, car leur rareté ne diminue pas le devoir de les écarter d'abord", "gbses", "rmshdc"),
])

use("p5")
s("Chaque question d'anamnèse cherche un mécanisme, car un siège, un horaire et une vitesse suffisent souvent à changer la filière", "rmsnp")
s("On demande depuis quand le trouble a commencé, car une installation en minutes oriente vers l'ischémie et une installation en années vers l'axone", "ofsavc", "rmsnp")
s("On demande si les deux pieds sont touchés ensemble, car la symétrie longueur-dépendante évoque la polyneuropathie distale", "rmsnp")
s("On demande si la nuit réveille les doigts, car le canal carpien donne des acroparesthésies d'abord matinales puis nocturnes", "ulg")
s("On demande si le cou, la toux ou le valsalva augmentent la douleur du bras, car la racine cervicale se comporte ainsi", "ulg", "rmshdc")
s("On demande les chutes récentes, car la vignette suisse décrit une patiente de 77 ans avec trois chutes en deux semaines", "rmsage")
s("On demande l'alcool en verres, car le seuil de risque cité est de plus de 30 grammes par jour", "rmsnp")
s("On demande la metformine et les inhibiteurs de pompe, car ces médicaments comptent parmi les causes de manque de cobalamine", "rmsnp")
s("On demande une chimiothérapie par platine, taxane, vinca, bortézomib ou thalidomide, car 60 % des patients traités développent une neuropathie", "rmsnp")
s("On demande un diabète connu et des plaies de pied, car 25 % des neuropathies diabétiques sont douloureuses et le déficit favorise le mal perforant", "rmsnp")
s("On demande les troubles sphinctériens et la ceinture qui monte, car ces deux réponses font craindre la moelle avant le nerf", "rmshdc")
s("On demande une faiblesse qui monte et un essoufflement, car le Guillain-Barré menace la ventilation dans les jours qui suivent", "gbses")
s("On demande une infection récente, car le Guillain-Barré suit souvent un épisode infectieux dans les séries européennes", "gbsuk")
s("Le " + L("f-drapeaux", "drapeau rouge") + " n'est utile que s'il dicte un geste, car une liste sans action ne change pas la prise en charge", "rmsnp")

fen("p5", "f-drapeaux", "Drapeaux rouges et geste imposé", [
    seul("Une installation en minutes impose la filière d'attaque cérébrale, car 2 580 décès ont été attribués aux attaques en deux mille vingt-trois", "ofsavc"),
    seul("Un niveau sensitif ou un trouble sphinctérien impose l'imagerie de la moelle, car la myélopathie symptomatique est déjà une indication chirurgicale", "rmshdc"),
    seul("Une aréflexie avec paresthésies ascendantes impose l'hôpital et la mesure de la respiration, car onze pour cent des cas espagnols ont été ventilés", "gbses"),
    seul("Plusieurs nerfs touchés en peu de temps imposent un bilan de vasculite, car la revue demande des investigations rapides même si le sang est normal", "rmsnp"),
    seul("Une ataxie de marche chez une personne âgée impose le dosage de la cobalamine, car le signe neurologique peut précéder l'anémie", "rmsnp"),
    seul("Une hypotension orthostatique ou une atteinte motrice marquée impose l'avis neurologique, car la mise au point suisse en fait un motif d'adressage", "rmsnp"),
])

tableau("p5", "Drapeau rouge, signification, action immédiate",
        ["Drapeau", "Signification", "Action immédiate"],
        [
            [seul("Le trouble sensitif apparaît en minutes sur un hémicorps, car cette vitesse est vasculaire jusqu'à preuve du contraire", "ofsavc"),
             seul("Un territoire cérébral est menacé, car la létalité moyenne des attaques atteint 12,2 %", "obsanavc"),
             seul("On active la filière d'attaque sans attendre un avis de neuropathie, car le retard coûte la fenêtre de reperfusion", "ofsavc")],
            [seul("Un niveau sensitif s'accompagne d'une faiblesse des jambes ou d'un sphincter, car la moelle est alors le site probable", "rmshdc"),
             seul("Les cordons sont comprimés, car l'image cervicale asymptomatique est fréquente mais ne rassure pas si le signe est là", "rmshdc"),
             seul("On demande une imagerie médullaire en urgence, car la chirurgie ne se diffère pas quand la myélopathie est symptomatique", "rmshdc")],
            [seul("Les fourmillements montent et les réflexes disparaissent, car ce couple évoque le Guillain-Barré", "gbses"),
             seul("La ventilation peut chuter en jours, car onze pour cent des patients de la série ont été assistés", "gbses"),
             seul("On hospitalise et l'on mesure la respiration, car le traitement spécifique ne se décide pas au domicile", "gbses")],
            [seul("Des nerfs distincts tombent les uns après les autres, car ce rythme évoque la vasculite plutôt que la longueur de l'axone", "rmsage"),
             seul("Le nerf est ischémié par le vaisseau, car 77 % de ces vasculites s'expriment sur le nerf périphérique", "rmsage"),
             seul("On lance le bilan inflammatoire et l'on adresse, car la revue suisse exige des investigations rapides", "rmsnp")],
        ])

use("p6")
s("On examine d'abord le normal attendu selon l'âge, car le seuil du diapason change déjà entre trente ans et cinquante ans", "rmsnp")
s("Au doigt ou à l'orteil, la limite inférieure du diapason gradué est de 6,9 sur 5,5 entre vingt et trente-neuf ans", "rmsnp")
s("Entre quarante et soixante ans, cette limite passe à 6,2 sur 4,7, car l'âge abaisse le seuil sans qu'il s'agisse encore d'une maladie", "rmsnp")
s("La vignette du sujet âgé montre une hypopallesthésie bimalléolaire à 2 sur 8, car ce chiffre est déjà pathologique par rapport aux normes adultes", "rmsage")
s("On examine d'abord les pieds, le tact, la piqûre et le froid, car le sens protopathique se teste aux orteils dans la polyneuropathie", "rmsnp")
s("On cherche une limite en chaussettes qui remonte, car cette géographie signe la longueur de l'axone et non un dermatome", "rmsage")
s("Le monofilament et le diapason se font chaque année chez la personne diabétique, car l'article du sujet âgé en fait un dépistage de routine", "rmsage")
s("On regarde la plante, la kératose et la plaie, car le déficit sensitif est un facteur de mal perforant", "rmsnp")
s("Aux mains, on compare le majeur et l'auriculaire, car le médian épargne le cinquième doigt quand on réinterroge le patient", "ulg")
s("Le déficit tactile peut manquer dans 20 à 50 % des canaux carpiens, car l'absence de signe sensitif n'écarte pas la compression", "ulg")
s("La pince pouce-index faible et l'amyotrophie thénarienne viennent tard, car le cours liégeois les réserve aux formes sévères", "ulg")
s("Le test de compression pendant trente secondes se fait poignet tenu, car sa sensibilité est de 87 % et sa spécificité de 90 %", "ulg")
s("Au cou et au bras, on cherche la racine et non le tronc, car la douleur de racine s'accompagne d'un réflexe diminué sur le myotome", "rmshdc")
s("On cherche un niveau sur le tronc avec un coton, car un niveau horizontal oriente vers la moelle et non vers le nerf distal", "rmshdc")
s("On cherche un signe pyramidal, une vivacité des réflexes et un clonus, car la myélopathie ajoute un syndrome central à la perte sensitive", "rmshdc")
s("Aux réflexes achilléens, l'abolition bilatérale va avec la polyneuropathie, car la vignette suisse la décrit avec l'ataxie", "rmsage")
s("La marche, le Romberg et le demi-tour cherchent l'ataxie, car le cordon postérieur et la grosse fibre se voient mieux debout", "rmsage")
s("Au visage et à l'hémicorps, on cherche un déficit qui coupe la ligne médiane, car ce dessin est cérébral et non périphérique", "ofsavc")
s("On chronomètre la force de la nuque et la toux si les paresthésies montent, car la ventilation du Guillain-Barré se surveille cliniquement", "gbses")
s("L'" + L("f-examen", "ordre de l'examen") + " suit le patient réel, car on commence par le geste qui écarte la forme grave avant le geste de confort", "rmshdc")

fen("p6", "f-examen", "Ordre de l'examen chez un patient sensitif", [
    seul("On observe d'abord la vigilance, la face et la parole, car un hémicorps sensitif aigu change la filière avant le déshabillage des pieds", "ofsavc"),
    seul("On demande ensuite de tousser et de compter, car une voix qui s'éteint évoque le Guillain-Barré plus qu'une chaussette chronique", "gbses"),
    seul("On palpe le ventre et l'on interroge le sphincter si les jambes faiblissent, car la moelle compressive ne se laisse pas pour la fin", "rmshdc"),
    seul("On teste alors le niveau sur le tronc, puis les réflexes, car un réflexe vif avec un niveau n'est pas une polyneuropathie", "rmshdc"),
    seul("On termine par les pieds, le diapason et le monofilament, car ces gestes caractérisent la forme fréquente une fois l'urgence écartée", "rmsage"),
    seul("Aux mains, le test de compression dure trente secondes, car le cours liégeois en publie la sensibilité et la spécificité", "ulg"),
])

use("p7")
s("Le premier syndrome est la polyneuropathie distale symétrique, car les deux pieds brûlent ou s'endorment et la limite remonte en chaussettes", "rmsnp")
s("Ses signes physiques sont la baisse du diapason, l'hypoesthésie distale et l'aréflexie achilléenne, car la grosse fibre et la petite fibre peuvent se combiner", "rmsnp")
s("Le deuxième syndrome est le canal carpien, car les doigts médians fourmillent la nuit et le cinquième doigt est épargné quand on précise la plainte", "ulg")
s("Le troisième syndrome est la radiculopathie cervicale, car la douleur part du cou, suit une racine et peut s'accompagner d'un réflexe aboli", "rmshdc")
s("Le quatrième syndrome est l'ischémie cérébrale sensitive, car l'hémicorps devient cotonneux en minutes, avec ou sans trouble du langage", "ofsavc")
s("Le cinquième syndrome est la myélopathie compressive, car un niveau, une main maladroite et un signe pyramidal se tiennent ensemble", "rmshdc")
s("Le sixième syndrome est le Guillain-Barré, car les paresthésies montent, les réflexes tombent et la force peut suivre en heures", "gbses")
s("Le septième syndrome est la mononévrite multiple, car des nerfs successifs deviennent douloureux et déficitaires sans respecter la longueur", "rmsage")
s("Le huitième syndrome est la sclérose combinée, car la pallesthésie s'effondre, la marche talonne et l'anémie peut manquer", "rmsnp")
s("Chaque syndrome se cherche par un geste unique, car multiplier les tests sans hypothèse noie le signe qui tranche", "rmsnp")

tableau("p7", "Syndromes, signes fonctionnels, signes physiques",
        ["Syndrome", "Signes fonctionnels", "Signes physiques"],
        [
            [seul("La polyneuropathie distale symétrique évolue sur des mois, car les axones longs sont touchés ensemble", "rmsnp"),
             seul("Le patient décrit des brûlures ou un engourdissement des deux pieds, car la plainte remonte ensuite vers les mains", "rmsage"),
             seul("Le diapason baisse aux malléoles et le réflexe achilléen disparaît, car la vignette suisse réunit ces deux signes", "rmsage")],
            [seul("Le canal carpien comprime le médian au poignet, car la neuropathie focale la plus fréquente siège là", "ulg"),
             seul("Les doigts médians fourmillent la nuit et le patient secoue la main, car ce horaire est classique dans le cours liégeois", "ulg"),
             seul("La compression de trente secondes réveille la plainte, car le déficit objectif peut manquer dans 20 à 50 % des cas", "ulg")],
            [seul("La myélopathie compressive rétrécit le canal, car le signe clinique et non l'image seule pose l'indication", "rmshdc"),
             seul("Les mains deviennent maladroites et les jambes raides, car le patient peut décrire un niveau sur le tronc", "rmshdc"),
             seul("Les réflexes sont vifs et un signe pyramidal est présent, car ce tableau s'oppose à l'aréflexie de la polyneuropathie", "rmshdc")],
            [seul("Le Guillain-Barré enflamme les racines en jours, car l'incidence reste proche de 1,67 pour 100 000", "gbses"),
             seul("Les fourmillements montent des pieds vers les genoux, car la faiblesse et l'essoufflement peuvent suivre", "gbses"),
             seul("Les réflexes sont abolis et la toux est faible, car la ventilation se juge au lit avant le résultat du liquide", "gbses")],
        ])

use("p8")
s("Le motif est affirmé quand l'un des six phénomènes de la taxonomie est présent, car la société savante les a définis sans exiger un mécanisme", "iasp")
s("Une plainte de picotement non désagréable correspond à la paresthésie, car la définition de deux mille onze exige que la sensation ne soit pas désagréable", "iasp")
s("Une sensation désagréable, spontanée ou provoquée, correspond à la dysesthésie, car la frontière avec la paresthésie se décide avec le patient", "iasp")
s("Une baisse de la sensibilité à un stimulus nommé, hors les sens spéciaux, correspond à l'hypoesthésie, car le lieu doit être écrit", "iasp")
s("Une douleur plus forte pour un stimulus déjà douloureux correspond à l'hyperalgésie, car le mode du stimulus reste le même", "iasp")
s("Le motif n'est pas affirmé par une image isolée, car 85 % des personnes dans leur septième décennie ont une modification cervicale et restent souvent sans symptôme", "rmshdc")
s("Le motif n'est pas affirmé par un ralentissement électrique isolé, car 18,4 % des témoins suédois avaient une neuropathie médiane sans que le chiffre ne vaille diagnostic", "atroshi")
s("La polyneuropathie distale est retenue quand le déficit est distal, symétrique et longueur-dépendant, car la mise au point suisse limite ainsi son champ", "rmsnp")
s("Elle n'est pas retenue si le déficit est aigu, asymétrique, moteur au premier plan ou dysautonomique sévère, car ces traits imposent un autre cadre", "rmsnp")
s("Aucun score unique ne classe les dix maladies de ce motif, car les critères de chacune restent ceux de sa société et non un barème commun", "rmsnp")
s("L'échelle de douleur neuropathique est citée par la revue pour suivre la douleur, car cette leçon ne récite pas une cotation absente de l'extrait lu", "rmsnp")

tableau("p8", "Ce qui affirme le motif, ce qui ne suffit pas",
        ["Proposition", "Décision"],
        [
            [seul("Le patient décrit une paresthésie, une dysesthésie, une hypoesthésie ou une hyperalgésie au sens de la taxonomie, car le lieu et le stimulus sont précisés", "iasp"),
             seul("Le motif sensitif est affirmé, car la définition clinique est remplie sans qu'un mécanisme soit encore choisi", "iasp")],
            [seul("Une image cervicale montre une usure chez une personne de la septième décennie, car 85 % de ces personnes portent de telles modifications", "rmshdc"),
             seul("Le diagnostic de myélopathie n'est pas posé, car la revue rappelle que la plupart de ces images restent asymptomatiques", "rmshdc")],
            [seul("La conduction du médian est ralentie chez une personne sans plainte, car 18,4 % des témoins suédois étaient dans ce cas", "atroshi"),
             seul("Le canal carpien n'est pas affirmé, car il faut la plainte clinique et non le seul tracé", "atroshi")],
        ])

use("p9")
s("Le gold standard du motif, au sens de la première reconnaissance, est clinique, car l'anamnèse et l'examen décident d'aller plus loin", "rmsnp")
s("En première intention, l'interniste cherche l'alcool, le diabète, la cobalamine et la gammapathie, car la mise au point suisse limite ainsi le bilan", "rmsnp")
s("La glycémie ou l'hémoglobine glyquée, la cobalamine et l'électrophorèse des protéines entrent dans ce premier sang, car la revue les place avant l'électricité", "rmsnp")
s("Les recommandations françaises ajoutent la formule sanguine, la protéine C réactive (CRP), les tests hépatiques, la créatinine et la thyréostimuline (TSH)", "rmsnp")
s("Ce complément européen cherche l'anémie, l'inflammation, l'alcool, le rein et la thyroïde, car la revue suisse le rapporte ainsi", "rmsnp")
s("Même devant un diabète évident, ce bilan de base reste indiqué, car une autre cause est présente dans 53 % des neuropathies de patients diabétiques", "rmsnp")
s("L'électroneuromyogramme (ENMG) n'est pas un examen de première ligne, car il est réservé aux formes atypiques ou sans cause claire", "rmsnp")
s("Si la cobalamine est limite, l'homocystéine et l'acide méthylmalonique confirment le manque, car la revue suisse indique ces deux dosages", "rmsnp")
s("Dans la vignette publiée, l'hémoglobine est à 108 grammes par litre, le volume globulaire à 101 femtolitres et les réticulocytes à 35 giga par litre", "rmsage")
s("La cobalamine de cette vignette est à 100 picomoles par litre et l'hémoglobine glyquée à 8 %, car plusieurs causes se superposent", "rmsage")
s("Le débit de filtration glomérulaire (DFG) y est de 49 millilitres par minute, car le rein participe alors au tableau", "rmsage")
s("L'imagerie cérébrale passe devant le sang quand le trouble est soudain et latéralisé, car la filière d'attaque ne se subordonne pas au bilan de neuropathie", "ofsavc")
s("L'imagerie du rachis cervical passe devant l'électricité quand un niveau ou un signe pyramidal est présent, car la moelle symptomatique est une indication chirurgicale", "rmshdc")
s("La biopsie nerveuse reste de deuxième intention, car elle cherche une vasculite, une amylose ou une inflammation traitable", "rmsage")
s("Sans cause préalable, seulement 17,5 % des biopsies de personnes âgées changent la prise en charge, car le geste ne se généralise pas", "rmsage")
s("Si l'imagerie par résonance est impossible, le scanner du canal ou l'avis neurochirurgical prennent le relais, car la décision de moelle ne peut pas rester sans image", "rmshdc")
s("Chez la personne enceinte, on évite d'abord l'irradiation et l'on privilégie l'examen clinique, car aucune dose médicamenteuse n'est fixée dans cette leçon", "rmsnp")
s("Si le débit est très bas, on lit la neuropathie avec le rein, car 70 % ou 90 % des stades terminaux s'accompagnent d'une atteinte", "rmsage", "rmsnp")
s("Cette " + L("f-sang", "lecture du sang") + " oriente chaque anomalie vers une conduite, car un chiffre isolé doit changer le geste", "rmsage")

fen("p9", "f-sang", "Interprétation du bilan initial", [
    seul("Une hémoglobine glyquée haute confirme l'exposition glucidique, car la vignette publie 8 % chez une patiente déjà traitée par metformine", "rmsage"),
    seul("Une cobalamine à 100 picomoles par litre affirme le manque dans cette vignette, car le chiffre se lit avec l'ataxie et non seul", "rmsage"),
    seul("Un volume globulaire à 101 femtolitres avec une hémoglobine à 108 grammes par litre montre une macrocytose, car l'anémie peut aussi manquer dans d'autres dossiers", "rmsage"),
    seul("Un débit à 49 millilitres par minute classe un stade G3a, car l'article du sujet âgé utilise cette borne pour l'insuffisance modérée", "rmsage"),
    seul("Une électrophorèse anormale ne signifie pas à elle seule une neuropathie, car 3 à 4 % des plus de cinquante ans portent une immunoglobuline monoclonale", "rmsnp"),
    seul("L'électricité nerveuse attend que ce sang soit lu, car la revue la réserve aux présentations atypiques ou sans cause", "rmsnp"),
])

tableau("p9", "Résultat, signification, conduite",
        ["Résultat", "Signification", "Conduite"],
        [
            [seul("La glycémie ou l'hémoglobine glyquée est haute, car l'exposition chronique est alors documentée", "rmsnp"),
             seul("Le diabète peut expliquer la polyneuropathie, car il reste la cause la plus commune", "rmsnp"),
             seul("On traite la glycémie et l'on inspecte les pieds, car une autre cause coexiste encore dans 53 % des cas", "rmsnp")],
            [seul("La cobalamine est basse ou les métabolites montent, car le manque est confirmé même sans anémie", "rmsnp"),
             seul("Les cordons postérieurs et les grosses fibres manquent de substrat, car l'ataxie en est le signe", "rmsage"),
             seul("On supplémente et l'on cherche la malabsorption, car la récupération se juge entre six semaines et trois mois", "rmsnp")],
            [seul("L'électrophorèse montre une immunoglobuline monoclonale, car 3 à 4 % des plus de cinquante ans sont dans ce cas", "rmsnp"),
             seul("Une hémopathie ou une gammapathie peut tenir la neuropathie, car la prévalence de l'atteinte va de 8 à 36 % dans ce groupe", "rmsage"),
             seul("On adresse en hématologie si la neuropathie évolue, car le traitement est celui de l'hémopathie et non un symptomatique isolé", "rmsnp")],
            [seul("Le débit glomérulaire tombe sous 60 millilitres par minute, car l'article du sujet âgé retient cette borne", "rmsage"),
             seul("Le rein peut ajouter une neuropathie indolente, car la prévalence atteint 42 % dans la cohorte de 2 290 personnes âgées", "rmsage"),
             seul("On ralentit la maladie rénale et l'on discute la suppléance si le stade terminal approche, car l'atteinte peut alors concerner 70 % des patients", "rmsage")],
        ])

use("p10")
s("Si le trouble sensitif est soudain et latéralisé, alors on ouvre la filière d'attaque cérébrale, car c'est le rang d'exclusion un", "obsanavc")
s("Si un niveau, un sphincter ou un signe pyramidal apparaît, alors on image la moelle, car la myélopathie symptomatique indique la chirurgie", "rmshdc")
s("Si les paresthésies montent avec une aréflexie, alors on hospitalise pour la respiration, car onze pour cent des cas espagnols ont été ventilés", "gbses")
s("Si plusieurs nerfs tombent en peu de temps, alors on cherche une vasculite, car les investigations doivent être rapides", "rmsnp")
s("Si les deux pieds sont touchés depuis des mois, alors on fait le sang de base, car l'alcool, le diabète, la cobalamine et la gammapathie s'y lisent", "rmsnp")
s("Si les doigts médians fourmillent la nuit, alors on teste la compression du poignet, car le canal carpien est la neuropathie focale la plus fréquente", "ulg")
s("Si la douleur suit une racine cervicale, alors on corrèle l'examen et l'image, car plus de 90 % des patients guérissent sans chirurgie", "rmshdc")
s("Si l'ataxie domine sans anémie, alors on dose la cobalamine, car le signe neurologique peut être isolé", "rmsnp")
s("Si le premier bilan est négatif et que des options thérapeutiques existent, alors on adresse au neurologue, car l'article du sujet âgé le recommande à ce moment", "rmsage")
s("Si la forme est typique et la cause claire, alors l'électricité nerveuse peut attendre, car la revue la réserve aux dossiers atypiques", "rmsnp")

use("p11")
s("Le but immédiat est d'écarter en heures les quatre rangs d'exclusion, car une attaque, une moelle, un Guillain-Barré ou une vasculite ne se traitent pas comme une chaussette", "obsanavc", "gbses")
s("Le but ensuite est de nommer une cause réversible et de protéger la marche, car l'article du sujet âgé vise l'autonomie autant que la douleur", "rmsage")
s("La " + L("f-urgence", "conduite chronologique") + " suit l'ordre des rangs d'exclusion, car chaque geste attend le signe qui le déclenche et non une horloge arbitraire", "rmshdc")
s("Le traitement de la cause passe avant le traitement du symptôme, car la revue suisse corrige d'abord ce qui peut l'être", "rmsage")
s("L'arrêt de l'alcool au-dessus de 30 grammes par jour et la vitamine précoce améliorent surtout la neuropathie récente, car le délai de prise en charge compte", "rmsnp")
s("La supplémentation en cobalamine se fait par voie orale ou intramusculaire, car la voie intramusculaire est préférée si l'atteinte est sévère ou l'absorption rompue", "rmsnp")
s("Cette leçon ne recopie aucun milligramme, car la dose exacte reste hors information professionnelle intégrée ici et se lit sur le texte Swissmedic en vigueur", "rmsnp")
s("La prégabaline et la gabapentine sont citées pour la douleur diabétique, car leur dose chiffrée de revue est hors information professionnelle Swissmedic (AIPS)", "rmsage")
s("L'amitriptyline ou la nortriptyline viennent en cas d'intolérance, car la revue demande de faibles doses initiales et des contrôles rapprochés sans en donner le chiffre", "rmsage")
s("La capsaïcine est une deuxième ligne et les opioïdes un dernier recours, car la mise au point suisse le dit sans milligramme", "rmsnp")
s("Les opioïdes se discutent avec un médecin formé à la douleur neuropathique, car la revue veut prévenir l'addiction", "rmsnp")
s("La rééducation, les semelles et l'aide à la marche font partie du traitement, car le déficit expose à la chute et peut gêner la conduite", "rmsage", "rmsnp")
s("La myélopathie symptomatique ne suit pas le délai de six à huit mois de la racine, car la revue lui donne une indication propre", "rmshdc")
s("Plus de 90 % des radiculopathies par hernie cervicale s'amendent sans chirurgie, car l'antalgie adaptée est le premier choix quand le déficit ne progresse pas", "rmshdc")
s("La grossesse et l'allaitement ne reçoivent ici aucune dose, car le texte mot pour mot de l'information professionnelle Swissmedic (AIPS) n'est pas recopié dans cette leçon", "rmsnp")
s("Chez la personne âgée, on commence bas et l'on revoit vite tout symptomatique, car la revue redoute le vertige, l'ataxie et la confusion", "rmsage")
s("Chez l'enfant, ce motif reste rare dans les sources lues, car les prévalences citées concernent l'adulte et le sujet âgé", "rmsnp")
s("Si le rein est très bas, la dialyse ou la greffe peuvent stopper la neuropathie urémique, car la revue suisse le rapporte", "rmsnp")
s("L'assurance-invalidité et l'arrêt de travail se discutent quand la marche ou la conduite sont perdues, car la revue signale l'incapacité de conduire liée au déficit", "rmsnp")
s("La surveillance de la ventilation dans le Guillain-Barré est continue à l'hôpital, car le pourcentage de 11 % mesure un besoin d'assistance et non un détail", "gbses")
s("On revoit la cobalamine entre six semaines et trois mois, car c'est la fenêtre de récupération neurologique citée par la revue", "rmsnp")
s("On revoit les pieds diabétiques au moins chaque année, car le diapason et le monofilament sont le dépistage recommandé", "rmsage")
s("La guérison du canal carpien se juge sur la disparition des réveils et le retour de la force, car le déficit sensitif objectif peut avoir manqué", "ulg")
s("La sortie après une attaque cérébrale dépend de la filière vasculaire, car cette leçon ne fixe pas un critère de sortie qui n'est pas dans les sources lues", "ofsavc")
s("Le pronostic de la polyneuropathie sans cause est souvent lent, car près d'un tiers des formes chroniques du sujet âgé restent sans étiologie", "rmsage")

fen("p11", "f-urgence", "Urgence — conduite dans l'ordre des rangs", [
    seul("D'abord on sécurise la vigilance et la respiration, car un Guillain-Barré ou une attaque peuvent les emporter avant le diagnostic de neuropathie", "gbses"),
    seul("Si le trouble est soudain et d'un côté, on appelle la filière d'attaque, car l'incidence suisse standardisée est de 249,4 pour 100 000", "obsanavc"),
    seul("Si un niveau ou un sphincter apparaît, on image la moelle le jour même, car la myélopathie symptomatique indique la chirurgie", "rmshdc"),
    seul("Si les réflexes tombent et que les paresthésies montent, on garde le patient, car onze pour cent ont été ventilés en Espagne", "gbses"),
    seul("Si des nerfs successifs tombent, on prélève le bilan de vasculite et l'on adresse, car la suspicion ne attend pas un électroneuromyogramme de confort", "rmsnp"),
    seul("Ensuite seulement on prélève le sang de base et l'on protège les pieds, car cette étape concerne la forme chronique une fois les quatre rangs écartés", "rmsnp"),
])

tableau("p11", "Molécule, place, limite de cette leçon",
        ["Molécule", "Place selon la source suisse", "Limite"],
        [
            [seul("La prégabaline est citée pour la polyneuropathie diabétique douloureuse, car la revue du sujet âgé lui reconnaît un bénéfice", "rmsage"),
             seul("Elle vient après la correction de la cause, car le symptomatique ne remplace pas le traitement du diabète", "rmsage"),
             seul("La dose est hors AIPS dans cette leçon, car aucun milligramme n'est recopié depuis l'information professionnelle", "rmsage")],
            [seul("La gabapentine est citée dans la même indication, car la revue l'associe à la prégabaline pour la douleur diabétique", "rmsage"),
             seul("Elle peut diminuer les performances cognitives, car la revue le signale chez la personne âgée", "rmsage"),
             seul("La dose est hors AIPS, car le seuil chiffré de la revue n'est pas un texte Swissmedic", "rmsage")],
            [seul("L'amitriptyline ou la nortriptyline servent si les précédentes échouent, car la revue les place en alternative", "rmsage"),
             seul("On les introduit avec prudence et des contrôles rapprochés, car la personne âgée tombe et se confond plus vite", "rmsage"),
             seul("La dose est hors AIPS, car la revue dit seulement de faibles doses initiales", "rmsage")],
            [seul("La cobalamine se supplémente par voie orale ou intramusculaire, car la voie injectable est préférée si le tableau est sévère", "rmsnp"),
             seul("Le but est la récupération neurologique, car elle se juge entre six semaines et trois mois", "rmsnp"),
             seul("Le schéma en milligrammes est hors AIPS ici, car l'extrait suisse ne donne pas la dose à recopier", "rmsnp")],
        ])

use("p12")
s("La prévention primaire vise le diabète lui-même, car le taux déclaré est passé de 4,8 % à 6,2 % entre les deux enquêtes", "obsandiab")
s("La prévention secondaire chez la personne diabétique est le dépistage annuel par diapason et monofilament, car l'article du sujet âgé le recommande pour éviter la plaie", "rmsage")
s("La prévention du mal perforant ajoute l'inspection des pieds et les chaussures adaptées, car le déficit sensitif est un facteur de plaie dans  la mise au point", "rmsnp")
s("La prévention alcoolique reste sous 30 grammes par jour, car la revue reprend aussi le nombre de verres de l'organisation mondiale", "rmsnp")
s("La prévention de la carence en cobalamine vise les personnes sous metformine ou sous inhibiteur de pompe, car ces traitements sont des causes de malabsorption citées", "rmsnp")
s("La prévention tertiaire limite la chute par la rééducation et l'aide à la marche, car la polyneuropathie du sujet âgé augmente ce risque", "rmsage")
s("La prévention de l'attaque cérébrale appartient à la filière vasculaire, car cette leçon retient surtout le devoir de ne pas manquer le premier épisode sensitif", "ofsavc")
s("La population cible du dépistage des pieds est la personne diabétique, car 30 à 50 % des diabétiques de type deux développent une neuropathie", "rmsnp")

use("p13")
s("Un trouble sensitif soudain et d'un seul côté ouvre la filière d'attaque cérébrale, car la létalité moyenne des attaques est de 12,2 %", "obsanavc")
s("Un niveau sensitif ou un signe pyramidal ouvre l'imagerie de la moelle, car la myélopathie symptomatique indique la chirurgie", "rmshdc")
s("Des paresthésies qui montent avec une aréflexie ouvrent l'hôpital, car onze pour cent des patients du Guillain-Barré espagnol ont été ventilés", "gbses")
s("Le diabète est la cause la plus commune de polyneuropathie, car il en explique 30 à 40 %, mais il ne dispense pas du reste du bilan", "rmsnp")
s("Aucune dose en milligrammes n'est donnée ici, car toute posologie se lit sur l'information professionnelle suisse en vigueur", "rmsage")
s("Le canal carpien est la neuropathie focale la plus fréquente, car sa prévalence clinique dans l'étude suédoise est de 3,8 %", "atroshi", "ulg")

use("p14")
s("Pourquoi une image cervicale à soixante-dix ans ne prouve-t-elle pas la myélopathie, car 85 % des gens de cet âge ont une modification souvent muette", "rmshdc")
s("La bonne réponse est que le signe clinique de moelle doit concorder avec l'image, car la revue refuse de traiter une radiographie isolée", "rmshdc")
s("Pourquoi un ralentissement du nerf médian chez un témoin ne pose-t-il pas le canal carpien, car 18,4 % des témoins suédois avaient ce ralentissement", "atroshi")
s("La bonne réponse est qu'il faut la plainte dans le territoire médian, car le tracé seul surestime la maladie", "atroshi")
s("Pourquoi peut-on manquer une carence en cobalamine si l'on attend l'anémie, car les signes neurologiques existent sans macrocytose", "rmsnp")
s("La bonne réponse est de doser la cobalamine devant l'ataxie, car la récupération dépend de la durée du manque", "rmsnp")
s("Pourquoi le délai de six à huit mois ne s'applique-t-il pas à la myélopathie, car ce délai concerne la douleur radiculaire résistante", "rmshdc")
s("La bonne réponse est que la myélopathie symptomatique indique la chirurgie par elle-même, car la revue le sépare du traitement conservateur de la racine", "rmshdc")
s("Pourquoi une dose de prégabaline lue dans une revue ne se recopie-t-elle pas, car cette leçon n'accepte le milligramme que depuis l'information professionnelle suisse", "rmsage")
s("La bonne réponse est de lire la spécialité en vigueur et d'écrire hors AIPS tant que ce texte n'est pas intégré, car la revue n'est pas l'autorisation", "rmsage")
s("Pourquoi un diabète connu ne ferme-t-il pas le bilan, car une autre cause est présente dans 53 % des neuropathies de ces patients", "rmsnp")
s("La bonne réponse est de chercher quand même la cobalamine et la gammapathie, car la revue suisse le demande même devant une cause évidente", "rmsnp")
s("Pourquoi le Guillain-Barré ne se rassure-t-il pas par sa rareté, car l'incidence moyenne espagnole n'est que de 1,67 pour 100 000", "gbses")
s("La bonne réponse est que onze pour cent ont besoin d'une ventilation, car la rareté ne baisse pas la gravité du cas présent", "gbses")
s("Ce cours, lu seul avec ses fenêtres, permet-il de reconnaître le motif, d'écarter les quatre urgences et de lancer le bilan suisse de première ligne", "rmsnp")

tableau("p14", "Question, réponse, raison",
        ["Question", "Réponse", "Raison"],
        [
            [seul("Une modification cervicale à soixante-dix ans équivaut-elle à une myélopathie, car l'image est très fréquente", "rmshdc"),
             seul("Non, car 85 % des personnes de la septième décennie portent une modification souvent asymptomatique", "rmshdc"),
             seul("Le signe de moelle doit concorder, car la chirurgie se décide sur la clinique corrélée", "rmshdc")],
            [seul("Faut-il recopier une dose de gabapentine lue dans une revue suisse, car un chiffre y figure", "rmsage"),
             seul("Non, car la dose de cette leçon reste hors AIPS tant que l'information professionnelle n'est pas intégrée", "rmsage"),
             seul("La revue n'est pas l'autorisation Swissmedic, car le milligramme ne se transpose pas d'un article à une ordonnance", "rmsage")],
            [seul("Un patient diabétique avec une chaussette a-t-il encore besoin d'un dosage de cobalamine, car la cause semble claire", "rmsnp"),
             seul("Oui, car une autre étiologie est présente dans 53 % de ces neuropathies", "rmsnp"),
             seul("La revue demande le bilan de base même devant une cause évidente, car deux mécanismes peuvent s'ajouter", "rmsnp")],
        ])
