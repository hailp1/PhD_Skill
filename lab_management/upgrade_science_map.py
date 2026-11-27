import re

def upgrade_science_map():
    with open('web/interactive_science_map.html', 'r', encoding='utf-8') as f:
        html = f.read()

    # 1. Add FontAwesome in head if not present
    if 'fontawesome' not in html.lower():
        html = html.replace('</head>', '    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">\n</head>')

    # 2. Add Export & Theme tools in header
    header_tools = '''        <!-- Công cụ Xuất Ảnh Thực Tế & Đổi Theme -->
        <div class="flex items-center space-x-2">
            <button id="btnThemeToggle" onclick="toggleTheme()" class="px-3 py-1.5 bg-slate-800 hover:bg-slate-700 border border-slate-700 rounded-lg text-xs font-semibold text-slate-200 transition" title="Chuyển sang nền trắng để chụp/xuất bài báo">
                ☀️ Nền Trắng Học Thuật
            </button>
            <button onclick="exportHighResVOS('png')" class="px-3 py-1.5 bg-emerald-600 hover:bg-emerald-500 rounded-lg text-xs font-bold text-white shadow-sm transition flex items-center gap-1.5" title="Xuất hình ảnh độ phân giải cao 300 DPI">
                <i class="fa-solid fa-camera"></i> Xuất PNG (300 DPI)
            </button>
            <button onclick="exportHighResVOS('svg')" class="px-3 py-1.5 bg-sky-600 hover:bg-sky-500 rounded-lg text-xs font-bold text-white shadow-sm transition flex items-center gap-1.5" title="Tải tệp đồ họa vector SVG chuẩn Elsevier">
                <i class="fa-solid fa-file-code"></i> Tải SVG Vector
            </button>
        </div>'''

    if 'id="btnThemeToggle"' not in html:
        # insert before </header>
        html = html.replace('</header>', header_tools + '\n    </header>')

    # 3. Add Theme support in draw() and export functions before </script>
    js_code = '''
        // ================= XUẤT ẢNH THỰC TẾ VÀ ĐỔI GIAO DIỆN HỌC THUẬT =================
        let isWhiteTheme = false;

        function toggleTheme() {
            isWhiteTheme = !isWhiteTheme;
            const btn = document.getElementById('btnThemeToggle');
            if (isWhiteTheme) {
                btn.innerHTML = '🌙 Nền Tối Lab';
                btn.className = "px-3 py-1.5 bg-indigo-900 border border-indigo-700 rounded-lg text-xs font-semibold text-white transition";
                canvas.style.backgroundColor = '#ffffff';
            } else {
                btn.innerHTML = '☀️ Nền Trắng Học Thuật';
                btn.className = "px-3 py-1.5 bg-slate-800 hover:bg-slate-700 border border-slate-700 rounded-lg text-xs font-semibold text-slate-200 transition";
                canvas.style.backgroundColor = '#0f172a';
            }
            draw();
        }

        function exportHighResVOS(format) {
            if (format === 'svg') {
                // Tải trực tiếp file vector SVG thực tế của VOSviewer
                const a = document.createElement('a');
                a.href = '../lab_projects/figures/figure2_vosviewer_real_network.svg';
                a.download = 'Figure2_VOSviewer_Real_Network_Map_TDTU.svg';
                document.body.appendChild(a);
                a.click();
                document.body.removeChild(a);
                return;
            }

            if (format === 'png') {
                // Tạo Canvas 300 DPI độ phân giải cao (3600 x 2400)
                const exportCanvas = document.createElement('canvas');
                exportCanvas.width = 3600;
                exportCanvas.height = 2400;
                const ectx = exportCanvas.getContext('2d');

                // Nền trắng chuẩn xuất bản tạp chí Scopus Q1
                ectx.fillStyle = '#ffffff';
                ectx.fillRect(0, 0, exportCanvas.width, exportCanvas.height);

                const expScale = 3600 / width * 0.95;
                const expOffsetX = exportCanvas.width / 2;
                const expOffsetY = exportCanvas.height / 2 + 60;
                const spread = Math.min(exportCanvas.width, exportCanvas.height) * 0.44;

                // 1. Tiêu đề chuẩn Elsevier
                ectx.fillStyle = '#0f172a';
                ectx.font = 'bold 44px -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif';
                ectx.textAlign = 'center';
                ectx.fillText('FIGURE 2: EMPIRICAL BIBLIOMETRIC CO-OCCURRENCE NETWORK MAP (VOSVIEWER)', exportCanvas.width / 2, 80);

                ectx.fillStyle = '#64748b';
                ectx.font = '26px sans-serif';
                ectx.fillText('Corpus: N = 1,441 core publications (2014-2024) | Fractional Counting | VOSviewer v1.6.20 Output', exportCanvas.width / 2, 125);

                // 2. Vẽ tất cả các liên kết (Edges)
                edges.forEach(e => {
                    const src = nodes.find(n => n.id === e.source);
                    const tgt = nodes.find(n => n.id === e.target);
                    if (!src || !tgt) return;

                    const x1 = expOffsetX + src.x * spread;
                    const y1 = expOffsetY + src.y * spread;
                    const x2 = expOffsetX + tgt.x * spread;
                    const y2 = expOffsetY + tgt.y * spread;

                    ectx.beginPath();
                    ectx.moveTo(x1, y1);
                    ectx.lineTo(x2, y2);
                    ectx.strokeStyle = src.cluster === tgt.cluster ? clusterColors[src.cluster] : '#94a3b8';
                    ectx.lineWidth = Math.max(1.5, e.weight * 0.4);
                    ectx.globalAlpha = Math.max(0.2, Math.min(0.7, e.weight * 0.04));
                    ectx.stroke();
                });
                ectx.globalAlpha = 1.0;

                // 3. Vẽ tất cả các nút (Nodes)
                nodes.forEach(n => {
                    const nx = expOffsetX + n.x * spread;
                    const ny = expOffsetY + n.y * spread;
                    const r = 16 + Math.sqrt(n.occ) * 3.8;

                    ectx.beginPath();
                    ectx.arc(nx, ny, r, 0, Math.PI * 2);
                    ectx.fillStyle = clusterColors[n.cluster];
                    ectx.fill();
                    ectx.lineWidth = 5;
                    ectx.strokeStyle = '#ffffff';
                    ectx.stroke();
                });

                // 4. Vẽ nhãn từ khóa (Pill badges)
                nodes.forEach(n => {
                    const nx = expOffsetX + n.x * spread;
                    const ny = expOffsetY + n.y * spread;
                    const r = 16 + Math.sqrt(n.occ) * 3.8;
                    const fontSize = Math.max(22, 20 + Math.sqrt(n.occ) * 0.85);

                    ectx.font = 'bold ' + fontSize + 'px sans-serif';
                    const textMetrics = ectx.measureText(n.label);
                    const bw = textMetrics.width + 24;
                    const bh = fontSize + 16;
                    const bx = nx - bw / 2;
                    let by = ny + r + 8;
                    if (by + bh > exportCanvas.height - 120) by = ny - r - bh - 8;

                    // Badge nền trắng
                    ectx.fillStyle = '#ffffff';
                    ectx.strokeStyle = clusterColors[n.cluster];
                    ectx.lineWidth = 3;
                    ectx.fillRect(bx, by, bw, bh);
                    ectx.strokeRect(bx, by, bw, bh);

                    // Chữ
                    ectx.fillStyle = clusterColors[n.cluster];
                    ectx.textAlign = 'center';
                    ectx.fillText(n.label, nx, by + fontSize + 2);
                });

                // 5. Chú thích Cụm ở chân trang (Footer Legend)
                const clusterLegends = [
                    { cid: 1, name: 'Cluster 1: Algorithmic Stimuli (S)', sub: '348 articles | AI & Personalization' },
                    { cid: 2, name: 'Cluster 2: Experiential Organism (O)', sub: '174 articles | E-Satisfaction & Trust' },
                    { cid: 3, name: 'Cluster 3: Behavioral Response (R)', sub: '344 articles | Impulse Buying & UBI' },
                    { cid: 4, name: 'Cluster 4: Boundary Condition (M)', sub: '62 articles | Ego Depletion & Friction' }
                ];

                const legY = exportCanvas.height - 70;
                clusterLegends.forEach((cl, i) => {
                    const lx = 180 + i * 820;
                    ectx.beginPath();
                    ectx.arc(lx, legY, 14, 0, Math.PI * 2);
                    ectx.fillStyle = clusterColors[cl.cid];
                    ectx.fill();
                    ectx.lineWidth = 3;
                    ectx.strokeStyle = '#ffffff';
                    ectx.stroke();

                    ectx.fillStyle = clusterColors[cl.cid];
                    ectx.font = 'bold 24px sans-serif';
                    ectx.textAlign = 'left';
                    ectx.fillText(cl.name, lx + 25, legY + 2);

                    ectx.fillStyle = '#64748b';
                    ectx.font = '19px sans-serif';
                    ectx.fillText(cl.sub, lx + 25, legY + 28);
                });

                // Tải xuống PNG
                exportCanvas.toBlob(blob => {
                    const url = URL.createObjectURL(blob);
                    const a = document.createElement('a');
                    a.href = url;
                    a.download = 'Figure2_VOSviewer_Network_Map_300DPI_TDTU.png';
                    document.body.appendChild(a);
                    a.click();
                    document.body.removeChild(a);
                    URL.revokeObjectURL(url);
                }, 'image/png');
            }
        }
'''

    if 'function exportHighResVOS' not in html:
        html = html.replace('window.onload = () => {', js_code + '\n        window.onload = () => {')

    with open('web/interactive_science_map.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print("Successfully upgraded web/interactive_science_map.html with real export features!")

if __name__ == '__main__':
    upgrade_science_map()
