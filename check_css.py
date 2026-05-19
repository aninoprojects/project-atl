import pathlib
p = pathlib.Path('index.html')
text = p.read_text('utf8')
idx = text.index('.db-action-btn:hover{background:rgba(249,115,22,0.16);}')
print(repr(text[idx:idx+220]))
