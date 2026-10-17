import markdown,subprocess,sys
md=open('AUDIT_examen_physique.md').read()
h=markdown.markdown(md,extensions=['tables'])
css="""@page{size:A4 landscape;margin:12mm}body{font-family:'DejaVu Sans',sans-serif;font-size:9pt;text-align:justify;color:#111}
h1{background:#1f6f43;color:#fff;padding:6px 10px}h2{border-bottom:3px solid #1f6f43;color:#000;margin-top:18px}h3{color:#1f6f43}
table{border-collapse:collapse;width:100%;font-size:7.6pt;margin:6px 0;page-break-inside:auto}th{background:#e8f3ec}td,th{border:1px solid #999;padding:3px;vertical-align:top;text-align:left}
tr:nth-child(even){background:#fafafa}strong{color:#000}"""
html=f"<html><head><meta charset=utf-8><style>{css}</style></head><body>{h}</body></html>"
html=html.replace('✗','<span style="color:#c00;font-weight:bold">✗</span>')
open('audit.html','w').write(html)
subprocess.run(['google-chrome','--headless','--no-sandbox','--disable-gpu','--no-pdf-header-footer','--print-to-pdf=AUDIT_examen_physique.pdf','audit.html'],check=True,capture_output=True)
