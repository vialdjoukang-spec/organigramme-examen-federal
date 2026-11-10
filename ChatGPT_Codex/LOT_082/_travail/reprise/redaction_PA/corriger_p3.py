from pathlib import Path
import json,re,hashlib,html
r=Path(__file__).resolve().parent
lot=r.parents[2]
source=lot/'LOT_082_Phase_A_V0.html'
s=source.read_text()
assert hashlib.sha256(source.read_bytes()).hexdigest()=='5e66d0f7b3deccf4e9325ec53249ce63d6fd32f250c8115572bf0a4b9a326169'
packet=json.loads((r/'paquet_controle.json').read_text())
other=json.loads((r.parent/'redaction_DX7/DX.7/paquet.json').read_text())
new=[]
for x in other['passages']:
    if x['id'] in ['pa17-lomb22-queue','pa17-lomb22-urgence']:
        new.append(dict(x))
for ident in ['s2','s14']:
    x=next(x for x in packet['passages'] if x['id']==ident)
    meta={k:x[k] for k in ['source','url','annee_source','date_publication','date_mise_a_jour','origine_date']}
    new.append({'id':'date-'+ident,'source':'Métadonnées éditoriales vérifiées — '+x['source'],'url':x['url'],'date':'2026-11-10','texte':json.dumps(meta,ensure_ascii=False),'nature':'Métadonnées bibliographiques distinctes de l’extrait clinique.'})
packet['passages']+=new
ids={x['id'] for x in packet['passages']}
changes=[]
def body(items):
    out=[]
    for text,refs in items:
        if isinstance(refs,str):refs=[refs]
        assert set(refs)<=ids
        out.append(html.escape(text)+''.join(f'<sup class="r"><a href="#sb-{x}">{x}</a></sup>' for x in refs))
    return ' '.join(out)
def replace(ident,items):
    global s
    pat=r'(<div class="p" id="'+ident+r'">)(.*?)(</div>)'
    before=re.search(pat,s,re.S);assert before
    after=body(items)
    s,n=re.subn(pat,lambda m:m.group(1)+after+m.group(3),s,flags=re.S);assert n==1
    changes.append({'id':ident,'avant':before.group(2),'apres':after})
replace('pa-p1-fait1',[
 ('Une modification de forme peut traduire un trouble articulaire, osseux ou aponévrotique ; son aspect ne suffit donc pas à nommer sa cause.',['s1','s10','s7']),
 ('Les définitions savantes sont propres aux entités : SRS, rapportée par SOSORT publié en 2018, définit la scoliose par un Cobb d’au moins dix degrés avec rotation axiale.',['s79','date-s79']),
 ('IWGDF 2023 décrit le Charcot comme une atteinte inflammatoire destructrice ostéoarticulaire sur terrain neuropathique ; ces définitions ne constituent pas une définition universelle de toute déformation.',['s11','s34','date-s34'])])
replace('pa-p2-fait8',[("La page HUG sur l’hallux, mise à jour le 16 septembre 2025, décrit cette population par âge sans la limiter à une cohorte suisse ; la publication initiale n’est pas indiquée.",['s2','date-s2'])])
replace('pa-p2-fait11',[("La même page HUG mise à jour en 2025 souligne une prédominance féminine ; ces chiffres ne mesurent pas toutes les déformations articulaires.",['s2','date-s2'])])
replace('pa-p2-fait14',[("La synthèse suisse Paediatrica de 2017 rapporte l’étude historique citée ; sa date de publication n’est pas la date de la cohorte et le chiffre ne constitue pas une fréquence nationale suisse.",['s3','date-s3'])])
replace('pa-p2-fait17',[("La même synthèse suisse de 2017 rapporte la diminution avec la croissance ; une forme flexible indolore conserve donc une signification développementale.",['s3','s4','date-s3'])])
replace('pa-p2-fait18',[("La synthèse pédiatrique de 2017 rapporte aussi une prévalence de 97 % pendant les premières années de vie ; il s’agit d’un chiffre cité dans cette synthèse.",['s3','date-s3'])])
replace('pa-p2-fait29',[("La synthèse suisse publiée en 2023 distingue environ 80 % de scolioses idiopathiques et environ 20 % de formes secondaires.",['s14','date-s14'])])
urgent=[
 ('Une rétention ou incontinence urinaire, une incontinence anale nouvelle ou une anesthésie en selle font rechercher un syndrome de la queue de cheval.','pa17-lomb22-queue'),
 ('Devant ces alarmes ou un déficit moteur, notamment du releveur, obtenir sans attendre une imagerie du rachis, idéalement une IRM, au minimum un scanner si nécessaire, avec avis neurochirurgical.','pa17-lomb22-urgence')]
replace('pa-p5-fait46',urgent)
replace('pa-p9-fait47',[
 ('Les alarmes de queue de cheval ou un déficit moteur imposent imagerie et avis neurochirurgical sans attendre ; elles ne relèvent pas du délai ambulatoire.','pa17-lomb22-urgence'),
 ('En leur absence, la publication pédiatrique décrit l’IRM ambulatoire devant douleur persistante au-delà de six à douze semaines, signes neurologiques peu clairs, courbure atypique ou suspicion de malformation.','s17'),
 ('L’examen couvre la jonction craniocervicale jusqu’au sacrum ; avant chirurgie, une IRM complète est recommandée même sans signe neurologique.','s17')])
replace('pa-p10-fait10',[
 ('Si déficit moteur ou signes de queue de cheval → avis neurochirurgical et imagerie immédiats, idéalement IRM, au minimum scanner si nécessaire.',['pa17-lomb22-urgence','pa17-lomb22-queue']),
 ('Sans ces alarmes, si douleur persistante, anomalie neurologique peu claire ou courbure atypique → bilan spécialisé avec IRM selon indication.','s17'),
 ('Si scoliose confirmée chez un adolescent en croissance → suivi et décision thérapeutique selon courbure et croissance restante.','s14')])
# Identify the source IDs by origin rather than relying on their ordinal positions.
origin={x.get('id_origine_redaction'):x['id'] for x in packet['passages']}
normal=body([
 ('Commencer par les repères comparatifs attendus : peau intacte, perfusion conservée, sensibilité perçue dans les territoires testés et mouvements actifs fonctionnels ; noter séparément chaque constat des deux côtés.',[origin[x] for x in ['oa82-hug-inspection','oa82-hug-mobilite','pa82-radius-neurovasculaire','pa82-main-sensibilite']]),
 ('Une force MRC cinq correspond à une force normale contre forte résistance ; pour les petites articulations, compléter par la fonction de préhension.',origin['oa82-hug-force'])])
s=s.replace('<div class="p" id="pa-p6-fait1">','<div class="p" id="pa-p6-normalite">'+normal+'</div>\n<div class="p" id="pa-p6-fait1">')
changes.append({'id':'pa-p6-normalite','ajout':normal})
replace('pa-p11-fait2',[
 ('Le pied plat physiologique indolore ne nécessite pas de cible de correction de la voûte.','s59'),
 ('Pour le Charcot, consigner température, œdème et imagerie et viser leur évolution compatible avec la rémission ; aucun seuil thermique universel n’est validé.',['s42','s11']),
 ('Pour la scoliose, mesurer le Cobb en degrés et le comparer au suivi en tenant compte de la croissance restante ; ce suivi quantifié ne transforme pas un seuil diagnostique en cible thérapeutique.',['s16','s14'])])
replace('pa-p11-fait29',[
 ('Une insuffisance hépatique sévère, une hépatite aiguë ou une maladie hépatique décompensée active contre-indiquent Dafalgan®.','aips88'),
 ('La maladie de Gilbert et l’hypersensibilité au paracétamol, aux substances apparentées ou aux excipients sont également des contre-indications.','aips88')])
replace('pa-p12-fait1',[
 ('Pour la variante physiologique, aucune prévention primaire de la morphologie par orthèses n’est démontrée : le consensus BSCOS ne retrouve pas de preuve de modification du développement de l’arche ni de prévention à long terme de douleur ou incapacité.','s59'),
 ('Cette limite justifie de ne pas imposer de traitement prophylactique, sans prétendre que l’observation empêche l’apparition d’un pied plat.','s59')])
replace('pa-p12-fait2',[
 ('La synthèse suisse de 2017 décrit l’évolution de la voûte avec la croissance ; reconnaître douleur, rigidité, asymétrie ou signes généraux relève de la détection secondaire.',['s3','s4','s58','date-s3'])])
m=re.search(r'<div class="p" id="pa-p12-fait2">.*?</div>\s*',s,re.S);assert m
block=m.group();s=s[:m.start()]+s[m.end():]
target='<h4>Prévention secondaire : repérer tôt ce qui change la trajectoire</h4>'
assert target in s;s=s.replace(target,target+'\n'+block)
for x in new:
    entry=f'<li id="sb-{x["id"]}">{html.escape(x["source"])} — {html.escape(x["url"])} (consulté le 2026-11-10)</li>'
    s=s.replace('</ol><p class="p">',entry+'\n</ol><p class="p">')
s=re.sub(r'(</(?:td|th|tr|li|div|section|h3|h4|p)>)\s*(?=<)',r'\1\n',s)
dest=r/'correction';dest.mkdir(exist_ok=True)
(dest/source.name).write_text(s)
(dest/'paquet.json').write_text(json.dumps(packet,ensure_ascii=False,indent=2)+'\n')
(dest/'MODIFICATIONS_P3.json').write_text(json.dumps({'audit':'audits/PA_P3_PREMIER.audit.json','avant_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),'apres_sha256':hashlib.sha256(s.encode()).hexdigest(),'corrections':changes,'limite_Q11a':'Pas de seuil inventé ; suivi quantifié explicité seulement.'},ensure_ascii=False,indent=2)+'\n')
print(len(s.encode()),hashlib.sha256(s.encode()).hexdigest())
