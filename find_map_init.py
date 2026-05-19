from pathlib import Path
text = Path('index.html').read_text('utf8')
needle = 'var map = null;'
idx = text.find(needle)
print('idx', idx)
if idx != -1:
    print(repr(text[idx:idx+120]))
