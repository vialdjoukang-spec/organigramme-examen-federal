#!/usr/bin/env python3
"""Renfort L1 de S2.4 : popover → fenêtres :target, sources par document, point 1 = définition.
Ne retire aucun fait : les passages d'un même document pointent vers une seule notice."""
import hashlib, html, re
from pathlib import Path
from bs4 import BeautifulSoup, NavigableString

ROOT = Path(__file__).resolve().parents[1]
CACHE = Path.home() / '.cache/medina_aips'

AIPS = {
    '55459': ('Nitroglycerin Sintetica', 'Septembre 2026',
              'https://files.refdata.ch/simis-public-prod/MedicinalDocuments/eafd69ba31ef42cfa7f242c538b24a02-fr.html'),
    '46613': ('Heparin-Na B. Braun', 'Juin 2026',
              'https://files.refdata.ch/simis-public-prod/MedicinalDocuments/4f8f734c6a0a4c9bb6ef48c2446fe431-fr.html'),
    '56554': ('Morphini HCl Streuli', 'Janvier 2026',
              'https://files.refdata.ch/simis-public-prod/MedicinalDocuments/cb79c0b47b314a5799c5b6e351a53ba0-fr.html'),
    '66983': ('Paracétamol axapharm', 'Septembre 2025',
              'https://files.refdata.ch/simis-public-prod/MedicinalDocuments/0d8000f65f984095adb4b8900f17ca3c-fr.html'),
    '51795': ('Aspirine Cardio', 'Mars 2026',
              'https://files.refdata.ch/simis-public-prod/MedicinalDocuments/5c0d9caab7df4b4bad5c584cf5bb5fc5-fr.html'),
    '38133': ('Aspégic', 'Décembre 2025',
              'https://files.refdata.ch/simis-public-prod/MedicinalDocuments/3654cabaf2774fda9fa35c4eae0eb4c3-fr.html'),
    '47256': ('Acide acétylsalicylique Panpharma', 'Septembre 2024',
              'https://files.refdata.ch/simis-public-prod/MedicinalDocuments/c22f097fbdd74538a5bf4ca52de63b60-fr.html'),
    '53987': ('Fentanyl Sintetica', 'Novembre 2025',
              'https://files.refdata.ch/simis-public-prod/MedicinalDocuments/90c9b45ef2b7473eac63944c6682acc9-fr.html'),
    '51480': ('Naproxen-Mepha', 'Septembre 2024',
              'https://files.refdata.ch/simis-public-prod/MedicinalDocuments/e50f9fb3f6e34322acaddfe69ce96675-fr.html'),
    '61859': ('Voltaren Dolo forte Emulgel', 'Février 2023',
              'https://files.refdata.ch/simis-public-prod/MedicinalDocuments/71d9564a38c147e984da3fe1aee5903f-fr.html'),
    '67940': ('Ibuprofen Viatris', 'Décembre 2024',
              'https://files.refdata.ch/simis-public-prod/MedicinalDocuments/c4b428dd8a5445dd9a918ab705bdf5ca-fr.html'),
    '70437': ('Inflamac Lotio forte', 'Février 2023',
              'https://files.refdata.ch/simis-public-prod/MedicinalDocuments/df897274349a4b23bd4750a2773fa06d-fr.html'),
}

# Phrases recopiées de l'AIPS lue le 2026-11-15 (grossesse, allaitement).
CIT = {
    '46613': (
        "Les données disponibles sur les femmes enceintes ne montrent aucune malformation et/ou toxicité fœtale/néonatale induite par l'héparine.",
        "L'héparine/les métabolites ne sont pas excrétés dans le lait maternel. Par conséquent, la prudence est de mise lors de l'utilisation de Heparin-Na B. Braun chez une mère qui allaite.",
    ),
    '55459': (
        "Dans ces circonstances, le médicament ne doit pas être administré durant la grossesse, sauf nécessité absolue.",
        "Il ne faut pas allaiter pendant le traitement par Nitroglycerin Sintetica.",
    ),
    '56554': (
        "Morphini HCl Streuli ne doit pas être administré pendant la grossesse, sauf en cas de nécessité absolue.",
        "La morphine passe dans le lait maternel. Il est absolument contre-indiqué d'allaiter, car les effets du traitement chez le nourrisson n'ont pas fait l'objet d'études.",
    ),
    '66983': (
        "En cas de nécessité clinique, le paracétamol peut être pris ou utilisé pendant la grossesse. Toutefois, il convient de prendre ou d'utiliser la dose efficace la plus faible pendant la durée la plus courte possible et à la fréquence la plus basse possible.",
        "Bien que l'utilisation du paracétamol soit considérée comme compatible avec l'allaitement, la prudence est de mise lors de l'utilisation du Paracétamol axapharm pendant l'allaitement.",
    ),
    '51795': (
        "L'acide acétylsalicylique est contre-indiqué au cours du troisième trimestre de la grossesse.",
        "Au cours de l'allaitement, prescrire Aspirine Cardio seulement en cas d'indication impérative, le sevrage est nécessaire lors de l'emploi régulier de hautes doses (>300 mg/jour).",
    ),
    '38133': (
        "L'administration d'inhibiteurs de la synthèse de la prostaglandine au début de la grossesse accroît en effet le risque de fausses couches, de malformations cardiaques et de gastroschisis.",
        "Par mesure de précaution, l'acide acétylsalicylique ne doit donc pas être administré aux femmes qui allaitent.",
    ),
    '47256': (
        "L'administration d'inhibiteurs de la synthèse de la prostaglandine au début de la grossesse accroît en effet le risque de fausses couches, de malformations cardiaques et de gastroschisis.",
        "Par mesure de précaution, l'acide acétylsalicylique ne doit donc pas être administré aux femmes qui allaitent.",
    ),
    '53987': (
        "Il n'existe pas de données adéquates sur l'utilisation de Fentanyl Sintetica en solution pour injection/perfusion chez la femme enceinte. Le risque potentiel chez les humains est inconnu.",
        "Ni l'allaitement ni l'utilisation de lait maternel pompé ne sont recommandés jusqu'à 24 heures après l'administration de Fentanyl Sintetica en solution pour injection/perfusion.",
    ),
    '67940': (
        "A moins d'une nécessité clairement établie, l'utilisation de l'ibuprofène est à éviter au cours du premier et du deuxième trimestre de la grossesse. L'ibuprofène est contre-indiqué au cours du troisième trimestre de la grossesse.",
        "Par prudence, l'ibuprofène ne doit donc pas être pris pendant l'allaitement. Si le traitement est indispensable, le nourrisson doit être sevré.",
    ),
    '51480': (
        "L'administration d'inhibiteurs de la synthèse des prostaglandines au début de la grossesse accroît en effet le risque de fausses couches, de malformations cardiaques et de gastroschisis.",
        "Par mesure de précaution, Naproxen-Mepha ne doit donc pas être pris par les femmes qui allaitent. Si le traitement s'avère indispensable, il convient alors de nourrir l'enfant au biberon.",
    ),
    '61859': (
        "Voltaren Dolo forte Emulgel ne doit pas être utilisé chez la femme enceinte. Voltaren Dolo forte Emulgel est contre-indiqué pendant le 3e trimestre de la grossesse.",
        "Voltaren Dolo forte Emulgel ne doit pas être utilisé chez la femme qui allaite.",
    ),
    '70437': (
        "Inflamac Lotio forte ne doit pas être utilisé chez la femme enceinte. Inflamac Lotio forte est contre-indiqué pendant le 3e trimestre de la grossesse.",
        "Inflamac Lotio forte ne doit pas être utilisé chez la femme qui allaite.",
    ),
}


def host_label(url):
    if 'revmed.ch' in url:
        return 'Revue Médicale Suisse, 2007'
    if 'nice.org.uk' in url:
        return 'NICE CG95, mise à jour 2016'
    if 'hug.ch' in url:
        return 'Hôpitaux universitaires de Genève'
    if 'pmc.ncbi' in url or 'ncbi.nlm.nih.gov' in url:
        return 'Article en accès ouvert'
    if 'escardio' in url:
        return 'Société européenne de cardiologie'
    if 'erj.' in url or 'ersnet' in url or 'ersjournals' in url:
        return 'European Respiratory Society'
    return 'Source citée'


def collapse_sources(h):
    m = re.search(r'(<section class="ilot" id="[^"]*sources"><h3>Sources</h3><ol>)(.*?)(</ol>)', h, re.S)
    if not m:
        raise SystemExit('bibliographie introuvable')
    lis = re.findall(r'<li id="([^"]+)">(.*?)</li>', m.group(2), re.S)
    url_of, order, dates = {}, [], {}
    for i, body in lis:
        um = re.search(r'https?://[^\s<"\u2014]+', body)
        url = um.group(0) if um else i
        url_of[i] = url
        if url not in order:
            order.append(url)
        dm = re.search(r'consulté le ([0-9-]+)', body)
        dates[url] = dm.group(1) if dm else '2026-11-10'
    short, n_s = {}, 0
    for url in order:
        am = re.search(r'/([0-9a-f]{20,})-fr\.html', url)
        num = None
        for k, (_n, _d, u) in AIPS.items():
            if u.split('/')[-1][:20] in url:
                num = k
                break
        if num:
            short[url] = f'sb-aips-{num}'
        else:
            n_s += 1
            short[url] = f'sb-s{n_s}'
    mapping = {i: short[url_of[i]] for i in url_of}

    def repl_sup(mm):
        nid = mapping.get(mm.group(1), mm.group(1))
        lab = nid.replace('sb-', '')
        return f'<sup class="r"><a href="#{nid}">{lab}</a></sup>'

    pre = re.sub(r'<sup class="r"><a href="#(sb-[^"]+)">[^<]*</a></sup>', repl_sup, h[:m.start()])
    pre = re.sub(r'(<sup class="r"><a href="#sb-[^"]+">[^<]*</a></sup>)(?:\s*\1)+', r'\1', pre)
    lines, seen = [], set()
    for url in order:
        sid = short[url]
        if sid in seen:
            continue
        seen.add(sid)
        if sid.startswith('sb-aips-'):
            num = sid.split('-')[-1]
            nom, maj, u = AIPS[num]
            body = (f'[{sid[3:]}] {nom}, information professionnelle Swissmedic n° {num}, '
                    f'mise à jour {maj} — {u} (consulté le 2026-11-15)')
        else:
            body = f'[{sid[3:]}] {host_label(url)} — {url} (consulté le {dates[url]})'
        lines.append(f'<li id="{sid}">{body}</li>')
    return pre + m.group(1) + ''.join(lines) + m.group(3) + h[m.end():]


def fermer(soup):
    a = soup.new_tag('a', href='#', attrs={'class': 'fermer', 'aria-label': 'Fermer'})
    a.string = 'Fermer ✕'
    return a


def make_window(soup, fid, label, nodes, mb=False):
    sec = soup.new_tag('section', attrs={
        'class': 'fenetre mb' if mb else 'fenetre',
        'id': fid, 'role': 'dialog', 'aria-label': label[:180],
    })
    fen = soup.new_tag('div', attrs={'class': 'fen'})
    h = soup.new_tag('h4')
    h.string = label
    fen.append(fermer(soup))
    fen.append(h)
    for n in nodes:
        fen.append(n)
    sec.append(fen)
    return sec


def convert_popovers(soup):
    for btn in list(soup.select('button.w')):
        tid = btn.get('popovertarget')
        label = ' '.join(btn.get_text().split())
        a = soup.new_tag('a', href=f'#f-{tid}', attrs={'class': 'ouvre'})
        a.string = label
        btn.replace_with(a)
        div = soup.find(id=tid)
        if div is None:
            continue
        kids = []
        for c in list(div.contents):
            kids.append(c.extract())
        win = make_window(soup, f'f-{tid}', label[:180] or tid, kids)
        div.replace_with(win)


def move_after_definition(soup, src_id, dst_id, keep_p):
    src, dst = soup.find(id=src_id), soup.find(id=dst_id)
    ps = [c for c in src.find_all('div', class_='p', recursive=False)]
    if len(ps) <= keep_p:
        return
    anchor = ps[keep_p - 1]
    moving, node = [], anchor.next_sibling
    while node is not None:
        nxt = node.next_sibling
        moving.append(node.extract())
        node = nxt
    h3 = dst.find('h3')
    for n in reversed([x for x in moving if not (isinstance(x, NavigableString) and not str(x).strip())]):
        h3.insert_after(n)


def retitle_point1(soup):
    for h in soup.find_all('h3'):
        t = ' '.join(h.get_text().split())
        if t.startswith('1.') and 'Définition' in t:
            h.clear()
            st = soup.new_tag('strong')
            st.string = '1. Définition'
            h.append(st)


def wrap_h4_groups(soup, section_id):
    sec = soup.find(id=section_id)
    children = [c for c in list(sec.children) if getattr(c, 'name', None)]
    groups, cur = [], None
    for c in children:
        if c.name == 'h4':
            if cur:
                groups.append(cur)
            cur = [c]
        elif cur is not None:
            cur.append(c)
    if cur:
        groups.append(cur)
    made = []
    for g in groups:
        if any(getattr(n, 'name', None) == 'section' and 'fenetre' in ' '.join(n.get('class') or []) for n in g):
            continue
        label = ' '.join(g[0].get_text().split()) or 'Région'
        fid = section_id + '-r-' + re.sub(r'[^a-z0-9]+', '-', label.lower())[:40].strip('-')
        nodes = [n.extract() for n in g]
        win = make_window(soup, 'f-' + fid, label, nodes)
        # réinséré plus bas
        made.append((label, win))
    # place les fenêtres après le dernier paragraphe d'introduction
    intro = sec.find('div', class_='p')
    cursor = intro
    for label, win in made:
        cursor.insert_after(win)
        cursor = win
    if made and intro is not None:
        # phrase de liens, propre au fichier
        p = soup.new_tag('div', attrs={'class': 'p'})
        if section_id.startswith('pa'):
            lead = "Le clinicien précise ensuite "
            tail = ", afin de suivre la menace vitale avant le geste local."
        else:
            lead = "Le médecin recherche ensuite "
            tail = ", afin de reproduire la douleur au siège décrit."
        p.append(NavigableString(lead))
        for i, (label, win) in enumerate(made):
            if i:
                p.append(NavigableString(', ' if i < len(made) - 1 else ' et '))
            a = soup.new_tag('a', href='#' + win['id'], attrs={'class': 'ouvre'})
            a.string = label[0].lower() + label[1:] if label[:1].isupper() and not label[:2].isdigit() else label
            p.append(a)
        p.append(NavigableString(tail))
        intro.insert_after(p)
    return len(made)


def sup(soup, num):
    s = soup.new_tag('sup', attrs={'class': 'r'})
    a = soup.new_tag('a', href=f'#sb-aips-{num}')
    a.string = f'aips-{num}'
    s.append(a)
    return s


def safety_table(soup, num):
    g, al = CIT[num]
    wrap = soup.new_tag('div', attrs={'class': 't', 'style': 'overflow-x:auto'})
    table = soup.new_tag('table')
    for rub, txt in (('Grossesse', g), ('Allaitement', al)):
        tr = soup.new_tag('tr')
        th = soup.new_tag('th')
        th.string = rub
        td = soup.new_tag('td')
        td.append(NavigableString(txt + ' '))
        td.append(sup(soup, num))
        tr.append(th)
        tr.append(td)
        table.append(tr)
    wrap.append(table)
    return wrap


def mark_mb(soup, fid, num):
    sec = soup.find(id=fid)
    if sec is None:
        return False
    classes = sec.get('class') or []
    if 'mb' not in classes:
        sec['class'] = classes + ['mb']
    fen = sec.find('div', class_='fen')
    if fen and not fen.find('th', string='Grossesse'):
        fen.append(safety_table(soup, num))
    return True


def new_mb(soup, parent, after, fid, label, num):
    win = make_window(soup, fid, label, [safety_table(soup, num)], mb=True)
    after.insert_after(win)
    return win


def link_sentence(soup, p, lead, items, tail):
    """items: list of (label, href)."""
    box = soup.new_tag('div', attrs={'class': 'p'})
    box.append(NavigableString(lead))
    for i, (label, href) in enumerate(items):
        if i:
            box.append(NavigableString(', ' if i < len(items) - 1 else ' et '))
        a = soup.new_tag('a', href=href, attrs={'class': 'ouvre'})
        a.string = label
        box.append(a)
    box.append(NavigableString(tail))
    p.insert_after(box)


def figure(soup, meta, titre, cliche, reperes, pieges, decision):
    w, h = meta['w'], meta['h']
    fig = soup.new_tag('figure', attrs={'class': 'cliche-guide'})
    p = soup.new_tag('p', attrs={'class': 'p'})
    b = soup.new_tag('b')
    b.string = titre + '. '
    p.append(b)
    p.append(NavigableString(cliche))
    fig.append(p)
    paire = soup.new_tag('div', attrs={'class': 'paire'})
    d1 = soup.new_tag('div')
    img = soup.new_tag('img', src=meta['fichier'], width=str(w), height=str(h), alt=titre + ', cliché brut')
    img['loading'] = 'lazy'
    d1.append(img)
    cap1 = soup.new_tag('p', attrs={'class': 'p'})
    cap1.string = f"Lisez d'abord seul ce cliché ({titre.lower()}) et cherchez vous-même le signe décisif."
    d1.append(cap1)
    d2 = soup.new_tag('div')
    marques = []
    for i, (x, y, _t) in enumerate(reperes, 1):
        cx, cy = x * w / 100, y * h / 100
        r = max(w, h) * 0.035
        marques.append(
            f'<circle cx="{cx:.0f}" cy="{cy:.0f}" r="{r:.0f}" fill="none" stroke="#b00020" '
            f'stroke-width="{max(w, h) * .006:.1f}" stroke-dasharray="{max(w, h) * .015:.0f}"/>'
            f'<text x="{cx + max(w, h) * .04:.0f}" y="{cy:.0f}" font-size="{max(w, h) * .045:.0f}" '
            f'font-weight="700" fill="#b00020" stroke="#fff" stroke-width="{max(w, h) * .004:.1f}">{i}</text>'
        )
    svg = BeautifulSoup(
        f'<svg viewBox="0 0 {w} {h}" role="img" aria-label="{html.escape(titre)}, copie annotée">'
        f'<image href="{meta["fichier"]}" width="{w}" height="{h}"/>{"".join(marques)}</svg>',
        'html.parser').svg
    d2.append(svg)
    cap2 = soup.new_tag('p', attrs={'class': 'p'})
    cap2.string = f"La copie annotée ({titre.lower()}) numérote les repères que la lecture guidée explique."
    d2.append(cap2)
    paire.append(d1)
    paire.append(d2)
    fig.append(paire)
    lecture = soup.new_tag('div')
    b2 = soup.new_tag('b')
    b2.string = 'Lecture guidée.'
    lecture.append(b2)
    ol = soup.new_tag('ol')
    for _x, _y, t in reperes:
        li = soup.new_tag('li')
        li.string = t
        ol.append(li)
    lecture.append(ol)
    fig.append(lecture)
    if pieges:
        d = soup.new_tag('div')
        b3 = soup.new_tag('b')
        b3.string = 'Pièges.'
        d.append(b3)
        ul = soup.new_tag('ul')
        for t in pieges:
            li = soup.new_tag('li')
            li.string = t
            ul.append(li)
        d.append(ul)
        fig.append(d)
    pd = soup.new_tag('p', attrs={'class': 'p'})
    b4 = soup.new_tag('b')
    b4.string = "Ce que l'image décide. "
    pd.append(b4)
    pd.append(NavigableString(decision))
    fig.append(pd)
    fc = soup.new_tag('figcaption')
    fc.append(NavigableString(
        f"Image : {meta.get('auteur') or 'auteur non indiqué'}, {meta['licence']}, Wikimedia Commons, "))
    a = soup.new_tag('a', href=meta['url'])
    a.string = meta['titre']
    fc.append(a)
    fc.append(NavigableString(
        f", consultée le {meta['consulte']}. La copie annotée est une œuvre dérivée sous la même licence."))
    fig.append(fc)
    return fig


def add_figure_window(soup, section_id, fid, label, fig):
    sec = soup.find(id=section_id)
    win = make_window(soup, fid, label, [fig])
    h3 = sec.find('h3')
    h3.insert_after(win)
    p = sec.find('div', class_='p')
    if p:
        extra = soup.new_tag('div', attrs={'class': 'p'})
        a = soup.new_tag('a', href='#' + fid, attrs={'class': 'ouvre'})
        a.string = label[0].lower() + label[1:]
        if section_id.startswith('pa-p3') or section_id.startswith('dx1-p3'):
            extra.append(NavigableString('La '))
            extra.append(a)
            extra.append(NavigableString(" situe le mécanisme avant les signes, afin que le geste clinique s'explique."))
        else:
            extra.append(NavigableString('Le '))
            extra.append(a)
            extra.append(NavigableString(' montre la modalité qui fait changer de conduite lorsque le tracé ou le siège tranche.'))
        p.insert_after(extra)


def load_meta(name):
    import json
    return json.loads((ROOT / 'images' / (name + '.json')).read_text())


def build(path, kind):
    raw = collapse_sources(path.read_text())
    soup = BeautifulSoup(raw, 'html.parser')
    if soup.style:
        soup.style.decompose()
    convert_popovers(soup)
    retitle_point1(soup)
    if kind == 'pa':
        soup.title.string = 'S2.4 — Gêne thoracique'
        h2 = soup.find('h2')
        if h2:
            h2.string = 'S2.4 — Gêne thoracique'
        move_after_definition(soup, 'pa-p1', 'pa-p7', 1)
        wrap_h4_groups(soup, 'pa-p6')
        for fid, num in (('f-pa-p11-f3', '46613'), ('f-pa-p11-f4', '55459'),
                         ('f-pa-p11-f5', '56554'), ('f-pa-p11-f6', '66983')):
            mark_mb(soup, fid, num)
        # fiches des autres molécules dosées dans le cours
        anchor = soup.find(id='pa-p11').find('div', class_='p')
        extras = []
        for num, label, fid in (
            ('51795', 'Aspirine Cardio', 'f-pa-p11-cardio'),
            ('38133', 'Aspégic', 'f-pa-p11-aspegic'),
            ('47256', 'acide acétylsalicylique injectable', 'f-pa-p11-aasinj'),
            ('53987', 'fentanyl', 'f-pa-p11-fentanyl'),
        ):
            win = make_window(soup, fid, label[0].upper() + label[1:] + f' (n° {num})',
                              [safety_table(soup, num)], mb=True)
            anchor.insert_after(win)
            extras.append((label, '#' + fid))
            anchor = win
        link_sentence(
            soup, soup.find(id='pa-p11').find('div', class_='p'),
            'Les fiches fixent aussi ',
            extras,
            ', afin que la grossesse et l’allaitement restent ceux de l’information professionnelle.',
        )
        add_figure_window(
            soup, 'pa-p3', 'f-pa-p3-image', 'Schéma de l’obstacle coronaire',
            figure(soup, load_meta('Blausen_0463_HeartAttack'),
                   'Obstacle coronaire et muscle lésé',
                   'Le schéma en couleur montre l’interruption du flux et la zone myocardique qui en dépend.',
                   [(78, 16, 'Le médaillon supérieur montre l’obstacle jaune dans la lumière, donc le flux s’interrompt en aval.'),
                    (52, 47, 'Le cercle désigne le siège de l’occlusion sur le réseau coronaire visible à la face du cœur.'),
                    (66, 63, 'La plage violacée correspond au muscle lésé, ce qui relie l’obstacle à la douleur.')],
                   ['Un obstacle incomplet peut déjà donner une gêne d’effort, alors que le muscle n’est pas encore nécrosé.',
                    'Le schéma ne remplace pas l’électrocardiogramme, qui seul déclenche l’alarme de reperfusion.'],
                   'Cette image impose de traiter la gêne d’effort ou de repos comme une ischémie tant que l’électrocardiogramme ne l’a pas écartée.'),
        )
        add_figure_window(
            soup, 'pa-p9', 'f-pa-p9-image', 'Électrocardiogramme avec sus-décalage',
            figure(soup, load_meta('12_Lead_EKG_ST_Elevation_tracing_color_coded'),
                   'Sus-décalage antérieur',
                   'Le tracé à douze dérivations colore le sus-décalage antérieur et le sous-décalage inférieur.',
                   [(76, 20, 'Le marquage orange couvre le sus-décalage des dérivations antérieures, donc l’infarctus avec élévation du segment ST est en cause.'),
                    (22, 58, 'Le marquage bleu montre le sous-décalage inférieur en miroir, tandis que la bande du bas sert au rythme.')],
                   ['Un tracé normal n’écarte pas un syndrome coronarien, et il faut répéter l’enregistrement si la douleur persiste.',
                    'L’embolie pulmonaire peut modifier le tracé sans reproduire ce sus-décalage antérieur orange.'],
                   'Ce sus-décalage déclenche l’alarme de reperfusion et sépare l’infarctus de l’embolie pulmonaire au premier contact.'),
        )
    else:
        soup.title.string = 'DX.1 — Syndrome de la paroi thoracique'
        move_after_definition(soup, 'dx1-p1', 'dx1-p7', 2)
        wrap_h4_groups(soup, 'dx1-p6')
        # une fiche par molécule dosée : on enveloppe le paragraphe qui la nomme
        sec = soup.find(id='dx1-p11')
        mapping = [
            ('66983', 'Paracétamol axapharm', 'paracétamol'),
            ('67940', 'Ibuprofen Viatris', 'ibuprofène'),
            ('51480', 'Naproxen-Mepha', 'naproxène'),
            ('61859', 'Voltaren Dolo forte Emulgel', 'diclofénac'),
        ]
        for num, label, needle in mapping:
            target = None
            for p in sec.find_all('div', class_='p', recursive=False):
                if needle in p.get_text().lower() and 'fiche' not in p.get_text()[:40].lower():
                    target = p
                    break
            if target is None:
                continue
            fid = f'f-dx1-p11-{num}'
            node = target.extract()
            win = make_window(soup, fid, f'{label} (n° {num})', [node, safety_table(soup, num)], mb=True)
            # lien à la place du paragraphe
            holder = soup.new_tag('div', attrs={'class': 'p'})
            holder.append(NavigableString('La fiche '))
            a = soup.new_tag('a', href='#' + fid, attrs={'class': 'ouvre'})
            a.string = label
            holder.append(a)
            holder.append(NavigableString(
                f' porte la dose, la grossesse et l’allaitement de l’autorisation {num}, afin de ne pas adoucir l’information professionnelle.'))
            # insère au début de la section après h3 pour garder l'ordre plus bas : on met après h3 cumulé
            sec.find('h3').insert_after(win)
            win.insert_after(holder)
        # inflamac, cité avec le gel
        fid = 'f-dx1-p11-70437'
        win = make_window(soup, fid, 'Inflamac Lotio forte (n° 70437)',
                          [safety_table(soup, '70437')], mb=True)
        sec.find('h3').insert_after(win)
        holder = soup.new_tag('div', attrs={'class': 'p'})
        holder.append(NavigableString('La fiche '))
        a = soup.new_tag('a', href='#' + fid, attrs={'class': 'ouvre'})
        a.string = 'Inflamac Lotio forte'
        holder.append(a)
        holder.append(NavigableString(
            ' reprend la même famille topique, et elle interdit le gel chez la femme enceinte comme chez celle qui allaite.'))
        win.insert_after(holder)
        add_figure_window(
            soup, 'dx1-p3', 'f-dx1-p3-image', 'Schéma des cartilages costaux',
            figure(soup, load_meta('Costal_Cartilage'),
                   'Cartilages costaux et jonctions',
                   'Le dessin en couleur place le sternum, les cartilages bleus et les jonctions que le doigt cherche.',
                   [(60, 30, 'Le sternum forme la ligne médiane, et les cartilages bleus s’y rattachent par les jonctions sternocostales.'),
                    (38, 50, 'Le cartilage costal bleu unit la côte osseuse au sternum, donc la pression digitale le met en tension.'),
                    (30, 70, 'La jonction chondrocostale siège au contact de la côte et du cartilage, là où la costochondrite se palpe.')],
                   ['La douleur reproduite à ce siège n’exclut pas une cause cardiaque qui coexiste.',
                    'Les côtes inférieures et le rebord costal ne se voient pas tous sur ce schéma antérieur.'],
                   'Le médecin palpe ces jonctions avant de conclure à une douleur pariétale, car le siège doit coïncider avec la plainte.'),
        )
        add_figure_window(
            soup, 'dx1-p9', 'f-dx1-p9-image', 'Électrocardiogramme qui réoriente',
            figure(soup, load_meta('12_Lead_EKG_ST_Elevation_tracing_color_coded'),
                   'Tracé qui écarte la paroi',
                   'Le même type de tracé sert ici à ne pas attribuer à la paroi une douleur qui est coronaire.',
                   [(74, 28, 'Le sus-décalage orange des dérivations précordiales fait quitter le diagnostic pariétal au profit de l’infarctus.'),
                    (18, 62, 'Le sous-décalage bleu inférieur accompagne souvent ce miroir, et il ne se palpe pas sur le cartilage.')],
                   ['Une palpation positive peut coexister avec ce tracé, donc elle ne rassure pas quand l’électrocardiogramme est anormal.',
                    'L’absence de sus-décalage ne prouve pas la paroi, et le contexte douloureux reste à reprendre.'],
                   'Dès que ce sus-décalage est présent, le médecin abandonne la conduite pariétale et déclenche le parcours de reperfusion.'),
        )
    # phrase adoucie connue : on renvoie aux fiches sans fusionner deux AIPS
    for p in soup.find_all('div', class_='p'):
        txt = p.get_text()
        if 'contre-indique par prudence' in txt and 'ibuprofène' in txt:
            p.clear()
            p.append(NavigableString(
                "L’ibuprofène et le naproxène interdisent l’allaitement dans leur fiche, et le nourrisson est sevré lorsque le traitement reste indispensable."))
    out = str(soup)
    if 'FIN_FICHIER' not in out[-400:]:
        part = 'Phase_A_V0' if kind == 'pa' else 'Phase_B_V0_DX.1'
        out = out.rstrip() + f'\n<!-- FIN_FICHIER LOT_043_{part} -->\n'
    if not out.startswith('<!DOCTYPE'):
        out = '<!DOCTYPE html>\n' + out
    path.write_text(out)
    print(path.name, len(out.encode()), 'fenêtres', out.count('class="fenetre"') + out.count("class=\"fenetre "))


def main():
    build(ROOT / 'LOT_043_Phase_A_V0.html', 'pa')
    build(ROOT / 'LOT_043_Phase_B_V0_DX.1.html', 'dx')


if __name__ == '__main__':
    main()
