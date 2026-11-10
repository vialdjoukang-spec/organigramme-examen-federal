#!/bin/bash
# finaliser_lot.sh LOT : HELP du LOT (concaténation des HELP de cibles), MANIFESTE, controle3 des 11 fichiers ensemble (P2/P4)
set -e
L=$1; cd /home/user/wt/lot-$L; D=Claude/LOT_$L; O=/home/user/organigramme-examen-federal/Claude/_outils
{ echo "# HELP — LOT_$L (lacunes de sources, hors du cours ; concaténation des HELP de cibles)"; for c in PA DX.1 DX.2 DX.3 DX.4 DX.5 DX.6 DX.7 DX.8 DX.9 DX.10; do f=$D/_travail/$c/HELP.md; [ -f $f ] && { echo; echo "## $c"; sed '1{/^# /d}' $f; }; done; } > $D/HELP.md
python3 $O/lecon.py manifeste --lot $L
python3 $O/controle3.py $D/LOT_${L}_Phase_*.html --ex 2 > $D/_travail/controle_lot.json || true
python3 - "$D" <<'P'
import json,sys,glob,re,os
d=sys.argv[1]; R=json.load(open(d+'/_travail/controle_lot.json'))
liste=[l.split(' — ',1)[1].split(' 🚩')[0].strip() for l in open(d+'/LISTE_DX_CANONIQUE.md') if l.startswith('DX.')]
ok=True
for r in R:
    m=re.search(r'DX\.(\d+)',r['fichier']); h=open(r['fichier']).read()
    if m:
        i=int(m.group(1)); t=re.search(r'<h2>(.*?)</h2>',h).group(1)
        import html; t=html.unescape(t)
        if t!=f'DX.{i} — {liste[i-1]}': ok=False; print('INCOHÉRENCE A↔B', r['fichier'], t)
    print(os.path.basename(r['fichier']), r['verdict'], r['octets'], r['connecteur%'], {k:v['n'] for k,v in r['defauts'].items()})
print('cohérence A↔B :', 'OK' if ok else 'ÉCHEC')
P
