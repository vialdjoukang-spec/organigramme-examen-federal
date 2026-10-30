#!/bin/sh
# Installe harnais/hooks/* dans .git/hooks/ en préservant tout hook existant (copie .avant-pons).
set -e
racine=$(git rev-parse --show-toplevel)
for h in "$racine"/harnais/hooks/*; do
  nom=$(basename "$h"); cible="$racine/.git/hooks/$nom"
  if [ -e "$cible" ] && ! cmp -s "$h" "$cible"; then
    cp "$cible" "$cible.avant-pons"
    # chaîne : le hook d'origine reste exécuté en premier
    { echo '#!/bin/sh'; echo "\"$cible.avant-pons\" \"\$@\" || true"; tail -n +2 "$h"; } > "$cible"
    echo "hook $nom : ancien conservé dans $nom.avant-pons et chaîné"
  else
    cp "$h" "$cible"; echo "hook $nom installé"
  fi
  chmod +x "$cible"
done
