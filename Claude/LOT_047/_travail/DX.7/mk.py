import re,os,sys
A={'RMS':'w1607b0-2','RMS11a':'wce725d-1','RMS11b':'wce725d-2','VD':'wd84e9e-4','VD3':'wd84e9e-3','SD13':'w026e83-4','SD13b':'w026e83-3',
'IMP':'wef180c-3','IMP4':'wef180c-4','IMP2':'wef180c-2','DIL':'w228bc3-4','DIL5':'w228bc3-5','SW6':'w965fff-6','SW7':'w965fff-7','SW4':'w965fff-4','SW5':'w965fff-5',
'DUP5':'wd2b321-5','DUP6':'wd2b321-6','DUP7':'wd2b321-7','DUP8':'wd2b321-8','MAI8':'w6aa848-8','MAI7':'w6aa848-7','MAI9':'w6aa848-9','OLE6':'w24c24f-6','OLE7':'w24c24f-7','OLE8':'w24c24f-8',
'PPI3':'wce3894-3','PPI4':'wce3894-4','PPI5':'wce3894-5','PPI6':'wce3894-6','DIET3':'wc09c23-3','DIET4':'wc09c23-4','ROB3':'w21134e-3','ARI3':'w13e0bd-3','ARI4':'w13e0bd-4',
'SHA4':'w52ed20-4','SHA5':'w52ed20-5','STC5':'w2e4534-5','STC6':'w2e4534-6','DSR5':'w7019a0-5','DSR6':'w7019a0-6','NMA9':'w580707-9','NMA10':'w580707-10','NMA11':'w580707-11',
'OIT':'waecd2e-6','BOS6':'we1fcb7-6','BOS7':'we1fcb7-7','AIPS1':'aips-62581-1','AIPS4':'aips-62581-4','AIPS34':'aips-62581-34','AIPS35':'aips-62581-35','AIPS8':'aips-62581-8',
'ROB4':'w21134e-4','G1':'w922e9d-1','G9':'w922e9d-9','G10':'w922e9d-10','G11':'w922e9d-11','G12':'w922e9d-12','UNI':'w918a70-2','UNI6':'w918a70-6'}
PRE={'u':'w3bd653-','m':'w79d85d-','r':'w2356b3-','p':'w4d05c5-','s':'w803d0d-','n':'w5c3b07-','a':'w527026-'}
def ident(t):
    if t in A: return A[t]
    if re.fullmatch(r'w[0-9a-f]{6}-\d+',t) or t.startswith('aips-'): return t
    m=re.fullmatch(r'([umrpsna])(\d+)',t)
    if m: return PRE[m.group(1)]+m.group(2)
    raise SystemExit('alias inconnu '+t)
def sub(m):
    return ''.join(f'<sup class="r"><a href="#sb-{ident(t)}">{ident(t)}</a></sup>' for t in m.group(1).split())
for n in range(1,15):
    f=f'src/p{n:02d}.txt'
    if not os.path.exists(f): continue
    s=open(f).read()
    s=re.sub(r'\[\[([^\]]+)\]\]',sub,s)
    open(f'fragments/p{n:02d}.html','w').write(s)
