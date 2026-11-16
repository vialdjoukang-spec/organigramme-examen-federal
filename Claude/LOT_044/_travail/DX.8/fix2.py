import re
INS={
'p01':[(0,1,"Ainsi,"),(11,3,"Par ailleurs,"),(12,1,"En effet,")],
'p02':[(11,1,"Ainsi,"),(12,2,"Ainsi,"),(23,2,"Cependant,"),(25,1,"En effet,"),(26,2,"Enfin,"),(30,2,"Enfin,")],
'p03':[(0,2,"Ainsi,"),(2,2,"Ensuite,"),(12,2,"En revanche,"),(13,2,"En outre,"),(17,2,"Ainsi,"),(25,2,"Ensuite,"),(25,3,"Enfin,")],
'p04':[(3,2,"Cependant,"),(17,2,"En outre,"),(18,1,"Ainsi,"),(20,1,"Ainsi,")],
'p05':[(0,1,"En effet,"),(6,1,"Ainsi,"),(8,2,"En outre,")],
'p06':[(2,1,"Par ailleurs,")],
'p07':[(2,2,"En outre,"),(10,2,"Ainsi,"),(12,2,"En outre,"),(19,2,"Par ailleurs,"),(22,2,"Ainsi,"),(26,1,"En effet,"),(28,2,"Par ailleurs,")],
'p08':[(2,2,"En outre,"),(5,1,"Ainsi,"),(19,2,"Enfin,"),(20,2,"En outre,")],
'p09':[(6,1,"Ainsi,"),(6,3,"Cependant,"),(18,1,"Ainsi,"),(18,3,"Par ailleurs,"),(22,1,"En outre,")],
'p10':[(24,1,"Enfin,")],
'p11':[(3,2,"Ainsi,"),(5,1,"Ensuite,"),(17,2,"En outre,"),(18,1,"Par ailleurs,"),(21,1,"Ainsi,"),(21,3,"En effet,"),(27,1,"Ainsi,"),(28,1,"Par ailleurs,"),(30,1,"D'abord,"),(30,2,"Ensuite,"),(30,3,"Enfin,"),(43,1,"Par ailleurs,"),(46,1,"En outre,"),(48,2,"En outre,"),(54,1,"En effet,"),(55,1,"Ensuite,")],
'p12':[(0,1,"Ainsi,"),(3,1,"En outre,"),(6,1,"En effet,"),(8,1,"Ainsi,"),(9,1,"Par ailleurs,"),(11,1,"Ainsi,")],
'p14':[(0,1,"Ainsi,")],
}
ACR=set("ESC ECG IRM AINS CRP HUG ICAP ST PR PET VCI".split())
def apply(f,ins):
    lines=open(f).read().split('\n')
    for li,si,conn in sorted(ins,key=lambda x:(x[0],-x[1])):
        ln=lines[li]; pre,_,body=ln.partition(' ')
        sents=re.split(r'(?<=[.!?])\s+(?=[A-ZÀ-Ý«])',body)
        if si>=len(sents): print('IDX',f,li,si); continue
        s=sents[si]
        first=re.match(r"[\w'’À-ÿ-]+",s)
        w=first.group(0) if first else ''
        if not (w in ACR or (len(w)>1 and w[1:].isupper()) or w.startswith('{{')):
            s=s[0].lower()+s[1:]
        sents[si]=conn+' '+s
        lines[li]=pre+' '+' '.join(sents)
    open(f,'w').write('\n'.join(lines))
for k,v in INS.items(): apply(f'src/{k}.txt',v)
# Q&A raison
s=open('src/p14.txt').read()
for a in ("Raison : de nombreux patients","Raison : cette association","Raison : la dose varie","Raison : dans une série"):
    s=s.replace(a,a.replace("Raison : ","Raison : en effet, "))
open('src/p14.txt','w').write(s)
