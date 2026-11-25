@echo off
title VOSviewer Desktop - Le Phuc Hai (TDTU)
echo ==============================================================================
echo   KHOI DONG VOSVIEWER DESKTOP (JAVA 21 JRE PORTABLE DA TICH HOP SAN)
echo   De tai: He thong de xuat AI va Mua boc dong truc tuyen (NCS Le Phuc Hai)
echo ==============================================================================
set "JAVA_HOME=%~dp0vosviewer\jre"
set "PATH=%~dp0vosviewer\jre\bin;%PATH%"
start "" "%~dp0vosviewer\VOSviewer.exe" -map "%~dp0data\vosviewer\keywords_map.txt" -network "%~dp0data\vosviewer\keywords_network.txt"
exit
