from pathlib import Path
import json,re,hashlib,html,difflib
D=Path(__file__).resolve().parent
S=D.parent/'redaction_DX2_3/DX.2'
P=json.loads((S/'paquet.json').read_text())
C=json.loads((S/'contrat.json').read_text())
old={i:(S/'fragments'/f'p{i:02}.html').read_text() for i in range(1,15)}
new=old.copy();ajouts=[]
def source(i,title,url,t,annee,archive):
 z={'id':i,'source':title,'url':url,'date':'2026-11-10','annee_edition':annee,'texte':t,'archive_source':str(archive),'lecture':'Passage contigu réellement lu ; aucune ellipse de fusion ajoutée.'}
 P['passages'].append(z);ajouts.append(z)
def cite(*ids):return ''.join(f'<sup class="r"><a href="#sb-{i}">{i}</a></sup>' for i in ids)
def para(t,*ids):return '<p class="p">'+t+cite(*ids)+'</p>\n'
def fenetre(i,label,paras):return f'<button class="w" popovertarget="{i}">{label}</button><div class="fenetre" id="{i}" popover><h4>{label}</h4>\n'+''.join(paras)+'</div>\n'
def content(name):return json.loads((D/name).read_text())['results'][0]['full_content']
w=content('source_wfns.json');wu='https://pmc.ncbi.nlm.nih.gov/articles/PMC10911853/'
a=w.index('In summary, lumbar disk herniations');z=w.index('The majority',a)
source('dx2corr-wfns-definition','WFNS Spine Committee — Lumbar disc herniation, recommandations2024, conclusion',wu,w[a:z].strip(),2024,D/'source_wfns.json')
a=w.index('. 2024 Feb 20;');z=w.index('\n\n# Lumbar',a)
source('dx2corr-wfns-date','WFNS Spine Committee — identification éditoriale2024',wu,w[a:z],2024,D/'source_wfns.json')
a=w.index('### Results');z=w.index('### Conclusions',a)
source('dx2corr-wfns-distribution','WFNS Spine Committee — distribution et évolution, résumé2024',wu,w[a:z].strip(),2024,D/'source_wfns.json')
r=content('source_euneuro.json');eu='https://pmc.ncbi.nlm.nih.gov/articles/PMC9816178/'
a=r.index('In children over 1 year of age,');z=r.index('\n\n',a)
source('dx2corr-euneuro-modalite','ESNR/ESPR/UEMS — recommandations européennes de neuroradiologie pédiatrique,2022',eu,r[a:z],2022,D/'source_euneuro.json')
a=r.index('The use of gadolinium-based contrast agents');z=r.index('At present, regulations',a)
source('dx2corr-euneuro-contraste','ESNR/ESPR/UEMS — indications et précautions du contraste pédiatrique,2022',eu,r[a:z].strip(),2022,D/'source_euneuro.json')
a=r.index('. 2022 Sep 5;');z=r.index('\n\n# European',a)
source('dx2corr-euneuro-date','ESNR/ESPR/UEMS — identification éditoriale2022',eu,r[a:z],2022,D/'source_euneuro.json')
r=content('source_aderim.json');au='https://aderim.radiologie.fr/irm-ou-scanner-hernie-discale';a=r.index('Ces examens sont indiqués');z=r.index('\n\nmots-clés',a)
source('dx2corr-aderim','ADERIM, portail français de radiologie — IRM ou scanner, hernie discale',au,r[a:z],None,D/'source_aderim.json')
ch=json.loads((D/'source_wfns_ch.json').read_text())['results'][1];t=ch['full_content'];a=t.index('WFNS\n');z=t.index('SNCLF',a)
source('dx2corr-ch-wfns','Société suisse de neurochirurgie — délégués auprès de la WFNS',ch['url'],t[a:z].strip(),None,D/'source_wfns_ch.json')
E=json.loads((D.parent/'redaction_DX10/paquet.json').read_text())
for x in E['passages']:
 t=x['texte'];a=t.find('**Pregnant or lactating mother with renal impairment**')
 if a>=0:
  z=t.index('Do not administer gadolinium-based contrast agents.',a)+len('Do not administer gadolinium-based contrast agents.')
  source('dx2corr-esur-mere-renale','ESUR Contrast Media Safety Committee — grossesse/allaitement et atteinte rénale,2026',x['url'],t[a:z],2026,D.parent/'redaction_DX10/paquet.json');break
else:raise ValueError('Extrait ESUR ciblé absent')
# A01 : définition de société datée ; description anatomique hospitalière conservée.
add=para('Le comité rachis de la World Federation of Neurosurgical Societies (WFNS) décrit cette entité dans ses recommandations publiées en 2024.','dx2corr-wfns-date','dx2corr-wfns-definition')
add+=para('Il retient un déplacement localisé du matériel discal au-delà des limites normales de l’espace intervertébral, associé à des manifestations myotomales ou dermatomales.','dx2corr-wfns-definition')
add+=para('La douleur, la faiblesse et l’engourdissement constituent les manifestations précisées ; leur distribution distingue cette présentation des autres douleurs lombaires.','dx2corr-wfns-definition')
a=new[1].index('</p>')+4;new[1]=new[1][:a]+'\n'+add+new[1][a:]
# A02 : dates documentées, sans inventer l’année des observations Insel.
s=new[2];s=s.replace('<th scope="col">Lecture utilisable</th>','<th scope="col">Date et portée temporelle</th><th scope="col">Lecture utilisable</th>',1)
a=s.index('<tbody>')+len('<tbody>');z=s.index('</tbody>',a);body=s[a:z];rows=re.findall(r'<tr>.*?</tr>',body,re.S);assert len(rows)==3
cells=[para('La période d’observation de cette estimation n’est pas précisée par la page institutionnelle ; la consultation est datée dans les Sources.','n81-hernie-epidemiologie'),para('Cette donnée figure dans la stratégie HUG éditée en 2022 ; cette année identifie le référentiel et non une nouvelle cohorte.','n81-hug22-date','n81-hug22-syndrome-radiculaire'),para('Cette information pronostique institutionnelle ne précise pas d’année d’observation ; sa date de consultation ne devient pas une date de cohorte.','n81-hernie-conservateur')]
for row,cell in zip(rows,cells):
 td=list(re.finditer('</td>',row));pos=td[1].end();repl=row[:pos]+'<td>'+cell+'</td>'+row[pos:];body=body.replace(row,repl,1)
s=s[:a]+body+s[z:]
insert=para('La synthèse WFNS publiée en 2024 décrit une prédominance masculine et une fréquence plus importante entre 30 et 50 ans.','dx2corr-wfns-distribution','dx2corr-wfns-date')
insert+=para('Cette synthèse complète le cadre suisse par des données internationales ; ses populations ne se confondent pas avec celles des consultations HUG.','dx2corr-wfns-distribution','n81-hug22-syndrome-radiculaire')
s=s.replace('</tbody></table></div>','</tbody></table></div>\n'+insert,1);new[2]=s
# A04 : badges canoniques conditionnels ; gestes/délais intacts.
s=new[4].replace('🚩 Une atteinte de queue de cheval constitue','🚩 E2 — Une atteinte de queue de cheval constitue',1).replace('Une infection vertébrale ou épidurale est une autre cause grave','🚩 E3 — Une infection vertébrale ou épidurale est une autre cause grave',1)
add=para('🚩 E2 — Un déficit moteur aigu ou progressif fait rechercher une compression grave ; une anomalie discrète stable conserve les conditions de surveillance décrites par HUG.','n81-hug22-urgence-neuro','n81-hug22-deficit-discret')
s=s.replace('<div class="t"',add+'<div class="t"',1);new[4]=s
# A05 : ligne pédiatrique radiologique ; AIPS exclue de cette justification.
s=new[9]
row='<tr><td>'+para('L’enfant de plus d’un an nécessite une exploration des structures intrarachidiennes selon la question clinique.','dx2corr-euneuro-modalite')+'</td><td>'+para('Le consensus européen retient l’IRM pour ces structures ; les radiographies gardent une place initiale dans certaines douleurs persistantes et questions de stabilité.','dx2corr-euneuro-modalite')+'</td><td>'+para('Le besoin de contraste est motivé par la pathologie suspectée, notamment tumorale, infectieuse ou inflammatoire, avec prise en compte des risques pédiatriques.','dx2corr-euneuro-contraste')+'</td></tr>'
s,n=re.subn(r'<tr><td>Le patient est mineur.*?</tr>',lambda m:row,s,count=1,flags=re.S);assert n==1
p=[]
p.append(para('L’outil français ADERIM indique une imagerie lorsqu’une prise en charge percutanée ou chirurgicale est envisagée, et en urgence devant une radiculalgie déficitaire.','dx2corr-aderim'))
p.append(para('Pour cette recherche de hernie, l’injection de contraste n’est en principe pas nécessaire ; la demande peut donc préciser une IRM lombaire sans injection.','dx2corr-aderim'))
p.append(para('La demande indique aussi le côté atteint, le territoire radiculaire et les déficits, afin de confronter la lésion à la présentation clinique.','n81-hernie-imagerie','n81-hug22-syndrome-radiculaire'))
p.append(para('L’exploration d’un rachis opéré peut parfois nécessiter du contraste ; cette situation est donc signalée séparément à la radiologie.','dx2corr-aderim'))
p.append(para('Chez l’enfant de plus d’un an, le consensus de l’European Society of Neuroradiology et de l’European Society of Paediatric Radiology recommande l’IRM pour les structures intrarachidiennes.','dx2corr-euneuro-modalite'))
p.append(para('Ce consensus européen publié en 2022 associe aussi la division de neuroradiologie de l’European Union of Medical Specialists.','dx2corr-euneuro-date'))
p.append(para('Les radiographies restent initiales pour certaines douleurs persistantes ou questions de stabilité ; une alarme neurologique conserve cependant sa filière urgente.','dx2corr-euneuro-modalite','n81-hug22-urgence-neuro'))
p.append(para('Le gadolinium répond notamment à une question tumorale, infectieuse ou inflammatoire ; son injection est soigneusement pesée devant les risques de rétention et de fibrose systémique néphrogénique.','dx2corr-euneuro-contraste'))
p.append(para('L’immaturité rénale du nourrisson et du nouveau-né fait également partie des éléments pédiatriques à considérer, plutôt que de copier une demande adulte.','dx2corr-euneuro-contraste'))
p.append(para('Pour une mère enceinte ou allaitante présentant une atteinte rénale, l’ESUR demande de ne pas administrer de produit de contraste gadoliné.','dx2corr-esur-mere-renale'))
p.append(para('Cette restriction est distincte de l’emploi exceptionnel d’un agent macrocyclique pendant une grossesse sans atteinte rénale, lorsque l’indication est très forte.','dx2corr-esur-mere-renale','pa814-esur-grossesse'))
add=fenetre('dx2-correction-irm','Prescrire l’IRM et justifier le contraste selon le contexte',p)
a=s.index('<h4>9.d');s=s[:a]+add+s[a:];new[9]=s
# A07 : séparer prévention du handicap et de la survenue, sans promesse non prouvée.
s=new[12];a=s.index('<h4>Prévention secondaire')
s=s[:a]+para('Les conseils d’activité portent ici sur le fonctionnement et le handicap ; ils ne constituent pas une démonstration de réduction de l’incidence des hernies.','n81-nice-activite','n81-hernie-epidemiologie')+s[a:];new[12]=s
for i,t in new.items():
 (D/'fragments'/f'p{i:02}.html').write_text(t)
 C['points'][str(i)]['citations_autorisees']=list(dict.fromkeys(re.findall(r'href="#sb-([\w.\-:]+)"',t)))
(D/'paquet.json').write_text(json.dumps(P,ensure_ascii=False,indent=2)+'\n');(D/'contrat.json').write_text(json.dumps(C,ensure_ascii=False,indent=2)+'\n')
(D/'EXTRAITS_COMPLEMENTAIRES.json').write_text(json.dumps(ajouts,ensure_ascii=False,indent=2)+'\n')
mods=[i for i in range(1,15)if new[i]!=old[i]]
(D/'CORRECTIONS.diff').write_text(''.join(''.join(difflib.unified_diff(old[i].splitlines(True),new[i].splitlines(True),fromfile=f'avant/p{i:02}.html',tofile=f'apres/p{i:02}.html'))for i in mods))
R={'audit_source':'audits/DX2_P3.audit.json','role':'Correction ciblée ; aucun score ni autoaudit P3','sha256_manuscrit_avant':'2931f597ef9ef3fedb7113acdb5fe6dcec47a2b81dbb71eb2bfbf3926d1fff54','points_modifies':mods,'correspondances':[{'id':'DX2-A01','action':'Définition de consensus WFNS2024 ajoutée, sans changer la définition hospitalière.','sources':['dx2corr-wfns-definition','dx2corr-wfns-date']},{'id':'DX2-A02','action':'Colonne date/portée temporelle ajoutée : HUG2022 distingué de la période de cohorte ; année Insel non inventée. Distribution par âge/sexe complétée depuis WFNS2024.','sources':['n81-hug22-date','n81-hug22-syndrome-radiculaire','n81-hernie-epidemiologie','n81-hernie-conservateur','dx2corr-wfns-distribution','dx2corr-wfns-date']},{'id':'DX2-A03','action':'Texte inchangé : aucune population cellulaire ni cascade de maintien déduite du seul dosage tissulaire TNFα.','limite_conservee':True},{'id':'DX2-A04','action':'Badges E2/E3 canoniques ajoutés aux branches pertinentes sans changement de conduite.','sources':['n81-hug22-urgence-neuro','n81-hug22-deficit-discret','n81-hug22-infection-tumeur']},{'id':'DX2-A05','action':'AIPS retirée de la ligne d’imagerie pédiatrique, remplacée par le consensus européen ESNR/ESPR/UEMS2022 ; besoin de contraste pour hernie précisé selon ADERIM ; restriction ESUR mère enceinte/allaitante avec atteinte rénale ajoutée.','sources':['dx2corr-euneuro-modalite','dx2corr-euneuro-contraste','dx2corr-euneuro-date','dx2corr-aderim','dx2corr-esur-mere-renale']},{'id':'DX2-A06','action':'Objectif fonctionnel individualisé conservé ; aucun seuil de guérison ni promesse numérique ajoutés.','limite_conservee':True},{'id':'DX2-A07','action':'Prévention du handicap explicitement distinguée d’une réduction d’incidence ; aucun programme suisse garanti inventé.','sources':['n81-nice-activite','n81-hernie-epidemiologie']}],'limites_persistantes':['Incidence et mortalité suisses propres à l’entité non acquises ; aucune donnée créée.','L’année des observations Insel n’est pas substituée à celle de consultation.','Les populations cellulaires et la chaîne moléculaire complète n’ont pas reçu de source complémentaire exploitable.','Aucune cible universelle de récupération fonctionnelle ni prévention primaire suisse spécifique n’est créée.'],'doses_et_voies':'Toutes les posologies et voies AIPS restent inchangées.','images':'Différées selon ordre utilisateur.'}
(D/'CORRECTIONS.json').write_text(json.dumps(R,ensure_ascii=False,indent=2)+'\n')
print('Fragments modifiés',mods,'sources ajoutées',len(ajouts))
