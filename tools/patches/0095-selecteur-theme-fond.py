#!/usr/bin/env python3
"""Ajouter le point d’entrée du sélecteur de fond, sans toucher aux blocs du haut."""
import os
from pathlib import Path

def appliquer(html):
    anchors=[('<link rel="stylesheet" href="assets/style/app-2.css">','<link rel="stylesheet" href="assets/style/app-2.css"><script defer src="assets/config/fond-theme.js"></script>'),('<nav class="tabs" role="tablist">','<div id="fond-theme"></div>\n<nav class="tabs" role="tablist">')]
    for a,b in anchors:assert html.count(a)==1 and b not in html
    for a,b in anchors:html=html.replace(a,b,1)
    return html
CSS='/* Thèmes choisis : surfaces de lecture claires, blocs du haut préservés. */\n:root[data-reading-theme] :is(.panel,#tip,#qp){--reading-bg:var(--chosen-reading-bg);--paper:#fff;--ink:#1a1a1a;--mut:#4a4a4a;--line:#dededb;--soft:#f3f3f1;--gold:#7a5b12;--gold2:#d9b65e;--deep:#4a380b;--ok:#1d6a3a;--warn:#8a5207;--bad:#a12a24;--grid:#e6e6e3;--grid2:#f6f6f4;color:var(--ink)}\n:root[data-reading-theme] .panel .m-it{background:var(--reading-bg)}\n#fond-theme{position:relative;min-height:40px;display:flex;justify-content:flex-end;align-items:center}\n#fond-theme>button{min-height:40px}\n#fond-palette{position:absolute;z-index:30;top:calc(100% + 6px);right:0;width:min(420px,100%);max-height:60dvh;overflow:auto;box-sizing:border-box;margin:0;padding:12px;border:1px solid var(--line);border-radius:12px;background:var(--paper);color:var(--ink);box-shadow:0 12px 30px -14px #0006}\n#fond-palette legend{font-weight:600;padding:0 6px}\n.fond-options{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:8px}\n.fond-choice{min-height:44px;padding:7px 6px;border:1px solid #9aa3a7;border-radius:8px;background:var(--swatch);color:#1a1a1a;font:600 .8rem var(--fb);cursor:pointer;overflow-wrap:anywhere}\n.fond-choice[aria-pressed=true]{outline:2px solid #7a5b12;outline-offset:1px;box-shadow:inset 0 0 0 1px #7a5b12}\n.fond-choice:focus-visible{outline:3px solid #1a1a1a;outline-offset:2px}\n#fond-palette p{margin:10px 0 0}\n'

def appliquer_css(css):
    anchor=':root[data-theme="light"] .panel .m-it{background:var(--reading-bg)}\n'
    assert css.count(anchor)==1 and CSS not in css
    return css.replace(anchor,anchor+CSS,1)

if __name__=='__main__':
    target=Path(os.environ.get('APP_FILE','app_v2.html'));style=Path(os.environ.get('STYLE_FILE','assets/style/app-2.css'))
    html=appliquer(target.read_text());css=appliquer_css(style.read_text())
    target.write_text(html);style.write_text(css)
