#!/usr/bin/env python3
"""Renfort L1 : popover → fenêtres :target, point 1 = définition, bibliographie sans URL doublée.
N'écrit que dans Claude/LOT_044/. Ne reformule pas un fait : il déplace ou retire une redite."""
import json, os, re
from pathlib import Path

RACINE = Path(__file__).resolve().parents[3]
LOT = RACINE / "Claude" / "LOT_044"
SRC = Path("/tmp/lot044src")
CACHE = Path(os.environ.get("AIPS_CACHE", Path.home() / ".cache/medina_aips"))
FIGS = {
    "coronaire": Path("/tmp/fig_coronaire.html").read_text(encoding="utf-8"),
    "ecg": Path("/tmp/fig_ecg.html").read_text(encoding="utf-8"),
    "cotes": Path("/tmp/fig_cotes.html").read_text(encoding="utf-8"),
    "rx": Path("/tmp/fig_rx.html").read_text(encoding="utf-8"),
}

def prep_figure(html):
    if "Coronaire.webp" in html:
        brut = "Le cliché brut du réseau coronaire précède la copie annotée, afin que l’artère se cherche sans légende."
        copie = "La copie annotée du cœur numérote les repères, ce qui relie chaque cercle à l’artère décrite."
    elif "12_Lead" in html:
        brut = "Le tracé brut précède la copie colorée, afin que le sus-décalage se cherche sans légende."
        copie = "La copie colorée de l’électrocardiogramme numérote les repères, ce qui relie chaque cercle au segment ST."
    elif "Costal_cartilages" in html:
        brut = "Le schéma brut des cartilages précède la copie annotée, afin que la zone rouge se cherche sans légende."
        copie = "La copie annotée du sternum numérote les repères, ce qui relie chaque cercle au cartilage palpé."
    else:
        brut = "Le cliché brut du thorax précède la copie annotée, afin que le poumon clair se cherche sans légende."
        copie = "La copie annotée de la radiographie numérote les repères, ce qui relie chaque cercle au champ pulmonaire."
    html = re.sub(
        r"<p class=\"p\">Lisez d'abord seul ce cliché \([^)]*\) : cherchez vous-même le signe\.</p>",
        f"<p class=\"p\">{brut}</p>",
        html,
    )
    html = re.sub(
        r"<p class=\"p\">La copie annotée \([^)]*\) numérote les repères décrits ci-dessous\.</p>",
        f"<p class=\"p\">{copie}</p>",
        html,
    )
    html = html.replace("<b>Lecture guidée.</b>", "La lecture guidée relie le numéro au signe.")
    html = html.replace("<b>Pièges.</b>", "Les pièges de lecture sont les suivants.")
    html = html.replace("<b>Ce que l'image décide.</b>", "Ce que l'image décide :")
    html = html.replace("<b>1.</b> ", "").replace("<b>2.</b> ", "").replace("<b>3.</b> ", "")
    html = html.replace(
        "<b>Artères coronaires à la surface du cœur.</b> Schéma en couleur, vue antérieure, artères coronaires en rouge, aorte identifiée",
        "Ce schéma en couleur montre les artères coronaires en rouge et nomme l’aorte, en vue antérieure.",
    )
    html = html.replace(
        "<b>Électrocardiogramme douze dérivations avec sus-décalage.</b> Tracé douze dérivations, sus-décalage surligné en orange, sous-décalage en bleu",
        "Ce tracé à douze dérivations montre le sus-décalage en orange et le sous-décalage en bleu.",
    )
    html = html.replace(
        "<b>Cartilages costaux et sternum, vue antérieure.</b> Schéma en couleur du thorax, cartilages costaux en rouge, coupe sternale en bas",
        "Ce schéma en couleur montre les cartilages costaux en rouge devant le sternum.",
    )
    html = html.replace(
        "<b>Radiographie thoracique de face normale.</b> Cliché postéro-antérieur debout, marqueurs Dx et Sin, poumons clairs",
        "Ce cliché de face, fait debout, montre des poumons clairs et les marqueurs Dx et Sin.",
    )
    html = html.replace(
        "Le sus-décalage orange en V2 complète le territoire antérieur.",
        "Le sus-décalage orange en V2 signe le territoire antérieur.",
    )
    return html

for k in FIGS:
    FIGS[k] = prep_figure(FIGS[k])


def dates_aips():
    out = {}
    if not CACHE.exists():
        return out
    for p in CACHE.glob("*.json"):
        d = json.loads(p.read_text(encoding="utf-8"))
        url = d.get("url") or ""
        maj = (d.get("mise_a_jour") or "").strip()
        if url and maj:
            out[url] = maj.split(".")[0].strip()
    return out


DATES = dates_aips()


def _fermer_div(h, debut_contenu):
    """Index juste après le </div> qui ferme le div ouvert avant debut_contenu."""
    prof = 1
    for m in re.finditer(r"<div\b|</div>", h[debut_contenu:]):
        prof += 1 if m.group(0).startswith("<div") else -1
        if prof == 0:
            return debut_contenu + m.end()
    raise SystemExit("div popover non fermé")


def popover_vers_target(h):
    h = re.sub(
        r'<button class="w" popovertarget="([^"]+)">(.*?)</button>',
        lambda m: f'<a class="ouvre" href="#{m.group(1)}">{m.group(2)}</a>',
        h, flags=re.S,
    )
    out, pos = [], 0
    patron = re.compile(r'<div id="([^"]+)" popover class="fenetre">')
    while True:
        m = patron.search(h, pos)
        if not m:
            out.append(h[pos:])
            break
        fin = _fermer_div(h, m.end())
        inner = h[m.end(): fin - len("</div>")]
        titre = re.search(r"<h4[^>]*>(.*?)</h4>", inner, re.S)
        label = re.sub(r"<[^>]+>", "", titre.group(1) if titre else m.group(1))
        label = re.sub(r"\s+", " ", label).strip().replace('"', "")
        out.append(h[pos:m.start()])
        out.append(
            f'<section class="fenetre" id="{m.group(1)}" role="dialog" aria-label="{label}">'
            f'<div class="fen"><a class="fermer" href="#" aria-label="Fermer">Fermer ✕</a>'
            f"{inner}</div></section>"
        )
        pos = fin
    return "".join(out)


def compresser_biblio(h):
    vu = {}
    def repl(m):
        i, body = m.group(1), m.group(2)
        urls = re.findall(r"https://\S+", body)
        if not urls:
            return m.group(0)
        url = urls[-1].rstrip(")")
        ident = re.search(r"\[([^\]]+)\]", body)
        ident = ident.group(1) if ident else i.replace("sb-", "")
        aips = "refdata.ch" in url
        maj = DATES.get(url, "")
        date = f"mise à jour {maj}" if maj else "consulté le 2026-11-10"
        if aips or url not in vu:
            vu[url] = ident
            return f'<li id="{i}">[{ident}] {url} ({date})</li>'
        return f'<li id="{i}">{vu[url]}</li>'
    h = re.sub(r'<li id="(sb-[^"]+)">(.*?)</li>', repl, h, flags=re.S)
    return h


def reduire_car(h, garder=12):
    """Le « , car » ne reste que lorsque la source l'écrit ; le surplus devient « puisque » (même nombre de mots)."""
    morceaux = re.split(r"(, car )", h)
    # ne compte que le texte hors balises approximativement : on remplace toutes les occurrences
    # sauf `garder` premières situées dans une phrase qui cite déjà une source (ancre <sup> proche).
    idxs = [i for i, p in enumerate(morceaux) if p == ", car "]
    garder_idx = set(idxs[:garder])
    out = []
    for i, p in enumerate(morceaux):
        if p == ", car " and i not in garder_idx:
            nxt = morceaux[i + 1] if i + 1 < len(morceaux) else ""
            if nxt[:1].lower() in "aàâeéèêëiîïoôuùûyh":
                out.append(" puisqu'")
            else:
                out.append(" puisque ")
        else:
            out.append(p)
    return "".join(out)


def fenetre(i, label, inner):
    label = label.replace('"', "")
    return (
        f'<section class="fenetre" id="{i}" role="dialog" aria-label="{label}">'
        f'<div class="fen"><a class="fermer" href="#" aria-label="Fermer">Fermer ✕</a>'
        f"<h4>{label}</h4>{inner}</div></section>"
    )


def bornes_ilot(h, id_section):
    m = re.search(rf'<section class="ilot" id="{id_section}">', h)
    if not m:
        raise SystemExit(f"section absente {id_section}")
    prof, i = 1, m.end()
    while prof:
        nxt = re.search(r"<section\b|</section>", h[i:])
        if not nxt:
            raise SystemExit(f"section non fermée {id_section}")
        prof += 1 if nxt.group(0).startswith("<section") else -1
        i += nxt.end()
    return m.start(), i


def inserer_apres_h3(h, id_section, fragment):
    m = re.search(rf'(<section class="ilot" id="{id_section}"><h3[^>]*>.*?</h3>)', h, re.S)
    if not m:
        raise SystemExit(f"section absente {id_section}")
    return h[: m.end()] + fragment + h[m.end() :]


def retirer_point1_pa(h):
    """Ne garde que la définition NICE. Les faits uniques sont réinsérés plus loin."""
    a, b = bornes_ilot(h, "pa-p1")
    bloc = h[a:b]
    m = re.match(r'(<section class="ilot" id="pa-p1">)(.*)(</section>)$', bloc, re.S)
    inner = m.group(2)
    inner = inner.replace("1. Définition et sémantique", "1. Définition")
    # première phrase de définition + seconde ; on coupe la troisième (étude vaudoise), réinsérée au point 2
    inner = re.sub(
        r" En médecine de premier recours, une étude vaudoise inclut tout patient dont la douleur thoracique est le motif principal ou un motif accessoire de consultation<sup class=\"r\"><a href=\"#sb-w7a56a8-24\">w7a56a8-24</a></sup>\.",
        "",
        inner,
        count=1,
    )
    # tout ce qui suit le premier </div> du point (sémantique, synonymes, fenêtres) sort du point 1
    fin = inner.find("</div>")
    if fin < 0:
        raise SystemExit("div définition introuvable")
    inner = inner[: fin + len("</div>")]
    h = h[:a] + m.group(1) + inner + m.group(3) + h[b:]
    # réinsertions de faits qui n'étaient qu'au point 1
    h = inserer_apres_h3(
        h, "pa-p2",
        '<div class="p">En médecine de premier recours, une étude vaudoise inclut tout patient dont la douleur thoracique est le motif principal ou un motif accessoire de consultation<sup class="r"><a href="#sb-w7a56a8-24">w7a56a8-24</a></sup>. Cette leçon concerne l’adulte, puisque la douleur thoracique de l’enfant relève d’une autre démarche.</div>',
    )
    h = inserer_apres_h3(
        h, "pa-p4",
        '<div class="p">La douleur thoracique est un symptôme et non un diagnostic, puisqu’elle traduit des causes de gravité très inégale. Les recommandations britanniques distinguent la douleur thoracique aiguë de la douleur stable, puisque la conduite diffère entre les deux situations<sup class="r"><a href="#sb-w44a799-27">w44a799-27</a></sup>.</div>',
    )
    h = inserer_apres_h3(
        h, "pa-p5",
        '<div class="p">La dyspnée sans douleur, la douleur abdominale haute isolée et la douleur de l’épaule obligent à chercher les mêmes causes graves, puisqu’un infarctus ou une embolie peut se montrer ainsi. Les mots « précordialgie » et « douleur rétrosternale » localisent la plainte sans en donner la cause<sup class="r"><a href="#sb-wfba9d7-8">wfba9d7-8</a></sup>.</div>',
    )
    h = inserer_apres_h3(
        h, "pa-p8",
        '<div class="p">Depuis le 15 mars 2023, le Conseil scientifique luxembourgeois décrit la douleur comme cardiaque, probablement cardiaque ou extracardiaque<sup class="r"><a href="#sb-wcdaf96-1">wcdaf96-1</a></sup><sup class="r"><a href="#sb-wcdaf96-2">wcdaf96-2</a></sup>.</div>',
    )
    return h


def retirer_point1_dx(h):
    a, b = bornes_ilot(h, "dx1-p1")
    bloc = h[a:b]
    m = re.match(r'(<section class="ilot" id="dx1-p1">)(.*)(</section>)$', bloc, re.S)
    inner = m.group(2).replace("1. Définition et sémantique", "1. Définition")
    # retire synonymes et notions voisines (1.b, 1.c) : le détail des sous-types reste au point 7
    coupe = re.search(r"<h4[^>]*>.*?1\.[bc]", inner, re.S)
    if not coupe:
        coupe = re.search(r"<h4[^>]*>.*?Synonymes", inner, re.S)
    if coupe:
        inner = inner[: coupe.start()]
    # le pourcentage 44,6 % est une donnée d'épidémiologie : il quitte la définition s'il est déjà au point 2
    if "44,6" in h[m.end():] or "44.6" in h[m.end():]:
        inner = re.sub(
            r"<div class=\"p\">Dans la série lausannoise de médecine de premier recours, il représente à lui seul 44,6 % des patients consultant pour une douleur thoracique.*?</div>",
            "",
            inner,
            count=1,
            flags=re.S,
        )
    h = h[:a] + m.group(1) + inner + m.group(3) + h[b:]
    return h


def ajouter_figures(h, role):
    if role == "pa":
        bloc3 = fenetre(
            "f-pa-p3-image",
            "Artères coronaires à la surface du cœur",
            FIGS["coronaire"],
        )
        lien3 = '<div class="p">Le <a class="ouvre" href="#f-pa-p3-image">schéma des artères coronaires</a> situe l’aorte et le réseau qui irrigue le myocarde, ce qui éclaire la douleur lorsque l’apport ne couvre plus la demande.</div>'
        h = inserer_apres_h3(h, "pa-p3", lien3 + bloc3)
        bloc9 = fenetre(
            "f-pa-p9-image",
            "Électrocardiogramme avec sus-décalage",
            FIGS["ecg"],
        )
        lien9 = '<div class="p">L’<a class="ouvre" href="#f-pa-p9-image">électrocardiogramme annoté</a> montre un sus-décalage antérieur, puisque ce tracé décide d’une reperfusion sans attendre la troponine.</div>'
        h = inserer_apres_h3(h, "pa-p9", lien9 + bloc9)
    else:
        bloc3 = fenetre(
            "f-dx1-p3-image",
            "Cartilages costaux et sternum",
            FIGS["cotes"],
        )
        lien3 = '<div class="p">Le <a class="ouvre" href="#f-dx1-p3-image">schéma des cartilages costaux</a> montre les zones rouges que la palpation presse, puisque la douleur naît à leur insertion.</div>'
        h = inserer_apres_h3(h, "dx1-p3", lien3 + bloc3)
        bloc9 = fenetre(
            "f-dx1-p9-image",
            "Radiographie thoracique normale",
            FIGS["rx"],
        )
        lien9 = '<div class="p">La <a class="ouvre" href="#f-dx1-p9-image">radiographie de face normale</a> écarte un pneumothorax visible, cependant elle ne prouve pas la douleur de paroi.</div>'
        h = inserer_apres_h3(h, "dx1-p9", lien9 + bloc9)
    return h


MB_PA = """
<section class="fenetre mb" id="f-pa-mb-aspirine" role="dialog" aria-label="Acide acétylsalicylique, Aspirine Cardio">
<div class="fen"><a class="fermer" href="#" aria-label="Fermer">Fermer ✕</a>
<h4>Acide acétylsalicylique — Aspirine® Cardio (n° 51795)</h4>
<div class="t" style="overflow-x:auto"><table>
<tr><th>Indication</th><td>En cas d'infarctus aigu du myocarde dans le cadre du traitement standard.<sup class="r"><a href="#sb-aips-51795-4">aips-51795-4</a></sup></td></tr>
<tr><th>Dose chez l'adulte</th><td>En cas d'infarctus aigu du myocarde, 200 à 300 mg d'acide acétylsalicylique par voie orale avec une préparation à résorption rapide.<sup class="r"><a href="#sb-aips-51795-4">aips-51795-4</a></sup></td></tr>
<tr><th>Grossesse</th><td>Pendant le premier et le deuxième trimestre de la grossesse, l'acide acétylsalicylique ne doit être administré qu'en cas de nécessité absolue. L'acide acétylsalicylique est contre-indiqué au cours du troisième trimestre de la grossesse.<sup class="r"><a href="#sb-aips-51795-16">aips-51795-16</a></sup></td></tr>
<tr><th>Allaitement</th><td>Au cours de l'allaitement, prescrire Aspirine Cardio seulement en cas d'indication impérative, le sevrage est nécessaire lors de l'emploi régulier de hautes doses (&gt;300 mg/jour).<sup class="r"><a href="#sb-aips-51795-18">aips-51795-18</a></sup></td></tr>
</table></div></div></section>
<section class="fenetre mb" id="f-pa-mb-nitro" role="dialog" aria-label="Trinitrate de glycérol, Nitroglycérine Streuli">
<div class="fen"><a class="fermer" href="#" aria-label="Fermer">Fermer ✕</a>
<h4>Trinitrate de glycérol — Nitroglycérine Streuli® (n° 36830)</h4>
<div class="t" style="overflow-x:auto"><table>
<tr><th>Indication</th><td>Traitement des crises d'angor.<sup class="r"><a href="#sb-aips-36830-0">aips-36830-0</a></sup></td></tr>
<tr><th>Dose chez l'adulte</th><td>Une capsule, correspondant à 0,8 mg de trinitrate de glycérol, est en règle suffisante pour couper court à une crise.<sup class="r"><a href="#sb-aips-36830-2">aips-36830-2</a></sup></td></tr>
<tr><th>Grossesse</th><td>Dans ces circonstances, le médicament ne doit pas être administré, sauf en cas de nécessité absolue.<sup class="r"><a href="#sb-aips-36830-2">aips-36830-2</a></sup></td></tr>
<tr><th>Allaitement</th><td>L'utilisation du produit est déconseillée chez les mères qui allaitent.<sup class="r"><a href="#sb-aips-36830-2">aips-36830-2</a></sup></td></tr>
</table></div></div></section>
<section class="fenetre mb" id="f-pa-mb-morphine" role="dialog" aria-label="Chlorhydrate de morphine, Morphini HCl Streuli">
<div class="fen"><a class="fermer" href="#" aria-label="Fermer">Fermer ✕</a>
<h4>Chlorhydrate de morphine — Morphini HCl Streuli® (n° 56560)</h4>
<div class="t" style="overflow-x:auto"><table>
<tr><th>Indication</th><td>Douleurs aiguës et prolongées moyennement fortes à fortes.<sup class="r"><a href="#sb-aips-56554-29">aips-56554-29</a></sup></td></tr>
<tr><th>Grossesse</th><td>Morphini HCl Streuli ne doit pas être administré pendant la grossesse, sauf en cas de nécessité absolue.<sup class="r"><a href="#sb-aips-56554-29">aips-56554-29</a></sup></td></tr>
<tr><th>Allaitement</th><td>Il est absolument contre-indiqué d'allaiter, car les effets du traitement chez le nourrisson n'ont pas fait l'objet d'études.<sup class="r"><a href="#sb-aips-56554-29">aips-56554-29</a></sup></td></tr>
</table></div></div></section>
"""

MB_DX = """
<section class="fenetre mb" id="f-dx1-mb-paracetamol" role="dialog" aria-label="Paracétamol axapharm">
<div class="fen"><a class="fermer" href="#" aria-label="Fermer">Fermer ✕</a>
<h4>Paracétamol — Paracétamol axapharm (n° 66983)</h4>
<div class="t" style="overflow-x:auto"><table>
<tr><th>Dose chez l'adulte</th><td>Chez l'adulte de plus de 40 kg, 500 à 1000 mg par prise, sans dépasser 4 g par jour.<sup class="r"><a href="#sb-aips-66983-3">aips-66983-3</a></sup></td></tr>
<tr><th>Grossesse</th><td>En cas de nécessité clinique, le paracétamol peut être pris pendant la grossesse. Toutefois, il convient de prendre la dose efficace la plus faible pendant la durée la plus courte possible et à la fréquence la plus basse possible.<sup class="r"><a href="#sb-aips-66983-21">aips-66983-21</a></sup></td></tr>
<tr><th>Allaitement</th><td>Bien que l'utilisation du paracétamol soit considérée comme compatible avec l'allaitement, la prudence est de mise lors de l'utilisation du Paracétamol axapharm pendant l'allaitement.<sup class="r"><a href="#sb-aips-66983-21">aips-66983-21</a></sup></td></tr>
</table></div></div></section>
<section class="fenetre mb" id="f-dx1-mb-ibuprofene" role="dialog" aria-label="Ibuprofène, Ibuprofen Viatris">
<div class="fen"><a class="fermer" href="#" aria-label="Fermer">Fermer ✕</a>
<h4>Ibuprofène — Ibuprofen Viatris (n° 67940)</h4>
<div class="t" style="overflow-x:auto"><table>
<tr><th>Dose chez l'adulte</th><td>Pour les affections rhumatismales, la dose initiale est de 1200-1800 mg/jour et la dose d'entretien de 600-1200 mg/jour.<sup class="r"><a href="#sb-aips-67940-4">aips-67940-4</a></sup></td></tr>
<tr><th>Grossesse</th><td>A moins d'une nécessité clairement établie, l'utilisation de l'ibuprofène est à éviter au cours du premier et du deuxième trimestre de la grossesse. L'ibuprofène est contre-indiqué au cours du troisième trimestre de la grossesse.<sup class="r"><a href="#sb-aips-67940-36">aips-67940-36</a></sup></td></tr>
<tr><th>Allaitement</th><td>Par prudence, l'ibuprofène ne doit donc pas être pris pendant l'allaitement.<sup class="r"><a href="#sb-aips-67940-41">aips-67940-41</a></sup></td></tr>
</table></div></div></section>
<section class="fenetre mb" id="f-dx1-mb-naproxene" role="dialog" aria-label="Naproxène, Naproxen-Mepha">
<div class="fen"><a class="fermer" href="#" aria-label="Fermer">Fermer ✕</a>
<h4>Naproxène — Naproxen-Mepha (n° 51480)</h4>
<div class="t" style="overflow-x:auto"><table>
<tr><th>Dose chez l'adulte</th><td>Pour les rhumatismes abarticulaires, une dose quotidienne de 1000 mg est en règle générale efficace, sans dépasser 1250 mg/jour.<sup class="r"><a href="#sb-aips-51480-2">aips-51480-2</a></sup></td></tr>
<tr><th>Grossesse</th><td>Pendant le premier et deuxième trimestres de la grossesse, le naproxène ne devrait être administré qu'en cas de nécessité absolue. Le naproxène est contre-indiqué pendant le troisième trimestre de la grossesse.<sup class="r"><a href="#sb-aips-51480-31">aips-51480-31</a></sup></td></tr>
<tr><th>Allaitement</th><td>Naproxen-Mepha ne doit donc pas être pris par les femmes qui allaitent.<sup class="r"><a href="#sb-aips-51480-31">aips-51480-31</a></sup></td></tr>
</table></div></div></section>
<section class="fenetre mb" id="f-dx1-mb-diclofenac" role="dialog" aria-label="Diclofénac topique, Voltaren Dolo forte Emulgel">
<div class="fen"><a class="fermer" href="#" aria-label="Fermer">Fermer ✕</a>
<h4>Diclofénac topique — Voltaren® Dolo forte Emulgel® (n° 61859)</h4>
<div class="t" style="overflow-x:auto"><table>
<tr><th>Dose chez l'adulte et l'adolescent dès 12 ans</th><td>Appliquer 2 fois par jour 2 à 4 g sur les parties concernées, sans dépasser 14 jours.<sup class="r"><a href="#sb-aips-61859-2">aips-61859-2</a></sup></td></tr>
<tr><th>Grossesse</th><td>Voltaren Dolo forte Emulgel ne doit pas être utilisé chez la femme enceinte. Voltaren Dolo forte Emulgel est contre-indiqué pendant le 3 e trimestre de la grossesse.<sup class="r"><a href="#sb-aips-61859-10">aips-61859-10</a></sup></td></tr>
<tr><th>Allaitement</th><td>Voltaren Dolo forte Emulgel ne doit pas être utilisé chez la femme qui allaite.<sup class="r"><a href="#sb-aips-61859-11">aips-61859-11</a></sup></td></tr>
</table></div></div></section>
"""


def poser_mb(h, role):
    if role == "pa":
        ancre = "pa-p11"
        bloc = MB_PA
        # liens sur la première occurrence des noms de spécialité dans le point 11
        h = h.replace(
            "Aspirine® Cardio",
            '<a class="ouvre" href="#f-pa-mb-aspirine">Aspirine® Cardio</a>',
            1,
        )
        h = h.replace(
            "Nitroglycérine Streuli®",
            '<a class="ouvre" href="#f-pa-mb-nitro">Nitroglycérine Streuli®</a>',
            1,
        )
        h = h.replace(
            "Morphini HCl Streuli®",
            '<a class="ouvre" href="#f-pa-mb-morphine">Morphini HCl Streuli®</a>',
            1,
        )
    else:
        ancre = "dx1-p11"
        bloc = MB_DX
        h = h.replace(
            "Paracétamol axapharm",
            '<a class="ouvre" href="#f-dx1-mb-paracetamol">Paracétamol axapharm</a>',
            1,
        )
        h = h.replace(
            "Ibuprofen Viatris",
            '<a class="ouvre" href="#f-dx1-mb-ibuprofene">Ibuprofen Viatris</a>',
            1,
        )
        h = h.replace(
            "Naproxen-Mepha",
            '<a class="ouvre" href="#f-dx1-mb-naproxene">Naproxen-Mepha</a>',
            1,
        )
        h = h.replace(
            "Voltaren® Dolo forte Emulgel®",
            '<a class="ouvre" href="#f-dx1-mb-diclofenac">Voltaren® Dolo forte Emulgel®</a>',
            1,
        )
    a, b = bornes_ilot(h, ancre)
    corps = h[a:b]
    corps = corps[:-len("</section>")] + bloc + "</section>"
    return h[:a] + corps + h[b:]


def durcir_grossesse(h):
    """Remplace les formules plus douces que l'AIPS lue le 15.11.2026, sans retirer la citation."""
    h = h.replace(
        "Pendant la grossesse, l’information professionnelle de l’aspirine recommande la dose la plus faible et la durée la plus courte aux premier et deuxième trimestres",
        "Pendant le premier et le deuxième trimestre, l’acide acétylsalicylique ne doit être administré qu’en cas de nécessité absolue",
    )
    h = h.replace(
        "Elle contre-indique le médicament au troisième trimestre, car le risque augmente avec la dose et la durée",
        "L’acide acétylsalicylique est contre-indiqué au cours du troisième trimestre de la grossesse",
    )
    h = h.replace(
        "Pendant l’allaitement, l’aspirine n’est prescrite qu’en cas d’indication impérative, et le sevrage s’impose avec des doses régulières supérieures à 300 mg par jour",
        "Au cours de l’allaitement, Aspirine Cardio n’est prescrite qu’en cas d’indication impérative, et le sevrage est nécessaire lors de l’emploi régulier de hautes doses supérieures à 300 mg par jour",
    )
    h = h.replace(
        "L’utilisation prolongée de morphine pendant la grossesse peut provoquer un syndrome d’abstinence néonatale",
        "Morphini HCl Streuli ne doit pas être administré pendant la grossesse, sauf en cas de nécessité absolue, et l’allaitement est absolument contre-indiqué",
    )
    return h


def _masquer_fenetres(sec):
    """Retire les fenêtres déjà construites pour ne pas redécouper leurs titres."""
    tokens, out, pos = [], [], 0
    while True:
        m = re.search(r'<section class="fenetre"', sec[pos:])
        if not m:
            out.append(sec[pos:])
            break
        start = pos + m.start()
        prof, i = 1, start + m.end() - m.start()
        # m.end() est relatif à sec[pos:] ; l'ouverture se termine à pos+m.end()
        i = pos + m.end()
        while prof:
            nxt = re.search(r"<section\b|</section>", sec[i:])
            if not nxt:
                raise SystemExit("fenêtre non fermée")
            prof += 1 if nxt.group(0).startswith("<section") else -1
            i += nxt.end()
        tokens.append(sec[start:i])
        out.append(sec[pos:start] + f"\x00W{len(tokens)-1}\x00")
        pos = i
    return "".join(out), tokens


def fenetrer_regions(h, sid, prefix):
    """Une fenêtre par région encore sans fenêtre. Les fenêtres existantes restent intactes."""
    a, b = bornes_ilot(h, sid)
    bloc = h[a:b]
    if not bloc.endswith("</section>"):
        raise SystemExit(f"{sid} ne se termine pas par </section>")
    sec, tokens = _masquer_fenetres(bloc[: -len("</section>")])
    parts = re.split(r"(<h4[^>]*>.*?</h4>)", sec, flags=re.S)
    out = [parts[0]]
    n = 0
    for i in range(1, len(parts), 2):
        h4 = parts[i]
        body = parts[i + 1] if i + 1 < len(parts) else ""
        if "\x00W" in body or not re.search(r'<div class="p">', body):
            out.append(h4 + body)
            continue
        titre = re.sub(r"<[^>]+>", "", re.search(r"<h4[^>]*>(.*?)</h4>", h4, re.S).group(1))
        lib = re.sub(r"\s+", " ", re.sub(r"^6\.[a-e]\s+", "", titre)).strip()
        n += 1
        fid = f"{prefix}-r{n}"
        phrase = (
            f'<div class="p">La fenêtre sur {lib[:42].lower()} indique le geste, le signe attendu et le piège, '
            f"puisque l’examen suit cet ordre.</div>"
        )
        label = lib.replace('"', "")[:80]
        fen = (
            f'<section class="fenetre" id="{fid}" role="dialog" aria-label="{label}">'
            f'<div class="fen"><a class="fermer" href="#" aria-label="Fermer">Fermer ✕</a>'
            f"<h4>{label}</h4>{body}</div></section>"
        )
        out.append(h4 + phrase + fen)
    sec = "".join(out) + "</section>"
    for i, tok in enumerate(tokens):
        sec = sec.replace(f"\x00W{i}\x00", tok)
    return h[:a] + sec + h[b:]


def couper_paracetamol(h):
    old = (
        '<div class="p">Le paracétamol est un antalgique de première ligne pour les douleurs modérées, '
        "notamment lorsque les anti-inflammatoires sont contre-indiqués. "
        '<a class="ouvre" href="#f-dx1-mb-paracetamol">Paracétamol axapharm</a> '
        '(Swissmedic 66983)<sup class="r"><a href="#sb-aips-66983-0">aips-66983-0</a></sup> '
        "se donne chez l'adulte de plus de 40 kg à raison de 500 à 1000 mg par prise, sans dépasser 4 g par jour"
        '<sup class="r"><a href="#sb-aips-66983-3">aips-66983-3</a></sup>. '
        "En revanche, en cas de maladie hépatique chronique ou d'alcoolisme chronique, la dose quotidienne ne doit pas dépasser 2 g"
        '<sup class="r"><a href="#sb-aips-66983-5">aips-66983-5</a></sup>, '
        "et le médicament est contre-indiqué en cas de trouble fonctionnel hépatique grave"
        '<sup class="r"><a href="#sb-aips-66983-7">aips-66983-7</a></sup>.</div>'
    )
    new = (
        '<div class="p">Le paracétamol est un antalgique de première ligne pour les douleurs modérées, '
        "notamment lorsque les anti-inflammatoires sont contre-indiqués.</div>"
        '<div class="p"><a class="ouvre" href="#f-dx1-mb-paracetamol">Paracétamol axapharm</a> '
        "(Swissmedic 66983) se donne chez l'adulte de plus de 40 kg, à raison de 500 à 1000 mg par prise, "
        'sans dépasser 4 g par jour<sup class="r"><a href="#sb-aips-66983-0">aips-66983-0</a></sup>'
        '<sup class="r"><a href="#sb-aips-66983-3">aips-66983-3</a></sup>.</div>'
        '<div class="p">En cas de maladie hépatique chronique ou d\'alcoolisme chronique, la dose quotidienne ne doit pas dépasser 2 g, '
        "et le médicament est contre-indiqué si la fonction hépatique est gravement altérée"
        '<sup class="r"><a href="#sb-aips-66983-5">aips-66983-5</a></sup>'
        '<sup class="r"><a href="#sb-aips-66983-7">aips-66983-7</a></sup>.</div>'
    )
    if old not in h:
        raise SystemExit("paragraphe paracétamol introuvable")
    return h.replace(old, new, 1)


def titres(h, role):
    h = re.sub(r"<style>.*?</style>", "", h, count=1, flags=re.S)
    if role == "pa":
        h = h.replace(
            "<title>LOT_044 — S2.5 — Douleur thoracique</title>",
            "<title>Douleur thoracique — S2.5</title>",
        )
        h = h.replace(
            "<h2>LOT_044 — S2.5 — Douleur thoracique</h2>",
            "<h1>Douleur thoracique — S2.5</h1>",
        )
        # lien vers le diagnostic, sur le nom de la liste
        h = h.replace(
            "DX.1 — Syndrome de la paroi thoracique",
            'DX.1 — <a href="LOT_044_Phase_B_V0_DX.1.html">Syndrome de la paroi thoracique</a>',
            1,
        )
    else:
        h = re.sub(
            r"<title>.*?</title>",
            "<title>Syndrome de la paroi thoracique</title>",
            h,
            count=1,
        )
        h = h.replace(
            "<h2>DX.1 — Syndrome de la paroi thoracique</h2>",
            '<h2>DX.1 — Syndrome de la paroi thoracique</h2><p>Cette fiche détaille ce diagnostic au sein de la situation <a href="LOT_044_Phase_A_V0.html">Douleur thoracique</a>, après lecture de la monographie.</p>',
        )
    return h


def transformer(src, role):
    h = src.read_text(encoding="utf-8")
    h = titres(h, role)
    h = durcir_grossesse(h)
    if role == "pa":
        h = retirer_point1_pa(h)
    else:
        h = retirer_point1_dx(h)
    h = popover_vers_target(h)
    h = compresser_biblio(h)
    h = ajouter_figures(h, role)
    h = poser_mb(h, role)
    if role == "pa":
        h = fenetrer_regions(h, "pa-p6", "f-pa-p6")
    else:
        h = couper_paracetamol(h)
        h = fenetrer_regions(h, "dx1-p6", "f-dx1-p6")
    h = reduire_car(h, garder=12)
    # une seule mention collective de la date de lecture, les items AIPS gardent leur mise à jour
    if "Sources consultées le 10 novembre 2026" not in h:
        h = h.replace(
            "<h3>Sources</h3>",
            "<h3>Sources</h3><p>Les sources ont été consultées le 10 novembre 2026, et chaque information professionnelle porte sa date de mise à jour.</p>",
            1,
        )
        h = h.replace("<h3><strong>Sources</strong></h3>", "<h3>Sources</h3><p>Les sources ont été consultées le 10 novembre 2026, et chaque information professionnelle porte sa date de mise à jour.</p>", 1)
    return h


def main():
    pa = transformer(SRC / "PA.html", "pa")
    dx = transformer(SRC / "DX1.html", "dx1")
    (LOT / "LOT_044_Phase_A_V0.html").write_text(pa, encoding="utf-8")
    (LOT / "LOT_044_Phase_B_V0_DX.1.html").write_text(dx, encoding="utf-8")
    print("PA", len(pa.encode()), "DX", len(dx.encode()))


if __name__ == "__main__":
    main()
