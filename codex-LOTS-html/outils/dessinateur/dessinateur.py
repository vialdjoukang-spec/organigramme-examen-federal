#!/usr/bin/env python3
"""Schémas conceptuels expliqués en SVG, jamais présentés comme images de patient.
Usage : python3 -B dessinateur.py specification.json sortie.html
Spécification : vues, formes SVG géométriques contrôlées, repères, définitions.
"""
import importlib.util,json,sys,re
from pathlib import Path
from html import escape as e
spec=importlib.util.spec_from_file_location('illustrer',Path(__file__).resolve().parents[1]/'illustration/illustrer.py')
lib=importlib.util.module_from_spec(spec);spec.loader.exec_module(lib)
ALLOWED={'path':{'d','fill','stroke','stroke-width','stroke-dasharray'},'rect':{'x','y','width','height','fill','stroke','rx'},'ellipse':{'cx','cy','rx','ry','fill','stroke','stroke-width'},'line':{'x1','x2','y1','y2','stroke','stroke-width','stroke-dasharray'}}

def render(s):
    if not re.fullmatch(r'[a-z][a-z0-9-]*',s['id']):raise ValueError('Identifiant invalide')
    for k in ['titre','source_medicale','acces_le','vues','auteur']:
        if not s.get(k):raise ValueError('Manque '+k)
    result=[lib.CSS,f'<figure class="illustration" data-illustration="{s["id"]}" data-dessin-exempte="true"><h3>{e(s["titre"])}</h3><p class="mode">Schémas pédagogiques conceptuels, hors échelle ; aucune image de patient.</p><p>Ouvrez une vue. Les noms apparaissent au survol ou au toucher des numéros ; cliquez pour les définitions.</p>']
    for k,v in enumerate(s['vues']):
        result.append(f'<details {"open" if k==0 else ""}><summary>{e(v["titre"])}</summary><div class="scene"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 720 320" role="img" aria-label="{e(v["titre"])}"><rect width="720" height="320" fill="#f5f9fc"/>')
        for shape in v['formes']:
            tag=shape['tag'];attrs=shape['attrs']
            if tag not in ALLOWED or not set(attrs)<=ALLOWED[tag]:raise ValueError('Forme ou attribut non autorisé')
            if any('url(' in str(x).lower() for x in attrs.values()):raise ValueError('Ressource externe refusée')
            result.append('<'+tag+' '+ ' '.join(f'{key}="{e(str(value))}"' for key,value in attrs.items())+'/>')
        result.append('</svg>')
        defs=[]
        for n,a in enumerate(v['reperes'],1):
            x,y=a['xy']; ident=f'{s["id"]}-v{k}-r{n}'
            result.append(f'<button type="button" class="repere" style="left:{x/720*100:.3f}%;top:{y/320*100:.3f}%" popovertarget="{ident}" aria-label="{n}. {e(a["nom"])}">{n}<span class="nom">{e(a["nom"])}</span></button>')
            defs.append(f'<div id="{ident}" class="definition" popover="manual"><strong>{n}. {e(a["nom"])}</strong><p>{e(a["definition"])}</p><button type="button" popovertarget="{ident}" popovertargetaction="hide">Fermer la définition</button></div>')
        result.append('</div>'+''.join(defs)+'<ol>'+''.join(f'<li><strong>{e(a["nom"])}</strong> : {e(a["definition"])}</li>' for a in v['reperes'])+f'</ol><p><strong>Lecture et pièges :</strong> {e(v["explication"])}</p></details>')
    result.append(f'<figcaption>{e(s["auteur"])}. Schéma original expliqué ; accès documentaire {e(s["acces_le"])}. <a href="{e(s["source_medicale"])}">Source médicale</a>. Les formes sont une simplification pédagogique, sans seuil ni mesure de patient.</figcaption></figure>')
    return ''.join(result)
if __name__=='__main__':
    p=Path(sys.argv[2]);lib.ensure_output(p);p.write_text(render(json.loads(Path(sys.argv[1]).read_text())));print(p)
