#!/usr/bin/env python3
"""Assemble un HTML Phase B : police, CSS, îlots déjà rédigés. Ne rédige aucun texte clinique."""
from __future__ import annotations
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FONT = Path(__file__).resolve().parent / "font_faces.css"

CSS = """
html{hyphens:auto;-webkit-hyphens:auto}
html,body,body *:not(code):not(pre){font-family:"Atkinson Hyperlegible",Verdana,system-ui,sans-serif!important}
body{margin:0;background:#f4f0e8;color:#1c1915;text-align:justify;hyphens:auto;line-height:1.55;font-size:16.5px}
main{max-width:48rem;margin:0 auto;padding:12px}
h2{font-size:1.35rem;line-height:1.3;margin:8px 12px 12px}
h3{font-size:1.08rem;margin:0 0 8px}
h4{font-size:1rem;margin:10px 0 4px}
p{margin:0 0 .7rem}
.ilot{background:#fff;border:1px solid #d5cbbd;border-radius:12px;margin:0 0 12px;padding:12px 14px}
[popover].fenetre{box-sizing:border-box;width:min(94vw,46rem);max-height:86vh;overflow:auto;padding:1rem;border:1px solid #888;border-radius:.5rem;text-align:justify;hyphens:auto;background:#fff}
[popover].fenetre::backdrop{background:rgb(15 23 42 / .55)}
button.fen{font-weight:700;background:none;border:0;border-bottom:1px dotted #6d28d9;color:#4c1d95;padding:0;cursor:pointer}
button.fermer{float:right;margin:0 0 8px 8px}
.defil{overflow-x:auto}
table{border-collapse:collapse;width:100%;font-size:.92rem}
td,th{border:1px solid #cfc6b8;padding:4px 6px;vertical-align:top;text-align:left}
figure{margin:.6rem 0}
svg{width:100%;height:auto;background:#fbfaf7;border:1px solid #ddd}
ol,ul{margin:.3rem 0 .7rem;padding-left:1.2rem}
li{margin:.25rem 0}
.sources{font-size:.92rem}
""".lstrip()


def page(dx: int, nom: str, body: str) -> str:
    font = FONT.read_text(encoding="utf-8")
    return f"""<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>LOT 131 DX.{dx}</title>
<style>
{font}
{CSS}
</style>
</head>
<body>
<main>
<h2>DX.{dx} — {nom}</h2>
<section class="monograph" id="dx{dx}">
{body}
</section>
</main>
</body>
</html>
<!-- FIN_FICHIER LOT_131_Phase_B_V0_DX.{dx} -->
"""


def ecrire(dx: int, nom: str, body: str) -> Path:
    html = page(dx, nom, body)
    # filet : aucune ligne au-delà de 2 800 caractères hors continuations de police déjà coupées
    bad = [i + 1 for i, line in enumerate(html.splitlines()) if len(line) > 3000]
    if bad:
        raise SystemExit(f"lignes trop longues: {bad[:8]}")
    out = ROOT / f"LOT_131_Phase_B_V0_DX.{dx}.html"
    out.write_text(html, encoding="utf-8")
    print(out.name, out.stat().st_size)
    return out


if __name__ == "__main__":
    raise SystemExit("importer ecrire()")
