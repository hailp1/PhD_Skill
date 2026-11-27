"""
H-AI ResearchLAB: Embed 100% Academic English Vector Figures into Paper 1 Manuscript
Replaces all previous diagram blocks with bulletproof atomic SVG image tags
"""

import os
import re
import urllib.parse

MANUSCRIPT_PATH = "lab_projects/PAPER_01_SLR_JRCS_MANUSCRIPT.md"

with open(MANUSCRIPT_PATH, "r", encoding="utf-8") as f:
    text = f.read()

# Read the 3 SVG files
with open("lab_projects/figures/figure1_prisma_flow_diagram.svg", "r", encoding="utf-8") as f:
    prisma_svg = f.read()
with open("lab_projects/figures/figure2_vosviewer_clusters.svg", "r", encoding="utf-8") as f:
    vos_svg = f.read()
with open("lab_projects/figures/figure3_theoretical_sor_model.svg", "r", encoding="utf-8") as f:
    sor_svg = f.read()

# Helper to produce bulletproof data URI image tag
def to_svg_img_tag(svg_content, fig_id, fig_title, fig_caption, extra_btn=None):
    # Clean SVG content into a safe URL-encoded data URI
    encoded_svg = urllib.parse.quote(svg_content)
    data_uri = f"data:image/svg+xml;utf-8,{encoded_svg}"
    
    btn_html = ""
    if extra_btn:
        btn_html = extra_btn
        
    html = f'''<div class="academic-figure-container" style="background:#ffffff; border:1.5px solid #cbd5e1; border-radius:12px; padding:1.5rem; margin:2rem 0; box-shadow:0 4px 16px rgba(0,0,0,0.03);">
<div style="display:flex; justify-content:space-between; align-items:center; border-bottom:1.5px solid #e2e8f0; padding-bottom:0.75rem; margin-bottom:1.25rem;">
<h4 style="font-size:1.05rem; font-weight:800; color:#0f172a; margin:0;"><i class="fa-solid fa-chart-line" style="color:#0284c7;"></i> {fig_title}</h4>
{btn_html}
</div>
<img src="{data_uri}" alt="{fig_title}" style="width:100%; height:auto; display:block; border-radius:8px; border:1px solid #e2e8f0;" />
<p style="font-size:0.85rem; color:#64748b; font-style:italic; text-align:center; margin:0.85rem 0 0 0;">{fig_caption}</p>
</div>'''
    return html

# 1. Figure 1: PRISMA 2020 Flow Diagram
fig1_html = to_svg_img_tag(
    prisma_svg,
    "fig1",
    "Figure 1: PRISMA 2020 Flow Diagram for Systematic Literature Reviews",
    "Figure 1. Systematic search and eligibility screening trajectory across Scopus, Web of Science, and Dimensions following the PRISMA 2020 statement."
)

# 2. Figure 2: VOSviewer Tri-Cluster Co-Occurrence Network Map
vos_btn = '<a href="http://localhost:8600" target="_blank" style="background:#0284c7; color:#ffffff; padding:0.45rem 0.95rem; border-radius:6px; font-size:0.8rem; font-weight:700; text-decoration:none; display:inline-flex; align-items:center; gap:0.4rem;"><i class="fa-solid fa-arrow-up-right-from-square"></i> Open Interactive VOSviewer (Port 8600)</a>'
fig2_html = to_svg_img_tag(
    vos_svg,
    "fig2",
    "Figure 2: Tri-Cluster Bibliometric Co-Occurrence Network Map (VOSviewer)",
    "Figure 2. Intellectual structure of the 866 core publications, highlighting the three interconnected thematic clusters (Red: Stimulus, Green: Organism, Blue: Response).",
    extra_btn=vos_btn
)

# 3. Figure 3: Integrative Conceptual S-O-R Model
fig3_html = to_svg_img_tag(
    sor_svg,
    "fig3",
    "Figure 3: Integrative Conceptual Model and Hypothesized Structural Relationships",
    "Figure 3. Proposed Stimulus-Organism-Response theoretical framework incorporating Cognitive Fit and Ego Depletion theories with formal hypotheses H1–H6."
)

# Replace in manuscript
# Replace PRISMA section
text = re.sub(r'<div class="prisma-flow-diagram">[\s\S]*?</div>\s*</div>', fig1_html, text)
text = re.sub(r'```\s*┌─+┐\s*│\s*PRISMA 2020 FLOW DIAGRAM\s*│[\s\S]*?```', fig1_html, text)

# Replace VOSviewer section
text = re.sub(r'<div class="vos-cluster-card">[\s\S]*?</div>\s*</div>', fig2_html, text)
text = re.sub(r'```\s*┌─+┐\s*│\s*TRI-CLUSTER BIBLIOMETRIC NETWORK\s*│[\s\S]*?```', fig2_html, text)

# Replace Conceptual model section
text = re.sub(r'<div class="sor-diagram-box">[\s\S]*?</div>\s*</div>', fig3_html, text)
text = re.sub(r'```\s*┌─+┐\s*│\s*INTEGRATIVE CONCEPTUAL MODEL\s*│[\s\S]*?```', fig3_html, text)

with open(MANUSCRIPT_PATH, "w", encoding="utf-8") as f:
    f.write(text)

print("[OK] Successfully embedded atomic SVG figures into PAPER_01_SLR_JRCS_MANUSCRIPT.md!")
