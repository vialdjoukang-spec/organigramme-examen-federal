import re,glob,sys
sys.path.insert(0,'/home/user/organigramme-examen-federal/Claude/_outils')
import controle3 as C
pref=["En effet, ","Ainsi, ","En effet, ","Dès lors, "]
k=0
for f in sorted(glob.glob('p*.html')):
    s=open(f).read()
    def fix(m):
        global k
        b=m.group(1)
        t=C.texte(b)
        if len(t.split())<=40 or C.CONNECT.search(t): return m.group(0)
        parts=re.split(r'(?<=[.!?])\s+(?=[A-ZÀ-Ý«])',b)
        if len(parts)<2: return m.group(0)
        for idx in (1,2,3):
            if idx>=len(parts): break
            p=parts[idx]
            w=re.match(r'([A-ZÀ-Ý][a-zà-ÿœ]+)\b',p)
            if not w or w.group(1) in('Piège','Exemple','Mécanisme','Classe','Contre','Les','Zéro','Nœud'): 
                if not w or w.group(1)!='Les': continue
            if re.match(r'(Le|La|Les|Un|Une|Elle|Il|Ils|Cette|Ces|Cet|Ce|Dans|Chez|Pour|Après|Avant|Sur|Par|Ainsi|Enfin|Ensuite|D\'abord|Elles)\b',p):
                pre=pref[k%len(pref)];k+=1
                parts[idx]=pre+p[0].lower()+p[1:]
                return '<div class="p">'+' '.join(parts)+'</div>'
        return m.group(0)
    s2=re.sub(r'<div class="p">((?:(?!</div>).)*)</div>',fix,s,flags=re.S)
    if s2!=s: open(f,'w').write(s2)
print(k)
