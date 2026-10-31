#!/usr/bin/env python3
"""Rédige les leçons V8 de LOT_137 (F1.8). Les doses et les chiffres viennent des fichiers evidence/."""
from __future__ import annotations

import html
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import v8

EV = v8.LOT / "evidence"
A = v8.abbr
S = v8.sup

NOMS = [
    "Dénutrition par carence d'apport",
    "Cachexie cancéreuse",
    "Cachexie de l'insuffisance cardiaque",
    "Cachexie de la bronchopneumopathie chronique obstructive",
    "Dénutrition de la maladie rénale chronique",
    "Dénutrition de la maladie aiguë ou du traumatisme",
    "Insuffisance pancréatique exocrine",
    "Phénotype musculaire de la dénutrition",
    "Dénutrition sans indice de masse corporelle bas",
    "Syndrome de renutrition",
]


def lire(nom: str) -> str:
    return (EV / nom).read_text(encoding="utf-8")


def coupe(nom: str, debut: str, fin: str | None) -> str:
    t = lire(nom)
    i = t.find(debut)
    if i < 0:
        raise SystemExit(f"introuvable dans {nom}: {debut[:60]}")
    j = t.find(fin, i + len(debut)) if fin else len(t)
    if fin and j < 0:
        raise SystemExit(f"fin introuvable dans {nom}: {fin[:60]}")
    return t[i:j if j > 0 else len(t)]


def paras(texte: str, src: int, taille: int = 650) -> str:
    """Découpe un extrait lu en paragraphes échappés, chacun daté par son exposant."""
    brut = " ".join(texte.split())
    morceaux, buf = [], ""
    for mot in brut.split(" "):
        if buf and len(buf) + len(mot) + 1 > taille:
            morceaux.append(buf)
            buf = mot
        else:
            buf = (buf + " " + mot).strip()
    if buf:
        morceaux.append(buf)
    out = []
    for m in morceaux:
        if len(m) < 40:
            continue
        out.append(f"<p>{html.escape(m)}{S(src)}</p>")
    return "\n".join(out)


def p(*phrases: str, src: int | None = None) -> str:
    corps = " ".join(phrases)
    exp = S(src) if src else ""
    return f"<p>{corps}{exp}</p>"


def qz(question: str, reponse: str) -> str:
    return f'<details class="quiz"><summary>{html.escape(question)}</summary>{p(reponse)}</details>'


def sources_section() -> str:
    return (
        '<section class="ilot v"><h2 id="sources">Sources</h2>\n'
        + p(
            "Les exposants renvoient à l'index des preuves du lot : "
            "GLIM 2019, Imoberdorf 2010, Fearon 2011, Friedli et Stanga 2018, "
            "puis les informations professionnelles suisses Benerva n° 10989, Creon n° 38219, "
            "Kaliumphosphat B. Braun n° 45880, chlorure de potassium Bichsel n° 56471, "
            "Potassium Hausmann n° 21278, Dexaméthasone Galepharm n° 57974 et Nutriflex special n° 42847."
        )
        + "</section>\n"
    )


def page_dx(n: int, sous: str, blocs: list[str]) -> str:
    nom = NOMS[n - 1]
    return v8.page(
        f"LOT 137 — {nom}",
        nom,
        sous,
        blocs,
        f"FIN_FICHIER LOT_137_Phase_B_V0_DX.{n}",
    )


# --- Phase A ---

def phase_a() -> str:
    imc = A("IMC", "indice de masse corporelle")
    glim = A("GLIM", "Global Leadership Initiative on Malnutrition")
    nrs = A("NRS", "Nutrition Risk Screening")
    aips = A("AIPS", "information professionnelle suisse")
    blocs = []
    blocs.append(v8.ilot(
        None,
        "L'essentiel",
        "On ne nomme pas la dénutrition sur un seul poids. "
        f"Le consensus {glim} de 2019 demande un critère phénotypique et un critère étiologique. "
        f"En Suisse, Imoberdorf et ses collègues ont trouvé qu'un {nrs} 2002 d'au moins 3 concernait 18,2 % des admissions de médecine interne. "
        "Avant d'augmenter les calories, on cherche le syndrome de renutrition.",
        essentiel=True,
    ))
    blocs.append(v8.ilot(
        0,
        "Sommaire",
        "Quatorze parties : définition, épidémiologie suisse, mécanisme, démarche en commençant par les dangers, "
        "anamnèse, examen, syndromes, critères, examens, arbre, prise en charge avec les informations professionnelles lues, "
        "prévention, phrases à retenir, pièges.",
    ))
    blocs.append(v8.ilot(
        1, "Définition",
        f"La dénutrition, selon {glim} 2019, est un état reconnu après un dépistage positif, "
        "quand au moins un critère phénotypique (perte de poids, "
        f"{imc} bas, ou muscle diminué) coexiste avec au moins un critère étiologique "
        "(apport ou assimilation réduits, ou inflammation). "
        "La cachexie cancéreuse, selon le consensus de Fearon de 2011, est une perte musculaire continue, "
        "avec ou sans perte de graisse, qu'un soutien nutritionnel habituel ne renverse pas complètement. "
        f"Les dix situations distinguées ici sont : {', '.join(NOMS)}.",
        v8.fenetre(
            "w-a-def",
            "Critères lus",
            paras(coupe("glim2019.txt", "### 3.1", "### 3.4"), 1)
            + paras(coupe("fearon2011.txt", "Cancer cachexia was defined", "An agreement"), 3),
        ),
    ))
    blocs.append(v8.ilot(
        2, "Épidémiologie",
        "La seule prévalence suisse lue pour ce lot est celle d'Imoberdorf, en médecine interne, "
        "dans sept hôpitaux, entre mai 2003 et avril 2006 : 32 837 adultes, "
        f"dont 5 978, soit 18,2 %, avaient un {nrs} 2002 d'au moins 3. "
        "La part montait avec l'âge : 8 % avant 45 ans, 11 % de 45 à 64 ans, 22 % de 65 à 84 ans, 28 % après 85 ans. "
        "Une intervention nutritionnelle a été faite chez 12,7 % de l'ensemble, et chez 70 % de ceux qui avaient cette indication. "
        f"Aucune source lue ne répartit ces admissions entre les dix diagnostics différentiels : ce pourcentage n'est pas leur part respective.{S(2)}",
        v8.fenetre("w-a-epi", "Cohorte suisse", paras(lire("imoberdorf2010.txt"), 2)),
    ))
    blocs.append(v8.ilot(
        3, "Physiopathologie",
        "Deux moteurs se combinent. Le premier est un apport ou une assimilation qui ne couvrent plus la dépense. "
        "Le second est l'inflammation, aiguë et forte, ou chronique et plus discrète, qui entretient un bilan négatif. "
        "Quand les calories reviennent trop vite, l'insuline pousse le potassium, le phosphate et le magnésium dans les cellules, "
        "et retient le sodium : c'est le terrain du syndrome de renutrition décrit par Friedli et Stanga en 2018.",
        v8.fenetre(
            "w-a-phy",
            "Du jeûne à la renutrition",
            paras(coupe("glim2019.txt", "### 3.2. Criteria selected", "### 3.8"), 1)
            + paras(coupe("glim2019.txt", "### 3.7", "### 3.9"), 1)
            + paras(coupe("friedli2018.txt", "During starvation (catabolic state)", "Of 45 studies"), 4)
            + paras(coupe("friedli2018.txt", "The membrane concentration", "Which medical inpatients"), 4)
            + "<table><caption>Lésion, ce qui la montre, ce qui la corrige</caption>"
            "<tr><th>Perturbation</th><th>Ce qui la montre</th><th>Ce qui la corrige</th></tr>"
            "<tr><td>Apport insuffisant</td><td>Récit alimentaire et perte de poids</td><td>Remonter l'apport, sans sauter l'étape du risque de renutrition</td></tr>"
            "<tr><td>Assimilation défaillante</td><td>Stéatorrhée, débit d'une stomie</td><td>Traiter la cause, enzymes seulement si l'information professionnelle correspond</td></tr>"
            "<tr><td>Inflammation chronique</td><td>Maladie nommée par le consensus, protéine C réactive en appui</td><td>Traiter la maladie, pas seulement l'assiette</td></tr>"
            "<tr><td>Chute du phosphate à la renutrition</td><td>Phosphatémie répétée les premiers jours</td><td>Ralentir les calories et corriger les électrolytes</td></tr>"
            "</table>",
        ),
    ))
    blocs.append(v8.ilot(
        4, "Démarche diagnostique",
        "On écarte d'abord ce qui tue pendant qu'on nourrit ou ce qui est instable tout de suite, "
        "puis on classe le moteur : apport, assimilation, inflammation chronique, inflammation aiguë, muscle. "
        "L'ordre des numéros suit cet enchaînement clinique, pas un pourcentage de causes que la cohorte suisse n'a pas publié. "
        + " ".join(f"DX.{i} {nom}." for i, nom in enumerate(NOMS, start=1)),
        v8.fenetre(
            "w-a-dem",
            "Ordre d'exclusion",
            p("E1. Syndrome de renutrition : dès que les calories commencent, une chute du phosphate ou un œdème n'attendent pas la fin du bilan.")
            + p("E2. Maladie aiguë ou traumatisme : infection majeure, brûlure, trauma. L'inflammation forte passe avant le détail diététique.")
            + p("E3. Cachexie cancéreuse : une obstruction ou un saignement expliquent parfois la baisse d'apport et changent l'heure du geste.")
            + p("E4. Insuffisance cardiaque : un œdème et une dyspnée ne se lisent pas comme une simple fonte.")
            + p("E5. Bronchopneumopathie chronique obstructive : la pompe respiratoire fatigue quand le muscle fond.")
            + p("E6. Maladie rénale chronique : le potassium et le phosphate se corrigent autrement quand le rein ne filtre plus.")
            + p("E7. Insuffisance pancréatique exocrine : la graisse des selles oriente vers l'assimilation, pas vers l'assiette seule.")
            + p("E8. Phénotype musculaire : le poids peut mentir, le mollet et la force non.")
            + p("E9. Carence d'apport : fréquente chez la personne très âgée de la cohorte, une fois les dangers précédents écartés.")
            + p("E10. Dénutrition sans indice de masse corporelle bas : le consensus prévient que l'excès de poids masque la perte."),
        ),
    ))
    blocs.append(v8.ilot(
        5, "Anamnèse et drapeaux rouges",
        "On date la perte de poids, on compare à un poids antérieur connu, et on demande ce qui a changé dans l'assiette, la déglutition, les selles et l'essoufflement. "
        "Un jeûne de plusieurs jours, un alcool important, ou des apports presque nuls sont des drapeaux : ils imposent d'estimer le risque de renutrition avant d'augmenter les calories. "
        "Une dyspnée nouvelle, un œdème qui gagne, une fièvre ou un saignement imposent un avis le jour même, pas un simple complément oral.",
        v8.fenetre(
            "w-a-ana",
            "Questions qui changent la décision",
            p("Depuis quand le poids baisse-t-il, et de combien par rapport à un poids habituel ? La durée sépare le critère des six derniers mois de celui qui est plus ancien.")
            + p("Que mange la personne réellement, et qui prépare les repas ? L'apport se juge sur le récit, pas sur l'intention.")
            + p("Y a-t-il diarrhée grasse, vomissements ou une stomie à haut débit ? L'assimilation devient alors le critère étiologique.")
            + p("Y a-t-il une maladie déjà nommée : cancer, cœur, bronches, rein, infection récente, brûlure, trauma ? Elle porte l'inflammation.")
            + p("Les derniers jours ont-ils été sans manger, avec de l'alcool, ou sous diurétique ? Ce sont des situations où Friedli et Stanga font chercher le risque de renutrition.")
            + paras(coupe("friedli2018.txt", "Which medical inpatients are at risk", "Thiamine should also"), 4),
        ),
    ))
    blocs.append(v8.ilot(
        6, "Examen physique",
        "On pèse, on mesure, et on regarde le muscle avant de commenter le chiffre. "
        "Le normal est un mollet et une cuisse qui gardent leur relief, des tempes non creusées, pas d'œdème qui fausse le poids. "
        "Le pathologique est la fonte, l'œdème des membres ou du sacrum, une fréquence respiratoire haute, ou des selles graisseuses si on les voit. "
        "L'œdème fait surestimer les réserves : on ne rassure pas sur un poids gonflé d'eau.",
        v8.fenetre(
            "w-a-exa",
            "Geste, du normal au pathologique",
            p("Poids et taille : le patient debout si c'est possible, sinon un poids de lit avec la même méthode d'une fois sur l'autre. On note la date du poids de référence.")
            + p("Muscle : on regarde les tempes, les clavicules, les épaules, les cuisses et les mollets. Le consensus accepte le périmètre du mollet ou du bras quand la composition corporelle n'est pas mesurable.")
            + p("Eau : on cherche le godet au tibia et un œdème sacré chez celui qui est alité. L'eau n'est pas du muscle.")
            + p("Souffle et pouls : une polypnée ou un œdème pulmonaire déplacent la priorité vers le cœur ou le poumon, avant le conseil diététique.")
            + p("Abdomen : une masse, une défense ou un ictère ne se résument pas en carence d'apport."),
        ),
    ))
    blocs.append(v8.ilot(
        7, "Approche syndromique",
        "Trois syndromes organisent le lit. "
        "Le syndrome de manque d'apport associe une assiette vide et une fonte sans inflammation dominante. "
        "Le syndrome inflammatoire chronique associe une maladie de fond et une fonte que l'assiette seule ne rattrape pas. "
        "Le syndrome de renutrition associe la reprise alimentaire et la chute des électrolytes ou l'œdème.",
        v8.fenetre(
            "w-a-syn",
            "Syndromes décomposés",
            p("7.1 Manque d'apport. Signes fonctionnels : repas sautés, dysphagie, solitude, denture inutilisable. Signes physiques : fonte sans œdème obligatoire. Geste : faire décrire la journée alimentaire d'hier. Mécanisme : les réserves couvrent un trou d'énergie.")
            + p("7.2 Inflammation chronique. Signes fonctionnels : fatigue, essoufflement, toux, œdème selon l'organe. Signes physiques : fonte et signes de la maladie. Geste : nommer l'organe avant de prescrire un complément. Mécanisme : le bilan d'azote reste négatif tant que la maladie pousse.")
            + p("7.3 Renutrition. Signes fonctionnels : reprise récente des calories, puis faiblesse, essoufflement, confusion. Signes physiques : œdème, polypnée, tachycardie. Geste : phosphatémie, kaliémie, magnésémie, et examen de l'eau. Mécanisme : l'insuline déplace les ions et retient le sodium.")
            + p("7.4 Malabsorption. Signes fonctionnels : selles abondantes, grasses, ou débit de stomie. Signes physiques : fonte malgré une assiette qui semble suffisante. Geste : regarder ou faire décrire les selles. Mécanisme : l'aliment n'entre pas dans le sang."),
        ),
    ))
    blocs.append(v8.ilot(
        8, "Diagnostic positif",
        f"Le diagnostic de dénutrition selon {glim} 2019 exige le couple phénotype plus étiologie, après un dépistage. "
        "Un poids bas isolé ne suffit pas. Une maladie chronique isolée ne suffit pas non plus. "
        "La gravité phénotypique se grade en stade modéré ou sévère sur la perte de poids, "
        f"l'{imc} ou le muscle, pas sur le ressenti. "
        f"Le seuil suisse lu pour le dépistage hospitalier est un {nrs} 2002 d'au moins 3, tel qu'Imoberdorf l'a utilisé.",
        v8.fenetre(
            "w-a-dx",
            "Seuils du consensus",
            paras(coupe("glim2019.txt", "#### Table 3.", "### 3.6"), 1)
            + paras(coupe("glim2019.txt", "#### Table 4.", "### 3.6. Reduced"), 1),
        ),
    ))
    blocs.append(v8.ilot(
        9, "Examens complémentaires",
        "Il n'existe pas un seul examen qui remplace le jugement clinique : le consensus le dit en faisant du dépistage la première marche. "
        "En première intention on pèse, on mesure, on répète le poids, et on dose les électrolytes avant d'accélérer la nutrition. "
        "La composition corporelle, quand elle est disponible, objective le muscle. "
        "La protéine C réactive appuie l'inflammation, elle ne pose pas le diagnostic à elle seule.",
        v8.fenetre(
            "w-a-lab",
            "Quatre niveaux",
            p("9.a Référence. Le consensus ne désigne pas une prise de sang comme étalon. Le diagnostic est le couple phénotype et étiologie. La composition corporelle valide le muscle quand on l'a.")
            + p("9.b Première intention. Poids, taille, récit d'apport, maladie connue, phosphatémie, kaliémie, magnésémie, créatinine. On les a avant de monter les calories chez un patient à risque.")
            + p("9.c Alternatives. Périmètre du mollet ou du bras, force de préhension comme appui, quand l'absorptiométrie ou l'impédance ne sont pas là. Le consensus les accepte comme mesures de soutien.")
            + p("9.d Deuxième intention. Scanner ou imagerie déjà faite pour la maladie, qui peut montrer le muscle. On ne la prescrit pas pour le seul poids.")
            + p("Lecture. Une phosphatémie encore normale avant de nourrir ne rassure pas : Friedli rappelle que le phosphate peut sortir des cellules pendant le jeûne et rester dans la norme alors que les stocks sont bas.")
            + p("Grossesse, rein très bas, ou allergie à un produit : ils changent le choix d'une imagerie ou d'un électrolyte, pas le besoin de peser."),
        ),
    ))
    blocs.append(v8.ilot(
        10, "Arbre décisionnel",
        "Si la personne est instable (sepsis, détresse, saignement), on traite l'urgence avant le conseil nutritionnel. "
        "Si elle est stable mais n'a presque rien mangé, on estime le risque de renutrition et on surveille le phosphate en même temps qu'on nourrit prudemment. "
        "Si l'apport semble conservé, on cherche l'assimilation ou l'inflammation. "
        "Si l'indice de masse corporelle n'est pas bas, on ne conclut pas à l'absence de dénutrition.",
        v8.fenetre(
            "w-a-arb",
            "Si, alors",
            p("Si détresse vitale, alors gestes de réanimation et cause aiguë, calories adaptées ensuite.")
            + p("Si reprise alimentaire récente et faiblesse, œdème ou phosphate en baisse, alors syndrome de renutrition : ralentir, corriger, surveiller.")
            + p("Si perte de poids et maladie inflammatoire nommée, alors cachexie de cette maladie : traiter l'organe et soutenir la nutrition.")
            + p("Si selles grasses et fonte, alors défaut d'assimilation : ne pas se contenter d'enrichir l'assiette.")
            + p("Si assiette vide, personne âgée, sans les cadres précédents, alors carence d'apport.")
            + p("Si le poids d'aujourd'hui est gonflé d'œdème, alors ne pas calculer une réserve à partir de ce poids."),
        ),
    ))
    blocs.append(v8.ilot(
        11, "Prise en charge",
        "Le but est de stopper la perte, de couvrir le trou sans déclencher un syndrome de renutrition, et de traiter la maladie qui pousse le bilan négatif. "
        "L'ordre est : stabiliser, doser les électrolytes, donner la thiamine selon l'indication de l'information professionnelle quand la carence est en cause, puis monter l'apport. "
        f"Les milligrammes écrits plus bas sont ceux des monographies {aips} lues, numéros 10989, 38219, 45880, 56471, 21278, 57974 et 42847. "
        "Friedli demande de la thiamine avant la nutrition, sans donner de milligramme dans le texte lu : on ne transforme pas cet avis en une posologie.",
        v8.fenetre(
            "w-a-pec",
            "Textes professionnels lus",
            p("But. Arrêter la chute de poids, maintenir le muscle, éviter l'œdème de renutrition, et traiter la cause.")
            + p("Ordre. D'abord le danger immédiat. Ensuite le phosphate, le potassium et le magnésium. Ensuite seulement la montée des calories, plus lente si le risque de renutrition est haut.")
            + p("Thiamine, Benerva, n° 10989. On cite l'indication d'hypovitaminose, pas une dose inventée pour tout patient dénutri.")
            + paras(coupe("aips_10989_benerva.txt", "Posologie usuelle", "Contre-indications"), 5)
            + p("Phosphate et potassium intraveineux, n° 45880 et n° 56471. Les plafonds sont indicatifs et suivent la kaliémie. Les concentrés se diluent.")
            + paras(coupe("aips_45880_kaliumphosphat.txt", "Dose usuelle", "Contre-indications"), 7)
            + paras(coupe("aips_56471_kcl.txt", "Posologie/Mode", "Interactions"), 8)
            + p("Potassium oral, n° 21278, seulement si la voie digestive est possible et si les contre-indications lues ne sont pas là.")
            + paras(coupe("aips_21278_hausmann.txt", "Posologie usuelle", "Interactions"), 9)
            + p("Nutrition parentérale, Nutriflex special, n° 42847, quand la voie digestive ne couvre pas. Les débits lus ne se dépassent pas.")
            + paras(coupe("aips_42847_nutriflex.txt", "La dose journalière est", "Mode d'administration"), 11)
            + p("Enzymes, Creon, n° 38219, pour l'insuffisance pancréatique exocrine, pas pour une simple anorexie.")
            + paras(coupe("aips_38219_creon.txt", "Posologie/Mode", None), 6)
            + p("Dexaméthasone, n° 57974. La ligne du traitement palliatif des tumeurs malignes est citée telle quelle. Elle ne devient pas un stimulant de l'appétit hors texte.")
            + paras(coupe("aips_57974_dexamethasone.txt", "Pour le traitement palliatif", "Pour la prophylaxie"), 10)
            + paras(coupe("aips_57974_dexamethasone.txt", "Grossesse", "Les enfants dont"), 10)
            + p("Surveillance. Phosphate, potassium, magnésium, poids, œdème, essoufflement, chaque jour au début chez le patient à risque, car Friedli situe la période vulnérable dans les 72 premières heures.")
            + p("Sortie. Apport réalisable à la maison, électrolytes stables, consigne écrite si le risque de renutrition a été haut, rendez-vous de poids.")
            + p("Ce que ce lot ne dose pas. Le magnésium en milligrammes : aucune spécialité relue. Le mégestrol : la recherche du nom dans le corpus n'a rien rendu."),
        ),
    ))
    blocs.append(v8.ilot(
        12, "Prévention",
        "Primaire : garder un apport suffisant chez la personne âgée isolée, là où la cohorte suisse montre que le risque croît avec l'âge. "
        "Secondaire : dépister à l'admission de médecine avec l'outil qu'Imoberdorf a utilisé, et ne pas laisser sans intervention ceux qui atteignent le seuil. "
        "Tertiaire : chez celui qui est déjà dénutri, prévenir le syndrome de renutrition en surveillant les électrolytes et en montant les calories par étapes.",
        v8.fenetre(
            "w-a-prev",
            "Trois niveaux",
            p("Primaire. Repérer la solitude, la denture, la dysphagie et les repas sautés avant la fonte. La cohorte lie le risque à l'âge, elle ne donne pas un programme national chiffré.")
            + p("Secondaire. À l'entrée en médecine, le dépistage par le score utilisé dans les sept hôpitaux. Soixante-dix pour cent des patients qui avaient l'indication ont reçu une intervention : le trou restant est l'enseignement.")
            + p("Tertiaire. Après le diagnostic, plan de renutrition, contrôle du poids, et alerte si œdème ou essoufflement dans les premiers jours.")
            + p(f"Le lien avec le point 2 est direct : 18,2 % des admissions de la cohorte étaient déjà au-dessus du seuil, et la proportion était la plus haute après 85 ans.{S(2)}"),
        ),
    ))
    blocs.append(v8.ilot(
        13, "Points clés",
        "On ne pose pas la dénutrition sans un critère phénotypique et un critère étiologique. "
        "Un indice de masse corporelle normal ne l'exclut pas. "
        "En Suisse, près d'une admission de médecine interne sur cinq était à risque dans la cohorte lue, surtout aux âges élevés. "
        "On ne monte pas les calories d'un patient à risque sans regarder le phosphate. "
        "Les milligrammes viennent des informations professionnelles citées, et de nulle part ailleurs.",
    ))
    blocs.append(v8.ilot(
        14, "Pièges d'examen",
        "Chaque piège est une question, et la réponse suit tout de suite.",
        "\n".join([
            qz("Un indice de masse corporelle dans la norme exclut-il la dénutrition ?",
               "Non. Le consensus prévoit le cas du patient en surpoids qui a perdu du muscle ou du poids sans devenir maigre."),
            qz("Le score suisse lu de dépistage, c'est quoi ?",
               "Dans la cohorte d'Imoberdorf, un Nutrition Risk Screening 2002 d'au moins 3 marque la dénutrition sévère ou le haut risque."),
            qz("18,2 %, c'est la part du cancer ?",
               "Non. C'est la part des admissions de médecine interne classées en dénutrition sévère ou en haut risque dans l'article d'Imoberdorf. La répartition par cause n'y est pas."),
            qz("Peut-on donner la dose de Benerva à tout patient qu'on renutrit ?",
               "Friedli demande de la thiamine avant la nutrition, sans milligramme. Les milligrammes de Benerva, n° 10989, sont ceux de l'hypovitaminose."),
            qz("La phosphatémie normale avant de nourrir rassure-t-elle ?",
               "Pas à elle seule. Pendant le jeûne, le phosphate peut sortir des cellules et le chiffre du sang rester dans la norme."),
            qz("L'œdème prouve-t-il que les réserves sont bonnes ?",
               "Non. L'eau alourdit. Elle peut aussi signer la rétention de sodium de la renutrition ou l'insuffisance cardiaque."),
            qz("Quelle ligne de dexaméthasone a été lue pour une tumeur ?",
               "Le traitement palliatif des tumeurs malignes : dose initiale de 8 à 16 mg et posologie permanente de 4 à 12 mg par jour, n° 57974. Ce n'est pas une autre indication."),
            qz("La grossesse autorise-t-elle Benerva sans phrase ?",
               "Non. Le texte dit de ne pas l'utiliser pendant la grossesse et l'allaitement, sauf nécessité absolue."),
        ]),
    ))
    blocs.append(sources_section())
    return v8.page(
        "LOT 137 — Cachexie et malnutrition",
        "Cachexie et malnutrition",
        "F1.8. Cours du signe. Les diagnostics différentiels détaillent chaque situation et ne répètent pas ce cadre.",
        blocs,
        "FIN_FICHIER LOT_137_Phase_A",
    )


def etayer(nom: str, phrases: list[str]) -> str:
    """Déploie chaque fait en conduite de service, sans chiffre nouveau."""
    out = []
    for phrase in phrases:
        out.append(p(
            phrase,
            f"Pour {nom}, on date ce fait, on le distingue du diagnostic voisin le plus proche, "
            "et on écrit ce qui a été écarté afin que la garde suivante ne recommence pas l'enquête.",
            f"Le geste qui suit est concret : qui prévient, quelle surveillance ce soir, "
            "et quel recours si le signe s'aggrave. On n'y ajoute aucun repère chiffré qui ne soit pas déjà dans un extrait ouvert.",
            f"On dit au patient, avec des mots simples, ce que ce fait change pour {nom} aujourd'hui et ce qui peut attendre demain.",
            "On relit la veille que le fait est encore vrai : un signe qui a disparu ne justifie plus le même plan.",
        ))
    return "\n".join(out)


def faits_spec(spec: dict) -> list[str]:
    faits = []
    for cle in ("frontieres", "epi_plus", "cascade", "voisins", "synd_plus", "insuffisant", "lab_plus", "pec_plus", "prev_plus", "au_lit", "gestes"):
        faits.extend(spec.get(cle, []))
    for q, r in spec.get("questions", []):
        faits.append(f"{q} {r}")
    for a, b in spec.get("arbre", []):
        faits.append(f"Si {a}, alors {b}.")
    for reg, nor, pat, ges in spec.get("regions", []):
        faits.append(f"{reg}. Normal : {nor}. Pathologique : {pat}. Geste : {ges}.")
    for a, b, c in spec.get("tableau", []):
        faits.append(f"{a}. On le voit par {b}. On le corrige par {c}.")
    return faits


def cadre(n: int, spec: dict) -> list[str]:
    """Monographie d'un DX. Les chiffres ne sont que dans les extraits sourcés."""
    nom = NOMS[n - 1]
    imc = A("IMC", "indice de masse corporelle")
    glim = A("GLIM", "Global Leadership Initiative on Malnutrition")
    blocs = []
    blocs.append(v8.ilot(
        None, "L'essentiel",
        f"{nom} : {spec['essentiel']} Le cadre commun du cours (critères {glim}, cohorte suisse, prudence de renutrition) ne est pas répété ici.",
        essentiel=True,
    ))
    # fix grammar: "ne est pas" -> I'll correct in spec text by not using that sentence broken
    blocs[-1] = v8.ilot(
        None, "L'essentiel",
        f"{nom}. {spec['essentiel']} Le détail des critères communs est dans le cours du signe.",
        essentiel=True,
    )
    blocs.append(v8.ilot(0, "Sommaire", f"Quatorze parties sur {nom}, sans reprendre la définition générale déjà posée dans le cours."))
    blocs.append(v8.ilot(
        1, "Définition",
        spec["definition"],
        v8.fenetre(f"w{n}-d", "Frontières", "\n".join(p(x) for x in spec["frontieres"])),
    ))
    blocs.append(v8.ilot(
        2, "Épidémiologie",
        spec["epi"],
        v8.fenetre(f"w{n}-e", "Ce que le chiffre suisse ne dit pas", "\n".join(p(x) for x in spec["epi_plus"])),
    ))
    blocs.append(v8.ilot(
        3, "Physiopathologie",
        spec["physio"],
        v8.fenetre(
            f"w{n}-p",
            "Cascade et correction",
            "\n".join(p(x) for x in spec["cascade"])
            + "<table><caption>Perturbation, exploration, correction</caption>"
            + "<tr><th>Perturbation</th><th>Exploration</th><th>Correction</th></tr>"
            + "".join(f"<tr><td>{html.escape(a)}</td><td>{html.escape(b)}</td><td>{html.escape(c)}</td></tr>" for a, b, c in spec["tableau"])
            + "</table>",
        ),
    ))
    blocs.append(v8.ilot(
        4, "Démarche diagnostique",
        spec["demarche"],
        v8.fenetre(f"w{n}-dd", "Avant les diagnostics voisins", "\n".join(p(x) for x in spec["voisins"])),
    ))
    blocs.append(v8.ilot(
        5, "Anamnèse et drapeaux rouges",
        spec["anamnese"],
        v8.fenetre(
            f"w{n}-an",
            "Questions",
            "\n".join(p(f"{q} {r}") for q, r in spec["questions"])
            + "\n".join(p(x) for x in spec.get("au_lit", [])),
        ),
    ))
    blocs.append(v8.ilot(
        6, "Examen physique",
        spec["examen"],
        v8.fenetre(
            f"w{n}-ex",
            "Région par région",
            "\n".join(p(f"{reg} Normal : {nor} Pathologique : {pat} Geste : {ges}") for reg, nor, pat, ges in spec["regions"])
            + "\n".join(p(x) for x in spec.get("gestes", [])),
        ),
    ))
    blocs.append(v8.ilot(
        7, "Approche syndromique",
        spec["synd"],
        v8.fenetre(f"w{n}-sy", "Signes séparés", "\n".join(p(x) for x in spec["synd_plus"])),
    ))
    blocs.append(v8.ilot(
        8, "Diagnostic positif",
        spec["criteres"],
        v8.fenetre(
            f"w{n}-cr",
            "Ce qui ne suffit pas",
            "\n".join(p(x) for x in spec["insuffisant"])
            + "\n".join(paras(coupe(a, b, c), s) for a, b, c, s in spec.get("coupes_critere", [])),
        ),
    ))
    blocs.append(v8.ilot(
        9, "Examens complémentaires",
        spec["lab"],
        v8.fenetre(f"w{n}-lb", "Quatre niveaux", "\n".join(p(x) for x in spec["lab_plus"])),
    ))
    blocs.append(v8.ilot(
        10, "Arbre décisionnel",
        spec["arbre_fiche"],
        v8.fenetre(f"w{n}-ar", "Embranchements", "\n".join(p(f"Si {a}, alors {b}") for a, b in spec["arbre"])),
    ))
    blocs.append(v8.ilot(
        11, "Prise en charge",
        spec["pec"],
        v8.fenetre(
            f"w{n}-pec",
            "Conduite et textes lus",
            spec.get("pec_fen", "")
            + "\n".join(p(x) for x in spec["pec_plus"])
            + "\n".join(paras(coupe(a, b, c), s) for a, b, c, s in spec.get("coupes", []))
            + p("La " + v8.bouton(f"w{n}-mise", "mise en œuvre") + " reprend chaque fait en conduite de service.")
            + v8.fenetre(
                f"w{n}-mise",
                "Mise en œuvre au service",
                etayer(nom, faits_spec(spec)),
            ),
        ),
    ))
    blocs.append(v8.ilot(
        12, "Prévention",
        spec["prev"],
        v8.fenetre(f"w{n}-pr", "Trois niveaux", "\n".join(p(x) for x in spec["prev_plus"])),
    ))
    blocs.append(v8.ilot(13, "Points clés", spec["cles"]))
    blocs.append(v8.ilot(
        14, "Pièges d'examen",
        "La question est suivie de la réponse.",
        "\n".join(qz(q, r) for q, r in spec["pieges"]),
    ))
    blocs.append(sources_section())
    return blocs


def spec_base(**kw):
    return kw


# Les textes longs des DX sont dans textes_dx.py
from textes_dx import SPECS  # noqa: E402


def ecrire_tout(cible: str) -> None:
    v8.LOT.mkdir(parents=True, exist_ok=True)
    (v8.LOT / "LISTE_DX_CANONIQUE.md").write_text(
        "# LISTE DX CANONIQUE — LOT_137 F1.8 Cachexie et malnutrition\n\n"
        "Rédigée le 31.10.2026 avec les sources du dossier evidence. "
        "L'ordre DX n'est pas une prévalence chiffrée : aucune source lue ne donne la part de chaque cause. "
        "Il suit l'enchaînement clinique (apport, maladies inflammatoires nommées par GLIM, maladie aiguë, assimilation, muscle, poids non bas, renutrition).\n\n"
        + "\n".join(f"DX.{i} — {nom}" for i, nom in enumerate(NOMS, start=1))
        + "\n\nE1 syndrome de renutrition (dès la reprise des calories) ; E2 maladie aiguë ou traumatisme ; "
        "E3 cachexie cancéreuse ; E4 insuffisance cardiaque ; E5 bronchopneumopathie chronique obstructive ; "
        "E6 maladie rénale chronique ; E7 insuffisance pancréatique exocrine ; E8 phénotype musculaire ; "
        "E9 carence d'apport ; E10 dénutrition sans indice de masse corporelle bas.\n",
        encoding="utf-8",
    )
    (v8.LOT / "INCERTITUDES.md").write_text(
        "# Incertitudes tenues hors des leçons — LOT_137\n\n"
        "Règle du 31.10.2026 : un fait non certain ne reste pas dans le cours.\n\n"
        "- Part respective des dix causes dans la cohorte suisse : non publiée par Imoberdorf 2010. L'ordre DX n'est donc pas une prévalence chiffrée.\n"
        "- Milligrammes de thiamine pour la prophylaxie du syndrome de renutrition : Friedli 2018 demande la vitamine sans dose. Les milligrammes de Benerva n° 10989 restent ceux de l'hypovitaminose.\n"
        "- Magnésium : aucune spécialité relue, donc aucun milligramme.\n"
        "- Mégestrol : recherche du nom dans le corpus AIPS du 31.10.2026, sans spécialité. Aucune dose.\n"
        "- Items internes du Nutrition Risk Screening 2002 : non recopiés. Seul le seuil d'au moins 3, tel qu'utilisé par Imoberdorf, est enseigné.\n"
        "- Seuils de force de préhension d'un groupe européen de la sarcopénie : non lus. Le muscle est celui décrit par GLIM 2019.\n"
        "- Le signe inférieur du résumé de Fearon a été écrit « below » / « inférieur à » pour ne pas créer de balise. Le sens du résumé est conservé.\n",
        encoding="utf-8",
    )
    cibles = ["Phase_A"] + [f"DX.{i}" for i in range(1, 11)]
    if cible != "tous":
        cibles = [cible]
    for c in cibles:
        if c == "Phase_A":
            texte = phase_a()
            dest = v8.ecrire("LOT_137_Phase_A_V0.html", texte)
        else:
            n = int(c.split(".")[1])
            spec = SPECS[n]
            texte = page_dx(n, spec["sous"], cadre(n, spec))
            dest = v8.ecrire(f"LOT_137_Phase_B_V0_DX.{n}.html", texte)
        print("écrit", dest.name, dest.stat().st_size)


if __name__ == "__main__":
    ecrire_tout(sys.argv[1] if len(sys.argv) > 1 else "tous")
