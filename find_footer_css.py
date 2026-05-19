from pathlib import Path
text = Path('index.html').read_text('utf8')
needle = '.db-footer a{'
idx = text.find(needle)
print('idx', idx)
print(repr(text[idx-50:idx+200]))
