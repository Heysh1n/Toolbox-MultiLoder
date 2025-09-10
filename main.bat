@echo off
chcp 65001 >nul
setlocal EnableDelayedExpansion

:: Подключаем цвета
call src\config\colors.bat

:: Проверка setup
if not exist "src/setup/.setup_done" (
    echo %white%[🛠] Running setup first time...%reset%
    powershell -ExecutionPolicy Bypass -File "src\setup\Setup1.ps1"
    echo setup complete > "src/setup/.setup_done"
    pause
)

:menu
cls
echo.
echo.

REM === ASCII banner с градиентом ===
echo %white%   ██╗  ██╗███████╗ ██╗███╗   ██╗    ██╗      ██████╗  █████╗ ██████╗ ███████╗██████╗   
echo %gray%   ██║  ██║██╔════╝███║████╗  ██║    ██║     ██╔═══██╗██╔══██╗██╔══██╗██╔════╝██╔══██╗ 
echo %magenta%   ███████║███████╗╚██║██╔██╗ ██║    ██║     ██║   ██║███████║██║  ██║█████╗  ██████╔╝ 
echo %magentaBright%   ██╔══██║╚════██║ ██║██║╚██╗██║    ██║     ██║   ██║██╔══██║██║  ██║██╔══╝  ██╔══██╗  
echo %pink1%   ██║  ██║███████║ ██║██║ ╚████║    ███████╗╚██████╔╝██║  ██║██████╔╝███████╗██║  ██║ 
echo %pink2%%bold%   ╚═╝  ╚═╝╚══════╝ ╚═╝╚═╝  ╚═══╝    ╚══════╝ ╚═════╝ ╚═╝  ╚═╝╚═════╝ ╚══════╝╚═╝  ╚═╝ %reset%
echo.

echo %pink2%==  ==  ==  ==  ==  ==  ==  ==  ==   %white%HS1N LOADER%pink2%   ==  ==  ==  ==  ==  ==  ==  ==  ==  ==%reset%
echo.

echo %pink1%[1]%white% 📥 Video downloader [Any platform]
echo %pink2%[2]%white% ♻️ All Convertors
echo %pink1%[3]%white% 🎞️ All to MP3
echo %pink1%[4]%white% 🎵 Music downloader [Spotify need VPN -- BETA]
echo %pink1%[0]%white% ❌ Exit
echo.

set /p choice=%gray%Choice from [0-4]: %reset%

if "%choice%"=="1" goto videodownloader
if "%choice%"=="2" goto allconvertors
if "%choice%"=="3" goto converter2mp3
if "%choice%"=="4" goto musicdownloader
if "%choice%"=="0" exit
goto menu

:videodownloader
call src/downloader/Downloader.bat
goto menu

:allconvertors
call src/convertors/ConvertorCore.bat
goto menu

:converter2mp3
call src/convertors/modules/2mp3.bat
goto menu

:musicdownloader
call src/music/MusicDownloader.bat
goto menu
