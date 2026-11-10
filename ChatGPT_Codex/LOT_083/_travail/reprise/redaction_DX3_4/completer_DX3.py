from pathlib import Path
import json
B=Path(__file__).parent;D=B/'DX.3';P=json.loads((D/'paquet.json').read_text());A=json.loads((D/'contenu.json').read_text());t=(B/'sources/doms2024_raw.txt').read_text()
def add(id,text,source,url,year,archive):
 P['passages'].append(dict(id=id,texte=text,source=source,url=url,annee_edition=year,date='2026-11-10',archive_source=archive))
a=t.index('Schroeter S, Bloch');z=t.index('1.',a);add('doms-date',t[a:z],'Revue DOMS, en-tête bibliographique primaire','https://doi.org/10.5960/dzsm.2024.608',2024,str(B/'sources/doms2024_raw.txt'))
t2=(B/'sources/rms2018_raw.txt').read_text();add('rms-date',t2[:t2.index('Les lésions musculaires')],'RMS, en-tête imprimé','https://www.revmed.ch/view/428428/3699762/RMS_613_1332.pdf',2018,str(B/'sources/rms2018_raw.txt'))
fetch=json.loads((B/'sources/EXTRACTIONS_COMPLEMENTAIRES.json').read_text());v=next(x for x in fetch['results']if x['url']=='https://sems-journal.ch/990');s=next(e for e in v['excerpts']if '29. Maffulli' in e);a=s.index('29. Maffulli');z=s.index('30.',a);add('ismult-date',s[a:z],'SEMS2018, référence bibliographique ISMuLT2013','https://sems-journal.ch/990',2018,str(B/'sources/EXTRACTIONS_COMPLEMENTAIRES.json'))
a=t.index('central role as');z=t.index('The characteristic features',a);add('doms-sarcomere',t[a:z],'Schroeter et al., biomécanique du sarcomère','https://doi.org/10.5960/dzsm.2024.608',2024,str(B/'sources/doms2024_raw.txt'))
for pt in A['points'].values():
 for group in ['blocs','fenetres']:
  for _,items in pt[group]:
   for x in items:
    if '2013' in x[1]: x[0]+='+ismult-date'
    if '2018' in x[1]: x[0]+='+rms-date'
    if '2024' in x[1]: x[0]+='+doms-date'
    if x[1].startswith(('Une force cotée 3','Une contraction visible')):x[0]+='+n81-cen-force'
A['points']['3']['fenetres'].append(['Le sarcomère et les contraintes excentriques',[
 ['doms-sarcomere','Le sarcomère constitue la plus petite unité contractile ; les stries Z séparent les unités disposées en série dans la myofibrille.'],
 ['doms-sarcomere','Les filaments fins d’actine et épais de myosine changent leur disposition relative pendant l’allongement, sans modification de leur longueur propre.'],
 ['doms-sarcomere','La titine intervient également dans les modèles biomécaniques proposés pour expliquer la force et la raideur pendant une charge excentrique.'],
 ['doms-sarcomere+doms-mecanisme','Cette organisation permet de comprendre comment une contrainte excessive peut toucher les structures ultrascopiques sans créer obligatoirement une rupture macroscopique.'],
 ['doms-mecanisme','Les images et mécanismes cellulaires décrits après effort ne constituent toutefois pas un examen nécessaire chez chaque patient présentant une douleur retardée.']]])
A['points']['11']['fenetres'].append(['Adapter les moyens physiques à leur objectif',[
 ['doms-physique','La chaleur peut contribuer au soulagement d’une courbature constituée, avec des effets proposés sur le tonus musculaire et la perfusion.'],
 ['doms-physique','Le froid est aussi étudié pour réduire les manifestations secondaires de la sollicitation, selon des modalités et des contextes variables.'],
 ['doms-physique','Une amélioration symptomatique après une application ne prouve pas que la fibre a retrouvé toute sa capacité fonctionnelle.'],
 ['doms-prevention+rms-reprise','Les décisions de reprise restent donc reliées à l’activité possible, à la douleur et à la récupération de la force.'],
 ['doms-physique','Les mécanismes proposés pour la compression associent perfusion et drainage veineux ou lymphatique ; les résultats cliniques ne sont pas uniformes.'],
 ['doms-physique','Le massage peut modifier la perfusion locale, mais la revue souligne les incertitudes concernant son moment d’application et ses bénéfices.']]])
A['points']['12']['fenetres'].append(['Préparer une progression plutôt que compenser une surcharge',[
 ['doms-prevention','Une prévention cohérente examine le niveau de départ, puis augmente lentement la charge au lieu de chercher seulement un soin après chaque séance.'],
 ['doms-mecanisme','Le travail excentrique et une sollicitation inhabituelle doivent être identifiés dans le programme, car ils peuvent précéder les manifestations retardées.'],
 ['doms-definition+rms-reprise','Une phase douloureuse avec baisse de performance justifie des contraintes ajustées avant une reprise progressive des efforts spécifiques.'],
 ['doms-nutrition','Les antioxydants et les acides aminés ramifiés font l’objet de discussions, sans constituer une prescription systématique fondée sur le seul diagnostic.'],
 ['doms-nutrition','La revue ne rapporte pas de bénéfice fonctionnel de la gélatine associée à la vitamine C pour la récupération après blessure.'],
 ['doms-nutrition','Les effets de la créatine sur les dommages musculaires restent peu clairs dans cette synthèse ; une supplémentation ne remplace pas l’ajustement de charge.']]])
A['points']['5']['fenetres'].append(['Documenter la charge et le contexte concret',[
 ['rms-clinique','Le type de sport et le niveau d’expérience sont consignés avec l’intensité, les antécédents et la charge d’entraînement récente.'],
 ['doms-mecanisme','Une activité connue peut devenir inhabituelle par sa charge relative ; le récit précis est donc plus informatif que son seul nom.'],
 ['rms-clinique','L’entretien recherche une sensation de claquement, de raccourcissement ou une tuméfaction apparue brutalement, qui orientent vers une lésion aiguë.'],
 ['ismult-clinique','La présence d’une douleur au repos n’exclut pas les courbatures, mais sa chronologie et les constatations associées restent déterminantes.'],
 ['rhabdo-clinique','Un état fébrile, une asthénie ou des nausées peuvent accompagner une rhabdomyolyse et imposent de conserver un raisonnement plus large.']]])
(D/'paquet.json').write_text(json.dumps(P,ensure_ascii=False,indent=2)+'\n');(D/'contenu.json').write_text(json.dumps(A,ensure_ascii=False,indent=2)+'\n')
