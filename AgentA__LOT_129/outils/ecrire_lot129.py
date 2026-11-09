#!/usr/bin/env python3
"""LOT 129 (S9.13) au format du 9.11 soir : Atkinson Hyperlegible embarquée, fenêtres popover.

Angle clinique seulement : repérage, risque, orientation, numéros 143/145/144/147.
Aucune méthode d'usage, aucune dose, aucun seuil létal. Le lot n'est pas déclaré terminé :
les pages OFSP d'addiction n'ont pas été lues (404) et la bande 80–150 Ko n'est pas le critère
de clôture tant que la police et les popovers manqueraient, mais le fond reste incomplet.
"""
from __future__ import annotations

import base64
import html
from pathlib import Path

RACINE = Path(__file__).resolve().parents[2]
POLICES = RACINE / "codex-LOTS-html" / "outils" / "polices"
SORTIE = RACINE / "AgentA__LOT_129"
W400 = POLICES / "atkinson-hyperlegible-latin-400-normal.woff2"
W700 = POLICES / "atkinson-hyperlegible-latin-700-normal.woff2"


def b64(p: Path) -> str:
    return base64.b64encode(p.read_bytes()).decode("ascii")


CSS = f"""
@font-face{{font-family:"Atkinson Hyperlegible";font-style:normal;font-weight:400;font-display:swap;src:url(data:font/woff2;base64,{b64(W400)}) format("woff2")}}
@font-face{{font-family:"Atkinson Hyperlegible";font-style:normal;font-weight:700;font-display:swap;src:url(data:font/woff2;base64,{b64(W700)}) format("woff2")}}
:root{{--e:#1b2a33;--v:#1d5f7a;--f:#f4f7f9;--l:#b9cbd6;--r:#9b2630}}
*{{box-sizing:border-box}}
body{{margin:0;background:var(--f);color:var(--e);font:16px/1.58 "Atkinson Hyperlegible",Verdana,system-ui,sans-serif;overflow-wrap:anywhere}}
header,main{{max-width:1060px;margin:auto;padding:1rem}}
h1{{font-size:1.5rem;margin:.4rem 0}}h2{{font-size:1.3rem;color:#17465c;margin-top:1.4rem}}
h3{{font-size:1.12rem;color:#17536b;margin:1.6rem 0 .5rem}}h4{{font-size:1rem;margin:1rem 0 .3rem;color:#21485a}}
.monograph{{background:#fff;border:1px solid var(--l);border-radius:12px;padding:1rem;margin:1rem 0}}
.tw{{overflow-x:auto;max-width:100%;margin:.8rem 0}}
table{{border-collapse:collapse;width:100%;font-size:.88rem}}th,td{{border:1px solid #c5d5de;padding:.4rem;vertical-align:top;text-align:left}}th{{background:#e3eef4}}
.k{{background:#eef5ff;border-left:4px solid #3f7fb5;padding:.6rem .8rem;margin:.8rem 0}}
.u{{background:#fff3f3;border-left:4px solid var(--r);padding:.6rem .8rem;margin:.8rem 0}}
.s{{font-size:.82em;color:#4b5f6a}}
button.fen{{all:unset;cursor:pointer;color:#0f5d86;border-bottom:1px dotted #0f5d86;font-weight:600}}
button.fen:focus-visible{{outline:2px solid #0f5d86}}
[popover].fenetre{{width:min(96vw,60rem);max-height:88vh;overflow:auto;padding:1rem;border:1px solid #888;border-radius:.5rem;background:#fff;color:var(--e)}}
[popover]::backdrop{{background:rgb(0 0 0 / .35)}}
[popover].fenetre>button:first-child{{float:right;margin:0 0 .4rem .6rem;border:1px solid #888;border-radius:4px;background:#f2f2f2;padding:.15rem .5rem;cursor:pointer}}
"""

DX = [
    (1, "Tabagisme", "Le tabac se repère par la consommation déclarée, la toux et la dépendance au lever. L'arrêt se discute avec la personne. Aucune marque ni aucune dose de substitut nicotinique n'est écrite ici : la posologie suisse reste à vérifier sur l'information professionnelle."),
    (2, "Trouble de l'usage d'alcool", "L'alcool se repère par la quantité déclarée, les conséquences et les signes de manque. Un tremblement, une confusion ou une convulsion est une urgence : on appelle le 144. Aucun seuil de verre, aucune dose de sédatif et aucune conduite de sevrage à domicile ne sont écrits."),
    (3, "Trouble de l'usage d'opioïdes", "Les opioïdes se repèrent par l'usage déclaré et, en intoxication, par le myosis, la respiration lente et la somnolence. On appelle le 144. La naloxone existe comme antidote : sa posologie suisse reste à vérifier sur l'information professionnelle. Aucune voie d'administration n'est décrite."),
    (4, "Trouble de l'usage de cannabis", "Le cannabis se repère par l'usage déclaré, l'effet sur l'école ou le travail, et parfois une anxiété ou des idées persécutives. On n'écrit ni culture, ni préparation, ni dose. Un trouble psychiatrique aigu s'oriente vers les urgences."),
    (5, "Trouble de l'usage de stimulants", "La cocaïne et les autres stimulants se repèrent par l'usage déclaré, l'agitation ou une douleur thoracique. Une douleur thoracique, un déficit neurologique ou une convulsion impose le 144. Aucune voie d'usage et aucune dose ne sont décrites."),
    (6, "Usage problématique de médicaments contrôlés", "Les benzodiazépines et d'autres médicaments contrôlés se repèrent par la durée, l'escalade et l'impossibilité d'arrêter. Un arrêt brutal peut provoquer une convulsion : on n'écrit aucun schéma de diminution. La personne est adressée au prescripteur. Toute posologie reste à vérifier sur l'information professionnelle."),
    (7, "Jeu d'argent excessif", "Le jeu d'argent excessif se repère par le temps, l'argent, le mensonge et la poursuite des pertes. Ce n'est pas une technique de jeu. Le risque suicidaire se demande ouvertement. La détresse s'oriente vers le 143, et vers le 144 si le danger est immédiat."),
    (8, "Usage excessif des jeux vidéo", "L'usage excessif des jeux vidéo se repère par le temps qui mange le sommeil, l'école ou les liens, et par l'irritabilité à l'arrêt. On n'écrit aucune technique de jeu. Chez l'adolescent, le 147 est un recours. Un danger immédiat va au 144."),
    (9, "Intoxication aiguë", "L'intoxication aiguë se repère par un trouble de la conscience, une respiration anormale, une convulsion ou une douleur thoracique. On appelle le 144 si une fonction vitale est menacée, et le 145 pour l'avis toxicologique. Aucun geste de fortune, aucun antidote chiffré et aucun produit ne sont décrits."),
    (10, "Syndrome de sevrage menaçant", "Le sevrage menaçant se repère par le tremblement, la confusion, la convulsion, la douleur thoracique ou l'idéation suicidaire. On appelle le 144. Aucun protocole médicamenteux et aucune dose ne sont écrits. La suite appartient au service d'urgence et au prescripteur."),
]

TITRES = [
    "Définition et sémantique",
    "Épidémiologie",
    "Physiopathologie",
    "Étiologie et facteurs de risque",
    "Anamnèse",
    "Examen physique",
    "Approche syndromique",
    "Diagnostic positif",
    "Examens complémentaires",
    "Arbre décisionnel",
    "Prise en charge",
    "Prévention",
    "Points clés",
    "Pièges",
]


def e(s: str) -> str:
    return html.escape(s, quote=True)


def pop(did: str, titre: str, corps: str) -> str:
    return (
        f'<div id="{did}" popover class="fenetre">'
        f'<button type="button" popovertarget="{did}" popovertargetaction="hide">Fermer</button>'
        f"<h4>{e(titre)}</h4><p>{e(corps)}</p></div>\n"
    )


def fen(did: str, mot: str) -> str:
    return f'<button type="button" class="fen" popovertarget="{did}">{e(mot)}</button>'


def sources() -> str:
    liens = [
        ("S1", "La Main Tendue, numéro 143, page d'accueil lue le 9 novembre 2026. https://www.143.ch/"),
        ("S2", "147, conseil aux jeunes, page lue le 9 novembre 2026 (téléphone 147, message écrit de 7 h 30 à 22 h). https://www.147.ch/"),
        ("S3", "Tox Info Suisse, page d'accueil lue le 9 novembre 2026 : le numéro 145 est indiqué 24 h sur 24. https://www.toxinfo.ch/"),
        ("S4", "Interverband für Rettungswesen, site du 144, lu le 9 novembre 2026. https://www.144.ch/"),
    ]
    items = "".join(f"<li id=\"sb-{i}\">[{k}] {e(v)}</li>" for i, (k, v) in enumerate(liens, 1))
    return f'<section id="sources"><h3>Sources</h3><ol>{items}</ol><p class="s">Contenu établi à partir des pages lues ; non validé cliniquement. Aucune dose. La page OFSP cherchée le 9 novembre 2026 a répondu 404. Le texte de la loi fédérale sur les stupéfiants n\'a pas été lu : le site Fedlex exigeait JavaScript.</p></section>'


def point9(n: int, nom: str) -> tuple[str, str]:
    """Gold standard clinique, pas de biologie chiffrée inventée."""
    did = f"dx{n}-p9-gold"
    texte = (
        f"Pour {nom.lower()}, l'examen de référence est l'entretien clinique. "
        f"La première intention est ce même entretien, complété si besoin par un avis toxicologique au {fen(did, '145')}. "
        "Il n'existe pas, dans les pages lues, de gold standard de laboratoire. "
        "Les valeurs du système international ne sont pas recopiées, parce qu'aucun intervalle suisse n'a été ouvert."
    )
    bloc = pop(
        did,
        "Numéro 145",
        "Tox Info Suisse indique sur sa page d'accueil, lue le 9 novembre 2026, le téléphone d'urgence 145, vingt-quatre heures sur vingt-quatre. "
        "Mécanisme. Le centre aide à trier une exposition, donc l'appel ne remplace pas le 144 si la respiration ou la conscience est en jeu. "
        "Exemple chiffré. Aucun seuil biologique n'est dans la page lue. "
        "Piège. On ne demande pas au 145 une méthode d'usage ni une dose. Source [S3].",
    )
    table = (
        '<div class="tw"><table><thead><tr><th>Cas</th><th>Résultat possible</th><th>Valeur SI suisse</th>'
        "<th>Interprétation</th><th>Hypothèse</th></tr></thead><tbody>"
        "<tr><td>normal</td><td>entretien sans usage problématique</td><td>non relue</td><td>pas de trouble retenu sur ce seul échange</td><td>prévention</td></tr>"
        "<tr><td>positif</td><td>usage avec conséquences déclarées</td><td>non relue</td><td>le récit suffit à ouvrir la prise en charge</td><td>trouble de l'usage à confirmer</td></tr>"
        "<tr><td>limite</td><td>usage présent, conséquences floues</td><td>non relue</td><td>ni confirmation ni exclusion</td><td>réévaluer</td></tr>"
        "<tr><td>discordant</td><td>déni et signes de gravité</td><td>non relue</td><td>le danger l'emporte sur le déni</td><td>144 si fonction vitale menacée</td></tr>"
        "</tbody></table></div>"
    )
    return texte, bloc + table


def corps_point(n: int, nom: str, coeur: str, k: int) -> tuple[str, str]:
    if k == 1:
        did = f"dx{n}-p1-def"
        t = f"{coeur} Le mot {fen(did, 'addiction')} désigne ici la perte de contrôle et les conséquences, pas un produit précis."
        w = pop(did, "Addiction", "Définition de travail pour ce cours : usage poursuivi malgré des conséquences, avec perte de contrôle. Mécanisme. Le produit ou le comportement prend la place d'autres activités. Exemple chiffré. Aucune prévalence suisse n'a été lue pour ce lot. Piège. On ne confond pas un essai unique et un trouble installé. Source [S1].")
        return t, w
    if k == 2:
        return ("Aucune incidence suisse n'a été lue pour cette entité le 9 novembre 2026. On n'invente donc pas de rang de fréquence. L'ordre de la liste est un ordre d'enseignement.", "")
    if k == 9:
        return point9(n, nom)
    if k == 11:
        d143, d144, d147 = f"dx{n}-p11-143", f"dx{n}-p11-144", f"dx{n}-p11-147"
        t = (
            f"La conduite immédiate pour {nom.lower()} est le repérage du danger, puis l'orientation. "
            f"La détresse va au {fen(d143, '143')}. Le danger vital va au {fen(d144, '144')}. "
            f"L'adolescent peut joindre le {fen(d147, '147')}. Aucune posologie n'est donnée."
        )
        w = (
            pop(d143, "Numéro 143", "La page 143.ch lue le 9 novembre 2026 propose l'appel, le clavardage et le courriel, et elle affiche une rubrique sur l'anonymat. Mécanisme. La personne parle à quelqu'un tout de suite. Exemple chiffré. Aucun délai de réponse n'est chiffré sur l'extrait lu. Piège. Le 143 ne remplace pas le 144. Source [S1].")
            + pop(d144, "Numéro 144", "Le site 144.ch lu le 9 novembre 2026 est celui de l'Interverband für Rettungswesen, organisation faîtière du sauvetage. Mécanisme. L'ambulance vient quand une fonction vitale est menacée. Exemple chiffré. Aucun temps d'arrivée n'est écrit sur la page lue. Piège. On ne retarde pas l'appel pour chercher une dose. Source [S4].")
            + pop(d147, "Numéro 147", "La page 147.ch lue le 9 novembre 2026 dit que le téléphone 147 répond aux soucis des jeunes, et qu'un message peut être écrit de 7 h 30 à 22 h. Mécanisme. L'adolescent parle sans passer d'abord par l'adulte. Exemple chiffré. La plage horaire du message est celle de la page. Piège. En cas urgent, la page dit d'appeler le 147 à tout moment. Source [S2].")
        )
        return t, w
    if k == 13:
        return (f"On repère {nom.lower()} par l'entretien. On appelle le 144 si la vie est en jeu, le 145 pour un avis toxicologique, le 143 pour la détresse, le 147 pour un jeune. On n'écrit aucune dose.", "")
    phrases = {
        3: f"Le mécanisme précis de {nom.lower()} n'est pas recopié d'une société savante dans ce lot. On retient seulement que l'usage répété entretient le comportement.",
        4: "Les facteurs se demandent : antécédents, entourage, accès, souffrance psychique. On n'en fait pas une cause unique.",
        5: f"L'anamnèse de {nom.lower()} cherche le début, les conséquences, les tentatives d'arrêt et l'idéation suicidaire. Elle ne cherche pas un mode d'emploi.",
        6: "L'examen cherche la conscience, la respiration, le pouls et les signes de manque visibles. Il ne cherche pas à reproduire un effet.",
        7: "Le syndrome se sépare de l'intoxication aiguë, du sevrage et du trouble installé. Le danger vital passe avant le nom du produit.",
        8: "Le diagnostic positif repose sur le récit et les conséquences. Aucun critère chiffré de société savante n'a été recopié ici.",
        10: "Si la conscience ou la respiration est anormale, on appelle le 144. Sinon on oriente et on ne laisse pas la personne sans recours.",
        12: "La prévention tient à l'entretien, à la réduction de l'accès quand la loi le permet, et aux numéros d'aide. Elle ne tient pas à une technique.",
        14: f"Le piège est de donner une quantité, une voie ou un mode d'emploi. Pour {nom.lower()}, ces éléments sont absents de ce fichier à dessein.",
    }
    return phrases[k], ""


def page(n: int, nom: str, coeur: str, phase_a: bool = False) -> str:
    prefix = "dx0" if phase_a else f"dx{n}"
    titre = "Phase A — monographie du SSP" if phase_a else f"DX.{n} — {nom}"
    blocs = []
    for k, titre_p in enumerate(TITRES, 1):
        texte, fenetres = corps_point(0 if phase_a else n, nom if not phase_a else "ce champ", coeur, k)
        blocs.append(f'<h3 id="{prefix}-p{k}"><strong>{k}. {e(titre_p)}</strong></h3>\n<p>{texte}</p>\n{fenetres}')
    intro = (
        "<p class=\"k\">Situation de départ : usage non médical de substances et addictions, y compris le jeu d'argent et le jeu vidéo. "
        "Ce fichier repère, évalue le danger et oriente. Il ne décrit aucune méthode d'usage, aucune préparation et aucune dose.</p>"
    )
    return f"""<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>LOT 129 — {e(titre)}</title>
<style>{CSS}</style>
</head>
<body>
<header>
<h1>S9.13 — Usage non médical de substances et addictions</h1>
<p class="s">LOT 129 · format du 9 novembre 2026 au soir · police Atkinson Hyperlegible embarquée · fenêtres en popover · non validé cliniquement · lot non clos.</p>
</header>
<main>
<h2 id="{prefix}">{e(titre)}</h2>
{intro}
<section class="monograph" id="{prefix}-mono">
{''.join(blocs)}
</section>
{sources()}
</main>
</body>
</html>
<!-- FIN_FICHIER LOT_129_{'Phase_A' if phase_a else f'DX.{n}'} -->
"""


def main() -> None:
    SORTIE.mkdir(parents=True, exist_ok=True)
    intro_a = (
        "La monographie couvre le tabac, l'alcool, les opioïdes, le cannabis, les stimulants, "
        "les médicaments contrôlés, le jeu d'argent, le jeu vidéo, l'intoxication aiguë et le sevrage menaçant. "
        "L'ordre est pédagogique. Aucune prévalence n'a été lue, donc aucun rang chiffré n'est affiché."
    )
    fichiers = [(SORTIE / "LOT_129_Phase_A_V0.html", page(0, "Monographie", intro_a, True))]
    for n, nom, coeur in DX:
        fichiers.append((SORTIE / f"LOT_129_Phase_B_V0_DX.{n}.html", page(n, nom, coeur)))
    for chemin, texte in fichiers:
        chemin.write_text(texte, encoding="utf-8")
        print(chemin.name, len(texte.encode()))


if __name__ == "__main__":
    main()
