from pathlib import Path
import json,re
B=Path(__file__).parent
p=json.loads((B/'paquet.json').read_text());source=(B.parent/'preparation_uro/eau_iu.txt').read_text().splitlines();print('\n'.join(source[:7]));p['passages'].append(dict(id='p-eau-version2026',source='EAU — Urological Infections, lien officiel vers l’édition 2026',url='https://uroweb.org/guidelines/urological-infections/chapter/the-guideline',date='2026-11-10',texte='\n'.join(source[:7])));(B/'paquet.json').write_text(json.dumps(p,ensure_ascii=False,indent=2)+'\n')
changes={
'L’European Association of Urology définit en 2026':['L’European Association of Urology définit en 2026 l’infection urinaire systémique par des manifestations générales infectieuses, avec ou sans symptômes urinaires locaux','Elle y inclut donc la pyélonéphrite, tandis que la cystite sans manifestations systémiques reste localisée'],
'La sémiologie du Collège national':['Le Collège national des enseignants de médecine interne décrit un patient allongé sur le dos sur un plan dur','Ses cuisses sont fléchies et écartées, tandis que l’examinateur se place face à lui'],
'Le pli cutané est moins fiable':['Le pli cutané est moins fiable chez l’enfant ou la personne obèse ; il peut aussi être accentué chez une personne âgée ou dénutrie','La perte d’élasticité cutanée explique cette dernière limite, donc son interprétation dépend du terrain'],
'Dans une présentation initiale typique simple':['Dans une présentation initiale typique simple, le référentiel AFU ne recommande pas de NFS, CRP ou créatinine systématiques','Cette restriction ne concerne donc pas le bilan de la forme grave décrit plus haut'],
'Le scanner recherche notamment une hypodensité':['Le scanner recherche notamment une hypodensité triangulaire à base externe au temps sécrétoire, qui oriente vers une néphrite selon l’AFU','Il peut aussi montrer un abcès intraparenchymateux ou une infection dans le fascia périrénal, ce qui révèle alors une complication locale'],
'La directive SSI concerne la femme adulte':['La directive SSI concerne la femme adulte non enceinte sans complication, donc sa population est précisément délimitée','Son choix oral pour la patiente stable ne suffit pas à décider chez tous les patients présentant une infection systémique'],
'Pour les infections urinaires systémiques, la recommandation forte':['Dans les infections urinaires systémiques, la recommandation forte EAU 2026 permet la ciprofloxacine empirique sous plusieurs conditions cumulées','La résistance locale est inférieure à 10 % et le patient présente une contre-indication aux céphalosporines de troisième génération ou aux aminoglycosides','Une hypersensibilité aux bêta-lactamines figure également parmi ces conditions, donc le choix ne dépend pas du seul taux de résistance'],
'L’EAU déconseille la ciprofloxacine et les autres':['L’EAU déconseille la ciprofloxacine et les autres fluoroquinolones empiriques chez les patients provenant d’un service urologique','Elle les déconseille aussi après une fluoroquinolone durant les six derniers mois ; l’anamnèse modifie donc le choix initial'],
'Chez le patient critique, qui se détériore':['Chez le patient critique, qui se détériore ou dont les voies urinaires sont obstruées, l’EAU préconise une couverture antimicrobienne large','Cette couverture tient notamment compte des entérobactéries productrices de BLSE et de Pseudomonas aeruginosa, donc la seule ligne ambulatoire ne répond pas à cette situation'],
'La prescription hospitalière est choisie':['La prescription hospitalière est choisie à partir de la gravité, des résistances locales et des cultures antérieures, puis son spectre est réduit selon l’antibiogramme','Le drainage d’un obstacle infecté reste donc une mesure urgente associée au traitement antimicrobien'],
'Chez l’homme présentant une douleur pelvienne':['Chez l’homme présentant une douleur pelvienne ou périnéale, un toucher rectal est nécessaire selon l’EAU pour rechercher une prostate sensible ou augmentée de volume','Le geste répond donc à une hypothèse de localisation prostatique']}
for f in (B/'fragments').glob('p*.html'):
 s=f.read_text()
 def sub(m):
  text,refs=m.group(1),m.group(2)
  for start,rows in changes.items():
   if text.startswith(start):
    if start in ['L’European Association of Urology définit en 2026','Pour les infections urinaires systémiques, la recommandation forte']:refs+='<sup class="r"><a href="#sb-p-eau-version2026">p-eau-version2026</a></sup>'
    return ''.join('<div class="p">'+r+refs+'.</div>\n' for r in rows)
  return m.group(0)
 s=re.sub(r'<div class="p">([^<]+)((?:<sup class="r">.*?</sup>)+)\.</div>',sub,s);f.write_text(s)
