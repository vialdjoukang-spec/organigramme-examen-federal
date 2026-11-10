from pathlib import Path
from html import escape
import re,json,hashlib,shutil
b=Path(__file__).resolve().parent;d=b/'correction_comparatif';d.mkdir(exist_ok=True)
items=[('Une surcharge régionale et de probables microtraumatismes participent au syndrome myofascial.',['s1']),('La pathogenèse reste incomplètement élucidée ; des anomalies de sensibilisation centrale ou de nocicepteurs périphériques concernent certains sous-groupes.',['s1']),('La charge inhabituelle provoque des perturbations ultrastructurales et une réaction locale.',['s47']),('Le choc direct produit une atteinte musculaire accompagnée d’un hématome.',['s12']),('Le tableau infectieux est lié aux virus Influenza ; des complications virales ou bactériennes secondaires sont possibles.',['s5']),('Les manifestations associées aux statines recouvrent des atteintes toxiques ou immunomédiées et des plaintes sans déficit moteur.',['s2','s22']),('Le trouble thyroïdien perturbe le métabolisme et la fonction mitochondriale du muscle.',['s3']),('La maladie comporte une expression inflammatoire des ceintures et reste d’étiologie incertaine.',['s4']),('La destruction des fibres libère leur contenu cellulaire, avec risque rénal et électrolytique.',['s58']),('Une vasculopathie périmysiale et une atrophie périfasciculaire caractérisent l’atteinte décrite.',['s14'])]
source=b/'LOT_083_Phase_A_V0.html';h=source.read_text();start=h.index('<section class="ilot" id="pa-p4">');end=h.index('<section class="ilot" id="pa-p5">',start);original=h[start:end];corrected=original.replace('<th>Piège</th>','<th>Mécanisme et piège</th>');assert corrected!=original
rows=re.findall(r'<tr>.*?</tr>',corrected,re.S);rows=[x for x in rows if '<td>'in x];assert len(rows)==10
trace=[]
for i,(row,(t,refs))in enumerate(zip(rows,items),1):
 cells=re.findall(r'<td>.*?</td>',row,re.S);assert len(cells)==5
 cit=''.join(f'<sup class="r"><a href="#sb-{x}">{x}</a></sup>'for x in refs)
 add=f'<div class="p" id="pa-p4-mecanisme-{i}">{escape(t)}{cit}</div>\n'
 newcell=cells[2].replace('<td>','<td>'+add,1);newrow=row.replace(cells[2],newcell,1);assert corrected.count(row)==1;corrected=corrected.replace(row,newrow,1);trace.append({'dx':i,'ajout':t,'sources':refs})
source=b/'LOT_083_Phase_A_V0.html';h=source.read_text();assert h.count(original)==1
out=h.replace(original,corrected,1);dest=d/source.name;dest.write_text(out)
(d/'p04.html').write_text(corrected)
for x in ['paquet.json','contrat.json']:shutil.copyfile(b/x,d/x)
report={'raison':'Conformité µ1.4 : colonne mécanisme requise, pièges conservés ; dix cellules seules complétées.','sha_avant':hashlib.sha256(source.read_bytes()).hexdigest(),'sha_apres':hashlib.sha256(dest.read_bytes()).hexdigest(),'octets':dest.stat().st_size,'autres_points_identiques':True,'remplacement_entete':['Piège','Mécanisme et piège'],'ajouts':trace}
(d/'CORRECTIONS_COMPARATIF.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n');print(report['octets'],report['sha_apres'])
