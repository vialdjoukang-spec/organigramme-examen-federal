import json,sys,os
s=open('/tmp/claude_c8.json').read()
c=json.loads(s[s.index('['):] if s.lstrip().startswith('[') else s[s.index('{'):])
c=c[0] if isinstance(c,list) else c
print(c['verdict'],c['octets'],c['connecteur%'],c['paragraphes_sans_connecteur'])
d=c['defauts']
only=sys.argv[1:] 
for k in d:
    if only and not any(k.startswith(o) for o in only): continue
    print('##',k,d[k]['n'])
    for x in d[k]['ex']: print('  ',x[:int(os.environ.get('W','260'))])
