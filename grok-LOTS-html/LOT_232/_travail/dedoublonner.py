# -*- coding: utf-8 -*-
"""Retire, dans une leçon assemblée, les phrases de 8 mots ou plus déjà dites plus haut (porte : phrase_double).

La première occurrence reste à sa place ; les suivantes sont ôtées du paragraphe. Un paragraphe vidé disparaît.
Ne touche que les <p> hors en-tête et hors sources. Aucun ajout de contenu.
"""
from __future__ import annotations

import html as H
import re

MOT = re.compile(r"[\wÀ-ÿŒœ]+(?:['’\-][\wÀ-ÿŒœ]+)*")
# fin de phrase : ponctuation forte, éventuellement suivie d'un appel de source, puis espace et majuscule (ou balise)
FIN = re.compile(r'(?<=[.!?…])((?:<sup class="s">[^<]*</sup>)?)\s+(?=(?:<[^>]+>)*[A-ZÀ-Ý«(\["“]|<button)')


def texte(frag: str) -> str:
    t = re.sub(r'<sup class="s">[^<]*</sup>', "", frag)
    t = re.sub(r"<[^>]+>", "", t)
    return H.unescape(t)


def cle(frag: str) -> str:
    return re.sub(r"[^a-z0-9àâäçéèêëîïôöùûüœ]+", " ", texte(frag).lower()).strip()


def morceaux(par: str) -> list[str]:
    out, i = [], 0
    for m in FIN.finditer(par):
        out.append(par[i:m.end(1)])
        i = m.end()
    out.append(par[i:])
    return [x for x in out if x.strip()]


def equilibre(frag: str) -> bool:
    ouv = len(re.findall(r"<(?!/)(?!br\b)[a-z]+[^>]*(?<!/)>", frag))
    fer = len(re.findall(r"</[a-z]+>", frag))
    return ouv == fer


def dedoublonner(page: str, min_mots: int = 8) -> str:
    debut = page.find("<main>")
    fin = page.find('<h2 id="sources">')
    tete, corps, queue = page[:debut], page[debut:fin], page[fin:]
    vus: set[str] = set()

    def un_p(m):
        attrs, contenu = m.group(1), m.group(2)
        garde = []
        for s in morceaux(contenu):
            k = cle(s)
            if len(MOT.findall(H.unescape(re.sub(r"<[^>]+>", "", s)))) >= min_mots and equilibre(s):
                if k in vus:
                    continue
                vus.add(k)
            garde.append(s)
        if not garde:
            return ""
        return f"<p{attrs}>" + " ".join(x.strip() for x in garde) + "</p>"

    corps = re.sub(r"<p((?:\s[^>]*)?)>(.*?)</p>\n?", lambda m: (lambda r: r + "\n" if r else "")(un_p(m)), corps, flags=re.S)
    return tete + corps + queue
