from pathlib import Path
import json, hashlib

B=Path(__file__).resolve().parent
S=B/'sources'
R=B.parent
P=[]
def add(i,title,url,text,cache,year=None):
    assert text and text.strip()
    p={'id':i,'source':title,'url':url,'date':'2026-11-10','annee_edition':year,'texte':text,'cache_primaire':str(cache),'verification':'Passage exact contigu du support local réellement relu ; pas de fusion ni ellipse ajoutée.'}
    P.append(p)
    return p
def filepart(i,name,title,url,a,b=None,year=None):
    f=S/name; full=f.read_text(); start=full.index(a) if isinstance(a,str) else a
    end=full.index(b,start) if isinstance(b,str) else (len(full)if b is None else b)
    text=full[start:end].strip(); assert text in full
    p=add(i,title,url,text,f,year);p['preuve']={'offset_debut':full.index(text),'offset_fin':full.index(text)+len(text),'sha256_cache':hashlib.sha256(f.read_bytes()).hexdigest()};return p
dgn=(R/'sources/source_01.txt').read_text();durl='https://register.awmf.org/assets/guidelines/030-051l_S1_Diagnostik-Differentialdiagnose-Myalgien_2025-04.pdf'
def dg(i,a,b):
    start=dgn.index(a)if isinstance(a,str)else a;end=dgn.index(b,start)if isinstance(b,str)else b
    return add(i,'DGN/AWMF030-051 — Myalgien, S1 révisée2025',durl,dgn[start:end].strip(),R/'sources/source_01.txt',2025)
dg('dgn-date','Leitlinien für Diagnostik und Therapie in der Neurologie © DGN 2025','Leitlinien für Diagnostik und Therapie in der Neurologie © DGN 2025') if False else None
add('dgn-date','DGN/AWMF030-051 — édition2025',durl,'Leitlinien für Diagnostik und Therapie in der Neurologie © DGN 2025',R/'sources/source_01.txt',2025)
dg('dgn-definition','Muskelschmerzen (Myalgien) sind','Myalgien – Leitlinien')
dg('dgn-anamnese','Wie bei anderen Erkrankungen mit dem Leitsymptom Schmerz','### **3\\.1.1.4**')
dg('dgn-examen','Begleitende Symptome wie Muskelschwäche','### **3\\.1.2**')
dg('dgn-labo','Basislabordiagnostik:','Die Bestimmung des CK-Werts')
dg('dgn-ck','Die Bestimmung des CK-Werts','Wenn die Differenzialdiagnose')
dg('dgn-imagerie',31901,34300)
dg('dgn-biopsie','Eine Muskelbiopsie ist ein invasiver Eingriff','Generell sollte nur')
dg('dgn-statine','Am häufigsten treten unerwünschte Wirkungen am Muskel durch Statine auf.','Die toxische Myositis unter Statintherapie')
dg('dgn-toxique','Die toxische Myositis unter Statintherapie','Die autoimmunvermittelte Statin-assoziierte Myopathie')
dg('dgn-thyroide','Die häufigsten endokrinologischen Störungen mit Affektion des Muskels','Auch eine Hyperthyreose kann')
p1=json.loads((R/'PAQUET_P1_REPRISE.json').read_text());imnm=next(x for x in p1['passages']if x['id']=='p83-statine-imnm');P.append(dict(imnm,id='dgn-imnm'))
easurl='https://eas-society.org/wp-content/uploads/2022/05/2015_Consensus-SAMS.pdf'
for i,a,b in [('eas-definition',11676,13800),('eas-imputabilite',14695,15361),('eas-interactions',15361,17280),('eas-therapie',21281,21850),('eas-mecanisme',34990,37680),('eas-complements',30043,31100)]:
    filepart(i,'eas_sams.txt','European Atherosclerosis Society — consensusSAMS2015',easurl,a,b,2015)
filepart('eas-frequence','eas_sams.txt','EAS — consensusSAMS2015',easurl,'In contrast to RCTs, patient registries','Statin-associated mu',2015)
filepart('eas-date','eas_sams.txt','EAS — édition2015',easurl,'European Heart Journal (2015)','Downloaded from',2015)
ctturl='https://www.ndph.ox.ac.uk/publications/1279372'
for i,a,b in [('ctt-methodes','We analysed individual participant data','Standard inverse'),('ctt-resultats','FINDINGS: Among 19','For all years combined'),('ctt-interpretation','INTERPRETATION:','FUNDING:'),('ctt-date','##### Publication Date','##### Volume')]:
    filepart(i,'ctt2022.txt','CTT Collaboration — Lancet2022, résumé primaire des auteursOxford',ctturl,a,b,2022)
mdurl='https://www.medix.ch/wissen/guidelines/kurzversion/stoffwechselerkrankungen/hyperlipidaemie'
filepart('mdx-sams','medix_lipides.txt','mediX Suisse — Hyperlipidämie, court02/2025',mdurl,'Management Statinintoleranz wegen Myopathie','### Hypertriglyzeridämie',2025)
filepart('mdx-diagnostic','medix_lipides.txt','mediX Suisse — Hyperlipidämie, court02/2025',mdurl,'Ergänzende Basis-Untersuchungen','Familiäre Hypercholesterinämie',2025)
escurl='https://academic.oup.com/eurheartj/advance-article/doi/10.1093/eurheartj/ehaf190/8234482?login=false'
filepart('esc-nonstatines','esc2025.txt','ESC/EAS — FocusedUpdate2025',escurl,'Patients who are unable to take statins','## 5\\.',2025)
filepart('esc-reprise-ch','fmh_esc2025_reprise.txt','FMH/SSC — reprise suisseESC/EAS2025','https://www.guidelines.fmh.ch/index_detail.cfm?id=EAF3C06F9874C7BF537FC74509DB0DC3&l=2','Origine','## Procédure',2025)
cen='https://www.cen-neurologie.fr/premier-cycle/semiologie-analytique/syndrome-myogene-myopathique'
for i,a,b in [('cen-myogene-definition','Ensemble des symptômes','## I'),('cen-myogene-clinique','### 1\\. Faiblesse musculaire','## III'),('cen-myogene-emg','### 1\\. Electrodiagnostic','### 2\\. Augmentation')]:
    filepart(i,'cen_syndrome_myogene.txt','Collège des enseignants de neurologie — sémiologie myogène, date non affichée',cen,a,b)
ce='https://www.cen-neurologie.fr/premier-cycle/examen-neurologique'
for i,a,b in [('cen-force','## III - FORCE MUSCULAIRE','## IV - TONUS'),('cen-rot','### 1\\. Principaux réflexes ostéo-tendineux','### 2\\. Principaux réflexes cutanéo')]:
    filepart(i,'cen_examen_neurologique.txt','CEN — examen neurologique, sémiologie stable, date non affichée',ce,a,b)
fmh='https://leitfaden.samw.fmh.ch/fr/guide-pratique-bases-juridique/7-secret-medical-rapports/76-certificats-aux-employeurs.cfm'
filepart('fmh-secret','fmh_assm_certificats.txt','ASSM/FMH — certificats employeurs et assureurs, chapitre7.6',fmh,'Les certificats médicaux établis','## L’incapacité de travail')
filepart('fmh-evaluation','fmh_assm_certificats.txt','ASSM/FMH — capacité professionnelle',fmh,'Même si l’incapacité de travail est une notion juridique','La capacité de travail est définie')
filepart('fmh-certificat','fmh_assm_certificats.txt','ASSM/FMH — certificat daté et degré d’incapacité',fmh,'Le certificat le plus répandu','## Conseil pratique')
# Sources spécialisées déjà acquises/lues par le rédacteurDX9, puis relues ici.
rp=json.loads((R/'redaction_DX9/DX.9/paquet.json').read_text())
for i in ['e13','s02','s03','s11']:
    q=next(x for x in rp['passages']if x['id']==i);P.append(dict(q,id='rhabdo-'+i))
for drug in ['sortis','crestor','ezetrol','euthyrox']:
    f=S/f'aips_{drug}_sections_lues.json';j=json.loads(f.read_text());sec={x['titre']:x['texte']for x in j['sections']};url=j['dokumentStorageUrl']
    keys={'indications':'Indications/Possibilités d’emploi','posologie':'Posologie/Mode d’emploi','ci':'Contre-indications','grossesse':'Grossesse, allaitement','conduite':'Effet sur l’aptitude à la conduite et l’utilisation de machines','autorisation':'Numéro d’autorisation','date':'Mise à jour de l’information'}
    for k,t in keys.items():add(f'aips83-{drug}-{k}',f'Swissmedic/AIPS — {drug}, {t}',url,sec[t],f)
    for k,t in [('pd','Propriétés/Effets'),('pk','Pharmacocinétique'),('interactions','Interactions'),('prudence','Mises en garde et précautions')]:
        text=sec[t]
        if k=='pd':text=text.split('Efficacité clinique')[0]
        if k=='pk'and drug in ['sortis','crestor']:text=text[text.index('Métabolisme'):text.index('Cinétique pour certains groupes de patients')]
        if k=='interactions'and drug=='sortis':continue # interactions du tableau musculaire déjà dans la rubrique prudence
        if k=='interactions'and drug=='crestor':continue # revue des transporteurs dans posologie/prudence
        add(f'aips83-{drug}-{k}',f'Swissmedic/AIPS — {drug}, {t}',url,text,f)
hasurl='https://www.has-sante.fr/upload/docs/application/pdf/2023-03/recommandation_prise_en_charge_des_hypothyroidies_chez_ladulte_mel.pdf'
for i,a,b in [('has-date',198,264),('has-clinique',16683,17793),('has-diagnostic',19109,21957),('has-anticorps',21957,23540),('has-therapie',25459,28283),('has-suivi',31472,35956),('has-specialiste',39025,40583)]:
    filepart(i,'has_hypothyroide.txt','HAS — hypothyroïdies adultes, validé15/12/2022, publication2023',hasurl,a,b,2022)
sfeurl='https://www.sfendocrino.org/item-243-hypothyroidie'
for i,a,b in [('sfe-definition',3777,6444),('sfe-epidemio',6444,8219),('sfe-clinique',8219,10533),('sfe-gravite',10720,12756),('sfe-morphologie',12756,13268),('sfe-biologie',15064,15651),('sfe-central',24857,26372)]:
    filepart(i,'sfe_hypothyroide.txt','SFE/CEEDMM — Hypothyroïdie, référentiel2021, page publiée2022',sfeurl,a,b,2021)
mdthy='https://www.medix.ch/media/algorithmus_hypothyreose_2022_.pdf?1773314892'
filepart('mdx-thyroide','medix_thyroide_algorithme.txt','mediX Suisse — algorithme hypothyroïdie02/2026',mdthy,0,None,2026)
filepart('ch-hypothyroide','hirslanden_hypothyroide.txt','Hirslanden — hypothyroïdie, information clinique suisse','https://www.hirslanden.ch/fr/corporate/description-pathologies/hypothyroidie.html',0,None)
old=json.loads(Path('ChatGPT_Codex/LOT_082/_travail/reprise/redaction_DX2_5/DX.5/paquet.json').read_text());P.append(next(x for x in old['passages']if x['id']=='prompt-question-finale'))
assert len({p['id']for p in P})==len(P)
for n,name in [(6,'Symptômes musculaires associés aux statines'),(7,'Myopathie hypothyroïdienne')]:
    selected=[p for p in P if (n==6 and not p['id'].startswith(('aips83-euthyrox','sfe-','has-','mdx-thyroide','ch-hypothyroide')))or(n==7 and not p['id'].startswith(('eas-','ctt-','mdx-sams','mdx-diagnostic','esc-','aips83-ezetrol','aips83-crestor')))]
    j={'LOT':'083','CODE_SSP':'S5.4','entite':name,'auteur':'/root/sources_lot080','date':'2026-11-10','statut':'Paquet préparé avant rédaction, aucune P3 autoattribuée','passages':selected,'points':{},'regles':['Priorité AIPS suisse du produit : CK/CPK>5×LSN impose arrêt Sortis/Crestor ; ne pas transformer DGN<10× en dérogation.','Une association sous statine ne prouve pas la causalité ; sorties rhabdomyolyse/IMNM explicites.','Posologie de lévothyroxine seulement Euthyrox AIPS ; algorithme2026/ HAS ne remplacent pas cette notice.','Anomalie TSH légère isolée ne prouve pas une myopathie ; CK normale ne l’exclut pas.','Aucune prophylaxie par CoQ10, ni dose étrangère de soluté ou immunothérapie.','CEN utilisé pour sémiologie stable ; ancienne normeCK<70UI/L non reprise.','Images différées, aucun rang/score/dose inventé.']}
    (B/f'DX.{n}'/'paquet.json').write_text(json.dumps(j,ensure_ascii=False,indent=2)+'\n')
    print(n,len(selected))
(B/'INDEX_SOURCES.json').write_text(json.dumps({'auteur':'/root/sources_lot080','date':'2026-11-10','passages':len(P),'fichiers':[{'nom':str(p.relative_to(B)),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()}for p in S.glob('*')if p.is_file()]},ensure_ascii=False,indent=2)+'\n')
