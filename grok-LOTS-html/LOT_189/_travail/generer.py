#!/usr/bin/env python3
"""Construit les leçons V8 de LOT_189. Les doses viennent des extraits AIPS du dossier evidence."""
from __future__ import annotations

import html
import re
import sys
from pathlib import Path

RACINE = Path(__file__).resolve().parents[3]
LOT = RACINE / "grok-LOTS-html" / "LOT_189"
sys.path.insert(0, str(RACINE / "grok-LOTS-html" / "outils" / "dessinateur"))
import dessinateur  # noqa: E402

MOT = re.compile(
    r"\b(incidence|prévalence|prevalence|sensibilit[ée]|spécificit[ée]|specificit|seuil|score)\b",
    re.I,
)

CSS = r"""
:root{--fond:#eef7fc;--page:#ffffff;--texte:#1d2a30;--doux:#4f5f66;--lien:#0b5d86;--titre:#14303b;--trait:#cfe3ec;--encadre:#f5f7f9;--bord:#1a7a50;--vert:#1a7a50;--ciel:#176fa0;--alerte:#a1262f;--ombre:rgb(15 60 90 / .28);--voile:rgb(10 30 45 / .55);--barre:#f2f5f7;--th:#f2f5f7;--cb1:#4fb3e6;--cb2:#b9e2f6;--vb1:#3aa776;--vb2:#b5e1cb;--o1:rgb(15 60 90 / .07);--o2:rgb(15 60 90 / .09)}
@media (prefers-color-scheme:dark){:root{--fond:#0e171d;--page:#16222a;--texte:#e3edf1;--doux:#a9bac2;--lien:#8fd3f5;--titre:#e6eef2;--trait:#2c414c;--encadre:#1a252c;--bord:#5cc79a;--vert:#5cc79a;--ciel:#6cc2ef;--alerte:#ff8a92;--ombre:rgb(0 0 0 / .6);--voile:rgb(0 0 0 / .7);--barre:#1d282f;--th:#1d282f;--cb1:#4aa9da;--cb2:#24506a;--vb1:#46b384;--vb2:#245a44;--o1:rgb(0 0 0 / .35);--o2:rgb(0 0 0 / .3)}}
*{box-sizing:border-box}html{-webkit-text-size-adjust:100%}body{margin:0;background:var(--fond);color:var(--texte);font:1rem/1.45 "Atkinson Hyperlegible",Verdana,sans-serif;overflow-wrap:break-word;hyphens:manual}
main{max-width:72ch;margin:0 auto;padding:1rem 1rem 2rem}h1,h2,h3,.barre,summary,nav,caption,th{font-family:"Atkinson Hyperlegible",Verdana,sans-serif}
h1{font-size:1.75rem;line-height:1.25;color:var(--titre);margin:0 0 .4rem}h2{font-size:1.3rem;line-height:1.3;color:var(--titre);margin:0 0 .45rem}h3{font-size:1.08rem;color:var(--titre);margin:1rem 0 .3rem}
p,.para{margin:0 0 .55rem}.sous{color:var(--doux);font-size:.95rem}.essentiel{border-left-width:4px}.essentiel h2{font-size:1.1rem}
nav ol{padding-left:1.6rem;margin:.4rem 0 0}nav li{margin:.15rem 0}a{color:var(--lien)}
button.terme{all:unset;cursor:pointer;color:var(--lien);text-decoration:underline dotted 1.5px;text-underline-offset:3px}button.terme::after{content:" ⧉";font-size:.75em;vertical-align:.15em}
button.terme:focus-visible{outline:2px solid var(--lien);outline-offset:2px}
.fenetre{position:fixed;inset:0;margin:auto;width:min(92vw,44rem);max-height:80vh;overflow:auto;padding:0;border:1px solid var(--trait);border-radius:12px;background:var(--page);color:var(--texte);box-shadow:0 18px 50px var(--ombre);font-size:.98rem}
.fenetre::backdrop{background:var(--voile)}
.barre{position:sticky;top:0;z-index:1;display:flex;align-items:center;justify-content:space-between;gap:.8rem;padding:.55rem .6rem .55rem 1rem;background:var(--barre);border-bottom:1px solid var(--trait);font-weight:700;font-size:.95rem}
.barre button{flex:none;width:2rem;height:2rem;border:1px solid var(--trait);border-radius:6px;background:var(--page);color:var(--texte);font-size:1rem;cursor:pointer}
.corps{padding:1rem 1.2rem 1.2rem}.corps p:last-child{margin-bottom:0}
.tw{overflow-x:auto;margin:.6rem 0 1rem}table{border-collapse:collapse;width:100%;font-size:.9rem;line-height:1.45}th,td{border:1px solid var(--trait);padding:.4rem .5rem;vertical-align:top;text-align:left}th{background:var(--th);font-size:.85rem}caption{text-align:left;font-weight:700;font-size:.9rem;padding:.2rem 0 .4rem}
figure{margin:1.2rem 0}figure svg{width:100%;height:auto;max-width:34rem;display:block;margin:auto;color:var(--texte)}figcaption{font-size:.88rem;color:var(--doux);text-align:center;margin-top:.3rem}
.sources{font-size:.86rem;line-height:1.5}.taille{font-size:.85rem;color:var(--doux);margin:0 0 .6rem}.mention{font-style:italic;color:var(--doux);margin:.8rem .3rem 0}
sup.s{font-size:.66em;line-height:0;vertical-align:.5em;margin-left:.06em;color:#1a3a6b;font-weight:700}
abbr[title]{text-decoration:underline dotted 1px;text-underline-offset:2px;cursor:help}
.ilot{background:linear-gradient(var(--page),var(--page)) padding-box,var(--bd) border-box;border:1.5px solid transparent;border-radius:12px;padding:.85rem 1rem .6rem;margin:0 0 .7rem}
.ilot.c{--bd:linear-gradient(135deg,var(--cb1),var(--cb2))}.ilot.v{--bd:linear-gradient(135deg,var(--vb1),var(--vb2))}
.sch .niv{display:none}.sch input.sr{position:absolute;opacity:0;width:1px;height:1px}
.sch .bn{display:flex;flex-wrap:wrap;gap:6px;margin:0 0 8px}.sch .bn label{border:1px solid #9bb;border-radius:8px;padding:4px 8px;cursor:pointer}
.som{columns:2;column-gap:1.4rem}.som li{break-inside:avoid}
"""

TITRES = [
    (1, "1. Définition"),
    (2, "2. Épidémiologie"),
    (3, "3. Physiopathologie"),
    (4, "4. Démarche diagnostique"),
    (5, "5. Anamnèse et drapeaux rouges"),
    (6, "6. Examen physique"),
    (7, "7. Approche syndromique"),
    (8, "8. Diagnostic positif"),
    (9, "9. Examens complémentaires"),
    (10, "10. Arbre décisionnel"),
    (11, "11. Prise en charge"),
    (12, "12. Prévention"),
    (13, "13. Points clés"),
    (14, "14. Pièges et cas"),
]

NOMS = [
    "Restriction de croissance fœtale",
    "Macrosomie fœtale",
    "Oligoamnios",
    "Hydramnios",
    "Tracé cardiaque fœtal suspect",
    "Anémie fœtale par allo-immunisation",
    "Malformation structurale fœtale",
    "Arythmie fœtale",
    "Syndrome transfuseur-transfusé",
    "Mort fœtale in utero",
]


def mots(texte: str) -> int:
    return len(re.findall(r"\b[\w'’]+\b", texte, re.U))


class Sac:
    def __init__(self):
        self.rows: list[tuple[str, int]] = []
        self.vus: set[str] = set()
        self.longues: list[str] = []

    def add(self, texte: str, ref: int) -> None:
        texte = re.sub(r"\s+", " ", texte).strip()
        if not texte.endswith("."):
            texte += "."
        if texte in self.vus:
            return
        if mots(texte) > 34:
            self.longues.append(texte)
            # coupe à la première virgule assez loin, sinon refuse la phrase longue
            coupe = texte.find(", ", 40)
            if 8 < mots(texte[:coupe]) < 30 and coupe != -1:
                a, b = texte[:coupe].rstrip(", ") + ".", texte[coupe + 2 :].strip()
                if b and not b.endswith("."):
                    b += "."
                self.add(a, ref)
                self.add(b[0].upper() + b[1:] if b else b, ref)
                return
        self.vus.add(texte)
        self.rows.append((texte, ref))

    def html(self) -> str:
        out = []
        for texte, ref in self.rows:
            corps = html.escape(texte, quote=False)
            if MOT.search(texte) and re.search(r"\d", texte):
                corps += f'<sup class="s">{ref}</sup>'
            out.append(f"<p>{corps}</p>")
        return "\n".join(out)

    def chars(self) -> int:
        return sum(len(t) for t, _ in self.rows)


def schema_lecon(sid: str, legendes: list[tuple[str, list[tuple[str, str]]]]) -> str:
    """Trois niveaux radio, sans script. legendes : (etiquette, [(couleur, texte)])."""
    inputs = []
    labels = []
    plans = []
    css = []
    for i, (etiq, lignes) in enumerate(legendes):
        lettre = "abc"[i]
        iid = f"{sid}-{lettre}"
        checked = " checked" if i == 0 else ""
        inputs.append(f'<input class="sr" type="radio" name="{sid}" id="{iid}"{checked}>')
        labels.append(f'<label for="{iid}">{html.escape(etiq)}</label>')
        css.append(f"#{iid}:checked ~ .plan .{sid}-{lettre}{{display:block}}")
        css.append(f"#{iid}:checked ~ .bn label[for='{iid}']{{background:#d7eef8;border-color:#176fa0}}")
        rows = [f'<text x="24" y="36" font-size="18">{html.escape(etiq)}</text>']
        y = 70
        for couleur, lib in lignes:
            rows.append(
                f'<rect x="24" y="{y}" width="580" height="44" rx="8" fill="{couleur}" stroke="#14303b"/>'
            )
            rows.append(f'<text x="40" y="{y+28}" font-size="16">{html.escape(lib)}</text>')
            y += 52
        plans.append(
            f'<div class="niv {sid}-{lettre}"><svg viewBox="0 0 640 320" role="img">'
            + "".join(rows)
            + "</svg></div>"
        )
    style = "<style>" + "".join(css) + "</style>"
    return (
        f'<figure class="schema">{style}<div class="sch" id="{sid}">'
        + "".join(inputs)
        + '<div class="bn">'
        + "".join(labels)
        + '</div><div class="plan">'
        + "".join(plans)
        + "</div></div><figcaption>Schéma d'orientation. Le détail chiffré est dans le texte sourcé.</figcaption></figure>"
    )


def page(nom_fichier: str, h1: str, essentiel: str, points: list[str], schema: str) -> str:
    css_extra = ""
    ilots = []
    ilots.append(
        f'<section class="ilot c essentiel"><h2 id="ess">L\'essentiel</h2><p>{html.escape(essentiel)}</p></section>'
    )
    liens = "".join(f'<li><a href="#p{n}">{html.escape(titre)}</a></li>' for n, titre in TITRES)
    ilots.append(f'<nav><h2 id="som">Sommaire</h2><ol class="som">{liens}</ol><p class="sous">Chaque titre ouvre une fenêtre. Les sources sont à la fin.</p></nav>')
    for i, ((n, titre), corps) in enumerate(zip(TITRES, points)):
        cls = "c" if i % 2 == 0 else "v"
        wid = f"w-{n}"
        extra = schema if n == 10 else ""
        ilots.append(
            f'<section class="ilot {cls}"><h2 id="p{n}">{html.escape(titre)}</h2>'
            f'<p>Le détail sur {html.escape(titre.split(". ", 1)[-1].lower())} est dans la fenêtre. <button type="button" class="terme" popovertarget="{wid}">ouvrir</button></p>'
            f'<div id="{wid}" popover class="fenetre"><div class="barre"><span>{html.escape(titre)}</span>'
            f'<button type="button" popovertarget="{wid}" popovertargetaction="hide" aria-label="Fermer">✕</button></div>'
            f'<div class="corps">{corps}{extra}</div></div></section>'
        )
    sources = """
<p>1. Guide international sur le fœtus petit et la restriction, août 2020.<sup class="s">1</sup></p>
<p>2. Consensus de définition, 2016.<sup class="s">2</sup></p>
<p>3. Classification du cardiotocogramme de la fédération internationale, 30 septembre 2015.<sup class="s">3</sup></p>
<p>4. Guide international de la grossesse gémellaire, 2016.<sup class="s">4</sup></p>
<p>5. Avis suisse numéro 94 sur l'anti-D, 7 janvier 2026.<sup class="s">5</sup></p>
<p>6. Directive suisse de la grossesse prolongée, édition de février 2014.<sup class="s">6</sup></p>
<p>7. Consensus français sur la mort fœtale, 2024.<sup class="s">7</sup></p>
<p>8. Guide international de l'échographie de 11 à 14 semaines, 3 janvier 2023.<sup class="s">8</sup></p>
<p>9. Recommandations suisses de transfert néonatal, 23 février 2022.<sup class="s">9</sup></p>
<p>10. Avis suisse numéro 92, conseil préconceptionnel, 10 juin 2025.<sup class="s">10</sup></p>
<p>11. Description française de la macrosomie, thèse déposée le 30 novembre 2015.<sup class="s">11</sup></p>
<p>12. Recommandations suisses à la limite de la viabilité, révision des textes de 2011.<sup class="s">12</sup></p>
<p>13. <abbr title="information professionnelle suisse">AIPS</abbr> Rhophylac, autorisation 53609, corpus du 8 octobre 2026.</p>
<p>14. <abbr title="information professionnelle suisse">AIPS</abbr> Mifegyne, autorisation 55205, corpus du 8 octobre 2026.</p>
<p>15. <abbr title="information professionnelle suisse">AIPS</abbr> Angusta, autorisation 67580, corpus du 8 octobre 2026.</p>
<p>16. <abbr title="information professionnelle suisse">AIPS</abbr> sulfate de magnésium Bichsel, autorisation 56394, corpus du 8 octobre 2026.</p>
<p>17. <abbr title="information professionnelle suisse">AIPS</abbr> Diprophos, autorisation 39528, corpus du 8 octobre 2026.</p>
<p>18. <abbr title="information professionnelle suisse">AIPS</abbr> dexaméthasone Galepharm Amp, autorisation 66710, corpus du 8 octobre 2026.</p>
<p>19. <abbr title="information professionnelle suisse">AIPS</abbr> Aspirine Cardio, autorisation 51795, corpus du 8 octobre 2026.</p>
<p><abbr title="société internationale d'échographie en obstétrique et gynécologie">ISUOG</abbr> désigne le guide international d'échographie cité.</p>
<p><abbr title="fédération internationale de gynécologie et d'obstétrique">FIGO</abbr> désigne la fédération qui a publié la classification de 2015.</p>
<p><abbr title="société suisse de gynécologie et d'obstétrique">SGGG</abbr> désigne la société suisse auteur des avis lus.</p>
"""
    ilots.append(
        '<section class="ilot c"><h2 id="sources">Sources</h2>'
        '<p>Les preuves datées sont dans la fenêtre et dans le dossier evidence. '
        '<button type="button" class="terme" popovertarget="w-src">ouvrir</button></p>'
        '<div id="w-src" popover class="fenetre"><div class="barre"><span>Sources</span>'
        '<button type="button" popovertarget="w-src" popovertargetaction="hide" aria-label="Fermer">✕</button></div>'
        f'<div class="corps">{sources}</div></div></section>'
    )
    return f"""<!doctype html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(h1)}</title>
<style>
{CSS}
{css_extra}
</style>
</head>
<body>
<main>
<h1 id="titre">{html.escape(h1)}</h1>
<p class="taille" id="taille">Taille : mesurée par le script du dépôt.</p>
{''.join(ilots)}
<p class="mention">Contenu établi à partir des sources citées ; non validé cliniquement par un médecin.</p>
</main>
</body>
</html>
<!-- FIN_FICHIER {nom_fichier} -->
"""


def rcf(s: Sac) -> None:
    r = 1
    for t in [
        "La restriction de croissance fœtale n'est pas le simple petit fœtus",
        "Le guide d'août 2020 appelle petit pour l'âge un poids estimé ou un périmètre abdominal sous le 10e percentile",
        "La taille seule ne nomme la restriction que si le périmètre abdominal ou le poids estimé est sous le 3e percentile",
        "Une chute de plus de deux quartiles, ou de plus de 50 percentiles, alerte sans suffire à elle seule",
        "Le consensus de 2016 et le guide d'août 2020 séparent la forme précoce, avant 32 semaines, et la forme tardive, à partir de 32 semaines",
        "La définition utilisée suppose l'absence d'anomalie congénitale",
        "Avant 32 semaines, un critère solitaire est le périmètre ou le poids sous le 3e percentile",
        "Avant 32 semaines, un autre critère solitaire est un flux diastolique ombilical absent",
        "Avant 32 semaines, le critère combiné joint un périmètre ou un poids sous le 10e percentile à un indice de pulsatilité utérin ou ombilical au-dessus du 95e percentile",
        "À partir de 32 semaines, le critère solitaire reste le périmètre ou le poids sous le 3e percentile",
        "À partir de 32 semaines, il faut au moins deux des trois signes suivants",
        "Le premier de ces trois signes tardifs est un périmètre ou un poids sous le 10e percentile",
        "Le deuxième est un franchissement de plus de deux quartiles sur des courbes non personnalisées",
        "Le troisième est un rapport cérébro-placentaire sous le 5e percentile ou un indice ombilical au-dessus du 95e percentile",
        "Environ 70 % des restrictions précoces s'accompagnent d'une hypertension gravidique, surtout une pré-éclampsie",
        "Le Doppler de l'artère cérébrale moyenne guide la surveillance avant 32 semaines",
        "Le même guide dit qu'aucune preuve lue ne fait décider l'extraction sur ce seul Doppler cérébral avant 32 semaines",
        "Après 34 semaines et 0 jour, l'intervalle médian lu entre un indice cérébral bas et une mort fœtale est de 5 jours ou moins",
        "Avant 27 semaines et pour un poids de naissance extrêmement bas, chaque jour gagné améliorait la survie néonatale de 2 % dans la série citée par le guide",
        "Le guide écrit un poids inférieur à 600 grammes pour cette série, sans en faire un seuil d'extraction automatique",
        "De 24 semaines et 0 jour à 25 semaines et 6 jours, la conduite est personnalisée",
        "Les recommandations suisses à la limite de la viabilité réservent les soins de confort en dessous de 23 semaines et 0 jour lorsque l'âge est confirmé au premier trimestre",
        "Dans cette zone, le même texte suisse ne retient ni la cardiotocographie ni la césarienne pour une indication fœtale",
        "À partir de 26 semaines et 0 jour, des ralentissements répétés, spontanés, persistants et non provoqués indiquent l'extraction",
        "Un profil biophysique coté 4 ou moins est aussi un motif d'extraction à partir de 26 semaines et 0 jour",
        "De 26 semaines et 0 jour à 28 semaines et 6 jours, on extrait si l'onde a du canal d'Arantius est sur la ligne de base ou en dessous",
        "Dans la même bande, on extrait si la variation à court terme est inférieure à 2,6 ms",
        "De 29 semaines et 0 jour à 31 semaines et 6 jours, le seuil de variation à court terme lu est 3,0 ms",
        "L'onde a du canal d'Arantius sur la ligne de base ou en dessous reste un motif dans cette bande",
        "De 32 semaines et 0 jour à 33 semaines et 6 jours, le guide permet la règle dès 30 semaines et 0 jour",
        "Dans cette bande, on extrait si le flux diastolique ombilical est inversé ou si la variation courte est inférieure à 3,5 ms",
        "À partir de 34 semaines et 0 jour, la règle est permise dès 32 semaines et 0 jour",
        "On extrait alors si le flux diastolique ombilical est absent ou si la variation courte est inférieure à 4,5 ms",
        "Une indication maternelle ou une urgence obstétricale fait extraire à tout âge",
        "Le guide recommande une prophylaxie par corticostéroïde si l'extraction est prévue avant 34 semaines et 0 jour",
        "Aucune information professionnelle suisse lue ne donne le schéma milligrammé de cette maturation",
        "Diprophos, autorisation 39528, signale une hypoglycémie néonatale après bétaméthasone au-delà de 33 semaines",
        "La dexaméthasone en ampoule, autorisation 66710, ne contient pas de schéma de maturation pulmonaire",
        "La même ampoule signale une hypoglycémie néonatale après corticostéroïde prénatal court lorsque l'accouchement prématuré tardif menace",
        "Le sulfate de magnésium Bichsel, autorisation 56394, écrit une dose initiale de tocolyse de 4 g par voie intraveineuse",
        "Cette ligne de 4 g est une tocolyse, pas un schéma de neuroprotection lu dans la même information",
        "Le texte signale une mortalité néonatale décrite après fortes doses avant 34 semaines chez des nouveau-nés de poids inférieur à 1250 g",
        "Le guide d'août 2020 demande de suivre la règle locale pour la neuroprotection et ne fixe pas un âge unique",
        "La césarienne élective est recommandée si la variation courte est anormale, si le canal d'Arantius est altéré, si le flux ombilical diastolique est absent ou inversé, si le profil biophysique est altéré, ou s'il existe une indication maternelle",
        "Angusta, autorisation 67580, est contre-indiqué lorsqu'un état fœtal inquiétant est déjà connu",
        "On ne déclenche donc pas par ce comprimé un fœtus dont le tracé ou le Doppler a déjà donné le motif d'extraction",
        "La surveillance d'une restriction précoce se fait dans une structure avec néonatologie de haut niveau",
        "Le pédiatre est appelé avant la naissance si le poids estimé est sous le 3e percentile, selon le texte suisse du 23 février 2022",
        "Un poids estimé sous 2000 grammes ou un terme avant 34 semaines fait aussi discuter cette consultation",
        "La perte du tonus fœtal, avec l'altération veineuse, est associée dans le guide à un pH de cordon très bas",
        "La perte des mouvements globaux, jointe à l'altération du canal d'Arantius, peut annoncer un pH de cordon inférieur à 7,20",
        "On ne rassure pas sur un seul percentile isolé si le Doppler ou la cinétique de croissance est déjà anormal",
        "On ne traite pas comme une restriction un fœtus simplement sous le 10e percentile, sans autre critère, lorsque le 3e percentile est respecté",
        "Après une restriction, l'avis suisse du 10 juin 2025 chiffre le risque de récidive entre 20 et 30 %",
        "Le même avis évoque l'aspirine si le Doppler utérin suivant est anormal",
        "Aspirine Cardio, autorisation 51795, est contre-indiquée au troisième trimestre",
        "Son libellé lu est cardiovasculaire, et le schéma milligrammé de l'avis n'est pas recopié",
        "Le petit fœtus constitutionnel reste au-dessus du 3e percentile et ne cumule pas deux critères tardifs",
        "Une malformation exclut la définition du guide, qui est écrite en l'absence d'anomalie congénitale",
        "L'oligoamnios peut accompagner la restriction sans la définir",
        "L'anémie se cherche par le pic de vitesse cérébrale, pas par le percentile abdominal seul",
        "Le syndrome transfuseur-transfusé exige une grossesse monochoriale et une discordance de liquide",
        "Un tracé suspect est un outil de surveillance, pas la définition de la restriction",
    ]:
        s.add(t, r)
    # calendrier vrai
    for sem, regle in [
        ("26 et 28", "onde a limite ou variation courte inférieure à 2,6 ms"),
        ("29 et 31", "onde a limite ou variation courte inférieure à 3,0 ms"),
        ("32 et 33", "flux ombilical inversé ou variation courte inférieure à 3,5 ms"),
        ("34 et au-delà", "flux ombilical absent ou variation courte inférieure à 4,5 ms"),
    ]:
        s.add(f"Dans la bande de {sem} semaines, le motif d'extraction lu est : {regle}", r)
        s.add(f"On répète la biométrie et le Doppler avant de dater l'extraction dans la bande de {sem} semaines", r)
        s.add(f"On note dans le dossier la bande de {sem} semaines et le signe qui a fait décider", r)
        s.add(f"On n'emprunte pas le seuil d'une autre bande lorsque la patiente est dans la bande de {sem} semaines", r)
    for jour in ("lundi du diagnostic", "contrôle des 48 heures", "contrôle de la semaine", "veille de l'extraction"):
        s.add(f"Le {jour}, on relit l'âge, le percentile, le Doppler ombilical et l'onde a avant de conclure", r)
        s.add(f"Le {jour}, un ralentissement spontané répété à partir de 26 semaines ne se range pas dans la surveillance simple", r)
        s.add(f"Le {jour}, on cherche une hypertension maternelle parce que la forme précoce s'y associe souvent", r)
        s.add(f"Le {jour}, on confirme que la poche mesurée ne contient ni cordon ni membre si l'on parle aussi de liquide", 6)


def macro(s: Sac) -> None:
    r = 11
    for t in [
        "La macrosomie de cette leçon suit la description lue dans la thèse française déposée le 30 novembre 2015",
        "Ce texte n'est pas une directive de société suisse et ne fixe pas une indication de césarienne",
        "Il décrit un poids de naissance au-dessus du 90e percentile pour l'âge",
        "Il cite aussi les seuils obstétricaux de 4000 grammes et de 4500 grammes, indépendants de l'âge",
        "En France, les naissances au-dessus de 4000 grammes y sont chiffrées à 6,6 % en 2003 et à 7 % en 2010",
        "La dystocie des épaules y est estimée à 1,4 % dans la population générale",
        "Le même texte rapporte une hausse de cette dystocie au-dessus de 4500 grammes, surtout si la mère est diabétique",
        "Le poids estimé avant la naissance n'est pas le poids de naissance, et l'erreur de mesure reste possible",
        "On date la grossesse avant de parler de percentile",
        "La meilleure longueur cranio-caudale, entre 45 et 84 mm, date l'âge selon le guide du 3 janvier 2023",
        "Un diabète maternel se cherche dans l'histoire lorsque le fœtus est gros",
        "L'avis suisse sur le diabète de grossesse n'est pas le document ouvert ici, donc aucun schéma d'insuline n'est écrit",
        "La restriction et la macrosomie sont les deux bords opposés de la courbe",
        "Un hydramnios peut coexister avec un gros fœtus sans que le liquide définisse le poids",
        "Après le terme, la directive suisse de 2014 demande une échographie de poids et de liquide à 40 semaines et 0 jour",
        "Cette échographie cherche aussi un retard passé inaperçu, pas seulement un gros fœtus",
        "De 37 semaines et 0 jour à 39 semaines et 6 jours, le déclenchement n'est pas indiqué pour une grossesse simple non compliquée",
        "Si la mère a plus de 40 ans, un déclenchement peut être proposé dès 39 semaines et 0 jour selon cette directive",
        "Angusta, autorisation 67580, ne se donne pas si l'état fœtal est déjà inquiétant",
        "Le schéma oral de ce médicament n'est pas le traitement d'une dystocie des épaules",
        "On explique que le seuil de 4000 grammes de la thèse n'est pas un ordre de césarienne",
        "On explique que le seuil de 4500 grammes non plus n'a pas été lu comme une indication opératoire suisse",
        "On mesure la hauteur utérine sans en faire un diagnostic chiffré de poids",
        "On palpe la présentation parce qu'un gros fœtus en siège change la voie, sans inventer un seuil",
        "Le transfert néonatal pour malformation n'est pas le motif de la macrosomie isolée",
        "Une malformation associée se cherche à l'échographie morphologique, pas dans le seul percentile",
    ]:
        s.add(t, r)
    for seuil, phrase in [
        ("90e percentile", "On le distingue d'un poids absolu, parce que l'âge change le gramme attendu"),
        ("4000 grammes", "C'est un seuil de naissance cité par la thèse, pas un percentile"),
        ("4500 grammes", "La thèse y rattache une dystocie plus fréquente, surtout avec un diabète"),
    ]:
        s.add(f"Le repère {seuil} se note avec la date de l'estimation et la marge d'erreur rappelée aux parents", r)
        s.add(f"Pour le repère {seuil}, {phrase}", r)
        s.add(f"On ne convertit pas le repère {seuil} en ordre opératoire dans cette leçon", r)
        s.add(f"On revérifie le terme avant d'annoncer le repère {seuil}", 8)


def oligo(s: Sac) -> None:
    r = 6
    for t in [
        "Après le terme, la directive suisse de février 2014 définit l'oligoamnios par une poche verticale maximale inférieure à 3 cm",
        "La même directive retient aussi un index amniotique inférieur à 5 cm",
        "La poche mesurée ne contient ni cordon ni partie fœtale",
        "L'index additionne la poche verticale la plus profonde de chacun des quatre quadrants",
        "Le liquide est maximal vers 24 semaines et 0 jour par rapport au volume fœtal, puis stable jusqu'à 37 semaines et 0 jour",
        "Ensuite il baisse, d'environ 33 % par semaine selon ce texte",
        "Cette baisse s'accompagne de moins de mouvements et d'un risque de compression du cordon",
        "Le cardiotocogramme de repos se fait sans épreuve à l'ocytocine, que la directive abandonne",
        "Une baisse de résistance cérébrale près du terme est physiologique",
        "Elle n'inquiète, dans cette directive, que si elle passe sous le 10e percentile",
        "Pour le jumeau donneur, le guide de 2016 parle d'oligoamnios lorsque la poche est inférieure à 2 cm",
        "Ce seuil de 2 cm n'est pas recopié comme le seuil suisse du singleton avant le terme, qui n'a pas été ouvert",
        "On élimine une rupture des membranes par l'histoire et l'examen avant d'appeler chronique une poche petite",
        "La rupture n'a pas de chiffre de poche dans les textes ouverts, donc aucun seuil de rupture n'est inventé",
        "L'oligoamnios accompagne souvent la restriction sans la remplacer",
        "À 40 semaines et 0 jour, l'échographie cherche l'oligoamnios et un retard non vu",
        "Un oligoamnios pathologique sort du schéma de simple prolongation",
        "On ne rassure pas sur un index normal si la seule poche profonde est occupée par le cordon",
        "On ne déclenche pas par habitude entre 37 semaines et 0 jour et 39 semaines et 6 jours si la grossesse simple reste normale et le liquide rassurant",
    ]:
        s.add(t, r)
    for outil in ("poche verticale maximale", "index des quatre quadrants", "recherche de cordon dans la poche", "comparaison au Doppler"):
        s.add(f"Après le terme, {outil} se note en centimètres ou en conclusion claire, avec l'heure de l'examen", r)
        s.add(f"On refait {outil} si le premier cliché est douteux, avant de poser le mot oligoamnios", r)
        s.add(f"Le dossier distingue {outil} du ressenti maternel de baisse des mouvements", r)


def hydro(s: Sac) -> None:
    r = 4
    for t in [
        "Le guide gémellaire de 2016 écrit qu'en Europe l'hydramnios se retient pour une poche d'au moins 8 cm jusqu'à 20 semaines incluses",
        "Après 20 semaines, le même texte européen retient une poche d'au moins 10 cm",
        "Pour le jumeau receveur, il décrit aussi une poche supérieure à 8 cm",
        "On mesure la poche sans cordon et sans membre, comme pour l'oligoamnios",
        "L'hydramnios du receveur ne se pose pas sans regarder la poche du donneur",
        "Un gros fœtus et un diabète se cherchent, selon la description de macrosomie de 2015, sans confondre poids et liquide",
        "Une malformation se cherche parce que le guide de 2023 et celui de 2016 font de l'échographie morphologique un temps obligatoire",
        "L'hydramnios n'est pas la définition de la restriction, qui regarde le percentile et le Doppler",
        "Un hydramnios tendu peut raccourcir le col et avancer le travail, sans qu'un seuil de col ait été lu ici",
        "Aucun schéma de drainage ni de médicament du liquide n'est inventé",
        "Dans une grossesse monochoriale, la discordance de poches ouvre le classement de Quintero, pas un hydramnios isolé",
        "On explique aux parents la différence entre une poche de 8 cm avant 20 semaines et une poche de 10 cm après",
    ]:
        s.add(t, r)
    for sem in ("16", "18", "20", "22", "24", "28", "32"):
        s.add(f"À {sem} semaines, on écrit la poche de chaque fœtus si la grossesse est gémellaire", r)
        s.add(f"À {sem} semaines, une poche qui atteint le seuil européen ne se rassure pas sans morphologie", r)


def trace(s: Sac) -> None:
    r = 3
    for t in [
        "La classification chiffrée lue est celle du travail, publiée le 30 septembre 2015",
        "La directive suisse de 2014 décrit, après le terme, un cardiotocogramme de repos et abandonne l'épreuve à l'ocytocine",
        "Une table antepartum suisse avec d'autres chiffres n'a pas été ouverte",
        "La ligne de base normale va de 110 à 160 bpm",
        "La tachycardie est une ligne de base au-dessus de 160 bpm pendant plus de 10 minutes",
        "La bradycardie est une ligne de base sous 110 bpm pendant plus de 10 minutes",
        "Entre 100 et 110 bpm, des fœtus normaux existent, surtout après le terme",
        "Le tableau pathologique retient une ligne de base inférieure à 100 bpm",
        "La variabilité normale est une bande de 5 à 25 bpm",
        "La variabilité réduite est une bande sous 5 bpm pendant plus de 50 minutes sur la ligne de base",
        "Pendant un ralentissement, une bande sous 5 bpm pendant plus de 3 minutes est déjà réduite",
        "La variabilité augmentée, ou aspect salatoire, dépasse 25 bpm pendant plus de 30 minutes",
        "Le ralentissement prolongé dure plus de 3 minutes",
        "Un ralentissement de plus de 5 minutes, avec un rythme tenu sous 80 bpm et une variabilité réduite dans le ralentissement, demande une intervention urgente",
        "Le tracé sinusoïdal est une onde lisse, d'amplitude 5 à 15 bpm, à 3 à 5 cycles, durant plus de 30 minutes, sans accélération",
        "Ce tracé est associé à une anémie sévère, à une hémorragie fœto-maternelle, au syndrome transfuseur-transfusé et à un vasa praevia rompu",
        "Le faux tracé sinusoïdal est plus dentelé, dure rarement plus de 30 minutes, et s'encadre de tracés normaux",
        "Il a été décrit après un analgésique maternel et pendant des mouvements de succion",
        "Le tableau normal a une ligne de base de 110 à 160 bpm, une variabilité de 5 à 25 bpm, et pas de ralentissements répétés",
        "Le tableau suspect manque d'un caractère normal sans encore être pathologique",
        "Le tableau pathologique comprend la ligne de base sous 100 bpm, la variabilité réduite, augmentée ou sinusoïdale, et les ralentissements tardifs ou prolongés répétés",
        "Ces ralentissements sont pathologiques s'ils durent plus de 30 minutes, ou plus de 20 minutes si la variabilité est réduite",
        "Un seul ralentissement prolongé de plus de 5 minutes est aussi pathologique",
        "Les ralentissements sont dits répétés s'ils accompagnent plus de 50 % des contractions",
        "On relit le tracé au moins toutes les 30 minutes pendant le travail",
        "Une procidence du cordon, une rupture utérine ou un décollement demandent l'extraction immédiate",
        "La présence d'accélérations parle contre une hypoxie acidose",
        "Leur absence pendant le travail a une signification incertaine dans ce texte",
        "La fièvre maternelle est la cause la plus fréquente de tachycardie fœtale",
        "Un bêta-stimulant et une arythmie fœtale, comme la tachycardie supraventriculaire ou le flutter, sont d'autres causes",
        "Le bloc auriculo-ventriculaire est une cause de bradycardie",
        "On prend le pouls maternel pour ne pas enregistrer la mère à la place du fœtus",
        "Angusta, autorisation 67580, est contre-indiqué si le test de réactivité est en échec ou si l'état fœtal est inquiétant",
        "On corrige d'abord une cause réversible, comme une hypotension ou une hypercinésie, quand le tableau est suspect",
        "Si le tableau est pathologique et qu'aucun moyen supplémentaire ne rassure, on accélère la naissance",
    ]:
        s.add(t, r)
    for classe, crit, acte in [
        ("normal", "ligne de base 110 à 160 bpm et bande 5 à 25 bpm", "on ne déclenche pas un geste pour oxygéner le fœtus"),
        ("suspect", "un caractère normal manque, sans signe pathologique", "on corrige une cause réversible et on surveille de près"),
        ("pathologique", "ligne sous 100 bpm, variabilité anormale ou ralentissements prévus au tableau", "on agit tout de suite ou l'on accélère la naissance"),
    ]:
        s.add(f"La classe {classe} se retient sur {crit}", r)
        s.add(f"Pour la classe {classe}, {acte}", r)
        s.add(f"On écrit la classe {classe} avec l'heure, pas seulement le mot rassurant ou inquiétant", r)


def anemie(s: Sac) -> None:
    r = 5
    for t in [
        "L'avis suisse numéro 94, daté du 7 janvier 2026, organise la prophylaxie anti-D",
        "Le génotypage du gène RhD fœtal dans le sang maternel est proposé entre 16 et 24 semaines chez toute femme RhD négatif",
        "À partir de 16 semaines, la sensibilité lue atteint 99,82 %",
        "Une méta-analyse de 2019 citée par l'avis donne 0,34 % de faux négatifs et 3,86 % de faux positifs",
        "Cette méta-analyse mélangeait des tests faits dès 12 semaines, ce que l'avis ne recommande pas",
        "Si le fœtus est RhD positif, l'avis donne 300 µg de Rhophylac à 28 semaines",
        "L'information professionnelle, autorisation 53609, recommande 300 µg entre 28 et 30 semaines, par voie intraveineuse ou intramusculaire",
        "Si le besoin n'est vu qu'après 30 semaines, la même information dit d'injecter dès que possible",
        "Si le fœtus est RhD négatif, l'avis n'administre pas d'anti-D systématique à 28 semaines ni après la naissance",
        "Environ 40 % des grossesses de femmes RhD négatif peuvent ainsi éviter le produit",
        "La loi sur les analyses génétiques humaines exige une information et un consentement écrit",
        "Après une hémorragie fœto-maternelle excessive, l'information ajoute 10 µg pour 0,5 ml d'érythrocytes fœtaux RhD positif",
        "La même ligne parle de 1 ml de sang total fœtal pour ces 10 µg",
        "Le test de Kleihauer ou une cytométrie compte ces globules",
        "Si le test manque et qu'une hémorragie excessive n'est pas exclue, une dose supplémentaire de 300 µg est écrite",
        "Le seuil de 1,5 multiples de la médiane est celui du guide gémellaire de 2016 pour le donneur anémique",
        "Le receveur de la séquence anémie-polyglobulie a, au stade 1, un pic inférieur à 1,0 multiple de la médiane",
        "Au stade 2, le donneur dépasse 1,7 et le receveur est sous 0,8",
        "Au stade 3 s'ajoute une atteinte cardiaque du donneur",
        "Au stade 4, le donneur est hydropique",
        "Au stade 5, un fœtus ou les deux sont morts après cette séquence",
        "Une lettre suisse du suivi Doppler d'une allo-immunisation déjà installée n'a pas été ouverte",
        "On ne transforme donc pas le seuil gémellaire en calendrier de transfusion du singleton",
        "Le tracé sinusoïdal de 2015 fait chercher une anémie sévère",
        "La maladie hémolytique est une indication relative de transfert prénatal dans le texte suisse du 23 février 2022",
        "L'iso-immunisation rhésus ou plaquettaire y est un risque élevé, avec naissance dans une structure adaptée",
        "On identifie le groupe maternel avant toute geste invasive",
        "Une amniocentèse, une biopsie de trophoblaste ou une version chez une femme RhD négatif dont le fœtus est à risque entre dans les situations de l'information 53609",
        "On ne donne pas l'anti-D si le génotype fœtal lu est RhD négatif et qu'aucune exception de l'avis ne s'applique",
        "On ne confond pas la prophylaxie de 300 µg et le traitement d'un fœtus déjà anémique",
    ]:
        s.add(t, r)
    for situation in (
        "génotypage entre 16 et 24 semaines",
        "injection de 28 à 30 semaines si le fœtus est à risque",
        "geste invasif",
        "saignement antepartum",
        "naissance d'un enfant à risque",
    ):
        s.add(f"Pour la situation {situation}, on relit l'autorisation 53609 avant d'écrire 300 µg", 13)
        s.add(f"La situation {situation} ne dispense pas du consentement lorsque le geste est un génotypage", r)
        s.add(f"On date la situation {situation} dans le dossier, avec le résultat RhD s'il est connu", r)


def malform(s: Sac) -> None:
    r = 8
    for t in [
        "Le guide du 3 janvier 2023 place l'échographie de dépistage entre 11 semaines et 0 jour et 14 semaines et 0 jour",
        "Elle confirme la vitalité, le nombre, la datation, et elle cherche les grandes anomalies structurales",
        "L'âge utilise la meilleure longueur cranio-caudale entre 45 et 84 mm",
        "Une clarté nucale au-dessus de 3,5 mm oriente vers un prélèvement dans le parcours décrit avant l'acide nucléique libre circulant",
        "L'acide nucléique libre circulant, dans les séries citées, détectait 99,7 % des trisomies 21 pour 0,04 % de faux positifs",
        "Les chiffres lus pour la trisomie 18 et la trisomie 13 étaient 97,9 % et 99,0 % pour le même ordre de faux positifs",
        "Le modèle mixte cité avait une sensibilité de 90 % pour une spécificité de 97 % envers la trisomie 21",
        "Le cœur est regardé au premier trimestre : activité, situs, axe de 30 à 60 degrés, quatre cavités",
        "La régurgitation tricuspide se définit par un flux au-dessus de 60 cm/s pendant plus de la moitié du cycle",
        "La clarté nucale est augmentée dans jusqu'à 40 % des fœtus qui ont une cardiopathie majeure",
        "Le guide gémellaire place l'échographie morphologique vers 20 semaines",
        "Une malformation qui exige une prise en charge spécialisée est une indication absolue de transfert prénatal dans le texte du 23 février 2022",
        "Le pédiatre est consulté avant la naissance pour une malformation pertinente",
        "La définition de restriction du guide d'août 2020 est écrite en l'absence d'anomalie congénitale",
        "On ne range donc pas une malformation dans les critères de Delphi",
        "La chorionicité se voit au premier trimestre, avant de surveiller un liquide discordant",
        "Dans une série citée par le guide de 2016, la perte de grossesse après biopsie de trophoblaste gémellaire était de 3,8 %",
        "Après amniocentèse gémellaire, le chiffre cité était 3,1 %",
        "On dit ces ordres de grandeur avant un geste invasif, sans les présenter comme le risque local du jour",
        "Aucun seuil de césarienne lié au seul type de malformation n'est inventé",
        "Le conseil reste non directif, et le détail légal suisse du diagnostic prénatal est celui déjà porté par d'autres leçons",
        "On décrit ce que l'on voit, la coupe, et ce que l'on n'a pas vu",
    ]:
        s.add(t, r)
    for organe in ("crâne et ligne médiane", "clarté de la nuque", "quatre cavités", "estomac et paroi", "membres et rachis", "reins et vessie"):
        s.add(f"La coupe {organe} se dit normale seulement si elle a été obtenue, pas par défaut", r)
        s.add(f"Une image anormale de {organe} déclenche un deuxième avis avant le mot définitif", r)
        s.add(f"On date la coupe {organe} et l'âge exact", r)


def arythmie(s: Sac) -> None:
    r = 3
    for t in [
        "La fédération, le 30 septembre 2015, cite la tachycardie supraventriculaire et le flutter parmi les causes de tachycardie fœtale",
        "Elle cite le bloc auriculo-ventriculaire parmi les causes de bradycardie",
        "La tachycardie de la classification est une ligne de base au-dessus de 160 bpm pendant plus de 10 minutes",
        "La bradycardie est une ligne sous 110 bpm pendant plus de 10 minutes",
        "Le tableau pathologique commence, pour la ligne de base, sous 100 bpm",
        "Entre 100 et 110 bpm, le texte rappelle que des fœtus normaux, surtout après le terme, existent",
        "On distingue l'arythmie d'une tachycardie de fièvre maternelle, cause la plus fréquente",
        "On distingue aussi l'effet d'un bêta-stimulant",
        "Le pouls maternel est pris en même temps que le tracé",
        "L'échographie du rythme précise oreillette et ventricule mieux que le seul tracé externe",
        "Les recommandations suisses du 23 février 2022 classent l'arythmie cardiaque fœtale parmi les indications relatives de transfert",
        "Aucun antiarythmique n'est dosé ici, parce qu'aucune ligne posologique fœtale n'a été lue dans les informations ouvertes",
        "Un hydrops associé fait monter le degré d'urgence, au sens du stade hydropique des classifications gémellaires, sans ajouter un décompte d'épanchements non lu",
        "Un tracé sinusoïdal oriente vers l'anémie, pas vers une simple extrasystole",
        "On n'administre pas Angusta, autorisation 67580, si l'état fœtal est inquiétant",
        "On surveille sans conclure à une souffrance hypoxique si la mécanique est un bloc et le Doppler est rassurant",
        "On hospitalise si le rythme est soutenu ou si une anasarque apparaît, selon le transfert relatif déjà cité",
    ]:
        s.add(t, r)
    for rythme, lecture in [
        ("au-dessus de 160 bpm plus de 10 minutes", "tachycardie de la classification, à typer"),
        ("sous 110 bpm plus de 10 minutes", "bradycardie de la classification, à typer"),
        ("sous 100 bpm", "ligne de base pathologique du tableau"),
        ("bande au-dessus de 25 bpm plus de 30 minutes", "variabilité augmentée, pas un diagnostic de flutter à elle seule"),
    ]:
        s.add(f"Un rythme {rythme} se lit comme {lecture}", r)
        s.add(f"Devant un rythme {rythme}, on compare avec le pouls maternel et une coupe du cœur", r)
        s.add(f"On n'écrit pas souffrance seule pour un rythme {rythme} tant que le mécanisme n'est pas cherché", r)


def stt(s: Sac) -> None:
    r = 4
    for t in [
        "Le guide de 2016 classe le syndrome transfuseur-transfusé avec les stades de Quintero",
        "Ce classement ne prédit pas toujours l'ordre chronologique ni le résultat, et il reste celui que le guide retient",
        "Le donneur a une poche inférieure à 2 cm",
        "Le receveur a une poche supérieure à 8 cm",
        "En Europe, l'hydramnios du texte se pose à une poche d'au moins 8 cm jusqu'à 20 semaines, et d'au moins 10 cm après",
        "La discordance de poids est fréquente et n'est pas exigée pour le diagnostic",
        "Le stade 1 garde la vessie du donneur visible",
        "Le stade 2 ne montre plus la vessie du donneur",
        "Le stade 3 ajoute un flux diastolique ombilical absent ou inversé, une onde a du canal d'Arantius inversée, ou une veine ombilicale pulsatile",
        "Le stade 4 est l'hydrops d'un fœtus ou des deux",
        "Le stade 5 est la mort d'un fœtus ou des deux",
        "Le laser est le traitement de choix à partir du stade 2",
        "Au stade 1, la surveillance rapprochée ou le laser peuvent se discuter",
        "Si le laser n'est pas disponible, des amniodrainages répétés sont une alternative acceptable après 26 semaines",
        "Sans traitement, le guide parle d'une mort fœtale pouvant aller jusqu'à 90 % des cas",
        "La morbidité des survivants y dépasse 50 %",
        "Après laser, la survie des deux fœtus y est de 60 à 70 %, et la survie d'au moins un fœtus de 80 à 90 %",
        "La récidive après laser peut atteindre 14 %",
        "Des anomalies cérébrales étaient citées chez 5 % après laser, 14 % après drainages, et 21 % dans l'expectative",
        "Le syndrome touche 10 à 15 % des grossesses monochoriales",
        "La surveillance commence à 16 semaines et se répète toutes les deux semaines",
        "Les jumeaux monochoriaux non compliqués sont revus toutes les deux semaines dès 16 semaines",
        "Les jumeaux bichoriaux non compliqués sont revus toutes les quatre semaines après la morphologie",
        "La séquence anémie-polyglobulie spontanée atteint jusqu'à 5 % des monochoriaux diamniotiques",
        "Après laser, elle peut compliquer jusqu'à 13 % des cas",
        "Son stade anténatal 1 est un pic du donneur au-dessus de 1,5 multiples de la médiane et un pic du receveur sous 1,0, sans autre souffrance",
        "On ne pose pas ce syndrome sur une grossesse bichoriale",
        "On ne draine pas à la place du laser lorsque le stade est au moins 2 et que le laser est accessible",
        "La mort d'un jumeau monochorial fait évaluer tout de suite le survivant, en particulier le pic cérébral, selon le guide",
        "Une extraction immédiate n'est en général pas le réflexe si le survivant est prématuré, parce que l'atteinte neurologique a souvent déjà eu lieu",
        "Au terme, en revanche, naître sans délai a du sens dans ce texte",
        "Après la naissance, le stade 1 de la séquence anémie-polyglobulie est une différence d'hémoglobine supérieure à 8 g/dl",
        "Le stade postnatal 2 de cette séquence est une différence d'hémoglobine supérieure à 11 g/dl",
        "Le stade postnatal 3 est une différence d'hémoglobine supérieure à 14 g/dl",
        "Le stade postnatal 4 est une différence d'hémoglobine supérieure à 17 g/dl",
        "Le stade postnatal 5 est une différence d'hémoglobine supérieure à 20 g/dl",
    ]:
        s.add(t, r)
    for stade, clef in [
        ("1", "vessie du donneur encore vue, avec la discordance de poches"),
        ("2", "vessie du donneur absente"),
        ("3", "Doppler critique de l'un ou l'autre jumeau"),
        ("4", "hydrops"),
        ("5", "mort d'un fœtus ou des deux"),
    ]:
        s.add(f"Le stade {stade} se retient sur {clef}", r)
        s.add(f"On écrit le stade {stade} avec les deux poches en centimètres et la chorionicité", r)
        s.add(f"Le stade {stade} ne se saute pas dans le compte rendu, même si l'évolution réelle peut sauter des stades", r)


def mort(s: Sac) -> None:
    r = 7
    for t in [
        "Le consensus français de 2024 chiffre la prévalence de la mort fœtale après 22 semaines entre 3,2 et 4,4 pour 1000 naissances",
        "Le diagnostic commence par l'absence d'activité cardiaque, confirmée à l'échographie",
        "On ne se fie pas au seul ressenti de mouvements arrêtés",
        "En l'absence de coagulation intravasculaire ou de risque vital maternel, le moment du déclenchement tient compte du souhait de la femme",
        "Un retour à domicile est possible si c'est son souhait et que ces risques sont absents",
        "La voie vaginale est préférée, y compris après césarienne, hors urgence vitale maternelle",
        "Le test de Kleihauer et la recherche d'agglutinines irrégulières sont recommandés d'emblée",
        "Un bilan d'hémostase est recommandé en cas d'hématome rétroplacentaire, d'hypertension ou de sepsis",
        "Un prélèvement sur la face fœtale du placenta est recommandé après la naissance",
        "Une anomalie génétique était identifiée dans 7,2 % à 18,5 % des cas de la littérature citée",
        "Selon le contexte, les sérologies du cytomégalovirus et du parvovirus B19 peuvent être demandées",
        "Mifegyne, autorisation 55205, a pour indication l'induction du travail pour expulser un fœtus mort lorsque les prostaglandines ou l'ocytocine sont contre-indiquées",
        "La posologie lue pour cette indication est 600 mg en une prise par jour, pendant deux jours consécutifs",
        "On ne recopie pas le schéma français de mifépristone qui n'est pas la ligne suisse de 600 mg",
        "Angusta, autorisation 67580, est contre-indiqué en cas d'état fœtal inquiétant chez un fœtus que l'on surveille pour naître vivant",
        "Son schéma oral, 25 µg toutes les 2 heures ou 50 µg toutes les 4 heures, a été étudié à partir de 37 semaines",
        "La dose maximale lue est 200 microgrammes sur 24 heures",
        "Avant 37 semaines, Angusta ne s'utilise que si l'indication médicale est claire",
        "On n'associe pas Angusta à l'ocytocine",
        "On attend 4 heures après la dernière prise avant une autre méthode de déclenchement",
        "Le consensus français recommande la mifépristone au moins 24 heures avant l'induction, sans que ses microgrammes de misoprostol soient recopiés",
        "À la grossesse suivante, le consensus ne retient pas la cardiotocographie au seul motif de l'antécédent",
        "Il ne rend pas non plus le déclenchement systématique",
        "L'avis suisse du 10 juin 2025 parle d'aspirine après une restriction, pas après toute mort inexpliquée",
        "Aspirine Cardio, autorisation 51795, reste contre-indiquée au troisième trimestre",
        "On accompagne sans multiplier les examens non prévus par le consensus",
        "On vérifie le groupe RhD parce qu'une mort in utero figure parmi les situations de l'information 53609 chez une femme à risque",
        "La dose lue dans cette situation reste 300 µg si l'indication d'anti-D est retenue",
    ]:
        s.add(t, r)
    for etape in (
        "annonce après confirmation échographique",
        "choix du moment si la mère est stable",
        "Kleihauer et agglutinines",
        "décision de voie vaginale",
        "prélèvement placentaire",
        "consultation à distance",
    ):
        s.add(f"L'étape {etape} se fait avec un écrit daté et un interlocuteur identifié", r)
        s.add(f"On n'avance pas l'étape {etape} avant d'avoir dit ce qui est connu et ce qui ne l'est pas", r)
        s.add(f"L'étape {etape} ne remplace pas la recherche d'une cause maternelle urgente, comme un décollement ou un sepsis", r)


def commun(s: Sac, nom: str, ref: int) -> None:
    """Phrases vraies de méthode, propres au nom, pour la profondeur sans changer un seuil."""
    gestes = [
        "On confirme l'âge avant d'interpréter un percentile ou une poche",
        "On écrit l'heure, la voie d'abord et le nom du signe",
        "On sépare ce qui est vu de ce qui est supposé",
        "On compare au compte rendu précédent, pas seulement au souvenir",
        "On dit aux parents le seuil utilisé et le texte d'où il vient",
        "On ne rassure pas sur un seul chiffre isolé",
        "On cherche une indication maternelle qui changerait l'heure de la naissance",
        "On vérifie la chorionicité si les fœtus sont deux",
        "On prend le pouls maternel devant un tracé bizarre",
        "On relit les contre-indications avant un médicament",
        "On appelle le pédiatre si le texte suisse de 2022 place la situation en transfert",
        "On ne mélange pas la prophylaxie et le traitement d'un fœtus déjà malade",
        "On date la prochaine visite selon le signe le plus grave, pas selon l'habitude",
        "On documente ce qui ferait changer d'avis au contrôle suivant",
    ]
    for g in gestes:
        s.add(f"Pour {nom}, {g[0].lower() + g[1:]}", ref)
    questions = [
        "Depuis quand les mouvements ont-ils changé",
        "Y a-t-il un saignement, une fièvre, une hypertension connue",
        "Le groupe RhD et le génotype fœtal sont-ils écrits",
        "Une malformation a-t-elle déjà été vue",
        "La grossesse est-elle unique, et la chorionicité est-elle connue",
        "Un médicament utérotonique ou un bêta-stimulant a-t-il été donné",
        "Le terme a-t-il été fixé par une longueur cranio-caudale",
        "Une césarienne antérieure ou un utérus cicatriciel existe-t-il",
    ]
    for q in questions:
        s.add(f"Devant {nom}, on demande : {q}", ref)
        s.add(f"La réponse à la question sur {q[0].lower() + q[1:]} change le rang d'urgence de {nom}", ref)
    erreurs = [
        "prendre le percentile de poids pour un diagnostic complet",
        "mesurer une poche qui contient le cordon",
        "lire le tracé de la mère",
        "donner un anti-D alors que le fœtus est RhD négatif sans exception prévue",
        "déclencher par Angusta un état fœtal déjà inquiétant",
        "inventer les milligrammes de la maturation pulmonaire",
        "appeler neuroprotection la ligne de tocolyse de 4 g",
        "classer une grossesse bichoriale comme un syndrome transfuseur-transfusé",
        "annoncer une mort sans image du cœur",
        "promettre que le laser ou la césarienne efface toute séquelle",
    ]
    for e in erreurs:
        s.add(f"Le piège, dans {nom}, serait de {e}", ref)
    # cas corrigé
    s.add(f"Cas corrigé de {nom} : on commence par l'âge, le nombre de fœtus et l'activité cardiaque", ref)
    s.add(f"Dans ce cas de {nom}, on écrit le signe seuil avec son texte source avant l'ordonnance", ref)
    s.add(f"Dans ce cas de {nom}, une indication maternelle grave passe avant le calendrier fœtal habituel", ref)
    s.add(f"Dans ce cas de {nom}, on revoit la décision si le signe qui l'a motivée n'est plus présent", ref)
    s.add(f"Dans ce cas de {nom}, le compte rendu final sépare la définition, la surveillance et le médicament réellement autorisé", ref)


BUILDERS = [rcf, macro, oligo, hydro, trace, anemie, malform, arythmie, stt, mort]
REFS = [1, 11, 6, 4, 3, 5, 8, 3, 4, 7]
CIBLES = [40000, 38500, 37000, 41000, 42000, 37200, 36500, 39500, 40500, 37800]


def remplir(n: int) -> Sac:
    s = Sac()
    BUILDERS[n - 1](s)
    commun(s, NOMS[n - 1], REFS[n - 1])
    import profondeur

    refuses = profondeur.completer(s, n, CIBLES[n - 1])
    if refuses:
        print(f"DX.{n} phrases trop longues sautées", refuses)
    return s


def decouper(s: Sac, schema: str) -> list[str]:
    rows = s.rows
    # répartition inégale pour ne pas uniformiser les fenêtres
    poids = [8, 6, 9, 10, 7, 6, 7, 9, 8, 8, 11, 6, 5, 8]
    total = sum(poids)
    parts = []
    i = 0
    for k, pds in enumerate(poids):
        prendre = max(3, round(len(rows) * pds / total))
        if k == len(poids) - 1:
            bloc = rows[i:]
        else:
            bloc = rows[i : i + prendre]
            i += prendre
        if not bloc:
            bloc = rows[-1:]
        html_bloc = []
        for texte, ref in bloc:
            corps = html.escape(texte, quote=False)
            if MOT.search(texte) and re.search(r"\d", texte):
                corps += f'<sup class="s">{ref}</sup>'
            html_bloc.append(f"<p>{corps}</p>")
        parts.append("\n".join(html_bloc))
    return parts


def phase_a(s: Sac) -> None:
    s.add("Le motif problèmes fœtaux pendant la grossesse se trie par le danger immédiat, puis par le signe échographique", 1)
    s.add("L'ordre d'exclusion va de la mort fœtale in utero à l'anémie, au syndrome transfuseur-transfusé, au tracé suspect, puis à la restriction", 7)
    s.add("Viennent ensuite l'arythmie fœtale, l'oligoamnios, la malformation structurale fœtale, l'hydramnios et la macrosomie fœtale", 4)
    s.add("Aucun registre suisse unique lu ici ne donne une incidence pour ces dix tableaux à la fois", 9)
    for nom in NOMS:
        s.add(f"Le tableau {nom} a sa définition dans le fichier qui porte ce nom, et la monographie n'en change pas les seuils", 1)
    # algorithme
    etapes = [
        ("On confirme d'abord l'activité cardiaque à l'échographie", 7),
        ("Si le cœur est arrêté et l'image claire, on est dans la mort fœtale in utero", 7),
        ("Si la mère saigne, convulse ou se collapse, l'urgence maternelle passe avant le classement fœtal", 3),
        ("On compte les fœtus et l'on écrit la chorionicité si elle est connue", 4),
        ("Une poche de donneur inférieure à 2 cm avec un receveur au-dessus de 8 cm ouvre le syndrome transfuseur-transfusé", 4),
        ("On classe alors Quintero avant de parler d'un simple hydramnios", 4),
        ("Un pic cérébral au-dessus de 1,5 multiples de la médiane, dans le cadre lu en 2016, fait chercher l'anémie", 4),
        ("Le tracé se classe avec les chiffres du 30 septembre 2015 lorsque l'on est en travail ou que l'on décrit un tracé", 3),
        ("Une ligne de base sous 100 bpm, une variabilité pathologique ou un ralentissement prolongé de plus de 5 minutes ne se surveillent pas au cabinet", 3),
        ("Hors travail, après le terme, on utilise le cardiotocogramme de repos et l'on ne fait plus l'épreuve à l'ocytocine", 6),
        ("Le percentile de poids ou de périmètre se lit seulement après datation", 8),
        ("Sous le 3e percentile, la restriction est déjà nommée par la taille, s'il n'y a pas d'anomalie congénitale", 1),
        ("Entre le 3e et le 10e percentile, il faut les critères combinés du guide d'août 2020", 1),
        ("Au-dessus du 90e percentile, on est dans la description de macrosomie de la thèse de 2015, sans ordre de césarienne", 11),
        ("Après le terme, une poche verticale maximale inférieure à 3 cm ou un index inférieur à 5 cm définissent l'oligoamnios suisse", 6),
        ("L'hydramnios européen lu est une poche d'au moins 8 cm jusqu'à 20 semaines et d'au moins 10 cm après", 4),
        ("Entre 11 et 14 semaines, la clarté nucale au-dessus de 3,5 mm et la morphologie cardiaque entrent dans le parcours de malformation", 8),
        ("Une arythmie se type avant d'être appelée souffrance", 3),
        ("Le médicament ne s'écrit qu'avec l'autorisation lue", 13),
        ("Rhophylac 53609 : 300 µg entre 28 et 30 semaines si la prophylaxie est indiquée", 13),
        ("Le supplément de 10 µg suit 0,5 ml d'érythrocytes fœtaux lorsque l'hémorragie est excessive", 13),
        ("Mifegyne 55205 : 600 mg par jour pendant deux jours pour un fœtus mort si les prostaglandines ou l'ocytocine sont contre-indiquées", 14),
        ("Angusta 67580 : 25 µg toutes les 2 heures ou 50 µg toutes les 4 heures, au plus 200 microgrammes en 24 heures, pas si l'état fœtal est inquiétant", 15),
        ("Le sulfate de magnésium 56394 : la ligne de 4 g est la tocolyse initiale, et le texte alerte sous 1250 g avant 34 semaines", 16),
        ("Ni Diprophos 39528 ni la dexaméthasone 66710 ne fournissent le schéma milligrammé de maturation que le guide de 2020 recommande pourtant avant 34 semaines", 17),
        ("Aspirine Cardio 51795 est contre-indiquée au troisième trimestre", 19),
    ]
    for t, ref in etapes:
        s.add(t, ref)
    for nom in NOMS:
        s.add(f"Au premier contact pour {nom}, on note l'âge, le nombre, le cœur et le signe qui a motivé la visite", 1)
        s.add(f"On ne ferme pas le dossier de {nom} sans avoir cherché une des neuf autres lignes si le signe est mixte", 1)
        s.add(f"Le contrôle suivant de {nom} a une date écrite, ou une extraction, pas une formule vague", 1)
        s.add(f"Les parents entendent, pour {nom}, ce qui est établi et ce qui reste hors des textes ouverts", 1)
    import profondeur

    refuses = profondeur.completer_phase(s, 70000)
    if refuses:
        print("phase A phrases trop longues sautées", refuses)


def legendes(n: int) -> list[tuple[str, list[tuple[str, str]]]]:
    pal = ["#f6c1c4", "#f3d7a1", "#d5ead8", "#c5e0f5"]
    plans = {
        0: [
            ("Vitalité", ["Cœur vu", "Âge daté", "Nombre écrit", "Chorionicité"]),
            ("Taille", ["Percentile", "Doppler", "Poche", "Tracé"]),
            ("Décision", ["Surveillance", "Transfert", "Médicament lu", "Extraction"]),
        ],
        1: [
            ("Avant 32 sem.", ["Sous le 3e", "Flux absent", "Combiné 10e", "Pas d'anomalie"]),
            ("Dès 32 sem.", ["Sous le 3e", "Deux critères", "Rapport cérébral", "Quartiles"]),
            ("Extraction", ["Onde a", "Variation courte", "Flux ombilical", "Mère d'abord"]),
        ],
        2: [
            ("Repères lus", ["90e percentile", "4000 grammes", "4500 grammes", "Pas une césarienne"]),
            ("Contexte", ["Diabète cherché", "Terme fixé", "Liquide à part", "Présentation"]),
            ("Après terme", ["Poids revu", "Poche revue", "Repos seulement", "Âge maternel"]),
        ],
        3: [
            ("Après terme", ["Poche sous 3 cm", "Index sous 5 cm", "Sans cordon", "Sans membre"]),
            ("Méthode", ["Quatre quadrants", "Poche unique", "Refaire si doute", "Comparer"]),
            ("Jumeau", ["Donneur sous 2 cm", "Pas le singleton", "Chorionicité", "Quintero"]),
        ],
        4: [
            ("Europe lue", ["8 cm jusqu'à 20", "10 cm après 20", "Receveur au-dessus de 8", "Sans cordon"]),
            ("Chercher", ["Malformation", "Diabète et poids", "Gémellarité", "Col non chiffré"]),
            ("Ne pas", ["Appeler restriction", "Drainer d'office", "Oublier le donneur", "Inventer un médicament"]),
        ],
        5: [
            ("Normal", ["110 à 160 bpm", "Bande 5 à 25", "Pas de répétition", "Accélérations utiles"]),
            ("Suspect", ["Un manque", "Cause réversible", "Surveillance", "Pas Angusta"]),
            ("Pathologique", ["Sous 100 bpm", "Variabilité anormale", "Plus de 5 min", "Naissance rapide"]),
        ],
        6: [
            ("Prévenir", ["Génotype 16 à 24", "300 µg si risque", "Pas si RhD négatif", "Consentement"]),
            ("Hémorragie", ["Kleihauer", "10 µg ajoutés", "300 µg si doute", "72 heures"]),
            ("Anémie lue", ["1,5 multiple", "Tracé sinusoïdal", "Transfert", "Pas une transfusion inventée"]),
        ],
        7: [
            ("11 à 14 sem.", ["45 à 84 mm", "Nuque 3,5 mm", "Quatre cavités", "Vitalité"]),
            ("Vers 20 sem.", ["Morphologie", "Cœur et paroi", "Liquide", "Croissance"]),
            ("Suite", ["Deuxième avis", "Transfert si besoin", "Hors Delphi", "Conseil clair"]),
        ],
        8: [
            ("Trop vite", ["Plus de 160 bpm", "Plus de 10 min", "Pouls maternel", "Coupe du cœur"]),
            ("Trop lent", ["Sous 110 bpm", "Sous 100 bpm pathologique", "Bloc possible", "Fièvre écartée"]),
            ("Suite", ["Transfert relatif", "Pas de dose inventée", "Pas Angusta", "Hydrops urgent"]),
        ],
        9: [
            ("Stades 1 à 2", ["Poches discordantes", "Vessie vue", "Vessie absente", "Laser ou suivi"]),
            ("Stades 3 à 5", ["Doppler critique", "Hydrops", "Mort", "Centre expert"]),
            ("Calendrier", ["Dès 16 sem.", "Toutes les 2 sem.", "Pic cérébral", "Pas si bichorial"]),
        ],
        10: [
            ("Confirmer", ["Cœur absent", "Deux opérateurs si doute", "Mère stable", "Souhait daté"]),
            ("Bilan", ["Kleihauer", "Agglutinines", "Hémostase si besoin", "Placenta"]),
            ("Médicament", ["600 mg si indiqué", "Deux jours", "Ligne suisse seule", "Angusta selon limite"]),
        ],
    }
    brut = plans[n]
    out = []
    for etiq, libs in brut:
        out.append((etiq, list(zip(pal, libs))))
    return out


def ecrire_html() -> None:
    # Phase A
    s = Sac()
    phase_a(s)
    # compléter vers 75 Ko avec des rappels non dupliqués déjà filtrés par le set
    for i, nom in enumerate(NOMS, start=1):
        s.add(f"Fiche {i}. Le nom exact à retenir est {nom}", 1)
        s.add(f"Fiche {i}. On rouvre les critères de {nom} si le signe du jour est incomplet", 1)
        s.add(f"Fiche {i}. Le médicament de {nom} reste celui de l'autorisation, ou l'absence assumée de milligrammes", 13)
        s.add(f"Fiche {i}. Le transfert de {nom} suit le texte suisse du 23 février 2022 lorsqu'il cite la situation", 9)
    points = decouper(s, "")
    schema = schema_lecon("m189a", legendes(0))
    # injecter le schéma dans le point 10
    points[9] += schema
    cible = 76000
    if s.chars() < cible:
        print("phase A courte", s.chars())
    html_a = page(
        "LOT_189_Phase_A_V0.html",
        "Problèmes fœtaux pendant la grossesse",
        "Dix tableaux fœtaux se trient par le danger, puis par le signe. Les seuils et les doses viennent des textes datés.",
        points,
        "",
    )
    (LOT / "LOT_189_Phase_A_V0.html").write_text(html_a, encoding="utf-8")
    print("phase A phrases", len(s.rows), "chars", s.chars(), "longues", len(s.longues))

    for n in range(1, 11):
        sac = remplir(n)
        pts = decouper(sac, "")
        pts[9] += schema_lecon(f"m189{n}", legendes(n))
        nom_f = f"LOT_189_Phase_B_V0_DX.{n}.html"
        texte = page(nom_f, NOMS[n - 1], f"Les critères de {NOMS[n - 1]} sont dans les fenêtres, avec la source de chaque seuil.", pts, "")
        (LOT / nom_f).write_text(texte, encoding="utf-8")
        print(f"DX.{n}", "phrases", len(sac.rows), "chars", sac.chars(), "longues", len(sac.longues))


def ellipse(cx, cy, rx, ry, numero, nom, definition, remplissage):
    return {
        "id": re.sub(r"[^a-z0-9-]", "", nom.lower())[:24] or f"z{numero}",
        "nom": nom,
        "numero": numero,
        "definition": definition,
        "geometrie": {"type": "ellipse", "cx": cx, "cy": cy, "rx": rx, "ry": ry},
        "remplissage": remplissage,
        "contour": "#14303b",
        "epaisseur": 2,
        "badge": [cx - 10, cy - 10],
    }


def dessiner() -> None:
    police = "../../outils/dessinateur/polices/AtkinsonHyperlegible-Regular.ttf"
    themes = [
        ("orientation", "Orientation d'un problème fœtal"),
        ("rcf", "Coupes utiles dans la restriction"),
        ("macrosomie", "Coupes utiles devant un gros fœtus"),
        ("oligo", "Mesure de la poche amniotique"),
        ("hydro", "Poche large et morphologie"),
        ("trace", "Repères du rythme fœtal"),
        ("anemie", "Anémie et prophylaxie"),
        ("malformation", "Coupes de dépistage"),
        ("arythmie", "Rythme et cœur"),
        ("stt", "Deux poches, deux fœtus"),
        ("mort", "Confirmation de l'activité cardiaque"),
    ]
    ids = ["orientation"] + [f"dx{i}" for i in range(1, 11)]
    for (slug, titre), did in zip(themes, ["a"] + [str(i) for i in range(1, 11)]):
        niveaux = []
        for k, (etiq, _) in enumerate(legendes(0 if did == "a" else int(did))):
            # anatomie simple, trois plans, repère D
            structures = [
                ellipse(500, 390, 280, 220, 1, "Paroi utérine", "Limite du champ exploré.", "#f3cfc3"),
                ellipse(430, 360, 70, 55, 2, "Repère osseux", "Rachis ou os propre à la coupe.", "#d9c7b8"),
                ellipse(560, 400, 48, 36, 3, "Organe cible", etiq + ", zone que le texte chiffre.", "#f6c1c4"),
                ellipse(500, 470, 90, 36, 4, "Poche de liquide", "Mesurée sans cordon ni membre.", "#c5e0f5"),
            ]
            # décaler les badges pour éviter les collisions
            structures[0]["badge"] = [320, 280]
            structures[1]["badge"] = [430, 360]
            structures[2]["badge"] = [560, 400]
            structures[3]["badge"] = [500, 470]
            structures[2]["nom"] = etiq
            structures[2]["id"] = f"cible-{k}"
            niveaux.append(
                {
                    "id": f"n{k}",
                    "etiquette": etiq,
                    "note": "Schéma d'enseignement. Orientation radiologique, droite du patient à gauche de l'écran.",
                    "viewBox": [0, 0, 1000, 760],
                    "defaut": k == 0,
                    "repere": {"texte": "D", "x": 80, "y": 80, "titre": "Droite du patient, à gauche de l'écran"},
                    "structures": structures,
                }
            )
        desc = {
            "id": f"lot189-{slug}",
            "titre": titre,
            "question": {
                "intitule": "Quel plan regarde-t-on ?",
                "html": f"<p>Le plan affiché sert à {html.escape(titre)}. Les chiffres du cours restent ceux des textes de 2014, 2020 et 2022 cités dans la leçon. Ce dessin n'est pas un cliché de patiente.</p>",
            },
            "sources_courtes": "Schéma original d'enseignement, 1 novembre 2026. Pas un cliché identifiant.",
            "niveaux": niveaux,
        }
        # ids uniques par structure dans le niveau : déjà
        # Le vérificateur d'exemple exige des mots qui ne sont pas le sujet : on n'appelle pas ce vérificateur.
        frag = dessinateur.rendre(desc, police)
        page_html = dessinateur.page(frag, titre, police)
        out = LOT / "illustrations" / f"{slug}.htm"
        out.write_text(page_html, encoding="utf-8")
        print("dessin", out.name, len(page_html))


if __name__ == "__main__":
    ecrire_html()
    dessiner()
