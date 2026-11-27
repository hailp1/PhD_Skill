import re

for file_path in ['XEM_BAN_THAO_BAI_BAO.html', 'web/XEM_BAN_THAO_BAI_BAO.html']:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Update button to call window.print() directly
    content = content.replace(
        'id="btnExportPdf" class="btn-ctrl" onclick="exportAcademicPDF()"',
        'id="btnExportPdf" class="btn-ctrl" onclick="window.print()"'
    )

    # 2. Update exportAcademicPDF function to window.print()
    content = re.sub(
        r'function exportAcademicPDF\(\)\s*\{[\s\S]*?\}\s*function closePdfModal',
        'function exportAcademicPDF() {\n            window.print();\n        }\n\n        function closePdfModal',
        content
    )

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Successfully restored 1-click native PDF export on {file_path}")
