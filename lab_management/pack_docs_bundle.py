import json
import os

docs_to_pack = {
    'paper1': ('lab_projects/PAPER_01_SLR_JRCS_MANUSCRIPT.md', 'Bản Thảo IMRAD: Paper 01 (JRCS Submission)', 'JRCS Q1 (IF: 11.0)', 'Bản Thảo 85%'),
    'plan': ('lab_projects/AUTOMATED_PAPER_WRITING_PLAN.md', 'Kế Hoạch Bài Báo Mới (IMRAD Blueprint)', 'H-AI Engine', 'Scopus Q1 Plan'),
    'survey': ('docs/survey_instrument.md', 'Paper 2: Bảng Hỏi Khảo Sát Thực Nghiệm', 'N = 450 (Likert 7)', '28 Items'),
    'proposal': ('docs/proposal_detailed.md', 'Đề Cương Nghiên Cứu Tiến Sĩ Chi Tiết', 'TDTU Ph.D.', 'Đề Cương Chuẩn'),
    'baumeister': ('lab_projects/parsed_markdown/baumeister_2002.md', 'Toàn Văn: Baumeister (2002) - Ego Depletion', 'JCR FT50', 'Lý Thuyết Nền'),
    'shanahan': ('lab_projects/parsed_markdown/shanahan_2019.md', 'Toàn Văn: Shanahan (2019) - Thang Đo PP', 'JRCS Q1', 'Thang Đo Gốc'),
    'beatty': ('lab_projects/parsed_markdown/beatty_1998.md', 'Toàn Văn: Beatty & Ferrell (1998) - Thang Đo UBI', 'J. Retailing Q1', 'Thang Đo Gốc'),
    'verhagen': ('lab_projects/parsed_markdown/verhagen_2011.md', 'Toàn Văn: Verhagen & van Dolen (2011) - Khung S-O-R', 'I&M Q1', 'Khung Lý Thuyết')
}

bundle = {}
for k, (fpath, title, tag, status) in docs_to_pack.items():
    if os.path.exists(fpath):
        with open(fpath, 'r', encoding='utf-8') as f:
            md_text = f.read()
            bundle[k] = {
                'title': title,
                'tag': tag,
                'status': status,
                'path': fpath,
                'markdown': md_text
            }
        print(f"Packed {k}: {len(md_text):,} chars")

with open('lab_projects/DOCUMENTS_BUNDLE.json', 'w', encoding='utf-8') as f:
    json.dump(bundle, f, ensure_ascii=False, indent=2)

print("Generated lab_projects/DOCUMENTS_BUNDLE.json successfully!")
