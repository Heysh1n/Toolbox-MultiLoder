@echo off
setlocal enabledelayedexpansion
chcp 65001 >nul
title Music Downloader

:: Цвета
call src\config\colors.bat

:: Пути
set "outputDir=doned\musics"
set "logDir=src\logs"

:: Создание папок
if not exist "%outputDir%" mkdir "%outputDir%"
if not exist "%logDir%" mkdir "%logDir%"

:menu
cls
echo %pink2% ╔═════════════════════════════════════════════════════╗
echo %pink2% ║                   %white%MUSIC DOWNLOADER%pink2%                  ║
echo %pink2% ╚═════════════════════════════════════════════════════╝
echo.
echo %white%[!] Paste a music link (Spotify, YouTube, SoundCloud, etc.)%reset%
echo %white%[!] Type "%gray%exit%white%" or "%gray%0%white%" to return to main menu.%reset%
echo.

set /p "link=🔗 URL: "

if /i "!link!"=="exit" exit /b
if /i "!link!"=="0" exit /b

:: Проверяем, пустая ли строка
if "!link!"=="" goto menu

echo.
echo %pink2%📥 Downloading...%reset%
echo %white%Source:%gray% !link!%reset%
echo.

:: Если ссылка на Spotify → используем spotdl
echo "!link!" | findstr /i "spotify.com" >nul
if %errorlevel%==0 (
    spotdl download "!link!" --output "%outputDir%\{title}.{ext}" 2>> "%logDir%\music_errors.log"
) else (
    :: Для остальных сервисов используем yt-dlp
    echo Checking for yt-dlp updates...
    src\downloader\yt-dlp.exe -U >nul 2>&1

    echo Extracting audio...
    src\downloader\yt-dlp.exe -x --audio-format mp3 -o "%outputDir%\%%(title)s.%%(ext)s" "!link!" 2>> "%logDir%\music_errors.log"
)

:: Проверка на ошибку
if %errorlevel% neq 0 (
    echo %red%[!] Error while downloading. Check logs in "%logDir%\music_errors.log"%reset%
    pause
    goto menu
)

echo.
echo %pink2%[✓] Done! Saved to:%reset% %outputDir%
echo.
start "" explorer "%outputDir%"
pause
goto menu