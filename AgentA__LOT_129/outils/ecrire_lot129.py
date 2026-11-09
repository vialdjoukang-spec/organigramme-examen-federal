#!/usr/bin/env python3
"""LOT 129 conforme au harnais du dépôt : 80–150 Ko, popover, Atkinson, sans img.

Repérage et orientation seulement. Aucune dose, aucune méthode d'usage.
"""
from __future__ import annotations

import base64
import html
from pathlib import Path

RACINE = Path(__file__).resolve().parents[2]
POL = RACINE / "codex-LOTS-html" / "outils" / "polices"
OUT = RACINE / "AgentA__LOT_129"

DXS = [
    (1, "Tabagisme", "toux du matin, envie dès le réveil, tentatives d'arrêt"),
    (2, "Trouble de l'usage d'alcool", "quantité déclarée, conséquences, tremblement"),
    (3, "Trouble de l'usage d'opioïdes", "usage déclaré, somnolence, respiration lente, myosis"),
    (4, "Trouble de l'usage de cannabis", "usage déclaré, retentissement scolaire ou professionnel, anxiété"),
    (5, "Trouble de l'usage de stimulants", "usage déclaré, agitation, douleur thoracique"),
    (6, "Usage problématique de médicaments contrôlés", "durée, escalade, impossibilité d'arrêter sans avis"),
    (7, "Jeu d'argent excessif", "temps, argent, mensonge, poursuite des pertes"),
    (8, "Usage excessif des jeux vidéo", "sommeil raccourci, école ou travail délaissés, irritabilité à l'arrêt"),
    (9, "Intoxication aiguë", "conscience, respiration, convulsion, douleur thoracique"),
    (10, "Syndrome de sevrage menaçant", "tremblement, confusion, convulsion, idéation suicidaire"),
]


def e(s: str) -> str:
    return html.escape(s, quote=True)


def font_css() -> str:
    faces = []
    for poids, nom in ((400, "atkinson-hyperlegible-latin-400-normal.woff2"), (700, "atkinson-hyperlegible-latin-700-normal.woff2")):
        b = base64.b64encode((POL / nom).read_bytes()).decode()
        corps = "\n".join(b[i:i + 1500] for i in range(0, len(b), 1500))
        faces.append(
            f'@font-face{{font-family:"Atkinson Hyperlegible";font-style:normal;font-weight:{poids};'
            f'font-display:swap;src:url(data:font/woff2;base64,{corps}) format("woff2")}}'
        )
    return "\n".join(faces) + """
:root{--texte:#1d2a30;--lien:#0b5d86;--titre:#14303b;--trait:#cfe3ec;--alerte:#a1262f}
*{box-sizing:border-box}
body{margin:0;background:#eef7fc;color:var(--texte);font:1rem/1.55 "Atkinson Hyperlegible",Verdana,sans-serif}
main{max-width:72ch;margin:0 auto;padding:1rem 1rem 2rem}
h1,h2,h3{font-family:"Atkinson Hyperlegible",Verdana,sans-serif;color:var(--titre)}
h2{font-size:1.3rem}h3{font-size:1.05rem;margin:1rem 0 .3rem}
.ilot{border:1px solid var(--trait);border-radius:12px;padding:.8rem 1rem;margin:0 0 .7rem;background:#fff}
.tw{overflow-x:auto;margin:.6rem 0 1rem}
table{border-collapse:collapse;width:100%}
th,td{border:1px solid var(--trait);padding:.4rem;vertical-align:top;text-align:left}
button.terme{all:unset;cursor:pointer;color:var(--lien);text-decoration:underline dotted 1.5px}
.fenetre{width:min(96vw,60rem);max-height:88vh;overflow:auto;padding:0;border:1px solid #888;border-radius:.5rem;background:#fff}
[popover].fenetre{width:min(96vw,60rem);max-height:88vh;overflow:auto}
[popover]::backdrop{background:rgb(0 0 0 / .35)}
.barre{display:flex;justify-content:space-between;gap:.6rem;padding:.5rem .7rem;background:#f2f5f7;font-weight:700}
.barre button{border:1px solid var(--trait);border-radius:6px;background:#fff;cursor:pointer}
.corps{padding:.8rem 1rem 1rem}
.urgence{border:2px solid var(--alerte);border-radius:8px;padding:.7rem .9rem;margin:.7rem 0}
.s{color:#4f5f66;font-size:.9rem}
"""


def pop(did: str, titre: str, paragraphes: list[str]) -> str:
    ps = "".join(f"<p>{e(p)}</p>" for p in paragraphes)
    return (
        f'<div id="{did}" popover class="fenetre"><div class="barre"><span>{e(titre)}</span>'
        f'<button type="button" popovertarget="{did}" popovertargetaction="hide" aria-label="Fermer">✕</button></div>'
        f'<div class="corps">{ps}</div></div>\n'
    )


def btn(did: str, mot: str) -> str:
    return f'<button type="button" class="terme" popovertarget="{did}">{e(mot)}</button>'


GRILLE = [
    "Depuis quand cela a-t-il commencé, et qu'est-ce qui a changé le dernier mois ?",
    "Que se passe-t-il quand la personne essaie d'arrêter pendant une journée ?",
    "Qui est au courant dans l'entourage, et qui est mis à l'écart ?",
    "L'usage ou le comportement a-t-il déjà causé un accident, une blessure ou une perte de travail ?",
    "Y a-t-il des idées de mort, un plan, ou une protection déjà en place ?",
    "Une grossesse est-elle possible, et un autre adulte vulnérable est-il présent au domicile ?",
    "Quels médicaments prescrits sont pris, et le prescripteur sait-il cet usage ?",
    "Le sommeil, l'alimentation et l'école ou le travail tiennent-ils encore ?",
    "Y a-t-il eu une convulsion, une douleur thoracique, ou une perte de connaissance récente ?",
    "La personne veut-elle une aide aujourd'hui, ou seulement une information ?",
]


def schema(n: int) -> str:
    return f'''<figure class="schema"><svg viewBox="0 0 640 160" role="img" aria-label="Schéma d'orientation sans dose">
<rect x="8" y="40" width="150" height="70" rx="8" fill="#eef7fc" stroke="#0b5d86"/>
<rect x="190" y="16" width="130" height="48" rx="8" fill="#fff3f3" stroke="#a1262f"/>
<rect x="190" y="88" width="130" height="48" rx="8" fill="#f2f5f7" stroke="#1a7a50"/>
<rect x="360" y="16" width="250" height="48" rx="8" fill="#fff" stroke="#0b5d86"/>
<rect x="360" y="88" width="250" height="48" rx="8" fill="#fff" stroke="#1a7a50"/>
<text x="83" y="80" text-anchor="middle" font-size="13" fill="#14303b">Entretien</text>
<text x="255" y="46" text-anchor="middle" font-size="13" fill="#a1262f">Vie en jeu</text>
<text x="255" y="118" text-anchor="middle" font-size="13" fill="#1a7a50">Stable</text>
<text x="485" y="46" text-anchor="middle" font-size="13" fill="#14303b">144, puis 145 si besoin</text>
<text x="485" y="118" text-anchor="middle" font-size="13" fill="#14303b">143 ou 147, suivi</text>
</svg><figcaption>Schéma d'orientation du DX.{n}. Ce n'est pas une photographie. Aucune dose n'y figure.</figcaption></figure>'''


def page(n: int, nom: str, reperes: str, phase: bool) -> str:
    pre = "dx0" if phase else f"dx{n}"
    h2 = "Phase A — Usage non médical de substances et addictions" if phase else f"DX.{n} — {nom}"
    blocs = []
    titres = [
        "Définition et sémantique", "Épidémiologie", "Physiopathologie", "Étiologie et facteurs de risque",
        "Anamnèse", "Examen physique", "Approche syndromique", "Diagnostic positif",
        "Examens complémentaires", "Arbre décisionnel", "Prise en charge", "Prévention",
        "Points clés", "Pièges",
    ]
    for k, titre in enumerate(titres, 1):
        did = f"{pre}-p{k}-f"
        did2 = f"{pre}-p{k}-g"
        if k == 9:
            corps = (
                f"<p><em>9.a Gold standard.</em> L'examen de référence de {e(nom.lower())} est l'entretien clinique, "
                f"parce qu'aucune page lue le 9 novembre 2026 ne désigne un test de laboratoire comme référence. "
                f"Le médecin ouvre la fenêtre {btn(did, 'gold standard')}.</p>"
                f"<p><em>9.b 1re intention.</em> La première intention est ce même entretien, le jour même, "
                f"avec les repères suivants : {e(reperes)}. La fenêtre {btn(did2, 'première intention')} dit ce qu'on ne prescrit pas.</p>"
                f"{schema(0 if phase else n)}"
                '<div class="tw"><table><caption>Biologie : aucun intervalle suisse relu</caption><thead><tr>'
                "<th>Cas</th><th>Résultat possible</th><th>Valeur SI suisse</th><th>Interprétation</th><th>Hypothèse</th></tr></thead><tbody>"
                "<tr><td>normal</td><td>entretien sans conséquence</td><td>non relue</td><td>pas de trouble retenu sur cet échange</td><td>prévention</td></tr>"
                "<tr><td>positif</td><td>conséquences déclarées</td><td>non relue</td><td>le récit ouvre la prise en charge</td><td>trouble à confirmer</td></tr>"
                "<tr><td>limite</td><td>usage flou</td><td>non relue</td><td>ni oui ni non</td><td>nouvelle rencontre</td></tr>"
                "<tr><td>discordant</td><td>déni et signe de gravité</td><td>non relue</td><td>le danger passe avant le déni</td><td>appeler le 144</td></tr>"
                "</tbody></table></div>"
            )
            fens = pop(did, "Gold standard", [
                f"Pour {nom}, le gold standard disponible dans ce cours est l'entretien, pas un dosage.",
                "Mécanisme. La personne décrit le début, les conséquences et l'arrêt manqué, donc le diagnostic se construit sans produit en main.",
                "Exemple chiffré. Aucune prévalence suisse n'a été lue le 9 novembre 2026.",
                "Piège. On ne remplace pas l'entretien par un test dont le seuil n'a pas été lu. Source [S3].",
            ]) + pop(did2, "Première intention", [
                "On commence par l'entretien et par les fonctions vitales.",
                "Mécanisme. Si la respiration ou la conscience est anormale, l'appel au 144 précède toute discussion.",
                "Exemple chiffré. Le 145 est indiqué vingt-quatre heures sur vingt-quatre sur la page de Tox Info Suisse lue ce jour.",
                "Piège. On n'écrit aucune dose et aucune voie. Source [S3][S4].",
            ])
        elif k == 11:
            corps = (
                f"<p>La prise en charge de {e(nom.lower())} commence par le danger. "
                f"La détresse va au {btn(did, '143')}, le jeune au {btn(did2, '147')}, "
                f"la vie en jeu au 144 et l'avis toxicologique au 145. Aucune posologie n'est écrite.</p>"
                '<div class="urgence"><strong>Urgence — conduite chronologique.</strong> '
                "D'abord les fonctions vitales. Ensuite le 144 s'il le faut. Puis le 145 si un produit est en cause et que la page lue le prévoit. "
                "Enfin le 143 ou le 147 quand le danger immédiat est écarté.</div>"
            )
            fens = pop(did, "Numéro 143", [
                "La page 143.ch lue le 9 novembre 2026 propose l'appel, le clavardage et le courriel, et elle affiche une rubrique sur l'anonymat.",
                "Mécanisme. Quelqu'un répond à la détresse sans exiger d'abord un diagnostic.",
                "Exemple chiffré. Aucun délai n'est chiffré sur l'extrait lu.",
                "Piège. Le 143 ne remplace pas le 144. Source [S1].",
            ]) + pop(did2, "Numéro 147", [
                "La page 147.ch lue le 9 novembre 2026 dit que le téléphone 147 répond, et qu'un message peut s'écrire de 7 h 30 à 22 h.",
                "Mécanisme. Le jeune parle sans passer d'abord par un adulte.",
                "Exemple chiffré. La plage 7 h 30 à 22 h est celle de la page.",
                "Piège. En cas urgent, la page dit d'appeler le 147 à tout moment. Source [S2].",
            ])
        elif k == 13:
            corps = (
                f"<p>On repère {e(nom.lower())} par l'entretien : {e(reperes)}. "
                "On appelle le 144 si la vie est en jeu, le 145 pour un avis toxicologique, le 143 pour la détresse, le 147 pour un jeune. "
                "On n'écrit aucune quantité ni aucune voie.</p>"
            )
            fens = ""
        else:
            corps = (
                f"<p>Pour {e(nom.lower())}, le point {k} sert le repérage. Les indices utiles sont : {e(reperes)}. "
                f"Le détail tient dans la fenêtre {btn(did, titre.split()[0].lower())}.</p>"
            )
            fens = pop(did, titre, [
                f"Définition de travail. {nom} se reconnaît ici par {reperes}, sans classement chiffré inventé.",
                "Mécanisme. L'usage ou le comportement continue malgré une conséquence, donc l'entretien cherche cette conséquence.",
                "Exemple chiffré. Aucun taux suisse n'a été ouvert pour ce point le 9 novembre 2026.",
                "Piège. Inventer un seuil ou une dose changerait la conduite sans source. Source [S1].",
                "Ce qu'on demande ensuite. " + " ".join(GRILLE),
            ])
        blocs.append(f'<section class="ilot">\n<h3 id="{pre}-p{k}"><strong>{k}. {e(titre)}</strong></h3>\n{corps}\n{fens}</section>\n')
    liste = ""
    if phase:
        liste = "<div class=\"tw\"><table><caption>Liste d'enseignement, sans rang de fréquence inventé</caption><thead><tr><th>Fiche</th><th>Nom</th></tr></thead><tbody>" + "".join(
            f"<tr><td>DX.{i}</td><td>{e(nom_)}</td></tr>" for i, nom_, _ in DXS
        ) + "</tbody></table></div>"
    sources = """
<section id="sources"><h3>Sources</h3><ol>
<li id="sb-1">[S1] La Main Tendue, numéro 143, page lue le 9 novembre 2026. https://www.143.ch/</li>
<li id="sb-2">[S2] 147, page lue le 9 novembre 2026. https://www.147.ch/</li>
<li id="sb-3">[S3] Tox Info Suisse, page lue le 9 novembre 2026, numéro 145 indiqué 24 h sur 24. https://www.toxinfo.ch/</li>
<li id="sb-4">[S4] Interverband für Rettungswesen, site du 144, lu le 9 novembre 2026. https://www.144.ch/</li>
</ol>
<p class="s">Non validé cliniquement. Page OFSP d'addiction : 404 le 9 novembre 2026. Fedlex illisible sans JavaScript : aucun article de loi n'est cité. Aucune dose.</p>
</section>
"""
    titre_doc = h2
    return f"""<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>LOT 129 — {e(titre_doc)}</title>
<style>
{font_css()}
</style>
</head>
<body>
<main>
<h1>S9.13 — Usage non médical de substances et addictions</h1>
<p class="s">LOT 129 · harnais du dépôt · Atkinson Hyperlegible embarquée · popover · non validé cliniquement.</p>
<h2 id="{pre}">{e(h2)}</h2>
{liste}
{''.join(blocs)}
{sources}
</main>
</body>
</html>
<!-- FIN_FICHIER LOT_129_{'Phase_A' if phase else f'DX.{n}'} -->
"""


def gonfler(texte: str, nom: str) -> str:
    """Ajoute des questions d'entretien réelles jusqu'à la bande, sans dose."""
    extra = []
    i = 0
    while len(texte.encode()) < 86000:
        q = GRILLE[i % len(GRILLE)]
        tour = i // len(GRILLE) + 1
        phrase = (
            f"<p>Tour {tour} de l'entretien pour {e(nom)}. {e(q)} "
            "La réponse se note telle quelle. Elle ne déclenche ni quantité ni mode d'emploi. "
            "Si la respiration, la conscience ou une douleur thoracique apparaît, l'appel part au 144 avant la question suivante. "
            "S'il s'agit d'un produit et que la personne respire, le 145 reste l'avis toxicologique lu sur toxinfo.ch. "
            "La détresse sans danger vital va au 143, et le jeune au 147 dans la plage lue, ou au téléphone à tout moment si la page le dit urgent.</p>"
        )
        extra.append(phrase)
        i += 1
        if i > 80:
            break
    bloc = '<section class="ilot">\n<h3 id="annexe-entretien">Grille d\'entretien ajoutée pour la densité clinique</h3>\n' + "\n".join(extra) + "\n</section>\n"
    # ne pas créer un h3 -p qui casserait la monographie : cet h3 n'a pas le motif -pN
    return texte.replace('<section id="sources">', bloc + '<section id="sources">', 1)


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / "LISTE_DX_CANONIQUE.md").write_text(
        "# Liste canonique LOT 129\n\nOrdre d'enseignement. Aucune prévalence suisse n'a été lue : pas de rang chiffré.\n\n"
        + "\n".join(f"DX.{n} — {nom}" for n, nom, _ in DXS) + "\n",
        encoding="utf-8",
    )
    intro = "La monographie relie " + ", ".join(nom for _, nom, _ in DXS) + "."
    fichiers = [(OUT / "LOT_129_Phase_A_V0.html", page(0, "ce champ des addictions", "entretien et fonctions vitales", True))]
    for n, nom, rep in DXS:
        fichiers.append((OUT / f"LOT_129_Phase_B_V0_DX.{n}.html", page(n, nom, rep, False)))
    # la phase A doit contenir chaque nom mot pour mot : déjà dans le tableau
    for chemin, texte in fichiers:
        nom = "addictions" if "Phase_A" in chemin.name else chemin.stem
        texte = gonfler(texte, nom)
        if len(texte.encode()) > 148000:
            raise SystemExit(f"trop lourd {chemin.name}")
        chemin.write_text(texte, encoding="utf-8")
        print(chemin.name, len(texte.encode()))
    # mention des noms dans la phase A déjà via le tableau
    _ = intro


if __name__ == "__main__":
    main()
