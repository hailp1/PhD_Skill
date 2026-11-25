"""
Script: pipeline_prisma_vosviewer.py
Mô tả: 
  ĐIỀU PHỐI TOÀN DIỆN LUỒNG CÔNG VIỆC TỔNG QUAN Y VĂN (MASTER PIPELINE):
  (1) Nạp tệp dữ liệu thô từ Dimensions / Scopus
  (2) Tự động lọc sạch theo 4 giai đoạn PRISMA 2020
  (3) Trích xuất ma trận từ khóa và đồng xuất hiện thực nghiệm
  (4) Tự động nạp vào VOSviewer Online chính thức của Đại học Leiden
Tác giả: Ph.D. Advisory System - Marketing & QTKD
"""

import os
import sys
import glob
import subprocess
from clean_dimensions_prisma import clean_data as run_prisma_clean
from process_real_bibliometric_network import run_real_bibliometric_mapping as run_mapping

def main():
    print("=" * 75)
    print("   QUY TRÌNH TỔNG QUAN Y VĂN TỰ ĐỘNG HÓA: PRISMA 2020 -> VOSVIEWER ONLINE")
    print("   NCS: Lê Phúc Hải - Trường Đại học Tôn Đức Thắng (TDTU)")
    print("=" * 75)

    workspace = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..", ".."))
    sys_dir = os.path.join(workspace, "data", "raw")
    raw_files = glob.glob(os.path.join(sys_dir, "*.csv"))

    if not raw_files:
        print("[LỖI] Không tìm thấy tệp dữ liệu thô dạng '*.csv' trong thư mục data/raw/.")
        return

    latest_raw = max(raw_files, key=os.path.getctime)
    print(f"\n[BƯỚC 1/3] Phát hiện tệp dữ liệu đầu vào: {os.path.basename(latest_raw)}")

    print("\n[BƯỚC 2/3] Thực thi giao thức sàng lọc PRISMA 2020...")
    from clean_dimensions_prisma import clean_data
    clean_data()

    print("\n[BƯỚC 3/3] Trích xuất dữ liệu thực chứng và kết nối VOSviewer Online...")
    from process_real_bibliometric_network import run_real_bibliometric_mapping
    run_real_bibliometric_mapping()

    print("\n" + "=" * 75)
    print("   HOÀN TẤT QUY TRÌNH! DỮ LIỆU ĐÃ SẴN SÀNG CHO VOSVIEWER ONLINE")
    print("=" * 75)
    print("-> Bạn có thể mở VOSviewer Online chính thức bằng 2 cách:")
    print("   1. Nhấp đúp vào tệp: CHAY_VOSVIEWER_ONLINE.bat (Chạy local trên trình duyệt port 8600)")
    print("   2. Hoặc mở: https://app.vosviewer.com -> Bấm 'Open' -> Chọn file: 'vos_map_keywords.txt' & 'vos_network_keywords.txt'")
    print("=" * 75)

if __name__ == "__main__":
    main()
