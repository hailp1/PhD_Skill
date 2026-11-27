import base64
import re

def embed_real_vosviewer_png():
    with open('lab_projects/figures/figure2_vosviewer_real_network.png', 'rb') as f:
        png_data = f.read()

    b64_str = base64.b64encode(png_data).decode('utf-8')
    data_uri = f"data:image/png;base64,{b64_str}"

    with open('lab_projects/PAPER_01_SLR_JRCS_MANUSCRIPT.md', 'r', encoding='utf-8') as f:
        text = f.read()

    # Pattern for Figure 2 image tag
    pattern = r'(<h4[^>]*>.*?Figure 2:.*?</h4>[\s\S]*?<img src=")[^"]+("[\s\S]*?<p[^>]*>Figure 2\..*?</p>)'

    if re.search(pattern, text):
        new_text = re.sub(pattern, rf'\g<1>{data_uri}\g<2>', text)
        with open('lab_projects/PAPER_01_SLR_JRCS_MANUSCRIPT.md', 'w', encoding='utf-8') as f:
            f.write(new_text)
        print("Successfully embedded REAL VOSviewer PNG (base64) into Figure 2 of manuscript!")
    else:
        print("Figure 2 pattern not found in manuscript!")

if __name__ == '__main__':
    embed_real_vosviewer_png()
