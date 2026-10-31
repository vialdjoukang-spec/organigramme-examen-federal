# -*- coding: utf-8 -*-
"""Schémas SVG. Le survol lit l'élément title. Le clic ouvre une définition."""
import html


COULEURS = {
    "ok": "#1a7a50",
    "non": "#a1262f",
    "soi": "#0b5d86",
    "entete": "#14303b",
}


def _cell(x, y, w, h, cls, label, title):
    fill = COULEURS[cls]
    return (
        f'<g class="cell"><title>{html.escape(title)}</title>'
        f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="5" fill="{fill}" stroke="#ffffff" stroke-width="1"/>'
        f'<text fill="#ffffff" font-size="12" font-family="Verdana, sans-serif" font-weight="700" '
        f'x="{x + w/2}" y="{y + 21}" text-anchor="middle">{html.escape(label)}</text>'
        f"</g>"
    )


def _entete(x, y, w, h, label):
    return (
        f'<g><rect x="{x}" y="{y}" width="{w}" height="{h}" rx="4" fill="#14303b"/>'
        f'<text fill="#ffffff" font-size="11" font-family="Verdana, sans-serif" font-weight="700" '
        f'x="{x + w/2}" y="{y + 18}" text-anchor="middle">{html.escape(label)}</text></g>'
    )


GROUPES = ("O", "A", "B", "AB")


def phrase_donneur(g):
    if g == "O":
        return "Le donneur ne porte ni l'antigène A ni l'antigène B"
    if g == "AB":
        return "Le donneur porte les antigènes A et B"
    return f"Le donneur porte l'antigène {g}"


def phrase_receveur_ac(g):
    if g == "AB":
        return "Le receveur n'a pas d'anticorps ABO naturels"
    if g == "O":
        return "Le receveur a des anticorps anti-A et anti-B"
    if g == "A":
        return "Le receveur a un anticorps anti-B"
    return "Le receveur a un anticorps anti-A"


def phrase_plasma(g):
    if g == "AB":
        return "Ce plasma ne contient pas d'anticorps anti-A ni anti-B"
    if g == "O":
        return "Ce plasma contient des anticorps anti-A et anti-B"
    if g == "A":
        return "Ce plasma contient un anticorps anti-B"
    return "Ce plasma contient un anticorps anti-A"


def phrase_receveur_ag(g):
    if g == "O":
        return "Le receveur ne porte ni l'antigène A ni l'antigène B"
    if g == "AB":
        return "Le receveur porte les antigènes A et B"
    return f"Le receveur porte l'antigène {g}"


def gr_ok(donneur, receveur):
    # Le receveur ne doit pas avoir d'anticorps contre un antigène du donneur.
    if donneur == "O":
        return True
    if receveur == "AB":
        return True
    if donneur == receveur:
        return True
    if donneur == "AB":
        return False
    return False


def plasma_ok(donneur, receveur):
    # Le plasma du donneur ne doit pas apporter d'anticorps contre les antigènes du receveur.
    if donneur == "AB":
        return True
    if receveur == "O":
        return True
    if donneur == receveur:
        return True
    if donneur == "O":
        return False
    return False


def schema_compatibilite():
    w, h = 68, 32
    parts = [
        '<figure class="schema"><svg viewBox="0 0 720 620" role="img" aria-labelledby="titre-abo">',
        '<title id="titre-abo">Compatibilité ABO des globules rouges et du plasma</title>',
        '<text fill="#14303b" font-size="15" font-family="Verdana, sans-serif" font-weight="700" x="16" y="28">Globules rouges, donneur en ligne, receveur en colonne</text>',
    ]
    x0, y0 = 168, 44
    for i, g in enumerate(GROUPES):
        parts.append(_entete(x0 + i * 74, y0, w, 26, g))
    for r, don in enumerate(GROUPES):
        y = y0 + 34 + r * 38
        parts.append(_entete(16, y, 146, h, "donne " + don))
        for c, rec in enumerate(GROUPES):
            ok = gr_ok(don, rec)
            iso = don == rec
            cls = "soi" if iso else ("ok" if ok else "non")
            mot = "même" if iso else ("oui" if ok else "non")
            if ok:
                pourquoi = (
                    f"Globules {don} vers receveur {rec} : compatible. "
                    f"{phrase_donneur(don)}. {phrase_receveur_ac(rec)}. "
                    f"Aucun anticorps du receveur ne correspond à un antigène A ou B du donneur."
                )
            else:
                pourquoi = (
                    f"Globules {don} vers receveur {rec} : incompatible. "
                    f"{phrase_donneur(don)}. {phrase_receveur_ac(rec)}. "
                    f"L'anticorps du receveur peut lyser ces globules, surtout s'il fixe le complément."
                )
            parts.append(_cell(x0 + c * 74, y, w, h, cls, mot, pourquoi))
    parts.append('<text fill="#14303b" font-size="15" font-family="Verdana, sans-serif" font-weight="700" x="16" y="268">Plasma, donneur en ligne, receveur en colonne</text>')
    y1 = 284
    for i, g in enumerate(GROUPES):
        parts.append(_entete(x0 + i * 74, y1, w, 26, g))
    for r, don in enumerate(GROUPES):
        y = y1 + 34 + r * 38
        parts.append(_entete(16, y, 146, h, "donne " + don))
        for c, rec in enumerate(GROUPES):
            ok = plasma_ok(don, rec)
            iso = don == rec
            cls = "soi" if iso else ("ok" if ok else "non")
            mot = "même" if iso else ("oui" if ok else "non")
            if ok:
                pourquoi = (
                    f"Plasma {don} vers receveur {rec} : compatible. "
                    f"{phrase_plasma(don)}. {phrase_receveur_ag(rec)}. "
                    f"L'anticorps du donneur ne cible pas un antigène A ou B du receveur."
                )
            else:
                pourquoi = (
                    f"Plasma {don} vers receveur {rec} : incompatible. "
                    f"{phrase_plasma(don)}. {phrase_receveur_ag(rec)}. "
                    f"L'anticorps voyage avec le plasma et peut lyser les globules du receveur."
                )
            parts.append(_cell(x0 + c * 74, y, w, h, cls, mot, pourquoi))
    parts.append(
        '<text fill="#14303b" font-size="13" font-family="Verdana, sans-serif" x="16" y="548">RhD : le concentré d\'urgence sans groupe connu est O RhD négatif</text>'
    )
    parts.append(
        '<text fill="#14303b" font-size="13" font-family="Verdana, sans-serif" x="16" y="576">Bleu : même groupe. Vert : compatible, pas identique. Rouge : incompatible.</text>'
    )
    parts.append("</svg>")
    parts.append(
        "<figcaption>Survoler une case lit la raison. Cliquer un nom ouvre la définition. "
        "Le bleu n'est pas plus sûr que le vert sur le plan ABO : il est seulement identique.</figcaption></figure>"
    )
    defs = [
        ("w-def-o", "Groupe O",
         "Groupe O : pas d'antigène A ni B sur le globule, et des anticorps anti-A et anti-B dans le plasma. "
         "Les globules O peuvent aller vers O, A, B et AB. Le plasma O ne va que vers un receveur O. "
         "Le concentré érythrocytaire O RhD négatif est celui que le référentiel genevois réserve aux extrêmes urgences, "
         "y compris dans le dépôt d'urgence. Ce n'est pas un plasma universel."),
        ("w-def-a", "Groupe A",
         "Groupe A : antigène A sur le globule, anticorps anti-B dans le plasma. "
         "Les globules A vont vers A et AB. Ils ne vont ni vers O ni vers B. "
         "Le plasma A va vers A et vers O, pas vers B ni vers AB."),
        ("w-def-b", "Groupe B",
         "Groupe B : antigène B sur le globule, anticorps anti-A dans le plasma. "
         "Les globules B vont vers B et AB. Le plasma B va vers B et vers O."),
        ("w-def-ab", "Groupe AB",
         "Groupe AB : antigènes A et B, pas d'anticorps ABO naturels. "
         "Le receveur AB peut recevoir des globules O, A, B et AB : c'est le receveur universel de globules rouges. "
         "Le plasma AB peut aller vers tous les groupes : c'est le donneur universel de plasma. "
         "Les globules AB ne vont que vers AB."),
        ("w-def-rh", "RhD et urgence",
         "L'antigène D est distinct de ABO. Un receveur RhD négatif, surtout une fille ou une femme qui peut être enceinte, "
         "ne doit pas recevoir des globules RhD positif hors urgence vitale sans groupe, parce que l'anti-D est un anticorps irrégulier "
         "qui traverse le placenta. Quand le groupe est inconnu et que l'on ne peut pas attendre, le référentiel des Hôpitaux "
         "universitaires de Genève, approuvé le 15 février 2024, désigne le concentré de groupe O RhD négatif pour l'extrême urgence. "
         "La carte au lit ne détermine pas le groupe : elle vérifie la compatibilité."),
        ("w-def-lit", "Contrôle au lit",
         "Deux verrous. La concordance documentaire concerne tout produit, y compris le plasma, les plaquettes et l'urgence. "
         "La carte de compatibilité ABO est réservée aux globules rouges, y compris le concentré O RhD négatif d'extrême urgence. "
         "Elle ne sert pas au plasma ni aux plaquettes. Un doute : on ne transfuse pas, on appelle le laboratoire."),
    ]
    boutons = []
    pops = []
    for wid, titre, texte in defs:
        boutons.append(
            f'<button type="button" class="terme" popovertarget="{wid}">{html.escape(titre)}</button> '
        )
        pops.append(
            f'<div id="{wid}" popover class="fenetre sousf"><div class="barre"><span>{html.escape(titre)}</span>'
            f'<button type="button" popovertarget="{wid}" popovertargetaction="hide" aria-label="Fermer">✕</button></div>'
            f'<div class="corps"><p>{html.escape(texte)}</p></div></div>'
        )
    return "".join(parts) + "<p>Définitions au clic : " + "".join(boutons) + "</p>" + "".join(pops)


def schema_algorithme():
    etapes = [
        (40, "1. Arrêter", "On arrête la transfusion dès qu'une réaction est suspectée. On ne laisse pas finir la poche pour voir."),
        (110, "2. Voie veineuse", "On garde un accès veineux. On ne rajoute rien dans la poche. Le guide 2026 prévoit le remplacement de volume si besoin."),
        (180, "3. Identité", "On revérifie le patient, la poche et les documents. Une confusion ABO se voit souvent là."),
        (250, "4. Appeler", "Médecin et laboratoire d'immunohématologie, puis la personne responsable de l'hémovigilance."),
        (320, "5. Bilan", "Si fièvre, douleur, urines foncées, choc ou doute d'hémolyse : le bilan en quatre volets de l'aide-mémoire du 9 août 2024."),
        (390, "6. Brancher", "Anaphylaxie : adrénaline intramusculaire. Surcharge : oxygène et diurétique lu. Atteinte pulmonaire sans surcharge : oxygène, pas le diurétique d'abord."),
        (460, "7. Déclarer", "La déclaration à Swissmedic suit l'article 63 de l'ordonnance sur les médicaments. Le grade ne dépend pas de l'imputabilité, sauf le décès."),
    ]
    parts = [
        '<figure class="schema"><svg viewBox="0 0 640 540" role="img">',
        "<title>Algorithme d'une réaction transfusionnelle</title>",
    ]
    for y, label, title in etapes:
        parts.append(
            f'<g class="cell"><title>{html.escape(title)}</title>'
            f'<rect x="80" y="{y}" width="480" height="52" rx="8" fill="#14303b"/>'
            f'<text fill="#ffffff" font-size="16" font-family="Verdana, sans-serif" font-weight="700" '
            f'x="320" y="{y + 32}" text-anchor="middle">{html.escape(label)}</text></g>'
        )
        if y < 460:
            parts.append(
                f'<path d="M320 {y+52} V {y+68}" stroke="#14303b" stroke-width="2" marker-end=""/>'
            )
    parts.append("</svg><figcaption>Sept temps. Le survol donne le geste. Le détail chiffré est dans le texte de la fenêtre.</figcaption></figure>")
    return "".join(parts)
