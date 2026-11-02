#!/bin/bash
# Groupes de 3 leçons, chacune enregistrée (.fait.json) : un redémarrage du conteneur ne perd qu'un groupe. Relancer = --reprendre.
cd /home/user/organigramme-examen-federal
for L in 001 002; do
  fs=(essai_lot$L/LOT_${L}_Phase_*.html)
  for ((i=0; i<${#fs[@]}; i+=3)); do
    python3 harnais/brain/lancer_parallele.py "${fs[@]:i:3}" --reprendre --limite-duo 240 --journal essai_lot$L/journal >> /tmp/claude-0/lot${L}_par.log 2>&1
  done
done
