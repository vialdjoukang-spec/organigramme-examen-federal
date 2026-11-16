import re,glob,sys,importlib.util
spec=importlib.util.spec_from_file_location('c3','/home/user/organigramme-examen-federal/Claude/_outils/controle3.py'); C3=importlib.util.module_from_spec(spec); spec.loader.exec_module(C3)
START=re.compile(r"^(le|la|les|l'|un|une|des|il|elle|ils|elles|chaque|ce|cette|ces|cela|la wsES|aucun|aucune|tout|toute|seul|seule|seules|seuls|on|l’)\\b",re.I)
CIT=re.compile(r'\[\[[\w\-|]+\]\]')
def words(s):
    s=CIT.sub('',s); s=re.sub(r'<[^>]+>',' ',s); return len(s.split())
SPL=[(', et ','. '),(', car ','. En effet, '),(', mais ','. Cependant, '),(' ; ','. '),(', tandis que ','. En revanche, '),(', ce qui ','. Cela '),(', puis ','. Ensuite, '),(', alors que ','. En revanche, '),(', parce que ','. En effet, '),(', d\'où ','. D\'où '),(', lorsque ','. Cela vaut lorsque ')]
def cap(s):
    return s
def split_sentence(sent):
    # sent: text without final period, may contain cites at end
    cites=''.join(CIT.findall(sent[-200:])) if CIT.search(sent[-120:]) else ''
    m=re.search(r'((?:\[\[[\w\-|]+\]\])+)$',sent)
    tail=m.group(1) if m else ''
    body=sent[:len(sent)-len(tail)] if tail else sent
    best=None
    n=words(body)
    for sep,rep in SPL:
        for mm in re.finditer(re.escape(sep),body):
            a=body[:mm.start()]; b=body[mm.end():]
            wa,wb=words(a),words(b)
            bt=re.sub(r'<[^>]+>','',b).strip()
            if wa>=9 and wb>=9 and wa<=30 and wb<=32 and (sep==' ; ' or START.match(bt)) and C3.est_verbale(bt):
                score=abs(wa-wb)
                if best is None or score<best[0]: best=(score,a,b,rep)
    if not best: return None
    _,a,b,rep=best
    if rep=='. ': b=b[:1].upper()+b[1:]
    return a+tail+rep+b+tail
def proc(text):
    # protect html tags & breaking: operate on 'blocks' = text between tags that are sentences: simple approach on lines
    out=[]
    def fix_line(line):
        if line.lstrip().startswith(('<h4','<table','<thead','<tr','</')) or '<td>' in line or '<th>' in line: return line
        # split line into sentences on '. ' followed by uppercase/emoji/<
        parts=re.split(r'(?<=\.)\s+(?=[A-ZÀ-Ý«🚩<])',line)
        res=[]
        for p in parts:
            core=p
            # identify the sentence end period
            if words(core)>30 and core.rstrip().endswith('.'):
                body=core.rstrip()[:-1]
                # strip leading tags
                lead=re.match(r'^(\s*(?:<[^>]+>\s*)*)',body).group(1)
                bb=body[len(lead):]
                # trailing tags (</div>, </li>)
                trail=re.search(r'((?:\s*</?[a-z0-9]+[^>]*>)+)$',bb)
                tr=''
                if trail and not CIT.search(trail.group(1)):
                    tr=trail.group(1); bb=bb[:len(bb)-len(tr)]
                r=split_sentence(bb)
                if r:
                    # r ends with tail cites, need final period
                    p=lead+r+'.'+tr
                    if not tr and False: pass
            res.append(p)
        return ' '.join(res)
    return '\n'.join(fix_line(l) for l in text.split('\n'))
for f in sorted(glob.glob('src/p*.txt')):
    t=open(f,encoding='utf-8').read()
    n=proc(t)
    if n!=t:
        open(f,'w',encoding='utf-8').write(n); print('changed',f)
