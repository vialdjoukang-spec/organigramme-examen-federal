import sys,json
p={x['id']:x['texte'] for x in json.load(open('paquet.json'))['passages']}
w=int(sys.argv[1])
for i in sys.argv[2:]: print(f'[{i}]',p[i][:w]); print()
