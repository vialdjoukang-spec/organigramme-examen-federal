import re,subprocess,html,glob,sys
sys.path.insert(0,'/home/user/organigramme-examen-federal/Claude/_outils')
out=subprocess.run(['python3','lint.py','conn'],capture_output=True,text=True).stdout.strip().split('\n')
OP=["En outre, ","Par ailleurs, ","Ensuite, ","Enfin, "]
files={f:open(f,encoding='utf-8').read().split('\n') for f in sorted(glob.glob('src/p*.txt'))}
k=0
for l in out:
    if not l.strip(): continue
    num,txt=l.split(' | ',1); f=f'src/p{num}.txt'
    key=html.unescape(txt)[:55]
    L=files[f]
    for idx,ln in enumerate(L):
        clean=re.sub(r'\{\{[^}]*\}\}','',ln); clean=re.sub(r'\(\(([\w-]+)\)\)','',clean)
        if key in clean:
            # split into sentences on '. ' preceding capital
            parts=re.split(r'(?<=\.)\s+(?=[A-ZÀ-Ý«])',ln)
            if len(parts)<2: print('SINGLE',f,key); break
            last=parts[-1]
            if re.match(r'(En outre|Par ailleurs|Ensuite|Enfin|Ainsi|Donc|Cependant|Toutefois|En revanche)',last): break
            w=last.split(' ',1)
            first=w[0]
            if not (len(first)>1 and first[1].isupper()):
                first=first[0].lower()+first[1:]
            parts[-1]=OP[k%4]+first+(' '+w[1] if len(w)>1 else '')
            L[idx]=' '.join(parts); k+=1
            break
    else: print('NOTFOUND',f,key)
for f,L in files.items(): open(f,'w',encoding='utf-8').write('\n'.join(L))
print(k,'ajouts')
