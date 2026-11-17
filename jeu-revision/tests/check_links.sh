#!/usr/bin/env bash
# Vérifie que chaque URL de data/sources.js répond (équivalent léger de lychee).
cd "$(dirname "$0")/.." || exit 1
fail=0
for u in $(grep -o 'url: "[^"]*"' data/sources.js | sed 's/url: "//;s/"$//'); do
  code=$(curl -sL -o /dev/null -w '%{http_code}' -A 'Mozilla/5.0' --max-time 30 "$u")
  echo "$code $u"; [ "$code" = "200" ] || fail=1
done
exit $fail
