import os,sys
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
import c1,c2,c3,c4
os.makedirs('fragments',exist_ok=True)
for n in range(1,15):
    m=[c1,c2,c3,c4][0 if n<=3 else 1 if n<=7 else 2 if n<=10 else 3]
    t=getattr(m,f'p{n:02d}')()
    for k in ('</div>','</tr>','</li>','</h4>'): t=t.replace(k,k+'\n')
    open(f'fragments/p{n:02d}.html','w').write(t)
