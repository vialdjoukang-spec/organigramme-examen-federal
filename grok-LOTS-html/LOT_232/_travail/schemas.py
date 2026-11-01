# -*- coding: utf-8 -*-
"""Trois schémas interactifs. Le survol, le focus et l'ancre :target épaississent le cadre."""


def _boite(gid, x, y, w, h, l1, l2=""):
    y1 = y + (18 if l2 else 28)
    t2 = (
        f'<text x="{x+w/2:.0f}" y="{y+34}" text-anchor="middle" font-size="13">{l2}</text>'
        if l2 else ""
    )
    return (
        f'<g class="etape" id="{gid}" tabindex="0">'
        f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="8"/>'
        f'<text x="{x+w/2:.0f}" y="{y1}" text-anchor="middle" font-size="13">{l1}</text>'
        f'{t2}</g>'
    )


def arbre():
    """Capacité et représentation. Lecture de haut en bas, puis la branche de droite."""
    b = []
    b.append(_boite("acte", 250, 12, 240, 46, "Acte proposé", "hors recherche"))
    b.append(_boite("urgence", 230, 88, 280, 46, "Danger immédiat ?", "Patient incapable"))
    b.append(_boite("oui379", 20, 170, 250, 52, "Oui : soins indispensables", "volonté présumée"))
    b.append(_boite("refusant", 20, 250, 250, 52, "Refus anticipé connu", "ne pas passer outre"))
    b.append(_boite("capa", 390, 170, 280, 52, "Non : capacité pour", "cette décision, ce moment"))
    b.append(_boite("capable", 390, 250, 280, 46, "Capable : il décide", "accord ou refus"))
    b.append(_boite("doute", 390, 322, 280, 46, "Doute : quatre aptitudes", "puis réévaluer"))
    b.append(_boite("incap", 390, 394, 280, 52, "Incapable : directives", "puis représentant"))
    b.append(_boite("plan", 390, 472, 280, 46, "Plan de traitement", "associer la personne"))
    fleches = (
        '<path d="M370 58 V88" marker-end="url(#fl)"/>'
        '<path d="M280 134 H145 V170" marker-end="url(#fl)"/>'
        '<path d="M460 134 H530 V170" marker-end="url(#fl)"/>'
        '<path d="M145 222 V250" marker-end="url(#fl)"/>'
        '<path d="M530 222 V250" marker-end="url(#fl)"/>'
        '<path d="M530 296 V322" marker-end="url(#fl)"/>'
        '<path d="M530 368 V394" marker-end="url(#fl)"/>'
        '<path d="M530 446 V472" marker-end="url(#fl)"/>'
    )
    return f'''<figure class="schema"><svg viewBox="0 0 700 540" role="img" aria-label="Arbre capacité et représentation">
<defs><marker id="fl" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="currentColor"/></marker></defs>
<g fill="none" stroke="currentColor" stroke-width="1.4">{fleches}</g>
{''.join(b)}
</svg>
<figcaption>Chaque cadre réagit au survol, au focus et à l'ancre. La branche de gauche est l'urgence. La branche de droite part de la capacité.</figcaption>
</figure>'''


def chaine():
    etapes = [
        ("c1", "Diagnostic"),
        ("c2", "Nature et but"),
        ("c3", "Bénéfices"),
        ("c4", "Risques fréquents"),
        ("c5", "Risques graves"),
        ("c6", "Alternatives"),
        ("c7", "Abstention"),
        ("c8", "Coût et suites"),
        ("c9", "Reformulation"),
        ("c10", "Délai, puis trace"),
    ]
    g = []
    for i, (gid, lab) in enumerate(etapes):
        x = 24 + (i % 2) * 330
        y = 16 + (i // 2) * 78
        g.append(_boite(gid, x, y, 300, 52, f"{i+1}. {lab}"))
    return f'''<figure class="schema"><svg viewBox="0 0 680 420" role="img" aria-label="Chaîne de l'information avant une intervention">
{''.join(g)}
</svg>
<figcaption>Dix maillons. Un maillon manquant, surtout un risque grave ou une alternative, empêche de parler d'information adéquate. Le survol épaissit le cadre.</figcaption>
</figure>'''


def urgence_refus():
    g = [
        _boite("u1", 180, 16, 300, 52, "Patient qui ne décide pas", "ou qui refuse"),
        _boite("u2", 24, 110, 280, 52, "Capable et refus stable", "respecter, tracer"),
        _boite("u3", 360, 110, 280, 52, "Incapable, danger immédiat", "soins indispensables"),
        _boite("u4", 24, 220, 280, 52, "Proposer l'alternative", "ne pas passer outre"),
        _boite("u5", 360, 220, 280, 52, "Chercher un refus écrit", "s'il ne retarde rien"),
        _boite("u6", 180, 330, 300, 52, "Dès que c'est possible", "reprendre avec lui"),
    ]
    return f'''<figure class="schema"><svg viewBox="0 0 680 410" role="img" aria-label="Parcours urgence et refus">
<g fill="none" stroke="currentColor" stroke-width="1.4">
<path d="M330 68 H164 V110" marker-end="url(#fl2)"/>
<path d="M330 68 H500 V110" marker-end="url(#fl2)"/>
<path d="M164 162 V220" marker-end="url(#fl2)"/>
<path d="M500 162 V220" marker-end="url(#fl2)"/>
<path d="M164 272 H330 V330" marker-end="url(#fl2)"/>
<path d="M500 272 H330 V330" marker-end="url(#fl2)"/>
</g>
<defs><marker id="fl2" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="currentColor"/></marker></defs>
{''.join(g)}
</svg>
<figcaption>À gauche, le refus d'une personne capable. À droite, l'urgence chez une personne incapable. Les deux se rejoignent : on rediscute dès que la personne peut décider.</figcaption>
</figure>'''


def page_schema(titre, svg, ancre):
    return f"""<!doctype html>
<html lang="fr"><head><meta charset="utf-8"><title>{titre}</title>
<style>
@font-face {{ font-family: Atk; src: url("../../outils/dessinateur/polices/AtkinsonHyperlegible-Regular.ttf"); }}
body {{ margin: 1rem; font-family: Atk, Verdana, sans-serif; background:#eef7fc; color:#1d2a30; }}
h1 {{ font-size: 1.3rem; }}
svg {{ width: min(100%, 760px); height: auto; background: white; border: 1px solid #cfe3ec; }}
.schema .etape rect {{ fill: #fff; stroke: #176fa0; stroke-width: 1.6; }}
.schema .etape:hover rect, .schema .etape:focus rect, .schema .etape:target rect {{ stroke: #a1262f; stroke-width: 3; }}
text {{ font-family: Atk, Verdana, sans-serif; fill: #1d2a30; }}
a {{ color: #0b5d86; }}
</style></head><body>
<h1>{titre}</h1>
<p>Interaction : survol, focus, ou lien d'ancre. Exemple : <a href="#{ancre}">mettre en évidence un cadre</a>.</p>
{svg}
</body></html>
"""
