#!/bin/bash
# Relance idempotente de tous les LOT en cours (reprise : les leçons finies .fait.json sont sautées) + détective. Capacité : .cache/brain/sonnet_max.
cd "$(dirname "$0")/../.."
for L in 001 002 003 004; do
  [ -d essai_lot$L ] || continue
  cat > /tmp/relance_lot$L.sh <<EOS
#!/bin/bash
cd $PWD
fs=(essai_lot$L/LOT_${L}_Phase_*.html)
for ((i=0; i<\${#fs[@]}; i+=4)); do
  python3 harnais/brain/lancer_parallele.py "\${fs[@]:i:4}" --reprendre --limite-duo 240 --journal essai_lot$L/journal >> /tmp/lot${L}_relance.log 2>&1
done
EOS
  (setsid nohup bash /tmp/relance_lot$L.sh > /dev/null 2>&1 &)
done
(setsid nohup python3 harnais/brain/detective.py --veille 60 > .cache/brain/detective.log 2>&1 &)
