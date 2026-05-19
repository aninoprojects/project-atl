import pathlib
p = pathlib.Path('index.html')
text = p.read_text('utf8')
idx = text.index('actionTd.appendChild(editBtn);')
print(repr(text[idx-200:idx+260]))
