from pathlib import Path
text = Path('index.html').read_text('utf8')
target = '<a href="/about.html" class="topbar-btn" style="text-decoration:none;">About</a>'
idx = text.find(target)
print('idx', idx)
if idx != -1:
    print(repr(text[idx-40:idx+100]))
