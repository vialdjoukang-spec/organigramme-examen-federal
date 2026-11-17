#!/usr/bin/env python3
"""Retire des redites de la Phase A : doses déjà tenues par le tableau, phrases répétées.
Chaque nombre retiré reste dans le tableau des médicaments ou dans une autre phrase du fichier."""
from bs4 import BeautifulSoup, NavigableString

PATH = 'Claude/LOT_043/LOT_043_Phase_A_V0.html'

# phrases plus courtes dont le fait reste dans une phrase plus complète
REDITES = [
    "Ainsi, en Suède, la mortalité à 30 jours atteint 8,9 %",
    "Le diagnostic d'un syndrome aortique aigu manqué intervient après un délai médian de 19 heures",
    "Ainsi, ce signe est un symptôme d'ischémie, une modification du segment ST-T",
    "Ainsi, le syndrome de Tietze associe des signes inflammatoires",
    "Les attaques de panique comportent une douleur thoracique dans 22 à 70 %",
    "le protocole des HUG réserve l'oxygène au seuil de 90 %",
    "En outre, elle est déclenchée par l'effort physique ; elle cède au repos",
    "L'effort augmente la demande en oxygène du myocarde, alors qu'une sténose limite l'apport, ce qui produit l'ischémie",
    "ne servent pas à diagnostiquer ni à exclure l'angor stable",
    "la colchicine, conseillée en complément dans tous les cas, réduit environ de moitié ce risque",
    "Le patient reçoit aussi des conseils individuels sur le moment où consulter de nouveau",
]


def drop_from(p, snippet):
    raw = str(p)
    i = raw.find(snippet)
    if i < 0:
        # le snippet peut être coupé par une balise : on cherche dans le texte
        if snippet[:40] not in p.get_text():
            return False
        # repli : retirer les contenus dont le texte cumulé couvre le snippet
        acc = ''
        nodes = list(p.contents)
        start = end = None
        for n, node in enumerate(nodes):
            piece = node.get_text() if hasattr(node, 'get_text') else str(node)
            if start is None and snippet[:24] in (acc + piece):
                start = n
            acc += piece
            if start is not None and snippet[:40] in acc and (acc.strip().endswith('.') or acc.strip().endswith('?')):
                end = n
                break
        if start is None:
            return False
        for node in nodes[start: (end if end is not None else start) + 1]:
            node.extract()
        return True
    j = raw.find('.', i)
    if j < 0:
        return False
    # inclure la citation collée avant le point si elle est après le snippet
    k = j
    while k + 1 < len(raw) and raw[k + 1] in ' \n':
        k += 1
    new = raw[:i] + raw[k + 1:]
    frag = BeautifulSoup(new, 'html.parser')
    p.clear()
    for c in list(frag.contents):
        p.append(c)
    return True


def set_paragraph(p, parts):
    """parts: list of str or ('sup', id)."""
    p.clear()
    for part in parts:
        if isinstance(part, tuple) and part[0] == 'sup':
            sup = p.new_tag('sup') if False else None
            from bs4 import BeautifulSoup as BS
            # tag factory via parent soup
            soup = p
            while soup.parent:
                soup = soup.parent
            s = soup.new_tag('sup', attrs={'class': 'r'})
            a = soup.new_tag('a', href=f'#{part[1]}')
            a.string = part[1].replace('sb-', '')
            s.append(a)
            p.append(s)
        else:
            p.append(NavigableString(part))


def main():
    html = open(PATH, encoding='utf-8').read()
    soup = BeautifulSoup(html, 'html.parser')
    n = 0
    for p in soup.find_all('div', class_='p'):
        for snip in REDITES:
            if snip in p.get_text() and drop_from(p, snip):
                n += 1
    print('redites retirées', n)

    ps = soup.find(id='pa-p11').find_all('div', class_='p', recursive=False)

    def refill(p, parts):
        p.clear()
        soup_root = soup
        for part in parts:
            if isinstance(part, tuple):
                s = soup_root.new_tag('sup', attrs={'class': 'r'})
                a = soup_root.new_tag('a', href=f'#{part[1]}')
                a.string = part[1].replace('sb-', '')
                s.append(a)
                p.append(s)
            else:
                p.append(NavigableString(part))

    # antiagrégation : milligrammes déjà dans le tableau
    refill(ps[4], [
        "Le premier temps est l'antiagrégation. NICE recommande une dose de charge unique d'aspirine dès que possible, sauf allergie, et les HUG utilisent la voie intraveineuse ou le sachet.",
        ('sup', 'sb-s2'),
        " NICE réserve les autres antiagrégants à l'hôpital.",
        ('sup', 'sb-s2'),
        " L'AIPS indique Aspégic dans les douleurs et la fièvre, et l'injectable Panpharma lorsque la voie orale est impossible.",
        ('sup', 'sb-aips-38133'),
        ('sup', 'sb-aips-47256'),
        " Leur emploi dans l'infarctus suit donc le protocole des HUG, hors indication de l'AIPS, tandis que les milligrammes restent ceux du tableau.",
    ])
    # héparine : schéma instable dans le tableau ; garder le schéma avec fibrinolyse
    refill(ps[5], [
        "Le deuxième temps est l'héparine de l'angor instable, dont le bolus et la perfusion figurent dans le tableau des médicaments. ",
        "Pour l'infarctus avec élévation du segment ST associé à des fibrinolytiques, le bolus est de 60 U.I./kg, avec un maximum de 4 000 unités internationales, puis 12 U.I./kg par heure.",
        ('sup', 'sb-aips-46613'),
        " L'ajustement suit ensuite le temps de thromboplastine partielle activée.",
        ('sup', 'sb-aips-46613'),
    ])
    refill(ps[6], [
        "NICE recommande la nitroglycérine sublinguale ou buccale pour soulager la douleur, puis un opioïde intraveineux si un infarctus est suspecté.",
        ('sup', 'sb-s2'),
        " La perfusion, son plafond et la limite de pression systolique figurent dans le tableau des médicaments.",
        ('sup', 'sb-aips-55459'),
    ])
    refill(ps[7], [
        "La morphine intraveineuse s'administre lentement et seulement lorsqu'un effet rapide est nécessaire, et la naloxone doit rester à portée de main.",
        ('sup', 'sb-aips-56554'),
        " La fiche rappelle qu'elle ne doit pas être administrée pendant la grossesse, sauf nécessité absolue.",
        ('sup', 'sb-aips-56554'),
    ])
    refill(ps[8], [
        "La réassurance et une antalgie simple suffisent généralement pour la paroi thoracique.",
        ('sup', 'sb-s1'),
        " L'intervalle du paracétamol est de 4 à 8 heures, et la dose baisse en cas d'atteinte hépatique ou rénale.",
        ('sup', 'sb-aips-66983'),
    ])

    # angor : les trois critères restent dans la fenêtre
    for p in soup.find_all('div', class_='p'):
        if p.get_text().startswith('Le terme angor désigne'):
            refill(p, [
                "Le terme angor désigne une gêne thoracique qui réunit trois caractères définis par NICE, et la fenêtre en détaille le compte.",
                ('sup', 'sb-s2'),
            ])
            break
    for p in soup.find_all('div', class_='p'):
        if 'quatre situations de soins voisines' in p.get_text():
            refill(p, [
                "Cette gêne se distingue de quatre situations voisines du catalogue, et le tableau dit le symptôme qui les sépare ainsi que le geste qui les reconnaît.",
            ])
            break

    # liens et textes nus sortis du paragraphe : les rattacher au div.p précédent
    for sec in soup.find_all('section', class_='ilot'):
        prev = None
        for node in list(sec.children):
            if getattr(node, 'name', None) == 'div' and 'p' in (node.get('class') or []):
                prev = node
                continue
            if prev is None:
                continue
            if isinstance(node, NavigableString) and node.strip():
                prev.append(node.extract())
            elif getattr(node, 'name', None) == 'a' and 'ouvre' in (node.get('class') or []):
                prev.append(NavigableString(' '))
                prev.append(node.extract())

    open(PATH, 'w', encoding='utf-8').write(str(soup))
    import re
    h = open(PATH, encoding='utf-8').read()
    s = re.sub(r'<svg\b.*?</svg>', '', h, flags=re.S)
    s = re.sub(r'<img\b[^>]*>', '', s)
    print('hors images', len(s.encode()))


if __name__ == '__main__':
    main()
