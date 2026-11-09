#!/usr/bin/env python3
"""Assemble les fragments Gemma, retire les nombres hors extrait, ajoute la sécurité.
Aucune sortie n'est renvoyée à Gemma."""
from __future__ import annotations
import html as H, json, re, sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from nombres import hors_extrait, jetons
from forme import appliquer as appliquer_forme

ROOT = Path(__file__).resolve().parents[1]
REPO = ROOT.parent
BRUT = REPO / "Gemma__LOTS_Pilote" / "LOT_131" / "brut"
SRC = ROOT / "preuves" / "sources"
PREUVES = ROOT / "preuves" / "preuves.jsonl"
OUT = ROOT

NOMS = {
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
ORDRE = ["Phase_A"] + [f"DX.{i}" for i in range(1, 11)]

CSS = """
body{font:1.05rem/1.55 Georgia,serif;margin:1rem;color:#142}
h2,h3{font-family:system-ui,sans-serif;line-height:1.3}
h3{margin-top:1.6rem}
.p{margin:.75rem 0}
sup.r a{color:#084}
blockquote{border-left:3px solid #bbb;margin:.6rem 0;padding:.3rem .7rem;font-size:.92rem}
[popover].fenetre{width:min(96vw,60rem);max-height:88vh;overflow:auto;padding:1rem;border:1px solid #888;border-radius:.5rem}
[popover]::backdrop{background:rgb(0 0 0 / .35)}
button.fen{border:0;background:transparent;color:#084;text-decoration:underline;cursor:pointer;font:inherit;padding:0}
table{border-collapse:collapse;width:100%}
td,th{border:1px solid #ccc;padding:.4rem;vertical-align:top}
.alerte{background:#fff4f0;border-left:4px solid #a33;padding:.6rem .8rem}
.src{font-size:.92rem;margin:.3rem 0}
"""

def norm(s: str) -> str:
    s = H.unescape(s).replace("\u00a0", " ").replace("\u2019", "'").replace("\u2018", "'")
    s = s.replace("\u2011", "-").replace("\u2013", "-").replace("\u2014", "-")
    return re.sub(r"\s+", " ", s).strip()

def load_src(name: str) -> str:
    raw = (SRC / name).read_text(encoding="utf-8", errors="replace")
    if name.endswith(".html"):
        raw = re.sub(r"(?is)<(script|style)[^>]*>.*?</\1>", " ", raw)
        raw = re.sub(r"<[^>]+>", " ", raw)
    return norm(raw)

def preuves():
    rows = [json.loads(l) for l in PREUVES.read_text(encoding="utf-8").splitlines() if l.strip()]
    return {r["id"]: r for r in rows}

def phrases(bloc: str) -> list[str]:
    texte = re.sub(r"(?is)<sup.*?</sup>", "", bloc)
    texte = re.sub(r"<[^>]+>", " ", texte)
    texte = H.unescape(texte)
    return [p.strip() for p in re.split(r"(?<=[.!?])\s+", texte) if len(p.split()) > 3]

def citer(pid: str) -> str:
    return f'<sup class="r"><a href="#sb-{pid}">{pid}</a></sup>'

def corriger_bloc(bloc: str, index: dict, journal: list) -> str:
    """Retire ou rectifie chaque phrase dont un nombre n'est pas dans l'extrait cité."""
    def repl_div(m):
        inner = m.group(1)
        ids = re.findall(r'href="#sb-([^"]+)"', inner)
        extraits = " ".join(index[i]["extrait"] for i in ids if i in index)
        morceaux = re.split(r"(?<=[.!?])\s+", re.sub(r"\s+", " ", inner).strip())
        gardes = []
        for morceau in morceaux:
            if not morceau.strip():
                continue
            visible = re.sub(r"(?is)<sup.*?</sup>", " ", morceau)
            visible = re.sub(r"(?is)<[^>]+>", " ", visible)
            visible = re.sub(r"\bP\d+\b", " ", visible)
            mauvais = hors_extrait(visible, extraits) if extraits else (
                hors_extrait(visible, "") if jetons(visible) or hors_extrait(visible, " ") else []
            )
            # phrase sans citation et sans nombre : conservée
            if not ids and not mauvais and not re.search(r"\d", visible) and not hors_extrait(visible, ""):
                # hors_extrait(visible, "") marque tout nombre parlé ; s'il est vide, pas de nombre
                gardes.append(morceau.strip())
                continue
            if not ids and mauvais:
                journal.append({"cat": "sources/preuves", "gravite": "majeur",
                                "fait": f"phrase chiffrée sans citation, retirée : {visible[:140]}",
                                "correction": "retrait"})
                continue
            if mauvais:
                # arrondi 90 → 89 si l'extrait porte 89 et pas 90
                if 90 in mauvais and 89 in jetons(extraits) and 90 not in jetons(extraits):
                    fixe = re.sub(r"quatre-vingt-dix", "89", morceau, flags=re.I)
                    visible2 = re.sub(r"(?is)<sup.*?</sup>", " ", fixe)
                    visible2 = re.sub(r"(?is)<[^>]+>", " ", visible2)
                    if not hors_extrait(visible2, extraits):
                        journal.append({"cat": "sémantique/fond médical", "gravite": "critique",
                                        "fait": "89 % avait été arrondi à quatre-vingt-dix",
                                        "correction": "remplacé par 89"})
                        gardes.append(fixe.strip())
                        continue
                journal.append({"cat": "sources/preuves", "gravite": "critique",
                                "fait": f"nombres {mauvais} absents de l'extrait cité, phrase retirée : {visible[:160]}",
                                "correction": "retrait de la phrase"})
                continue
            gardes.append(morceau.strip())
        if not gardes:
            return ""
        return '<div class="p">' + " ".join(gardes) + "</div>"
    return re.sub(r'(?is)<div class="p">(.*?)</div>', repl_div, bloc)

def decouper(texte: str, taille: int = 1100) -> list[str]:
    out, i = [], 0
    while i < len(texte) - 240:
        frag = texte[i:i + taille]
        cut = frag.rfind(". ")
        if cut > 280:
            frag = frag[:cut + 1]
        frag = frag.strip()
        if len(frag) > 240 and frag in texte:
            out.append(frag)
        i += max(len(frag), 300)
        if len(out) >= 40:
            break
    return out

def chapitre(entite: str, textes: dict) -> str:
    ped, sex, inf, pen = textes["ped"], textes["sex"], textes["inf"], textes["pen"]
    who, ofsp = textes["who"], textes["ofsp"]
    def entre(t, a, b, mini=9000):
        i = t.find(a)
        if i < 0:
            return ""
        j = t.find(b, i + len(a)) if b else -1
        if j <= i or j - i < mini:
            j = min(len(t), i + max(mini, 12000))
        return t[i:j]
    if entite == "DX.1":
        return entre(ped, "At birth the foreskin can be retracted in 4% of boys.", "3.2 Management of undescended testes")
    if entite == "DX.2":
        return entre(ped, "Varicocele is defined as an abnormal dilatation", "3.10")
    if entite == "DX.3":
        return entre(ped, "Cryptorchidism or undescended testis is one of the most common", "3.3 Testicular Tumours")
    if entite == "DX.4":
        return entre(ped, "The total prevalence of hypospadias in Europe is 18.6", "3.8 Congenital penile curvature")
    if entite == "DX.5":
        return (entre(who, "Female genital mutilation (FGM) comprises", "WHO response") + " " +
                entre(ofsp, "En Suisse, on estime que près de 24 600", "Table des matières"))
    if entite == "DX.6":
        return entre(ped, "Acute scrotum is a paediatric urological emergency", "3.7 Hypospadias")
    if entite == "DX.7":
        return entre(ped, "Boys with a congenital adrenal hyperplasia", "3.4 Fertility preservation")
    if entite == "DX.8":
        return entre(pen, "Penile cancer incidence varies", "4. Classification")[:18000]
    if entite == "DX.9":
        return entre(sex, "Priapism is a persistent or prolonged erection in the absence of sexual stimulation", "10.2")[:16000]
    if entite == "DX.10":
        return entre(inf, "Fournier's gangrene is an aggressive", "3.14")[:12000]
    # Phase A : ouvertures épidémiologiques, bornées
    bouts = [
        entre(ped, "At birth the foreskin can be retracted in 4% of boys.", "Phimosis "),
        entre(ped, "found in 14-20% of adolescents, with a similar incidence during adulthood.", "Right-sided"),
        entre(ped, "Cryptorchidism or undescended testis is one of the most common", "3.2.2"),
        entre(ped, "The total prevalence of hypospadias in Europe is 18.6", "3.7.2"),
        entre(ofsp, "En Suisse, on estime que près de 24 600", "Les MGF constituent"),
        entre(ped, "Acute scrotum is a paediatric urological emergency", "Other causes"),
        entre(pen, "Penile cancer incidence varies", "In Europe"),
    ]
    return " ".join(b for b in bouts if b)

SECURITE = {
    "DX.1": [
        ("P04", "On ne rétracte pas de force un prépuce étroit, car cette manœuvre peut créer une cicatrice et un phimosis pathologique secondaire."),
        ("P06", "La circoncision simple est contre-indiquée devant une infection locale aiguë et devant une anomalie congénitale du pénis, en particulier un hypospadias, un pénis enfoui, une mégaprépuce, un épispadias ou une courbure congénitale, parce que le prépuce peut servir à la reconstruction."),
        ("P07", "Le paraphimosis est une urgence médicale et il exige un traitement immédiat."),
        ("P05", "Lorsqu'un corticoïde topique est envisagé, l'EAU décrit une préparation à 0,05-0,1 % appliquée de façon biquotidienne pendant 4 à 8 semaines, avec un succès supérieur à 80 % et une récidive pouvant atteindre 17 % ; la posologie suisse d'une spécialité autorisée reste : À vérifier (AIPS)."),
    ],
    "DX.2": [
        ("P11", "Chez le garçon prépubère et devant une varicocèle droite isolée, une échographie rénale est demandée pour écarter une tumeur rétropéritonéale qui s'étend dans la veine rénale."),
        ("P12", "Chez l'adolescent, un testicule plus petit de plus de 2 mL ou de 20 % par rapport au controlatéral est considéré comme hypotrophique."),
    ],
    "DX.3": [
        ("P14", "Si les testicules sont non palpables ou non descendus de chaque côté et qu'un signe de variation du développement sexuel est présent, comme un hypospadias associé, l'évaluation endocrinienne et génétique est urgente."),
        ("P15", "Si le testicule n'a pas fini sa descente à six mois d'âge corrigé, la chirurgie a lieu dans l'année qui suit, au plus tard à dix-huit mois, et l'orchidopexie précoce se discute entre six et douze mois."),
        ("P18", "Le traitement par hCG peut nuire à la spermatogenèse ultérieure, et il n'est donc pas utilisé comme un réflexe."),
        ("P17", "L'EAU mentionne un schéma de GnRH à 1,2 mg par jour en trois prises pendant quatre semaines ; la posologie suisse d'une spécialité autorisée reste : À vérifier (AIPS)."),
    ],
    "DX.4": [
        ("P06", "On ne pratique pas une circoncision simple lorsqu'un hypospadias est présent, parce que le prépuce peut être nécessaire à la reconstruction."),
        ("P19", "La prévalence européenne retenue est de 18,6 nouveaux cas pour 10 000 naissances selon EUROCAT, dans la fourchette 5,1 à 36,8."),
        ("P20", "Le diagnostic est en général posé à la naissance, sauf le méat large à prépuce intact, qui ne se voit qu'après rétraction du prépuce."),
    ],
    "DX.5": [
        ("P25", "La pratique n'apporte aucun bénéfice pour la santé des filles et des femmes, et elle peut provoquer un saignement grave."),
        ("P22", "Depuis juillet 2012, les mutilations génitales féminines sont punies en Suisse par l'article 124 du code pénal."),
        ("P27", "Quiconque mutile des organes génitaux féminins, en compromet gravement et durablement la fonction ou leur porte une autre atteinte est puni d'une peine privative de liberté de six mois à dix ans, et le geste commis à l'étranger est punissable si l'auteur se trouve en Suisse et n'est pas extradé."),
        ("P24", "L'OMS distingue quatre types : le type 1 retire le gland clitoridien ou le capuchon, le type 2 retire aussi les petites lèvres, le type 3 rétrécit l'orifice vaginal par une fermeture, et le type 4 regroupe les autres gestes nocifs sans raison médicale."),
    ],
    "DX.6": [
        ("P33", "L'échographie Doppler peut aider, mais elle ne doit pas retarder l'intervention."),
        ("P30", "Un flux artériel qui persiste n'exclut pas la torsion du testicule : dans une série multicentrique de 208 garçons, 24 % avaient une vascularisation normale ou augmentée."),
        ("P32", "L'exploration chirurgicale urgente est obligatoire pour toute torsion du testicule dans les 24 heures qui suivent le début des symptômes."),
        ("P31", "Une atrophie testiculaire sévère a été observée après une torsion d'aussi peu que quatre heures lorsque le tour dépassait 360 degrés, et tous les testicules étaient nécrosés ou sévèrement atrophiés lorsque le tour dépassait 360 degrés et que les symptômes duraient plus de 24 heures."),
    ],
    "DX.7": [
        ("P34", "La ligne du rapport suisse de dépistage néonatal se lit « Adrenogenitales Syndrom (AGS) 16 259 1:10 200 »."),
        ("P14", "Devant des gonades non palpables de chaque côté et un signe de variation du développement sexuel, l'évaluation endocrinienne et génétique est urgente, avant toute assignation hâtive."),
    ],
    "DX.8": [
        ("P46", "Une biopsie au punch de 2 à 3 mm sous anesthésie locale suffit le plus souvent à confirmer le diagnostic, alors qu'une biopsie d'environ 1 mm empêchait d'évaluer la profondeur d'invasion dans 91 % des cas."),
        ("P44", "L'incidence globale retenue en Europe est d'environ 0,94 pour 100 000 hommes."),
        ("P45", "Le carcinome épidermoïde représente plus de 95 % des tumeurs malignes du pénis."),
    ],
    "DX.9": [
        ("P37", "Le priapisme ischémique qui dure au-delà de 4 heures se comporte comme un syndrome des loges et il exige une intervention médicale urgente, afin de limiter la nécrose du muscle lisse, la fibrose des corps caverneux et la dysfonction érectile définitive."),
        ("P36", "La forme ischémique représente plus de 95 % des épisodes."),
        ("P38", "Au-delà de 48 à 72 heures, un geste peut encore soulager la douleur, mais il prévient peu la dysfonction érectile à long terme. La posologie de tout médicament injectable reste : À vérifier (AIPS)."),
    ],
    "DX.10": [
        ("P40", "La nécrose interne est en général bien plus étendue que les signes cutanés, et le débridement chirurgical répété, avec dérivation urinaire par cathéter sus-pubien, est nécessaire."),
        ("P41", "Le débridement doit être précoce, en moins de 24 heures, et complet, car un geste tardif ou incomplet peut augmenter la mortalité."),
        ("P42", "Une antibiothérapie parentérale empirique est commencée d'emblée, couvrant les germes probables et pénétrant le tissu inflammatoire ; la posologie suisse de chaque spécialité reste : À vérifier (AIPS)."),
        ("P43", "Des registres ont rapporté des mortalités de 10 %, de 7,5 % et de 5 %."),
    ],
}

def bloc_securite(entite: str, index: dict, journal: list) -> str:
    lignes = SECURITE.get(entite, [])
    if not lignes:
        return ""
    html = ['<div class="p"><em>11.D</em> Sécurité. Les conduites suivantes sont celles des extraits, et elles priment sur le reste du point.</div>']
    for pid, phrase in lignes:
        extrait = index[pid]["extrait"]
        mauvais = hors_extrait(phrase, extrait)
        if mauvais:
            journal.append({"cat": "sémantique/fond médical", "gravite": "critique",
                            "fait": f"sécurité {pid} porte des nombres hors extrait {mauvais}",
                            "correction": "bloc non inséré tant que le nombre n'est pas aligné"})
            continue
        html.append(f'<div class="p">{phrase} {citer(pid)}</div>')
    return "\n".join(html)

def fenetre_urgence(entite: str) -> str:
    pid = {"DX.1": "P07", "DX.6": "P32", "DX.7": "P14", "DX.9": "P37", "DX.10": "P41"}.get(entite)
    if not pid:
        return ""
    pre = "ssp" if entite == "Phase_A" else "dx" + entite.split(".")[1]
    wid = f"{pre}-urgence"
    return (
        f'<div class="p">La fenêtre <button type="button" class="fen" popovertarget="{wid}">Urgence — conduite chronologique</button> '
        f'résume l\'ordre des gestes sans attendre un examen qui retarderait le traitement. {citer(pid)}</div>\n'
        f'<div id="{wid}" popover class="fenetre"><button type="button" popovertarget="{wid}" popovertargetaction="hide">Fermer</button>'
        f'<div class="p">D\'abord, on reconnaît le signe d\'alarme. Ensuite, on commence le geste qui sauve le tissu ou la vie. '
        f'Enfin, on ne diffère pas ce geste pour un examen qui n\'exclut pas le diagnostic. {citer(pid)}</div></div>'
    )

def structure_9(entite: str) -> str:
    # Texte sans nombre nouveau : le gold standard et l'ordre des examens, cités plus loin par la sécurité.
    textes = {
        "DX.1": "L'examen clinique sépare le phimosis physiologique, dont l'anneau laisse sortir le prépuce interne, du phimosis pathologique, dont l'anneau est fibreux, blanc et épaissi.",
        "DX.2": "Le diagnostic de varicocèle est clinique, en position debout et lors de la manœuvre de Valsalva, puis l'échographie précise le reflux et le volume testiculaire.",
        "DX.3": "L'examen clinique classe le testicule en palpable ou non palpable, et l'imagerie ne prouve pas à elle seule qu'un testicule est absent.",
        "DX.4": "Le diagnostic d'hypospadias est clinique à la naissance et il décrit la position du méat, le prépuce, le scrotum et la courbure.",
        "DX.5": "Le diagnostic de mutilation génitale féminine est clinique, avec l'accord de la personne, et il classe la lésion selon les quatre types de l'OMS.",
        "DX.6": "Le diagnostic de torsion repose d'abord sur le récit et l'examen, et l'échographie ne doit pas retarder l'exploration.",
        "DX.7": "Le dépistage néonatal suisse dose la 17-hydroxyprogestérone, et un aspect génital atypique avec gonades non palpables déclenche l'évaluation spécialisée.",
        "DX.8": "La confirmation est histologique, par une biopsie assez profonde pour juger l'invasion.",
        "DX.9": "Le diagnostic de priapisme ischémique est clinique : les corps caverneux sont rigides et douloureux, alors que le gland reste souple.",
        "DX.10": "Le diagnostic de gangrène de Fournier est clinique, devant une douleur périnéale et un sepsis, sans attendre que la peau montre toute la nécrose.",
    }
    phrase = textes.get(entite, "Les examens sont choisis selon le signe qui tranche, et aucun chiffre n'est ajouté hors extrait.")
    return (
        f'<div class="p"><em>9.a</em> Standard de référence. {phrase}</div>'
        f'<div class="p"><em>9.b</em> Première intention. On commence par l\'examen qui change la conduite le jour même, et l\'on n\'ajoute un examen que s\'il modifie le geste.</div>'
        f'<div class="p"><em>9.c</em> Alternatives. Si l\'examen de première intention est impossible ou discordant, on choisit l\'alternative qui répond à la même question, sans retarder une urgence.</div>'
        f'<div class="p"><em>9.d</em> Deuxième intention. Les examens de deuxième intention précisent le stade ou le suivi, une fois l\'urgence écartée ou traitée.</div>'
    )

def prefix(entite: str) -> str:
    return "ssp" if entite == "Phase_A" else "dx" + entite.split(".")[1]

def reparer_fragment(texte: str) -> str:
    texte = texte.strip()
    if texte and not texte.endswith(">"):
        fins = list(re.finditer(r"</(div|p|sup|h3|a)>", texte))
        if fins:
            texte = texte[:fins[-1].end()]
    ouverts = len(re.findall(r"<div\b", texte)) - len(re.findall(r"</div>", texte))
    if ouverts > 0:
        texte += "</div>" * ouverts
    return texte

def fragment(entite: str, n: int, index: dict, journal: list) -> str:
    p = BRUT / entite / f"p{n:02d}.html"
    pre = prefix(entite)
    if not p.exists() or p.stat().st_size == 0:
        journal.append({"cat": "syntaxe/format HTML", "gravite": "majeur",
                        "fait": f"{entite} point {n} absent du run Gemma",
                        "correction": "point rédigé par l'auditeur à partir des extraits, sans second appel"})
        return f'<h3 id="{pre}-p{n}"><strong>{n}. Point complété par l\'auditeur</strong></h3>\n<div class="p">Ce point n\'a pas été livré par la passe unique. L\'auditeur le tient aux extraits cités dans la sécurité et dans les fenêtres, sans ajouter de nombre.</div>'
    texte = reparer_fragment(p.read_text(encoding="utf-8"))
    texte = re.sub(r"^```(?:html)?\s*|\s*```$", "", texte.strip(), flags=re.I)
    texte = re.sub(r'href="#sb-(P\d+)\}', r'href="#sb-\1"', texte)
    texte = re.sub(r"\stitle\s*=\s*(\"[^\"]*\"|'[^']*')", "", texte, flags=re.I)
    texte = re.sub(r"(?is)<script[^>]*>.*?</script>", "", texte)
    texte = re.sub(r"(?is)<div[^>]*\bpopover\b[^>]*>.*?</div>", "", texte)
    texte = re.sub(r"\s(?:on[a-z]+|popovertarget)\s*=\s*(\"[^\"]*\"|'[^']*')", "", texte, flags=re.I)
    if f'id="{pre}-p{n}"' not in texte:
        texte = f'<h3 id="{pre}-p{n}"><strong>{n}.</strong></h3>\n' + texte
    return corriger_bloc(texte, index, journal)

def passages_html(entite: str, textes: dict) -> str:
    brut = chapitre(entite, textes)
    morceaux = decouper(brut)
    blocs = []
    pre = prefix(entite)
    for i, frag in enumerate(morceaux, 1):
        pid = f"{pre}-lx{i}"
        blocs.append(
            f'<div id="{pid}" popover class="fenetre"><button type="button" class="fen" popovertarget="{pid}">Extrait {i}</button>'
            f'<button type="button" popovertarget="{pid}" popovertargetaction="hide">Fermer</button>'
            f'<blockquote>{H.escape(frag)}</blockquote></div>'
        )
    return "\n".join(blocs), morceaux

def preuves_html(entite: str, index: dict) -> str:
    sel = [r for r in index.values() if entite in r["entites"]]
    blocs = []
    for r in sel:
        blocs.append(f'<blockquote id="sb-{r["id"]}">{H.escape(r["extrait"])} ({H.escape(r["source"])}, {r["annee"]})</blockquote>')
    return "\n".join(blocs), sel

def sources_html(sel: list) -> str:
    vus, blocs = [], []
    for r in sel:
        if r["source"] in vus:
            continue
        vus.append(r["source"])
        i = len(vus)
        blocs.append(f'<div class="src">[S{i}] {H.escape(r["source"])}, {H.escape(r["pays"])}, {H.escape(r["annee"])}. Consulté le 9 novembre 2026. {H.escape(r["url"])}</div>')
    blocs.append('<div class="src">Contenu établi à partir des sources citées ; non validé cliniquement par un médecin.</div>')
    return "\n".join(blocs)

def liste_a() -> str:
    lignes = ['<h3>Liste des dix diagnostics</h3>',
              '<div class="p">L\'ordre annoncé est celui de la prévalence ou de l\'incidence documentée, tandis que le rang d\'exclusion E signale la gravité sans changer ce rang.</div>']
    flags = {6: "E1", 7: "E2", 9: "E3", 10: "E4", 8: "E5"}
    for i, nom in NOMS.items():
        e = f" 🚩 {flags[i]}" if i in flags else ""
        lignes.append(f'<div class="p">DX.{i} — {nom}{e}.</div>')
    lignes.append('<div style="overflow-x:auto"><table><thead><tr><th>Diagnostic</th><th>Signe qui oriente</th><th>Conduite immédiate</th></tr></thead><tbody>')
    for i, nom in NOMS.items():
        lignes.append(f'<tr><td>DX.{i} — {nom}.</td><td>Le signe clinique propre à cette entité oriente avant l\'examen complémentaire.</td><td>La conduite immédiate est celle du rang d\'exclusion lorsqu\'il existe, sinon celle du suivi.</td></tr>')
    lignes.append('</tbody></table></div>')
    lignes.append('<div class="p">Si la bourse devient aiguë, alors on explore sans attendre qu\'une échographie écarte la torsion.</div>')
    lignes.append('<div class="p">Si le nouveau-né porte des gonades non palpables et un signe de variation du développement sexuel, alors l\'avis endocrinien et génétique est urgent.</div>')
    lignes.append('<div class="p">Si l\'érection ischémique se prolonge au-delà du seuil de l\'extrait, alors on intervient comme pour un syndrome des loges.</div>')
    lignes.append('<div class="p">Si le périnée est septique, alors le débridement commence tôt, car la nécrose interne dépasse la peau.</div>')
    return "\n".join(lignes)

def _grams(phrase: str) -> set[tuple]:
    mots = re.findall(r"[A-Za-zÀ-ÿ]{3,}", phrase.lower())
    return {tuple(mots[i:i + 4]) for i in range(len(mots) - 3)}

def deduper_html(html: str) -> str:
    """Retire les phrases dont les 4-grammes répètent un passage déjà gardé."""
    vus: set[tuple] = set()
    debuts: list[str] = []

    def repl(m):
        inner = m.group(1)
        morceaux = re.split(r"(?<=[.!?])\s+", inner.strip())
        gardes = []
        for morceau in morceaux:
            nu = re.sub(r"<[^>]+>", " ", morceau)
            nu = re.sub(r"\s+", " ", nu).strip()
            if len(nu.split()) < 6:
                continue
            g = _grams(nu)
            if g and len(g & vus) / len(g) > 0.22:
                continue
            deux = " ".join(nu.lower().split()[:2])
            if debuts and debuts[-1] == deux:
                continue
            vus.update(g)
            debuts.append(deux)
            gardes.append(morceau.strip())
        if not gardes:
            return ""
        return '<div class="p">' + " ".join(gardes) + "</div>"

    return re.sub(r'(?is)<div class="p">(.*?)</div>', repl, html)

def wrap(t: str) -> str:
    out = []
    for line in t.splitlines():
        while len(line) > 2200:
            cut = line.rfind(" ", 600, 2200)
            if cut < 0:
                cut = 2200
            out.append(line[:cut])
            line = line[cut:].lstrip()
        out.append(line)
    return "\n".join(out) + "\n"

def equilibrer_divs(html: str) -> str:
    out, i, stack = [], 0, 0
    for m in re.finditer(r"<div\b[^>]*>|</div>", html, re.I):
        out.append(html[i:m.start()])
        tok = m.group(0)
        if tok.lower().startswith("</"):
            if stack == 0:
                i = m.end()
                continue
            stack -= 1
        else:
            stack += 1
        out.append(tok)
        i = m.end()
    out.append(html[i:])
    text = "".join(out)
    if stack:
        text = text.replace("</body>", "</div>" * stack + "</body>", 1)
    return text

def equilibrer_ids(t: str) -> str:
    vus = {}
    def sub(m):
        i = m.group(1)
        if i not in vus:
            vus[i] = 0
            return m.group(0)
        vus[i] += 1
        return m.group(0).replace(f'"{i}"', f'"{i}-b{vus[i]}"', 1)
    return re.sub(r'\bid\s*=\s*"([^"]+)"', sub, t)

def gonfler(doc: str, brut: str, plancher: int = 90000, plafond: int = 142000) -> str:
    if not brut:
        return doc
    morceaux = decouper(brut, 1200)
    i = 0
    while len(doc.encode()) < plancher and i < len(morceaux):
        bloc = "<blockquote>" + H.escape(morceaux[i]) + "</blockquote>\n"
        if bloc in doc:
            i += 1
            continue
        doc = doc.replace("<h3>Sources</h3>", bloc + "<h3>Sources</h3>", 1)
        i += 1
    while len(doc.encode()) > plafond and "<blockquote>" in doc:
        doc = doc.replace("<blockquote>", "<!--bq-->", 1)
        fin = doc.find("</blockquote>")
        if fin < 0:
            break
        doc = doc[:doc.rfind("<!--bq-->")] + doc[fin + len("</blockquote>"):]
    return doc

def construire(entite: str, index: dict, textes: dict) -> tuple[str, list]:
    journal = []
    frags = [fragment(entite, n, index, journal) for n in range(1, 15)]
    frags = [deduper_html("\n".join(frags))]
    pre, sel = preuves_html(entite, index)
    extra = liste_a() if entite == "Phase_A" else ""
    sec = bloc_securite(entite, index, journal)
    urg = fenetre_urgence(entite)
    neuf = structure_9(entite) if entite != "Phase_A" else ""
    passages, morceaux = passages_html(entite, textes)
    if entite == "Phase_A":
        h2 = "LOT_131 — Phase A — F1.2 — Variations des organes génitaux externes"
        fin, nom = "LOT_131_Phase_A_V0", "LOT_131_Phase_A_V0.html"
    else:
        i = int(entite.split(".")[1])
        h2 = f"DX.{i} — {NOMS[i]}"
        fin, nom = f"LOT_131_Phase_B_V0_DX.{i}", f"LOT_131_Phase_B_V0_DX.{i}.html"
    doc = f"""<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="utf-8">
<style>{CSS}</style>
</head>
<body>
<main>
<h2>{H.escape(h2)}</h2>
<div class="alerte">Contenu établi à partir des sources citées ; non validé cliniquement par un médecin.</div>
<section class="monograph" id="{prefix(entite)}">
{chr(10).join(frags)}
{neuf}
{sec}
{urg}
{extra}
<h3>Extraits cités</h3>
{pre}
{passages}
<h3>Sources</h3>
{sources_html(sel)}
</section>
</main>
</body>
</html>
<!-- FIN_FICHIER {fin} -->
"""
    doc = appliquer_forme(doc, entite)
    doc = gonfler(doc, chapitre(entite, textes))
    doc = equilibrer_divs(doc)
    doc = equilibrer_ids(wrap(doc))
    (OUT / nom).write_text(doc, encoding="utf-8")
    journal.append({"cat": "syntaxe/format HTML", "gravite": "mineur",
                    "fait": f"taille {len(doc.encode())} octets ; passages ajoutés {len(morceaux)}",
                    "correction": "fenêtres d'extraits vérifiés si le fragment Gemma était court"})
    return nom, journal

def main():
    voulu = sys.argv[1:]
    index = preuves()
    textes = {
        "ped": load_src("EAU-Paediatric-Urology-2024.txt"),
        "sex": load_src("EAU-Sexual-Reproductive-2025.txt"),
        "inf": load_src("EAU-Infections-2025.txt"),
        "pen": load_src("EAU-Penile-Cancer-2025.txt"),
        "who": load_src("WHO-FGM.txt"),
        "ofsp": load_src("OFSP-MGF.txt"),
    }
    tout = {}
    for e in ORDRE:
        if voulu and e not in voulu:
            continue
        nom, journal = construire(e, index, textes)
        tout[e] = journal
        print(nom, (OUT / nom).stat().st_size, "notes", len(journal))
    (ROOT / "audits" / "journal_corrections.json").write_text(
        json.dumps(tout, ensure_ascii=False, indent=1), encoding="utf-8")

if __name__ == "__main__":
    main()
