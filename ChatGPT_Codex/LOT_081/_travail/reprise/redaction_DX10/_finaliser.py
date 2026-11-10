from pathlib import Path
from html.parser import HTMLParser
from collections import Counter
import re, json, hashlib, subprocess, os

B = Path(__file__).resolve().parent
ROOT = B.parents[3]
F = B / 'LOT_081_Phase_B_V0_DX.10.html'
J = lambda p: json.loads(p.read_text())
def out(name, value):
    (B / name).write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n')
def sha(path): return hashlib.sha256(path.read_bytes()).hexdigest()
h = F.read_text()
questions = re.findall(r'<div class="p" id="dx10-question-finale">.*?</div>', h, re.S)
assert len(questions) == 1
h = h.replace(questions[0], '')
fin = '<p class="p">Le contenu reprend les sources citées ; il n’a pas été validé cliniquement par un médecin.</p>'
assert h.count(fin) == 1
h = h.replace(fin, fin + '\n' + questions[0])
h = re.sub(r'\n*<li id="sb-', '\n<li id="sb-', h)
h = re.sub(r'</li>\n*</ol>', '</li>\n</ol>', h)
F.write_text(h)
out('MANIFESTE.json', {F.name: {'octets': F.stat().st_size, 'sha256': sha(F)}})
env = dict(os.environ, PYTHONDONTWRITEBYTECODE='1')
r = subprocess.run(['python3', str(ROOT/'_outils/controle3.py'), str(F), '--paquet', str(B/'paquet.json'), '--ex', '40'], text=True, capture_output=True, env=env)
assert r.returncode == 0, r.stdout + r.stderr
c = json.loads(r.stdout)
if isinstance(c, list): c = c[0]
out('CONTROLE3.json', c)
class Audit(HTMLParser):
    def __init__(self):
        super().__init__(); self.ids=[]; self.targets=[]; self.windows=[]; self.images=0
    def handle_starttag(self,t,a):
        a=dict(a)
        if a.get('id'): self.ids.append(a['id'])
        if 'popover' in a: self.windows.append(a.get('id'))
        if a.get('popovertarget'): self.targets.append(a['popovertarget'])
        if a.get('href','').startswith('#'): self.targets.append(a['href'][1:])
        if t == 'img': self.images += 1
v=Audit();v.feed(h)
d=[x for x,n in Counter(v.ids).items() if n>1]
m=sorted(set(v.targets)-set(v.ids))
assert not d and not m and not v.images
q='Ce cours, lu seul avec ses fenêtres, suffit-il pour gagner 90 à 100 % des points sur ce sujet et pour traiter ce patient en sécurité ?'
assert h.count(q)==1
out('CONTROLE_LIVRAISON_PRIVE.json', {'fichier':str(F.relative_to(ROOT.parent)), 'octets':F.stat().st_size, 'sha256':sha(F),'ids_total':len(v.ids),'ids_distincts':len(set(v.ids)), 'ids_dupliques':d,'fenetres':len(v.windows),'cibles_absentes':m,'images':v.images,'question_finale_exacte':True,'controle_original':c,'audit_P3':'Recontrôle indépendant requis sur ces octets.'})
rem=J(B/'REMISE.json')
rem.update(octets=F.stat().st_size,sha256=sha(F),sha256_paquet=sha(B/'paquet.json'),statut='Correction ciblée P3 appliquée ; stable pour recontrôle indépendant et poussée par root.')
out('REMISE.json',rem)
rem=J(B/'REMISE_AUDIT.json')
rem.update(octets=F.stat().st_size,sha256=sha(F),controle=c)
rem['points_corriges_P3']={str(n):(B/'fragments'/f'p{n:02d}.html').read_text() for n in [9,11]}
out('REMISE_AUDIT.json',rem)
print(json.dumps({'octets':F.stat().st_size,'sha256':sha(F),'controle':c,'ids_uniques':len(set(v.ids)),'fenetres':len(v.windows)},ensure_ascii=False,indent=2))
