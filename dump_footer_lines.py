import pathlib
text = pathlib.Path('index.html').read_text('utf8')
lines = text.splitlines()
for i,l in enumerate(lines):
    if 'db-edit-hint' in l:
        print('line', i, repr(l))
        print('next', i+1, repr(lines[i+1]))
        print('next2', i+2, repr(lines[i+2]))
        break
