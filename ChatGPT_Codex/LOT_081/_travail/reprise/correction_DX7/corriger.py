from pathlib import Path
import json,shutil,re
B=Path(__file__).parent; R=B.parent;S=R/'redaction_DX7_9/DX.7'
shutil.copytree(S/'fragments',B/'fragments',dirs_exist_ok=True)
shutil.copy2(S/'contrat.json',B/'contrat.json')
p=json.loads((S/'paquet.json').read_text());ids={x['id'] for x in p['passages']}
for x in json.loads((R/'preparation_infections_onco/COMPLEMENT_GESTES_NEUROLOGIQUES.json').read_text())['passages']+json.loads((R/'redaction_DX7_9/DX.9/COMPLEMENT_EXAMEN.json').read_text()):
 if x['id'] not in ids:p['passages'].append(x);ids.add(x['id'])
(B/'paquet.json').write_text(json.dumps(p,ensure_ascii=False,indent=2)+'\n')
for f in (B/'fragments').glob('p*.html'):
 n=int(f.stem[1:]);s=f.read_text();s=re.sub(r'dx7-w(\d+)',lambda m:f'dx7-p{n}-w{m.group(1)}',s);f.write_text(s)
def p(t,c):return '<div class="p">'+t+''.join('<sup class="r"><a href="#sb-'+i+'">'+i+'</a></sup>' for i in c.split())+'.</div>\n'
def win(n,key,title,rows):
 f=B/'fragments'/f'p{n:02}.html'; ident=f'dx7-p{n}-complement-{key}';block=p('La fenêtre <button class="w" popovertarget="'+ident+'">'+title+'</button> précise donc la recherche clinique','')+'<div id="'+ident+'" popover class="fenetre"><h4>'+title+'</h4>'+''.join(p(t,c) for t,c in rows)+'</div>\n';f.write_text(f.read_text()+block)
win(6,'rot','Percussion tendineuse et réponse attendue',[
('Le relâchement musculaire du patient est nécessaire pour rechercher les réflexes tendineux, qui sont des réflexes myotatiques médullaires monosynaptiques','semiol-uness-relachement'),
('Pour le rotulien, le patient est assis avec les jambes pendantes ; une autre position est couchée, jambe semi-fléchie soutenue par l’examinateur','semiol-cen-rot'),
('La percussion du tendon rotulien provoque une contraction du quadriceps et une extension du genou, ce qui explore l’arc réflexe L4','semiol-cen-rot'),
('Au tendon d’Achille, la percussion déclenche une contraction du triceps sural avec flexion plantaire du pied ; cette réponse correspond au niveau S1','semiol-cen-rot'),
('Pour le bicipital, l’avant-bras est semi-fléchi et en supination ; le pouce placé sur le tendon bicipital reçoit la percussion','semiol-cen-rot'),
('Une contraction du biceps avec flexion du coude constitue alors la réponse attendue de l’arc C5','semiol-cen-rot'),
('Le stylo-radial est recherché sur le bord externe du radius au-dessus de la styloïde, avec l’avant-bras semi-fléchi en position intermédiaire','semiol-cen-rot'),
('La contraction du brachioradial et la flexion du coude caractérisent cette réponse au niveau C6, plutôt qu’une extension du coude','semiol-cen-rot'),
('Pour le tricipital, l’examinateur soutient l’avant-bras semi-fléchi et percute le tendon au-dessus de l’olécrâne ; le triceps se contracte et le coude s’étend','semiol-cen-rot'),
('Cette dernière réponse correspond à C7 ; l’interprétation compare ensuite les résultats aux autres territoires déjà examinés','semiol-cen-rot neuro-ao-reflexes'),
('Des réflexes constitutionnellement faibles ou absents existent, donc leur absence isolée ne démontre pas automatiquement une lésion acquise','semiol-cen-variation-normale')])
win(6,'plantaire','Réponse plantaire normale puis signe de Babinski',[
('Une stimulation non douloureuse parcourt le bord externe de la plante, depuis l’arrière vers l’avant ; la réponse normale est une flexion du gros orteil','semiol-cen-plantaire'),
('Les autres orteils peuvent aussi fléchir, tandis qu’une extension lente du gros orteil définit le signe de Babinski','semiol-cen-plantaire'),
('Un écartement des autres orteils accompagne parfois cette extension ; le signe s’intègre donc à la recherche d’une atteinte pyramidale','semiol-cen-plantaire semiol-cen-essentiel')])
win(6,'clonus','Étirement de cheville et clonus',[
('L’examinateur imprime au pied une dorsiflexion brusque puis maintient cette position, afin de rechercher un clonus de cheville','semiol-cen-clonus'),
('Le signe est une succession rythmée de brèves flexions et extensions, typiquement inépuisables ; il traduit une exagération du réflexe myotatique','semiol-cen-clonus'),
('Cette hyperréactivité appartient à la spasticité, donc son interprétation rejoint celle du tonus et des autres signes pyramidaux','semiol-cen-clonus')])
win(7,'spasticite','Hypertonie pyramidale et manœuvre passive',[
('La spasticité est l’hypertonie pyramidale, décrite comme élastique par le Collège des enseignants de neurologie ; elle augmente à l’action','semiol-cen-essentiel'),
('Son examen évalue la résistance à la mobilisation passive des segments de membre, d’abord à vitesse moyenne puis à grande vitesse','semiol-cen-tonus'),
('L’étude du ballant mobilise alternativement le segment proximal pour observer l’articulation distale, ce qui complète l’appréciation du tonus','semiol-cen-tonus'),
('Dans la compression médullaire, ces anomalies se combinent aux déficits sous-lésionnels ; elles ne constituent donc pas une preuve isolée de métastase','neuro-cofer-medullaire')])
win(7,'diffusion','Réflexes vifs, diffusés et polycinétiques',[
('Une réponse réflexe vive appartient à l’hyperréflexie, tandis que la diffusion correspond à une extension de la zone réflexogène','semiol-cen-pyramidal semiol-cen-essentiel'),
('Le polycinétisme désigne plusieurs réponses motrices successives ; leur répétition peut ainsi produire un clonus du pied ou de la rotule','semiol-cen-clonus'),
('La dorsiflexion brusque maintenue recherche le clonus du pied, donc une série de flexions-extensions rythmiques après cet étirement soutient la spasticité','semiol-cen-clonus'),
('La spasticité et l’hyperréflexie traduisent une exagération du réflexe myotatique, ce qui relie ces anomalies à un même mécanisme','semiol-cen-clonus'),
('Une lésion aiguë étendue peut au contraire entraîner une aréflexie ; l’absence initiale de réflexes vifs ne suffit donc pas à exclure l’atteinte pyramidale','semiol-cen-pyramidal')])
win(7,'babinski','Extension plantaire pathologique',[
('Le Babinski correspond à une extension lente du gros orteil après stimulation non douloureuse du bord externe de la plante, conduite d’arrière en avant','semiol-cen-plantaire'),
('La flexion du gros orteil constitue la réponse normale, tandis que son extension s’associe parfois à l’écartement des autres orteils','semiol-cen-plantaire'),
('Dans ce syndrome, cette réponse pathologique est recherchée avec le déficit moteur et la spasticité, afin de reconnaître une atteinte des voies pyramidales','semiol-cen-essentiel neuro-cofer-medullaire')])
(B/'MODIFICATIONS.json').write_text(json.dumps({'role':'Correcteur ciblé ; aucune autoévaluation','modifications':['IDs des fenêtres préfixés par numéro de point avec cibles actualisées.','Point6 : gestes ROT membres supérieurs/inférieurs, réponses attendues et variante constitutionnelle ; plantaire, Babinski et clonus.','Point7 : spasticité, tonus passif, diffusion, polycinétisme, mécanisme myotatique et définition/recherche Babinski.','Question finale exacte et retours entre blocs ajoutés après assemblage.'],'limites_non_modifiees':['Épidémiologie suisse non représentative : aucun dénominateur créé.','Composantes/seuils SINS non acquis : aucun score inventé.','Doses de compression urgente non transposées depuis palliation ou œdème cérébral.','Prévention primaire spécifique de la métastase non enrichie sans preuve.']},ensure_ascii=False,indent=2)+'\n')
