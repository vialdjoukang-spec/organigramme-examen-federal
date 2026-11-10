import os,sys
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
import c1,c2,c3,c4,c5
os.makedirs('fragments',exist_ok=True)
for n in range(1,15):
    m=[c1,c2,c3,c4][0 if n<=3 else 1 if n<=7 else 2 if n<=10 else 3]
    t=getattr(m,f'p{n:02d}')()
    if n==8: t=t+c5.p08x()
    if n==9: t=t+c5.p09x()
    if n==10: t=t+c5.p10x()
    if n==11:
        mk='<h4><em>11.C Surveillance'
        t=t.replace(mk,c5.p11x()+mk)
    for k in ('</div>','</tr>','</li>','</h4>'): t=t.replace(k,k+'\n')
    open(f'fragments/p{n:02d}.html','w').write(t)
