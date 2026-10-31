#!/usr/bin/env python3
"""Rend l'inventaire JSON en HTML autonome filtrable, imprimable et CSV téléchargeable.
Usage : python3 -B codex-LOTS-html/outils/rendre_etat_des_lieux.py
Le rapport n'est pas une leçon V8 et n'entre pas dans le décompte des leçons.
"""
import csv
import html
import io
import json
from pathlib import Path

BASE = Path(__file__).resolve().parents[1]
D = json.loads((BASE / 'etat_lieux_20261031/mesures.json').read_text())
F, LOTS, B = D['fichiers'], D['lots'], D['bilan']
# La synthèse éditoriale ci-dessous décrit ce checkpoint précis. Empêcher sa
# réutilisation silencieuse avec d'autres chiffres lors d'une reprise future.
assert (B['fichiers'], B['lots_complets'], B['bande_v0_ok'], B['v8_positifs'], B['citations_aips']) == (170, 15, 55, 4249, 660), 'Checkpoint différent : actualiser la synthèse éditoriale avant publication.'


def e(value):
    return html.escape(str(value), quote=True)


def ko(value):
    return f'{value / 1000:.3f}'.replace('.', ',')


def badge(ok, yes='Oui', no='Non'):
    return f'<span class="badge {"ok" if ok else "warn"}">{yes if ok else no}</span>'


def link(path, label):
    return f'<a href="{e(path)}">{e(label)}</a>'


def issues(items):
    if not items:
        return '<p>Aucun signal de cette catégorie.</p>'
    return '<ul>' + ''.join('<li><strong>' + e(x['code']) + '</strong> — ' + e(x['message']) +
                            ''.join('<blockquote>' + e(s) + '</blockquote>' for s in x.get('exemples', [])) + '</li>' for x in items) + '</ul>'


lotrows = []
for lot in LOTS:
    rows = [f for f in F if f['lot'] == lot['lot']]
    lotrows.append(f'''<tr><th scope="row"><a href="#{lot['lot']}">{lot['lot']}</a><small>{e(lot['code'])} · {e(lot['titre'])}</small></th>
<td>{lot['html_presents']}/11<br>{badge(lot['complet_11_html'], 'Complet en production', 'Partiel')}</td>
<td>{ko(lot['x_octets'])}</td><td>{ko(lot['y_octets'])}</td><td>{ko(lot['x_octets']+lot['y_octets'])}</td><td>{ko(lot['octets_html'])}</td>
<td>{sum(f['taille_v8_ok'] for f in rows)}/{len(rows)}</td><td>{lot['bande_v0_ok']}/{len(rows)}</td>
<td>{sum(f['v8_positifs'] for f in rows)}/{sum(f['v8_nombre'] for f in rows)}</td>
<td>{link(lot['preuve_historique'], 'Relectures et corrections')}<br>{link(lot['preuve_v8'], 'Contrôle frais')}</td></tr>''')

sections = []
for lot in LOTS:
    rows_html = []
    for f in (f for f in F if f['lot'] == lot['lot']):
        flags = ' '.join(k for k, condition in [('sous80', f['octets_html'] < 80000), ('taillev8', not f['taille_v8_ok']),
                                               ('echecv8', bool(f['v8_echecs'])), ('langue', bool(f['langue_critiques'] or f['langue_avertissements']))] if condition)
        failtext = '<p>Aucun échec statique V8.</p>' if not f['v8_echecs'] else '<ul>' + ''.join('<li>' + e(x['controle']) + ' : ' + e(json.dumps(x['detail'], ensure_ascii=False)) + '</li>' for x in f['v8_echecs']) + '</ul>'
        reviewtext = ''.join('<p><time>' + e(p['horodatage']) + '</time> — ' + e(p['raison']) + '</p>' for p in f['passes_relecture']) or '<p>Pas de passe individuelle retrouvée.</p>'
        detail = f'''<details><summary>Mesures et preuves de cette leçon</summary>
<p><strong>Fichier :</strong> {e(f['chemin'])}<br><strong>SHA-256 :</strong> <code>{f['sha256']}</code><br>
Empreinte et poids identiques au manifeste : {"oui" if f['empreinte_manifeste_ok'] and f['octets_manifeste_ok'] else "non"}.</p>
<p>x = {f['x_octets']} octets ; y = {f['y_octets']} octets ; x + y = {f['xy_octets']} octets ; HTML = {f['octets_html']} octets.
{f['fenetres']} fenêtres et {f['depliants']} dépliants. Marge sous le plafond de texte V8 : {ko(f['plafond_x_octets']-f['x_octets'])} Ko.</p>
<p><strong>Écart à la bande historique :</strong> {('manque ' + ko(80000-f['octets_html']) + ' Ko au plancher de 80 Ko') if f['octets_html'] < 80000 else ('au-dessus du plafond' if f['octets_html'] > 150000 else 'dans la bande de 80–150 Ko')}. Aucun remplissage n'a été ajouté.</p>
<h4>Contrôle V8</h4>{failtext}<p>{link(lot['preuve_v8'], 'Les 25 contrôles détaillés')}</p>
<h4>Langue — résultat brut du contrôleur historique</h4><p>Ces nombres comptent des catégories de signaux ; les occurrences sont indiquées ci-dessous.</p>
{issues(f['langue_critiques'])}{issues(f['langue_avertissements'])}<p>{link(f['preuve_langue'], 'Rapport linguistique complet, avec détails')}</p>
<h4>Relecture antérieure consignée</h4>{reviewtext}
<p>{link(lot['preuve_historique'], 'Documents de validation, corrections et journal du lot')}.
Cette trace atteste une passe déclarée ; elle ne prouve pas à elle seule l'exactitude exhaustive du fond.</p>
<p><strong>AIPS :</strong> {f['citations_aips']} paragraphes de citation détectés. {'Tous retrouvés dans les originaux archivés après normalisation des espaces.' if f['citations_aips'] else 'Aucune citation détectée : ce zéro ne prouve pas qu’aucune citation ni aucun traitement ne soit nécessaire.'}
Les indications, omissions, adaptations et doses hors citation ne sont pas certifiées par ce comptage.</p>
<p><strong>Verdict global du prompt :</strong> non démontré intégralement. Taille V8 vérifiée ; contrôles statiques détaillés ci-dessus ; langue avec réserves ; relecture médicale interne tracée, aucun audit indépendant ni validation clinique.</p></details>'''
        rows_html.append(f'''<tr class="lesson" data-flags="{flags}" data-search="{e(f['lot']+' '+f['lecon']+' '+f['titre'])}">
<th scope="row">{link(f['chemin'], f['lecon']+' — '+f['titre'])}{detail}</th>
<td class="num">{ko(f['x_octets'])}</td><td class="num">{ko(f['y_octets'])}</td><td class="num">{ko(f['xy_octets'])}</td><td class="num"><strong>{ko(f['octets_html'])}</strong></td>
<td>{badge(f['taille_v8_ok'])}<small>{ko(f['plafond_x_octets'])} Ko max.<br>{f['x_octets']/f['plafond_x_octets']*100:.1f} % utilisé</small></td>
<td>{badge(f['bande_v0_ok'])}<small>{'Sous 80 Ko' if f['octets_html'] < 80000 else ('Au-dessus de 150 Ko' if f['octets_html'] > 150000 else '80–150 Ko')}</small></td>
<td>{badge(not f['v8_echecs'], str(f['v8_positifs'])+'/'+str(f['v8_nombre']), str(f['v8_positifs'])+'/'+str(f['v8_nombre']))}<small>{f['parties']} parties<br>{f['questions']} questions</small></td>
<td><span class="badge warn">Réserves</span><small>{len(f['langue_critiques'])} C · {len(f['langue_avertissements'])} A<br>Non certifiée</small></td>
<td>Interne tracée<small>AIPS : {f['citations_aips']} citation(s) retrouvée(s)<br>Indépendant : non<br>Clinique : non</small></td></tr>''')
    sections.append(f'''<section class="lot-section" id="{lot['lot']}" data-lot="{lot['lot']}"><h3>{lot['lot']} <span>{e(lot['code'])} · {e(lot['titre'])}</span></h3>
<p>{lot['html_presents']}/11 leçons présentes. {'Lot complet en production ; conformité globale non certifiée.' if lot['complet_11_html'] else 'Lot incomplet : Phase A et DX.1–4 présents ; DX.5–10 absents. Reprise prévue à Blépharite.'}
<a href="#{'synthese'}">Retour à la synthèse</a></p>
<div class="table-wrap"><table class="lessons"><caption>Tailles en Ko — {lot['lot']}. C = catégorie critique, A = catégorie d’avertissement du contrôleur historique.</caption>
<thead><tr><th>Leçon et preuves</th><th>Sans fenêtres<br>x</th><th>Fenêtres seules<br>y</th><th>Avec fenêtres<br>x + y</th><th>Fichier HTML<br>réel</th><th>Taille V8<br>vérifiée ?</th><th>Bande initiale<br>80–150 Ko ?</th><th>Statique V8<br>et structure</th><th>Langue</th><th>Fond médical</th></tr></thead>
<tbody>{''.join(rows_html)}</tbody></table></div></section>''')

warningrows = ''.join(f'<tr><td>{e(code)}</td><td>{count}</td></tr>' for code, count in B['codes_langue_avertissements'].items())
source_links = ''.join('<li>' + link('../'+s['chemin'], s['chemin']) + '<br><code>' + s['sha256'] + '</code></li>' for s in D['sources_normatives'])
csv_text = (BASE / 'etat_lieux_20261031/mesures.csv').read_text()
options = ''.join(f'<option value="{x["lot"]}">{x["lot"]} — {e(x["titre"])}</option>' for x in LOTS)
result = f'''<!doctype html>
<html lang="fr"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Vial · État des lieux des leçons — 31 octobre 2026</title>
<style>
:root{{--ink:#172d3c;--muted:#4c6373;--paper:#f2f6f8;--line:#cbd9e1;--green:#07634f;--amber:#774600;--blue:#164f84}}
*{{box-sizing:border-box}}body{{margin:0;background:var(--paper);color:var(--ink);font:16px/1.55 system-ui,sans-serif}}header{{background:#142e40;color:white;padding:40px max(24px,calc((100vw - 1480px)/2))}}header p{{max-width:980px;color:#e0eaf0}}h1{{font-size:clamp(28px,4vw,46px);line-height:1.15;margin:12px 0 20px;letter-spacing:-.025em}}h2{{font-size:26px;margin-top:38px}}h3{{font-size:22px}}h3 span{{font-size:17px;font-weight:500}}h4{{margin-bottom:6px}}main{{max-width:1530px;margin:auto;padding:24px}}a{{color:var(--blue);text-underline-offset:3px}}header a{{color:#c3e6ff}}.eyebrow{{letter-spacing:.13em;text-transform:uppercase;font-size:13px;font-weight:700}}.meta{{font-size:14px}}.cards{{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:14px}}.card{{padding:20px;border:1px solid var(--line);border-radius:12px;background:white}}.card strong{{display:block;font-size:32px;line-height:1.1}}.card span{{display:block;margin-top:10px;color:var(--muted)}}.notice{{border-left:5px solid #b77811;background:#fff6e6;padding:16px 20px;margin:22px 0}}.note{{border-left:5px solid #347fab;background:#e8f3fa;padding:16px 20px;margin:20px 0}}.grid{{display:grid;grid-template-columns:1fr 1fr;gap:24px}}.panel{{background:white;border:1px solid var(--line);border-radius:12px;padding:20px}}.panel h3{{margin-top:0}}table{{border-collapse:collapse;width:100%;background:white;font-size:14px}}caption{{text-align:left;padding:12px 0;color:var(--muted)}}td,th{{padding:12px;border-bottom:1px solid var(--line);vertical-align:top;text-align:left}}thead th{{background:#e5edf2;color:#203c4f;font-size:13px}}tbody tr:hover{{background:#f7fbfe}}th[scope=row]{{font-weight:600}}small{{display:block;font-size:12px;font-weight:400;color:var(--muted);margin-top:6px;line-height:1.5}}.num{{text-align:right;font-variant-numeric:tabular-nums;white-space:nowrap}}.table-wrap{{overflow-x:auto;border:1px solid var(--line);border-radius:10px}}.lessons{{min-width:1350px}}.lessons th[scope=row]{{width:340px;min-width:310px}}.badge{{display:inline-block;border-radius:5px;padding:3px 7px;font-size:12px;font-weight:700;white-space:nowrap}}.ok{{background:#dff4eb;color:var(--green)}}.warn{{background:#fff0d4;color:var(--amber)}}details{{font-weight:400;font-size:13px;margin-top:12px}}summary{{cursor:pointer;color:var(--blue);font-weight:600}}details[open]{{background:#eef4f8;padding:12px;border-radius:7px}}code{{font-size:11px;overflow-wrap:anywhere}}blockquote{{margin:8px 0;padding-left:10px;border-left:2px solid #adbfc9;font-size:12px}}.lot-section{{margin-top:38px;scroll-margin-top:16px}}.filters{{display:flex;gap:14px;flex-wrap:wrap;background:#e2ecf2;padding:16px;border-radius:10px}}label{{font-size:13px;font-weight:700;display:block}}input,select,button,.button{{font:inherit;border-radius:6px;border:1px solid #9ab0bf;padding:9px 12px;background:white;color:var(--ink)}}input{{min-width:260px}}button,.button{{cursor:pointer}}.actions{{display:flex;gap:12px;flex-wrap:wrap;margin:14px 0}}.button{{display:inline-block;text-decoration:none;font-size:14px}}[hidden]{{display:none!important}}.foot{{border-top:1px solid var(--line);margin-top:40px;padding:20px 0;color:var(--muted)}}.tight li{{margin-bottom:8px}}.rule-table th{{min-width:160px}}
@media(max-width:800px){{.cards,.grid{{grid-template-columns:1fr 1fr}}main{{padding:16px}}.grid{{grid-template-columns:1fr}}header{{padding:28px 18px}}}}
@media print{{body{{background:white;font-size:10pt}}header{{background:white;color:black;padding:0}}header p{{color:black}}main{{max-width:none;padding:0}}.filters,.actions{{display:none}}.table-wrap{{overflow:visible;border:0}}.lessons{{min-width:0;font-size:7pt}}.lessons th[scope=row]{{min-width:0;width:24%}}th,td{{padding:4px}}.lot-section{{break-before:page}}.cards strong{{font-size:22px}}.badge{{font-size:8px;white-space:normal}}small{{font-size:7pt}}summary{{display:none}}@page{{size:A3 landscape;margin:12mm}}}}
</style></head><body>
<header><div class="eyebrow">Vial · Chantier LOTS · codex/lots</div><h1>Le poids des leçons.<br>Les contrôles. Leurs limites.</h1>
<p>État des lieux mesuré sur les fichiers présents : <strong>15 lots complets en production, 1 lot partiel, 170 leçons</strong>.
La taille V8 est respectée partout. La conformité intégrale au prompt, notamment linguistique et médicale, n'est pas démontrée.</p>
<p class="meta">Mesure : {e(D['date_utc'])} · Commit source : <code>{D['commit_source']}</code><br>
Périmètre : codex-LOTS-html/LOT_018 à LOT_033. Les autres producteurs sont exclus. Rapport prioritaire ; rédaction des monographies suspendue pendant sa création.</p></header>
<main>
<section aria-label="Chiffres clés" class="cards"><div class="card"><strong>170 leçons</strong><span>165 dans les 15 lots complets + 5 du LOT_033</span></div>
<div class="card"><strong>170 / 170</strong><span>Respectent le plafond de texte V8</span></div>
<div class="card"><strong>115 sous 80 Ko</strong><span>55 dans l'ancienne bande ; aucun au-dessus de 150 Ko</span></div>
<div class="card"><strong>4 249 / 4 250</strong><span>Contrôles statiques V8 positifs ; un contrôle échoue sur les 6 liens futurs du LOT_033</span></div></section>
<div class="notice"><strong>Réponse directe :</strong> les fichiers HTML pèsent de <strong>{ko(min(f['octets_html'] for f in F))} à {ko(max(f['octets_html'] for f in F))} Ko</strong>.
Le maximum historique de 150 Ko est respecté pour chacun. Le minimum historique de 80 Ko ne l'est pas pour 115 leçons. Le plafond actuel porte sur le texte principal, et il est respecté pour les 170 leçons.
Une petite taille ne prouve ni omission ni exhaustivité : le fond doit être évalué sur les notions réellement couvertes.</div>
<h2>Ce que signifient « sans fenêtres » et « avec fenêtres »</h2>
<div class="grid"><div class="panel"><h3>Texte, en Ko UTF-8</h3><p><strong>x — Sans fenêtres :</strong> texte principal mesuré par le harnais officiel, hors popovers et dépliants. Il inclut les titres, liens et sources qui sont hors fenêtres.</p>
<p><strong>y — Fenêtres seules :</strong> texte de tous les popovers, sous-fenêtres et dépliants ; les imbrications ne sont comptées qu'une fois.</p>
<p><strong>x + y — Avec fenêtres :</strong> total de ces textes. Le style, les scripts, l'en-tête HTML et le badge de taille sont exclus selon le contrôleur officiel.</p></div>
<div class="panel"><h3>Poids réel du fichier HTML</h3><p>Nombre exact d'octets du fichier sur disque, incluant texte, balises, styles et polices embarquées.
<strong>Ouvrir une fenêtre ne change pas ce poids</strong> : son contenu est déjà dans le fichier.</p><p>1 Ko = 1 000 octets. Les trois décimales conservent la précision à l'octet ; aucun jeton ni Kio n'est utilisé. La colonne x n'est pas le poids d'un second fichier HTML amputé de ses fenêtres.</p>
<p>Les 170 empreintes et poids correspondent aux manifestes déjà déposés. Aucune leçon n'a été modifiée pour ce rapport. Le présent HTML de synthèse n'est pas une leçon et n'entre pas dans ces 170 mesures.</p></div></div>
<h2>Comparaison explicite avec les instructions</h2>
<div class="table-wrap"><table class="rule-table"><thead><tr><th>Instruction</th><th>Règle</th><th>Constat et verdict</th></tr></thead><tbody>
<tr><th scope="row">V8 applicable au chantier</th><td>Phase A : x ≤ 100 Ko.<br>Chaque diagnostic : x ≤ 9 Ko.<br>y sans plafond ; pas de plafond du fichier HTML dans cette règle.</td><td><strong>170/170 conformes pour la taille.</strong> Diagnostics : x de 3,363 à 5,613 Ko. Phase A : x de 5,173 à 13,119 Ko.</td></tr>
<tr><th scope="row">Bande initiale V0 et §1 du prompt V2</th><td>80 000 à 150 000 octets par fichier, bornes incluses ; cible de premier jet 110–125 Ko dans V2.</td><td><strong>55/170 dans la bande.</strong> 115 sous le plancher ; 0 au-dessus du plafond. La cible de premier jet n'est pas un contrôle du fichier final.</td></tr>
<tr><th scope="row">14 parties et 14 questions</th><td>Chaque leçon présente doit contenir les 14 parties ordonnées et 14 questions.</td><td><strong>170/170 réussissent les contrôles structurels</strong> : 2 380 parties et 2 380 questions. Le comptage ne valide pas leur qualité pédagogique.</td></tr>
<tr><th scope="row">Après rédaction : relecture et corrections</th><td>Relecture interne autorisée en session unique, traces par fichier, corrections et contrôle transversal.</td><td><strong>170/170 passes internes retrouvées</strong>, documents de corrections par lot, 16 traces transversales ; celle du LOT_033 porte sur les cinq leçons présentes. Ces traces ne remplacent pas un nouvel audit intégral du contenu.</td></tr>
<tr><th scope="row">Conformité linguistique</th><td>Langue correcte et règles de forme V8 ; contrôle après rédaction.</td><td><strong>Vérification automatique exécutée sur 170/170 ; verdict brut historique : 0/170 conformes.</strong> Incompatibilités de règles et avertissements explicités ci-dessous. Conformité linguistique intégrale non certifiée.</td></tr>
<tr><th scope="row">Fond médical et AIPS</th><td>Sources réellement lues, décisions cohérentes, doses exactes et adaptations pertinentes.</td><td><strong>Relectures internes documentées ; 660/660 citations détectées retrouvées dans les notices archivées.</strong> Exhaustivité, actualité de chaque recommandation, adéquation clinique et exactitude de tout texte hors citation non démontrées par ce contrôle.</td></tr>
<tr><th scope="row">Audit indépendant et scores demandés initialement</th><td>Auditeur distinct et objectifs chiffrés dans les instructions initiales ; poursuite seul autorisée ensuite par Vial.</td><td><strong>Non réalisés ; aucun score attribué.</strong> L'autorisation de continuer seul ne constitue pas une preuve d'audit indépendant ni de validation clinique.</td></tr>
<tr><th scope="row">Rendu navigateur et mobile</th><td>Affichage, ouvertures et fermeture des fenêtres à vérifier réellement.</td><td><strong>Non vérifiés au navigateur.</strong> Le graphe de liens et les attributs de fenêtres ont été contrôlés statiquement.</td></tr>
</tbody></table></div>
<p class="note">Le <a href="etat_lieux_20261031/MESSAGE_DEMARRAGE_CODEX.md">message de démarrage joint</a> demande explicitement la norme V8 et la priorité du prompt Codex. Le §12 de <a href="../PROMPT_PRODUCTION_V2.md">PROMPT_PRODUCTION_V2.md</a>, décision du 30.10.2026, dit : « Le texte des fenêtres (y) n'a pas de plafond » et « c'est le texte qui compte ».
Le même dépôt conserve la bande 80–150 Ko dans <a href="../PROMPT_Casern/PROMPT_ULTIME_PRODUCTION_LOTS_V0.md">le prompt V0 (§14)</a> et une mention résiduelle 150–200 Ko (§17), alors que le §14 abolit cet ancien critère.
Le présent rapport applique V8 pour la taille courante et conserve séparément le verdict de la bande V0. Il ne transforme pas cette coexistence en conformité à toutes les versions du prompt.</p>
<h2>Langue et médecine : ce qui est établi</h2>
<div class="grid"><div class="panel"><h3>Contrôleur linguistique historique</h3><p>Réexécuté, sans correction automatique. Ses catégories critiques sont : <strong>title : 170 fichiers</strong>, <strong>h3_14 : 154 diagnostics</strong>, <strong>bande : 115 fichiers</strong>.</p>
<p>V8 demande les abréviations avec <code>abbr title</code> et des parties en <code>h2</code>, alors que cet outil interdit tout <code>title</code> et exige des <code>h3</code>. Les vérifications V8 correspondantes passent. La différence de taille est chiffrée, sans effacer le résultat brut.</p>
<table><caption>Avertissements : nombre de fichiers concernés, catégories non exclusives</caption><thead><tr><th>Signal</th><th>Fichiers</th></tr></thead><tbody>{warningrows}</tbody></table>
<p>Ces signaux ne sont pas un décompte de fautes avérées. Exemples vérifiés : les espaces avant ponctuation signalés dans dix fichiers sont dans des citations AIPS ; l'alerte de chaîne de points-virgules du LOT_021 DX.7 porte aussi sur une citation. Certaines répétitions concernent un déclencheur et son titre de fenêtre. <strong>Les autres alertes ne sont pas déclarées résolues globalement.</strong></p></div>
<div class="panel"><h3>Relecture médicale interne</h3><p>Les journaux mentionnent une relecture pour chaque leçon ; les validations et corrections existantes sont conservées dans les preuves du rapport. Les 660 paragraphes AIPS ont été comparés aux notices originales archivées, avec normalisation des espaces uniquement.</p>
<p><strong>Ce rapport ne constitue pas une nouvelle relecture médicale des 170 leçons.</strong> Une citation exacte peut être inadaptée à une indication ou insuffisante pour couvrir toutes les situations. Un fichier sans citation n'est pas automatiquement exempt de cette exigence.</p>
<p>La conformité linguistique complète, l'exhaustivité médicale, l'absence d'erreurs graves, l'actualité des recommandations et la qualité clinique restent à établir par une évaluation de fond. Aucun médecin ni auditeur indépendant n'est présenté comme ayant validé ces fichiers ; aucune note de qualité n'est inventée.</p>
<p><strong>Conséquence pour la suite :</strong> conserver les alertes avec leur contexte, vérifier les besoins de contenu des 115 fichiers sous l'ancien plancher, et corriger les défauts effectivement constatés. Ajouter des octets sans information utile ne démontrerait aucune conformité de fond.</p></div></div>
<section id="synthese"><h2>État des lots</h2><p>« Complet en production » signifie onze leçons présentes et clôture documentée ; cela ne signifie pas « validé cliniquement ». Le LOT_018 est inclus dans l'inventaire sans être recommencé. LOT_034 à LOT_133 : aucun HTML produit dans ce dossier. Il reste 101 lots à achever dans la plage 18–133, dont le LOT_033 partiel.</p>
<div class="table-wrap"><table><caption>Sommes des poids par lot, en Ko ; les plafonds s'appliquent à chaque leçon et non à ces sommes.</caption><thead><tr><th>Lot et sujet</th><th>Production</th><th>Σ x</th><th>Σ y</th><th>Σ (x + y)</th><th>Σ HTML</th><th>Taille V8</th><th>Bande V0</th><th>Contrôles V8</th><th>Preuves</th></tr></thead><tbody>{''.join(lotrows)}</tbody></table></div></section>
<h2>Chaque leçon, mesurée séparément</h2><p>Ouvrir « Mesures et preuves » pour les octets exacts, empreintes, messages linguistiques, relecture consignée et verdicts détaillés. Les deux colonnes de taille évaluent deux règles différentes ; aucun « oui » de taille ne vaut validation générale du prompt.</p>
<div class="filters"><label>Rechercher<input type="search" id="search" placeholder="Diagnostic, numéro de lot…"></label>
<label>Lot<select id="lot"><option value="">Tous les lots</option>{options}</select></label>
<label>Afficher<select id="filter"><option value="">Toutes les leçons</option><option value="sous80">Sous l'ancien minimum de 80 Ko</option><option value="taillev8">Taille V8 non conforme</option><option value="echecv8">Au moins un échec statique V8</option><option value="langue">Signaux du contrôleur de langue</option></select></label>
<button type="button" id="reset">Réinitialiser</button></div><p id="count" role="status" aria-live="polite">170 / 170 leçons affichées.</p>
<div class="actions"><button type="button" id="csv">Télécharger toutes les mesures CSV</button><button type="button" id="print">Imprimer la sélection</button>{link('etat_lieux_20261031/mesures.json','Données JSON et empreintes')}</div>
<noscript><p>Toutes les leçons et leurs preuves restent lisibles sans JavaScript ; seuls les filtres et le téléchargement intégré nécessitent son activation. <a href="etat_lieux_20261031/mesures.csv">CSV local</a>.</p></noscript>
{''.join(sections)}
<h2>Traçabilité et reproduction</h2><p>Mesures prises sur le commit source indiqué en tête, avec empreinte individuelle de chaque HTML. Les pages de cours et preuves liées sont accessibles dans le dépôt ; l'état des lieux et ses détails restent lisibles dans ce fichier HTML autonome.</p>
<p>Exécuter depuis la racine du dépôt : <code>python3 -B codex-LOTS-html/outils/etat_des_lieux.py</code>, puis <code>python3 -B codex-LOTS-html/outils/rendre_etat_des_lieux.py</code>. Ces scripts écrivent uniquement le rapport et ses preuves dans codex-LOTS-html/. Ils ne réécrivent ni les leçons ni les outils communs. Une nouvelle exécution remplace cet état daté ; conserver le commit pour l'historique.</p>
<details><summary>Sources normatives et empreintes des contrôleurs utilisés</summary><ul class="tight">{source_links}</ul></details>
<footer class="foot">Rapport de contrôle établi seul, sans sous-agents. Aucun changement de modèle revendiqué. Aucun audit indépendant, score ou test navigateur simulé.
La veille locale contrôle le contrat chaque minute tant que l'environnement existe ; elle ne produit aucune leçon. Reprise de rédaction conservée : LOT_033, DX.5 Blépharite.</footer>
</main>
<script type="application/json" id="csv-data">{json.dumps(csv_text, ensure_ascii=False).replace('<', chr(92)+'u003c')}</script>
<script>
const search = document.getElementById('search'), lot = document.getElementById('lot'), filter = document.getElementById('filter');
const norm = s => s.normalize('NFD').replace(/[\u0300-\u036f]/g,'').toLowerCase();
function update() {{
  const query = norm(search.value.trim()); let count = 0;
  document.querySelectorAll('.lot-section').forEach(section => {{
    let shown = 0;
    section.querySelectorAll('.lesson').forEach(row => {{
      const match = (!lot.value || section.dataset.lot === lot.value) && (!query || norm(row.dataset.search).includes(query)) && (!filter.value || row.dataset.flags.split(' ').includes(filter.value));
      row.hidden = !match; if (match) {{ shown++; count++; }}
    }}); section.hidden = shown === 0;
  }});
  document.getElementById('count').textContent = count + ' / 170 leçons affichées.';
}}
[search,lot,filter].forEach(x => x.addEventListener('input', update));
document.getElementById('reset').addEventListener('click', () => {{ search.value=''; lot.value=''; filter.value=''; update(); }});
document.getElementById('print').addEventListener('click', () => window.print());
document.getElementById('csv').addEventListener('click', () => {{
  const blob = new Blob(['\ufeff', JSON.parse(document.getElementById('csv-data').textContent)], {{type:'text/csv;charset=utf-8'}});
  const url = URL.createObjectURL(blob), a = document.createElement('a'); a.href=url; a.download='vial-mesures-20261031.csv'; a.click(); setTimeout(() => URL.revokeObjectURL(url),1000);
}});
</script></body></html>'''
(BASE / 'ETAT_DES_LIEUX.html').write_text(result, encoding='utf-8')
print('ETAT_DES_LIEUX.html :', len(result.encode('utf-8')), 'octets ;', len(F), 'leçons')
