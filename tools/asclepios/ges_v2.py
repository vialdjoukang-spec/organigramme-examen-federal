"""Asclépios · restructuration de GES (3 axes, sous-régions, ordre strict, renvois, lacunes).
Idempotent : repart de la version de main (git show origin/main:app_v2.html via json_inject extract faite avant)."""
import json,sys
P='data/GES.json'; g=json.load(open(P))
if any('ax' in r for r in g): sys.exit('GES déjà restructuré')
R={r['id']:r for r in g}
for r in g:
  for i,it in enumerate(r['items']): it['k']=f"{r['id']}_{i}"   # clé de progression stable
def take(rid,s):
  L=R[rid]['items']; m=[x for x in L if x['s']==s]; assert len(m)==1,(rid,s); return m[0]
FM='Füeßl H. S., Middeke M., Anamnese und Klinische Untersuchung (Duale Reihe, Thieme), chapitre « {} » : édition et pages À vérifier'
def new(p,s,gst,n,src,chap,key):
  return dict(p=p,s=s,g=gst,n=n,k=key,src=src+' · '+FM.format(chap),av='Pages Füeßl/Middeke à vérifier')
NEW={
'atm':new('Palpation','Articulation temporo-mandibulaire',"Inspecter la région prétragienne (tuméfaction, rougeur). Palper l’articulation juste en avant du tragus pendant que le patient ouvre et ferme lentement la bouche, puis palper le masséter et le temporal. Rechercher un claquement ou une crépitation.","Une douleur à la palpation de l’articulation et des bruits articulaires orientent vers une atteinte intra-articulaire ; une douleur des muscles masticateurs à la mobilisation oriente vers une cause musculaire.","Walker HK et al., Clinical Methods, 3e éd., chap. 163 « The Temporomandibular Joint Examination » (NCBI NBK271) ; StatPearls « Temporomandibular Syndrome » (NBK551612)","Kopf und Hals",'tete-cou_n1'),
'globe':new('Percussion','Globe vésical',"Patient en décubitus : percuter sur la ligne médiane de l’ombilic vers la symphyse, puis palper doucement la région sus-pubienne. Éviter la palpation profonde, douloureuse et source de réaction vagale.","Une matité sus-pubienne et une tension à la palpation évoquent un globe : matité jusque sous l’ombilic ≈ 500 mL, au-dessus ≈ 1000 mL. L’examen surestime le volume : le confirmer par échographie vésicale.","StatPearls « Postoperative Urinary Retention » (NBK549844) ; StatPearls « Male Urinary Retention: Acute and Chronic » (NBK538499)","Abdomen",'abdomen_n1'),
'releve':new('Palpation','Relevé ganglionnaire complet',"Palper bilatéralement et symétriquement toutes les aires accessibles : cervicales, sus-claviculaires, axillaires, épitrochléennes, inguinales et poplitées. Décrire chaque ganglion : siège, taille, consistance, mobilité ou fixité, sensibilité.","Seuils indicatifs chez l’adulte : anormal au-delà de 1 cm (cervical, axillaire), 1,5 cm (inguinal) et 0,5 cm (épitrochléen) ; tout ganglion sus-claviculaire, iliaque ou poplité palpable est anormal. Distinguer adénopathie localisée et généralisée, puis examiner le territoire de drainage.","StatPearls « Lymphadenopathy » (NBK558918) ; Mohseni S et al., Peripheral Lymphadenopathy: Approach and Diagnostic Tools, Iran J Med Sci 2014 (PMC3993046)","Lymphknoten",'ganglions_n1'),
'epitro':new('Palpation','Aires épitrochléennes',"Coude fléchi à 90°, soutenir l’avant-bras du patient d’une main ; de l’autre main, passée derrière le coude, palper juste au-dessus de l’épicondyle médial. Examiner les deux côtés.","Un ganglion épitrochléen de plus de 0,5 cm est pathologique chez l’adulte. Causes : infection de la main ou de l’avant-bras, mononucléose, lymphome ; plus rarement syphilis secondaire.","Walker HK et al., Clinical Methods, 3e éd., chap. 149 « Lymphadenopathy » (NCBI NBK256) ; StatPearls « Lymphadenopathy » (NBK513250)","Lymphknoten",'ganglions_n2'),
'ingui':new('Palpation','Aires inguinales',"Patient en décubitus, palper sous le ligament inguinal les groupes superficiels supéro-latéral, supéro-médial et inférieur, des deux côtés. Examiner la peau du membre inférieur, du périnée et des organes génitaux.","De petits ganglions fermes et mobiles de moins de 1 cm sont fréquents ; au-delà de 1,5 cm, le ganglion est anormal. Territoire : membre inférieur, peau sous l’ombilic, canal anal sous la ligne pectinée, scrotum, vulve ; rechercher une infection sexuellement transmissible ou une lésion du membre homolatéral.","StatPearls « Anatomy, Abdomen and Pelvis: Inguinal Lymph Node » (NBK557639) ; Clinical Methods chap. 149 (NBK256) ; PMC3993046","Lymphknoten",'ganglions_n3'),
'epaule':new('Neurologique','Examen neuro-vasculaire distal',"Avant et après toute réduction d’une luxation, tester la sensibilité de la face latérale du moignon de l’épaule (territoire du nerf axillaire) et palper la contraction du deltoïde. Palper le pouls radial, contrôler la recoloration et rechercher une tuméfaction axillaire. Noter le résultat.","Le nerf axillaire est lésé dans environ 40 % des luxations antérieures. Une sensibilité conservée n’exclut pas une paralysie motrice : la contraction du deltoïde est le meilleur indicateur.","StatPearls « Anterior Glenohumeral Joint Dislocation » (NBK557862) ; StatPearls « Shoulder Dislocations Overview » (NBK459125) ; Axillary nerve injury associated with glenohumeral dislocation (PMC5890131)","Schulter / Bewegungsapparat",'epaule_n1'),
'genou':new('Neurologique','Examen neuro-vasculaire distal',"Après un traumatisme du genou ou une suspicion de luxation, palper les pouls pédieux et tibial postérieur, mesurer la recoloration et l’IPS. Tester le nerf fibulaire commun (flexion dorsale de la cheville et des orteils, éversion, sensibilité du dos du pied) et le nerf tibial (flexion plantaire, sensibilité plantaire).","Le nerf fibulaire est atteint dans 10 à 40 % des luxations du genou. IPS < 0,9 : écho-doppler artériel ou angio-CT ; IPS ≥ 0,9 : surveillance clinique répétée pendant 48 à 72 h. Des pouls normaux n’excluent pas une lésion artérielle.","StatPearls « Knee Dislocation » (NBK470595) ; StatPearls « Peroneal Nerve Injury » (NBK549859) ; StatPearls « Ankle Brachial Index » (NBK544226)","Knie / Bewegungsapparat",'genou_n1'),
}
def grp(rid,spec):
  out=[]
  for sr,titles in spec:
    for t in titles:
      it=NEW[t[1:]] if t.startswith('+') else take(rid,t)
      it=dict(it); it['sr']=sr; out.append(it)
  return out
tc=grp('tete-cou',[('Face et articulation temporo-mandibulaire',['Faciès et symétrie','Artères temporales','+atm']),('Yeux',['Yeux : paupières, conjonctives, sclérotiques','Acuité visuelle',"Fond d'œil"]),('Oreilles',['Otoscopie','Test de Weber','Test de Rinne']),('Nez et sinus',['Nez et sinus']),('Bouche et oropharynx',['Cavité buccale et oropharynx',"Score de Centor pour l'angine"]),('Cou',['Cou','Thyroïde','Ganglions cervicaux','Trachée','Glandes salivaires','Souffle thyroïdien'])])
co=grp('coeur-vaisseaux',[('Précordium et veines jugulaires',['Région précordiale','Veines jugulaires','Reflux hépato-jugulaire','Choc de pointe','Soulèvement parasternal et frémissement',"Foyers d'auscultation",'Bruits B1, B2 et dédoublement','B3 et B4',"Caractérisation d'un souffle",'Souffles diastoliques','Frottement péricardique','Manœuvres dynamiques'])])
va=grp('coeur-vaisseaux',[('Artères et veines des membres',['Varices et insuffisance veineuse','Pouls périphériques','Aorte abdominale','Œdèmes','Souffles vasculaires','Indice de pression systolique cheville-bras (IPS)',"Test d'Allen",'Suspicion de thrombose veineuse profonde'])])
tr=grp('tr-genital',[('Région anale et rectum',['Préparation','Région anale','Toucher rectal','Prostate']),('Région inguinale',['Hernies de la paroi','Orifice inguinal','Hernie étranglée']),('Organes génitaux masculins',['Pénis et méat','Testicules, épididymes et cordons','Transillumination scrotale','Varicocèle','Scrotum aigu']),('Organes génitaux féminins',['Examen gynécologique au spéculum','Toucher vaginal bimanuel'])])
ra=grp('rachis',[('Statique et palpation',['Statique rachidienne','Épineuses et muscles paravertébraux',"Test d'Adams"]),('Rachis cervical',['Rachis cervical','Test de Spurling','Signe de Lhermitte']),('Rachis thoracique',['Rachis thoracique et ampliation']),('Rachis lombaire et racines',['Rachis lombaire','Test de Schober','Signe de Lasègue','Signe de Bragard','Lasègue inversé (étirement fémoral)','Examen radiculaire lombo-sacré','Syndrome de la queue de cheval']),('Articulations sacro-iliaques',['Articulations sacro-iliaques','Test de Gaenslen','Test FABER (Patrick) pour la sacro-iliaque'])])
cm=grp('coude-main',[('Coude',['Coude','Repères du coude','Mobilité du coude','Épicondylite latérale (test de Cozen)','Épicondylite médiale','Nerf ulnaire au coude']),('Poignet et main',['Main','Compression des métacarpo-phalangiennes','Tabatière anatomique','Doigt à ressaut','Mobilité du poignet et des doigts','Tendons fléchisseurs','Test de Phalen','Signe de Tinel au poignet','Testing moteur des nerfs de la main',"Test de Finkelstein (manœuvre d'Eichhoff)",'Grind test de la rhizarthrose'])])
for rid,L in [('tete-cou',tc),('tr-genital',tr),('rachis',ra),('coude-main',cm)]:
  assert len(L)==len(R[rid]['items'])+(1 if rid=='tete-cou' else 0),rid; R[rid]['items']=L
assert len(co)+len(va)==len(R['coeur-vaisseaux']['items'])
R['coeur-vaisseaux']['items']=co; R['coeur-vaisseaux']['r']='Cœur'
R['epaule']['items'].append(dict(NEW['epaule'])); R['genou']['items'].append(dict(NEW['genou']))
ab=R['abdomen']['items']; j=[x['s'] for x in ab].index('Signe du flot (onde liquidienne)')
ab[j]['s']='Signe du flot abdominal (onde liquidienne)'; ab.insert(j+1,dict(NEW['globe']))
take('genou','Signe du flot (balayage)')['s']='Signe du flot du genou (balayage)'
vasc=dict(r='Vaisseaux périphériques',id='vasc',items=va); gang=dict(r='Relevé ganglionnaire',id='ganglions',items=[dict(NEW['releve'],sr='Toutes les aires'),dict(NEW['ingui'],sr='Aires inguinales'),dict(NEW['epitro'],sr='Aires épitrochléennes')])
R['vasc']=vasc; R['ganglions']=gang
# doublons à technique identique : la technique renvoie, l'interprétation propre reste
f=take('rachis','Test FABER (Patrick) pour la sacro-iliaque'); f['g']="Technique identique au test FABER de la hanche (voir le renvoi) : flexion, abduction et rotation externe, talon sur le genou opposé, pression douce sur le genou et sur l’épine iliaque antéro-supérieure opposée."
o=take('geriatrie','Hypotension orthostatique'); o['g']="Technique : test d’orthostatisme de Schellong (voir le renvoi Constantes), en interrogeant en plus sur les symptômes au lever."
# renvois bidirectionnels (12)
X=[(('vasc','Aorte abdominale'),('abdomen','Palpation profonde')),
(('rachis','Test FABER (Patrick) pour la sacro-iliaque'),('hanche','Test FABER (Patrick)')),
(('neuro-nc','Dépistage cognitif'),('geriatrie','Dépistage cognitif')),
(('constantes',"Test d'orthostatisme (Schellong)"),('geriatrie','Hypotension orthostatique')),
(('neuro-nc','Pupilles et réflexes photomoteurs (II, III)'),('meninge-gcs','Pupilles et réflexes du tronc chez le comateux')),
(('neuro-nc','Vigilance et orientation'),('psychiatrie','Conscience et orientation')),
(('neuro-nc','Attention et mémoire'),('psychiatrie','Attention, concentration et mémoire')),
(('peau','Muqueuse buccale'),('tete-cou','Cavité buccale et oropharynx')),
(('neuro-moteur','Marche'),('hanche','Statique et marche')),(('neuro-moteur','Marche'),('geriatrie','Vitesse de marche')),
(('pediatrie','Méningite chez le nourrisson'),('meninge-gcs','Raideur de nuque')),
(('pediatrie','Pouls fémoraux'),('vasc','Pouls périphériques')),(('hanche','Examen neuro-vasculaire distal'),('vasc','Pouls périphériques')),
(('neuro-nc','Audition (VIII)'),('tete-cou','Test de Weber')),(('neuro-nc','Audition (VIII)'),('tete-cou','Test de Rinne')),
(('genou','Signe du flot du genou (balayage)'),('abdomen','Signe du flot abdominal (onde liquidienne)')),
(('epaule','Examen neuro-vasculaire distal'),('vasc','Pouls périphériques')),(('genou','Examen neuro-vasculaire distal'),('vasc','Pouls périphériques')),
(('ganglions','Relevé ganglionnaire complet'),('tete-cou','Ganglions cervicaux')),(('ganglions','Relevé ganglionnaire complet'),('seins','Creux axillaires')),(('ganglions','Relevé ganglionnaire complet'),('seins','Creux sus- et sous-claviculaires')),
(('ganglions','Aires épitrochléennes'),('coude-main','Coude')),(('ganglions','Aires inguinales'),('tr-genital','Orifice inguinal'))]
for a,b in X:
  for u,v in [(a,b),(b,a)]:
    it=take(*u); it.setdefault('x',[])
    if list(v) not in it['x']: it['x'].append(list(v))
AX={'reg':['peau','tete-cou','thorax','coeur-vaisseaux','seins','abdomen','tr-genital','rachis','epaule','coude-main','hanche','genou','cheville-pied'],
'sys':['constantes','vasc','ganglions','neuro-nc','neuro-moteur','meninge-gcs'],'pop':['pediatrie','geriatrie','psychiatrie']}
cred={c['region']:c for c in json.load(open('assets/cs/credits.json'))['images']}
out=[]
for ax,ids in AX.items():
  for i in ids:
    r=R[i]; r['ax']=ax
    if i in cred:
      c=cred[i]; r['fig']=dict(f=c['fichier'],c=c['legende'],cr=f"« {c['titre']} » · {c['auteur']} · {c['source']} · {c['licence']}",u=c['source_url'])
    out.append(r)
assert len(out)==22 and sum(len(r['items']) for r in out)==315
json.dump(out,open(P,'w'),ensure_ascii=False,separators=(',',':'))
print('OK',len(out),sum(len(r['items']) for r in out))
