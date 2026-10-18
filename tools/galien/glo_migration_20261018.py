import json
from pathlib import Path
S=Path('data/ck/src.json');src=json.loads(S.read_text());urls={s['url']:s['id'] for s in src}
def source(i,title,url,org,pays):
 if url in urls:return urls[url]
 src.append(dict(id=i,titre=title,url=url,org=org,pays=pays,type='glossaire',annee=2026,note='Définition ou mission seulement ; paragraphe pertinent relu le 18.10.2026. Année 2026 : consultation, pas date de publication établie.'));urls[url]=i;return i
chuv='https://www.chuv.ch/fr/cardiologie/car-home/patients-et-famille/examens-et-interventions/'
a=source('R-CHUV-TAVI','Implantation de valve aortique',chuv+'cardiologie-interventionnelle/implantation-de-valve-aortique-tavi/','Centre hospitalier universitaire vaudois','CH')
b=source('R-CHUV-DEFIB','Implantation d’un défibrillateur',chuv+'troubles-du-rythme/stimulateur-cardiaque','Centre hospitalier universitaire vaudois','CH')
c=source('R-LAR-VALVULO','Réparation des valves cardiaques','https://www.larousse.fr/encyclopedie/medical/valvuloplastie/16854','Larousse Médical','FR')
d=source('R-LAR-SCIATIQUE','Douleur dans le trajet du nerf de la jambe','https://www.larousse.fr/encyclopedie/medical/sciatique/16011','Larousse Médical','FR')
e=source('R-OFAS-MISSION','Mission de l’administration fédérale des assurances sociales','https://www.bsv.admin.ch/fr/mission-ofas','Confédération suisse','CH')
f=source('R-OFSP-LTX','Législation en médecine de la transplantation','https://www.bag.admin.ch/fr/legislation-medecine-de-la-transplantation','Office fédéral de la santé publique','CH')
rows=[
 ('tavi','TAVI','abreviation',[],'Cette intervention remplace la valve aortique par cathéter.',a,'Présentation de la procédure'),
 ('cardioverter','Cardioverter','terme',['cardioverteur'],'Cet appareil interrompt certains rythmes cardiaques trop rapides.',b,'Implantation d’un défibrillateur'),
 ('valvuloplastie','Valvuloplastie','terme',[],'Cette intervention répare une valve cardiaque malade.',c,'Définition, sans reprise des indications'),
 ('sciatalgie','Sciatalgie','signe',['douleur sciatique'],'Cette douleur irradie le long du nerf sciatique.',d,'Définition initiale seulement, pas le traitement'),
 ('ofas','OFAS','abreviation',['Office fédéral des assurances sociales'],'Cet office fédéral est compétent pour la prévoyance et l’invalidité.',e,'Domaine de compétence'),
 ('ltx','LTx','abreviation',['Loi sur la transplantation'],'Cette loi suisse encadre le don et la greffe.',f,'Base légale et champ, sans règle de consentement'),
 ('cardiopulmonaire','Cardiopulmonaire','terme',['cardio-pulmonaire','cardiopulmonaires','cardio-pulmonaires'],'Cet adjectif concerne le cœur et les poumons.',None,''),
 ('hemodynamiquement','Hémodynamiquement','terme',[],'Ce mot est relatif à la circulation du sang.',None,''),
 ('endothelialisation','Endothélialisation','terme',[],'Des cellules de revêtement couvrent la surface interne du vaisseau.',None,''),
]
p=Path('data/ck/glo.json');glo=json.loads(p.read_text());ids={x['id'] for x in glo}
for i,label,typ,alias,definition,sid,loc in rows:
 if i in ids:continue
 x=dict(id=i,type=typ,label=label,alias=alias,**{'def':definition},statut='sourcé' if sid else 'À vérifier',valide_par_vial=False)
 if sid:x['src']=[dict(id=sid,loc=loc,lu_le='2026-10-18')]
 glo.append(x)
p.write_text(json.dumps(glo,ensure_ascii=False,indent=1)+'\n');S.write_text(json.dumps(src,ensure_ascii=False,indent=1)+'\n')
p=Path('qa/domaines.yml');s=p.read_text();s=s.replace('suisse: [','suisse: [bsv.admin.ch, ') if 'bsv.admin.ch' not in s.split('suisse: [',1)[1].split(']',1)[0] else s;s=s.replace('europe: [','europe: [larousse.fr, ') if 'larousse.fr' not in s.split('europe: [',1)[1].split(']',1)[0] else s;note='# Codex 18.10 : bsv.admin.ch (mission officielle) et larousse.fr (définitions lexicales seules) lus et enregistrés.';s+=('\n'+note+'\n') if note not in s else '';p.write_text(s)

# Année de publication/mise à jour établie, sinon champ omis.
for entry in src:
 if entry['id'] in ['R-CHUV-TAVI','R-CHUV-DEFIB','R-OFAS-MISSION']:
  entry['annee']={'R-CHUV-TAVI':2023,'R-CHUV-DEFIB':2024,'R-OFAS-MISSION':2025}[entry['id']]
  entry['note']='Définition ou mission uniquement ; date affichée par la page, passage relu le 18.10.2026.'
 elif entry['id'] in ['R-LAR-VALVULO','R-LAR-SCIATIQUE','R-OFSP-LTX']:
  entry.pop('annee',None);entry['note']='Définition ou champ uniquement ; passage relu le 18.10.2026, date de publication non établie.'
S.write_text(json.dumps(src,ensure_ascii=False,indent=1)+'\n')
for entry in glo:
 if entry['id']=='sciatalgie':entry['recherche']='On demande au patient de décrire le trajet de la douleur.'
Path('data/ck/glo.json').write_text(json.dumps(glo,ensure_ascii=False,indent=1)+'\n')
