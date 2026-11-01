from pathlib import Path
import json,hashlib,datetime
from lxml import html
B=Path(__file__).resolve().parents[2];D=Path(__file__).resolve().parent
controls=[];cs=json.loads((D/'CANDIDATS.json').read_text())['candidats'];assert len(cs)==7
report=html.parse(str(B/'BILAN_IMAGERIE_ECG.html'))
for lot,pmc,n in [(31,'PMC9856561',2),(32,'PMC8509796',3),(33,'PMC8554953',2)]:
 p=B/f'LOT_{lot:03}/illustrations/recherche_web';acc=json.loads((p/(pmc+'-acces.json')).read_text())
 assert hashlib.sha256((p/(pmc+'.xml')).read_bytes()).hexdigest()==acc['sha256']
 assert hashlib.sha256((p/(pmc+'-metadata.json')).read_bytes()).hexdigest()==acc['metadata_sha256']
 acq=json.loads((p/'ACQUISITIONS.json').read_text())['resultats'];assert len(acq)==n
 assert all(not x['acquis'] and not x['integre'] and 'Domaine exclu' in x['erreur'] for x in acq)
 original=next(a for a in json.loads((p/'RECHERCHE.json').read_text())['articles'] if a['pmcid']==pmc)
 for c in [c for c in cs if c['lot']==lot]:
  f=next(f for f in original['figures'] if f['id']==c['id'])
  assert all(f[k]==c[k] for k in ['auteur','licence','licence_url','source_url','legende_source','original_url'])
  assert c['revue_documentaire'] and not c['original_acquis'] and not c['pixels_inspectes']
  text=' '.join(report.xpath('//details[@data-campagne="tri_031_033"]//text()'))
  assert c['titre'] in text and c['auteur'] in text and c['piege'] in text
 controls.append({'lot':lot,'pmcid':pmc,'xml_et_metadonnees_sha256':True,'candidats_documentes':n,'acquisitions_arretees_avant_http':n})
for lot,pmc,decision in [(32,'PMC5647537','exclu_NC_ND'),(33,'PMC7963878','reserve_licence')]:
 p=B/f'LOT_{lot:03}/illustrations/recherche_web';assert not (p/(pmc+'.xml')).exists();assert json.loads((p/(pmc+'-acces.json')).read_text())['droits']['decision']==decision
nav=json.loads((B/'imagerie_20261101/tri_037_040/NAVIGATEUR.json').read_text())
assert nav['sha256_rapport']==hashlib.sha256((B/'BILAN_IMAGERIE_ECG.html').read_bytes()).hexdigest() and len(nav['essais'])==40
r={'date':datetime.datetime.now(datetime.timezone.utc).isoformat(timespec='seconds'),'controles':controls,'exclusion_nc_et_reserve_droits_sans_xml':True,'rapport_final_sha_verifie':True,'validation_clinique':False}
(D/'CONTROLE_SOURCES.json').write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n');print(json.dumps(r,ensure_ascii=False))
