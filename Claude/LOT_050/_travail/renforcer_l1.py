#!/usr/bin/env python3
"""Conversion L1 du LOT_050 (Phase A et DX.1), sans réécriture du fond.

Lit les originaux de _travail/originaux/, convertit les fenêtres popover en
sections :target, sort la sémantique du point 1, place une fenêtre par région
et par examen, consolide les entrées bibliographiques qui répètent la même URL,
puis insère les figures déjà téléchargées. Relançable : il repart toujours des originaux.
"""
import html
import json
import re
from pathlib import Path

RACINE = Path(__file__).resolve().parents[1]
ORIG = RACINE / "_travail" / "originaux"
IMAGES = RACINE / "images"

FICHIERS = {
    "LOT_050_Phase_A_V0.html": "pa",
    "LOT_050_Phase_B_V0_DX.1.html": "dx1",
}


def texte(fragment):
    brut = re.sub(r"<[^>]+>", " ", fragment)
    return re.sub(r"\s+", " ", html.unescape(brut)).strip()


def mots(s):
    return len(re.findall(r"\S+", s))


def e(s):
    return html.escape(s, quote=True)


def fin_balise(source, debut):
    """Fin (exclusive) de l'élément ouvert à `debut`, imbrication comprise."""
    m = re.match(r"<(\w+)", source[debut:])
    if not m:
        raise RuntimeError(source[debut:debut + 40])
    nom = m.group(1)
    gt = source.find(">", debut)
    ouvrant = source[debut:gt + 1]
    if ouvrant.endswith("/>"):
        return gt + 1
    prof = 1
    i = gt + 1
    token = re.compile(rf"</?{nom}\b[^>]*>", re.I)
    while prof:
        m = token.search(source, i)
        if not m:
            raise RuntimeError(f"balise {nom} non fermée")
        if m.group(0).startswith("</"):
            prof -= 1
            if prof == 0:
                return m.end()
        elif not m.group(0).endswith("/>"):
            prof += 1
        i = m.end()
    return i


def extraire_divs_popover(source):
    """Remplace chaque <div popover> par une section :target, au même endroit."""
    monographies = set()
    for m in re.finditer(r'<button\b[^>]*popovertarget="([^"]+)"[^>]*>(.*?)</button>', source, re.S):
        if "monographie" in texte(m.group(2)).lower():
            monographies.add(m.group(1))
    source = re.sub(
        r'<button\b[^>]*popovertarget="([^"]+)"[^>]*>(.*?)</button>',
        lambda m: f'<a class="ouvre" href="#f-{m.group(1)}">{m.group(2)}</a>',
        source,
        flags=re.S,
    )
    sortie = []
    i = 0
    motif = re.compile(r'<div\b[^>]*\bpopover\b[^>]*>', re.I)
    while True:
        m = motif.search(source, i)
        if not m:
            sortie.append(source[i:])
            break
        sortie.append(source[i:m.start()])
        fin = fin_balise(source, m.start())
        ouvrant = source[m.start():source.find(">", m.start()) + 1]
        ident = re.search(r'\bid="([^"]+)"', ouvrant).group(1)
        titre = re.search(r'\baria-label="([^"]*)"', ouvrant)
        lib = titre.group(1) if titre else ident
        if ident in monographies or "monographie" in source[m.start():fin][:400].lower():
            classe = "fenetre mb"
        else:
            classe = "fenetre"
        interieur = source[source.find(">", m.start()) + 1:fin - len("</div>")]
        # retire un </div> final déjà compté par la tranche : fin_balise inclut </div>
        bloc = (
            f'<section class="{classe}" id="f-{ident}" role="dialog" aria-label="{e(lib)}">'
            f'<div class="fen"><a class="fermer" href="#" aria-label="Fermer">Fermer ✕</a>'
            f"{interieur}</div></section>"
        )
        sortie.append(bloc)
        i = fin
    return "".join(sortie)


def hisser_fenetres(fragment):
    """Sort les sections.fenetre pour qu'aucune ne reste imbriquée dans une autre."""
    gardes = []
    sortie = []
    i = 0
    motif = re.compile(r'<section\b[^>]*class="[^"]*\bfenetre\b[^"]*"[^>]*>', re.I)
    while True:
        m = motif.search(fragment, i)
        if not m:
            sortie.append(fragment[i:])
            break
        sortie.append(fragment[i:m.start()])
        fin = fin_balise(fragment, m.start())
        gardes.append(fragment[m.start():fin])
        i = fin
    return "".join(sortie), gardes


def fenetre(ident, libelle, corps):
    return (
        f'<section class="fenetre" id="{ident}" role="dialog" aria-label="{e(libelle)}">'
        f'<div class="fen"><a class="fermer" href="#" aria-label="Fermer">Fermer ✕</a>'
        f"{corps}</div></section>"
    )


def lier_premier_paragraphe(fragment, ident, ancre):
    """Entoure le premier mot du paragraphe d'un lien, sans ajouter de mots."""
    m = re.search(r'<div class="p">', fragment)
    if not m:
        return fragment, ""
    fin = fin_balise(fragment, m.start())
    premier = fragment[m.start():fin]
    premier, n = re.subn(
        r'(<div class="p">)([^<]{0,3}?)([A-Za-zÀ-ÿ][^ <]{2,})',
        lambda mm: f'{mm.group(1)}{mm.group(2)}<a class="ouvre" href="#{ident}">{mm.group(3)}</a>',
        premier,
        count=1,
    )
    if n == 0:
        premier = premier.replace(
            '<div class="p">',
            f'<div class="p"><a class="ouvre" href="#{ident}">détail</a> ',
            1,
        )
    return premier, fragment[fin:]


def ouvrir_fermer(section):
    """Sépare la balise ouvrante, l'intérieur et la fermeture d'une section."""
    fin_ouvrante = section.find(">") + 1
    fermeture = section.rfind("</section>")
    return section[:fin_ouvrante], section[fin_ouvrante:fermeture], section[fermeture:]


def envelopper_regions(section, prefixe, numero):
    """Une fenêtre par h4 des points 5, 6 et 9. Le premier paragraphe reste sur la page."""
    if numero not in {5, 6, 9}:
        return section
    ouvrant, interieur, fermant = ouvrir_fermer(section)
    morceaux = re.split(r"(?=<h4\b)", interieur)
    if len(morceaux) == 1:
        return section
    sortie = [morceaux[0]]
    for i, morceau in enumerate(morceaux[1:], 1):
        hm = re.match(r"<h4[^>]*>.*?</h4>", morceau, re.S)
        if not hm:
            sortie.append(morceau)
            continue
        titre = texte(hm.group(0))
        suite = morceau[hm.end():]
        suite, fenetres = hisser_fenetres(suite)
        ident = f"f-{prefixe}-p{numero}-r{i}"
        ancre = re.sub(r"^[0-9]+\.[0-9A-Za-z.]+\s*", "", titre) or titre
        page, reste = lier_premier_paragraphe(suite, ident, "le détail")
        corps = hm.group(0) + reste
        sortie.append(page)
        if texte(reste):
            sortie.append(fenetre(ident, titre, corps))
        else:
            # le seul paragraphe reste sur la page : on retire le lien sans cible
            sortie[-1] = re.sub(
                rf'<a class="ouvre" href="#{ident}">(.*?)</a>',
                r"\1",
                page,
                count=1,
                flags=re.S,
            )
        sortie.extend(fenetres)
    return ouvrant + "".join(sortie) + fermant


def sortir_semantique(section, prefixe):
    """Le point 1 ne garde que la définition. Le reste part vers le point 4."""
    if "1. Définition" not in section and "Définition et sémantique" not in section:
        return section, ""
    section = section.replace("1. Définition et sémantique", "1. Définition", 1)
    ouvrant, interieur, fermant = ouvrir_fermer(section)
    morceaux = re.split(r"(?=<h4\b)", interieur)
    garde = [morceaux[0]]
    deplace = []
    for morceau in morceaux[1:]:
        titre = texte(re.match(r"<h4[^>]*>.*?</h4>", morceau, re.S).group(0))
        if "Définition retenue" in titre:
            garde.append(morceau)
        else:
            deplace.append(morceau)
    return ouvrant + "".join(garde) + fermant, "".join(deplace)


def inserer_dans_point4(section, prefixe, deplace):
    if not deplace:
        return section
    deplace, fenetres = hisser_fenetres(deplace)
    if prefixe == "pa":
        phrase = (
            "Les rythmes que cette plainte peut recouvrir, et les termes qu'il faut éviter, "
            'se lisent dans les <a class="ouvre" href="#f-pa-p4-limites">limites de la définition</a>, '
            "car ce tri précède tout tracé."
        )
        lib = "Limites de la définition"
        ident = "f-pa-p4-limites"
    else:
        phrase = (
            "Les frontières de l'extrasystole idiopathique et les termes qu'il faut réserver "
            'se lisent dans les <a class="ouvre" href="#f-dx1-p4-limites">limites de l\'entité</a>, '
            "car l'exclusion d'une cardiopathie vient ensuite."
        )
        lib = "Limites de l'entité"
        ident = "f-dx1-p4-limites"
    assert 12 <= mots(texte(phrase)) <= 28, mots(texte(phrase))
    bloc = f'<div class="p">{phrase}</div>' + fenetre(ident, lib, deplace) + "".join(fenetres)
    return re.sub(r"(</h3>)", r"\1" + bloc, section, count=1)


def retitrer(html, prefixe):
    html = re.sub(
        rf'<section class="ilot" id="{prefixe}-p(\d+)">',
        rf'<section class="ilot" id="bloc-{prefixe}-\1">',
        html,
    )
    html = re.sub(
        rf'<h3 id="{prefixe}-h(\d+)">',
        rf'<h3 id="{prefixe}-p\1">',
        html,
    )
    if prefixe == "pa":
        html = html.replace("<title>LOT_050 — S2.11 — Palpitations</title>", "<title>S2.11 — Palpitations</title>")
        html = html.replace(
            "<h2>LOT_050 — S2.11 — Palpitations</h2>",
            "<h2>S2.11 — Palpitations</h2>",
        )
    html = re.sub(r"<style\b[^>]*>.*?</style>", "", html, count=1, flags=re.S)
    html = html.replace('<div class="t">', '<div class="t" style="overflow-x:auto">')
    return html


def norm_url(url):
    url = html.unescape(url).replace("&amp;", "&")
    url = re.sub(r"&rettype=abstract&retmode=text", "", url)
    return url.rstrip(".,);")


def cle_source(ident, corps):
    m = re.match(r"sb-aips-(\d+)", ident)
    urls = re.findall(r"https?://[^\s<\"]+", corps)
    url = norm_url(urls[0]) if urls else ""
    if m:
        return ("aips", m.group(1)), url
    return ("url", url or ident), url


def libelle_source(cle, url, dates):
    if cle[0] == "aips":
        maj = dates.get(cle[1], "")
        maj_txt = f", mise à jour {maj}" if maj else ""
        return (
            f"Swissmedic, information professionnelle n° {cle[1]}{maj_txt} — {url} "
            f"(consulté le 2026-11-15)."
        )
    if "hug.ch" in url and "fibrillation" in url:
        nom = "Hôpitaux universitaires de Genève, stratégie de la fibrillation auriculaire, 2023"
    elif "hug.ch" in url:
        nom = "Hôpitaux universitaires de Genève, page des troubles du rythme cardiaque"
    elif "pmc" in url or "PMC" in url or "id=" in url and "pmc" in url:
        pmc = re.search(r"(?:pmc&id=|PMC)(\d+)", url, re.I)
        nom = f"PubMed Central, article PMC{pmc.group(1)}" if pmc else "PubMed Central, article lu"
    elif "pubmed" in url or "efetch" in url and "pubmed" in url:
        pmid = re.search(r"id=(\d+)", url)
        nom = f"PubMed, résumé PMID {pmid.group(1)}" if pmid else "PubMed, résumé lu"
    elif "uliege" in url or "rmlg" in url:
        nom = "Revue médicale de Liège, article sur les tachycardies à complexes fins"
    elif "refdata.ch" in url:
        nom = "Swissmedic, information professionnelle"
    else:
        nom = "Source européenne ou suisse lue pour cette leçon"
    return f"{nom} — {url} (consulté le 2026-11-10)."


def dates_aips():
    """Dates de mise à jour déjà mises en cache par aips_fiche, si le préchargement est fini."""
    cache = Path.home() / ".cache" / "medina_aips"
    dates = {}
    if not cache.exists():
        return dates
    for fj in cache.glob("*.json"):
        try:
            d = json.loads(fj.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            continue
        nums = d.get("numero") or []
        maj = (d.get("mise_a_jour") or "").split()
        if nums and maj:
            dates[nums[0]] = maj[0]
    return dates


def consolider_sources(html):
    m = re.search(r'<section class="ilot" id="[^"]*sources"', html)
    if not m:
        return html
    fin = fin_balise(html, m.start())
    section = html[m.start():fin]
    entrees = re.findall(r'<li\s+id="([^"]+)"[^>]*>([\s\S]*?)</li>', section)
    groupes = {}
    ordre = []
    carte = {}
    for ident, corps_li in entrees:
        cle, url = cle_source(ident, corps_li)
        if cle not in groupes:
            groupes[cle] = {"url": url, "ids": []}
            ordre.append(cle)
        elif url and not groupes[cle]["url"]:
            groupes[cle]["url"] = url
        groupes[cle]["ids"].append(ident)
    canon = {}
    vus = set()
    for cle in ordre:
        if cle[0] == "aips":
            base = f"sb-aips-{cle[1]}"
        else:
            base = re.sub(r"-\d+$", "", groupes[cle]["ids"][0])
        ident = base
        n = 2
        while ident in vus:
            ident = f"{base}-{n}"
            n += 1
        vus.add(ident)
        canon[cle] = ident
        for ancien in groupes[cle]["ids"]:
            carte[ancien] = ident

    def remplace_href(match):
        ancien = match.group(1)
        nouveau = carte.get(ancien, ancien)
        visible = nouveau.split("-")[-1] if nouveau.startswith("sb-aips-") else nouveau.removeprefix("sb-")
        return f'href="#{nouveau}">{visible}'

    html = re.sub(r'href="#(sb-[^"]+)">[^<]*', remplace_href, html)
    m = re.search(r'<section class="ilot" id="[^"]*sources"', html)
    fin = fin_balise(html, m.start())
    section = html[m.start():fin]
    h3 = re.search(r"<h3\b[^>]*>.*?</h3>", section, re.S).group(0)
    avert = re.search(r"<p class=\"p\">.*?</p>\s*$", section, re.S)
    dates = dates_aips()
    items = []
    for cle in ordre:
        url = groupes[cle]["url"]
        items.append(f'<li id="{canon[cle]}">{e(libelle_source(cle, url, dates))}</li>')
    nouveau = section[:section.find(">") + 1] + h3 + "<ol>" + "".join(items) + "</ol>"
    if avert:
        nouveau += avert.group(0)
    nouveau += "</section>"
    return html[:m.start()] + nouveau + html[fin:]


def figure(meta, titre, presentation, reperes, pieges, decision, avant, apres, guide):
    w, h = meta["w"], meta["h"]
    fichier = meta["fichier"]
    marques = []
    lecture = []
    for i, (x, y, phrase) in enumerate(reperes, 1):
        lettre = "ABCDEF"[i - 1]
        cx, cy = x * w / 100, y * h / 100
        r = max(w, h) * 0.035
        marques.append(
            f'<circle cx="{cx:.0f}" cy="{cy:.0f}" r="{r:.0f}" fill="none" stroke="#9b1c1c" '
            f'stroke-width="{max(w, h) * 0.006:.1f}"/>'
            f'<text x="{cx + r:.0f}" y="{cy:.0f}" font-size="{max(w, h) * 0.045:.0f}" '
            f'font-weight="700" fill="#9b1c1c">{lettre}</text>'
        )
        lecture.append(f"<li>{e(phrase)}</li>")
    piege = "".join(f"<li>{e(p)}</li>" for p in pieges)
    return f'''<figure class="cliche-guide"><p class="p">{e(presentation)}</p>
<div class="paire"><div><img src="{fichier}" width="{w}" height="{h}" alt="{e(titre)}, cliché brut" loading="lazy"><p class="p">{e(avant)}</p></div>
<div><svg viewBox="0 0 {w} {h}" role="img" aria-label="{e(titre)}, copie annotée"><image href="{fichier}" width="{w}" height="{h}"/>{''.join(marques)}</svg><p class="p">{e(apres)}</p></div></div>
<div class="p">{e(guide)}<ol>{''.join(lecture)}</ol></div>
<div class="p"><b>Pièges.</b><ul>{piege}</ul></div>
<p class="p"><b>Ce que l'image décide.</b> {e(decision)}</p>
<figcaption>Image : {e(meta['auteur'])}, {e(meta['licence'])}, <a href="{e(meta['url'])}">{e(meta['titre'])}</a>, consultée le {meta['consulte']}. La copie annotée est une œuvre dérivée sous la même licence.</figcaption></figure>'''


def charger_meta(nom):
    return json.loads((IMAGES / nom).read_text(encoding="utf-8"))


def inserer_figures(html, prefixe):
    conduction = charger_meta("2019_Cardiac_ConductionN.json")
    if prefixe == "pa":
        reperes = [
            (16, 40, "Le temps marqué au départ lance l'influx, avant toute contraction visible des cavités."),
            (84, 30, "Les oreillettes s'activent ensuite, ce qui précède le passage vers les ventricules."),
            (50, 88, "Les ventricules s'activent en dernier, et c'est alors que le pouls peut être perçu."),
        ]
        decision = (
            "Une palpitation correspond à une rupture de cette séquence, par un battement prématuré, "
            "une accélération ou une pause, et le tracé doit la documenter."
        )
        fig = figure(
            conduction,
            "Séquence de la conduction cardiaque",
            "Ce schéma en couleur montre six temps de la conduction, du départ de l'influx jusqu'aux ventricules.",
            reperes,
            ["Le dessin ne montre pas un tracé, donc il ne nomme pas l'arythmie en cause."],
            decision,
            "Le cycle se parcourt d'abord sans lettres, afin de voir à quel moment les ventricules s'activent.",
            "Les lettres nomment ensuite le départ de l'influx, l'activation des oreillettes et celle des ventricules.",
            "La lecture du schéma suit le cycle, depuis le départ de l'influx jusqu'aux ventricules.",
        )
        phrase = (
            "La séquence normale de l'influx, du départ jusqu'aux ventricules, se voit sur le "
            '<a class="ouvre" href="#f-pa-p3-schema">schéma de la conduction</a>, '
            "car une palpitation naît quand cette séquence se rompt."
        )
        ident, lib = "f-pa-p3-schema", "Schéma de la conduction"
        ecg = charger_meta("RVOT_Tachycardia.json")
        reperes_ecg = [
            (18, 42, "Les dérivations des membres montrent des complexes larges et rapides, sans retour à un aspect fin."),
            (62, 18, "En V1 le complexe reste large, ce qui empêche de conclure à une tachycardie supraventriculaire simple."),
            (62, 72, "Les précordiales gardent le même aspect large, et le doute doit être traité comme ventriculaire."),
        ]
        fig_ecg = figure(
            ecg,
            "Tachycardie à complexes larges",
            "Cet électrocardiogramme est publié comme une tachycardie ventriculaire monomorphe de la chambre de chasse droite.",
            reperes_ecg,
            [
                "La légende du fichier parle de chambre de chasse, mais le seul aspect large ne localise pas le foyer.",
                "Aucun nom de patient n'est lisible sur le tracé.",
            ],
            "Un complexe large et rapide se traite comme une tachycardie ventriculaire tant que le doute n'est pas levé, parce qu'un bloqueur du nœud serait dangereux.",
            "Le tracé brut montre des complexes larges dans plusieurs dérivations, avant toute lettre de lecture.",
            "Les lettres posées sur ce tracé désignent les dérivations des membres, puis V1 et les précordiales.",
            "Ces lettres montrent où le complexe reste large, des membres jusqu'aux précordiales.",
        )
        phrase_ecg = (
            "Le tracé qui doit alerter est la tachycardie à complexes larges, montrée sur "
            '<a class="ouvre" href="#f-pa-p9-trace">l\'électrocardiogramme de référence</a>, '
            "car un doute se traite comme une origine ventriculaire."
        )
        ident_ecg, lib_ecg = "f-pa-p9-trace", "Électrocardiogramme de référence"
    else:
        reperes = [
            (16, 40, "L'influx normal part d'en haut, alors qu'une extrasystole ventriculaire naît dans le muscle ventriculaire."),
            (84, 62, "Le faisceau descend dans le septum avant les ventricules, ce que l'extrasystole court-circuite."),
            (50, 88, "L'activation ventriculaire termine le cycle normal, et un battement prématuré la devance."),
        ]
        fig = figure(
            conduction,
            "Où naît l'extrasystole ventriculaire",
            "Le même schéma montre où naît un battement parti du muscle ventriculaire, hors du trajet normal.",
            reperes,
            ["Le schéma ne distingue pas une extrasystole idiopathique d'une extrasystole sur cardiopathie."],
            "Le diagnostic d'extrasystole ventriculaire exige le tracé du battement prématuré, puis l'exclusion d'une cardiopathie.",
            "Le cycle complet montre les ventricules activés en dernier, avant que les lettres ne les nomment.",
            "Les lettres de ce second schéma distinguent le départ normal, la descente septale et le ventricule.",
            "Cette lecture montre le trajet ordinaire, afin de situer l'extrasystole qui le court-circuite.",
        )
        phrase = (
            "L'extrasystole ventriculaire naît en aval du nœud, ce que situe le "
            '<a class="ouvre" href="#f-dx1-p3-schema">schéma de la conduction</a>, '
            "car l'influx normal n'atteint les ventricules qu'en dernier."
        )
        ident, lib = "f-dx1-p3-schema", "Schéma de la conduction"
        ecg = charger_meta("Extrasistole_isolata.json")
        reperes_ecg = [
            (28, 18, "Le complexe étroit précède le battement prématuré et sert de repère de largeur normale."),
            (52, 20, "Le complexe large et précoce de V1 est l'extrasystole, différent du complexe sinusal voisin."),
            (70, 22, "La ligne isoélectrique qui suit est la pause, et elle explique la sensation de battement manqué."),
        ]
        fig_ecg = figure(
            ecg,
            "Extrasystole ventriculaire en précordiales",
            "Ce tracé des dérivations précordiales montre un battement prématuré large, puis la pause qui le suit.",
            reperes_ecg,
            [
                "Un seul battement large ne quantifie pas la charge sur vingt-quatre heures.",
                "Le tracé ne porte aucun identifiant de patient.",
            ],
            "Ce battement large et prématuré documente l'extrasystole, mais il ne dispense pas de chercher une cardiopathie si la charge ou les symptômes l'exigent.",
            "Le tracé brut montre le complexe étroit, puis le battement large et la pause qui le suit.",
            "Les lettres de ce tracé séparent le complexe sinusal, l'extrasystole large et la pause compensatrice.",
            "Cette lecture montre le battement large, puis la pause qui explique la sensation de saut.",
        )
        phrase_ecg = (
            "L'aspect du battement prématuré large, puis la pause qui le suit, se lisent sur "
            '<a class="ouvre" href="#f-dx1-p9-trace">le tracé de l\'extrasystole</a>, '
            "car le diagnostic reste électrocardiographique."
        )
        ident_ecg, lib_ecg = "f-dx1-p9-trace", "Tracé de l'extrasystole"
    for phrase_i, ident_i, lib_i, fig_i, point in (
        (phrase, ident, lib, fig, 3),
        (phrase_ecg, ident_ecg, lib_ecg, fig_ecg, 9),
    ):
        assert 12 <= mots(texte(phrase_i)) <= 32, (point, mots(texte(phrase_i)), texte(phrase_i))
        bloc = f'<div class="p">{phrase_i}</div>' + fenetre(ident_i, lib_i, fig_i)
        html = re.sub(
            rf'(<h3 id="{prefixe}-p{point}">.*?</h3>)',
            r"\1" + bloc,
            html,
            count=1,
            flags=re.S,
        )
    return html


def traiter_fichier(nom):
    prefixe = FICHIERS[nom]
    source = (ORIG / nom).read_text(encoding="utf-8")
    source = retitrer(source, prefixe)
    source = extraire_divs_popover(source)
    sortie = []
    i = 0
    motif = re.compile(r'<section class="ilot" id="(bloc-[^"]+)">')
    deplace = ""
    while True:
        m = motif.search(source, i)
        if not m:
            sortie.append(source[i:])
            break
        sortie.append(source[i:m.start()])
        fin = fin_balise(source, m.start())
        section = source[m.start():fin]
        numero = re.search(r"bloc-" + prefixe + r"-(\d+)", m.group(1))
        n = int(numero.group(1)) if numero else 0
        if n == 1:
            section, deplace = sortir_semantique(section, prefixe)
        section = envelopper_regions(section, prefixe, n)
        if n == 4:
            section = inserer_dans_point4(section, prefixe, deplace)
        sortie.append(section)
        i = fin
    html_out = "".join(sortie)
    html_out = inserer_figures(html_out, prefixe)
    html_out = consolider_sources(html_out)
    html_out = html_out.replace(
        "car aucune source lue ne les chiffre comme causes de palpitations.",
        "car ils entrent dans la tachycardie sinusale secondaire.",
    )
    # Ancre identique collée deux fois de suite : la seconde ne porte aucun fait de plus.
    html_out = re.sub(
        r'(<sup class="r"><a href="#[^"]+">[^<]*</a></sup>)\1+',
        r"\1",
        html_out,
    )
    fin = html_out.rstrip()
    if "FIN_FICHIER" not in fin[-400:]:
        raise RuntimeError("FIN_FICHIER perdu : " + fin[-180:])
    dest = RACINE / nom
    dest.write_text(html_out, encoding="utf-8")
    print(nom, "octets", len(html_out.encode()), "fenêtres", html_out.count('class="fenetre'))


if __name__ == "__main__":
    for nom in FICHIERS:
        traiter_fichier(nom)
