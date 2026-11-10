#!/usr/bin/env python3
"""Affiche la passation obligatoire ; ne lance aucune production et ne modifie rien."""
from pathlib import Path
import hashlib


def main():
    guide = Path(__file__).resolve().with_name('PASSATION_OUVERTE.md')
    contenu = guide.read_bytes()
    print(contenu.decode('utf-8'))
    print('\nSHA256 de la passation : ' + hashlib.sha256(contenu).hexdigest())
    print('LECTURE REQUISE AVANT INTERVENTION — reprise ouverte à toute IA ; production Codex arrêtée.')


if __name__ == '__main__':
    main()
