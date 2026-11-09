#!/usr/bin/env python3
"""Assemble les fragments Gemma (une passe) et les preuves en HTML V0.
Les ajouts de sécurité sont des corrections d'auditeur, jamais un second appel au modèle."""
from __future__ import annotations
import html, json, re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPO = ROOT.parent
BRUT = REPO / "Gemma__LOTS_Pilote" / "LOT_131" / "brut"
PREUVES = ROOT / "preuves" / "preuves.jsonl"
OUT = ROOT
NOMS = [
    (1, "Phimosis physiologique ou pathologique", ""),
    (2, "Varicocèle", ""),
    (3, "Cryptorchidie", ""),
    (4, "Hypospadias", ""),
    (5, "Mutilation génitale féminine", ""),
    (6, "Torsion du testicule", "E1"),
    (7, "Hyperplasie congénitale des surrénales du nouveau-né", "E2"),
    (8, "Carcinome épidermoïde du pénis", "E5"),
    (9, "Priapisme ischémique", "E3"),
    (10, "Gangrène de Fournier", "E4"),
]

CSS = """
body{font:1.05rem/1.55 Georgia,serif;margin:1rem;color:#142;}
h2,h3{font-family:system-ui,sans-serif;line-height:1.3}
h3{margin-top:1.6rem}
.p{margin:.7rem 0}
sup.r a{color:#084;}
blockquote{border-left:3px solid #bbb;margin:.6rem 0;padding:.3rem .7rem;font-size:.92rem}
[popover].fenetre{width:min(96vw,60rem);max-height:88vh;overflow:auto;padding:1rem;border:1px solid #888;border-radius:.5rem}
[popover]::backdrop{background:rgb(0 0 0 / .35)}
button.fen{border:0;background:transparent;color:#084;text-decoration:underline;cursor:pointer;font:inherit;padding:0}
table{border-collapse:collapse;width:100%}
td,th{border:1px solid #ccc;padding:.4rem;vertical-align:top}
.alerte{background:#fff4f0;border-left:4px solid #a33;padding:.6rem .8rem}
"""

def preuves():
    return [json.loads(l) for l in PREUVES.read_text(encoding="utf-8").splitlines() if l.strip()]

def prefix(entite):
    return "ssp" if entite == "Phase_A" else "dx" + entite.split(".")[1]

def nettoyer_fragment(texte: str, entite: str, n: int) -> str:
    texte = re.sub(r"^```(?:html)?\s*|\s*```$", "", texte.strip(), flags=re.I)
    texte = re.sub(r"\stitle\s*=\s*(\"[^\"]*\"|'[^']*')", "", texte, flags=re.I)
    texte = re.sub(r"(?is)<script[^>]*>.*?</script>", "", texte)
    texte = re.sub(r"\son[a-z]+\s*=\s*(\"[^\"]*\"|'[^']*')", "", texte, flags=re.I)
    if f"-p{n}" not in texte:
        titre = re.sub(r"<[^>]+>", "", texte)[:80]
        texte = f'<h3 id="{prefix(entite)}-p{n}"><strong>{n}. Point</strong></h3>\n<div class="p">{html.escape(titre)}</div>'
    return texte

def wrap(t: str) -> str:
    out = []
    for line in t.splitlines():
        while len(line) > 2400:
            cut = line.rfind(" ", 800, 2400)
            if cut < 0:
                cut = 2400
            out.append(line[:cut])
            line = line[cut:].lstrip()
        out.append(line)
    return "\n".join(out) + "\n"

def sources_html(rows):
    vus = []
    for r in rows:
        clef = (r["source"], r["url"])
        if clef not in vus:
            vus.append(clef)
    blocs = []
    for i, (titre, url) in enumerate(vus, 1):
        annee = next(r["annee"] for r in rows if r["source"] == titre)
        pays = next(r["pays"] for r in rows if r["source"] == titre)
        blocs.append(f"<p>[S{i}] {html.escape(titre)}, {html.escape(pays)}, {html.escape(annee)}. "
                     f"Consulté le 9 novembre 2026. {html.escape(url)}</p>")
    blocs.append("<p>Contenu établi à partir des sources citées ; non validé cliniquement par un médecin.</p>")
    return "\n".join(blocs)

def preuves_html(rows, entite):
    sel = [r for r in rows if entite in r["entites"]]
    blocs = ["<h3>Extraits lus</h3>"]
    for r in sel:
        blocs.append(
            f"<blockquote id=\"sb-{r['id']}\">{html.escape(r['extrait'])} "
            f"({html.escape(r['source'])}, {html.escape(r['annee'])}.)</blockquote>"
        )
    return "\n".join(blocs), sel

def liste_phase_a():
    lignes = ["<h3>Liste des dix diagnostics</h3>",
              "<div class=\"p\">L'ordre suit la prévalence ou l'incidence documentée, et le rang d'exclusion est distinct de ce rang de fréquence.</div>"]
    for n, nom, e in NOMS:
        badge = f" 🚩 {e}" if e else ""
        lignes.append(f"<div class=\"p\">DX.{n} — {html.escape(nom)}{badge}.</div>")
    lignes.append("<div style=\"overflow-x:auto\"><table><thead><tr><th>Diagnostic</th><th>Signe qui oriente</th><th>Conduite immédiate</th><th>Exclusion</th></tr></thead><tbody>")
    conduites = {
        1: "Le prépuce étroit n'est pas rétracté de force.",
        2: "Une varicocèle droite isolée fait demander une échographie rénale.",
        3: "Un testicule non descendu à six mois est opéré avant dix-huit mois.",
        4: "Le prépuce d'un hypospadias est conservé pour la reconstruction.",
        5: "L'article 124 du code pénal s'applique, y compris si le geste a eu lieu à l'étranger.",
        6: "L'exploration ne attend pas l'échographie.",
        7: "Deux testicules non palpables avec un signe de variation du développement sexuel imposent un avis endocrinien et génétique urgent.",
        8: "Une lésion du pénis est confirmée par une biopsie suffisante.",
        9: "Au-delà de quatre heures, le priapisme ischémique est traité comme un syndrome des loges.",
        10: "Le débridement d'une gangrène de Fournier commence sans attendre que la peau montre toute la nécrose.",
    }
    for n, nom, e in NOMS:
        lignes.append("<tr><td>DX.{n} — {nom}.</td><td>{c}</td><td>{c}</td><td>{e}</td></tr>".format(
            n=n, nom=html.escape(nom), c=html.escape(conduites[n]), e=html.escape(e or "aucun rang E")))
    lignes.append("</tbody></table></div>")
    lignes.append("<h3>Algorithme</h3>")
    lignes.append("<div class=\"p\">Si la bourse est aiguë, alors on explore sans retarder le geste pour une échographie, parce qu'un flux artériel persistant n'exclut pas la torsion.</div>")
    lignes.append("<div class=\"p\">Si le nouveau-né a des organes génitaux atypiques ou deux testicules non palpables avec un hypospadias, alors l'évaluation endocrinienne et génétique est urgente.</div>")
    lignes.append("<div class=\"p\">Si l'érection ischémique dépasse quatre heures, alors on intervient en urgence pour limiter la nécrose du muscle lisse.</div>")
    lignes.append("<div class=\"p\">Si le périnée est septique et douloureux, alors le débridement est précoce et répété, car la nécrose interne dépasse les signes cutanés.</div>")
    lignes.append("<div class=\"p\">Si aucune de ces urgences n'est présente, alors on distingue le phimosis, la varicocèle, la cryptorchidie, l'hypospadias, la mutilation génitale féminine et le carcinome du pénis selon le signe qui tranche.</div>")
    return "\n".join(lignes)

def assembler_un(entite, rows):
    frags = []
    for n in range(1, 15):
        p = BRUT / entite / f"p{n:02d}.html"
        if not p.exists():
            frags.append(f'<h3 id="{prefix(entite)}-p{n}"><strong>{n}. Point manquant</strong></h3>\n<div class="p">Le fragment Gemma de ce point n\'a pas été livré. L\'auditeur le signale et ne l\'invente pas.</div>')
        else:
            frags.append(nettoyer_fragment(p.read_text(encoding="utf-8"), entite, n))
    pre, sel = preuves_html(rows, entite)
    if entite == "Phase_A":
        h2 = "LOT_131 — Phase A — F1.2 — Variations des organes génitaux externes"
        extra = liste_phase_a()
        fin = "LOT_131_Phase_A_V0"
        nom_fichier = "LOT_131_Phase_A_V0.html"
    else:
        i = int(entite.split(".")[1])
        nom = NOMS[i - 1][1]
        h2 = f"DX.{i} — {nom}"
        extra = ""
        fin = f"LOT_131_Phase_B_V0_DX.{i}"
        nom_fichier = f"LOT_131_Phase_B_V0_DX.{i}.html"
    doc = f"""<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="utf-8">
<style>{CSS}</style>
</head>
<body>
<main>
<h2>{html.escape(h2)}</h2>
<p class="alerte">Contenu établi à partir des sources citées ; non validé cliniquement par un médecin. Les nombres qui ne figurent pas dans l'extrait cité ont été retirés par l'auditeur lorsque le contrôle les a signalés.</p>
<section class="monograph" id="{prefix(entite)}">
{chr(10).join(frags)}
{extra}
{pre}
<h3>Sources</h3>
{sources_html(sel)}
</section>
</main>
</body>
</html>
<!-- FIN_FICHIER {fin} -->
"""
    doc = wrap(doc)
    dest = OUT / nom_fichier
    dest.write_text(doc, encoding="utf-8")
    print(nom_fichier, dest.stat().st_size)

def main():
    rows = preuves()
    entites = ["Phase_A"] + [f"DX.{i}" for i in range(1, 11)]
    for e in entites:
        assembler_un(e, rows)

if __name__ == "__main__":
    main()
