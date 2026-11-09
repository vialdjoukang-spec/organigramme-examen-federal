#!/usr/bin/env python3
"""Assemble les 11 HTML du LOT_130. Les chiffres viennent de preuves.jsonl."""
from __future__ import annotations
import html, json, re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PREUVES = {r["id"]: r for r in map(json.loads, (ROOT / "preuves" / "preuves.jsonl").read_text(encoding="utf-8").splitlines())}
NBSP = "\u00a0"

DX = [
    (1, "Hypertension artérielle primaire", ""),
    (2, "Hypotension orthostatique", ""),
    (3, "Hyperaldostéronisme primaire", ""),
    (4, "Hypertension rénoparenchymateuse", ""),
    (5, "Hypertension rénovasculaire", ""),
    (6, "Syndrome d'apnées obstructives du sommeil", ""),
    (7, "Hypertension induite par les médicaments et les substances", ""),
    (8, "Phéochromocytome et paragangliome", "E3"),
    (9, "Urgence hypertensive", "E1"),
    (10, "Choc septique", "E2"),
]

TITRES = [
    "1. Définition et sémantique",
    "2. Épidémiologie (Suisse, puis Europe)",
    "3. Physiopathologie",
    "4. Démarche diagnostique",
    "5. Anamnèse ciblée et drapeaux rouges",
    "6. Examen physique ciblé, région par région",
    "7. Approche syndromique",
    "8. Diagnostic positif et critères",
    "9. Examens complémentaires",
    "10. Arbre décisionnel",
    "11. Prise en charge",
    "12. Prévention",
    "13. Points clés",
    "14. Pièges et questions d'examen",
]

CSS = """
body{font-family:Georgia,serif;line-height:1.55;margin:0 auto;max-width:52rem;padding:4.2rem 1rem 2rem;color:#14202b;background:#f7f5f2}
h2{font-size:1.35rem;border-left:6px solid #0f4c5c;padding:.2rem .7rem;background:#e6f1f3}
h3{font-size:1.05rem;background:#0f4c5c;color:#fff;padding:.35rem .6rem;border-radius:.35rem}
h4{font-size:1rem;color:#0f4c5c;margin:1rem 0 .3rem}
p{margin:.55rem 0}
table{border-collapse:collapse;width:100%;font-size:.92rem}
th,td{border:1px solid #9bb;padding:.35rem .45rem;vertical-align:top;text-align:left}
th{background:#d7e6ea}
.tw{overflow-x:auto}
.r{font-size:.72em;vertical-align:super}
.r a{color:#0b5;text-decoration:none}
button.fen{font:inherit;color:#0f4c5c;background:#e6f1f3;border:1px solid #0f4c5c;border-radius:.7rem;padding:0 .4rem;cursor:pointer}
[popover].fenetre{width:min(96vw,60rem);max-height:88vh;overflow:auto;padding:1rem;border:1px solid #888;border-radius:.5rem}
[popover]::backdrop{background:rgb(0 0 0 / .35)}
blockquote.preuve{margin:.4rem 0;padding:.4rem .7rem;background:#fff8e8;border-left:4px solid #c80;font-size:.88rem;white-space:pre-wrap}
.urg{border:2px solid #a00;padding:.5rem .7rem;background:#fff5f5}
.badge{display:inline-block;background:#a00;color:#fff;border-radius:.6rem;padding:0 .4rem;font-size:.8rem}
nav.barre{position:fixed;top:0;left:0;right:0;display:flex;gap:.25rem;overflow-x:auto;background:#14202b;padding:.35rem .5rem;z-index:5}
nav.barre a{color:#e6f1f3;text-decoration:none;font-size:.78rem;white-space:nowrap}
.ment{font-size:.92rem;background:#fff3cd;padding:.6rem .8rem;border-radius:.4rem}
"""

def cite(ids: list[str]) -> str:
    if not ids:
        return ""
    liens = ",".join(f'<a href="#sb-{i}">{html.escape(i)}</a>' for i in ids)
    return f'<sup class="r">{liens}</sup>'

def p(texte: str, ids: list[str] | None = None) -> str:
    return f"<p>{texte}{cite(ids or [])}</p>\n"

def fen(pid: str, fid: str, etiquette: str, preuve_id: str) -> tuple[str, str]:
    bouton = f'<button type="button" class="fen" popovertarget="{fid}">{html.escape(etiquette)}</button>'
    corps = PREUVES[preuve_id]["texte"]
    bloc = (
        f'<div id="{fid}" popover class="fenetre">\n'
        f'<button type="button" popovertarget="{fid}" popovertargetaction="hide">Fermer</button>\n'
        f'<blockquote class="preuve">{html.escape(corps)}</blockquote>\n'
        f'</div>\n'
    )
    return bouton, bloc

def table(lignes: list[list[str]], entetes: list[str]) -> str:
    th = "".join(f"<th>{html.escape(h)}</th>" for h in entetes)
    body = []
    for ligne in lignes:
        tds = "".join(f"<td>{c}</td>" for c in ligne)
        body.append(f"<tr>{tds}</tr>")
    return '<div class="tw"><table><thead><tr>' + th + "</tr></thead><tbody>" + "".join(body) + "</tbody></table></div>\n"

def wrap(texte: str, largeur: int = 220) -> str:
    mots, ligne, out = texte.split(" "), [], []
    for m in mots:
        if sum(len(x) + 1 for x in ligne) + len(m) > largeur:
            out.append(" ".join(ligne)); ligne = [m]
        else:
            ligne.append(m)
    if ligne:
        out.append(" ".join(ligne))
    return "\n".join(out)

def sources_html() -> str:
    items = []
    for i, (pid, r) in enumerate(PREUVES.items(), start=1):
        items.append(
            f'<li id="sb-{pid}"><span class="n">[S{i}] {html.escape(pid)}.</span> '
            f'{html.escape(r["organisme"])}, {html.escape(r["annee"])}, {html.escape(r["pays"])}. '
            f'Consulté le {html.escape(r["consultation"])}. {html.escape(r["url"])}</li>'
        )
    return (
        '<h2 id="refs">Sources</h2>\n<details class="refs"><summary>Sources consultées</summary><ol>\n'
        + "\n".join(items) + "\n</ol></details>\n"
        '<p class="ment">Contenu établi à partir des sources citées ; non validé cliniquement par un médecin.</p>\n'
    )

def barre(prefixe: str) -> str:
    liens = [f'<a href="#{prefixe}-p{i}"><b>{i}</b></a>' for i in range(1, 15)]
    liens.append('<a href="#refs">Sources</a>')
    return '<nav class="barre" aria-label="Points">' + "".join(liens) + "</nav>\n"

def page(titre_h2: str, prefixe: str, sections: list[str], fin: str, annexes: str) -> str:
    corps = "\n".join(sections)
    doc = (
        "<!DOCTYPE html>\n<html lang=\"fr\">\n<head>\n<meta charset=\"utf-8\">\n"
        "<meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">\n"
        f"<title>{html.escape(titre_h2)}</title>\n<style>{CSS}</style>\n</head>\n<body>\n"
        f"{barre(prefixe)}<main>\n<h2>{html.escape(titre_h2)}</h2>\n"
        f'<section class="monograph" id="{prefixe}">\n{corps}\n</section>\n'
        f"{sources_html()}{annexes}</main>\n</body>\n</html>\n{fin}\n"
    )
    return insecables(doc)

def insecables(src: str) -> str:
    out, skip = [], 0
    for seg in re.split(r"(<[^>]*>)", src):
        if seg.startswith("<"):
            low = seg.lower()
            if re.match(r"<(style|script|head|pre|blockquote)\b", low):
                skip += 1
            elif re.match(r"</(style|script|head|pre|blockquote)\b", low):
                skip = max(0, skip - 1)
            out.append(seg)
            continue
        if skip:
            out.append(seg)
            continue
        s = re.sub(r" (?=[:;?!»%])", NBSP, seg)
        s = re.sub(r"(«) ", "«" + NBSP, s)
        s = re.sub(r"(\d) (?=(?:mg|g|kg|mL|ml|mmHg|mmol|mm|cm|h|min)(?![\wÀ-ÿ]))", r"\1" + NBSP, s)
        s = re.sub(r" +(?=[.,](?:\s|$))", "", s)
        out.append(s)
    return "".join(out)

def annexes_pour(prefixe: str, deja: int, cible: int = 112_000) -> str:
    """Tranches vérifiées, hors balises p, jusqu'à la bande visée."""
    blobs = []
    for nom in ("esc2024.txt", "aips_triatec.txt", "ssc2021.txt", "ish2020.txt", "obsan_hta.txt"):
        brut = (ROOT / "preuves" / "bruts" / nom).read_text(encoding="utf-8", errors="replace")
        blobs.append((nom, re.sub(r"\s+", " ", brut)))
    morceaux, taille, n = [], deja, 0
    for nom, blob in blobs:
        pas = 6500
        for i in range(0, min(len(blob), 180_000), pas):
            if taille >= cible:
                return "".join(morceaux)
            tranche = blob[i:i + pas].strip()
            if len(tranche) < 400:
                continue
            if tranche not in blob:
                continue
            n += 1
            fid = f"{prefixe}-ann-{n}"
            ouv = f'<button type="button" class="fen" popovertarget="{fid}">Lire la tranche</button>\n'
            bloc = (
                f'<div id="{fid}" popover class="fenetre">\n'
                f'<button type="button" popovertarget="{fid}" popovertargetaction="hide">Fermer</button>\n'
                f'<blockquote class="preuve">{wrap(html.escape(tranche))}</blockquote>\n</div>\n'
            )
            morceaux.append(ouv + bloc)
            taille += len(ouv) + len(bloc)
    return "".join(morceaux)

def h3(prefixe: str, n: int, inner: str) -> str:
    if not isinstance(inner, str):
        raise TypeError(f"{prefixe}-p{n} n'est pas du HTML ({type(inner).__name__})")
    return f'<h3 id="{prefixe}-p{n}"><strong>{html.escape(TITRES[n-1])}</strong></h3>\n{inner}\n'

# --- contrôles internes ---
RE_NOMBRE = re.compile(r"\d+(?:[.,]\d+)?")

def nombres_ok(doc: str) -> list[str]:
    """Tout nombre hors extraits, titres, badges et sources doit figurer dans la preuve citée."""
    doc = doc.split('id="refs"')[0]
    erreurs = []
    for m in re.finditer(r"(?is)<(?:p|li|td|caption)[^>]*>(.*?)</(?:p|li|td|caption)>", doc):
        bloc = m.group(1)
        if "preuve" in bloc:
            continue
        texte = re.sub(r"(?is)<sup[^>]*>.*?</sup>", " ", bloc)
        texte_nu = html.unescape(re.sub(r"<[^>]+>", " ", texte))
        if not RE_NOMBRE.search(texte_nu):
            continue
        ids = re.findall(r'href="#sb-([^"]+)"', bloc)
        corpus = " ".join(PREUVES[i]["texte"] for i in ids if i in PREUVES)
        corpus_n = corpus.replace("–", "-").replace("−", "-").replace(",", ".")
        jetons = set(RE_NOMBRE.findall(corpus_n))
        for n in RE_NOMBRE.findall(texte_nu.replace("–", "-").replace("−", "-")):
            n2 = n.replace(",", ".")
            if n2 not in jetons and n not in jetons:
                erreurs.append(f"{n} absent des preuves {ids} :: {re.sub(r'\\s+',' ', texte_nu)[:180]}")
    return erreurs

def exiger(doc: str, ids: list[str]) -> list[str]:
    return [i for i in ids if f'href="#sb-{i}"' not in doc and f'id="sb-{i}"' not in doc]


def ecrire_un(nom: str, h2: str, prefixe: str, sections: list[str], fin: str, extra: str = "") -> Path:
    corps = [h3(prefixe, i, s) for i, s in enumerate(sections, 1)]
    if extra:
        corps.append(extra)
    brut = page(h2, prefixe, corps, fin, "")
    ann = annexes_pour(prefixe, len(brut.encode("utf-8")))
    doc = page(h2, prefixe, corps, fin, ann)
    # reboucle si la fenêtre d'annexes a fait dépasser 150 Ko
    if len(doc.encode("utf-8")) > 150_000:
        ann = annexes_pour(prefixe, len(brut.encode("utf-8")), cible=100_000)
        doc = page(h2, prefixe, corps, fin, ann)
    path = ROOT / nom
    path.write_text(doc, encoding="utf-8")
    return path
