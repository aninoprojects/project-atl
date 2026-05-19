from pathlib import Path
text = Path('index.html').read_text('utf8')
needle = '      <span id="db-footer-label">Source: Project ATL Spreadsheet v3.1</span>'
idx = text.find(needle)
print('idx', idx)
if idx != -1:
    print(repr(text[idx:idx+400]))
