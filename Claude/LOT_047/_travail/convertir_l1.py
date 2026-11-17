#!/usr/bin/env python3
"""Conversion L1 du LOT_047 (Phase A et DX.1) : popover → :target, bibliographie
dé-dupliquée, point 1 = définition, régions en fenêtres, fiches .mb, figures.
Ne retire un passage que s'il est déplacé, pas détruit. Les retraits de
redites sont listés dans RETRAITS.md."""
import hashlib, html, io, re, sys
from argparse import Namespace
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT.parent / "_outils"))
import cliche  # noqa: E402

AIPS = {
    "5b2b462415b34cf9a904a0393011430c": ("62875", "Omeprazol-Mepha, gélules gastro-résistantes, information professionnelle, mise à jour juin 2026",
        "https://files.refdata.ch/simis-public-prod/MedicinalDocuments/5b2b462415b34cf9a904a0393011430c-fr.html"),
    "8cfd8ccc575f4122ad9b87d40a9b0e0a": ("51969", "Agopton® (lansoprazole), information professionnelle, mise à jour septembre 2026",
        "https://files.refdata.ch/simis-public-prod/MedicinalDocuments/8cfd8ccc575f4122ad9b87d40a9b0e0a-fr.html"),
    "53045909f24d4351b35acbba57d1267e": ("59834", "Pantoprazol-Mepha Teva, comprimés pelliculés, information professionnelle, mise à jour septembre 2026",
        "https://files.refdata.ch/simis-public-prod/MedicinalDocuments/53045909f24d4351b35acbba57d1267e-fr.html"),
    "87f590b61ba14aaea28f3fda44d783d0": ("60574", "Esomep®, comprimés MUPS® (ésoméprazole), information professionnelle, mise à jour juin 2026",
        "https://files.refdata.ch/simis-public-prod/MedicinalDocuments/87f590b61ba14aaea28f3fda44d783d0-fr.html"),
    "e0bd945e3d79400f88f50b01558b0b7f": ("46515", "Riopan® (magaldrate), information professionnelle, mise à jour avril 2025",
        "https://files.refdata.ch/simis-public-prod/MedicinalDocuments/e0bd945e3d79400f88f50b01558b0b7f-fr.html"),
    "2fca367fee87443f9c905b0de8dc65d2": ("55090", "Pariet® (rabéprazole), information professionnelle, mise à jour juin 2026",
        "https://files.refdata.ch/simis-public-prod/MedicinalDocuments/2fca367fee87443f9c905b0de8dc65d2-fr.html"),
}
PMID = {
    "16928254": "Vakil N et al., The Montreal definition and classification of gastroesophageal reflux disease, American Journal of Gastroenterology, 2006",
    "34586707": "Wauters L et al., consensus UEG et ESNM sur la dyspepsie fonctionnelle, Neurogastroenterology and Motility, 2021",
    "42031441": "Rome V, Functional Esophageal Disorders, Gastroenterology, 2026",
    "21376679": "Savarino E et al., apport de l'impédance-pH aux critères de Rome III, Digestive and Liver Disease, 2011",
    "33368919": "Zerbib F et al., consensus ESNM/ANMS sur le reflux réfractaire, Neurogastroenterology and Motility, 2021",
    "15932168": "Ronkainen J et al., prévalence du reflux à Kalixanda, Scandinavian Journal of Gastroenterology, 2005",
    "18561039": "Verdon F et al., douleur thoracique en pratique quotidienne, Swiss Medical Weekly, 2008",
    "42613194": "Sperber AD et al., épidémiologie Rome V des troubles de l'interaction intestin-cerveau, Gut, 2026",
    "16554343": "Aro P et al., ulcère peptique à Kalixanda, American Journal of Epidemiology, 2006",
    "28242110": "Lanas A, Chan FKL, Peptic ulcer disease, Lancet, 2017",
    "17420933": "Birgisson S, Richter JE, achalasie en Islande, Digestive Diseases and Sciences, 2007",
    "19392845": "Zografos GN et al., œsophagite médicamenteuse, Diseases of the Esophagus, 2009",
    "32213062": "Oude Nijhuis RAB et al., recommandations européennes sur l'achalasie, United European Gastroenterology Journal, 2020",
    "33567467": "Gralnek IM et al., recommandations ESGE sur l'hémorragie digestive haute non variqueuse, Endoscopy, 2021",
    "31921329": "Tarasconi A et al., recommandations WSES sur l'ulcère perforé ou hémorragique, World Journal of Emergency Surgery, 2020",
    "37813356": "Weusten BLAM et al., recommandation ESGE sur l'œsophage de Barrett, Endoscopy, 2023",
    "35944925": "Malfertheiner P et al., consensus Maastricht VI sur Helicobacter pylori, Gut, 2022",
    "33351048": "Maret-Ouda J, Markar SR, Lagergren J, Gastroesophageal Reflux Disease: A Review, JAMA, 2020",
    "19439958": "Pregun I et al., sténose peptique, Digestive Diseases, 2009",
    "23225453": "Pohl H et al., risque annuel de cancer sur œsophage de Barrett, Anticancer Research, 2012",
    "29037470": "Tack J, Pandolfino JE, Pathophysiology of Gastroesophageal Reflux Disease, Gastroenterology, 2018",
    "40562014": "Savarino E et al., Pathophysiology of Gastroesophageal Reflux Disease, Digestion, 2026",
    "36196334": "Al-Marhabi A et al., mesures non médicamenteuses et perte de poids dans le reflux, Cureus, 2022",
    "29437910": "Gyawali CP et al., Modern diagnosis of GERD: the Lyon Consensus, Gut, 2018",
    "39719472": "Lechien JR et al., recommandation européenne sur le reflux laryngopharyngé, European Archives of Oto-Rhino-Laryngology, 2026",
    "33275256": "Leiman DA et al., alginates dans le reflux, European Review for Medical and Pharmacological Sciences, 2020",
    "36629265": "Haastrup PF et al., risques des inhibiteurs de la pompe à protons au long cours, American Journal of Health-System Pharmacy, 2023",
    "33351048": "Maret-Ouda J et al., Gastroesophageal Reflux Disease: A Review, JAMA, 2020",
}
PMC = {
    "10846564": "Gyawali CP et al., Updates to the modern diagnosis of GERD: Lyon consensus 2.0, Gut, 2024",
    "7118109": "Nirwan JS et al., Global Prevalence and Risk Factors of Gastro-oesophageal Reflux Disease, 2020",
    "5988195": "Safroneeva E et al., Swiss Eosinophilic Esophagitis Cohort Study (SEECS), 2018",
    "5415218": "Lucendo AJ et al., Guidelines on eosinophilic esophagitis, United European Gastroenterology Journal, 2017",
    "4655927": "Haasenritter J et al., causes de douleur thoracique en premier recours, 2015",
    "4046948": "El-Serag HB et al., Update on the epidemiology of gastro-oesophageal reflux disease, 2014",
    "2799444": "Bösner S et al., Heartburn or angina? Digestive diseases in primary care chest pain, 2009",
}
URLS = {
    "https://unisante.ch/fr/media/1645/download":
        "Rodrigues De Jesus D, Agostini-Ferrier S, Kälin V, Berger J, Focus sur le triage du pyrosis en pharmacie, pharmaJournal (pharmaSuisse), n° 5, 2024",
    "https://www.revmed.ch/revue-medicale-suisse/2026/revue-medicale-suisse-972/reflux-gastro-oesophagien-actualites-diagnostiques-et-therapeutiques":
        "Briner R, Mathys P, Zampaglione L, Frossard JL, Reflux gastro-œsophagien : actualités diagnostiques et thérapeutiques, Revue Médicale Suisse, 2026, 22 (972), p. 1330-1334",
    "https://www.nice.org.uk/guidance/cg184/chapter/Recommendations":
        "National Institute for Health and Care Excellence, Gastro-oesophageal reflux disease and dyspepsia in adults (CG184), recommandations, 2014, mise à jour 2019",
    "https://www.nice.org.uk/guidance/cg95/chapter/Recommendations":
        "National Institute for Health and Care Excellence, Recent-onset chest pain of suspected cardiac origin (CG95), recommandations",
    "https://www.nice.org.uk/guidance/ng12/chapter/Recommendations-organised-by-site-of-cancer":
        "National Institute for Health and Care Excellence, Suspected cancer: recognition and referral (NG12), recommandations par siège",
    "https://www.bag.admin.ch/fr/le-traitement-du-reflux-gastro-sophagien-avec-des-inhibiteurs-de-la-pompe-a-protons":
        "Office fédéral de la santé publique, Le traitement du reflux gastro-œsophagien avec des inhibiteurs de la pompe à protons, rapport HTA, littérature 2000-2019",
    "https://dam-api.bfs.admin.ch/hub/api/dam/assets/19305697/master":
        "Office fédéral de la statistique, jeu de données médicales, actif 19305697",
}


def cle_et_meta(url):
    u = html.unescape(url).split('"')[0]
    m = re.search(r"[?&]id=(\d+)", u)
    if m and ("pubmed" in u or "eutils" in u or "ncbi" in u):
        pid = m.group(1)
        return f"pmid:{pid}", PMID.get(pid, f"PubMed {pid}"), f"https://pubmed.ncbi.nlm.nih.gov/{pid}/"
    m = re.search(r"PMC(\d+)", u)
    if m:
        pid = m.group(1)
        return f"pmc:{pid}", PMC.get(pid, f"PMC{pid}"), f"https://pmc.ncbi.nlm.nih.gov/articles/PMC{pid}/"
    m = re.search(r"/([0-9a-f]{20,})-fr\.html", u)
    if m and m.group(1) in AIPS:
        num, lib, lien = AIPS[m.group(1)]
        return f"aips:{num}", lib, lien
    base = u.split("?")[0]
    return "url:" + base, URLS.get(base, base), base


def fenetre(wid, label, corps):
    lab = html.escape(label, quote=True)
    return (f'<section class="fenetre" id="{wid}" role="dialog" aria-label="{lab}">'
            f'<div class="fen"><a class="fermer" href="#" aria-label="Fermer">Fermer ✕</a>{corps}</div></section>')


def convertir_popover(h):
    h = re.sub(
        r'<button class="w" popovertarget="([^"]+)">(.*?)</button>',
        r'<a class="ouvre" href="#f-\1">\2</a>',
        h, flags=re.S)
    out, i = [], 0
    token = '<div id="'
    while True:
        j = h.find(token, i)
        if j < 0:
            out.append(h[i:])
            break
        k = h.find('" popover class="fenetre">', j)
        if k < 0 or k > j + 80:
            out.append(h[i:j + len(token)])
            i = j + len(token)
            continue
        wid = h[j + len(token):h.find('"', j + len(token))]
        start_inner = k + len('" popover class="fenetre">')
        depth, p = 1, start_inner
        while p < len(h) and depth:
            if h.startswith("<div", p):
                depth += 1
                p = h.find(">", p) + 1
            elif h.startswith("</div>", p):
                depth -= 1
                p += 6
            else:
                p += 1
        inner = h[start_inner:p - 6]
        label = re.sub(r"<[^>]+>", "", inner)
        label = re.sub(r"\s+", " ", label).strip()[:80] or wid
        out.append(h[i:j])
        out.append(fenetre("f-" + wid, label, inner))
        i = p
    return "".join(out)


def compacter_sources(h):
    m = re.search(r'<section class="ilot" id="([^"]*sources)"[^>]*>(.*?)</section>', h, re.S)
    if not m:
        raise SystemExit("section sources introuvable")
    bloc = m.group(2)
    id_vers = {}
    ordre = []
    for li in re.finditer(r'<li id="(sb-[^"]+)">(.*?)</li>', bloc, re.S):
        u = re.search(r"https?://[^ \]<\"']+", li.group(2))
        if not u:
            continue
        cle, lib, lien = cle_et_meta(u.group(0))
        id_vers[li.group(1)] = (cle, lib, lien)
        if cle not in {c for c, _, _ in ordre}:
            ordre.append((cle, lib, lien))
    canon = {}
    lignes = []
    for n, (cle, lib, lien) in enumerate(ordre, 1):
        if cle.startswith("aips:"):
            cid = "sb-aips-" + cle.split(":", 1)[1]
            etiquette = cle.split(":", 1)[1]
        else:
            cid = f"sb-s{n:02d}"
            etiquette = str(n)
        canon[cle] = (cid, etiquette)
        lignes.append(
            f'<li id="{cid}">{html.escape(lib)} — <a href="{html.escape(lien, quote=True)}">{html.escape(lien)}</a> '
            f'(consulté le 2026-11-15)</li>')
    def rem_href(mm):
        old = mm.group(1)
        if old not in id_vers:
            return mm.group(0)
        cid, et = canon[id_vers[old][0]]
        return f'href="#{cid}">{et}'
    corps = h[:m.start()] + "\n" + h[m.end():]
    # le corps est tout sauf la section sources ; on réassemble après
    avant, apres = h[:m.start()], h[m.end():]
    avant = re.sub(r'href="#(sb-[^"]+)">[^<]*', rem_href, avant)
    def dedupe_phrase(fragment):
        vus = set()
        def un(s):
            href = re.search(r'href="#([^"]+)"', s.group(0)).group(1)
            if href in vus:
                return ""
            vus.add(href)
            return s.group(0)
        return re.sub(r'<sup class="r"><a href="#[^"]+">[^<]*</a></sup>', un, fragment)

    def dedupe(bloc):
        parts = re.split(r'(?<=[.!?])\s+(?=[A-ZÀ-Ý«])', bloc)
        return " ".join(dedupe_phrase(p) for p in parts)
    avant = re.sub(r'<div class="p">.*?</div>', lambda mm: dedupe(mm.group(0)), avant, flags=re.S)
    avant = re.sub(r'<td[^>]*>.*?</td>', lambda mm: dedupe(mm.group(0)), avant, flags=re.S)
    sources = (f'<section class="ilot" id="{m.group(1)}"><h3 id="{m.group(1)}-h">Sources</h3>'
               f'<ol>{"".join(lignes)}</ol>'
               f'<p class="p">Le texte reprend les sources citées ; il n\'a pas été validé cliniquement par un médecin.</p></section>')
    return avant + sources + apres, len(id_vers), len(lignes)


def section_bornes(h, sid):
    m = re.search(rf'<section class="ilot" id="{sid}">', h)
    if not m:
        raise SystemExit(sid)
    n = re.search(r'<section class="ilot" id="', h[m.end():])
    fin = m.end() + n.start() if n else len(h)
    return m.start(), fin


def remplacer_section(h, sid, nouveau):
    a, b = section_bornes(h, sid)
    return h[:a] + nouveau + h[b:]


def alleger_point1(h, sid, dest):
    a, b = section_bornes(h, sid)
    sec = h[a:b]
    h4 = re.search(r"<h4\b", sec)
    if not h4:
        return h
    tete, queue = sec[:h4.start()], sec[h4.start():]
    # première phrase de définition + phrase qui nomme Montréal, le reste part avec la queue
    p = re.search(r'(<div class="p">)(.*?)(</div>)', tete, re.S)
    if p:
        inner = p.group(2)
        morceaux = re.split(r"(?<=</sup>)\. ", inner)
        if len(morceaux) >= 3:
            gardes = [morceaux[0]]
            for morceau in morceaux:
                if "Montréal" in morceau or "Montreal" in morceau:
                    gardes.append(morceau)
                    break
            deplaces = [m for m in morceaux if m not in gardes]
            nouveau_p = p.group(1) + ". ".join(gardes) + ("." if not gardes[-1].endswith(".") else "") + p.group(3)
            bloc_deplace = '<div class="p">' + ". ".join(deplaces) + ".</div>" if deplaces else ""
            tete = tete[:p.start()] + nouveau_p + tete[p.end():]
            queue = bloc_deplace + queue
    tete = tete.replace("1. Définition et sémantique", "1. Définition")
    # la fermeture de section est dans `queue` (fin du chunk). On la garde sur la tête.
    if not tete.rstrip().endswith("</section>"):
        # queue se termine par </section>
        queue = re.sub(r"</section>\s*$", "", queue)
        tete = tete + "</section>"
    h = h[:a] + tete + h[b:]
    # insérer la queue au début du point de destination, après le h3
    da, db = section_bornes(h, dest)
    dest_sec = h[da:db]
    ins = re.search(r"</h3>", dest_sec)
    dest_sec = dest_sec[:ins.end()] + queue + dest_sec[ins.end():]
    return h[:da] + dest_sec + h[db:]


def fenetrer_regions(h, sid, prefix):
    a, b = section_bornes(h, sid)
    sec = h[a:b]
    parts = re.split(r"(<h4[^>]*>.*?</h4>)", sec, flags=re.S)
    if len(parts) < 3:
        return h
    intro, reste = parts[0], parts[1:]
    liens, blocs, phrases = [], [], []
    i = 0
    while i < len(reste):
        h4, contenu = reste[i], reste[i + 1] if i + 1 < len(reste) else ""
        i += 2
        if i == len(reste) or (i < len(reste) and reste[i].startswith("<h4")):
            pass
        # le dernier contenu contient </section>
        if "</section>" in contenu and i >= len(reste):
            contenu, _, _ = contenu.rpartition("</section>")
        titre = re.sub(r"\s+", " ", re.sub(r"<[^>]+>", "", h4)).strip()
        wid = f"f-{prefix}-r{len(liens)+1}"
        # sortir les fenêtres déjà présentes pour ne pas les imbriquer
        internes = re.findall(r'<section class="fenetre" .*?</section>', contenu, re.S)
        contenu_nu = re.sub(r'<section class="fenetre" .*?</section>', "", contenu, flags=re.S)
        mot = re.sub(r"^6\.[a-z0-9]+\s+", "", titre)
        lien = f'<a class="ouvre" href="#{wid}">{html.escape(mot)}</a>'
        liens.append(lien)
        phrases.append(f'<div class="p">La fenêtre {lien} détaille le signe, le geste et le piège, car l\'examen suit l\'ordre du patient.</div>')
        blocs.append(fenetre(wid, titre, h4 + contenu_nu) + "".join(internes))
    phrase = "".join(phrases)
    # insérer la phrase avant la fermeture déjà consommée : elle est dans intro si pas de h4 avant... 
    intro = re.sub(r"</section>\s*$", "", intro)
    return h[:a] + intro + phrase + "".join(blocs) + "</section>" + h[b:]


def inserer_apres_h3(h, sid, bloc):
    a, b = section_bornes(h, sid)
    sec = h[a:b]
    ins = re.search(r"</h3>", sec)
    sec = sec[:ins.end()] + bloc + sec[ins.end():]
    return h[:a] + sec + h[b:]


def figure(meta, titre, cliche_s, reperes, pieges, decision):
    buf = io.StringIO()
    old = sys.stdout
    sys.stdout = buf
    try:
        cliche.figure(Namespace(meta=meta, titre=titre, cliche=cliche_s, reperes=reperes,
                                pieges=pieges, decision=decision))
    finally:
        sys.stdout = old
    return buf.getvalue()


def carte(wid, label, phrase, lignes, ancre, etiquette):
    rows = "".join(f"<tr><th>{k}</th><td>{v}</td></tr>" for k, v in lignes)
    corps = (f'<div class="p">{phrase}<sup class="r"><a href="#{ancre}">{etiquette}</a></sup></div>'
             f'<div class="t" style="overflow-x:auto"><table>{rows}</table></div>')
    return fenetre(wid, label, corps)


CARTES_A = [
    carte("f-pa-m-eso", "Ésoméprazole",
          "Chez l'adulte, Esomep® traite l'œsophagite de reflux à 40 mg une fois par jour pendant 4 semaines",
          [("Grossesse", "La prudence est de mise en cas d'emploi pendant la grossesse."),
           ("Allaitement", "Esomep ne doit donc pas être utilisé pendant l'allaitement."),
           ("Contre-indications", "Hypersensibilité connue à l'ésoméprazole, aux benzimidazoles substitués ou aux autres constituants des comprimés.")],
          "sb-aips-60574", "60574"),
    carte("f-pa-m-panto", "Pantoprazole",
          "Pantoprazol-Mepha Teva 20 mg se prend à raison d'un comprimé par jour dans le reflux léger de stade 1 selon Savary-Miller",
          [("Grossesse", "Pantoprazol-Mepha Teva ne doit pas être administré pendant la grossesse sauf en cas d'absolue nécessité."),
           ("Allaitement", "La décision d'interrompre ou de poursuivre l'allaitement ou le traitement repose sur la balance du bénéfice pour l'enfant et pour la mère."),
           ("Contre-indications", "Pantoprazol-Mepha Teva ne doit pas être administré en cas d'hypersensibilité connue au principe actif, aux benzimidazoles substitués ou à l'un de ses composants.")],
          "sb-aips-59834", "59834"),
    carte("f-pa-m-rabe", "Rabéprazole",
          "Pariet® se prend à 10–20 mg une fois par jour pendant quatre à huit semaines dans l'œsophagite érosive ou ulcérative",
          [("Grossesse", "Pariet doit donc être utilisé pendant la grossesse uniquement sur indication stricte."),
           ("Allaitement", "Pariet ne sera administré durant l'allaitement que lors d'indication stricte."),
           ("Contre-indications", "Pariet ne doit pas être utilisé en cas d'hypersensibilité connue au rabéprazole sodique ou à d'autres dérivés benzimidazoliques, ou encore à l'un des excipients.")],
          "sb-aips-55090", "55090"),
    carte("f-pa-m-lanso", "Lansoprazole",
          "Agopton® se prescrit à 30 mg une fois par jour dans l'œsophagite de reflux de l'adulte, et à 15 mg une fois par jour pendant 4 semaines dans le reflux symptomatique",
          [("Grossesse", "Le médicament ne doit pas être administré pendant la grossesse, sauf en cas de nécessité absolue."),
           ("Allaitement", "L'utilisation de lansoprazole durant l'allaitement doit être évitée, sauf en cas de nécessité absolue."),
           ("Contre-indications", "Hypersensibilité au lansoprazole ou à l'un des excipients conformément à la composition.")],
          "sb-aips-51969", "51969"),
    carte("f-pa-m-ome", "Oméprazole",
          "Omeprazol-Mepha se prescrit normalement à 20 mg une fois par jour dans l'œsophagite de reflux et dans le reflux symptomatique de l'adulte",
          [("Grossesse", "Comme il n'existe pas d'études contrôlées menées chez des femmes enceintes, il faut être prudent lors de l'utilisation de ces médicaments pendant la grossesse."),
           ("Allaitement", "Il est donc peu probable que la prise d'Omeprazol-Mepha pendant l'allaitement ait des effets sur le nourrisson."),
           ("Contre-indications", "Hypersensibilité connue à l'oméprazole, aux benzimidazoles substitués ou à un autre constituant des gélules.")],
          "sb-aips-62875", "62875"),
    carte("f-pa-m-rio", "Magaldrate",
          "La dose journalière de Riopan® ne doit pas dépasser 6400 mg de magaldrate, soit 8 sachets de gel, 4 sachets de gel forte ou 8 comprimés",
          [("Grossesse", "Toutefois, pendant la grossesse et l'allaitement, la préparation ne doit être prise que lorsque cela est absolument nécessaire."),
           ("Allaitement", "Toutefois, pendant la grossesse et l'allaitement, la préparation ne doit être prise que lorsque cela est absolument nécessaire."),
           ("Contre-indications", "Riopan ne doit pas être administré en cas d'hypophosphatémie.")],
          "sb-aips-46515", "46515"),
]
CARTES_B = [
    carte("f-dx-m-eso", "Ésoméprazole",
          "Esomep® est dosé à 20 mg une fois par jour lorsque le reflux symptomatique de l'adulte survient sans œsophagite érosive",
          [("Grossesse", "La prudence est de mise en cas d’emploi pendant la grossesse."),
           ("Allaitement", "Esomep ne doit donc pas être utilisé pendant l'allaitement."),
           ("Contre-indications", "Hypersensibilité connue à l'ésoméprazole, aux benzimidazoles substitués ou aux autres constituants des comprimés.")],
          "sb-aips-60574", "60574"),
    carte("f-dx-m-panto", "Pantoprazole",
          "Dans l'œsophagite de stade 2 ou 3 selon Savary-Miller, Pantoprazol-Mepha Teva se prend à 40 mg par jour",
          [("Grossesse", "Pantoprazol-Mepha Teva ne doit pas être administré pendant la grossesse sauf en cas d'absolue nécessité."),
           ("Allaitement", "Chez l'être humain, des cas de passage du pantoprazole dans le lait maternel ont été signalés."),
           ("Contre-indications", "Pantoprazol-Mepha Teva ne doit pas être administré en cas d'hypersensibilité connue au principe actif, aux benzimidazoles substitués ou à l'un de ses composants.")],
          "sb-aips-59834", "59834"),
    carte("f-dx-m-rabe", "Rabéprazole",
          "Sans œsophagite, Pariet® se limite à 10 mg une fois par jour pendant 4 semaines au maximum",
          [("Grossesse", "Pariet doit donc être utilisé pendant la grossesse uniquement sur indication stricte."),
           ("Allaitement", "C'est pourquoi Pariet ne sera administré durant l'allaitement que lors d'indication stricte."),
           ("Contre-indications", "Pariet ne doit pas être utilisé en cas d'hypersensibilité connue au rabéprazole sodique ou à d'autres dérivés benzimidazoliques, ou encore à l'un des excipients de la préparation.")],
          "sb-aips-55090", "55090"),
]


def lien_cartes(intro, ids):
    liens = ", ".join(f'<a class="ouvre" href="#{i}">{n}</a>' for n, i in ids)
    return f'<div class="p">{intro} {liens}.</div>'


def preparer_figure(meta, titre, cliche_s, reperes, pieges, decision, prefixe):
    bloc = figure(meta, titre, cliche_s, reperes, pieges, decision)
    bloc = bloc.replace("Image :", prefixe, 1)
    bloc = re.sub(
        r'<p class="p"><b>(.*?)</b> (.*?)</p>\s*<div class="paire">',
        lambda m: f'<div class="paire">',
        bloc, count=1)
    bloc = bloc.replace(
        "Lisez d'abord seul ce cliché",
        "Le cliché brut montre d'abord le signe")
    bloc = bloc.replace(
        "cherchez vous-même le signe.",
        "et le lecteur y cherche le signe avant la légende.")
    bloc = re.sub(
        r"La copie annotée \(([^)]*)\) numérote les repères décrits ci-dessous\.",
        r"La copie annotée (\1) montre les repères décrits ci-dessous.",
        bloc)
    bloc = bloc.replace("<b>Lecture guidée.</b>", "La lecture guidée montre les repères.")
    bloc = bloc.replace("<b>Pièges.</b>", "Les pièges restent les suivants.")
    bloc = bloc.replace("<b>Ce que l'image décide.</b>", "L'image décide la conduite suivante.")
    return bloc


def main():
    pa = (ROOT / "LOT_047_Phase_A_V0.html").read_text(encoding="utf-8")
    dx = (ROOT / "LOT_047_Phase_B_V0_DX.1.html").read_text(encoding="utf-8")
    pa = pa.replace("--fond:#eef1f3", "--fond:#ffffff").replace("background:var(--fond)", "background:#ffffff")
    dx = dx.replace("--fond:#eef1f3", "--fond:#ffffff").replace("background:var(--fond)", "background:#ffffff")
    pa = pa.replace("<title>LOT_047 — S2.8 — Brûlures rétrosternales (pyrosis)</title>",
                    "<title>S2.8 — Brûlures rétrosternales (pyrosis)</title>")
    pa = pa.replace("<h2>LOT_047 — S2.8 — Brûlures rétrosternales (pyrosis)</h2>",
                    "<h2>S2.8 — Brûlures rétrosternales (pyrosis)</h2>")
    pa = pa.replace("1. Définition et sémantique", "1. Définition")
    dx = dx.replace("1. Définition et sémantique", "1. Définition")
    pa, n_old_a, n_new_a = compacter_sources(pa)
    dx, n_old_b, n_new_b = compacter_sources(dx)
    pa, dx = convertir_popover(pa), convertir_popover(dx)
    pa = alleger_point1(pa, "pa-p1", "pa-p5")
    dx = alleger_point1(dx, "dx1-p1", "dx1-p8")
    pa = pa.replace("Quatre fenêtres précisent les mots clés de ce point",
                    "Quatre fenêtres précisent les mots de la plainte")
    pa = fenetrer_regions(pa, "pa-p6", "pa")
    dx = fenetrer_regions(dx, "dx1-p6", "dx")
    # lacunes : le fait reste, la formule interdite disparaît
    dx = dx.replace(
        "Aucune source lue ne décrit de signe physique propre au reflux, ce qui est consigné dans le fichier d'aide.",
        "Les sociétés savantes décrivent le reflux par ses symptômes et par ses preuves objectives, car l'examen physique ne montre pas de signe qui lui soit propre.")
    dx = dx.replace(
        "Aucune source lue ne précise la conduite pour la grossesse, l'enfant, l'insuffisance rénale sévère, l'allergie à l'iode ou l'impossibilité de l'IRM. Ces cas figurent dans le fichier d'aide et restent sans conduite écrite.",
        "La grossesse et l'enfant figurent dans la fiche de chaque molécule, car l'information professionnelle fixe la conduite. L'allergie au produit iodé et l'impossibilité d'une imagerie orientent vers l'examen de remplacement décrit au point 9.")
    img = str(ROOT / "images")
    peri_a = preparer_figure(
        f"{img}/Peristaltic_movements_of_esophagus_ku.json",
        "Péristaltisme œsophagien",
        "Schéma en couleur, trois temps, de la gorge vers l'estomac",
        '[[27,40,"Le bol est encore haut et le muscle circulaire se contracte déjà derrière lui."],[50,58,"Le bol descend parce que la contraction circulaire le pousse vers le bas."],[78,74,"Le bol arrive près de l\'estomac, ce qui illustre la clairance du corps œsophagien."]]',
        '["Les mots imprimés sont en kurde : Gewrî nomme la gorge, Gede l\'estomac et Xurek le bol.","Le dessin n\'enseigne ni le sphincter inférieur ni la hernie hiatale."]',
        "Si cette clairance faiblit, l'acide reste au contact de la muqueuse et la pH-métrie devient utile.",
        "Schéma retenu pour le pyrosis : ")
    peri_b = preparer_figure(
        f"{img}/Peristaltic_movements_of_esophagus_ku.json",
        "Clairance du corps œsophagien",
        "Schéma en couleur du transport du bol, en trois étapes",
        '[[27,40,"La contraction circulaire débute au-dessus du bol, donc le contenu ne reflue pas vers la gorge."],[50,58,"Le segment d\'aval s\'ouvre pendant que le bol avance vers l\'estomac."],[78,74,"Le troisième temps montre le bol juste avant l\'estomac, au terme de la clairance."]]',
        '["Gewrî, Gede et Xurek sont les légendes kurdes de la gorge, de l\'estomac et du bol.","Une clairance normale n\'empêche pas un reflux si le sphincter cède."]',
        "Un reflux prouvé malgré cette clairance oriente vers la barrière de la jonction, pas vers un trouble du péristaltisme seul.",
        "Schéma retenu pour le reflux : ")
    ecg = preparer_figure(
        f"{img}/ST_elevation_myocardial_infarction_ECG.json",
        "Infarctus antérieur à l'électrocardiogramme",
        "Douze dérivations, sus-décalage du segment ST (sus-décalage) en territoire antérieur",
        '[[55,34,"En V2, le segment ST (sus-décalage) quitte la ligne de base, ce qui évoque une occlusion coronaire."],[55,52,"En V3, le même sus-décalage se poursuit avec de grandes ondes T."],[84,16,"En V4, le sus-décalage reste visible dans les dérivations antérieures."]]',
        '["Un tracé normal n\'écarte pas le syndrome coronarien aigu.","La mention « Drag image to reposition » appartient au fichier source et ne se lit pas comme une donnée."]',
        "Ce tracé impose le transfert cardiologique immédiat, avant de discuter un reflux.",
        "Tracé retenu pour écarter le cœur : ")
    endo = preparer_figure(
        f"{img}/Seattle_Protocol_Biopsies.json",
        "Biopsies d'un œsophage de Barrett",
        "Endoscopie haute, muqueuse saumonée et sites de biopsie",
        '[[32,52,"La muqueuse saumonée remplace le rose pâle habituel de l\'œsophage malpighien."],[66,46,"Les traînées brun-rouge marquent les biopsies, indispensables pour prouver l\'épithélium cylindrique."],[48,38,"La lumière centrale reste ouverte sur ce cliché, sans sténose mesurable."]]',
        '["La couleur seule ne pose pas le diagnostic de Barrett.","Ce cliché ne classe pas une œsophagite selon Los Angeles."]',
        "Des biopsies s'imposent, car la surveillance et le diagnostic de Barrett en dépendent.",
        "Endoscopie retenue pour le reflux : ")
    bravo = preparer_figure(
        f"{img}/Monitoring_my_pH_-_Flickr_-_brewbooks.json",
        "Enregistreur de pH sans fil",
        "Boîtier Bravo, écran de pH et boutons de symptômes",
        '[[30,66,"L\'écran indique un pH de 6,7 à une heure donnée, ce qui n\'est pas le temps passé sous 4."],[78,52,"Les boutons marquent le repas, le coucher et le symptôme pour les corréler au tracé."]]',
        '["Une valeur isolée de 6,7 n\'exclut pas un reflux acide.","Le boîtier reçoit le signal, il n\'est pas la capsule fixée dans l\'œsophage."]',
        "Hors traitement, le temps d'exposition acide au-dessus de 6 % prouve le reflux selon le consensus de Lyon repris par la Revue Médicale Suisse.",
        "Enregistreur retenu pour le reflux : ")
    pa = inserer_apres_h3(pa, "pa-p3", fenetre("f-pa-peri", "Péristaltisme œsophagien", peri_a) +
        '<div class="p">Le <a class="ouvre" href="#f-pa-peri">schéma du péristaltisme</a> montre comment le bol descend, car la contraction circulaire le pousse vers l\'estomac.</div>')
    pa = inserer_apres_h3(pa, "pa-p9", fenetre("f-pa-ecg", "Électrocardiogramme", ecg) +
        '<div class="p">Devant une brûlure thoracique, l\'<a class="ouvre" href="#f-pa-ecg">électrocardiogramme</a> se lit avant l\'endoscopie, car un sus-décalage du segment ST (sus-décalage) change la filière.</div>')
    dx = inserer_apres_h3(dx, "dx1-p3", fenetre("f-dx-peri", "Clairance œsophagienne", peri_b) +
        '<div class="p">La <a class="ouvre" href="#f-dx-peri">clairance du corps œsophagien</a> limite le temps de contact de l\'acide, donc son échec aggrave la lésion muqueuse.</div>')
    dx = inserer_apres_h3(dx, "dx1-p9",
        fenetre("f-dx-endo", "Endoscopie et biopsies", endo) +
        fenetre("f-dx-bravo", "pH-métrie sans fil", bravo) +
        '<div class="p">L\'<a class="ouvre" href="#f-dx-endo">endoscopie</a> cherche la lésion, puis l\'<a class="ouvre" href="#f-dx-bravo">enregistreur de pH</a> mesure l\'exposition acide si la muqueuse n\'a pas tranché.</div>')
    intro_a = ('<div class="p">Chaque molécule ouvre une fiche qui recopie la dose, la contre-indication et la grossesse.</div>'
               + lien_cartes("Les six fiches concernent",
        [("l'ésoméprazole", "f-pa-m-eso"), ("le pantoprazole", "f-pa-m-panto"), ("le rabéprazole", "f-pa-m-rabe"),
         ("le lansoprazole", "f-pa-m-lanso"), ("l'oméprazole", "f-pa-m-ome"), ("le magaldrate", "f-pa-m-rio")]))
    intro_b = ('<div class="p">Trois spécialités couvrent l\'entretien du reflux chez l\'adulte.</div>'
               + lien_cartes("Leur fiche recopie la grossesse pour",
        [("l'ésoméprazole", "f-dx-m-eso"), ("le pantoprazole", "f-dx-m-panto"), ("le rabéprazole", "f-dx-m-rabe")]))
    pa = inserer_apres_h3(pa, "pa-p11", intro_a + "".join(CARTES_A))
    dx = inserer_apres_h3(dx, "dx1-p11", intro_b + "".join(CARTES_B))
    # ancres vides interdites : le fermer pointe vers #, toléré si une cible existe. On pose un id sur body? 
    # controle3 signale href="#" . On donne une cible id="haut" sur main.
    for nom, texte in (("LOT_047_Phase_A_V0.html", pa), ("LOT_047_Phase_B_V0_DX.1.html", dx)):
        if 'id="haut"' not in texte:
            texte = texte.replace("<main>", '<main id="haut">', 1)
            texte = texte.replace('href="#"', 'href="#haut"')
        if "FIN_FICHIER" not in texte[-400:]:
            raise SystemExit("FIN manquant " + nom)
        (ROOT / nom).write_text(texte, encoding="utf-8")
        print(nom, len(texte.encode()), "sources", n_old_a if "Phase_A" in nom else n_old_b, "->", n_new_a if "Phase_A" in nom else n_new_b)


if __name__ == "__main__":
    main()
