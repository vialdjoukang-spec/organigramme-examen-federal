#!/usr/bin/env python3
"""Contrôles mécaniques ; jamais un audit médical."""
import argparse, hashlib, json, re, time
from html.parser import HTMLParser
from pathlib import Path

VOID = set('area base br col embed hr img input link meta param source track wbr'.split())

class Structure(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.stack, self.errors, self.monographs, self.current = [], [], {}, None
        self.ids, self.targets, self.viewport = set(), [], False
    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag in {'script','iframe','img','link','object','embed','audio','video'}:
            self.errors.append(f'élément interdit ou externe : {tag}')
        if attrs.get('id'):
            if attrs['id'] in self.ids: self.errors.append(f'identifiant dupliqué : {attrs["id"]}')
            self.ids.add(attrs['id'])
        if attrs.get('href','').startswith('#'): self.targets.append(attrs['href'][1:])
        if tag=='meta' and attrs.get('name','').casefold()=='viewport': self.viewport=True
        if 'title' in attrs:
            self.errors.append('attribut title interdit')
        if tag == 'table' and not any(t == 'div' and 'overflow-x' in a.get('style','') for t,a in self.stack):
            self.errors.append('tableau sans enveloppe overflow-x')
        if 'data-monograph' in attrs:
            name = attrs['data-monograph']
            if self.current or name in self.monographs:
                self.errors.append(f'monographie imbriquée ou dupliquée : {name}')
            self.current = name
            self.monographs[name] = {'points':[], 'subpoints':[]}
        if self.current:
            if 'data-point' in attrs: self.monographs[self.current]['points'].append(attrs['data-point'])
            if 'data-subpoint' in attrs: self.monographs[self.current]['subpoints'].append(attrs['data-subpoint'])
        if tag not in VOID: self.stack.append((tag, attrs))
    def handle_startendtag(self, tag, attrs):
        self.handle_starttag(tag, attrs)
        if tag not in VOID: self.handle_endtag(tag)
    def handle_endtag(self, tag):
        if tag in VOID: return
        if not self.stack or self.stack[-1][0] != tag:
            self.errors.append(f'fermeture déséquilibrée : {tag}')
            return
        _, attrs = self.stack.pop()
        if 'data-monograph' in attrs: self.current = None

def check(path, rubric):
    b = path.read_bytes()
    text = b.decode('utf-8')
    p = Structure(); p.feed(text); p.close()
    errors = list(p.errors)
    if p.stack: errors.append('balises non fermées')
    if not p.viewport: errors.append('meta viewport absent')
    if any(t not in p.ids for t in p.targets): errors.append('ancre interne absente')
    if re.search(r'@import\b|url\s*\(',text,re.I): errors.append('ressource CSS externe ou image incorporée interdite')
    if not re.match(r'\s*<!doctype html>', text, re.I): errors.append('DOCTYPE absent')
    if not re.search(r'</html>\s*<!-- FIN_FICHIER [^>]+-->\s*$',text): errors.append('fin HTML ou FIN_FICHIER absent/invalide')
    if not 90000 <= len(b) <= 200000: errors.append(f'taille hors 90–200 Ko : {len(b)} octets')
    if max(map(len,text.splitlines()),default=0)>3000: errors.append('ligne >3000 caractères')
    if not p.monographs: errors.append('aucune monographie identifiée')
    for name,m in p.monographs.items():
        if m['points'] != list(map(str,range(1,15))): errors.append(f'{name} : points 1 à 14 absents, dupliqués ou désordonnés')
        required = ['9.a','9.b','9.c','9.d','11.A','11.B','11.C','11.D']
        if any(m['subpoints'].count(k)!=1 for k in required): errors.append(f'{name} : sous-parties 9/11 incomplètes ou dupliquées')
    if 'non validé cliniquement par un médecin' not in text: errors.append('mention de non-validation absente')
    if not re.search(r'\[S\d+\]',text): errors.append('références numérotées absentes')
    return {'file':str(path),'sha256':hashlib.sha256(b).hexdigest(),'bytes':len(b),
            'structural_pass':not errors,'semantic_validation':False,'errors':errors,
            'monographs':p.monographs,'questions_for_agent':rubric['points'],
            'notice':'Les questions doivent être évaluées sur les preuves ; aucun score clinique automatique.'}

def main():
    a=argparse.ArgumentParser(); a.add_argument('html',type=Path); a.add_argument('--report',type=Path,required=True)
    a.add_argument('--watch',action='store_true'); args=a.parse_args()
    rubric=json.loads((Path(__file__).resolve().parents[1]/'config/rubric.json').read_text())
    old=None; last_error=None
    while True:
        try:
            digest=hashlib.sha256(args.html.read_bytes()).hexdigest()
            if digest!=old:
                r=check(args.html,rubric); args.report.parent.mkdir(parents=True,exist_ok=True)
                tmp=args.report.with_suffix('.tmp'); tmp.write_text(json.dumps(r,ensure_ascii=False,indent=2)); tmp.replace(args.report)
                print(json.dumps({'file':args.html.name,'structural_pass':r['structural_pass'],'errors':len(r['errors']),'sha256':digest}),flush=True)
                old=digest
            if not args.watch: return 0 if r['structural_pass'] else 1
        except (OSError,UnicodeError) as e:
            if not args.watch: raise
            if last_error!=str(e): print(json.dumps({'pending':str(e)}),flush=True)
            last_error=str(e)
        time.sleep(2)

if __name__=='__main__': raise SystemExit(main())
