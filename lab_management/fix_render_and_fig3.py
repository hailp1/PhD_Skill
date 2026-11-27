import re

for path in ['XEM_BAN_THAO_BAI_BAO.html', 'web/XEM_BAN_THAO_BAI_BAO.html']:
    with open(path, 'r', encoding='utf-8') as f:
        html = f.read()

    # 1. Hide .journal-top-bar in @media print so internal file path / status never leaks onto PDF Page 1
    html = html.replace(
        '.reader-navbar, .reader-sidebar, .toc-section, #pdfExportModal, .pdf-modal-backdrop {',
        '.reader-navbar, .reader-sidebar, .toc-section, .journal-top-bar, #pdfExportModal, .pdf-modal-backdrop {'
    )

    # 2. Ensure print body uses Merriweather/Georgia/Times New Roman serif font so uppercase I never looks like lowercase l
    html = html.replace(
        'font-size: 11pt !important;\n                line-height: 1.65 !important;',
        'font-family: "Merriweather", Georgia, "Times New Roman", serif !important;\n                font-size: 10.5pt !important;\n                line-height: 1.65 !important;'
    )

    # 3. Ensure <pre> and <code> wrap cleanly in both screen and print so Boolean query never clips at right margin
    pre_wrap_css = """
        pre, code {
            white-space: pre-wrap !important;
            word-wrap: break-word !important;
            overflow-wrap: break-word !important;
            max-width: 100% !important;
        }
        @page {"""
    if 'word-wrap: break-word !important;' not in html:
        html = html.replace('@page {', pre_wrap_css, 1)

    with open(path, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f'Updated print CSS & pre-wrap in {path}')

# Also update P8 (-) arrow in Figure 3 SVG so it points cleanly to the Stimulus -> Organism bridge
fig3_path = 'lab_projects/figures/figure3_theoretical_sor_model.svg'
with open(fig3_path, 'r', encoding='utf-8') as f:
    svg = f.read()

# Move P8 (-) vertical arrow to x=284 targeting the S->O bridge region (spanning P1, P2, P3)
svg = svg.replace(
    '<line x1="280" y1="475" x2="280" y2="250" stroke="#e11d48" stroke-width="2" stroke-dasharray="4,4" marker-end="url(#marr-rose)"/>',
    '<line x1="284" y1="475" x2="284" y2="265" stroke="#e11d48" stroke-width="2" stroke-dasharray="4,4" marker-end="url(#marr-rose)"/>\n  <rect x="262" y="150" width="44" height="225" rx="6" fill="none" stroke="#e11d48" stroke-width="1.2" stroke-dasharray="3,3" opacity="0.6"/>'
)

with open(fig3_path, 'w', encoding='utf-8') as f:
    f.write(svg)
print('Updated Figure 3 P8 (-) boundary arrow to span the entire S -> O bridge!')
