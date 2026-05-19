import pathlib
p = pathlib.Path('index.html')
text = p.read_text('utf8')
idx = text.index('db-footer-label')
print(repr(text[idx-150:idx+150]))
