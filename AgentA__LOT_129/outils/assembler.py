#!/usr/bin/env python3
"""Assemble une monographie. La police et les fenêtres sont mécaniques ; le texte vient d'un fichier rédigé."""
import base64, html, re, sys
from pathlib import Path

POL = Path("/agent/repos/organigramme-examen-federal/codex-LOTS-html/outils/polices")
OUT = Path("/tmp/wt129/AgentA__LOT_129")


def font_css():
    faces = []
    for poids, nom in (
        (400, "atkinson-hyperlegible-latin-400-normal.woff2"),
        (700, "atkinson-hyperlegible-latin-700-normal.woff2"),
    ):
        raw = base64.b64encode((POL / nom).read_bytes()).decode()
        corps = "\n".join(raw[i : i + 1500] for i in range(0, len(raw), 1500))
        faces.append(
            '@font-face{font-family:"Atkinson Hyperlegible";font-style:normal;font-weight:'
            + str(poids)
            + ';font-display:swap;src:url(data:font/woff2;base64,'
            + corps
            + ') format("woff2")}'
        )
    return "\n".join(faces) + """
body{margin:0;background:#eef7fc;color:#1d2a30;font:1rem/1.55 "Atkinson Hyperlegible",Verdana,sans-serif}
main{max-width:74ch;margin:auto;padding:1rem 1rem 2rem}
h2,h3{font-family:"Atkinson Hyperlegible",Verdana,sans-serif;color:#14303b}
.ilot{border:1px solid #cfe3ec;border-radius:12px;padding:.85rem 1rem;margin:0 0 .75rem;background:#fff}
.tw{overflow-x:auto}
table{border-collapse:collapse;width:100%}th,td{border:1px solid #cfe3ec;padding:.4rem;vertical-align:top;text-align:left}
button.terme{all:unset;cursor:pointer;color:#0b5d86;text-decoration:underline dotted 1.5px}
[popover].fenetre{width:min(96vw,60rem);max-height:88vh;overflow:auto;padding:0;border:1px solid #888;border-radius:.5rem;background:#fff}
[popover]::backdrop{background:rgb(0 0 0 / .35)}
.barre{display:flex;justify-content:space-between;padding:.5rem .8rem;background:#f2f5f7;font-weight:700}
.barre button{border:1px solid #cfe3ec;border-radius:6px;background:#fff;cursor:pointer}
.corps{padding:.8rem 1rem 1rem}
figure{margin:.6rem 0}
.s{color:#4f5f66}
"""


def e(s):
    return html.escape(s, quote=True)


def bouton(did, mot):
    return (
        '<button type="button" class="terme" popovertarget="'
        + did
        + '">'
        + e(mot)
        + "</button>"
    )


def fenetre(did, titre, paras):
    corps = "".join("<p>" + e(p) + "</p>" for p in paras)
    return (
        '<div id="'
        + did
        + '" popover class="fenetre"><div class="barre"><span>'
        + e(titre)
        + '</span><button type="button" popovertarget="'
        + did
        + '" popovertargetaction="hide">Fermer</button></div><div class="corps">'
        + corps
        + "</div></div>"
    )


def inline(texte, prefixe):
    """[[w12|mot]] devient un bouton dont l'id est prefixe-w12."""

    def repl(m):
        return bouton(prefixe + "-" + m.group(1), m.group(2))

    return re.sub(r"\[\[([A-Za-z0-9_-]+)\|([^\]]+)\]\]", repl, texte)


def parse(md, prefixe):
    lignes = md.splitlines()
    sections = []
    titre = None
    buf = []
    pops = {}
    i = 0
    while i < len(lignes):
        ln = lignes[i]
        if ln.startswith("@@"):
            cle = ln[2:].strip().split(" ", 1)
            did = prefixe + "-" + cle[0]
            ptitle = cle[1] if len(cle) > 1 else cle[0]
            i += 1
            paras = []
            cur = []
            while i < len(lignes) and lignes[i].strip() != "@@":
                if lignes[i].strip() == "":
                    if cur:
                        paras.append(" ".join(cur))
                        cur = []
                else:
                    cur.append(lignes[i].strip())
                i += 1
            if cur:
                paras.append(" ".join(cur))
            pops[did] = (ptitle, paras)
            i += 1
            continue
        if ln.startswith("## "):
            if titre is not None:
                sections.append((titre, buf))
            titre = ln[3:].strip()
            buf = []
            i += 1
            continue
        buf.append(ln)
        i += 1
    if titre is not None:
        sections.append((titre, buf))
    return sections, pops


def blocs_de(lignes, pops, prefixe, deja):
    html_parts = []
    extra = []
    i = 0
    while i < len(lignes):
        ln = lignes[i]
        if ln.strip() == "%%TABLE":
            i += 1
            rows = []
            while i < len(lignes) and lignes[i].strip() != "%%":
                if lignes[i].strip():
                    rows.append([c.strip() for c in lignes[i].split("|")])
                i += 1
            head, body = rows[0], rows[1:]
            thead = "".join("<th>" + e(c) + "</th>" for c in head)
            tbody = "".join(
                "<tr>" + "".join("<td>" + e(c) + "</td>" for c in r) + "</tr>" for r in body
            )
            html_parts.append("<div class=\"tw\"><table><thead><tr>" + thead + "</tr></thead><tbody>" + tbody + "</tbody></table></div>")
            i += 1
            continue
        if ln.strip() == "%%HTML":
            i += 1
            raw = []
            while i < len(lignes) and lignes[i].strip() != "%%":
                raw.append(lignes[i])
                i += 1
            html_parts.append("\n".join(raw))
            i += 1
            continue
        if ln.strip() == "":
            i += 1
            continue
        # paragraphe jusqu'à ligne vide
        cur = [ln.strip()]
        i += 1
        while i < len(lignes) and lignes[i].strip() not in ("", "%%TABLE", "%%HTML") and not lignes[i].startswith("##"):
            cur.append(lignes[i].strip())
            i += 1
        texte = " ".join(cur)
        html_parts.append("<p>" + inline(e_sauf_boutons(texte), prefixe) + "</p>")
    # fenêtres citées dans cette section
    cites = set(re.findall(r'popovertarget="([^"]+)"', "\n".join(html_parts)))
    for did in cites:
        if did in pops and did not in deja:
            titre, paras = pops[did]
            extra.append(fenetre(did, titre, paras))
            deja.add(did)
    return "\n".join(html_parts), "\n".join(extra)


def e_sauf_boutons(texte):
    """Échappe le texte en préservant les marqueurs [[id|mot]]."""
    morceaux = re.split(r"(\[\[[A-Za-z0-9_-]+\|[^\]]+\]\])", texte)
    out = []
    for m in morceaux:
        if m.startswith("[["):
            out.append(m)
        else:
            out.append(e(m))
    return "".join(out)


def page(prefixe, h2, md, sources):
    sections, pops = parse(md, prefixe)
    bits = []
    utilises = set()
    for n, (titre, lignes) in enumerate(sections, 1):
        corps, extra = blocs_de(lignes, pops, prefixe, utilises)
        for did in re.findall(r'popovertarget="([^"]+)"', corps):
            utilises.add(did)
        bits.append(
            '<section class="ilot"><h3 id="'
            + prefixe
            + "-p"
            + str(n)
            + '"><strong>'
            + str(n)
            + ". "
            + e(titre)
            + "</strong></h3>\n"
            + corps
            + "\n"
            + extra
            + "</section>"
        )
    manquants = [d for d in utilises if d not in pops]
    if manquants:
        raise SystemExit("fenêtres sans texte : " + ", ".join(manquants))
    src = (
        '<section id="sources"><h3>Sources</h3><ol>\n'
        + "\n".join('<li id="sb-' + str(i) + '">' + e(t) + "</li>" for i, t in enumerate(sources, 1))
        + '\n</ol>\n<p class="s">Non validé cliniquement. Le référentiel de liens n\'est pas une source de cours.</p></section>'
    )
    return (
        '<!DOCTYPE html>\n<html lang="fr"><head><meta charset="utf-8">'
        '<meta name="viewport" content="width=device-width, initial-scale=1">'
        "<title>LOT 129</title><style>\n"
        + font_css()
        + "</style></head><body><main>\n"
        '<p class="s">LOT 129 · S9.13 · non validé cliniquement.</p>\n'
        '<h2 id="' + prefixe + '">' + e(h2) + "</h2>\n"
        + "\n".join(bits)
        + "\n"
        + src
        + "\n</main></body></html>\n<!-- FIN_FICHIER LOT_129 -->\n"
    )


def phrases(html_text):
    t = re.sub(r"(?is)<style.*?</style>", " ", html_text)
    t = re.sub(r'(?is)<section id="sources">.*?</section>', " ", t)
    t = re.sub(r"(?is)<h[1-3][^>]*>.*?</h[1-3]>", " ", t)
    t = html.unescape(re.sub(r"<[^>]+>", " ", t))
    t = t.replace("\u00a0", " ")
    out = []
    for s in re.split(r"[.!?]+", t):
        s = re.sub(r"\s+", " ", s).strip().lower()
        if len(s.split()) >= 8:
            out.append(s)
    return out


def controler_texte(html_text, autres):
    ph = phrases(html_text)
    uniq = set(ph)
    taux = (len(uniq) / len(ph)) if ph else 0
    coll = uniq & autres
    longues = [i + 1 for i, l in enumerate(html_text.splitlines()) if len(l) > 3000]
    return {
        "phrases": len(ph),
        "uniques": len(uniq),
        "taux": round(taux, 3),
        "collisions": len(coll),
        "exemple": next(iter(coll), ""),
        "lignes": longues[:3],
        "octets": len(html_text.encode()),
    }
