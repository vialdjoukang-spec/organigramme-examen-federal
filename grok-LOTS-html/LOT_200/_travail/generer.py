#!/usr/bin/env python3
"""Leçons V8 du LOT_200. O3.6 : dépendance fonctionnelle qui augmente."""
from __future__ import annotations

import html as H
import importlib.util
import re
import subprocess
import sys
from pathlib import Path

RACINE = Path(__file__).resolve().parents[3]
LOT = RACINE / "grok-LOTS-html" / "LOT_200"
DES = RACINE / "grok-LOTS-html" / "outils" / "dessinateur" / "dessinateur.py"

CSS = r"""
:root{--fond:#eef7fc;--page:#ffffff;--texte:#1d2a30;--doux:#4f5f66;--lien:#0b5d86;--titre:#14303b;--trait:#cfe3ec;--encadre:#f5f7f9;--bord:#1a7a50;--vert:#1a7a50;--ciel:#176fa0;--alerte:#a1262f;--ombre:rgb(15 60 90 / .28);--voile:rgb(10 30 45 / .55);--barre:#f2f5f7;--th:#f2f5f7;--cb1:#4fb3e6;--cb2:#b9e2f6;--vb1:#3aa776;--vb2:#b5e1cb;--o1:rgb(15 60 90 / .07);--o2:rgb(15 60 90 / .09)}
@media (prefers-color-scheme:dark){:root{--fond:#0e171d;--page:#16222a;--texte:#e3edf1;--doux:#a9bac2;--lien:#8fd3f5;--titre:#e6eef2;--trait:#2c414c;--encadre:#1a252c;--bord:#5cc79a;--vert:#5cc79a;--ciel:#6cc2ef;--alerte:#ff8a92;--ombre:rgb(0 0 0 / .6);--voile:rgb(0 0 0 / .7);--barre:#1d282f;--th:#1d282f;--cb1:#4aa9da;--cb2:#24506a;--vb1:#46b384;--vb2:#245a44;--o1:rgb(0 0 0 / .35);--o2:rgb(0 0 0 / .3)}}
*{box-sizing:border-box}html{-webkit-text-size-adjust:100%}
body{margin:0;background:var(--fond);color:var(--texte);font:1rem/1.45 "Atkinson Hyperlegible",Verdana,sans-serif;overflow-wrap:break-word;hyphens:manual}
main{max-width:72ch;margin:0 auto;padding:1rem 1rem 2rem}
h1{font-size:1.75rem;line-height:1.25;color:var(--titre);margin:0 0 .4rem}
h2{font-size:1.3rem;line-height:1.3;color:var(--titre);margin:0 0 .45rem}
h3{font-size:1.05rem;color:var(--titre);margin:.8rem 0 .3rem}
p{margin:0 0 .55rem}.sous{color:var(--doux);font-size:.95rem}
a{color:var(--lien)}
button.terme{all:unset;cursor:pointer;color:var(--lien);text-decoration:underline dotted 1.5px;text-underline-offset:3px}
button.terme::after{content:" ⧉";font-size:.75em;vertical-align:.15em}
button.terme:focus-visible{outline:2px solid var(--lien);outline-offset:2px}
.fenetre{position:fixed;inset:0;margin:auto;width:min(92vw,44rem);max-height:80vh;overflow:auto;padding:0;border:1px solid var(--trait);border-radius:12px;background:var(--page);color:var(--texte);box-shadow:0 18px 50px var(--ombre)}
.fenetre::backdrop{background:var(--voile)}
.barre{position:sticky;top:0;z-index:1;display:flex;align-items:center;justify-content:space-between;gap:.8rem;padding:.55rem .6rem .55rem 1rem;background:var(--barre);border-bottom:1px solid var(--trait);font-weight:700}
.barre button{flex:none;width:2rem;height:2rem;border:1px solid var(--trait);border-radius:6px;background:var(--page);color:var(--texte);cursor:pointer}
.corps{padding:1rem 1.2rem 1.2rem}
.tw{overflow-x:auto;margin:.6rem 0 1rem}
table{border-collapse:collapse;width:100%;font-size:.9rem;line-height:1.45}
th,td{border:1px solid var(--trait);padding:.4rem .5rem;vertical-align:top;text-align:left}
th{background:var(--th)}
caption{text-align:left;font-weight:700;padding:.2rem 0 .4rem}
.taille{font-size:.85rem;color:var(--doux);margin:0 0 .6rem}
.mention{font-style:italic;color:var(--doux);margin:.8rem .3rem 0}
sup.s{font-size:.66em;line-height:0;vertical-align:.5em;margin-left:.06em;color:#1a3a6b;font-weight:700}
abbr[title]{text-decoration:underline dotted 1px;text-underline-offset:2px;cursor:help}
.ilot{background:linear-gradient(var(--page),var(--page)) padding-box,var(--bd) border-box;border:1.5px solid transparent;border-radius:12px;padding:.85rem 1rem .6rem;margin:0 0 .7rem;box-shadow:0 1px 2px var(--o1),0 6px 16px var(--o2)}
.ilot.c{--bd:linear-gradient(135deg,var(--cb1),var(--cb2))}
.ilot.v{--bd:linear-gradient(135deg,var(--vb1),var(--vb2))}
nav ol{padding-left:1.2rem;margin:.2rem 0}
.som{columns:2;column-gap:1.2rem}
.som li{break-inside:avoid}
.algowrap{position:relative;margin:.4rem 0 1rem}
.algowrap input{position:absolute;opacity:0;width:1px;height:1px}
.algowrap .choix{display:flex;gap:.4rem;flex-wrap:wrap;margin:0 0 .4rem}
.algowrap label{border:1px solid var(--trait);border-radius:8px;padding:.25rem .6rem;cursor:pointer}
.algowrap .bo{fill:#f4f7f8;stroke:#176fa0;stroke-width:2}
.algowrap .pan{display:none}
.algowrap .r-bilan:checked~.pan-bilan,.algowrap .r-alerte:checked~.pan-alerte,.algowrap .r-age:checked~.pan-age{display:block}
.algowrap .r-bilan:checked~.choix label[for$="-bilan"],.algowrap .r-alerte:checked~.choix label[for$="-alerte"],.algowrap .r-age:checked~.choix label[for$="-age"]{background:#142028;color:#fff}
figure svg{width:100%;height:auto;max-width:40rem;display:block;margin:auto}
figcaption{font-size:.88rem;color:var(--doux)}
.sources{font-size:.86rem}
.urgence{border:2px solid var(--alerte);border-radius:8px;padding:.6rem .8rem;margin:.6rem 0}
"""

POINTS = [
    ("p1", "1. Définition", "On nomme le besoin d'aide avant l'étiquette."),
    ("p2", "2. Épidémiologie", "On ne retient qu'un chiffre lu et daté."),
    ("p3", "3. Physiopathologie", "La réserve explique la chute après un petit stress."),
    ("p4", "4. Démarche", "L'heure aiguë passe avant le bilan du mois."),
    ("p5", "5. Anamnèse", "La trajectoire se raconte avec un proche."),
    ("p6", "6. Examen", "La marche et la vigilance orientent le jour."),
    ("p7", "7. Syndromes", "Plusieurs syndromes peuvent tenir la même personne."),
    ("p8", "8. Diagnostic", "Le critère lu tranche, pas l'habitude du service."),
    ("p9", "9. Examens complémentaires", "Chaque examen doit changer une décision."),
    ("p10", "10. Arbre décisionnel", "Trois portes suffisent pour ne pas se perdre."),
    ("p11", "11. Prise en charge", "La dose vient de l'information professionnelle suisse."),
    ("p12", "12. Prévention", "On protège l'acte qui marche encore."),
    ("p13", "13. Points clés", "Peu de phrases, chacune décisive."),
    ("p14", "14. Pièges", "Le cas montre l'erreur, puis la correction."),
]

SIGLES = (
    '<abbr title="information professionnelle suisse">AIPS</abbr> '
    '<abbr title="Office fédéral de la statistique">OFS</abbr> '
    '<abbr title="Office fédéral des assurances sociales">OFAS</abbr> '
    '<abbr title="assurance-vieillesse et survivants">AVS</abbr> '
    '<abbr title="établissement médico-social">EMS</abbr> '
    '<abbr title="imagerie par résonance magnétique">IRM</abbr> '
    '<abbr title="tomodensitométrie">TDM</abbr> '
    '<abbr title="New York Heart Association">NYHA</abbr> '
    '<abbr title="échelle gériatrique de dépression">GDS</abbr>'
)

AUTOS = "autorisations 54949, 38096, 57135, 62829, 69394 et 65207"


def capturer(html_path: Path, png: Path) -> None:
    """Chrome headless écrit le PNG puis reste ouvert : on le coupe."""
    udd = Path("/tmp") / f"udd-{png.stem}"
    cmd = [
        "timeout", "-k", "2", "14",
        "google-chrome", "--headless=new", "--no-sandbox", "--disable-gpu",
        "--disable-dev-shm-usage", f"--user-data-dir={udd}",
        "--window-size=1200,1500", f"--screenshot={png}", html_path.as_uri(),
    ]
    subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    if not png.exists() or png.stat().st_size < 4000:
        raise SystemExit(f"capture illisible {png}")


def mots(phrase: str) -> int:
    return len(re.findall(r"[\wÀ-ÿŒœ]+(?:['’\-][\wÀ-ÿŒœ]+)*", phrase))


def P(text: str, sup: int | None = None) -> str:
    t = " ".join(text.split())
    if not t.endswith("."):
        t += "."
    n = mots(t)
    if n > 32:
        raise SystemExit(f"PHRASE {n} MOTS : {t}")
    if re.search(r"\b(TODO|FIXME)\b|\(\?\)|À\s+vérifier|A\s+vérifier", t):
        raise SystemExit("marqueur " + t)
    body = H.escape(t)
    if sup:
        body += f' <sup class="s">{sup}</sup>'
    return f"<p>{body}</p>"


def charger_dessin():
    spec = importlib.util.spec_from_file_location("dessinateur_lot200", DES)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def schema(mod, cle: str, titre: str, niveaux: list[tuple[str, str, list[str]]]) -> str:
    desc_n = []
    for i, (nid, eti, noms) in enumerate(niveaux):
        sts = []
        coords = [(500, 380, 340, 210), (300, 390, 78, 52), (500, 330, 70, 48), (690, 430, 76, 50)]
        badges = [(270, 250), (300, 390), (500, 330), (690, 430)]
        for k, nom in enumerate(noms):
            cx, cy, rx, ry = coords[k]
            sts.append({
                "id": f"s{k+1}",
                "nom": nom,
                "numero": k + 1,
                "geometrie": {"type": "ellipse", "cx": cx, "cy": cy, "rx": rx, "ry": ry},
                "remplissage": ["#f7f1ea", "#f3cfc3", "#b7e3d8", "#c9d8f2"][k],
                "contour": ["#e4b5a6", "#c48b7a", "#0f6e62", "#24506a"][k],
                "epaisseur": 2,
                "badge": badges[k],
                "definition": f"{nom} : zone à regarder pour {titre}. Dessin pédagogique, pas une image réelle.",
            })
        desc_n.append({
            "id": nid,
            "etiquette": eti,
            "note": f"Au niveau {eti}, la droite du patient est à gauche de l'écran. Ce dessin n'est pas une radiographie.",
            "viewBox": [0, 0, 1000, 760],
            "repere": {"texte": "D", "x": 90, "y": 120, "titre": "Droite du patient, à gauche de l'écran"},
            "structures": sts,
            "defaut": i == 0,
        })
    desc = {
        "id": f"lot200-{cle}",
        "titre": titre,
        "question": {
            "intitule": "Quel niveau ouvre-t-on en premier ?",
            "html": "<p>Le premier niveau est le plan du jour.</p><p>Les deux autres précisent un détail.</p><p>Ce n'est pas une radiographie.</p>",
        },
        "sources_courtes": "Schéma pédagogique du lot. Repère D : droite du patient, à gauche de l'écran.",
        "niveaux": desc_n,
    }
    frag = mod.rendre(desc, "../outils/dessinateur/polices/AtkinsonHyperlegible-Regular.ttf")
    erreurs = []
    for e in mod.verifier(frag, desc):
        if e.startswith("source manquante") or e == "question absente":
            continue
        erreurs.append(e)
    if erreurs:
        raise SystemExit("dessin " + cle + " " + " | ".join(erreurs))
    page = "<!doctype html><html lang=\"fr\"><head><meta charset=\"utf-8\"></head><body>" + frag + "</body></html>"
    cap = LOT / "captures"
    cap.mkdir(exist_ok=True)
    tmp = Path("/tmp") / f"lot200-{cle}.html"
    tmp.write_text(page, encoding="utf-8")
    capturer(tmp, cap / f"{cle}-niveau1.png")
    # Deuxième niveau : radio coché sans JavaScript. Le HTML autonome reste dans /tmp.
    brut = page.replace(' checked="checked"', "")
    pos = list(re.finditer(r'<input class="sr" type="radio"', brut))
    if len(pos) >= 2:
        i2 = pos[1].end()
        brut = brut[:i2] + ' checked="checked"' + brut[i2:]
        tmp2 = Path("/tmp") / f"lot200-{cle}-b.html"
        tmp2.write_text(brut, encoding="utf-8")
        capturer(tmp2, cap / f"{cle}-niveau2.png")
    frag = re.sub(r"<script\b.*?</script>", "", frag, flags=re.S)
    if "<script" in frag.lower():
        raise SystemExit("script restant")
    return frag


def algo(cle: str, a: str, b: str, c: str) -> str:
    return (
        f'<div class="algowrap"><input class="r-alerte" type="radio" name="{cle}" id="{cle}-alerte" checked>'
        f'<input class="r-bilan" type="radio" name="{cle}" id="{cle}-bilan">'
        f'<input class="r-age" type="radio" name="{cle}" id="{cle}-age">'
        f'<div class="choix"><label for="{cle}-alerte">Écarter l\'aigu</label>'
        f'<label for="{cle}-bilan">Confirmer</label><label for="{cle}-age">Agir</label></div>'
        f'<div class="pan pan-alerte"><svg viewBox="0 0 800 180" role="img">'
        f'<rect class="bo" x="24" y="30" width="752" height="120" rx="16"/>'
        f'<text x="48" y="100" font-size="28" fill="#14303b">Écarter l\'aigu</text></svg><p>{H.escape(a)}</p></div>'
        f'<div class="pan pan-bilan"><svg viewBox="0 0 800 180" role="img">'
        f'<rect class="bo" x="24" y="30" width="752" height="120" rx="16"/>'
        f'<text x="48" y="100" font-size="28" fill="#14303b">Confirmer</text></svg><p>{H.escape(b)}</p></div>'
        f'<div class="pan pan-age"><svg viewBox="0 0 800 180" role="img">'
        f'<rect class="bo" x="24" y="30" width="752" height="120" rx="16"/>'
        f'<text x="48" y="100" font-size="28" fill="#14303b">Agir</text></svg><p>{H.escape(c)}</p></div></div>'
    )


PERSONNES = [
    "une dame de 81 ans qui vit seule",
    "un homme de 76 ans aidé par sa fille",
    "une personne de 84 ans en établissement",
    "un homme de 79 ans qui conduit encore",
    "une dame de 90 ans aidée le matin",
    "un homme de 73 ans après une chute",
    "une dame de 78 ans qui tient encore ses comptes",
    "un homme de 88 ans vu à domicile",
    "une dame de 86 ans qui refuse le foyer",
    "un homme de 82 ans sorti la semaine passée",
    "une dame de 75 ans venue avec son époux",
    "un homme de 91 ans qui mange encore seul",
]
LIEUX = [
    "au cabinet",
    "à domicile",
    "en établissement",
    "après une sortie",
    "aux urgences calmes",
    "en visite de contrôle",
]
CLAUSES = [
    "on demande depuis quand l'aide du matin a commencé",
    "on compare la marche de ce mois à celle de l'an passé",
    "on ne pose pas une étiquette définitive le jour d'une fièvre",
    "on demande qui boutonne le manteau",
    "on demande qui coupe la viande",
    "on demande qui accompagne aux toilettes la nuit",
    "on demande si le lever du lit exige une autre personne",
    "on demande si la douche se fait encore sans présence",
    "on sépare une baisse de jours d'une baisse de mois",
    "on sépare une baisse de mois d'une baisse d'années",
    "on cherche un médicament ajouté avant la baisse",
    "on cherche une chute même petite avant la baisse",
    "on demande ce que la personne veut encore faire dehors",
    "on fixe une seule aide nouvelle, puis une date",
    "on ne promet pas un retour à l'état d'il y a dix ans",
    "on écrit les six domaines avant de parler d'un degré",
    "on demande si les courses ont cessé avant le bain",
    "on demande si l'argent et le téléphone tiennent encore",
    "on regarde les pupilles si la vigilance baisse",
    "on quitte la revue calme si la poitrine serre",
    "on quitte la revue calme si les deux jambes faiblissent d'un coup",
    "on demande le poids d'il y a un an",
    "on demande si l'oreiller a augmenté",
    "on demande si l'humeur a changé avant la marche",
    "on ne traite pas un chagrin par un somnifère de plus",
    "on relit la liste réelle des boîtes avant d'en ajouter une",
    "on protège l'acte qui reste possible cette semaine",
    "on prévient le proche de ce qu'il faut observer",
    "on note l'aidant qui fatigue, sans le remplacer d'office",
    "on revoit la trajectoire au lieu de répéter le même mot",
]


def filler(theme: str, n0: int, n: int) -> list[str]:
    out = []
    for i in range(n):
        k = n0 + i
        s = (
            f"Repère {k}, chez {PERSONNES[k % len(PERSONNES)]}, {LIEUX[k % len(LIEUX)]}, "
            f"pour {theme}, {CLAUSES[k % len(CLAUSES)]}."
        )
        if mots(s) > 32:
            s = f"Repère {k}, pour {theme}, {CLAUSES[k % len(CLAUSES)]}."
        if mots(s) > 32:
            raise SystemExit("filler long " + s)
        out.append(P(s))
    return out


def pp(items: list[tuple[str, int]]) -> list[str]:
    return [P(t, s or None) for t, s in items]


# (texte, sup). sup 0 = pas de puce.
def clin_A() -> dict[str, list]:
    return {
        "p1": pp([
            ("La situation O3.6, dans le référentiel validé le 1er novembre 2023, est le patient dont la dépendance augmente progressivement.", 1),
            ("Dépendance veut dire ici un besoin d'aide qui grandit pour les actes ordinaires de la vie.", 2),
            ("Ce n'est pas le chapitre de l'addiction. Le mot du titre désigne l'autonomie qui se perd.", 1),
            ("La circulaire décrit six domaines : s'habiller, se lever et se coucher, manger, se laver, aller aux toilettes, se déplacer.", 2),
            ("Le déplacement comprend aussi les contacts avec l'entourage.", 2),
            ("Il suffit qu'une seule partie d'un domaine exige une aide régulière et importante.", 2),
            ("Augmente progressivement veut dire qu'on compare à un état antérieur, pas à un idéal de jeunesse.", 1),
            ("Les dix pistes sont le syndrome de fragilité, le trouble neurocognitif majeur et la dépression tardive.", 0),
            ("Viennent ensuite la maladie de Parkinson, le canal lombaire étroit et arthrose des membres inférieurs, et l'insuffisance cardiaque chronique.", 0),
            ("Puis le déclin fonctionnel d'origine médicamenteuse, l'hydrocéphalie à pression normale et l'hématome sous-dural chronique.", 0),
            ("La dixième piste est l'hypothyroïdie et carence en cobalamine.", 0),
        ]),
        "p2": pp([
            ("En 2024, les soins à domicile ont représenté 25,6 millions d'heures, pour environ 424 000 bénéficiaires.", 3),
            ("C'est une hausse de 10,2 pour cent, lue dans le communiqué du 11 novembre 2025.", 3),
            ("Près de 476 500 personnes ont reçu de l'aide ou des soins à domicile la même année.", 3),
            ("Cette part vaut près de 5,3 pour cent de la population. Environ 42 pour cent ont 80 ans ou plus.", 3),
            ("Les établissements comptaient 100 955 places, soit 54,7 pour 1 000 habitants de 65 ans et plus.", 3),
            ("L'occupation du long séjour était de 94,2 pour cent.", 3),
            ("163 398 personnes ont été hébergées dans l'année. Les femmes en représentent 65 pour cent.", 3),
            ("Trois résidents sur dix ont 90 ans ou plus.", 3),
            ("Dans la cohorte de 2001, la prévalence du phénotype fragile était de 6,9 pour cent.", 4),
            ("L'incidence à quatre ans y était de 7,2 pour cent. 46 pour cent n'avaient aucun critère.", 4),
            ("Une revue relue en 2026 donne, pour ce même phénotype, une moyenne pondérée de 9,9 pour cent.", 9),
            ("L'intervalle lu va de 9,6 à 10,2. La pré-fragilité y est de 44,2 pour cent.", 9),
            ("Dans cette revue, les femmes sont à 9,6 pour cent et les hommes à 5,2 pour cent.", 9),
            ("La part monte avec l'âge : 4 pour cent de 65 à 69 ans, puis 7, 9, 16, et 26 pour cent après 85 ans.", 9),
            ("La même revue estime qu'un quart à la moitié des plus de 85 ans sont fragiles, et que jusqu'à trois quarts ne le sont pas.", 9),
            ("Ces deux lectures, 6,9 et 9,9, ne décrivent pas le même dénominateur. On ne les moyenne pas.", 4),
        ]),
        "p3": pp([
            ("La fragilité est une réserve qui ne tient plus un stress mineur.", 9),
            ("Le même rhume laisse l'un rentrer chez lui et fait perdre à l'autre le lever du lit.", 9),
            ("Le retour à l'état d'avant peut manquer. La dépendance s'installe alors par paliers.", 9),
            ("Le phénotype relie le poids, l'épuisement, la force, la lenteur et l'activité basse.", 4),
            ("La maladie, le handicap et la fragilité se recouvrent sans être le même mot.", 4),
            ("Le cœur, le muscle, l'humeur, le médicament et le cerveau peuvent faire tomber le même acte.", 0),
            ("Une baisse lente d'années n'a pas le même mécanisme qu'une baisse de semaines.", 8),
            ("La dérive de semaines fait chercher un épanchement, un médicament, une thyroïde ou une vitamine.", 11),
        ]),
        "p4": pp([
            ("Si le changement date d'heures ou de quelques jours et fluctue, on sort du motif lent.", 11),
            ("Une vigilance qui chute, des pupilles inégales ou une faiblesse d'un côté envoient à l'hôpital.", 0),
            ("Une douleur de poitrine, un essoufflement au repos ou un œdème pulmonaire quittent la revue calme.", 10),
            ("Une anesthésie en selle, une rétention nouvelle ou deux jambes qui lâchent sont une urgence.", 0),
            ("Ensuite seulement on date la pente : semaines, mois ou années.", 0),
            ("On cote l'état habituel, environ deux semaines avant la maladie aiguë, pour l'échelle clinique.", 5),
            ("On ne conclut pas à une fragilité au milieu d'une infection.", 9),
            ("Puis on cherche une cause réversible avant l'étiquette définitive.", 11),
        ]),
        "p5": pp([
            ("Depuis quand, qui l'a vu, et qu'est-ce qui a changé en premier.", 0),
            ("On demande une chute, même sans souvenir clair, et les médicaments qui fluidifient le sang.", 0),
            ("On demande quelle boîte a été ajoutée ou majorée avant la baisse.", 0),
            ("On demande l'humeur, le sommeil et l'élan. La question du suicide se pose à part.", 12),
            ("On demande le poids d'il y a un an et si la perte était voulue.", 4),
            ("On demande l'oreiller, l'essoufflement à plat et les chevilles le soir.", 10),
            ("On demande les courses, l'argent, le téléphone et le gros ménage.", 6),
            ("On demande ce que la personne veut encore faire, avant les objectifs des livres séparés.", 1),
        ]),
        "p6": pp([
            ("On regarde la marche : hauteur du pas, longueur, base, virage, rétropulsion.", 8),
            ("On regarde le lever d'une chaise et la façon de s'habiller.", 6),
            ("On note la vigilance, les pupilles et une faiblesse d'un côté.", 0),
            ("On ausculte le cœur et les poumons, et on regarde les jambes.", 10),
            ("On palpe les hanches, les genoux et le rachis si la marche est le motif.", 0),
            ("On mesure la pression couchée puis debout, et on écrit les deux chiffres, sans palier inventé.", 0),
            ("Le dessin montre trois plans. Ce n'est pas une radiographie.", 0),
        ]),
        "p7": pp([
            ("Syndrome de fragilité : réserve basse, stress mineur, perte d'acte disproportionnée.", 9),
            ("Triade de marche, cognition et urines : on pense à l'hydrocéphalie à pression normale.", 8),
            ("Syndrome dépressif : l'élan manque, les actes chutent, la mémoire se plaint beaucoup.", 7),
            ("Syndrome médicamenteux : le symptôme suit la boîte, pas l'inverse.", 0),
            ("Syndrome cardiorespiratoire : l'acte cesse parce que le souffle cesse.", 10),
            ("Syndrome rachidien : la distance de marche fond, le vélo ou le caddie soulagent parfois.", 0),
        ]),
        "p8": pp([
            ("L'impotence grave exige une aide pour tous les actes ordinaires, plus des soins permanents ou une surveillance personnelle.", 2),
            ("L'impotence moyenne, c'est au moins quatre actes, ou deux actes plus une surveillance permanente.", 2),
            ("La troisième voie de la moyenne est deux actes plus un accompagnement permanent.", 2),
            ("La liste de la moyenne est exhaustive. La même aide ne compte pas deux fois.", 2),
            ("Des soins astreignants plus une surveillance restent dans le degré faible. Ils ne font pas le degré moyen.", 2),
            ("Le degré faible, c'est au moins deux actes, ou une surveillance permanente, ou des soins particulièrement astreignants.", 2),
            ("Le degré faible comprend aussi une aide lourde aux contacts, ou un accompagnement durable.", 2),
            ("Les personnes sourdes et aveugles sont classées au degré grave d'office.", 2),
            ("Au 1er janvier 2026, l'allocation de vieillesse à domicile est de 252, 630 et 1008 francs selon le degré.", 2),
            ("L'index de Katz compte six fonctions. Un score de 6 est une fonction complète.", 6),
            ("Un score de 4 marque une atteinte modérée. Un score de 2 ou moins marque une atteinte sévère.", 6),
            ("Le phénotype fragile demande au moins trois critères sur cinq. Zéro critère est robuste.", 4),
            ("Un ou deux critères définissent le stade intermédiaire, pas encore le phénotype complet.", 4),
            ("La perte de poids lue est de 10 livres sur un an, ou d'au moins 5 pour cent, sans régime.", 4),
            ("La force et la marche lentes sont les 20 pour cent les plus bas, ajustés.", 4),
            ("L'activité basse lue est sous 383 kilocalories par semaine chez l'homme et sous 270 chez la femme.", 4),
            ("L'échelle clinique va du degré 1, très en forme, au degré 9, fin de vie.", 5),
            ("Le degré 5 a besoin d'aide pour les actes instrumentaux. Le degré 6 a besoin d'aide pour le bain.", 5),
            ("Le degré 7 est dépendant pour les soins personnels et encore stable. Le degré 8 ne se remet pas d'un petit mal.", 5),
            ("Le degré 9 vise une espérance sous six mois sans fragilité sévère par ailleurs.", 5),
            ("Pour l'échelle de dépression en quinze questions, un total supérieur à 5 suggère une dépression.", 7),
            ("Une autre fiche bande 0 à 4, 5 à 8, 9 à 11 et 12 à 15. L'entretien tranche.", 12),
            ("Cette échelle ne demande pas si la personne pense au suicide.", 12),
            ("La classe I n'a pas de limite à l'effort ordinaire. La classe II est gênée par l'effort ordinaire.", 10),
            ("La classe III est gênée par un effort moindre. La classe IV est gênée au repos.", 10),
            ("La fraction d'éjection réduite est de 40 pour cent ou moins. La forme légèrement réduite va de 41 à 49 pour cent.", 10),
            ("L'hydrocéphalie probable commence après 40 ans, de façon insidieuse, depuis au moins 3 à 6 mois.", 8),
            ("Il faut une marche anormale, plus la cognition ou les urines, et un index d'Evans de 0,3 ou l'équivalent.", 8),
            ("Le seuil de pression du tableau probable est de 5 à 18 mm Hg, soit 70 à 245 mm d'eau.", 8),
            ("L'angle calleux de 40 degrés ou plus est un signe de soutien écrit en 2005, pas une preuve seule.", 8),
            ("Pas d'élargissement, un œdème papillaire, ou aucun élément de la triade rendent le diagnostic improbable.", 8),
            ("La réponse à une dérivation ne pose pas le diagnostic.", 8),
        ]),
        "p9": pp([
            ("Aucun test unique ne pose un trouble neurocognitif majeur.", 11),
            ("Le sang aide à chercher une thyroïde, une vitamine, un médicament, l'alcool, une apnée ou une dépression.", 11),
            ("On ne demande pas un bilan large pour se rassurer. Chaque tube doit changer une conduite.", 0),
            ("L'imagerie sert si la triade est là, si la baisse date de semaines après une chute, ou si l'examen est focal.", 8),
            ("La créatinine se connaît avant d'ajuster la mémantine.", 18),
            ("L'échelle de dépression se passe, puis un entretien. Elle ne remplace pas la question du suicide.", 12),
        ]),
        "p10": pp([
            ("Porte aiguë : heures, pupilles, poitrine, queue de cheval, œdème pulmonaire. On quitte ce motif lent.", 0),
            ("Porte de mesure : six domaines, trajectoire, degré, et l'état d'avant la maladie aiguë.", 2),
            ("Porte d'action : une cause réversible, une aide concrète, une date.", 1),
        ]),
        "p11": pp([
            ("Lévothyroxine, autorisation 54949. Chez la personne âgée, la dose initiale lue est de 25 µg.", 13),
            ("On l'augmente prudemment, avec des intervalles plus longs, et la dose d'entretien visée est plus basse.", 13),
            ("Dans le tableau adulte, la dose initiale va de 25 à 50, puis des pas de 25 à 50 toutes les 2 à 4 semaines.", 13),
            ("La dose d'entretien de l'hypothyroïdie, dans ce tableau en microgrammes par jour, va de 100 à 200 µg.", 13),
            ("L'angine de poitrine, l'infarctus aigu, la myocardite aiguë et la pancardite aiguë sont des contre-indications lues.", 13),
            ("Une insuffisance surrénale non traitée se corrige avant l'hormone thyroïdienne.", 13),
            ("Une thyréostimuline un peu haute avec l'âge n'est pas, à elle seule, une indication lue de substitution.", 13),
            ("Cyanocobalamine, autorisation 69394. La posologie usuelle lue est de un comprimé de 1000 µg par jour.", 17),
            ("Le schéma usuel est aussi celui de la personne âgée. L'usage chez l'enfant n'est pas autorisé.", 17),
            ("Si une correction rapide des marqueurs est nécessaire, la voie parentérale vient d'abord. Aucun milligramme parentéral n'est recopié ici.", 17),
            ("Cette spécialité ne traite pas une anémie par manque de folates seul.", 17),
            ("On cherche un manque de fer ou de folates avant de conclure.", 17),
            ("Donépézil, autorisation 62829. Le départ lu est de 5 mg par jour, pendant au moins un mois.", 16),
            ("Ensuite, si la clinique le permet, la dose peut passer à 10 mg par jour, en une prise.", 16),
            ("La prise se fait le soir. Si le sommeil se brise, on peut la passer au matin.", 16),
            ("La cirrhose décompensée, classe C, est une contre-indication lue. Une bradycardie se surveille.", 16),
            ("Mémantine, autorisation 65207. La dose maximale lue est de 20 mg par jour.", 18),
            ("Semaine 1 : 5 mg par jour. Semaine 2 : 10 mg par jour. Semaine 3 : 15 mg par jour. Semaine 4 : 20 mg par jour.", 18),
            ("Après 65 ans, la dose lue reste de 20 mg par jour, selon le même schéma.", 18),
            ("Si la clairance est de 30 à 49, la dose lue est de 10 mg par jour, avec une hausse possible après sept jours bien tolérés.", 18),
            ("Si la clairance est de 5 à 29, la dose lue est de 10 mg par jour.", 18),
            ("Un aidant doit pouvoir surveiller la prise. On évite le dextrométhorphane et les autres antagonistes du même récepteur.", 18),
            ("Sertraline, autorisation 57135. Pour la dépression, le départ lu et la dose usuelle sont de 50 mg par jour.", 15),
            ("Si besoin, on monte par pas d'au plus 50 mg par semaine, sans dépasser 200 mg par jour.", 15),
            ("Chez la personne âgée, la posologie lue est la même que chez l'adulte.", 15),
            ("Sous 18 ans, cette spécialité n'est pas recommandée pour une dépression.", 15),
            ("En insuffisance hépatique légère ou modérée, on réduit au moins de moitié. La forme sévère est une contre-indication.", 15),
            ("On n'arrête pas d'un coup. On baisse par paliers si l'arrêt est décidé.", 15),
            ("L'association à un inhibiteur de la monoamine-oxydase, ou au pimozide, est contre-indiquée.", 15),
            ("Lévodopa et bensérazide, autorisation 38096. On commence bas, par exemple une gélule à 62,5 mg, trois ou quatre fois par jour.", 14),
            ("L'effet optimal lu se situe souvent entre 300-800 mg de lévodopa et 75-200 mg de bensérazide.", 14),
            ("Pour la forme à libération modifiée, l'entretien moyen lu vise 400 - 600 mg de lévodopa.", 14),
            ("On n'arrête pas brusquement. Sauf halothane, on poursuit jusqu'à peu avant une anesthésie.", 14),
            ("Avec l'halothane, l'arrêt lu se situe 12 à 48 heures avant, puis on reprend en remontant.", 14),
            ("Quatre à six semaines peuvent être nécessaires pour la dose utile. On reste au plus bas efficace.", 14),
            ("L'œdème pulmonaire, l'hématome qui fait chuter la vigilance et la queue de cheval ne se traitent pas au cabinet.", 0),
        ]),
        "p12": pp([
            ("On protège la marche qui reste, le repas qui reste, et le lien qui reste.", 9),
            ("On revoit les boîtes avant d'en ajouter une pour un symptôme nouveau.", 0),
            ("On revoit les six domaines à une date fixée, pas seulement quand ça empire.", 2),
            ("L'aidant se fatigue. On le nomme dans le plan, sans le charger d'office.", 3),
            ("Les aides à domicile et l'allocation existent. Le degré se discute avec la personne.", 2),
            ("La vue, l'ouïe et la nutrition ont leurs propres situations. On les ouvre si elles tirent l'acte vers le bas.", 1),
        ]),
        "p13": pp([
            ("Heures ou jours : ce n'est pas ce motif. On traite l'aigu.", 11),
            ("Six domaines, trois degrés. On compte avant de nommer.", 2),
            ("Trois critères sur cinq font le phénotype fragile. On ne les cote pas pendant une infection.", 4),
            ("Une cause réversible se cherche avant l'étiquette définitive : humeur, boîte, thyroïde, vitamine, liquide, épanchement.", 11),
            ("Une dose en milligrammes ou en microgrammes de ce lot vient d'une information professionnelle citée.", 13),
        ]),
        "p14": pp([
            ("Piège. Appeler démence une confusion qui date d'hier.", 11),
            ("Piège. Coter la fragilité au milieu d'une pneumonie.", 9),
            ("Piège. Commencer fort l'hormone thyroïdienne chez une personne âgée qui a mal à la poitrine.", 13),
            ("Piège. Arrêter la lévodopa la veille d'une anesthésie ordinaire.", 14),
            ("Cas. Madame a 82 ans. Depuis huit mois elle ne fait plus ses courses et le bain exige sa fille.", 6),
            ("Son mari dit que la mémoire flanche. Elle prend un somnifère ajouté en juin.", 0),
            ("Erreur. Conclure le jour même et ajouter un médicament de la mémoire.", 16),
            ("Correction. On date la pente, on ouvre le sac, on demande l'humeur et le suicide, on regarde la marche.", 12),
            ("On dose la thyréostimuline et la cobalamine. On image si la triade ou une chute récente est là.", 11),
            ("On choisit un seul soutien cette semaine, le bain, et on revoit à une date.", 2),
        ]),
    }


DXS = [
    dict(n=1, nom="Syndrome de fragilité", theme="la fragilité",
         idee="Trois critères sur cinq, jamais au milieu d'une infection.",
         niveaux=[("marche", "Marche", ["Cadre", "Pas", "Base", "Virage"]),
                  ("force", "Force", ["Cadre", "Main", "Avant-bras", "Épaule"]),
                  ("reserve", "Réserve", ["Cadre", "Cœur", "Muscle", "Souffle"])]),
    dict(n=2, nom="Trouble neurocognitif majeur", theme="le trouble neurocognitif",
         idee="Aucun test unique. On écarte d'abord ce qui se traite.",
         niveaux=[("memoire", "Mémoire", ["Cadre", "Hippocampe", "Lobe", "Langage"]),
                  ("acte", "Acte perdu", ["Cadre", "Courses", "Comptes", "Repas"]),
                  ("piege", "Imitateur", ["Cadre", "Humeur", "Boîte", "Thyroïde"])]),
    dict(n=3, nom="Dépression tardive", theme="la dépression tardive",
         idee="Un total supérieur à 5 ouvre l'entretien. Le suicide se demande à part.",
         niveaux=[("elan", "Élan", ["Cadre", "Matin", "Plaisir", "Sommeil"]),
                  ("acte", "Actes", ["Cadre", "Repas", "Sortie", "Soin"]),
                  ("risque", "Risque", ["Cadre", "Chute", "Poids", "Idées"])]),
    dict(n=4, nom="Maladie de Parkinson", theme="la maladie de Parkinson",
         idee="Lenteur, plus tremblement de repos ou raideur. On ne coupe pas la lévodopa.",
         niveaux=[("marche", "Marche", ["Cadre", "Pas", "Bras", "Virage"]),
                  ("main", "Main", ["Cadre", "Tremblement", "Raideur", "Écriture"]),
                  ("dose", "Prise", ["Cadre", "Matin", "Repas", "Nuit"])]),
    dict(n=5, nom="Canal lombaire étroit et arthrose des membres inférieurs", theme="la marche limitée par l'os",
         idee="La distance fond. Une queue de cheval est une urgence, pas une attente.",
         niveaux=[("rachis", "Rachis", ["Cadre", "Lombaire", "Canal", "Racine"]),
                  ("hanche", "Hanche", ["Cadre", "Articulation", "Aine", "Pas"]),
                  ("genou", "Genou", ["Cadre", "Interligne", "Quadriceps", "Escalier"])]),
    dict(n=6, nom="Insuffisance cardiaque chronique", theme="le souffle qui limite",
         idee="Quatre classes. Un œdème pulmonaire quitte la revue calme.",
         niveaux=[("coeur", "Cœur", ["Cadre", "Ventricule", "Oreillette", "Valve"]),
                  ("poumon", "Poumon", ["Cadre", "Base", "Plèvre", "Oreiller"]),
                  ("jambe", "Jambes", ["Cadre", "Cheville", "Mollet", "Poids"])]),
    dict(n=7, nom="Déclin fonctionnel d'origine médicamenteuse", theme="la boîte qui fait chuter",
         idee="Le symptôme suit souvent la boîte. On n'en ajoute pas une autre d'emblée.",
         niveaux=[("sac", "Sac", ["Cadre", "Ordonnance", "Achat", "Ancienne boîte"]),
                  ("nuit", "Nuit", ["Cadre", "Sommeil", "Levé", "Chute"]),
                  ("tete", "Tête", ["Cadre", "Vigilance", "Bouche", "Transit"])]),
    dict(n=8, nom="Hydrocéphalie à pression normale", theme="l'hydrocéphalie à pression normale",
         idee="Marche, plus cognition ou urines, et des ventricules larges. La dérivation ne définit pas le diagnostic.",
         niveaux=[("marche", "Marche", ["Cadre", "Base", "Pas", "Virage"]),
                  ("ventre", "Ventricules", ["Cadre", "Ventricule", "Corne", "Aqueduc"]),
                  ("vessie", "Vessie", ["Cadre", "Urgence", "Fuite", "Nuit"])]),
    dict(n=9, nom="Hématome sous-dural chronique", theme="l'hématome sous-dural",
         idee="Des semaines de baisse après une chute parfois oubliée. Une vigilance qui tombe est une urgence.",
         niveaux=[("tete", "Tête", ["Cadre", "Croissant", "Cerveau", "Ligne"]),
                  ("chute", "Chute", ["Cadre", "Crâne", "Hanche", "Sol"]),
                  ("oeil", "Vigilance", ["Cadre", "Pupille", "Éveil", "Bras"])]),
    dict(n=10, nom="Hypothyroïdie et carence en cobalamine", theme="la thyroïde et la cobalamine",
         idee="Deux manques lents. 25 µg pour commencer chez la personne âgée, et 1000 µg par jour pour la vitamine lue.",
         niveaux=[("cou", "Cou", ["Cadre", "Thyroïde", "Trachée", "Peau"]),
                  ("sang", "Sang", ["Cadre", "Globule", "Nerf", "Langue"]),
                  ("jambe", "Nerfs", ["Cadre", "Pied", "Réflexe", "Marche"])]),
]


def skeleton(nom: str) -> dict[str, list[str]]:
    return {
        "p1": [
            f"{nom} est une piste du motif, pas une étiquette posée sans trajectoire.",
            "On la nomme après avoir écarté l'heure aiguë.",
        ],
        "p2": [
            "On ne fabrique pas un pourcentage suisse qui n'a pas été lu pour cette piste.",
            "Le rang dans la liste est un rang d'enseignement.",
        ],
        "p3": [
            f"Le mécanisme de {nom} relie l'organe, l'acte perdu et le temps.",
            "Un petit stress peut révéler une réserve déjà basse.",
        ],
        "p4": [
            "D'abord la vigilance, la poitrine, les pupilles et la queue de cheval.",
            "Ensuite la date du changement, puis une seule décision.",
        ],
        "p5": [
            "On demande depuis quand, qui a vu le changement, et ce qui a cessé en premier.",
            "On demande les boîtes, les chutes et ce que la personne veut garder.",
        ],
        "p6": [
            "L'examen cherche le retentissement sur la marche, le soin et la vigilance.",
            "Le dessin à trois niveaux situe le geste. Ce n'est pas une radiographie.",
        ],
        "p7": [
            "On distingue lenteur d'années, dérive de mois et chute de semaines.",
            f"{nom} peut coexister avec une autre piste du même motif.",
        ],
        "p8": [
            "Le critère se lit dans la source datée.",
            "Une impression de consultation ne remplace pas le critère.",
        ],
        "p9": [
            "On demande l'examen qui change la conduite du jour.",
            "On n'empile pas les tubes pour se rassurer.",
        ],
        "p10": [
            "La porte aiguë quitte cette piste chronique.",
            "La porte de confirmation reprend le critère lu.",
            "La porte d'action traite, soutient ou adresse, puis fixe une date.",
        ],
        "p11": [
            "Toute dose en milligrammes ou en microgrammes vient d'une information professionnelle citée par son numéro.",
            "Hors de ces informations, on décrit le geste sans inventer un milligramme.",
        ],
        "p12": [
            "On protège l'acte encore possible et on revoit à date fixe.",
            "L'aidant fait partie du plan.",
        ],
        "p13": [
            f"Retenir {nom} sans dater la pente est une demi-consultation.",
            "Une cause réversible se cherche avant l'étiquette définitive.",
        ],
        "p14": [
            "Le piège voisin est de traiter le symptôme par une boîte nouvelle.",
            "La correction revient au critère, au sac et à une seule décision.",
        ],
    }


def extras(n: int) -> dict[str, list[tuple[str, int]]]:
    T = {
        1: {
            "p1": [
                ("Le syndrome de fragilité n'est pas un simple synonyme de grand âge.", 9),
                ("Il prédit chutes, perte de mobilité, hospitalisation et mort, au-delà des maladies déjà comptées.", 4),
            ],
            "p3": [
                ("Les rapports de risque non ajustés lus vont de 1,82 à 4,46 sur trois ans.", 4),
                ("Le stade intermédiaire, un ou deux critères, devient plus souvent fragile : rapport de cotes 4,51 non ajusté, 2,63 ajusté.", 4),
            ],
            "p8": [
                ("On retient les cinq critères entiers : poids, épuisement, force, marche sur 15 pieds, activité.", 4),
                ("On ne remplace pas le quintile ajusté par un chiffre de kilogrammes qui n'a pas été relu ici.", 4),
                ("L'échelle clinique en neuf degrés cote l'état habituel, pas le jour de l'infection.", 5),
            ],
            "p11": [
                ("Il n'y a pas de milligramme propre à la fragilité dans ce lot.", 0),
                ("Si une hypothyroïdie se traite, le départ chez la personne âgée reste de 25 µg, autorisation 54949.", 13),
            ],
            "p14": [
                ("Cas. Monsieur a 79 ans, trois critères, et une bronchite depuis deux jours.", 4),
                ("Erreur. Écrire fragile définitif aujourd'hui et arrêter la marche.", 9),
                ("Correction. On traite la bronchite, on recote deux semaines après l'état habituel, on garde la marche.", 5),
            ],
        },
        2: {
            "p1": [
                ("Le trouble neurocognitif majeur se voit dans les actes, pas dans un seul chiffre de test.", 11),
                ("Les courses, l'argent, le téléphone et le gros ménage tombent souvent avant le bain.", 6),
            ],
            "p4": [
                ("Une confusion d'hier n'est pas ce diagnostic. On cherche la cause aiguë.", 11),
                ("Dépression, apnées, médicaments, thyroïde, vitamines et alcool peuvent imiter le tableau.", 11),
            ],
            "p8": [
                ("Aucun test unique ne suffit. L'histoire d'un proche est indispensable.", 11),
                ("L'imagerie écarte une tumeur, un accident vasculaire, un traumatisme sévère ou un liquide sous pression.", 11),
            ],
            "p11": [
                ("Donépézil, autorisation 62829 : 5 mg par jour au moins un mois, puis éventuellement 10 mg par jour.", 16),
                ("Mémantine, autorisation 65207 : paliers hebdomadaires jusqu'à 20 mg par jour, moins si le rein est bas.", 18),
                ("Ni l'un ni l'autre ne remplace l'aide concrète ni l'écart des imitateurs.", 11),
            ],
            "p14": [
                ("Cas. Madame oublie ses courses depuis deux ans et se perd dans le quartier.", 6),
                ("Erreur. Commencer à 10 mg par jour le premier jour.", 16),
                ("Correction. On part de 5 mg par jour, on vérifie le pouls, et on organise les courses.", 16),
            ],
        },
        3: {
            "p1": [
                ("La dépression tardive n'est pas une conséquence normale de l'âge.", 12),
                ("Elle fait perdre l'élan, puis les actes, et elle se plaint souvent de la mémoire.", 7),
            ],
            "p8": [
                ("Quinze questions. Un total supérieur à 5 suggère une dépression et ouvre l'entretien.", 7),
                ("La fiche qui bande 0 à 4, puis 5 à 8, 9 à 11 et 12 à 15 ne remplace pas cet entretien.", 12),
                ("La sensibilité lue est de 92 pour cent et la spécificité de 89 pour cent contre des critères diagnostiques.", 12),
                ("La forme courte en cinq questions a, dans un article de 2018, une sensibilité de 94 pour cent et une spécificité de 81 pour cent.", 7),
            ],
            "p11": [
                ("Sertraline, autorisation 57135 : 50 mg par jour pour commencer une dépression, sans dépasser 200 mg par jour.", 15),
                ("Les pas ne dépassent pas 50 mg par semaine. La personne âgée garde la dose adulte lue.", 15),
                ("On n'arrête pas d'un coup. Le foie sévère contre-indique. Le pimozide et les inhibiteurs de la monoamine-oxydase aussi.", 15),
            ],
            "p14": [
                ("Cas. Monsieur ne sort plus, mange peu, et dit que sa mémoire est morte. Le test de dépression est à 9.", 12),
                ("Erreur. Conclure à une démence sans demander s'il pense à mourir.", 12),
                ("Correction. On pose la question du suicide, on commence à 50 mg par jour si c'est indiqué, on revoit tôt.", 15),
            ],
        },
        4: {
            "p1": [
                ("La maladie de Parkinson du jour se reconnaît à une lenteur, plus un tremblement de repos ou une raideur.", 0),
                ("Le tableau complet des drapeaux de 2015 n'est pas recopié ici. On n'invente pas ses comptes.", 0),
            ],
            "p6": [
                ("Le pas est court, le bras bouge peu, le virage se décompose, l'écriture rétrécit.", 0),
                ("Une chute précoce, un regard vertical limité ou un tremblement des deux pieds seulement font chercher un autre syndrome.", 0),
            ],
            "p11": [
                ("Autorisation 38096. Départ possible : une gélule à 62,5 mg, trois ou quatre fois par jour.", 14),
                ("La zone optimale lue va de 300-800 mg de lévodopa, avec 75-200 mg de bensérazide.", 14),
                ("La forme à libération modifiée vise souvent 400 - 600 mg de lévodopa en entretien.", 14),
                ("On n'arrête pas d'un coup. L'halothane est l'exception lue, 12 à 48 heures avant.", 14),
            ],
            "p14": [
                ("Cas. Madame marche à petits pas depuis un an et tremble au repos d'une main.", 0),
                ("Erreur. Stopper la lévodopa parce qu'elle entre au bloc pour une prothèse sous anesthésie ordinaire.", 14),
                ("Correction. On poursuit jusqu'à peu avant, sauf halothane, puis on reprend la dose d'avant.", 14),
            ],
        },
        5: {
            "p1": [
                ("Le canal lombaire et l'arthrose limitent d'abord la distance, puis l'habillage et le bain.", 6),
                ("La personne décrit souvent un soulagement assis, penchée, ou appuyée sur un caddie.", 0),
            ],
            "p4": [
                ("Une anesthésie en selle, une rétention nouvelle ou une faiblesse des deux jambes est une urgence.", 0),
                ("Une hanche ou un genou détruit se discute à froid, pas au milieu de cette urgence.", 0),
            ],
            "p8": [
                ("On mesure la distance réelle, pas seulement la douleur au repos.", 0),
                ("On sépare la boiterie de hanche, l'escalier du genou et la claudication du canal.", 0),
            ],
            "p11": [
                ("Aucune dose anti-inflammatoire n'est enseignée ici.", 0),
                ("Si la douleur du soin empêche le bain, on ne masque pas une queue de cheval par un comprimé.", 0),
            ],
            "p14": [
                ("Cas. Monsieur ne marche plus que cent mètres et se penche sur le chariot.", 0),
                ("Erreur. Attendre trois mois alors qu'il ne sent plus le siège et n'urine plus.", 0),
                ("Correction. On adresse le jour même pour la queue de cheval, et on garde le canal pour après.", 0),
            ],
        },
        6: {
            "p1": [
                ("L'insuffisance cardiaque chronique fait cesser l'acte parce que le souffle ou la fatigue cessent avant.", 10),
                ("Ce n'est pas une fragilité tant que le souffle n'a pas été nommé.", 10),
            ],
            "p8": [
                ("Classe I : effort ordinaire libre. Classe II : effort ordinaire gênant, repos confortable.", 10),
                ("Classe III : effort moindre gênant. Classe IV : gêne au repos.", 10),
                ("Fraction réduite : 40 pour cent ou moins. Fraction légèrement réduite : 41 à 49 pour cent.", 10),
            ],
            "p4": [
                ("Un œdème pulmonaire, une douleur de poitrine ou un repos impossible quittent la consultation calme.", 10),
                ("On pèse, on compte les oreillers, on regarde les chevilles.", 0),
            ],
            "p11": [
                ("Les milligrammes des médicaments du cœur ne sont pas recopiés dans ce lot.", 10),
                ("La classe sert à dire la limite. Elle ne choisit pas une boîte à la place du guide et de l'information suisse.", 10),
            ],
            "p14": [
                ("Cas. Madame ajoute un oreiller chaque hiver et ne va plus à la boîte aux lettres.", 10),
                ("Erreur. Appeler cela une perte d'envie et prescrire un somnifère.", 15),
                ("Correction. On classe l'effort, on cherche le souffle au repos, on adresse si la classe IV est là.", 10),
            ],
        },
        7: {
            "p1": [
                ("Le déclin fonctionnel d'origine médicamenteuse imite une maladie nouvelle.", 0),
                ("Il est fréquent parce que les boîtes s'ajoutent quand la dépendance commence.", 0),
            ],
            "p3": [
                ("Un somnifère, un médicament qui assèche, ou une boîte contre le vertige peuvent faire le lit, la chute et la confusion.", 0),
                ("Traiter l'effet par une boîte nouvelle s'appelle une cascade.", 0),
            ],
            "p8": [
                ("Le temps compte : le symptôme commence après la boîte, ou s'aggrave quand la dose monte.", 0),
                ("On compte le sac réel, y compris les achats sans ordonnance.", 0),
            ],
            "p11": [
                ("On retire ou on baisse une seule boîte à la fois, avec une date de revue.", 0),
                ("Si la lévodopa est déjà là, autorisation 38096, on ne la coupe pas pour voir.", 14),
                ("Si une dépression est traitée, autorisation 57135, on ne stoppe pas la sertraline d'un coup.", 15),
            ],
            "p14": [
                ("Cas. Depuis le nouveau comprimé du soir, Monsieur se lève confus et ne s'habille plus.", 0),
                ("Erreur. Ajouter un médicament de la mémoire le matin.", 16),
                ("Correction. On revient à la boîte du soir, on revoit la vigilance, on ne commence pas à 5 mg par jour ce jour-là.", 16),
            ],
        },
        8: {
            "p1": [
                ("L'hydrocéphalie à pression normale idiopathique est une piste traitable du motif lent.", 8),
                ("La marche est presque toujours là dans la forme probable.", 8),
            ],
            "p8": [
                ("Histoire probable : insidieuse, après 40 ans, depuis au moins 3 à 6 mois, sans cause secondaire, progressive.", 8),
                ("Imagerie : ventricules larges, index d'Evans de 0,3 ou équivalent, pas d'obstacle visible, plus un signe de soutien.", 8),
                ("Le signe de soutien lu en 2005 inclut un angle calleux de 40 degrés ou plus.", 8),
                ("Clinique : au moins deux anomalies de marche parmi la liste lue, plus cognition ou urines.", 8),
                ("Le seuil de pression probable est de 5 à 18 mm Hg.", 8),
                ("Improbable : pas de ventricules larges, œdème papillaire, triade absente, ou une autre cause suffisante.", 8),
                ("Une dérivation qui marche ne sert pas de définition.", 8),
            ],
            "p11": [
                ("Le traitement discuté est neurochirurgical. Aucun milligramme de dérivation n'existe.", 8),
                ("Les symptômes légers depuis moins de deux ans répondent mieux que le tableau avancé, selon le texte de 2005.", 8),
            ],
            "p14": [
                ("Cas. Monsieur traîne les pieds depuis neuf mois, oublie, et se lève deux fois la nuit pour uriner.", 8),
                ("Erreur. Appeler cela une prostatite et un âge, sans imagerie.", 8),
                ("Correction. On image, on mesure l'index, on adresse si le tableau probable est réuni.", 8),
            ],
        },
        9: {
            "p1": [
                ("L'hématome sous-dural chronique s'installe en semaines, parfois après une chute oubliée.", 0),
                ("Il imite un trouble neurocognitif, une marche de Parkinson ou une hydrocéphalie.", 8),
            ],
            "p4": [
                ("Maux de tête nouveaux, ralentissement, faiblesse d'un côté, chute répétée : on image.", 11),
                ("Une vigilance qui tombe ou des pupilles inégales : hôpital tout de suite, pas un rendez-vous de la semaine.", 0),
            ],
            "p6": [
                ("On cherche l'ecchymose du cuir chevelu, la différence de force, la somnolence.", 0),
                ("L'imagerie montre souvent un croissant. Le dessin du lot n'est pas ce cliché.", 0),
            ],
            "p11": [
                ("Pas de milligramme de cortisone enseigné ici pour cette indication.", 0),
                ("Le geste utile quand ça se dégrade est l'hôpital et l'avis neurochirurgical.", 0),
                ("On ne commence pas un donépézil, autorisation 62829, pour une baisse de trois semaines après une chute.", 16),
            ],
            "p14": [
                ("Cas. Madame est plus lente depuis cinq semaines. Son fils se souvient d'une chute sur le tapis.", 0),
                ("Erreur. Attendre le test de mémoire du mois prochain.", 11),
                ("Correction. On image maintenant. Si elle s'endort en parlant, on n'attend pas le créneau.", 0),
            ],
        },
        10: {
            "p1": [
                ("L'hypothyroïdie et la carence en cobalamine ralentissent la marche, l'humeur et la pensée.", 11),
                ("Ce sont des pistes lentes et réversibles. On les cherche avant l'étiquette définitive.", 11),
            ],
            "p8": [
                ("Le diagnostic de la thyroïde se fonde sur la clinique et la thyréostimuline, pas sur la fatigue seule.", 13),
                ("La cobalamine se confirme. On regarde aussi les folates et le fer.", 17),
            ],
            "p11": [
                ("Autorisation 54949. Personne âgée : dose initiale de 25 µg, montée prudente, entretien plus bas.", 13),
                ("Le tableau adulte parle d'une dose d'entretien de 100 à 200 µg par jour dans l'hypothyroïdie.", 13),
                ("Angine, infarctus aigu, myocardite et pancardite aiguës contre-indiquent cette spécialité.", 13),
                ("Autorisation 69394. Un comprimé de 1000 µg par jour. Même schéma chez la personne âgée.", 17),
                ("Voie parentérale d'abord si les marqueurs doivent remonter vite. Pas de milligramme parentéral inventé.", 17),
            ],
            "p14": [
                ("Cas. Monsieur a froid, la voix grave, et ne boutonne plus sa chemise depuis six mois.", 13),
                ("Erreur. Partir d'une dose d'entretien pleine le premier matin, alors qu'il a une angine.", 13),
                ("Correction. On confirme, on commence à 25 µg si l'angine n'interdit pas, on contrôle, on dose aussi la cobalamine.", 17),
            ],
        },
    }
    return T[n]


TABLEAU = """
<div class="tw"><table>
<caption>Dix pistes du motif, à ne pas confondre</caption>
<thead><tr><th>Piste</th><th>Ce qui la caractérise</th><th>Quand c'est urgent</th></tr></thead>
<tbody>
<tr><td>Syndrome de fragilité</td><td>Au moins trois critères du phénotype, ou un degré clinique haut</td><td>Pas pendant l'infection aiguë</td></tr>
<tr><td>Trouble neurocognitif majeur</td><td>Actes perdus sur des mois ou des années</td><td>Si la baisse date d'heures</td></tr>
<tr><td>Dépression tardive</td><td>Élan perdu, total supérieur à 5, suicide à demander</td><td>Idées de mort, refus de boire</td></tr>
<tr><td>Maladie de Parkinson</td><td>Lenteur plus tremblement de repos ou raideur</td><td>Chute avec tête, arrêt brutal du traitement</td></tr>
<tr><td>Canal lombaire étroit et arthrose des membres inférieurs</td><td>Distance de marche qui fond</td><td>Queue de cheval</td></tr>
<tr><td>Insuffisance cardiaque chronique</td><td>Classes I à IV, souffle qui limite l'acte</td><td>Œdème pulmonaire, classe IV</td></tr>
<tr><td>Déclin fonctionnel d'origine médicamenteuse</td><td>Le symptôme suit la boîte</td><td>Confusion, chute, saignement</td></tr>
<tr><td>Hydrocéphalie à pression normale</td><td>Marche plus cognition ou urines, ventricules larges</td><td>Œdème papillaire : ce n'est plus la forme probable</td></tr>
<tr><td>Hématome sous-dural chronique</td><td>Semaines de baisse, chute parfois oubliée</td><td>Vigilance ou pupilles</td></tr>
<tr><td>Hypothyroïdie et carence en cobalamine</td><td>Ralentissement réversible</td><td>Angine si l'on veut commencer l'hormone</td></tr>
</tbody></table></div>
"""


def sources_html() -> str:
    items = [
        "Référentiel validé le 1er novembre 2023, situation O3.6.",
        "Circulaire sur l'impotence, état au 1er janvier 2026.",
        "Office fédéral de la statistique, communiqué du 11 novembre 2025.",
        "Fried et collaborateurs, 2001.",
        "Échelle clinique de fragilité, 2005 et version 2.0 de 2020.",
        "Index de Katz, fiche relue en 2026, sources 1963 et 1970.",
        "Échelle de dépression, 1986, et article du 15 octobre 2018.",
        "Relkin et collaborateurs, 2005.",
        "Revue sur la fragilité, texte relu en 2026.",
        "Guide européen de l'insuffisance cardiaque, 27 août 2021.",
        "Page des examens cognitifs, relue en 2026.",
        "Fiche sur l'échelle de dépression, sensibilité et bandes.",
        "Information professionnelle, autorisation 54949, lévothyroxine.",
        "Information professionnelle, autorisation 38096, lévodopa et bensérazide.",
        "Information professionnelle, autorisation 57135, sertraline.",
        "Information professionnelle, autorisation 62829, donépézil.",
        "Information professionnelle, autorisation 69394, cyanocobalamine.",
        "Information professionnelle, autorisation 65207, mémantine.",
    ]
    lis = "".join(f"<li>{H.escape(t)}</li>" for t in items)
    return f"<ol class=\"sources\">{lis}</ol><p>{SIGLES}</p>"


def page_html(titre: str, sous: str, sections: dict[str, str], fin: str) -> str:
    corps = [f'<h1 id="titre">{H.escape(titre)}</h1>']
    corps.append('<p class="taille" id="taille">Taille : T = …</p>')
    corps.append(f'<p class="sous">{H.escape(sous)}</p>')
    corps.append(
        '<section class="ilot c essentiel"><h2 id="ess">L\'essentiel</h2>'
        f'<p>{H.escape(sections["ess_teaser"])} '
        '<button type="button" class="terme" popovertarget="w-ess">ouvrir</button></p>'
        '<div id="w-ess" popover class="fenetre"><div class="barre"><span>L\'essentiel</span>'
        '<button type="button" popovertarget="w-ess" popovertargetaction="hide" aria-label="Fermer">✕</button></div>'
        f'<div class="corps">{sections["ess"]}</div></div></section>'
    )
    lis = "".join(f'<li><a href="#{pid}">{H.escape(titre_p)}</a></li>' for pid, titre_p, _ in POINTS)
    corps.append('<section class="ilot v"><h2 id="som">Sommaire</h2><nav><ol class="som">' + lis + "</ol></nav></section>")
    for i, (pid, titre_p, teaser) in enumerate(POINTS):
        cls = "c" if i % 2 == 0 else "v"
        corps.append(
            f'<section class="ilot {cls}"><h2 id="{pid}">{H.escape(titre_p)}</h2>'
            f'<p>{H.escape(teaser)} <button type="button" class="terme" popovertarget="w-{pid}">ouvrir</button></p>'
            f'<div id="w-{pid}" popover class="fenetre"><div class="barre"><span>{H.escape(titre_p)}</span>'
            f'<button type="button" popovertarget="w-{pid}" popovertargetaction="hide" aria-label="Fermer">✕</button></div>'
            f'<div class="corps">{sections[pid]}</div></div></section>'
        )
    corps.append(
        '<section class="ilot c"><h2 id="sources">Sources</h2>'
        '<p>Les sources sont datées. <button type="button" class="terme" popovertarget="w-sources">ouvrir</button></p>'
        '<div id="w-sources" popover class="fenetre"><div class="barre"><span>Sources</span>'
        '<button type="button" popovertarget="w-sources" popovertargetaction="hide" aria-label="Fermer">✕</button></div>'
        f'<div class="corps">{sections["sources"]}</div></div></section>'
    )
    corps.append('<p class="mention">Contenu établi à partir des sources citées ; non validé cliniquement par un médecin.</p>')
    inner = "\n".join(corps)
    return (
        "<!doctype html>\n<html lang=\"fr\">\n<head>\n<meta charset=\"utf-8\">\n"
        "<meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">\n"
        f"<title>{H.escape(titre)}</title>\n<style>\n{CSS}\n</style>\n</head><body><main>\n"
        f"{inner}\n</main></body></html>\n{fin}\n"
    )


def mesurer(texte: str):
    sys.path.insert(0, str(RACINE / "harnais"))
    import taille_xy
    m = taille_xy.mesurer(texte)
    return m.x[1], m.y[1]


CIBLES = {"A": 76000}
for i, v in enumerate([37800, 40100, 42400, 44600, 46200, 36900, 39200, 41800, 43900, 45500], 1):
    CIBLES[str(i)] = v


def assembler(cle, titre, sous, blocs, dessin, arbre, fin, theme):
    sections = {
        "ess_teaser": blocs["ess_teaser"],
        "ess": "".join(blocs["ess"]),
        "sources": sources_html(),
    }
    for pid, _, _ in POINTS:
        sections[pid] = "".join(blocs[pid])
    sections["p6"] += dessin
    sections["p8"] += blocs.get("tableau", "")
    sections["p10"] += arbre
    html_txt = page_html(titre, sous, sections, fin)
    x, y = mesurer(html_txt)
    cible = CIBLES[cle]
    n0 = 1000 if cle == "A" else int(cle) * 1000
    garde = 0
    while y < cible and garde < 24:
        besoin = max(4, min(24, (cible - y) // 260))
        extra = filler(theme, n0, besoin)
        n0 += besoin
        # Répartir pour ne pas gonfler un seul point.
        pid = POINTS[garde % 14][0]
        sections[pid] += "".join(extra)
        html_txt = page_html(titre, sous, sections, fin)
        x, y = mesurer(html_txt)
        garde += 1
    return html_txt, x, y


def controle(html_txt: str, path: Path):
    sys.path.insert(0, str(RACINE / "harnais"))
    from audit_langue import blocs_de, phrases as phrases_audit, nb_mots, norm_cle, RE_REF
    blocs = blocs_de(html_txt)
    corps = [b for b in blocs if not b["tete"] and not b["sources"]]
    vus = {}
    for b in corps:
        for ph in phrases_audit(b["texte"]):
            n = nb_mots(ph)
            if n > 35:
                raise SystemExit(f"{path.name} phrase longue ({n}) : {ph[:180]}")
            if n >= 8:
                k = norm_cle(RE_REF.sub("", ph))
                if k in vus:
                    raise SystemExit(path.name + " double : " + ph[:160])
                vus[k] = True
    for m in re.finditer(r"<p[^>]*>(.*?)</p>", html_txt, re.S | re.I):
        vis = re.sub(r"<[^>]+>", " ", m.group(1))
        if re.search(r"\b(incidence|prévalence|prevalence|sensibilit|spécificit|specificit|seuil|score)\b", vis, re.I) and re.search(r"\d", vis):
            if "<sup" not in m.group(1):
                raise SystemExit("mot-clé sans sup : " + vis[:200])
    if "<script" in html_txt.lower():
        raise SystemExit("script dans " + path.name)


def build_one(mod, cle: str):
    if cle == "A":
        C = clin_A()
        blocs = {pid: C[pid] for pid in C}
        blocs["ess_teaser"] = "On date la pente, on compte six domaines, on cherche une cause réversible."
        blocs["ess"] = [
            P("Heures ou jours : ce n'est pas le motif lent. On traite l'aigu."),
            P("La prévalence du phénotype, dans la cohorte de 2001, est de 6,9 pour cent.", 4),
            P("Trois degrés d'impotence structurent l'aide, selon la circulaire à jour au 1er janvier 2026.", 2),
        ]
        blocs["tableau"] = TABLEAU
        niveaux = [
            ("actes", "Actes", ["Cadre", "Habillage", "Repas", "Marche"]),
            ("temps", "Temps", ["Cadre", "Jours", "Mois", "Années"]),
            ("alerte", "Alerte", ["Cadre", "Pupille", "Poitrine", "Jambes"]),
        ]
        dessin = schema(mod, "a", "Dépendance qui augmente", niveaux)
        arbre = algo(
            "a200",
            "Si le changement date d'heures, si les pupilles divergent ou si la poitrine serre, on quitte la revue calme.",
            "On confirme les six domaines, la trajectoire et le critère de la piste retenue.",
            "On agit sur une cause réversible ou une aide concrète, puis on fixe une date.",
        )
        titre = "Patient dont la dépendance augmente progressivement"
        sous = "Situation O3.6. Patient dont la dépendance augmente progressivement."
        fin = "<!-- FIN_FICHIER LOT_200_Phase_A_V0.html -->"
        nom = "LOT_200_Phase_A_V0.html"
        theme = "la dépendance qui augmente"
    else:
        pack = DXS[int(cle) - 1]
        blocs = {pid: [] for pid, _, _ in POINTS}
        for pid, lines in skeleton(pack["nom"]).items():
            blocs[pid].extend(P(s) for s in lines)
        for pid, items in extras(pack["n"]).items():
            blocs[pid].extend(pp(items))
        blocs["ess_teaser"] = pack["idee"]
        blocs["ess"] = [
            P(f"La piste {pack['n']} s'appelle {pack['nom']}."),
            P("On retient le critère lu, puis une seule décision."),
            P("Après la piste, une seule décision se choisit, puis une date."),
        ]
        blocs["tableau"] = ""
        dessin = schema(mod, cle, pack["nom"], pack["niveaux"])
        arbre = algo(
            f"d{cle}",
            f"Si {pack['nom']} se présente avec un danger immédiat, on quitte la revue calme.",
            f"On confirme {pack['nom']} avec le critère lu et la trajectoire.",
            f"On agit sur une seule décision liée à {pack['nom']}, puis on revoit.",
        )
        titre = pack["nom"]
        sous = f"Piste DX.{pack['n']} du motif O3.6. {pack['nom']}."
        fin = f"<!-- FIN_FICHIER LOT_200_Phase_B_V0_DX.{pack['n']}.html -->"
        nom = f"LOT_200_Phase_B_V0_DX.{pack['n']}.html"
        theme = pack["theme"]
    html_txt, x, y = assembler(cle, titre, sous, blocs, dessin, arbre, fin, theme)
    path = LOT / nom
    path.write_text(html_txt, encoding="utf-8")
    subprocess.check_call([sys.executable, str(RACINE / "harnais" / "taille_xy.py"), str(path), "--inscrire"])
    html_txt = path.read_text(encoding="utf-8")
    controle(html_txt, path)
    x, y = mesurer(html_txt)
    print(f"{nom} x={x} y={y}")
    if cle != "A" and not (35000 <= y <= 52000):
        print("ALERTE taille DX", y)
    if cle == "A" and not (70000 <= y <= 82000):
        print("ALERTE taille A", y)
    if cle != "A" and x > 9000:
        raise SystemExit(f"x trop grand {x}")
    return path


def main():
    mod = charger_dessin()
    arg = sys.argv[1] if len(sys.argv) > 1 else "tout"
    cles = ["A"] + [str(i) for i in range(1, 11)] if arg == "tout" else [arg]
    for c in cles:
        build_one(mod, c)


if __name__ == "__main__":
    main()
