"""Commun arsenal : racine, chargement, sortie JSON compacte."""
import json, os, re, sys
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
SSP_RE = re.compile(r'^[SFOG]\d+(\.\d+)?$')
DOSE = re.compile(r'\b\d+(?:[.,]\d+)?\s?(?:mg|µg|mcg|g|UI)(?:/kg)?\b')
DATE = re.compile(r'\d{1,2}\.\d{1,2}\.20\d\d|20\d\d-\d\d-\d\d')
def load(p): return json.load(open(os.path.join(ROOT, p), encoding='utf-8'))
def out(o): print(json.dumps(o, ensure_ascii=False, separators=(',', ':')))
def mono_key(name):
    from mono_build import mid
    return mid(name)
