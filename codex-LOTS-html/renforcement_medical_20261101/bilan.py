"""Bilan de couverture, sans score médical ni clôture générale fictive."""
import json
from datetime import datetime,timezone
from html import escape as e
from pathlib import Path
from lxml import html
D=Path(__file__).resolve().parent
B=D.parent
r=json.loads((D/'CONTROLE.json').read_text())
rows=[]
for x in r['lecons']:
    p=B/x['fichier'];doc=html.fromstring(p.read_text())
    heads=doc.xpath('//main/h1|//main/h2') or doc.xpath('//title')
    title=heads[0].text_content() if heads else p.stem
    vals=[f'{x[k]/1000:.3f}'.replace('.',',') for k in ['octets_avant','octets_apres','texte_fiche_octets','texte_fenetres_octets']]
    rows.append('<tr><td><a href="'+e(x['fichier'])+'">'+e(p.parent.name+' — '+('Phase A' if '_Phase_A_' in p.name else p.stem.split('_V0_')[-1]))+'</a><br><small>'+e(title)+'</small></td>'+''.join('<td>'+v+'</td>' for v in vals)+'<td>14 / 14</td></tr>')
out='''<!doctype html><html lang="fr"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Renforcement médical — première tranche relue</title><style>body{margin:0;background:#eef4f6;color:#18313d;font:18px/1.6 system-ui}main{max-width:1150px;margin:auto;padding:24px}h1{line-height:1.2}h2{margin-top:0}section{background:white;border:1px solid #b7cbd1;border-radius:12px;padding:22px;margin:18px 0}a{color:#075a84}small{font-size:.85rem}table{border-collapse:collapse;min-width:820px;width:100%}td,th{text-align:left;vertical-align:top;padding:10px;border:1px solid #b7cbd1}.table{overflow:auto}.chiffres{display:flex;flex-wrap:wrap;gap:12px}.chiffres p{background:#e2f1ec;border-radius:10px;padding:10px 16px;margin:0}@media(max-width:600px){main{padding:12px}section{padding:16px}h1{font-size:1.8rem}}</style></head><body><main><h1>Renforcement médical et images réelles</h1><p>Première tranche du DATE · branche codex/lots.</p><div class="chiffres"><p><strong>6 leçons</strong> renforcées sur 244</p><p><strong>84 parties</strong> et 84 réponses relues</p><p><strong>2 images réelles</strong> acquises et annotées</p></div>
<section><h2>Ce qui a changé dans les cours</h2><ul>
<li><strong>Perte de vision :</strong> localisation, signes discriminants, limites des tests, urgences et interprétation des explorations ; précaution explicite contre l’échographie en cas de suspicion de globe ouvert.</li>
<li><strong>Troubles de réfraction :</strong> mécanismes optiques, limites du trou sténopéique, dioptries versus axe, développement visuel et risque rétinien distinct de la correction.</li>
<li><strong>Cataracte :</strong> retentissement fonctionnel, diagnostics associés, bilan préopératoire, biométrie, choix des implants et limites du résultat attendu.</li>
<li><strong>Microcéphalie et macrocéphalie :</strong> mesure, trajectoire, développement, urgences, choix des examens et interprétation contextualisée.</li>
<li><strong>Macrocéphalie familiale :</strong> conditions précises de rassurance et critères imposant de quitter cette hypothèse.</li>
<li><strong>Élargissement sous-arachnoïdien :</strong> mécanismes incertains, espaces liquidiens versus atrophie, limites des signes d’imagerie et évaluation d’une collection sous-durale associée.</li></ul>
<p>Les sous-titres, le <strong>gras</strong>, l’<em>italique</em> et les tableaux organisent le raisonnement. Le nombre de mots n’est pas un score de qualité médicale.</p></section>
<section><h2>Deux paires originales/annotées dans les fenêtres d’examens</h2>
<p><a href="LOT_018/LOT_018_Phase_A_V0.html">LOT_018 — Phase A</a> : partie 9, puis « membrane échogène intravitréenne ». Échographie du jeu de données officiel ERDES, CC BY 4.0. Panneau classé décollement rétinien par les auteurs. Résolution native 200 × 200 pixels ; aucune conclusion sur la macula ou la papille.</p>
<p><a href="LOT_029/LOT_029_Phase_A_V0.html">LOT_029 — Phase A</a> : partie 9, puis « repérage du matériel de dérivation ». Cliché du dépôt officiel CSF Shunt Valves Dataset, CC BY 4.0. <strong>Il montre du matériel chez un patient déjà équipé, pas une lésion cérébrale.</strong> Il ne prouve ni réglage, ni perméabilité, ni fonctionnement. Le cliché lésionnel de BESS/hydrocéphalie reste à acquérir.</p>
<p>Chaque fenêtre juxtapose l’original et la copie avec contours rouges pointillés, numéros, légendes, auteurs, licence et date d’accès. Les sources historiques et schémas existants ont été préservés.</p></section>
<section><h2>Tailles après enrichissement</h2><p>1 Ko = 1000 octets. Le texte de la fiche DD reste sous 9 Ko ; le texte de la Phase A reste sous 100 Ko. Les fenêtres illustrées ne sont pas plafonnées. Le poids HTML inclut images, polices et balisage.</p><div class="table"><table><thead><tr><th>Leçon</th><th>HTML avant, Ko</th><th>HTML après, Ko</th><th>Fiche, Ko</th><th>Fenêtres, Ko</th><th>Parties / questions</th></tr></thead><tbody>TABLE</tbody></table></div></section>
<section><h2>Relecture et vérifications</h2><p><strong>Six agents mobilisés :</strong> deux rédacteurs Astra, deux iconographes, un contrelecteur médical distinct et un contrôleur de présentation. Le coordinateur intègre les corrections et publie.</p>
<p>La contrelecture porte sur les 84 parties et 84 questions/réponses des six cours, avec examen des deux nouvelles illustrations. Une précaution importante sur le globe ouvert et une ambiguïté syntaxique ont été corrigées. Aucun score médical inventé. Cette relecture par IA ne constitue pas une validation clinique humaine ; les doses AIPS historiques n’ont pas fait l’objet d’un réaudit pharmaceutique exhaustif.</p>
<p>550 conditions statiques V8 réussies sur les 22 fichiers présents des deux lots. Les 238 autres leçons et les neuf fichiers du harnais restent intacts. Les tests navigateur portent sur les fenêtres et les réponses ; un défaut de contraste des anciens titres de figures en thème sombre a été corrigé. Les preuves de rendu sont conservées dans le dossier QA.</p>
<p><a href="renforcement_medical_20261101/contrelecture/VERSIONS_INTEGREES_RELUES.json">Versions médicales relues</a> · <a href="renforcement_medical_20261101/CONTROLE.json">Structure, conservation et tailles</a> · <a href="renforcement_medical_20261101/CRITERES_RELECTURE.json">Critères de fond</a></p></section>
<section><h2>Couverture et suite</h2><p><strong>6 leçons renforcées sur 244 : la refonte générale reste en cours.</strong> Les six leçons ne disposent pas toutes d’un cliché propre à leur diagnostic. Aucun LOT n’est déclaré entièrement refait. Prochaine tranche : DX3 du LOT_018 et DX3 du LOT_029, puis progression dans les deux périmètres existants.</p><p>Les exigences de profondeur, d’images réelles et de travail en équipe sont inscrites au contrat et au prompt pour les futurs cours. La réservation reste LOT_018–133. Aucun lot absent n’a été créé par cette campagne.</p><p><a href="BILAN_IMAGERIE_ECG.html">Inventaire général de l’imagerie et des ECG</a></p></section></main></body></html>'''
out=out.replace('DATE',datetime.now(timezone.utc).isoformat(timespec='seconds')).replace('TABLE',''.join(rows))
(B/'BILAN_RENFORCEMENT_MEDICAL.html').write_text(out)
print('Bilan créé : six leçons, deux images, limites explicites.')
