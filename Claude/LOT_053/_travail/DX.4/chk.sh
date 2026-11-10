#!/bin/bash
cd /home/user/wt/lot-053/Claude/LOT_053/_travail/DX.4
python3 build.py
( echo '<html><body>'; for f in fragments/p*.html; do echo "<section id=\"dx4-$(basename $f .html)\">"; cat $f; echo '</section>'; done; echo '</body></html><!-- FIN_FICHIER -->' ) > /tmp/claude-0/test.html
python3 /home/user/organigramme-examen-federal/Claude/_outils/controle3.py /tmp/claude-0/test.html --paquet paquet.json --points 0 --min 0 --max 999999 --ex ${1:-4} | python3 -c "
import json,sys
r=json.load(sys.stdin)[0]
print(r['verdict'],r['octets'],r['connecteur%'],r['paragraphes_sans_connecteur'])
for k,v in r['defauts'].items():
    print('##',k,v['n'])
    for e in v['ex']: print('   ',e)
"
