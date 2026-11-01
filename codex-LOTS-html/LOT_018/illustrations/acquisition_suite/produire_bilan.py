#!/usr/bin/env python3
"""Bilan mesuré des onze leçons ; ne modifie aucune leçon ni aucun contrôleur."""
import hashlib
import importlib.util
import json
import re
import subprocess
from datetime import datetime, timezone
from html import escape as e
from pathlib import Path

from lxml import html

D = Path(__file__).resolve().parent
B = D.parents[2]
R = B.parent


def produire():
    if not (B / '_cache/production.lock').exists():
        raise SystemExit('Verrou officiel requis')
    res = json.loads((R / 'IA_RESERVATIONS.json').read_text())['codex']
    branch = subprocess.check_output(['git', 'branch', '--show-current'], cwd=R, text=True).strip()
    assert branch == res['branche'] == 'codex/lots' and res['plage'][0] <= 18 <= res['plage'][1]
    spec = importlib.util.spec_from_file_location('taille_originale', R / 'harnais/taille_xy.py')
    taille = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(taille)
    candidats = []
    for parent in [D.parent / 'acquisition', D]:
        reg = json.loads((parent / 'CANDIDATS.json').read_text())
        candidats.extend(s for s in reg['candidats'] if s['decision'] in ('retenu_sous_reserve_visuelle', 'suspendu_provenance'))
    assert candidats and len(candidats) == len({s['id'] for s in candidats})
    retenus = [s for s in candidats if s['decision'] == 'retenu_sous_reserve_visuelle']
    suspendus = [s for s in candidats if s['decision'] == 'suspendu_provenance']
    assert not any((B / s['destination']).exists() for s in candidats)
    paths = sorted((B / 'LOT_018').glob('LOT_*_Phase_*.html'), key=lambda p: 0 if '_Phase_A_' in p.name else int(re.search(r'DX\.(\d+)', p.name)[1]))
    rows = []
    for p in paths:
        raw = p.read_bytes()
        doc = html.document_fromstring(raw.decode())
        pa = '_Phase_A_' in p.name
        ident = 'PhaseA' if pa else 'DX' + re.search(r'DX\.(\d+)', p.name)[1]
        titre = doc.xpath('//h1' if pa else '//main/h2')[0].text_content().strip()
        m = taille.mesurer(raw.decode())
        rows.append({'id': ident, 'titre': titre, 'fichier': str(p.relative_to(B)),
                     'sha256': hashlib.sha256(raw).hexdigest(), 'x': m.x[1], 'y': m.y[1],
                     'xy': m.x[1] + m.y[1], 'html': len(raw), 'plafond_x': 100000 if pa else 9000,
                     'conforme_x': m.x[1] <= (100000 if pa else 9000),
                     'supports': doc.xpath('//figure[@data-illustration]/@data-illustration'),
                     'candidats': [s['id'] for s in candidats if ident in s['cibles']]})
    data = {'mesure_le': datetime.now(timezone.utc).isoformat(timespec='seconds'),
            'commit_depart': subprocess.check_output(['git','rev-parse','HEAD'],cwd=R,text=True).strip(),
            'lecons': rows, 'candidats': candidats, 'cliches_integres': 0,
            'candidats_retenus': len(retenus), 'candidats_suspendus': len(suspendus),
            'supports_uniques': len({s for r in rows for s in r['supports']}),
            'validation_medicale_humaine': False, 'audit_independant': False}
    (D / 'BILAN_DONNEES.json').write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
    out = ['<!doctype html><html lang="fr"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">',
           '<title>LOT 018 — illustrations, sources et tailles</title><style>body{font:16px/1.55 system-ui,sans-serif;margin:0;background:#f4f6f8;color:#172f3b}main{max-width:1180px;margin:auto;padding:24px}h1{font-size:2rem;line-height:1.2}h2{margin-top:32px;font-size:1.35rem}a{color:#075e86}p{max-width:1000px}.etat{background:#fff0da;border-left:5px solid #a15d09;padding:14px}.chiffres{display:flex;flex-wrap:wrap;gap:12px}.chiffres p{flex:1;min-width:160px;padding:16px;margin:0;background:white;border:1px solid #c7d2db;border-radius:8px}.chiffres strong{display:block;font-size:1.8rem;color:#164e65}.table{overflow-x:auto;background:white}table{border-collapse:collapse;width:100%;min-width:1000px;font-size:14px}th,td{border:1px solid #c7d2db;padding:9px;text-align:left;vertical-align:top}th{background:#e2edf1}.nombre{white-space:nowrap;font-variant-numeric:tabular-nums}.ok{color:#17582d}details{background:white;border:1px solid #c7d2db;border-radius:8px;margin:12px 0;padding:12px}summary{cursor:pointer;font-weight:600}small{color:#3a5665}code{overflow-wrap:anywhere}li{margin:6px 0}footer{border-top:1px solid #c7d2db;margin-top:28px;padding-top:16px}@media(max-width:600px){main{padding:16px}h1{font-size:1.7rem}}</style></head><body><main>',
           '<h1>LOT 018 — illustrations, sources et tailles</h1>',
           '<p>Perte de vision aiguë ou progressive · état documentaire et mesures réelles des onze leçons.</p>',
           f'<p><small>Mesuré le {e(data["mesure_le"])} · branche codex/lots · départ {e(data["commit_depart"][:8])}.</small></p>',
           f'<p class="etat"><strong>Rattrapage incomplet.</strong> Les onze leçons ont des supports annotés. Parmi {len(candidats)} candidats documentés, {len(retenus)} restent retenus sous réserve visuelle et {len(suspendus)} est suspendu pour discordance de provenance. Aucun cliché pathologique n’est intégré. Le texte des articles Europe PMC est maintenant accessible ; leurs fichiers d’images sur le CDN NCBI et les originaux Wikimedia restent hors des domaines autorisés. Une notice lue ne remplace pas l’examen de l’image.</p>',
           f'<div class="chiffres"><p><strong>11 / 11</strong>leçons avec supports</p><p><strong>12</strong>composants déjà intégrés</p><p><strong data-compte="retenus">{len(retenus)}</strong>candidats retenus sous réserve visuelle</p><p><strong data-compte="suspendus">{len(suspendus)}</strong>candidat suspendu</p><p><strong>0</strong>cliché pathologique intégré</p></div>',
           '<h2>Tailles mesurées, leçon par leçon</h2>',
           '<p>1 Ko = 1 000 octets UTF-8. <strong>x</strong> mesure le texte de la fiche sans fenêtres ; <strong>y</strong>, le texte des fenêtres et dépliants. <strong>x + y</strong> inclut les deux. <strong>HTML</strong> est le poids réel du fichier, avec balisage, styles et images incorporées. La fiche reste limitée à 9 Ko pour un diagnostic, 100 Ko pour Phase A. Le texte des fenêtres illustrées et le poids HTML ne sont pas plafonnés par la dernière consigne de Vial.</p>',
           '<div class="table" tabindex="0" aria-label="Tailles des onze leçons, défilement horizontal possible"><table><thead><tr><th>Leçon</th><th>x · Ko</th><th>y · Ko</th><th>x + y · Ko</th><th>HTML · Ko</th><th>Plafond x</th><th>Supports présents</th><th>Clichés candidats</th></tr></thead><tbody>']
    for r in rows:
        cells = ''.join(f'<td class="nombre" data-mesure="{k}">{r[k]/1000:.3f}</td>' for k in ['x','y','xy','html'])
        links = '<br>'.join(f'<a href="#{e(i)}">{e(i)}' + (' (suspendu)' if any(s['id'] == i for s in suspendus) else '') + '</a>' for i in r['candidats']) or 'Aucun retenu ; schémas de focalisation présents.'
        out.append(f'<tr data-lecon="{r["id"]}"><td><a href="{e(r["fichier"])}">{e(r["titre"])}</a></td>{cells}<td class="ok">Conforme ({r["plafond_x"]/1000:g} Ko)</td><td>{len(r["supports"])}</td><td>{links}</td></tr>')
    out += ['</tbody></table></div>',
            '<p>« Conforme » concerne exclusivement le plafond x. Les supports existants sont une illustration anatomique normale de Commons et des schémas pédagogiques originaux ; ils ne constituent pas des clichés de lésions de patients. Les 21 vues uniques et leurs inspections antérieures sont documentées dans les preuves du lot.</p>',
            f'<h2>Les {len(candidats)} candidats documentés</h2><p>Les descriptions sont celles des notices. Tous restent non acquis, non inspectés et non intégrés. Le candidat suspendu est exclu de l’import automatique. Ouvrir une ligne pour voir les crédits, le contrôle de provenance et le piège de lecture prévu.</p>']
    for s in candidats:
        suspendu = s['decision'] == 'suspendu_provenance'
        statut = 'SUSPENDU — provenance discordante' if suspendu else 'Retenu sous réserve visuelle'
        provenance = s.get('controle_provenance', {})
        precision = ('<p class="etat"><strong>Import suspendu.</strong> ' + e(provenance['constat']) + ' ' + e(provenance['condition_reactivation']) + '</p>') if suspendu else ''
        if provenance:
            precision += f'<p><a href="{e(provenance["source_primaire"])}">Texte primaire consulté</a> · <a href="{e(provenance["preuve"])}">Copie XML datée</a> · accès le {e(provenance["date"])}.</p>'
        out.append(f'<details id="{e(s["id"])}" data-decision="{e(s["decision"])}"><summary>{e(s["titre"])} — {e(", ".join(s["cibles"]))} · {statut}</summary>{precision}<p><strong>{e(s["auteur"])}</strong> · licence annoncée : {e(s["licence"])} · notice consultée le {e(s["acces_le"])}.</p><p>{e(s["description_selon_notice"])}</p><p><strong>Point à contrôler avant annotation :</strong> {e(s["piege_a_expliquer"])}</p><p><a href="{e(s["source_url"])}">Notice source</a> · <a href="{e(s["revision_url"])}">Révision lue</a> · <a href="{e(s["licence_url"])}">Licence</a></p></details>')
    out += ['<h2>Ce qui est vérifié — et ce qui reste à faire</h2>',
            '<ul><li>Tailles recalculées avec le harnais commun inchangé ; onze fiches sous leur plafond.</li><li>Quinze notices examinées au total : neuf candidats retenus, un suspendu pour provenance discordante, trois écartés pour l’usage envisagé et deux en réserve. Un fichier nommé « normal » est écarté comme témoin sain car sa description mentionne un glaucome.</li><li>La lecture primaire de Hao et al. contredit le numéro de figure indiqué par Commons : la figure 1 est un organigramme, pas le fond d’œil annoncé. Aucun autre panneau n’est attribué par supposition.</li><li>Les légendes originales de Werner et al. et de Heiferman/Fawzi confirment le contexte documentaire des deux autres figures PLoS ; leurs pixels restent à inspecter. L’angiographie de l’exemple d’occlusion montre un masquage, qui ne suffit pas à conclure à une non-perfusion. La figure de DMLA documente une conversion vers l’exsudation ; ne pas confondre les stades.</li><li>Les contours, les lésions réellement visibles et la lisibilité restent à vérifier sur les originaux et les rendus.</li><li>Aucune nouvelle dose, aucun audit indépendant et aucune validation médicale humaine. Les résultats V8 et linguistiques antérieurs restent datés ; leur succès ou échec n’est pas renouvelé par ce bilan.</li></ul>',
            '<p>Suite : autorisation réseau effective pour les originaux, acquisition, inspection, annotation, contrôle du rendu, puis intégration dans les fenêtres. Aucun nouveau diagnostic avant la fin du rattrapage demandé.</p>',
            '<footer><a href="LOT_018/illustrations/acquisition_suite/BILAN_DONNEES.json">Mesures et empreintes exactes</a> · <a href="LOT_018/illustrations/acquisition/CANDIDATS.json">Première sélection</a> · <a href="LOT_018/illustrations/acquisition_suite/CANDIDATS.json">Complément</a> · <a href="ETAT_ILLUSTRATIONS.html">Inventaire des 244 leçons</a><p>Contenu établi à partir des sources citées ; non validé cliniquement par un médecin.</p></footer></main></body></html>']
    assert len(rows) == 11 and all(r['conforme_x'] for r in rows)
    assert data['supports_uniques'] == 12
    (B / 'BILAN_CLICHES_LOT_018.html').write_text('\n'.join(out)+'\n')
    print(json.dumps({'lecons':len(rows),'plafonds_x_conformes':11,'candidats':len(candidats),'retenus':len(retenus),'suspendus':len(suspendus),'cliches_integres':0}))


if __name__ == '__main__':
    produire()
