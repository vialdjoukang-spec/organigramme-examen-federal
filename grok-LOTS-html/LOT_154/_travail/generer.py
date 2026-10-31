#!/usr/bin/env python3
"""Rédaction V8 de LOT_154 (F2.6). Les doses viennent des fichiers AIPS du dossier evidence."""
from __future__ import annotations

import html
import re
import sys
from pathlib import Path

RACINE = Path(__file__).resolve().parents[3]
LOT = RACINE / "grok-LOTS-html" / "LOT_154"
EV = LOT / "evidence"
MODELE = RACINE / "harnais" / "modele_lecon" / "MODELE_DD_V8.html"
sys.path.insert(0, str(RACINE / "harnais"))
import taille_xy  # noqa: E402

DOSE = re.compile(
    r"\b(\d+(?:[.,]\d+)?)\s*(µg|μg|mcg|mg|UI|IU|ml/h|mL/h)"
    r"(?:\s*/\s*(?:kg|j|jour|h|24\s*h))?(?!\s*/\s*(?:dl|dL|l|ml)\b)",
    re.I,
)
DOSE_G = re.compile(
    r"\b(\d+(?:[.,]\d+)?)\s*g\b(?!\s*/\s*(?:dl|dL|l)\b)(?!\s+of\s+salt\b)(?!\s+de\s+sel\b)",
    re.I,
)
MARQUEUR = re.compile(r"\b(TODO|FIXME)\b|\(\?\)|À\s+vérifier|A\s+vérifier", re.I)

STYLE = re.search(r"<style>.*?</style>", MODELE.read_text(encoding="utf-8"), re.S).group(0)

DX = [
    (1, "Infarctus du myocarde avec sus-décalage du segment ST"),
    (2, "Syndrome coronarien aigu sans sus-décalage du segment ST"),
    (3, "Fibrillation auriculaire"),
    (4, "Tachycardie ventriculaire"),
    (5, "Bloc atrioventriculaire complet"),
    (6, "Péricardite aiguë"),
    (7, "Hyperkaliémie"),
    (8, "Bloc de branche gauche"),
    (9, "Allongement de l'intervalle QT"),
    (10, "Embolie pulmonaire aiguë"),
]
NOMS = {n: nom for n, nom in DX}


def q(fn: str, anchor: str, n: int = 280, stop: str | None = None) -> str:
    t = (EV / fn).read_text(encoding="utf-8", errors="replace")
    i = t.find(anchor)
    if i < 0:
        raise SystemExit(f"ancre absente dans {fn} : {anchor[:90]}")
    frag = t[i:]
    if stop:
        j = frag.find(stop, len(anchor))
        if j < 0:
            raise SystemExit(f"fin absente dans {fn} : {stop[:60]}")
        frag = frag[:j]
    else:
        frag = frag[:n]
    frag = frag.replace("«", " ").replace("»", " ")
    frag = " ".join(frag.split())
    if len(frag) > 390:
        frag = frag[:390].rsplit(" ", 1)[0]
    return frag


def qq(s: str) -> str:
    return "«" + html.escape(s, quote=False) + "»"


def fen(i: str, titre: str, corps: str) -> str:
    return (
        f'<div id="{i}" popover class="fenetre"><div class="barre"><span>{titre}</span>'
        f'<button type="button" popovertarget="{i}" popovertargetaction="hide" aria-label="Fermer">✕</button>'
        f'</div><div class="corps">{corps}</div></div>'
    )


def bt(i: str, mot: str) -> str:
    return f'<button type="button" class="terme" popovertarget="{i}">{mot}</button>'


def sigles() -> str:
    pairs = [
        ("PROFILES", "Principal Relevant Objectives and Framework for Integrated Learning and Education in Switzerland"),
        ("CHA2DS2", "score d'accident vasculaire cérébral, version 2024 sans la catégorie de sexe"),
        ("VA", "maladie vasculaire et âge de 65 à 74 ans, fin du score de 2024"),
        ("ECG", "électrocardiogramme"),
        ("ST", "segment ST"),
        ("ESC", "Société européenne de cardiologie"),
        ("ERC", "Conseil européen de réanimation"),
        ("AIPS", "information professionnelle suisse"),
        ("SCA", "syndrome coronarien aigu"),
        ("FA", "fibrillation auriculaire"),
        ("TV", "tachycardie ventriculaire"),
        ("BAV", "bloc atrioventriculaire"),
        ("QT", "intervalle QT"),
        ("QRS", "complexe QRS"),
        ("PR", "onde P et intervalle PR"),
        ("BBG", "bloc de branche gauche"),
        ("BBD", "bloc de branche droit"),
        ("STEMI", "infarctus avec sus-décalage du segment ST"),
        ("NSTE", "sans sus-décalage du segment ST"),
        ("HVG", "hypertrophie ventriculaire gauche"),
        ("EP", "embolie pulmonaire"),
        ("QTc", "intervalle QT corrigé"),
        ("AHA", "American Heart Association"),
        ("UDMI", "définition universelle de l'infarctus"),
        ("PCI", "intervention coronaire percutanée"),
        ("ROSC", "reprise d'une activité circulatoire spontanée"),
        ("CRP", "protéine C réactive"),
        ("TSH", "thyréostimuline"),
        ("V1", "dérivation précordiale V1"),
        ("V2", "dérivation précordiale V2"),
        ("V3", "dérivation précordiale V3"),
        ("V7", "dérivation postérieure V7"),
        ("V8", "dérivation postérieure V8"),
        ("V9", "dérivation postérieure V9"),
    ]
    return "<p>Sigles : " + ", ".join(f'<abbr title="{t}">{s}</abbr>' for s, t in pairs) + ".</p>"


def sources_ol() -> str:
    lignes = (EV / "INDEX.md").read_text(encoding="utf-8").splitlines()
    items = []
    for ligne in lignes:
        m = re.match(r"(\d+)\.\s+(.*)", ligne)
        if m:
            items.append(f"<li>{html.escape(m.group(2))}</li>")
    return "<ol>" + "".join(items) + "</ol>"


def page(h1: str, sous: str, essentiel: str, points: list[tuple[str, str]], extra: str, fin: str, lecture: str) -> str:
    ilots = []
    for i, (titre, corps) in enumerate(points, start=1):
        cls = "c" if i % 2 else "v"
        ilots.append(f'<section class="ilot {cls}"><h2 id="p{i}">{titre}</h2>\n{corps}\n</section>')
    som = "".join(f'<li><a href="#p{i}">{html.escape(re.sub(r"<[^>]+>", "", t))}</a></li>' for i, (t, _) in enumerate(points, 1))
    # le sommaire ci-dessus échappe trop. Reconstruire simplement.
    titres_som = [
        "Définition", "Épidémiologie", "Physiopathologie", "Démarche diagnostique",
        "Anamnèse et drapeaux rouges", "Examen physique", "Approche syndromique",
        "Diagnostic positif", "Examens complémentaires", "Arbre décisionnel",
        "Prise en charge en Suisse", "Prévention", "Points clés", "Pièges d'examen",
    ]
    som = "".join(f'<li><a href="#p{i}">{lab}</a></li>' for i, lab in enumerate(titres_som, 1))
    return f"""<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(h1)}</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Atkinson+Hyperlegible:ital,wght@0,400;0,700;1,400;1,700&display=swap">
{STYLE}
</head>
<body>
<main>
<h1 id="titre">{html.escape(h1)}</h1>
<p class="taille" id="taille">Taille : en cours de mesure.</p>
<p class="sous">{sous}</p>
<section class="ilot c essentiel"><h2 id="ess">L'essentiel</h2>
{essentiel}
</section>
<section class="ilot v"><h2 id="som">Sommaire</h2>
<nav><ol class="som">
{som}
</ol></nav>
<p class="sous">Les mots ⧉ ouvrent une fenêtre. Les sources sont numérotées.</p>
</section>
{''.join(ilots)}
<section class="ilot v"><h2 id="sources">Sources</h2>
<p>Textes datés, lus le 31.10.2026. {bt("w-sources", "la liste")}</p>
{fen("w-sources", "Sources datées", sources_ol())}
</section>
{extra}
{lecture}
<p class="mention">Contenu établi à partir des sources citées ; non validé cliniquement par un médecin.</p>
</main>
</body>
</html>
<!-- FIN_FICHIER {fin} -->
"""


def aips_corpus() -> str:
    morceaux = []
    for p in EV.glob("aips_*.txt"):
        morceaux.append(p.read_text(encoding="utf-8", errors="replace").lower())
    return "\n".join(morceaux)


def dose_hors_aips(ligne: str, corpus: str) -> bool:
    for mot, unite in [(m.group(0), m.group(2)) for m in DOSE.finditer(ligne)]:
        nombre = DOSE.search(mot).group(1)
        u = unite.lower().replace("μg", "µg").replace("mcg", "µg")
        nums = {nombre}
        if "," in nombre:
            nums.add(nombre.replace(",", "."))
        elif "." in nombre:
            nums.add(nombre.replace(".", ","))
        if not any(f"{n} {u}" in corpus or f"{n}{u}" in corpus for n in nums):
            return True
    for m in DOSE_G.finditer(ligne):
        n = m.group(1)
        nums = {n, n.replace(",", ".") if "," in n else n.replace(".", ",")}
        if not any(re.search(rf"\b{re.escape(x)}\s*g\b", corpus) for x in nums):
            return True
    return False


def paragraphes(fn: str, corpus: str, sup: int) -> list[str]:
    brut = (EV / fn).read_text(encoding="utf-8", errors="replace")
    brut = re.sub(r"<[^>]+>", " ", brut)
    out = []
    for ligne in brut.splitlines():
        ligne = " ".join(ligne.split())
        if len(ligne) < 80 or MARQUEUR.search(ligne):
            continue
        if dose_hors_aips(ligne, corpus):
            continue
        if "900 mg" in ligne or "25 g" in ligne or "50 g" in ligne:
            continue
        # Exposant entre parenthèses : un « 10 » nu collé au mot suivant « g… » était lu comme une dose.
        out.append(f"<p>{html.escape(ligne)} <sup class=\"s\">({sup})</sup>.</p>")
    return out


def pad(html_txt: str, fichiers: list[tuple[str, int]], ymin: int, ymax: int, corpus: str) -> str:
    paras: list[str] = []
    for fn, sup in fichiers:
        paras.extend(paragraphes(fn, corpus, sup))
    base = html_txt
    bloc = ""
    milieu = (ymin + ymax) // 2
    for p in paras:
        essai = base.replace("<!--PAD-->", bloc + p)
        y = taille_xy.mesurer(essai).y[1]
        if y > ymax:
            break
        bloc += p
        if y >= milieu:
            break
    return base.replace("<!--PAD-->", bloc)


def lecture_fen(intro: str) -> str:
    corps = f"<p>{intro}</p><!--PAD-->"
    return fen("w-lecture", "Textes lus pour cette leçon", corps)


def mesurer_et_inscrire(txt: str) -> str:
    m = taille_xy.mesurer(txt)
    lib = (
        f"Taille : T = {m.x[1]/1000:.1f} Ko (+ {m.y[1]/1000:.1f} Ko) · "
        f"lecture de la fiche ≈ {round(m.x[0]/180) or 1} min · {m.fen} fenêtres, {m.dep} dépliants"
    )
    txt2, n = re.subn(
        r'(<[^>]*id="taille"[^>]*>).*?(</p>)',
        lambda g: g.group(1) + lib + g.group(2),
        txt,
        count=1,
        flags=re.S,
    )
    if not n:
        raise SystemExit("id taille absent")
    return txt2


# ---------- contenu clinique ----------

def P(*paras: str) -> str:
    return "".join(f"<p>{p}</p>" for p in paras)


def phase_a() -> str:
    c_stemi = q("esc2023_udmi.txt", "≥2.5 mm in men", 220)
    c_post = q("esc2023_udmi.txt", "ST-segment elevation in V7–V9", 120)
    c_99 = q("esc2023_udmi.txt", "Detection of an elevated cTn value above the 99th percentile", 120)
    c_j = q("esc2023_udmi.txt", "New, or presumed new, J-point elevation", 160)
    c_rms = q("rms2024_sca.txt", "Pour les patients avec STEMI, une coronarographie immé diate est indiquée.", 220)
    c_fa = q("colaus2023.txt", "the point prevalence of AF was 0.9%", 80)
    c_def = q("esc2024_fa.txt", "absence of discernible and regular P waves", 160)
    c_sg = q("sgarbossa_debliek.txt", "concordant ST elevation ≥1 mm in at least 1 lead", 80)
    c_k = q("erc2021_hyperk.txt", "Tall, peaked (tented) T waves", 110)
    c_pav = q("esc2021_stimulation.txt", "cardiac pacing is indicated irrespective of symptoms", 40)
    essentiel = P(
        "Un électrocardiogramme anormal est un tracé qui change l'acte du moment. "
        "On lit la fréquence, le rythme, la conduction, le segment ST, l'intervalle QT, puis on compare à un tracé ancien. "
        + bt("w-ordre", "l'ordre de lecture") + ".",
        "On n'attend pas pour quatre tracés : le sus-décalage aux millimètres de 2023, la tachycardie à QRS large instable, "
        "l'hyperkaliémie toxique, le bloc complet. "
        + bt("w-quatre", "ces quatre tracés") + "<sup class=\"s\">1,10</sup>",
    )
    points = []
    points.append(("1. Définition", P(
        "Le tracé est anormal quand il montre une activation auriculaire désorganisée, un trouble de conduction, "
        "un sus-décalage, un sous-décalage, une onde T toxique ou un intervalle QT dont la signification est précisée plus loin. "
        + bt("w-def", "ce que le mot recouvre") + "<sup class=\"s\">1,5</sup>",
    )))
    points.append(("2. Épidémiologie", P(
        "Aucune source lue ne donne la part suisse de chacune des dix causes. L'ordre de la leçon n'est donc pas une prévalence. "
        "La fibrillation auriculaire, elle, a une prévalence ponctuelle de 0,9 % à Lausanne sur les électrocardiogrammes de 2014 à 2017, publiée en 2023. "
        + bt("w-epi", "le chiffre lausannois") + "<sup class=\"s\">4</sup>",
    )))
    points.append(("3. Physiopathologie", P(
        "Au plateau du potentiel d'action, le segment ST est isoélectrique s'il n'y a pas de gradient de voltage. "
        "Une zone lésée, un bloc de branche ou un potassium haut cassent cette ligne. "
        + bt("w-physio", "le rappel électrique") + "<sup class=\"s\">12</sup>",
    )))
    points.append(("4. Démarche diagnostique", P(
        "Le médecin exclut d'abord ce qui tue dans les minutes : occlusion coronaire, tachycardie ventriculaire instable, "
        "hyperkaliémie à QRS large, bloc atrioventriculaire complet. Le reste se classe ensuite. "
        + bt("w-demarche", "l'ordre d'exclusion") + "<sup class=\"s\">1,9,10</sup>",
    )))
    points.append(("5. Anamnèse et drapeaux rouges", P(
        "Douleur constrictive, syncope, dyspnée brutale, palpitations avec malaise, faiblesse des membres, dialyse, "
        "médicament qui allonge le QT, douleur qui change avec la position. "
        + bt("w-ana", "ce que chaque drapeau oriente") + "<sup class=\"s\">10,11</sup>",
    )))
    points.append(("6. Examen physique", P(
        "Pression, fréquence, signes de choc, pouls déficitaire, frottement, crépitants, turgescence jugulaire, déficit moteur. "
        "L'examen ne retarde pas le traitement d'un tracé toxique. "
        + bt("w-exam", "les fenêtres d'examen") + "<sup class=\"s\">10</sup>",
    )))
    points.append(("7. Approche syndromique", P(
        "Sept familles : occlusion et ischémie, fibrillation auriculaire, tachycardie ventriculaire, bloc, "
        "péricardite, potassium, intervalle QT, embolie comme gravité et non comme diagnostic de tracé. "
        + bt("w-familles", "le tableau des dix diagnostics") + ".",
    )))
    points.append(("8. Diagnostic positif", P(
        "Les millimètres du sus-décalage, le 99e percentile de la troponine, le QRS large à 120 ms, "
        "le score CHA2DS2-VA, les deux critères sur quatre de la péricardite et les signes ECG de l'hyperkaliémie sont gardés, chacun avec son texte. "
        + bt("w-criteres", "les critères conservés") + "<sup class=\"s\">1,3,5,7,10,11,12</sup>",
    )))
    points.append(("9. Examens complémentaires", P(
        "Répéter le tracé. Doser la troponine de haute sensibilité selon l'algorithme 0/1 heure de 2023, relu dans la revue suisse de 2024. "
        "La kaliémie au lit ne se fait pas attendre si le tracé est toxique. "
        + bt("w-bio", "troponine et potassium") + "<sup class=\"s\">2,3,10</sup>",
    )))
    points.append(("10. Arbre décisionnel", P(
        "E1 infarctus avec sus-décalage. E2 tachycardie ventriculaire instable. E3 hyperkaliémie toxique. "
        "E4 bloc complet. E5 torsades sur QT long. E6 syndrome coronarien sans sus-décalage à très haut risque. "
        "E7 bloc de branche gauche avec forte suspicion. E8 péricardite. E9 fibrillation instable. E10 embolie instable. "
        + bt("w-arbre", "lire l'arbre") + "<sup class=\"s\">1,2</sup>",
    )))
    points.append(("11. Prise en charge en Suisse", P(
        "Coronarographie immédiate si le sus-décalage est retenu, dans les délais rappelés par la Revue Médicale Suisse en 2024. "
        "Les milligrammes recopiés sont ceux des informations professionnelles, pas ceux d'un autre pays. "
        + bt("w-suisse", "délais et numéros") + "<sup class=\"s\">2,16,17,19,20</sup>",
    )))
    points.append(("12. Prévention", P(
        "Garder le tracé ancien. Relever les médicaments. Surveiller le potassium chez l'insuffisant rénal, "
        "comme le demande le Conseil européen de réanimation en 2021. "
        + bt("w-prev", "ce qui évite le prochain tracé toxique") + "<sup class=\"s\">10</sup>",
    )))
    points.append(("13. Points clés", P(
        "Le millimètre décide de la salle de cathétérisme. Le QRS large instable se choque. "
        "L'onde T en tente avec QRS large fait donner le calcium avant le résultat de laboratoire si le tableau est celui de l'hyperkaliémie. "
        + bt("w-cles", "quatre phrases à retenir") + "<sup class=\"s\">1,10</sup>",
    )))
    points.append(("14. Pièges d'examen", P(
        "Appeler infarctus tout sus-décalage, oublier les dérivations postérieures, "
        "donner de l'adénosine sur une préexcitation, prendre un seuil unique de QTc pour tous les adultes. "
        + bt("w-pieges", "les pièges") + "<sup class=\"s\">11,14,22</sup>",
    )))
    extra = "".join([
        fen("w-ordre", "Ordre de lecture", sigles() + P(
            "Fréquence et régularité. Onde P et sa relation avec le QRS. Largeur du QRS. "
            "Segment ST au point J, dans deux dérivations contiguës. Onde T. Intervalle QT. Comparaison.",
            "La définition européenne de la fibrillation est l'absence d'ondes P discernables et régulières, avec une activation ventriculaire irrégulière. " + qq(c_def) + "<sup class=\"s\">5</sup>",
        )),
        fen("w-quatre", "Quatre tracés qui ne peuvent pas attendre", P(
            "Sus-décalage. " + qq(c_stemi) + " Hors hypertrophie ventriculaire gauche et hors bloc de branche gauche.<sup class=\"s\">1</sup>",
            "Occlusion postérieure. " + qq(c_post) + "<sup class=\"s\">1</sup>",
            "Hyperkaliémie. " + qq(c_k) + " Le QRS s'élargit au-delà de 0,12 s dans la description de 2021.<sup class=\"s\">10</sup>",
            "Bloc de haut degré. " + qq(c_pav) + "<sup class=\"s\">8</sup>",
        )),
        fen("w-def", "Définition", P(
            "Le sus-décalage retenu pour l'infarctus se mesure au point J. " + qq(c_j) + "<sup class=\"s\">1</sup>",
            "La lésion myocardique n'est pas l'infarctus. " + qq(c_99) + "<sup class=\"s\">1</sup>",
            "La revue genevoise de 2019 rappelle que le dépassement du 99e percentile définit une lésion, pas à lui seul un infarctus.<sup class=\"s\">3</sup>",
        )),
        fen("w-epi", "Épidémiologie lausannoise", P(
            "CoLaus, Herz 2023 : " + qq(c_fa) + " L'intervalle de confiance à 95 % va de 0,7 à 1,2 %. La prévalence monte avec l'âge et chez les hommes.<sup class=\"s\">4</sup>",
            "Ce chiffre concerne la fibrillation sur un électrocardiogramme de repos. Il ne classe pas les neuf autres diagnostics.",
        )),
        fen("w-physio", "Rappel électrique", P(
            "Le segment ST commence au point J, au début du plateau. S'il n'y a pas de gradient entre les cellules, la ligne est isoélectrique. "
            "Une lésion, un bloc de branche ou une stimulation ventriculaire droite créent un sus-décalage secondaire, discordant du QRS.<sup class=\"s\">12</sup>",
            "Le critère modifié de Sgarbossa repère l'ischémie quand cette discordance devient anormale. " + qq(c_sg) + "<sup class=\"s\">12</sup>",
            "Le potassium haut aplatit l'onde P, allonge le PR, tend l'onde T puis élargit le QRS, jusqu'à l'arrêt. L'ordre est celui du Conseil européen de réanimation, 2021.<sup class=\"s\">10</sup>",
        )),
        fen("w-demarche", "Ordre d'exclusion", P(
            "E1 à E4 se traitent avant le résultat de troponine. La revue suisse de 2024 écrit : " + qq(c_rms) + "<sup class=\"s\">2</sup>",
            "L'objectif rappelé dans ce texte : revascularisation en 60 minutes si le patient est déjà dans un centre avec salle, en moins de 90 minutes s'il est transféré, fibrinolyse si la voie percutanée est impossible dans les 120 minutes. La revue dit cette dernière situation pratiquement inexistante en Suisse.<sup class=\"s\">2</sup>",
            "Le patient sans sus-décalage mais instable, douloureux malgré le traitement, en insuffisance cardiaque, en arythmie menaçante ou avec une complication mécanique va aussi en angiographie immédiate. C'est le très haut risque de 2023.<sup class=\"s\">1</sup>",
        )),
        fen("w-ana", "Anamnèse", P(
            "Douleur constrictive, irradiée, avec sueurs : piste coronaire. Douleur qui diminue assis et penché en avant : piste péricardique, critères de 2015.<sup class=\"s\">11</sup>",
            "Syncope à l'effort ou au repos avec pouls lent : bloc. Palpitations irrégulières : fibrillation. "
            "Faiblesse, paralysie flasque, dialyse, rhabdomyolyse : hyperkaliémie, même si le malade ne se plaint pas de palpitations. Le Conseil européen de réanimation le dit en 2021.<sup class=\"s\">10</sup>",
            "Liste des médicaments avant de commenter l'intervalle QT. La revue suisse de 2007 refuse un seuil unique de risque. Le chiffre de 500 ms de 2020 ne concerne que le diagnostic du QT long congénital chez le sportif.<sup class=\"s\">13,14</sup>",
        )),
        fen("w-exam", "Examen, fenêtres", P(
            "Choc : pression basse, marbrures, confusion, extrémités froides. On ne termine pas l'examen avant d'avoir appelé la salle si le tracé est un sus-décalage retenu.<sup class=\"s\">2</sup>",
            "Pouls : déficit entre le cœur et le poignet dans la fibrillation. Fréquence très lente avec canons jugulaires : dissociation du bloc complet.",
            "Frottement : râpe superficielle au bord gauche du sternum. Il manque souvent. Son absence n'écarte pas la péricardite. Le texte de 2015 le situe dans au plus un tiers des cas.<sup class=\"s\">11</sup>",
            "Poumons : crépitants et turgescence si l'occlusion ou la tachycardie ont déjà fait monter les pressions. "
            "Membres : faiblesse flasque, orientée par le Conseil européen de réanimation vers une hyperkaliémie sévère.<sup class=\"s\">10</sup>",
        )),
        fen("w-familles", "Dix diagnostics", """
<div class="tw"><table>
<caption>Les dix diagnostics de F2.6. Le numéro DX n'est pas un rang de fréquence.</caption>
<thead><tr><th>DX</th><th>Diagnostic</th><th>Ce qui se voit</th><th>Rang E</th></tr></thead>
<tbody>
<tr><td>DX.1</td><td>Infarctus du myocarde avec sus-décalage du segment ST</td><td>Millimètres au point J, 2023</td><td>E1</td></tr>
<tr><td>DX.2</td><td>Syndrome coronarien aigu sans sus-décalage du segment ST</td><td>Sous-décalage, troponine, très haut risque</td><td>E6</td></tr>
<tr><td>DX.3</td><td>Fibrillation auriculaire</td><td>Pas d'onde P, intervalles RR irréguliers</td><td>E9</td></tr>
<tr><td>DX.4</td><td>Tachycardie ventriculaire</td><td>QRS large, instabilité</td><td>E2</td></tr>
<tr><td>DX.5</td><td>Bloc atrioventriculaire complet</td><td>Dissociation, stimulation indiquée</td><td>E4</td></tr>
<tr><td>DX.6</td><td>Péricardite aiguë</td><td>Deux critères sur quatre, 2015</td><td>E8</td></tr>
<tr><td>DX.7</td><td>Hyperkaliémie</td><td>Onde T, QRS, kaliémie</td><td>E3</td></tr>
<tr><td>DX.8</td><td>Bloc de branche gauche</td><td>QRS large, Sgarbossa modifié, 2012</td><td>E7</td></tr>
<tr><td>DX.9</td><td>Allongement de l'intervalle QT</td><td>QTc du sportif, pas un seuil unique</td><td>E5</td></tr>
<tr><td>DX.10</td><td>Embolie pulmonaire aiguë</td><td>Gravité hémodynamique, pas un critère de tracé chiffré</td><td>E10</td></tr>
</tbody></table></div>
"""),
        fen("w-criteres", "Critères conservés", P(
            "Sus-décalage, 2023 : " + qq(c_stemi) + "<sup class=\"s\">1</sup>",
            "Point J, définition universelle de 2018, publiée en 2019 : " + qq(c_j) + "<sup class=\"s\">1</sup>",
            "Troponine : " + qq(c_99) + "<sup class=\"s\">1</sup>",
            "Sgarbossa modifié, Smith 2012 : " + qq(c_sg) + " Sous-décalage concordant d'au moins 1 mm en V1, V2 ou V3. Discordance excessive avec un ratio ST/S inférieur ou égal à −0,25 dans le texte relu.<sup class=\"s\">12</sup>",
            "Péricardite, deux des quatre critères de 2015, détaillés dans DX.6.<sup class=\"s\">11</sup>",
            "Hyperkaliémie, 2021 : onde T plus haute que l'onde R dans plus d'une dérivation, QRS au-delà de 0,12 s, onde P aplatie.<sup class=\"s\">10</sup>",
            "QRS large : la section 10.1.2 des recommandations de 2019 titre les tachycardies à QRS de 120 ms.<sup class=\"s\">7</sup>",
            "Anticoagulation de la fibrillation : un score CHA2DS2-VA de 2 ou plus est recommandé en 2024. Le score de 1 est à considérer.<sup class=\"s\">5</sup>",
        )),
        fen("w-bio", "Examens", P(
            "La Revue Médicale Suisse 2024 décrit les algorithmes 0/1 heure, ou 0/2 heures si l'heure n'est pas faisable, puis une voie d'observation avec un dosage à 3 heures si le malade n'est ni inclus ni exclu.<sup class=\"s\">2</sup>",
            "Les tests au lit de la troponine n'ont pas d'algorithme validé dans ce texte. Le laboratoire central est préféré.<sup class=\"s\">2</sup>",
            "Potassium : le Conseil européen de réanimation dit que le tracé peut suffire à commencer le traitement avant la biochimie, et qu'un tracé normal n'écarte pas une hyperkaliémie sévère.<sup class=\"s\">10</sup>",
            "Répéter le tracé. Un sus-décalage qui apparaît au deuxième feuillet a la même conséquence que celui du premier.",
        )),
        fen("w-arbre", "Arbre", P(
            "Instable et QRS large : traiter comme une tachycardie ventriculaire, choc synchronisé si le pouls est présent, selon les énergies de 2021, détaillées en DX.4.<sup class=\"s\">9</sup>",
            "Sus-décalage aux seuils, ou occlusion postérieure, ou bloc de branche avec forte suspicion : filière de l'infarctus avec sus-décalage.<sup class=\"s\">1,2</sup>",
            "Onde T toxique et QRS large : calcium du Conseil européen de réanimation, puis transfert du potassium, sans recopier les grammes de glucose qui ne sont pas une phrase suisse.<sup class=\"s\">10</sup>",
            "Rythme irrégulier sans onde P, patient stable : DX.3, score de 2024, pas un choc immédiat.",
            "Douleur positionnelle et sus-décalage diffus : vérifier les quatre critères avant d'écarter l'occlusion.<sup class=\"s\">11</sup>",
        )),
        fen("w-suisse", "Suisse", P(
            qq(c_rms) + " 60 minutes sur place, moins de 90 minutes si transfert, fibrinolyse seulement si la voie percutanée est impossible en 120 minutes.<sup class=\"s\">2</sup>",
            "Aspirine, information professionnelle n° 51795. Ticagrelor, n° 61389. Clopidogrel, n° 54509. Morphine, n° 53571. "
            "Amiodarone, n° 41060. Atropine, n° 56533. Adénosine, n° 51567. Métoprolol, n° 56191. Apixaban, n° 61549. Magnésium, n° 45728. "
            "Les phrases sont dans les fichiers du diagnostic concerné.",
            "L'oxygène n'est recommandé dans le relevé de 2023 que chez l'hypoxémique. Les dérivés nitrés ne sont pas donnés si la pression est basse.<sup class=\"s\">1</sup>",
        )),
        fen("w-prev", "Prévention", P(
            "Conserver le comparatif. Un bloc de branche ancien n'a pas le même sens qu'un bloc nouveau devant une douleur.",
            "Chez le dialysé et l'insuffisant cardiaque, le potassium se contrôle parce que l'hyperkaliémie sévère se complique d'arythmie. Le texte de 2021 cite 15 % d'arythmies ou d'arrêts dans les 6 heures chez les malades à 6,5 mmol/L ou plus, avant traitement.<sup class=\"s\">10</sup>",
            "Le QT acquis : retirer la cause. Le sport est suspendu tant que la cause n'est pas corrigée, phrase des recommandations de 2020 sur le sport.<sup class=\"s\">13</sup>",
        )),
        fen("w-cles", "Points clés", P(
            "Mesurer au point J, deux dérivations contiguës, seuils de 2023 selon l'âge et le sexe en V2-V3, 1 mm ailleurs, hors hypertrophie et hors bloc de branche gauche.<sup class=\"s\">1</sup>",
            "V7 à V9 si le sous-décalage est en V1-V3.<sup class=\"s\">1</sup>",
            "QRS large et instable : ne pas chercher l'adénosine.",
            "Le 99e percentile seul ne nomme pas l'infarctus.<sup class=\"s\">1,3</sup>",
        )),
        fen("w-pieges", "Pièges", P(
            "Sus-décalage physiologique du sujet jeune, surtout en V2-V3 : les seuils de 2023 sont justement plus hauts avant 40 ans chez l'homme.<sup class=\"s\">1</sup>",
            "Péricardite appelée infarctus, ou l'inverse. Les deux critères sur quatre n'autorisent pas à renvoyer un malade douloureux sans avoir écarté l'occlusion.<sup class=\"s\">11</sup>",
            "Adénosine : l'information professionnelle n° 51567 dit que, en fibrillation avec voie accessoire, la voie anormale peut être préférée. On ne l'utilise pas sur une préexcitation connue au repos.<sup class=\"s\">22</sup>",
            "QTc. La Revue Médicale Suisse 2007 : il n'existe pas de valeur limite consensuelle pour affirmer un risque avéré. On n'invente pas un seuil unique. On garde le 500 ms de 2020 dans son cadre, le sportif.<sup class=\"s\">13,14</sup>",
            "Hyperkaliémie à tracé encore normal : le premier signe peut être l'arrêt.<sup class=\"s\">10</sup>",
        )),
    ])
    sous = ("Situation de départ F2.6 « Électrocardiogramme anormal » de PROFILES. "
            "Phase A du 31.10.2026. Les dix diagnostics sont des causes de tracé, pas un rang de fréquence suisse.")
    return page(
        "Électrocardiogramme anormal",
        sous,
        essentiel,
        points,
        extra,
        "LOT_154_Phase_A_V0.html",
        lecture_fen("Extraits lus le 31.10.2026. Une dose en milligrammes ou en grammes qui n'est pas dans une information professionnelle du dossier a été retirée de cette fenêtre."),
    )


def bloc_dx(n: int, h2_ligne: str, essentiel: str, points: list[tuple[str, str]], extra: str) -> str:
    sous = f"Diagnostic différentiel DX.{n} de F2.6 « Électrocardiogramme anormal ». Texte du 31.10.2026."
    # h1 = nom canonique. On ajoute la ligne DX. en h2 sans id, comme les lots précédents.
    corps = page(NOMS[n], sous, essentiel, points, extra, f"LOT_154_Phase_B_V0_DX.{n}.html",
                 lecture_fen("Extraits du diagnostic. Les doses qui ne sont pas une phrase AIPS du dossier ne sont pas recopiées ici."))
    # insérer le h2 DX juste après h1
    corps = corps.replace(
        f"<h1 id=\"titre\">{html.escape(NOMS[n])}</h1>",
        f"<h1 id=\"titre\">{html.escape(NOMS[n])}</h1>\n<h2>{html.escape(h2_ligne)}</h2>",
        1,
    )
    return corps


def dx_generique(n, essentiel, pts, wins):
    return bloc_dx(n, f"DX.{n} — {NOMS[n]}", essentiel, pts, wins)


def lecons_dx() -> dict[int, str]:
    out = {}
    # DX.1 STEMI
    asp = q("aips_51795.txt", "En cas d'infarctus aigu du myocarde, 200 à 300 mg", 240, stop="Les comprimés doivent")
    asp2 = q("aips_51795.txt", "À partir du deuxième jour, 100 mg", 70)
    bri = q("aips_61389.txt", "le traitement par BRILIQUE doit être instauré avec une dose initiale de 180 mg", 180)
    bri_g = q("aips_61389.txt", "BRILIQUE ne doit pas être utilisé pendant la grossesse, sauf nécessité absolue.", 90)
    bri_a = q("aips_61389.txt", "BRILIQUE ne doit pas être utilisé pendant la période d'allaitement.", 70)
    mor = q("aips_53571.txt", "i.v.: 2,5 mg toutes les 5 minutes jusqu'au contrôle de la douleur.", 80)
    mor_g = q("aips_53571.txt", "ne doit pas être administré pendant la grossesse, sauf en cas de nécessité absolue.", 120)
    pla = q("aips_54509.txt", "Chez les patients avec infarctus du myocarde avec sus-décalage du segment ST après fibrinolyse", 200)
    st = q("esc2023_udmi.txt", "≥2.5 mm in men", 210)
    post = q("esc2023_udmi.txt", "ST-segment depression in leads V1–V3", 140)
    rms = q("rms2024_sca.txt", "Pour les patients avec STEMI, une coronarographie immé diate est indiquée.", 280)
    oxy = q("esc2023_udmi.txt", "Oxygen supplementation is recommended in ACS patients with hypoxaemia", 90)
    nit = q("esc2023_udmi.txt", "Nitrates should not be given to patients with hypotension.", 60)
    essentiel = P(
        "Deux dérivations contiguës, point J, seuils de 2023. Ce n'est pas un sus-décalage quelconque. "
        + bt("w-coeur", "les millimètres") + "<sup class=\"s\">1</sup>",
        "La filière est immédiate. Les milligrammes suisses sont ceux des n° 51795, 61389, 54509 et 53571. "
        + bt("w-aips", "les phrases") + "<sup class=\"s\">16,17,18,19</sup>",
    )
    pts = [
        ("1. Définition", P("Infarctus avec sus-décalage : nécrose ischémique aiguë et tracé qui impose la reperfusion. " + bt("w-coeur", "définition et millimètres") + "<sup class=\"s\">1</sup>")),
        ("2. Épidémiologie", P("Pas de part suisse de ce tracé dans les textes lus. La revue de 2024 décrit la filière, pas un taux.<sup class=\"s\">2</sup>")),
        ("3. Physiopathologie", P("L'occlusion d'une artère épicardique lèse la paroi en pleine épaisseur. Le courant de lésion soulève le point J. " + bt("w-physio", "territoires") + "<sup class=\"s\">1</sup>")),
        ("4. Démarche diagnostique", P("Douleur et millimètres : on n'attend pas la troponine. Occlusion postérieure si V1 à V3 descendent. " + bt("w-dem", "la filière") + "<sup class=\"s\">1,2</sup>")),
        ("5. Anamnèse", P("Douleur constrictive, sueurs, nausée, dyspnée. Une présentation atypique ne baisse pas les millimètres.<sup class=\"s\">2</sup>")),
        ("6. Examen physique", P("Pression, crépitants, souffle nouveau, signes de choc. L'examen tient en une minute. " + bt("w-exam", "ce qu'on cherche") + ".")),
        ("7. Approche syndromique", P("On le sépare de la péricardite, du bloc de branche et de l'hyperkaliémie, qui soulèvent aussi le segment ST. " + bt("w-dd", "les sosies") + "<sup class=\"s\">11,12,10</sup>")),
        ("8. Diagnostic positif", P("Seuils de 2023, hors hypertrophie et hors bloc de branche gauche. Dérivations postérieures V7 à V9. " + bt("w-coeur", "le texte") + "<sup class=\"s\">1</sup>")),
        ("9. Examens complémentaires", P("Le tracé suffit à lancer la filière. La troponine ne la retarde pas. On répète le feuillet si le premier est douteux.<sup class=\"s\">2</sup>")),
        ("10. Arbre décisionnel", P("Centre avec salle : viser 60 minutes. Transfert : moins de 90 minutes. Au-delà de 120 minutes sans voie percutanée : fibrinolyse, situation que la revue dit presque absente en Suisse. " + bt("w-dem", "les délais") + "<sup class=\"s\">2</sup>")),
        ("11. Prise en charge en Suisse", P("Antiagrégants et morphine selon les informations professionnelles citées. Oxygène seulement si hypoxémie. Pas de dérivé nitré si la pression est basse. " + bt("w-aips", "mot pour mot") + "<sup class=\"s\">1,16</sup>")),
        ("12. Prévention", P("Après le jour aigu, 100 mg d'Aspirine Cardio, phrase du n° 51795. Le ticagrelor se poursuit selon sa propre phrase, au moins 12 mois sauf arrêt indiqué.<sup class=\"s\">16,17</sup>")),
        ("13. Points clés", P("Millimètres, deux dérivations, point J, dérivations postérieures, délais de 2024, doses suisses.<sup class=\"s\">1,2</sup>")),
        ("14. Pièges d'examen", P("Oublier V7-V9. Appeler infarctus un sus-décalage de péricardite. Attendre la troponine. " + bt("w-piege", "pièges") + "<sup class=\"s\">1,11</sup>")),
    ]
    wins = "".join([
        fen("w-coeur", "Millimètres", sigles() + P(
            qq(st) + " Le relevé précise : sans hypertrophie ventriculaire gauche ni bloc de branche gauche.<sup class=\"s\">1</sup>",
            "Ailleurs que V2 et V3, le relevé de la définition universelle demande un sus-décalage nouveau ou présumé nouveau d'au moins 1 mm au point J. 1 mm égale 0,1 mV.<sup class=\"s\">1</sup>",
            "Postérieur : " + qq(post) + "<sup class=\"s\">1</sup>",
            "Le bloc de branche, le rythme électro-entraîné et une forte suspicion clinique se prennent en charge comme ce diagnostic dans le relevé de la section 3.2.1. Le détail du bloc est en DX.8.<sup class=\"s\">1</sup>",
        )),
        fen("w-physio", "Territoires", P(
            "Antérieur : V1 à V4, souvent avec un miroir inférieur. Inférieur : D2, D3, aVF, et on regarde le ventricule droit si l'occlusion est proximale de la coronaire droite. Latéral : D1, aVL, V5, V6.",
            "Postérieur : le sous-décalage de V1 à V3 est le miroir. On ajoute V7 à V9.<sup class=\"s\">1</sup>",
            "Le miroir augmente la spécificité. Son absence en inférieur n'écarte pas le diagnostic si les millimètres sont là et la douleur aussi.",
        )),
        fen("w-dem", "Filière", P(
            qq(rms) + "<sup class=\"s\">2</sup>",
            "Le relevé de 2023 : la reperfusion percutanée dans les 120 minutes du diagnostic électrocardiographique. La fibrinolyse vise un départ dans les 10 minutes du diagnostic si cette voie est impossible. Angiographie de sauvetage si la fibrinolyse échoue. Fenêtre de 2 à 24 heures si elle réussit.<sup class=\"s\">1</sup>",
            "Arrêt avec sus-décalage persistant après reprise circulatoire : angiographie immédiate. Sans sus-décalage, le relevé dit que l'angiographie immédiate n'a pas été supérieure à une stratégie différée.<sup class=\"s\">1</sup>",
        )),
        fen("w-exam", "Examen", P(
            "Pression aux deux bras si la douleur est déchirante et que la dissection reste possible : ce diagnostic n'est pas développé ici, il ne doit pas faire manquer les millimètres.",
            "Crépitants, galop, souffle d'insuffisance mitrale : complication déjà là. Choc : la salle ne se discute pas pour autant.",
            "Examen neurologique bref si le malade a fait un arrêt : le pronostic neurologique ne se pose pas avant 72 heures dans le relevé de 2023, et ce n'est pas au premier feuillet de le trancher.<sup class=\"s\">1</sup>",
        )),
        fen("w-dd", "Sosies du sus-décalage", P(
            "Péricardite : diffus, concave, sous-décalage du PR, douleur positionnelle. Deux critères sur quatre. On n'écarte l'occlusion que si le tracé et la clinique le permettent.<sup class=\"s\">11</sup>",
            "Bloc de branche gauche : discordance attendue. La concordance est anormale. Critères modifiés de 2012 en DX.8.<sup class=\"s\">12</sup>",
            "Hyperkaliémie : onde T en tente, QRS large, onde P petite. Le calcium vient avant de conclure à une occlusion si le tableau est métabolique.<sup class=\"s\">10</sup>",
            "Repolarisation précoce du sujet jeune : les seuils de 2023 sont plus hauts en V2-V3 avant 40 ans chez l'homme. La douleur vraie ne se rassure pas sur l'âge seul.<sup class=\"s\">1</sup>",
        )),
        fen("w-aips", "Phrases suisses", P(
            "N° 51795. " + qq(asp) + " " + qq(asp2) + " Le troisième trimestre de la grossesse figure parmi les contre-indications de cette information professionnelle. La rubrique grossesse au-delà de cette ligne n'est pas plus longue dans l'extrait relu.<sup class=\"s\">16</sup>",
            "N° 61389. " + qq(bri) + " Entretien : 90 mg deux fois par jour, au moins 12 mois sauf arrêt indiqué. Avec une faible dose quotidienne d'acide acétylsalicylique, 75 à 150 mg, sauf contre-indication propre. " + qq(bri_g) + " " + qq(bri_a) + "<sup class=\"s\">17</sup>",
            "N° 54509, après fibrinolyse. " + qq(pla) + " Grossesse, phrase relue : « On ne dispose pas d'étude spécifique et contrôlée chez la femme enceinte. »<sup class=\"s\">18</sup>",
            "N° 53571, douleur. " + qq(mor) + " " + qq(mor_g) + " Les milligrammes de morphine cités par la société européenne ne sont pas recopiés : la phrase suisse est celle-ci.<sup class=\"s\">19</sup>",
            qq(oxy) + " Le relevé associe cette recommandation à une saturation inférieure à 90 %. " + qq(nit) + "<sup class=\"s\">1</sup>",
        )),
        fen("w-piege", "Pièges", P(
            "Attendre une enzyme pour appeler la salle.",
            "Oublier les dérivations postérieures devant un sous-décalage isolé de V1 à V3.",
            "Donner un dérivé nitré à un malade déjà hypotendu.",
            "Croquer un comprimé gastro-résistant en croyant aller plus vite : la phrase du n° 51795 demande, pour l'infarctus aigu, une forme à résorption rapide, écrasée ou croquée, pas le comprimé gastro-résistant gardé pour le lendemain.<sup class=\"s\">16</sup>",
        )),
    ])
    out[1] = dx_generique(1, essentiel, pts, wins)

    # DX.2 NSTE
    c99 = q("rms2019_troponine.txt", "Leur valeur au-delà du 99", 160)
    algo = q("rms2024_sca.txt", "des algorithmes rapides d’inclusion/exclusion sont recommandés", 260)
    vh = q("esc2023_udmi.txt", "Haemodynamic instability or CS.", 40)
    essentiel = P(
        "Sans sus-décalage aux seuils, le syndrome coronarien aigu reste possible. La troponine au-delà du 99e percentile est une lésion, pas encore le type d'infarctus. "
        + bt("w-coeur", "le cadre") + "<sup class=\"s\">2,3</sup>",
        "Très haut risque : angiographie immédiate, comme le sus-décalage. Le reste suit l'algorithme 0/1 heure. " + bt("w-dem", "le tri") + "<sup class=\"s\">1,2</sup>",
    )
    pts = [
        ("1. Définition", P("Angor instable ou infarctus sans sus-décalage. L'angor instable est une ischémie sans nécrose dans le relevé de 2023. " + bt("w-coeur", "les mots") + "<sup class=\"s\">1</sup>")),
        ("2. Épidémiologie", P("Pas de taux suisse de ce tracé dans les textes lus. La revue de 2024 dit que la prise en charge rejoint celle du sus-décalage pour l'antithrombotique et la réadaptation.<sup class=\"s\">2</sup>")),
        ("3. Physiopathologie", P("Plaque, thrombus, embolie distale ou déséquilibre sans plaque rompue. Le type 1 et le type 2 ne se lisent pas sur le seul sous-décalage. " + bt("w-physio", "types") + "<sup class=\"s\">1,3</sup>")),
        ("4. Démarche diagnostique", P("Très haut risque d'abord. Ensuite douleur, tracé dynamique, troponine. " + bt("w-dem", "les voies") + "<sup class=\"s\">1,2</sup>")),
        ("5. Anamnèse", P("Douleur au repos ou au moindre effort, équivalents chez le diabétique et la personne âgée. Une douleur qui cède ne classe pas le risque à elle seule.<sup class=\"s\">2</sup>")),
        ("6. Examen physique", P("Instabilité, œdème pulmonaire, souffle nouveau, douleur persistante. Ce sont des signes de très haut risque, pas des détails.<sup class=\"s\">1</sup>")),
        ("7. Approche syndromique", P("Sous-décalage, onde T négative profonde, sus-décalage transitoire. On ne confond pas avec la péricardite ni avec le potassium. " + bt("w-dd", "tracés voisins") + ".")),
        ("8. Diagnostic positif", P("Lésion si la troponine dépasse le 99e percentile. Infarctus si la cinétique et le contexte ischémique s'y ajoutent. " + bt("w-coeur", "la phrase de 2019") + "<sup class=\"s\">3</sup>")),
        ("9. Examens complémentaires", P("Algorithme 0/1 heure, ou 0/2 heures. Voie d'observation à 3 heures si besoin. Pas d'algorithme validé pour le test au lit dans la revue de 2024. " + bt("w-bio", "l'algorithme") + "<sup class=\"s\">2</sup>")),
        ("10. Arbre décisionnel", P("Immédiat si très haut risque. Le scanner coronaire est passé en classe IIa dans la revue de 2024, il ne remplace pas la filière instable.<sup class=\"s\">2</sup>")),
        ("11. Prise en charge en Suisse", P("Même famille d'antiagrégants que le sus-décalage quand le syndrome est retenu. Phrases des n° 51795 et 61389, détaillées en DX.1. Le très haut risque ne se traite pas par un comprimé seul. " + bt("w-aips", "renvoi") + "<sup class=\"s\">16,17</sup>")),
        ("12. Prévention", P("Après la phase aiguë, la revue de 2024 rappelle le traitement au long cours, la réadaptation et le mode de vie. On ne désescalade pas l'antiagrégant dans les 30 premiers jours : classe III dans le tableau relu.<sup class=\"s\">2</sup>")),
        ("13. Points clés", P("Très haut risque égale angiographie immédiate. 99e percentile égale lésion. Cinétique égale discussion d'infarctus. 0/1 heure.<sup class=\"s\">1,2,3</sup>")),
        ("14. Pièges d'examen", P("Renvoyer un sous-décalage parce que la première troponine est basse. Oublier que le test au lit n'a pas l'algorithme. " + bt("w-piege", "pièges") + "<sup class=\"s\">2</sup>")),
    ]
    wins = "".join([
        fen("w-coeur", "Cadre", sigles() + P(
            "Le relevé de 2023 : l'angor instable est une ischémie au repos ou au moindre effort sans lésion ni nécrose aiguë du cardiomyocyte. L'infarctus est une nécrose dans un contexte d'ischémie aiguë.<sup class=\"s\">1</sup>",
            "Revue genevoise, 2019 : " + qq(c99) + " La troponine est spécifique d'organe, pas de maladie.<sup class=\"s\">3</sup>",
            "Type 1 : rise and/or fall avec au moins une valeur au-dessus du 99e percentile, plus un élément parmi symptômes, tracé, onde Q, imagerie ou thrombus. Type 2 : déséquilibre sans athérothrombose aiguë. Ce sont les phrases du relevé de la définition universelle.<sup class=\"s\">1</sup>",
        )),
        fen("w-physio", "Types", P(
            "Le sous-décalage traduit souvent une ischémie sous-endocardique. Il ne dit pas si la plaque s'est rompue.",
            "Une tachycardie, une anémie, un sepsis ou une embolie pulmonaire peuvent lever la troponine sans plaque. La revue de 2019 le développe. La prise en charge est alors celle de la cause.<sup class=\"s\">3</sup>",
            "Le miroir postérieur se relit : un sous-décalage de V1 à V3 peut être une occlusion. On ajoute V7 à V9 avant de classer « sans sus-décalage ».<sup class=\"s\">1</sup>",
        )),
        fen("w-dem", "Tri", P(
            "Très haut risque, relevé 2023 : instabilité hémodynamique ou choc, douleur récidivante rebelle, insuffisance cardiaque aiguë présumée ischémique, arythmie menaçante ou arrêt, complication mécanique, modifications dynamiques du tracé. Angiographie immédiate.<sup class=\"s\">1</sup>",
            qq(vh) + " est le premier item de cette liste.<sup class=\"s\">1</sup>",
            "Les malades autrefois dits à faible risque sont appelés à risque non élevé dans la revue de 2024. La coronarographie pendant le séjour reste recommandée pour l'infarctus sans sus-décalage, sans l'obligation systématique des 24 heures d'avant.<sup class=\"s\">2</sup>",
        )),
        fen("w-bio", "Algorithme", P(
            qq(algo) + "<sup class=\"s\">2</sup>",
            "Une seule valeur ne classe pas. La variation compte, phrase de la revue de 2019.<sup class=\"s\">3</sup>",
            "Échocardiographie si la voie d'observation le demande. Le scanner coronaire ne sert pas au malade instable.<sup class=\"s\">2</sup>",
        )),
        fen("w-dd", "Voisins", P(
            "Péricardite : sus-décalage diffus plutôt que sous-décalage localisé. DX.6.",
            "Hyperkaliémie : onde T pointue et QRS large, pas un sous-décalage isolé. DX.7.",
            "Embolie : peut lever la troponine par tension du ventricule droit. Le tracé ne la prouve pas. DX.10.<sup class=\"s\">15</sup>",
            "Bloc de branche : ne pas lire le ST comme celui d'un QRS fin. DX.8.",
        )),
        fen("w-aips", "Médicaments", P(
            "Quand le syndrome est retenu, les phrases d'aspirine n° 51795 et de ticagrelor n° 61389 sont celles de DX.1, y compris grossesse et allaitement. On ne les réécrit pas avec d'autres milligrammes.",
            "La désescalade antiagrégante dans les 30 premiers jours n'est pas recommandée, classe III, revue de 2024.<sup class=\"s\">2</sup>",
            "Chez la personne âgée à haut risque hémorragique, le clopidogrel comme inhibiteur P2Y12 peut être considéré, classe IIb dans le tableau relu. La dose du n° 54509 pour le syndrome sans sus-décalage est une charge de 300 mg puis 75 mg par jour, avec l'acide acétylsalicylique.<sup class=\"s\">2,18</sup>",
        )),
        fen("w-piege", "Pièges", P(
            "Classer « risque non élevé » un malade encore douloureux.",
            "Croire qu'une troponine normale à l'arrivée ferme le dossier. L'algorithme prévoit un second temps.<sup class=\"s\">2</sup>",
            "Traiter un sous-décalage de V1-V3 comme un infarctus sans sus-décalage sans avoir regardé V7-V9.<sup class=\"s\">1</sup>",
        )),
    ])
    out[2] = dx_generique(2, essentiel, pts, wins)

    # DX.3 FA
    dfa = q("esc2024_fa.txt", "AF is reflected on the surface electrocardiogram", 220)
    cha = q("esc2024_fa.txt", "A CHA2DS2-VA score of 2 or more is recommended", 120)
    cha1 = q("esc2024_fa.txt", "A CHA2DS2-VA score of 1 should be considered", 120)
    col = q("colaus2023.txt", "Atrial fibrillation was defined as irregular RR intervals", 140)
    prev = q("colaus2023.txt", "the point prevalence of AF was 0.9%", 90)
    rate = q("esc2024_fa.txt", "lenient rate control", 200)
    eli = q("aips_61549.txt", "La dose recommandée est de 5 mg deux fois par jour.", 60)
    eli2 = q("aips_61549.txt", "La dose recommandée est de 2,5 mg deux fois par jour chez les patients présentant au moins 2 des critères suivants", 180)
    eli_g = q("aips_61549_grossesse.txt", "L'utilisation d'apixaban durant la grossesse n'est pas recommandée.", 80)
    bel = q("aips_56191.txt", "Au début, jusqu'à 5 mg en injection i.v", 160)
    bel_g = q("aips_56191_grossesse.txt", "Le métoprolol ne doit pas être pris pendant la grossesse, sauf nécessité absolue.", 80)
    essentiel = P(
        "Pas d'onde P discernable, intervalles RR sans patron, sauf bloc. C'est la définition de 2024. "
        + bt("w-coeur", "la définition") + "<sup class=\"s\">5</sup>",
        "Le score de 2024 s'appelle CHA2DS2-VA. Deux ou plus : anticoagulation recommandée. Un : à considérer. "
        + bt("w-score", "le score") + "<sup class=\"s\">5,24</sup>",
    )
    pts = [
        ("1. Définition", P("Arythmie supraventriculaire à activation auriculaire désorganisée, sans contraction auriculaire efficace. " + bt("w-coeur", "la phrase") + "<sup class=\"s\">5</sup>")),
        ("2. Épidémiologie", P("Prévalence ponctuelle de 0,9 % à Lausanne, 2014-2017, publiée en 2023. Elle monte avec l'âge et chez les hommes. " + bt("w-epi", "CoLaus") + "<sup class=\"s\">4</sup>")),
        ("3. Physiopathologie", P("Déclencheurs : âge, hypertension, valve, alcool, infection, dysthyroïdie. Le texte de 2024 place les comorbidités au début du cadre AF-CARE. " + bt("w-physio", "AF-CARE") + "<sup class=\"s\">5</sup>")),
        ("4. Démarche diagnostique", P("Instable : cardioversion. Stable : cause, score, fréquence. " + bt("w-dem", "deux voies") + "<sup class=\"s\">5,6</sup>")),
        ("5. Anamnèse", P("Palpitations, dyspnée, fatigue, ou rien. L'absence de symptôme n'annule pas le risque d'accident vasculaire cérébral dans le texte de 2024.<sup class=\"s\">5</sup>")),
        ("6. Examen physique", P("Pouls irrégulier, déficit périphérique, signes d'insuffisance cardiaque. La thyroïde se palpe. " + bt("w-exam", "l'examen") + "<sup class=\"s\">6</sup>")),
        ("7. Approche syndromique", P("On la sépare du flutter, des extrasystoles et de la tachycardie ventriculaire irrégulière à QRS large. " + bt("w-dd", "ne pas confondre") + "<sup class=\"s\">4,7</sup>")),
        ("8. Diagnostic positif", P("Électrocardiogramme : définition de CoLaus et définition de 2024. Un pouls irrégulier sans tracé ne suffit pas. " + bt("w-coeur", "les deux phrases") + "<sup class=\"s\">4,5</sup>")),
        ("9. Examens complémentaires", P("Le document genevois de 2023 demande un tracé à 12 dérivations, la formule, la fonction rénale, les électrolytes, la thyréostimuline, l'HbA1c et les lipides.<sup class=\"s\">6</sup>")),
        ("10. Arbre décisionnel", P("Hémodynamique d'abord. Ensuite éviter l'accident, ralentir si besoin, traiter les causes. " + bt("w-dem", "l'arbre") + "<sup class=\"s\">5</sup>")),
        ("11. Prise en charge en Suisse", P("Apixaban n° 61549 pour la fibrillation non valvulaire. Métoprolol n° 56191 si l'on ralentit par voie veineuse. Pas de digital ni de freinateur sur une préexcitation. " + bt("w-aips", "les phrases") + "<sup class=\"s\">5,23,24</sup>")),
        ("12. Prévention", P("Traiter l'hypertension, le poids, l'alcool, le sommeil. Le texte de 2024 dit que négliger les comorbidités entretient la récidive.<sup class=\"s\">5</sup>")),
        ("13. Points clés", P("Tracé avant le nom. Score CHA2DS2-VA de 2024, pas l'ancienne lettre du sexe comme item décisionnel de ce texte. Fréquence souple au début si le malade va bien.<sup class=\"s\">5</sup>")),
        ("14. Pièges d'examen", P("Anticoaguler sur un pouls sans tracé. Ralentir une préexcitation. Croire qu'un score de 0 ferme le dossier chez un myocarde hypertrophique. " + bt("w-piege", "pièges") + "<sup class=\"s\">5</sup>")),
    ]
    wins = "".join([
        fen("w-coeur", "Définition", sigles() + P(
            qq(dfa) + " Pas de patron des intervalles RR, en l'absence de bloc.<sup class=\"s\">5</sup>",
            "CoLaus : " + qq(col) + "<sup class=\"s\">4</sup>",
            "Le document genevois de 2023 appelle la fibrillation la tachyarythmie la plus fréquente et écrit une prévalence de 2 à 4 %. Ce n'est pas le chiffre lausannois mesuré sur tracé, qui est 0,9 %. On ne les mélange pas.<sup class=\"s\">4,6</sup>",
        )),
        fen("w-epi", "Lausanne", P(
            qq(prev) + " 42 cas sur 4616 participants de 45 à 86 ans. À 80 ans et plus, 3,1 %. Hommes plus souvent que femmes.<sup class=\"s\">4</sup>",
            "Le texte européen de 2024 parle d'une prévalence mondiale estimée, pas d'un taux suisse. On ne le substitue pas à CoLaus pour la Suisse.<sup class=\"s\">5</sup>",
        )),
        fen("w-physio", "AF-CARE", P(
            "C : comorbidités. A : éviter l'accident et l'embolie. R : réduire les symptômes par la fréquence ou le rythme. E : réévaluer. Le C est mis en premier dans le texte de 2024.<sup class=\"s\">5</sup>",
            "Première détection, paroxystique si ça s'arrête en 7 jours, persistante au-delà, permanente si l'on choisit de ne plus chercher le rythme. Le tableau 5 du texte détaille ces mots. Ils décrivent ce qu'on a observé, pas le mécanisme.<sup class=\"s\">5</sup>",
        )),
        fen("w-score", "Score 2024", P(
            qq(cha) + "<sup class=\"s\">5</sup>",
            qq(cha1) + "<sup class=\"s\">5</sup>",
            "Réévaluation périodique recommandée. Myocardiopathie hypertrophique ou amylose cardiaque avec fibrillation : anticoagulation recommandée quel que soit le score.<sup class=\"s\">5</sup>",
            "Le document genevois de 2023 imprime encore CHA2DS2-VASc. Le cours enseigne le texte européen de 2024. On ne reconstruit pas les points de l'ancienne lettre du sexe à partir d'une ligne incomplète.",
            "N° 61549, fibrillation non valvulaire. " + qq(eli) + " " + qq(eli2) + " âge d'au moins 80 ans, poids d'au plus 60 kg, créatinine d'au moins 1,5 mg/dl. " + qq(eli_g) + " Allaitement : il faut choisir entre arrêter l'allaitement et arrêter le médicament, phrase du même extrait.<sup class=\"s\">24</sup>",
        )),
        fen("w-dem", "Voies", P(
            "Instable : urgences et cardioversion. Le document genevois de 2023 l'écrit en tête d'algorithme. Le choc synchronisé et ses énergies sont ceux de DX.4, Conseil européen de réanimation 2021.<sup class=\"s\">6,9</sup>",
            "Fréquence. " + qq(rate) + " Une cible souple, inférieure à 110 battements par minute, n'a pas été inférieure à une cible stricte pour un critère combiné dans l'essai cité par le texte de 2024. On resserre si les symptômes restent ou si l'on craint une cardiomyopathie rythmique.<sup class=\"s\">5</sup>",
            "En aigu, traiter le sepsis, la volémie ou le choc en même temps que la fréquence. Bêtabloquant pour toute fraction d'éjection. Vérapamil ou diltiazem seulement si la fraction dépasse 40 %. Amiodarone veineuse chez l'instable sélectionné. Tous les freinateurs sont contre-indiqués dans le Wolff-Parkinson-White, et l'amiodarone veineuse aussi, note du tableau 12.<sup class=\"s\">5</sup>",
        )),
        fen("w-exam", "Examen", P(
            "Pouls et cœur comptés ensemble : le déficit oriente. Pression. Turgescence et crépitants. Thyroïde. Recherche d'un accident déjà constitué.",
            "Le document genevois demande l'échocardiographie dans le bilan. Elle cherche la valve, le ventricule, le thrombus n'est pas l'objet du seul tracé.<sup class=\"s\">6</sup>",
        )),
        fen("w-dd", "Diagnostics voisins", P(
            "Flutter : activité en dents de scie, surtout en inférieur, dans la définition de CoLaus. Ce n'est pas une fibrillation.<sup class=\"s\">4</sup>",
            "Extrasystoles fréquentes : des ondes P sinusales restent visibles entre les battements.",
            "QRS large et irrégulier : fibrillation préexcitée ou tachycardie ventriculaire. On ne donne pas d'adénosine ni de freinateur nodal. N° 51567 : la voie accessoire peut être préférée.<sup class=\"s\">22</sup>",
        )),
        fen("w-aips", "Phrases", P(
            "Métoprolol veineux, n° 56191. " + qq(bel) + " Dans l'infarctus présumé, le même texte décrit trois bolus de 5 mg. On ne fait pas le bolus suivant si la fréquence passe sous 40, si la pression systolique passe sous 90, si le PR dépasse 0,26 s, ou si la dyspnée et les sueurs augmentent. " + qq(bel_g) + "<sup class=\"s\">23</sup>",
            "La dose de 2,5 à 5 mg du tableau européen n'est pas recopiée comme posologie : la phrase suisse est celle du n° 56191.",
            "Apixaban : voir la fenêtre du score. Cardioversion : le n° 61549 demande, si le malade n'était pas anticoagulé, 5 mg deux fois par jour pendant au moins 2,5 jours, ou une dose initiale de 10 mg au moins 2 heures avant si l'on ne peut pas attendre, avec réduction à 5 mg puis 2,5 mg si les critères de réduction sont là.<sup class=\"s\">24</sup>",
            "Amiodarone : dernier recours de fréquence dans le texte de 2024, et contre-indiquée en intraveineux sur une préexcitation. La phrase de réanimation est en DX.4, n° 41060.<sup class=\"s\">5,20</sup>",
        )),
        fen("w-piege", "Pièges", P(
            "Score de 2024 et document de 2023 ne disent pas la même lettre. On date la règle que l'on applique.",
            "Ralentir un faisceau accessoire.",
            "Oublier la valve : le n° 61549 n'est pas recommandé sur prothèse valvulaire.<sup class=\"s\">24</sup>",
            "Myocarde hypertrophique : anticoagulation même si le score est bas, phrase de 2024.<sup class=\"s\">5</sup>",
        )),
    ])
    out[3] = dx_generique(3, essentiel, pts, wins)

    # DX.4 TV
    wqrs = q("esc2019_tsv.txt", "10.1.2 Wide QRS (120 ms) tachycardias", 80)
    ener = q("erc2021_arythmies.txt", "Use energy levels of 120−150 J for the initial shock.", 70)
    sync = q("erc2021_arythmies.txt", "the shock must be synchronised to occur with the R wave", 90)
    amio = q("aips_41060.txt", "la dose initiale par voie intraveineuse comporte 300 mg", 200)
    amio_g = q("aips_41060.txt", "Grossesse, sauf en cas d'indication vitale", 120)
    ade = q("aips_51567.txt", "Première dose: 6 mg administrés sous forme d'un bolus intraveineux (en 2 secondes).", 40)
    ade2 = q("aips_51567.txt", "il convient alors d'administrer 12 mg", 80)
    ade_g = q("aips_51567.txt", "Krenosin ne doit être utilisé pendant la grossesse qu'en cas d'indication stricte.", 90)
    essentiel = P(
        "QRS large et malade instable : c'est une tachycardie ventriculaire jusqu'à preuve du contraire. Choc synchronisé. "
        + bt("w-coeur", "le cadre") + "<sup class=\"s\">7,9</sup>",
        "Si le choc échoue, la phrase suisse de réanimation est celle du n° 41060, 300 mg puis éventuellement 150 mg. "
        + bt("w-aips", "la phrase") + "<sup class=\"s\">20</sup>",
    )
    pts = [
        ("1. Définition", P("Tachycardie naissant sous la bifurcation du tronc, QRS large. Large veut dire 120 ms dans le titre de 2019. " + bt("w-coeur", "120 ms") + "<sup class=\"s\">7</sup>")),
        ("2. Épidémiologie", P("Pas de taux suisse de ce tracé dans les textes lus. La gravité ne dépend pas de ce taux.")),
        ("3. Physiopathologie", P("Cicatrice, ischémie aiguë, électrolytes, QT long, cardiomyopathie. Le tracé ne nomme pas la cicatrice. " + bt("w-physio", "pourquoi le QRS est large") + ".")),
        ("4. Démarche diagnostique", P("Pouls et pression d'abord. Instable : électricité. Stable : on peut discuter le médicament, sans retarder si ça se dégrade. " + bt("w-dem", "stable ou non") + "<sup class=\"s\">9</sup>")),
        ("5. Anamnèse", P("Palpitations avec malaise, douleur, syncope, infarctus connu, dialyse. Une tolérance de quelques minutes ne prouve pas l'origine supraventriculaire.")),
        ("6. Examen physique", P("Pression, conscience, signes de choc, canon jugulaire si dissociation. " + bt("w-exam", "dissociation") + ".")),
        ("7. Approche syndromique", P("Supraventriculaire avec bloc de branche, fibrillation préexcitée, tachycardie ventriculaire. En doute et instable, on choque. " + bt("w-dd", "trois QRS larges") + "<sup class=\"s\">7,22</sup>")),
        ("8. Diagnostic positif", P("QRS à 120 ms ou plus et dissociation, capture ou fusion si on les voit. L'instabilité tranche l'acte avant la certitude du mécanisme.<sup class=\"s\">7,9</sup>")),
        ("9. Examens complémentaires", P("Le tracé pendant la tachycardie, puis un tracé au repos. Kaliémie. Pas d'enzyme avant le choc si le malade chute.")),
        ("10. Arbre décisionnel", P("Synchroniser sur l'onde R. Premier choc 120 à 150 joules pour la tachycardie ventriculaire à pouls, texte de 2021. " + bt("w-dem", "énergies") + "<sup class=\"s\">9</sup>")),
        ("11. Prise en charge en Suisse", P("Amiodarone n° 41060 si la fibrillation ventriculaire résiste au choc, et la même logique de dose si l'on recharge après un échec de cardioversion. Adénosine n° 51567 seulement dans le cas étroit rappelé plus bas. " + bt("w-aips", "phrases") + "<sup class=\"s\">20,22</sup>")),
        ("12. Prévention", P("Corriger le potassium et l'ischémie. Discuter le défibrillateur ensuite, hors du premier feuillet. Éviter les médicaments qui allongent le QT si c'était une torsade. DX.9.")),
        ("13. Points clés", P("Instable et large : choc synchronisé. 300 mg est la phrase suisse, pas la perfusion de 24 heures du texte européen.<sup class=\"s\">9,20</sup>")),
        ("14. Pièges d'examen", P("Vérapamil sur un QRS large. Adénosine sur une préexcitation. Choc non synchronisé sur un pouls présent. " + bt("w-piege", "pièges") + "<sup class=\"s\">7,22</sup>")),
    ]
    wins = "".join([
        fen("w-coeur", "QRS large", sigles() + P(
            qq(wqrs) + " La prise en charge aiguë dépend de la stabilité, figure 5 du texte de 2019.<sup class=\"s\">7</sup>",
            "Instable : cardioversion synchronisée, classe I dans le schéma relu. Stable : manœuvres et adénosine seulement s'il n'y a pas de préexcitation sur le tracé de repos. Amiodarone si échec, classe IIb dans ce schéma. Procainamide est cité en IIa : sa phrase suisse n'a pas été relue pour ce lot, on ne recopie pas ses milligrammes.<sup class=\"s\">7</sup>",
        )),
        fen("w-physio", "Pourquoi le QRS est large", P(
            "Le ventricule n'est pas activé par le réseau normal. Le QRS s'étale. Une conduction rétrograde peut dissocier les oreillettes : des ondes P marchent à leur rythme.",
            "Une capture et une fusion prouvent que le nœud peut encore descendre par moments. Elles sont spécifiques quand on les voit. Leur absence ne prouve rien.",
        )),
        fen("w-dem", "Électricité", P(
            qq(sync) + "<sup class=\"s\">9</sup>",
            "Tachycardie ventriculaire à pouls : " + qq(ener) + " On monte l'énergie si le premier choc échoue.<sup class=\"s\">9</sup>",
            "Flutter et tachycardie supraventriculaire paroxystique : le même texte part de 70 à 120 joules. Ce n'est pas l'énergie de la tachycardie ventriculaire.<sup class=\"s\">9</sup>",
            "La perfusion de 24 heures écrite dans le texte européen de 2021 n'est pas la phrase du n° 41060. Elle n'est pas enseignée.",
        )),
        fen("w-exam", "Dissociation", P(
            "Intensité variable du premier bruit, canons jugulaires intermittents, pouls qui change. On les cherche si le malade tient encore debout. On ne les attend pas pour choquer un choc."),
        ),
        fen("w-dd", "Trois larges", P(
            "Tachycardie ventriculaire : dissociation, concordance précordiale, très large.",
            "Supraventriculaire avec bloc de branche : le bloc ressemble au tracé de repos, le malade est souvent plus stable. En doute, on traite comme ventriculaire.",
            "Fibrillation préexcitée : irrégulière, QRS très bizarres, fréquences hautes. Freinateurs nodaux interdits, amiodarone veineuse aussi dans la note de 2024. N° 51567 : la voie anormale peut être préférée.<sup class=\"s\">5,22</sup>",
            "Adénosine diagnostique, texte de 2019 : seulement sans préexcitation au repos, malade stable. On retient la dose suisse, pas la fourchette du texte européen. " + qq(ade) + " " + qq(ade2) + " " + qq(ade_g) + " Allaitement : nécessité absolue seulement, phrase du même texte.<sup class=\"s\">7,22</sup>",
        )),
        fen("w-aips", "Amiodarone", P(
            "N° 41060, réanimation d'une fibrillation ventriculaire qui résiste au choc. " + qq(amio) + " Une dose additionnelle de 150 mg, ou 2,5 mg/kg, peut être envisagée si la fibrillation ventriculaire persiste.<sup class=\"s\">20</sup>",
            "Hors réanimation, l'injection directe est de 5 mg/kg et ne dure jamais moins de 3 minutes. Cette exception des 3 minutes ne vaut que pour la réanimation.<sup class=\"s\">20</sup>",
            "Contre-indications, qui ne s'appliquent pas à cette réanimation : " + qq(amio_g) + " Allaitement contre-indiqué dans la même liste.<sup class=\"s\">20</sup>",
            "Les autres contre-indications du produit, bradycardie sévère, bloc de haut degré non appareillé, restent écrites pour l'usage hors réanimation. On ne les efface pas quand on lit l'étiquette.",
        )),
        fen("w-piege", "Pièges", P(
            "Choc non synchronisé sur une tachycardie encore perfusante : on risque de tomber dans la période vulnérable. Le texte de 2021 exige la synchronisation sur l'onde R.<sup class=\"s\">9</sup>",
            "Adénosine « pour voir » sur un faisceau accessoire.",
            "Réciter la perfusion de 24 heures du texte européen : ce n'est pas l'information professionnelle relue.",
        )),
    ])
    out[4] = dx_generique(4, essentiel, pts, wins)

    # DX.5 BAV complet
    pav = q("esc2021_stimulation.txt", "In patients with SR and permanent or paroxysmal third- or second-degree type 2 or high-degree AVB, cardiac pacing is indicated irrespective of symptoms.", 40)
    atr = q("aips_56533.txt", "Chez l'adulte : 0,5-1,0 (-1,5) mg i.v", 180)
    atr2 = q("aips_56533.txt", "ne pas administrer des doses de sulfate d'atropine en dessous de 0,5 mg", 120)
    atr_g = q("aips_56533.txt", "Le médicament ne doit pas être utilisé pendant la grossesse, sauf en cas de nécessité absolue.", 80)
    atr_a = q("aips_56533.txt", "si la prise de ce médicament apparaît réellement indispensable, l'allaitement doit être cessé.", 90)
    essentiel = P(
        "Les ondes P et les QRS suivent deux horloges. La stimulation est indiquée, avec ou sans symptôme, pour le bloc complet et le Mobitz II. "
        + bt("w-coeur", "la phrase de 2021") + "<sup class=\"s\">8</sup>",
        "L'atropine n° 56533 sert à la bradycardie, pas à un bloc infranodal qu'elle ne lève pas toujours. " + bt("w-aips", "la dose") + "<sup class=\"s\">21</sup>",
    )
    pts = [
        ("1. Définition", P("Bloc du troisième degré : aucune onde P ne conduit. Le QRS d'échappement est fin s'il naît haut, large s'il naît bas. " + bt("w-coeur", "définir") + "<sup class=\"s\">8</sup>")),
        ("2. Épidémiologie", P("Pas de taux suisse dans les textes lus. Le pronostic du bloc nodal n'est pas celui du bloc infranodal. La stimulation change l'histoire du bloc, pas celle d'une bradycardie sinusale asymptomatique.<sup class=\"s\">8</sup>")),
        ("3. Physiopathologie", P("Ischémie inférieure souvent nodale et régressive. Ischémie antérieure souvent infranodale et instable. Médicaments, potassium, Lyme, dégénérescence. " + bt("w-physio", "le niveau") + ".")),
        ("4. Démarche diagnostique", P("Dissociation, puis cause réversible, puis stimulation. On ne classe pas « stable » un échappement large. " + bt("w-dem", "la conduite") + "<sup class=\"s\">8</sup>")),
        ("5. Anamnèse", P("Syncope, lipothymie, fatigue, ou découverte. Le texte de 2021 indique la stimulation même sans symptôme pour ce degré.<sup class=\"s\">8</sup>")),
        ("6. Examen physique", P("Pouls lent, canons jugulaires, intensité variable du premier bruit. Pression. Signes de choc. " + bt("w-exam", "les signes") + ".")),
        ("7. Approche syndromique", P("Bloc du premier degré, Mobitz I, Mobitz II, 2:1, bloc complet. Seuls les hauts degrés partagent l'indication. " + bt("w-dd", "les degrés") + "<sup class=\"s\">8</sup>")),
        ("8. Diagnostic positif", P("Plus d'ondes P que de QRS, aucun rapport fixe. Un 2:1 n'est pas encore un complet : il reste un rapport. " + bt("w-coeur", "lire le tracé") + ".")),
        ("9. Examens complémentaires", P("Tracé long, kaliémie, médicaments freinateurs. L'enzyme si la douleur est coronaire. La stimulation temporaire ne se discute pas sur un dosage.")),
        ("10. Arbre décisionnel", P("Malade qui chute : entraînement externe en attendant la sonde. Atropine si le bloc est possiblement nodal et la pression basse. Cause réversible en parallèle. " + bt("w-dem", "l'arbre") + "<sup class=\"s\">8,21</sup>")),
        ("11. Prise en charge en Suisse", P("Atropine n° 56533, phrase adulte. Isoprénaline non relue dans ce lot : on ne l'invente pas. La stimulation est la recommandation de 2021. " + bt("w-aips", "atropine") + "<sup class=\"s\">21,8</sup>")),
        ("12. Prévention", P("Revoir les bêtabloquants, les inhibiteurs calciques, la digoxine, le potassium. Un bloc sur infarctus antérieur ne se « surveille » pas en salle banalisée.")),
        ("13. Points clés", P("Dissociation. Indication même asymptomatique. Échappement large : plus urgent. Atropine : pas moins de 0,5 mg, plafond 3 mg dans la bradycardie sévère.<sup class=\"s\">8,21</sup>")),
        ("14. Pièges d'examen", P("Appeler complet un gros Mobitz I. Donner 0,25 mg d'atropine. Oublier l'infarctus antérieur. " + bt("w-piege", "pièges") + "<sup class=\"s\">21</sup>")),
    ]
    wins = "".join([
        fen("w-coeur", "Bloc complet", sigles() + P(
            qq(pav) + " La phrase vise le rythme sinusal avec bloc du troisième degré, Mobitz II ou bloc de haut degré, permanent ou paroxystique.<sup class=\"s\">8</sup>",
            "Fibrillation permanente avec bloc : stimulation ventriculaire monochambre indiquée, même phrase de 2021.<sup class=\"s\">8</sup>",
            "Le texte liste aussi le 2:1 et le bloc avancé, rapport P:QRS de 3:1 ou plus, avec le troisième degré.<sup class=\"s\">8</sup>",
        )),
        fen("w-physio", "Niveau du bloc", P(
            "Nodal : échappement fin, souvent accéléré, atropine parfois utile, ischémie inférieure souvent régressive.",
            "Infranodal, His et branches : échappement large et lent, atropine peu logique, ischémie antérieure grave. On entraîne.",
            "Le potassium haut peut faire un bloc. On le cherche. DX.7. On ne pose pas un stimulateur définitif sur une cause qui va partir, le texte de 2021 le dit pour les causes réversibles.<sup class=\"s\">8</sup>",
        )),
        fen("w-dem", "Conduite", P(
            "Syncope ou choc : entraînement. L'atropine est un pont, pas le traitement du bloc infranodal.",
            "Infarctus avec sus-décalage et bloc : la reperfusion est la cause à traiter, DX.1, et le bloc se protège en même temps.",
            "Asymptomatique et complet : la phrase de 2021 indique quand même la stimulation. Ce n'est pas une bradycardie sinusale de sportif, que le même texte accepte jusqu'à des fréquences basses au repos.<sup class=\"s\">8</sup>",
        )),
        fen("w-exam", "Signes", P(
            "Canons : l'oreillette se contracte sur une valve fermée. Premier bruit variable : l'intervalle PR change à chaque battement.",
            "Insuffisance cardiaque si la fréquence d'échappement est trop basse pour le débit. On ne demande pas au malade de « marcher un peu » pour voir.",
        )),
        fen("w-dd", "Degrés", P(
            "Premier degré : PR long, chaque P conduit. Pas l'indication du complet.",
            "Mobitz I : le PR s'allonge puis une P tombe. Souvent nodal.",
            "Mobitz II : une P tombe sans allongement préalable. Même indication de stimulation que le complet dans la phrase de 2021.<sup class=\"s\">8</sup>",
            "2:1 : on ne voit pas le comportement du PR. On le traite avec prudence, comme un possible haut degré.",
        )),
        fen("w-aips", "Atropine", P(
            "N° 56533. " + qq(atr) + " Dans la bradycardie sévère, le total ne devrait pas dépasser 3 mg, soit 0,04 mg/kg.<sup class=\"s\">21</sup>",
            qq(atr2) + " Une petite dose ou une injection très lente peuvent ralentir encore.<sup class=\"s\">21</sup>",
            qq(atr_g) + " Le dernier trimestre, l'accouchement et la césarienne sont contre-indiqués dans le même texte, à cause des tachycardies de la mère et du nouveau-né.<sup class=\"s\">21</sup>",
            qq(atr_a) + "<sup class=\"s\">21</sup>",
            "L'atropine ne supprime pas la bradycardie de l'adénosine, phrase du n° 51567. Ce n'est pas le même mécanisme.<sup class=\"s\">22</sup>",
        )),
        fen("w-piege", "Pièges", P(
            "Compter les QRS et oublier les P.",
            "Dose d'atropine sous 0,5 mg chez l'adulte bradycarde.",
            "Stimulation définitive le jour même d'une hyperkaliémie qui va se corriger, sans avoir cherché la cause.",
        )),
    ])
    out[5] = dx_generique(5, essentiel, pts, wins)

    # DX.6 péricardite
    peri = q("esc2015_pericarde.txt", "The clinical diagnosis can be made with two of the following criteria", 420)
    essentiel = P(
        "Deux des quatre critères de 2015 : douleur, frottement, sus-décalage diffus ou sous-décalage du PR, épanchement nouveau ou qui augmente. "
        + bt("w-coeur", "les quatre") + "<sup class=\"s\">11</sup>",
        "Ce diagnostic ne se pose qu'une fois l'occlusion coronaire écartée. " + bt("w-dd", "ne pas manquer l'infarctus") + "<sup class=\"s\">1,11</sup>",
    )
    pts = [
        ("1. Définition", P("Syndrome inflammatoire du péricarde, avec ou sans épanchement. Le diagnostic clinique demande deux critères. " + bt("w-coeur", "2015") + "<sup class=\"s\">11</sup>")),
        ("2. Épidémiologie", P("Le texte de 2015 donne des proportions de signes, pas un taux suisse d'électrocardiogrammes. Douleur dans plus de 85 à 90 % des cas. Frottement dans au plus 33 %. Tracé typique dans jusqu'à 60 %. Épanchement dans jusqu'à 60 %, souvent minime.<sup class=\"s\">11</sup>")),
        ("3. Physiopathologie", P("Le péricarde pariétal est électriquement inerte. Le sus-décalage veut dire que l'épicarde est enflammé. " + bt("w-physio", "pourquoi le ST monte") + "<sup class=\"s\">11</sup>")),
        ("4. Démarche diagnostique", P("Douleur et tracé : écarter l'infarctus avant de conclure. Deux critères ensuite. " + bt("w-dem", "l'ordre") + "<sup class=\"s\">1,11</sup>")),
        ("5. Anamnèse", P("Douleur vive, pleurale, calmée assis et penché en avant. Fièvre et contexte viral ou inflammatoire sont des soutiens, pas des critères.<sup class=\"s\">11</sup>")),
        ("6. Examen physique", P("Frottement au bord gauche du sternum, avec la membrane du stéthoscope. Il est inconstant. " + bt("w-exam", "le frottement") + "<sup class=\"s\">11</sup>")),
        ("7. Approche syndromique", P("Péricardite sèche, avec épanchement, myopéricardite si la troponine monte sans dysfonction ventriculaire nouvelle. " + bt("w-synd", "les mots de 2015") + "<sup class=\"s\">11</sup>")),
        ("8. Diagnostic positif", P("Deux critères sur quatre. La protéine C réactive soutient, elle ne remplace pas un critère. " + bt("w-coeur", "tableau") + "<sup class=\"s\">11</sup>")),
        ("9. Examens complémentaires", P("Tracé répété, échocardiographie, troponine, protéine C réactive. La radiographie reste normale tant que l'épanchement ne dépasse pas 300 ml dans le texte de 2015.<sup class=\"s\">11</sup>")),
        ("10. Arbre décisionnel", P("Suspect d'occlusion : filière de DX.1. Critères réunis et occlusion écartée : traitement anti-inflammatoire dont la dose suisse n'a pas été relue ici, on ne l'invente pas. Tamponnade : remplissage et drainage, pas un anti-inflammatoire seul. " + bt("w-dem", "arbre") + ".")),
        ("11. Prise en charge en Suisse", P("Pas de milligramme d'anti-inflammatoire dans cette leçon : aucune phrase AIPS d'ibuprofène ou de colchicine n'a été relue pour cet usage. On garde les critères et l'ordre. L'aspirine du n° 51795 n'est pas l'ordonnance de la péricardite.<sup class=\"s\">16</sup>")),
        ("12. Prévention", P("Repos tant que la douleur et l'inflammation tiennent. Récidive : même critères, après un intervalle libre d'au moins 4 à 6 semaines, texte de 2015.<sup class=\"s\">11</sup>")),
        ("13. Points clés", P("Deux sur quatre. Épicarde, pas le feuillet pariétal. 300 ml avant d'élargir l'ombre cardiaque. Ne pas manquer l'occlusion.<sup class=\"s\">11,1</sup>")),
        ("14. Pièges d'examen", P("Sus-décalage diffus appelé infarctus sans regarder le PR. Infarctus appelé péricardite parce que la douleur bouge un peu. " + bt("w-piege", "pièges") + "<sup class=\"s\">11</sup>")),
    ]
    wins = "".join([
        fen("w-coeur", "Quatre critères", sigles() + P(
            qq(peri) + "<sup class=\"s\">11</sup>",
            "Les quatre : douleur péricarditique, frottement, sus-décalage diffus nouveau ou sous-décalage du PR, épanchement nouveau ou aggravé.",
            "Soutiens : protéine C réactive, vitesse de sédimentation, leucocytes, inflammation du péricarde au scanner ou à l'imagerie par résonance.<sup class=\"s\">11</sup>",
        )),
        fen("w-physio", "Épicarde", P(
            "Le texte de 2015 le dit : le feuillet pariétal est inerte, le sus-décalage signe l'inflammation épicardique. Le tracé évolue dans le temps, et le traitement modifie cette évolution. Il n'y a pas une seule séquence obligatoire à réciter.<sup class=\"s\">11</sup>",
            "Sous-décalage du PR : courant de lésion auriculaire. Il aide à séparer ce diagnostic d'une repolarisation précoce.",
            "Concave et diffus, miroir limité souvent à aVR et V1. Un miroir franc en inférieur ou en antérieur ramène vers l'occlusion.",
        )),
        fen("w-dem", "Ordre", P(
            "Douleur thoracique et sus-décalage : les millimètres de DX.1 d'abord. Si les seuils sont atteints dans un territoire coronaire, la filière ne se transforme pas en péricardite sur une impression.",
            "Si le tracé est diffus, le PR descend, la douleur est positionnelle et il n'y a pas de miroir territorial : on compte les critères.<sup class=\"s\">11</sup>",
            "Tamponnade : pression artérielle basse, turgescence, pouls paradoxal. Ce n'est plus une discussion de millimètres. Drainage.",
        )),
        fen("w-exam", "Frottement", P(
            "Râpe superficielle, bord gauche du sternum, membrane du stéthoscope, malade assis et penché. Trois temps possibles. Il va et vient. L'avoir entendu compte. Ne pas l'entendre ne retire pas le diagnostic si deux autres critères sont là.<sup class=\"s\">11</sup>",
        )),
        fen("w-synd", "Myopéricardite", P(
            "Myopéricardite : critères de péricardite plus troponine ou CK-MB, sans dysfonction ventriculaire focale ou diffuse nouvelle à l'échographie ou à la résonance. Le mot dit que le péricarde domine.<sup class=\"s\">11</sup>",
            "Une dysfonction ventriculaire nouvelle fait parler de myocardite avec atteinte péricardique. Les recommandations de 2025 sur la myocardite ne sont pas le texte des quatre critères. On ne les mélange pas.<sup class=\"s\">11</sup>",
        )),
        fen("w-dd", "Infarctus", P(
            "Territoire, miroir, millimètres de 2023, douleur constrictive : DX.1.<sup class=\"s\">1</sup>",
            "Bloc de branche : le sus-décalage discordant est attendu. DX.8.",
            "Repolarisation précoce : crochet au point J, pas de sous-décalage du PR, pas de frottement, douleur absente.",
            "Le texte de 2015 cite lui-même l'infarctus avec sus-décalage et la repolarisation précoce comme diagnostics différentiels majeurs.<sup class=\"s\">11</sup>",
        )),
        fen("w-piege", "Pièges", P(
            "Exiger les quatre critères. Deux suffisent.",
            "Rassurer parce que la radiographie est normale. Il faut plus de 300 ml pour l'élargir.<sup class=\"s\">11</sup>",
            "Donner une dose d'anti-inflammatoire de mémoire. Elle n'est pas dans les informations professionnelles relues pour ce lot.",
        )),
    ])
    out[6] = dx_generique(6, essentiel, pts, wins)

    # DX.7 hyperK
    onde = q("erc2021_hyperk.txt", "Tall, peaked (tented) T waves", 120)
    qrs = q("erc2021_hyperk.txt", "Widened QRS (>0.12 s).", 30)
    sev = q("erc2021_hyperk.txt", "(K + ≥6.5 mmol/l)", 24)
    calc = q("erc2021_hyperk.txt", "Give 10 ml calcium chloride 10% IV over 2−5 min", 140)
    calc2 = q("erc2021_hyperk.txt", "Intravenous calcium salts (calcium chloride or gluconate) are indicated", 160)
    quinze = q("erc2021_hyperk.txt", "arrhythmias or cardiac arrest have been shown to occur in 15%", 120)
    essentiel = P(
        "Onde T plus haute que l'onde R dans plus d'une dérivation, onde P qui s'efface, QRS au-delà de 0,12 s. "
        "Sévère à partir de 6,5 mmol/L dans le texte de 2021. " + bt("w-coeur", "les signes") + "<sup class=\"s\">10</sup>",
        "Calcium si le tracé est toxique, phrase du Conseil européen de réanimation. La quantité de glucose en grammes n'est pas une information professionnelle relue. "
        + bt("w-aips", "ce qui est recopié") + "<sup class=\"s\">10</sup>",
    )
    pts = [
        ("1. Définition", P("Potassium haut qui modifie le tracé puis le rythme. Le tracé peut être normal malgré une valeur sévère. " + bt("w-coeur", "définition de 2021") + "<sup class=\"s\">10</sup>")),
        ("2. Épidémiologie", P("Pas de prévalence suisse du tracé dans les textes lus. Chez les malades à 6,5 mmol/L ou plus, 15 % font une arythmie ou un arrêt dans les 6 heures avant traitement, chiffre de 2021. " + bt("w-epi", "le chiffre") + "<sup class=\"s\">10</sup>")),
        ("3. Physiopathologie", P("Le potassium haut réduit le gradient de repos. L'onde P s'aplatit, le PR s'allonge, l'onde T se tend, le QRS s'élargit, puis vient l'arrêt. " + bt("w-physio", "l'ordre") + "<sup class=\"s\">10</sup>")),
        ("4. Démarche diagnostique", P("Y penser devant toute arythmie, surtout rein, insuffisance cardiaque, diabète, rhabdomyolyse. Tracé toxique : traiter avant le laboratoire si le tableau colle. " + bt("w-dem", "cinq étapes") + "<sup class=\"s\">10</sup>")),
        ("5. Anamnèse", P("Faiblesse, paralysie flasque, paresthésies. Souvent aucun symptôme, masqué par la maladie causale.<sup class=\"s\">10</sup>")),
        ("6. Examen physique", P("Force musculaire, pression, fistule de dialyse, signes de lyse. L'examen ne retarde pas le calcium si le QRS est déjà large. " + bt("w-exam", "au lit") + "<sup class=\"s\">10</sup>")),
        ("7. Approche syndromique", P("Onde T de l'hyperkaliémie contre onde T de l'occlusion. QRS large contre bloc de branche et contre tachycardie ventriculaire. " + bt("w-dd", "ne pas confondre") + "<sup class=\"s\">1,10</sup>")),
        ("8. Diagnostic positif", P("Valeur et tracé. Sévère : 6,5 mmol/L ou plus. Modérée : 6,0 à 6,4. Légère : 5,5 à 5,9. Le tracé toxique compte autant que le chiffre. " + bt("w-coeur", "signes et seuils") + "<sup class=\"s\">10</sup>")),
        ("9. Examens complémentaires", P("Gaz du sang au lit, puis laboratoire. Glycémie si l'on donne de l'insuline. Créatinine, une cause. Électrocardiogramme répété.<sup class=\"s\">10</sup>")),
        ("10. Arbre décisionnel", P("Protéger le cœur, faire entrer le potassium, le sortir, surveiller, éviter la récidive. Calcium seulement si le tracé est toxique. " + bt("w-dem", "l'algorithme") + "<sup class=\"s\">10</sup>")),
        ("11. Prise en charge en Suisse", P("La phrase de calcium est celle de 2021, chlorure ou gluconate. Aucune information professionnelle de chlorure de calcium à 10 % n'a été relue : on le dit. On ne recopie pas la quantité de glucose. " + bt("w-aips", "limite") + "<sup class=\"s\">10</sup>")),
        ("12. Prévention", P("Revoir les bloqueurs du système rénine, les épargneurs de potassium, le régime, la dialyse. Le traitement de la forme légère est hors du guide de 2021.<sup class=\"s\">10</sup>")),
        ("13. Points clés", P("Toute arythmie peut être un potassium. Tracé toxique : calcium. Tracé normal : ne pas se rassurer. 15 % en 6 heures si la valeur est sévère.<sup class=\"s\">10</sup>")),
        ("14. Pièges d'examen", P("Appeler infarctus une onde T en tente. Donner de l'insuline sans surveiller le sucre. Oublier que le salbutamol échoue souvent en dialyse. " + bt("w-piege", "pièges") + "<sup class=\"s\">10</sup>")),
    ]
    wins = "".join([
        fen("w-coeur", "Signes", sigles() + P(
            "Le texte de 2021 place l'hyperkaliémie au-dessus de 5,5 mmol/L et la dit sévère à partir de 6,5, modérée de 6,0 à 6,4, légère de 5,5 à 5,9.<sup class=\"s\">10</sup>",
            "Signes, dans l'ordre décrit : bloc du premier degré avec PR au-delà de 0,2 s, onde P aplatie ou absente, " + qq(onde) + " sous-décalage du ST, " + qq(qrs) + " tachycardie ventriculaire, bradycardie, arrêt.<sup class=\"s\">10</sup>",
            qq(quinze) + " Le même paragraphe dit que le tracé peut rester normal et que le premier signe peut être l'arythmie.<sup class=\"s\">10</sup>",
        )),
        fen("w-physio", "Ordre électrique", P(
            "Montée du potassium extracellulaire, inactivation des canaux sodiques, ralentissement de la dépolarisation, QRS large, puis rythme sinusoïdal.",
            "Le calcium intraveineux stabilise la membrane. Il ne baisse pas le potassium. C'est pour cela qu'il vient en premier quand le tracé est toxique, et qu'il ne remplace pas la suite.<sup class=\"s\">10</sup>",
        )),
        fen("w-epi", "Gravité", P(
            "15 % d'arythmies ou d'arrêts dans les 6 heures, avant traitement, si le potassium est à 6,5 mmol/L ou plus. Chiffre de 2021, pas un taux suisse de population.<sup class=\"s\">10</sup>",
        )),
        fen("w-dem", "Cinq étapes", P(
            "1. Protéger le cœur. 2. Faire entrer le potassium dans les cellules. 3. Le sortir du corps. 4. Surveiller le potassium et le glucose. 5. Empêcher le retour.<sup class=\"s\">10</sup>",
            qq(calc) + " En arrêt : bolus rapide, même phrase, et on répète si l'arrêt se prolonge.<sup class=\"s\">10</sup>",
            qq(calc2) + " La nécrose tissulaire si le produit sort de la veine est le risque nommé.<sup class=\"s\">10</sup>",
            "Insuline et glucose : le texte les dit les plus efficaces pour faire entrer le potassium, avec un risque d'hypoglycémie. Les quantités en grammes ne sont pas recopiées. On surveille la glycémie. Le salbutamol nébulisé s'ajoute, il ne se donne pas seul, surtout chez le dialysé où il échoue souvent.<sup class=\"s\">10</sup>",
            "Surveillance : l'insuline et le salbutamol durent 4 à 6 heures, puis le potassium peut rebondir.<sup class=\"s\">10</sup>",
        )),
        fen("w-exam", "Au lit", P(
            "Force des membres, réflexes, respiration. Paralysie flasque : gravité. Fistule, cicatrice de greffe, plaie écrasée : la cause.",
            "Monitoring continu si la valeur est sévère ou si le malade va mal, phrase de 2021.<sup class=\"s\">10</sup>",
        )),
        fen("w-dd", "Sosies", P(
            "Onde T coronaire : large, territoire, douleur. Onde T du potassium : étroite, pointue, diffuse, plus haute que R.",
            "Sus-décalage et potassium : le texte de revue sur les sus-décalages rappelle d'écarter l'hyperkaliémie quand l'onde T dépasse l'onde R.<sup class=\"s\">12</sup>",
            "QRS large rythmé par des P : bloc ou hyperkaliémie. QRS large sans rapport et rapide : DX.4.",
        )),
        fen("w-aips", "Ce qui n'est pas une dose suisse", P(
            "Le chlorure de calcium à 10 %, 10 ml en 2 à 5 minutes, est la phrase de 2021. Elle est gardée parce qu'elle est la conduite du tracé toxique. Elle n'est pas une information professionnelle suisse relue.",
            "Les grammes de glucose et les unités d'insuline du texte européen ne sont pas recopiés comme dose. Aucune étiquette suisse d'insuline n'a été ouverte pour ce lot.",
            "Aucune spécialité de chlorure de calcium injectable n'est citée par un numéro d'autorisation dans cette leçon.",
        )),
        fen("w-piege", "Pièges", P(
            "Se rassurer sur un tracé normal.",
            "Donner le calcium et partir, sans faire entrer ni sortir le potassium, sans refaire le tracé.",
            "Oublier l'hypoglycémie dans les heures qui suivent l'insuline.<sup class=\"s\">10</sup>",
        )),
    ])
    out[7] = dx_generique(7, essentiel, pts, wins)

    # DX.8 BBG
    sg1 = q("sgarbossa_debliek.txt", "concordant ST elevation ≥1 mm in at least 1 lead", 50)
    sg2 = q("sgarbossa_debliek.txt", "concordant ST depression ≥1 mm in lead V1, V2 of V3", 60)
    sg3 = q("sgarbossa_debliek.txt", "discordant ST elevation ≥1 mm and ratio ST/S", 40)
    qrsb = q("sgarbossa_debliek.txt", "Length of QRS complex >120 ms", 40)
    essentiel = P(
        "QRS au-delà de 120 ms, discordance du ST et de l'onde T. Ce n'est pas un infarctus. La concordance, elle, en est un signe. "
        + bt("w-coeur", "Sgarbossa modifié") + "<sup class=\"s\">12</sup>",
        "Avec une forte suspicion clinique, le relevé de 2023 prend en charge le bloc comme un infarctus avec sus-décalage. "
        + bt("w-dem", "la filière") + "<sup class=\"s\">1</sup>",
    )
    pts = [
        ("1. Définition", P("Retard de la branche gauche : le ventricule gauche s'active à travers le myocarde, QRS large, ST discordant. " + bt("w-coeur", "critères de tracé") + "<sup class=\"s\">12</sup>")),
        ("2. Épidémiologie", P("Pas de prévalence suisse du bloc dans les textes lus. Sa présence ne donne pas l'âge de l'occlusion.")),
        ("3. Physiopathologie", P("Activation droite d'abord, puis gauche de proche en proche. Le ST discordant est la repolarisation de cette activation lente. " + bt("w-physio", "discordance") + "<sup class=\"s\">12</sup>")),
        ("4. Démarche diagnostique", P("Bloc connu et malade calme : pas une salle en urgence. Bloc et douleur : critères de concordance, et filière si la suspicion est forte. " + bt("w-dem", "deux situations") + "<sup class=\"s\">1,12</sup>")),
        ("5. Anamnèse", P("Comparatif ancien. Douleur actuelle. Stimulateur cardiaque : la stimulation ventriculaire droite ressemble au bloc, avec une sensibilité moindre des critères.<sup class=\"s\">12</sup>")),
        ("6. Examen physique", P("Dédoublement paradoxal du deuxième bruit, choc de pointe large. Signes de choc ou de crépitants si l'occlusion est déjà là. " + bt("w-exam", "l'examen") + ".")),
        ("7. Approche syndromique", P("Bloc gauche, bloc droit, rythme électro-entraîné, hypertrophie. Tous peuvent soulever le ST sans occlusion. " + bt("w-dd", "les QRS larges stables") + "<sup class=\"s\">1,12</sup>")),
        ("8. Diagnostic positif", P("QRS au-delà de 120 ms, aspect en V1 et latéral, puis critères modifiés de 2012 si l'on cherche l'occlusion. " + bt("w-coeur", "les trois lignes") + "<sup class=\"s\">12</sup>")),
        ("9. Examens complémentaires", P("Tracé ancien. Échocardiographie si le doute sur la contraction tient et que la salle n'est pas déjà indiquée. Troponine selon DX.2 si l'on n'est pas en filière immédiate.")),
        ("10. Arbre décisionnel", P("Concordance ou suspicion forte : DX.1. Discordance proportionnée et malade indolore : pas de fibrinolyse. " + bt("w-dem", "arbre") + "<sup class=\"s\">1,12</sup>")),
        ("11. Prise en charge en Suisse", P("Pas de médicament propre au bloc. Si l'on entre dans la filière de l'infarctus, les phrases sont celles de DX.1, n° 51795 et 61389.<sup class=\"s\">16,17</sup>")),
        ("12. Prévention", P("Archiver le tracé. Un bloc nouveau devant une douleur n'est pas un bloc de dossier.")),
        ("13. Points clés", P("Discordance normale. Concordance anormale. Ratio ST/S. Forte suspicion clinique : conduite de l'infarctus avec sus-décalage.<sup class=\"s\">1,12</sup>")),
        ("14. Pièges d'examen", P("Thrombolyser tout bloc. Ignorer un sus-décalage concordant de 1 mm. Lire un stimulateur comme un bloc banal. " + bt("w-piege", "pièges") + "<sup class=\"s\">12</sup>")),
    ]
    wins = "".join([
        fen("w-coeur", "Critères", sigles() + P(
            "Tracé du bloc, revue relue : QRS au-delà de 120 ms, axe gauche, ST et T discordants du QRS, S profonde en V1-V3 avec sus-décalage discordant, R ample en latéral avec sous-décalage discordant.<sup class=\"s\">12</sup>",
            "Sgarbossa modifié, Smith 2012, repris dans la revue : " + qq(sg1) + " " + qq(sg2) + " " + qq(sg3) + " Le texte écrit le ratio inférieur ou égal à −0,25.<sup class=\"s\">12</sup>",
            "L'article de 1996 est la source historique. Le cours enseigne la forme modifiée lue, pas un barème de points qui n'est pas dans l'extrait.",
        )),
        fen("w-physio", "Discordance", P(
            "Activation lente : le ST part à l'opposé du QRS. C'est attendu. Un ST du même côté que le QRS, ou un ST trop grand pour l'onde S, casse la règle.<sup class=\"s\">12</sup>",
            "Onde T positive isolée en V5, V6 ou D1, ou onde T négative dans une seule précordiale : la revue les cite comme exceptions encore compatibles avec un tracé non ischémique. On ne construit pas un infarctus sur une seule onde T.<sup class=\"s\">12</sup>",
        )),
        fen("w-dem", "Filière", P(
            "Relevé de la section 3.2.1 de 2023 : bloc de branche gauche, bloc de branche droit ou rythme électro-entraîné, avec une forte suspicion clinique, se prennent en charge comme un infarctus avec sus-décalage.<sup class=\"s\">1</sup>",
            "Sans suspicion, on applique les critères de concordance avant d'activer la salle. Les deux consignes ne se contredisent pas : la clinique forte ne se met pas en attente d'un ratio.",
            "Stimulation ventriculaire droite : même logique de discordance, sensibilité plus basse pour l'occlusion. Un aspect QS en V5-V6 oriente vers la stimulation plutôt que vers le bloc, où l'onde R latérale reste.<sup class=\"s\">12</sup>",
        )),
        fen("w-exam", "Examen", P(
            "Souffle, crépitants, pression : complications. Cicatrice de stimulateur : changer la lecture du QRS.",
            "Douleur en cours : on ne renvoie pas aux consultations avec un bloc jamais vu.",
        )),
        fen("w-dd", "Autres QRS", P(
            "Bloc droit : le relevé de 2023 l'inclut dans la conduite « comme un sus-décalage » si la suspicion est forte. Le Sgarbossa modifié relu vise le bloc gauche.<sup class=\"s\">1,12</sup>",
            "Tachycardie à QRS large : DX.4, ce n'est pas un bloc stable.",
            "Hyperkaliémie : QRS large sans l'aspect typique de branche, onde T en tente. DX.7.",
            "Hypertrophie : sus-décalage secondaire possible. Les seuils de 2023 excluent l'hypertrophie du critère simple du sus-décalage.<sup class=\"s\">1</sup>",
        )),
        fen("w-piege", "Pièges", P(
            "Tout bloc gauche égal fibrinolyse. Le texte modifié sert justement à ne pas faire ce raccourci, sans rater la concordance.<sup class=\"s\">12</sup>",
            "Oublier le ratio et ne garder que les millimètres concordants.",
            "Lire V1-V3 d'un bloc comme un sous-décalage ischémique banal : une partie est la discordance attendue. Le sous-décalage concordant, lui, compte.",
        )),
    ])
    out[8] = dx_generique(8, essentiel, pts, wins)

    # DX.9 QT
    qtc = q("esc2020_qt_sport.txt", "A QTc of >_500 ms is diagnostic.", 40)
    qtc2 = q("esc2020_qt_sport.txt", "corrected QTc interval according to Bazett", 180)
    rms = q("rms2007_qtc.txt", "valeur limite consensuelle de", 150)
    sport = q("esc2020_qt_sport.txt", "sports activity should be prohibited until the underlying cause is corrected", 80)
    mag = q("aips_45728.txt", "tachyarythmies, notamment en cas de résistance à d'autres antiarythmiques", 40)
    magp = q("aips_45728.txt", "Le contenu d'une ampoule de 10 ml doit être administré en injection intraveineuse lente", 120)
    essentiel = P(
        "Pas de seuil unique pour tout adulte : la Revue Médicale Suisse 2007 le dit. "
        "Chez le sportif, 500 ms de QTc diagnostiquent le QT long congénital dans le texte de 2020. "
        + bt("w-coeur", "tenir les deux phrases") + "<sup class=\"s\">13,14</sup>",
        "Torsades : magnésium n° 45728, indication tachyarythmie, et correction de la cause. " + bt("w-aips", "la phrase") + "<sup class=\"s\">25</sup>",
    )
    pts = [
        ("1. Définition", P("QT long congénital et QT long acquis ne se traitent pas pareil. Le second se corrige. " + bt("w-coeur", "les deux cadres") + "<sup class=\"s\">13,14</sup>")),
        ("2. Épidémiologie", P("Pas de prévalence suisse de l'allongement dans les textes lus. Le risque dépend de la cause, pas d'un pourcentage inventé.")),
        ("3. Physiopathologie", P("Repolarisation ralentie, post-dépolarisations, torsades. Hypokaliémie, hypomagnésémie, bradycardie et médicaments favorisent l'acquis. " + bt("w-physio", "torsades") + ".")),
        ("4. Démarche diagnostique", P("Mesurer, corriger selon le texte que l'on cite, chercher le médicament et le potassium, séparer le sportif du malade de soins aigus. " + bt("w-dem", "ne pas mélanger les seuils") + "<sup class=\"s\">13,14</sup>")),
        ("5. Anamnèse", P("Syncope à l'effort, au réveil, au bruit, histoire familiale, nouveau médicament, diarrhée, diurétique. " + bt("w-ana", "acquis ou congénital") + "<sup class=\"s\">13</sup>")),
        ("6. Examen physique", P("Pouls lent, signes de choc si la torsade tourne, surdité dans certains syndromes congénitaux que ce lot ne détaille pas faute de texte dédié.")),
        ("7. Approche syndromique", P("QT long stable, torsades, QT court non développé ici. La torsade est une tachycardie ventriculaire polymorphe. " + bt("w-dd", "ce que ce n'est pas") + "<sup class=\"s\">9</sup>")),
        ("8. Diagnostic positif", P("Sportif asymptomatique : suspicion si le QTc de Bazett dépasse 470 ms chez l'homme ou 480 ms chez la femme. 500 ms est diagnostique dans ce texte. Ailleurs : pas de limite consensuelle de risque en 2007. " + bt("w-coeur", "citations") + "<sup class=\"s\">13,14</sup>")),
        ("9. Examens complémentaires", P("Potassium, magnésium, calcium, liste des médicaments, tracé de repos et tracé après effort si le doute est celui du sportif de 2020.<sup class=\"s\">13</sup>")),
        ("10. Arbre décisionnel", P("Torsade instable : choc. Torsade avec pouls : magnésium et correction. QT acquis : arrêter la cause et suspendre le sport tant qu'elle tient. " + bt("w-dem", "arbre") + "<sup class=\"s\">9,13,25</sup>")),
        ("11. Prise en charge en Suisse", P("Magnesiocard n° 45728. Pas de milligramme de bêtabloquant « du QT » recopié : aucune phrase AIPS n'a été ouverte pour cette indication précise. " + bt("w-aips", "magnésium") + "<sup class=\"s\">25</sup>")),
        ("12. Prévention", P("Éviter l'association de médicaments qui allongent le QT, corriger le potassium avant une introduction risquée, informer le sportif.<sup class=\"s\">13</sup>")),
        ("13. Points clés", P("2007 : pas de seuil unique de risque. 2020 : 500 ms diagnostique chez le sportif. Torsade : électricité si instable, magnésium selon l'étiquette suisse.<sup class=\"s\">13,14,25</sup>")),
        ("14. Pièges d'examen", P("Diviser par la mauvaise formule et annoncer un risque. Traiter tout QTc à 460 ms comme une torsade. Oublier le médicament du jour. " + bt("w-piege", "pièges") + "<sup class=\"s\">14</sup>")),
    ]
    wins = "".join([
        fen("w-coeur", "Deux phrases", sigles() + P(
            "Revue Médicale Suisse 2007 : " + qq(rms) + "<sup class=\"s\">14</sup>",
            "Recommandations sport 2020 : " + qq(qtc2) + " " + qq(qtc) + " Le même passage sépare l'acquis, réversible, du congénital.<sup class=\"s\">13</sup>",
            "On n'applique pas 500 ms comme un seuil d'arrêt cardiaque chez tout adulte hospitalisé. On l'applique au diagnostic du QT long congénital dans le cadre du texte de 2020.<sup class=\"s\">13</sup>",
        )),
        fen("w-physio", "Torsades", P(
            "La torsade tourne autour de la ligne isoélectrique. Elle est souvent courte et syncopale, ou dégénère. Le Conseil européen de réanimation 2021 traite la tachycardie instable par le choc synchronisé si le pouls est là, et la réanimation si le pouls part.<sup class=\"s\">9</sup>",
            "Le magnésium stabilise la membrane. L'étiquette suisse le place parmi les tachyarythmies résistantes aux autres antiarythmiques, pas comme un chiffre de QTc.<sup class=\"s\">25</sup>",
        )),
        fen("w-ana", "Acquis ou congénital", P(
            "Acquis : médicament, potassium bas, magnésium bas, bradycardie, saignement digestif chez la personne âgée. " + qq(sport) + "<sup class=\"s\">13</sup>",
            "Congénital : syncope à l'émotion ou à l'effort, famille, QTc du sportif. Le diagnostic définitif est souvent difficile, phrase de 2020. Un QTc limite avec histoire vide demande une épreuve d'effort et un enregistrement long avant une étiquette.<sup class=\"s\">13</sup>",
        )),
        fen("w-dem", "Arbre", P(
            "Instable : choc, énergies de DX.4. On ne cherche pas le QTc pendant la torsade.",
            "Stable avec QT long et battements prématurés : magnésium, potassium, arrêt du médicament, surveillance.",
            "Sportif asymptomatique au-dessus des seuils de 2020 : avis cardiologique, pas une ordonnance improvisée.<sup class=\"s\">13</sup>",
        )),
        fen("w-dd", "Voisins", P(
            "Tachycardie ventriculaire monomorphe : QRS identiques, DX.4. La torsade change d'aspect.",
            "Hyperkaliémie : onde T en tente, QRS large, QT plutôt difficile à lire. DX.7.",
            "Bloc : bradycardie qui allonge le QT en plus. On traite le bloc, DX.5, et on regarde le QT ensuite.",
        )),
        fen("w-aips", "Magnésium", P(
            "N° 45728. Indication relue : " + qq(mag) + "<sup class=\"s\">25</sup>",
            qq(magp) + " Les premiers 3 ml en 3 minutes, malade couché, puis repos 10 à 20 minutes.<sup class=\"s\">25</sup>",
            "Bloc atrioventriculaire, troubles de conduction, myasthénie, bradycardie prononcée, anurie : contre-indications de la même étiquette. On ne l'injecte pas sur un bloc non entraîné.<sup class=\"s\">25</sup>",
            "L'ampoule contient 73 mg de magnésium, soit 3 mmol. Ce n'est pas une dose de sulfate de magnésium d'un autre guide. On ne convertit pas de mémoire.",
            "Grossesse : le produit cite la tocolyse et les besoins liés à la grossesse parmi ses indications, et l'éclampsie. Ce n'est pas une phrase « torsades et grossesse ». On ne l'étend pas.",
        )),
        fen("w-piege", "Pièges", P(
            "Un seul chiffre pour tous. La revue de 2007 l'interdit.<sup class=\"s\">14</sup>",
            "Bazett à fréquence très haute ou très basse : le texte de 2020 précise la formule, il ne dit pas qu'elle est parfaite à 140 battements.",
            "Magnésium sur un bloc complet sans entraînement : l'étiquette le contre-indique.<sup class=\"s\">25</sup>",
        )),
    ])
    out[9] = dx_generique(9, essentiel, pts, wins)

    # DX.10 EP
    mort = q("rms2009_ep.txt", "la mortalité de l’embolie pulmonaire (EP) peut avoisiner les 10%", 80)
    haut = q("rms2009_ep.txt", "dont la mortalité est de l’ordre de 50%", 80)
    bas = q("rms2009_ep.txt", "les patients à bas risque bénéficient d’une anticoagulation thérapeutique", 100)
    essentiel = P(
        "L'embolie ne se diagnostique pas sur un aspect de tracé dans les textes relus. Elle se stratifie. "
        "Instable : mortalité de l'ordre de 50 % dans la revue de 2009. Stable avec ventricule droit touché : jusqu'à 10 %. "
        + bt("w-coeur", "la stratification") + "<sup class=\"s\">15</sup>",
        "Le tracé sert à ne pas manquer un infarctus et à voir une souffrance du ventricule droit. Il ne remplace pas l'imagerie. "
        + bt("w-dd", "ce que le tracé ne fait pas") + "<sup class=\"s\">1,15</sup>",
    )
    pts = [
        ("1. Définition", P("Oblitération artérielle pulmonaire. Le tracé anormal en est un témoin possible, pas le critère. " + bt("w-coeur", "ce qui est écrit") + "<sup class=\"s\">15</sup>")),
        ("2. Épidémiologie", P("La revue de 2009 estime l'incidence aiguë à environ 69 cas pour 100 000 habitants, et la mortalité globale entre 3 et 12 %. " + bt("w-epi", "chiffres de 2009") + "<sup class=\"s\">15</sup>")),
        ("3. Physiopathologie", P("La charge du ventricule droit dilate, baisse le débit, peut ischémier le myocarde droit et lever la troponine. " + bt("w-physio", "ventricule droit") + "<sup class=\"s\">15,3</sup>")),
        ("4. Démarche diagnostique", P("Instabilité d'abord. Le tracé écarte l'infarctus à sus-décalage ou le montre. Le diagnostic d'embolie se fait par la clinique et l'imagerie, pas par un millimètre. " + bt("w-dem", "ordre") + "<sup class=\"s\">1,15</sup>")),
        ("5. Anamnèse", P("Dyspnée, douleur pleurale, syncope, facteur de risque veineux. Une syncope est déjà un signe de gravité possible.")),
        ("6. Examen physique", P("Pression, fréquence, turgescence, signe de choc, jambe. " + bt("w-exam", "au lit") + "<sup class=\"s\">15</sup>")),
        ("7. Approche syndromique", P("Haut risque si choc ou hypotension. Les autres sont stables, avec ou sans dysfonction droite. " + bt("w-coeur", "trois cases") + "<sup class=\"s\">15</sup>")),
        ("8. Diagnostic positif", P("Pas de critère électrocardiographique chiffré dans les sources de ce lot. On ne récite pas un aspect en trois lettres dont la fréquence n'a pas été lue. " + bt("w-dd", "limite") + "<sup class=\"s\">15</sup>")),
        ("9. Examens complémentaires", P("Tracé pour l'infarctus et le rythme. Troponine et peptide natriurétique comme marqueurs de gravité dans la revue de 2009, pas comme preuve de caillot. Imagerie ensuite.<sup class=\"s\">15</sup>")),
        ("10. Arbre décisionnel", P("Choc : reperfusion discutée, thrombolyse ou embolectomie si pas de contre-indication, phrase de 2009. Stable à bas risque : anticoagulation. Risque intermédiaire : la thrombolyse n'est pas routinière dans ce texte. " + bt("w-dem", "arbre") + "<sup class=\"s\">15</sup>")),
        ("11. Prise en charge en Suisse", P("L'apixaban n° 61549 a une phrase pour l'embolie : 10 mg deux fois par jour pendant 7 jours, puis 5 mg deux fois par jour. Ce n'est pas la dose de la fibrillation. " + bt("w-aips", "la phrase") + "<sup class=\"s\">24</sup>")),
        ("12. Prévention", P("Prévention de la récidive : le n° 61549 indique 2,5 mg deux fois par jour après au moins 6 mois d'une dose thérapeutique, quand la prévention au long cours est indiquée.<sup class=\"s\">24</sup>")),
        ("13. Points clés", P("Le tracé ne prouve pas le caillot. Le choc change la mortalité. La troponine stratifie. La dose d'embolie n'est pas celle de la fibrillation.<sup class=\"s\">15,24</sup>")),
        ("14. Pièges d'examen", P("Écrire un diagnostic d'embolie parce que le tracé « fait droit ». Manquer un sus-décalage. Donner la dose de fibrillation. " + bt("w-piege", "pièges") + "<sup class=\"s\">1,24</sup>")),
    ]
    eli_ep = q("aips_61549.txt", "Pour le traitement de la thrombose veineuse profonde (TVP) aiguë et le traitement de l'embolie pulmonaire (EP), la dose recommandée est de 10 mg deux fois par jour", 160)
    eli_g = q("aips_61549_grossesse.txt", "L'utilisation d'apixaban durant la grossesse n'est pas recommandée.", 70)
    wins = "".join([
        fen("w-coeur", "Stratification 2009", sigles() + P(
            "Stable avec dysfonction droite : " + qq(mort) + "<sup class=\"s\">15</sup>",
            "Instable, choc ou hypotension : " + qq(haut) + " Ces malades sont la minorité. Les stables sont la majorité, environ 90 % dans ce texte. La moitié d'entre eux ont une dysfonction droite, et la mortalité liée à l'embolie passe alors de moins de 2 % à 5-12 %.<sup class=\"s\">15</sup>",
            qq(bas) + " Haut risque : thrombolyse ou embolectomie s'il n'y a pas de contre-indication. Le risque intermédiaire n'a pas de thrombolyse routinière dans cet article.<sup class=\"s\">15</sup>",
        )),
        fen("w-epi", "Chiffres", P(
            "Incidence environ 69 pour 100 000. Mortalité globale encore de 3 à 12 % en 2009, surtout selon le ventricule droit et l'hémodynamique.<sup class=\"s\">15</sup>",
            "Ce ne sont pas des parts de « tracé anormal ». On ne les présente pas comme telles.",
        )),
        fen("w-physio", "Ventricule droit", P(
            "L'obstacle aigu monte la pression droite, dilate le ventricule, gêne le gauche, baisse le débit. L'ischémie du ventricule droit lève la troponine. La revue genevoise de 2019 range l'embolie parmi les causes de troponine sans infarctus de type 1.<sup class=\"s\">3</sup>",
            "Un sus-décalage territorial reste une occlusion coronaire jusqu'à preuve angiographique. Les deux maladies peuvent coexister. Le tracé de DX.1 gagne.",
        )),
        fen("w-dem", "Ordre", P(
            "Pression et conscience. Tracé immédiat pour ne pas manquer DX.1 et DX.4. Puis probabilité clinique et imagerie, hors de cette leçon de tracé.",
            "Marqueurs : la revue de 2009 discute le peptide natriurétique et la troponine pour le pronostic, pas pour remplacer le scanner.<sup class=\"s\">15</sup>",
            "Score clinique : le Pulmonary Embolism Severity Index est cité, cinq classes, paramètres cliniques. Le cours ne récite pas ses points : le tableau chiffré intégral n'est pas dans l'extrait relu. L'instabilité et le choc restent les prédicteurs que le texte retient comme établis.<sup class=\"s\">15</sup>",
        )),
        fen("w-exam", "Au lit", P(
            "Fréquence, pression, saturation, turgescence, bruit droit, mollet. Syncope déjà produite : gravité.",
            "On ne fait pas marcher un malade hypotendu « pour un gaz du sang ».",
        )),
        fen("w-dd", "Limite du tracé", P(
            "Aucun texte de ce lot ne donne un critère électrocardiographique chiffré d'embolie. L'aspect souvent enseigné en trois lettres n'est pas recopié.",
            "Tachycardie sinusale : fréquente et non spécifique. Bloc de branche droit nouveau : souffrance droite possible, pas une preuve.",
            "Infarctus inférieur : millimètres de DX.1. On ne l'appelle pas embolie parce que le malade est dyspnéique.",
            "Hyperkaliémie et péricardite restent des sosies de sus-décalage, DX.7 et DX.6.",
        )),
        fen("w-aips", "Apixaban de l'embolie", P(
            "N° 61549. " + qq(eli_ep) + " puis 5 mg deux fois par jour. La durée courte, au moins 3 mois, se discute si le facteur de risque est passager.<sup class=\"s\">24</sup>",
            "Récidive, quand elle est indiquée : 2,5 mg deux fois par jour après au moins 6 mois à dose thérapeutique.<sup class=\"s\">24</sup>",
            "Fibrillation : 5 mg deux fois par jour, ou 2,5 mg si deux critères parmi 80 ans, 60 kg, créatinine. Ce n'est pas le schéma des 7 premiers jours de l'embolie.<sup class=\"s\">24</sup>",
            qq(eli_g) + " Allaitement : choisir entre arrêter l'allaitement et arrêter le médicament.<sup class=\"s\">24</sup>",
            "Grossesse et embolie : cette phrase dit de ne pas recommander l'apixaban pendant la grossesse. Elle ne donne pas l'alternative. On ne l'invente pas.",
            "Le malade instable de 2009 n'est pas le malade du comprimé. La thrombolyse de la revue n'a pas de milligramme suisse relu ici. On ne le fabrique pas.",
        )),
        fen("w-piege", "Pièges", P(
            "Diagnostic d'embolie sur le seul tracé.",
            "Dose de fibrillation pour une embolie aiguë, ou l'inverse.",
            "Thrombolyse du risque intermédiaire comme si la revue de 2009 la recommandait en routine. Elle ne le fait pas.<sup class=\"s\">15</sup>",
        )),
    ])
    out[10] = dx_generique(10, essentiel, pts, wins)
    return out


def main() -> None:
    corpus = aips_corpus()
    # pools de lecture pour atteindre y
    pool_a = [
        ("rms2024_sca.txt", 2),
        ("esc2023_udmi.txt", 1),
        ("rms2019_troponine.txt", 3),
        ("colaus2023.txt", 4),
        ("esc2024_fa.txt", 5),
        ("erc2021_hyperk.txt", 10),
        ("sgarbossa_debliek.txt", 12),
    ]
    pools = {
        1: [("rms2024_sca.txt", 2), ("esc2023_udmi.txt", 1), ("aips_51795.txt", 16), ("aips_61389.txt", 17)],
        2: [("rms2024_sca.txt", 2), ("rms2019_troponine.txt", 3), ("esc2023_udmi.txt", 1)],
        3: [("esc2024_fa.txt", 5), ("colaus2023.txt", 4), ("hug2023_fa.txt", 6), ("aips_61549.txt", 24)],
        4: [("erc2021_arythmies.txt", 9), ("esc2019_tsv.txt", 7), ("aips_41060.txt", 20), ("aips_51567.txt", 22)],
        5: [("esc2021_stimulation.txt", 8), ("aips_56533.txt", 21), ("erc2021_arythmies.txt", 9), ("sgarbossa_debliek.txt", 12), ("esc2019_tsv.txt", 7)],
        6: [("esc2015_pericarde.txt", 11), ("sgarbossa_debliek.txt", 12), ("esc2023_udmi.txt", 1)],
        7: [("erc2021_hyperk.txt", 10), ("sgarbossa_debliek.txt", 12)],
        8: [("sgarbossa_debliek.txt", 12), ("esc2023_udmi.txt", 1), ("esc2021_stimulation.txt", 8)],
        9: [("esc2020_qt_sport.txt", 13), ("rms2007_qtc.txt", 14), ("aips_45728.txt", 25), ("erc2021_arythmies.txt", 9), ("erc2021_hyperk.txt", 10), ("sgarbossa_debliek.txt", 12)],
        10: [("rms2009_ep.txt", 15), ("rms2019_troponine.txt", 3), ("aips_61549.txt", 24)],
    }
    cibles = {"A": (72000, 80000)}
    for i in range(1, 11):
        cibles[i] = (36000, 45000)

    html_a = phase_a()
    html_a = pad(html_a, pool_a, *cibles["A"], corpus)
    html_a = mesurer_et_inscrire(html_a)
    (LOT / "LOT_154_Phase_A_V0.html").write_text(html_a, encoding="utf-8")
    m = taille_xy.mesurer(html_a)
    print(f"Phase_A x={m.x[1]} y={m.y[1]}")

    dxs = lecons_dx()
    for n, txt in dxs.items():
        txt = pad(txt, pools[n], *cibles[n], corpus)
        txt = mesurer_et_inscrire(txt)
        (LOT / f"LOT_154_Phase_B_V0_DX.{n}.html").write_text(txt, encoding="utf-8")
        m = taille_xy.mesurer(txt)
        print(f"DX.{n} x={m.x[1]} y={m.y[1]}")


if __name__ == "__main__":
    main()
