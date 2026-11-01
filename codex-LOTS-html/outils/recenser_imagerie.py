#!/usr/bin/env python3
"""Repérage documentaire de l'imagerie et des ECG, sans modifier les leçons."""
import csv
import hashlib
import json
import re
import subprocess
from datetime import datetime, timezone
from html import escape
from pathlib import Path
from lxml import html

B = Path(__file__).resolve().parents[1]
R = B.parent
D = B / 'imagerie_20261101'
MOTIFS = {
    'ECG': r'\bECG\b|électrocardio\w+',
    'IRM': r'\bIRM\b|résonance magnétique',
    'Scanner': r'\bTDM\b|\bscanner\b|tomodensitom\w+|angioscanner',
    'Radiographie': r'radiograph\w+',
    'Échographie / Doppler': r'échograph\w+|échocardiograph\w+|ultrason\w+|\bDoppler\b',
    'OCT': r'\bOCT(?:A)?\b|tomographie par cohérence optique',
    'Angiographie': r'angiograph\w+',
    'Endoscopie / laryngoscopie': r'endoscop\w+|(?:naso)?fibroscop\w+|laryngoscop\w+|stroboscop\w+|rhinoscop\w+|\bFEES\b',
    'Vidéofluoroscopie / transit': r'vid[ée]ofluoroscop\w+|\bVFSS\b|transit (?:pharyngo[-‑])?(?:œsophag\w+|oesophag\w+)|transit baryt\w+',
    'Fond d’œil / rétinographie': r'fond(?:s)? d[’\x27 ](?:œil|oeil|yeux)|rétinograph\w+',
    'Scintigraphie / TEP': r'scintigraph\w+|\bTEP\b|\bPET(?:-CT)?\b|tomographie par émission de posit(?:ons|rons)',
    'Imagerie non précisée': r'\bimagerie\b',
}
REGEX = {k: re.compile(v, re.I) for k, v in MOTIFS.items()}


def texte(node):
    return ' '.join(' '.join(node.itertext()).split())


def analyser(p):
    raw = p.read_bytes()
    doc = html.document_fromstring(raw.decode('utf-8'))
    heads = doc.xpath('//h1') or doc.xpath('//h2')
    titre = texte(heads[0]) if heads else p.stem
    sections = doc.xpath('//h2[contains(@id,"-p9")]/parent::section')
    if len(sections) != 1:
        raise ValueError(f'Section 9 non unique : {p}')
    roots = list(sections)
    ids = set()
    # Les détails d'examens sont souvent dans des popovers hors de la section.
    for root in roots:
        for target in root.xpath('.//*[@popovertarget]/@popovertarget'):
            if target in ids:
                continue
            ids.add(target)
            nodes = doc.xpath('//*[@id=$id]', id=target)
            if len(nodes) != 1:
                raise ValueError(f'Cible absente ou ambiguë : {p}#{target}')
            corps = nodes[0].xpath('./*[@class="corps"]')
            roots.append(corps[0] if corps else nodes[0])
    passages = []
    vus = set()
    for root in roots:
        for node in root.xpath('.//p|.//li[not(.//p)]|.//tr'):
            t = texte(node)
            if not t or t in vus:
                continue
            vus.add(t)
            categories = [k for k, rx in REGEX.items() if rx.search(t)]
            if not categories:
                continue
            parents = node.xpath('ancestor-or-self::*[@id]')
            anchor = parents[-1].get('id') if parents else sections[0].xpath('./h2/@id')[0]
            passages.append({'categories': categories, 'extrait_exact_normalise': t,
                             'ancre': anchor, 'statut': 'à relire : indication, exclusion ou contexte'})
    return {'lot': int(p.parent.name.split('_')[1]), 'fichier': str(p.relative_to(B)),
            'titre': titre, 'sha256': hashlib.sha256(raw).hexdigest(),
            'fenetres_parcourues': sorted(ids), 'passages': passages,
            'categories': sorted({c for x in passages for c in x['categories']})}


def produire():
    assert (B / '_cache/production.lock').exists(), 'Verrou requis'
    res = json.loads((R / 'IA_RESERVATIONS.json').read_text())['codex']
    assert subprocess.check_output(['git', 'branch', '--show-current'], cwd=R, text=True).strip() == res['branche'] == 'codex/lots'
    subprocess.run(['python3', '-B', str(B/'registre_ia.py'), 'pret', 'codex'], cwd=R, check=True)
    bornes = res['plage']
    def ordre(p):
        dx = re.search(r'DX\.(\d+)', p.name)
        return int(p.parent.name.split('_')[1]), int(dx[1]) if dx else 0
    lecons = [analyser(p) for p in sorted(B.glob('LOT_*/*.html'), key=ordre)
              if bornes[0] <= int(p.parent.name.split('_')[1]) <= bornes[1]]
    catalogue = {int(r['lot']): r for r in csv.DictReader((R/'LOT_Claude_Finaux/CATALOGUE_248.csv').open())}
    lots = []
    for n in range(bornes[0], bornes[1]+1):
        rows = [r for r in lecons if r['lot'] == n]
        lots.append({'lot': n, 'ssp': catalogue[n]['ssp_profiles_2023_fr_en'],
                     'lecons_presentes': len(rows), 'lecons_avec_mentions': sum(bool(r['passages']) for r in rows),
                     'passages': sum(len(r['passages']) for r in rows),
                     'categories': sorted({c for r in rows for c in r['categories']}),
                     'statut': 'recensement des textes présents' if rows else 'non rédigé : examens non évaluables'})
    data = {'date': datetime.now(timezone.utc).isoformat(timespec='seconds'), 'borne': bornes,
            'commit_source': subprocess.check_output(['git','rev-parse','HEAD'],cwd=R,text=True).strip(),
            'methode': 'Section 9 et fenêtres liées récursivement ; repérage lexical, sans conclusion automatique sur l’indication.',
            'limites': 'Une mention peut déconseiller un examen ou concerner un diagnostic alternatif. Absence de mot repéré ne prouve pas absence de besoin iconographique. Les autres parties et les lots non rédigés ne sont pas évalués par ce repérage.',
            'consigne': 'Même cliché : original à gauche sans annotation ajoutée, copie annotée à droite ; pointillés rouges contrastés, repères numérotés et légende française. Les deux restent dans la fenêtre. Source, licence et contrôle visuel obligatoires.',
            'lots': lots, 'lecons': lecons,
            'totaux': {'lots_autorises': len(lots), 'lots_avec_textes': sum(bool(r['lecons_presentes']) for r in lots),
                       'lecons': len(lecons), 'lecons_avec_mentions': sum(bool(r['passages']) for r in lecons),
                       'passages': sum(len(r['passages']) for r in lecons)}}
    triage = json.loads((D/'TRIAGE.json').read_text()) if (D/'TRIAGE.json').exists() else {'lecons': []}
    par_fichier = {r['fichier']: r for r in triage['lecons']}
    for row in lecons:
        if row['fichier'] in par_fichier:
            revue = par_fichier[row['fichier']]
            assert row['sha256'] == revue['sha256_lecon'], 'Triage à refaire : leçon modifiée'
            assert [hashlib.sha256(x['extrait_exact_normalise'].encode()).hexdigest() for x in row['passages']] == [x['sha256_texte'] for x in revue['passages_lus']], 'Triage à revoir : passages modifiés'
    data['triage_documentaire_lecons'] = len(par_fichier)
    D.mkdir(exist_ok=True)
    (D/'INVENTAIRE.json').write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
    e = escape
    out = ['<!doctype html><html lang="fr"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Imagerie et ECG — inventaire des LOTS</title>',
           '<style>body{font:17px/1.55 system-ui,sans-serif;background:#f2f6f8;color:#173448;margin:0}main{max-width:1160px;margin:auto;padding:24px}h1{font-size:2rem}a{color:#006184}details,.note{background:white;border:1px solid #bacbd5;border-radius:8px;padding:14px;margin:12px 0}summary{cursor:pointer;font-weight:650}input,select{font:inherit;padding:8px;max-width:100%;box-sizing:border-box}.filtres{display:flex;gap:12px;flex-wrap:wrap}blockquote{margin:10px 0;border-left:4px solid #168499;padding:10px 16px;background:#eff7fa;overflow-wrap:anywhere}.tag{color:#785213;font-weight:600}.table{overflow:auto}table{border-collapse:collapse;width:100%;min-width:720px}td,th{text-align:left;border:1px solid #bacbd5;padding:8px;vertical-align:top}small{color:#435c69}[hidden]{display:none!important}@media(max-width:600px){main{padding:14px}h1{font-size:1.6rem}}</style><main>',
           '<h1>Imagerie et ECG : où rechercher les illustrations</h1>',
           f'<p>Inventaire du {e(data["date"])} · LOTS {bornes[0]:03}–{bornes[1]:03} · source {e(data["commit_source"][:8])}.</p>',
           f'<p><strong>{len(lecons)} leçons parcourues ; {data["totaux"]["lecons_avec_mentions"]} avec au moins une mention ; {data["totaux"]["passages"]} passages repérés.</strong></p>',
           f'<p><strong>{len(par_fichier)} leçons triées en contexte.</strong> Les objectifs d’illustration et les pièges sont affichés dans les fiches concernées. Ce tri documentaire ne vaut pas validation médicale.</p>',
           '<div class="note"><strong>Repérage documentaire à relire.</strong> '+e(data['methode'])+' '+e(data['limites'])+'</div>',
           '<p>'+e(data['consigne'])+'</p>',
           '<p>Aucun cliché nouveau acquis ni intégré par cet inventaire. Les domaines de téléchargement Wikimedia et CDN NCBI restent exclus de la configuration réseau au dernier contrôle. Les neuf candidats retenus du LOT_018 restent sous réserve visuelle ; un autre est suspendu pour provenance discordante.</p>',
           '<p><a href="BILAN_CLICHES_LOT_018.html">Candidats déjà documentés et tailles du LOT_018</a> · <a href="imagerie_20261101/INVENTAIRE.json">Données, extraits et empreintes</a></p>',
           '<details><summary>Couverture des lots attribués</summary><div class="table"><table><thead><tr><th>Lot / SSP</th><th>Leçons présentes</th><th>Leçons avec mention</th><th>Modalités repérées</th></tr></thead><tbody>']
    for lot in lots:
        out.append(f'<tr data-lot="{lot["lot"]}"><td>{lot["lot"]:03} — {e(lot["ssp"])}</td><td>{lot["lecons_presentes"]}</td><td>{lot["lecons_avec_mentions"] if lot["lecons_presentes"] else "Non évaluable"}</td><td>{e(", ".join(lot["categories"]) or lot["statut"])}</td></tr>')
    out += ['</tbody></table></div></details><h2>Passages à examiner</h2><div class="filtres"><label>Rechercher <input id="recherche" type="search" placeholder="Lot, diagnostic ou mot"></label><label>Modalité <select id="modalite"><option value="">Toutes</option>']
    out += [f'<option>{e(k)}</option>' for k in MOTIFS]
    out += ['</select></label></div><p id="compte" role="status"></p>']
    for row in lecons:
        if not row['passages']:
            continue
        out.append(f'<details class="lecon" data-categories="{e(json.dumps(row["categories"],ensure_ascii=False),quote=True)}"><summary>LOT_{row["lot"]:03} — {e(row["titre"])} · {len(row["passages"])} passages</summary>')
        if row['fichier'] in par_fichier:
            revue = par_fichier[row['fichier']]
            out.append(f'<aside class="note" data-triage="effectue"><strong>Projet d’illustration : {e(revue["objectif_iconographique"])}</strong><p>{e(revue["contexte"])}</p><p><strong>Piège à préserver :</strong> {e(revue["piege"])}</p><small>Tri documentaire interne ; aucun cliché acquis ou observé dans cette passe.</small></aside>')
        for i, x in enumerate(row['passages'], 1):
            out.append(f'<article><p class="tag">{i}. {e(", ".join(x["categories"]))} — à relire</p><blockquote>{e(x["extrait_exact_normalise"])}</blockquote><a href="{e(row["fichier"])}#{e(x["ancre"])}">Ouvrir la leçon source</a></article>')
        out.append('</details>')
    if (D/'CANDIDATS_ORL.json').exists():
        selection = json.loads((D/'CANDIDATS_ORL.json').read_text())
        out.append('<h2>Pistes iconographiques du LOT_019</h2><p>Deux candidats CC BY 4.0 retenus sous réserve visuelle, deux en réserve pour version de licence à établir ; un candidat exclu pour licence NC. Aucun original acquis.</p>')
        for c in selection['candidats']:
            decision = {'retenu_documentaire_sous_reserve_visuelle': 'Retenu sous réserve visuelle', 'reserve_version_licence': 'Réserve : licence à préciser'}[c['decision']]
            out.append(f'<details class="candidat"><summary>{e(c["titre"])} — {e(decision)}</summary><p>{e(c["auteur"])} · {e(c.get("licence",c.get("licence_annoncee","")))}</p><p>{e(c.get("piege",c.get("condition","")))}</p><a href="{e(c["source_url"])}">Publication source</a></details>')
        out.append(f'<p><a href="imagerie_20261101/CANDIDATS_ORL.json">Crédits et décisions détaillés</a> · <a href="imagerie_20261101/TRIAGE.json">Tri des {len(par_fichier)} leçons</a> · <a href="imagerie_20261101/sources_orl/LECTURES.json">Lectures suisses et européennes</a></p>')
    sans_mention = [r for r in lecons if not r['passages'] and r['fichier'] in par_fichier]
    if sans_mention:
        out.append(f'<h2>Fenêtres relues sans mention repérée</h2><p>Ces leçons ne figurent pas parmi les {data["totaux"]["lecons_avec_mentions"]} fiches filtrables ci-dessus. Leur bilan peut justifier une photographie clinique ou un schéma documenté. L’absence de mot-clé ne signifie pas absence de besoin visuel.</p>')
        for row in sans_mention:
            revue = par_fichier[row['fichier']]
            out.append(f'<details class="sans-imagerie"><summary>LOT_{row["lot"]:03} — {e(row["titre"])}</summary><aside data-triage="effectue"><strong>{e(revue["objectif_iconographique"])}</strong><p>{e(revue["contexte"])}</p><p><strong>Piège :</strong> {e(revue["piege"])}</p><a href="{e(row["fichier"])}#{e(revue["extrait_supplementaire_lu"]["ancre"])}">Ouvrir la fenêtre source</a></aside></details>')
    suite = D/'tri_020_021/CANDIDATS.json'
    if suite.exists():
        selection = json.loads(suite.read_text())
        out.append('<h2>Pistes iconographiques des LOT_020 et LOT_021</h2><p>Trois candidats CC BY 4.0 documentés ; aucun cliché acquis ou inspecté. Une source NC/ND refusée, une autre en réserve pour licence à préciser.</p>')
        for c in selection['candidats']:
            out.append(f'<details class="candidat-suite"><summary>LOT_{c["lot"]:03} — {e(c["titre"])}</summary><p>{e(c["auteur"])} · {e(c["licence"])}</p><p>{e(c["piege"])}</p><a href="{e(c["source_url"])}">Publication source</a></details>')
        out.append('<p><a href="imagerie_20261101/tri_020_021/CANDIDATS.json">Crédits et décisions détaillés</a> · <a href="imagerie_20261101/tri_020_021/LECTURES.json">Lectures et limites</a></p>')
    suite = D/'tri_022_024/CANDIDATS.json'
    if suite.exists():
        selection = json.loads(suite.read_text())
        out.append('<h2>Pistes iconographiques des LOT_023 et LOT_024</h2><p>Quatre candidats documentés sous licences CC BY 2.0 ou 4.0 ; aucun cliché acquis ou inspecté. Le tri des LOT_022–024 comprend aussi les photographies cliniques et les examens dynamiques.</p>')
        for c in selection['candidats']:
            out.append(f'<details class="candidat-nouveau"><summary>LOT_{c["lot"]:03} — {e(c["titre"])}</summary><p>{e(c["auteur"])} · {e(c["licence"])}</p><p>{e(c["piege"])}</p><a href="{e(c["source_url"])}">Publication source</a></details>')
        out.append('<p><a href="imagerie_20261101/tri_022_024/CANDIDATS.json">Crédits et décisions détaillés</a> · <a href="imagerie_20261101/tri_022_024/LECTURES.json">Lectures et limites</a></p>')
    # Les campagnes suivantes apparaissent sans ajout manuel d'une nouvelle section HTML.
    for suite in sorted(D.glob('tri_*/CANDIDATS.json')):
        if suite.parent.name in ('tri_020_021', 'tri_022_024'):
            continue
        selection = json.loads(suite.read_text())
        campagne = suite.parent.name
        out.append(f'<h2>Campagne {e(campagne.replace("tri_", "").replace("_", "–"))} : figures candidates</h2><p>{len(selection["candidats"])} figures documentées. Les cibles désignent les leçons envisagées ; elles ne prouvent pas une intégration.</p>')
        if selection.get('limite'):
            out.append(f'<p class="note">{e(selection["limite"])}</p>')
        for c in selection['candidats']:
            etat = 'Original acquis' if c.get('original_acquis') else 'Original non acquis'
            out.append(f'<details class="candidat-auto" data-campagne="{e(campagne)}"><summary>{e(c["titre"])}</summary><p>Cibles : {e(", ".join(c["cibles"]))}</p><p>{e(c["auteur"])} · {e(c["licence"])} · accès : {e(c["acces_le"])}</p><p>{e(etat)} ; inspection visuelle : {"oui" if c.get("pixels_inspectes") else "non"}.</p><p>{e(c["piege"])}</p><a href="{e(c["source_url"])}">Publication source</a></details>')
        out.append(f'<p><a href="imagerie_20261101/{e(campagne)}/CANDIDATS.json">Crédits et décisions détaillés</a> · <a href="imagerie_20261101/{e(campagne)}/LECTURES.json">Lectures et limites</a></p>')
    out += ['<script>const q=document.querySelector("#recherche"),m=document.querySelector("#modalite"),rows=[...document.querySelectorAll("details.lecon")];function filtre(){let n=0;for(const r of rows){const ok=r.textContent.toLocaleLowerCase("fr").includes(q.value.toLocaleLowerCase("fr"))&&(!m.value||JSON.parse(r.dataset.categories).includes(m.value));r.hidden=!ok;if(ok)n++;}document.querySelector("#compte").textContent=n+" leçons affichées";}q.addEventListener("input",filtre);m.addEventListener("change",filtre);filtre();</script>',
            '<footer><p>Les extraits décrivent les textes présents, sans nouvelle validation médicale. La sélection de chaque cliché devra préciser le signe visible, le contexte clinique, les limites et les droits de réutilisation.</p></footer></main></html>']
    (B/'BILAN_IMAGERIE_ECG.html').write_text('\n'.join(out)+'\n')
    print(json.dumps(data['totaux'],ensure_ascii=False))


if __name__ == '__main__':
    produire()
