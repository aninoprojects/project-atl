from pathlib import Path
import re

path = Path('index.html')
text = path.read_text('utf8')
pattern = re.compile(
    r"(var lbl = document.getElementById\('db-footer-label'\);)([\s\S]*?)(if \(hint\) hint\.style\.display = adminSession \? 'inline' : 'none';)",
    re.MULTILINE,
)
match = pattern.search(text)
if not match:
    raise SystemExit('pattern not found')
new = (
    match.group(1)
    + "\n\n  var adminControls = document.getElementById('db-admin-controls');\n"
    + "  if (adminControls) adminControls.style.display = adminSession ? 'flex' : 'none';\n\n"
    + match.group(2)
    + match.group(3)
)
text = text[:match.start()] + new + text[match.end():]
path.write_text(text, 'utf8')
print('patched')
