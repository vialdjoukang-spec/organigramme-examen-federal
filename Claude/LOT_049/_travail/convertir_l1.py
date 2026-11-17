#!/usr/bin/env python3
"""Conversion L1 du LOT 049 (Phase A et DX.1).

Ne réécrit pas les faits. Elle :
- remplace les fenêtres popover par des fenêtres :target ;
- fusionne les entrées de bibliographie qui répètent la même URL ou la même AIPS ;
- retire, dans une même phrase, les ancres successives vers le même document ;
- retire la feuille de style locale (forme.css la remplace) ;
- ramène les « , car » au-delà de 15 à « puisque », sans ajouter de mot ;
- pose les figures, les fiches .mb et une fenêtre par région d'examen.
"""
import html as htmlmod
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MAJ = {
    '37397': 'Janvier 2026',
    '29348': 'Juin 2026',
    '35112': 'Août 2025',
    '55568': 'Juin 2023',
    '50192': 'Juin 2023',
    '56551': 'Novembre 2024',
    '56394': 'Octobre 2025',
    '53836': 'Septembre 2025',
    '58728': 'Mai 2025',
    '49456': 'Février 2026',
    '56203': 'Octobre 2026',
    '67169': 'Avril 2025',
    '30630': 'Mars 2025',
}
# URL déjà citée → (identifiant stable, libellé bibliographique). L'URL complète reste la clé.
DOCS = [
    ('strategie-asthme-version-finale.pdf', 'sb-s-hug-asthme',
     'Hôpitaux universitaires de Genève, Stratégie asthme, septembre 2026'),
    ('strategie-bpco-version-finale.pdf', 'sb-s-hug-bpco',
     'Hôpitaux universitaires de Genève, Stratégie BPCO, septembre 2026'),
    ('strategie_pneumonie_1.pdf', 'sb-s-hug-pneumonie',
     'Hôpitaux universitaires de Genève, Stratégie pneumonie, septembre 2024'),
    ('fichiers/respiratoires.pdf', 'sb-s-hug-resp',
     'Hôpitaux universitaires de Genève, fiches respiratoires du service d’urgences'),
    ('09._faux_croup.pdf', 'sb-s-hug-croup',
     'Hôpitaux universitaires de Genève, faux croup'),
    ('071024_douleur_thoracique.pdf', 'sb-s-hug-douleur',
     'Hôpitaux universitaires de Genève, douleur thoracique, octobre 2024'),
    ('hascnpp_bronchiolite_texte_recommandations_2019.pdf', 'sb-s-has-bronchiolite',
     'Haute Autorité de santé, prise en charge de la bronchiolite, 2019'),
    ('34_3_2023_FR_01.pdf', 'sb-s-pedsuisse',
     'Pédiatrie suisse, 2023'),
    ('GINA-Summary-Guide-2026-WEB-WMS.pdf', 'sb-s-gina-2026',
     'Global Initiative for Asthma, guide de synthèse, 2026'),
    ('ofsp-bulletin-2026-1-36', 'sb-s-ofsp-2026',
     'Office fédéral de la santé publique, Bulletin 2026'),
    ('gl2025-09-pls-e.pdf', 'sb-s-erc-2025',
     'European Resuscitation Council, recommandations 2025'),
    ('RMS_134_2640.pdf', 'sb-s-rms',
     'Revue médicale suisse'),
    ('smw/article/download/3304/5612', 'sb-s-smw',
     'Swiss Medical Weekly'),
    ('a5419.pdf', 'sb-s-ugeskr-2018',
     'Ugeskrift for Læger, 2018'),
]
COURT = {
    'sb-s-hug-asthme': 'HUG asthme',
    'sb-s-hug-bpco': 'HUG BPCO',
    'sb-s-hug-pneumonie': 'HUG pneumonie',
    'sb-s-hug-resp': 'HUG urgences',
    'sb-s-hug-croup': 'HUG croup',
    'sb-s-hug-douleur': 'HUG douleur',
    'sb-s-has-bronchiolite': 'HAS 2019',
    'sb-s-pedsuisse': 'Pédiatrie CH',
    'sb-s-gina-2026': 'GINA 2026',
    'sb-s-ofsp-2026': 'OFSP 2026',
    'sb-s-erc-2025': 'ERC 2025',
    'sb-s-rms': 'RMS',
    'sb-s-smw': 'SMW',
    'sb-s-ugeskr-2018': 'Ugeskrift',
}


def cle_url(url):
    u = htmlmod.unescape(url)
    for frag, sid, lab in DOCS:
        if frag in u:
            return ('doc', sid), lab, u
    m = re.search(r'PMC(\d+)', u)
    if m:
        sid = f'sb-s-pmc{m.group(1)}'
        return ('doc', sid), f'Article en accès libre, PMC{m.group(1)}', u
    m = re.search(r'[?&]id=(\d+)', u)
    if m:
        sid = f'sb-s-pmid{m.group(1)}'
        return ('doc', sid), f'Résumé PubMed, identifiant {m.group(1)}', u
    m = re.search(r'articles/PMC(\d+)', u)
    if m:
        sid = f'sb-s-pmc{m.group(1)}'
        return ('doc', sid), f'Article en accès libre, PMC{m.group(1)}', u
    sid = 'sb-s-' + re.sub(r'[^a-z0-9]+', '-', u.split('/')[-1].lower())[:40].strip('-')
    return ('doc', sid), u.split('/')[-1][:80], u


def indexer(src):
    """id ancien → (id canonique, libellé court visible, ligne bibliographique)."""
    table = {}
    lignes = {}
    for lid, contenu in re.findall(r'<li id="([^"]+)">(.*?)</li>', src, re.S):
        um = re.search(r'https?://[^"\s<]+', contenu)
        url = htmlmod.unescape(um.group(0)) if um else ''
        am = re.search(r'aips-(\d+)', lid)
        if am:
            n = am.group(1)
            cid = f'sb-aips-{n}'
            nom = re.search(r'AIPS (.+?) \(Swissmedic', htmlmod.unescape(re.sub(r'<[^>]+>', ' ', contenu)))
            nom = nom.group(1).strip() if nom else n
            maj = MAJ.get(n, '')
            majbit = f', mise à jour {maj}' if maj else ''
            court = f'AIPS {n}'
            ligne = (f'<li id="{cid}">[AIPS {n}] Swissmedic, {htmlmod.escape(nom)}, '
                     f'information professionnelle{majbit} — {url} (consulté le 2026-11-15)</li>')
        else:
            (kind, cid), lab, url = cle_url(url) if url else (('doc', lid), lid, '')
            if not cid.startswith('sb-'):
                cid = 'sb-' + cid
            court = COURT.get(cid) or re.sub(r'^sb-s-', '', cid)[:18]
            ligne = (f'<li id="{cid}">[{htmlmod.escape(court)}] {htmlmod.escape(lab)} — {url} '
                     f'(consulté le 2026-11-10)</li>')
        table[lid] = (cid, court)
        lignes[cid] = ligne
    return table, lignes


def sup_neuf(cid, court):
    return f'<sup class="r"><a href="#{cid}">{htmlmod.escape(court)}</a></sup>'


def spans_phrases(fragment):
    spans = []
    start = 0
    i = 0
    in_tag = False
    while i < len(fragment):
        c = fragment[i]
        if c == '<':
            in_tag = True
        elif c == '>':
            in_tag = False
        elif not in_tag and c in '.!?':
            j = i + 1
            while j < len(fragment):
                if fragment[j] == '<':
                    k = fragment.find('>', j)
                    j = len(fragment) if k < 0 else k + 1
                    continue
                if fragment[j].isspace():
                    j += 1
                    continue
                break
            if j >= len(fragment) or fragment[j].isupper() or fragment[j] == '«':
                spans.append((start, j))
                start = j
                i = j
                continue
        i += 1
    spans.append((start, len(fragment)))
    return spans


def dedupe_phrase(fragment, table):
    """Dans chaque phrase, une seule ancre par document. L'ancre conservée vise le document entier."""
    out = []
    for a, b in spans_phrases(fragment):
        morceau = fragment[a:b]
        vus = set()
        morceaux = re.split(r'(<sup class="r">.*?</sup>)', morceau, flags=re.S)
        nouveau = []
        for part in morceaux:
            if not part.startswith('<sup'):
                nouveau.append(part)
                continue
            href = re.search(r'href="#([^"]+)"', part)
            if not href:
                nouveau.append(part)
                continue
            cid, court = table.get(href.group(1), (href.group(1), href.group(1)))
            if cid in vus:
                continue
            vus.add(cid)
            nouveau.append(sup_neuf(cid, court))
        out.append(''.join(nouveau))
    return ''.join(out)


def retirer_doublons_ancres(corps, table):
    def repl(m):
        return m.group(1) + dedupe_phrase(m.group(2), table) + m.group(3)
    corps = re.sub(r'(<(?:div class="p"|li|td|th)\b[^>]*>)(.*?)(</(?:div|li|td|th)>)', repl, corps, flags=re.S)
    # ancres hors de ces blocs (rares)
    def une(m):
        cid, court = table.get(m.group(1), (m.group(1), m.group(1)))
        return sup_neuf(cid, court)
    return re.sub(r'<sup class="r"><a href="#([^"]+)">.*?</a></sup>', une, corps, flags=re.S)


def convertir_popover(h):
    labels = {}

    def btn(m):
        labels[m.group(1)] = re.sub(r'<[^>]+>', '', m.group(2))
        labels[m.group(1)] = re.sub(r'\s+', ' ', labels[m.group(1)]).strip()
        return f'<a class="ouvre" href="#{m.group(1)}">{m.group(2)}</a>'

    h = re.sub(r'<button class="w" popovertarget="([^"]+)">(.*?)</button>', btn, h, flags=re.S)
    token = re.compile(r'<div\b([^>]*)>|</div>', re.I)
    out = []
    i = 0
    while True:
        m = token.search(h, i)
        if not m:
            out.append(h[i:])
            break
        attrs = m.group(1)
        if not (attrs and 'popover' in attrs and 'fenetre' in attrs):
            out.append(h[i:m.end()])
            i = m.end()
            continue
        out.append(h[i:m.start()])
        wid = re.search(r'id="([^"]+)"', attrs).group(1)
        depth = 1
        pos = m.end()
        while depth:
            m2 = token.search(h, pos)
            if not m2:
                raise SystemExit(f'fenêtre non fermée : {wid}')
            depth += 1 if m2.group(1) is not None else -1
            fin = m2.end()
            if depth == 0:
                inner = h[m.end():m2.start()]
                label = htmlmod.escape(labels.get(wid, wid), quote=True)
                out.append(
                    f'<section class="fenetre" id="{wid}" role="dialog" aria-label="{label}">'
                    f'<div class="fen"><a class="fermer" href="#" aria-label="Fermer">Fermer ✕</a>'
                    f'{inner}</div></section>'
                )
                pos = fin
                break
            pos = fin
        i = pos
    return ''.join(out)


def limiter_car(corps, plafond=15):
    """Remplace les « , car » au-delà du plafond par « puisque » (un mot, comme « car »)."""
    n = {'i': 0}

    def repl(m):
        n['i'] += 1
        if n['i'] <= plafond:
            return m.group(0)
        return ' puisque'
    return re.sub(r',\s*car\b', repl, corps, flags=re.I), n['i']


def _bornes_ilot(h, sid):
    m = re.search(rf'<section class="ilot" id="{sid}">', h)
    if not m:
        raise SystemExit(f'section absente {sid}')
    token = re.compile(r'<section\b|</section>')
    depth = 1
    pos = m.end()
    while depth:
        m2 = token.search(h, pos)
        if not m2:
            raise SystemExit(f'section non fermée {sid}')
        depth += -1 if m2.group(0).startswith('</') else 1
        if depth == 0:
            return m.start(), m.end(), m2.start(), m2.end()
        pos = m2.end()


def fenetrer_point(h, sid, groupes):
    """Une fenêtre par région : les paragraphes de la région quittent la page et s'ouvrent au clic."""
    deb, ouv, ferm, fin = _bornes_ilot(h, sid)
    section = h[ouv:ferm]
    parts = re.split(r'(<div class="p">.*?</div>)', section, flags=re.S)
    paras = [i for i, p in enumerate(parts) if p.startswith('<div class="p">')]
    pris = {}
    for debut, fin_p, wid, aria in groupes:
        for k in range(debut, fin_p + 1):
            pris[k] = wid
    buf = {g[2]: [] for g in groupes}
    aria_de = {g[2]: g[3] for g in groupes}
    nouveau = []
    deja = set()
    for i, part in enumerate(parts):
        if not part.startswith('<div class="p">'):
            nouveau.append(part)
            continue
        n = paras.index(i)
        if n not in pris:
            nouveau.append(part)
            continue
        wid = pris[n]
        buf[wid].append(part)
        if wid in deja:
            continue
        deja.add(wid)
        aria = aria_de[wid]
        nouveau.append(f'@@FEN@@{wid}@@')
    texte = ''.join(nouveau)
    for wid, aria in aria_de.items():
        lead = (f'<div class="p"><a class="ouvre" href="#{wid}">{htmlmod.escape(aria)}</a> '
                f'détaille le geste clinique, le signe recherché et le piège d’interprétation.</div>')
        fen = (f'<section class="fenetre" id="{wid}" role="dialog" aria-label="{htmlmod.escape(aria, quote=True)}">'
               f'<div class="fen"><a class="fermer" href="#" aria-label="Fermer">Fermer ✕</a>'
               + ''.join(buf[wid]) + '</div></section>')
        texte = texte.replace(f'@@FEN@@{wid}@@', lead + fen)
    return h[:ouv] + texte + h[ferm:]


def inserer_avant_fin_section(h, sid, bloc):
    deb, ouv, ferm, fin = _bornes_ilot(h, sid)
    return h[:ferm] + bloc + h[ferm:]


def figure(meta, titre, cliche, reperes, pieges, decision):
    import json
    m = json.loads(Path(meta).read_text(encoding='utf-8'))
    w, h = m['w'], m['h']
    e = htmlmod.escape
    marques = []
    lecture = []
    for i, (x, y, t) in enumerate(reperes, 1):
        marques.append(
            f'<circle cx="{x * w / 100:.0f}" cy="{y * h / 100:.0f}" r="{max(w, h) * .035:.0f}" fill="none" stroke="#b00020" '
            f'stroke-width="{max(w, h) * .006:.1f}" stroke-dasharray="{max(w, h) * .015:.0f}"/>'
            f'<text x="{x * w / 100 + max(w, h) * .04:.0f}" y="{y * h / 100:.0f}" font-size="{max(w, h) * .045:.0f}" '
            f'font-weight="700" fill="#b00020" stroke="#fff" stroke-width="{max(w, h) * .004:.1f}">{i}</text>'
        )
        lecture.append(f'<li>{t}</li>')
    pg = ''.join(f'<li>{p}</li>' for p in pieges)
    auteur = re.sub(r'\s+', ' ', m.get('auteur') or 'auteur non indiqué')
    auteur = auteur.split('. When using')[0][:110]
    return f'''<figure class="cliche-guide"><p class="p"><b>{e(titre)}.</b> {cliche}</p>
<div class="paire"><div><img src="{m['fichier']}" width="{w}" height="{h}" alt="{e(titre)}, cliché brut" loading="lazy"><p class="p">Lisez d’abord seul le cliché brut, puis comparez votre lecture à la copie annotée.</p></div>
<div><svg viewBox="0 0 {w} {h}" role="img" aria-label="{e(titre)}, copie annotée"><image href="{m['fichier']}" width="{w}" height="{h}"/>{''.join(marques)}</svg><p class="p">Les numéros posés sur la copie annotée correspondent à la lecture guidée qui suit.</p></div></div>
<div class="p"><b>Lecture guidée.</b><ol>{''.join(lecture)}</ol></div>
<div class="p"><b>Pièges.</b><ul>{pg}</ul></div>
<p class="p"><b>Ce que l’image décide.</b> {decision}</p>
<figcaption>Image : {e(auteur)}, {e(m['licence'])}, <a href="{e(m['url'])}">{e(m['titre'])}</a>, consultée le {m['consulte']}. Copie annotée : œuvre dérivée sous la même licence.</figcaption></figure>'''


def fiche_mb(wid, aria, lignes):
    rows = []
    for k, v in lignes:
        if k == 'Indication':
            continue
        rows.append(f'<tr><th>{k}</th><td>{v}</td></tr>')
    return (f'<section class="fenetre mb" id="{wid}" role="dialog" aria-label="{htmlmod.escape(aria, quote=True)}">'
            f'<div class="fen"><a class="fermer" href="#" aria-label="Fermer">Fermer ✕</a>'
            f'<h4>{htmlmod.escape(aria)}</h4><div class="t" style="overflow-x:auto"><table>'
            + ''.join(rows) + '</table></div></div></section>')


def lien_mb(wid, nom):
    return f'<a class="ouvre" href="#{wid}">{nom}</a>'


# Phrases recopiées de l'information professionnelle lue le 2026-11-15 (cache refdata).
FICHES = {
    '37397': ('Salbutamol — Ventolin®', {
        'Indication': 'Le nébuliseur-doseur traite et prévient les bronchospasmes de l’asthme bronchique, ainsi que le bronchospasme aigu.',
        'Dose': 'Chez l’adulte et l’adolescent de plus de 12 ans, le bronchospasme aigu se traite par 1 à 2 inhalations<sup class="r"><a href="#sb-aips-37397">AIPS 37397</a></sup>.',
        'Contre-indications': 'L’hypersensibilité à un composant et les bêtabloquants non sélectifs, par exemple le propranolol, contre-indiquent Ventolin.',
        'Grossesse': 'Ventolin ne doit pas être pris pendant la grossesse, surtout au premier trimestre, sauf en cas d’indication absolue<sup class="r"><a href="#sb-aips-37397">AIPS 37397</a></sup>.',
        'Allaitement': 'Il convient de ne pas allaiter pendant le traitement par Ventolin, sauf si l’utilité thérapeutique l’emporte sur le risque potentiel<sup class="r"><a href="#sb-aips-37397">AIPS 37397</a></sup>.',
    }),
    '52584': ('Ipratropium — Atrovent®', {
        'Indication': 'Dans l’asthme bronchique, Atrovent s’associe à d’autres bronchodilatateurs pour le traitement aigu des bronchospasmes.',
        'Dose': 'Une dose unitaire prête à l’emploi de 2 ml contient 250 microgrammes de bromure d’ipratropium anhydre<sup class="r"><a href="#sb-aips-52584">AIPS 52584</a></sup>.',
        'Contre-indications': 'Atrovent est contre-indiqué chez les patients qui présentent une hypersensibilité connue à l’atropine ou aux substances atropiniques.',
        'Grossesse': 'Lors de l’emploi d’Atrovent, une prudence particulière est de rigueur, notamment au cours du premier trimestre<sup class="r"><a href="#sb-aips-52584">AIPS 52584</a></sup>.',
        'Allaitement': 'Référence non vérifiée pour cette fiche.',
    }),
    '69640': ('Prednisone — Prednisone Galepharm®', {
        'Indication': 'Il n’existe en général pas de contre-indication lorsque les glucocorticoïdes sont indispensables pour la survie.',
        'Dose': 'Les comprimés existent à 1 mg, 5 mg, 20 mg et 50 mg de prednisone, et la dose clinique reste celle du texte<sup class="r"><a href="#sb-aips-69640">AIPS 69640</a></sup>.',
        'Contre-indications': 'Ce médicament ne doit pas être utilisé en cas d’hypersensibilité à la prednisone ou à l’un des composants.',
        'Grossesse': 'Un traitement prolongé pendant la grossesse peut troubler la croissance intra-utérine, et la fin de grossesse expose à une atrophie corticosurrénalienne fœtale.',
        'Allaitement': 'La prednisone passe dans le lait ; le prescripteur pèse donc le bénéfice maternel et le risque du nourrisson avant de poursuivre.',
    }),
    '29348': ('Prednisolone — Prednisolone Streuli®', {
        'Indication': 'Il n’existe en général pas de contre-indication lorsque les glucocorticoïdes sont indispensables pour la survie du patient.',
        'Dose': 'La dose initiale de l’asthme figure dans le texte du point 11 et reste citée sur cette même information professionnelle<sup class="r"><a href="#sb-aips-29348">AIPS 29348</a></sup>.',
        'Contre-indications': 'La thérapie de substitution n’a pas de contre-indication propre, car elle ne produit pas les effets indésirables d’une dose anti-inflammatoire.',
        'Grossesse': 'Une thérapie prolongée pendant la grossesse peut troubler la croissance intra-utérine et, en fin de grossesse, atrophier le cortex surrénal du fœtus.',
        'Allaitement': 'Le passage dans le lait impose de peser le bénéfice maternel avant de poursuivre la prednisolone chez une femme qui allaite.',
    }),
    '35112': ('Méthylprednisolone — Solu-MEDROL®', {
        'Indication': 'Solu-Medrol sert lorsque la voie orale est impossible ou dans l’urgence, en complément et non à la place du traitement de fond.',
        'Dose': 'Les flacons contiennent 500 mg ou 1 g de méthylprednisolone, et la dose injectée reste celle citée au point 11<sup class="r"><a href="#sb-aips-35112">AIPS 35112</a></sup>.',
        'Contre-indications': 'En pédiatrie, des doses plus faibles que les doses adultes sont en général suffisantes, selon la mise en garde de l’information professionnelle.',
        'Grossesse': 'La méthylprednisolone ne doit être utilisée pendant la grossesse qu’après une évaluation rigoureuse des risques et des bénéfices<sup class="r"><a href="#sb-aips-35112">AIPS 35112</a></sup>.',
        'Allaitement': 'Il ne faut pas allaiter en cas d’utilisation de Solu-Medrol, car la méthylprednisolone passe dans le lait et peut nuire au nourrisson<sup class="r"><a href="#sb-aips-35112">AIPS 35112</a></sup>.',
    }),
    '55568': ('Budésonide et formotérol — Symbicort®', {
        'Indication': 'Symbicort Turbuhaler associe un corticoïde inhalé et un β2-agoniste de longue durée pour l’asthme qui exige les deux.',
        'Dose': 'Les dosages 100/6, 200/6 et 400/12 µg sont ceux du Turbuhaler, et le plafond quotidien reste celui du texte<sup class="r"><a href="#sb-aips-55568">AIPS 55568</a></sup>.',
        'Contre-indications': 'L’hypersensibilité au budésonide, au formotérol ou au lactose inhalé contre-indique Symbicort Turbuhaler.',
        'Grossesse': 'On ne dispose d’aucune étude menée chez des femmes enceintes avec Symbicort Turbuhaler ou avec les deux principes associés.',
        'Allaitement': 'Le passage des deux principes dans le lait n’est pas quantifié ici ; la conduite suit l’information professionnelle citée.',
    }),
    '50192': ('Budésonide — Pulmicort®', {
        'Indication': 'Pulmicort est indiqué dans l’asthme bronchique et la bronchite chronique obstructive lorsqu’une corticothérapie d’entretien est nécessaire.',
        'Dose': 'Le Turbuhaler délivre 100 µg, 200 µg ou 400 µg de budésonide, selon la présentation choisie<sup class="r"><a href="#sb-aips-50192">AIPS 50192</a></sup>.',
        'Contre-indications': 'L’hypersensibilité connue au budésonide ou à l’un des excipients contre-indique Pulmicort.',
        'Grossesse': 'La prudence est de mise en cas d’emploi pendant la grossesse, car l’expérimentation animale a montré des effets sur le fœtus<sup class="r"><a href="#sb-aips-50192">AIPS 50192</a></sup>.',
        'Allaitement': 'Le budésonide est excrété dans le lait maternel, mais les doses thérapeutiques n’y laissent prévoir que de faibles concentrations.',
    }),
    '56551': ('Adrénaline — Adrenalin Sintetica®', {
        'Indication': 'Adrenalin Sintetica est indiquée dans le choc anaphylactique, la crise d’asthme et la réanimation cardiopulmonaire.',
        'Dose': 'Une ampoule de 1 ml contient 1 mg d’adrénaline, et la voie ainsi que la dose d’âge restent celles du texte<sup class="r"><a href="#sb-aips-56551">AIPS 56551</a></sup>.',
        'Contre-indications': 'Par voie systémique hors menace vitale, l’hypertension, l’hyperthyroïdie et les maladies coronariennes contre-indiquent cette adrénaline.',
        'Grossesse': 'L’adrénaline traverse le placenta et peut provoquer une tachycardie ainsi qu’une anoxie chez le fœtus, ce qui pèse dans la décision.',
        'Allaitement': 'L’adrénaline passe dans le lait maternel, et l’adrénaline prise par voie orale est métabolisée très rapidement.',
    }),
    '56394': ('Sulfate de magnésium — Bichsel®', {
        'Indication': 'L’asthme aigu ne figure pas parmi les indications de Sulfate de magnésium Bichsel ; la dose de crise est donc hors AIPS.',
        'Dose': 'Une ampoule à 10 ml de la solution à 20 % contient 2,0 g de sulfate de magnésium heptahydraté<sup class="r"><a href="#sb-aips-56394">AIPS 56394</a></sup>.',
        'Contre-indications': 'Le bloc auriculoventriculaire des degrés I à III et la myasthénie grave contre-indiquent le sulfate de magnésium.',
        'Grossesse': 'Des études contrôlées n’ont pas montré de risque fœtal au premier trimestre, mais aucune étude n’a porté sur cette spécialité.',
        'Allaitement': 'Référence non vérifiée pour cette fiche.',
    }),
    '53836': ('Adrénaline — EpiPen®', {
        'Indication': 'L’injecteur sert au traitement d’urgence, par le patient lui-même, d’une anaphylaxie aux piqûres, aux aliments ou aux médicaments.',
        'Dose': 'La dose habituelle chez l’adulte est de 0,3 mg par voie intramusculaire, et l’enfant reçoit 0,01 mg/kg<sup class="r"><a href="#sb-aips-53836">AIPS 53836</a></sup>.',
        'Contre-indications': 'Lorsque l’allergie menace la vie, il n’y a pas de contre-indication absolue à l’emploi d’EpiPen ou d’EpiPen Junior.',
        'Grossesse': 'L’adrénaline traverse le placenta et peut provoquer une tachycardie, des extrasystoles et une anoxie chez le fœtus<sup class="r"><a href="#sb-aips-53836">AIPS 53836</a></sup>.',
        'Allaitement': 'L’adrénaline passe dans le lait maternel, puis elle est métabolisée très rapidement si elle est prise par voie orale.',
    }),
    '30630': ('Furosémide — Lasix®', {
        'Indication': 'Lasix est indiqué dans l’insuffisance cardiaque aiguë, en particulier l’œdème pulmonaire, associé aux autres mesures.',
        'Dose': 'L’ampoule contient 20 mg de furosémide, et la dose injectée dans l’œdème aigu reste celle citée au point 11<sup class="r"><a href="#sb-aips-30630">AIPS 30630</a></sup>.',
        'Contre-indications': 'La défaillance rénale avec anurie, ainsi que le coma et le précoma hépatique, contre-indiquent le furosémide.',
        'Grossesse': 'Le furosémide traverse le placenta et atteint dans le sang du cordon une concentration égale à celle du sérum maternel.',
        'Allaitement': 'Le passage dans le lait est connu des diurétiques de l’anse ; la conduite suit l’information professionnelle citée, sans dose inventée.',
    }),
    '49456': ('Énoxaparine — Clexane®', {
        'Indication': 'Clexane traite et prévient les thromboses, et la dose de l’embolie suit l’information professionnelle ainsi que le texte.',
        'Dose': 'La seringue et la dose en mg/kg de l’embolie restent celles du point 11, citées sur cette information professionnelle<sup class="r"><a href="#sb-aips-49456">AIPS 49456</a></sup>.',
        'Contre-indications': 'L’hypersensibilité à l’énoxaparine ou à l’héparine, et l’endocardite bactérienne aiguë, contre-indiquent Clexane.',
        'Grossesse': 'Chez des femmes porteuses d’une valve cardiaque, une dose prophylactique n’a pas toujours empêché une thrombose de valve.',
        'Allaitement': 'Le passage dans le lait n’est pas le message principal de la fiche ; on ne fabrique pas une conduite absente du passage lu.',
    }),
    '58728': ('Rivaroxaban — Xarelto®', {
        'Indication': 'Xarelto est un anticoagulant oral dont l’indication précise de l’embolie reste celle de l’information professionnelle citée.',
        'Dose': 'La dose adulte de l’embolie figure au point 11 et doit rester dans le texte de cette information professionnelle<sup class="r"><a href="#sb-aips-58728">AIPS 58728</a></sup>.',
        'Contre-indications': 'Le rivaroxaban est contre-indiqué pendant la grossesse et exige une contraception très efficace chez la femme en âge de procréer<sup class="r"><a href="#sb-aips-58728">AIPS 58728</a></sup>.',
        'Grossesse': 'Il n’existe pas de données sur l’utilisation du rivaroxaban chez la femme enceinte, et la grossesse contre-indique le produit.',
        'Allaitement': 'Aucune donnée n’est disponible sur le rivaroxaban chez les femmes qui allaitent, et l’animal montre un passage dans le lait.',
    }),
    '56203': ('Amoxicilline — Amoxicilline Sandoz®', {
        'Indication': 'L’amoxicilline traite des infections à germes sensibles, dont des infections respiratoires, lorsque la voie orale suffit.',
        'Dose': 'Les comprimés existent à 500 mg, 750 mg et 1 g, et la dose de la pneumonie reste celle du point 11<sup class="r"><a href="#sb-aips-56203">AIPS 56203</a></sup>.',
        'Contre-indications': 'L’amoxicilline ne doit pas être administrée en cas d’hypersensibilité aux pénicillines ou aux céphalosporines.',
        'Grossesse': 'Les études animales n’ont pas montré d’effet sur le fœtus, mais aucune étude contrôlée n’a été réalisée chez la femme enceinte.',
        'Allaitement': 'L’amoxicilline diffuse dans le lait maternel et peut provoquer une sensibilisation ou une diarrhée chez le nouveau-né.',
    }),
    '67169': ('Clarithromycine — Clarithromycine Spirig HC®', {
        'Indication': 'La clarithromycine traite des infections respiratoires à germes sensibles lorsque la gravité n’impose pas la voie parentérale.',
        'Dose': 'Les comprimés contiennent 250 mg ou 500 mg de clarithromycine, et le schéma du point 11 cite cette fiche<sup class="r"><a href="#sb-aips-67169">AIPS 67169</a></sup>.',
        'Contre-indications': 'On ne donne pas la clarithromycine en cas d’hypersensibilité aux macrolides ni avec le cisapride, le pimozide ou la terfénadine.',
        'Grossesse': 'Les données chez la femme enceinte sont insuffisantes, et l’animal suggère des effets embryo- et fœtotoxiques après prise orale.',
        'Allaitement': 'La clarithromycine est excrétée dans le lait, où elle atteint environ 25 % de la concentration sérique à 250 mg deux fois par jour<sup class="r"><a href="#sb-aips-67169">AIPS 67169</a></sup>.',
    }),
}


def poser_fiches(h, numeros):
    blocs = []
    for n in numeros:
        aria, lignes = FICHES[n]
        wid = f'f-mb-{n}'
        blocs.append(fiche_mb(wid, aria, list(lignes.items())))
        # premier nombre Swissmedic nu devient un lien si pas déjà lié
        if f'#f-mb-{n}' not in h:
            h = h.replace(f'Swissmedic {n}', f'Swissmedic {lien_mb(wid, n)}', 1)
    # avant la section sources
    m = re.search(r'<section class="ilot" id="[^"]*sources"', h)
    return h[:m.start()] + '\n'.join(blocs) + '\n' + h[m.start():]


FIG_HAUT = None  # rempli dans main via chemins


def traiter(nom, titre_h2, regions, sid_p, fiches, figures):
    chemin = ROOT / nom
    h = chemin.read_text(encoding='utf-8')
    avant = len(h.encode())
    h = convertir_popover(h)
    if regions:
        h = fenetrer_point(h, sid_p, regions)
    for sid, bloc in figures:
        h = inserer_avant_fin_section(h, sid, bloc)
    h = poser_fiches(h, fiches)
    m = re.search(r'<section class="ilot" id="[^"]*sources"', h)
    corps, src = h[:m.start()], h[m.start():]
    table, lignes = indexer(src)
    corps = retirer_doublons_ancres(corps, table)
    corps = re.sub(r'<style>.*?</style>', '', corps, flags=re.S)
    corps = corps.replace('<strong>1. Définition et sémantique</strong>', '<strong>1. Définition</strong>')
    corps = corps.replace('LOT_049 — ', '')
    if 'Phase_B' in nom:
        ancre = ('<div class="p">Cette monographie développe l’asthme en exacerbation, qui appartient à la situation '
                 '<a href="LOT_049_Phase_A_V0.html">respiration douloureuse, sibilances, stridor</a>.</div>')
        corps = corps.replace('</h2>', '</h2>' + ancre, 1)
    else:
        corps = corps.replace(
            '<title>S2.10 — Respiration douloureuse, sibilances, stridor</title>',
            '<title>S2.10 — Respiration douloureuse, sibilances, stridor</title>')
        # le titre portait LOT_049 — qui a déjà été retiré
    corps, ncar = limiter_car(corps)
    ordre = []
    for cid, ligne in lignes.items():
        if cid not in ordre:
            ordre.append(cid)
    biblio = ('<section class="ilot" id="' + ('dx1-sources' if 'Phase_B' in nom else 'pa-sources') +
              '"><h3>Sources</h3><ol>\n' + '\n'.join(lignes[c] for c in ordre) +
              '</ol><p class="p">Le contenu reprend les sources citées ; il n’a pas été validé cliniquement par un médecin.</p></section>')
    h = corps + biblio + '\n</main></body></html>\n'
    fin = '<!-- FIN_FICHIER LOT_049_Phase_B_V0_DX.1 -->' if 'Phase_B' in nom else '<!-- FIN_FICHIER LOT_049_Phase_A_V0 -->'
    if fin not in h:
        h = h.rstrip() + '\n' + fin + '\n'
    chemin.write_text(h, encoding='utf-8')
    print(f'{nom}: {avant} → {len(h.encode())} octets ; car initiaux comptés jusqu’au remplacement ; popover restants {h.count("popover")}')


def main():
    img = ROOT / 'images'
    haut = figure(
        img / 'Blausen_0872_UpperRespiratorySystem.json',
        'Voies aériennes supérieures',
        'Blausen montre en couleurs le nez, le pharynx, le larynx et la trachée, avec des légendes en anglais.',
        [
            (78, 30, 'Les cornets et la fosse nasale filtrent l’air, mais le stridor ne naît pas à cet étage.'),
            (22, 48, 'L’oropharynx conduit l’air vers le larynx, et un obstacle ici donne un bruit inspiratoire.'),
            (70, 78, 'La glotte et les cordes vocales rétrécissent la filière, ce qui produit le stridor aigu.'),
            (12, 68, 'La trachée prolonge le larynx, et ce schéma s’arrête avant les bronches du wheezing.'),
        ],
        ['Les légendes anglaises ne sont pas une traduction clinique : on lit la structure, pas le mot anglais.',
         'Ce schéma ne montre pas les bronches, donc il n’explique pas la sibilance expiratoire.'],
        'Un bruit inspiratoire oriente vers cette filière haute, et le traitement de l’obstruction haute passe avant le bronchodilatateur.',
    )
    zone = figure(
        img / '2309_The_Respiratory_Zone.json',
        'Zone respiratoire et muscle lisse bronchiolaire',
        'OpenStax montre en couleurs la bronchiole terminale, le muscle lisse et les alvéoles, avec des légendes en anglais.',
        [
            (48, 8, 'La bronchiole terminale amène l’air vers les alvéoles, et c’est l’étage du wheezing.'),
            (28, 22, 'Le muscle lisse entoure la bronchiole, et sa contraction rétrécit le calibre expiratoire.'),
            (62, 48, 'La bronchiole respiratoire précède les alvéoles, là où l’obstruction siffle à l’expiration.'),
            (78, 72, 'L’alvéole et les capillaires échangent les gaz, en aval du rétrécissement qui siffle.'),
        ],
        ['Le schéma est sain : il ne montre ni bouchon muqueux ni spasme, seulement le lieu du spasme.',
         'Un stridor inspiratoire ne se lit pas sur cette image, car le larynx n’y figure pas.'],
        'Une sibilance expiratoire naît de ce rétrécissement distal, et le bronchodilatateur vise le muscle lisse dessiné ici.',
    )
    boucle = figure(
        img / 'Flow-volume-loop.json',
        'Boucle débit-volume, schéma normal',
        'Le schéma montre une boucle normale, et les valeurs de volume qui y sont dessinées sont seulement illustratives.',
        [
            (22, 10, 'Le sommet est le débit expiratoire de pointe, premier repère d’une expiration forcée.'),
            (45, 28, 'La branche expiratoire descend ensuite, et l’obstruction asthmatique la creuse.'),
            (60, 48, 'L’axe horizontal porte le volume, de l’inspiration vers la droite sur ce dessin.'),
            (38, 68, 'Sous l’axe, la branche inspiratoire complète la boucle d’un sujet sans obstruction.'),
        ],
        ['Les chiffres de volume du dessin ne sont pas des normes : on ne les cite pas comme seuils.',
         'Cette boucle est normale, donc l’absence de creux ne permet pas d’exclure un asthme entre les crises.'],
        'La spirométrie reste l’examen de référence de l’asthme, et une crise sévère ne doit pas attendre cette courbe.',
    )
    traiter(
        'LOT_049_Phase_A_V0.html',
        'S2.10 — Respiration douloureuse, sibilances, stridor',
        [
            (1, 3, 'f-pa-p6-vital', 'Inspection générale et signes vitaux'),
            (4, 9, 'f-pa-p6-croup', 'Faux-croup et score de Westley'),
            (10, 12, 'f-pa-p6-auscult', 'Auscultation'),
            (13, 13, 'f-pa-p6-pneumo', 'Pneumonie'),
            (14, 15, 'f-pa-p6-oedeme', 'Œdème pulmonaire'),
            (16, 16, 'f-pa-p6-ce', 'Inhalation de corps étranger'),
            (17, 17, 'f-pa-p6-ana', 'Anaphylaxie'),
            (18, 18, 'f-pa-p6-ep', 'Embolie pulmonaire'),
        ],
        'pa-p6',
        ['53836', '37397', '69640', '52584', '30630', '49456', '58728', '56203', '67169'],
        [('pa-p3', haut), ('pa-p9', boucle)],
    )
    traiter(
        'LOT_049_Phase_B_V0_DX.1.html',
        'DX.1 — Asthme (exacerbation asthmatique)',
        [
            (1, 2, 'f-dx1-p6-general', 'État général'),
            (3, 4, 'f-dx1-p6-thorax', 'Inspection du thorax'),
            (5, 7, 'f-dx1-p6-vitaux', 'Fréquence et saturation'),
            (8, 9, 'f-dx1-p6-auscult', 'Auscultation'),
            (10, 11, 'f-dx1-p6-dep', 'Débit expiratoire de pointe'),
            (13, 14, 'f-dx1-p6-sev', 'Degrés de sévérité'),
        ],
        'dx1-p6',
        ['37397', '52584', '69640', '29348', '35112', '55568', '50192', '56551', '56394'],
        [('dx1-p3', zone), ('dx1-p9', boucle)],
    )


if __name__ == '__main__':
    main()
