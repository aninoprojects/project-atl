import re, json, pathlib, ast
text = pathlib.Path('index.html').read_text(encoding='utf-8')
start = text.index('var ATL_DB_DATA = [')
end = text.index('];', start) + 2
js = text[start:end]
arr_text = js[js.index('['):]
arr_text = arr_text.replace('\n', ' ')
arr_text = re.sub(r'([\{,\s])(\w+)\s*:', r'\1"\2":', arr_text)
arr_text = arr_text.replace("'", '"')
arr_text = re.sub(r',\s*\}', '}', arr_text)
# Extract all object literals
objects = re.findall(r'\{[^\}]*\}', arr_text)
data = []
for obj in objects:
    try:
        data.append(json.loads(obj))
    except json.JSONDecodeError:
        try:
            data.append(ast.literal_eval(obj))
        except Exception:
            pass
seen = {}
for r in data:
    key = re.sub(r'[^A-Z0-9]+', '', (r.get('toda') or '').upper())
    seen.setdefault(key, []).append(r)
dups = {k:v for k,v in seen.items() if len(v) > 1}
print('duplicate count:', len(dups))
for k,v in sorted(dups.items(), key=lambda kv: -len(kv[1]))[:30]:
    print(k, len(v), [x.get('toda') for x in v])
