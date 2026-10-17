#!/usr/bin/env python3
"""Écrit dans links.txt les URL ajoutées ou modifiées dans app_v2.html et data/ck/ (sources CK) depuis <base>."""
import re, subprocess, sys
base = sys.argv[1] if len(sys.argv) > 1 else 'origin/main'
diff = subprocess.run(['git', 'diff', '-U0', base, '--', 'app_v2.html', 'data/ck', ':(exclude)data/ck/schema'],
                      capture_output=True, text=True, check=True).stdout
urls = set()
for line in diff.splitlines():
    if line.startswith('+') and not line.startswith('+++'):
        urls.update(re.findall(r'https?://[^\s"\'<>\\)\]]+', line))
urls = sorted(u.rstrip('.,;') for u in urls)
open('links.txt', 'w').write('\n'.join(urls) + ('\n' if urls else ''))
print(f'{len(urls)} URL nouvelles ou modifiées.')
