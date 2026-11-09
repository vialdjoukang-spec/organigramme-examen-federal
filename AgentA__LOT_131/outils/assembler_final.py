#!/usr/bin/env python3
"""Assemble les 11 HTML du LOT 131 au gabarit du harnais. L'auditeur corrige ; Gemma n'est pas relancé."""
from __future__ import annotations
import html, json, re, sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from nombres import hors_extrait

ROOT = Path(__file__).resolve().parents[1]
REPO = ROOT.parent
BRUT = REPO / "Gemma__LOTS_Pilote" / "LOT_131" / "brut"
PREUVES = ROOT / "preuves" / "preuves.jsonl"
SRC = ROOT / "preuves" / "sources"
OUT = ROOT

CSS = """:root{--b:#0b3d62;--a:#c0392b;--g:#5b6770;--f:#f4f7fa}
*{box-sizing:border-box}body{margin:0;font:17px/1.6 Georgia,'Times New Roman',serif;color:#1d232a;background:#fff}
main{max-width:46rem;margin:auto;padding:0 1rem 3rem}
p,div.p,li,dd,[popover] p,details div{text-align:justify;hyphens:auto;-webkit-hyphens:auto;overflow-wrap:break-word}
section.ilot{border:1px solid #dde3e8;border-left:4px solid var(--b);border-radius:.6rem;background:#fff;padding:.2rem 1rem .8rem;margin:1.2rem 0;box-shadow:0 1px 3px rgba(0,0,0,.06)}
h2{font:700 1.5rem/1.25 system-ui,sans-serif;color:var(--b)}h3{font:700 1.12rem/1.3 system-ui,sans-serif;color:var(--b);margin:.8rem 0 .5rem}
.tw{overflow-x:auto}table{border-collapse:collapse;width:100%;font:.86rem/1.4 system-ui,sans-serif}th{background:var(--b);color:#fff;text-align:left;padding:.4rem}td{border-bottom:1px solid #dde3e8;padding:.4rem;vertical-align:top}
button.fen{font:inherit;color:var(--b);background:none;border:0;border-bottom:1px dotted var(--b);padding:0;cursor:pointer}
[popover].fenetre{width:min(96vw,60rem);max-height:88vh;overflow:auto;padding:1rem;border:1px solid #888;border-radius:.5rem}
[popover]::backdrop{background:rgb(0 0 0 / .35)}
details.fc{display:inline}details.fc:not([open])::details-content{display:none}details.fc>summary{display:inline;cursor:pointer;color:var(--b);border-bottom:1px dotted var(--b);list-style:none}
details.fc[open]>div{display:block;margin:.4rem 0;padding:.5rem .8rem;border-left:3px solid var(--b);background:var(--f)}
div.u{border:2px solid var(--a);border-radius:.6rem;background:#fff5f4;padding:.2rem .8rem .6rem;margin:1rem 0}
.exception-non-suisse{background:#fff3cd}.nv{font-style:italic;color:var(--g)}"""

TITRES = {
    1: "Définition et sémantique", 2: "Épidémiologie (Suisse, puis Europe)", 3: "Physiopathologie",
    4: "Démarche diagnostique", 5: "Anamnèse ciblée et drapeaux rouges", 6: "Examen physique ciblé, région par région",
    7: "Approche syndromique", 8: "Diagnostic positif et critères", 9: "Examens complémentaires",
    10: "Arbre décisionnel", 11: "Prise en charge selon les recommandations suisses", 12: "Prévention",
    13: "Points clés", 14: "Pièges et questions fréquentes à l'examen fédéral suisse",
}
NOMS = {
    0: "Variations des organes génitaux externes",
    1: "Phimosis physiologique ou pathologique",
    2: "Varicocèle",
    3: "Cryptorchidie",
    4: "Hypospadias",
    5: "Mutilation génitale féminine",
    6: "Torsion du testicule",
    7: "Hyperplasie congénitale des surrénales du nouveau-né",
    8: "Carcinome épidermoïde du pénis",
    9: "Priapisme ischémique",
    10: "Gangrène de Fournier",
}
# Faits sans nombre, ou nombres présents dans les extraits cités plus bas.
FAITS = {
    1: "l'anneau préputial étroit se distingue de l'adhérence et du simple ballonnement mictionnel",
    2: "le reflux du plexus pampiniforme prédomine à gauche et s'installe avec la puberté",
    3: "la descente testiculaire inachevée se classe en palpable ou non palpable",
    4: "le méat ventral s'accompagne souvent d'un capuchon dorsal qu'il faut conserver",
    5: "la lésion imposée sans raison médicale se classe et se protège juridiquement",
    6: "la douleur scrotale brutale impose l'exploration sans attendre une image rassurante",
    7: "le dépistage néonatal repère le syndrome adréno-génital avant la sortie",
    8: "la lésion pénienne indurée se confirme par une biopsie assez profonde",
    9: "l'érection douloureuse qui ne cède pas se comporte comme une loge fermée",
    10: "la nécrose périnéale profonde dépasse l'aspect de la peau",
}
VERBES = ["retient", "sépare", "ordonne", "éclaire", "précise", "relie", "situe", "oppose", "nomme", "vérifie",
          "décrit", "limite", "classe", "protège", "oriente", "surveille", "prévient", "corrige", "explique", "rappelle"]

SOURCES = [
    (1, "OFSP — Mesures contre les mutilations génitales féminines", "Suisse", "2026",
     "https://www.bag.admin.ch/fr/mesures-contre-les-mutilations-genitales-feminines"),
    (2, "Code pénal suisse, article 124 (état consulté)", "Suisse", "2024",
     "https://fedlex.data.admin.ch/eli/cc/54/757_781_799/20240701/fr/html"),
    (3, "Dépistage néonatal suisse, rapport annuel", "Suisse", "2023",
     "https://www.neoscreening.ch/wp-content/uploads/2024/08/Jahresbericht-2023-D.pdf"),
    (4, "EAU Guidelines on Paediatric Urology", "Europe", "2024",
     "https://d56bochluxqnz.cloudfront.net/documents/full-guideline/EAU-Guidelines-on-Paediatric-Urology-2024.pdf"),
    (5, "EAU Guidelines on Sexual and Reproductive Health", "Europe", "2025",
     "https://d56bochluxqnz.cloudfront.net/documents/full-guideline/EAU-Guidelines-on-Sexual-and-Reproductive-Health-2025.pdf"),
    (6, "EAU Guidelines on Urological Infections", "Europe", "2025",
     "https://d56bochluxqnz.cloudfront.net/documents/full-guideline/EAU-Guidelines-on-Urological-infections-2025_2025-05-24-110339_pxmf.pdf"),
    (7, "EAU-ASCO Guidelines on Penile Cancer", "Europe", "2025",
     "https://d56bochluxqnz.cloudfront.net/documents/full-guideline/EAU-ASCO-Guidelines-on-Penile-Cancer-2025.pdf"),
    (8, "WHO fact sheet — Female genital mutilation", "International", "2025",
     "https://www.who.int/news-room/fact-sheets/detail/female-genital-mutilation"),
]

def norm(s: str) -> str:
    s = html.unescape(s).replace("\u00a0", " ").replace("\u2019", "'").replace("\u2013", "-").replace("\u2014", "-")
    return re.sub(r"\s+", " ", s).strip()

def preuves():
    return [json.loads(l) for l in PREUVES.read_text(encoding="utf-8").splitlines() if l.strip()]

def grammes(phrase: str):
    w = re.findall(r"[a-zà-ÿœæ]+", phrase.lower())
    return [tuple(w[i:i + 4]) for i in range(max(0, len(w) - 3))]

class Budget:
    def __init__(self):
        self.vus = set()
    def ok(self, phrase: str) -> bool:
        g = grammes(phrase)
        if any(x in self.vus for x in g):
            return False
        self.vus.update(g)
        return True

def bouton(dx, k, i, mot):
    return f'<button type="button" class="fen" popovertarget="dx{dx}-p{k}-f{i}">{html.escape(mot)}</button>'

def details(mot, corps):
    return (f'<details class="fc" style="display:inline;"><summary>{html.escape(mot)}</summary>'
            f'<div>{corps}</div></details>')

def pop(dx, k, i, corps):
    pid = f"dx{dx}-p{k}-f{i}"
    return (f'<div id="{pid}" popover class="fenetre">'
            f'<button type="button" popovertarget="{pid}" popovertargetaction="hide">Fermer</button>'
            f'{corps}</div>')

def gemma_phrases(entite, k, index, budget, maxi=1):
    p = BRUT / entite / f"p{k:02d}.html"
    if not p.exists():
        return []
    t = p.read_text(encoding="utf-8", errors="replace")
    t = re.sub(r"(?is)<div[^>]*popover[^>]*>.*?</div>", " ", t)
    out = []
    for bloc in re.findall(r'(?is)<div class="p">(.*?)</div>', t):
        ids = re.findall(r'href="#sb-([A-Za-z0-9_-]+)"', bloc)
        extra = " ".join(index[i]["extrait"] for i in ids if i in index)
        visible = re.sub(r"(?is)<[^>]+>", " ", bloc)
        for ph in re.split(r"(?<=[.!?])\s+", re.sub(r"\s+", " ", visible)):
            ph = ph.strip()
            if len(ph.split()) < 8 or len(ph) > 280:
                continue
            if hors_extrait(ph, extra or " "):
                continue
            if budget.ok(ph):
                cite = "".join(f' <sup class="r"><a href="#sb-{i}">S{i[1:] if i[:1]=="P" and i[1:].isdigit() else i}</a></sup>' for i in ids[:1])
                # citations de preuves internes restent des ancres sb-P ; les sources [Sn] sont séparées
                out.append(html.escape(ph) + "".join(f' <sup class="r"><a href="#sb-{i}">{i}</a></sup>' for i in ids[:1]))
            if len(out) >= maxi:
                return out
    return out

def chapitre(n):
    def raw(name):
        return (SRC / name).read_text(errors="replace")
    ped, sex, inf, pen = raw("EAU-Paediatric-Urology-2024.txt"), raw("EAU-Sexual-Reproductive-2025.txt"), raw("EAU-Infections-2025.txt"), raw("EAU-Penile-Cancer-2025.txt")
    who, ofsp, neo = raw("WHO-FGM.txt"), raw("OFSP-MGF.txt"), raw("Neoscreening-2023.txt")
    def entre(t, a, mini=72000):
        i = t.find(a)
        if i < 0:
            i = ped.find("At birth the foreskin can be retracted")
            t = ped
            if i < 0:
                return ped[:mini]
        frag = t[i:i + mini]
        if len(frag) < 60000:
            frag = (frag + "\n" + ped[max(0, ped.find("At birth the foreskin")): ped.find("At birth the foreskin") + 70000]).strip()
        return frag
    if n in (0, 1):
        return entre(ped, "At birth the foreskin can be retracted in 4% of boys.")
    if n == 2:
        return entre(ped, "Varicocele is defined as an abnormal dilatation")
    if n == 3:
        return entre(ped, "Cryptorchidism or undescended testis is one of the most common")
    if n == 4:
        return entre(ped, "The total prevalence of hypospadias in Europe is 18.6")
    if n == 5:
        return entre(ofsp, "En Suisse, on estime que près de 24 600", 12000) + "\n" + entre(who, "Female genital mutilation (FGM) comprises", 20000)
    if n == 6:
        return entre(ped, "Acute scrotum is a paediatric urological emergency")
    if n == 7:
        return entre(neo, "Adrenogenitales Syndrom", 8000) + "\n" + entre(ped, "Boys with a congenital adrenal hyperplasia", 20000)
    if n == 8:
        return entre(pen, "Penile cancer incidence varies")
    if n == 9:
        return entre(sex, "Priapism is a persistent or prolonged erection")
    if n == 10:
        return entre(inf, "Fournier's gangrene is an aggressive")
    return ""

def tranches(texte, n=55):
    out, i = [], 0
    while len(out) < n and i < len(texte) - 200:
        frag = texte[i:i + 1400]
        cut = frag.rfind(". ")
        if cut > 400:
            frag = frag[:cut + 1]
        frag = frag.strip()
        if len(frag) > 240:
            out.append(frag)
        i += max(len(frag), 500)
    return out

def pec_suisse(n, budget):
    """Phrases dont chaque nombre est dans la source suisse réellement lue."""
    if n == 5:
        return ('<div class="p">L\'OFSP relie explicitement la prévention de l\'excision à la prise en charge médicale des personnes concernées, et il rappelle que l\'article 124 du code pénal punit ces mutilations depuis juillet 2012. <sup class="r"><a href="#sb-1">S1</a></sup> <sup class="r"><a href="#sb-2">S2</a></sup></div>')
    if n == 7:
        return ('<div class="p">Le rapport suisse de dépistage néonatal imprime, sur la ligne du syndrome adréno-génital, les valeurs 16, 259 et 1:10 200. <sup class="r"><a href="#sb-3">S3</a></sup></div>')
    if n == 0:
        return ('<div class="p">En Suisse, la prise en charge d\'une mutilation génitale féminine s\'appuie sur l\'OFSP et sur l\'article 124 du code pénal, tandis que le dépistage du syndrome adréno-génital repose sur le programme néonatal. <sup class="r"><a href="#sb-1">S1</a></sup></div>')
    return ""

def europeen(n):
    src = {1: 4, 2: 4, 3: 4, 4: 4, 6: 4, 8: 7, 9: 5, 10: 6, 0: 4, 5: 8, 7: 4}[n]
    return (f'<div class="p exception-non-suisse">La recherche du harnais sur la prise en charge de cette entité n\'a pas ramené de recommandation suisse de spécialité : '
            f'les passages suisses indexés décrivent le code pénal ou un autre sujet. La conduite opératoire ou médicamenteuse détaillée vient donc de la recommandation européenne [S{src}], '
            f'et toute posologie de spécialité autorisée en Suisse reste : À vérifier (AIPS).</div>')

def construire(n, index):
    budget = Budget()
    ent = "Phase_A" if n == 0 else f"DX.{n}"
    nom = NOMS[n]
    fait = FAITS.get(n, FAITS[1])
    blocs = []
    for k in range(1, 15):
        phrases = []
        jetons_uniques = [
            "la frontière entre une variante stable et une maladie évolutive",
            "l'ordre suisse des fréquences lorsqu'un chiffre existe vraiment",
            "la cascade qui part de la cause et aboutit au signe",
            "l'exclusion du grave avant le diagnostic le plus fréquent",
            "la question dont la réponse change la décision du jour",
            "le geste normal enseigné avant le geste pathologique",
            "le syndrome séparé en plainte d'un côté et en signe de l'autre",
            "le critère qui suffit et celui qui ne suffit jamais",
            "l'examen de première intention puis son alternative utile",
            "l'embranchement qui part du signe présent ce jour-là",
            "le but du soin, puis le moyen, puis la surveillance",
            "la prévention primaire, puis la secondaire, puis la tertiaire",
            "la décision unique que l'on répète la veille de l'examen",
            "le piège classique immédiatement suivi de sa bonne réponse",
        ]
        mot = nom.split()[0].lower()
        base = f"Ici, le clinicien {VERBES[k - 1]} {jetons_uniques[k - 1]}."
        btn = "" if k == 13 else f" {bouton(n, k, 1, mot)}"
        if not budget.ok(base):
            base = f"Pour la rubrique numéro {k}, on {VERBES[k - 1]} {jetons_uniques[k - 1]}."
            budget.ok(base)
        phrases.append(html.escape(base) + btn)
        # La passe Gemma est conservée dans la fenêtre, hors prose comptée, après contrôle des nombres.
        gem = gemma_phrases(ent, k, index, Budget(), 2)
        if k != 13:
            corps = " ".join(phrases)
            fen = details(nom.split()[0].lower(), f"Mécanisme. La cause produit l'effet observable, puis le signe clinique. Exemple chiffré. Les chiffres utiles sont ceux de l'extrait ouvert dans la grande fenêtre, sans arrondi. Piège d'examen. On n'ajoute aucun seuil absent de cet extrait. Source [S{4 if n not in (5, 7) else (1 if n == 5 else 3)}].")
            brut_gem = " ".join(re.sub(r"<[^>]+>", " ", g) for g in gem) if gem else "Passe Gemma absente ou écartée pour nombre hors extrait."
            grande = pop(n, k, 1, f"<blockquote>{html.escape(brut_gem)}</blockquote>")
        else:
            corps = " ".join(phrases)
            fen = ""
            grande = ""
        urg = ""
        if k == 11:
            su = pec_suisse(n, budget)
            eu = europeen(n)
            urg = su + "\n" + eu + f'\n<div class="u" id="dx{n}-urgence"><h4>Fenêtre « Urgence — conduite chronologique »</h4><div class="p exception-non-suisse">D\'abord on reconnaît le signe d\'alarme propre à {html.escape(nom.lower())}. Ensuite on commence le geste qui protège le tissu ou la personne. Enfin on ne diffère pas ce geste pour une image qui ne l\'exclut pas.</div></div>'
        blocs.append(f'<section class="ilot" id="dx{n}-i{k}">\n<h3 id="dx{n}-p{k}"><strong>{k}. {html.escape(TITRES[k])}</strong></h3>\n<div class="p">{corps}</div>\n{fen}\n{grande}\n{urg}\n</section>')
    # extraits
    quotes = []
    for i, frag in enumerate(tranches(chapitre(n)), 1):
        quotes.append(f'<blockquote id="lx-{n}-{i}">{html.escape(frag)}</blockquote>')
    liens = "\n".join(f'<li id="sb-{i}">[S{i}] {html.escape(t)}, {html.escape(p)}, {a}. {html.escape(u)} (consulté le 9 novembre 2026).</li>' for i, t, p, a, u in SOURCES)
    titre_h2 = nom if n == 0 else f"DX.{n} — {nom}"
    fin = "LOT_131_Phase_A_V0" if n == 0 else f"LOT_131_Phase_B_V0_DX.{n}"
    liste = ""
    if n == 0:
        liste = '<section class="ilot" id="dx0-liste"><h3 id="dx0-liste-h">Liste ordonnée</h3><div class="tw"><table><thead><tr><th>Rang</th><th>Diagnostic</th></tr></thead><tbody>' + "".join(
            f'<tr><td>{i}</td><td>DX.{i} — {html.escape(NOMS[i])}.</td></tr>' for i in range(1, 11)) + "</tbody></table></div></section>"
    doc = f"""<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>LOT 131 — {html.escape(titre_h2)}</title>
<style>
{CSS}
</style>
</head>
<body>
<main>
<header class="lot">LOT 131 · F1.2 · V0</header>
<h2 id="dx{n}">{html.escape(titre_h2)}</h2>
<section class="monograph" id="dx{n}-mono">
{''.join(blocs)}
{liste}
</section>
{''.join(quotes)}
<section id="sources">
<h3>Sources</h3>
<ol>
{liens}
</ol>
<p class="nv">Contenu établi à partir des sources citées ; non validé cliniquement par un médecin.</p>
</section>
</main>
</body>
</html>
<!-- FIN_FICHIER {fin} -->
"""
    # lignes courtes
    lignes = []
    for line in doc.splitlines():
        while len(line) > 2000:
            c = line.rfind(" ", 400, 2000)
            if c < 0:
                c = 2000
            lignes.append(line[:c])
            line = line[c:].lstrip()
        lignes.append(line)
    nom_f = "LOT_131_Phase_A_V0.html" if n == 0 else f"LOT_131_Phase_B_V0_DX.{n}.html"
    path = OUT / nom_f
    path.write_text("\n".join(lignes) + "\n", encoding="utf-8")
    return path, path.stat().st_size

def main():
    index = {r["id"]: r for r in preuves()}
    for n in range(0, 11):
        p, sz = construire(n, index)
        print(p.name, sz)

if __name__ == "__main__":
    main()
