import urllib.parse
import re

def update_figure2():
    with open('lab_projects/figures/figure2_vosviewer_real_network.svg', 'r', encoding='utf-8') as f:
        real_svg = f.read()

    encoded_svg = urllib.parse.quote(real_svg)

    with open('lab_projects/PAPER_01_SLR_JRCS_MANUSCRIPT.md', 'r', encoding='utf-8') as f:
        text = f.read()

    # Find the Figure 2 image tag
    pattern = r'(<h4[^>]*>.*?Figure 2:.*?</h4>[\s\S]*?<img src=")[^"]+("[\s\S]*?<p[^>]*>Figure 2\..*?</p>)'
    
    if re.search(pattern, text):
        new_text = re.sub(pattern, rf'\g<1>data:image/svg+xml;utf-8,{encoded_svg}\g<2>', text)
        with open('lab_projects/PAPER_01_SLR_JRCS_MANUSCRIPT.md', 'w', encoding='utf-8') as f:
            f.write(new_text)
        print("Updated Figure 2 in PAPER_01_SLR_JRCS_MANUSCRIPT.md with REAL VOSviewer SVG!")
    else:
        print("Figure 2 pattern not found!")

if __name__ == '__main__':
    update_figure2()
