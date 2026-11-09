#!/usr/bin/env python3
"""Assemble un HTML de Phase B : police et CSS communs, prose déjà écrite."""
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
CSS = (ROOT / "preuves" / "coquille.css").read_text(encoding="utf-8")


def assembler(corps: str, dx: str, sortie: Path) -> int:
    html = (
        "<!DOCTYPE html>\n<html lang=\"fr\">\n<head>\n<meta charset=\"utf-8\">\n"
        "<meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">\n"
        f"<title>LOT 129 DX.{dx}</title>\n<style>\n{CSS}\n</style>\n</head>\n<body>\n"
        "<main>\n"
        "<p class=\"s\">LOT 129 · S9.13 · Usage non médical de substances et addictions · "
        "contenu établi à partir des sources citées ; non validé cliniquement par un médecin.</p>\n"
        f"{corps.strip()}\n"
        "</main>\n</body>\n</html>\n"
        f"<!-- FIN_FICHIER LOT_129_Phase_B_V0_DX.{dx} -->\n"
    )
    lignes = []
    for ligne in html.splitlines():
        if len(ligne) <= 2400:
            lignes.append(ligne)
            continue
        while len(ligne) > 2400:
            coupure = ligne.rfind(" ", 0, 2400)
            if coupure < 400:
                coupure = 2400
            lignes.append(ligne[:coupure])
            ligne = ligne[coupure:].lstrip()
        if ligne:
            lignes.append(ligne)
    texte = "\n".join(lignes) + "\n"
    sortie.write_text(texte, encoding="utf-8")
    return sortie.stat().st_size


if __name__ == "__main__":
    src, dx, dest = sys.argv[1], sys.argv[2], sys.argv[3]
    n = assembler(Path(src).read_text(encoding="utf-8"), dx, Path(dest))
    print(dest, n)
