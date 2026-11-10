import json
d=json.load(open('controle.json'))[0]
for k,v in d.items():
    if isinstance(v,dict):
        for kk,vv in v.items():
            print('##',kk,vv['n'])
            for x in vv['ex']: print('  -',x)
