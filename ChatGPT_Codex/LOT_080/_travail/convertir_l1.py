#!/usr/bin/env python3
"""Conversion Lo (popover) → L1 (:target) pour LOT_080, Phase A et DX.1.
Ne touche que les fichiers passés en argument. Prompt L1 lu et appliqué.
"""
import re
import sys
from pathlib import Path

SOSORT = "https://link.springer.com/article/10.1186/s13013-017-0145-8"
PAED = "https://www.paediatrieschweiz.ch/fr/examen-clinique-et-radiologique-scoliose"
PAED17 = "https://www.paediatrieschweiz.ch/fr/scolioses/"


def fin_div(html, start):
    """Index juste après le </div> qui ferme le <div> ouvert avant start."""
    prof = 1
    for m in re.finditer(r"<(/?)div\b[^>]*>", html[start:], re.I):
        prof += -1 if m.group(1) else 1
        if prof == 0:
            return start + m.end()
    raise SystemExit("div non fermé")


def convertir_fenetres(html):
    out = []
    i = 0
    while True:
        j = html.find("<div id=", i)
        if j < 0:
            out.append(html[i:])
            break
        k = html.find(">", j)
        ouvre = html[j:k + 1]
        if "popover" in ouvre and "fenetre" in ouvre:
            wid = re.search(r'id="([^"]+)"', ouvre).group(1)
            fin = fin_div(html, k + 1)
            inner = html[k + 1:fin]
            inner = re.sub(r"</div>\s*$", "", inner, count=1)
            hm = re.search(r"<h5>(.*?)</h5>", inner, re.S)
            label = re.sub(r"<[^>]+>", "", hm.group(1) if hm else wid)
            label = re.sub(r"\s+", " ", label).strip().replace('"', "")
            bloc = (
                f'<section class="fenetre" id="{wid}" role="dialog" aria-label="{label}">'
                f'<div class="fen"><a class="fermer" href="#" aria-label="Fermer">Fermer ✕</a>'
                f"{inner}</div></section>"
            )
            out.append(html[i:j])
            out.append(bloc)
            i = fin
        else:
            out.append(html[i:k + 1])
            i = k + 1
    html = "".join(out)
    html = re.sub(
        r'<button class="w" popovertarget="([^"]+)">(.*?)</button>',
        r'<a class="ouvre" href="#\1">\2</a>',
        html,
        flags=re.S,
    )
    return html


def propre_id(i):
    s = i
    s = re.sub(r"audit-?", "", s, flags=re.I)
    s = re.sub(r"prompt-?", "", s, flags=re.I)
    s = re.sub(r"-+", "-", s).strip("-")
    if not s.startswith("sb-"):
        s = "sb-" + s
    return s


def consolider_sources(html):
    m = re.search(r"(<h3>Sources</h3><ol>)(.*?)(</ol>)", html, re.S)
    if not m:
        raise SystemExit("bibliographie absente")
    lis = re.findall(r'<li id="(sb-[^"]+)">(.*?)</li>', m.group(2), re.S)
    url_premier = {}
    id_vers = {}
    for i, contenu in lis:
        if "prompt-question" in i or "PROMPT_" in contenu or "PROMPT_LOTS" in contenu:
            id_vers[i] = None
            continue
        u = re.search(r"https?://[^<\s]+", contenu)
        url = u.group(0) if u else "local:" + i
        if url not in url_premier:
            cid = propre_id(i)
            url_premier[url] = [cid, contenu, i]
        id_vers[i] = url_premier[url][0]
    pris = set()
    for url, triple in url_premier.items():
        cid = triple[0]
        base, n = cid, 2
        while cid in pris:
            cid = f"{base}-{n}"
            n += 1
        triple[0] = cid
        pris.add(cid)
    for i, contenu in lis:
        if id_vers.get(i):
            u = re.search(r"https?://[^<\s]+", contenu)
            url = u.group(0) if u else "local:" + i
            id_vers[i] = url_premier[url][0]

    def remplace_lien(mm):
        ancien = mm.group(1)
        if ancien not in id_vers:
            return mm.group(0)
        if id_vers[ancien] is None:
            return ""
        neuf = id_vers[ancien]
        lib = neuf[3:] if neuf.startswith("sb-") else neuf
        return f'<a href="#{neuf}">{lib}</a>'

    items = []
    for url, (cid, contenu, _orig) in url_premier.items():
        lib = cid[3:] if cid.startswith("sb-") else cid
        corps = re.sub(r"^\[[^\]]+\]\s*", "", contenu).strip()
        corps = re.sub(r"\baudit\b", "relecture", corps, flags=re.I)
        items.append(f'<li id="{cid}">[{lib}] {corps}</li>')
    # Indices calculés avant toute réécriture des liens, sinon la fin du fichier est tronquée.
    html = html[:m.start(2)] + "".join(items) + html[m.end(2):]
    html = re.sub(r'<a href="#(sb-[^"]+)">[^<]*</a>', remplace_lien, html)
    html = re.sub(r"<sup class=\"r\">\s*</sup>", "", html)
    html = re.sub(
        r'(<sup class="r"><a href="(#[^"]+)">[^<]*</a></sup>)(?:\s*<sup class="r"><a href="\2">[^<]*</a></sup>)+',
        r"\1",
        html,
    )
    return html, {url: triple[0] for url, triple in url_premier.items()}


def retirer_question_finale(html):
    html = re.sub(
        r'<div class="p"[^>]*>\s*(?:<strong>)?Question finale.*?</div>',
        "",
        html,
        flags=re.S,
    )
    html = re.sub(
        r'<div class="p" id="[^"]*question-finale"[^>]*>.*?</div>',
        "",
        html,
        flags=re.S,
    )
    return html


def deplacer_apres_h4(html, section_id, h4_debut, destination_id):
    """Déplace le HTML depuis un h4 jusqu'à la fin de la section, juste après le h3 de destination."""
    sec = re.search(rf'<section class="ilot" id="{section_id}">', html)
    if not sec:
        return html
    fin_sec = html.find('<section class="ilot"', sec.end())
    if fin_sec < 0:
        return html
    bloc = html[sec.start():fin_sec]
    i = bloc.find(h4_debut)
    if i < 0:
        print("h4 introuvable", section_id, h4_debut[:40])
        return html
    garde, bouge = bloc[:i], bloc[i:]
    bouge_corps = re.sub(r"</section>\s*$", "", bouge)
    html = html[:sec.start()] + garde + "</section>" + html[fin_sec:]
    dest = re.search(rf'(<section class="ilot" id="{destination_id}"><h3[^>]*>.*?</h3>)', html, re.S)
    if not dest:
        print("destination absente", destination_id)
        return html
    return html[:dest.end()] + bouge_corps + html[dest.end():]


def cite(cid):
    lib = cid[3:] if cid.startswith("sb-") else cid
    return f'<sup class="r"><a href="#{cid}">{lib}</a></sup>'


def inserer_avant(html, marque, fragment):
    """Insère le fragment dans la section qui précède la balise `marque`."""
    i = html.find(marque)
    if i < 0:
        print("marque absente", marque[:70])
        return html
    fermeture = html.rfind("</section>", 0, i)
    if fermeture < 0:
        print("fermeture absente avant", marque[:70])
        return html
    return html[:fermeture] + fragment + html[fermeture:]


def completer(html, urls, phase_a):
    so = urls.get(SOSORT)
    pe = urls.get(PAED)
    if not so or not pe:
        print("ancre manquante", "sosort" if not so else "", "paed" if not pe else "")
        return html
    cso, cpe = cite(so), cite(pe)
    if phase_a:
        p2 = (
            '<h4><em>2.e Le retentissement collectif se lit dans la fonction, pas dans un taux de décès</em></h4>'
            f'<div class="p">SOSORT retient le plus souvent une fréquence de 2 à 3 % pour la scoliose idiopathique au-dessus de 10°, malgré une fourchette publiée beaucoup plus large{cso}.</div>'
            f'<div class="p">Environ 10 % des cas diagnostiqués relèvent d’un traitement conservateur, tandis que 0,1 à 0,3 % relèvent d’une correction opératoire{cso}.</div>'
            f'<div class="p">Lorsqu’une courbure dépasse 50° en fin de croissance, la progression adulte est jugée presque certaine, avec des problèmes de santé et une qualité de vie réduite{cso}.</div>'
            f'<div class="p">Une déformation sévère non traitée peut limiter la capacité du thorax, l’exercice et le travail, ce qui place l’enjeu dans la fonction quotidienne{cso}.</div>'
        )
        p3 = (
            '<h4><em>3.f Le niveau moléculaire reste sans chaîne unique établie</em></h4>'
            f'<div class="p">SOSORT écrit que l’étiopathogénie de la scoliose n’est pas élucidée, donc aucune voie moléculaire unique ne doit être présentée comme acquise{cso}.</div>'
            f'<div class="p">Les facteurs génétiques sont mis en avant, puisque la déformation survient volontiers dans certaines familles, sans mode de transmission unique retenu{cso}.</div>'
            f'<div class="p">Le rôle de la mélatonine est aujourd’hui tenu pour limité, alors que des travaux n’ont pas montré de différence avec un groupe sain{cso}.</div>'
            f'<div class="p">La chaîne utile au clinicien relie ensuite la croissance, la torsion du tronc et l’angle de Cobb, tandis que le corset vise d’abord à stopper la progression{cso}.</div>'
        )
        p11 = (
            '<h4><em>11.E Situations particulières, pronostic et critères de sortie</em></h4>'
            f'<div class="p">SOSORT recommande le corset au-delà de 20° plus ou moins 5°, si le patient grandit encore entre Risser 0 et 3 et si une progression ou un risque élevé est démontré{cso}.</div>'
            f'<div class="p">Le port initial devrait couvrir la journée ou au moins 18 heures, sauf justification d’un clinicien spécialisé du traitement conservateur{cso}.</div>'
            f'<div class="p">En dessous de 15° plus ou moins 5°, le corset ne devrait pas être proposé, sauf justification spécialisée consignée par ce même clinicien{cso}.</div>'
            f'<div class="p">Paediatrica indique que les courbures inférieures à 45° en fin de puberté restent en général stables pendant des décennies, jusqu’à la ménopause{cpe}.</div>'
            f'<div class="p">Elles peuvent s’aggraver lorsque des processus dégénératifs liés à l’âge s’installent, donc un contrôle tardif reste possible tous les 5 ans selon la clinique{cpe}.</div>'
            f'<div class="p">Le sevrage du corset vise le stade de Risser III ou IV, puis un contrôle est prévu 1 à 2 ans après l’arrêt afin d’écarter une progression lente{cpe}.</div>'
            '<div class="p">Chez la femme enceinte, le protocole d’imagerie propre à cette déformation n’est pas détaillé dans les textes lus : Référence non vérifiée pour cette fiche.</div>'
            '<div class="p">Le remboursement suisse du corset n’est pas extrait d’un texte d’assurance lu pour cette fiche : Référence non vérifiée pour cette fiche.</div>'
        )
        html = inserer_avant(html, '<section class="ilot" id="pa-p3">', p2)
        html = inserer_avant(html, '<section class="ilot" id="pa-p4">', p3)
        html = inserer_avant(html, '<section class="ilot" id="pa-p12">', p11)
    else:
        p3 = (
            '<h4><em>3.f Ce que l’on sait au niveau familial et ce qui reste sans chaîne unique</em></h4>'
            f'<div class="p">Pour la scoliose idiopathique, SOSORT constate que l’étiopathogénie n’est pas élucidée, donc le clinicien ne dispose pas d’une cause moléculaire unique à corriger{cso}.</div>'
            f'<div class="p">La tendance familiale soutient une participation génétique, cependant aucun mode de transmission n’est retenu comme règle de conseil{cso}.</div>'
            f'<div class="p">La mélatonine n’occupe plus qu’une place limitée, après des comparaisons qui n’ont pas séparé les adolescentes scoliotiques d’un groupe sain{cso}.</div>'
            f'<div class="p">On relie malgré cela la poussée de croissance, la torsion vertébrale et la gibbosité, puis l’on mesure l’angle qui décidera du corset{cso}.</div>'
        )
        p7 = (
            '<h4><em>7.6 Chaque signe neurologique ou respiratoire a son geste</em></h4>'
            f'<div class="p">Les <a class="ouvre" href="#dx1-p7-reflexes">réflexes abdominaux</a> se recherchent par un trait cutané léger de dehors en dedans, car une asymétrie oriente vers une atteinte médullaire{cpe}.</div>'
            '<section class="fenetre" id="dx1-p7-reflexes" role="dialog" aria-label="Réflexes abdominaux">'
            '<div class="fen"><a class="fermer" href="#" aria-label="Fermer">Fermer ✕</a>'
            '<h5>Réflexes abdominaux</h5>'
            f'<div class="p">Le geste part de la fosse iliaque vers la ligne médiane, des deux côtés, afin de comparer la contraction des muscles larges{cpe}.</div>'
            f'<div class="p">Une réponse absente d’un seul côté, chez un adolescent mince, doit faire discuter une malformation intraspinale plutôt qu’un simple oubli d’examen{cpe}.</div>'
            '</div></section>'
            f'<div class="p">La <a class="ouvre" href="#dx1-p7-force">force des membres</a> se cote segment par segment, puisqu’un déficit nouveau change l’urgence et impose une imagerie sans attendre le contrôle orthopédique{cpe}.</div>'
            '<section class="fenetre" id="dx1-p7-force" role="dialog" aria-label="Force segmentaire">'
            '<div class="fen"><a class="fermer" href="#" aria-label="Fermer">Fermer ✕</a>'
            '<h5>Force segmentaire</h5>'
            f'<div class="p">On oppose une résistance à la flexion et à l’extension des hanches, des genoux et des chevilles, puis l’on note le côté le plus faible{cpe}.</div>'
            '<div class="p">La marche sur talons et sur pointes complète ce geste, donc un faiblissement unilatéral ne se résume pas à une boiterie d’inégalité de longueur.</div>'
            '</div></section>'
            f'<div class="p">La <a class="ouvre" href="#dx1-p7-souffle">capacité respiratoire</a> s’apprécie d’abord par l’effort et le thorax, car les troubles décrits concernent surtout les courbures thoraciques sévères{cso}.</div>'
            '<section class="fenetre" id="dx1-p7-souffle" role="dialog" aria-label="Retentissement respiratoire">'
            '<div class="fen"><a class="fermer" href="#" aria-label="Fermer">Fermer ✕</a>'
            '<h5>Retentissement respiratoire</h5>'
            f'<div class="p">On demande à l’adolescent de monter un étage et de décrire l’essoufflement, puis l’on observe l’ampliation du côté de la gibbosité{cso}.</div>'
            f'<div class="p">SOSORT place la prévention du trouble respiratoire parmi les buts du traitement conservateur, surtout lorsque la courbure thoracique est majeure{cso}.</div>'
            '</div></section>'
        )
        p9 = (
            '<h4><em>9.e Lorsque l’IRM manque ou lorsque la patiente est enceinte</em></h4>'
            f'<div class="p">Paediatrica réserve l’IRM ambulatoire aux douleurs qui durent plus de 6 à 12 semaines, aux signes neurologiques peu clairs et aux courbures atypiques{cpe}.</div>'
            f'<div class="p">Une courbure thoracique convexe à gauche, ou une courbure sans rotation, devrait donc faire demander cette IRM, même si la douleur reste modeste{cpe}.</div>'
            f'<div class="p">Si l’IRM est impossible, le texte suisse maintient la radiographie debout et l’examen neurologique, et il réserve la tomodensitométrie à une question osseuse précise{cpe}.</div>'
            f'<div class="p">La tomodensitométrie ne remplace pas la lecture de la moelle, donc une suspicion de syringomyélie ne se clôt pas sur un cliché osseux normal{cpe}.</div>'
            '<div class="p">Le choix d’imagerie chez l’adolescente enceinte n’est pas écrit dans les recommandations lues pour cette fiche : Référence non vérifiée pour cette fiche.</div>'
        )
        p11 = (
            '<h4><em>11.E Assurance, heures de port et sortie de surveillance</em></h4>'
            f'<div class="p">Au début, le corset devrait être porté à temps plein ou au moins 18 heures par jour, sauf justification d’un clinicien spécialisé{cso}.</div>'
            f'<div class="p">L’essai rapporté par SOSORT a obtenu 72 % de succès sous corset contre 48 % sous observation, le seuil opératoire étant une courbure d’au moins 50°{cso}.</div>'
            f'<div class="p">Ces pourcentages décrivent l’essai, donc ils ne promettent pas le même résultat à chaque adolescent appareillé{cso}.</div>'
            f'<div class="p">La sortie du corset vise Risser III ou IV, puis un cliché sans orthèse est prévu 1 à 2 ans plus tard pour écarter une progression lente{cpe}.</div>'
            f'<div class="p">Avant ce cliché sans corset, l’orthèse doit être retirée pendant 48 heures, afin que la correction observée soit réaliste{cpe}.</div>'
            '<div class="p">La prise en charge du corset par l’assurance obligatoire n’est pas extraite d’un texte lu pour cette fiche : Référence non vérifiée pour cette fiche.</div>'
        )
        p12 = (
            '<div class="p">La prévention primaire d’une cause n’est pas établie, puisque l’étiopathogénie reste non élucidée et qu’aucun geste populationnel ne supprime la déformation{cso}.</div>'
            f'<div class="p">La prévention secondaire est la détection pendant la croissance, avant qu’une courbure modérée ne franchisse le domaine où le corset est recommandé{cpe}.</div>'
            f'<div class="p">La prévention tertiaire vise à limiter la progression, la gêne respiratoire et la douleur, ce qui correspond aux buts conservateurs énoncés par SOSORT{cso}.</div>'
        )
        html = inserer_avant(html, '<section class="ilot" id="dx1-p4">', p3)
        html = inserer_avant(html, '<section class="ilot" id="dx1-p8">', p7)
        html = inserer_avant(html, '<section class="ilot" id="dx1-p10">', p9)
        html = inserer_avant(html, '<section class="ilot" id="dx1-p12">', p11)
        marque12 = '<section class="ilot" id="dx1-p12">'
        j = html.find(marque12)
        h3fin = html.find("</h3>", j)
        html = html[:h3fin + 5] + p12 + html[h3fin + 5:]
        html = html.replace(
            "<h4><em>12.a La détection précoce conserve une démarche de sélection</em></h4>",
            "<h4><em>12.a Prévention secondaire : détecter avant la progression</em></h4>",
            1,
        )
        html = html.replace(
            "<h4><em>12.b Le suivi vise la prévention de progression évitable</em></h4>",
            "<h4><em>12.b Prévention tertiaire : limiter la progression et le retentissement</em></h4>",
            1,
        )
        html = html.replace(
            "<h4><em>12.c L'exposition radiologique est limitée à ce qui aide la décision</em></h4>",
            "<h4><em>12.c Prévention tertiaire : ne pas irradier sans décision</em></h4>",
            1,
        )
    html = html.replace("proposé pour contrelecture", "donc qualitatif")
    html = html.replace("1. Définition et sémantique", "1. Définition")
    return html


def main():
    for chemin in sys.argv[1:]:
        p = Path(chemin)
        html = p.read_text(encoding="utf-8")
        html = convertir_fenetres(html)
        html = retirer_question_finale(html)
        if "pa-p1" in html:
            html = deplacer_apres_h4(
                html, "pa-p1", "<h4><em>1.b", "pa-p8",
            )
        if "dx1-p1" in html:
            html = deplacer_apres_h4(
                html, "dx1-p1", "<h4><em>1.c", "dx1-p4",
            )
        html, urls = consolider_sources(html)
        html = completer(html, urls, "Phase_A" in p.name)
        # completer uses current html which already moved; phase_a flag:
        # bug: I passed phase based on html after edits which still has pa-p1 if phase A.
        p.write_text(html, encoding="utf-8")
        print(p.name, len(html.encode()), "sosort", urls.get(SOSORT), "paed", urls.get(PAED))


if __name__ == "__main__":
    main()
