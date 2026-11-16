#!/bin/bash
cd /home/user/wt/lot-044/Claude/LOT_044/_travail/DX.4
python3 expand.py
S=/tmp/claude-0/-home-user/15c9849e-78d1-5a00-9dcf-bd21b180736d/scratchpad
( for f in fragments/p*.html; do echo "<section id=\"dx4-$(basename $f .html)\">"; cat $f; echo "</section>"; done; echo "<!-- FIN_FICHIER x -->" ) > /tmp/dx4test.html
python3 $S/ref/outils/controle3.py /tmp/dx4test.html --paquet paquet.json --points 0 --min 0 --ex 12 | python3 -c "
import json,sys
r=json.load(sys.stdin)[0]
print(r['verdict'],r['octets'],r['connecteur%'],r['paragraphes_sans_connecteur'])
for k,v in r['defauts'].items():
  print(k,v['n'])
  for e in v['ex']: print('   ',e)"
