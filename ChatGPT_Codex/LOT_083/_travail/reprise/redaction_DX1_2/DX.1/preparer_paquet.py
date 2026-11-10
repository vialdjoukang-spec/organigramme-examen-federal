from pathlib import Path
import json,re,hashlib
B=Path(__file__).resolve().parent
LOT=B.parents[3]
R=Path('/workspace/organigramme-examen-federal')
passages=[]
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def ajouter(i,t,source,url,fichier=None,start=None,**meta):
    assert i not in {x['id']for x in passages}
    d={'id':i,'source':source,'url':url,'date':'2026-11-10','texte':t,'lecture':'Extrait exact et contigu réellement lu avant rédaction ; aucune fusion.',**meta}
    if fichier:
        d['preuve']={'fichier':str(fichier),'sha256_fichier':sha(fichier),'offset_debut':start,'offset_fin':None if start is None else start+len(t),'unite':'caractères Unicode Python'}
    passages.append(d)
def bornes(i,s,debut,fin,source,url,cache,**meta):
    a=s.index(debut);z=s.index(fin,a+len(debut)) if fin else len(s)
    ajouter(i,s[a:z].strip(),source,url,cache,a,**meta)
raw=LOT/'reprise/PAQUET_P1_REPRISE.json'
if not raw.exists():raw=R/'ChatGPT_Codex/LOT_083/_travail/reprise/PAQUET_P1_REPRISE.json'
pk=json.loads(raw.read_text())
for x in pk['passages']:
    d=dict(x);d['provenance_P1']={'fichier':str(raw),'sha256':sha(raw)};passages.append(d)
src=R/'ChatGPT_Codex/LOT_083/_travail/reprise/sources/source_01.txt';s=src.read_text();u='https://register.awmf.org/assets/guidelines/030-051l_S1_Diagnostik-Differentialdiagnose-Myalgien_2025-04.pdf'
for i,a,z in [
('dgn83-bib','**Version**','**Korrespondenz**'),
('dgn83-localisation','### **3\\.1.1.1**','### **3\\.1.1.5**'),
('dgn83-laboratoire','### **3\\.1.2**','**Tabelle 1.'),
('dgn83-imagerie','### **3\\.1.4**','### **3\\.1.5**')]:bornes(i,s,a,z,'DGN/SNG — Diagnostik und Differenzialdiagnose bei Myalgien, révision2025',u,src,annee_edition=2025)
# Références locales : la source diagnostique DGN implique explicitement la SNG.
path=B/'EXTRACTION_CAIRN.json';dat=json.loads(path.read_text())['results'][0];s=dat['full_content'];url=dat['url'];source='Jean-Michel Guérit — Le syndrome de la douleur myofasciale, Consilio manuque2020/2, mise en ligne2024'
for n in [1,2,7,8,9,10,13,15,16,17,19,20,21,22,23,25,26,27,30,31]:
    m=re.search(r'(?m)^'+str(n)+r' ',s);assert m,n;a=m.start();m2=re.search(r'(?m)^(?:'+str(n+1)+r' |# )',s[m.end():]);z=m.end()+m2.start() if m2 else len(s)
    ajouter(f'c83-{n}',s[a:z].strip(),source,url,path,a,annee_edition=2020,mise_en_ligne='2024-04-10',limite='Revue clinique européenne ; seuls les passages lus utilisés, descriptions d’images produites par IA écartées.')
path=B/'EXTRACTION_IASP_BARBERO.json';d=json.loads(path.read_text())['results'];s=d[0]['full_content'];url=d[0]['url'];source='IASP — Myofascial Pain, Fact Sheet14, fichier révisé2017'
for i,a,z in [
('iasp83-definition','Myofascial pain syndrome (MPS)','**Epidemiology**'),
('iasp83-physio','**Pathophysiology**','**Clinical Features**'),
('iasp83-clinique','**Clinical Features**','**Diagnostic Criteria**'),
('iasp83-criteres','**Diagnostic Criteria**','**Diagnosis and Treatment**'),
('iasp83-traitement','**Diagnosis and Treatment**','**REFERENCES**')]:bornes(i,s,a,z,source,url,path,annee_document=2017,limite='Date2017 issue du nom du document révisé ; date de chargement2022 distincte. Statistiques de populations non identifiées non transposées à la Suisse.')
ajouter('barbero83-resume',d[1]['full_content'], 'Barbero/Schneebeli/Koetsier/Maino, SUPSI et Lugano — revue suisse2019, résumé seulement',d[1]['url'],path,None,annee_edition=2019,acces='Résumé institutionnel seulement ; ne signifie pas lecture de l’article complet.')
path=B/'EXTRACTION_EU2019_NEEDLING.json';d=json.loads(path.read_text())['results'][0];s=d['full_content'];source='Fernández-de-las-Peñas/Nijs — revue européenne, J Pain Res2019, mécanismes et limites du dry needling'
starts=[
('eu83-actif','Myofascial TrPs can be clinically classified'),
('eu83-latent','Similarly, a latent TrP'),
('eu83-phenotypes','The referred sensation elicited'),
('eu83-milieu','Muscle TrPs are associated'),
('eu83-moteur','Importantly, and many times'),
('eu83-modes','Several needling treatments'),
('eu83-twitch-doute','However, the number of local twitch'),
('eu83-risques','Clinicians must follow guidelines'),
('eu83-courbatures','Nevertheless, it is commonly seen'),
('eu83-efficacite','It was 40 years ago'),
('eu83-limite-effet','In 2016, the Canadian Agency'),
('eu83-comparateur','An interesting meta-analysis'),
('eu83-heterogene','Nevertheless, it should be recognized'),
('eu83-modeles','The underlying mechanisms by which'),
('eu83-mecanique','From a mechanical viewpoint'),
('eu83-neurophysio','From a neurophysiological viewpoint'),
('eu83-peripherie','There is evidence supporting that'),
('eu83-brainstem','Finally, a decrease of dorsal horn'),
('eu83-multimodal','When providing dry needling'),
('eu83-sensibilisation','Here we provide a proposal'),
('eu83-nociplastic','Pain arising from altered nociception'),
('eu83-reeducation','Understanding central nervous'),
('eu83-education','Applying contemporary pain neuroscience'),
('eu83-attentes','Some aspects not usually considered'),
('eu83-communication','Fourth, another important topic')]
for i,needle in starts:
    a=s.index(needle);z=s.find('\n\n',a);assert a<39500,(i,a)
    ajouter(i,s[a:z],source,d['url'],path,a,annee_edition=2019,portee='Synthèse par auteurs européens ; ne sert pas de recommandation américaine. Modèles expérimentaux explicitement distingués des effets cliniques.')
path=B/'EXTRACTION_DVS_NICE.json';d=json.loads(path.read_text())['results'];s=d[0]['full_content'];u=d[0]['url'];source='Dry Needling Association Switzerland — Swiss Guidelines for safe Dry Needling, version2.0/19.08.2022'
for i,a,z in [
('dvs83-bib','# Swiss Guidelines','**Preface**'),
('dvs83-indications','**2\\.** **Indication','**3\\.** **Contraindications'),
('dvs83-infections','3.1. **Acute systemic','3\\.3. **Anticoagulant'),
('dvs83-coagulation','3\\.3. **Anticoagulant','3\\.4. **No explicit'),
('dvs83-consentement','3\\.4. **No explicit','3\\.6. **Lymphoedema'),
('dvs83-locaux','3\\.6. **Lymphoedema','3\\.14. **Pregnancy**'),
('dvs83-speciaux','3\\.14. **Pregnancy**','**4\\.** **Important'),
('dvs83-competences','**4\\.** **Important','**5\\.** **Handling'),
('dvs83-information','**5\\.** **Handling','**6\\.** **Practical'),
('dvs83-asepsie','8\\.6. **Disinfection','8\\.8. **Handling'),
('dvs83-pneumothorax','9.1. **Pneumothorax**','9\\.2. **Traumas'),
('dvs83-hemorragie','9\\.4. **Bleedings**','9\\.5. **Infections**'),
('dvs83-infection-apres','9\\.5. **Infections**','9\\.6. **Vegetative reactions**')]:bornes(i,s,a,z,source,u,path,annee_edition=2022,portee='Sécurité du geste par association suisse ; pas une recommandation nationale d’efficacité ni un protocole autonome pour praticien non formé.')
s=d[1]['full_content'];u=d[1]['url'];source='NICE NG193 — Chronic pain (primary and secondary), recommandations publiées07.04.2021, page officielle consultée2026'
for i,a,z in [
('nice83-definition','This section covers all types','##### 1\\.1.1'),
('nice83-evaluation','##### 1\\.1.1','##### 1\\.1.6'),
('nice83-vie','##### 1\\.1.6','##### 1\\.1.10'),
('nice83-physique','##### 1\\.2.1','##### Psychological'),
('nice83-psycho','###### 1\\.2.3','##### Acupuncture'),
('nice83-aiguilles','###### 1\\.2.5','##### Electrical'),
('nice83-eviter','##### 1\\.2.10','##### 1\\.2.11'),
('nice83-reviser','##### 1\\.2.11','##### 1\\.2.13')]:bornes(i,s,a,z,source,u,path,annee_edition=2021,portee='Traitement seulement si douleur chronique primaire>=16ans ; évaluation générale de toute douleur chronique distincte. Ne couvre pas automatiquement toute myofascialgie aiguë ou secondaire.')
ancien=R/'ChatGPT_Codex/LOT_082/_travail/reprise/redaction_DX7/DX.7/paquet.json';d=json.loads(ancien.read_text())
selected=['pa82-esur-gadolinium-grossesse','pa82-esur-renal','pa82-esur-hypersensibilite','pa82-esur-alternative','pa82-esur-mere-renale','pa82-esur-iode-grossesse','pa82-esur-allaitement','oa82-hug-force','pa17-lomb22-queue','pa17-lomb22-urgence','prompt-question-finale']
for x in d['passages']:
    if x['id']in selected:
        y=dict(x);y['provenance_reemploi']={'fichier':str(ancien),'sha256':sha(ancien),'lecture':'Extrait relu avant rédaction LOT083 ; aucun texte de cours réutilisé.'};passages.append(y)
path=R/'ChatGPT_Codex/LOT_080/_travail/preparation_suivante/AIPS_HUG2022/aips_dafalgan_sections_lues.json';d=json.loads(path.read_text())
for n,i in [(3,'indication'),(4,'posologie'),(5,'contreindications'),(8,'grossesse'),(16,'numero'),(19,'edition')]:
    if i=='numero':n=next(k for k,x in enumerate(d['sections'])if x['titre']=='Numéro d’autorisation')
    x=d['sections'][n];ajouter('aips-m83-dafalgan-'+i,x['texte'],'Swissmedic AIPS — Dafalgan®, information professionnelle juillet2026 ; '+x['titre'],d['dokumentStorageUrl'],path,None,type='aips',rubrique=x['titre'],date_source='juillet2026',portee='Antalgie symptomatique dans indications AIPS ; aucune efficacité spécifique du syndrome myofascial déduite.')
for cache,key,start,end in [
    ('EXTRACTION_EU2019_NEEDLING.json','eu83-bib','J Pain Res','## Abstract'),
    ('EXTRACTION_CAIRN.json','c83-bib','[Consilio manuque 2020/2','# Le syndrome'),
    ('EXTRACTION_DVS_NICE.json','nice83-bib','# Chronic pain','## On this page')]:
    f=B/cache;rows=json.loads(f.read_text())['results'];d=rows[1] if key=='nice83-bib'else rows[0];s=d['full_content'];bornes(key,s,start,end,d['title'],d['url'],f,nature='Métadonnées éditoriales exactes, distinctes des assertions cliniques.')
assert len({x['id']for x in passages})==len(passages)
pack={'LOT':'083','CODE_SSP':'S5.4','entite':'Syndrome douloureux myofascial','numero_DX':1,'auteur':'/root/sources_cutanees','date':'2026-11-10','statut':'PAQUET_DOCUMENTAIRE_AVANT_REDACTION','liste_canonique_sha256':'11a5d9fefc00b144b97b15fd0116849bede90d854bac04504cd7fcda0a2c9a6d','passages':passages,'limites':['Pas de prévalence/incidence suisse spécifique de MPS établie par les sources consultées ; fait qualitatif DGN conservé.','NICE NG193 : champ chronique primaire>=16ans, différent de l’antalgie d’une cause secondaire aiguë.','IASP : observations biologiques et critères discutés ; pas de biomarqueur clinique prétendu validé.','Barbero2019 : résumé suisse effectivement lu, corps complet non acquis.','Revue Guérit2020 mise en ligne2024 : descriptions d’images par IA ignorées ; aucune figure transcrite ni générée.','Images différées ; score/P3 exclusivement indépendant.']}
(B/'paquet.json').write_text(json.dumps(pack,ensure_ascii=False,indent=2)+'\n')
(B/'fragments').mkdir(exist_ok=True)
print('PAQUET',len(passages),'extraits',sha(B/'paquet.json'))
