import pathlib
p = pathlib.Path('index.html')
text = p.read_text('utf8')
print('contains db-footer-label', 'db-footer-label' in text)
print('count', text.count('db-footer-label'))
