from pathlib import Path
import json,copy,hashlib
B=Path(__file__).parent; R=B.parents[3]; S=B/'sources'; P=R/'LOT_083/_travail/reprise'
items=[]
def cut(id,file,start,end,title,url,year):
 t=Path(file).read_text();a=t.index(start);z=t.index(end,a+len(start));v=t[a:z].strip()
 items.append(dict(id=id,texte=v,source=title,url=url,annee_edition=year,date='2026-11-10',archive_source=str(file),bornes_caracteres=[a,z],integrite='Passage contigu réellement lu ; extraction sans fusion de règles.'))
u='https://www.revmed.ch/view/428428/3699762/RMS_613_1332.pdf';f=S/'rms2018_raw.txt';title='Schwitzguebel et al., CHUV, Revue médicale suisse — lésions musculaires aiguës, 11 juillet 2018'
for id,a,z in [('rms-mecanisme','Les lésions musculaires sont fréquentes','Acute muscle lesions'),('rms-clinique','Anamnèse\n• Mécanisme traumatique','TABLEAU 1 Eléments diagnostiques'),('rms-doms','les cas où un avis chirurgical','Le traitement des lésions musculaires est influencé'),('rms-imagerie','Le traitement des lésions musculaires est influencé','Anamnèse\n• Mécanisme traumatique'),('rms-reeducation','Rééducation adaptée\n','TABLEAU 4 Résumé'),('rms-reprise','Retour au sport:\n','≥ 2 jours ≥ 5 jours'),('rms-persistance','Si les objectifs rééducatifs','Autres modalités thérapeutiques'),('rms-antalgie','En raison de leur effet potentiellement','Même si, en phase subaiguë')]:
 cut(id,f,a,z,title,u,2018)
cut('rms-doms-soins',f,'Prise en charge médicale aiguë et subaiguë • Charge adaptée','Phase 1 rééducative',title,u,2018)
f=S/'doms2024_raw.txt';u='https://doi.org/10.5960/dzsm.2024.608';title='Schroeter et al., GOTS/Altius Swiss Sportmed — Update DOMS, août2024, Dtsch Z Sportmed75:189–194'
for id,a,z in [('doms-definition','The term Delayed Onset Muscle Soreness (DOMS)','The striated skeletal musculature'),('doms-mecanisme','Overload-Related Muscle Injuries:','Coupled with the inflammatory process'),('doms-biologie-imagerie','Coupled with the inflammatory process','Therapeutic Approaches to the Treatment'),('doms-prevention','injury entity. The central target','Systemic cryotherapy including'),('doms-physique','Systemic cryotherapy including','Finally, optimal sports nutrition'),('doms-nutrition','Finally, optimal sports nutrition','Conflict of Interest')]:
 cut(id,f,a,z,title,u,2024)
f=P/'sources/source_05.txt';u='https://pmc.ncbi.nlm.nih.gov/articles/PMC3940495/';title='ISMuLT, Italian Society of Muscles Ligaments and Tendons — Guidelines, édition2013, mise en ligne24février2014'
for id,a,z in [('ismult-direct','## After direct trauma','## After indirect trauma'),('ismult-indirect','## After indirect trauma','## Structural injuries'),('ismult-clinique','## Diagnosis: clinical assessment','## Imaging assessment'),('ismult-us','## Ultrasound scanning','## Magnetic Resonance Imaging')]:
 try:cut(id,f,a,z,title,u,2013)
 except ValueError:pass
f=P/'sources/source_07.txt';u='https://pmc.ncbi.nlm.nih.gov/articles/PMC6013414/';title='GOTS, German-Austrian-Swiss Society — Nonoperative treatment of muscle injuries,22juin2018'
for id,a,z in [('gots-price','### Primary care and initial treatment','#### Fig. 2.'),('gots-glace','#### Ice','#### Elevation'),('gots-protection','#### Protection/Rest','#### Ice'),('gots-elevation','#### Elevation','Finally, the initial'),('gots-ponction','#### Aspiration of intramuscular haematoma','##### Fig. 4.'),('gots-corticoides','##### Corticosteroid injections','##### Actovegin')]:
 cut(id,f,a,z,title,u,2018)
f=P/'sources/source_03.txt';u='https://www.revmed.ch/view/595366/4682463/RMS_716_2272.pdf';title='Dall’Aglio et al., CHUV — Rhabdomyolyse prise en charge initiale,25novembre2020'
for id,a,z in [('rhabdo-clinique','### PRÉSENTATION CLINIQUE','### INVESTIGATIONS DIAGNOSTIQUES'),('rhabdo-laboratoire','Laboratoire\n','Imagerie\n'),('rhabdo-orientation','### PRISE EN CHARGE MÉDICALE AIGUË','La clé de voûte'),('rhabdo-physiopath','### PHYSIOPATHOLOGIE','VIGNETTE CLINIQUE')]:cut(id,f,a,z,title,u,2020)
def take(path,select,prefix=''):
 for v in json.loads(Path(path).read_text())['passages']:
  if select(v):
   w=copy.deepcopy(v);w['id_origine']=w['id'];w['id']=prefix+w['id'];items.append(w)
take(R/'LOT_082/_travail/reprise/redaction_DX6_8/DX.8/paquet.json',lambda v:v['id'].startswith('r82-boast2025-loges'))
take(R/'LOT_081/_travail/reprise/preparation_neuro/radiculopathie_hernie_discale/paquet.json',lambda v:v['id']in['n81-hug22-force-normale','n81-cen-force','n81-cen-sensibilite'])
take(R/'LOT_082/_travail/reprise/redaction_DX1/DX.1/paquet.json',lambda v:v['id'].startswith('aips-oa82-dafalgan')and v['id'].split('-')[-1]in['forme','indications','posologie','ci','prudence','interactions','grossesse','effets','autorisation','date'])
take(R/'LOT_082/_travail/reprise/redaction_DX9_10/DX.10/paquet.json',lambda v:v['id']in['x101n','x101o','x101p','x101r','x101s','x101t'])
for n,name in [(3,'Courbatures retardées après effort'),(4,'Contusion musculaire traumatique')]:
 d=B/f'DX.{n}';d.mkdir(exist_ok=True);(d/'fragments').mkdir(exist_ok=True)
 pack=dict(lot='083',entite=name,date='2026-11-10',auteur='sources_os_rhum81',statut='Paquet documentaire avant rédaction ; aucun autoaudit',passages=items,limites=['Absence de fréquence suisse spécifique acquise ; chiffres de lésions sportives non transposés à DOMS ou contusion.','Délais de reprise des classifications anciennes non utilisés comme prescription universelle.','RMS2018 date du corps11juillet, distincte métadonnée connecteur4juillet ; GOTS2018 distincte métadonnée2022.','DOMS2024 actualise description et thérapeutique ; preuve variable des traitements symptomatiques.'])
 (d/'paquet.json').write_text(json.dumps(pack,ensure_ascii=False,indent=2)+'\n')
print(len(items),'passages',sum(len(x['texte'])for x in items),'caractères')
