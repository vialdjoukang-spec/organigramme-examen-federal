#!/usr/bin/env python3
"""Renfort L1 de la Phase A et du DX.1 (LOT_048). Ne touche pas au texte médical hors déplacements,
redites de bibliographie et phrases exigées par les fenêtres. Prompt L1 lu et appliqué."""
import html
import json
import re
import subprocess
import sys
from pathlib import Path

RACINE = Path(__file__).resolve().parents[3]
LOT = RACINE / "Claude" / "LOT_048"
sys.path.insert(0, str(RACINE / "Claude" / "_outils"))
import cliche  # noqa: E402

MAJ = {
    "55609": "juin 2026",
    "56313": "septembre 2023",
    "59834": "septembre 2026",
    "57801": "novembre 2024",
    "55090": "juin 2026",
    "66999": "décembre 2022",
    "49503": "juillet 2026",
    "44772": "décembre 2025",
    "49188": "janvier 2026",
    "53668": "décembre 2025",
    "65165": "juillet 2023",
    "57386": "juillet 2023",
}
AIPS_NOM = {
    "55609": "AIPS Nexium® (ésoméprazole), Swissmedic 55609",
    "56313": "AIPS Omeprazol Zentiva® (oméprazole), Swissmedic 56313",
    "59834": "AIPS Pantoprazol-Mepha Teva® (pantoprazole), Swissmedic 59834",
    "57801": "AIPS Lansoprazol Zentiva® (lansoprazole), Swissmedic 57801",
    "55090": "AIPS Pariet® (rabéprazole), Swissmedic 55090",
    "66999": "AIPS Jorveza® (budésonide), Swissmedic 66999",
    "49503": "AIPS Diflucan® (fluconazole), Swissmedic 49503",
    "44772": "AIPS Zovirax® i.v. (aciclovir), Swissmedic 44772",
    "49188": "AIPS Cymevene® (ganciclovir), Swissmedic 49188",
    "53668": "AIPS Acyclovir-Mepha® (aciclovir), Swissmedic 53668",
    "65165": "AIPS Binosto® (alendronate), Swissmedic 65165",
    "57386": "AIPS Fosavance® (alendronate et cholécalciférol), Swissmedic 57386",
}
# URL canonique remplaçant l'URL d'extraction doublée (même article).
SOURCES = {
    "12269739": ("UEG et ESNM, recommandations sur la dysphagie, 2025", "https://pmc.ncbi.nlm.nih.gov/articles/PMC12269739/"),
    "7005998": ("UEG et ESNM, recommandations sur l'achalasie, 2020", "https://pmc.ncbi.nlm.nih.gov/articles/PMC7005998/"),
    "10759704": ("Terkelsen et al., obstruction alimentaire œsophagienne, 2024", "https://pmc.ncbi.nlm.nih.gov/articles/PMC10759704/"),
    "5063605": ("ESSD et EUGMS, dysphagie oropharyngée du sujet âgé, 2016", "https://pmc.ncbi.nlm.nih.gov/articles/PMC5063605/"),
    "13719356": ("Selg et al., incidence de la dysphagie après accident vasculaire", "https://pmc.ncbi.nlm.nih.gov/articles/PMC13719356/"),
    "8564153": ("ESO et ESSD, dysphagie après accident vasculaire, 2021", "https://pmc.ncbi.nlm.nih.gov/articles/PMC8564153/"),
    "5412545": ("Lee et al., signes d'alarme et cancers digestifs hauts, 2017", "https://pmc.ncbi.nlm.nih.gov/articles/PMC5412545/"),
    "5415218": ("Lucendo et al., recommandations sur l'œsophagite à éosinophiles, 2017", "https://pmc.ncbi.nlm.nih.gov/articles/PMC5415218/"),
    "10846564": ("Gyawali et al., consensus de Lyon 2.0 sur le reflux, 2024", "https://pmc.ncbi.nlm.nih.gov/articles/PMC10846564/"),
    "5969363": ("Sami et al., recommandations britanniques sur la dilatation œsophagienne, 2018", "https://pmc.ncbi.nlm.nih.gov/articles/PMC5969363/"),
    "12780910": ("Huh et al., mise à jour du consensus de Séoul sur le reflux, 2026", "https://pmc.ncbi.nlm.nih.gov/articles/PMC12780910/"),
    "9944358": ("Li et al., chirurgie antireflux ou IPP dans la sténose peptique, 2023", "https://pmc.ncbi.nlm.nih.gov/articles/PMC9944358/"),
    "8079876": ("Boregowda et al., sténoses œsophagiennes bénignes réfractaires, 2021", "https://pmc.ncbi.nlm.nih.gov/articles/PMC8079876/"),
    "42934940": ("Recommandations européennes sur l'œsophagite à éosinophiles, 2026", "https://pubmed.ncbi.nlm.nih.gov/42934940/"),
    "26862844": ("ESGE, retrait des corps étrangers du tube digestif haut, 2016", "https://pubmed.ncbi.nlm.nih.gov/26862844/"),
    "34913965": ("Épidémiologie du diverticule de Zenker dans un système de santé, 2022", "https://pubmed.ncbi.nlm.nih.gov/34913965/"),
    "41361129": ("Troubles de la déglutition dans la myasthénie, revue, 2026", "https://pubmed.ncbi.nlm.nih.gov/41361129/"),
    "19392845": ("Zografos et al., œsophagite médicamenteuse, 2009", "https://pubmed.ncbi.nlm.nih.gov/19392845/"),
    "35914638": ("ESMO, cancer de l'œsophage, 2022", "https://pubmed.ncbi.nlm.nih.gov/35914638/"),
    "32375192": ("ESGE, endoscopie des troubles moteurs digestifs, 2020", "https://pubmed.ncbi.nlm.nih.gov/32375192/"),
    "28232473": ("Prévalence mondiale des symptômes de reflux, méta-analyse, 2018", "https://pubmed.ncbi.nlm.nih.gov/28232473/"),
    "37813356": ("ESGE, diagnostic et prise en charge de l'endobrachyœsophage, 2023", "https://pubmed.ncbi.nlm.nih.gov/37813356/"),
    "32732370": ("Prévalence mondiale de l'endobrachyœsophage chez les patients refluants, 2021", "https://pubmed.ncbi.nlm.nih.gov/32732370/"),
    "29037470": ("Physiopathologie de la maladie de reflux, 2018", "https://pubmed.ncbi.nlm.nih.gov/29037470/"),
    "19439958": ("Sténose peptique de l'œsophage, traitement médical, 2009", "https://pubmed.ncbi.nlm.nih.gov/19439958/"),
}


def mots(s):
    return re.findall(r"[A-Za-zÀ-ÿ0-9''’-]+", s)


def exiger(phrase, lo=12, hi=28):
    n = len(mots(phrase))
    if not lo <= n <= hi:
        raise SystemExit(f"{n} mots : {phrase}")
    return phrase


def fin_balise(h, debut, nom):
    prof = 0
    for m in re.finditer(rf"<(/?){nom}\b[^>]*>", h[debut:], re.I):
        prof += -1 if m.group(1) else 1
        if prof == 0:
            return debut + m.end()
    raise SystemExit(f"balise {nom} non fermée")


def convertir_popovers(h):
    h = re.sub(
        r'<button class="w" popovertarget="([^"]+)">(.*?)</button>',
        r'<a class="ouvre" href="#\1">\2</a>',
        h,
        flags=re.S,
    )
    out, i = [], 0
    while True:
        j = h.find("<div ", i)
        if j < 0:
            out.append(h[i:])
            break
        k = h.find(">", j)
        ouvrant = h[j : k + 1]
        if "popover" not in ouvrant or "fenetre" not in ouvrant:
            out.append(h[i : j + 5])
            i = j + 5
            continue
        ident = re.search(r'id="([^"]+)"', ouvrant).group(1)
        fin = fin_balise(h, j, "div")
        inner = h[k + 1 : fin - len("</div>")]
        fort = re.search(r"<strong>(.*?)</strong>", inner, re.S)
        aria = re.sub(r"<[^>]+>", "", fort.group(1) if fort else ident)
        aria = re.sub(r"\s+", " ", aria).strip()[:70].replace('"', "")
        bloc = (
            f'<section class="fenetre" id="{ident}" role="dialog" aria-label="{html.escape(aria)}">'
            f'<div class="fen"><a class="fermer" href="#" aria-label="Fermer">Fermer ✕</a>{inner}</div></section>'
        )
        out.append(h[i:j])
        out.append(bloc)
        i = fin
    return "".join(out)


def deplacer(h, debut, fin_exclusive, ancre_insertion, nouveau_debut=""):
    a = h.find(debut)
    if a < 0:
        raise SystemExit("introuvable " + debut[:60])
    b = h.find(fin_exclusive, a)
    if b < 0:
        raise SystemExit("fin introuvable " + fin_exclusive[:60])
    bloc = nouveau_debut + h[a:b]
    h = h[:a] + h[b:]
    c = h.find(ancre_insertion)
    if c < 0:
        raise SystemExit("ancre introuvable " + ancre_insertion[:60])
    return h[:c] + bloc + h[c:]


def limiter_car(h, maximum=15):
    i = h.find(">Sources<")
    corps, src = h[:i], h[i:]
    parts = corps.split(", car ")
    if len(parts) - 1 <= maximum:
        return h
    out = parts[0]
    for n, p in enumerate(parts[1:], 1):
        out += (", car " if n <= maximum else " parce que ") + p
    return out + src


def canon_url(u):
    u = html.unescape(u)
    m = re.search(r"[?&]id=(\d+)", u)
    if m and m.group(1) in SOURCES:
        return SOURCES[m.group(1)]
    if "swissheart.ch" in u:
        return ("Fondation Suisse de Cardiologie, dossier accident vasculaire, 2020", u)
    if "bfs.admin.ch" in u or "dam-api.bfs" in u:
        return ("Office fédéral de la statistique, jeu de données cancers", u)
    if "revmed.ch" in u and "2026" in u:
        return ("Revue Médicale Suisse, reflux gastro-œsophagien, 2026", u.split("?")[0])
    if "revmed.ch" in u and "2024" in u:
        return ("Revue Médicale Suisse, maladie de reflux, 2024", u.split("?")[0])
    if "files.refdata.ch" in u:
        num = re.search(r"aips-(\d+)", "")  # rempli par l'identifiant
        return None
    return None


def recrire_biblio(h):
    def une(m):
        ident, corps = m.group(1), m.group(2)
        urls = re.findall(r"https://[^<\s\"]+", corps)
        date = "2026-11-10"
        d = re.search(r"consulté le (\d{4}-\d{2}-\d{2})", corps)
        if d:
            date = d.group(1)
        num = re.search(r"aips-(\d+)", ident)
        if num and urls:
            n = num.group(1)
            url = html.unescape(urls[-1])
            lib = AIPS_NOM.get(n, f"AIPS Swissmedic {n}")
            maj = MAJ.get(n, "")
            extra = f", mise à jour {maj}" if maj else ""
            return f'<li id="{ident}">{lib}{extra} — {url} (consulté le {date})</li>'
        info = None
        for u in urls:
            cle = re.search(r"[?&]id=(\d+)", html.unescape(u))
            if cle and cle.group(1) in SOURCES:
                info = SOURCES[cle.group(1)]
                break
            info = canon_url(html.unescape(u)) or info
        if not info and urls:
            url = html.unescape(urls[-1])
            lib = re.sub(r"<[^>]+>", "", corps)
            lib = re.sub(r"https://\S+", "", lib)
            lib = re.sub(r"\s+", " ", lib).strip(" —")[:90] or "Source citée"
            info = (lib, url)
        if not info:
            return m.group(0)
        lib, url = info
        return f'<li id="{ident}">{lib} — {url} (consulté le {date})</li>'

    return re.sub(r'<li id="([^"]+)">(.*?)</li>', une, h, flags=re.S)


def ajouter_ancre_molecule(h):
    """Une entrée sans suffixe d'extrait, lue par aips_fiche.py."""
    blocs = []
    for n, lib in AIPS_NOM.items():
        if f'id="sb-aips-{n}"' in h:
            continue
        m = re.search(rf'id="sb-aips-{n}-\d+"[^>]*>.*?https://[^<\s"]+', h, re.S)
        if not m:
            continue
        url = re.search(r"https://[^<\s\"]+", m.group(0)).group(0)
        url = html.unescape(url)
        blocs.append(
            f'<li id="sb-aips-{n}">{lib}, mise à jour {MAJ[n]} — {url} (consulté le 2026-11-15)</li>'
        )
    if not blocs:
        return h
    return h.replace("</ol>", "\n" + "\n".join(blocs) + "\n</ol>", 1)


def habiller_regions(h, id_h3, ouvertures):
    m = re.search(rf'(<h3 id="{id_h3}"[^>]*>.*?</h3>)', h, re.S)
    if not m:
        raise SystemExit("h3 absent " + id_h3)
    debut = m.end()
    nxt = re.search(r"<h3 id=", h[debut:])
    fin = debut + nxt.start()
    bloc = h[debut:fin]
    parts = re.split(r"(<h4>.*?</h4>)", bloc, flags=re.S)
    out = [parts[0]]
    k = 0
    i = 1
    while i < len(parts):
        titre = parts[i]
        corps = parts[i + 1] if i + 1 < len(parts) else ""
        k += 1
        if k > len(ouvertures):
            raise SystemExit(f"ouverture manquante {id_h3} région {k}")
        fid = f"f-{id_h3}-r{k}"
        phrase = ouvertures[k - 1]
        mot = re.search(r"\[\[(.+?)\]\]", phrase).group(1)
        visible = phrase.replace(f"[[{mot}]]", f'<a class="ouvre" href="#{fid}">{mot}</a>', 1)
        exiger(re.sub(r"\[\[|\]\]", "", phrase))
        aria = re.sub(r"<[^>]+>", "", titre)
        aria = re.sub(r"\s+", " ", aria).strip()[:70]
        fen = (
            f'<section class="fenetre" id="{fid}" role="dialog" aria-label="{html.escape(aria)}">'
            f'<div class="fen"><a class="fermer" href="#" aria-label="Fermer">Fermer ✕</a>{corps}</div></section>'
        )
        out.append(titre + f'<div class="p">{visible}</div>\n' + fen + "\n")
        i += 2
    if k != len(ouvertures):
        raise SystemExit(f"{id_h3} : {k} régions, {len(ouvertures)} ouvertures")
    return h[:debut] + "".join(out) + h[fin:]


def figure_html(meta, titre, legende, reperes, pieges, decision):
    for p in [legende, decision, *pieges, *[r[2] for r in reperes]]:
        exiger(p)
    import io
    from contextlib import redirect_stdout

    ns = type("N", (), {})()
    ns.meta = str(meta)
    ns.titre = titre
    ns.cliche = legende
    ns.reperes = json.dumps(reperes, ensure_ascii=False)
    ns.pieges = json.dumps(pieges, ensure_ascii=False)
    ns.decision = decision
    buf = io.StringIO()
    with redirect_stdout(buf):
        cliche.figure(ns)
    bloc = buf.getvalue()
    bloc = bloc.replace(
        "Lisez d'abord seul ce cliché",
        "Le cliché brut se lit avant les repères numérotés",
    )
    bloc = bloc.replace(" : cherchez vous-même le signe.", ".")
    bloc = bloc.replace("numérote les repères décrits ci-dessous.", "porte les repères numérotés de la lecture guidée.")
    return bloc


def fenetre_figure(fid, aria, figure):
    return (
        f'<section class="fenetre" id="{fid}" role="dialog" aria-label="{html.escape(aria)}">'
        f'<div class="fen"><a class="fermer" href="#" aria-label="Fermer">Fermer ✕</a>{figure}</div></section>'
    )


def inserer_apres_h3(h, id_h3, html_ajout):
    m = re.search(rf'<h3 id="{id_h3}"[^>]*>.*?</h3>', h, re.S)
    if not m:
        raise SystemExit(id_h3)
    return h[: m.end()] + html_ajout + h[m.end() :]


def carte(fid, aria, lignes):
    trs = "".join(f"<tr><th>{a}</th><td>{b}</td></tr>" for a, b in lignes)
    return (
        f'<section class="fenetre mb" id="{fid}" role="dialog" aria-label="{html.escape(aria)}">'
        f'<div class="fen"><a class="fermer" href="#" aria-label="Fermer">Fermer ✕</a><h4>{aria}</h4>'
        f'<div class="t" style="overflow-x:auto"><table>{trs}</table></div></div></section>'
    )


def citer(n, texte):
    return f'{texte}<sup class="r"><a href="#sb-aips-{n}">{n}</a></sup>'


def lier_premiere(h, mot, fid):
    a = h.find(">Sources<")
    corps, src = h[:a], h[a:]
    i = corps.find(mot)
    if i < 0:
        raise SystemExit("molécule introuvable " + mot)
    lien = f'<a class="ouvre" href="#{fid}">{mot}</a>'
    return corps[:i] + lien + corps[i + len(mot) :] + src


def cartes_phase_a():
    n = "55609"
    c = []
    c.append(carte("f-pa-m-nexium", "Ésoméprazole — Nexium® (n° 55609)", [
        ("Indication et dose", citer(n, "Œsophagite de reflux : 40 mg, 1 fois par jour, durant 4 semaines. L'entretien des récidives utilise 20 mg une fois par jour.")),
        ("Contre-indications", citer(n, "« Hypersensibilité connue à l'ésoméprazole, aux benzimidazoles substitués ou aux autres constituants des comprimés. »")),
        ("Grossesse", citer(n, "« La prudence est de mise en cas d'emploi pendant la grossesse. »")),
        ("Allaitement", citer(n, "« Nexium ne doit donc pas être utilisé pendant l'allaitement. »")),
    ]))
    n = "56313"
    c.append(carte("f-pa-m-omeprazole", "Oméprazole — Omeprazol Zentiva® (n° 56313)", [
        ("Indication et dose", citer(n, "L'œsophagite de reflux de l'adulte se traite à 20 mg une fois par jour, et à 40 mg si la réponse aux autres traitements est insuffisante.")),
        ("Contre-indications", citer(n, "« Hypersensibilité connue à l'oméprazole aux benzimidazoles substitués ou à un autre constituant du comprimé. »")),
        ("Grossesse", citer(n, "« Comme il n'existe pas d'études contrôlées menées chez des femmes enceintes, il faut être prudent lors de l'utilisation de ces médicaments pendant la grossesse. »")),
        ("Allaitement", citer(n, "« L'oméprazole passe en faible quantité dans le lait maternel, mais il est inactivé par l'acide contenu dans l'estomac du nouveau-né. »")),
    ]))
    n = "59834"
    c.append(carte("f-pa-m-pantoprazole", "Pantoprazole — Pantoprazol-Mepha Teva® (n° 59834)", [
        ("Indication et dose", citer(n, "L'œsophagite de reflux se traite par un comprimé de 40 mg par jour, et cette dose peut être doublée si l'œsophagite persiste.")),
        ("Contre-indications", citer(n, "« Pantoprazol-Mepha Teva ne doit pas être administré en cas d'hypersensibilité connue au principe actif, aux benzimidazoles substitués ou à l'un de ses composants. »")),
        ("Grossesse", citer(n, "« Pantoprazol-Mepha Teva ne doit pas être administré pendant la grossesse sauf en cas d'absolue nécessité. »")),
        ("Allaitement", citer(n, "« Chez l'être humain, des cas de passage du pantoprazole dans le lait maternel ont été signalés. »")),
    ]))
    n = "66999"
    c.append(carte("f-pa-m-jorveza", "Budésonide — Jorveza® (n° 66999)", [
        ("Indication et dose", citer(n, "L'œsophagite à éosinophiles de l'adulte se traite par 1 mg matin et soir pendant 6 semaines, et l'entretien utilise 0,5 mg ou 1 mg matin et soir.")),
        ("Contre-indications", citer(n, "« Hypersensibilité au principe actif ou à l'un des excipients selon la composition. »")),
        ("Grossesse", citer(n, "« Pendant la grossesse, l'administration doit être évitée sauf en présence d'arguments solides pouvant justifier le traitement par Jorveza. »")),
        ("Allaitement", citer(n, "« Il faut décider soit d'interrompre l'allaitement, soit d'interrompre/de s'abstenir du traitement par le budésonide. »")),
    ]))
    n = "49503"
    c.append(carte("f-pa-m-diflucan", "Fluconazole — Diflucan® (n° 49503)", [
        ("Indication et dose", citer(n, "La candidose œsophagienne commence par 200 à 400 mg le premier jour, puis 100 à 200 mg une fois par jour pendant 14 à 30 jours.")),
        ("Contre-indications", citer(n, "« Hypersensibilité connue au fluconazole ou à l'un des excipients de Diflucan, ainsi qu'à d'autres dérivés azolés. »")),
        ("Grossesse", citer(n, "« L'utilisation du fluconazole pendant la grossesse doit être évitée sauf si, en présence d'une infection fongique sévère ou potentiellement létale, les bénéfices attendus du fluconazole l'emportent sur les risques encourus par le fœtus. »")),
        ("Allaitement", citer(n, "« Il est déconseillé d'allaiter pendant l'utilisation de fluconazole, en particulier à des doses élevées. » Les patients présentant une intolérance au galactose, un déficit total en lactase ou un syndrome de malabsorption du glucose et du galactose (maladies héréditaires rares) ne doivent pas prendre ce médicament.")),
    ]))
    n = "44772"
    c.append(carte("f-pa-m-zovirax", "Aciclovir intraveineux — Zovirax® i.v. (n° 44772)", [
        ("Indication et dose", citer(n, "L'infection des muqueuses à Herpes simplex de l'adulte se perfuse en une heure, à 5 mg/kg toutes les 8 heures.")),
        ("Contre-indications", citer(n, "« Zovirax est contre-indiqué en cas d'hypersensibilité connue à l'aciclovir et au valaciclovir. »")),
        ("Grossesse", citer(n, "« Néanmoins, pendant la grossesse, le traitement intraveineux et oral n'est indiqué qu'en cas de nécessité impérieuse. »")),
        ("Allaitement", citer(n, "« Pour cette raison, il ne faut pas allaiter pendant un traitement par Zovirax. »")),
    ]))
    n = "49188"
    c.append(carte("f-pa-m-cymevene", "Ganciclovir — Cymevene® (n° 49188)", [
        ("Indication et dose", citer(n, "L'infection à cytomégalovirus de l'adulte immunodéprimé se traite par 5 mg/kg en perfusion d'une heure, toutes les 12 heures.")),
        ("Contre-indications", citer(n, "« Pendant la grossesse et l'allaitement ainsi que chez l'homme désireux de procréer, Cymevene est contre-indiqué. »")),
        ("Grossesse", citer(n, "« Cymevene ne doit pas être administré pendant la grossesse sauf si le bénéfice thérapeutique pour la mère l'emporte sur le risque tératogène potentiel pour l'enfant. »")),
        ("Allaitement", citer(n, "« Pendant la grossesse et l'allaitement ainsi que chez l'homme désireux de procréer, Cymevene est contre-indiqué. »")),
    ]))
    return "\n".join(c)


def cartes_dx1():
    n = "55609"
    c = [carte("f-dx1-m-nexium", "Ésoméprazole — Nexium® (n° 55609)", [
        ("Indication et dose", citer(n, "Œsophagite de reflux : 40 mg, 1 fois par jour, durant 4 semaines. La prophylaxie des récidives utilise 20 mg une fois par jour.")),
        ("Contre-indications", citer(n, "« Hypersensibilité connue à l'ésoméprazole, aux benzimidazoles substitués ou aux autres constituants des comprimés. »")),
        ("Grossesse", citer(n, "« La prudence est de mise en cas d'emploi pendant la grossesse. »")),
        ("Allaitement", citer(n, "« Nexium ne doit donc pas être utilisé pendant l'allaitement. »")),
    ])]
    n = "59834"
    c.append(carte("f-dx1-m-pantoprazole", "Pantoprazole — Pantoprazol-Mepha Teva® (n° 59834)", [
        ("Indication et dose", citer(n, "L'œsophagite de reflux légère à moyennement grave se traite par 40 mg par jour, sans dépasser 40 mg chez le patient âgé ou insuffisant rénal.")),
        ("Contre-indications", citer(n, "« Pantoprazol-Mepha Teva ne doit pas être administré en cas d'hypersensibilité connue au principe actif, aux benzimidazoles substitués ou à l'un de ses composants. »")),
        ("Grossesse", citer(n, "« Pantoprazol-Mepha Teva ne doit pas être administré pendant la grossesse sauf en cas d'absolue nécessité. »")),
        ("Allaitement", citer(n, "« Chez l'être humain, des cas de passage du pantoprazole dans le lait maternel ont été signalés. »")),
    ]))
    n = "56313"
    c.append(carte("f-dx1-m-omeprazole", "Oméprazole — Omeprazol Zentiva® (n° 56313)", [
        ("Indication et dose", citer(n, "L'œsophagite de reflux se traite à 20 mg une fois par jour, puis à 40 mg une fois par jour si les autres traitements n'ont pas suffi.")),
        ("Contre-indications", citer(n, "« Hypersensibilité connue à l'oméprazole aux benzimidazoles substitués ou à un autre constituant du comprimé. »")),
        ("Grossesse", citer(n, "« Comme il n'existe pas d'études contrôlées menées chez des femmes enceintes, il faut être prudent lors de l'utilisation de ces médicaments pendant la grossesse. »")),
        ("Allaitement", citer(n, "« L'oméprazole passe en faible quantité dans le lait maternel, mais il est inactivé par l'acide contenu dans l'estomac du nouveau-né. »")),
    ]))
    n = "57801"
    c.append(carte("f-dx1-m-lansoprazole", "Lansoprazole — Lansoprazol Zentiva® (n° 57801)", [
        ("Indication et dose", citer(n, "L'œsophagite de reflux se traite en général par 30 mg une fois par jour.")),
        ("Contre-indications", citer(n, "« Hypersensibilité au lansoprazole ou à l'un des excipients conformément à la composition. »")),
        ("Grossesse", citer(n, "« Le médicament ne doit pas être administré pendant la grossesse, sauf en cas de nécessité absolue. »")),
        ("Allaitement", citer(n, "« L'utilisation de Lansoprazol Zentiva durant l'allaitement doit être évitée, sauf en cas de nécessité absolue. »")),
    ]))
    n = "55090"
    c.append(carte("f-dx1-m-pariet", "Rabéprazole — Pariet® (n° 55090)", [
        ("Indication et dose", citer(n, "L'œsophagite érosive ou ulcérative se traite par 10 à 20 mg une fois par jour pendant quatre à huit semaines.")),
        ("Contre-indications", citer(n, "« Pariet ne doit pas être utilisé en cas d'hypersensibilité connue au rabéprazole sodique ou à d'autres dérivés benzimidazoliques, ou encore à l'un des excipients de la préparation. »")),
        ("Grossesse", citer(n, "« Pariet doit donc être utilisé pendant la grossesse uniquement sur indication stricte. »")),
        ("Allaitement", citer(n, "« Pariet ne sera administré durant l'allaitement que lors d'indication stricte. »")),
    ]))
    return "\n".join(c)


def traiter_phase_a(h):
    h = convertir_popovers(h)
    h = h.replace("<strong>1. Définition et sémantique</strong>", "<strong>1. Définition</strong>")
    h = h.replace(
        "<title>LOT_048 — S2.9 — Passage difficile ou douloureux des aliments, dysphagie, régurgitation</title>",
        "<title>S2.9 — Passage difficile ou douloureux des aliments, dysphagie, régurgitation</title>",
    )
    h = h.replace(
        "<h2>LOT_048 — S2.9 — Passage difficile ou douloureux des aliments, dysphagie, régurgitation</h2>",
        "<h2>S2.9 — Passage difficile ou douloureux des aliments, dysphagie, régurgitation</h2>",
    )
    h = deplacer(
        h,
        "<h4><em>1.a Termes proches et termes à éviter</em></h4>",
        '<section class="ilot" id="pa-p2">',
        '<section class="ilot" id="pa-p8">',
        "",
    )
    h = h.replace(
        "<h4><em>1.a Termes proches et termes à éviter</em></h4>",
        "<h4><em>7.7 Termes proches qui imitent la dysphagie</em></h4>",
        1,
    )
    h = h.replace(
        "<h4><em>1.b Ce que la situation n'est pas</em></h4>",
        "<h4><em>7.8 Ce que cette plainte n'est pas</em></h4>",
        1,
    )
    # Le déplacement a mis 7.7/7.8 avant le point 8 : les rattacher au point 7.
    marque = "<h4><em>7.7 Termes proches qui imitent la dysphagie</em></h4>"
    a = h.find(marque)
    b = h.find('<section class="ilot" id="pa-p8">', a)
    bloc = h[a:b]
    h = h[:a] + h[b:]
    ancre = '<section class="ilot" id="pa-p8">'
    h = h.replace(ancre, bloc + ancre, 1)
    h = habiller_regions(h, "pa-h6", [
        "[[L'état nutritionnel]] s'apprécie avant le reste, parce qu'une perte de poids récente change l'urgence de l'endoscopie.",
        "[[L'examen neurologique]] vient ensuite, parce qu'un déficit aigu de la déglutition impose le jeûne et la filière vasculaire.",
        "[[La bouche et le cou]] se regardent région par région, parce qu'une lésion visible explique une dysphagie haute.",
        "[[Le thorax et l'abdomen]] ferment l'examen somatique, parce qu'une douleur projetée peut mimer une cause œsophagienne.",
        "[[L'épreuve de déglutition]] se fait avec une gorgée d'eau, parce qu'elle juge la toux et la voix avant de nourrir.",
    ])
    fig = figure_html(
        LOT / "images" / "2412_The_Esophagus.json",
        "Œsophage et ses deux sphincters",
        "Schéma sagittal de profil, tête à gauche, avec la trachée en avant de l'œsophage.",
        [
            [36, 46, "La trachée longe l'œsophage cervical, donc une fausse route haute atteint l'arbre aérien."],
            [70, 36, "Le sphincter supérieur ferme l'entrée de l'œsophage lorsque aucun bolus n'est engagé."],
            [62, 70, "Le sphincter inférieur sépare l'œsophage distal de l'estomac et s'oppose au reflux."],
        ],
        ["Les traits de la trachée ne doivent pas être lus comme la lumière de l'œsophage."],
        "Ce repérage distingue une plainte haute, au-dessus du sphincter supérieur, d'une plainte rétrosternale.",
    )
    phrase = exiger("Le schéma de l'œsophage place les deux sphincters, parce que la plainte se situe entre ces barrières.")
    lien = '<a class="ouvre" href="#f-pa-p3-schema">schéma de l\'œsophage</a>'
    bloc = '<div class="p">' + phrase.replace("schéma de l'œsophage", lien, 1) + "</div>"
    bloc += fenetre_figure("f-pa-p3-schema", "Œsophage et ses deux sphincters", fig)
    h = inserer_apres_h3(h, "pa-h3", bloc)
    fig2 = figure_html(
        LOT / "images" / "Aspiration_on_barium_swallow.json",
        "Aspiration au transit baryté",
        "Trois clichés de profil d'un transit œsophagien, avec une colonne barytée et un passage bronchique.",
        [
            [55, 42, "La colonne barytée du panneau central descend dans l'œsophage vers l'estomac."],
            [82, 40, "Le panneau droit montre le produit dans les bronches, ce qui signe une aspiration."],
        ],
        ["L'inscription technique du bord supérieur ne nomme pas le patient et ne se lit pas comme un diagnostic."],
        "Ce cliché sépare une colonne œsophagienne d'un passage bronchique, donc la plainte haute passe avant l'œsophage.",
    )
    phrase2 = exiger("Le transit baryté montre une aspiration lorsque le produit quitte l'œsophage vers les bronches.")
    bloc2 = (
        '<div class="p">'
        + phrase2.replace("transit baryté", '<a class="ouvre" href="#f-pa-p9-aspi">transit baryté</a>', 1)
        + "</div>"
        + fenetre_figure("f-pa-p9-aspi", "Aspiration au transit baryté", fig2)
    )
    h = inserer_apres_h3(h, "pa-h9", bloc2)
    h = h.replace('<section class="ilot" id="pa-p12">', cartes_phase_a() + '\n<section class="ilot" id="pa-p12">', 1)
    for mot, fid in [
        ("Nexium®", "f-pa-m-nexium"),
        ("Omeprazol Zentiva®", "f-pa-m-omeprazole"),
        ("Pantoprazol-Mepha Teva®", "f-pa-m-pantoprazole"),
        ("Jorveza®", "f-pa-m-jorveza"),
        ("Diflucan®", "f-pa-m-diflucan"),
        ("Zovirax®", "f-pa-m-zovirax"),
        ("Cymevene®", "f-pa-m-cymevene"),
    ]:
        h = lier_premiere(h, mot, fid)
    h = recrire_biblio(h)
    h = ajouter_ancre_molecule(h)
    h = limiter_car(h)
    return h


def traiter_dx1(h):
    h = convertir_popovers(h)
    h = h.replace("<strong>1. Définition et sémantique</strong>", "<strong>1. Définition</strong>")
    h = deplacer(
        h,
        "<h4><em>1.c Synonymes admis et termes à éviter</em></h4>",
        '<section class="ilot" id="dx1-p2">',
        '<section class="ilot" id="dx1-p9">',
    )
    h = h.replace(
        "<h4><em>1.c Synonymes admis et termes à éviter</em></h4>",
        "<h4><em>8.e Synonymes admis et termes à éviter</em></h4>",
        1,
    )
    h = h.replace(
        "<h4><em>1.d Ce que l'entité n'est pas</em></h4>",
        "<h4><em>8.f Ce que cette entité n'est pas</em></h4>",
        1,
    )
    marque = "<h4><em>8.e Synonymes admis et termes à éviter</em></h4>"
    a = h.find(marque)
    b = h.find('<section class="ilot" id="dx1-p9">', a)
    bloc = h[a:b]
    h = h[:a] + h[b:]
    h = h.replace('<section class="ilot" id="dx1-p9">', bloc + '<section class="ilot" id="dx1-p9">', 1)
    h = habiller_regions(h, "dx1-h6", [
        "[[L'examen au lit]] montre peu de signes, parce que l'œsophagite peptique reste invisible sans endoscope.",
        "[[Le poids]] se note à chaque visite, parce qu'un amaigrissement fait chercher une sténose serrée ou une tumeur.",
        "[[La bouche et le cou]] se palpent pour une cause haute, parce que le reflux n'y laisse aucune lésion muqueuse.",
        "[[Le thorax et l'abdomen]] se palpent sans différer, parce qu'une défense abdominale impose un avis en urgence.",
    ])
    fig = figure_html(
        LOT / "images" / "GERD.json",
        "Barrière antireflux et reflux",
        "Schéma en couleur, estomac coupé, sphincter inférieur fermé en haut et ouvert en bas.",
        [
            [30, 20, "Le schéma du haut montre le sphincter inférieur fermé, donc le contenu reste dans l'estomac."],
            [74, 48, "Le schéma du bas montre le sphincter ouvert et le contenu gastrique qui remonte dans l'œsophage."],
            [16, 74, "La silhouette de gauche rappelle que l'œsophage thoracique rejoint l'estomac sous le diaphragme."],
        ],
        ["Le reflux dessiné en rouge ne prouve pas à lui seul une œsophagite ni une sténose."],
        "Le clinicien relie ainsi la brûlure rétrosternale à une barrière inférieure incompétente, puis cherche une sténose.",
    )
    phrase = exiger("Le schéma du reflux compare un sphincter fermé et un sphincter ouvert, parce que la barrière explique la brûlure.")
    bloc = (
        '<div class="p">'
        + phrase.replace("schéma du reflux", '<a class="ouvre" href="#f-dx1-p3-gerd">schéma du reflux</a>', 1)
        + "</div>"
        + fenetre_figure("f-dx1-p3-gerd", "Barrière antireflux et reflux", fig)
    )
    h = inserer_apres_h3(h, "dx1-h3", bloc)
    fig2 = figure_html(
        LOT / "images" / "Peptic_stricture.json",
        "Sténose peptique en endoscopie",
        "Endoscopie en couleur, vue endoluminale, lumière rétrécie au centre et muqueuse congestive.",
        [
            [42, 50, "La lumière résiduelle est le pertuis sombre au centre, donc le calibre est réduit."],
            [78, 42, "La muqueuse de droite est rouge et saigne, ce qui traduit une fragilité de la paroi."],
        ],
        ["Les reflets blancs sont des éclats de lumière et non des dépôts que l'on biopsie en priorité."],
        "Cette lumière étroite et fragile conduit à biopsier la sténose avant toute dilatation instrumentale.",
    )
    phrase2 = exiger("L'endoscopie montre la sténose peptique lorsque la lumière se rétrécit et que la muqueuse saigne.")
    bloc2 = (
        '<div class="p">'
        + phrase2.replace("endoscopie", '<a class="ouvre" href="#f-dx1-p9-stenose">endoscopie</a>', 1)
        + "</div>"
        + fenetre_figure("f-dx1-p9-stenose", "Sténose peptique en endoscopie", fig2)
    )
    h = inserer_apres_h3(h, "dx1-h9", bloc2)
    h = h.replace('<section class="ilot" id="dx1-p12">', cartes_dx1() + '\n<section class="ilot" id="dx1-p12">', 1)
    for mot, fid in [
        ("Nexium®", "f-dx1-m-nexium"),
        ("Pantoprazol-Mepha Teva®", "f-dx1-m-pantoprazole"),
        ("Omeprazol Zentiva®", "f-dx1-m-omeprazole"),
        ("Lansoprazol Zentiva®", "f-dx1-m-lansoprazole"),
        ("Pariet®", "f-dx1-m-pariet"),
    ]:
        h = lier_premiere(h, mot, fid)
    h = recrire_biblio(h)
    h = ajouter_ancre_molecule(h)
    h = limiter_car(h)
    return h


def main():
    pa = LOT / "LOT_048_Phase_A_V0.html"
    dx = LOT / "LOT_048_Phase_B_V0_DX.1.html"
    a = traiter_phase_a(pa.read_text(encoding="utf-8"))
    b = traiter_dx1(dx.read_text(encoding="utf-8"))
    pa.write_text(a, encoding="utf-8")
    dx.write_text(b, encoding="utf-8")
    print("phase A", len(a.encode()), "dx1", len(b.encode()))


if __name__ == "__main__":
    main()
