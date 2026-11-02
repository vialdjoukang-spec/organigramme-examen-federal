from pathlib import Path
P=Path(__file__).parent
ns={'__file__':str(P/'b_base.py')}
exec(compile((P/'b_base.py').read_text(),str(P/'b_base.py'),'exec'),ns)
for i in range(1,11):
 f=P/f'b_dx{i:02}.py'
 if f.exists():exec(compile(f.read_text(),str(f),'exec'),ns)
for n,ids in enumerate([[1,2],[3,4,5],[6,7],[8,9,10]],1):
 if all(i in ns['MONOS'] for i in ids):ns['finish'](n,ids)
