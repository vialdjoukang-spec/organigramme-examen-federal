import re,sys
def rs(f,prefix,new):
    t=open(f).read()
    i=t.find(prefix)
    if i<0: print('MISSING',f,prefix[:50]); return
    m=re.compile(r'\.(?=\s|</|$)').search(t,i+len(prefix)-1 if prefix.endswith('.') else i+len(prefix))
    # fin = premier point suivi d'espace/balise après le préfixe (hors "6,1" etc.)
    j=None
    for mm in re.finditer(r'(?<!\d)\.(?=\s|</|$)|(?<=\d)\.(?=\s|</|$)',t[i:]):
        j=i+mm.end(); break
    t=t[:i]+new+t[j:]
    open(f,'w').write(t)
