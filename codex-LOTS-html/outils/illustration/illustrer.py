#!/usr/bin/env python3
"""Annotation reproductible d'une image locale documentée ; aucune image synthétique.
Usage : python3 -B illustrer.py specification.json sortie.html
Les coordonnées sont exprimées dans l'image après éventuel recadrage.
"""
import base64, hashlib, io, json, re, sys
from datetime import date
from html import escape as e
from pathlib import Path
from urllib.parse import urlparse
from PIL import Image
BASE=Path(__file__).resolve().parents[2]
CSS='''<style>.illustration{margin:20px 0;padding:16px;border:1px solid #768795;border-radius:12px;background:#fff;color:#142633}.illustration svg{display:block;width:100%;height:auto}.illustration .scene{position:relative;max-width:760px;margin:auto}.illustration .repere{position:absolute;transform:translate(-50%,-50%);padding:0!important;min-width:30px;min-height:30px;border:2px solid #fff;border-radius:50%;background:#162c48!important;color:#fff!important;font:700 16px system-ui;cursor:pointer}.illustration .nom{display:none;position:absolute;bottom:100%;left:0;padding:5px 8px;min-width:140px;background:#162c48;color:white;font:14px system-ui;z-index:2}.illustration .repere:hover .nom,.illustration .repere:focus .nom{display:block}.illustration .definition{box-sizing:border-box;max-width:min(90vw,550px);max-height:80vh;overflow:auto;padding:12px;border-left:4px solid #087985;margin:8px 0;background:#edf6f7}.illustration summary{cursor:pointer;padding:9px}.illustration figcaption{font-size:14px;margin-top:12px}.illustration p{line-height:1.5}.illustration .mode{font-weight:700;color:#304a64}</style>'''

def validate(s):
    for k in ['id','titre','auteur','licence','licence_url','source_url','acces_le','nature','legende','pieges']:
        if not s.get(k): raise ValueError('Métadonnée manquante : '+k)
    if not re.fullmatch(r'[a-z][a-z0-9-]*',s['id']): raise ValueError('Identifiant invalide')
    if not re.fullmatch(r'CC BY(?:-SA)? (?:[1234]\.0|2\.5)|CC0 1\.0|Domaine public',s['licence']): raise ValueError('Licence refusée')
    source=urlparse(s['source_url'])
    if source.scheme!='https':raise ValueError('Source HTTPS requise')
    host=source.hostname
    if host not in ['commons.wikimedia.org','europepmc.org','www.europepmc.org','openi.nlm.nih.gov']:raise ValueError('Source non autorisée')
    lic=urlparse(s['licence_url'])
    suffix={'Domaine public':'/publicdomain/mark/1.0/','CC0 1.0':'/publicdomain/zero/1.0/'}.get(s['licence'])
    if suffix is None:
        kind,version=s['licence'].rsplit(' ',1); suffix='/licenses/'+kind.replace('CC ','').lower()+'/'+version+'/'
    if lic.scheme!='https' or lic.hostname!='creativecommons.org' or lic.path.rstrip('/')!=suffix.rstrip('/'):raise ValueError('URL de licence incohérente')
    if date.fromisoformat(s['acces_le'])>date.today(): raise ValueError('Date future')
    if not s.get('annotations'):raise ValueError('Annotations absentes')
    if s['nature'] not in ['anatomie normale','image clinique']:raise ValueError('Nature ambiguë')


def ensure_output(p):
    if not p.resolve().is_relative_to(BASE):raise ValueError('Sortie hors périmètre Codex')


def render(spec):
    validate(spec)
    original=(BASE/spec['image']).resolve(); raw=original.read_bytes()
    if hashlib.sha256(raw).hexdigest()!=spec['sha256_original']:raise ValueError('Original modifié')
    im=Image.open(io.BytesIO(raw)).convert('RGB')
    if spec.get('crop'): im=im.crop(tuple(spec['crop']))
    w,h=im.size; stream=io.BytesIO();im.save(stream,format='WEBP',quality=92)
    encoded=base64.b64encode(stream.getvalue()).decode()
    svg=[f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" role="img" aria-label="{e(spec["titre"])}"><image href="data:image/webp;base64,{encoded}" width="{w}" height="{h}"/>']
    buttons=[];defs=[]
    for n,a in enumerate(spec['annotations'],1):
        points=a['contour']
        if len(points)<3 or any(not(0<=x<=w and 0<=y<=h) for x,y in points):raise ValueError('Contour hors image')
        x,y=a['repere']
        if not(0<=x<=w and 0<=y<=h):raise ValueError('Repère hors image')
        poly=' '.join(f'{px},{py}' for px,py in points)
        svg.append(f'<polygon points="{poly}" fill="none" stroke="#152538" stroke-width="3"/><polygon points="{poly}" fill="none" stroke="#ffff68" stroke-width="1.7" stroke-dasharray="4 3"/>')
        buttons.append(f'<button type="button" class="repere" style="left:{x/w*100:.3f}%;top:{y/h*100:.3f}%" popovertarget="{spec["id"]}-def{n}" aria-label="{n}. {e(a["nom"])}">{n}<span class="nom">{e(a["nom"])}</span></button>')
        defs.append(f'<div id="{spec["id"]}-def{n}" popover="manual" class="definition"><strong>{n}. {e(a["nom"])}</strong><p>{e(a["definition"])}</p><button type="button" popovertarget="{spec["id"]}-def{n}" popovertargetaction="hide">Fermer la définition</button></div>')
    svg.append('</svg>')
    caption=f'{spec["auteur"]} — {spec["licence"]} — accès {spec["acces_le"]}. {spec.get("modifications", "Contours et numéros ajoutés.")}'
    return CSS+f'<figure class="illustration" data-illustration="{spec["id"]}"><h3>{e(spec["titre"])}</h3><p class="mode">{e(spec["nature"].capitalize())} — repères explicatifs</p><p>Survolez ou touchez un numéro pour son nom ; cliquez pour sa définition.</p><div class="scene">'+''.join(svg+buttons)+'</div>'+''.join(defs)+'<ol>'+''.join(f'<li><strong>{e(a["nom"])}</strong> : {e(a["definition"])}</li>' for a in spec['annotations'])+f'</ol><p>{e(spec["legende"])}</p><p><strong>Piège :</strong> {e(spec["pieges"])}</p><figcaption>{e(caption)} <a href="{e(spec["source_url"])}">Source</a> · <a href="{e(spec["licence_url"])}">Licence</a> · <a href="{e(spec.get("source_medicale",spec["source_url"]))}">Référence médicale</a></figcaption></figure>'

if __name__=='__main__':
    s=json.loads(Path(sys.argv[1]).read_text());p=Path(sys.argv[2]);ensure_output(p);p.write_text(render(s));print(p)
