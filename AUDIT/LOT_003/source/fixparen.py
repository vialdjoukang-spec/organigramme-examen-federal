import sys
p=sys.argv[1]
for i in range(40):
    s=open(p).read()
    try: compile(s,p,'exec'); print('ok after',i); break
    except SyntaxError as e:
        print(e.msg, e.lineno)
        if "unmatched ')'" not in e.msg: break
        L=s.split('\n'); l=L[e.lineno-1]; k=l.rfind(')'); L[e.lineno-1]=l[:k]+l[k+1:]; open(p,'w').write('\n'.join(L))
