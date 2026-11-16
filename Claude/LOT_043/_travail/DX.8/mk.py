import re,glob,os
for f in sorted(glob.glob('t/p*.txt')):
    out=[]
    for l in open(f,encoding='utf8').read().split('\n'):
        l=l.rstrip()
        if not l: continue
        if l.startswith('P:'): l='<div class="p">'+l[2:].strip()+'</div>'
        elif l.startswith('- '): l='\x00<li>'+l[2:].strip()+'</li>'
        l=re.sub(r'\{([^}]+)\}',lambda m:''.join(f'<sup class="r"><a href="#sb-{i.strip()}">{i.strip()}</a></sup>' for i in m.group(1).split(',')),l)
        l=re.sub(r'([.!?])((?:<sup class="r">.*?</sup>)+)',lambda m:m.group(2)+m.group(1),l)
        out.append(l)
    # wrap consecutive li
    s='\n'.join(out); s=re.sub(r'((?:\x00<li>.*</li>\n?)+)',lambda m:'<ul>'+m.group(1).strip().replace('\x00','')+'</ul>\n',s)
    open('fragments/'+os.path.basename(f).replace('.txt','.html'),'w',encoding='utf8').write(s+'\n')
