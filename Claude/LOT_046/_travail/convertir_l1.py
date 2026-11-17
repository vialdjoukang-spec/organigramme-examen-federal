#!/usr/bin/env python3
"""Conversion L1 du LOT_046 : popover → fenêtres :target, point 1 = définition,
fiches .mb, bibliographie regroupée, images guidées. Ne réécrit pas les faits."""
import json, re, html
from pathlib import Path
from bs4 import BeautifulSoup, NavigableString, Comment

RACINE = Path(__file__).resolve().parents[1]
ORIG = RACINE / "_travail" / "origine"
FIG = RACINE / "_travail" / "figures"
VERBATIM = json.loads((RACINE / "_travail" / "mb_verbatim.json").read_text())

# Phrases recopiées mot pour mot de l'AIPS lue le 15.11.2026, là où le découpage
# automatique avait avalé la rubrique.
VERBATIM["30630"]["allaitement"] = (
    "Furosémide passe dans le lait maternel et inhibe la lactation. "
    "L'utilisation de Lasix est donc déconseillée pendant l'allaitement. "
    "Si une prescription de Lasix se révèle indispensable et qu'il n'existe pas "
    "d'alternative moins risquée, un sevrage est indiqué."
)
VERBATIM["51795"]["grossesse"] = (
    "Pendant le premier et le deuxième trimestre de la grossesse, l'acide "
    "acétylsalicylique ne doit être administré qu'en cas de nécessité absolue. "
    "L'acide acétylsalicylique est contre-indiqué au cours du troisième trimestre "
    "de la grossesse."
)
VERBATIM["51795"]["allaitement"] = (
    "Les salicylates passent dans le lait maternel. Au cours de l'allaitement, "
    "prescrire Aspirine Cardio seulement en cas d'indication impérative, le sevrage "
    "est nécessaire lors de l'emploi régulier de hautes doses (>300 mg/jour)."
)
VERBATIM["49456"]["grossesse"] = (
    "Dans une étude clinique portant sur 8 femmes enceintes porteuses d'une "
    "prothèse valvulaire cardiaque, des caillots sanguins se sont développés chez "
    "deux d'entre-elles, après administration de 1 mg/kg d'énoxaparine 2 fois par "
    "jour pour la prophylaxie des thromboembolies."
)
VERBATIM["62207"]["allaitement"] = (
    "Levofloxacin Fresenius i.v. ne doit pas être administré aux enfants ou aux "
    "adolescents en période de croissance, aux femmes enceintes ou en période "
    "d'allaitement, étant donné que l'on n'a pas acquis d'expérience suffisante "
    "en ce qui concerne la sécurité d'application du produit chez ces groupes de patients."
)

FEN_A = {
    "37397": "pa-p11-f2", "58253": "pa-p11-f3", "66994": "pa-p11-f4",
    "30630": "pa-p11-f5", "40558": "pa-p11-f6", "58728": "pa-p11-f7",
    "53836": "pa-p11-f8",
}
MOLECULES_A = ["37397", "58253", "66994", "30630", "40558", "58728", "53836", "49456", "51795"]
MOLECULES_B = ["45674", "50469", "51352", "62207", "59876", "61475", "37404", "44911", "55196"]


def texte(el):
    return re.sub(r"\s+", " ", el.get_text(" ", strip=True))


def split_premiere_phrase(inner):
    """Coupe le HTML au premier point suivi d'une majuscule, hors balises."""
    hors = False
    i = 0
    while i < len(inner) - 2:
        c = inner[i]
        if c == "<":
            hors = True
        elif c == ">":
            hors = False
        elif not hors and inner[i:i + 2] == ". " and inner[i + 2].isupper():
            return inner[: i + 1], inner[i + 2 :]
        i += 1
    return inner, ""


def fenetre(soup, fid, label, contenu_html, mb=False):
    sec = soup.new_tag("section")
    sec["class"] = ["fenetre", "mb"] if mb else ["fenetre"]
    sec["id"] = fid
    sec["role"] = "dialog"
    sec["aria-label"] = label[:120]
    fen = soup.new_tag("div")
    fen["class"] = "fen"
    fermer = soup.new_tag("a", href="#")
    fermer["class"] = "fermer"
    fermer["aria-label"] = "Fermer"
    fermer.string = "Fermer ✕"
    fen.append(fermer)
    bloc = BeautifulSoup(contenu_html, "html.parser")
    for enfant in list(bloc.contents):
        fen.append(enfant)
    sec.append(fen)
    return sec


def convertir_popovers(soup):
    for b in list(soup.find_all("button")):
        if not b.has_attr("popovertarget"):
            continue
        a = soup.new_tag("a", href="#" + b["popovertarget"])
        a["class"] = "ouvre"
        for enfant in list(b.contents):
            a.append(enfant)
        b.replace_with(a)
    for d in list(soup.find_all("div")):
        classes = d.get("class") or []
        if "fenetre" not in classes or not d.has_attr("popover"):
            continue
        fid = d.get("id")
        label = fid
        for a in soup.find_all("a", href="#" + fid):
            label = texte(a) or fid
            break
        sec = fenetre(soup, fid, label, "")
        fen = sec.find("div", class_="fen")
        # le fermer est déjà là ; on y ajoute les enfants d'origine
        for enfant in list(d.contents):
            fen.append(enfant)
        d.replace_with(sec)


def retitrer_definition(soup, sid):
    sec = soup.find(id=sid)
    fort = sec.find("h3").find("strong")
    if fort:
        fort.string = "1. Définition"
    return sec


def deplacer_hors_definition(soup, sid, route):
    sec = retitrer_definition(soup, sid)
    garde = True
    for enfant in list(sec.children):
        if not getattr(enfant, "name", None):
            continue
        if enfant.name == "h3":
            continue
        if garde and enfant.name == "div" and "p" in (enfant.get("class") or []):
            garde = False
            continue
        dest = soup.find(id=route(texte(enfant).lower()))
        dest.append(enfant)


def route_a(t):
    if any(k in t for k in ("insuffisance respiratoire", "ray", "breathlessness", "dyspnée chronique",
                            "notions proches", "nijmegen", "platypn", "borg", "monographie")):
        return "pa-p8"
    return "pa-p3"


def route_b(t):
    if any(k in t for k in ("bronchite", "eurodem", "cancer", "bronchiectas", "fibrose")):
        return "dx1-p4"
    if any(k in t for k in ("âgé", "agée", "personnes âgées", "confusion", "très vieux", "vieux patient")):
        return "dx1-p5"
    return "dx1-p8"


def region_vers_fenetre(soup, div, fid, mot):
    inner = div.decode_contents()
    premiere, reste = split_premiere_phrase(inner)
    if not reste.strip():
        premiere, reste = inner, ""
    premiere = re.sub(
        re.escape(mot),
        f'<a class="ouvre" href="#{fid}">{mot}</a>',
        premiere, count=1, flags=re.I,
    )
    if f'href="#{fid}"' not in premiere:
        premiere = f'<a class="ouvre" href="#{fid}">{mot}</a>. ' + premiere
    nouveau = soup.new_tag("div")
    nouveau["class"] = "p"
    bloc = BeautifulSoup(premiere, "html.parser")
    for enfant in list(bloc.contents):
        nouveau.append(enfant)
    contenu = reste if reste.strip() else inner
    sec = fenetre(soup, fid, mot, f'<div class="p">{contenu}</div>')
    div.replace_with(nouveau)
    nouveau.insert_after(sec)


def regions_phase_a(soup):
    sec = soup.find(id="pa-p6")
    regles = [
        ("constantes", "constantes", "pa-p6-constantes"),
        ("Inspection générale", "Inspection générale", "pa-p6-inspection"),
        ("Peau et muqueuses", "Peau et muqueuses", "pa-p6-peau"),
        ("Cou.", "Cou", "pa-p6-cou"),
        ("Thorax", "Thorax", "pa-p6-thorax"),
        ("Cœur", "Cœur", "pa-p6-coeur"),
        ("Abdomen", "Abdomen", "pa-p6-abdomen"),
        ("Oxymétrie", "Oxymétrie", "pa-p6-oxymetrie"),
    ]
    for debut, mot, fid in regles:
        for div in list(sec.find_all("div", class_="p", recursive=False)):
            t = texte(div)
            if t.startswith(debut) or t.startswith(debut.rstrip(".")) or (
                debut == "constantes" and "constantes" in t[:120].lower()
            ):
                region_vers_fenetre(soup, div, fid, mot)
                break


def regions_dx(soup):
    sec = soup.find(id="dx1-p6")
    paras = [d for d in sec.find_all("div", class_="p", recursive=False)]
    groupes = [
        ("constantes", [1, 2]),
        ("conscience", [3]),
        ("inspection", [4, 5]),
        ("percussion", [6, 7]),
        ("auscultation", [8, 9, 10]),
        ("échographie", [11, 12]),
        ("cœur", [13]),
        ("membres inférieurs", [14]),
    ]
    for mot, idxs in groupes:
        cibles = [paras[i] for i in idxs if i < len(paras)]
        if not cibles:
            continue
        fid = "dx1-p6-" + re.sub(r"[^a-z]+", "-", mot.lower()).strip("-")
        premier = cibles[0]
        inner = premier.decode_contents()
        tete, reste = split_premiere_phrase(inner)
        tete = f'<a class="ouvre" href="#{fid}">{mot}</a> : ' + tete
        nouveau = soup.new_tag("div")
        nouveau["class"] = "p"
        bloc = BeautifulSoup(tete, "html.parser")
        for enfant in list(bloc.contents):
            nouveau.append(enfant)
        morceaux = []
        if reste.strip():
            morceaux.append(f'<div class="p">{reste}</div>')
        for autre in cibles[1:]:
            morceaux.append(str(autre))
        sec_f = fenetre(soup, fid, mot, "".join(morceaux) or f'<div class="p">{inner}</div>')
        premier.replace_with(nouveau)
        nouveau.insert_after(sec_f)
        for autre in cibles[1:]:
            autre.decompose()


def _court(s, n=130):
    s = re.sub(r"\s+", " ", s).strip()
    s = (s.replace("lai t", "lait").replace("pati ents", "patients")
         .replace("un e ", "une "))
    parts = [p.strip() for p in re.split(r"(?<=\.)\s+", s) if p.strip()]
    cle = re.compile(
        r"ne doit pas|ne doivent pas|nécessité absolue|sevrage|contre-indiqu|"
        r"ne doit être|ne devrait|ne pas allaiter|déconseill", re.I)
    for p in parts:
        if cle.search(p):
            return p[:n]
    return (parts[0] if parts else s)[:n]


def tableau_mb(numero, ancre):
    v = VERBATIM[numero]
    cite = f'<sup class="r"><a href="#sb-{ancre}">{ancre}</a></sup>'

    def cel(s):
        s = _court(s)
        morceaux = re.split(r"(?<=\.)\s+", s)
        lies = []
        for m in morceaux:
            if not m:
                continue
            esc = html.escape(m, quote=False)
            if esc.endswith("."):
                lies.append(esc[:-1] + cite + ".")
            else:
                lies.append(esc + cite)
        return " ".join(lies)

    return (
        '<div class="t" style="overflow-x:auto"><table>'
        f'<tr><th>Contre-indications</th><td>{cel(v["ci"])}</td></tr>'
        f'<tr><th>Grossesse</th><td>{cel(v["grossesse"])}</td></tr>'
        f'<tr><th>Allaitement</th><td>{cel(v["allaitement"])}</td></tr>'
        "</table></div>"
    )


def ancre_primaire(soup, numero):
    ids = re.findall(rf'id="(sb-aips-{numero}-[^"]+)"', str(soup))
    hrefs = re.findall(rf'href="#(sb-aips-{numero}-[^"]+)"', str(soup))
    for cand in ids + hrefs:
        return cand.replace("sb-", "", 1) if False else cand[3:] if cand.startswith("sb-") else cand
    return f"aips-{numero}-0"


def ajouter_table_dans(soup, sec, numero):
    ancre = ancre_primaire(soup, numero)
    # l'ancre stockée sans le préfixe sb- pour le href sb-
    if ancre.startswith("sb-"):
        ancre = ancre[3:]
    fen = sec.find("div", class_="fen")
    if fen.find("th", string=re.compile("Grossesse")):
        return ancre
    bloc = BeautifulSoup(tableau_mb(numero, ancre), "html.parser")
    for enfant in list(bloc.contents):
        fen.append(enfant)
    classes = sec.get("class") or []
    if isinstance(classes, str):
        classes = classes.split()
    if "mb" not in classes:
        sec["class"] = classes + ["mb"]
    return ancre


def mb_phase_a(soup):
    for numero, fid in FEN_A.items():
        sec = soup.find(id=fid)
        if sec:
            ajouter_table_dans(soup, sec, numero)
    point = soup.find(id="pa-p11")
    for numero in ("49456", "51795"):
        nom = VERBATIM[numero]["nom"]
        fid = f"pa-p11-m-{numero}"
        if soup.find(id=fid):
            continue
        intro = soup.new_tag("div")
        intro["class"] = "p"
        intro.append(BeautifulSoup(
            f'La fiche de <a class="ouvre" href="#{fid}">{html.escape(nom)}</a> '
            f'reprend les contre-indications, la grossesse et l\'allaitement de '
            f'l\'information professionnelle suisse.',
            "html.parser"))
        ancre = ancre_primaire(soup, numero)
        if ancre.startswith("sb-"):
            ancre = ancre[3:]
        sec = fenetre(soup, fid, nom, tableau_mb(numero, ancre), mb=True)
        point.append(intro)
        point.append(sec)


def mb_phase_b(soup):
    point = soup.find(id="dx1-p11")
    for numero in MOLECULES_B:
        porteur = None
        for div in point.find_all("div", class_="p"):
            classes_parent = []
            parent = div.find_parent("section")
            while parent:
                brut = parent.get("class") or []
                if isinstance(brut, str):
                    brut = brut.split()
                if "fenetre" in brut:
                    break
                parent = parent.find_parent("section")
            else:
                parent = None
            if parent:
                continue
            if numero in texte(div) or VERBATIM[numero]["nom"].split("—")[-1].strip(" ®")[:6].lower() in texte(div).lower():
                porteur = div
                break
        nom = VERBATIM[numero]["nom"]
        fid = f"dx1-p11-m-{numero}"
        ancre = ancre_primaire(soup, numero)
        if ancre.startswith("sb-"):
            ancre = ancre[3:]
        if porteur is None:
            intro = soup.new_tag("div")
            intro["class"] = "p"
            bloc = BeautifulSoup(
                f'<a class="ouvre" href="#{fid}">{html.escape(nom)}</a> '
                f'figure dans le tableau de synthèse, et la fiche recopie la grossesse, '
                f'l\'allaitement et les contre-indications de l\'information professionnelle.',
                "html.parser")
            intro.append(bloc)
            sec = fenetre(soup, fid, nom, tableau_mb(numero, ancre), mb=True)
            point.append(intro)
            point.append(sec)
            continue
        inner = porteur.decode_contents()
        tete, reste = split_premiere_phrase(inner)
        if f'href="#{fid}"' not in tete:
            tete = f'<a class="ouvre" href="#{fid}">{html.escape(nom.split("—")[-1].strip())}</a> — ' + tete
        nouveau = soup.new_tag("div")
        nouveau["class"] = "p"
        for enfant in BeautifulSoup(tete, "html.parser").contents:
            nouveau.append(enfant)
        corps = (f'<div class="p">{reste}</div>' if reste.strip() else "") + tableau_mb(numero, ancre)
        sec = fenetre(soup, fid, nom, corps, mb=True)
        porteur.replace_with(nouveau)
        nouveau.insert_after(sec)


REMPLACEMENTS_FIGURE = [
    ("La trachée descend au centre et se divise en deux bronches souches.",
     "La trachée conduit l'air jusqu'aux deux bronches souches."),
    ("Le poumon gauche présente une incisure cardiaque et ne compte que deux lobes.",
     "Le poumon gauche porte une incisure cardiaque et ne compte que deux lobes."),
    ("La bronche lobaire se divise ensuite en bronches segmentaires.",
     "La bronche lobaire conduit l'air vers les bronches segmentaires."),
    ("Le capillaire longe la membrane respiratoire, très mince chez le sujet sain.",
     "Le capillaire reste contre la membrane respiratoire, très mince chez le sujet sain."),
    ("Le sac alvéolaire réunit plusieurs alvéoles au bout du canal alvéolaire.",
     "Le sac alvéolaire contient plusieurs alvéoles au bout du canal alvéolaire."),
    ("La culture nasopharyngée citée par l'auteur ne prouve pas le germe du foyer, donc l'image ne nomme pas la bactérie.",
     "La culture nasopharyngée citée par l'auteur ne montre pas le germe du foyer, donc l'image reste sans nom de bactérie."),
    ("Un cliché normal n'exclut pas une pneumonie débutante chez la personne âgée.",
     "Un cliché normal ne permet pas d'écarter une pneumonie débutante chez la personne âgée."),
]


def preparer_figure(nom_fichier, phrase_brut, phrase_titre, phrase_annotee):
    brut = (FIG / nom_fichier).read_text().replace("’", "'").replace("‘", "'")
    brut = re.sub(r"<b>\d+\.\s*</b>\s*", "", brut)
    brut = re.sub(
        r"Lisez d'abord seul ce cliché \([^)]+\) : cherchez vous-même le signe\.",
        phrase_brut, brut)
    brut = re.sub(
        r"La copie annotée \([^)]+\) numérote les repères décrits ci-dessous\.",
        phrase_annotee, brut)
    brut = re.sub(
        r"<p class=\"p\"><b>([^<]+)</b>\s*[^<]*</p>",
        lambda m: f'<p class="p"><b>{m.group(1)}</b> {phrase_titre}</p>',
        brut, count=1)
    for ancien, nouveau in REMPLACEMENTS_FIGURE:
        brut = brut.replace(ancien, nouveau)
    brut = re.sub(r'<p class="p">Le (?:cliché|schéma) brut se lit.*?</p>', "", brut)
    brut = re.sub(r'<p class="p">La copie annotée.*?</p>', "", brut)
    return brut


def inserer_figure(soup, sid, fid, label, html_figure, phrase_page):
    point = soup.find(id=sid)
    intro = soup.new_tag("div")
    intro["class"] = "p"
    for enfant in BeautifulSoup(phrase_page, "html.parser").contents:
        intro.append(enfant)
    sec = fenetre(soup, fid, label, html_figure)
    # après le premier paragraphe du point
    premier = point.find("div", class_="p")
    if premier:
        premier.insert_after(sec)
        sec.insert_before(intro)
    else:
        point.append(intro)
        point.append(sec)


def denicher(soup):
    """Une fenêtre ne reste jamais dans une autre fenêtre."""
    change = True
    while change:
        change = False
        for sec in list(soup.find_all("section", class_="fenetre")):
            parent = sec.find_parent(lambda t: getattr(t, "name", None) == "section" and "fenetre" in (" ".join(t.get("class")) if isinstance(t.get("class"), list) else str(t.get("class") or "")))
            if not parent:
                continue
            prev = sec.find_previous_sibling("div", class_="p")
            parent.insert_after(sec)
            if prev and sec.get("id") and ("#" + sec.get("id")) in str(prev):
                sec.insert_before(prev)
            change = True
            break


def images(soup, kind):
    if kind == "A":
        fig = preparer_figure(
            "anatomie.html",
            "Le cliché brut se lit d'abord sans annotation, afin de situer la trachée et les lobes.",
            "OpenStax a publié ce schéma en couleurs, et la lecture en précise les lobes.",
            "La copie annotée montre les repères, et chaque repère correspond à une phrase.")
        inserer_figure(
            soup, "pa-p3", "pa-p3-anatomie", "Anatomie des poumons",
            fig,
            'Le <a class="ouvre" href="#pa-p3-anatomie">schéma des poumons</a> '
            'montre trois lobes à droite et deux à gauche, ce qui guide l\'auscultation '
            '<sup class="r"><a href="#sb-openstax-2013">openstax-2013</a></sup>.')
        fig2 = preparer_figure(
            "oedeme.html",
            "Le cliché brut se lit d'abord sans annotation, afin de comparer le cœur et les deux bases.",
            "Häggström a publié cette radiographie sous licence CC0, et elle montre un cœur élargi.",
            "La copie annotée indique le cœur et les bases, et chaque repère porte sa lecture.")
        inserer_figure(
            soup, "pa-p9", "pa-p9-oedeme", "Radiographie d'un œdème pulmonaire",
            fig2,
            'La <a class="ouvre" href="#pa-p9-oedeme">radiographie d\'un œdème cardiogénique</a> '
            'permet de distinguer un infiltrat bilatéral d\'un foyer unique, sans exclure le syndrome coronarien '
            '<sup class="r"><a href="#sb-rx-kerley">rx-kerley</a></sup>.')
    else:
        fig = preparer_figure(
            "alveoles.html",
            "Le schéma brut se lit d'abord sans annotation, afin de situer l'alvéole et le capillaire.",
            "OpenStax a dessiné la zone respiratoire en couleurs, et le schéma relie l'alvéole au capillaire.",
            "La copie annotée précise les repères, et chaque repère correspond à une structure.")
        inserer_figure(
            soup, "dx1-p3", "dx1-p3-alveole", "Zone respiratoire",
            fig,
            'Le <a class="ouvre" href="#dx1-p3-alveole">schéma de la zone respiratoire</a> '
            'montre l\'alvéole où l\'exsudat de la pneumonie gêne l\'échange '
            '<sup class="r"><a href="#sb-openstax-2013">openstax-2013</a></sup>.')
        fig2 = preparer_figure(
            "pneumonie.html",
            "Le cliché brut se lit d'abord sans annotation, afin de chercher la condensation avant la flèche publiée.",
            "Häggström a publié cette radiographie sous licence CC0, et la flèche rouge appartient au fichier.",
            "La copie annotée indique la condensation, et chaque repère en précise la lecture.")
        inserer_figure(
            soup, "dx1-p9", "dx1-p9-radio", "Radiographie d'une condensation lobaire",
            fig2,
            'La <a class="ouvre" href="#dx1-p9-radio">radiographie d\'une condensation lobaire</a> '
            'montre le foyer qui fait passer l\'hypothèse à la pneumonie avérée '
            '<sup class="r"><a href="#sb-rx-pneumonie">rx-pneumonie</a></sup>.')


def sources_images(kind):
    commun = (
        '<li id="sb-openstax-2013">OpenStax College, Anatomy and Physiology, schéma des poumons '
        'et de la zone respiratoire, 2013, licence CC BY 3.0 — '
        'https://commons.wikimedia.org/wiki/File:2312_Gross_Anatomy_of_the_Lungs.jpg '
        '(consulté le 2026-11-15).</li>'
    )
    if kind == "A":
        return commun + (
            '<li id="sb-rx-kerley">Mikael Häggström, radiographie thoracique avec lignes de Kerley B '
            'et cœur élargi, licence CC0 — '
            'https://commons.wikimedia.org/wiki/File:Chest_radiograph_of_a_lung_with_Kerley_B_lines.jpg '
            '(consulté le 2026-11-15).</li>'
        )
    return commun + (
        '<li id="sb-rx-pneumonie">Mikael Häggström, radiographie thoracique d\'une condensation '
        'lobaire du lobe moyen droit, licence CC0 — '
        'https://commons.wikimedia.org/wiki/File:X-ray_of_lobar_pneumonia.jpg '
        '(consulté le 2026-11-15).</li>'
    )


def comprimer_sources(soup, kind):
    sec = soup.find("section", id=re.compile("sources"))
    ol = sec.find("ol")
    items = ol.find_all("li", recursive=False)
    aips = {}
    autres = {}
    ordre_aips = []
    ordre_url = []
    for li in items:
        ident = li.get("id") or ""
        corps = li.decode_contents()
        m = re.match(r"sb-aips-(\d+)", ident)
        if m:
            n = m.group(1)
            if n not in aips:
                aips[n] = []
                ordre_aips.append(n)
            aips[n].append((ident, corps))
            continue
        urls = re.findall(r"https?://[^<\s]+", corps)
        url = urls[0] if urls else ident
        if url not in autres:
            autres[url] = []
            ordre_url.append(url)
        autres[url].append((ident, corps))
    ol.clear()
    for n in ordre_aips:
        couples = aips[n]
        principal, corps = couples[0]
        maj = VERBATIM.get(n, {}).get("maj", "")
        for ident, _ in couples[1:]:
            for a in soup.find_all("a", href="#" + ident):
                a["href"] = "#" + principal
        url = re.search(r"https?://[^<\s]+", corps)
        url = url.group(0) if url else ""
        date = re.search(r"consulté le [^<)]+", corps)
        date = date.group(0) if date else "consulté le 2026-11-10"
        li = soup.new_tag("li", id=principal)
        li.append(BeautifulSoup(
            f"Information professionnelle suisse, autorisation {n}, mise à jour {maj}. "
            f"{url} ({date}).", "html.parser"))
        ol.append(li)
    for url in ordre_url:
        couples = autres[url]
        principal, corps = couples[0]
        for ident, _ in couples[1:]:
            for a in soup.find_all("a", href="#" + ident):
                a["href"] = "#" + principal
        date = re.search(r"consulté le [^<)]+", corps)
        date = date.group(0) if date else "consulté le 2026-11-10"
        li = soup.new_tag("li", id=principal)
        # on garde le premier intitulé, une seule URL
        propre = re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", corps))
        propre = re.sub(r"https?://\S+", "", propre)
        propre = propre[:60].strip(" -—")
        li.append(BeautifulSoup(
            f"{html.escape(propre)} {url} ({date}).", "html.parser"))
        ol.append(li)
    ol.append(BeautifulSoup(sources_images(kind), "html.parser"))


def titres(soup, kind):
    if kind == "A":
        titre = "S2.7 — Dyspnée"
    else:
        titre = "DX.1 — Pneumonie communautaire 🚩 E5"
    if soup.title:
        soup.title.string = titre
    h2 = soup.find("h2")
    if h2:
        h2.clear()
        h2.append(titre)
    # retire la feuille locale grise : forme.css impose le fond blanc
    for st in soup.find_all("style"):
        st.decompose()


def limiter_car(html_texte, plafond=15):
    morceaux = re.split(r"(, car )", html_texte, flags=re.I)
    n = 0
    out = []
    for morceau in morceaux:
        if re.fullmatch(r", car ", morceau, flags=re.I):
            n += 1
            out.append(morceau if n <= plafond else ", parce que ")
        else:
            out.append(morceau)
    return "".join(out), n


def varier_amorces(html_texte):
    remplacements = [
        ("La réponse est ", ["Le corrigé retient ", "L'attendu retient ", "La décision retient "]),
        ("Le tableau suivant ", ["Ce tableau ", "Le récapitulatif ", "Le tableau ci-dessous "]),
        ("Le geste de ", ["Le temps ", "Cette étape ", "Le mouvement "]),
    ]
    for amorce, variantes in remplacements:
        vus = 0
        def repl(m, vus_boite=[0]):
            vus_boite[0] += 1
            if vus_boite[0] <= 5:
                return m.group(0)
            return variantes[(vus_boite[0] - 6) % len(variantes)]
        html_texte = re.sub(re.escape(amorce), repl, html_texte)
    return html_texte


def finaliser(soup, kind):
    brut = str(soup)
    if not brut.startswith("<!DOCTYPE"):
        brut = "<!DOCTYPE html>\n" + brut
    brut, ncar = limiter_car(brut)
    brut = varier_amorces(brut)
    brut = re.sub(r", parce que (elle|il|ils|elles|on|un|une)\b", r", parce qu'\1", brut)
    # Les identifiants internes d'extraits sont raccourcis ; l'ancre et l'URL restent.
    anciens = sorted(set(re.findall(r"sb-(?!aips-)[A-Za-z0-9._:-]+", brut)), key=len, reverse=True)
    for i, old in enumerate(anciens, 1):
        nouveau = f"sb-n{i}"
        brut = brut.replace(f'id="{old}"', f'id="{nouveau}"')
        brut = brut.replace(f'href="#{old}"', f'href="#{nouveau}"')

    def sup_court(m):
        href = m.group(1)
        num = re.search(r"aips-(\d+)", href)
        vis = num.group(1) if num else href.rsplit("-", 1)[-1]
        return f'<sup class="r"><a href="{href}">{vis}</a></sup>'

    brut = re.sub(r'<sup class="r"><a href="(#[^"]+)">[^<]*</a></sup>', sup_court, brut)
    brut = re.sub(
        r"<section\b([^>]*?)\bclass=\"fenetre mb\"([^>]*)>",
        lambda m: '<section class="fenetre mb"' + (m.group(1) + m.group(2)).replace(' class="fenetre mb"', "") + ">",
        brut)
    # la légende garde la licence et la date ; l'URL reste dans la bibliographie
    brut = re.sub(
        r'(<figcaption>.*?)(?:<a href="https://commons\.wikimedia\.org[^"]*">[^<]*</a>,?\s*)(.*?</figcaption>)',
        r"\1\2", brut, flags=re.S)
    fin = f"<!-- FIN_FICHIER LOT_046_{'Phase_A' if kind == 'A' else 'Phase_B_V0_DX.1'} -->"
    if kind == "A":
        fin = "<!-- FIN_FICHIER LOT_046_Phase_A_V0 -->"
    else:
        fin = "<!-- FIN_FICHIER LOT_046_Phase_B_V0_DX.1 -->"
    brut = re.sub(r"<!-- FIN_FICHIER.*?-->\s*", "", brut)
    brut = brut.rstrip() + "\n" + fin + "\n"
    return brut, ncar


def traiter(nom, kind):
    soup = BeautifulSoup((ORIG / nom).read_text(), "html.parser")
    convertir_popovers(soup)
    if kind == "A":
        deplacer_hors_definition(soup, "pa-p1", route_a)
        regions_phase_a(soup)
        mb_phase_a(soup)
    else:
        deplacer_hors_definition(soup, "dx1-p1", route_b)
        regions_dx(soup)
        mb_phase_b(soup)
    images(soup, kind)
    denicher(soup)
    comprimer_sources(soup, kind)
    titres(soup, kind)
    brut, ncar = finaliser(soup, kind)
    dest = RACINE / nom
    dest.write_text(brut)
    print(nom, "octets", len(brut.encode()), "car_initiaux", ncar)


if __name__ == "__main__":
    traiter("LOT_046_Phase_A_V0.html", "A")
    traiter("LOT_046_Phase_B_V0_DX.1.html", "B")
