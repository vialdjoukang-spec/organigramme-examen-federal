#!/usr/bin/env python3
"""Assemble les textes relus du seul LOT_226 en HTML autonomes."""
from pathlib import Path
import html, json, re, textwrap

ROOT=Path(__file__).resolve().parent
SOURCE_PATH=ROOT/'evidence/registre_sources.json'
SOURCES=json.loads(SOURCE_PATH.read_text())['sources']
CSS='''
:root{color-scheme:light;--ink:#122d3b;--blue:#145d86;--green:#176642;--line:#c6dce6}
*{box-sizing:border-box}html{scroll-behavior:smooth}body{margin:0;background:#edf6fb;color:var(--ink);font-family:Tahoma,Arial,sans-serif;line-height:1.65}
main{width:min(1080px,100%);margin:auto;padding:24px 18px 60px;background:#fff;min-height:100vh}
h1,h2,h3,h4{line-height:1.3;overflow-wrap:anywhere}h2{color:#145d86;border-bottom:3px solid #2980b9;padding-bottom:16px}h3{font-size:1.12rem;margin:28px 0 10px}h4{font-size:1rem}
a{color:#075b86;overflow-wrap:anywhere}p{margin:9px 0}summary{cursor:pointer;color:#155c40;line-height:1.5}summary:focus-visible,a:focus-visible{outline:3px solid #195fb0;outline-offset:4px}
details{margin:12px 0;border:1px solid var(--line);border-radius:8px;padding:12px 14px;background:#f5fbff}details[open]>summary{margin-bottom:10px}details.mono{background:white;border:2px solid #bad6e3;padding:16px}details.mono>summary{font-size:1.2rem;color:#13496c}
details.fenetre{border-left:4px solid #3285ad;background:#eef8fd}details.cas{border-left:4px solid #278459;background:#eef9f2}
.lead{font-size:1.02rem}.badge{display:inline-block;font-size:.78rem;padding:3px 8px;margin:6px 0;background:#e4f5eb;color:#145b3c;border-radius:5px}.caution{padding:12px;border-left:4px solid #a14b1e;background:#fff4ed}.scope{padding:12px;background:#ecf8f1;border-left:4px solid #267653}
.table-scroll{overflow-x:auto;max-width:100%;margin:14px 0}table{width:100%;border-collapse:collapse;font-size:.93rem}th,td{border:1px solid #bfd5df;text-align:left;vertical-align:top;padding:10px;min-width:145px}th{background:#daedf7}tr:nth-child(even){background:#f7fbfd}
nav{padding:12px;background:#eaf6fb;border-radius:8px}nav a{display:inline-block;margin:3px 10px 3px 0}.refs{font-size:.86rem;color:#31545c}.equation{padding:12px;border:1px solid #6e9cbb;background:white;overflow-wrap:anywhere}.sources li{margin:12px 0;overflow-wrap:anywhere}footer{font-size:.9rem;border-top:2px solid #bfd9e6;margin-top:30px;padding-top:16px}
@media(max-width:500px){main{padding:16px 10px 40px}details.mono{padding:10px}details{padding:10px}h2{font-size:1.32rem}th,td{padding:8px;min-width:135px}body{font-size:15px}}
@media print{body{background:#fff}main{width:100%;padding:0}details{break-inside:avoid}nav{display:none}}
'''

def p(s):return '<p>'+s+'</p>\n'
def refs(*ids):return '<p class="refs">'+ ' · '.join(f'<a href="#source-{i}">[{i}]</a>' for i in ids)+'</p>\n'
def table(headers,rows):
 return '<div class="table-scroll" style="overflow-x:auto;">\n<table>\n<thead><tr>'+''.join('<th scope="col">'+h+'</th>' for h in headers)+'</tr></thead>\n<tbody>\n'+''.join('<tr>'+''.join('<td>'+c+'</td>' for c in row)+'</tr>\n' for row in rows)+'</tbody>\n</table>\n</div>\n'
def window(title,body,kind='fenetre'):
 return f'<details class="{kind}">\n<summary>{title}</summary>\n{body}</details>\n'
def source_section():
 return '<section id="sources"><h3><strong>Les sources ont été ouvertes le 25 octobre 2026.</strong></h3>\n<ol class="sources">'+''.join(f'<li id="source-{s["id"]}">[{s["id"]}] {html.escape(s["title"])}. {html.escape(s["org"])} ; {html.escape(s["year"])}. <a href="{html.escape(s["url"],quote=True)}">Le document source est consultable ici.</a> La consultation date du 25 octobre 2026.'+(' '+html.escape(s['status']) if s.get('status') else '')+'</li>\n' for s in SOURCES)+'</ol></section>\n'
def page(name,title,body,ending):
 text='<!DOCTYPE html>\n<html lang="fr">\n<head>\n<meta charset="UTF-8">\n<meta name="viewport" content="width=device-width,initial-scale=1">\n<title>LOT_226 · O7.4 · '+html.escape(title)+'</title>\n<style>\n'+CSS+'</style>\n</head>\n<body><main id="haut">\n<h2>LOT_226 · SSP O7.4<br>Aspects environnementaux et psychosociaux des maladies chroniques</h2>\n'+p(title)+body+source_section()+'<footer>Contenu produit par IA à partir des sources citées ; non validé cliniquement par un médecin.</footer>\n</main></body>\n</html>\n<!-- FIN_FICHIER '+ending+' -->\n'
 # Les retours sont placés entre éléments, sans tronquer une phrase ni ajouter du remplissage.
 text=re.sub(r'>(?=<)', '>\n',text)
 text='\n'.join('\n'.join(textwrap.wrap(line,width=1400,break_long_words=False,break_on_hyphens=False,replace_whitespace=False)) if len(line)>2800 else line for line in text.splitlines())+'\n'
 (ROOT/name).write_text(text,encoding='utf-8')
 return len(text.encode('utf-8'))

POINTS=[
 'Définition et sémantique','Épidémiologie suisse et limites des données','Cadre légal et mécanismes de vulnérabilité','Démarche situationnelle et diagnostics discriminants','Anamnèse ciblée et drapeaux rouges','Examen ciblé, du normal au pathologique','Approche syndromique et unités sémiologiques','Diagnostic situationnel et critères de décision','Explorations et outils : référence, première intention, alternatives et seconde intention','Arbre décisionnel','Prise en charge : buts, moyens, surveillance et pronostic','Prévention primaire, secondaire et tertiaire','Points clés','Pièges et questions de l’examen fédéral'
]
def mono(title,sections,ident,academic=False):
 out=f'<details open class="mono'+(' plan-academique' if academic else '')+f'" id="{ident}">\n<summary>{title}</summary>\n'
 for i,(lead,extra) in enumerate(sections,1):out+=f'<section id="{ident}-p{i}">\n<h3><strong>{i}. {POINTS[i-1]}</strong></h3>\n<div class="lead">{p(lead)}</div>\n'+extra+'</section>\n'
 return out+'</details>\n'

DX=[
 ('Dépression ou anxiété comorbide','Le retrait, la perte d’intérêt ou la détresse font rechercher une souffrance psychique, une cause somatique et un danger immédiat.','L’entretien clinique évalue humeur, fonctionnement et suicidalité.','Une boucle entre symptômes, réduction des activités et maladie somatique peut maintenir la souffrance.','Le médecin sécurise la situation, puis organise une prise en charge intégrée.','S21'),
 ('Précarité et renoncement aux soins','Le patient renonce à une prestation qu’il juge nécessaire parce qu’il ne peut pas l’assumer financièrement.','Le bilan social vérifie couverture, factures, participation et accès réel aux soins.','Le coût et les démarches retardent les soins ; la maladie peut à son tour réduire les ressources.','Le médecin traite l’urgence puis construit une solution financière avec le service social.','S04'),
 ('Littératie limitée ou barrière linguistique','Le patient ne peut pas reformuler une consigne importante ou la consultation n’a pas de langue commune fiable.','Une reformulation demandée sans jugement et un interprète professionnel éclaircissent la situation.','La complexité de l’information et des parcours dépasse les ressources disponibles.','Le médecin adapte le message, vérifie sa compréhension et précise le financement de l’interprétariat.','S05'),
 ('Épuisement du proche aidant','L’aidant n’arrive plus à assurer les tâches essentielles ou dit qu’il ne pourra pas continuer.','L’outil OFSP décrit tâches, fréquence, charge et besoin de décharge.','La charge nocturne, l’absence de relais et les besoins du malade peuvent dépasser les ressources de l’aidant.','Le médecin assure un relais concret et évalue séparément la sécurité du patient et de son proche.','S09'),
 ('Travail, incapacité et réadaptation','Les exigences du poste ne correspondent plus aux capacités fonctionnelles du patient.','La description du travail est confrontée aux limitations médicales et aux possibilités d’adaptation.','L’atteinte fonctionnelle réduit la participation ; un arrêt prolongé peut aussi fragiliser la structure quotidienne.','Le médecin décrit les capacités résiduelles et coordonne une réadaptation sans promettre une rente.','S19'),
 ('Solitude et isolement social','Le patient souffre de relations qu’il perçoit comme insuffisantes ou ne dispose d’aucun relais disponible.','L’entretien distingue sentiment de solitude, réseau réel et aide mobilisable.','L’insuffisance relationnelle perçue peut accroître la détresse et compliquer le recours aux soins.','Le médecin recherche la préférence du patient et construit un lien accessible, choisi et vérifiable.','S10'),
 ('Chaleur et décompensation d’une maladie chronique','Une période chaude s’accompagne d’un malaise, d’une confusion ou d’une aggravation de la maladie.','L’évaluation clinique recherche la gravité et le contexte thermique sans attendre un seuil isolé.','La sudation et la vasodilatation peuvent entraîner pertes hydriques, déséquilibre électrolytique et surcharge cardiovasculaire.','Le médecin rafraîchit, évalue l’urgence et individualise hydratation et médicaments.','S11'),
 ('Pollution de l’air extérieur','Les symptômes respiratoires ou cardiovasculaires s’aggravent dans un contexte d’exposition aux polluants.','L’examen clinique évalue la décompensation ; les données d’air décrivent l’exposition sans prouver la causalité individuelle.','Les polluants atteignent les voies respiratoires et peuvent accroître la charge d’une maladie déjà présente.','Le médecin traite la maladie aiguë et réduit l’exposition sans attribuer toute dyspnée à la pollution.','S13'),
 ('Environnement intérieur : radon, fumée et humidité','Les symptômes varient avec le bâtiment, une fumée est présente ou une mesure de radon dépasse la référence applicable.','Le bilan médical et l’enquête sur le logement orientent des mesures ciblées, réalisées par des professionnels compétents.','Les expositions diffèrent : une fumée ou une humidité peut irriter ; le radon expose au risque pulmonaire à long terme.','Le médecin traite les symptômes, documente les circonstances et organise la correction du bâtiment.','S16'),
 ('Adolescent malade chronique et transition','Le jeune risque une rupture de suivi ou les adultes ne lui permettent pas encore de participer à ses soins.','Un entretien adapté et une transmission entre équipes évaluent l’autonomie, les besoins et le discernement.','Le changement de service, la maladie et les attentes de l’entourage peuvent désorganiser le parcours.','Le médecin prépare un relais nominatif, garantit une parole propre au jeune et associe les proches avec son accord.','S18')
]

def dx_table():
 return table(['Le scénario est identifié.','Le signe d’alerte guide l’entretien.','L’outil éclaire la décision.','Le mécanisme relie les difficultés.','La première conduite est engagée.'],[[f'DX.{i} — {x[0]}<br><span class="badge">Le rang {i} est pédagogique ; la fréquence suisse de ce scénario n’est pas quantifiée.</span>',*x[1:5]] for i,x in enumerate(DX,1)])

if __name__=='__main__':
 from contenu_a import sections_a, annexes_a
 body=p('Le plan académique transpose les quatorze points à une situation de départ, ou Situation as Starting Point (SSP), transversale : une situation psychosociale ne constitue pas à elle seule une maladie. Les dix DX désignent ici dix scénarios gradués. Les vignettes sont fictives et servent à appliquer les sources ; elles ne constituent pas des recommandations supplémentaires.')
 body+=window('Le lecteur peut développer les sigles et les unités avant de poursuivre.',p('Health Literacy Survey 2019–2021 (HLS19–21) désigne l’enquête sur les compétences en santé. Statistics on Income and Living Conditions (SILC) désigne l’enquête sur les revenus et les conditions de vie. Le Centre national pour les services climatiques (NCCS) réunit les services climatiques suisses.')+p('L’ordonnance sur la protection de l’air est abrégée OPair. L’assurance-invalidité est abrégée AI. Le becquerel par mètre cube (Bq/m³) exprime une concentration d’activité radioactive ; le microgramme par mètre cube (µg/m³) exprime une concentration massique. Ces unités ne sont pas interchangeables.')+p('La plate-forme suisse d’information sur les médicaments (AIPS) donne accès aux informations professionnelles. Une dose ne sera considérée comme vérifiée que si la fiche pertinente a effectivement été lue. Les acronymes qui apparaissent dans les titres officiels des sources restent attribués à leurs organismes.')+refs('S05','S04','S12','S14','S23','S29'))
 body+='<div class="scope">'+p('Le lecteur doit pouvoir repérer un danger, préciser l’obstacle modifiable, respecter l’autonomie et organiser un suivi réalisable. Le cours distingue les données populationnelles, le droit suisse et les propositions pédagogiques appliquées à un cas.')+'</div>\n'
 body+='<nav aria-label="Navigation du fichier">'+''.join(f'<a href="#ssp-p{i}">Point {i}</a>' for i in range(1,15))+'<a href="#dx-liste">Scénarios</a><a href="#sources">Sources</a></nav>\n'
 body+=mono('Appel A · Le SSP O7.4 est étudié en quatorze points transposés.',sections_a(),'ssp',True)
 body+='<section id="dx-liste"><h3><strong>Le Bloc 2 fixe les dix scénarios de l’Appel B.</strong></h3>'+p('L’ordre ci-dessous conserve l’attribution du lot et sert la progression pédagogique. Les sources consultées ne permettent pas de comparer leurs fréquences parmi les malades chroniques en Suisse ; aucun classement statistique n’est donc prétendu. Les urgences du scénario 7, les dangers psychiques du scénario 1 et la mise en danger dans le scénario 4 passent toujours avant cet ordre de lecture.')+dx_table()+'</section>\n'+annexes_a()
 print('Appel A, octets:',page('LOT_226_Appel_A_V8_Plan_et_Liste.html','Appel A · Le cadre, l’évaluation et les dix scénarios sont établis.',body,'LOT_226_A'))
