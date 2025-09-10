@echo off
setlocal enabledelayedexpansion
chcp 65001 >nul
title Video Downloader

:: Цвета
call src\config\colors.bat

:: Пути
set "outputDir=doned\videos"
set "logDir=src\logs"

:: Создание папок
if not exist "%outputDir%" mkdir "%outputDir%"
if not exist "%logDir%" mkdir "%logDir%"

:menu
cls
echo %pink2% ╔═════════════════════════════════════════════════════╗
echo %pink2% ║                   %white%VIDEO DOWNLOADER%pink2%                  ║
echo %pink2% ╚═════════════════════════════════════════════════════╝
echo.
echo %white%[!] Paste a video URL (YouTube, Vimeo, Twitch, etc.)%reset%
echo %white%[!] Type "%gray%exit%white%" or "%gray%0%white%" to return to main menu.%reset%
echo.

set /p "url=🔗 URL: "

if /i "!url!"=="exit" exit /b
if /i "!url!"=="0" exit /b

echo Checking for yt-dlp updates...
src\downloader\yt-dlp.exe -U >nul 2>&1

echo.
echo %pink2%📥 Downloading video...%reset%
echo.

src\downloader\yt-dlp.exe -f bestvideo+bestaudio/best --merge-output-format mp4 ^
 -o "%outputDir%\%%(title)s.%%(ext)s" "!url!" 2>> "%logDir%\videoDownloader.log"

if %errorlevel% neq 0 (
    echo.
    echo %red%[!] Error while downloading! Check logs in "%logDir%\videoDownloader.log"%reset%
    pause
    goto menu
)

echo.
echo %pink2%[✓] Done! Saved to:%reset% %outputDir%
echo.
start "" explorer "%outputDir%"
pause
goto menu