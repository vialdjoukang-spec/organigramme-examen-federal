import re,sys
pat=re.compile(sys.argv[1],re.I); w=int(sys.argv[2]) if len(sys.argv)>2 else 220; mx=int(sys.argv[3]) if len(sys.argv)>3 else 12
only=sys.argv[4] if len(sys.argv)>4 else ''
n=0
for l in open('/home/user/wt/lot-053/Claude/LOT_053/_travail/DX.7/dump.txt'):
    i=l.split(']')[0][1:]
    if only and not i.startswith(only): continue
    for m in pat.finditer(l):
        print('[%s] ...%s'%(i,l[max(0,m.start()-w):m.end()+w].replace('\n',' ')));n+=1
        break
    if n>=mx:break
