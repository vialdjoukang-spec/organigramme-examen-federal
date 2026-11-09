#!/usr/bin/env python3
"""Repère les nombres d'une phrase et les compare aux jetons numériques d'un extrait."""
from __future__ import annotations
import re

UNITS = {
    "un": 1, "une": 1, "deux": 2, "trois": 3, "quatre": 4, "cinq": 5, "six": 6,
    "sept": 7, "huit": 8, "neuf": 9, "dix": 10, "onze": 11, "douze": 12,
    "treize": 13, "quatorze": 14, "quinze": 15, "seize": 16,
}
TENS = {"vingt": 20, "trente": 30, "quarante": 40, "cinquante": 50, "soixante": 60}
COMPOUNDS = [
    ("quatre-vingt-dix-neuf", 99), ("quatre-vingt-dix-huit", 98), ("quatre-vingt-dix-sept", 97),
    ("quatre-vingt-seize", 96), ("quatre-vingt-quinze", 95), ("quatre-vingt-quatorze", 94),
    ("quatre-vingt-treize", 93), ("quatre-vingt-douze", 92), ("quatre-vingt-onze", 91),
    ("quatre-vingt-dix", 90), ("quatre-vingts", 80), ("quatre-vingt", 80),
    ("soixante-dix-neuf", 79), ("soixante-dix-huit", 78), ("soixante-dix-sept", 77),
    ("soixante-seize", 76), ("soixante-quinze", 75), ("soixante-quatorze", 74),
    ("soixante-treize", 73), ("soixante-douze", 72), ("soixante-onze", 71), ("soixante-dix", 70),
    ("dix-sept", 17), ("dix-huit", 18), ("dix-neuf", 19),
]

def jetons(texte: str) -> set[int]:
    return {int(x) for x in re.findall(r"\d+", texte)}

def _parler(fragment: str) -> int | None:
    fragment = fragment.strip()
    for mot, val in COMPOUNDS:
        if fragment == mot:
            return val
    if fragment in UNITS:
        return UNITS[fragment]
    if fragment in TENS:
        return TENS[fragment]
    for ten, base in TENS.items():
        if fragment.startswith(ten + "-"):
            rest = fragment[len(ten) + 1:]
            rest = rest.removeprefix("et-")
            if rest in UNITS:
                return base + UNITS[rest]
    if fragment.startswith("quatre-vingt-"):
        rest = fragment[len("quatre-vingt-"):]
        if rest in UNITS:
            return 80 + UNITS[rest]
    return None

MOT = r"(?:quatre-vingt(?:s|-(?:dix(?:-(?:sept|huit|neuf)|sept|huit|neuf)?|onze|douze|treize|quatorze|quinze|seize|et-un))?|soixante(?:-dix(?:-(?:sept|huit|neuf)|sept|huit|neuf)?|-et-onze|-onze|-douze|-treize|-quatorze|-quinze|-seize)?|dix-sept|dix-huit|dix-neuf|cinquante(?:-et-un|-deux|-trois|-quatre|-cinq|-six|-sept|-huit|-neuf)?|quarante(?:-et-un|-deux|-trois|-quatre|-cinq|-six|-sept|-huit|-neuf)?|trente(?:-et-un|-deux|-trois|-quatre|-cinq|-six|-sept|-huit|-neuf)?|vingt(?:-et-un|-deux|-trois|-quatre|-cinq|-six|-sept|-huit|-neuf)?|seize|quinze|quatorze|treize|douze|onze|dix|neuf|huit|sept|six|cinq|quatre|trois|deux|un|une)"

def nombres_parles(phrase: str) -> list[int]:
    t = phrase.lower().replace("’", "'").replace("–", "-").replace("—", "-")
    t = re.sub(r"\s+", " ", t)
    vals = []
    for m in re.finditer(rf"(?<![\w'-]){MOT}(?![\w'-])", t):
        mot = m.group(0)
        if mot in ("un", "une"):
            suite = t[m.end():m.end() + 14]
            if "pour cent" not in suite:
                continue
        val = _parler(mot.replace(" ", "-"))
        if val is not None:
            vals.append(val)
    return vals

# Mots anglais ou français qui portent le même nombre dans l'extrait source.
MOTS_NOMBRE = {
    2: ["two", "deux"], 3: ["three", "trois"], 4: ["four", "quatre"], 5: ["five", "cinq"],
    5: ["five", "cinq"], 6: ["six"], 8: ["eight", "huit"], 9: ["nine", "neuf"],
    10: ["ten", "dix"], 12: ["twelve", "douze"], 13: ["thirteen", "treize"],
    16: ["sixteen", "seize"], 18: ["eighteen", "dix-huit"], 20: ["twenty", "vingt"],
    24: ["twenty-four", "twenty four"], 42: ["forty-two", "quarante-deux"],
    50: ["fifty", "cinquante"],
    80: ["eighty"], 90: ["ninety"],
}

def nombres_phrase(phrase: str) -> list[int]:
    return [int(x) for x in re.findall(r"\d+", phrase)] + nombres_parles(phrase)

def hors_extrait(phrase: str, extrait: str) -> list[int]:
    ok = jetons(extrait)
    bas = extrait.lower()
    mauvais = []
    for n in nombres_phrase(phrase):
        if n in ok:
            continue
        if any(re.search(rf"(?<![\w'-]){re.escape(w)}(?![\w'-])", bas) for w in MOTS_NOMBRE.get(n, [])):
            continue
        mauvais.append(n)
    return mauvais
