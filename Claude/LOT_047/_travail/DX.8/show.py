import json,sys,re
P=json.load(open('paquet.json'))['passages']
for p in P:
    if p['id'].split('-')[0] in sys.argv[1:] :
        t=p['texte']
        if re.search(r'\(\d+\)[A-Z]|Conflict of interest|received (speaker|research|consult)|Copyright ©',t): 
            t=re.sub(r'.*?(BACKGROUND|PURPOSE|INTRODUCTION|OBJECTIVE|BACKGROUND:|IMPORTANCE)',r'\1',t,count=1) if re.search(r'BACKGROUND|PURPOSE|INTRODUCTION|OBJECTIVE|IMPORTANCE',t) else ''
            if not t: continue
        print(f"[{p['id']}] {t}")
