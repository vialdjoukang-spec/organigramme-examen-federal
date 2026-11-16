import sys,re
pre,rx=sys.argv[1],sys.argv[2]; w=int(sys.argv[3]) if len(sys.argv)>3 else 600
for l in open('/tmp/claude-0/aips_dx3.txt'):
    m=re.match(r'\[(aips-%s-\d+)\]'%pre,l)
    if not m: continue
    mm=re.search(rx,l,re.I)
    if mm: print(m.group(1),'::',l[max(0,mm.start()-150):mm.start()+w].replace('\n',' '),'\n')
