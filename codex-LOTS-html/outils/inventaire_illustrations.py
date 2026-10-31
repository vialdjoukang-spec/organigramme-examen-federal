#!/usr/bin/env python3
"""Inventaire reproductible, lecture seule des leçons et du harnais commun."""
import csv
import hashlib
import importlib.util
import json
import re
import subprocess
import sys
from datetime import datetime, timezone
from html import escape
from pathlib import Path
from lxml import html

sys.dont_write_bytecode = True
BASE = Path(__file__).resolve().parents[1]
ROOT = BASE.parent
OUT = BASE / 'illustrations_20261031'


def collect():
    reservation = json.loads((ROOT / 'IA_RESERVATIONS.json').read_text())['codex']
    branch = subprocess.check_output(['git', 'branch', '--show-current'], cwd=ROOT, text=True).strip()
    if branch != reservation['branche']:
        raise RuntimeError('Branche non autorisée')
    spec = importlib.util.spec_from_file_location('mesure_originale', ROOT / 'harnais/taille_xy.py')
    mesure = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mesure)
    catalogue = {int(r['lot']): r for r in csv.DictReader((ROOT / 'LOT_Claude_Finaux/CATALOGUE_248.csv').open())}
    rows, lots = [], []
    reviewed = {}
    proof = BASE / 'LOT_018/illustrations/REVUE_VISUELLE.json'
    integrity = BASE / 'LOT_018/illustrations/CONTROLE_INTEGRITE.json'
    if proof.exists() and integrity.exists():
        reviewed = {r['fichier']: r['sha256'] for r in json.loads(integrity.read_text())}
    for directory in sorted(BASE.glob('LOT_[0-9][0-9][0-9]')):
        n = int(directory.name[4:])
        paths = sorted(directory.glob('LOT_*_Phase_*.html'), key=lambda p: 0 if '_Phase_A_' in p.name else int(re.search(r'DX\.(\d+)', p.name)[1]))
        if not paths:
            continue
        if not reservation['plage'][0] <= n <= reservation['plage'][1]:
            raise RuntimeError('Lot hors réservation : ' + directory.name)
        count = 0
        for p in paths:
            raw = p.read_bytes()
            text = raw.decode('utf-8')
            doc = html.document_fromstring(text)
            m = mesure.mesurer(text)
            pa = '_Phase_A_' in p.name
            titles = doc.xpath('//h1' if pa else '//main/h2')
            title = titles[0].text_content().strip() if titles else p.stem
            # Détecte également les représentations moins usuelles, sans prétendre
            # en vérifier le contenu, la licence ou la qualité visuelle.
            visual = doc.xpath('//img | //svg | //canvas | //object | //embed | //iframe')
            css_images = len(re.findall(r'(?:background(?:-image)?|content)\s*:[^;}]*url\s*\(', text, re.I))
            count += bool(visual or css_images)
            rows.append(dict(lot=directory.name, fichier=str(p.relative_to(BASE)), titre=title,
                             sha256=hashlib.sha256(raw).hexdigest(), octets_html=len(raw),
                             x_octets=m.x[1], y_octets=m.y[1], xy_octets=sum((m.x[1], m.y[1])),
                             plafond_x_octets=100000 if pa else 9000,
                             taille_x_conforme=m.x[1] <= (100000 if pa else 9000),
                             bande_historique_80_150_ko=80000 <= len(raw) <= 150000,
                             images=len(doc.xpath('//img')), svg=len(doc.xpath('//svg')),
                             autres_supports=len(visual)-len(doc.xpath('//img | //svg')),
                             images_css=css_images,
                             controle_visuel_effectue=directory.name == 'LOT_018' and reviewed.get(p.name) == hashlib.sha256(raw).hexdigest(), validation_medicale_nouvelle=False))
        lots.append(dict(lot=directory.name, titre=catalogue[n]['ssp_profiles_2023_fr_en'].split(' | ')[0],
                         lecons=len(paths), lecons_avec_support=count,
                         rattrapage='à réaliser' if count == 0 else 'à contrôler'))
    return dict(date_utc=datetime.now(timezone.utc).isoformat(timespec='seconds'),
                commit_source=subprocess.check_output(['git','rev-parse','HEAD'], cwd=ROOT,text=True).strip(),
                branche=branch, reservation=reservation, unite='1 Ko = 1000 octets UTF-8',
                lots=lots, fichiers=rows,
                synthese=dict(lots=len(lots), lecons=len(rows), lecons_avec_support=sum(x['lecons_avec_support'] for x in lots),
                              tailles_x_conformes=sum(x['taille_x_conforme'] for x in rows),
                              dans_bande_historique=sum(x['bande_historique_80_150_ko'] for x in rows)))


def render(data):
    s = data['synthese']
    out = ['<!doctype html><html lang="fr"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">',
           '<title>Illustrations et tailles — état des lieux</title><style>body{font:17px/1.5 system-ui;max-width:1200px;margin:auto;padding:24px;color:#182332;background:#fafbfc}table{border-collapse:collapse;width:100%;font-size:14px}td,th{border:1px solid #bac4cc;padding:8px;text-align:left}th{background:#e5edf5}summary{cursor:pointer;padding:14px;background:#edf1f5}details{margin:16px 0}a{color:#155a9d}.bloc{border-left:5px solid #a74713;padding:12px;background:#fff0e4}.table{overflow:auto}</style>',
           '<h1>Rattrapage des illustrations — état des lieux</h1>',
           f'<p>Mesuré dans l’arbre de travail le {escape(data["date_utc"])} · commit de départ <code>{data["commit_source"]}</code>.</p>',
           f'<p><strong>{s["lots"]} lots, {s["lecons"]} leçons ; {s["lecons_avec_support"]} leçon avec support visuel détecté.</strong> Les 22 lots 018–039 sont complets en fichiers textuels ; LOT_040 contient Phase A et DX1. Cela ne constitue pas une validation médicale.</p>',
           '<p class="bloc">Rattrapage partiel : les scripts Codex sont créés. Trois leçons de LOT_018 contiennent une anatomie Commons annotée ou des schémas pédagogiques, examinés visuellement et testés dans Chromium. Aucun cliché pathologique ajouté ; aucun lot entièrement rattrapé. La rédaction de nouveaux diagnostics reste suspendue pendant le rattrapage.</p>',
           '<p>1 Ko = 1 000 octets. « Fiche » = texte x hors fenêtres ; « Fenêtres » = texte y des popovers et dépliants ; « Texte total » = x + y ; « HTML » = fichier complet, polices et balisage inclus. Mesures par le harnais taille_xy.py inchangé. Le plafond V8 est 9 Ko pour les DD, 100 Ko pour Phase A. La bande historique de 80–150 Ko du fichier HTML est indiquée séparément : elle ne remplace pas le plafond V8 du texte.</p>',
           f'<p>{s["tailles_x_conformes"]}/{s["lecons"]} fiches respectent le plafond x ; {s["dans_bande_historique"]}/{s["lecons"]} fichiers sont dans la bande historique. Les poids HTML ci-dessous incluent les illustrations. Leur exemption autorisée n’est pas soustraite aux poids bruts ; les fiches x restent mesurées par le harnais inchangé.</p>',
           '<p>L’absence de support rend le rattrapage nécessaire à l’échelle de chaque lot. La sélection et l’illustration des lésions clés restent à compléter : ce relevé ne prescrit pas une image dans chacune des leçons. Il ne renouvelle ni relecture linguistique, ni audit médical, ni contrôle AIPS.</p>',
           '<p><a href="illustrations_20261031/INVENTAIRE.json">Données exactes et empreintes SHA-256</a> · <a href="CONSIGNE_ILLUSTRATIONS.md">Consigne et critères de réception</a></p>']
    for lot in data['lots']:
        out.append(f'<details><summary>{escape(lot["lot"])} — {escape(lot["titre"])} · {lot["lecons"]} leçons · illustrations : {lot["rattrapage"]}</summary><div class="table"><table><thead><tr><th>Leçon</th><th>Fiche Ko</th><th>Fenêtres Ko</th><th>Texte total Ko</th><th>HTML Ko</th><th>Plafond x</th><th>Bande 80–150</th><th>Images / SVG</th></tr></thead><tbody>')
        for row in (r for r in data['fichiers'] if r['lot'] == lot['lot']):
            out.append(f'<tr><td><a href="{escape(row["fichier"])}">{escape(row["titre"])}</a></td>' + ''.join(f'<td>{row[k]/1000:.3f}</td>' for k in ['x_octets','y_octets','xy_octets','octets_html']) + f'<td>{"Respecté" if row["taille_x_conforme"] else "DÉPASSÉ"}</td><td>{"Respectée" if row["bande_historique_80_150_ko"] else "Hors bande"}</td><td>{row["images"]} / {row["svg"]}</td></tr>')
        out.append('</tbody></table></div></details>')
    return '\n'.join(out) + '\n</html>\n'


if __name__ == '__main__':
    data = collect()
    OUT.mkdir(exist_ok=True)
    (OUT / 'INVENTAIRE.json').write_text(json.dumps(data, ensure_ascii=False, indent=2)+'\n')
    (BASE / 'ETAT_ILLUSTRATIONS.html').write_text(render(data))
    print(json.dumps(data['synthese'], ensure_ascii=False))
