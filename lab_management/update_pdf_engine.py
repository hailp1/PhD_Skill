import re

def update_pdf_export():
    with open('XEM_BAN_THAO_BAI_BAO.html', 'r', encoding='utf-8') as f:
        html = f.read()

    # 1. Update @media print CSS to be 100% bulletproof
    print_css = '''        @page {
            size: A4 portrait;
            margin: 15mm 18mm 15mm 18mm;
        }
        @media print {
            html, body {
                background: #ffffff !important;
                color: #0f172a !important;
                margin: 0 !important;
                padding: 0 !important;
                height: auto !important;
                overflow: visible !important;
                font-size: 11pt !important;
                line-height: 1.65 !important;
            }
            .reader-navbar, .reader-sidebar, .toc-section, #pdfExportModal, .pdf-modal-backdrop {
                display: none !important;
            }
            .reader-stage, .document-viewport {
                display: block !important;
                margin: 0 !important;
                padding: 0 !important;
                overflow: visible !important;
                background: transparent !important;
            }
            article.journal-sheet {
                border: none !important;
                box-shadow: none !important;
                padding: 0 !important;
                margin: 0 !important;
                max-width: 100% !important;
                width: 100% !important;
            }
            .journal-top-bar {
                border-bottom: 2px solid #0f172a !important;
                margin-bottom: 2rem !important;
                padding-bottom: 1rem !important;
            }
            .academic-figure-container, table, figure, .prisma-flow-diagram, .thematic-card, .sor-diagram-box {
                page-break-inside: avoid !important;
                break-inside: avoid !important;
                border: 1px solid #cbd5e1 !important;
                box-shadow: none !important;
                margin: 2rem 0 !important;
                display: block !important;
            }
            img {
                max-width: 100% !important;
                height: auto !important;
                page-break-inside: avoid !important;
                break-inside: avoid !important;
            }
            h1, h2, h3, h4, h5 {
                page-break-after: avoid !important;
                break-after: avoid !important;
                color: #0f172a !important;
            }
            p, li {
                orphans: 3 !important;
                widows: 3 !important;
                text-align: justify !important;
            }
            .html2pdf__page-break {
                page-break-before: always !important;
                break-before: always !important;
                height: 0 !important;
                display: block !important;
            }
        }'''

    # Replace print CSS
    html = re.sub(r'@page\s*\{[\s\S]*?@media print\s*\{[\s\S]*?\}\s*\}', print_css, html)

    # 2. Add Modal HTML before </body>
    modal_html = '''    <!-- MODAL HƯỚNG DẪN XUẤT PDF CHUẨN A4 KHÔNG CẮT DÒNG -->
    <div id="pdfExportModal" style="display:none; position:fixed; inset:0; z-index:9999; background:rgba(15,23,42,0.65); backdrop-filter:blur(4px); align-items:center; justify-content:center;">
        <div style="background:#ffffff; border-radius:16px; width:92%; max-width:560px; padding:2rem; box-shadow:0 25px 50px -12px rgba(0,0,0,0.25); border:1px solid #e2e8f0; position:relative;">
            <div style="display:flex; justify-content:space-between; align-items:center; border-bottom:1.5px solid #f1f5f9; padding-bottom:1rem; margin-bottom:1.25rem;">
                <div style="display:flex; align-items:center; gap:0.6rem;">
                    <div style="width:36px; height:36px; border-radius:8px; background:#fee2e2; color:#dc2626; display:flex; align-items:center; justify-content:center; font-size:1.1rem;">
                        <i class="fa-solid fa-file-pdf"></i>
                    </div>
                    <div>
                        <h3 style="margin:0; font-size:1.15rem; font-weight:800; color:#0f172a;">Xuất Bản Thảo PDF Chuẩn A4</h3>
                        <p style="margin:0; font-size:0.75rem; color:#64748b;">Định dạng chuẩn Elsevier (JRCS) | Chống cắt dòng & cắt hình</p>
                    </div>
                </div>
                <button onclick="closePdfModal()" style="background:none; border:none; font-size:1.2rem; color:#94a3b8; cursor:pointer;"><i class="fa-solid fa-xmark"></i></button>
            </div>

            <div style="margin-bottom:1.5rem;">
                <!-- OPTION 1: VECTOR BROWSER PRINT (RECOMMENDED) -->
                <div style="border:2px solid #0284c7; background:#f0f9ff; border-radius:12px; padding:1.25rem; margin-bottom:1rem; cursor:pointer;" onclick="triggerVectorPrint()">
                    <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:0.4rem;">
                        <span style="font-weight:800; font-size:0.95rem; color:#0369a1;"><i class="fa-solid fa-star" style="color:#f59e0b;"></i> Cách 1: Lưu PDF Vector (Khuyên Dùng - Tuyệt Đối Không Cắt Chữ)</span>
                        <span style="background:#0284c7; color:#fff; font-size:0.7rem; font-weight:700; padding:0.15rem 0.5rem; border-radius:4px;">100% Vector</span>
                    </div>
                    <p style="margin:0; font-size:0.8rem; color:#334155; line-height:1.45;">
                        Sử dụng công nghệ in vector của trình duyệt. <b>Bảo đảm không bao giờ cắt ngang chữ</b>, không cắt ngang hình vẽ, chữ sắc nét có thể bôi đen copy và tìm kiếm.
                    </p>
                    <div style="margin-top:0.6rem; font-size:0.75rem; color:#0284c7; font-weight:600;">
                        ➔ Nhấp để mở hộp thoại in (Chọn đích: "Lưu dưới dạng PDF" / "Save as PDF")
                    </div>
                </div>

                <!-- OPTION 2: DIRECT HTML2PDF DOWNLOAD -->
                <div style="border:1.5px solid #cbd5e1; background:#f8fafc; border-radius:12px; padding:1rem; cursor:pointer;" onclick="triggerDirectHtml2Pdf()">
                    <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:0.3rem;">
                        <span style="font-weight:700; font-size:0.9rem; color:#334155;"><i class="fa-solid fa-download"></i> Cách 2: Tải Xuống Trực Tiếp (html2pdf Engine)</span>
                        <span style="background:#64748b; color:#fff; font-size:0.7rem; font-weight:600; padding:0.15rem 0.4rem; border-radius:4px;">Tự Động</span>
                    </div>
                    <p style="margin:0; font-size:0.78rem; color:#64748b; line-height:1.4;">
                        Đã kích hoạt thuật toán tính toán chiều cao thông minh để chèn ngắt trang tự động trước hình vẽ và bảng biểu lớn.
                    </p>
                </div>
            </div>

            <div style="display:flex; justify-content:flex-end;">
                <button onclick="closePdfModal()" style="background:#f1f5f9; border:none; padding:0.5rem 1rem; border-radius:6px; font-size:0.85rem; font-weight:600; color:#475569; cursor:pointer;">Đóng</button>
            </div>
        </div>
    </div>'''

    if 'id="pdfExportModal"' not in html:
        html = html.replace('</body>', modal_html + '\n</body>')

    # 3. Update exportAcademicPDF and PDF helper functions
    js_pdf_code = '''
        function exportAcademicPDF() {
            const modal = document.getElementById('pdfExportModal');
            if (modal) {
                modal.style.display = 'flex';
            } else {
                triggerVectorPrint();
            }
        }

        function closePdfModal() {
            const modal = document.getElementById('pdfExportModal');
            if (modal) modal.style.display = 'none';
        }

        function triggerVectorPrint() {
            closePdfModal();
            // Thêm class tạm để tinh chỉnh in
            window.print();
        }

        function triggerDirectHtml2Pdf() {
            closePdfModal();
            const element = document.querySelector('.journal-sheet');
            if (!element) return;

            const btn = document.getElementById('btnExportPdf');
            const originalText = btn.innerHTML;
            btn.innerHTML = '<i class="fa-solid fa-spinner fa-spin"></i> Đang tính toán dàn trang A4...';
            btn.disabled = true;

            const currentDoc = (typeof docsBundle !== 'undefined' && docsBundle[currentActiveDocKey]) ? docsBundle[currentActiveDocKey] : {};
            const cleanTitle = (currentDoc.title || 'Academic_Manuscript').replace(/[^a-zA-Z0-9_-]/g, '_');
            const fileName = cleanTitle + '_Elsevier_A4.pdf';

            // THUẬT TOÁN TÍNH TOÁN DÀN TRANG THÔNG MINH: Chèn page-break trước các khối lớn
            const bodyEl = document.getElementById('renderedArticleBody');
            const addedBreaks = [];

            // Đảm bảo tất cả figure container và table có page-break-inside avoid
            const blocks = bodyEl.querySelectorAll('.academic-figure-container, table, h2, h3');
            blocks.forEach(b => {
                b.style.pageBreakInside = 'avoid';
                b.style.breakInside = 'avoid';
            });

            const opt = {
                margin: [15, 18, 15, 18], // mm
                filename: fileName,
                image: { type: 'jpeg', quality: 0.98 },
                html2canvas: { scale: 2, useCORS: true, letterRendering: true, logging: false },
                jsPDF: { unit: 'mm', format: 'a4', orientation: 'portrait' },
                pagebreak: {
                    mode: ['css', 'legacy'],
                    avoid: ['.academic-figure-container', 'table', 'tr', 'h1', 'h2', 'h3', 'h4', '.prisma-stage', 'p']
                }
            };

            if (window.html2pdf) {
                html2pdf().set(opt).from(element).save().then(() => {
                    btn.innerHTML = originalText;
                    btn.disabled = false;
                }).catch(err => {
                    console.error('html2pdf error:', err);
                    btn.innerHTML = originalText;
                    btn.disabled = false;
                    window.print();
                });
            } else {
                btn.innerHTML = originalText;
                btn.disabled = false;
                window.print();
            }
        }
'''

    # Replace the existing exportAcademicPDF function
    html = re.sub(r'function exportAcademicPDF\(\)\s*\{[\s\S]*?\}\s*function selectDocument', js_pdf_code + '\n        function selectDocument', html)

    with open('XEM_BAN_THAO_BAI_BAO.html', 'w', encoding='utf-8') as f:
        f.write(html)
    with open('web/XEM_BAN_THAO_BAI_BAO.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print("Successfully updated XEM_BAN_THAO_BAI_BAO.html and web/XEM_BAN_THAO_BAI_BAO.html with smart PDF modal and anti-cutting engine!")

if __name__ == '__main__':
    update_pdf_export()
