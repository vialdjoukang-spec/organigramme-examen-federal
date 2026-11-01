"""Trois coupes coronales conceptuelles, originales, sans cliché de patient."""
from pathlib import Path
import importlib.util
import json

D = Path(__file__).resolve().parent
BASE = D.parents[2]
sp = importlib.util.spec_from_file_location('dessinateur', BASE/'outils/dessinateur/dessinateur.py')
draw = importlib.util.module_from_spec(sp)
sp.loader.exec_module(draw)

def f(tag, **a):
    return {'tag':tag, 'attrs':{k.replace('_','-'):v for k,v in a.items()}}

def trait(x1,y1,x2,y2):
    return f('line',x1=x1,y1=y1,x2=x2,y2=y2,stroke='#132d3d',stroke_width=2)

def point(x,y,nom,definition):
    return {'xy':[x,y],'nom':nom,'definition':definition}

def contour(d):
    return [f('path',d=d,fill='none',stroke='#152538',stroke_width=6),
            f('path',d=d,fill='none',stroke='#ffec68',stroke_width=3,stroke_dasharray='7 5')]

orbites=[]
for x in [230,490]:
    orbites += [f('ellipse',cx=x,cy=160,rx=104,ry=116,fill='#e2e7ed',stroke='#718392',stroke_width=3),
                f('ellipse',cx=x,cy=160,rx=92,ry=104,fill='#f4e9bd'),
                f('ellipse',cx=x,cy=160,rx=24,ry=24,fill='#087d8a')]
    orbites += contour(f'M{x-33} 160 a33 33 0 1 0 66 0 a33 33 0 1 0 -66 0')
orbites += [trait(120,60,215,139),trait(600,60,505,139)]

chiasma=[f('ellipse',cx=360,cy=156,rx=250,ry=136,fill='#e5ebf1'),
         f('rect',x=290,y=112,width=140,height=24,fill='#087d8a',rx=9),
         f('ellipse',cx=360,cy=215,rx=43,ry=26,fill='#a883b8')]
chiasma += contour('M280 102 H440 V146 H280 Z')
chiasma += [trait(535,75,417,124),trait(525,260,397,225)]

occiput=[f('path',d='M345 35 C120 15 100 300 345 285 L345 185 L285 160 L345 135 Z',fill='#dde6ee',stroke='#718392',stroke_width=3),
         f('path',d='M375 35 C600 15 620 300 375 285 L375 185 L435 160 L375 135 Z',fill='#dde6ee',stroke='#718392',stroke_width=3),
         f('path',d='M335 110 L335 129 L275 160 L335 191 L335 212',fill='none',stroke='#ce6b2a',stroke_width=14),
         f('path',d='M385 110 L385 129 L445 160 L385 191 L385 212',fill='none',stroke='#ce6b2a',stroke_width=14),
         trait(160,65,306,142),trait(560,65,414,142),trait(230,260,310,160)]

spec={
 'id':'i018-niveaux-visuels',
 'titre':'Voies visuelles : trois niveaux de coupe',
 'auteur':'Codex — schémas originaux, CC BY 4.0 ; aucune figure publiée reproduite',
 'source_medicale':'https://www.cen-neurologie.fr/premier-cycle/les-fondamentaux-de-la-pathologie-neurologique/la-semiologie-neurologique-et-ses-bases-anatomofonctionnelles/chapitre-9-semiologie-des-nerfs-craniens',
 'acces_le':'2026-11-01',
 'vues':[
  {'titre':'1. Niveau orbitaire — en arrière des globes', 'formes':orbites,
   'reperes':[
    point(120,60,'Nerf optique droit','Section du nerf dans l’orbite droite, à gauche du dessin. Il conduit l’information de l’œil droit avant le chiasma.'),
    point(600,60,'Nerf optique gauche','Section du nerf de l’autre œil. Les globes, situés plus en avant, ne sont pas dans cette coupe.')],
   'explication':'Les deux nerfs sont dessinés séparément. Une atteinte préchiasmatique peut produire un déficit monoculaire. La couleur turquoise indique une structure normale, pas un hypersignal inflammatoire.'},
  {'titre':'2. Niveau chiasmatique — région suprasellaire', 'formes':chiasma,
   'reperes':[
    point(535,75,'Chiasma optique','Bande turquoise au-dessus de l’hypophyse. Les fibres des hémirétines nasales y changent de côté ; toutes les fibres ne croisent pas.'),
    point(525,260,'Hypophyse','Repère violet situé sous le chiasma. Aucune masse ni compression n’est représentée.')],
   'explication':'Une atteinte chiasmatique peut altérer les deux champs temporaux. Ce schéma spatial ne représente ni le trajet individuel des fibres ni une imagerie de tumeur.'},
  {'titre':'3. Niveau occipital — berges des sillons calcarins', 'formes':occiput,
   'reperes':[
    point(160,65,'Cortex visuel droit','Berges orange de la face médiale occipitale droite. Ce côté participe à la vision de l’hémichamp gauche des deux yeux.'),
    point(560,65,'Cortex visuel gauche','Berges orange du côté gauche. Une atteinte de ce côté peut donner un déficit homonyme droit.'),
    point(230,260,'Sillon calcarin droit','Enfoncement médial stylisé, entre les deux berges orangées. La disposition réelle des plis varie.')],
   'explication':'Les nerfs optiques ne se prolongent pas directement dans le cortex : les voies postchiasmatiques comportent un relais géniculé puis les radiations, hors de cette coupe. Distinguer perte d’un hémichamp et perte d’un œil.'}
 ]}
(D/'coupes.json').write_text(json.dumps(spec,ensure_ascii=False,indent=2)+'\n')
render=draw.render(spec)
intro='<p><strong>Orientation commune :</strong> coupes frontales vues de face ; droite du patient à gauche du dessin, haut vers le sommet du crâne. Trois positions successives d’avant en arrière, sans distance ni épaisseur mesurée. Les contours pointillés repèrent l’anatomie normale ; ils ne désignent pas des lésions.</p>'
render=render.replace('<details open>',intro+'<details open>',1)
credits=(' <a href="https://www.hug.ch/neuroreeducation/atteinte-champ-visuel">HUG : côté du déficit visuel</a>.'
 ' <a href="https://www.cen-neurologie.fr/premier-cycle/les-fondamentaux-de-la-pathologie-neurologique/notions-fondamentales/chapitre-1-anatomie-descriptive-et-fonctionnelle">CEN : anatomie occipitale</a>.'
 ' <a href="https://creativecommons.org/licenses/by/4.0/">Licence du dessin</a>.')
render=render.replace('</figcaption>',credits+'</figcaption>')
(D/'coupes.html').write_text(render)
print('Trois niveaux et sept repères générés ; inspection visuelle à faire.')
