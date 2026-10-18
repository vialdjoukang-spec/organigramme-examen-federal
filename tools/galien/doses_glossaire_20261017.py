import json,hashlib,pathlib
p=pathlib.Path('data/ck/src.json');src=json.loads(p.read_text()); src=[x for x in src if x['id']!='R-ESMO-GEP-2012']; urls={s['url']:s['id'] for s in src}
def source(i,title,url,org='Larousse',year=2026):
 if url in urls:return urls[url]
 src.append(dict(id=i,titre=title,url=url,org=org,pays='FR',type='glossaire',annee=year,note='Définition uniquement ; passage relu le 17.10.2026 UTC.'));urls[url]=i;return i
r=source('R-LAR-RAYNAUD','Maladie de Raynaud','https://www.larousse.fr/encyclopedie/medical/maladie_de_Raynaud/15754')
b=source('R-LAR-BUERGER','Maladie de Léo Buerger','https://www.larousse.fr/encyclopedie/medical/maladie_de_L%C3%A9o_Buerger/14170')
g=source('R-LAR-GI','Adjectif relatif à l’estomac et à l’intestin','https://www.larousse.fr/dictionnaires/francais/gastro-intestinal/36236')
v=source('R-VIDAL-DFG-2022','Estimation de la filtration rénale','https://www.vidal.fr/actualites/29875-estimation-du-debit-de-filtration-glomerulaire-les-marqueurs-endogenes.html','Vidal',2022)
e=source('R-EMA-SOMAKIT-2016','Somakit TOC — évaluation publique : sites des tumeurs digestives','https://www.ema.europa.eu/en/documents/assessment-report/somakit-toc-epar-public-assessment-report_en.pdf','European Medicines Agency',2016)
a=source('R-AMELI-IMP-2026','Symptômes de l’incontinence urinaire','https://www.ameli.fr/assure/sante/themes/incontinence-urinaire/symptomes-diagnostic','Assurance maladie')
rows=json.load(open('data/ck/doses_ch.json'))
def row_source(rid):
 row=next((x for x in rows if x['id']==rid),None)
 return urls.get(row['url_texte']) if row else None
entries=[
 ('maladie-raynaud','Maladie de Raynaud',[], 'Le froid ou une émotion contracte les petits vaisseaux des doigts, qui deviennent pâles et douloureux.',r,'Définition ; symptômes'),
 ('maladie-buerger','Maladie de Buerger',['maladie de Léo Buerger','thromboangéite oblitérante','thromboangéite'], 'Les artères des membres s’enflamment et se bouchent progressivement.',b,'Définition et obstruction artérielle'),

 ('gastro-intestinal','Gastro-intestinal', ['gastro-intestinale','gastro-intestinaux'], 'Cet adjectif décrit ce qui concerne l’estomac et l’intestin.',g,'Définition'),
 ('gastro-entero-pancreatique','Gastro-entéro-pancréatique',['gastro-entéro-pancréatiques'], 'Cet adjectif concerne l’estomac, l’intestin et le pancréas.',e,'Définition initiale des sites anatomiques'),
 ('egfr','eGFR',['DFG estimé'], 'Ce nombre est une estimation du volume de plasma filtré par les reins par unité de temps.',v,'Résumé et définition'),
 ('imperiosite','Impériosité',['impériosité urinaire'], 'Le besoin d’uriner apparaît soudainement et devient difficile à différer.',a,'Les fuites précédées d’un besoin pressant'),
 ('gastro-resistant','Gastro-résistant',['gastro-résistante','gastro-résistants'], 'L’enrobage permet au médicament de traverser l’estomac avant de libérer son principe actif dans l’intestin.',row_source('aspirine-po-adulte-infarctus'),'Posologie, mode d’administration'),
 ('kleihauer-betke','Test de Kleihauer-Betke',['test de Kleihauer-'], 'Cet examen mesure les globules rouges du fœtus présents dans le sang maternel.',row_source('immunoglobuline-anti-d'),'Posologie, hémorragie fœto-maternelle'),
 ('lap','LAP',[], 'Cette abréviation désigne la leucémie aiguë promyélocytaire.',row_source('tretinoine-po-lap'),'Indications'),
]
for entry in src:
 if entry['id']=='R-EMA-SOMAKIT-2016':entry['pays']='NL'
p.write_text(json.dumps(src,ensure_ascii=False,indent=1)+'\n')
p=pathlib.Path('data/ck/glo.json');glo=json.loads(p.read_text()); glo=[x for x in glo if x['id'] not in ['thromboangeite','gastro-entero-pancreatique','maladie-buerger','egfr']]; ids={x['id'] for x in glo};pending=[]
for i,label,alias,definition,sid,loc in entries:
 if i in ids:continue
 # Les termes absents de la branche ne sont pas introduits gratuitement.
 if i in ['lap','kleihauer-betke'] and not sid:continue
 e=dict(id=i,type='abreviation' if i in ['lap','egfr'] else 'terme',label=label,alias=alias,**{'def':definition},src=[dict(id=sid,loc=loc,lu_le='2026-10-17')] if sid else [],statut='sourcé' if sid else 'À vérifier',valide_par_vial=False)
 glo.append(e)
 if not sid:pending.append(i)
p.write_text(json.dumps(glo,ensure_ascii=False,indent=1)+'\n')
p=pathlib.Path('qa/termes_exclus.txt');t=p.read_text()
for term in ['AUTOGEL','CEFEPIM','HM','LEMAN','MACURE','VEOZA']:
 if not any(x.split('\t')[0]==term for x in t.splitlines()):t+=term+'\tÉlément du nom commercial suisse, pas un terme de sémiologie ; dose liée à la DCI dans doses_ch.\n'
for term,reason in [('UTC','Fuseau de datation des sources, pas un terme médical.'),('PICO','Repère méthodologique de la recommandation citée, pas un terme clinique.'),('encephalitis','Mot anglais du titre bibliographique ; le terme français encéphalite est couvert séparément.')]:
 if not any(x.split('\t')[0]==term for x in t.splitlines()):t+=term+'\t'+reason+'\n'
p.write_text(t)
p=pathlib.Path('qa/domaines.yml');t=p.read_text().replace('europe: [','europe: [ema.europa.eu, larousse.fr, vidal.fr, ameli.fr, ');p.write_text(t)
if pending:
 p=pathlib.Path('journal/asclepios.md');p.write_text(p.read_text()+'\n### Relecture doses · termes à sourcer (17.10.2026 UTC)\nDéfinitions provisoires signalées « À vérifier », sans validation Vial : '+', '.join(pending)+'. Chercher une référence de terminologie CH/UE avant de les déclarer sourcées.\n')
print('Glossaire ciblé : définitions sourcées, sans exclusion de terme clinique.')
