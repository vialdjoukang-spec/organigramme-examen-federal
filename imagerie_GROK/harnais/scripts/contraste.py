#!/usr/bin/env python3
"""contraste.py — ratios WCAG du gabarit de l'interface.

Texte courant : au moins 7:1. Petit libellé (corps < 15 px) : au moins 4,5:1.
Un gris pâle (peu saturé, plus sombre que #F2F4F7) est refusé comme couleur de texte.
CLI : python3 scripts/contraste.py [app_template.html]
Code 1 si un ratio ou un gris pâle échoue.
"""
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MIN_TEXTE = 7.0
MIN_LIBELLE = 4.5
SEUIL_PETIT = 15.0


def _lin(c):
    c = c / 255.0
    return c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4


def lum(h):
    h = h.lstrip("#")
    if len(h) == 3:
        h = "".join(ch * 2 for ch in h)
    r, g, b = int(h[0:2], 16), int(h[2:4], 16), int(h[4:6], 16)
    return 0.2126 * _lin(r) + 0.7152 * _lin(g) + 0.0722 * _lin(b)


def ratio(fg, bg):
    a, b = lum(fg), lum(bg)
    hi, lo = max(a, b), min(a, b)
    return (hi + 0.05) / (lo + 0.05)


def _hex(token):
    token = token.strip().lower()
    if token in ("#fff", "#ffffff"):
        return "#ffffff"
    m = re.fullmatch(r"#([0-9a-f]{6}|[0-9a-f]{3})", token)
    return "#" + m.group(1) if m else None


def variables(css):
    out = {}
    for name, value in re.findall(r"(--[a-z0-9-]+)\s*:\s*([^;}{]+)", css, flags=re.I):
        hx = _hex(value.strip().split()[0])
        if hx:
            out[name.lower()] = hx
    return out


def resolve(value, vars_):
    value = value.strip().split("!")[0].strip()
    hx = _hex(value.split()[0])
    if hx:
        return hx
    m = re.search(r"var\(\s*(--[a-z0-9-]+)\s*\)", value, flags=re.I)
    if m:
        return vars_.get(m.group(1).lower())
    return None


def gris_pale(hx):
    """Peu saturé et plus sombre que #F2F4F7 : le gris pâle interdit pour le texte."""
    h = hx.lstrip("#")
    if len(h) == 3:
        h = "".join(ch * 2 for ch in h)
    r, g, b = int(h[0:2], 16), int(h[2:4], 16), int(h[4:6], 16)
    if max(r, g, b) - min(r, g, b) > 28:
        return False
    return lum("#F2F4F7") - lum(hx) > 0.02 and lum(hx) > 0.04


def regles(css):
    for block in css.split("}"):
        if "{" not in block:
            continue
        sel, body = block.split("{", 1)
        decl = {}
        for part in body.split(";"):
            if ":" not in part:
                continue
            k, v = part.split(":", 1)
            decl[k.strip().lower()] = v.strip()
        yield sel.strip().split("\n")[-1].strip(), decl


def check(path):
    css = open(path, encoding="utf-8").read()
    style = css.split("<style>", 1)[-1].split("</style>", 1)[0]
    vars_ = variables(style)
    erreurs = []
    if lum(vars_.get("--tx", "#000000")) + 1e-6 < lum("#F2F4F7"):
        erreurs.append("--tx plus sombre que #F2F4F7")
    if lum(vars_.get("--mu", "#000000")) + 1e-6 < lum("#F2F4F7"):
        erreurs.append("--mu plus sombre que #F2F4F7")
    for sel, decl in regles(style):
        if sel.startswith("@") or "color" not in decl:
            continue
        fg = resolve(decl["color"], vars_)
        if not fg:
            continue
        if gris_pale(fg):
            erreurs.append(f"gris pâle {fg} dans {sel}")
            continue
        if sel == ".num":
            continue
        bg = None
        for key in ("background-color", "background"):
            if key in decl:
                bg = resolve(decl[key], vars_)
                if bg:
                    break
        fonds = [bg] if bg else [vars_.get("--bg"), vars_.get("--pan"), vars_.get("--pan2"), "#000000"]
        size = 16.0
        m = re.search(r"([\d.]+)\s*px", decl.get("font-size", ""))
        if m:
            size = float(m.group(1))
        plancher = MIN_LIBELLE if size < SEUIL_PETIT else MIN_TEXTE
        pire = min(ratio(fg, fond) for fond in fonds if fond)
        if pire + 1e-6 < plancher:
            erreurs.append(f"{sel} : {fg} contraste {pire:.2f} < {plancher:.1f}")
    # Numéros noirs sur les pastilles vives des quatre rôles.
    for fond in (vars_.get("--c-principale"), vars_.get("--c-associee"), vars_.get("--c-secondaire"), vars_.get("--c-complication")):
        if not fond:
            continue
        r = ratio("#000000", fond)
        if r + 1e-6 < MIN_TEXTE:
            erreurs.append(f"numéro noir sur {fond} : {r:.2f} < {MIN_TEXTE:.1f}")
    return erreurs


def main():
    path = sys.argv[1] if len(sys.argv) > 1 else os.path.join(os.path.dirname(os.path.abspath(__file__)), "app_template.html")
    erreurs = check(path)
    if erreurs:
        print(f"CONTRASTE {path} : {len(erreurs)} écart")
        for e in erreurs:
            print(" -", e)
        return 1
    print(f"CONTRASTE OK {path} : texte ≥ {MIN_TEXTE:.0f}:1, petit libellé ≥ {MIN_LIBELLE:.1f}:1, pas de gris pâle")
    return 0


if __name__ == "__main__":
    sys.exit(main())
