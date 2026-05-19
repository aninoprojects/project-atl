import pathlib
path = pathlib.Path('index.html')
text = path.read_text('utf8')
text = text.replace('\r\n', '\n')
footer_anchor = '      <span id="db-edit-hint" style="display:none;color:var(--accent-l);">Admin: click Edit to change a row, then Save or Cancel</span>\n\n      <span id="db-footer-label">Source: Project ATL Spreadsheet v3.1</span>'
footer_replacement = '      <div style="display:flex;align-items:center;gap:8px;flex-wrap:wrap;">\n        <span id="db-edit-hint" style="display:none;color:var(--accent-l);">Admin: click Edit to change a row, then Save or Cancel</span>\n        <div id="db-admin-controls" style="display:none;align-items:center;gap:8px;">\n          <button class="db-action-btn" type="button" onclick="addDbColumn()">+ Column</button>\n          <button class="db-action-cancel" type="button" onclick="editDbColumns()">Manage Columns</button>\n          <button class="db-action-delete" type="button" onclick="restoreDeletedDbRows()">Restore deleted</button>\n        </div>\n      </div>\n\n      <span id="db-footer-label">Source: Project ATL Spreadsheet v3.1</span>'
action_anchor = '      actionTd.appendChild(editBtn);\n\n      if (_dbEditingKey === rowKey) {'
action_replacement = '      actionTd.appendChild(editBtn);\n\n      var deleteBtn = document.createElement(\'button\');\n      deleteBtn.type = \'button\';\n      deleteBtn.className = \'db-action-delete\';\n      deleteBtn.textContent = \'Delete\';\n      deleteBtn.addEventListener(\'click\', function(ev){ ev.stopPropagation(); deleteDbRow(rowKey,rowName); });\n      actionTd.appendChild(deleteBtn);\n\n      if (_dbEditingKey === rowKey) {'
css_anchor = '.db-action-btn:hover{background:rgba(249,115,22,0.16);}\n\n    .db-action-cancel{color:#94a3b8;border-color:rgba(148,163,184,0.4);background:rgba(148,163,184,0.08);margin-left:6px;}\n\n    .db-action-cancel:hover{background:rgba(148,163,184,0.14);}\n'
css_replacement = '.db-action-btn:hover{background:rgba(249,115,22,0.16);}\n\n    .db-action-delete{font-family:\'IBM Plex Mono\',monospace;font-size:0.65rem;padding:4px 8px;border-radius:6px;border:1px solid rgba(239,68,68,0.35);color:#dc2626;background:rgba(254,202,202,0.16);margin-left:6px;}\n\n    .db-action-delete:hover{background:rgba(254,202,202,0.3);}\n\n    .db-action-cancel{color:#94a3b8;border-color:rgba(148,163,184,0.4);background:rgba(148,163,184,0.08);margin-left:6px;}\n\n    .db-action-cancel:hover{background:rgba(148,163,184,0.14);}\n'
for name, anchor in [('footer', footer_anchor), ('action', action_anchor), ('css', css_anchor)]:
    if anchor not in text:
        raise SystemExit(f'{name} anchor not found')
text = text.replace(footer_anchor, footer_replacement, 1)
text = text.replace(action_anchor, action_replacement, 1)
text = text.replace(css_anchor, css_replacement, 1)
path.write_text(text.replace('\n','\r\n'), encoding='utf-8')
print('patches applied')
