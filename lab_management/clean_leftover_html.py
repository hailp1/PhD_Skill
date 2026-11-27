import re

MANUSCRIPT_PATH = "lab_projects/PAPER_01_SLR_JRCS_MANUSCRIPT.md"

with open(MANUSCRIPT_PATH, "r", encoding="utf-8") as f:
    text = f.read()

# 1. Clean leftover PRISMA HTML
# Between the first academic-figure-container and "### 2.3. Bibliometric Mapping Protocol"
p1 = r'(<div class="academic-figure-container"[\s\S]*?PRISMA 2020 Flow Diagram[\s\S]*?</div>\s*</div>)[\s\S]*?(### 2\.3\. Bibliometric Mapping Protocol)'
text = re.sub(p1, r'\1\n\n\2', text)

# 2. Clean leftover S-O-R HTML
# Between the third academic-figure-container and "### 4.1. Algorithmic Stimuli"
p2 = r'(<div class="academic-figure-container"[\s\S]*?Integrative Conceptual Model[\s\S]*?</div>\s*</div>)[\s\S]*?(### 4\.1\. Algorithmic Stimuli)'
text = re.sub(p2, r'\1\n\n\2', text)

# 3. Check for any non-English/Vietnamese characters
vn_pattern = re.compile(r'[àáảãạăằắẳẵặâầấẩẫậèéẻẽẹêềếểễệìíỉĩịòóỏõọôồốổỗộơờớởỡợùúủũụưừứửữựỳýỷỹỵđÀÁẢÃẠĂẰẮẲẴẶÂẦẤẨẪẬÈÉẺẼẸÊỀẾỂỄỆÌÍỈĨỊÒÓỎÕỌÔỒỐỔỖỘƠỜỚỞỠỢÙÚỦŨỤƯỪỨỬỮỰỲÝỶỸỴĐ]')
vn_matches = vn_pattern.findall(text)
print(f"Remaining Vietnamese characters: {len(vn_matches)}")

with open(MANUSCRIPT_PATH, "w", encoding="utf-8") as f:
    f.write(text)

print("[OK] Finished cleaning manuscript!")
