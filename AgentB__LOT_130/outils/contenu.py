#!/usr/bin/env python3
"""Texte français du LOT_130. Chaque chiffre est cité vers preuves.jsonl."""
from __future__ import annotations
import html, re
from fabriquer import p, fen, table, cite, DX

_n = 0

def W(prefix: str, label: str, pid: str) -> tuple[str, str]:
    global _n
    _n += 1
    return fen(prefix, f"{prefix}-f{_n}", label, pid)

def h4(titre: str) -> str:
    return f'<h4 class="struct">{html.escape(titre)}</h4>\n'

def cell(texte: str, ids: list[str]) -> str:
    return texte + cite(ids)

def pack(morceaux: list[str], fenetres: list[str]) -> str:
    return "".join(morceaux) + "".join(fenetres)

def urgence(prefix: str, lignes: list[tuple[str, list[str]]]) -> str:
    fid = f"{prefix}-p11-urgence"
    from fabriquer import SN
    pas = "".join(f"<div class=\"pas\">{t}{cite(ids)}</div>" for t, ids in lignes)
    liens = []
    for _t, ids in lignes:
        for i in ids:
            if i in SN and i not in [x[0] for x in liens]:
                liens.append((i, SN[i]))
    src = " ".join(f'<a href="#sb-{i}">[S{n}]</a>' for i, n in liens)
    return (
        "<p>Dès lors, les gestes urgents commencent tout de suite, et le bilan complet vient ensuite.</p>\n"
        f"<details style='display:inline;' id=\"{fid}\"><summary>Urgence — conduite chronologique</summary>"
        f"<div class=\"corps\">{pas}"
        f"<div class=\"piege\">Piège d'examen : attendre une confirmation alors que l'organe ou la perfusion souffre déjà.</div>"
        f"<div class=\"src\">Sources {src}.</div>"
        f"</div></details>\n"
    )

def divergence(prefix: str) -> str:
    from fabriquer import cite as C
    return (
        "<details style='display:inline;' id=\"" + prefix + "-cibles\">"
        "<summary>cibles tensionnelles</summary><div class=\"corps\">"
        "<div class=\"meca\">D'abord, la fiche suisse et le texte européen ne fixent pas la même cible. "
        "Ensuite, le candidat cite les deux. Ainsi, il ne fond pas les textes en un seul seuil.</div>"
        "<div class=\"ex\">La fiche suisse maintient, pour la plupart, une cible sous 140/90 mmHg, "
        "sous 140/85 mmHg en cas de diabète ou de maladie rénale, et sous 150 mmHg "
        "dans l'hypertension systolique isolée du sujet âgé."
        f"{C(['SSHCIB'])}</div>"
        "<div class=\"ex\">Le texte européen vise 120 à 129 mmHg de systolique si cette cible est tolérée, "
        "et il l'assouplit après 85 ans, en cas de fragilité marquée, ou lorsque l'hypotension orthostatique est symptomatique."
        f"{C(['ESCCIBLE'])}</div>"
        "<div class=\"piege\">Piège d'examen : présenter les deux cibles comme si elles étaient identiques.</div>"
        "<div class=\"src\">Sources <a href=\"#sb-SSHCIB\">[S"
        + str(__import__('fabriquer').SN['SSHCIB']) + "]</a> et <a href=\"#sb-ESCCIBLE\">[S"
        + str(__import__('fabriquer').SN['ESCCIBLE']) + "]</a>.</div>"
        "</div></details>\n"
    )

GLOSSAIRE = [
    ("ramipril", "AIPSHT"), ("spironolactone", "ESCPAD"), ("créatinine", "ESCLAB"),
    ("métanéphrines", "SSHMET"), ("polysomnographie", "ESCOSA"), ("lactate", "SSCLAC"),
    ("noradrénaline", "SSCNE"), ("nicardipine", "ISHMAP"), ("labétalol", "ISHMAP"),
    ("albumine", "ESCLAB"), ("doppler", "SSHRAS"), ("fond d'œil", "ESCFO"),
    ("sodium", "ESCSOD"), ("grossesse", "AIPSCI"), ("sacubitril", "AIPS36"),
    ("aliskiren", "AIPSAL"), ("sténose", "AIPSST"), ("apnées", "ESCOSA"),
    ("orthostatique", "ESCOH"), ("phéochromocytome", "ESCPHE"), ("aldostérone", "SSHALD"),
    ("cristalloïde", "SSCVOL"), ("pression moyenne", "SSCMAP"), ("thrombolyse", "ESCSTR"),
    ("prééclampsie", "ESCPRE"), ("manchette", "SSHM1B"), ("automesure", "SSHM2"),
    ("résistante", "ESCRES"), ("nocturne", "ESCNUIT"), ("dysplasie", "ESCRVH"),
    ("cocaïne", "SSHT3"), ("anti-inflammatoires", "SSHT3"), ("kaliémie", "ISHK"),
]
_vus_glossaire: set[str] = set()

AMORCES = {
    1: "D'abord, le repère sain précède l'interprétation du chiffre anormal.",
    2: "Ensuite, les données suisses ouvrent l'épidémiologie, et l'Europe vient après.",
    3: "En effet, chaque lésion doit rester reliée à l'exploration puis au traitement.",
    4: "Ainsi, les hypothèses qui menacent la vie passent devant les causes fréquentes.",
    5: "Cependant, une question d'anamnèse ne vaut que si elle change la conduite.",
    6: "Par conséquent, l'examinateur décrit le geste normal avant le signe pathologique.",
    7: "Dès lors, chaque syndrome se déplie en signes fonctionnels et en signes physiques.",
    8: "En outre, le critère décisif se distingue de ce qui ne suffit pas.",
    9: "Toutefois, prescrire un examen suppose de savoir l'interpréter.",
    10: "De plus, chaque embranchement nomme le résultat qui fait choisir.",
    11: "En revanche, le but du traitement se formule avant la liste des moyens.",
    12: "Enfin, prévenir ne consiste pas à recopier le traitement déjà indiqué.",
    14: "Or, un piège d'examen se pose comme une question, puis se ferme par la réponse.",
}

def rendre(prefix: str, spec: list[list]) -> list[str]:
    """Chaque point est une liste de chaînes HTML ou de tuples (texte, ids, etiquette, preuve)."""
    global _vus_glossaire
    _vus_glossaire = set()
    out = []
    for numero, bloc in enumerate(spec, start=1):
        morceaux, fenetres = [], []
        if numero in AMORCES:
            morceaux.append(p(AMORCES[numero]))
        if numero == 11:
            fenetres.append(divergence(prefix))
        for item in bloc:
            if isinstance(item, str):
                morceaux.append(item if item.endswith("\n") else item + "\n")
                continue
            texte, ids, etiq, pid = item
            if texte.startswith("Posologie"):
                texte = "La " + texte[0].lower() + texte[1:].replace(" : À vérifier (AIPS).", " demeure à vérifier dans l'information professionnelle suisse.")
            if numero == 13:
                morceaux.append(p(texte, ids))
                continue
            if etiq and pid:
                _bouton, div = W(prefix, etiq, pid)
                morceaux.append(p(texte, ids))
                fenetres.append(div)
            else:
                morceaux.append(p(texte, ids))
        if numero != 13:
            brut = re.sub(r"<[^>]+>", " ", "".join(morceaux)).lower()
            from fabriquer import fenetre
            for terme, pid in GLOSSAIRE:
                if terme in _vus_glossaire or terme not in brut:
                    continue
                _vus_glossaire.add(terme)
                fenetres.append(fenetre(f"{prefix}-g-{len(_vus_glossaire)}", terme, pid))
        html_point = pack(morceaux, fenetres)
        if numero != 13 and "<details" not in html_point:
            from fabriquer import fenetre as F
            lien = re.search(r'href="#sb-([^"]+)"', html_point)
            pid = lien.group(1) if lien else "ESCDEF"
            html_point += F(f"{prefix}-p{numero}-notion", f"notion du point {numero}", pid)
        out.append(html_point)
    if len(out) != 14:
        raise SystemExit(f"{prefix}: {len(out)} points")
    return out
