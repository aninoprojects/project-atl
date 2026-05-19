from pathlib import Path
text = Path("index.html").read_text("utf8")
needle = "var hint = document.getElementById('db-edit-hint');"
idx = text.find(needle)
print("idx", idx)
print(repr(text[idx-120:idx+220]))
