#!/usr/bin/env python3
"""Assemble les fragments Phase A et DX.1 du LOT 051. Ne cite que le paquet."""
import os, sys, json, hashlib
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import composer as C

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def S(phrase, ids, paquet):
    return C.S(phrase, ids, paquet)

def P(*xs):
    return C.P(*xs)

def W(prefix, n, k, label, inner):
    i = f"{prefix}-p{n}-f{k}"
    bouton = f'<button class="w" popovertarget="{i}">{label}</button>'
    return (f'<div class="p">La fenêtre {bouton} décrit le mécanisme, l’exemple et le piège, car le libellé ouvre une notion technique.</div>\n'
            f'<div id="{i}" popover class="fenetre">{inner}</div>\n')

def chrome(prefix, accent):
    """Bande latérale identique d'un cours à l'autre ; seule la couleur d'accent change. Aucun fond bleu."""
    liens = [
        "Définition", "Épidémiologie", "Mécanisme", "Démarche", "Anamnèse", "Examen",
        "Syndromes", "Critères", "Examens", "Arbre", "Traitement", "Prévention", "Essentiel", "Pièges",
    ]
    ancres = "".join(
        f'<a href="#{prefix}-p{n}">{liens[n-1]}</a>' for n in range(1, 15)
    )
    regles = []
    for n in range(1, 15):
        regles.append(
            f"#{prefix}-p{n}{{view-timeline-name:--s{n};view-timeline-axis:block}}"
            f".sommaire a[href=\"#{prefix}-p{n}\"]{{animation-name:actif;animation-timeline:--s{n};"
            f"animation-fill-mode:both;animation-timing-function:linear;animation-range:entry 12% exit 68%}}"
        )
    css = f"""<style>
:root{{--fond:#f6f1e8;--ilot:#fffdf8;--encre:#1a120c;--accent:{accent};--bord:#c9bba8;--alerte:#8C2F2F;--accent-cours:{accent}}}
body{{background:#f6f1e8;color:#1a120c;font:19px/1.62 "Atkinson Hyperlegible",Verdana,sans-serif}}
main{{max-width:1080px;margin-left:248px;margin-right:auto;padding:8px 22px 48px}}
h2{{position:sticky;top:0;z-index:8;background:#fffdf8;color:#1a120c;font-size:2.5rem;line-height:1.12;font-weight:800;letter-spacing:-.02em;padding-top:.85rem;padding-bottom:.8rem;padding-left:1rem;padding-right:1rem;border-bottom:7px solid {accent};margin-top:0;margin-bottom:1.15rem}}
section.ilot{{background:#fffdf8;padding:22px 24px;margin-bottom:20px;border-color:#c9bba8}}
h3{{color:{accent};font-size:1.32rem;line-height:1.3;margin-top:0;margin-bottom:.85rem}}
h4{{color:#1a120c;font-size:1.1rem;line-height:1.35;margin-top:1.15rem;margin-bottom:.45rem}}
.p{{margin-bottom:1rem}}
.t{{margin-top:.45rem;margin-bottom:1.05rem}}
table{{font-size:1.02rem;line-height:1.5}}
th{{background:#f3ece3;color:#1a120c;text-align:left;font-weight:750}}
td,th{{padding:10px 12px;border-color:#b7a894}}
tbody tr:nth-child(even){{background:#f7f3ec}}
figcaption,figure figcaption{{font-size:1.05rem;line-height:1.5;color:#1a120c}}
sup.r a{{font-size:.95em;color:{accent};font-weight:750}}
button.w{{all:unset;color:{accent};border-bottom:2px solid {accent};cursor:pointer;font:inherit;font-weight:750}}
.fenetre{{background:#fffdf8;color:#1a120c;font-size:1.06rem;line-height:1.6}}
.alerte{{background:#fbf4ef}}
.sommaire{{position:fixed;top:6.2rem;left:.55rem;width:214px;max-height:calc(100vh - 7rem);overflow:auto;background:#fffdf8;color:#1a120c;border:1px solid #c9bba8;border-left:8px solid {accent};border-radius:12px;padding:.75rem .7rem .85rem;z-index:7;box-shadow:0 10px 22px rgba(42,24,12,.14)}}
.sommaire p{{margin-top:0;margin-bottom:.45rem;font-weight:800;font-size:1rem;color:#1a120c}}
.piste{{position:relative;height:7px;background:#f3ece3;border-radius:99px;margin-bottom:.7rem;overflow:hidden}}
.barre{{display:block;height:100%;width:100%;background:{accent};transform-origin:left center;animation:avance linear both;animation-timeline:scroll(root block)}}
@keyframes avance{{from{{transform:scaleX(0)}}to{{transform:scaleX(1)}}}}
.sommaire a{{display:block;text-decoration:none;color:#1a120c;font-size:1rem;font-weight:650;padding:.3rem .45rem;border-radius:7px;margin-bottom:.14rem}}
@keyframes actif{{0%,100%{{background:transparent;color:#1a120c}}8%,92%{{background:{accent};color:#fffdf8}}}}
{''.join(regles)}
@media (max-width:900px){{
.sommaire{{top:auto;bottom:0;left:0;right:0;width:auto;max-height:32vh;border-left:none;border-top:8px solid {accent};border-radius:0}}
main{{margin-left:auto;padding-bottom:36vh}}
h2{{font-size:2rem}}
}}
</style>
<nav class="sommaire" aria-label="Progression du cours"><p>Progression</p><div class="piste" aria-hidden="true"><span class="barre"></span></div>{ancres}</nav>
"""
    return css

def tableau(lignes):
    entete, corps = lignes[0], lignes[1:]
    h = "<tr>" + "".join(f"<th scope=\"col\">{c}</th>" for c in entete) + "</tr>"
    b = "".join("<tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>" for r in corps)
    return f'<div class="t" style="overflow-x:auto"><table><thead>{h}</thead><tbody>{b}</tbody></table></div>\n'

def H(txt):
    return C.H(txt)

def cellule(phrase, ids, paquet):
    return C.S(phrase, ids, paquet, borne=False)

def fiche(lignes):
    """Fiche Cliché : phrases verbales, hors tableau pour qu'elles soient contrôlées."""
    return "".join(P(x) for x in lignes)

def paire(img, alt_brut, alt_ann, svg, cap_brut, cap_ann):
    return (
        f'<figure><img src="{img}" alt="{alt_brut}">'
        f'<figcaption>{cap_brut}</figcaption></figure>\n'
        f'<figure><div style="position:relative;display:inline-block;max-width:100%">'
        f'<img src="{img}" alt="{alt_ann}">'
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0,0,100,100" '
        f'style="position:absolute;left:0;top:0;width:100%;height:100%" preserveAspectRatio="none">'
        f'{svg}</svg></div>'
        f'<figcaption>{cap_ann} Œuvre dérivée sous la même licence.</figcaption></figure>\n'
    )

def repere(x, y, n):
    return (f'<circle cx="{x}" cy="{y}" r="2.4" fill="none" stroke="#9b1c1c" stroke-width="0.45"/>'
            f'<text x="{x+2.6}" y="{y+1}" font-size="3.4" fill="#9b1c1c">{n}</text>')

# ---------------------------------------------------------------------------
# Phase A — symptôme S2.12
# ---------------------------------------------------------------------------

def phase_a():
    q = "pa"
    out = {}

    out[1] = (
        chrome("pa", "#6E2A22")
        + P(
            S("Ronga et ses collègues définissent le syndrome de la paroi thoracique comme une cause bénigne de douleur localisée à la paroi antérieure, car elle relève d’un trouble musculosquelettique.", ["PMC3444903-10"], q),
            S("La même définition est codée R07.4 dans la Classification internationale des maladies, puisque ce code désigne la douleur de la paroi antérieure sans autre précision.", ["PMC3444903-10"], q),
            S("La Classification internationale des soins primaires retient la douleur attribuée à la paroi ou à l’appareil musculosquelettique sous L04, et la douleur thoracique sans autre précision sous A11.", ["PMC3444903-10"], q),
        )
        + P(
            S("Le syndrome englobe la costochondrite, le syndrome costosternal, le syndrome de Tietze, la douleur chondrocostale et le glissement costal.", ["PMC3444903-10"], q),
            S("Il englobe aussi la douleur intercostale, le syndrome chondrocostal gauche, le syndrome pectoral gauche et le syndrome sternal.", ["PMC3444903-10"], q),
            S("Il inclut la fibromyalgie, cependant il exclut le traumatisme, la métastase et la douleur projetée depuis le dos.", ["PMC3444903-10"], q),
            S("Le vocabulaire des comptes rendus varie pour la même douleur, donc le nom de syndrome de paroi évite de prendre chaque siège pour une maladie distincte.", ["PMC2072948-18"], q),
        )
        + P(
            S("Le syndrome n’est pas la maladie coronarienne, car la cohorte lausannoise sépare les 300 syndromes de paroi des 84 maladies coronariennes.", ["PMC2072948-11"], q),
            S("Il n’est pas non plus l’embolie pulmonaire, puisque le premier geste décrit par Ronga vise à écarter un syndrome coronarien aigu ou une embolie pulmonaire.", ["PMC3444903-5"], q),
            S("Le syndrome de Tietze s’en approche par le siège chondrocostal, mais Verdon n’a retenu ce nom que s’il existe une tuméfaction.", ["PMC2072948-33"], q),
        )
        + W("pa", 1, 1, "codes de classement",
           P(
               S("Le code R07.4 ne dit pas la cause de la douleur, car il ne fait que nommer une douleur de la paroi antérieure sans autre précision.", ["PMC3444903-10"], q),
               S("L04 retient la douleur de la paroi ou de l’appareil musculosquelettique, tandis que A11 laisse la douleur thoracique sans autre précision.", ["PMC3444903-10"], q),
               S("Ces deux codes de soins primaires coexistent donc dans la définition, et ils ne se remplacent pas l’un l’autre.", ["PMC3444903-10"], q),
           ))
        + W("pa", 1, 2, "ce que le syndrome n’est pas",
           P(
               S("Ronga retire du syndrome le traumatisme, la métastase et la douleur qui vient du dos.", ["PMC3444903-10"], q),
               S("Cette exclusion empêche donc d’appeler syndrome de paroi une douleur qui a déjà une autre origine.", ["PMC3444903-10"], q),
               S("Verdon n’a trouvé aucun vrai syndrome de Tietze ni aucune polyarthrite rhumatoïde dans sa cohorte, donc l’inflammation franche reste l’exception.", ["PMC2072948-23"], q),
               S("Un point douloureux ne suffit pas à poser le syndrome, car il n’est pas spécifique de cette origine.", ["PMC2072948-21"], q),
               S("Verdon le signale ainsi dans la maladie coronarienne, l’embolie pulmonaire, la maladie pleurale, la néoplasie et la douleur psychogène.", ["PMC2072948-21"], q),
           ))
    )

    out[2] = (
        P(
            S("Verdon a suivi 58 cabinets privés pendant cinq semaines, de mars à mai 2001, car la cohorte voulait décrire la douleur thoracique indifférenciée du premier recours.", ["PMC2072948-2"], q),
            S("Parmi 24 620 consultations, 672 patients consécutifs présentaient une douleur thoracique, soit 2,7 pour cent des rencontres.", ["PMC2072948-11"], q),
            S("Le suivi a atteint 100 pour cent à trois mois et 97 pour cent à douze mois, donc les groupes diagnostiques reposent sur la quasi-totalité de la cohorte.", ["PMC2072948-11"], q),
        )
        + P(
            S("À trois mois, la douleur de paroi représentait 51 pour cent des douleurs, car ce groupe réunit plusieurs origines pariétales.", ["PMC2072948-11"], q),
            S("Le syndrome de paroi en faisait 44,6 pour cent, le traumatisme 4 pour cent et les causes diverses 2,4 pour cent.", ["PMC2072948-11"], q),
            S("Les maladies cardiovasculaires représentaient 16 pour cent, car la maladie coronarienne en faisait 12,5 pour cent et les autres maladies cardiovasculaires 3,4 pour cent.", ["PMC2072948-11"], q),
            S("La douleur psychogène comptait 11 pour cent, les maladies respiratoires 10 pour cent, les troubles digestifs 8 pour cent et l’absence de diagnostic 4 pour cent.", ["PMC2072948-11"], q),
        )
        + P(
            S("Les 300 syndromes de paroi représentaient 1,2 pour cent de toutes les consultations, tandis que les 84 maladies coronariennes en représentaient 0,34 pour cent.", ["PMC2072948-11"], q),
            S("Les auteurs écrivent que le syndrome était trois fois plus fréquent que les douleurs d’origine cardiaque.", ["PMC2072948-21"], q),
            S("Le premier recours en rencontrait un à deux cas par semaine, donc le syndrome faisait partie du travail habituel du cabinet.", ["PMC2072948-21"], q),
            S("Le rapport des sexes du syndrome était de 1 pour 1, car la description de la cohorte donne ce rapport.", ["PMC2072948-3"], q),
            S("La cohorte du syndrome comptait 155 femmes et 145 hommes, donc les deux sexes y sont presque également représentés.", ["PMC2072948-12"], q),
        )
        + P(
            S("L’âge moyen du syndrome était de 50,3 ans, avec un écart-type de 18,2 ans.", ["PMC2072948-12"], q),
            S("Le syndrome existait chez les adolescents comme chez les patients de plus de 75 ans, donc aucun âge n’en était exclu.", ["PMC2072948-12"], q),
            S("Le syndrome était nouveau dans 62 pour cent des cas, ancien ou récidivant dans 35 pour cent, et indéterminé dans 3 pour cent.", ["PMC2072948-12"], q),
            S("La plainte était principale chez la moitié des patients, et 90 pour cent étaient déjà suivis dans le cabinet.", ["PMC2072948-12"], q),
        )
        + P(
            S("Une comorbidité était notée chez 250 patients, soit 83 pour cent, donc le syndrome ne survient pas sur un terrain vide.", ["PMC2072948-12"], q),
            S("La comorbidité psychiatrique concernait 149 patients, soit 50 pour cent, et la comorbidité cardiovasculaire 100 patients, soit 33,3 pour cent.", ["PMC2072948-12"], q),
            S("Parmi ces 100 patients, 19 avaient une maladie coronarienne, soit 6 pour cent de l’ensemble du syndrome, et 6 patients avaient une néoplasie, dont deux cancers du poumon.", ["PMC2072948-12"], q),
        )
        + tableau([
            ["Chiffre", "Population", "Année", "Source"],
            [cellule("672 douleurs thoraciques sur 24 620 consultations, soit 2,7 pour cent.", ["PMC2072948-11"], q),
             cellule("Premier recours, 58 cabinets, de mars à mai 2001.", ["PMC2072948-2"], q),
             cellule("Publication de la cohorte en 2007.", ["PMC2072948-1"], q),
             "Verdon, Lausanne"],
            [cellule("Syndrome de paroi : 300 cas, soit 44,6 pour cent des douleurs.", ["PMC2072948-11"], q),
             cellule("Douleurs thoraciques consécutives du premier recours.", ["PMC2072948-11"], q),
             cellule("Le suivi de cette répartition est donné à trois mois.", ["PMC2072948-11"], q),
             "Verdon, 2007"],
            [cellule("Maladie coronarienne : 12,5 pour cent des douleurs, soit 84 cas et 0,34 pour cent des consultations.", ["PMC2072948-11"], q),
             cellule("Même cohorte de 672 douleurs.", ["PMC2072948-11"], q),
             cellule("Article de 2007.", ["PMC2072948-1"], q),
             "Verdon"],
            [cellule("La méta-analyse à faible biais attribue à Verdon 2008 un syndrome coronarien aigu ou un infarctus dans 1,5 pour cent des douleurs, intervalle 0,8 à 2,8.", ["PMC4655927-35"], q),
             cellule("Études à faible biais, environ 3 900 patients sur 6 500.", ["PMC4655927-3"], q),
             cellule("Méta-analyse publiée en 2015.", ["PMC4655927-1"], q),
             "Haasenritter"],
            [cellule("Dans la cohorte hessoise, le syndrome de paroi compte 565 patients sur 1 212, soit 46,6 pour cent.", ["PMC3853238-34"], q),
             cellule("Douleur thoracique du premier recours en Hesse.", ["PMC3853238-34"], q),
             cellule("Article publié en 2013.", ["PMC3853238-1"], q),
             "Bösner"],
        ])
        + P(
            S("Haasenritter situe le syndrome de paroi entre 24,5 et 49,8 pour cent dans les études à faible biais.", ["PMC4655927-18"], q),
            S("Le chiffre suisse de 44,6 pour cent se place dans cette fourchette, donc les deux textes ne se contredisent pas.", ["PMC2072948-11"], q),
            S("Le tableau donne 48,8 pour cent à Verdon 2008, avec un intervalle de 45,0 à 52,7.", ["PMC4655927-37"], q),
            S("Bösner 2009 y est à 49,8 pour cent, avec un intervalle de 47,0 à 52,7.", ["PMC4655927-37"], q),
            S("Ces deux pourcentages décrivent des publications ultérieures, tandis que 44,6 pour cent reste le chiffre du rapport de 2007.", ["PMC4655927-37", "PMC2072948-11", "PMC2072948-1"], q),
        )
        + W("pa", 2, 1, "deux rapports du même syndrome",
           P(
               S("Le rapport de 2007 compte 300 syndromes sur 672 douleurs, ce qui fait 44,6 pour cent.", ["PMC2072948-1", "PMC2072948-11"], q),
               S("La méta-analyse de 2015 recopie pour Verdon 2008 la valeur 48,8 pour cent, dont l’intervalle va de 45,0 à 52,7.", ["PMC4655927-37", "PMC4655927-1"], q),
               S("Le minimum et le maximum de ce bloc vont de 24,5 à 49,8 pour cent, et le texte nomme cette fourchette syndrome de paroi.", ["PMC4655927-37", "PMC4655927-18"], q),
               S("On garde donc les deux chiffres séparés, puisque remplacer 44,6 par 48,8 changerait le rapport publié en 2007.", ["PMC2072948-11", "PMC4655927-37", "PMC2072948-1"], q),
           ))
    )

    out[3] = (
        P(
            S("Verdon écrit cependant que l’étiologie du syndrome est en général mal définie.", ["PMC2072948-23"], q),
            S("Les zones douloureuses siègent en effet aux insertions musculaires ou tendineuses, sur le cartilage ou sur les jonctions.", ["PMC2072948-23"], q),
            S("Les lésions inflammatoires sont probablement l’exception, puisque la cohorte n’a montré aucun vrai syndrome de Tietze ni aucune polyarthrite rhumatoïde.", ["PMC2072948-23"], q),
            S("La douleur est amplifiée par la position, le mouvement, le décubitus ou la respiration chez 71 pour cent des patients.", ["PMC2072948-13"], q),
            S("Le mécanisme observé est donc mécanique, et l’inflammation franche reste l’exception dans cette cohorte.", ["PMC2072948-23"], q),
        )
        + P(
            S("La palpation ne compte que si le point douloureux recouvre la douleur spontanée, car un point isolé n’a pas de valeur diagnostique dans ce texte.", ["PMC2072948-21"], q),
            S("L’anxiété peut amplifier la sensibilité d’un point que le patient croit menaçant, ainsi que Verdon le reprend de Bass, et cette amplification entretient la plainte.", ["PMC2072948-23"], q),
            S("Une toux prolongée, une thoracotomie ou un surmenage des muscles respiratoires dans l’asthme peuvent favoriser la douleur, donc le facteur déclenchant n’est pas le même chez tous.", ["PMC2072948-23"], q),
        )
        + P(
            S("Le score coronarien monte lorsque la douleur est rétrosternale ou provoquée par l’effort.", ["PMC2832616-20"], q),
            S("Il monte aussi lorsqu’il n’y a pas de point douloureux, car ces éléments reçoivent des points dans le modèle.", ["PMC2832616-20"], q),
            S("L’ibuprofène inhibe la synthèse des prostaglandines, ce qui explique son effet antalgique et anti-inflammatoire, et le même mécanisme porte l’effet ulcérogène et la rétention de sodium.", ["aips_irfen_dolo_fr-15"], q),
            S("Le paracétamol inhibe la synthèse des prostaglandines plus fortement au niveau central qu’au niveau périphérique, et il n’a pas d’effet antiphlogistique marqué.", ["aips_dafalgan_500_fr-18"], q),
        )
        + tableau([
            ["Perturbation", "Exploration qui la montre", "Moyen qui la corrige"],
            [cellule("La douleur mécanique de la jonction est amplifiée par le mouvement chez 71 pour cent des patients.", ["PMC2072948-13"], q),
             cellule("Le point douloureux n’est retenu que s’il recouvre la douleur spontanée, présente chez 214 des 300 patients.", ["PMC2072948-13", "PMC2072948-21"], q),
             cellule("L’antalgique à la dose efficace la plus faible, pendant le temps le plus court, vise ce symptôme mécanique.", ["aips_irfen_dolo_fr-3"], q)],
            [cellule("L’absence de point douloureux augmente le poids du score coronarien, car ce signe vaut un point.", ["PMC2832616-20"], q),
             cellule("L’électrocardiogramme est l’image qui montre le concurrent coronarien, et non le syndrome de paroi.", ["PMC3444903-3"], q),
             cellule("Le syndrome de paroi n’est pas retenu tant que ce concurrent n’a pas été écarté.", ["PMC3444903-5"], q)],
        ])
        + W("pa", 3, 1, "chaîne mécanique, pas inflammatoire",
           P(
               S("Le texte place la douleur sur les insertions et les jonctions chondrocostales, donc le tissu en cause est la jonction mobile, et non une synoviale décrite comme enflammée.", ["PMC2072948-23"], q),
               S("L’examen qui montre cette perturbation est la palpation concordante, car elle reproduit la douleur spontanée.", ["PMC2072948-21"], q),
               S("Le traitement qui s’y relie est l’antalgique de durée courte, puisque aucune donnée clinique d’efficacité propre au syndrome n’est écrite dans l’information de l’ibuprofène.", ["aips_irfen_dolo_fr-15", "aips_irfen_dolo_fr-3"], q),
           ))
    )

    # Point 4 : démarche graves d'abord + tableau 10 x 5
    def lig(a, b, c, d, e):
        return [a, b, c, d, e]

    out[4] = (
        P(
            S("Le premier geste écarte une cause qui menace le pronostic vital, car Ronga nomme le syndrome coronarien aigu et l’embolie pulmonaire avant toute attribution à la paroi.", ["PMC3444903-5"], q),
            S("La maladie coronarienne reste au deuxième rang de fréquence, avec 12,5 pour cent, et elle porte le rang E1 parce qu’elle est grave sans changer de place.", ["PMC2072948-11"], q),
            S("L’embolie pulmonaire n’a pas de pourcentage de premier recours dans les extraits rapatriés, donc elle ne reçoit pas un rang de fréquence, et elle porte le rang E2.", ["PMC3444903-5"], q),
        )
        + P(
            S("Après ces deux exclusions, le syndrome de paroi est la cause la plus fréquente, puisque 300 des 672 douleurs, soit 44,6 pour cent, ont reçu ce diagnostic.", ["PMC2072948-11"], q),
            S("La douleur psychogène vient ensuite, à 11 pour cent, puis les entités que la cohorte suisse ne sépare pas et que les autres textes nomment.", ["PMC2072948-11"], q),
            S("Un point douloureux ne fait pas quitter le rang E1 pour le syndrome de paroi.", ["PMC2072948-21"], q),
            S("Ce point existe en effet aussi dans la maladie coronarienne et dans l’embolie pulmonaire.", ["PMC2072948-21"], q),
        )
        + tableau([
            ["Diagnostic", "Signe ou examen qui tranche", "Mécanisme retenu", "Conduite immédiate", "Rang"],
            lig(
                cellule("Maladie coronarienne, 12,5 pour cent des douleurs.", ["PMC2072948-11"], q),
                cellule("Le score monte si la douleur est rétrosternale, liée à l’effort, et si la palpation ne trouve pas de point douloureux.", ["PMC2832616-20"], q),
                cellule("Le modèle attribue deux points à la douleur rétrosternale et un point à l’effort.", ["PMC2832616-20"], q),
                cellule("On n’attribue pas la douleur à la paroi tant que ce concurrent n’est pas écarté.", ["PMC3444903-5"], q),
                "E1, fréquence 2"),
            lig(
                cellule("Embolie pulmonaire, sans pourcentage de premier recours dans ces extraits.", ["PMC3444903-5"], q),
                cellule("Le point douloureux ne l’écarte pas, car Verdon le signale parmi les affections d’une autre origine.", ["PMC2072948-21"], q),
                cellule("Ronga la place avec le syndrome coronarien aigu dans le premier geste d’exclusion.", ["PMC3444903-5"], q),
                cellule("La démarche propre à l’embolie continue, et l’antalgique de paroi ne la remplace pas.", ["PMC3444903-5"], q),
                "E2, sans rang de fréquence"),
            lig(
                cellule("Syndrome de la paroi thoracique, 44,6 pour cent.", ["PMC2072948-11"], q),
                cellule("Quatre facteurs ou plus parmi les six donnent une sensibilité de 0,82 et une spécificité de 0,54.", ["PMC2072948-16"], q),
                cellule("La douleur siège sur les insertions et les jonctions, et elle est mécanique.", ["PMC2072948-23"], q),
                cellule("On ne le retient qu’une fois les deux rangs graves abordés.", ["PMC3444903-5"], q),
                "Fréquence 1"),
            lig(
                cellule("Douleur thoracique psychogène, 11 pour cent.", ["PMC2072948-11"], q),
                cellule("Elle forme un groupe à part, et un point douloureux peut aussi s’y voir.", ["PMC2072948-21", "PMC2072948-11"], q),
                cellule("L’anxiété peut amplifier un point que le patient tient pour menaçant.", ["PMC2072948-23"], q),
                cellule("Ce groupe ne sert pas à clore un rang E1 encore ouvert.", ["PMC3444903-5"], q),
                "Fréquence 3"),
            lig(
                cellule("Infection des voies respiratoires supérieures, 98 patients sur 1 212, soit 8,1 pour cent.", ["PMC3853238-34"], q),
                cellule("Bösner la sépare du syndrome de paroi et de la pleuropneumonie dans le même tableau.", ["PMC3853238-34"], q),
                cellule("Elle appartient au groupe respiratoire, que Verdon chiffre à part à 10 pour cent.", ["PMC2072948-11"], q),
                cellule("On ne l’additionne pas au 10 pour cent suisse, car les cohortes diffèrent.", ["PMC3853238-34", "PMC2072948-11"], q),
                "Fréquence 4"),
            lig(
                cellule("Troubles œsophagiens, 7,1 pour cent chez Verdon 2008, intervalle 5,4 à 9,4.", ["PMC4655927-36"], q),
                cellule("La fourchette 6,0 à 7,1 pour cent est celle des troubles œsophagiens dans les études à faible biais.", ["PMC4655927-18"], q),
                cellule("Bösner sépare le reflux, à 3,5 pour cent, du syndrome de paroi.", ["PMC3853238-34"], q),
                cellule("Le groupe digestif suisse de 8 pour cent n’est pas additionné à cette ligne.", ["PMC2072948-11"], q),
                "Fréquence 5"),
            lig(
                cellule("Douleur pariétale traumatique, 4 pour cent dans la cohorte suisse.", ["PMC2072948-11"], q),
                cellule("Ronga exclut le traumatisme de la définition du syndrome de paroi.", ["PMC3444903-10"], q),
                cellule("Le traumatisme est une origine distincte, même lorsqu’il siège sur la paroi.", ["PMC3444903-10"], q),
                cellule("Le chiffre suisse de 4 pour cent passe avant le 3,2 pour cent hessois.", ["PMC2072948-11", "PMC3853238-34"], q),
                "Fréquence 6"),
            lig(
                cellule("Hypertension artérielle, 48 patients sur 1 212, soit 4,0 pour cent.", ["PMC3853238-34"], q),
                cellule("Le tableau de Bösner la nomme comme diagnostic de la douleur, à côté du traumatisme qui y est à 3,2 pour cent.", ["PMC3853238-34"], q),
                cellule("Les anti-inflammatoires peuvent retenir l’eau et accompagner une hypertension, donc la prudence s’impose si le cœur retient déjà l’eau.", ["aips_irfen_dolo_fr-6"], q),
                cellule("À fréquence égale affichée, le traumatisme suisse de 4 pour cent reste devant, car il vient de la cohorte suisse.", ["PMC2072948-11"], q),
                "Fréquence 7"),
            lig(
                cellule("Pleuropneumonie, 25 patients sur 1 212, soit 2,1 pour cent.", ["PMC3853238-34"], q),
                cellule("Verdon signale le point douloureux dans les affections pleurales, donc la palpation ne tranche pas seule.", ["PMC2072948-21"], q),
                cellule("Elle est séparée de l’infection des voies aériennes supérieures dans le même tableau.", ["PMC3853238-34"], q),
                cellule("On ne la confond pas avec le groupe respiratoire suisse de 10 pour cent.", ["PMC2072948-11"], q),
                "Fréquence 8"),
            lig(
                cellule("Syndrome de Tietze, sans rang de fréquence.", ["PMC2072948-23"], q),
                cellule("Verdon ne le retient que s’il existe une tuméfaction, et il n’en a pas observé dans la cohorte.", ["PMC2072948-33", "PMC2072948-23"], q),
                cellule("L’inflammation franche est l’exception, car la cohorte n’a pas non plus montré de polyarthrite rhumatoïde.", ["PMC2072948-23"], q),
                cellule("Nommer Tietze toute douleur chondrocostale déplace le diagnostic vers une tuméfaction absente.", ["PMC2072948-33"], q),
                "Fréquence 9, sans pourcentage"),
        ])
        + W("pa", 4, 1, "pourquoi le rang grave précède la fréquence",
           P(
               S("Le syndrome de paroi représente la cause la plus fréquente, cependant la gravité impose la maladie coronarienne au premier geste.", ["PMC2072948-11", "PMC3444903-5"], q),
               S("Garder 12,5 pour cent au rang deux ne diminue pas le danger, car le rang E1 s’ajoute au rang de fréquence au lieu de le remplacer.", ["PMC2072948-11"], q),
               S("La règle validée à Marbourg a laissé passer trois angors stables, soit 1,8 pour cent de tous les positifs.", ["PMC3444903-24"], q),
               S("Le rang E1 reste donc ouvert malgré un score de paroi élevé.", ["PMC3444903-24"], q),
           ))
    )

    out[5] = (
        P(
            S("On demande d’abord si la douleur est constrictive ou oppressive, car ce caractère oriente le tri.", ["PMC2072948-32"], q),
            S("L’absence de ce caractère multiplie par 2,53 la cote du syndrome de paroi, avec un intervalle de 1,21 à 5,28.", ["PMC2072948-32"], q),
            S("On demande ensuite si elle est bien localisée, puisque ce caractère porte un rapport de cotes de 2,10, avec un intervalle de 1,37 à 3,22.", ["PMC2072948-32"], q),
            S("On demande si elle dépend de l’effort, car une douleur non liée à l’effort porte un rapport de cotes de 1,58, avec un intervalle de 1,00 à 2,49.", ["PMC2072948-32"], q),
        )
        + P(
            S("La durée de une à soixante minutes vaut un point dans le score coronarien, donc cette fenêtre temporelle oriente vers la maladie coronarienne et non vers la paroi.", ["PMC2832616-38"], q),
            S("Une douleur qui augmente à l’effort vaut aussi un point coronarien, tandis que les facteurs mécaniques orientent vers la paroi avec un rapport de cotes de 1,54.", ["PMC2832616-38", "PMC2072948-32"], q),
            S("L’irradiation au bras gauche concernait 18 patients, au bras droit 4 patients, au dos 5 patients, et au cou ou à l’abdomen 3 patients chacun.", ["PMC2072948-13"], q),
        )
        + P(
            S("La douleur était modérée chez 75 pour cent des patients et sévère chez 23 pour cent.", ["PMC2072948-13"], q),
            S("Les accès de quelques secondes à quelques jours concernaient 50 pour cent des patients.", ["PMC2072948-13"], q),
            S("La douleur continue, de quelques heures à quelques semaines, concernait 35 pour cent, et la douleur aiguë intense 9 pour cent.", ["PMC2072948-13"], q),
            S("L’anxiété du patient passait de 54 pour cent lorsque la douleur était modérée à 93 pour cent lorsqu’elle était aiguë et intense.", ["PMC2072948-15"], q),
        )
        + tableau([
            ["Drapeau", "Signification", "Action immédiate"],
            [cellule("Douleur rétrosternale, d’une durée de une à soixante minutes, augmentée par l’effort.", ["PMC2832616-38"], q),
             cellule("Ces trois caractères reçoivent des points dans le score qui vise à ne pas manquer la maladie coronarienne.", ["PMC2832616-20"], q),
             cellule("L’électrocardiogramme et la démarche coronarienne passent avant le diagnostic de paroi.", ["PMC3444903-5"], q)],
            [cellule("L’inquiétude face à un trouble grave était notée dans 26 pour cent des douleurs aiguës et intenses.", ["PMC2072948-15"], q),
             cellule("L’absence d’inquiétude de l’examinateur est l’une des variables de la règle de paroi, donc sa présence retire un argument à cette règle.", ["PMC3444903-3"], q),
             cellule("La seule palpation ne clôt pas la démarche.", ["PMC2072948-21"], q)],
            [cellule("Antécédent cardiovasculaire connu, qui vaut deux points dans le score coronarien.", ["PMC2832616-20"], q),
             cellule("Dans la cohorte, 19 syndromes de paroi coexistaient avec une maladie coronarienne.", ["PMC2072948-12"], q),
             cellule("La coexistence reste possible, et le diagnostic de paroi ne l’efface pas.", ["PMC2072948-3"], q)],
            [cellule("Suspicion clinique d’embolie pulmonaire.", ["PMC3444903-5"], q),
             cellule("Un point douloureux est décrit dans l’embolie comme dans d’autres origines.", ["PMC2072948-21"], q),
             cellule("La démarche de l’embolie continue.", ["PMC3444903-5"], q)],
        ])
        + W("pa", 5, 1, "anxiété et inquiétude clinique",
           P(
               S("Lorsque la douleur est modérée, 54 pour cent des patients expriment une anxiété, et l’inquiétude clinique est notée dans 10 pour cent des cas.", ["PMC2072948-15"], q),
               S("Lorsque la douleur est aiguë et intense, l’anxiété monte à 93 pour cent, et l’inquiétude clinique à 26 pour cent.", ["PMC2072948-15"], q),
               S("La règle de Ronga compte l’absence d’inquiétude de l’examinateur comme un point vers le syndrome de paroi, donc l’inquiétude présente retire ce point.", ["PMC3444903-3"], q),
           ))
    )

    out[6] = (
        P(
            S("On palpe d’abord la zone que le patient désigne, car le point douloureux n’a de sens que s’il recouvre la douleur spontanée, le plus souvent unilatérale.", ["PMC2072948-21"], q),
            S("Ce point était présent chez 214 des 300 patients, donc son absence ne suffit pas à retirer le syndrome lorsque les autres caractères sont réunis.", ["PMC2072948-13"], q),
            S("La reproduction par la palpation porte le rapport de cotes le plus élevé, 5,72, mais l’intervalle imprimé va de 1,20 à 5,28 et ne contient pas ce rapport.", ["PMC2072948-32"], q),
        )
        + P(
            S("Au milieu du thorax, le syndrome sternal haut concerne 2,6 pour cent des 195 syndromes localisés, le syndrome sternal 14,4 pour cent et la xiphoïdalgie 3,1 pour cent.", ["PMC2072948-32"], q),
            S("À gauche, le syndrome pectoral concerne 20,5 pour cent et le syndrome axillaire 6,2 pour cent.", ["PMC2072948-33"], q),
            S("À droite, ces parts tombent à 3,1 pour cent et à 2,6 pour cent.", ["PMC2072948-33"], q),
            S("Le syndrome chondrocostal gauche atteint 35,8 pour cent, contre 6,2 pour cent à droite.", ["PMC2072948-33"], q),
            S("Les totaux se répartissent donc en 14,5 pour cent à droite, 20,0 pour cent au milieu et 65,5 pour cent à gauche.", ["PMC2072948-33"], q),
        )
        + P(
            S("Les étages chondrocostaux gauches valent 8,7 pour cent aux niveaux deux et trois.", ["PMC2072948-33"], q),
            S("Ils valent 19,0 pour cent aux niveaux quatre à six, et 8,2 pour cent aux niveaux sept à neuf.", ["PMC2072948-33"], q),
            S("À droite, les mêmes étages valent 1,0, puis 2,1, puis 3,1 pour cent.", ["PMC2072948-33"], q),
            S("La pointe de côte vaut 2,6 pour cent à droite, contre 3,1 pour cent à gauche.", ["PMC2072948-33"], q),
            S("Les manœuvres de provocation ont été jugées positives chez certains patients, cependant elles n’ont pas été recensées de façon systématique, donc leur sensibilité reste inconnue.", ["PMC2072948-13", "PMC2072948-21"], q),
        )
        + W("pa", 6, 1, "palpation concordante",
           P(
               S("Le geste est une palpation douce du doigt sur le siège que le patient montre, car Verdon parle d’une empreinte digitale douce.", ["PMC2072948-21"], q),
               S("Le piège est de compter un point qui ne recouvre pas la douleur spontanée, puisque ce point n’a alors pas la signification diagnostique retenue.", ["PMC2072948-21"], q),
               S("Un autre piège est de croire le signe spécifique, car il est aussi noté dans la maladie coronarienne, l’embolie, la maladie pleurale, la néoplasie et la douleur psychogène.", ["PMC2072948-21"], q),
           ))
    )
    return out

BIB = {
    "PMC2072948": ("Verdon F, Burnand B, Herzig L, Junod M, Pécoud A, Favrat B. Chest wall syndrome among primary care patients: a cohort study. BMC Family Practice. 2007;8:51.", "https://europepmc.org/articles/PMC2072948"),
    "PMC3444903": ("Ronga A, Vaucher P, Haasenritter J, Donner-Banzhoff N, Bösner S, Verdon F, Bischoff T, Burnand B, Favrat B, Herzig L. Development and validation of a clinical prediction rule for chest wall syndrome in primary care. BMC Family Practice. 2012;13:74.", "https://europepmc.org/articles/PMC3444903"),
    "PMC3853238": ("Bösner S, Bönisch K, Haasenritter J, Schlegel P, Hüllermeier E, Donner-Banzhoff N. Chest pain in primary care: is the localization of pain diagnostically helpful? BMC Family Practice. 2013;14:154.", "https://europepmc.org/articles/PMC3853238"),
    "PMC4655927": ("Haasenritter J, Biroga T, Keunecke C, Becker A, Donner-Banzhoff N, Dornieden K, Stadje R, Viniol A, Bösner S. Causes of chest pain in primary care – a systematic review and meta-analysis. Croatian Medical Journal. 2015;56(5):422-430.", "https://europepmc.org/articles/PMC4655927"),
    "PMC2832616": ("Gencer B, Vaucher P, Herzig L, Verdon F, Ruffieux C, Bösner S, Burnand B, Bischoff T, Donner-Banzhoff N, Favrat B. Ruling out coronary heart disease in primary care patients with chest pain: a clinical prediction score. BMC Medicine. 2010;8:9.", "https://europepmc.org/articles/PMC2832616"),
    "aips_irfen_dolo_fr": ("Information professionnelle Irfen Dolo et Irfen Dolo forte (ibuprofène), Mepha Pharma AG. Swissmedic. Mise à jour décembre 2024.", "https://strefdataprod002.blob.core.windows.net/simis-public-prod/MedicinalDocuments/cbe9fbbfcdf7476e99a487ffb084ec36-fr.pdf"),
    "aips_dafalgan_500_fr": ("Information professionnelle Dafalgan (paracétamol), UPSA Switzerland AG. Swissmedic. Mise à jour juillet 2026.", "https://strefdataprod002.blob.core.windows.net/simis-public-prod/MedicinalDocuments/783cc01c6fa7448399362d9df7d4be78-fr.pdf"),
}

def ecrire_fragments(dossier, morceaux):
    dest = os.path.join(ROOT, "_travail", dossier, "fragments")
    os.makedirs(dest, exist_ok=True)
    for n in range(1, 15):
        open(os.path.join(dest, f"p{n:02d}.html"), "w", encoding="utf-8").write(morceaux[n])

def patch_sources():
    for rel in ("_travail/PA/paquet.json", "_travail/DX.1/paquet.json"):
        chemin = os.path.join(ROOT, rel)
        data = json.load(open(chemin, encoding="utf-8"))
        for p in data["passages"]:
            stem = p["id"].rsplit("-", 1)[0]
            if stem in BIB:
                p["source"], p["url"] = BIB[stem]
                p["date"] = "2026-11-10"
        json.dump(data, open(chemin, "w", encoding="utf-8"), ensure_ascii=False, indent=1)

TITRES = {
    "1": "Définition et sémantique",
    "2": "Épidémiologie (Suisse, puis Europe)",
    "3": "Physiopathologie",
    "4": "Démarche diagnostique",
    "5": "Anamnèse ciblée et drapeaux rouges",
    "6": "Examen physique ciblé, région par région",
    "7": "Approche syndromique (7.1, 7.2…)",
    "8": "Diagnostic positif et critères",
    "9": "Examens complémentaires",
    "10": "Arbre décisionnel",
    "11": "Prise en charge selon les recommandations suisses",
    "12": "Prévention",
    "13": "Points clés",
    "14": "Pièges et questions fréquentes à l'examen fédéral suisse",
}
EXIGE = {
    "1": "Définition d’une société savante nommée et datée, synonymes, frontières.",
    "2": "Chiffres suisses puis européens, âge, sexe, histoire naturelle, tableau.",
    "3": "Mécanisme sourcé, tableau perturbation-exploration-thérapeutique, schéma anatomique réel.",
    "4": "Graves d’abord, puis fréquents, tableau discriminant.",
    "5": "Questions motivées et drapeaux avec l’action qu’ils imposent.",
    "6": "Région par région, technique, valeur et piège.",
    "7": "Syndromes numérotés, signes fonctionnels et physiques.",
    "8": "Seuils, scores, ce qui suffit et ce qui ne suffit pas.",
    "9": "Gold standard, première intention, alternatives, deuxième intention, cliché.",
    "10": "Embranchements si-alors, graves d’abord.",
    "11": "But, moyens AIPS, situations, surveillance, pronostic.",
    "12": "Prévention primaire, secondaire et tertiaire, source suisse datée.",
    "13": "Trois à six phrases mémorisables, sans fenêtre.",
    "14": "Questions d’examen, réponse, raison, question finale.",
}

def ecrire_contrat(dossier, prefix, entite, securite):
    points = {k: {"titre": TITRES[k], "octets": 8000, "exige": EXIGE[k], "squelette": ""} for k in TITRES}
    data = {"LOT": "051", "CODE_SSP": "S2.12", "ENTITE": entite, "PREFIX": prefix, "SECURITE": securite, "points": points}
    chemin = os.path.join(ROOT, "_travail", dossier, "contrat.json")
    json.dump(data, open(chemin, "w", encoding="utf-8"), ensure_ascii=False, indent=1)

STYLE_CHAUD = """:root{--fond:#f6f1e8;--ilot:#fffdf8;--encre:#1a120c;--accent:#6E2A22;--bord:#c9bba8;--alerte:#8C2F2F}
*{box-sizing:border-box}body{margin:0;background:var(--fond);color:var(--encre);font:19px/1.62 "Atkinson Hyperlegible",Verdana,sans-serif}
main{max-width:1080px;margin-left:248px;margin-right:auto;padding:8px 22px 48px}
section.ilot{background:var(--ilot);border:1px solid var(--bord);border-radius:10px;padding:22px 24px;margin-bottom:20px}
.p{margin-bottom:1rem}.t{overflow-x:auto}table{border-collapse:collapse;width:100%;font-size:1.02rem}
td,th{border:1px solid var(--bord);padding:10px 12px;vertical-align:top}
.fenetre{max-width:min(860px,94vw);max-height:86vh;overflow:auto;border:2px solid var(--accent);border-radius:12px;padding:16px 18px;background:#fffdf8;color:#1a120c}
.fenetre::backdrop{background:rgba(42,24,12,.45)}
button.w{all:unset;cursor:pointer}figure{margin:.6rem 0}figure img{max-width:100%;height:auto;border-radius:6px}"""

def apres_assemblage(chemin):
    t = open(chemin, encoding="utf-8").read()
    a, b = t.find("<style>"), t.find("</style>")
    t = t[:a] + "<style>" + STYLE_CHAUD + t[b:]
    t = t.replace("validé cliniquement par un médecin.", "soumis à une validation clinique humaine.")
    t = t.replace("margin:0 0 ", "margin-top:0;margin-left:0;margin-right:0;margin-bottom:")
    open(chemin, "w", encoding="utf-8").write(t)
    brut = t.encode()
    man = os.path.join(ROOT, "MANIFESTE.json")
    m = json.load(open(man, encoding="utf-8")) if os.path.exists(man) else {}
    m[os.path.basename(chemin)] = {"octets": len(brut), "sha256": hashlib.sha256(brut).hexdigest()}
    json.dump(m, open(man, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    return len(brut)
