#!/usr/bin/env python3
"""Dessinateur : fragment HTML/SVG interactif, autonome, sans réseau.

Entrée : description JSON (niveaux, structures, lésion, question).
Sortie : fragment à insérer dans une fenêtre de LOT, ou une page d'exemple.

  python3 grok-LOTS-html/outils/dessinateur/dessinateur.py rendre DESC.json -o PAGE.html
  python3 grok-LOTS-html/outils/dessinateur/dessinateur.py --autotest

Bibliothèque standard seulement. Police : Atkinson Hyperlegible (SIL OFL),
fichier local, pas de feuille de style distante.
"""
from __future__ import annotations

import argparse
import html
import json
import math
import re
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

ICI = Path(__file__).resolve().parent
EXEMPLE = ICI / "exemples" / "LOT_150" / "dissection_aortique.json"
K = 0.5522847498


class DescriptionInvalide(ValueError):
    pass


def _n(v: float) -> str:
    s = f"{v:.1f}"
    if s.endswith(".0"):
        return s[:-2]
    return s


def ellipse_path(cx: float, cy: float, rx: float, ry: float) -> str:
    return (
        f"M{_n(cx - rx)},{_n(cy)}"
        f"C{_n(cx - rx)},{_n(cy - K * ry)} {_n(cx - K * rx)},{_n(cy - ry)} {_n(cx)},{_n(cy - ry)}"
        f"C{_n(cx + K * rx)},{_n(cy - ry)} {_n(cx + rx)},{_n(cy - K * ry)} {_n(cx + rx)},{_n(cy)}"
        f"C{_n(cx + rx)},{_n(cy + K * ry)} {_n(cx + K * rx)},{_n(cy + ry)} {_n(cx)},{_n(cy + ry)}"
        f"C{_n(cx - K * rx)},{_n(cy + ry)} {_n(cx - rx)},{_n(cy + K * ry)} {_n(cx - rx)},{_n(cy)}Z"
    )


def _ang(cx: float, cy: float, x: float, y: float) -> float:
    return math.degrees(math.atan2(y - cy, x - cx)) % 360


def _pt(cx: float, cy: float, rx: float, ry: float, deg: float) -> tuple[float, float]:
    r = math.radians(deg)
    return cx + rx * math.cos(r), cy + ry * math.sin(r)


def arc_secteur(cx: float, cy: float, rx: float, ry: float, a0: float, a1: float) -> str:
    """Secteur elliptique. 0° = droite de l'écran, 90° = bas, sens horaire."""
    span = (a1 - a0) % 360
    if span == 0:
        span = 360
    large = 1 if span > 180 else 0
    x0, y0 = _pt(cx, cy, rx, ry, a0)
    x1, y1 = _pt(cx, cy, rx, ry, a0 + span)
    return (
        f"M{_n(x0)},{_n(y0)}A{_n(rx)},{_n(ry)} 0 {large} 1 {_n(x1)},{_n(y1)}Z"
    )


def part_verticale(cx, cy, rx, ry, corde, cote: str) -> tuple[str, float, float]:
    """Partage une ellipse par une corde verticale. cote: gauche ou droite (écran)."""
    if not (cx - rx < corde < cx + rx):
        raise DescriptionInvalide(f"corde {corde} hors de l'ellipse")
    t = 1 - ((corde - cx) / rx) ** 2
    dy = ry * math.sqrt(max(t, 0))
    haut = (corde, cy - dy)
    bas = (corde, cy + dy)
    a_haut = _ang(cx, cy, *haut)
    a_bas = _ang(cx, cy, *bas)
    # Cap gauche : de l'angle bas vers l'angle haut en passant par 180°.
    if cote == "gauche":
        a0, a1 = a_bas, a_haut
        if (a_haut - a_bas) % 360 > 180:
            a0, a1 = a_haut, a_bas
        # forcer le passage par la gauche (180°)
        span = (a1 - a0) % 360
        milieu = (a0 + span / 2) % 360
        if not (90 < milieu < 270):
            a0, a1 = a1, a0
    elif cote == "droite":
        a0, a1 = a_haut, a_bas
        span = (a1 - a0) % 360
        milieu = (a0 + span / 2) % 360
        if 90 < milieu < 270:
            a0, a1 = a1, a0
    else:
        raise DescriptionInvalide(f"cote inconnue : {cote}")
    return arc_secteur(cx, cy, rx, ry, a0, a1), haut[1], bas[1]


def croissant(cx, cy, rx, ry, a0, a1, echelle: float) -> str:
    """Anneau partiel (thrombus périphérique)."""
    span = (a1 - a0) % 360 or 360
    large = 1 if span > 180 else 0
    x0, y0 = _pt(cx, cy, rx, ry, a0)
    x1, y1 = _pt(cx, cy, rx, ry, a0 + span)
    irx, iry = rx * echelle, ry * echelle
    ix1, iy1 = _pt(cx, cy, irx, iry, a0 + span)
    ix0, iy0 = _pt(cx, cy, irx, iry, a0)
    return (
        f"M{_n(x0)},{_n(y0)}A{_n(rx)},{_n(ry)} 0 {large} 1 {_n(x1)},{_n(y1)}"
        f"L{_n(ix1)},{_n(iy1)}A{_n(irx)},{_n(iry)} 0 {large} 0 {_n(ix0)},{_n(iy0)}Z"
    )


def geometrie(spec: dict) -> tuple[str, tuple[float, float, float, float], dict]:
    """Retourne d, bbox, attributs de présentation par défaut (surchargeables)."""
    t = spec.get("type")
    extra: dict = {}
    if t == "ellipse":
        cx, cy, rx, ry = (float(spec[k]) for k in ("cx", "cy", "rx", "ry"))
        return ellipse_path(cx, cy, rx, ry), (cx - rx, cy - ry, cx + rx, cy + ry), extra
    if t == "chemin":
        d = spec["d"].strip()
        bb = _bbox_chemin(d)
        return d, bb, extra
    if t == "trait":
        d = spec["d"].strip()
        extra["trait"] = True
        return d, _bbox_chemin(d), extra
    if t == "anneau":
        cx, cy = float(spec["cx"]), float(spec["cy"])
        rx, ry = float(spec["rx"]), float(spec["ry"])
        rix, riy = float(spec["rix"]), float(spec["riy"])
        d = ellipse_path(cx, cy, rx, ry) + ellipse_path(cx, cy, rix, riy)
        extra["evenodd"] = True
        return d, (cx - rx, cy - ry, cx + rx, cy + ry), extra
    if t == "part":
        cx, cy = float(spec["cx"]), float(spec["cy"])
        rx, ry = float(spec["rx"]), float(spec["ry"])
        d, _, _ = part_verticale(cx, cy, rx, ry, float(spec["corde"]), spec["cote"])
        return d, (cx - rx, cy - ry, cx + rx, cy + ry), extra
    if t == "secteur":
        cx, cy = float(spec["cx"]), float(spec["cy"])
        rx, ry = float(spec["rx"]), float(spec["ry"])
        d = arc_secteur(cx, cy, rx, ry, float(spec["a0"]), float(spec["a1"]))
        return d, (cx - rx, cy - ry, cx + rx, cy + ry), extra
    if t == "croissant":
        cx, cy = float(spec["cx"]), float(spec["cy"])
        rx, ry = float(spec["rx"]), float(spec["ry"])
        d = croissant(cx, cy, rx, ry, float(spec["a0"]), float(spec["a1"]), float(spec.get("echelle", 0.62)))
        return d, (cx - rx, cy - ry, cx + rx, cy + ry), extra
    if t == "vertebre":
        cx, cy = float(spec["cx"]), float(spec["cy"])
        rx, ry = float(spec["rx"]), float(spec["ry"])
        d = ellipse_path(cx, cy, rx, ry)
        d += f"M{_n(cx - rx * 0.22)},{_n(cy + ry * 0.72)}L{_n(cx)},{_n(cy + ry + 48)}L{_n(cx + rx * 0.22)},{_n(cy + ry * 0.72)}Z"
        return d, (cx - rx, cy - ry, cx + rx, cy + ry + 48), extra
    raise DescriptionInvalide(f"géométrie inconnue : {t}")


_TOKEN = re.compile(r"[MmLlHhVvCcQqZz]|[-+]?(?:\d+\.?\d*|\.\d+)(?:[eE][-+]?\d+)?")


def _bbox_chemin(d: str) -> tuple[float, float, float, float]:
    tokens = _TOKEN.findall(d)
    i = 0
    cmd = ""
    xs: list[float] = []
    ys: list[float] = []
    cx = cy = 0.0

    def num() -> float:
        nonlocal i
        v = float(tokens[i])
        i += 1
        return v

    while i < len(tokens):
        if tokens[i].isalpha() or tokens[i] in "MmLlHhVvCcQqZz":
            cmd = tokens[i]
            i += 1
            if cmd in "Zz":
                continue
        if cmd in "Mm":
            x, y = num(), num()
            if cmd == "m":
                x, y = cx + x, cy + y
            cx, cy = x, y
            xs.append(x)
            ys.append(y)
            cmd = "L" if cmd == "M" else "l"
        elif cmd in "Ll":
            x, y = num(), num()
            if cmd == "l":
                x, y = cx + x, cy + y
            cx, cy = x, y
            xs.append(x)
            ys.append(y)
        elif cmd in "Hh":
            x = num()
            if cmd == "h":
                x += cx
            cx = x
            xs.append(x)
            ys.append(cy)
        elif cmd in "Vv":
            y = num()
            if cmd == "v":
                y += cy
            cy = y
            xs.append(cx)
            ys.append(y)
        elif cmd in "Cc":
            pts = [num() for _ in range(6)]
            if cmd == "c":
                pts = [pts[0] + cx, pts[1] + cy, pts[2] + cx, pts[3] + cy, pts[4] + cx, pts[5] + cy]
            xs.extend(pts[0::2])
            ys.extend(pts[1::2])
            cx, cy = pts[4], pts[5]
        elif cmd in "Qq":
            pts = [num() for _ in range(4)]
            if cmd == "q":
                pts = [pts[0] + cx, pts[1] + cy, pts[2] + cx, pts[3] + cy]
            xs.extend(pts[0::2])
            ys.extend(pts[1::2])
            cx, cy = pts[2], pts[3]
        elif cmd == "A":
            rx, ry = num(), num()
            num()  # rotation
            num()  # large
            num()  # sweep
            x, y = num(), num()
            xs.extend((cx - rx, cx + rx, x))
            ys.extend((cy - ry, cy + ry, y))
            cx, cy = x, y
        else:
            raise DescriptionInvalide(f"commande de chemin non gérée : {cmd}")
    if not xs:
        raise DescriptionInvalide("chemin vide")
    return min(xs), min(ys), max(xs), max(ys)


def _esc(s: str) -> str:
    return html.escape(s if s is not None else "", quote=True)


def _style_zone(st: dict) -> str:
    fill = st.get("remplissage", "#f4f7f8")
    stroke = st.get("contour", "#1c2428")
    sw = st.get("epaisseur", 1.6)
    return f' fill="{fill}" stroke="{stroke}" stroke-width="{sw}"'


def rendre(desc: dict, police_url: str) -> str:
    if not desc.get("id") or not desc.get("niveaux"):
        raise DescriptionInvalide("id et niveaux sont requis")
    if len(desc["niveaux"]) < 3:
        raise DescriptionInvalide("au moins trois niveaux")
    prefix = re.sub(r"[^a-z0-9-]", "", desc["id"].lower())
    niveaux = desc["niveaux"]
    defaut = next((n["id"] for n in niveaux if n.get("defaut")), niveaux[0]["id"])
    radios = []
    labels = []
    svgs = []
    legs = []
    notes = []
    for niv in niveaux:
        nid = niv["id"]
        if not re.fullmatch(r"[a-z0-9-]+", nid):
            raise DescriptionInvalide(f"id de niveau invalide : {nid}")
        rid = f"{prefix}-{nid}"
        checked = ' checked="checked"' if nid == defaut else ""
        radios.append(
            f'<input class="sr" type="radio" name="{prefix}-niv" id="{rid}"{checked}/>'
        )
        labels.append(f'<label for="{rid}">{_esc(niv["etiquette"])}</label>')
        vx, vy, vw, vh = niv["viewBox"]
        zones = []
        items = []
        vus = set()
        for st in niv["structures"]:
            sid = st["id"]
            if sid in vus:
                raise DescriptionInvalide(f"doublon {sid}")
            vus.add(sid)
            if not st.get("nom"):
                raise DescriptionInvalide(f"{sid} sans nom")
            d, bb, extra = geometrie(st["geometrie"])
            pad = 8 if extra.get("trait") else 2
            if bb[0] < vx - pad or bb[1] < vy - pad or bb[2] > vx + vw + pad or bb[3] > vy + vh + pad:
                raise DescriptionInvalide(f"{nid}/{sid} déborde du viewBox {bb}")
            num = int(st["numero"])
            definition = (st.get("definition") or "").strip()
            titre = st["nom"] if not definition else f"{st['nom']}. {definition}"
            even = ' fill-rule="evenodd"' if extra.get("evenodd") else ""
            trait = extra.get("trait") or st.get("trait")
            if trait:
                forme = (
                    f'<path class="touche" d="{d}" fill="none" stroke="transparent" stroke-width="18"/>'
                    f'<path class="vis" d="{d}" fill="none" stroke="{st.get("contour", "#f7f5f1")}" '
                    f'stroke-width="{st.get("epaisseur", 8)}" stroke-linecap="round"/>'
                )
            else:
                forme = f'<path class="vis" d="{d}"{_style_zone(st)}{even}/>'
            zid = f"{prefix}-{nid}-{sid}"
            zones.append(
                f'<g class="zone" id="{zid}" tabindex="0" role="button" '
                f'data-nom="{_esc(st["nom"])}" data-definition="{_esc(definition)}">'
                f"<title>{_esc(titre)}</title>{forme}</g>"
            )
            items.append((num, f"<li><span>{num}</span> {_esc(st['nom'])}</li>"))
        rep = niv["repere"]
        if rep.get("texte") != "D":
            raise DescriptionInvalide("le repère radiologique doit être « D »")
        rx, ry = float(rep["x"]), float(rep["y"])
        if not (vx <= rx <= vx + vw and vy <= ry <= vy + vh):
            raise DescriptionInvalide(f"repère hors cadre {nid}")
        note = niv.get("note", "")
        svgs.append(
            f'<div class="niv niv-{nid}">'
            f'<div class="cadre">'
            f'<svg viewBox="{vx} {vy} {vw} {vh}" role="img" aria-labelledby="{rid}-titre">'
            f'<title id="{rid}-titre">{_esc(niv["etiquette"])}</title>'
            f"{''.join(zones)}</svg>"
            f'<span class="repere" style="left:{_n(100 * (rx - vx) / vw)}%;top:{_n(100 * (ry - vy) / vh)}%" '
            f'title="{_esc(rep.get("titre", "Droite du patient"))}">D</span>'
            f"</div></div>"
        )
        legs.append(f'<ol class="leg leg-{nid}">{"".join(html_li for _, html_li in sorted(items))}</ol>')
        notes.append(f'<p class="note note-{nid}">{_esc(note)}</p>')
    q = desc["question"]
    sources = desc.get("sources_courtes", "")
    css = _css(prefix, [n["id"] for n in niveaux])
    js = _js()
    return (
        f'<div data-dessinateur="1" id="{prefix}">'
        f"{''.join(radios)}"
        f'<div class="barre" role="tablist">{"".join(labels)}</div>'
        f'<div class="plan">{"".join(svgs)}</div>'
        f'<p class="bulle" hidden="hidden"><strong class="bulle-nom"></strong> '
        f'<span class="bulle-def" hidden="hidden"></span></p>'
        f"{''.join(notes)}{''.join(legs)}"
        f"<details><summary>{_esc(q['intitule'])}</summary>"
        f'<div class="reponse">{q["html"]}</div></details>'
        f'<p class="sources">{sources}</p>'
        f"</div>{css}{js}"
    )


def _css(prefix: str, ids: list[str]) -> str:
    regles = []
    for nid in ids:
        regles.append(
            f"#{prefix}-{nid}:checked~.plan .niv-{nid},"
            f"#{prefix}-{nid}:checked~.leg-{nid},"
            f"#{prefix}-{nid}:checked~.note-{nid}{{display:block}}"
            f"#{prefix}-{nid}:checked~.barre label[for=\"{prefix}-{nid}\"]{{background:#142028;color:#fff}}"
            f"#{prefix}-{nid}:focus~.barre label[for=\"{prefix}-{nid}\"]{{outline:3px solid #ffe14a}}"
        )
    return (
        "<style>"
        f"@{_font_face()}"
        "[data-dessinateur]{--encre:#142028;--papier:#f4f7f8;--filet:#c5d0d6;"
        "position:relative;max-width:920px;margin:0 auto;color:var(--encre);"
        "font:16px/1.4 Atkinson Hyperlegible,Verdana,sans-serif}"
        "[data-dessinateur] .sr{position:absolute;width:1px;height:1px;margin:-1px;padding:0;"
        "overflow:hidden;clip:rect(0 0 0 0);border:0}"
        "[data-dessinateur] .barre{display:flex;flex-wrap:wrap;gap:.4rem;margin:0 0 .6rem}"
        "[data-dessinateur] .barre label{cursor:pointer;border:2px solid var(--encre);"
        "border-radius:999px;padding:.35rem .75rem;background:#fff}"
        "[data-dessinateur] .barre label:focus-within,[data-dessinateur] .sr:focus+label{outline:3px solid #ffe14a}"
        "[data-dessinateur] .niv,[data-dessinateur] .leg,[data-dessinateur] .note{display:none}"
        + "".join(regles) +
        "[data-dessinateur] .cadre{position:relative}"
        "[data-dessinateur] svg{width:100%;height:auto;display:block;background:#e7eef2;border-radius:12px}"
        "[data-dessinateur] .repere{position:absolute;transform:translate(-50%,-50%);"
        "font-weight:700;background:#fff;color:#111;border:2px solid #111;border-radius:6px;"
        "padding:0 .4rem;line-height:1.3;pointer-events:none}"
        "[data-dessinateur] .zone{cursor:pointer;outline:none}"
        "[data-dessinateur] .zone:hover .vis,[data-dessinateur] .zone:focus-visible .vis,"
        "[data-dessinateur] .zone.actif .vis{stroke:#111;stroke-width:3.5px;stroke-dasharray:6 4;"
        "filter:drop-shadow(0 0 1px #fff) drop-shadow(0 0 1px #fff)}"
        "[data-dessinateur] .bulle{margin:.55rem 0 0;padding:.55rem .7rem;background:#142028;color:#fff;"
        "border-radius:8px;overflow-wrap:anywhere}"
        "[data-dessinateur] .bulle[hidden]{display:none}"
        "[data-dessinateur] .bulle-def{display:block;margin-top:.25rem;color:#ffe9a8}"
        "[data-dessinateur] .note{margin:.45rem 0;font-size:.92rem}"
        "[data-dessinateur] .leg{margin:.2rem 0 0;padding:0;list-style:none;columns:2;gap:1rem}"
        "[data-dessinateur] .leg li{break-inside:avoid;margin:0 0 .2rem}"
        "[data-dessinateur] .leg span{display:inline-block;min-width:1.4rem;font-weight:700}"
        "[data-dessinateur] details{margin-top:.8rem;border:2px solid var(--encre);border-radius:10px;"
        "background:#fff}"
        "[data-dessinateur] summary{cursor:pointer;padding:.55rem .7rem;font-weight:700}"
        "[data-dessinateur] .reponse{padding:0 .8rem .7rem}"
        "[data-dessinateur] .reponse p{margin:.4rem 0}"
        "[data-dessinateur] .sources{font-size:.82rem;color:#24343c}"
        "@media (max-width:640px){[data-dessinateur] .leg{columns:1}}"
        "</style>"
    )


def _font_face() -> str:
    return (
        'font-face{font-family:"Atkinson Hyperlegible";font-style:normal;font-weight:400;'
        'font-display:swap;src:url("POLICE") format("truetype")}'
    )


def _js() -> str:
    # Pas de « < » nu : le fragment reste du XML bien formé.
    return (
        "<script>//<![CDATA[\n"
        "(function(){\n"
        "document.querySelectorAll('[data-dessinateur]').forEach(function(racine){\n"
        "var bulle=racine.querySelector('.bulle');\n"
        "var nom=bulle.querySelector('.bulle-nom');\n"
        "var def=bulle.querySelector('.bulle-def');\n"
        "var actif=null;\n"
        "function montrer(z){\n"
        "if(actif)actif.classList.remove('actif');\n"
        "actif=z;\n"
        "if(!z){bulle.setAttribute('hidden','hidden');return;}\n"
        "z.classList.add('actif');\n"
        "nom.textContent=z.getAttribute('data-nom');\n"
        "var t=z.getAttribute('data-definition')||'';\n"
        "def.textContent=t;\n"
        "if(t)def.removeAttribute('hidden');else def.setAttribute('hidden','hidden');\n"
        "bulle.removeAttribute('hidden');\n"
        "}\n"
        "racine.addEventListener('pointerover',function(e){\n"
        "if(e.pointerType==='touch')return;\n"
        "var z=e.target.closest?e.target.closest('.zone'):null;\n"
        "if(z&&racine.contains(z))montrer(z);\n"
        "});\n"
        "racine.addEventListener('pointerout',function(e){\n"
        "if(e.pointerType==='touch')return;\n"
        "var z=e.target.closest?e.target.closest('.zone'):null;\n"
        "if(!z)return;\n"
        "var vers=e.relatedTarget;\n"
        "if(vers&&z.contains(vers))return;\n"
        "montrer(null);\n"
        "});\n"
        "racine.addEventListener('pointerdown',function(e){\n"
        "if(e.pointerType!=='touch')return;\n"
        "var z=e.target.closest?e.target.closest('.zone'):null;\n"
        "if(!z){montrer(null);return;}\n"
        "montrer(z===actif?null:z);\n"
        "});\n"
        "racine.addEventListener('focusin',function(e){\n"
        "var z=e.target.closest?e.target.closest('.zone'):null;\n"
        "if(z)montrer(z);\n"
        "});\n"
        "racine.addEventListener('focusout',function(){montrer(null);});\n"
        "});\n"
        "})();\n"
        "//]]></script>"
    )


def page(fragment: str, titre: str, police_url: str) -> str:
    frag = fragment.replace('url("POLICE")', f'url("{html.escape(police_url, quote=True)}")')
    return (
        "<!DOCTYPE html>\n<html lang=\"fr\">\n<head>\n<meta charset=\"utf-8\"/>\n"
        "<meta name=\"viewport\" content=\"width=device-width, initial-scale=1\"/>\n"
        f"<title>{html.escape(titre)}</title>\n</head>\n<body style=\"margin:0;background:#e7eef2\">\n"
        f"<main style=\"padding:1rem\">\n<h1 style=\"font:600 1.25rem/1.3 Atkinson Hyperlegible,Verdana,sans-serif;"
        f"max-width:920px;margin:0 auto .6rem\">{html.escape(titre)}</h1>\n"
        f"{frag}\n</main>\n</body>\n</html>\n"
    )


def _texte(el: ET.Element) -> str:
    return "".join(el.itertext())


def verifier(fragment: str, desc: dict) -> list[str]:
    """Contrôles structurels. Le rendu visuel se juge sur les captures."""
    erreurs = []
    prefix = re.sub(r"[^a-z0-9-]", "", desc["id"].lower())
    try:
        # Le fragment a plusieurs racines (div + style + script). On emballe.
        emballe = "<wrapper>" + fragment.replace('url("POLICE")', 'url("police.ttf")') + "</wrapper>"
        racine = ET.fromstring(emballe)
    except ET.ParseError as exc:
        return [f"XML invalide : {exc}"]
    if racine.find(".//script") is None:
        erreurs.append("script absent")
    titres = racine.findall(".//title")
    zones = racine.findall(".//g[@class='zone']")
    attendu = sum(len(n["structures"]) for n in desc["niveaux"])
    if len(zones) != attendu:
        erreurs.append(f"{len(zones)} zones pour {attendu} structures")
    noms = set()
    for z in zones:
        nom = z.get("data-nom") or ""
        if not nom:
            erreurs.append("zone sans data-nom")
        titre = next((t.text or "" for t in z.findall("title")), "")
        if nom not in titre:
            erreurs.append(f"title sans le nom : {nom}")
        if z.find("path") is None:
            erreurs.append(f"zone sans path : {nom}")
        if not z.get("tabindex"):
            erreurs.append(f"zone sans focus clavier : {nom}")
        noms.add(nom)
    for niv in desc["niveaux"]:
        nums = sorted(int(st["numero"]) for st in niv["structures"])
        if nums != list(range(1, len(nums) + 1)):
            erreurs.append(f"numéros non continus : {niv['id']} {nums}")
    if "D" not in _texte(racine):
        erreurs.append("repère D absent")
    checks = [i for i in racine.findall(".//input") if i.get("checked")]
    if len(checks) != 1:
        erreurs.append(f"{len(checks)} niveaux cochés")
    details = racine.find(".//details")
    if details is None or "faux chenal" not in _texte(details).lower():
        erreurs.append("question absente")
    reponse = _texte(details) if details is not None else ""
    for marque in ("2014", "2020", "2022", "Radiopaedia"):
        if marque not in reponse:
            erreurs.append(f"source manquante dans la question : {marque}")
    brut = ET.tostring(racine, encoding="unicode")
    if re.search(r"""(?:src|href)\s*=\s*["']https?:""", fragment):
        # Les liens de citation sont dans le paragraphe sources : autorisés.
        hors = re.sub(r"<p class=\"sources\">.*?</p>", "", fragment, flags=re.S)
        if re.search(r"""(?:src|href)\s*=\s*["']https?:""", hors):
            erreurs.append("ressource réseau hors citations")
    if "fonts.googleapis" in fragment or "url(http" in fragment or "url(\"http" in fragment:
        erreurs.append("police ou image distante")
    for niv in desc["niveaux"]:
        for st in niv["structures"]:
            if st.get("lesion") and not (st.get("definition") or "").strip():
                erreurs.append(f"lésion sans définition : {st['id']}")
            if len(st["nom"]) > 48:
                erreurs.append(f"nom trop long : {st['nom']}")
            if st.get("definition") and len(st["definition"]) > 360:
                erreurs.append(f"définition trop longue : {st['id']}")
    # Sans script, les title restent.
    if not titres:
        erreurs.append("aucun title : mode dégradé vide")
    # Un seul niveau visible par les règles CSS.
    if f"#{prefix}-" not in fragment or "display:none" not in fragment:
        erreurs.append("bascule de niveau absente")
    return erreurs


def _charger(chemin: Path) -> dict:
    return json.loads(chemin.read_text(encoding="utf-8"))


def autotest(chemin: Path = EXEMPLE) -> int:
    desc = _charger(chemin)
    frag = rendre(desc, "POLICE")
    erreurs = verifier(frag, desc)
    poids = len(frag.encode("utf-8"))
    print(f"fragment {poids} octets, {sum(len(n['structures']) for n in desc['niveaux'])} zones, "
          f"{len(desc['niveaux'])} niveaux")
    if erreurs:
        for e in erreurs:
            print("ÉCHEC", e)
        return 1
    print("autotest vert")
    return 0


def main(argv: list[str]) -> int:
    p = argparse.ArgumentParser(description="Génère un schéma SVG interactif autonome.")
    p.add_argument("--autotest", action="store_true")
    p.add_argument("commande", nargs="?", choices=("rendre",))
    p.add_argument("description", nargs="?")
    p.add_argument("-o", "--sortie")
    p.add_argument("--police", default="../../polices/AtkinsonHyperlegible-Regular.ttf")
    args = p.parse_args(argv)
    if args.autotest:
        return autotest(Path(args.description) if args.description else EXEMPLE)
    if args.commande != "rendre" or not args.description or not args.sortie:
        p.print_help()
        return 2
    desc = _charger(Path(args.description))
    frag = rendre(desc, args.police)
    erreurs = verifier(frag, desc)
    if erreurs:
        for e in erreurs:
            print("ÉCHEC", e, file=sys.stderr)
        return 1
    html_page = page(frag, desc.get("titre", desc["id"]), args.police)
    Path(args.sortie).write_text(html_page, encoding="utf-8")
    print(f"écrit {args.sortie} ({len(html_page.encode('utf-8'))} octets)")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
