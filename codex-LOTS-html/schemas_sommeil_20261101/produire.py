"""Ajout ciblé et reproductible de schémas originaux dans deux fenêtres V8."""
import gzip
import hashlib
import importlib.util
import json
import math
import re
import subprocess
import sys
from pathlib import Path

D = Path(__file__).resolve().parent
B = D.parent
R = B.parent
sys.path.insert(0, str(R / 'harnais'))
import taille_xy

def charger(nom, p):
    s = importlib.util.spec_from_file_location(nom, p)
    m = importlib.util.module_from_spec(s)
    s.loader.exec_module(m)
    return m

dessin = charger('dessin_sommeil', B/'outils/dessinateur/dessinateur.py')
HUG = 'https://www.hug.ch/pneumologie/troubles-respiratoires-sommeil'
INSERM = 'https://www.inserm.fr/dossier/apnee-sommeil/'

def courbe(y, couleur, pause=False):
    points = []
    for x in range(140, 661, 2):
        valeur = y if pause and 300 <= x <= 460 else y - 28 * math.sin((x-140)*math.pi/40)
        points.append(f'{x},{valeur:.2f}')
    return {'tag':'path','attrs':{'d':'M'+' L'.join(points),'fill':'none','stroke':couleur,'stroke-width':3}}

def specification():
    vues = []
    for k, titre in enumerate(['Ventilation régulière : repère de lecture', 'Apnée obstructive : efforts persistants', 'Apnée centrale : efforts absents']):
        formes = [courbe(90, '#126098', k>0), courbe(220, '#9b4b08', k==2)]
        formes += [{'tag':'path','attrs':{'d':'M140,285 L660,285 L649,279 M660,285 L649,291','fill':'none','stroke':'#4e5963','stroke-width':2}}]
        reperes = [
            {'xy':[90,90], 'nom':'Débit aérien (courbe bleue)', 'definition':'Lire d’abord le passage de l’air. '+('Les oscillations illustrent une ventilation régulière.' if k==0 else 'Les oscillations illustrent une ventilation ; le segment plat représente ici son interruption.')+' Aucun débit chiffré ni signal réel n’est reproduit.'},
            {'xy':[90,220], 'nom':'Effort respiratoire (courbe brune)', 'definition':'Lire ensuite les mouvements respiratoires. Cette courbe conceptuelle résume les efforts ; elle ne remplace pas les deux signaux thoracique et abdominal d’un enregistrement.'}]
        if k:
            formes += [{'tag':'path','attrs':{'d':'M300,35 L460,35 L460,260 L300,260 Z','fill':'none','stroke':'#be1537','stroke-width':3,'stroke-dasharray':'8 5'}}]
            reperes += [{'xy':[480,40], 'nom':'Intervalle à comparer (pointillés rouges)', 'definition':('Le débit s’interrompt alors que les efforts persistent : mécanisme obstructif illustré.' if k==1 else 'Le débit et les efforts s’interrompent ensemble : mécanisme central illustré.')}]
        explication = 'Le temps va de gauche à droite. Durée, amplitude et fréquence sont arbitraires : ce dessin ne permet ni cotation d’événements ni calcul d’un indice d’apnées-hypopnées. '
        explication += ('La présence de cycles réguliers sur ce dessin ne permet pas d’exclure un trouble du sommeil.' if k==0 else 'Vérifier la qualité des capteurs avant toute conclusion : une perte de signal peut imiter une interruption. La qualification clinique nécessite un enregistrement interprétable et son contexte.')
        vues.append({'titre':titre, 'formes':formes, 'reperes':reperes, 'explication':explication})
    return {'id':'sommeil-signaux','titre':'Débit et effort : reconnaître deux mécanismes', 'source_medicale':HUG, 'acces_le':'2026-11-01', 'auteur':'Codex — dessin pédagogique original, CC BY 4.0', 'vues':vues}

def main():
    assert (B/'_cache/production.lock').exists()
    assert subprocess.check_output(['git','branch','--show-current'],cwd=R,text=True).strip() == 'codex/lots'
    plage = json.loads((R/'IA_RESERVATIONS.json').read_text())['codex']['plage']
    spec = specification()
    fragment = dessin.render(spec)
    fragment = fragment.replace('</figcaption>', f' <a href="{INSERM}">Complément Inserm : mécanismes et enregistrements</a>, consulté le 01.11.2026. <a href="https://creativecommons.org/licenses/by/4.0/">Licence du dessin : CC BY 4.0</a>.</figcaption>')
    # Couleurs explicites dans les surfaces claires, y compris en thème sombre.
    fragment += '<style>.illustration h3,.illustration a,.illustration summary,.illustration .definition{color:#142633}.illustration .definition{margin:auto;inset:10vh auto auto 5vw}.illustration .definition button{min-height:44px}.illustration .repere .nom{max-width:200px}.illustration .scene{scroll-margin-top:80px}</style>'
    (D/'SPECIFICATION.json').write_text(json.dumps(spec,ensure_ascii=False,indent=2)+'\n')
    (D/'SCHEMA.html').write_text(fragment)
    manifeste = []
    for n, original in [(34,'débit, effort'),(40,'débit, mouvements thoraco-abdominaux')]:
        assert plage[0] <= n <= plage[1]
        p = B/f'LOT_{n:03}/LOT_{n:03}_Phase_B_V0_DX.1.html'
        backup = D/(p.name+'.avant.gz')
        if not backup.exists():
            backup.write_bytes(gzip.compress(p.read_bytes(),mtime=0))
        raw = gzip.decompress(backup.read_bytes())
        t = raw.decode()
        assert t.count(original) == 1
        cible = '<button type="button" class="terme" popovertarget="sommeil-signaux-fenetre">'+original+'</button>'
        t = t.replace(original,cible)
        fenetre = '<div id="sommeil-signaux-fenetre" class="fenetre sousf" popover="manual"><div class="barre"><span>Débit et effort respiratoire</span><button type="button" popovertarget="sommeil-signaux-fenetre" popovertargetaction="hide" aria-label="Fermer">✕</button></div><div class="corps">'+fragment+'</div></div>\n'
        t = t.replace('</main>',fenetre+'</main>')
        m = taille_xy.mesurer(t)
        lib = f'Taille : T = {m.x[1]/1000:.1f} Ko (+ {m.y[1]/1000:.1f} Ko) · lecture de la fiche ≈ {round(m.x[0]/180)} min · {m.fen} fenêtres, {m.dep} dépliants'
        t, count = re.subn(r'(<[^>]*id="taille"[^>]*>).*?(</[a-z]+>)',lambda g:g[1]+lib+g[2],t,count=1,flags=re.S)
        assert count == 1 and m.x[1] <= 9000
        p.write_text(t)
        source = {'portee':'Schéma ajouté uniquement ; sources antérieures conservées dans la leçon.', 'images_et_schemas':[{'id':spec['id'], 'nature':'schéma pédagogique original ; aucune image de patient', 'titre':spec['titre'], 'auteur':spec['auteur'], 'licence':'CC BY 4.0','licence_url':'https://creativecommons.org/licenses/by/4.0/', 'date_acces':'2026-11-01', 'source_medicale':HUG, 'source_complementaire':INSERM, 'specification':'../schemas_sommeil_20261101/SPECIFICATION.json', 'rendu':'../schemas_sommeil_20261101/SCHEMA.html', 'sha256_rendu':hashlib.sha256(fragment.encode()).hexdigest(), 'lecon':p.name, 'fenetre':'sommeil-signaux-fenetre', 'validation_humaine':False, 'preuve':'../schemas_sommeil_20261101/REVUE.json'}]}
        (p.parent/'SOURCES.json').write_text(json.dumps(source,ensure_ascii=False,indent=2)+'\n')
        avant = taille_xy.mesurer(raw.decode())
        manifeste.append({'fichier':str(p.relative_to(B)), 'sha256_avant':hashlib.sha256(raw).hexdigest(), 'sha256_apres':hashlib.sha256(t.encode()).hexdigest(), 'octets_avant':len(raw), 'octets_apres':len(t.encode()), 'fiche_octets_avant':avant.x[1], 'fiche_octets_apres':m.x[1], 'fenetres_octets_avant':avant.y[1], 'fenetres_octets_apres':m.y[1]})
    (D/'MODIFICATIONS.json').write_text(json.dumps(manifeste,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(manifeste,ensure_ascii=False))

if __name__=='__main__':main()
