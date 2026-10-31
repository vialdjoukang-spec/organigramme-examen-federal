from pathlib import Path
from html import escape
import base64,json,re
D=Path(__file__).resolve().parents[1]
R=D.parents[1]
S=json.loads((D/'evidence/sources.json').read_text())
T=['Définition et sémantique','Épidémiologie et contexte','Physiopathologie et bases indispensables','Démarche diagnostique : les graves d’abord','Anamnèse et drapeaux rouges','Examen physique ciblé','Approche syndromique','Diagnostic positif et critères','Examens complémentaires','Arbre décisionnel','Prise en charge en Suisse','Prévention','Points clés','Pièges d’examen']
def paras(*texts):return '\n'.join('<p>'+t+'</p>' for t in texts)
def table(headers,rows):return '<div class="tw"><table><thead><tr>'+''.join('<th scope="col">'+h+'</th>' for h in headers)+'</tr></thead><tbody>'+ '\n'.join('<tr>'+''.join('<td>'+v+'</td>' for v in row)+'</tr>' for row in rows)+'</tbody></table></div>'
def steps(*texts):return '<ol>'+''.join('<li>'+t+'</li>\n' for t in texts)+'</ol>'
def ref(ns):return '<sup class="s">'+','.join(f'<a href="#s{n}">{n}</a>' for n in ns)+'</sup>'
ABBR={'EHRA':'Association européenne du rythme cardiaque','INR':'rapport international normalisé du temps de prothrombine','AVK':'antivitamine K','AOD':'anticoagulant oral direct','PTI':'purpura thrombopénique immunologique','CIVD':'coagulation intravasculaire disséminée','HTA':'hypertension artérielle','BCG':'bacille de Calmette et Guérin','SFORL':'Société française d’oto-rhino-laryngologie et de chirurgie de la face et du cou','CHU':'centre hospitalier universitaire','ANSM':'Agence nationale de sécurité du médicament et des produits de santé','i.m.':'intramusculaire','i.v.':'intraveineux','p. ex.':'par exemple','AOH':'angioœdème héréditaire','ESMO':'Société européenne d’oncologie médicale','EURACAN':'réseau européen de référence pour les cancers solides rares de l’adulte','SCAR':'réaction cutanée indésirable sévère','ECG':'électrocardiogramme','CHUV':'Centre hospitalier universitaire vaudois','LCR':'liquide cérébrospinal','VIH':'virus de l’immunodéficience humaine','VZV':'virus varicelle-zona','AIT':'accident ischémique transitoire','PNDS':'protocole national de diagnostic et de soins','HAS':'Haute Autorité de santé','UNESS':'Université numérique en santé et sport','SPILF':'Société de pathologie infectieuse de langue française','DGN':'Société allemande de neurologie','IEC':'inhibiteur de l’enzyme de conversion de l’angiotensine','ORL':'oto-rhino-laryngologie','HUG':'Hôpitaux universitaires de Genève','TDM':'tomodensitométrie','IRM':'imagerie par résonance magnétique','EMG':'électromyographie','HPV':'papillomavirus humain','CEN':'Collège des enseignants de neurologie','AIPS':'plateforme suisse de publication des informations sur les médicaments','DOI':'identifiant numérique permanent d’un document','AVC':'accident vasculaire cérébral'}
ABBR.update({'ENT UK':'association britannique des spécialistes des oreilles, du nez et de la gorge','NHS':'service national de santé britannique','AP-HM':'Assistance publique–Hôpitaux de Marseille','CERECAI':'centre de référence des cytopénies auto-immunes de l’adulte','IgA':'immunoglobuline A','IgIV':'immunoglobulines intraveineuses','p.c.':'poids corporel','NaCl':'chlorure de sodium','ADH':'hormone antidiurétique','SIADH':'syndrome de sécrétion inappropriée d’hormone antidiurétique','FVIII:C':'activité coagulante du facteur VIII','FvW:RCo':'activité cofacteur de la ristocétine du facteur de von Willebrand','FvW':'facteur de von Willebrand','UI':'unités internationales'})
ABBR.update({'env.':'environ','SDU':'présentation en dose unitaire','NICE':'institut britannique pour la qualité des soins et des recommandations cliniques'})
ABBR.update({'FEES':'évaluation endoscopique de la déglutition','VFSS':'vidéofluoroscopie de la déglutition','UEG':'United European Gastroenterology','ESNM':'Société européenne de neurogastroentérologie et de motilité','ESGE':'Société européenne d’endoscopie digestive','SRC':'Swiss Resuscitation Council','ERC':'Conseil européen de réanimation','RCP':'réanimation cardiopulmonaire','DAE':'défibrillateur automatisé externe','ESO':'Organisation européenne de l’accident vasculaire cérébral','ESSD':'Société européenne des troubles de la déglutition','BLS':'réanimation de base','AED':'défibrillateur automatisé externe'})
ABBR.update({'MuSK':'tyrosine kinase spécifique du muscle','LRP4':'protéine 4 apparentée au récepteur des lipoprotéines','BPF':'bonnes pratiques de fabrication','CYP3A':'sous-famille 3A des enzymes cytochromes P450','POEM':'myotomie endoscopique perorale','HRM':'manométrie à haute résolution','FLIP':'planimétrie fonctionnelle par impédance','IPP':'inhibiteur de la pompe à protons','NTI':'néphrite tubulo-interstitielle','resp.':'respectivement'})
ABBR.update({'ESHNR':'Société européenne de radiologie de la tête et du cou','CKS':'synthèses de connaissances cliniques de NICE','ClCr':'clairance de la créatinine'})
ABBR.update({'SSI':'Société suisse d’infectiologie','SDCEP':'programme écossais de recommandations pour les soins dentaires','BNFC':'formulaire national britannique pédiatrique','HSV':'virus herpès simplex','PCR':'réaction de polymérisation en chaîne','EULAR':'Alliance européenne des associations de rhumatologie'})
ABBR.update({'SSA':'antigène A associé à Sjögren, aussi appelé Ro','EHNS':'Société européenne de la tête et du cou','ESTRO':'Société européenne de radiothérapie et d’oncologie'})
ABBR.update({'cf.':'se reporter à'})
ABBR.update({'OFSP':'Office fédéral de la santé publique','RCEM':'Collège royal britannique de médecine d’urgence','HLA-A*3101':'allèle A*3101 du système des antigènes leucocytaires humains','HLA-B*1502':'allèle B*1502 du système des antigènes leucocytaires humains'})
ABBR.update({'CMV':'cytomégalovirus','PTEN':'gène codant la phosphatase et homologue de la tensine','BESS':'élargissement bénin des espaces sous-arachnoïdiens','ADN':'acide désoxyribonucléique'})
ABBR.update({'ERN GENTURIS':'réseau européen de référence des syndromes génétiques de prédisposition tumorale','IgM':'immunoglobulines de classe M','ASPM':'gène de la protéine associée à la microcéphalie à fuseau anormal','WDR62':'gène de la protéine 62 à répétitions WD','CDK5RAP2':'gène de la protéine 2 associée au régulateur de la kinase 5 dépendante des cyclines'})
ABBR.update({'EPOS2020':'édition 2020 des recommandations européennes sur les rhinosinusites et la polypose nasale','EPOS':'recommandations européennes sur les rhinosinusites et la polypose nasale','IgE':'immunoglobulines de classe E','CRP':'protéine C réactive','QT':'intervalle électrocardiographique de dépolarisation et repolarisation ventriculaires'})
ABBR.update({'CYP3A4':'enzyme cytochrome P450 3A4','DFG':'débit de filtration glomérulaire'})
ABBR.update({'BIHAM':'Institut bernois de médecine de famille','p.ex.':'par exemple'})
ABBR.update({'NAIROS':'essai britannique Nasal AIRway Obstruction Study sur la chirurgie de la cloison nasale'})
ABBR.update({'S2k':'recommandation allemande élaborée par consensus structuré'})
ABBR.update({'PC':'poids corporel','AINS':'anti-inflammatoires non stéroïdiens','NYHA':'classification fonctionnelle de la New York Heart Association','S3':'recommandation allemande fondée sur une recherche systématique et un consensus structuré','AO Spine':'réseau international de recherche et formation sur le rachis','NEXUS':'règle National Emergency X-Radiography Utilization Study pour le traumatisme cervical'})
ABBR.update({'SSSSC':'Société suisse de recherche sur le sommeil, de médecine du sommeil et de chronobiologie','SAHOS':'syndrome d’apnées-hypopnées obstructives du sommeil','IAH':'indice d’apnées-hypopnées','PPC':'pression positive continue','CPAP':'pression positive continue','OAM':'orthèse d’avancement mandibulaire','PSG':'polysomnographie','IMC':'indice de masse corporelle','TSH':'thyréostimuline','T4':'thyroxine','GH':'hormone de croissance','IGF-1':'facteur de croissance analogue à l’insuline de type 1','TPO':'thyroperoxydase'})
ABBR.update({'TBG':'globuline fixant la thyroxine','LAR':'présentation à libération prolongée','IGF - 1':'facteur de croissance analogue à l’insuline de type 1','s.c.':'sous-cutanée','s .c.':'sous-cutanée','NoSAS':'score de risque associant tour de cou, obésité, ronflement, âge et sexe','STOP-Bang':'questionnaire de risque associant ronflement, fatigue, apnées observées, pression artérielle, corpulence, âge, tour de cou et sexe'})
ABBR.update({'RCOphth':'Royal College of Ophthalmologists, collège royal britannique des ophtalmologistes','SNC':'système nerveux central','SFO':'Société française d’ophtalmologie','AFSOP':'Association francophone de strabologie et d’ophtalmologie pédiatrique','EUGOGO':'Groupe européen sur l’orbitopathie de Graves','III':'troisième nerf crânien, nerf oculomoteur','IV':'quatrième nerf crânien, nerf trochléaire','VI':'sixième nerf crânien, nerf abducens'})
ABBR.update({'i. v.':'intraveineux','i. m.':'intramusculaire','RB1':'gène de prédisposition au rétinoblastome'})
ABBR.update({'i.m .':'intramusculaire','WAO':'Organisation mondiale de l’allergie','EAACI':'Académie européenne d’allergologie et d’immunologie clinique'})
class Lesson:
 def __init__(self,title,n=None):self.title=title;self.n=n;self.prefix='a' if n is None else f'dx{n}';self.parts=[];self.windows=[]
 def add(self,main,detail='',refs=(1,)):
  i=len(self.parts)+1
  if detail:
   m=re.search(r'\{([^{}]+)\}',main);assert m
   ident=f'{self.prefix}-detail{i}';label=m[1]
   main=main.replace(m[0],f'<button type="button" class="terme" popovertarget="{ident}">{label}</button>')
   self.windows.append(f'<div id="{ident}" popover class="fenetre"><div class="barre"><span>{label}</span><button type="button" popovertarget="{ident}" popovertargetaction="hide" aria-label="Fermer">✕</button></div><div class="corps">{detail}{ref(refs)}</div></div>')
  self.parts.append((main,refs))
 def subwindow(self,key,label,detail,refs):
  ident=f'{self.prefix}-{key}'
  self.windows.append(f'<div id="{ident}" popover class="fenetre sousf"><div class="barre"><span>{label}</span><button type="button" popovertarget="{ident}" popovertargetaction="hide" aria-label="Fermer">✕</button></div><div class="corps">{detail}{ref(refs)}</div></div>')
  return f'<button type="button" class="terme" popovertarget="{ident}">{label}</button>'
 def quiz(self,items,refs=(1,3,4,6,7)):
  assert len(items)==14
  self.add('Les {pièges d’examen} relient les signes aux décisions utiles. Ces questions pédagogiques sont originales et ne sont pas présentées comme des sujets officiels.', '\n'.join('<details class="quiz"><summary>'+q+'</summary>'+paras(a)+'</details>' for q,a in items),refs)
 def write(self):
  assert len(self.parts)==14
  css=(R/'harnais/modele_lecon/style_lecon.css').read_text()
  for w in (400,700):
   b=base64.b64encode((R/f'codex-LOTS-html/outils/polices/atkinson-hyperlegible-latin-{w}-normal.woff2').read_bytes()).decode();b='\\\n'.join(b[i:i+160] for i in range(0,len(b),160))
   css+=f'\n@font-face{{font-family:"Atkinson Hyperlegible";font-weight:{w};font-style:normal;src:url("data:font/woff2;base64,{b}") format("woff2")}}'
  css+='\n@media(max-width:480px){.fenetre.sousf{translate:0 .6rem}.som{columns:1}}'
  heading=self.title if self.n is None else f'DX.{self.n} — {self.title}'
  out=['<!doctype html>','<html lang="fr"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">',f'<title>{escape(self.title)} — S1.21</title><style>'+css.replace('}','}\n')+'</style></head><body><main>',f'<h2>{heading}</h2>','<p class="sous">Situation S1.21 · Sources consultées le 31 octobre 2026.</p>','<p id="taille" class="taille">Taille à mesurer.</p>']
  if self.n is not None:out.append(paras('Pour le tri et les gestes communs, voir le <a href="LOT_037_Phase_A_V0.html">cours sur le strabisme</a>.'))
  out.append('<nav class="ilot v" aria-label="Sommaire"><h2>Sommaire</h2><ol class="som">'+''.join(f'<li><a href="#{self.prefix}-p{i}">{t}</a></li>\n' for i,t in enumerate(T,1))+'</ol></nav>')
  for i,(main,refs) in enumerate(self.parts,1):out.append(f'<section class="ilot {"c" if i%2 else "v"}"><h2 id="{self.prefix}-p{i}">{i}. {T[i-1]}</h2>'+paras(main+ref(refs))+'</section>')
  out.extend(self.windows)
  used=sorted({int(x) for x in re.findall(r'href="#s(\d+)"',''.join(out))})
  out.append('<section class="ilot c sources"><h2>Sources</h2><ol>'+''.join(f'<li id="s{n}" value="{n}">{escape(S[n-1][0])} <a href="{escape(S[n-1][1],quote=True)}">Source</a>. Consulté le 31.10.2026.</li>\n' for n in used)+'</ol></section>')
  out.append(paras('Contenu établi à partir des sources citées ; non validé cliniquement par un médecin.'))
  fin='LOT_037_Phase_A' if self.n is None else f'LOT_037_Phase_B_DX.{self.n}'
  out+=['</main></body></html>',f'<!-- FIN_FICHIER {fin} -->']
  raw='\n'.join(out).replace('\u00a0',' ').replace('\u202f',' ')
  pattern=re.compile(r'(?<!\w)('+'|'.join(re.escape(k) for k in ABBR)+r')(?!\w)')
  chunks=[];body=False
  for x in re.split('(<[^>]+>)',raw):
   if x.startswith('<body'):body=True
   chunks.append(pattern.sub(lambda m:f'<abbr title="{ABBR[m[0]]}">{m[0]}</abbr>',x) if body and not x.startswith('<') else x)
  dest=D/('LOT_037_Phase_A_V0.html' if self.n is None else f'LOT_037_Phase_B_V0_DX.{self.n}.html');dest.write_text(''.join(chunks));print(dest.name)
