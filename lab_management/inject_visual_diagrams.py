"""
H-AI ResearchLAB: Inject publication-grade visual components into Paper 1 manuscript
- PRISMA 2020 Flowchart
- VOSviewer 3-Cluster Network Map
- S-O-R Conceptual Framework Model
"""

import os
import re

MANUSCRIPT_PATH = "lab_projects/PAPER_01_SLR_JRCS_MANUSCRIPT.md"

prisma_html = """
<div class="prisma-flow-diagram">
    <div class="prisma-header">
        <h4><i class="fa-solid fa-filter" style="color:#0284c7;"></i> PRISMA 2020 Flow Diagram: Search & Systematic Screening Flow</h4>
        <p>Quy trình thu thập và sàng lọc y văn hệ thống (Scopus, Web of Science & Dimensions 2014–2024)</p>
    </div>
    
    <!-- Stage 1: Identification -->
    <div class="prisma-stage">
        <div class="prisma-stage-label">1. Identification<br>(Xác định)</div>
        <div class="prisma-stage-content">
            <div class="prisma-box main-stream">
                <b>Cơ sở dữ liệu trích xuất ban đầu:</b><br>
                • Scopus, Web of Science, Dimensions: <b>N = 2,500</b> bản ghi
            </div>
            <div class="prisma-box exclude-stream">
                <b>Loại bỏ trước sàng lọc:</b><br>
                • Bản ghi trùng lặp (Duplicates): <b>n = 42</b><br>
                ➔ Bản ghi duy nhất đi tiếp: <b>N = 2,458</b>
            </div>
        </div>
    </div>
    <div class="prisma-arrow-down"><i class="fa-solid fa-arrow-down"></i></div>

    <!-- Stage 2: Screening -->
    <div class="prisma-stage">
        <div class="prisma-stage-label">2. Screening<br>(Sàng lọc)</div>
        <div class="prisma-stage-content">
            <div class="prisma-box main-stream">
                <b>Sàng lọc Tiêu đề & Tóm tắt:</b><br>
                • Tổng số bài được quét độc lập: <b>N = 2,458</b>
            </div>
            <div class="prisma-box exclude-stream">
                <b>Bản ghi bị loại trừ (n = 701):</b>
                <ul>
                    <li>Bản thảo chưa bình duyệt (SSRN, Preprints): <b>n = 129</b></li>
                    <li>Kỷ yếu hội thảo (Conference Proceedings): <b>n = 357</b></li>
                    <li>Xuất bản trước 2018 (ngoài khung công nghệ): <b>n = 153</b></li>
                    <li>Tóm tắt không đạt chuẩn (&lt; 30 từ): <b>n = 62</b></li>
                </ul>
            </div>
        </div>
    </div>
    <div class="prisma-arrow-down"><i class="fa-solid fa-arrow-down"></i></div>

    <!-- Stage 3: Eligibility -->
    <div class="prisma-stage">
        <div class="prisma-stage-label">3. Eligibility<br>(Đánh giá)</div>
        <div class="prisma-stage-content">
            <div class="prisma-box main-stream">
                <b>Đánh giá Toàn văn chuyên sâu:</b><br>
                • Số lượng bài báo đọc toàn văn: <b>N = 1,757</b>
            </div>
            <div class="prisma-box exclude-stream">
                <b>Toàn văn bị loại trừ có lý do (n = 316):</b>
                <ul>
                    <li>Không đo lường hành vi người tiêu dùng: <b>n = 226</b></li>
                    <li>Thiếu yếu tố thuật toán đề xuất: <b>n = 71</b></li>
                    <li>Thuần kỹ thuật phần cứng/y tế: <b>n = 19</b></li>
                </ul>
            </div>
        </div>
    </div>
    <div class="prisma-arrow-down"><i class="fa-solid fa-arrow-down"></i></div>

    <!-- Stage 4: Included -->
    <div class="prisma-stage">
        <div class="prisma-stage-label">4. Included<br>(Thu nạp)</div>
        <div class="prisma-stage-content" style="grid-template-columns: 1fr;">
            <div class="prisma-box main-stream" style="border-color:#10b981; background:#ecfdf5; padding:1.2rem;">
                <div style="font-size:1rem; font-weight:800; color:#065f46; margin-bottom:0.4rem;">
                    <i class="fa-solid fa-circle-check" style="color:#10b981;"></i> TỔNG HỢP CỐT LÕI Y VĂN ĐÃ BÌNH DUYỆT (CORE SLR CORPUS): N = 1,441 BÀI BÁO
                </div>
                <div style="font-size:0.85rem; color:#047857; line-height:1.6;">
                    • 100% công bố trên tạp chí quốc tế xếp hạng Scopus Q1/Q2 (JRCS: 34 bài, CHB: 28 bài, JBR: 22 bài, I&M: 19 bài...)<br>
                    • <b>Mạng lưới Trắc lượng thư mục VOSviewer:</b> Chọn lọc <b>N = 866 bài nòng cốt</b> có số trích dẫn ≥ 10 kết nối qua 250 liên kết đồng xuất hiện từ khóa.
                </div>
            </div>
        </div>
    </div>
</div>
"""

vos_html = """
<div class="vos-cluster-card">
    <div class="vos-cluster-header">
        <h4><i class="fa-solid fa-diagram-project" style="color:#0284c7;"></i> Figure 1: Tri-Cluster Bibliometric Co-Occurrence Network Map (VOSviewer)</h4>
        <a href="http://localhost:8600" target="_blank" class="vos-link-btn">
            <i class="fa-solid fa-arrow-up-right-from-square"></i> Mở VOSviewer Trực Tiếp (Port 8600)
        </a>
    </div>

    <!-- Interactive SVG Network Diagram -->
    <svg viewBox="0 0 800 240" style="width:100%; height:auto; background:#f8fafc; border-radius:8px; border:1px solid #e2e8f0; margin:0.5rem 0 1rem 0;">
        <!-- Connecting Links -->
        <line x1="180" y1="120" x2="400" y2="120" stroke="#94a3b8" stroke-width="3" stroke-dasharray="4" />
        <line x1="400" y1="120" x2="620" y2="120" stroke="#94a3b8" stroke-width="3" stroke-dasharray="4" />
        <path d="M 180 100 Q 400 20 620 100" fill="none" stroke="#cbd5e1" stroke-width="2" stroke-dasharray="6" />

        <!-- Link Labels -->
        <text x="290" y="110" fill="#64748b" font-size="11" font-family="sans-serif" font-weight="bold">Cognitive Fit</text>
        <text x="510" y="110" fill="#64748b" font-size="11" font-family="sans-serif" font-weight="bold">Affective Urge</text>
        <text x="400" y="48" fill="#94a3b8" font-size="11" font-family="sans-serif" text-anchor="middle">Direct Algorithmic Influence</text>

        <!-- Cluster 1: Red Node (Stimulus) -->
        <circle cx="180" cy="120" r="55" fill="#ffe4e6" stroke="#f43f5e" stroke-width="3" />
        <text x="180" y="112" text-anchor="middle" fill="#9f1239" font-size="12" font-family="sans-serif" font-weight="bold">CLUSTER 1</text>
        <text x="180" y="128" text-anchor="middle" fill="#e11d48" font-size="10" font-family="sans-serif">(Stimulus - S)</text>
        <text x="180" y="142" text-anchor="middle" fill="#881337" font-size="9" font-family="sans-serif">AI Algorithms (348)</text>

        <!-- Cluster 2: Green Node (Organism) -->
        <circle cx="400" cy="120" r="55" fill="#dcfce7" stroke="#10b981" stroke-width="3" />
        <text x="400" y="112" text-anchor="middle" fill="#065f46" font-size="12" font-family="sans-serif" font-weight="bold">CLUSTER 2</text>
        <text x="400" y="128" text-anchor="middle" fill="#059669" font-size="10" font-family="sans-serif">(Organism - O)</text>
        <text x="400" y="142" text-anchor="middle" fill="#064e3b" font-size="9" font-family="sans-serif">E-Satisfaction (174)</text>

        <!-- Cluster 3: Blue Node (Response) -->
        <circle cx="620" cy="120" r="55" fill="#dbeafe" stroke="#3b82f6" stroke-width="3" />
        <text x="620" y="112" text-anchor="middle" fill="#1e40af" font-size="12" font-family="sans-serif" font-weight="bold">CLUSTER 3</text>
        <text x="620" y="128" text-anchor="middle" fill="#2563eb" font-size="10" font-family="sans-serif">(Response - R)</text>
        <text x="620" y="142" text-anchor="middle" fill="#1e3a8a" font-size="9" font-family="sans-serif">Impulse Buying (344)</text>
    </svg>

    <div class="cluster-grid">
        <div class="cluster-item red">
            <h5><i class="fa-solid fa-microchip"></i> Cụm 1: Thuật toán AI (S)</h5>
            <b>348 bài báo:</b> Recommendation Systems, Collaborative Filtering, Deep Learning, Perceived Personalization, Accuracy, Novelty.
        </div>
        <div class="cluster-item green">
            <h5><i class="fa-solid fa-heart-pulse"></i> Cụm 2: Cơ thể Tâm lý (O)</h5>
            <b>174 bài báo:</b> Cumulative E-Satisfaction, Trust, Cognitive Fit, Flow State, Perceived Value, Affective Comfort.
        </div>
        <div class="cluster-item blue">
            <h5><i class="fa-solid fa-cart-shopping"></i> Cụm 3: Phản ứng Mua sắm (R)</h5>
            <b>344 bài báo:</b> Urge to Buy Impulsively (UBI), Online Impulse Buying (IB), Ego Depletion, Self-Control Failure.
        </div>
    </div>
</div>
"""

sor_html = """
<div class="sor-diagram-box">
    <div style="text-align:center; margin-bottom:1.25rem;">
        <h4 style="font-size:1.15rem; font-weight:800; color:#0f172a; margin-bottom:0.25rem;">
            Figure 2: Integrative Conceptual Model & Hypothesized Structural Relationships
        </h4>
        <p style="font-size:0.825rem; color:#64748b; margin-bottom:0;">
            Mô hình S-O-R mở rộng tích hợp Thuyết Tương Thích Nhận Thức (Cognitive Fit) và Mô Hình Nguồn Lực Tự Kiểm Soát (Baumeister Ego Depletion)
        </p>
    </div>

    <!-- Visual Responsive S-O-R Flow -->
    <div class="sor-grid">
        <!-- STIMULUS COL -->
        <div class="sor-col stimulus">
            <div class="sor-col-title" style="color:#e11d48;"><i class="fa-solid fa-bolt"></i> STIMULUS (S)<br><span style="font-size:0.75rem; font-weight:600;">Đặc tính thuật toán AI</span></div>
            <div style="background:#fff; border:1px solid #fecdd3; padding:0.5rem; border-radius:6px; margin-bottom:0.5rem; font-size:0.8rem; font-weight:700;">
                Cá nhân hóa cảm nhận (PP)
            </div>
            <div style="background:#fff; border:1px solid #fecdd3; padding:0.5rem; border-radius:6px; margin-bottom:0.5rem; font-size:0.8rem; font-weight:700;">
                Độ chính xác cảm nhận (ACC)
            </div>
            <div style="background:#fff; border:1px solid #fecdd3; padding:0.5rem; border-radius:6px; font-size:0.8rem; font-weight:700;">
                Tính mới & Tình cờ (NOV)
            </div>
        </div>

        <div style="display:flex; flex-direction:column; align-items:center; justify-content:center;">
            <span style="font-size:0.75rem; font-weight:800; color:#0284c7; background:#e0f2fe; padding:0.2rem 0.5rem; border-radius:4px; margin-bottom:0.25rem;">H1, H2, H4 (+)</span>
            <span class="sor-arrow"><i class="fa-solid fa-arrow-right"></i></span>
        </div>

        <!-- ORGANISM COL -->
        <div class="sor-col organism">
            <div class="sor-col-title" style="color:#059669;"><i class="fa-solid fa-heart"></i> ORGANISM (O)<br><span style="font-size:0.75rem; font-weight:600;">Trạng thái tâm lý trung gian</span></div>
            <div style="background:#fff; border:2px solid #10b981; padding:1.25rem 0.75rem; border-radius:8px; font-size:0.95rem; font-weight:800; color:#065f46;">
                SỰ HÀI LÒNG ĐIỆN TỬ TÍCH LŨY (ES)
            </div>
        </div>

        <div style="display:flex; flex-direction:column; align-items:center; justify-content:center;">
            <span style="font-size:0.75rem; font-weight:800; color:#0284c7; background:#e0f2fe; padding:0.2rem 0.5rem; border-radius:4px; margin-bottom:0.25rem;">H3 (+)</span>
            <span class="sor-arrow"><i class="fa-solid fa-arrow-right"></i></span>
        </div>

        <!-- RESPONSE COL -->
        <div class="sor-col response">
            <div class="sor-col-title" style="color:#2563eb;"><i class="fa-solid fa-cart-shopping"></i> RESPONSE (R)<br><span style="font-size:0.75rem; font-weight:600;">Phản ứng hành vi</span></div>
            <div style="background:#fff; border:1px solid #bfdbfe; padding:0.6rem; border-radius:6px; margin-bottom:0.75rem; font-size:0.85rem; font-weight:700;">
                Thôi thúc mua bốc đồng (UBI)
            </div>
            <div style="font-size:1.1rem; color:#0284c7; margin:-0.3rem 0;"><i class="fa-solid fa-arrow-down"></i> <span style="font-size:0.75rem; font-weight:800;">H5 (+)</span></div>
            <div style="background:#fff; border:2px solid #3b82f6; padding:0.6rem; border-radius:6px; font-size:0.85rem; font-weight:800; color:#1e40af;">
                Hành vi mua bốc đồng (IB)
            </div>
        </div>
    </div>

    <!-- MODERATOR BOX -->
    <div style="background:#f8fafc; border:2px dashed #f59e0b; border-radius:8px; padding:0.85rem; text-align:center; max-width:480px; margin:0 auto;">
        <div style="font-size:0.75rem; font-weight:800; color:#d97706; text-transform:uppercase; margin-bottom:0.2rem;">
            <i class="fa-solid fa-shield-halved"></i> YẾU TỐ ĐIỀU TIẾT (MODERATOR) - H6 (+)
        </div>
        <div style="font-size:0.875rem; font-weight:700; color:#b45309;">
            Sự Cạn Kiệt Nguồn Lực Tự Kiểm Soát (Ego Depletion - EGO)
        </div>
        <div style="font-size:0.75rem; color:#78350f; margin-top:0.2rem;">
            Tác động điều tiết tăng cường: Khi người tiêu dùng cạn kiệt ý chí, quan hệ giữa UBI và IB càng mạnh mẽ hơn.
        </div>
    </div>
</div>
"""

with open(MANUSCRIPT_PATH, 'r', encoding='utf-8') as f:
    text = f.read()

# Replace PRISMA ASCII block
prisma_pattern = r'```\s*┌─+┐\s*│\s*PRISMA 2020 FLOW DIAGRAM\s*│[\s\S]*?```'
if re.search(prisma_pattern, text):
    text = re.sub(prisma_pattern, prisma_html, text)
    print("[OK] Replaced PRISMA ASCII block with rich visual HTML component!")
else:
    print("[!] Could not match PRISMA ASCII block.")

# Replace TRI-CLUSTER ASCII block
cluster_pattern = r'```\s*┌─+┐\s*│\s*TRI-CLUSTER BIBLIOMETRIC NETWORK\s*│[\s\S]*?```'
if re.search(cluster_pattern, text):
    text = re.sub(cluster_pattern, vos_html, text)
    print("[OK] Replaced TRI-CLUSTER ASCII block with rich visual HTML component!")
else:
    print("[!] Could not match TRI-CLUSTER ASCII block.")

# Replace CONCEPTUAL MODEL ASCII block
sor_pattern = r'```\s*┌─+┐\s*│\s*INTEGRATIVE CONCEPTUAL MODEL\s*│[\s\S]*?```'
if re.search(sor_pattern, text):
    text = re.sub(sor_pattern, sor_html, text)
    print("[OK] Replaced CONCEPTUAL MODEL ASCII block with rich visual HTML component!")
else:
    print("[!] Could not match CONCEPTUAL MODEL ASCII block.")

with open(MANUSCRIPT_PATH, 'w', encoding='utf-8') as f:
    f.write(text)

print(f"[SUCCESS] Updated {MANUSCRIPT_PATH} with publication-grade visual diagrams!")
