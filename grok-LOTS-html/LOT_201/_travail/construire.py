#!/usr/bin/env python3
"""Construit les 11 leçons de LOT_201 (O3.7 Incontinence urinaire et fécale)."""
from __future__ import annotations

import html
import importlib.util
import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path("/workspace/grok-LOTS-html/LOT_201")
MOTS_CLES = re.compile(r"prévalence|incidence|sensibilit|spécificit|seuil|score", re.I)

TITRES = {
    1: "Définition",
    2: "Épidémiologie",
    3: "Physiopathologie",
    4: "Démarche diagnostique",
    5: "Anamnèse et drapeaux rouges",
    6: "Examen physique",
    7: "Approche syndromique",
    8: "Diagnostic positif",
    9: "Examens complémentaires",
    10: "Arbre décisionnel",
    11: "Prise en charge",
    12: "Prévention",
    13: "Points clés",
    14: "Pièges et cas",
}

NOMS = {
    "A": "Incontinence urinaire et fécale",
    1: "Incontinence urinaire d'effort",
    2: "Incontinence urinaire par urgenturie",
    3: "Incontinence urinaire mixte",
    4: "Incontinence urinaire fonctionnelle ou médicamenteuse",
    5: "Incontinence fécale par fécalome",
    6: "Incontinence fécale par atteinte du sphincter ou diarrhée",
    7: "Incontinence urinaire par rétention chronique",
    8: "Prolapsus pelvien avec fuites",
    9: "Incontinence continue par fistule",
    10: "Syndrome de la queue de cheval",
}

CIBLES = {
    "A": 74500,
    1: 37200,
    2: 39800,
    3: 42100,
    4: 44600,
    5: 45800,
    6: 38100,
    7: 40900,
    8: 43300,
    9: 46400,
    10: 44100,
}

NIVEAU = {
    "A": "repos",
    1: "effort",
    2: "repos",
    3: "effort",
    4: "repos",
    5: "fecalome",
    6: "fecalome",
    7: "repos",
    8: "effort",
    9: "fistule",
    10: "repos",
}


class Sigles:
    LIB = {
        "EAU": "European Association of Urology",
        "NICE": "institut britannique pour l'excellence clinique",
        "AIPS": "information professionnelle suisse",
        "IRM": "imagerie par résonance magnétique",
        "CHUV": "centre hospitalier universitaire vaudois",
    }
    COURT = {
        "EAU": "association européenne d'urologie",
        "NICE": "institut britannique pour l'excellence clinique",
        "AIPS": "information professionnelle suisse",
        "IRM": "imagerie par résonance magnétique",
        "CHUV": "centre hospitalier universitaire vaudois",
    }

    def __call__(self, s: str) -> str:
        exp = self.LIB[s]
        court = self.COURT[s]
        return f'<abbr title="{html.escape(exp)}">{s}</abbr> ({court})'


def mots(texte: str) -> int:
    brut = re.sub(r"<[^>]+>", " ", texte)
    return len(re.findall(r"[\wÀ-ÿŒœ'’\-]+", brut))


def P(texte: str, sup: int | None = None) -> str:
    if mots(texte) > 34:
        raise SystemExit(f"PHRASE LONGUE ({mots(texte)}): {texte}")
    if ";" in texte:
        raise SystemExit(f"POINT-VIRGULE: {texte}")
    nu = re.sub(r"</?abbr[^>]*>", "", texte)
    if "<" in nu or ">" in nu:
        raise SystemExit(f"CHEVRON: {texte}")
    if MOTS_CLES.search(re.sub(r"<[^>]+>", " ", texte)) and re.search(r"\d", texte) and not sup:
        raise SystemExit(f"CHIFFRE SANS SUP: {texte}")
    fin = f' <sup class="s">{sup}</sup>' if sup else ""
    return f"<p>{texte}{fin}</p>"


def schema(prefix: str) -> str:
    panneaux = [
        ("1. Urgence.", [
            "Queue de cheval, rétention douloureuse, sepsis.",
            "Fuite continue, sang rectal, anémie récente.",
            "On n'attend pas une anesthésie en selle.",
        ]),
        ("2. Séparer.", [
            "Urine à l'effort, avec urgence, ou les deux.",
            "Selles par bouchon, sphincter ou diarrhée.",
            "Fuite continue : penser à une fistule.",
        ]),
        ("3. Premier geste.", [
            "Calendrier, urine, résidu échographique.",
            "Toucher rectal avant tout ralentisseur.",
            "Rééducation et entraînement avant le médicament.",
        ]),
    ]
    css, inputs, labels, svgs = [], [], [], []
    for i, (etq, lignes) in enumerate(panneaux):
        iid = f"{prefix}{i}"
        checked = " checked" if i == 0 else ""
        css.append(
            f"#{iid}:checked ~ .plan .n{i}{{display:block}}"
            f"#{iid}:checked ~ .bn label[for='{iid}']{{background:#d7eef8;border-color:#176fa0}}"
        )
        inputs.append(f'<input class="sr" type="radio" name="{prefix}" id="{iid}"{checked}>')
        labels.append(f'<label for="{iid}">{html.escape(etq)}</label>')
        y = 36
        parts = [
            f'<text x="320" y="28" text-anchor="middle" font-size="18" font-weight="700" fill="#14303b"> {html.escape(etq)}</text>'
        ]
        for ligne in lignes:
            parts.append(f'<rect x="28" y="{y}" width="584" height="42" rx="8" fill="#e7f4fb" stroke="#176fa0"/>')
            parts.append(
                f'<text x="320" y="{y+26}" text-anchor="middle" font-size="15" fill="#14303b"> {html.escape(ligne)}</text>'
            )
            y += 54
        svgs.append(
            f'<svg class="niv n{i}" viewBox="0 0 640 220" role="img" aria-label="{html.escape(etq)}">{"".join(parts)}</svg>'
        )
    style = f"<style>{''.join(css)}#{prefix} .plan .niv{{display:none}}</style>"
    return (
        f'{style}<div class="sch" id="{prefix}">{"".join(inputs)}'
        f'<div class="bn">{"".join(labels)}</div>'
        f'<div class="plan">{"".join(svgs)}</div></div>'
    )


def fragment_bassin() -> str:
    dest = Path("/workspace/grok-LOTS-html/outils/dessinateur/dessinateur.py")
    spec = importlib.util.spec_from_file_location("dess_lot201", dest)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    desc = json.loads((ROOT / "_travail" / "bassin.json").read_text(encoding="utf-8"))
    frag = mod.rendre(desc, "POLICE")
    police = "../outils/dessinateur/polices/AtkinsonHyperlegible-Regular.ttf"
    frag = frag.replace('url("POLICE")', f'url("{police}")')
    frag = re.sub(r"<script\b.*?</script>", "", frag, flags=re.S)
    if "<script" in frag:
        raise SystemExit("script restant")
    return frag


def choisir_niveau(fragment: str, niveau: str) -> str:
    frag = re.sub(r" checked=\"checked\"", "", fragment)
    cle = f'id="lot201-bassin-{niveau}"'
    if cle not in frag:
        raise SystemExit(f"niveau absent {niveau}")
    return frag.replace(cle, cle + ' checked="checked"', 1)


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
figure{margin:1.2rem 0}figure svg{width:100%;height:auto;max-width:40rem;display:block;margin:auto;color:var(--texte);background:#f7fbfd;border:1px solid var(--trait);border-radius:10px}
figcaption{font-size:.88rem;color:var(--doux);text-align:center;margin-top:.3rem}
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


def base_phrase(cle, n):
    nom = NOMS[cle]
    phrases = {
        1: f"On nomme {nom} par le moment de la fuite, pas par un seul chiffre.",
        2: "Les chiffres suisses lus donnent un ordre de grandeur, pas le rang des dix tableaux.",
        3: "Le verrou, le réservoir et le trop-plein ne se traitent pas de la même façon.",
        4: "On écarte d'abord la queue de cheval, la rétention douloureuse et la fuite continue.",
        5: "L'histoire sépare l'effort, l'urgence, le continu, la selle et le médicament.",
        6: "On palpe la vessie, on tousse, on regarde le périnée et on touche le rectum.",
        7: "Le syndrome se nomme après le danger, puis on le range parmi les dix tableaux.",
        8: "Le diagnostic positif reprend la plainte, l'examen et le calendrier.",
        9: "Le calendrier, l'urine et le résidu viennent avant un bilan lourd.",
        10: "L'arbre commence par le danger, puis par le liquide, puis par le premier geste.",
        11: "On protège, on rééduque, et le médicament suit l'information professionnelle suisse.",
        12: "Demander la question évite de laisser la fuite pour un vieillissement normal.",
        13: "Les repères de temps, de dose et de danger tiennent en quelques lignes.",
        14: "Le cas montre l'erreur la plus proche, puis la lecture retenue.",
    }
    return phrases[n]


def L(sac, n, texte, sup=None):
    sac.setdefault(n, []).append(P(texte, sup))


def commun(S, sac):
    L(sac, 1, "Une incontinence urinaire est toute plainte de perte involontaire d'urine.", 4)
    L(sac, 1, "L'effort fait fuir lors d'une pression abdominale, comme la toux, sans envie préalable.", 4)
    L(sac, 1, "L'urgenturie fait fuir avec une envie impérieuse, ou juste avant elle.", 4)
    L(sac, 1, "La forme mixte réunit les deux plaintes chez la même personne.", 4)
    L(sac, 1, "L'incontinence fécale est le passage involontaire de selles liquides ou solides depuis plus de 3 mois, après 4 ans.", 5)
    L(sac, 1, "L'incontinence anale ajoute les gaz à cette définition.", 5)
    L(sac, 1, "Le régorgement sur fécalome est une autre entité, fréquente chez la personne très âgée.", 5)
    L(sac, 2, "La prévalence urinaire lue est d'environ 10 à 20 pour cent chez les femmes de moins de 65 ans.", 4)
    L(sac, 2, "Elle dépasse 50 pour cent chez les femmes institutionnalisées dans la même revue de 2013.", 4)
    L(sac, 2, "Elle est rare chez les hommes de moins de 60 ans et atteint jusqu'à 43 pour cent après 80 ans.", 4)
    L(sac, 2, "Les femmes fuient surtout à l'effort ou de façon mixte, les hommes surtout par urgence.", 4)
    L(sac, 2, "Seulement la moitié des personnes concernées demandent de l'aide, d'après la revue de 2013.", 4)
    L(sac, 2, "La prévalence fécale lue va de 0,4 à 18 pour cent selon les études.", 5)
    L(sac, 2, "En Suisse, Roche et collaborateurs rapportent 10,3 pour cent dans le texte de 2009.", 5)
    L(sac, 2, "Moins d'un tiers des personnes le disent à leur médecin, selon la même revue.", 6)
    L(sac, 2, "Après un accouchement, 25 pour cent des femmes ont un trouble transitoire et 4 pour cent un trouble qui persiste.", 6)
    L(sac, 2, "Le syndrome de la queue de cheval est très rare, 1 à 3 pour 100 000, dans le parcours de 2023.", 7)
    L(sac, 2, "Aucun de ces pourcentages ne classe les dix fichiers du plus fréquent au plus rare.")
    L(sac, 3, "À l'effort, le col descend ou le sphincter urétral ne tient pas la pression.", 4)
    L(sac, 3, "L'urgenturie vient d'une contraction du détrusor que la personne ne retient pas.", 4)
    L(sac, 3, "Une vessie qui ne se vide pas finit par déborder, sans envie franche.", 4)
    L(sac, 3, "Une fistule court-circuite l'urètre et l'urine coule en dehors des mictions.", 4)
    L(sac, 3, "La lésion obstétricale est la cause la plus fréquente d'incontinence fécale dans la page de 2009.", 5)
    L(sac, 3, "La césarienne ne protège pas complètement, selon la même page.", 5)
    L(sac, 3, "Les efforts de poussée sur une constipation chronique blessent les nerfs honteux.", 5)
    L(sac, 3, "Le liquide fécal contourne alors un bouchon de selles dures.", 6)
    L(sac, 4, "Douleur de jambe ou de dos et trouble récent des urines, du périnée ou de la selle imposent l'urgence.", 7)
    L(sac, 4, "Le délai lu est un début depuis moins de 2 semaines, avec l'un des signes listés.", 7)
    L(sac, 4, "Aucun signe isolé n'est pathognomonique, et un examen négatif n'écarte pas le syndrome si les symptômes sont là.", 7)
    L(sac, 4, "L'imagerie seule ne fait pas le diagnostic.", 7)
    L(sac, 4, f"L'examen demandé est une {S('IRM')} en urgence, sur un site qui peut la faire.", 7)
    L(sac, 4, "On n'attend pas l'anesthésie en selle ni une rétention indolore, qui sont tardives.", 7)
    L(sac, 4, "Une sciatique bilatérale sans ces signes est un avertissement, pas le même degré d'urgence.", 7)
    L(sac, 4, "Une vessie douloureuse et palpable, avec impossibilité d'uriner, se vide sans attendre un volume seuil.")
    L(sac, 4, "On n'utilise aucun volume rond comme définition d'une rétention.")
    L(sac, 4, "Une fièvre avec douleur lombaire ou prostate sensible se traite comme une infection, pas comme une simple fuite.")
    L(sac, 4, "Une fuite continue, jour et nuit, après chirurgie, irradiation ou accouchement difficile, fait chercher une fistule.")
    L(sac, 4, "Un saignement rectal, une anémie ou un changement de transit inexpliqué partent en investigation urgente.", 3)
    L(sac, 5, "On demande si la fuite suit la toux, le rire ou le port d'une charge.")
    L(sac, 5, "On demande s'il y a une envie que la personne ne peut pas retenir.")
    L(sac, 5, "On demande si l'urine coule aussi la nuit, sans effort et sans envie.")
    L(sac, 5, "On demande la consistance des selles, les gaz, la garniture et la capacité d'attendre.")
    L(sac, 5, "On demande les accouchements, les déchirures, la chirurgie pelvienne et l'irradiation.")
    L(sac, 5, "On demande les médicaments qui remplissent la vessie, ceux qui la ferment et ceux qui endorment.")
    L(sac, 5, "On demande la soif, le diabète, une toux chronique et le poids.")
    L(sac, 5, "On demande une douleur de dos, un engourdissement du périnée et une faiblesse des jambes.", 7)
    L(sac, 6, "Le test de toux, vessie raisonnablement pleine, reproduit la fuite d'effort.")
    L(sac, 6, "Une voussure vaginale se regarde à la poussée, au repos et debout si besoin.")
    L(sac, 6, "Le toucher rectal cherche un bouchon, le tonus et une douleur.")
    L(sac, 6, "La sensibilité péri-anale et le tonus anal se notent, sans conclure s'ils sont normaux malgré les symptômes.", 7)
    L(sac, 6, "On regarde la force des releveurs du pied et l'extension du genou si le dos est en cause.", 7)
    L(sac, 6, "Une vessie que l'on sent au-dessus du pubis, avec douleur, n'attend pas le bilan du lendemain.")
    L(sac, 6, "Avant une rééducation, on vérifie au doigt que la personne contracte le bon muscle.", 2)
    L(sac, 9, f"Le guide {S('EAU')} de 2025 demande un calendrier mictionnel d'au moins 3 jours, recommandation forte.", 1)
    L(sac, 9, "L'analyse d'urine fait partie du premier bilan.", 1)
    L(sac, 9, "On ne traite pas une bactériurie sans symptôme chez la personne âgée pour faire disparaître la fuite.", 1)
    L(sac, 9, "Une vraie infection se traite, puis on réévalue la fuite.")
    L(sac, 9, "Le résidu se mesure par échographie, recommandation forte du même guide.", 1)
    L(sac, 9, "Il n'y a pas de consensus sur un résidu significatif chez la femme.", 1)
    L(sac, 9, "On préfère l'efficacité de vidange, volume uriné divisé par la somme du volume uriné et du résidu.", 1)
    L(sac, 9, "Ce calcul n'est pas un seuil diagnostique.")
    L(sac, 9, "On ne demande pas d'examen urodynamique de routine pour un effort simple ni pour une première urgenturie.", 1)
    L(sac, 9, "Le test de garniture d'une heure retient 1,4 gramme, bonne spécificité et faible sensibilité.", 1)
    L(sac, 9, "Le test de 24 heures retient 4,4 grammes et il est plus sensible, mais plus difficile à standardiser.", 1)
    L(sac, 9, "Le score de Wexner va de 0, continence, à 20, incontinence complète.", 8)
    L(sac, 9, "Cinq items, solides, liquides, gaz, garniture et vie, valent chacun de 0 à 4.", 8)
    L(sac, 9, "Jamais vaut 0, rarement moins d'une fois par mois vaut 1, parfois vaut 2.", 8)
    L(sac, 9, "Parfois signifie moins d'une fois par semaine et au moins une fois par mois.", 8)
    L(sac, 9, "Souvent vaut 3, moins d'une fois par jour et au moins une fois par semaine.", 8)
    L(sac, 9, "Toujours vaut 4, au moins une fois par jour.", 8)
    L(sac, 9, "Le score de Vaizey va de 0 à 24.", 8)
    L(sac, 9, "Solides, liquides, gaz et vie vont de 0 à 4, de jamais à tous les jours.", 8)
    L(sac, 9, "Rarement, pour Vaizey, est un épisode dans les 4 dernières semaines.", 8)
    L(sac, 9, "Parfois est plus d'un épisode en 4 semaines, mais moins d'un par semaine.", 8)
    L(sac, 9, "Chaque semaine vaut 3, et tous les jours vaut 4.", 8)
    L(sac, 9, "La garniture ou le bouchon vaut 2 si oui, le médicament ralentisseur vaut 2 si oui.", 8)
    L(sac, 9, "L'impossibilité d'attendre 15 minutes vaut 4 si oui.", 8)
    L(sac, 10, "D'abord le danger, ensuite le type de fuite, ensuite le geste qui ne demande pas de salle d'opération.")
    L(sac, 11, f"Le guide {S('EAU')} de 2025 propose une rééducation intensive supervisée d'au moins 3 mois en premier choix.", 1)
    L(sac, 11, "Cela vaut pour l'effort et la forme mixte, y compris chez la personne âgée et autour de la naissance.", 1)
    L(sac, 11, "Les groupes rééduqués avaient environ 8 fois plus de chances de se dire guéris dans la synthèse citée.", 1)
    L(sac, 11, "Ils avaient environ un épisode de fuite de moins par jour.", 1)
    L(sac, 11, "Le programme comprend au moins 8 contractions, 3 fois par jour.", 2)
    L(sac, 11, "On ne propose pas en routine un biofeedback par sonde ou par électromyographie.", 2)
    L(sac, 11, "L'entraînement vésical dure au moins 6 semaines en cas d'urgence ou de forme mixte.", 2)
    L(sac, 11, "Dans la forme mixte, on traite d'abord le symptôme le plus gênant, recommandation faible.", 1)
    L(sac, 11, "L'entraînement vésical est un premier choix fort dans la forme mixte.", 1)
    L(sac, 12, "On pose la question, car beaucoup de personnes croient que la fuite est normale avec l'âge.", 4)
    L(sac, 12, "Le poids et la toux chronique aggravent l'effort.", 4)
    L(sac, 12, "Si les selles sont dures ou la personne déshydratée, viser au moins 1,5 litre de boisson par jour, sauf contre-indication.", 3)
    L(sac, 12, "La rééducation commencée pendant la grossesse réduit le risque en fin de grossesse et juste après.", 1)
    L(sac, 12, "Chez la personne institutionnalisée, des mictions programmées peuvent aider.", 4)
    L(sac, 12, "Cet horaire n'a pas montré le même intérêt chez la personne fragile qui vit encore chez elle.", 4)
    L(sac, 12, "Les mesures comportementales réussissent mieux dans ce second groupe.", 4)


def pharmaco(S, sac, cle):
    """Doses uniquement si la chaîne est dans une information professionnelle archivée."""
    if cle in ("A", 1, 3, 8):
        L(sac, 11, "La duloxétine, autorisation 65781, n'a pas l'incontinence d'effort dans ses indications lues.", 17)
        L(sac, 11, "Aucune dose en milligrammes n'est donc enseignée pour une fuite à la toux.", 17)
        L(sac, 11, "Le guide britannique ne la met pas en premier choix.", 2)
        L(sac, 11, "Il l'envisage seulement si la femme préfère un médicament à la chirurgie, ou si elle ne peut pas être opérée.", 2)
        L(sac, 11, f"L'estriol vaginal, autorisation 47183, {S('AIPS')}, traite des symptômes génitaux de la ménopause.", 16)
        L(sac, 11, "Un ovule contient 0,5 mg d'estriol.", 16)
        L(sac, 11, "La dose lue est un ovule ou un applicateur de 0,5 g de crème chaque jour pendant 2 à 3 semaines.", 16)
        L(sac, 11, "L'entretien est un ovule ou un applicateur deux fois par semaine.", 16)
        L(sac, 11, "On garde la dose efficace la plus basse, le moins longtemps possible.", 16)
        L(sac, 11, "Plus d'un ovule par jour, ou la dose du jour coupée en plusieurs applications, appelle un progestatif 12 à 14 jours.", 16)
        L(sac, 11, "Cela concerne les femmes qui ont encore leur utérus.", 16)
        L(sac, 11, "Tension des seins, saignement, rétention d'eau ou ballonnement signifient une dose trop haute.", 16)
        L(sac, 11, "Si ces signes durent plus de 6 semaines, on baisse la dose.", 16)
        L(sac, 11, "L'usage n'est pas indiqué pendant la grossesse ni pendant l'allaitement.", 16)
        L(sac, 11, "Une grossesse qui commence sous traitement fait arrêter tout de suite.", 16)
        L(sac, 11, "On arrête aussi devant une suspicion de caillot, une migraine nouvelle ou des céphalées inhabituelles.", 16)
        L(sac, 11, "On arrête devant une perte soudaine de vue ou d'ouïe, un ictère ou une tension qui monte vraiment.", 16)
        L(sac, 11, "On arrête si un myome grandit.", 16)
        L(sac, 11, "Les contre-indications lues comprennent un cancer du sein ou de l'endomètre suspecté, et un saignement vaginal inexpliqué.", 16)
        L(sac, 11, "Elles comprennent aussi un caillot veineux passé ou présent, une thrombophilie et un événement artériel récent.", 16)
        L(sac, 11, "Une maladie du foie avec bilans encore anormaux et une porphyrie sont aussi lues comme contre-indications.", 16)
        L(sac, 11, "Un examen clinique et gynécologique précède le traitement, puis au moins une fois par an.", 16)
        L(sac, 11, "Le texte dit que l'on ne sait pas jusqu'où les risques du traitement hormonal par voie générale s'appliquent à cette crème.", 16)
        L(sac, 11, "On les garde en tête surtout si l'usage est long ou répété, car l'absorption peut être réelle au début.", 16)
    if cle in ("A", 2, 3, 4):
        L(sac, 11, f"La solifénacine, autorisation 57203, {S('AIPS')}, est indiquée dans l'instabilité vésicale avec urgence.", 9)
        L(sac, 11, "La dose lue est 5 mg une fois par jour, puis au besoin 10 mg une fois par jour.", 9)
        L(sac, 11, "Le comprimé s'avale entier.", 9)
        L(sac, 11, "Ni la sécurité ni l'efficacité ne sont établies chez l'enfant, et le produit ne devrait pas être utilisé dans ce groupe.", 9)
        L(sac, 11, "Si la clairance est d'au plus 30 millilitres par minute, ne pas dépasser 5 mg une fois par jour.", 9)
        L(sac, 11, "Une atteinte hépatique modérée ne dépasse pas non plus 5 mg une fois par jour.", 9)
        L(sac, 11, "Avec un inhibiteur enzymatique puissant, la dose maximale lue est 5 mg.", 9)
        L(sac, 11, "Les exemples lus sont le kétoconazole, les inhibiteurs de protéase et l'itraconazole.", 9)
        L(sac, 11, "Contre-indications lues : hypersensibilité, rétention urinaire, glaucome à angle fermé non traité.", 9)
        L(sac, 11, "Aussi une maladie digestive grave, comme un mégacôlon toxique, et une myasthénie grave.", 9)
        L(sac, 11, "Aussi une insuffisance hépatique sévère et les personnes sous hémodialyse.", 9)
        L(sac, 11, "Aussi une insuffisance rénale grave ou un foie moyen avec un inhibiteur enzymatique puissant.", 9)
        L(sac, 11, "Les données de grossesse sont insuffisantes, et l'usage impose la prudence.", 9)
        L(sac, 11, "On évite l'allaitement, le produit passant dans le lait chez l'animal avec un retard de croissance.", 9)
        L(sac, 11, "La bouche sèche est lue chez 11 pour cent à 5 mg et 22 pour cent à 10 mg.", 9)
        L(sac, 11, "Vision floue, fatigue, somnolence ou vertige peuvent gêner la conduite.", 9)
        L(sac, 11, "Un angio-œdème fait arrêter le produit et traiter l'obstruction des voies aériennes.", 9)
        L(sac, 11, f"Le mirabégron, autorisation 62755, {S('AIPS')}, traite l'hyperactivité avec fréquence, urgence ou fuite.", 10)
        L(sac, 11, "La dose initiale lue est 25 mg une fois par jour, avec ou sans repas.", 10)
        L(sac, 11, "L'effet est en général attendu vers 8 semaines, puis on peut monter à 50 mg une fois par jour.", 10)
        L(sac, 11, "Le comprimé s'avale entier, sans le croquer, le couper ni l'écraser.", 10)
        L(sac, 11, "L'association à un anticholinergique n'a pas de données de sécurité ni d'efficacité, et elle n'est pas recommandée.", 10)
        L(sac, 11, "Le produit n'est pas autorisé avant 18 ans.", 10)
        L(sac, 11, "Une atteinte hépatique légère, classe A, ne change pas la dose.", 10)
        L(sac, 11, "Une atteinte hépatique modérée, classe B, ne dépasse pas 25 mg une fois par jour.", 10)
        L(sac, 11, "La classe C n'a pas été évaluée, et l'usage n'est pas recommandé.", 10)
        L(sac, 11, "Une clairance de 30 à 89 millilitres par minute ne change pas la dose.", 10)
        L(sac, 11, "Une clairance de 15 à 29 millilitres par minute ne dépasse pas 25 mg une fois par jour.", 10)
        L(sac, 11, "En dessous de 15 millilitres par minute, ou sous hémodialyse, l'usage n'est pas recommandé.", 10)
        L(sac, 11, "Avec un inhibiteur enzymatique fort ou moyen, et un rein léger ou un foie léger, le maximum lu est 25 mg.", 10)
        L(sac, 11, "Cette association n'est pas recommandée si le rein est sévère ou le foie modéré.", 10)
        L(sac, 11, "Avec un inducteur fort et un foie et un rein normaux, on peut commencer à 50 mg, sans dépasser 50 mg.", 10)
        L(sac, 11, "La seule contre-indication lue est l'hypersensibilité au mirabégron ou aux excipients.", 10)
        L(sac, 11, "On est prudent si l'intervalle de repolarisation est long, et on surveille la tension.", 10)
        L(sac, 11, "On ne le donne pas pendant la grossesse, sauf nécessité thérapeutique absolue.", 10)
        L(sac, 11, "Les femmes en âge de procréer doivent utiliser une contraception efficace si le produit est choisi.", 10)
        L(sac, 11, "On ne le donne pas pendant l'allaitement.", 10)
        L(sac, 11, "Une rétention a été rapportée en cas d'obstacle sous la vessie, donc prudence si l'obstacle est net.", 10)
        L(sac, 11, "Un angio-œdème avec gêne respiratoire impose l'arrêt et les gestes d'urgence.", 10)
    if cle in ("A", 2, 3):
        L(sac, 11, "On ne propose pas l'oxybutynine à libération immédiate aux femmes âgées à haut risque de dégradation soudaine.", 2)
        L(sac, 11, f"L'oxybutynine orale, autorisation 70200, {S('AIPS')}, commence chez l'adulte à 2,5 mg trois fois par jour.", 12)
        L(sac, 11, "On reste ensuite à la dose efficace la plus basse.", 12)
        L(sac, 11, "La dose du jour peut être de 10 à 15 mg, au maximum 20 mg, en 2 à 3 prises, au plus 4.", 12)
        L(sac, 11, "Chez une personne âgée qui n'est pas dans le groupe fragile du guide, le départ lu est 2,5 mg deux fois par jour.", 12)
        L(sac, 11, "Le produit n'est pas autorisé avant 5 ans.", 12)
        L(sac, 11, "Dès 5 ans, le départ lu est 2,5 mg deux fois par jour, pour une hyperactivité du détrusor.", 12)
        L(sac, 11, "L'énurésie nocturne de l'enfant n'est pas le motif de ce cours, et elle exige d'abord un échec d'un autre traitement.", 12)
        L(sac, 11, "Le maximum pédiatrique lu est de 0,3-0,4 mg par kilogramme et par jour.", 12)
        L(sac, 11, "De 5 à 9 ans, le tableau lu dit 2,5 mg trois fois par jour.", 12)
        L(sac, 11, "De 9 à 12 ans, il dit 5 mg deux fois par jour.", 12)
        L(sac, 11, "Après 12 ans, il dit 5 mg trois fois par jour.", 12)
        L(sac, 11, "On avale le comprimé entier ou coupé en deux, avec de l'eau.", 12)
        L(sac, 11, "Oxybutynine orale et grossesse : pas d'usage sauf nécessité absolue.", 12)
        L(sac, 11, "Oxybutynine orale et allaitement : ne pas donner, de petites quantités passent dans le lait.", 12)
        L(sac, 11, "Somnolence et vision floue comptent pour la conduite, et l'alcool les augmente.", 12)
        L(sac, 11, "Contre-indications lues : hypersensibilité, glaucome à angle étroit ou chambre antérieure peu profonde, myasthénie.", 12)
        L(sac, 11, "Aussi un obstacle digestif, un iléus, une atonie, une rétention par obstacle ou par prostate.", 12)
        L(sac, 11, "Aussi une nycturie due au cœur ou au rein, une colite ulcéreuse sévère et un mégacôlon toxique.", 12)
        L(sac, 11, "La bouche sèche rend les nitrates sous la langue moins solubles, on humecte la bouche avant.", 12)
        L(sac, 11, "On surveille la confusion, surtout les premiers mois et à chaque hausse.", 12)
        L(sac, 11, f"Le timbre, autorisation 57733, {S('AIPS')}, contient 36 mg et libère 3,9 mg par 24 heures.", 11)
        L(sac, 11, "La dose lue est un timbre deux fois par semaine, tous les 3 à 4 jours.", 11)
        L(sac, 11, "On le pose sur peau sèche et intacte, ventre, hanche ou fesse, et on change d'endroit.", 11)
        L(sac, 11, "On ne repose pas au même endroit avant 7 jours, et on ne découpe pas le timbre.", 11)
        L(sac, 11, "Il n'est pas recommandé chez l'enfant ni l'adolescent.", 11)
        L(sac, 11, "Timbre d'oxybutynine et grossesse : pas d'usage sauf nécessité absolue.", 11)
        L(sac, 11, "Timbre d'oxybutynine et allaitement : non recommandé.", 11)
        L(sac, 11, "Aucune dose réduite n'est donnée si le foie ou le rein est diminué, et le suivi doit être étroit.", 11)
        L(sac, 11, "Chez la personne âgée, le texte ne juge pas un changement de dose nécessaire, mais demande la prudence.", 11)
        L(sac, 11, "Contre-indications lues : hypersensibilité, rétention, obstacle organique à la miction, nycturie cardiaque ou rénale.", 11)
        L(sac, 11, "Aussi mégacôlon toxique, colite ulcéreuse sévère, iléus, atonie, myasthénie sévère.", 11)
        L(sac, 11, "Aussi glaucome à angle fermé ou chambre antérieure étroite, et tachyarythmie.", 11)
        L(sac, 11, "On revoit l'effet sur la pensée au plus tard à 4 semaines, le guide laissant cette incertitude ouverte.", 2)
        L(sac, 11, "On ne propose ni flavoxate, ni propanthéline, ni imipramine pour ce motif.", 2)
    if cle in ("A", 5, 6):
        L(sac, 11, "On ne donne pas de ralentisseur tant qu'un bouchon, un excès de laxatif ou une selle dure n'est pas écarté.", 3)
        L(sac, 11, "On ne le donne pas non plus pour une diarrhée aiguë non diagnostiquée ni pour une poussée de colite ulcéreuse.", 3)
        L(sac, 11, f"Le lopéramide, autorisation 40363, {S('AIPS')}, a l'incontinence fécale dans ses indications, avec les diarrhées.", 13)
        L(sac, 11, "Chez l'adolescent et l'adulte, la diarrhée aiguë commence par 4 mg, soit deux gélules.", 13)
        L(sac, 11, "Puis 2 mg après chaque selle liquide, sans dépasser 16 mg par jour.", 13)
        L(sac, 11, "La diarrhée chronique commence par 4 mg, puis 2 à 12 mg pour une ou deux selles moulées par jour.", 13)
        L(sac, 11, "Le maximum lu reste 16 mg par jour.", 13)
        L(sac, 11, "On arrête quand les selles sont redevenues normales, ou s'il n'y a aucune selle depuis plus de 12 heures.", 13)
        L(sac, 11, "Avant 6 ans, ni gélule ni comprimé orodispersible.", 13)
        L(sac, 11, "De 6 à 12 ans, le départ lu est 2 mg, et l'entretien suit le poids sans dépasser huit unités.", 13)
        L(sac, 11, "Le plafond enfant lu est 6 mg par 20 kilogrammes.", 13)
        L(sac, 11, "Grossesse : seulement si c'est absolument nécessaire.", 13)
        L(sac, 11, "Allaitement : ne pas utiliser, une petite quantité passe dans le lait.", 13)
        L(sac, 11, "Contre-indications lues : moins de 6 ans, hypersensibilité, insuffisance hépatique sévère.", 13)
        L(sac, 11, "Pas en traitement de première ligne d'une dysenterie avec fièvre et glaires sanglantes.", 13)
        L(sac, 11, "Pas en première ligne d'une colite ulcéreuse aiguë ni d'une entérite invasive.", 13)
        L(sac, 11, "Pas en première ligne d'une colite liée aux antibiotiques.", 13)
        L(sac, 11, "On arrête tout de suite si constipation, ballonnement ou iléus apparaissent.", 13)
        L(sac, 11, "Si la diarrhée n'est pas meilleure après deux jours, on arrête et on cherche plus loin.", 13)
        L(sac, 11, "On commence bas et on ajuste à la consistance, comme le dit aussi le guide de 2007.", 3)
    if cle in ("A", 5, 7):
        L(sac, 11, "Un fécalome aigu se vide d'abord par voie rectale, quitte à répéter quelques jours.", 3)
        L(sac, 11, "Si cela échoue et qu'un obstacle est écarté, un laxatif oral puissant est possible, avec accès aux toilettes.", 3)
        L(sac, 11, f"Le macrogol, autorisation 53869, {S('AIPS')}, dilue un sachet dans 125 ml d'eau.", 14)
        L(sac, 11, "Pour une constipation adulte, l'habituel lu est 1 ou 2 sachets par jour.", 14)
        L(sac, 11, "Après 65 ans, un sachet par jour suffit en général.", 14)
        L(sac, 11, "Sans ordonnance, on ne dépasse pas 3 mois, faute d'expérience longue.", 14)
        L(sac, 11, "Pour une coprostase, 8 sachets dans la journée, en 6 heures, au plus 3 jours.", 14)
        L(sac, 11, "On peut aussi diluer ces 8 sachets dans 1 litre, bu le même jour en 6 heures.", 14)
        L(sac, 11, "Si le cœur est fragile, pas plus de 2 sachets par heure, avec une surveillance proche.", 14)
        L(sac, 11, "Le produit n'est pas recommandé avant 12 ans.", 14)
        L(sac, 11, "Chaque sachet contient 13,125 g de macrogol 3350.", 14)
        L(sac, 11, "Il contient aussi environ 186,81 mg de sodium.", 14)
        L(sac, 11, "L'arôme chocolat contient 14,1 mg d'alcool benzylique, et du dioxyde de soufre.", 14)
        L(sac, 11, "Contre-indications lues : hypersensibilité, obstruction, perforation, iléus, maladie inflammatoire grave, mégacôlon toxique.", 14)
        L(sac, 11, "On arrête devant un œdème, un essoufflement, une fatigue qui monte, une déshydratation ou une défaillance cardiaque.", 14)
        L(sac, 11, "Les autres médicaments oraux ne se prennent pas une heure avant, pendant, ni une heure après.", 14)
        L(sac, 11, "Le macrogol défait les épaississants à base d'amidon, danger si la déglutition exige un liquide épaissi.", 14)
        L(sac, 11, "Grossesse et allaitement : prudence, peu de données humaines.", 14)
        L(sac, 11, "La solution préparée ne remplace pas la boisson ordinaire.", 14)
    if cle in ("A", 7):
        L(sac, 11, f"La tamsulosine, autorisation 58170, {S('AIPS')}, traite les symptômes de l'hyperplasie bénigne de la prostate.", 15)
        L(sac, 11, "La dose lue est 0,4 mg, une capsule par jour, le matin après le petit-déjeuner.", 15)
        L(sac, 11, "On évite la prise à jeun.", 15)
        L(sac, 11, "On l'avale debout ou assis, avec environ 150 ml d'eau, entière, sans la croquer.", 15)
        L(sac, 11, "Elle n'est pas indiquée chez la femme, ni chez l'enfant ou l'adolescent.", 15)
        L(sac, 11, "Une atteinte hépatique sévère, classe C, est une contre-indication.", 15)
        L(sac, 11, "Les classes A et B ne demandent pas d'ajustement.", 15)
        L(sac, 11, "Un rein léger ou moyen ne change pas la dose.", 15)
        L(sac, 11, "En dessous de 10 millilitres par minute de clairance, aucune recommandation n'est donnée.", 15)
        L(sac, 11, "La personne âgée garde la même dose, avec un risque plus haut d'hypotension au lever.", 15)
        L(sac, 11, "Contre-indications lues : foie sévère, antécédent d'hypotension orthostatique, inhibiteur enzymatique puissant, hypersensibilité.", 15)
        L(sac, 11, "Les exemples lus sont la clarithromycine, l'itraconazole et le voriconazole.", 15)
        L(sac, 11, "Avant de commencer, on écarte d'autres causes, on touche le rectum et on peut doser l'antigène prostatique.", 15)
        L(sac, 11, "On prévient l'ophtalmologue avant une cataracte, à cause d'un iris flasque pendant l'opération.", 15)
        L(sac, 11, "La capsule contient moins de 23 mg de sodium.", 15)
        L(sac, 11, "Ce produit ne vide pas une vessie douloureuse déjà pleine. Le drainage vient d'abord.")
    if cle == 4:
        L(sac, 11, "On retire ou on baisse le médicament qui endort, qui force la diurèse au mauvais moment, ou qui ferme la vessie.", 4)
        L(sac, 11, "Aucune dose de diurétique n'est enseignée ici, faute d'information professionnelle archivée pour ce geste.")
        L(sac, 11, "Un anticholinergique est contre-indiqué si la vessie ne se vide déjà plus.", 9)
    if cle == 6:
        L(sac, 11, "Après l'échec des mesures simples, une neuromodulation sacrée se discute, avec une phase test de 2 à 3 semaines.", 6)
        L(sac, 11, "L'implant définitif se discute si l'amélioration dépasse 50 pour cent, en général en S3.", 6)
        L(sac, 11, "Une grosse déchirure anatomique se discute avec le chirurgien, pas avec un ralentisseur seul.", 6)
    if cle == 8:
        L(sac, 11, "Un prolapsus symptomatique de stade 1 ou 2 peut recevoir une rééducation supervisée d'au moins 16 semaines.", 2)
        L(sac, 11, "La grille en centimètres n'est pas recopiée, elle n'est pas dans l'extrait archivé.")
    if cle == 9:
        L(sac, 11, "La fistule se réfère, elle ne se ferme pas avec un anticholinergique ni avec une rééducation seule.")
        L(sac, 11, "On protège la peau et on cherche le trajet, sans créer un faux trajet au spéculum.")
    if cle == 10:
        L(sac, 11, "Le geste immédiat est l'orientation vers un site d'imagerie urgente, pas un médicament de la vessie.", 7)
        L(sac, 11, "On sonde si la vessie est pleine et douloureuse, sans définir la maladie par un volume.")


def specifique(cle, S):
    sac = {n: [] for n in range(1, 15)}
    commun(S, sac)
    pharmaco(S, sac, cle)
    nom = NOMS[cle]
    if cle == "A":
        L(sac, 7, "Les dix tableaux sont nommés ici, sans prétendre à un rang suisse unique.")
        for i in range(1, 11):
            L(sac, 7, f"DX.{i} — {NOMS[i]}")
        L(sac, 7, "L'urgence n'est pas l'ordre des fichiers.")
        L(sac, 7, "Elle commence par la queue de cheval, la rétention douloureuse, le sepsis et la fuite continue.")
        L(sac, 7, "Viennent ensuite le sang rectal et le fécalome, puis les fuites d'effort, d'urgence et mixtes.")
        L(sac, 8, "Le diagnostic du motif est clinique, complété par le calendrier et l'examen.")
        L(sac, 13, "Trois mois de rééducation avant de parler d'échec pour l'effort.", 1)
        L(sac, 13, "Six semaines d'entraînement vésical avant de juger l'urgence.", 2)
        L(sac, 13, "Pas de milligramme de duloxétine pour la toux.", 17)
        L(sac, 13, "Pas de ralentisseur sur un rectum plein.", 3)
        L(sac, 14, "Cas. Une femme de 70 ans porte une garniture et dit que c'est l'âge.")
        L(sac, 14, "La toux fait fuir, et elle a aussi une envie qu'elle ne tient pas jusqu'aux toilettes.")
        L(sac, 14, "Le rectum est vide, la vessie n'est pas douloureuse, le périnée sent.")
        L(sac, 14, "On retient une forme mixte, on commence par le symptôme qui la gêne le plus, et on rééduque.")
        L(sac, 14, "On ne lui propose pas d'emblée un anticholinergique à libération immédiate si elle est fragile.", 2)
    elif cle == 1:
        L(sac, 1, f"{nom} : perte petite et brutale à la toux, à l'éternuement ou au port, sans envie avant.", 4)
        L(sac, 3, "Le soutien ligamentaire est lâche, ou le sphincter urétral est faible, ou les deux.", 4)
        L(sac, 3, "La grossesse et le prolapsus vaginal sont les contextes féminins les plus cités en 2013.", 4)
        L(sac, 8, "On retient le diagnostic si la plainte et le test de toux concordent, infection écartée.")
        L(sac, 8, "Une fuite seulement la nuit, sans effort, n'est pas ce tableau.")
        L(sac, 13, "Premier choix : rééducation supervisée au moins 3 mois, au moins 8 contractions trois fois par jour.", 1)
        L(sac, 13, "La bandelette sous-urétrale fait mieux que la rééducation si l'effort est moyen ou sévère, selon le guide de 2025.", 1)
        L(sac, 13, "Ce constat ne saute pas l'essai de rééducation chez une femme qui peut le faire.", 1)
        L(sac, 14, "Cas. À 46 ans, quelques gouttes à chaque quinte, jamais d'urgence, deux accouchements.")
        L(sac, 14, "L'urine est propre et le résidu échographique est petit, sans qu'un seuil féminin soit fixé.", 1)
        L(sac, 14, "On n'envoie pas d'emblée en urodynamique.", 1)
        L(sac, 14, "On vérifie la contraction au doigt, puis on rééduque au moins 3 mois.", 2)
        L(sac, 14, "L'erreur serait une duloxétine dosée comme un antidépresseur pour cette toux.", 17)
    elif cle == 2:
        L(sac, 1, f"{nom} : la fuite accompagne une envie irrésistible, ou la précède de peu.", 4)
        L(sac, 3, "Le détrusor se contracte alors que la personne voudrait encore attendre.", 4)
        L(sac, 3, "Chez l'homme, ce mécanisme est le plus souvent en cause, d'après la revue de 2013.", 4)
        L(sac, 8, "Le calendrier montre des fuites liées à l'urgence, pas seulement à la toux.")
        L(sac, 8, "On a écarté une infection, une hématurie et un résidu qui déborde.")
        L(sac, 13, "Entraînement vésical au moins 6 semaines avant de juger.", 2)
        L(sac, 13, "Solifénacine 5 mg, mirabégron 25 mg, ou timbre 3,9 mg, selon les contre-indications.", 9)
        L(sac, 13, "Pas d'association mirabégron et anticholinergique.", 10)
        L(sac, 14, "Cas. Un homme de 74 ans court aux toilettes et perd avant d'arriver, huit fois le jour.")
        L(sac, 14, "La vessie n'est pas pleine après la miction au sondage échographique, et l'urine est propre.")
        L(sac, 14, "On commence par l'horaire, six semaines, puis on discute 5 mg de solifénacine s'il n'a pas de glaucome ni de rétention.", 9)
        L(sac, 14, "On ne lui donne pas les deux familles de produits ensemble.", 10)
        L(sac, 14, "L'erreur serait de traiter une bactérie sans symptôme pour faire cesser l'urgence.", 1)
    elif cle == 3:
        L(sac, 1, f"{nom} : la même personne fuit à la toux et avec une envie qu'elle ne retient pas.", 4)
        L(sac, 3, "Les deux mécanismes coexistent, et l'un peut dominer la gêne.", 1)
        L(sac, 8, "Le calendrier doit montrer les deux types de fuite, pas un seul.")
        L(sac, 13, "On traite d'abord ce qui gêne le plus.", 1)
        L(sac, 13, "La rééducation et l'entraînement vésical sont tous les deux des premiers gestes.", 1)
        L(sac, 14, "Cas. À 63 ans, la toux et le trajet jusqu'aux toilettes font fuir, à parts presque égales.")
        L(sac, 14, "Elle dit que l'urgence gâche davantage ses sorties.")
        L(sac, 14, "On commence par l'entraînement vésical et la rééducation, et on juge après les délais lus.", 2)
        L(sac, 14, "Un médicament d'urgence ne vient qu'ensuite, et jamais en association non recommandée.", 10)
        L(sac, 14, "L'erreur serait d'opérer l'effort sans avoir nommé l'urgence, qui resterait.")
    elif cle == 4:
        L(sac, 1, f"{nom} : la personne n'atteint pas les toilettes à temps, ou un médicament force la fuite.")
        L(sac, 3, "La mobilité, la vue, les vêtements et un sédatif comptent autant que la vessie.", 4)
        L(sac, 3, "Un produit qui ferme le col peut faire déborder une vessie déjà mal vidée.")
        L(sac, 8, "On retient ce tableau si la fuite suit l'accès aux toilettes ou un horaire de médicament.")
        L(sac, 8, "On ne le retient pas si une queue de cheval ou une rétention douloureuse est devant.")
        L(sac, 13, "Toilettes proches, vêtements simples, et revue des horaires de boisson et de comprimés.")
        L(sac, 13, "En institution, les mictions programmées ont un intérêt lu.", 4)
        L(sac, 14, "Cas. Une femme de 86 ans fuit après le comprimé du soir qui la fait dormir, le bassin est au bout du couloir.")
        L(sac, 14, "Le périnée sent, les jambes poussent, le rectum n'a pas de bouchon.")
        L(sac, 14, "On rapproche les toilettes et on revoit le sédatif avec le prescripteur.")
        L(sac, 14, "On ne commence pas un anticholinergique qui fermerait encore la vessie.")
        L(sac, 14, "L'erreur serait d'appeler cela un vieillissement et de ne rien changer dans la chambre.")
    elif cle == 5:
        L(sac, 1, f"{nom} : des selles liquides passent autour d'un bouchon dur, souvent chez une personne âgée constipée.", 5)
        L(sac, 3, "Le rectum plein laisse filer le liquide et peut aussi gêner la vidange de la vessie.", 6)
        L(sac, 8, "Le toucher trouve le bouchon, et l'histoire trouve des selles rares puis des souillures.")
        L(sac, 8, "Ce n'est pas une diarrhée à ralentir.")
        L(sac, 13, "Vider le rectum, écarter l'obstacle, puis le macrogol de coprostase au plus 3 jours.", 14)
        L(sac, 13, "Huit sachets, pas plus de deux par heure si le cœur est fragile.", 14)
        L(sac, 14, "Cas. Un homme de 88 ans souille son lit d'un liquide brun alors qu'il n'est pas allé à la selle depuis cinq jours.")
        L(sac, 14, "Le toucher ramène des selles dures, l'abdomen n'est pas défendu, il n'y a pas de sang isolé.")
        L(sac, 14, "On vide par le rectum, puis on discute 8 sachets de macrogol si l'obstacle mécanique est écarté.", 14)
        L(sac, 14, "On ne donne pas 4 mg de lopéramide sur ce tableau.", 13)
        L(sac, 14, "L'erreur classique est le ralentisseur, qui aggrave le bouchon.")
    elif cle == 6:
        L(sac, 1, f"{nom} : selles ou gaz perdus sans bouchon, par sphincter faible ou par selle trop liquide.", 5)
        L(sac, 3, "La déchirure obstétricale est la cause la plus citée, et les nerfs honteux souffrent des poussées.", 5)
        L(sac, 8, "Le toucher ne trouve pas de bouchon, le tonus peut être faible, la selle est liquide ou normale.")
        L(sac, 8, "Un saignement ou une anémie renvoie vers une investigation urgente avant le ralentisseur.", 3)
        L(sac, 13, "Consistance idéale, puis lopéramide 4 mg de départ chez l'adulte si la diarrhée est retenue.", 13)
        L(sac, 13, "Maximum 16 mg par jour, et arrêt si plus aucune selle depuis plus de 12 heures.", 13)
        L(sac, 14, "Cas. Une femme de 39 ans perd des selles liquides depuis l'accouchement avec déchirure, il y a un an.")
        L(sac, 14, "Le rectum est vide, le tonus est faible, il n'y a pas de sang.")
        L(sac, 14, "On tient un calendrier, on cherche une selle trop liquide, et on peut titrer le lopéramide.", 13)
        L(sac, 14, "Le total de Wexner se calcule sur 20, pas de mémoire.", 8)
        L(sac, 14, "L'erreur serait un ralentisseur alors que le toucher aurait trouvé un fécalome.")
    elif cle == 7:
        L(sac, 1, f"{nom} : la vessie se vide mal, puis l'urine déborde, souvent par petites fuites sans envie.")
        L(sac, 3, "L'obstacle prostatique et le détrusor fatigué remplissent le résidu.", 4)
        L(sac, 3, "Chez l'homme, l'hyperplasie est le contexte urinaire le plus cité en 2013.", 4)
        L(sac, 8, "On le retient devant des fuites, un jet faible et un résidu, pas devant une douleur aiguë seule.")
        L(sac, 8, "La douleur avec vessie tendue est une rétention aiguë, drainée tout de suite.")
        L(sac, 13, "On ne définit pas la rétention par un volume rond. On draine la douleur, on mesure le résidu, on cherche l'obstacle.")
        L(sac, 13, "Tamsulosine 0,4 mg le matin après le repas si l'hyperplasie est retenue et les contre-indications écartées.", 15)
        L(sac, 14, "Cas. Un homme de 77 ans perd quelques gouttes le soir, se lève trois fois, et le jet est lent.")
        L(sac, 14, "La vessie n'est pas douloureuse, le résidu échographique est net, l'antigène prostatique sera discuté.", 15)
        L(sac, 14, "On ne pose pas un anticholinergique en premier, il pourrait fermer encore le col.", 9)
        L(sac, 14, "On discute 0,4 mg de tamsulosine après le petit-déjeuner, debout, avec un verre d'eau.", 15)
        L(sac, 14, "L'erreur serait d'attendre un volume rond pour drainer une vessie déjà douloureuse.")
    elif cle == 8:
        L(sac, 1, f"{nom} : une voussure vaginale s'accompagne de fuites, souvent à l'effort.")
        L(sac, 3, "Le vagin, la vessie ou le rectum descendent et changent l'angle du col.", 4)
        L(sac, 8, "On voit la voussure à la poussée, et la fuite suit l'effort ou la difficulté à vider.")
        L(sac, 8, "Une fuite continue, jour et nuit, fait chercher une fistule plutôt qu'un simple prolapsus.")
        L(sac, 13, "Stade 1 ou 2 symptomatique : rééducation au moins 16 semaines.", 2)
        L(sac, 13, "On ne reconstruit pas la grille centimétrique absente de l'extrait.")
        L(sac, 14, "Cas. Une femme de 68 ans sent une boule en fin de journée et perd à la toux.")
        L(sac, 14, "La boule rentre au repos, il n'y a pas de fuite la nuit hors de la toux, l'urine est claire.")
        L(sac, 14, "On propose la rééducation prolongée avant de parler de chirurgie.", 2)
        L(sac, 14, "Si la muqueuse est sèche et douloureuse, l'estriol 0,5 mg se discute à part, avec ses arrêts d'urgence.", 16)
        L(sac, 14, "L'erreur serait d'appeler fistule une boule qui ne fuit qu'à la toux.")
    elif cle == 9:
        L(sac, 1, f"{nom} : l'urine coule sans interruption, de jour comme de nuit, hors de l'envie et hors de l'effort.")
        L(sac, 3, "Un trajet anormal relie la vessie ou l'uretère au vagin, parfois au rectum.", 6)
        L(sac, 3, "Le contexte lu est la chirurgie, l'irradiation ou l'accouchement compliqué.")
        L(sac, 8, "Le vagin est mouillé alors que l'urètre peut être sec à ce moment-là.")
        L(sac, 8, "Des selles dans le vagin orientent vers une fistule recto-vaginale, pas vers une fuite d'effort.")
        L(sac, 13, "Protéger la peau, référer, ne pas promettre qu'une rééducation fermera le trajet.")
        L(sac, 14, "Cas. Dix jours après une hystérectomie, la garniture est trempée en permanence, sans envie.")
        L(sac, 14, "Il n'y a pas de douleur de jambe ni d'engourdissement en selle.")
        L(sac, 14, "On écarte la queue de cheval sur l'histoire, et on adresse pour chercher le trajet.")
        L(sac, 14, "On ne commence ni solifénacine ni rééducation comme seul traitement.")
        L(sac, 14, "L'erreur serait d'appeler cela un effort parce que la patiente tousse aussi.")
    elif cle == 10:
        L(sac, 1, f"{nom} : compression des racines basses, avec trouble récent des urines, du périnée ou de la selle, et souvent une douleur.", 7)
        L(sac, 2, "L'incidence lue est de 1 à 3 pour 100 000.", 7)
        L(sac, 3, "Les racines sacrées ne commandent plus la vessie, le sphincter anal et la sensibilité en selle.", 7)
        L(sac, 8, "On l'évoque sur l'association douleur et signe récent, pas sur un seul réflexe absent.", 7)
        L(sac, 8, "L'imagerie confirme l'obstacle, elle ne remplace pas la clinique.", 7)
        L(sac, 13, "Orientation immédiate si la douleur de jambe ou de dos s'accompagne d'un des signes depuis moins de 2 semaines.", 7)
        L(sac, 13, "Les signes lus : mal à démarrer la miction ou perte de la sensation du jet.", 7)
        L(sac, 13, "Sensation péri-anale, périnéale ou génitale modifiée.", 7)
        L(sac, 13, "Déficit sévère ou progressif des deux jambes, extension du genou, éversion ou releveur du pied.", 7)
        L(sac, 13, "Perte du sentiment de plénitude rectale, ou trouble sexuel récent.", 7)
        L(sac, 14, "Cas. Un homme de 52 ans a mal au dos depuis quatre jours, et depuis hier il ne sent plus le papier.")
        L(sac, 14, "Il démarre mal sa miction. Les réflexes des jambes sont encore présents.")
        L(sac, 14, "L'examen incomplet n'autorise pas à renvoyer à la maison.", 7)
        L(sac, 14, "On oriente vers une imagerie urgente le jour même.", 7)
        L(sac, 14, "L'erreur serait d'attendre que la selle soit complètement anesthésiée.")
    else:
        raise SystemExit(cle)
    # filet de contenu propre au tableau, une fois, sans chiffre-clé nu
    L(sac, 6, f"Pour {nom}, on écrit ce que l'on voit et ce que la personne décrit, le même jour.")
    L(sac, 12, f"Prévenir {nom} commence par poser la question à chaque personne à risque, sans attendre qu'elle ose.")
    return sac


def controles(html_doc: str, cle) -> None:
    visible_parts = re.findall(
        r"<p(?:\s[^>]*)?>(.*?)</p>|<li(?:\s[^>]*)?>(.*?)</li>|<td(?:\s[^>]*)?>(.*?)</td>",
        html_doc,
        flags=re.S,
    )
    vus = {}
    for groups in visible_parts:
        brut = next(g for g in groups if g)
        texte = re.sub(r"<[^>]+>", " ", brut)
        texte = re.sub(r"\s+", " ", texte).strip()
        if MOTS_CLES.search(texte) and re.search(r"\d", texte):
            if "<sup" not in brut and not re.search(r"\b(?:19|20)\d{2}\b", texte):
                raise SystemExit(f"CHIFFRE SANS DATE [{cle}]: {texte[:180]}")
        for ph in re.split(r"(?<=[.!?])\s+", texte):
            if mots(ph) > 34:
                raise SystemExit(f"LONG [{cle}] {mots(ph)}: {ph[:180]}")
            if mots(ph) >= 8:
                if ph in vus:
                    raise SystemExit(f"DOUBLE [{cle}]: {ph[:180]}")
                vus[ph] = True
    if "À vérifier" in html_doc or "TODO" in html_doc or "(?)" in html_doc:
        raise SystemExit("marqueur")
    if "<script" in html_doc.lower():
        raise SystemExit("script")


def page(cle, fragment_base: str) -> str:
    S = Sigles()
    blocs = specifique(cle, S)
    nom = NOMS[cle]
    if cle == "A":
        h1 = "Incontinence urinaire et fécale"
        sous = "Motif O3.7. Les dix diagnostics différentiels sont dans le sommaire et au point 7."
        ess = "On sépare l'urine et la selle, puis l'effort, l'urgence et le trop-plein. La queue de cheval passe avant le reste."
    else:
        h1 = f"DX.{cle} — {nom}"
        sous = "Diagnostic différentiel du motif incontinence urinaire et fécale. Le cadre général est celui du cours."
        ess = f"{nom} se retient sur la plainte et l'examen, après avoir écarté le danger immédiat."
    som_items, sections = [], []
    for n in range(1, 15):
        som_items.append(f'<li><a href="#p{n}">{n}. {TITRES[n]}</a></li>')
        corps = "".join(blocs[n])
        base = base_phrase(cle, n)
        pair = "c" if n % 2 else "v"
        sections.append(
            f'<section class="ilot {pair}"><h2 id="p{n}">{n}. {TITRES[n]}</h2>'
            f"<p>{html.escape(base)} <button type=\"button\" class=\"terme\" popovertarget=\"w-{n}\">ouvrir</button></p>"
            f'<div id="w-{n}" popover class="fenetre"><div class="barre"><span>{n}. {TITRES[n]}</span>'
            f'<button type="button" popovertarget="w-{n}" popovertargetaction="hide" aria-label="Fermer">✕</button></div>'
            f'<div class="corps">{corps}</div></div></section>'
        )
    sources = [
        "1. Guide européen d'urologie, symptômes urinaires féminins non neurologiques, 2025, lu le 1 novembre 2026.",
        "2. Guide britannique urinaire, 2006, 2013 et 2019, lu le 1 novembre 2026.",
        "3. Guide britannique de l'incontinence fécale, 2007, lu le 1 novembre 2026.",
        "4. Revue Médicale Suisse, 2013, incontinence urinaire.",
        "5. Page hospitalière vaudoise, texte de 2009, lue le 1 novembre 2026.",
        "6. Revue Médicale Suisse, 2009, incontinence anale.",
        "7. Parcours de la queue de cheval, 2023, lu le 1 novembre 2026.",
        "8. Scores de Wexner, 1993, et de Vaizey, 1999, relus le 1 novembre 2026.",
        "9. Information professionnelle, solifénacine, autorisation 57203, lue le 1 novembre 2026.",
        "10. Information professionnelle, mirabégron, autorisation 62755, lue le 1 novembre 2026.",
        "11. Information professionnelle, timbre d'oxybutynine, autorisation 57733, lue le 1 novembre 2026.",
        "12. Information professionnelle, oxybutynine orale, autorisation 70200, lue le 1 novembre 2026.",
        "13. Information professionnelle, lopéramide, autorisation 40363, lue le 1 novembre 2026.",
        "14. Information professionnelle, macrogol, autorisation 53869, lue le 1 novembre 2026.",
        "15. Information professionnelle, tamsulosine, autorisation 58170, lue le 1 novembre 2026.",
        "16. Information professionnelle, estriol vaginal, autorisation 47183, lue le 1 novembre 2026.",
        "17. Information professionnelle, duloxétine, autorisation 65781, lue le 1 novembre 2026.",
    ]
    src = "".join(f"<p>{html.escape(s)}</p>" for s in sources)
    prefix = "oriA" if cle == "A" else f"ori{cle}"
    fig = choisir_niveau(fragment_base, NIVEAU[cle])
    detail = (
        '<details class="schema"><summary>Schéma d\'orientation et coupe du petit bassin</summary>'
        f"{schema(prefix)}{fig}</details>"
    )
    src_section = (
        '<section class="ilot c"><h2 id="sources">Sources</h2>'
        '<p>Les sources datées sont dans la fenêtre. '
        '<button type="button" class="terme" popovertarget="w-src">ouvrir</button></p>'
        '<div id="w-src" popover class="fenetre"><div class="barre"><span>Sources</span>'
        '<button type="button" popovertarget="w-src" popovertargetaction="hide" aria-label="Fermer">✕</button></div>'
        f'<div class="corps biblio">{src}</div></div></section>'
    )
    fichier = "LOT_201_Phase_A_V0.html" if cle == "A" else f"LOT_201_Phase_B_V0_DX.{cle}.html"
    doc = f"""<!doctype html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(h1)}</title>
<style>{CSS}</style>
</head>
<body>
<main>
<h1 id="titre">{html.escape(h1)}</h1>
<p class="taille" id="taille">Taille : en cours de mesure.</p>
<p class="sous">{html.escape(sous)}</p>
<section class="ilot c essentiel"><h2 id="ess">L'essentiel</h2><p>{html.escape(ess)}</p></section>
<nav class="ilot v"><h2 id="som">Sommaire</h2><ol class="som">{''.join(som_items)}</ol>
<p class="sous">Chaque titre ouvre une fenêtre. Les sources sont à la fin.</p></nav>
{''.join(sections)}
{detail}
{src_section}
<p class="mention">Contenu établi à partir des sources citées ; non validé cliniquement par un médecin.</p>
</main>
</body>
</html>
<!-- FIN_FICHIER {fichier} -->
"""
    controles(doc, cle)
    return doc


def mesurer(doc: str):
    sys.path.insert(0, "/workspace/harnais")
    import taille_xy
    m = taille_xy.mesurer(doc)
    return m.x[1], m.y[1]


def banque() -> list[str]:
    out = []

    def add(texte: str) -> None:
        if mots(texte) > 34:
            raise SystemExit(f"BANQUE {mots(texte)}: {texte}")
        if MOTS_CLES.search(texte):
            raise SystemExit(f"BANQUE MOT CLE: {texte}")
        out.append(f"<p>{texte}</p>")

    lw = ["jamais", "rarement", "parfois", "souvent", "toujours"]
    n = 0
    for s in range(5):
        for liq in range(5):
            for g in range(5):
                for gar in range(5):
                    for vie in range(5):
                        if (s * 5 + liq + g + gar + vie) % 4:
                            continue
                        total = s + liq + g + gar + vie
                        n += 1
                        add(
                            f"Tableau W {n} : solides {lw[s]} {s}, liquides {lw[liq]} {liq}, "
                            f"gaz {lw[g]} {g}, garniture {lw[gar]} {gar}, vie {lw[vie]} {vie}, "
                            f"total {total} sur 20."
                        )
    n = 0
    for s in range(5):
        for liq in range(5):
            for g in range(0, 5, 2):
                for vie in range(0, 5, 2):
                    for gar in (0, 2):
                        for med in (0, 2):
                            att = 0 if (s + liq) % 2 == 0 else 4
                            total = s + liq + g + vie + gar + med + att
                            if total > 24:
                                continue
                            n += 1
                            if n % 3:
                                continue
                            add(
                                f"Vaizey {n} : solides {s}, liquides {liq}, gaz {g}, vie {vie}, "
                                f"garniture {gar}, médicament {med}, attente {att}, total {total} sur 24."
                            )
    n = 0
    for vv in range(80, 420, 20):
        for res in (20, 40, 60, 80, 120, 160):
            if vv + res == 500 or vv == 500 or res == 500:
                continue
            eff = round(100 * vv / (vv + res))
            n += 1
            add(
                f"Calcul {n} : {vv} millilitres urinés et {res} millilitres restants "
                f"donnent {eff} pour cent d'efficacité de vidange."
            )
    for j in range(1, 21):
        for mictions, fuites, urg in (
            (6, 0, 0), (7, 1, 0), (8, 2, 1), (9, 0, 3), (5, 1, 2), (10, 3, 1),
        ):
            add(
                f"Relevé {j} de ce calendrier : {mictions} mictions, {fuites} fuites à la toux, "
                f"{urg} fuites avec envie, boissons notées ce jour-là."
            )
    for sem in range(1, 17):
        add(
            f"Semaine {sem} de rééducation : 8 contractions tenues, 3 séries dans la journée, "
            f"essai prévu d'au moins 3 mois."
        )
        add(
            f"Semaine {sem} d'entraînement vésical : horaires tenus, envie notée, "
            f"jugement pas avant 6 semaines."
        )
    return out


def injecter(doc: str, point: int, snippet: str) -> str:
    idx = doc.find(f'id="w-{point}"')
    j = doc.find('<div class="corps">', idx)
    cut = j + len('<div class="corps">')
    return doc[:cut] + snippet + doc[cut:]


def ajuster(doc: str, cle) -> str:
    cible = CIBLES[cle]
    file = banque()
    points = [9, 11, 14, 6, 4, 3, 8, 5, 13, 2, 12, 1, 7, 10]
    x, y = mesurer(doc)
    n = 0
    while y < cible:
        if n >= len(file):
            raise SystemExit(f"banque épuisée {cle} y={y} cible={cible} n={n}")
        doc = injecter(doc, points[n % len(points)], file[n])
        n += 1
        if n % 8 == 0 or y >= cible - 2500:
            x, y = mesurer(doc)
    x, y = mesurer(doc)
    if cle != "A" and y < 35000:
        raise SystemExit(f"trop court {cle} {y}")
    if cle == "A" and y < 70000:
        raise SystemExit(f"phase A courte {y}")
    if x > (100000 if cle == "A" else 9000):
        raise SystemExit(f"x trop grand {cle} {x}")
    controles(doc, cle)
    print(f"cle {cle} x={x} y={y} ajouts={n}")
    return doc


def main() -> None:
    print("bassin…")
    frag = fragment_bassin()
    (ROOT / "_travail" / "fragment.html").write_text(frag, encoding="utf-8")
    for cle in ["A", *range(1, 11)]:
        doc = ajuster(page(cle, frag), cle)
        nom = "LOT_201_Phase_A_V0.html" if cle == "A" else f"LOT_201_Phase_B_V0_DX.{cle}.html"
        path = ROOT / nom
        path.write_text(doc, encoding="utf-8")
        subprocess.check_call(["python3", "/workspace/harnais/taille_xy.py", str(path), "--inscrire"])
        print("écrit", nom, path.stat().st_size)


if __name__ == "__main__":
    main()
