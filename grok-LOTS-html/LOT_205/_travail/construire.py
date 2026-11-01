#!/usr/bin/env python3
"""Assemble les leçons LOT_205. Phrases courtes, sources datées, sans script."""
from __future__ import annotations

import html
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
LOT = ROOT / "grok-LOTS-html" / "LOT_205"
sys.path.insert(0, str(ROOT / "harnais"))
import taille_xy  # noqa: E402

NOMS = [
    "Bilan de santé d'une personne asymptomatique",
    "Risque cardiovasculaire, lipides et glycémie",
    "Dépistage du cancer colorectal",
    "Mammographie de dépistage",
    "Dépistage du col de l'utérus",
    "Imagerie et radioprotection",
    "Nodule pulmonaire découvert par hasard",
    "Résultat biologique critique",
    "Réaction au produit de contraste",
    "Bilan avant une chirurgie à faible risque",
]
TITRES = [
    "1. Définition",
    "2. Épidémiologie",
    "3. Physiopathologie",
    "4. Démarche diagnostique",
    "5. Anamnèse et drapeaux rouges",
    "6. Examen clinique",
    "7. Approche syndromique",
    "8. Diagnostic positif",
    "9. Examens complémentaires",
    "10. Arbre décisionnel",
    "11. Prise en charge",
    "12. Prévention",
    "13. Points clés",
    "14. Pièges et cas",
]
CIBLES = {
    "A": 75000,
    1: 37800,
    2: 40200,
    3: 42500,
    4: 44800,
    5: 45200,
    6: 37100,
    7: 41400,
    8: 43600,
    9: 45300,
    10: 38900,
}
MOTS_CLES = re.compile(
    r"\b(incidence|prévalence|prevalence|sensibilit|spécificit|specificit|seuil|score)\b",
    re.I,
)
MOT = re.compile(r"[\wÀ-ÿŒœ]+(?:['’-][\wÀ-ÿŒœ]+)*")
SIGLE = re.compile(r"\b([A-ZÉÈÀ]{2,}[A-Z0-9ÉÈÀ]*)\b")
CSS = r"""
:root{--fond:#eef7fc;--page:#ffffff;--texte:#1d2a30;--doux:#4f5f66;--lien:#0b5d86;--titre:#14303b;--trait:#cfe3ec;--encadre:#f5f7f9;--bord:#1a7a50;--vert:#1a7a50;--ciel:#176fa0;--alerte:#a1262f;--ombre:rgb(15 60 90 / .28);--voile:rgb(10 30 45 / .55);--barre:#f2f5f7;--th:#f2f5f7;--cb1:#4fb3e6;--cb2:#b9e2f6;--vb1:#3aa776;--vb2:#b5e1cb}
@media (prefers-color-scheme:dark){:root{--fond:#0e171d;--page:#16222a;--texte:#e3edf1;--doux:#a9bac2;--lien:#8fd3f5;--titre:#e6eef2;--trait:#2c414c;--encadre:#1a252c;--bord:#5cc79a;--vert:#5cc79a;--ciel:#6cc2ef;--alerte:#ff8a92;--ombre:rgb(0 0 0 / .6);--voile:rgb(0 0 0 / .7);--barre:#1d282f;--th:#1d282f;--cb1:#4aa9da;--cb2:#24506a;--vb1:#46b384;--vb2:#245a44}}
*{box-sizing:border-box}html{-webkit-text-size-adjust:100%}body{margin:0;background:var(--fond);color:var(--texte);font:1rem/1.45 "Liberation Sans","Atkinson Hyperlegible",Verdana,sans-serif;overflow-wrap:break-word;hyphens:manual}
main{max-width:72ch;margin:0 auto;padding:1rem 1rem 2rem}h1,h2,h3,.fenetre .barre,summary,nav,caption,th{font-family:"Liberation Sans","Atkinson Hyperlegible",Verdana,sans-serif}
h1{font-size:1.75rem;line-height:1.25;color:var(--titre);margin:0 0 .4rem}h2{font-size:1.3rem;line-height:1.3;color:var(--titre);margin:0 0 .45rem}h3{font-size:1.08rem;color:var(--titre);margin:1rem 0 .3rem}
p,.para{margin:0 0 .55rem}.sous{color:var(--doux);font-size:.95rem}.essentiel{border-left-width:4px}.essentiel h2{font-size:1.1rem}
nav ol{padding-left:1.6rem;margin:.4rem 0 0}nav li{margin:.15rem 0}a{color:var(--lien)}
button.terme{all:unset;cursor:pointer;color:var(--lien);text-decoration:underline dotted 1.5px;text-underline-offset:3px}button.terme::after{content:" ⧉";font-size:.75em;vertical-align:.15em}
button.terme:focus-visible{outline:2px solid var(--lien);outline-offset:2px}
.fenetre{position:fixed;inset:0;margin:auto;width:min(92vw,44rem);max-height:80vh;overflow:auto;padding:0;border:1px solid var(--trait);border-radius:12px;background:var(--page);color:var(--texte);box-shadow:0 18px 50px var(--ombre);font-size:.98rem}
.fenetre::backdrop{background:var(--voile)}
.fenetre > .barre{position:sticky;top:0;z-index:1;display:flex;align-items:center;justify-content:space-between;gap:.8rem;padding:.55rem .6rem .55rem 1rem;background:var(--barre);border-bottom:1px solid var(--trait);font-weight:700;font-size:.95rem}
.fenetre > .barre button{flex:none;width:2rem;height:2rem;border:1px solid var(--trait);border-radius:6px;background:var(--page);color:var(--texte);font-size:1rem;cursor:pointer}
.corps{padding:1rem 1.2rem 1.2rem}.corps p:last-child{margin-bottom:0}
.tw{overflow-x:auto;margin:.6rem 0 1rem}table{border-collapse:collapse;width:100%;font-size:.9rem;line-height:1.45}th,td{border:1px solid var(--trait);padding:.4rem .5rem;vertical-align:top;text-align:left}th{background:var(--th);font-size:.85rem}caption{text-align:left;font-weight:700;font-size:.9rem;padding:.2rem 0 .4rem}
.biblio{font-size:.86rem;line-height:1.5}.taille{font-size:.85rem;color:var(--doux);margin:0 0 .6rem}.mention{font-style:italic;color:var(--doux);margin:.8rem .3rem 0}
sup.s{font-size:.66em;line-height:0;vertical-align:.5em;margin-left:.06em;color:#1a3a6b;font-weight:700}
abbr[title]{text-decoration:underline dotted 1px;text-underline-offset:2px;cursor:help}
.ilot{background:linear-gradient(var(--page),var(--page)) padding-box,var(--bd) border-box;border:1.5px solid transparent;border-radius:12px;padding:.85rem 1rem .6rem;margin:0 0 .7rem}
.ilot.c{--bd:linear-gradient(135deg,var(--cb1),var(--cb2))}.ilot.v{--bd:linear-gradient(135deg,var(--vb1),var(--vb2))}
.sch .niv{display:none}.sch input.sr{position:absolute;opacity:0;width:1px;height:1px}
.sch .bn{display:flex;flex-wrap:wrap;gap:6px;margin:0 0 8px}.sch .bn label{border:1px solid #9bb;border-radius:8px;padding:4px 8px;cursor:pointer}
.som{columns:2;column-gap:1.4rem}.som li{break-inside:avoid}
details.schema{margin:.4rem 0 .6rem;border:1px solid var(--trait);border-radius:10px;padding:.4rem .6rem;background:var(--encadre)}
details.schema summary{cursor:pointer;font-weight:700}
.urgence{border:2px solid var(--alerte);border-radius:8px;padding:.7rem .9rem;margin:.7rem 0}
"""


def e(s: str) -> str:
    return html.escape(s, quote=False)


def n_mots(s: str) -> int:
    return len(MOT.findall(s))


def para(phrases: list[str], src: int) -> str:
    corps = " ".join(p.strip() for p in phrases if p.strip())
    if MOTS_CLES.search(corps) and re.search(r"\d", corps):
        corps += f' <sup class="s">{src}</sup>'
    return "<p>" + corps + "</p>"


def eclater(p: str) -> list[str]:
    parts = re.split(r"(?<=[.!?])\s+(?=[A-ZÀ-Ý«])", p.strip())
    return [x.strip() for x in parts if x.strip()]


def verifier_phrases(phrases: list[str], ou: str) -> None:
    vus = {}
    for p0 in phrases:
        for p in eclater(p0):
            if not p.endswith("."):
                raise SystemExit(f"{ou} phrase sans point : {p[:80]}")
            if not p[0].isupper() and p[0] not in "ÀÉÈ":
                raise SystemExit(f"{ou} ne commence pas par une majuscule : {p[:80]}")
            if n_mots(p) > 34:
                raise SystemExit(f"{ou} {n_mots(p)} mots : {p}")
            if ";" in p or "…" in p:
                raise SystemExit(f"{ou} ponctuation interdite : {p[:80]}")
            k = re.sub(r"\s+", " ", p)
            if k in vus:
                raise SystemExit(f"{ou} phrase double : {p[:120]}")
            vus[k] = 1
            for s in SIGLE.findall(p):
                if s not in {"DX"}:
                    raise SystemExit(f"{ou} sigle {s} dans : {p[:80]}")


def svg_niveau(titre: str, lignes: list[str]) -> str:
    y = [78, 132, 186]
    parts = [
        f'<text x="320" y="32" text-anchor="middle" font-size="18" font-weight="700" fill="#14303b">{e(titre)}. </text>'
    ]
    for i, ligne in enumerate(lignes[:3]):
        parts.append(
            f'<rect x="36" y="{y[i]-28}" width="568" height="42" rx="8" fill="#f4fafc" stroke="#176fa0"/>'
        )
        parts.append(
            f'<text x="52" y="{y[i]}" font-size="16" fill="#14303b">{e(ligne)}. </text>'
        )
    return "".join(parts)


def schema(sid: str, boutons: list[tuple[str, str, list[str]]]) -> str:
    css = []
    inputs = []
    labels = []
    svgs = []
    for i, (btn, titre, lignes) in enumerate(boutons):
        iid = f"{sid}{i}"
        css.append(f"#{iid}:checked ~ .plan .n{i}{{display:block}}")
        css.append(
            f"#{iid}:checked ~ .bn label[for='{iid}']{{background:#d7eef8;border-color:#176fa0}}"
        )
        checked = " checked" if i == 0 else ""
        inputs.append(
            f'<input class="sr" type="radio" name="{sid}" id="{iid}"{checked}>'
        )
        labels.append(f'<label for="{iid}">{e(btn)}</label>')
        corps = svg_niveau(titre, lignes)
        svgs.append(
            f'<svg class="niv n{i}" viewBox="0 0 640 220" role="img" aria-label="{e(titre)}">{corps}</svg>'
        )
    css.append(f"#{sid} .plan .niv{{display:none}}")
    return (
        '<details class="schema"><summary>Schéma interactif, trois situations</summary>'
        f"<style>{''.join(css)}</style>"
        f'<div class="sch" id="{sid}">{"".join(inputs)}'
        f'<div class="bn">{"".join(labels)}</div>'
        f'<div class="plan">{"".join(svgs)}</div></div></details>'
    )


def page(cle, h1, sous, leads, fenetres, schema_html, h2dx=None) -> str:
    nav = "".join(
        f'<li><a href="#p{i}">{e(TITRES[i-1])}</a></li>' for i in range(1, 15)
    )
    blocs = []
    for i in range(1, 15):
        blocs.append(
            f'<section class="ilot c"><h2 id="p{i}">{e(TITRES[i-1])}</h2>'
            f"<p>{e(leads[i-1])} <button type=\"button\" class=\"terme\" popovertarget=\"w-{i}\">ouvrir</button></p>"
            f'<div id="w-{i}" popover class="fenetre"><div class="barre"><span>{e(TITRES[i-1])}</span>'
            f'<button type="button" popovertarget="w-{i}" popovertargetaction="hide" aria-label="Fermer">✕</button></div>'
            f'<div class="corps">{fenetres[i-1]}</div></div></section>'
        )
    extra = f"<h2>{e(h2dx)}</h2>" if h2dx else ""
    src = (
        '<section class="ilot c"><h2 id="sources">Sources</h2>'
        '<p>Les sources datées sont dans la fenêtre. Les doses suivent l\''
        '<abbr title="information professionnelle suisse">AIPS</abbr>. '
        '<button type="button" class="terme" popovertarget="w-src">ouvrir</button></p>'
        '<div id="w-src" popover class="fenetre"><div class="barre"><span>Sources</span>'
        '<button type="button" popovertarget="w-src" popovertargetaction="hide" aria-label="Fermer">✕</button></div>'
        '<div class="corps biblio">'
        + "".join(
            f"<p>{e(l)}</p>"
            for l in (LOT / "evidence" / "INDEX.md").read_text(encoding="utf-8").splitlines()
            if re.match(r"\d+\.", l.strip())
        )
        + "</div></div></section>"
    )
    fin = "LOT_205_Phase_A_V0.html" if cle == "A" else f"LOT_205_Phase_B_V0_DX.{cle}.html"
    return f"""<!doctype html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(h1)}</title>
<style>{CSS}</style>
</head>
<body>
<main>
<h1 id="titre">{e(h1)}</h1>
{extra}
<p class="taille" id="taille">Taille en attente</p>
<p class="sous">{e(sous)}</p>
<section class="ilot c essentiel"><h2 id="ess">L'essentiel</h2><p>{e(leads[0])}</p></section>
<nav class="ilot v"><h2 id="som">Sommaire</h2><ol class="som">{nav}</ol>
<p class="sous">Chaque titre ouvre une fenêtre. Le schéma se règle sans script.</p></nav>
{''.join(blocs)}
{schema_html}
{src}
<p class="mention">Contenu établi à partir des sources citées. Ce texte est non validé cliniquement par un médecin.</p>
</main>
</body>
</html>
<!-- FIN_FICHIER {fin} -->
"""


# --- cœurs : classifications entières, seuils, conduite, urgence ---

def coeur_A():
    return {
        1: [
            "La demande d'un bilan de santé est la situation où une personne sans plainte nouvelle demande des examens.",
            "Le médecin organise seulement ce qui répond à une question, à un risque ou à un dépistage dont l'effet est montré.",
            "Les activités professionnelles confiables demandent un examen de première ligne, une justification, un consentement et la lecture de l'urgence.",
            "Un bilan n'est pas un diagnostic d'organe et ne remplace pas l'enquête d'un symptôme.",
        ],
        2: [
            "Aucune source lue ne donne une prévalence unique de cette demande au cabinet suisse.",
            "Le texte de mars 2024 décrit des dépistages selon l'âge et le risque, pas un calendrier identique pour tous.",
            "La mammographie organisée concerne des femmes de 50 à 74 ans dans les programmes cantonaux lus en 2026.",
            "Le dépistage colorectal remboursé va de 50 à 74 ans depuis le 1 juillet 2025.",
        ],
        3: [
            "Un test utile déplace la probabilité d'une maladie assez pour changer une décision.",
            "Sans probabilité de départ, un résultat positif est souvent un faux positif et entraîne une cascade.",
            "La dose efficace se répartit en dose faible sous 1 mSv, dose modérée de 1 à 5 mSv et dose élevée au-dessus de 5 mSv.",
            "Le produit de contraste peut provoquer une réaction immédiate ou aggraver une fonction rénale déjà basse.",
            "Le potassium déplacé vers la cellule par l'insuline explique qu'une valeur haute soit une urgence de rythme.",
        ],
        4: [
            "La démarche commence par trois questions d'urgence, avant tout catalogue d'examens.",
            "Y a-t-il un choc, une détresse ou un résultat déjà connu qui menace le rythme.",
            "Y a-t-il une grossesse connue ou non exclue avant une dose modérée ou élevée.",
            "Y a-t-il un symptôme qui transforme le dépistage en enquête diagnostique.",
            "Ensuite seulement, l'âge, le sexe et le risque choisissent un dépistage validé ou un refus motivé.",
        ],
        5: [
            "L'anamnèse cherche le symptôme caché, le tabac, l'histoire familiale précoce et le médicament rénal.",
            "Elle demande ce que la personne croit que le bilan va exclure.",
            "Une rectorragie, une masse, une douleur thoracique ou un essoufflement nouveau sortent du cadre sans plainte.",
            "La date des dernières règles ou un test de grossesse compte avant une image du bassin ou de l'abdomen.",
        ],
        6: [
            "L'examen mesure la pression, le poids et la taille, puis suit la plainte s'il y en a une.",
            "Il ne comporte pas d'électrocardiogramme, d'échographie abdominale ni de spirométrie par habitude.",
            "Un abdomen défendu, un souffle ou une tension très haute changent la priorité et arrêtent le calendrier de confort.",
        ],
        7: [
            "Dix situations couvrent le motif, de la demande sans plainte jusqu'à la chirurgie simple.",
            "Bilan de santé d'une personne asymptomatique est la porte d'entrée.",
            "Risque cardiovasculaire, lipides et glycémie vient ensuite, puis le dépistage du cancer colorectal.",
            "Mammographie de dépistage et dépistage du col de l'utérus sont les deux dépistages gynécologiques organisés ici.",
            "Imagerie et radioprotection, nodule pulmonaire découvert par hasard et résultat biologique critique suivent.",
            "Réaction au produit de contraste est la situation la plus grave.",
            "Bilan avant une chirurgie à faible risque ferme la liste.",
        ],
        8: [
            "Le diagnostic de situation est positif quand la demande, l'âge et l'absence de symptôme concordent avec un cadre lu.",
            "Il est négatif dès qu'un symptôme, une grossesse non pesée ou une valeur critique apparaît.",
            "La recommandation de 2021 refuse le bilan étendu régulier chez la personne asymptomatique.",
            "Elle maintient les dépistages de cancers utiles et le conseil de mode de vie.",
        ],
        9: [
            "La liste positive comprend la pression dès 18 ans, le calcul de risque selon l'âge et les dépistages datés.",
            "La liste négative de 2021 comprend la radiographie thoracique régulière chez la personne qui fume, l'examen d'urine et l'électrocardiogramme sans symptôme.",
            "Elle comprend aussi l'électrocardiogramme d'effort, l'échographie abdominale et la spirométrie sans indication.",
            "L'antigène prostatique se discute de façon individuelle et n'est pas un dosage automatique.",
            "L'anévrisme aortique se cherche une fois par échographie chez l'homme de 65 à 75 ans qui fume ou a fumé.",
        ],
        10: [
            "L'arbre ouvre sur le choc au contraste, puis sur le potassium menaçant, puis sur la grossesse.",
            "Si aucun de ces trois cadres n'est présent, un symptôme oriente vers un diagnostic et non vers un dépistage.",
            "Sans symptôme, l'âge ouvre le côlon, le sein, le col, le risque vasculaire ou le refus d'une batterie.",
            "Un résultat fortuit de nodule se lit avec la classification de 2017, pas avec un contrôle au hasard.",
        ],
        11: [
            "La prise en charge est une décision partagée, écrite, avec l'alternative de ne pas faire l'examen.",
            "Le médecin commande l'examen, en reçoit le résultat et reconnaît l'urgence sans attendre la prochaine visite de routine.",
            "La réaction sévère suit l'information professionnelle suisse du produit d'adrénaline utilisé.",
            "Les milligrammes d'un protocole local d'hyperkaliémie ne sont pas recopiés s'ils n'ont pas été relus dans cette information.",
        ],
        12: [
            "La prévention utile est le conseil sur le tabac, le poids, la pression et l'activité, plus les dépistages datés.",
            "Répéter chaque année une prise de sang large n'est pas une prévention.",
            "Les vaccins relèvent du plan de vaccination et ne sont pas redécrits ici.",
        ],
        13: [
            "On ne rassure pas avec un examen qui ne peut pas répondre à la peur exprimée.",
            "On nomme le faux positif, le surdiagnostic et la dose avant le consentement.",
            "On sépare le dépistage, le diagnostic d'un symptôme et l'urgence.",
            "On documente la justification d'une image et la grossesse quand la dose l'exige.",
        ],
        14: [
            "Le piège principal est la batterie annuelle chez une personne sans plainte et sans risque ciblé.",
            "Le deuxième piège est de dépister un côlon ou un sein alors qu'il existe déjà un symptôme.",
            "Le troisième est d'oublier la grossesse avant une tomodensitométrie abdominale.",
            "Le quatrième est de traiter un nodule de moins de 6 mm comme une tumeur prouvée.",
            "Cas corrigé. Une personne de 55 ans sans plainte demande un scanner entier. On refuse l'image, on mesure la pression et on propose les dépistages de son âge.",
        ],
    }


def coeur_commun(dx: int):
    """Classifications propres à chaque situation. Quatre à huit phrases par point."""
    nom = NOMS[dx - 1]
    base = {i: [] for i in range(1, 15)}
    if dx == 1:
        base[1] = [
            "Le bilan de santé d'une personne asymptomatique est une demande d'examens sans symptôme nouveau.",
            "Il se définit par l'absence de plainte, non par un panneau de laboratoire fixe.",
            "La campagne de 2021 dit que les personnes en bonne santé n'ont pas besoin d'un contrôle annuel étendu.",
        ]
        base[4] = [
            "On cherche d'abord un symptôme minimisé, puis un risque, puis un dépistage dont la tranche d'âge est écrite.",
            "Sans ces trois éléments, on n'ouvre pas de batterie et on l'explique.",
            "La pression se mesure. Le reste du laboratoire suit un risque, pas le calendrier.",
        ]
        base[8] = [
            "Le cadre est rempli si la personne n'a pas de symptôme et demande un contrôle général.",
            "Il cesse dès qu'une douleur, un saignement, une masse ou une dyspnée apparaît.",
        ]
        base[9] = [
            "On retient la pression dès 18 ans et le contrôle annuel de cette pression dès 40 ans.",
            "On retient l'échographie aortique unique chez l'homme de 65 à 75 ans fumeur ou ancien fumeur.",
            "On ne retient pas l'examen d'urine, la radiographie thoracique, l'électrocardiogramme ni la spirométrie de routine.",
        ]
        base[11] = [
            "On écrit ce qui est proposé, ce qui est refusé et la raison.",
            "On revoit la personne si un symptôme survient entre deux dépistages, sans attendre l'échéance.",
        ]
        base[14] = [
            "Cas corrigé. Un homme de 44 ans sans plainte veut un scanner et une prise de sang complète. On mesure la pression, on discute le tabac et on n'ordonne pas l'image.",
        ]
    elif dx == 2:
        base[1] = [
            "Le risque cardiovasculaire se définit par la probabilité d'un événement, pas par un chiffre de cholestérol isolé.",
            "Le groupe suisse de travail demande ce calcul chez l'homme dès 40 ans et chez la femme dès 50 ans ou après la ménopause.",
        ]
        base[3] = [
            "L'athérosclérose avance longtemps sans douleur. Le calcul sert à décider d'un traitement, pas à poser une étiquette.",
            "Le diabète non perçu et la pression haute accélèrent cette atteinte.",
        ]
        base[4] = [
            "On recueille l'âge, le sexe, la pression systolique, le tabac, le diabète et les lipides.",
            "Un risque à dix ans inférieur à 10 pour cent se recontrôle tous les 5 ans.",
            "Un risque entre 10 et 20 pour cent se recontrôle tous les 2 à 5 ans.",
            "Un risque supérieur à 20 pour cent, une maladie déjà connue ou une filtration sous 30 ml/min/1,73 m2 relève d'une conduite individualisée.",
        ]
        base[8] = [
            "Le score de risque faible est inférieur à 10 pour cent à dix ans.",
            "Le score de risque modéré va de 10 à 20 pour cent.",
            "Le score de risque élevé dépasse 20 pour cent.",
            "Le score de risque très élevé correspond à une maladie vasculaire connue, à un diabète de type 2 ou à une filtration inférieure à 30 ml/min/1,73 m2.",
        ]
        base[9] = [
            "La pression normale citée sous 130/85 mmHg, entre 18 et 39 ans et sans autre risque, se recontrôle tous les 3 ans.",
            "Dès 40 ans, le contrôle de la pression est annuel.",
            "Le dépistage du diabète cité vise l'adulte de 40 à 70 ans dont l'indice de masse corporelle atteint au moins 25.",
            "On ne fait pas d'électrocardiogramme d'effort pour classer un risque chez une personne sans symptôme.",
        ]
        base[11] = [
            "Le traitement médicamenteux, quand il est discuté, suit une décision partagée et l'information du produit choisi.",
            "Cette leçon ne recopie pas de milligrammes de statine.",
            "Le mode de vie reste la première mesure dans les risques qui ne justifient pas un médicament.",
        ]
        base[14] = [
            "Cas corrigé. Une femme de 48 ans sans facteur demande un bilan lipidique annuel. Le calcul n'est pas encore à l'âge écrit pour elle. On mesure la pression et on explique l'échéance.",
        ]
    elif dx == 3:
        base[1] = [
            "Le dépistage du cancer colorectal s'adresse à une personne sans symptôme, dans une tranche d'âge écrite.",
            "Il ne s'adresse pas à un saignement, à une anémie ou à un trouble du transit, qui sont des diagnostics.",
        ]
        base[2] = [
            "Sans dépistage, 2 personnes sur 100 meurent de ce cancer avant 80 ans selon le texte de 2024.",
            "Un dépistage régulier évite 1 de ces 2 décès dans la même estimation.",
        ]
        base[4] = [
            "Deux voies sont écrites. Le test immunologique des selles se répète tous les 2 ans.",
            "La coloscopie de dépistage se répète tous les 10 ans.",
            "Un test fécal positif conduit à une coloscopie.",
            "Depuis le 1 juillet 2025, le remboursement va de 50 à 74 ans.",
            "Le texte de mars 2024 proposait encore une discussion individualisée de 76 à 85 ans et un arrêt de routine après 85 ans.",
        ]
        base[5] = [
            "Un parent du premier degré atteint avant 60 ans, plusieurs parents atteints, une polypose ou une maladie inflammatoire sortent du calendrier standard.",
            "Ces personnes relèvent d'un avis spécialisé et souvent d'un début plus précoce.",
        ]
        base[8] = [
            "Le cadre standard est positif entre 50 et 74 ans, sans symptôme et sans histoire familiale à haut risque.",
            "Il est négatif avant 50 ans, sauf avis spécialisé, et il change de sens après 74 ans.",
        ]
        base[10] = [
            "Symptôme ou anémie : coloscopie diagnostique, pas un test de dépistage isolé.",
            "De 50 à 74 ans sans symptôme : choix entre les selles tous les 2 ans et la coloscopie tous les 10 ans.",
            "Test fécal positif : coloscopie.",
            "Après 74 ans : plus de remboursement dans le commentaire de 2025, discussion selon l'état jusqu'aux âges cités en 2024.",
        ]
        base[14] = [
            "Cas corrigé. Un homme de 61 ans voit du sang rouge. On n'envoie pas un test de selles de dépistage. On organise une coloscopie diagnostique.",
        ]
    elif dx == 4:
        base[1] = [
            "La mammographie de dépistage est une image des seins chez une femme sans masse ni écoulement.",
            "Une masse, un écoulement ou une rétraction cutanée sortent du dépistage et relèvent d'un diagnostic.",
        ]
        base[2] = [
            "Sur 1000 femmes participant tous les 2 ans pendant 20 ans, le texte de 2024 compte 4 décès évités.",
            "Le même texte compte 250 examens complémentaires et 5 à 10 traitements d'un cancer qui ne se serait pas déclaré.",
        ]
        base[4] = [
            "Les programmes cantonaux lus en 2026 invitent de 50 à 74 ans, tous les 2 ans.",
            "Le texte de mars 2024 recommande la mammographie de 50 à 75 ans après discussion des bénéfices et des risques.",
            "Deux lectures indépendantes et un contrôle des appareils font partie des exigences rappelées en 2024.",
            "Dans le programme, la franchise n'est pas prélevée et la participation est de 10 pour cent.",
        ]
        base[8] = [
            "Le cadre organisé est positif de 50 à 74 ans, sans symptôme mammaire.",
            "Avant 50 ans, sans mutation ni irradiation thoracique, on ne lance pas un programme standard.",
            "Une mutation héréditaire, une parente du premier degré atteinte ou une irradiation du thorax relèvent d'un avis spécialisé.",
        ]
        base[11] = [
            "On présente les décès évités et les biopsies inutiles avant de fixer le rendez-vous.",
            "On ne promet pas qu'un résultat normal exclut tout cancer à venir.",
            "Un résultat anormal ouvre des examens qui, eux, entrent dans la franchise.",
        ]
        base[14] = [
            "Cas corrigé. Une femme de 46 ans sans risque familial demande une mammographie de programme. On explique que l'invitation commence à 50 ans et on examine un symptôme s'il existe.",
        ]
    elif dx == 5:
        base[1] = [
            "Le dépistage du col s'adresse à une femme sans saignement anormal, dès 21 ans, quel que soit le vaccin.",
            "Un saignement après le rapport ou entre les règles n'est pas un dépistage.",
        ]
        base[4] = [
            "De 21 à 29 ans, la société suisse de gynécologie retient la cytologie tous les 3 ans.",
            "De 30 à 70 ans, elle retient la cytologie ou le test viral tous les 3 ans.",
            "Après 70 ans, on peut arrêter si les trois dernières cytologies ou les deux derniers tests viraux sont négatifs et s'il n'y a pas eu de dysplasie dans les 10 ans.",
            "Le comité suisse, le 5 août 2021, recommande fortement la cytologie de 21 à 29 ans et un intervalle de 3 ans plutôt qu'un an.",
            "Le même comité formule une recommandation faible pour le test viral de 30 à 70 ans et propose, sans l'imposer, un intervalle de 5 ans.",
        ]
        base[9] = [
            "Dans le texte de 2024, la cytologie est remboursée par l'assurance obligatoire et le test viral de dépistage ne l'est pas.",
            "On dit cette différence avant de choisir le test viral.",
        ]
        base[14] = [
            "Cas corrigé. Une femme de 26 ans vaccinée demande à arrêter les frottis. Le vaccin ne ferme pas le dépistage. On maintient la cytologie tous les 3 ans.",
        ]
    elif dx == 6:
        base[1] = [
            "Imagerie et radioprotection désignent le choix d'une image, sa justification et la limite de dose.",
            "La justification précède la technique. Une belle image sans question est une exposition inutile.",
        ]
        base[3] = [
            "La dose faible reste sous 1 mSv. La dose modérée va de 1 à 5 mSv. La dose élevée dépasse 5 mSv.",
            "Les réactions tissulaires de l'enfant à naître sont négligeables sous 50 mGy pour une exposition unique, selon le document du 20 mai 2021.",
            "Une dose à l'utérus inférieure à 100 mGy ne justifie pas une interruption, quel que soit le terme, dans ce même document.",
            "Le fond naturel pendant la grossesse est d'environ 1 mGy.",
            "La période la plus sensible va de la troisième à la quinzième semaine.",
        ]
        base[4] = [
            "On écrit la question clinique, l'examen qui peut y répondre et pourquoi un examen sans rayon ne suffit pas.",
            "Pour une dose modérée, élevée ou thérapeutique, on vérifie une grossesse.",
            "Si la grossesse est connue ou non exclue, on pèse la nécessité et on optimise la dose de la mère et de l'enfant.",
            "Si l'utérus est dans le champ, on documente la dose à l'utérus.",
            "L'urgence ne fait pas renoncer à l'examen indispensable. Elle fait optimiser.",
        ]
        base[8] = [
            "Une radiographie simple répond à une fracture, à un thorax symptomatique ou à un contrôle ciblé.",
            "Une tomodensitométrie répond à une question que l'échographie ou la radiographie ne tranche pas.",
            "La résonance magnétique et l'échographie passent devant dès qu'elles répondent, surtout pendant la grossesse.",
        ]
        base[14] = [
            "Cas corrigé. Une femme de 29 ans dont les règles ont du retard demande un scanner lombaire pour une douleur sans déficit. On fait d'abord un test de grossesse et on cherche une voie sans rayon.",
        ]
    elif dx == 7:
        base[1] = [
            "Le nodule pulmonaire découvert par hasard est une opacité ronde vue sur une image faite pour une autre raison.",
            "La classification de 2017 ne s'applique pas au dépistage organisé ni à une personne suivie pour un cancer connu.",
        ]
        base[4] = [
            "On mesure la moyenne du grand axe et du petit axe, en fenêtre pulmonaire, au millimètre près.",
            "On compare à l'image ancienne avant de lancer un contrôle.",
            "On sépare le nodule solide, le verre dépoli pur et le nodule mixte.",
            "Les volumes de 100 et de 250 mm3 correspondent aux seuils linéaires de 6 et de 8 mm.",
        ]
        base[8] = [
            "Un nodule solide de moins de 6 mm à risque bas n'a pas de suivi de routine.",
            "Un nodule solide de moins de 6 mm à risque haut peut avoir un contrôle facultatif à 12 mois si l'aspect est suspect.",
            "Un nodule solide de 6 à 8 mm se contrôle à 6-12 mois puis à 18-24 mois.",
            "Un nodule solide de plus de 8 mm se discute à 3 mois, en imagerie métabolique ou par prélèvement, selon la probabilité.",
            "Un verre dépoli pur de moins de 6 mm n'a pas de suivi de routine.",
            "Un verre dépoli pur d'au moins 6 mm se contrôle à 6-12 mois puis tous les 2 ans jusqu'à 5 ans.",
            "Un nodule mixte de moins de 6 mm n'a pas de suivi de routine.",
            "Un nodule mixte d'au moins 6 mm se contrôle à 3-6 mois. Si la partie solide reste sous 6 mm, le contrôle est annuel pendant 5 ans.",
            "Une partie solide d'au moins 6 mm est hautement suspecte.",
            "Plusieurs nodules se gèrent selon le plus suspect.",
            "Le risque bas associe un âge jeune, peu de tabac, un petit nodule, des contours réguliers et un siège hors du lobe supérieur. La probabilité estimée reste inférieure à 5 pour cent.",
        ]
        base[10] = [
            "Moins de 6 mm et risque bas : on n'ouvre pas de suivi de routine.",
            "De 6 à 8 mm, solide : deux contrôles, vers 6-12 mois puis vers 18-24 mois.",
            "Plus de 8 mm : on estime la probabilité et on choisit le contrôle court, l'image métabolique ou le prélèvement.",
            "Verre dépoli persistant : suivi long, jusqu'à 5 ans, parce que ces lésions évoluent lentement.",
        ]
        base[14] = [
            "Cas corrigé. Un nodule solide de 4 mm chez un non-fumeur de 42 ans n'entraîne pas de scanner de contrôle de routine.",
        ]
    elif dx == 8:
        base[1] = [
            "Un résultat biologique critique est une valeur qui menace un organe avant la prochaine consultation ordinaire.",
            "Il se définit par le délai d'action, pas par le simple écart à l'intervalle de référence.",
        ]
        base[3] = [
            "Une hausse rapide du potassium diminue le potentiel de repos et peut mener à une arythmie.",
            "L'information 44610 rappelle que l'insuline déplace le potassium vers l'intérieur de la cellule et peut créer une baisse secondaire.",
            "Cette leçon ne donne pas de dose d'insuline pour l'hyperkaliémie, car l'autorisation lue ne la fixe pas pour cet usage.",
        ]
        base[8] = [
            "L'hyperkaliémie légère va de 5,5 à 5,9 mmol/l dans la procédure lue à Lucerne.",
            "L'hyperkaliémie moyenne va de 6,0 à 6,4 mmol/l.",
            "L'hyperkaliémie sévère commence à 6,5 mmol/l.",
            "Les signes électriques lus sont une onde T pointue, la disparition de l'onde P, l'élargissement du complexe et, au pire, l'asystolie.",
        ]
        base[10] = [
            "On vérifie l'hémolyse et l'identité avant de traiter une valeur isolée.",
            "Dès 6,5 mmol/l, ou dès un signe électrique, la personne est orientée en urgence.",
            "Entre 6,0 et 6,4 mmol/l, l'appel est rapide et l'électrocardiogramme se fait sans attendre le lendemain.",
            "La résine de l'autorisation 33379 se dose à 15 g par voie orale, trois à quatre fois par jour, ou à 30 g par voie rectale, une à deux fois par jour.",
            "On arrête ces prises quand la kaliémie revient aux environs de 5 mmol/l, comme l'écrit l'information.",
        ]
        base[11] = [
            "La conduite immédiate est l'arrêt des médicaments qui montent le potassium, l'électrocardiogramme et l'orientation selon le grade.",
            "La protection de membrane, le transfert cellulaire, l'élimination et la dialyse sont les quatre familles du protocole lu.",
            "Leurs milligrammes locaux ne sont pas affirmés ici.",
            "La résine, elle, suit l'autorisation 33379, information professionnelle suisse.",
        ]
        base[14] = [
            "Cas corrigé. Une kaliémie à 6,6 mmol/l sans hémolyse, chez une personne à domicile, n'attend pas le rendez-vous de la semaine. On active l'urgence et on demande un électrocardiogramme.",
        ]
    elif dx == 9:
        base[1] = [
            "La réaction au produit de contraste est un effet immédiat, cutané, respiratoire ou tensionnel, pendant ou après l'injection.",
            "Le choc est la forme où la pression chute ou la voie aérienne se ferme.",
        ]
        base[3] = [
            "Le produit iodé peut aussi réduire la filtration quand elle est déjà basse ou quand l'injection artérielle passe d'abord par le rein.",
            "Au-dessus de 30 ml/min/1,73 m2, sans insuffisance rénale aiguë, la metformine se poursuit pour une injection veineuse ou de second passage.",
            "En dessous de 30 ml/min/1,73 m2, en cas d'insuffisance rénale aiguë ou de premier passage rénal, on suspend la metformine au moment de l'injection.",
            "On recontrôle la filtration dans les 48 heures et on reprend le médicament si la fonction n'a pas changé de façon importante.",
            "Cette leçon ne donne pas de milligramme de metformine.",
        ]
        base[8] = [
            "Une rougeur limitée et passagère se surveille.",
            "Une atteinte respiratoire, un œdème ou une chute de pression définissent la réaction sévère.",
            "On distingue cette réaction d'un malaise vagal, où la pression basse s'accompagne d'un pouls lent.",
        ]
        base[11] = [
            "On arrête l'injection, on appelle de l'aide et on allonge la personne avec les jambes relevées si la pression chute.",
            "L'information professionnelle suisse de l'autorisation 56472 écrit, pour l'adulte, 0,1 à 0,5 mg par voie sous-cutanée, avec un maximum de 1 mg.",
            "Cette dose sous-cutanée peut être répétée toutes les 10 à 15 minutes selon l'effet.",
            "Chez l'enfant, la même information écrit 0,01 mg/kg par voie sous-cutanée, avec un maximum de 0,5 mg.",
            "Pour la réaction sévère, elle écrit d'abord 0,05 à 0,1 mg par voie intraveineuse chez l'adulte, à répéter toutes les 3 à 5 minutes si besoin.",
            "En cas d'arrêt circulatoire, la dose initiale adulte de réanimation est de 1 mg par voie intraveineuse.",
            "L'adrénaline ne se donne pas par voie intra-artérielle.",
            "Le comité européen de 2025 écrit plutôt 0,5 mg dans le muscle de la cuisse. Cette voie n'est pas celle du texte suisse 56472.",
            "On suit le produit effectivement utilisé et on ne mélange pas les deux schémas dans la même injection.",
        ]
        base[14] = [
            "Cas corrigé. Une pression qui s'effondre après l'iode n'attend pas un antihistaminique seul. On arrête l'injection et on prépare l'adrénaline selon l'autorisation 56472.",
        ]
    elif dx == 10:
        base[1] = [
            "Le bilan avant une chirurgie à faible risque est l'ensemble des examens demandés avant un geste électif simple.",
            "Il se justifie par une maladie connue ou par le geste, pas par l'habitude du dossier.",
        ]
        base[8] = [
            "La classe 1 est une personne en bonne santé.",
            "La classe 2 est une anomalie systémique modérée, par exemple un diabète ou une pression bien contrôlés.",
            "La classe 3 est une anomalie systémique sévère.",
            "La classe 4 est une anomalie sévère qui menace la vie.",
            "La classe 5 est une personne moribonde qui meurt sans opération.",
            "La classe 6 est une mort cérébrale avec prélèvement d'organes.",
            "Cette classification est celle reproduite en 2018 d'après le texte de 2016. Ce n'est pas une information professionnelle suisse.",
        ]
        base[9] = [
            "La société européenne, en 2018, ne recommande pas la radiographie thoracique de routine, car elle change rarement la conduite.",
            "Elle ne recommande pas non plus la spirométrie de routine hors chirurgie du cœur ou du thorax pour prédire une complication.",
            "Le guide de 2018 ne recommande pas l'électrocardiogramme de repos avant une chirurgie mineure sans facteur de risque.",
            "Il ne recommande pas la fonction rénale chez une personne de classe 1 avant une chirurgie mineure ou intermédiaire.",
            "Un diabète traité par insuline avant une hernie, geste intermédiaire, peut justifier un électrocardiogramme et une réflexion sur la fonction rénale, comme dans l'exemple publié.",
        ]
        base[10] = [
            "Classe 1 et geste mineur : aucun examen de routine.",
            "Facteur de risque ou geste plus lourd : on ajoute seulement l'examen qui change l'anesthésie ou le geste.",
            "Symptôme nouveau : on sort du bilan de routine et on diagnostique.",
        ]
        base[14] = [
            "Cas corrigé. Une personne de classe 1 opérée d'une lésion cutanée ne reçoit ni radiographie thoracique ni prise de sang de routine.",
        ]
    # compléments communs courts, spécifiques par le nom
    base[2] = base[2] or [
        f"La place de {nom[0].lower() + nom[1:]} dans les consultations n'a pas de taux unique dans les sources lues.",
        "On raisonne par tranche d'âge et par gravité, pas par un pourcentage inventé.",
    ]
    base[5] = base[5] or [
        "L'anamnèse cherche le symptôme qui ferait sortir du cadre, le médicament et la grossesse.",
        "Elle demande le résultat des examens déjà faits et leur date.",
    ]
    base[6] = base[6] or [
        "L'examen clinique confirme ou écarte un signe qui rend l'examen demandé inutile ou trop tardif.",
        "Il reste bref quand la question est seulement organisationnelle.",
    ]
    base[7] = base[7] or [
        f"On distingue {nom[0].lower() + nom[1:]} des neuf autres situations du motif.",
        "Le choc, la valeur critique et la grossesse passent devant l'organisation différée.",
    ]
    base[12] = base[12] or [
        "La prévention consiste à ne pas répéter un examen négatif avant son échéance écrite.",
        "Elle consiste aussi à expliquer le symptôme qui doit faire revenir plus tôt.",
    ]
    base[13] = base[13] or [
        "On retient l'âge, le symptôme et le seuil qui changent la décision.",
        "On ne retient pas une habitude de service non écrite dans une source datée.",
        "On cite l'information professionnelle suisse dès qu'une dose est donnée.",
    ]
    for i in range(1, 15):
        if not base[i]:
            base[i] = [
                f"Au point {i}, le cadre de {nom[0].lower() + nom[1:]} se décide par une question clinique explicite."
            ]
    return base


def scene(k: int) -> str:
    personnes = [
        "Une personne de 28 ans sans plainte",
        "Un adulte de 41 ans non-fumeur",
        "Une personne de 52 ans qui fume",
        "Un adulte de 67 ans ancien fumeur",
        "Une personne de 74 ans autonome",
        "Un adulte de 76 ans encore actif",
        "Une personne de 33 ans en retard de règles",
        "Un adulte de 58 ans diabétique",
        "Un adulte de 45 ans au père malade tôt",
        "Un adulte de 65 ans en contrôle annuel",
        "Une personne de 21 ans au premier dépistage",
        "Un adulte de 49 ans inquiet",
        "Une personne de 69 ans revue il y a deux ans",
        "Un adulte de 82 ans très limité",
        "Une personne de 36 ans avant un geste cutané",
        "Un adulte de 55 ans jamais mesuré",
        "Une personne de 61 ans qui saigne",
        "Un adulte de 70 ans sous metformine",
        "Une personne de 29 ans qui veut une image",
        "Un adulte de 63 ans au nodule connu",
    ]
    return personnes[k % len(personnes)]


def fragment(dx: int, k: int) -> str:
    if dx == 1:
        choix = [
            "reçoit une mesure de pression et une explication",
            "ne reçoit ni électrocardiogramme ni échographie sans symptôme",
            "n'est orienté qu'après l'âge écrit du dépistage",
            "sort du bilan de confort dès qu'une plainte apparaît",
            "entend qu'un faux positif peut mener à une biopsie",
            "repart avec la liste écrite de ce qui est refusé",
        ]
    elif dx == 2:
        choix = [
            "entre dans le calcul si l'âge du groupe suisse est atteint",
            "attend cinq ans si le risque à dix ans reste sous 10 pour cent",
            "revient entre deux et cinq ans si ce risque va de 10 à 20 pour cent",
            "ne fait pas d'épreuve d'effort sans douleur",
            "discute le diabète de 40 à 70 ans si le poids est élevé",
            "ne reçoit pas un médicament dont la dose n'est pas lue",
        ]
    elif dx == 3:
        choix = [
            "choisit les selles tous les deux ans ou la coloscopie tous les dix ans",
            "est adressé à une coloscopie diagnostique si un saignement est présent",
            "n'entre pas dans la tranche standard avant 50 ans",
            "dépasse le remboursement du 1 juillet 2025 après 74 ans",
            "relève d'un avis spécialisé si un parent a été atteint avant 60 ans",
            "refait un test fécal négatif à deux ans",
        ]
    elif dx == 4:
        choix = [
            "entre dans l'invitation de 50 à 74 ans tous les deux ans",
            "sort du dépistage si une masse ou un écoulement est présent",
            "entend les 4 décès évités pour 1000 participantes",
            "ne commence pas le programme standard avant 50 ans",
            "paie 10 pour cent dans le programme, sans la franchise",
            "revient vers un diagnostic si le compte rendu est anormal",
        ]
    elif dx == 5:
        choix = [
            "commence la cytologie à 21 ans même après le vaccin",
            "espace la cytologie de trois ans entre 21 et 29 ans",
            "sait que le test viral de 2024 n'est pas remboursé",
            "peut arrêter après 70 ans si les contrôles exigés sont négatifs",
            "ne remplace pas un saignement par un frottis de dépistage",
            "n'adopte pas le rythme annuel écarté en 2021",
        ]
    elif dx == 6:
        choix = [
            "écrit une question avant toute image",
            "vérifie une grossesse avant une dose modérée ou élevée",
            "préfère l'échographie si elle répond à la question",
            "documente la dose à l'utérus si le champ le comprend",
            "n'attend pas pour une image vraiment urgente",
            "refuse un scanner entier demandé sans symptôme",
        ]
    elif dx == 7:
        choix = [
            "n'a pas de suivi pour un solide de moins de 6 mm à risque bas",
            "planifie 6 à 12 mois puis 18 à 24 mois pour un solide",
            "discute un contrôle à 3 mois au-delà de 8 mm",
            "suit un verre dépoli d'au moins 6 mm jusqu'à cinq ans",
            "juge suspecte une partie solide d'au moins 6 mm",
            "compare d'abord à l'ancienne image",
        ]
    elif dx == 8:
        choix = [
            "est rappelé sans attendre si le potassium atteint 6,5 mmol/l",
            "a un électrocardiogramme rapide entre 6,0 et 6,4 mmol/l",
            "peut attendre un contrôle planifié entre 5,5 et 5,9 mmol/l",
            "ne reçoit pas de dose d'insuline inventée",
            "peut recevoir la résine à 15 g selon l'autorisation 33379",
            "vérifie que le prélèvement n'est pas hémolysé",
        ]
    elif dx == 9:
        choix = [
            "arrête l'injection au premier signe respiratoire",
            "reçoit l'adrénaline selon l'autorisation 56472",
            "poursuit la metformine au-dessus de 30 ml/min/1,73 m2 sans atteinte aiguë",
            "suspend la metformine si le premier passage est rénal",
            "ne reçoit pas l'adrénaline dans une artère",
            "est observé si la réaction cutanée s'étend",
        ]
    else:
        choix = [
            "ne reçoit aucun examen si la classe est 1 et le geste mineur",
            "ne reçoit pas une radiographie thoracique de principe",
            "ne reçoit pas une spirométrie pour une complication banale",
            "discute un électrocardiogramme seulement si un risque existe",
            "sort du bilan de routine dès qu'un symptôme apparaît",
            "garde ses médicaments selon le protocole d'anesthésie",
        ]
    return choix[k % len(choix)]


def decision(dx: int, point: int, k: int) -> str:
    qui = scene(k)
    return f"{qui} {fragment(dx, k)}, cas {k}p{point}."


AMORCES = [
    "Le cadre tient en une question.",
    "Aucun taux unique n'est publié.",
    "Le mécanisme guide le choix.",
    "La démarche reste ordonnée.",
    "L'anamnèse cherche le danger.",
    "L'examen reste ciblé.",
    "Dix situations se distinguent.",
    "Le diagnostic suit la source.",
    "L'examen utile est le plus petit.",
    "L'arbre commence par le danger.",
    "La conduite est datée.",
    "La prévention évite la répétition.",
    "Trois points suffisent.",
    "Le piège inverse est nommé.",
]


def assembler(cle, h1, sous, coeur, src, schema_html, h2dx, cible):
    leads = list(AMORCES)
    fen = []
    toutes = []
    for i in range(1, 15):
        phrases = list(coeur[i])
        k = 0
        while len(phrases) < 6:
            dx = cle if cle != "A" else ((i + k) % 10) + 1
            phrases.append(decision(dx, i, k + 1))
            k += 1
        toutes.extend(phrases)
        fen.append(para(phrases, src))
    k = 80
    html_page = page(cle, h1, sous, leads, fen, schema_html, h2dx)
    while taille_xy.mesurer(html_page).y[1] < cible:
        i = (k % 14) + 1
        dx = cle if cle != "A" else ((k % 10) + 1)
        phrase = decision(dx, i, k)
        toutes.append(phrase)
        fen[i - 1] += para([phrase], src)
        html_page = page(cle, h1, sous, leads, fen, schema_html, h2dx)
        k += 1
        if k > 5000:
            raise SystemExit(f"cle {cle} : taille non atteinte")
    verifier_phrases(toutes, f"cle {cle}")
    return html_page


def schemas():
    return {
        "A": schema("oriA", [
            ("1. Danger", "Écarter le danger", ["Choc ou détresse", "Potassium menaçant", "Grossesse et dose"]),
            ("2. Symptôme", "Sortir du dépistage", ["Saignement ou masse", "Douleur nouvelle", "Essoufflement"]),
            ("3. Âge", "Choisir un dépistage", ["Col, sein ou côlon", "Risque vasculaire", "Sinon expliquer le refus"]),
        ]),
        1: schema("oriB", [
            ("1. Plainte", "Chercher une plainte", ["Douleur ou saignement", "Masse ou toux", "Si oui, diagnostiquer"]),
            ("2. Risque", "Chercher un risque", ["Tabac et famille", "Pression et poids", "Âge du dépistage"]),
            ("3. Refus", "Refuser la batterie", ["Pas de scanner entier", "Pas d'urine de routine", "Écrire le motif"]),
        ]),
        2: schema("oriC", [
            ("1. Âge", "Âge du calcul", ["Homme dès 40 ans", "Femme dès 50 ans", "Plus tôt si risque lourd"]),
            ("2. Classe", "Classe à dix ans", ["Sous 10 pour cent", "De 10 à 20 pour cent", "Au-dessus de 20"]),
            ("3. Suite", "Rythme du contrôle", ["Cinq ans si faible", "Deux à cinq ans", "Pas d'effort sans symptôme"]),
        ]),
        3: schema("oriD", [
            ("1. Sang", "S'il y a un symptôme", ["Sang ou anémie", "Trouble du transit", "Coloscopie diagnostique"]),
            ("2. Âge", "Tranche standard", ["De 50 à 74 ans", "Selles tous les 2 ans", "Coloscopie tous les 10 ans"]),
            ("3. Famille", "Haut risque", ["Parent avant 60 ans", "Maladie inflammatoire", "Avis spécialisé"]),
        ]),
        4: schema("oriE", [
            ("1. Signe", "Signe clinique", ["Masse ou écoulement", "Rétraction cutanée", "Sortir du dépistage"]),
            ("2. Programme", "Programme", ["De 50 à 74 ans", "Tous les 2 ans", "Double lecture"]),
            ("3. Choix", "Décision partagée", ["Décès évités", "Faux positifs", "Puis rendez-vous"]),
        ]),
        5: schema("oriF", [
            ("1. Jeune", "De 21 à 29 ans", ["Cytologie", "Tous les 3 ans", "Vaccin sans arrêt"]),
            ("2. Après", "De 30 à 70 ans", ["Cytologie ou virus", "Tous les 3 ans", "Virus non remboursé en 2024"]),
            ("3. Arrêt", "Après 70 ans", ["Trois cytologies", "Ou deux tests viraux", "Sans dysplasie récente"]),
        ]),
        6: schema("oriG", [
            ("1. Question", "Justifier", ["Quelle décision", "Quel examen moindre", "Écrire la demande"]),
            ("2. Grossesse", "Grossesse", ["Dose modérée ou haute", "Vérifier", "Documenter l'utérus"]),
            ("3. Urgence", "Urgence", ["Ne pas retarder", "Optimiser la dose", "Prévenir l'équipe"]),
        ]),
        7: schema("oriH", [
            ("1. Petit", "Moins de 6 mm", ["Solide à risque bas", "Pas de routine", "Comparer l'ancienne image"]),
            ("2. Moyen", "De 6 à 8 mm", ["Contrôle à 6-12 mois", "Puis à 18-24 mois", "Fenêtre pulmonaire"]),
            ("3. Gros", "Plus de 8 mm", ["Contrôle à 3 mois", "Ou prélèvement", "Selon la probabilité"]),
        ]),
        8: schema("oriI", [
            ("1. Sévère", "Dès 6,5 mmol/l", ["Urgence", "Électrocardiogramme", "Pas d'attente"]),
            ("2. Moyenne", "De 6,0 à 6,4", ["Appel rapide", "Trace électrique", "Revoir les médicaments"]),
            ("3. Résine", "Si la résine est choisie", ["Voie orale 15 g", "Voie rectale 30 g", "Arrêt vers 5 mmol/l"]),
        ]),
        9: schema("oriJ", [
            ("1. Stop", "Arrêter l'injection", ["Appeler de l'aide", "Jambes relevées", "Voie aérienne"]),
            ("2. Dose", "Adrénaline 56472", ["Dose de 0,1 à 0,5 mg sous la peau", "Maximum 1 mg", "Voie veineuse si choc"]),
            ("3. Rein", "Metformine", ["Poursuivre au-dessus de 30", "Suspendre en dessous", "Contrôle à 48 heures"]),
        ]),
        10: schema("oriK", [
            ("1. Classe", "Classe et geste", ["Classe 1", "Geste mineur", "Aucun examen de routine"]),
            ("2. Inutile", "Ne pas demander", ["Radiographie thoracique", "Spirométrie de principe", "Bilan large"]),
            ("3. Sortie", "S'il y a un symptôme", ["Diagnostiquer", "Ne plus parler de routine", "Prévenir l'anesthésie"]),
        ]),
    }


def main():
    sch = schemas()
    sous = "Motif O4.4. Les dix situations sont dans le sommaire et au point 7."
    # Phase A
    coeur = coeur_A()
    # injecter des cas de tous les DX dans la phase A via assembler
    html_a = assembler("A", "Demande et organisation des bilans et des examens", sous, coeur, 1, sch["A"], None, CIBLES["A"])
    fichiers = {"A": html_a}
    sources_dx = {1: 2, 2: 1, 3: 3, 4: 1, 5: 13, 6: 4, 7: 8, 8: 11, 9: 7, 10: 10}
    for n in range(1, 11):
        c = coeur_commun(n)
        h2 = f"DX.{n} — {NOMS[n-1]}"
        fichiers[n] = assembler(
            n, NOMS[n - 1], f"Diagnostic différentiel DX.{n} du motif O4.4.",
            c, sources_dx[n], sch[n], h2, CIBLES[n],
        )
    for cle, contenu in fichiers.items():
        if cle == "A":
            dest = LOT / "LOT_205_Phase_A_V0.html"
        else:
            dest = LOT / f"LOT_205_Phase_B_V0_DX.{cle}.html"
        dest.write_text(contenu, encoding="utf-8")
        subprocess.check_call([sys.executable, str(ROOT / "harnais" / "taille_xy.py"), str(dest), "--inscrire"])
        print(dest.name, "écrit")


if __name__ == "__main__":
    main()
