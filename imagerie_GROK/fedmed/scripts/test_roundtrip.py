#!/usr/bin/env python3
"""Vérifie que le découpage non modifié restitue le fichier octet pour octet."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import commun as C
import decouper
import reinjecter


def main():
    decouper.decouper()
    texte = reinjecter.reconstruire_brut()
    origine = C.ORIGINAL.read_text(encoding="utf-8")
    if texte == origine:
        print(f"OK octet identique ({len(texte)} caractères)")
        return
    limite = min(len(texte), len(origine))
    for i in range(limite):
        if texte[i] != origine[i]:
            raise SystemExit(
                f"écart à {i} : {texte[max(0,i-40):i+40]!r} || {origine[max(0,i-40):i+40]!r}"
            )
    raise SystemExit(f"longueurs {len(texte)} contre {len(origine)}")


if __name__ == "__main__":
    main()
