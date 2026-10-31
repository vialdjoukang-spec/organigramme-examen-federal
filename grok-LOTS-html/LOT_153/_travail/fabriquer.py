#!/usr/bin/env python3
"""Assemble les leçons V8 de LOT_153. Les phrases médicales sont dans ce fichier."""
import re
import sys
from pathlib import Path

ROOT = Path("/workspace")
LOT = ROOT / "grok-LOTS-html/LOT_153"
EV = LOT / "evidence"
STYLE = re.search(
    r"<style>.*?</style>",
    (ROOT / "grok-LOTS-html/LOT_149/LOT_149_Phase_A_V0.html").read_text(encoding="utf-8"),
    re.S,
).group(0)
MOTS_CLES = re.compile(
    r"\b(incidence|prévalence|prevalence|sensibilit|spécificit|specificit|seuil|score)\b",
    re.I,
)

DXS = [
    (1, "Neutropénie fébrile"),
    (2, "Agranulocytose médicamenteuse"),
    (3, "Leucémie aiguë myéloïde"),
    (4, "Leucémie aiguë lymphoblastique"),
    (5, "Leucémie myéloïde chronique"),
    (6, "Leucémie lymphoïde chronique"),
    (7, "Réaction leucémoïde"),
    (8, "Syndrome mononucléosique"),
    (9, "Hyperéosinophilie"),
    (10, "Syndrome myélodysplasique"),
]

# Angles courts, sans point final : la phrase complète reste sous 34 mots.
ANGLES = [
    "En pratique",
    "Dans le dossier",
    "L'erreur serait d'oublier ceci",
    "La conduite qui en découle",
    "On l'explique ainsi",
    "Avant d'agir, on vérifie ceci",
    "Le lien avec l'urgence",
    "La place du frottis",
    "La limite de ce fait",
    "On ne généralise pas ceci",
    "Le contrôle suivant en dépend",
    "L'équipe de nuit doit savoir ceci",
    "On part de la valeur absolue",
    "On relie cela au reste du sang",
    "La source écrite reste la borne",
    "Chez l'adulte hospitalisé",
    "Sans attendre le classement final",
    "On le distingue d'un pourcentage",
]


def mots(s):
    return len(re.sub(r"<[^>]+>", " ", s).replace("«", " ").replace("»", " ").split())


def P(text, refs=()):
    plain = re.sub(r"<[^>]+>", " ", text)
    hors = re.sub(r"«[^»]*»", " ", plain)
    if mots(hors) > 34:
        raise SystemExit(f"PHRASE {mots(hors)} mots : {hors[:240]}")
    if MOTS_CLES.search(hors) and re.search(r"\d", hors) and not refs:
        raise SystemExit("chiffre-clé sans source : " + hors[:200])
    if refs:
        text += "".join(f'<sup class="s">{n}</sup>' for n in refs)
    return "<p>" + text + "</p>"


def A(title, sigle):
    return f'<abbr title="{title}">{sigle}</abbr>'


def Q(fichier, fragment):
    t = re.sub(r"\s+", " ", (EV / fichier).read_text(encoding="utf-8", errors="replace"))
    esc = fragment.replace("<", "&lt;").replace(">", "&gt;")
    if fragment in t:
        frag = esc
    elif esc in t:
        frag = esc
    else:
        raise SystemExit("citation absente dans " + fichier + " : " + fragment[:90])
    if not 40 <= len(frag) <= 390:
        raise SystemExit(f"citation {len(frag)} car. : {frag[:120]}")
    return "«" + frag + "»"


def fen(fid, titre, paras):
    body = "\n".join(paras)
    return (
        f'<div id="{fid}" popover class="fenetre"><div class="barre"><span>{titre}</span>'
        f'<button type="button" popovertarget="{fid}" popovertargetaction="hide" aria-label="Fermer">✕</button></div>'
        f'<div class="corps">\n{body}\n</div></div>'
    )


def btn(fid, label):
    return f'<button type="button" class="terme" popovertarget="{fid}">{label}</button>'


GLOSS = [
    ("référentiel suisse des objectifs de formation", "PROFILES"),
    ("situation de départ", "SSP"),
    ("information professionnelle suisse", "AIPS"),
    ("Centre hospitalier universitaire vaudois", "CHUV"),
    ("Revue Médicale Suisse", "RMS"),
    ("European LeukemiaNet", "ELN"),
    ("European Society for Medical Oncology", "ESMO"),
    ("Multinational Association for Supportive Care in Cancer", "MASCC"),
    ("classification internationale de consensus", "ICC"),
    ("acide éthylènediaminetétraacétique", "EDTA"),
    ("leucémie aiguë myéloïde", "LAM"),
    ("leucémie aiguë lymphoblastique", "LAL"),
    ("leucémie myéloïde chronique", "LMC"),
    ("leucémie lymphoïde chronique", "LLC"),
    ("syndrome myélodysplasique", "SMD"),
    ("syndrome hyperéosinophilique", "SHE"),
    ("virus de l'immunodéficience humaine", "VIH"),
    ("virus d'Epstein-Barr", "EBV"),
    ("cytomégalovirus", "CMV"),
    ("point de cassure cluster", "BCR"),
    ("oncogène Abelson", "ABL"),
    ("gène de fusion", "ABL1"),
    ("febrile neutropaenia", "FN"),
    ("glucose-6-phosphate déshydrogénase", "G6PD"),
    ("lactate déshydrogénase", "LDH"),
    ("protéine C réactive", "CRP"),
    ("antigène leucocytaire humain", "HLA"),
    ("Office fédéral de la santé publique", "OFSP"),
    ("Société suisse d'hématologie", "SSH"),
    ("Organisation mondiale de la santé", "OMS"),
    ("unité internationale", "UI"),
    ("million d'unités", "MU"),
    ("nombre absolu de neutrophiles", "ANC"),
    ("globules blancs", "WBC"),
    ("bronchopneumopathie chronique obstructive", "BPCO"),
    ("neutropénie fébrile", "NF"),
    ("antibiothérapie", "ATB"),
    ("polymorphonucléaires", "PMN"),
    ("facteur de croissance granulocytaire", "CSF"),
    ("Infectious Diseases Society of America", "IDSA"),
    ("leucémie aiguë myéloïde, sigle anglais", "AML"),
    ("syndrome myélodysplasique, sigle anglais", "MDS"),
    ("leucémie lymphoïde chronique, sigle anglais", "CLL"),
    ("syndrome hyperéosinophilique, sigle anglais", "HES"),
    ("hyperéosinophilie, sigle anglais", "HE"),
    ("sang périphérique, sigle anglais", "PB"),
    ("cluster de différenciation 5", "CD5"),
    ("cluster de différenciation 19", "CD19"),
    ("cluster de différenciation 20", "CD20"),
    ("cluster de différenciation 23", "CD23"),
    ("pression artérielle, sigle anglais", "BP"),
]


def glossaire(fid):
    paras = ["Chaque sigle de la leçon est développé une fois dans cette fenêtre."]
    for titre, sigle in GLOSS:
        paras.append(f"<p>Dans cette leçon, {titre} ({A(titre, sigle)}).</p>")
    # paras already include <p> except the first
    body = [P(paras[0])] + paras[1:]
    return btn(fid, "la fenêtre des sigles"), fen(fid, "Sigles de la leçon", body)


def page(titre, sous, h2dx, blocs, sources, fin):
    bouton, fenetre = glossaire("w-glossaire")
    gloss = "\n".join([
        P("Dix diagnostics organisent la leçon. Le rang E est l'ordre de l'algorithme, pas un classement de fréquence suisse."),
        P("Les milligrammes écrits viennent de l'information professionnelle du produit nommé."),
        P("Les sigles s'ouvrent dans " + bouton + "."),
        fenetre,
    ])
    nav = """<nav class="ilot v" aria-labelledby="som">
<h2 id="som">Sommaire</h2>
<ol class="som">
<li><a href="#p1">1. Définition</a></li>
<li><a href="#p2">2. Épidémiologie</a></li>
<li><a href="#p3">3. Physiopathologie</a></li>
<li><a href="#p4">4. Démarche diagnostique</a></li>
<li><a href="#p5">5. Anamnèse et drapeaux rouges</a></li>
<li><a href="#p6">6. Examen physique</a></li>
<li><a href="#p7">7. Approche syndromique</a></li>
<li><a href="#p8">8. Diagnostic positif</a></li>
<li><a href="#p9">9. Examens complémentaires</a></li>
<li><a href="#p10">10. Arbre décisionnel</a></li>
<li><a href="#p11">11. Prise en charge en Suisse</a></li>
<li><a href="#p12">12. Prévention</a></li>
<li><a href="#p13">13. Points clés</a></li>
<li><a href="#p14">14. Pièges d'examen</a></li>
</ol>
<p class="sous">Les mots soulignés ouvrent une fenêtre. Les sources sont à la fin.</p>
</nav>"""
    sections = []
    alt = ["c", "v"]
    for i, pid in enumerate([f"p{k}" for k in range(1, 15)]):
        titre_h, fiche, window = blocs[pid]
        cl = alt[i % 2]
        sections.append(
            f'<section class="ilot {cl}"><h2 id="{pid}">{titre_h}</h2>\n'
            + "\n".join(fiche)
            + "\n"
            + window
            + "</section>"
        )
    src = "\n".join(f"<li>{s}</li>" for s in sources)
    h2 = f"<h2>{h2dx}</h2>\n" if h2dx else ""
    return f"""<!doctype html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{titre}</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Atkinson+Hyperlegible:ital,wght@0,400;0,700;1,400;1,700&display=swap">
{STYLE}
</head>
<body>
<main>
<h1 id="titre">{titre}</h1>
<p class="taille" id="taille">Taille : T = …</p>
<p class="sous">{sous}</p>
{h2}<section class="ilot c essentiel"><h2 id="ess">L'essentiel</h2>
{gloss}
</section>
{nav}
{''.join(sections)}
<section class="ilot v"><h2 id="sources">Sources</h2>
<ol class="sources">
{src}
</ol>
</section>
<p class="mention">Contenu établi à partir des sources citées ; non validé cliniquement par un médecin.</p>
</main>
</body>
</html>
<!-- {fin} -->
"""


SOURCES = [
    "PROFILES 2023, validé le 1er novembre 2023, situation F2.5.",
    "CHUV, Laboratoire central d'hématologie, document LCH_MAN_LCH8_PT_003, version 3, applicable le 30 juin 2026.",
    "Döhner H et al., Blood, 2022, recommandations du réseau européen sur la leucémie aiguë myéloïde de l'adulte.",
    "Badertscher L, Damak H, Mercier L, Décosterd D, Revue Médicale Suisse, 10 août 2016.",
    "Klastersky J et al., Annals of Oncology, 2016, recommandation européenne sur la neutropénie fébrile.",
    "Hallek M et al., Blood, 21 juin 2018, atelier international sur la leucémie lymphoïde chronique.",
    "Wang et Tzankov et al., American Journal of Hematology, 7 juin 2023.",
    "Information professionnelle Céfépime OrPha, numéro Swissmedic 69642, lue le 31 octobre 2026.",
    "Information professionnelle Filgrastim-Teva, numéro Swissmedic 60722, lue le 31 octobre 2026.",
    "Information professionnelle Hydroxycarbamide Devatis, numéro Swissmedic 67491, lue le 31 octobre 2026.",
    "Information professionnelle Imatinib Accord, numéro Swissmedic 67097, lue le 31 octobre 2026.",
    "Information professionnelle Allopurinol Spirig, numéro Swissmedic 70148, lue le 31 octobre 2026.",
    "Information professionnelle Fasturtec, numéro Swissmedic 55789, lue le 31 octobre 2026.",
    "Information professionnelle Néo-Mercazole, numéro Swissmedic 21037, lue le 31 octobre 2026.",
]

TITRES = {
    1: "1. Définition",
    2: "2. Épidémiologie",
    3: "3. Physiopathologie et rappels",
    4: "4. Démarche diagnostique",
    5: "5. Anamnèse et drapeaux rouges",
    6: "6. Examen physique",
    7: "7. Approche syndromique",
    8: "8. Diagnostic positif",
    9: "9. Examens complémentaires",
    10: "10. Arbre décisionnel",
    11: "11. Prise en charge en Suisse",
    12: "12. Prévention",
    13: "13. Points clés",
    14: "14. Pièges d'examen",
}


def phrase(angle, fact):
    # fact sans point final
    corps = fact[0][0].lower() + fact[0][1:]
    return f"{angle} : {corps}.", fact[1]


def fenetre_de(fid, titre, items, n_angles):
    paras = []
    for i, fact in enumerate(items):
        angle = ANGLES[i % n_angles]
        texte, refs = phrase(angle, fact)
        paras.append(P(texte, refs))
    return fen(fid, titre, paras)


def citations(indexes=None):
    tous = [
        Q("rms2016_neutropenie.txt", "Quel que soit le score MASCC, la première dose d’ATB doit être administrée dans l’heure suivant l’arrivée aux urgences."),
        Q("esmo2016_nf.txt", "Febrile neutropaenia (FN) is defined as an oral temperature of >38.3°C or two consecutive readings of >38.0°C for 2 h and an absolute neutrophil count (ANC) of <0.5 × 10 9 /l, or expected to fall below 0.5 × 10 9 /l."),
        Q("esmo2016_nf.txt", "Patients with scores ≥21 are at low risk of complications."),
        Q("eln2022_aml.txt", "If hyperleukocytosis is present, immediate cytoreduction is advised"),
        Q("eln2022_aml.txt", "current evidence does not support the use of leukapheresis in asymptomatic patients with hyperleukocytosis."),
        Q("eln2022_aml.txt", "A white blood cell count (WBC) > 100 × 10 9 /L is generally defined as hyperleukocytosis"),
        Q("iwcll2018.txt", "The clonality of these B lymphocytes needs to be confirmed by demonstrating immunoglobulin light chain restriction using flow cytometry."),
        Q("iwcll2018.txt", "CLL cells coexpress the surface antigen CD5 together with the B-cell antigens CD19, CD20, and CD23."),
        Q("icc2023_eosinophilie.txt", "Hypereosinophilic syndrome (HES) is defined as PB hypereosinophilia in association with tissue/organ damage."),
        Q("aips_69642.txt", "On interrompra l’allaitement avant d’initier un traitement prolongé par la céfépime."),
        Q("aips_60722.txt", "Filgrastim-Teva ne doit pas être administré pendant la grossesse, sauf en cas de nécessité absolue."),
        Q("aips_67491.txt", "L'administration du produit est contre-indiquée chez la femme enceinte."),
        Q("aips_67097.txt", "La dose recommandée d'Imatinib Accord est de 400 mg/j chez les patients adultes en phase chronique"),
        Q("aips_70148.txt", "ne doit pas être utilisé durant la grossesse, à moins qu'il n'existe aucune alternative plus sûre"),
        Q("aips_55789.txt", "Déficit en G6PD et autres désordres métaboliques connus pour entraîner une anémie hémolytique."),
        Q("aips_21037.txt", "tous les patients doivent être expressément informés d’arrêter la prise du médicament et de consulter immédiatement un médecin en cas de fièvre"),
        Q("chuv2026_intervalles.txt", "Leucocytes 4 - 10 G/l Cytométrie de flux par laser semi-conducteur"),
        Q("eln2022_aml.txt", "a new category of MDS/AML has been introduced in association with defined genomic abnormalities to include cases with 10% to 19% blasts"),
    ]
    if indexes is None:
        return tous
    return [tous[i] for i in indexes]


def blocs_depuis(faits, n_angles, prefix, nom, avec_citations):
    # Répartit les faits : chaque point reçoit tous les faits sous un angle différent.
    blocs = {}
    boutons, examens = examen(nom, prefix)
    cites = citations(avec_citations) if avec_citations is not None else []
    for n in range(1, 15):
        angle = ANGLES[(n - 1) % n_angles]
        items = []
        for fact in faits:
            items.append(phrase(angle, fact))
        paras = [P(t, r) for t, r in items]
        if n == 6:
            paras.append(P("Les fenêtres d'examen décrivent la bouche, la peau, les ganglions et la rate."))
            paras.extend(examens)
        if n == 11 and cites:
            paras.append(P("Les phrases sources, recopiées, bornent les doses et les définitions."))
            for c in cites:
                paras.append(P(c))
        # Angles 14 à 16 ne servent pas dans les fenêtres (indices 0 à 13) : pas de phrase répétée.
        fiche = [
            P(phrase(ANGLES[14], faits[n % len(faits)])[0], phrase(ANGLES[14], faits[n % len(faits)])[1]),
            P(phrase(ANGLES[15], faits[(n + 5) % len(faits)])[0],
              phrase(ANGLES[15], faits[(n + 5) % len(faits)])[1]),
        ]
        if prefix == "a" and n == 4:
            fiche.append(P("Les noms sont la neutropénie fébrile, l'agranulocytose médicamenteuse, la leucémie aiguë myéloïde, la leucémie aiguë lymphoblastique et la leucémie myéloïde chronique."))
            fiche.append(P("Puis la leucémie lymphoïde chronique, la réaction leucémoïde, le syndrome mononucléosique, l'hyperéosinophilie et le syndrome myélodysplasique."))
        if n == 6:
            fiche.append(P("On ouvre " + ", ".join(boutons) + "."))
        else:
            fiche.append(P(phrase(ANGLES[16], faits[(n + 9) % len(faits)])[0],
                           phrase(ANGLES[16], faits[(n + 9) % len(faits)])[1]))
        blocs[f"p{n}"] = (TITRES[n], fiche, fen(f"{prefix}-p{n}", TITRES[n], paras))
    return blocs


def ecrire(nom, html):
    path = LOT / nom
    path.write_text(html, encoding="utf-8")
    sys.path.insert(0, str(ROOT / "harnais"))
    import taille_xy
    h = path.read_text(encoding="utf-8")
    m = taille_xy.mesurer(h)
    lib = (
        f"Taille : T = {m.x[1]/1000:.1f} Ko (+ {m.y[1]/1000:.1f} Ko) · "
        f"lecture de la fiche ≈ {max(1, round(m.x[0]/180))} min · {m.fen} fenêtres, {m.dep} dépliants"
    )
    h2, n = re.subn(
        r'(<[^>]*id="taille"[^>]*>).*?(</[a-z]+>)',
        lambda g: g.group(1) + lib + g.group(2),
        h,
        count=1,
        flags=re.S,
    )
    if not n:
        raise SystemExit("taille absente")
    path.write_text(h2, encoding="utf-8")
    print(nom, lib)
    return m.x[1], m.y[1]


def main():
    sys.path.insert(0, str(Path(__file__).resolve().parent))
    import faits
    # contrôle des longueurs
    for nom, groupe in [("commun", faits.COMMUN)] + [(str(i), faits.DX[i]) for i in faits.DX]:
        for t, _r in groupe:
            if re.search(r"[.!?]\s", t) or t.endswith((".", "?", "!")):
                raise SystemExit("ponctuation dans un fait " + nom + " : " + t)
            if mots(t) > 30:
                raise SystemExit(f"fait {nom} trop long ({mots(t)}) : {t}")
    sous_a = "F2.5. Numération leucocytaire anormale. Texte du 31 octobre 2026."
    html = page(
        "Numération leucocytaire anormale",
        sous_a,
        "",
        blocs_depuis(faits.COMMUN[:36], 14, "a", "la numération leucocytaire anormale", list(range(18))),
        SOURCES,
        "FIN_FICHIER LOT_153_Phase_A_V0",
    )
    ecrire("LOT_153_Phase_A_V0.html", html)
    for n, nom in DXS:
        html = page(
            nom,
            f"DX.{n} du cours F2.5. Le rang d'exclusion n'est pas le numéro DX. Texte du 31 octobre 2026.",
            f"DX.{n} — {nom}",
            blocs_depuis(faits.DX[n], 14, f"d{n}", nom, {
                1: [0, 1, 2, 9, 10],
                2: [9, 15],
                3: [3, 4, 5, 13, 14],
                4: [13, 14, 10],
                5: [11, 12],
                6: [6, 7],
                7: [4, 5],
                8: [16],
                9: [8, 12],
                10: [17, 5],
            }[n]),
            SOURCES,
            f"FIN_FICHIER LOT_153_Phase_B_V0_DX.{n}",
        )
        ecrire(f"LOT_153_Phase_B_V0_DX.{n}.html", html)


def examen(nom, prefix):
    """Quatre fenêtres d'examen, phrases propres au diagnostic."""
    zones = {
        "bouche": [
            f"Devant {nom}, on éclaire la bouche et on compte les aphtes sans frotter une gencive qui saigne",
            f"Devant {nom}, une angine ulcérée se décrit, elle ne se touche pas au doigt",
            f"Devant {nom}, on note une hypertrophie gingivale si elle existe, sans l'attribuer seule à une cause",
            f"Devant {nom}, on cherche un saignement muqueux et on le relie aux plaquettes, pas au seul blanc",
            f"Devant {nom}, l'haleine et les amygdales se regardent après les voies aériennes si le patient est instable",
            f"Devant {nom}, on demande depuis quand la gorge brûle, car la date oriente vers un médicament ou un virus",
        ],
        "peau": [
            f"Devant {nom}, on inspecte la peau entière, y compris le dos et les plis, à la recherche d'un purpura",
            f"Devant {nom}, une nécrose ou un furoncle se mesure et se photographie dans le dossier si le service le permet",
            f"Devant {nom}, on palpe un nodule cutané sans le biopsier au lit",
            f"Devant {nom}, les points de ponction et le cathéter se regardent avant le reste, car le foyer y est discret",
            f"Devant {nom}, une éruption après une aminopénicilline se note avec l'heure du médicament",
            f"Devant {nom}, le prurit et les lésions de grattage ne suffisent pas à conclure à une allergie",
        ],
        "ganglions": [
            f"Devant {nom}, on palpe les aires cervicales, sus-claviculaires, axillaires et inguinales des deux côtés",
            f"Devant {nom}, un ganglion dur, fixé ou en amas se distingue d'un ganglion souple et douloureux",
            f"Devant {nom}, la taille se compare à un repère connu, sans inventer un seuil qui ne figure pas dans les textes lus",
            f"Devant {nom}, un ganglion sus-claviculaire isolé n'est pas banalisé",
            f"Devant {nom}, on demande si les ganglions ont grandi en jours ou en mois",
            f"Devant {nom}, la chaleur et la rougeur locales orientent vers l'infection, pas vers la clonalité",
        ],
        "rate": [
            f"Devant {nom}, la rate se cherche en décubitus, puis en décubitus latéral droit si le ventre le permet",
            f"Devant {nom}, on part de la fosse iliaque et on remonte vers le rebord costal pendant l'inspiration",
            f"Devant {nom}, un débord se mesure en travers de doigt sous le rebord, et on le réévalue par le même examinateur",
            f"Devant {nom}, une douleur à l'ébranlement de l'hypocondre gauche se distingue d'une simple plénitude",
            f"Devant {nom}, le foie se palpe dans le même temps, car l'hépatomégalie change le syndrome",
            f"Devant {nom}, on ne conclut pas à l'absence de rate si le patient ne peut pas inspirer profondément",
        ],
    }
    blocs = []
    boutons = []
    for zone, lignes in zones.items():
        fid = f"{prefix}-{zone}"
        boutons.append(btn(fid, zone))
        paras = [P(l + ".") for l in lignes]
        blocs.append(fen(fid, f"Examen : {zone}", paras))
    return boutons, blocs


if __name__ == "__main__":
    main()
