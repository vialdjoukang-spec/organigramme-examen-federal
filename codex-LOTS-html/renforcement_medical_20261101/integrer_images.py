"""Intégration ciblée des deux paires réelles, après revue des agents."""
import gzip
import hashlib
import json
import re
import sys
from pathlib import Path

D=Path(__file__).resolve().parent
B=D.parent
sys.path.insert(0,str(B.parent/'harnais'))
import taille_xy

def main():
    assert (B/'_cache/production.lock').exists()
    rows=[]
    for n,anchor,fragment,term,context,warning in [
        (18,'a-explorations','images_ophtalmo/fragments/erdes-membrane-retinienne.html','membrane échogène intravitréenne',
         'À l’échographie oculaire, une {button} est un signe à décrire et à confronter aux attaches, à la dynamique et au contexte. L’exemple permet de comparer le cliché original à son annotation.',
         '<p><strong>Sécurité :</strong> en cas de suspicion de traumatisme à globe ouvert, l’échographie oculaire est contre-indiquée. Cet exemple pédagogique ne modifie pas la priorité de l’avis ophtalmologique urgent.<sup class="s"><a href="#s33">33</a></sup></p>'),
        (29,'a-detail9','images_neuropediatrie/certas_14-fragment.html','repérage du matériel de dérivation',
         'Chez un patient déjà porteur d’une dérivation, le {button} est distinct de l’étude des ventricules. Le cliché présenté ne permet pas de conclure au fonctionnement du système.',
         '<p><strong>Contexte limité :</strong> patient déjà porteur d’une dérivation. Cette image de matériel ne montre ni une dilatation ventriculaire ni un élargissement des espaces sous-arachnoïdiens ; elle ne justifie pas une radiographie initiale de toute macrocéphalie.</p>')]:
        p=B/f'LOT_{n:03}/LOT_{n:03}_Phase_A_V0.html'
        backup=D/(p.name+'.avant_images.gz')
        if not backup.exists():backup.write_bytes(gzip.compress(p.read_bytes(),mtime=0))
        raw=gzip.decompress(backup.read_bytes());t=raw.decode();frag=(D/fragment).read_text()
        ident=f'image-reelle-{n:03}'
        button=f'<button type="button" class="terme" popovertarget="{ident}">{term}</button>'
        target=t.index(f'id="{anchor}"');start=t.index('<div class="corps">',target)+len('<div class="corps">')
        t=t[:start]+'<p>'+context.format(button=button)+'</p>'+t[start:]
        popup=f'<div id="{ident}" class="fenetre sousf" popover="manual"><div class="barre"><span>{term.capitalize()}</span><button type="button" popovertarget="{ident}" popovertargetaction="hide" aria-label="Fermer">✕</button></div><div class="corps">{warning}{frag}</div></div>\n'
        t=t.replace('</main>',popup+'</main>')
        # Les figures historiques restent intactes, correction de contraste hors figures.
        style='<style data-renforcement="contraste-images">.illustration h3,.illustration h4,.illustration figcaption,.illustration .definition{color:#142633}.illustration a{color:#075a84}.illustration .definition{margin:auto;inset:10vh auto auto 5vw}.illustration .scene{scroll-margin-top:80px}</style>'
        t=t.replace('</head>',style+'</head>')
        p.write_text(t);taille_xy.main([str(p),'--inscrire'])
        sourcefile=B/f'LOT_{n:03}/SOURCES.json'
        source=json.loads(sourcefile.read_text()) if sourcefile.exists() else {'portee':'Images nouvelles ; bibliographies cliniques conservées dans les leçons.','images_et_schemas':[]}
        specification=D/('images_ophtalmo/specification_erdes.json' if n==18 else 'images_neuropediatrie/certas_14-spec.json')
        spec=json.loads(specification.read_text())
        source['images_et_schemas']=[x for x in source['images_et_schemas'] if x.get('id')!=spec['id']]
        source['images_et_schemas'].append({'id':spec['id'],'titre':spec['titre'],'nature':spec['nature'],'auteur':spec['auteur'],'licence':spec['licence'],'licence_url':spec['licence_url'],'source_url':spec['source_url'],'date_acces':spec['acces_le'],'sha256_original':spec['sha256_original'],'fenetre':ident,'lecon':p.name,'specification':str(specification.relative_to(B)),'preuve':str((D/fragment).relative_to(B)),'revue_visuelle_interne':True,'validation_clinique_humaine':False})
        sourcefile.write_text(json.dumps(source,ensure_ascii=False,indent=2)+'\n')
        rows.append({'fichier':str(p.relative_to(B)),'sha256_avant_images':hashlib.sha256(raw).hexdigest(),'sha256_apres_images':hashlib.sha256(p.read_bytes()).hexdigest(),'fenetre_source':anchor,'fenetre_image':ident,'fragment':fragment})
    p=B/'LOT_018/LOT_018_Phase_B_V0_DX.1.html';t=p.read_text()
    if 'data-renforcement="contraste-images"' not in t:
        t=t.replace('</head>',style+'</head>');p.write_text(t)
    p=B/'LOT_029/LOT_029_Phase_B_V0_DX.1.html';t=p.read_text();old='une discordance développementale ou de trajectoire stable appelle un bilan adapté';new='chez un enfant cliniquement stable, une discordance développementale ou de trajectoire appelle un bilan adapté'
    assert old in t or new in t
    if old in t:t=t.replace(old,new);p.write_text(t);taille_xy.main([str(p),'--inscrire'])
    (D/'INTEGRATION_IMAGES.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n')
if __name__=='__main__':main()
