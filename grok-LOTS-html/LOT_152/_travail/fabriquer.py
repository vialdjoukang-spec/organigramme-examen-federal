#!/usr/bin/env python3
"""Leçons V8 du LOT_152. python3 fabriquer.py [A|1|2|…|10|tout]"""
from __future__ import annotations

import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from lib_html import A, EV, P, S, b, cite, fen, ilot, page, table

OUT = Path(__file__).resolve().parents[1]
DOSE = re.compile(
    r"\b\d+(?:[.,]\d+)?\s*(?:µg|μg|mcg|mg|UI|IU|ml/h|mL/h)\b",
    re.I,
)
DOSE_G = re.compile(r"\b\d+(?:[.,]\d+)?\s*g\b(?!\s*/\s*(?:dl|dL|l)\b)", re.I)
WSES = A("WSES", "World Society of Emergency Surgery")

DX = {
    1: "Pneumonie acquise en communauté",
    2: "Œdème pulmonaire cardiogénique",
    3: "Épanchement pleural",
    4: "Pneumothorax spontané",
    5: "Suspicion de dissection aortique",
    6: "Occlusion du grêle sur adhérences",
    7: "Perforation d'ulcère peptique",
    8: "Fracture de l'extrémité distale du radius",
    9: "Fracture du scaphoïde",
    10: "Luxation rétrolunaire du carpe",
}


def paragraphes(fn: str, mots: tuple[str, ...] = (), limite: int = 24, aips: bool = False) -> list[str]:
    brut = re.sub(r"\s+", " ", (EV / fn).read_text(encoding="utf-8"))
    blocs = re.split(r"(?<=[.!?])\s+(?=[A-ZÀÂÉÈÊÎÔÙÇa-z])", brut)
    pris = []
    for bloc in blocs:
        t = " ".join(bloc.split())
        if len(t) < 140 or len(t) > 1500:
            continue
        if "@" in t or "http" in t or "doi.org" in t or "Comité" in t:
            continue
        if re.search(r"À\s+vérifier|TODO|FIXME|\(\?\)", t, re.I):
            continue
        if not aips and (DOSE.search(t) or DOSE_G.search(t)):
            continue
        if mots and not any(m.lower() in t.lower() for m in mots):
            continue
        t = t.replace("«", " ").replace("»", " ").replace("<", " inférieur à ").replace(">", " supérieur à ")
        pris.append(" ".join(t.split()))
        if len(pris) >= limite:
            break
    return pris


def fen_source(pid: str, titre: str, fn: str, sup: int, mots: tuple[str, ...] = (), limite: int = 22, aips: bool = False) -> str:
    paras = paragraphes(fn, mots, limite, aips=aips)
    if not paras:
        return ""
    inner = [P(
        f"Extraits lus le 31 octobre 2026 dans {fn.replace('_', ' ').replace('.txt', '')}. "
        "Chaque phrase est dans le dossier de preuves. Elle éclaire ce diagnostic. Elle n'est pas une conduite copiée hors de son indication."
        + S(sup)
    )]
    for i, t in enumerate(paras, 1):
        inner.append(P(f"Lecture {i}. {t}" + S(sup)))
    return fen(pid, titre, "\n".join(inner))


def sources(*specs: tuple) -> str:
    """specs: (pid, titre, fn, sup, mots, limite, aips)"""
    return "\n".join(fen_source(*s) for s in specs)


def elargi(n: int, pairs: list[tuple[str, int, int]]) -> str:
    specs = []
    for i, (fn, sup, lim) in enumerate(pairs):
        specs.append((f"w{n}-el{i}", f"Contexte lu {i + 1}", fn, sup, (), lim, False))
    return sources(*specs)


C_CO = cite(
    "aips_55185.txt",
    "Dans des cas particuliers (sinusites aiguës, pneumonies ambulatoire, exacerbations aiguës d'une bronchite chronique",
    "3x 625 mg (500/125) par jour.",
)
C_CO_REC = cite(
    "aips_55185.txt",
    "Co-Amoxicilline Sandoz doit être utilisé conformément aux recommandations locales officielles sur l'utilisation d'antibiotiques",
    "données locales de sensibilité.",
)
C_CO_G = cite(
    "aips_55185.txt",
    "Co-Amoxicilline Sandoz ne devrait donc être utilisé pendant la grossesse qu'en cas de nécessité absolue.",
)
C_CO_A = cite(
    "aips_55185.txt",
    "Il ne faudrait donc pas allaiter pendant le traitement par Co-Amoxicilline Sandoz.",
)
C_LA = cite(
    "aips_30630.txt",
    "Oedème pulmonaire aigu : injecter comme dose initiale 40 mg (2 x 20 mg) de Lasix en i.v.",
    "20 à 40 mg de Lasix.",
)
C_LA_IND = cite(
    "aips_30630.txt",
    "Insuffisance cardiaque aiguë, en particulier œdème pulmonaire (l'administration sera associée à d'autres mesures thérapeutiques).",
)
C_LA_AD = cite(
    "aips_30630.txt",
    "Sauf prescription contraire, administrer aux adultes et aux adolescents à partir de 15 ans une dose initiale de 20 à 40 mg de Lasix en i.v. ou i.m.",
)
C_LA_G = cite(
    "aips_30630.txt",
    "Pour cette raison Lasix ne devrait pas être employé pendant la grossesse, sauf en cas de nécessité absolue.",
)
C_LA_A = cite(
    "aips_30630.txt",
    "L'utilisation de Lasix est donc déconseillée pendant l'allaitement.",
)
C_PA = cite(
    "aips_47503.txt",
    "Il ne faut pas dépasser la dose journalière maximale de 4000 mg de paracétamol.",
)
C_PA_DOSE = cite(
    "aips_47503.txt",
    "500 à 1'000 mg soit 1 à 2 comprimé(s) par prise",
    "4 à 8 h (adultes)",
)
C_PA_CI = cite(
    "aips_47503.txt",
    "Le paracétamol est contre-indiqué en cas de maladie hépatique active décompensée, notamment d'hépatite due à l'abus d'alcool",
)
C_PA_IND = cite(
    "aips_47503.txt",
    "Traitement contre les douleurs d'intensité faible à modérée",
    "douleurs après blessures",
)


def som() -> str:
    liens = "\n".join(
        f'<li><a href="#{i}">{t}</a></li>'
        for i, t in (
            ("p1", "Définition"),
            ("p2", "Épidémiologie"),
            ("p3", "Physiopathologie"),
            ("p4", "Démarche diagnostique"),
            ("p5", "Anamnèse"),
            ("p6", "Examen physique"),
            ("p7", "Approche syndromique"),
            ("p8", "Diagnostic positif"),
            ("p9", "Examens complémentaires"),
            ("p10", "Arbre décisionnel"),
            ("p11", "Prise en charge en Suisse"),
            ("p12", "Prévention"),
            ("p13", "Points clés"),
            ("p14", "Pièges d'examen"),
        )
    )
    return ilot("som", "v", "Sommaire", f'<nav><ol class="som">\n{liens}\n</ol></nav>\n<p class="sous">Le détail est dans les fenêtres.</p>')


def sources_ol() -> str:
    items = [
        "Revue Médicale Suisse 2019, lecture systématique du thorax.",
        "Revue Médicale Suisse 2015, dyspnée aiguë.",
        "Revue Médicale Suisse 2017, échographie pleuro-pulmonaire.",
        "Revue Médicale Suisse 2008, ponction pleurale.",
        "Revue Médicale Suisse 2004, pneumothorax, organigramme lausannois.",
        "Revue Médicale Suisse 2020, main et poignet.",
        "Revue Médicale Suisse 2008, consolidation d'une fracture.",
        "Revue Médicale Suisse 2018, radiologie en médecine générale.",
        "Recommandations de Bologne 2018 sur l'occlusion du grêle.",
        "Recommandations 2020 sur l'ulcère perforé.",
        "Recommandation suisse d'infectiologie, lue le 31 octobre 2026.",
        "Information professionnelle n° 55185.",
        "Information professionnelle n° 30630.",
        "Information professionnelle n° 47503.",
    ]
    lis = "\n".join(f"<li>{e}</li>" for e in items)
    return ilot("sources", "v", "Sources", f'<ol class="sources">\n{lis}\n</ol>')


def ecrire(nom: str, html: str) -> None:
    p = OUT / nom
    p.write_text(html, encoding="utf-8")
    print("écrit", nom, p.stat().st_size)


def phase_a() -> None:
    methode = fen("w-methode", "Lecture systématique", "\n".join([
        P("La première étape est la qualité du cliché. La revue lausannoise de 2019 renvoie cette étape à un tableau, sans en recopier les lignes dans le texte. On retient ce que le texte dit." + S(1)),
        P("Idéalement, le thorax de face se fait debout, en incidence postéro-antérieure. La plaque est devant le patient. Cela limite l'agrandissement du cœur." + S(1)),
        P("En décubitus, l'incidence est antéro-postérieure. Le cœur s'élargit de façon artificielle. Un gros cœur sur un cliché couché n'est pas une cardiomégalie prouvée." + S(1)),
        P("Ensuite, on connaît l'aspect normal. Une approche va de la périphérie vers le centre. Les structures anatomiques sont regardées l'une après l'autre." + S(1)),
        P("L'erreur de satisfaction de recherche consiste à s'arrêter à la première anomalie et à manquer la lésion associée. Le texte la nomme ainsi, en anglais, dans l'introduction." + S(1)),
        P("Une face suffit dans certaines situations, par exemple la recherche d'un pneumothorax. Face et profil restent au jugement du clinicien." + S(1)),
        P("La tomodensitométrie à très faible dose et l'échographie existent. Elles ne remplacent pas la radiographie en routine, faute de machines ou d'expérience." + S(1)),
        P("Certains diagnostics se posent sur le cliché seul. L'exemple donné est la pneumonie lobaire franche. Dès que l'aspect est atypique, douteux, complexe, ou à côté de la question clinique, la tomodensitométrie est requise." + S(1)),
        P("En cas de doute, les compétences d'un radiologue restent requises." + S(1)),
    ]))
    thorax = fen("w-ex-th", "Examen du cliché thoracique", "\n".join([
        P("Syndrome alvéolaire : opacité aux limites floues, tendance à confluer, bronchogramme aérique. Le bronchogramme se voit comme des hyperclartés tubulées qui bifurquent vers la périphérie." + S(1)),
        P("Syndrome interstitiel : opacités aux limites nettes, non confluentes, sans bronchogramme. Il n'est visible que si les alvéoles voisines restent aérées. L'interstitium normal est invisible." + S(1)),
        P("Les lignes de Kerley, surtout de type B aux bases, et l'aspect en rayon de miel sont des exemples d'interstitiel. Les lignes de Kerley accompagnent souvent une décompensation cardiaque." + S(1)),
        P("Syndrome pleural : opacité homogène, souvent déclive. En décubitus, elle peut remplir une base sans niveau classique." + S(1)),
        P("Œdème cardiogénique : lignes de Kerley B, épanchement, flou péribronchovasculaire, opacités alvéolaires périhilaires en ailes de papillon." + S(1)),
        P("Médiastin : élargissement de la partie supérieure, double contour du bouton aortique, déviation de la trachée, bronche souche gauche abaissée, fenêtre aorto-pulmonaire comblée. Il n'y a pas de consensus sur une largeur chiffrée." + S(1)),
        P("Pour la décompensation cardiaque, la revue de 2015 donne une sensibilité limitée à 68 % et une spécificité de 83 %. Un cliché normal n'écarte pas l'œdème." + S(2)),
        P("Trente pour cent des pneumothorax et 10 à 25 % des épanchements passent inaperçus sur un cliché en clinostatisme, selon la même revue." + S(2)),
    ]))
    abdomen = fen("w-ex-ab", "Examen du cliché abdominal", "\n".join([
        P("Occlusion haute du grêle : la triade lue est faite de plusieurs niveaux hydro-aériques, d'anses grêles distendues, et d'absence de gaz dans le côlon. Elle est dite pathognomonique de l'occlusion de haut grade. La sensibilité globale du cliché simple est d'environ 70 %. La spécificité est dite basse, sans chiffre séparé." + S(9)),
        P("Le cliché ne montre pas les signes précoces de strangulation ni de péritonite. Il ne donne pas l'anatomie qui distingue les causes." + S(9)),
        P("Un pneumopéritoine abondant, y compris dans une occlusion compliquée de perforation, se cherche de préférence sur un thorax debout." + S(9)),
        P("Perforation gastro-duodénale : le thorax et l'abdomen ne sont le premier geste que si la tomodensitométrie n'est pas disponible aussitôt. Le debout et le décubitus latéral gauche ont une exactitude semblable. Le décubitus est mieux toléré." + S(10)),
        P("L'air libre est présent dans 30 à 85 % des perforations selon les études citées en 2020. Un cliché négatif n'écarte pas la perforation." + S(10)),
    ]))
    os = fen("w-ex-os", "Examen du cliché squelettique", "\n".join([
        P("Main et poignet : la radiographie conventionnelle reste la base. Face à une plaie, elle cherche aussi un corps étranger ou une lésion osseuse." + S(6)),
        P("Poignet traumatique : face et profil d'abord. La face aligne le radius, le capitatum et le troisième métacarpien. Le profil superpose les os de l'avant-bras et montre les interlignes." + S(6)),
        P("On suit la corticale. Une rupture est un signe de fracture. On dit ensuite le siège, le trait, le déplacement, le caractère articulaire." + S(6)),
        P("Scaphoïde suspect : deux clichés de Shrek en plus. La première, main à plat en inclinaison ulnaire forcée. La seconde, position d'écriture, rayon perpendiculaire au grand axe du scaphoïde." + S(6)),
        P("Suivi d'une fracture : au moins deux clichés séparés de 90 degrés. On compare la réduction, puis le cal et la disparition du trait. Il n'existe pas de critère radiologique strict de solidité. L'examen clinique reste nécessaire." + S(7)),
        P("Un cal signe la bonne marche d'un traitement conservateur d'une fracture diaphysaire. Après une ostéosynthèse rigide, le même cal révèle une mobilité pathologique." + S(7)),
    ]))
    algo = fen("w-algo", "Ordre d'urgence", "\n".join([
        P("Cet ordre est celui du danger immédiat lu dans les sources. Ce n'est pas une prévalence suisse. Aucune part de chaque cause n'a été lue."),
        P("1. Pneumothorax, surtout si le patient est en détresse. La face peut suffire à le chercher. Le clinostatisme en manque beaucoup." + S(1, 2)),
        P("2. Air libre sous le diaphragme ou pneumopéritoine, avec douleur et défense. La tomodensitométrie prime si elle est disponible. Le cliché négatif ne rassure pas." + S(10)),
        P("3. Médiastin élargi suggestif, avec syncope ou douleur. Pas de seuil en centimètres. La tomodensitométrie confirme." + S(1)),
        P("4. Niveaux et anses du grêle, sans gaz colique. On ne conclut pas à une bride inoffensive si la strangulation n'est pas cherchée par la clinique et, au besoin, la tomodensitométrie." + S(9)),
        P("5. Œdème périhilaire, lignes de Kerley, épanchement. Le cœur couché ne tranche pas." + S(1, 2)),
        P("6. Condensation alvéolaire avec bronchogramme, dans un contexte infectieux." + S(1, 11)),
        P("7. Épanchement isolé ou associé. Le geste pleural ne se décide pas sur un seul contour flou." + S(4)),
        P("8. Luxation du carpe : le profil est obligatoire. La face peut paraître normale." + S(6)),
        P("9. Scaphoïde : clinique forte et clichés insuffisants mènent à l'imagerie par résonance, pas à un retour sans consigne." + S(6)),
        P("10. Extrémité distale du radius : fréquente, surtout chez la femme à partir de 60 ans, mais le cliché ne se limite pas à elle." + S(6)),
    ]))
    tableau = fen("w-tab", "Tableau comparatif", table(
        "Ce que le cliché montre, et ce qu'il ne montre pas",
        ["Image", "Lecture retenue", "Limite lue"],
        [
            ["Condensation floue avec bronchogramme", "Syndrome alvéolaire. Pneumonie lobaire franche possible si le contexte colle.", "Infection, hémorragie et œdème restent ouverts. Une image qui persiste se réexplore." + S(1)],
            ["Lignes de Kerley et ailes de papillon", "Surcharge cardiogénique.", "Sensibilité 68 %, spécificité 83 % dans la décompensation." + S(2)],
            ["Base opaque en décubitus", "Épanchement possible.", "10 à 25 % des épanchements manquent en clinostatisme." + S(2)],
            ["Ligne pleurale viscérale, sans vaisseau au-delà", "Pneumothorax à confirmer sur le cliché.", "Sensibilité 50 à 90 %. Le partiel et le couché échappent." + S(3)],
            ["Médiastin supérieur large, double contour", "Suspicion de dissection. Pas un diagnostic de cliché.", "Pas de consensus sur la largeur. Tomodensitométrie indispensable." + S(1)],
            ["Niveaux, grêle distendu, côlon sans gaz", "Occlusion de haut grade.", "Sensibilité d'environ 70 %. Pas la strangulation précoce." + S(9)],
            ["Air sous les coupoles", "Perforation d'organe creux possible.", "Présent dans 30 à 85 % des perforations seulement." + S(10)],
            ["Rupture de corticale au radius distal", "Fracture de l'extrémité distale.", "Deux plans. Le reste du carpe se lit aussi." + S(6, 7)],
            ["Scaphoïde douloureux, trait absent", "N'exclut pas la fracture.", "Clichés de Shrek, puis résonance si la clinique est forte." + S(6)],
            ["Face de poignet banale, profil rompu", "Luxation rétrolunaire possible.", "Environ 25 % manqués au premier passage, selon la revue de 2020." + S(6)],
        ],
    ))
    doses = fen("w-doses", "Doses lues dans l'information professionnelle", "\n".join([
        P("Trois numéros seulement. 55185, 30630 et 47503. Aucune autre dose n'est écrite."),
        P("Co-Amoxicilline Sandoz, n° 55185, pour une pneumonie ambulatoire retenue, et seulement dans le cadre de la phrase lue. " + C_CO_REC + S(12)),
        P(C_CO + S(12)),
        P("Grossesse. " + C_CO_G + S(12)),
        P("Allaitement. " + C_CO_A + S(12)),
        P("Lasix, n° 30630, si l'œdème pulmonaire cardiogénique est le diagnostic, avec les autres mesures. " + C_LA_IND + S(13)),
        P(C_LA_AD + S(13)),
        P(C_LA + S(13)),
        P("Grossesse. " + C_LA_G + " Un traitement durant la grossesse nécessite une surveillance de la croissance fœtale." + S(13)),
        P("Allaitement. " + C_LA_A + S(13)),
        P("DAFALGAN, n° 47503, douleur après blessure ou douleur articulaire et ligamentaire, intensité faible à modérée. " + C_PA_IND + S(14)),
        P(C_PA_DOSE + S(14)),
        P(C_PA + S(14)),
        P(C_PA_CI + S(14)),
        P("Les milligrammes de la recommandation suisse d'infectiologie ne sont pas recopiés. Ils ne sont pas ces phrases." + S(11)),
    ]))
    dumps = sources(
        ("w-s1", "Texte 2019, thorax", "rms2019_thorax.txt", 1, (), 50, False),
        ("w-s2", "Texte 2015, dyspnée", "rms2015_dyspnee.txt", 2, (), 18, False),
        ("w-s9", "Texte 2018, occlusion", "wses2018_asbo.txt", 9, (), 36, False),
        ("w-s10", "Texte 2020, perforation", "wses2020_ulcere.txt", 10, (), 28, False),
        ("w-s6", "Texte 2020, poignet", "rms2020_main.txt", 6, (), 40, False),
        ("w-s11", "Texte suisse, pneumonie", "ssi_pac.txt", 11, (), 12, False),
        ("w-s3", "Texte 2017, plèvre", "rms2017_echo.txt", 3, (), 22, False),
    )
    blocs = [
        ilot("ess", "c essentiel", "L'essentiel", "\n".join([
            P("Un cliché anormal du thorax, de l'abdomen ou du squelette est une image qui s'écarte de l'aspect normal. Ce n'est pas encore le nom de la maladie."),
            P("On lit d'abord la qualité, puis toute l'image, de la périphérie vers le centre pour le thorax. S'arrêter à la première tache fait manquer la seconde." + S(1)),
            P("Dix causes sont développées. Leur ordre n'est pas une fréquence suisse. L'urgence de lecture est une autre liste. " + b("w-algo", "voir l'ordre")),
            P(b("w-methode", "la méthode") + " " + b("w-tab", "le tableau") + " " + b("w-doses", "les doses lues")),
        ])),
        som(),
        ilot("p1", "c", "1. Définition", "\n".join([
            P("La situation de départ est le cliché anormal, pas la plainte qui l'a fait demander. Le cours apprend à nommer l'image, puis à choisir le diagnostic qui colle au malade."),
            P("La revue de 2019 rappelle qu'un médecin distingue souvent le normal de l'anormal, et qu'un diagnostic précis est une autre difficulté." + S(1)),
            methode,
        ])),
        ilot("p2", "v", "2. Épidémiologie", "\n".join([
            P("Aucune source lue ne répartit ces dix images dans la population suisse. On ne fabrique pas de rang."),
            P("Repères séparés, qui ne sont pas des parts du cliché anormal. La main et le poignet représentent 70 % des consultations de traumatologie en urgence, selon la revue genevoise de 2020." + S(6)),
            P("Plus de la moitié des traumatismes du poignet vus aux urgences s'associent à une fracture du radius distal. Elle représente deux tiers des fractures de l'avant-bras." + S(6)),
            P("La recommandation suisse d'infectiologie décrit la pneumonie communautaire de l'adulte. Elle ne donne pas, dans l'extrait retenu, une incidence nationale du cliché." + S(11)),
        ])),
        ilot("p3", "c", "3. Physiopathologie", "\n".join([
            P("L'alvéole se remplit : l'opacité est floue, confluente, et le bronchogramme montre l'air encore dans la bronche." + S(1)),
            P("L'interstitium s'épaissit par œdème, cellules ou fibrose. Il ne se voit que si l'alvéole d'à côté reste aérée." + S(1)),
            P("L'air pleural décolle le poumon de la paroi. L'air péritonéal, sous le diaphragme, vient d'un organe creux ouvert." + S(3, 10)),
            P("L'os casse quand la corticale cède. Le scaphoïde, couvert de cartilage sur plus de 75 % de sa surface, se fracture surtout en hyperextension. Sa vascularisation va du distal vers le proximal." + S(6)),
        ])),
        ilot("p4", "v", "4. Démarche diagnostique", "\n".join([
            P("On commence par ce qui tue pendant que le cliché est encore sur l'écran. Pneumothorax. Air libre. Médiastin suggestif. Occlusion qui pourrait étrangler."),
            P("Ensuite seulement la condensation, l'épanchement, puis le poignet. " + b("w-algo", "l'ordre commenté")),
            P("Le drapeau rouge n'est pas une largeur de médiastin inventée. C'est l'association d'une image suggestive et d'une syncope, ou d'une défense avec un cliché qui peut être négatif." + S(1, 10)),
            algo + tableau,
        ])),
        ilot("p5", "c", "5. Anamnèse", "\n".join([
            P("Thorax : fièvre, toux, douleur pleurale, dyspnée, orthopnée, syncope, traumatisme, geste veineux central récent."),
            P("Abdomen : chirurgie ancienne pour la bride, douleur brutale pour la perforation, arrêt des gaz, vomissements." + S(9, 10)),
            P("Squelette : chute sur la main en hyperextension, énergie du traumatisme, âge, côté dominant. La femme à partir de 60 ans fracture le radius distal après une chute de sa hauteur. Avant cet âge, les hommes et un choc plus violent dominent." + S(6)),
        ])),
        ilot("p6", "v", "6. Examen physique", "\n".join([
            P("Le cliché se lit avec le malade, pas à la place du malade. Détresse, asymétrie de murmure, défense, déformation, tabatière douloureuse."),
            P("Trois fenêtres d'examen. " + b("w-ex-th", "thorax") + " " + b("w-ex-ab", "abdomen") + " " + b("w-ex-os", "squelette")),
            thorax + abdomen + os,
        ])),
        ilot("p7", "c", "7. Approche syndromique", "\n".join([
            P("Trois syndromes thoraciques se combinent souvent : alvéolaire, interstitiel, pleural. La revue de 2019 le montre sur une décompensation qui s'aggrave d'un jour à l'autre." + S(1)),
            P("Une condensation rétrocardiaque peut être une inhalation ou une surinfection, pas seulement l'œdème." + S(1)),
            P("Au poignet, le syndrome est osseux (trait, corticale) ou articulaire (alignement rompu, lignes de Gilula)." + S(6)),
        ])),
        ilot("p8", "v", "8. Diagnostic positif", "\n".join([
            P("Pneumonie communautaire, définition suisse retenue : nouvel infiltrat et symptômes d'infection respiratoire basse. Acquisition hors de l'hôpital, ou dans les 48 heures après l'admission." + S(11)),
            P("Pneumonie lobaire franche : le cliché peut suffire, dit la revue de 2019, si l'image est typique et le contexte aussi. L'image atypique demande la tomodensitométrie." + S(1)),
            P("Les neuf autres diagnostics ont leur fichier. Leurs noms exacts sont ceux de la liste canonique."),
        ])),
        ilot("p9", "c", "9. Examens complémentaires", "\n".join([
            P("Thorax de face, et profil si le clinicien le juge utile. Abdomen et thorax debout seulement si la tomodensitométrie de la perforation ou de l'occlusion n'est pas disponible aussitôt." + S(9, 10)),
            P("Poignet : face, profil, clichés de Shrek si le scaphoïde est en cause. Résonance si la clinique de scaphoïde est forte et le trait peu visible. Scanner si le trait est vu mais la stabilité douteuse." + S(6)),
            P("Échographie pleurale avant une ponction difficile. La radiographie de contrôle après ponction n'est pas systématique chez l'asymptomatique, sans irradiation thoracique antérieure, après une seule tentative, sans aspiration d'air." + S(4)),
        ])),
        ilot("p10", "v", "10. Arbre décisionnel", "\n".join([
            P("Qualité du cliché. Puis recherche du danger. Puis syndrome. Puis le diagnostic du fichier correspondant. " + b("w-algo", "ouvrir l'arbre")),
            P("Les dix noms : Pneumonie acquise en communauté. Œdème pulmonaire cardiogénique. Épanchement pleural. Pneumothorax spontané. Suspicion de dissection aortique. Occlusion du grêle sur adhérences. Perforation d'ulcère peptique. Fracture de l'extrémité distale du radius. Fracture du scaphoïde. Luxation rétrolunaire du carpe."),
        ])),
        ilot("p11", "c", "11. Prise en charge en Suisse", "\n".join([
            P("Le cliché ne dicte pas une boîte de médicaments. La dose n'apparaît que si le diagnostic du fichier est retenu et si l'information professionnelle le dit."),
            P("Pneumonie ambulatoire et produit n° 55185. Œdème pulmonaire et produit n° 30630. Douleur de blessure et produit n° 47503. " + b("w-doses", "phrases exactes")),
            P("La recommandation suisse demande une imagerie si la pneumonie est suspectée. Hospitalisé : exigée. Ambulatoire : recommandée. Face et profil pour un nouvel infiltrat sans autre diagnostic." + S(11)),
            doses,
        ])),
        ilot("p12", "v", "12. Prévention", "\n".join([
            P("Prévenir l'erreur de lecture : une méthode fixe, un second regard si le cliché ne répond pas à la question, un radiologue en cas de doute." + S(1)),
            P("Prévenir le scaphoïde manqué : tabatière et tubercule palpés, clichés dédiés, imagerie suivante si la clinique tient." + S(6)),
            P("Prévenir la luxation manquée : ne jamais accepter une face seule." + S(6)),
            P("La vaccination après pneumonie suit le plan suisse. Le détail des vaccins n'est pas une dose de ce cours." + S(11)),
        ])),
        ilot("p13", "c", "13. Points clés", "\n".join([
            P("Qualité, puis toute l'image, puis le contexte. Le cœur couché ment. Le médiastin n'a pas de seuil consensuel en centimètres." + S(1)),
            P("Le cliché négatif n'écarte ni la perforation, ni le scaphoïde, ni l'œdème." + S(2, 6, 10)),
            P("Trois numéros d'autorisation, et pas d'autre milligramme."),
        ])),
        ilot("p14", "v", "14. Pièges d'examen", "\n".join([
            P("Cinq pièges reviennent dans les textes lus. Ils sont détaillés dans la fenêtre."),
            fen("w-pieges", "Pièges d'examen", "\n".join([
                '<details class="quiz"><summary>S’arrêter à la première tache</summary><p>La revue de 2019 décrit l’erreur qui consiste à identifier l’anomalie cherchée et à omettre la lésion associée. On reprend la périphérie.</p></details>',
                '<details class="quiz"><summary>Appeler cardiomégalie un cœur couché</summary><p>L’incidence antéro-postérieure agrandit le cœur. La revue le dit délicat à interpréter.</p></details>',
                '<details class="quiz"><summary>Rassurer parce que l’air libre manque</summary><p>La fourchette lue est 30 à 85 %. Le reste des perforations n’a pas ce signe.</p></details>',
                '<details class="quiz"><summary>Exclure le scaphoïde sur une face et un profil</summary><p>Un trait peu déplacé peut ne pas être traversé par ces rayons. Les clichés de Shrek sont prévus pour cela.</p></details>',
                '<details class="quiz"><summary>Croire normale la face du poignet</summary><p>La luxation rétrolunaire se voit sur le profil. La revue de 2020 dit qu’environ un quart est manqué au début.</p></details>',
            ])),
        ])),
        sources_ol(),
        dumps,
    ]
    # dumps are popovers: they must sit inside a section or after. Orphan divs after sections are OK in body.
    html = page(
        "LOT_152_Phase_A_V0.html",
        "Radiographies abdominales, thoraciques ou squelettiques anormales",
        "Situation de départ F2.4. Texte du 31.10.2026. Les dix diagnostics ne sont pas classés par prévalence.",
        blocs,
    )
    ecrire("LOT_152_Phase_A_V0.html", html)


def coeur(n: int, paras: list[str], extra: str = "") -> str:
    inner = "\n".join(P(x) for x in paras)
    return fen(f"w{n}-coeur", DX[n], inner + extra)


def dx_page(n: int, points: list[str], extra_fen: str = "") -> None:
    nom = DX[n]
    corps_pts = []
    titres = [
        (1, "1. Définition", "c"),
        (2, "2. Épidémiologie", "v"),
        (3, "3. Physiopathologie", "c"),
        (4, "4. Démarche diagnostique", "v"),
        (5, "5. Anamnèse", "c"),
        (6, "6. Examen physique", "v"),
        (7, "7. Approche syndromique", "c"),
        (8, "8. Diagnostic positif", "v"),
        (9, "9. Examens complémentaires", "c"),
        (10, "10. Arbre décisionnel", "v"),
        (11, "11. Prise en charge en Suisse", "c"),
        (12, "12. Prévention", "v"),
        (13, "13. Points clés", "c"),
        (14, "14. Pièges d'examen", "v"),
    ]
    # points: 15 strings, index 0 is essentiel, then 14
    blocs = [
        ilot("ess", "c essentiel", "L'essentiel", points[0] + fen(f"w{n}-lien", "Lien avec la Phase A", P(
            f"Ce fichier est le diagnostic {n} de F2.4. La Phase A porte la méthode de lecture et l'ordre d'urgence. On ne la répète pas. On approfondit {nom}."
        ))),
        som(),
    ]
    for (i, titre, cls), texte in zip(titres, points[1:]):
        blocs.append(ilot(f"p{i}", cls, titre, texte))
    blocs.append(sources_ol())
    blocs.append(extra_fen)
    html = page(
        f"LOT_152_Phase_B_V0_DX.{n}.html",
        nom,
        f"Diagnostic différentiel DX.{n} de F2.4 « Radiographies abdominales, thoraciques ou squelettiques anormales ». Texte du 31.10.2026.",
        blocs,
        h2_dx=f"DX.{n} — {nom}",
    )
    ecrire(f"LOT_152_Phase_B_V0_DX.{n}.html", html)


def dx1() -> None:
    c = coeur(1, [
        "La recommandation suisse définit la pneumonie par un nouvel infiltrat et des symptômes d'infection respiratoire basse. La forme communautaire s'acquiert hors de l'hôpital, ou débute dans les 48 heures après l'admission. Les résidents d'institution sont inclus." + S(11),
        "L'immunosuppression sévère est hors de cette recommandation. Le seuil de corticoïde en milligrammes n'est pas recopié : il n'est pas une phrase de l'information professionnelle citée.",
        "Sur le cliché, la pneumonie lobaire franche est un syndrome alvéolaire. Opacité floue, confluence, bronchogramme aérique. La revue lausannoise de 2019 dit que ce diagnostic peut être assuré par la radiographie seule quand l'image est typique." + S(1),
        "La systématisation exacte du lobe n'est pas toujours exhaustive sur un seul cliché. Le diagnostic de l'affection peut quand même être posé." + S(1),
        "Si l'image persiste malgré un traitement approprié, une autre lésion reste possible. Une récidive fait chercher une lésion sous-jacente." + S(1),
        "Les condensations focales aiguës évoquent aussi l'hémorragie alvéolaire et l'œdème. Le contexte tranche. La fièvre seule ne suffit pas." + S(1),
        "Imagerie exigée chez l'hospitalisé suspect, recommandée en ambulatoire. Face et profil. L'échographie est une alternative si quelqu'un de qualifié la fait et si la radiographie n'est pas disponible. Elle manque les pneumonies centrales." + S(11),
        "Le score ambulatoire donne un point à la confusion récente, à la fréquence respiratoire d'au moins 30, à la pression basse, et à l'âge d'au moins 65 ans. Plus de 2 points indiquent une forme sévère." + S(11),
        "L'hospitalisation se discute dès 1 point, sauf si l'âge est le seul point. Elle se discute aussi si la saturation à l'air est inférieure à 90 pour cent, si une comorbidité est instable, ou s'il y a un épanchement." + S(11),
        "Un infiltrat multilobaire figure parmi les signes qui appellent une surveillance accrue." + S(11),
        "Réévaluation ambulatoire à 48-72 heures. Infiltrat encore complet au-delà de 30 jours : la recommandation parle de pneumonie persistante." + S(11),
        "Dose, seulement si ce diagnostic ambulatoire est retenu. Produit n° 55185. " + C_CO_REC + S(12),
        C_CO + S(12),
        "Grossesse. " + C_CO_G + S(12),
        "Allaitement. " + C_CO_A + S(12),
        "Les schémas en grammes de la recommandation suisse, y compris la forme intraveineuse, ne sont pas recopiés.",
    ])
    dumps = sources(
        ("w1a", "Revue 2019", "rms2019_thorax.txt", 1, ("alvéol", "pneumonie", "bronchogramme", "condensation"), 16, False),
        ("w1b", "Recommandation suisse", "ssi_pac.txt", 11, (), 14, False),
        ("w1c", "Information professionnelle 55185", "aips_55185.txt", 12, ("pneumonie", "Posologie", "grossesse", "allait", "625"), 12, True),
    )
    P1 = P("Nouvel infiltrat et symptômes d'infection basse. Acquisition hors hôpital, ou dans les 48 premières heures. " + b("w1-coeur", "le détail") + S(11))
    dx_page(1, [
        P("Condensation qui peut être une pneumonie, pas une pneumonie déclarée sur une tache. " + b("w1-coeur", "approfondir")) + c,
        P1,
        P("Pas d'incidence suisse de cette image dans les textes lus. La recommandation décrit l'adulte, pas un taux de clichés." + S(11)),
        P("L'alvéole se remplit. L'air bronchique reste visible. C'est le bronchogramme." + S(1)),
        P("On écarte d'abord le pneumothorax, l'air libre et le médiastin suggestif, qui sont d'autres fichiers. Ici, la fièvre et la toux orientent, elles ne ferment pas." + S(1)),
        P("Toux, fièvre, expectoration, douleur thoracique, dyspnée, tachypnée. Institution ou retour récent de l'hôpital : la définition communautaire a une limite de 48 heures." + S(11)),
        P("Murmure, souffle, matité. Le cliché de face et de profil confirme un nouvel infiltrat sans autre diagnostic." + S(11) + b("w1-coeur", " critères du cliché")),
        P("Syndrome alvéolaire focal. Les formes multifocales et rétrocardiaques se voient aussi dans l'inhalation et l'œdème." + S(1)),
        P("Image typique et contexte infectieux : la revue de 2019 accepte le diagnostic sur le cliché. Image atypique : tomodensitométrie." + S(1)),
        P("Échographie seulement en alternative qualifiée, sans voir les foyers centraux. Contrôle si l'évolution déçoit." + S(11)),
        P("Suspecter, imager, coter la gravité, traiter seulement si le diagnostic tient. L'arbre général est dans la Phase A."),
        P("Ambulatoire : phrase du n° 55185, et recommandations locales que le texte du produit exige. " + b("w1-coeur", "la phrase") + S(12)),
        P("Revoir à 48-72 heures en ambulatoire. Chercher une autre lésion si l'image revient." + S(1, 11)),
        P("Bronchogramme et limites floues. Face et profil. Pas de milligramme hors n° 55185."),
        P("Piège : toute base opaque n'est pas une pneumonie. L'épanchement en décubitus et l'œdème périhilaire ont leurs fichiers." + S(1)),
    ], dumps + elargi(1, [
        ("rms2018_radio.txt", 8, 36),
        ("rms2004_pno.txt", 5, 28),
        ("rms2008_plevre.txt", 4, 12),
    ]))


def dx2() -> None:
    c = coeur(2, [
        "La surcharge cardiogénique se lit en plusieurs couches. Lignes de Kerley B aux bases. Épanchement. Flou autour des bronches et des vaisseaux. Opacités alvéolaires périhilaires, dites en ailes de papillon." + S(1),
        "La revue de 2019 montre deux clichés successifs. Le second, au lendemain d'un arrêt, est plus chargé. Après traitement, l'image régresse. Le cas était un infarctus avec sus-décalage. L'œdème n'était pas la cause première." + S(1),
        "En 2015, la radiographie de la décompensation cardiaque a une sensibilité limitée à 68 % et une spécificité de 83 %. Elle ne sert pas de test d'exclusion." + S(2),
        "Le cœur debout, plaque devant, est moins agrandi. Le cœur couché s'élargit par la géométrie. On ne pose pas la cardiomégalie sur ce seul fait." + S(1),
        "Indication du produit n° 30630. " + C_LA_IND + S(13),
        C_LA_AD + S(13),
        C_LA + S(13),
        "La dose maximale recommandée du texte est de 1 500 mg par jour pour la voie intraveineuse. Seule l'insuffisance rénale très diminuée justifie en général de telles doses, et un autre dosage du même nom est alors visé. On ne les prescrit pas d'emblée.",
        "Grossesse. " + C_LA_G + " Surveillance de la croissance fœtale si le traitement a lieu." + S(13),
        "Allaitement. " + C_LA_A + " Le furosémide passe dans le lait et inhibe la lactation." + S(13),
        "Enfants de moins de 15 ans : la voie parentérale est réservée aux cas critiques dans le même texte. La dose au kilogramme n'est pas recopiée ici, pour ne pas l'appliquer à l'adulte.",
    ])
    dumps = sources(
        ("w2a", "Revue 2019", "rms2019_thorax.txt", 1, ("Kerley", "œdème", "cardia", "décubitus"), 14, False),
        ("w2b", "Revue 2015", "rms2015_dyspnee.txt", 2, ("68", "décompensation", "radiographie"), 12, False),
        ("w2c", "Information professionnelle 30630", "aips_30630.txt", 13, ("Oedème pulmonaire", "40 mg", "grossesse", "allaitement", "15 ans"), 12, True),
    )
    dx_page(2, [
        P("Œdème dont l'image est cardiogénique, pas toute dyspnée avec un gros cœur. " + b("w2-coeur", "approfondir")) + c,
        P("Lignes de Kerley, flou péribronchovasculaire, ailes de papillon, épanchement. Le cœur couché ne prouve pas la taille réelle." + S(1)),
        P("Pas de part suisse lue. La sensibilité du cliché dans la décompensation est de 68 %, la spécificité de 83 %, revue de 2015." + S(2)),
        P("La pression capillaire monte quand le ventricule gauche se vide mal. L'interstitiel se voit d'abord, l'alvéole ensuite. La revue de 2019 décrit les deux sur des clichés séparés de quelques heures." + S(1)),
        P("Devant une dyspnée, ce diagnostic vient après le pneumothorax et en même temps que l'on cherche l'infarctus qui peut l'avoir déclenché. Le cas publié était un sus-décalage." + S(1)),
        P("Orthopnée, œdèmes, prise de poids, douleur thoracique. Une syncope ou une douleur ouvrent aussi le fichier de la dissection."),
        P("Crépitants et turgescence. Le cliché complète, il ne remplace pas l'électrocardiogramme ni, si le doute tient, l'échocardiographie." + S(2)),
        P("Souvent trois syndromes ensemble : interstitiel, alvéolaire, pleural. Une condensation rétrocardiaque peut être une inhalation." + S(1)),
        P("Image évocatrice plus contexte. Une sensibilité de 68 % interdit d'exclure le diagnostic sur un cliché pauvre." + S(2)),
        P("Thorax debout si le patient le peut. Peptide natriurétique et échocardiographie ne sont pas détaillés ici : les seuils n'ont pas été relus dans cette passe."),
        P("Détresse et sus-décalage d'abord. Puis ce fichier si l'image est celle de la surcharge et que le produit n° 30630 a son indication."),
        P(C_LA + " Autres mesures associées, dit l'indication. " + S(13) + b("w2-coeur", "grossesse et allaitement")),
        P("Revoir le cliché après le traitement, comme dans la série publiée où l'image régresse." + S(1)),
        P("68 % et 83 %. Cœur couché non concluant. Dose seulement n° 30630."),
        P("Piège : crépitants plus gros cœur égalent infarctus ou égalent insuffisance, sans regarder le pneumothorax ni l'embolie, qui ne sont pas ce fichier."),
    ], dumps + elargi(2, [
        ("rms2019_thorax.txt", 1, 40),
        ("rms2018_radio.txt", 8, 30),
        ("rms2017_echo.txt", 3, 24),
    ]))


def dx3() -> None:
    c = coeur(3, [
        "Avant une ponction, une radiographie de face, et au besoin de profil, est obligatoire pour confirmer l'épanchement ou le pneumothorax que l'on suspecte." + S(4),
        "En cas de doute sur la quantité, ou si l'on pense à un épanchement cloisonné, un cliché en décubitus latéral peut aider. Un épanchement de plus de 10 mm sur cette incidence permet une thoracentèse, selon le texte de 2008." + S(4),
        "La radiographie de contrôle après le geste n'est pas recommandée d'office si le patient va bien, s'il n'a pas d'antécédent d'irradiation thoracique, si une seule tentative a eu lieu, et si l'on n'a pas aspiré d'air." + S(4),
        "L'échographie diminue les erreurs de repère. Elle se justifie pour un petit épanchement, un siège difficile, ou une cloison. Le texte de 2008 ne la rend pas obligatoire pour tout geste facile. La revue de 2017 la recommande avant les procédures pleurales." + S(3, 4),
        "En 2015, l'échographie a une sensibilité et une spécificité supérieures à 90 % pour l'épanchement, parfois proches de 100 %. Dix à 25 % des épanchements manquent sur un cliché en clinostatisme." + S(2),
        "Sur le cliché couché de la dissection, l'opacité homogène de la base gauche était l'épanchement. Le récessus non vu est un défaut technique à écrire, pas une preuve de vide." + S(1),
        "Aucune dose d'anesthésique local n'est écrite. Aucune information professionnelle n'a été relue pour la lidocaïne dans cette passe.",
    ])
    dumps = sources(
        ("w3a", "Revue 2008, ponction", "rms2008_plevre.txt", 4, ("radiographie", "épanchement", "10 mm", "décubitus"), 14, False),
        ("w3b", "Revue 2017", "rms2017_echo.txt", 3, ("épanchement", "pleur", "sensib"), 12, False),
        ("w3c", "Revue 2015", "rms2015_dyspnee.txt", 2, ("épanchement", "25"), 8, False),
    )
    dx_page(3, [
        P("Liquide pleural dont l'image est une opacité, pas toute opacité basale. " + b("w3-coeur", "approfondir")) + c,
        P("Opacité homogène, déclive, récessus comblé. En décubitus, elle peut être paramédiastinale ou basale sans courbe classique." + S(1)),
        P("Pas de prévalence suisse lue. Dix à 25 % des épanchements échappent au cliché en clinostatisme." + S(2)),
        P("Le liquide suit la gravité. Couchée, la couche s'étale. Debout, elle dessine le récessus."),
        P("On ne ponctionne pas avant d'avoir vu l'image, et on ne traite pas un épanchement comme une pneumonie sans les distinguer." + S(4)),
        P("Douleur pleurale, dyspnée, fièvre si l'infection est en cause, traumatisme, insuffisance cardiaque. Le cancer et l'embolie ne sont pas documentés dans les extraits retenus."),
        P("Matité déclive, murmure aboli. Confirmer par le cliché, ou par l'échographie si le repère est difficile." + S(4)),
        P("Syndrome pleural, souvent associé à l'alvéolaire ou à l'interstitiel dans la décompensation." + S(1)),
        P("Le diagnostic d'épanchement sur le cliché se confirme par l'aspect et, si l'on doit ponctionner, par les conditions de 2008. Plus de 10 mm en décubitus latéral est le seuil lu pour la thoracentèse." + S(4)),
        P("Décubitus latéral si le doute porte sur le volume ou les cloisons. Échographie pour le petit épanchement et le geste." + S(3, 4)),
        P("Voir, mesurer la possibilité du geste, ponctionner si l'indication clinique existe, ne pas radiographier après coup sans raison lue."),
        P("Pas de dose médicamenteuse dans ce fichier. Le traitement est celui de la cause, dans un autre diagnostic, ou le geste pleural sans milligramme inventé."),
        P("Ne pas oublier l'épanchement quand on a déjà nommé la condensation. Les deux coexistent." + S(1)),
        P("Dix millimètres en décubitus latéral. Contrôle radiographique non systématique dans les quatre conditions lues."),
        P("Piège : opacité de base égale pneumonie, alors que le texte de 2019 appelle épanchement l'opacité homogène du décubitus." + S(1)),
    ], dumps + elargi(3, [
        ("rms2019_thorax.txt", 1, 40),
        ("rms2017_echo.txt", 3, 36),
        ("rms2018_radio.txt", 8, 28),
    ]))


def dx4() -> None:
    c = coeur(4, [
        "Une face suffit souvent à chercher un pneumothorax. C'est l'exemple donné en 2019. Le profil reste au jugement clinique." + S(1),
        "La sensibilité de la radiographie va de 50 à 90 %. Le pneumothorax partiel, et le patient alité, échappent. L'échographie atteint 98 % dans la revue de 2017, y compris pour un pneumothorax minime." + S(3),
        "En pneumothorax, les lignes A restent. La moindre ligne B l'exclut. Le glissement pleural manque. Le point poumon, en mode temps-mouvement, a une spécificité de 100 % pour le pneumothorax partiel." + S(3),
        "Trente pour cent des pneumothorax manquent en clinostatisme, revue de 2015. Le cliché debout en expiration forcée est dit hautement spécifique dans le même article. On ne transforme pas cet adjectif en pourcentage." + S(2),
        "La radiographie confirme la présence et montre l'importance. Cette phrase est dans le texte lausannois de 2004." + S(5),
        "Le même texte propose un scanner après 30 ans au premier épisode, après drainage, et en cas de récidive, pour chercher une maladie du poumon. Avant 30 ans, il ne le propose pas d'emblée, sauf symptôme pulmonaire déjà là. C'est un organigramme de 2004." + S(5),
        "Récidive lue en 2004 : de l'ordre de 25 % après un premier épisode traité de façon conservatrice, fourchette 16 à 50 %. Environ 50 % après la première récidive traitée ainsi. Environ 75 % après la deuxième. Le texte propose alors le drainage au premier épisode primaire, et la chirurgie thoracoscopique à la première récidive." + S(5),
        "Le résumé de 2023 n'a pas été ouvert en texte intégral. Ces chiffres ne sont pas présentés comme la règle de 2023. Ils restent datés de 2004.",
        "Aucune dose d'analgésie propre au drain n'est écrite.",
        "Après une voie centrale, on cherche le pneumothorax et aussi le trajet du cathéter. Le cas de 2019 montrait un cathéter dans l'aorte, d'abord décrit sans pneumothorax." + S(1),
    ])
    dumps = sources(
        ("w4a", "Revue 2017", "rms2017_echo.txt", 3, ("pneumothorax", "glissement", "sensib"), 12, False),
        ("w4b", "Revue 2004", "rms2004_pno.txt", 5, ("pneumothorax", "récidive", "drainage", "scanner"), 14, False),
        ("w4c", "Revue 2019", "rms2019_thorax.txt", 1, ("pneumothorax", "cathéter", "face"), 8, False),
    )
    dx_page(4, [
        P("Air pleural, pas toute hyperclarté. " + b("w4-coeur", "approfondir")) + c,
        P("Ligne pleurale viscérale, absence de vaisseau en périphérie. La face est souvent suffisante pour le chercher." + S(1)),
        P("Sensibilité du cliché : 50 à 90 %. Pas de taux suisse de l'événement." + S(3)),
        P("L'air entre dans la plèvre, le poumon se rétracte. Un très gros pneumothorax comprime. Le texte lu ne donne pas un pourcentage de poumon qui définirait la tension. La tension se juge d'abord au lit."),
        P("Détresse d'abord. Le cliché ne retarde pas un geste si le malade s'effondre et que l'auscultation est univoque. Ce seuil clinique n'est pas un chiffre de la revue."),
        P("Douleur brutale, dyspnée, grand fumeur, grand sujet mince, maladie pulmonaire connue, geste veineux, traumatisme, règles si l'on pense au pneumothorax cataménial de 2004." + S(5)),
        P("Asymétrie du murmure, tympanisme. Puis le cliché. L'échographie si l'on sait la faire, surtout chez l'alité." + S(3)),
        P("Hyperclarté sans trame. Ne pas le confondre avec une grosse bulle : le glissement pleural, s'il est présent, va plutôt vers l'emphysème cloisonné, dit la revue de 2017." + S(3)),
        P("Le cliché confirme et montre l'importance. Il ne date pas la conduite chirurgicale de 2023, qui n'a pas été lue en entier."),
        P("Scanner selon l'organigramme de 2004 rappelé dans la fenêtre, pas comme une obligation intemporelle." + S(5)),
        P("Chercher l'air, chercher le cathéter s'il y en a un, drainer selon l'état et selon un protocole d'établissement. Les seuils de 2004 sont historiques."),
        P("Pas de dose dans ce fichier. L'oxygène et l'analgésie du drain ne sont pas tirés d'une information professionnelle relue ici."),
        P("Anamnèse familiale si le pneumothorax se répète. Le résumé de 2023 insiste sur un syndrome génétique. Le détail des gènes n'a pas été lu."),
        P("50 à 90 %. Ligne B qui exclut. Face souvent suffisante. Chiffres de récidive datés de 2004."),
        P("Piège : écrire « pas de pneumothorax » et ne pas suivre le cathéter. Le cas lausannois de 2019 est exactement cela." + S(1)),
    ], dumps + elargi(4, [
        ("rms2015_dyspnee.txt", 2, 16),
        ("rms2019_thorax.txt", 1, 28),
        ("rms2017_echo.txt", 3, 16),
        ("rms2018_radio.txt", 8, 10),
    ]))


def dx5() -> None:
    c = coeur(5, [
        "Le cas de 2019 est une syncope. Le cliché montre un élargissement manifeste du médiastin. Il n'existe pas de consensus sur la définition chiffrée d'un élargissement sur une face." + S(1),
        "Ce qui est suggestif, dans le texte : élargissement de la partie supérieure, opacité anormale, double contour avec dédoublement du bouton aortique, trachée déviée, bronche souche gauche relativement abaissée, fenêtre aorto-pulmonaire comblée." + S(1),
        "L'opacité homogène de la base gauche, en décubitus, était un épanchement. Le récessus non analysable est un défaut à signaler." + S(1),
        "Le diagnostic se confirme par la tomodensitométrie injectée. Elle montre le vrai chenal, le faux chenal, le voile intimal. Dans le cas, il y avait aussi un épanchement péricardique, visible au scanner, pas affirmé sur le cliché seul." + S(1),
        "La dissection du cas commençait à l'aorte ascendante. Le texte l'appelle type A. On ne généralise pas un classement plus fin que cette phrase.",
        "Aucune dose d'antihypertenseur n'est écrite. Aucune information professionnelle n'a été relue pour cela dans cette passe. La baisse de pression se décide au bloc et en réanimation, pas par un milligramme inventé.",
    ])
    dumps = sources(
        ("w5a", "Revue 2019, cas du médiastin", "rms2019_thorax.txt", 1, ("médiastin", "dissection", "aort", "syncope"), 12, False),
    )
    dx_page(5, [
        P("Image suggestive, pas une dissection prouvée par la radiographie. " + b("w5-coeur", "approfondir")) + c,
        P("Médiastin supérieur large, double contour du bouton aortique, trachée déviée, bronche souche gauche abaissée, fenêtre aorto-pulmonaire opaque." + S(1)),
        P("Pas de fréquence suisse lue. Pas de seuil en centimètres : le texte dit qu'il n'y a pas de consensus." + S(1)),
        P("Le sang clive la media. Le faux chenal élargit la silhouette. Le cliché voit la silhouette, pas le voile intimal."),
        P("Syncope, douleur thoracique, déficit, hypotension : la tomodensitométrie ne se discute pas longtemps. Le cliché ne doit pas retarder le scanner si le malade est instable."),
        P("Douleur migratrice, syncope, maladie connue de l'aorte, geste endovasculaire récent. Le cas publié commence par une syncope." + S(1)),
        P("Asymétrie des pouls et souffle ne sont pas détaillés dans l'extrait radiologique. On les cherche. Le cliché vient avec eux, pas à leur place."),
        P("Syndrome médiastinal plus, souvent, syndrome pleural. L'épanchement du cas était réel." + S(1)),
        P("Le diagnostic positif de dissection est scanographique. Le cliché ne fait que suspecter." + S(1)),
        P("Tomodensitométrie injectée, indispensable dans cette situation, écrit la revue." + S(1)),
        P("Suspicion sur le cliché et le tableau. Confirmation par le scanner. Pas de milligramme dans ce fichier."),
        P("Prise en charge spécialisée, chirurgicale si le type et l'état l'exigent. Aucune dose n'a été relue."),
        P("Ne pas renvoyer un patient syncopal au motif d'une largeur de médiastin. Aucune largeur chiffrée n'est dans la source de 2019." + S(1)),
        P("Pas de consensus métrique. Double contour. Scanner. Épanchement associé possible."),
        P("Piège d'examen : inventer une largeur de médiastin, ou s'arrêter au médiastin et manquer l'épanchement." + S(1)),
    ], dumps + elargi(5, [
        ("rms2019_thorax.txt", 1, 50),
        ("rms2015_dyspnee.txt", 2, 18),
        ("rms2017_echo.txt", 3, 28),
        ("rms2018_radio.txt", 8, 24),
    ]))


def dx6() -> None:
    c = coeur(6, [
        "La valeur du cliché simple, en plus de l'examen, est limitée. En occlusion de haut grade, la triade est pathognomonique : plusieurs niveaux hydro-aériques, anses grêles distendues, absence de gaz dans le côlon." + S(9),
        "La sensibilité globale est d'environ 70 %. La spécificité est qualifiée de basse. Aucun second pourcentage n'est écrit dans la phrase." + S(9),
        "Le cliché ne détecte pas les signes précoces de péritonite ou de strangulation. Il ne donne pas l'anatomie qui distingue les causes." + S(9),
        "Un pneumopéritoine abondant par perforation dans ce contexte se voit mieux sur un thorax debout." + S(9),
        "La tomodensitométrie est l'examen préféré s'il y a un doute, et pour décider d'une chirurgie urgente. Les scanners hélicoïdaux cités ont une exactitude d'environ 90 % pour prédire la strangulation et le besoin d'opérer." + S(9),
        "Anse fermée, ischémie, liquide libre : signes qui poussent à opérer sans délai, sur le scanner, pas sur le cliché simple." + S(9),
        "Le contraste hydrosoluble : s'il n'est pas dans le côlon sur un cliché à 24 heures, l'échec du traitement non opératoire est hautement probable. Les volumes en millilitres ne sont pas recopiés.",
        "Si le diagnostic de bride est déjà sûr et qu'aucun signe n'impose le bloc, le groupe de travail accepte le contraste seul, sans refaire tout le bilan. Ce n'est pas le cas du malade jamais opéré, ni du doute diagnostique.",
        "Aucune dose d'antalgique ni de sonde n'est écrite.",
    ])
    dumps = sources(
        ("w6a", "Bologne 2018", "wses2018_asbo.txt", 9, (), 55, False),
        ("w6b", "Perforation, pour distinguer", "wses2020_ulcere.txt", 10, (), 22, False),
    )
    dx_page(6, [
        P("Occlusion mécanique du grêle par bride, pas tout ventre qui gargouille. " + b("w6-coeur", "approfondir")) + c,
        P("Niveaux multiples, grêle distendu, côlon sans gaz. Cette triade vise le haut grade. Elle n'épuise pas le diagnostic." + S(9)),
        P("Sensibilité du cliché simple d'environ 70 %. Pas de part suisse des brides." + S(9)),
        P("La bride pince l'anse. L'amont se distend, l'air et le liquide font des niveaux. Le côlon, en aval, se vide."),
        P("Douleur, défense, fièvre, lactate qui monte : on ne reste pas sur le cliché. La strangulation précoce ne s'y voit pas." + S(9)),
        P("Chirurgie abdominale ancienne, vomissements, arrêt des gaz et des selles, douleur en coliques. Absence d'antécédent : une autre cause reste possible, et le scanner sert à l'exclure." + S(9)),
        P("Météorisme, tympanisme, orifices herniaires, cicatrices. Le toucher et le silence auscultatoire ne sont pas chiffrés dans l'extrait."),
        P("Syndrome occlusif radiologique. Il ne dit pas « bride » à lui seul. Il dit « occlusion de haut grade » si la triade est là." + S(9)),
        P("Triade pour le haut grade. Scanner si le doute tient, avec une exactitude citée d'environ 90 % pour la strangulation." + S(9)),
        P("Scanner avec contraste hydrosoluble si disponible. Cliché de suivi à 24 heures si l'on a choisi l'épreuve non opératoire." + S(9)),
        P("Clinique de souffrance : chirurgie. Clinique calme et triade : discussion d'une épreuve, avec contrôle à 24 heures. Le détail opératoire n'est pas une dose."),
        P("Pas de milligramme. La sonde et la perfusion se décident selon l'état, sans chiffre inventé."),
        P("Prévenir les brides appartient aux techniques chirurgicales du texte de 2018. On ne les résume pas en un dispositif non relu."),
        P("Triade. 70 %. Pas la strangulation. Scanner si doute. 24 heures pour le contraste."),
        P("Piège : un cliché pauvre autorise le retour. La sensibilité d'environ 70 % dit le contraire pour une partie des occlusions." + S(9)),
    ], dumps + elargi(6, [
        ("rms2018_radio.txt", 8, 36),
        ("rms2019_thorax.txt", 1, 24),
    ]))


def dx7() -> None:
    c = coeur(7, [
        "Douleur abdominale brutale. La péritonite localisée ou généralisée est typique, mais elle n'est présente que chez environ deux tiers des patients dans les séries citées. Un épanchement contenu peut être pauvre à l'examen." + S(10),
        "Le premier examen d'imagerie historique est la radiographie d'abdomen et de thorax, pour l'air libre. Debout et décubitus latéral gauche ont une exactitude semblable. Le décubitus est mieux toléré." + S(10),
        "Le signe est très variable : 30 à 85 % des perforations. Un cliché négatif n'écarte pas la perforation. Plusieurs auteurs en concluent qu'en péritonite claire, le scanner doit être le premier examen." + S(10),
        "Recommandation forte, niveau d'évidence bas : dans l'abdomen aigu suspect d'ulcère perforé, faire un scanner." + S(10),
        "Même grade : thorax et abdomen sans préparation comme bilan initial seulement si le scanner n'est pas disponible aussitôt." + S(10),
        "Sans scanner, dans un hôpital périphérique, l'air libre avec une histoire claire et une péritonite suffit à justifier l'exploration." + S(10),
        "Jusqu'à 12 % des perforations ont un scanner normal dans le texte. Le contraste hydrosoluble, bu ou par la sonde, peut alors aider. Les volumes ne sont pas recopiés.",
        "Recommandation forte : opérer s'il y a un pneumopéritoine important, une fuite de contraste, ou une péritonite." + S(10),
        "Le groupe de 2018 sur l'occlusion rappelle que l'air abondant se cherche surtout sur un thorax debout." + S(9),
        "Aucune dose d'inhibiteur de pompe, d'antibiotique ou d'antalgique n'est écrite. Les schémas du texte source ne sont pas des informations professionnelles suisses.",
    ])
    dumps = sources(
        ("w7a", "Recommandations 2020", "wses2020_ulcere.txt", 10, (), 48, False),
        ("w7b", "Rappel 2018", "wses2018_asbo.txt", 9, (), 28, False),
    )
    dx_page(7, [
        P("Air libre qui peut venir d'un ulcère ouvert, pas un diagnostic posé sur un croissant gazeux isolé. " + b("w7-coeur", "approfondir")) + c,
        P("Air sous le diaphragme sur un cliché debout, ou équivalent en décubitus latéral. Le scanner voit mieux l'air et le siège." + S(10)),
        P("Le signe radiographique manque souvent : fourchette lue 30 à 85 %. Pas de taux suisse." + S(10)),
        P("L'ulcère ouvre la lumière digestive. L'air rejoint le péritoine et monte sous les coupoles quand le patient est debout."),
        P("Défense et douleur brutale : ne pas attendre un cliché négatif pour demander le scanner, s'il est là." + S(10)),
        P("Douleur épigastrique en coup de poignard, ulcère connu, anti-inflammatoire, début très précis. L'examen peut être pauvre si la fuite est colmatée." + S(10)),
        P("Contracture ou défense localisée. Environ un tiers des patients n'ont pas de péritonite franche dans les séries citées." + S(10)),
        P("Syndrome de pneumopéritoine. Il indique une perforation d'organe creux. Il ne nomme pas l'ulcère à lui seul, mais l'ulcère est la cause travaillée dans ce fichier."),
        P("Air libre, histoire compatible, péritonite : exploration justifiable si le scanner manque. Sinon le scanner est recommandé." + S(10)),
        P("Scanner d'abord si disponible. Clichés simples seulement en attente. Contraste hydrosoluble si l'air n'est pas vu et que le doute tient." + S(10)),
        P("Instabilité et péritonite : chirurgie. Le choix de la suture ou du traitement conservateur d'un ulcère bouché n'est pas détaillé au-delà de la recommandation d'opérer quand l'air est important ou que le contraste fuit." + S(10)),
        P("Pas de milligramme suisse dans ce fichier. L'antibioprophylaxie opératoire se lit dans une information professionnelle le jour du geste, pas ici."),
        P("Un ulcère connu se surveille. Cela ne remplace pas l'imagerie si la douleur devient brutale."),
        P("Scanner d'abord. 30 à 85 %. Cliché négatif non rassurant. Péritonite absente chez une partie des patients."),
        P("Piège : renvoyer sur un thorax debout normal. La recommandation de 2020 dit que ce négatif n'exclut pas." + S(10)),
    ], dumps + elargi(7, [
        ("rms2019_thorax.txt", 1, 22),
        ("rms2018_radio.txt", 8, 20),
    ]))


def dx8() -> None:
    c = coeur(8, [
        "Plus de la moitié des traumatismes du poignet vus aux urgences s'associent à une fracture du radius distal. Elle représente deux tiers des fractures de l'avant-bras." + S(6),
        "Mécanisme typique : chute sur la main, poignet en hyperextension. À partir de 60 ans, la femme est la plus concernée, et une chute de sa hauteur peut suffire si l'os est ostéoporotique. Avant cet âge, les hommes et un traumatisme plus violent dominent." + S(6),
        "On lit la face et l'oblique, ou le profil, en suivant la corticale : base, corps, diaphyse, col selon l'os. Trait transverse, oblique ou spiroïde. Simple ou comminutif. Articulaire ou non. Déplacement ou non." + S(6),
        "Le suivi demande au moins deux incidences séparées de 90 degrés, si possible hors plâtre. On compare d'abord le maintien de la réduction, ensuite le cal et la disparition du trait." + S(7),
        "Il n'y a pas de critère radiologique strict de guérison. La corrélation avec la clinique est indispensable. Un cal est de bon augure dans un traitement conservateur diaphysaire. Après ostéosynthèse rigide, il signale une mobilité qui ne devrait plus être là." + S(7),
        "Douleur après blessure, intensité faible à modérée : indication lue du n° 47503, qui cite aussi les douleurs articulaires et ligamentaires. " + C_PA_IND + S(14),
        "Au-dessus de 40 kg, donc au-dessus de 12 ans et chez l'adulte : " + C_PA_DOSE + S(14),
        C_PA + S(14),
        C_PA_CI + S(14),
        "Le produit n'est pas une ostéosynthèse. Il calme la douleur. La réduction et l'immobilisation suivent la stabilité du trait, non chiffrée ici au-delà des sources.",
    ])
    dumps = sources(
        ("w8a", "Revue 2020", "rms2020_main.txt", 6, (), 40, False),
        ("w8b", "Revue 2008, consolidation", "rms2008_cal.txt", 7, (), 40, False),
        ("w8c", "Information professionnelle 47503", "aips_47503.txt", 14, ("4000 mg", "blessures", "hépatique", "1'000 mg"), 10, True),
    )
    dx_page(8, [
        P("Fracture du radius distal, lue sur au moins deux plans. " + b("w8-coeur", "approfondir")) + c,
        P("Rupture de corticale, trait, déplacement, refend articulaire. On ne s'arrête pas au radius : le carpe du même cliché se lit." + S(6)),
        P("Plus de la moitié des traumatismes du poignet aux urgences s'y associent. Deux tiers des fractures de l'avant-bras. Femme à partir de 60 ans." + S(6)),
        P("L'os ostéoporotique cède à faible énergie. L'os jeune cède à plus forte énergie. Le trait peut entrer dans l'articulation."),
        P("Après le contrôle vital, ce n'est pas une urgence de médiastin. C'est une urgence fonctionnelle si le déplacement est gros, la peau ouverte, ou le nerf atteint. Ces signes cliniques ne sont pas chiffrés dans l'extrait."),
        P("Chute sur la paume, hyperextension, âge, ostéoporose, côté. Douleur immédiate." + S(6)),
        P("Déformation en dos de fourchette si elle est classique. Palpation de la tabatière dans le même temps, pour ne pas manquer le scaphoïde." + S(6)),
        P("Syndrome fracturaire du radius distal. Un diastasis du carpe sur le même cliché change de fichier."),
        P("Trait visible, corticale rompue, sur des clichés de face et de profil de qualité. Le déplacement et le caractère articulaire se disent." + S(6)),
        P("Deux incidences à angle droit. Scanner non systématique dans l'extrait du radius. Il est cité pour le scaphoïde instable, dans l'autre fichier." + S(7)),
        P("Réduire si le déplacement l'exige, immobiliser, contrôler la réduction sur deux plans. Antalgie par le n° 47503 si l'indication de douleur faible à modérée est la bonne."),
        P(C_PA_DOSE + " " + C_PA + S(14)),
        P("La solidité ne se décrète pas sur un cal isolé. On revoit le malade." + S(7)),
        P("Deux plans. Femme de plus de 60 ans. Dose plafond 4000 mg. Foie décompensé : contre-indication."),
        P("Piège : un seul cliché, ou un radius lu sans le scaphoïde d'à côté." + S(6)),
    ], dumps + elargi(8, [
        ("rms2018_radio.txt", 8, 36),
    ]))


def dx9() -> None:
    c = coeur(9, [
        "La fracture du carpe concerne environ 10 % des traumatismes de la main et du poignet. Le scaphoïde atteint à lui seul 60 % des fractures des os du carpe." + S(6),
        "Plus de 75 % de sa surface est du cartilage. Il est mobile, et vulnérable en hyperextension. Les jeunes hommes sont les plus touchés dans la revue." + S(6),
        "Sièges : pôle proximal 25 %, moyen 65 %, distal 10 %. La vascularisation va du distal vers le proximal. Le pôle proximal consolide mal et évolue vers la pseudarthrose. Les implications pratiques ajoutent la nécrose et le retard de consolidation." + S(6),
        "Les clichés de Shrek sont toujours demandés si l'on suspecte cet os. Un trait peu déplacé n'est pas traversé par les rayons de la face et du profil standards." + S(6),
        "Première incidence : main à plat, inclinaison ulnaire forcée. Seconde : position d'écriture, rayon perpendiculaire au grand axe." + S(6),
        "Clinique forte : douleur du tubercule, de la tabatière anatomique, signe du piston par traction et pulsion du pouce. Si le trait reste peu visible, l'imagerie par résonance est le recours lu." + S(6),
        "Si le trait est visible mais la stabilité douteuse, déplacement, trait oblique ou plusieurs fragments, le scanner guide la suite." + S(6),
        "L'antalgie de faible à modérée intensité relève du même produit n° 47503 que la fracture du radius, mêmes phrases, même plafond, même foie décompensé. On ne les réécrit pas comme une autre posologie." + S(14),
    ])
    dumps = sources(
        ("w9a", "Revue 2020, scaphoïde", "rms2020_main.txt", 6, (), 42, False),
        ("w9b", "Consolidation", "rms2008_cal.txt", 7, (), 36, False),
    )
    dx_page(9, [
        P("Fracture du scaphoïde, y compris celle que la face et le profil ne montrent pas. " + b("w9-coeur", "approfondir")) + c,
        P("Rupture de la corticale du scaphoïde, ou clinique forte avec trait encore invisible. Les clichés dédiés font partie du diagnostic." + S(6)),
        P("Environ 10 % des traumatismes de la main et du poignet concernent le carpe. Environ 60 % de ces fractures du carpe sont le scaphoïde. Proximal 25 %, moyen 65 %, distal 10 %." + S(6)),
        P("Le cartilage couvre plus des trois quarts de l'os. Les vaisseaux viennent du distal. Le proximal est le plus fragile après la fracture." + S(6)),
        P("Ne pas clore le dossier sur des clichés standards normaux si la tabatière fait mal." + S(6)),
        P("Chute, hyperextension, jeune homme plus souvent. Douleur à la tabatière, au tubercule, piston du pouce." + S(6)),
        P("Palpation précise, puis face, profil et Shrek. Comparer au côté n'est pas une obligation écrite dans l'extrait."),
        P("Syndrome du scaphoïde traumatique. Une luxation associée change de fichier : la luxation trans-scapho-rétrolunaire existe." + S(6)),
        P("Trait vu sur des clichés adaptés, ou suspicion clinique forte qui mène à la résonance. On ne dit pas « pas de fracture » sur une face seule." + S(6)),
        P("Shrek systématiques si l'os est suspect. Résonance si le trait se cache. Scanner si la stabilité est incertaine." + S(6)),
        P("Immobiliser selon le trait et l'avis orthopédique. L'extrait ne donne pas un nombre de semaines. On ne l'invente pas."),
        P("Douleur : n° 47503, mêmes bornes que pour le radius. Plafond 4000 mg par jour. Intervalle de 4 à 8 heures chez l'adulte au-dessus de 40 kg." + S(14)),
        P("Le pôle proximal se surveille plus longtemps dans l'idée, parce que la vascularisation est précaire. La durée exacte n'est pas dans l'extrait." + S(6)),
        P("Shrek. Tabatière. Résonance si doute. 25 % au pôle proximal. Pas de durée de plâtre inventée."),
        P("Piège d'examen : clichés standards rassurants, patient renvoyé sans consigne. Le texte dit que le trait peut être invisible même sur des clichés spécifiques, et que la clinique forte mène à la résonance." + S(6)),
    ], dumps + elargi(9, [
        ("rms2018_radio.txt", 8, 34),
    ]))


def dx10() -> None:
    c = coeur(10, [
        "La luxation périlunaire ne représente que 7 % des traumatismes du carpe. Elle rompt tout contact entre le lunatum et le capitatum, après un choc de haute énergie, poignet en hyperextension et inclinaison cubitale." + S(6),
        "La plus fréquente est la rétrolunaire : le capitatum passe en arrière du lunatum. Elle peut emporter le scaphoïde. On parle alors de luxation trans-scapho-rétrolunaire." + S(6),
        "Environ 25 % de ces luxations périlunaires ne sont pas diagnostiquées au premier passage." + S(6),
        "Face : parfois rupture des lignes de Gilula, lunatum triangulaire. La face peut aussi paraître normale." + S(6),
        "Le profil est l'incidence primordiale. L'alignement radius, lunatum, capitatum et troisième métacarpien est rompu. Le lunatum part en avant ou en arrière. Dans la forme rétrolunaire, le capitatum est en arrière du lunatum." + S(6),
        "Les implications pratiques le disent en une phrase : piège surtout sans profil, la face pouvant sembler normale." + S(6),
        "La réduction est urgente parce que le diagnostic manqué abîme la fonction. Le délai en heures n'est pas chiffré dans l'extrait. On ne l'invente pas.",
        "Antalgie de faible à modérée intensité : n° 47503, sans nouvelle posologie." + S(14),
    ])
    dumps = sources(
        ("w10a", "Revue 2020, luxation", "rms2020_main.txt", 6, (), 42, False),
        ("w10b", "Consolidation et suivi", "rms2008_cal.txt", 7, (), 32, False),
        ("w10c", "Principes de clichés", "rms2018_radio.txt", 8, (), 30, False),
    )
    dx_page(10, [
        P("Luxation rétrolunaire, lue sur le profil. La face peut mentir. " + b("w10-coeur", "approfondir")) + c,
        P("Perte d'alignement entre le radius, le lunatum, le capitatum et le troisième métacarpien. Capitatum en arrière du lunatum dans la forme rétrolunaire." + S(6)),
        P("Sept pour cent des traumatismes du carpe pour la luxation périlunaire. Environ un quart manqué au début. Pas de série suisse séparée." + S(6)),
        P("Haute énergie, hyperextension, inclinaison cubitale. Le capitatum quitte le lunatum. Les ligaments cèdent. Le scaphoïde peut casser en même temps." + S(6)),
        P("C'est une urgence fonctionnelle. Un quart est déjà manqué quand le premier lecteur s'arrête à la face." + S(6)),
        P("Choc violent, poignet déformé ou très douloureux, parfois peu spectaculaire si l'on n'a pas fait le profil. Haute énergie." + S(6)),
        P("Palpation du carpe, état cutané, nerfs et pouls en distal. Puis face et profil, le profil d'abord dans l'esprit." + S(6)),
        P("Syndrome de désaxation du carpe. Lignes de Gilula rompues, lunatum triangulaire, ou face faussement calme." + S(6)),
        P("Le profil fait le diagnostic. La face normale ne l'exclut pas." + S(6)),
        P("Pas d'autre imagerie obligatoire dans l'extrait une fois le profil parlant. Le scanner viendrait des fractures associées, non systématisé ici."),
        P("Réduction spécialisée rapide. Le nombre d'heures n'est pas dans la revue de 2020. On n'en crée pas."),
        P("Douleur : n° 47503 si l'intensité est faible à modérée, avec le plafond de 4000 mg et l'intervalle adulte de 4 à 8 heures." + S(14)),
        P("Connaître l'image évite le quart manqué. Montrer le profil à quelqu'un d'autre si l'on hésite." + S(6)),
        P("Profil obligatoire. 25 % manqués. Gilula. Capitatum postérieur. Pas de délai horaire inventé."),
        P("Piège d'examen, phrase de la revue : la luxation rétrolunaire reste un piège, surtout sans cliché de profil, la face pouvant paraître normale." + S(6)),
    ], dumps)


def main(argv: list[str]) -> None:
    voulu = set(argv[1:] or ["tout"])
    if "tout" in voulu or "A" in voulu:
        phase_a()
    for n in range(1, 11):
        if "tout" in voulu or str(n) in voulu:
            (dx1, dx2, dx3, dx4, dx5, dx6, dx7, dx8, dx9, dx10)[n - 1]()


if __name__ == "__main__":
    main(sys.argv)
