#!/bin/sh
# Lance la suite de tests (aucun accès réseau, aucun vrai LOT).
cd "$(dirname "$0")/common" && exec python3 -m unittest discover -s tests -v "$@"
