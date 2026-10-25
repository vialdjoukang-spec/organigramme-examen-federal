from pathlib import Path
p = Path(__file__).parent
ns = {'__file__': str(p / 'build_appel_a.py')}
for name in ['build_appel_a.py', 'appel_a_suite.py', 'corrections_a.py', 'appel_a_bloc2.py']:
    exec(compile((p / name).read_text(), str(p / name), 'exec'), ns)
