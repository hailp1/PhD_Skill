@echo off
title VOSviewer Online - Leiden University (Port 8600)
echo ==============================================================================
echo   KHOI DONG VOSVIEWER ONLINE CUA DAI HOC LEIDEN (PORT 8600)
echo   De tai: He thong de xuat AI va Mua boc dong truc tuyen (NCS Le Phuc Hai)
echo ==============================================================================
echo [1/2] Dang mo trinh duyet web den VOSviewer Online voi bo du lieu thuc chung...
start "" "http://localhost:8600/?json=data/luan_an_real_network.json"
echo [2/2] May chu local dang chay tai: http://localhost:8600
echo       (De tat may chu, hay dong cua so Command Prompt nay)
echo.

if exist "%~dp0tools\vosviewer-online\dist\vosviewer-online\data\luan_an_real_network.json" (
    cd /d "%~dp0tools\vosviewer-online\dist\vosviewer-online"
) else (
    cd /d "%~dp0vosviewer-online\dist\vosviewer-online"
)

python -m http.server 8600
