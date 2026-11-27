from PIL import Image
import base64
import re

def crop_and_update():
    im = Image.open('lab_projects/figures/figure2_vosviewer_real_network.png')
    
    # Core network is clustered between X=380 and 1920, Y=140 and 1080
    cropped = im.crop((380, 140, 1920, 1080))
    cropped_path = 'lab_projects/figures/figure2_vosviewer_real_network_cropped.png'
    cropped.save(cropped_path, quality=95)
    print("Saved cropped image! Dimensions:", cropped.size)

    with open(cropped_path, 'rb') as f:
        b64 = base64.b64encode(f.read()).decode('utf-8')
    data_uri = f"data:image/png;base64,{b64}"

    with open('lab_projects/PAPER_01_SLR_JRCS_MANUSCRIPT.md', 'r', encoding='utf-8') as f:
        text = f.read()

    # 1. Remove the web button from Figure 2 container header
    new_header = '''<div style="border-bottom:1.5px solid #e2e8f0; padding-bottom:0.75rem; margin-bottom:1.25rem;">
<h4 style="font-size:1.05rem; font-weight:800; color:#0f172a; margin:0;"><i class="fa-solid fa-chart-line" style="color:#0284c7;"></i> Figure 2: Empirical Keyword Co-Occurrence Network Map (VOSviewer Cluster Analysis)</h4>
<p style="font-size:0.8rem; color:#64748b; margin:0.25rem 0 0 0;">Network configuration: Fractional counting, minimum occurrence threshold T = 5, association strength normalization.</p>
</div>'''

    btn_pattern = r'<div style="display:flex; justify-content:space-between; align-items:center; border-bottom:1.5px solid #e2e8f0;[\s\S]*?<a href="http://localhost:8600[^\"]*"[^>]*>[\s\S]*?</a>\s*</div>'
    text = re.sub(btn_pattern, new_header, text)

    # 2. Update the Base64 image in Figure 2
    img_pattern = r'(<h4[^>]*>.*?Figure 2:.*?</h4>[\s\S]*?<img src=")[^"]+("[\s\S]*?<p[^>]*>Figure 2\..*?</p>)'
    text = re.sub(img_pattern, rf'\g<1>{data_uri}\g<2>', text)

    # 3. Format Table 1 into standard academic three-line table (NO ASCII box)
    ascii_table_pattern = r'```[\s\S]*?Table 1: Top 10 Most Influential Articles[\s\S]*?```'
    
    academic_table_1 = """**Table 1. Top 10 Most Influential Publications in the Systematic Literature Corpus (Ranked by Total Citations)**

| Rank | Author(s) & Year | Publication Year | Journal Outlet | Total Citations | Primary Thematic Domain |
| :---: | :--- | :---: | :--- | :---: | :--- |
| 1 | Dwivedi et al. | 2020 | *International Journal of Information Management* | 5,901 | Digital Marketing and Artificial Intelligence Agenda |
| 2 | Davenport et al. | 2020 | *Journal of the Academy of Marketing Science* | 1,680 | Artificial Intelligence in Marketing Architecture |
| 3 | Rauschnabel et al. | 2022 | *Computers in Human Behavior* | 1,291 | Extended Reality (XR) and Augmented Retailing |
| 4 | Dwivedi, Hughes, et al. | 2022 | *Psychology & Marketing* | 1,203 | Metaverse, Virtual Worlds, and Consumer Engagement |
| 5 | Følstad & Brandtzæg | 2020 | *Telematics and Informatics* | 1,087 | Conversational Agents and Interaction Satisfaction |
| 6 | Miao et al. | 2021 | *Journal of Marketing* | 704 | Theory of Avatar Marketing and Virtual Influencers |
| 7 | Mariani et al. | 2023 | *Psychology & Marketing* | 612 | AI in Marketing and Consumer Psychology Systematic Review |
| 8 | Guha et al. | 2022 | *Journal of Business Research* | 538 | Machine Learning Algorithms and Consumer Behavioral Responses |
| 9 | Xiao & Benbasat | 2018 | *Information Systems Research* | 495 | Recommendation Agent Explanation Facilities and Trust |
| 10 | Sundar & Kim | 2019 | *Computers in Human Behavior* | 468 | Machine Heuristics and User Interface Cues in AI Perception |

*Note: Citation metrics indexed via Scopus and Crossref Core Collections as of November 2026.*"""

    text = re.sub(ascii_table_pattern, academic_table_1, text)

    with open('lab_projects/PAPER_01_SLR_JRCS_MANUSCRIPT.md', 'w', encoding='utf-8') as f:
        f.write(text)
    print("Successfully refined Figure 2 (cropped) and converted Table 1 to academic three-line format!")

if __name__ == "__main__":
    crop_and_update()
