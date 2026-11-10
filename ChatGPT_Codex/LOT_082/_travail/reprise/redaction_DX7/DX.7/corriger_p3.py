from pathlib import Path
import json, re, hashlib, difflib
B=Path(__file__).resolve().parent
P=B/'paquet.json'
pack=json.loads(P.read_text())
old={n:(B/'fragments'/f'p{n:02d}.html').read_text() for n in [6,9,11,12]}
assert hashlib.sha256((B/'LOT_082_Phase_B_V0_DX.7.html').read_bytes()).hexdigest()=='daf93434391d774a41da65ef18f113f076759dd12e2d82a51891c4b25db05025'
rawtable=json.loads((B/'cache/CORRECTION_SOSORT_TABLE10.json').read_text())['results'][0]
table=rawtable['full_content']
pan=json.loads((B/'cache/CORRECTION_TECHNIQUE_EXTRACT.json').read_text())['results'][0]
rawpan=pan['full_content']
newpass=[]
def passage(id,texte,raw,source,url,**meta):
    assert texte in raw, id
    x={'id':id,'source':source,'url':url,'date':'2026-11-10','texte':texte,'lecture':'Passage exact et contigu effectivement lu dans le cache primaire ; aucune fusion.',**meta}
    newpass.append(x)
    return id
for n in [9,10,15]:
    line=next(x for x in table.splitlines() if x.startswith('|'+str(n)+'\\. '))
    text=line.split('|')[1].split('. ',1)[1].strip()
    passage(f'dx7-corr-sosort-r{n}',text,table,'SOSORT — Recommendation on bracing, tableau10 des recommandations2016 publiées2018',rawtable['url'],annee_edition=2018,cache='cache/CORRECTION_SOSORT_TABLE10.json')
start=rawpan.index('3\\. It is recommended that the measurement')
end=rawpan.index('5\\. In the case',start)
passage('dx7-corr-pan-mesure',rawpan[start:end].strip(),rawpan,'Czaprowski et al. — recommandations du Comité de réhabilitation de l’Académie polonaise des sciences, édition2021',pan['url'],annee_edition=2021,date_publication_web=pan.get('publish_date'),cache='cache/CORRECTION_TECHNIQUE_EXTRACT.json')
caption='Fig. 2A-B. Measurement of the trunk rotation angle: A) front view, B) example of the measurement result – 5 degrees right side asymmetry of the back.'
passage('dx7-corr-pan-figure',caption,rawpan,'Czaprowski et al. — figure2, page imprimée100',pan['url'],annee_edition=2021,cache='cache/CORRECTION_TECHNIQUE_EXTRACT.json',verification_visuelle={'fichier':'cache/CZAPROWSKI2021_page100.png','pdf_sha256':hashlib.sha256((B/'cache/CZAPROWSKI2021.pdf').read_bytes()).hexdigest(),'observation':'Figure2A/B effectivement inspectée : appareil tenu transversalement sur le dos penché, échancrure médiane centrée sur la ligne rachidienne ; la légende anglaise est citée exactement, cette observation est distincte du texte cité.'})
for x in newpass:assert not any(p['id']==x['id']for p in pack['passages'])
pack['passages'].extend(newpass)
def c(id):return f'<sup class="r"><a href="#sb-{id}">{id}</a></sup>'
def p(s):return '<div class="p">'+s+'</div>\n'
edits=[]
def replace(n,before,after,label):
    f=B/'fragments'/f'p{n:02d}.html';s=f.read_text();assert s.count(before)==1,(n,label,s.count(before));f.write_text(s.replace(before,after));edits.append({'id':label,'point':n,'avant':before,'apres':after})
# C01 : compléter la fenêtre technique, sans remanier le reste de l’examen.
before='<div id="dx7-p6-scoliometre" popover class="fenetre"><h5>Une mesure de surface ne remplace pas la référence radiographique</h5>'
after=before+p('Pendant la flexion antérieure, le clinicien pose le scoliomètre transversalement sur le dos et centre son échancrure sur la ligne rachidienne ; la figure de technique montre cette installation'+c('dx7-corr-pan-figure')+'.')
after+=p('Il règle la flexion pour rendre le segment examiné parallèle au sol ; il parcourt les niveaux rachidiens et retient les maxima thoracique proximal, thoracique principal et thoracolombaire ou lombaire'+c('dx7-corr-pan-mesure')+'.')
after+=p('SOSORT rapporte, pour un ATR de 5°, une sensibilité d’environ 100% et une spécificité d’environ 47%'+c('sia82-sos18-scoliometre')+'. À 7°, la sensibilité descend à 83% tandis que la spécificité atteint 86%'+c('sia82-sos18-scoliometre')+'.')
after+=p('Ces performances proviennent des travaux repris par SOSORT ; le seuil inférieur privilégie la sensibilité, tandis que le seuil supérieur privilégie la spécificité'+c('sia82-sos18-scoliometre')+'. Le résultat reste un angle de tronc ; il ne devient donc pas un Cobb radiographique'+c('prep-dx1-scoliometre')+c('pa17-sosort-cobb')+'.')
replace(6,before,after,'DX7-C01-scoliometre')
# C02 : mesure et erreur de Cobb au point9.
before='<h4><em>9.a La radiographie constitue la référence diagnostique</em></h4>\n'
after=before+p('Sur le cliché global debout, le clinicien repère les vertèbres limites dont les plateaux sont les plus inclinés ; il prolonge ces plateaux pour tracer l’angle de Cobb'+c('p82-scoliose-radio')+'. La mesure quantifie ainsi la courbure, tandis que le profil analyse sa composante sagittale'+c('p82-scoliose-radio')+'.')
after+=p('SOSORT indique que l’erreur de mesure manuelle de Cobb la plus souvent citée est de 5°'+c('sia82-sos18-mesure-erreur')+'. Dès lors, une petite différence entre deux mesures ne prouve pas, à elle seule, une progression certaine'+c('sia82-sos18-mesure-erreur')+'.')
replace(9,before,after,'DX7-C02-Cobb')
# C03 : vraie recommandation prescriptive ; ne pas transformer une dose étudiée en règle.
before='<div id="dx7-p11-corset" popover class="fenetre"><h5>L\'orthèse est un moyen de contrôle de progression</h5>'
after=before+p('Pour débuter le traitement, SOSORT recommande un port à plein temps ou au moins 18 heures par jour ; une exception doit être justifiée par un clinicien spécialisé dans le traitement conservateur des déformations rachidiennes'+c('dx7-corr-sosort-r9')+'.')
after+=p('Le prescripteur adapte les heures quotidiennes à la sévérité, à l’âge, au stade, au but et aux résultats du traitement, ainsi qu’à l’adhésion réalisable'+c('dx7-corr-sosort-r10')+'. Ainsi, le régime choisi possède un nombre d’heures explicite et une justification clinique'+c('dx7-corr-sosort-r9')+c('dx7-corr-sosort-r10')+'.')
after+=p('Le contrôle compare ensuite l’utilisation effective à cette prescription ; SOSORT recommande de vérifier régulièrement l’adhésion au moyen de dispositifs de monitorage'+c('dx7-corr-sosort-r15')+'. Les régimes rapportés dans les études de dose-réponse restent des données d’étude ; ils ne remplacent donc pas la prescription individualisée'+c('eu-sosort-2018-108')+c('eu-sosort-2018-109')+c('dx7-corr-sosort-r10')+'.')
replace(11,before,after,'DX7-C03-prescription-corset')
# C04 : déplacer le dépistage sous le bon niveau et expliciter le périmètre de preuve.
before='<h4><em>12.a La prévention primaire ne se confond pas avec une explication posturale</em></h4>\n'
after='<h4><em>12.a La prévention primaire causale reste une limite des recommandations citées</em></h4>\n'
after+=p('L’étiopathogénie de la scoliose idiopathique demeure non élucidée ; les recommandations citées ne fournissent donc pas de prévention primaire causale démontrée'+c('prep-dx1-etiopathogenie')+c('eu-sosort-2018-205')+'. Le dépistage recherche une maladie déjà présente et relève ici de la prévention secondaire'+c('eu-sosort-2018-205')+'.')
after+='<h4><em>12.b La prévention secondaire vise détection et progression</em></h4>\n'
replace(12,before,after,'DX7-C04-prevention')
f=B/'fragments/p12.html';s=f.read_text();marker='<h4><em>12.b La prévention secondaire vise détection et progression</em></h4>\n';assert s.count(marker)==2;first=s.index(marker);second=s.index(marker,first+len(marker));f.write_text(s[:second]+s[second+len(marker):])
# Répercuter les seules citations effectivement employées dans les contrats de points.
for n in [6,9,11,12]:pack['points'][str(n)]=sorted(set(re.findall(r'href="#sb-([^"]+)"',(B/'fragments'/f'p{n:02d}.html').read_text())))
P.write_text(json.dumps(pack,ensure_ascii=False,indent=2)+'\n')
contract=json.loads((B/'contrat.json').read_text())
for n in [6,9,11,12]:
    if 'sources' in contract['points'][str(n)]:contract['points'][str(n)]['sources']=pack['points'][str(n)]
(B/'contrat.json').write_text(json.dumps(contract,ensure_ascii=False,indent=2)+'\n')
(B/'CORRECTIONS_P3.json').write_text(json.dumps({'audit':'audits/DX7_P3_PREMIER.audit.json','SHA_avant':'daf93434391d774a41da65ef18f113f076759dd12e2d82a51891c4b25db05025','statut':'Corrections d’auteur ; aucune autoévaluation P3','remplacements':edits,'nouveaux_passages':[x['id']for x in newpass]},ensure_ascii=False,indent=2)+'\n')
diff=''.join(''.join(difflib.unified_diff(old[n].splitlines(True),(B/'fragments'/f'p{n:02d}.html').read_text().splitlines(True),fromfile=f'p{n:02d}.avant.html',tofile=f'p{n:02d}.apres.html'))for n in [6,9,11,12])
(B/'CORRECTIONS_P3.diff').write_text(diff)
print('Quatre zones corrigées ;',len(newpass),'passages nouveaux, aucun score P3.')
