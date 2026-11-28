"""
Academic Tone, Structural Rigor & Anti-AI Audit Tool v2.0
Designed for Doctoral Dissertations & Scopus Q1/Q2 Papers in Business Administration & Marketing.

Upgraded Checks:
1. AI Clichés & Buzzwords (English & Vietnamese)
2. Boastful assertions & Lack of Academic Hedging (Absolute claims)
3. AI Boilerplate Openers & Generic Formulas
4. Overuse of Mechanical Enumeration (Thứ nhất, Thứ hai, Thứ ba, etc.)
5. Parenthetical Citation Dumping vs. Narrative Citation Ratio
6. Em-dash and mechanical formatting markers
7. Composite Academic Naturalness & Human Scholarly Score (0 - 100)
"""

import sys
import os
import re
import argparse
import statistics

# 1. English AI Clichés & Overused Buzzwords
EN_AI_CLICHES = [
    r"\bdelv(e|es|ed|ing)\s+into\b",
    r"\brich\s+tapestry\b",
    r"\btapestry\b",
    r"\btestament\s+to\b",
    r"\bbeacon\s+of\b",
    r"\bgame[- ]changer\b",
    r"\brevolutionary\b",
    r"\bgroundbreaking\b",
    r"\bunpack(ing)?\b",
    r"\bseamless(ly)?\b",
    r"\bvibrant\b",
    r"\bbespoke\b",
    r"\bin\s+today'?s\s+(fast-paced\s+)?digital\s+(age|world|era)\b",
    r"\bit\s+is\s+(worth\s+noting|important\s+to\s+note|crucial\s+to\s+understand)\s+that\b",
    r"\ba\s+plethora\s+of\b",
    r"\bfoster(ing)?\s+a\s+sense\s+of\b",
    r"\bnavigat(e|ing)\s+the\s+complexities\b",
    r"\bexponential(ly)?\b",
    r"\bdramatic(ally)?\b",
    r"\bfundamentally\b",
    r"\bpivotal\b",
    r"\bindispensable\b",
    r"\bremarkably\b",
    r"\bgold\s+standard\b",
    r"\b100%\s+verified\b",
    r"\bexceptionally\s+high\b",
    r"\bnever\s+been\s+systematically\b",
]

# 2. Vietnamese AI Clichés & Sáo Rỗng Báo Chí / Dịch Máy Gượng Gạo
VN_AI_CLICHES = [
    r"bức\s+tranh\s+toàn\s+cảnh",
    r"chiếc\s+chìa\s+khóa\s+vạn\s+năng",
    r"kim\s+chỉ\s+nam",
    r"minh\s+chứng\s+hùng\s+hồn",
    r"đào\s+sâu\s+nghiên\s+cứu",
    r"mổ\s+xẻ\s+vấn\s+đề",
    r"đột\s+phá\s+mang\s+tính\s+cách\s+mạng",
    r"không\s+thể\s+phủ\s+nhận\s+rằng",
    r"trong\s+kỷ\s+nguyên\s+số\s+hóa\s+vũ\s+bão",
    r"đóng\s+vai\s+trò\s+vô\s+cùng\s+to\s+lớn",
    r"chiếc\s+cầu\s+nối\s+vững\s+chắc",
    r"chiều\s+kích\s+mới\s+mẻ",
    r"hộp\s+đen\s+tâm\s+lý",
    r"hộp\s+đen",
    r"chiều\s+kích\s+công\s+nghệ",
    r"dòng\s+chảy\s+y\s+văn",
    r"độ\s+lệch\s+căn\s+bản",
    r"dưới\s+lăng\s+kính\s+của",
]

# 3. Generic AI Opening Formulas (Mở đầu khuôn mẫu thiếu thực chứng)
GENERIC_AI_OPENERS = [
    r"sự\s+phát\s+triển\s+(mạnh\s+mẽ\s+)?của\s+(công\s+nghệ|trí\s+tuệ\s+nhân\s+tạo|ai|internet)",
    r"trong\s+bối\s+cảnh\s+(bùng\s+nổ|phát\s+triển\s+vũ\s+bão|hội\s+nhập\s+sâu\s+rộng)",
    r"ngày\s+nay,\s+với\s+sự\s+ra\s+đời\s+của",
    r"cùng\s+với\s+sự\s+bùng\s+nổ\s+của",
    r"in\s+the\s+era\s+of\s+(rapid\s+)?technological\s+advancement",
    r"with\s+the\s+(rapid\s+)?advent\s+of",
]

# 4. Boastful / Absolute Claims (Lack of Academic Hedging)
ABSOLUTE_CLAIMS = [
    r"\bprove(s|d)?\s+100%\b",
    r"\bproves?\s+definitively\b",
    r"\bundeniabl(y|e)\b",
    r"\bfirst\s+and\s+only\s+study\b",
    r"\bcompletely\s+solves\b",
    r"chứng\s+minh\s+hoàn\s+toàn",
    r"chắc\s+chắn\s+100%",
    r"giải\s+quyết\s+triệt\s+để\s+mọi",
    r"nghiên\s+cứu\s+đầu\s+tiên\s+và\s+duy\s+nhất",
    r"hiệu\s+quả\s+vượt\s+trội\s+tuyệt\s+đối",
    r"hoàn\s+hảo\s+tuyệt\s+đối",
]

# 5. Boilerplate AI Transitions & Conclusions
AI_CONCLUSIONS_AND_TRANSITIONS = [
    r"\bin\s+conclusion,\s+this\s+study\b",
    r"\bin\s+summary,\s+these\s+findings\b",
    r"\btóm\s+lại,\s+(nghiên\s+cứu|bài\s+viết|luận\s+án)\s+này\b",
    r"nhìn\s+chung,\s+có\s+thể\s+thấy\s+rằng",
]


def analyze_citations(text: str) -> dict:
    """Phân tích tỷ lệ Trích dẫn Tự sự (Narrative) vs. Trích dẫn Thụ động trong ngoặc (Parenthetical)"""
    # Parenthetical pattern: (Author, Year) or (Author et al., Year)
    parenthetical_pattern = r"\([A-ZÀ-Ỹa-zà-ỹ\s&]+,\s+\d{4}[a-z]?\)"
    parenthetical_matches = re.findall(parenthetical_pattern, text)
    
    # Narrative pattern: Author (Year) or Author et al. (Year) or Tác giả và cộng sự (Year)
    narrative_pattern = r"\b[A-ZÀ-Ỹ][a-zà-ỹ]+(?:\s+(?:et\s+al\.|và\s+cộng\s+sự|&|\bvà\b)\s+[A-ZÀ-Ỹ][a-zà-ỹ]+)?\s+\(\d{4}[a-z]?\)"
    narrative_matches = re.findall(narrative_pattern, text)
    
    total_citations = len(parenthetical_matches) + len(narrative_matches)
    narrative_ratio = (len(narrative_matches) / total_citations * 100) if total_citations > 0 else 0
    
    return {
        "parenthetical_count": len(parenthetical_matches),
        "narrative_count": len(narrative_matches),
        "total_citations": total_citations,
        "narrative_ratio": round(narrative_ratio, 1)
    }


def analyze_enumeration_patterns(lines: list) -> list:
    """Phát hiện liệt kê rập khuôn Thứ nhất, Thứ hai, Thứ ba liên tiếp"""
    flags = []
    enum_regex = re.compile(r"^(thứ\s+nhất|thứ\s+hai|thứ\s+ba|thứ\s+tư|firstly|secondly|thirdly)", re.IGNORECASE)
    
    consecutive_count = 0
    start_line = None
    
    for idx, line in enumerate(lines, 1):
        clean = line.strip()
        if enum_regex.search(clean):
            consecutive_count += 1
            if start_line is None:
                start_line = idx
            if consecutive_count >= 3:
                flags.append({
                    "line": start_line,
                    "type": "Mechanical Enumeration Triad",
                    "matched": f"Chuỗi liệt kê {consecutive_count} đoạn từ dòng {start_line}",
                    "context": clean[:100],
                    "suggestion": "Thay thế liệt kê cơ học bằng liên kết dòng chảy lập luận (biện chứng, so sánh đối chiếu quan điểm)."
                })
        else:
            if clean and not clean.startswith("#"):
                consecutive_count = 0
                start_line = None
                
    return flags


def audit_academic_text(text: str) -> dict:
    # Strip References section, embedded SVG blocks, HTML tags, and base64 strings before prose auditing
    body_only = re.split(r'^##\s+REFERENCES\b', text, flags=re.MULTILINE)[0]
    clean_text = re.sub(r'<svg[\s\S]*?</svg>', '', body_only)
    clean_text = re.sub(r'data:image/[^"]+', '', clean_text)
    clean_text = re.sub(r'<[^>]+>', ' ', clean_text)

    lines = clean_text.split("\n")
    issues = []
    
    em_dash_count = len(re.findall(r"—", clean_text))
    
    # Analyze citation balance
    citation_stats = analyze_citations(clean_text)
    if citation_stats["total_citations"] >= 5 and citation_stats["narrative_ratio"] < 25.0:
        issues.append({
            "line": 1,
            "type": "Parenthetical Citation Dumping",
            "matched": f"Narrative Citation Ratio: {citation_stats['narrative_ratio']}% ({citation_stats['narrative_count']}/{citation_stats['total_citations']})",
            "context": "Hầu hết các trích dẫn đều để trong ngoặc đơn cuối câu (Parenthetical) thay vì lồng ghép chủ động vào ngữ pháp của câu.",
            "suggestion": "Tăng cường trích dẫn chủ động (Narrative): 'Komiak và Benbasat (2006) chỉ ra rằng...', 'Theo Oliver (1980)...' (Tối thiểu 30-40% tổng số trích dẫn)."
        })
        
    # Analyze mechanical enumeration
    enum_issues = analyze_enumeration_patterns(lines)
    issues.extend(enum_issues)

    # Analyze excessive inline bolding (visual AI hallmark)
    inline_bolds = len(re.findall(r"\*\*[^*\n]{2,60}\*\*", clean_text))
    if inline_bolds > 60:
        issues.append({
            "line": 1,
            "type": "AI Visual Formatting (Excessive Inline Bolding)",
            "matched": f"{inline_bolds} inline **bold** spans detected",
            "context": "Lạm dụng in đậm giữa đoạn văn (indiscriminate inline bolding) là dấu ấn thị giác điển hình của văn phong AI.",
            "suggestion": "Gỡ bỏ in đậm ở các cụm khái niệm trong câu văn xuôi; chỉ giữ in đậm cho tiêu đề mục, nhãn bảng/hình (Table X, Figure X) hoặc mã giả thuyết/mệnh đề (H1, P1)."
        })
    
    # Sentence length statistics
    sentence_delimiters = re.split(r"[.!?]\s+", clean_text)
    word_counts = [len(s.split()) for s in sentence_delimiters if len(s.split()) > 3]
    std_dev_sentence = statistics.stdev(word_counts) if len(word_counts) > 2 else 0
    mean_sentence = statistics.mean(word_counts) if len(word_counts) > 0 else 0
    
    for idx, line in enumerate(lines, 1):
        clean_line = line.strip()
        if not clean_line or clean_line.startswith("#"):
            continue

        # 1. EN Clichés
        for pattern in EN_AI_CLICHES:
            for m in re.finditer(pattern, clean_line, re.IGNORECASE):
                issues.append({
                    "line": idx,
                    "type": "AI Cliché (EN)",
                    "matched": m.group(0),
                    "context": clean_line,
                    "suggestion": "Dùng thuật ngữ học thuật trung tính và cụ thể."
                })

        # 2. VN Clichés
        for pattern in VN_AI_CLICHES:
            for m in re.finditer(pattern, clean_line, re.IGNORECASE):
                issues.append({
                    "line": idx,
                    "type": "AI Cliché (VN)",
                    "matched": m.group(0),
                    "context": clean_line,
                    "suggestion": "Tránh sáo rỗng báo chí; dùng từ học thuật trung tính."
                })

        # 3. Generic Openers
        for pattern in GENERIC_AI_OPENERS:
            for m in re.finditer(pattern, clean_line, re.IGNORECASE):
                issues.append({
                    "line": idx,
                    "type": "Generic AI Opener",
                    "matched": m.group(0),
                    "context": clean_line,
                    "suggestion": "Mở đầu bằng số liệu thực chứng cụ thể (báo cáo ngành, số liệu kinh tế) hoặc nghịch lý lý thuyết."
                })

        # 4. Absolute claims
        for pattern in ABSOLUTE_CLAIMS:
            for m in re.finditer(pattern, clean_line, re.IGNORECASE):
                issues.append({
                    "line": idx,
                    "type": "Lack of Hedging (Tuyệt đối hóa)",
                    "matched": m.group(0),
                    "context": clean_line,
                    "suggestion": "Áp dụng kỹ thuật khiêm tốn học thuật: 'bước đầu cung cấp bằng chứng', 'có xu hướng gợi mở'."
                })

        # 5. Repetitive conclusions
        for pattern in AI_CONCLUSIONS_AND_TRANSITIONS:
            for m in re.finditer(pattern, clean_line, re.IGNORECASE):
                issues.append({
                    "line": idx,
                    "type": "Repetitive AI Transition / Conclusion",
                    "matched": m.group(0),
                    "context": clean_line,
                    "suggestion": "Viết đoạn kết hoặc chuyển ý tự nhiên gắn với hàm ý thực nghiệm."
                })

    # Calculate Academic Naturalness Score (0 - 100)
    penalty = (len(issues) * 7) + (em_dash_count * 5)
    if citation_stats["total_citations"] > 0 and citation_stats["narrative_ratio"] < 25.0:
        penalty += 10
    score = max(0, min(100, 100 - penalty))

    return {
        "total_lines": len(lines),
        "total_issues": len(issues),
        "em_dash_count": em_dash_count,
        "citation_stats": citation_stats,
        "mean_sentence_length": round(mean_sentence, 1),
        "std_dev_sentence_length": round(std_dev_sentence, 1),
        "naturalness_score": score,
        "issues": issues
    }


def main():
    parser = argparse.ArgumentParser(description="Academic Tone & Anti-AI Audit for Dissertations v2.0")
    parser.add_argument("--file", type=str, required=True, help="Path to text or markdown file")
    parser.add_argument("--strict", action="store_true", help="Exit with code 1 if score < 80 or em-dashes > 0")
    args = parser.parse_args()

    if not os.path.exists(args.file):
        print(f"Error: File not found: {args.file}")
        sys.exit(1)

    with open(args.file, "r", encoding="utf-8", errors="ignore") as f:
        content = f.read()

    result = audit_academic_text(content)

    print("=" * 70)
    print(f"ACADEMIC TONE & ANTI-AI AUDIT REPORT v2.0: {os.path.basename(args.file)}")
    print("=" * 70)
    print(f"Total lines analyzed          : {result['total_lines']}")
    print(f"Academic Naturalness Score    : {result['naturalness_score']} / 100")
    print(f"Em-dashes detected            : {result['em_dash_count']}")
    print(f"Citations Analyzed            : {result['citation_stats']['total_citations']} (Narrative: {result['citation_stats']['narrative_count']}, Parenthetical: {result['citation_stats']['parenthetical_count']})")
    print(f"Narrative Citation Ratio      : {result['citation_stats']['narrative_ratio']}% (Target: >= 30%)")
    print(f"Sentence Length Mean / StdDev : {result['mean_sentence_length']} / {result['std_dev_sentence_length']} words")
    print(f"Total Flags / Issues          : {result['total_issues']}\n")

    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")

    if result["total_issues"] == 0:
        print("[PASS] EXCELLENT: No AI clichés, robotic symmetry, or structural hallmarks detected!")
        print("The manuscript reflects authentic, highly sophisticated doctoral scholarly prose.")
    else:
        print("--- FLAGGED ISSUES & ACTIONS REQUIRED ---")
        for i, issue in enumerate(result["issues"], 1):
            print(f"[{i}] Line {issue['line']} | {issue['type']}")
            print(f"    Target: \"{issue['matched']}\"")
            print(f"    Context: {issue['context'][:100]}")
            print(f"    Fix: {issue['suggestion']}")
            print("-" * 55)

    if args.strict and (result["naturalness_score"] < 80 or result["em_dash_count"] > 0):
        print(f"\n[GATE FAILED] Academic Naturalness Score ({result['naturalness_score']}/100) < 80 or Em-dashes ({result['em_dash_count']}) > 0.")
        sys.exit(1)


if __name__ == "__main__":
    main()
