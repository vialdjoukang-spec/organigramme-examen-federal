#!/usr/bin/env python3
"""Écrit les URL réellement nouvelles/modifiées ; une ligne minifiée ne rend pas nouveaux ses liens inchangés."""
import re, subprocess, sys


def changed_urls(diff):
    added, removed = set(), set()
    for line in diff.splitlines():
        if line.startswith(('+++', '---')) or not line.startswith(('+', '-')):
            continue
        values = set()
        for url in re.findall(r'https?://[^\s"\'<>\\\]]+', line[1:]):
            url = url.rstrip('.,;')
            # Les DOI contiennent des parenthèses ; seule une fermeture de prose
            # extérieure à l’URL est retirée (ex. « (voir https://exemple.org) »).
            while url.endswith(')') and url.count(')') > url.count('('):
                url = url[:-1].rstrip('.,;')
            values.add(url)
        (added if line[0] == '+' else removed).update(values)
    return sorted(added - removed)


def main():
    base = sys.argv[1] if len(sys.argv) > 1 else 'origin/main'
    diff = subprocess.run(['git', 'diff', '-U0', base, '--', 'app_v2.html', 'data/ck', ':(exclude)data/ck/schema'],
                          capture_output=True, text=True, check=True).stdout
    urls = changed_urls(diff)
    with open('links.txt', 'w') as output:
        output.write('\n'.join(urls) + ('\n' if urls else ''))
    print(f'{len(urls)} URL nouvelles ou modifiées.')


if __name__ == '__main__':
    main()
