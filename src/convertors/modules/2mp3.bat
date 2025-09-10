@echo off
setlocal enabledelayedexpansion
chcp 65001 >nul
title Video ➜ MP3 Converter

:: Create folders
if not exist "doned\videos" mkdir "doned\videos"
if not exist "doned\video-music" mkdir "doned\video-music"

:: Supported video formats
set "formats=mp4 mkv avi mov webm flv mpg wmv m4v ts 3gp vob ogv m2ts flac wav ogg"

:loop
cls
:: Gradient-style banner
echo [95m ╔═════════════════════════════════════════════════════╗
echo [95m ║                 [97mALL ➜  MP3 CONVERTER[95m                ║
echo [95m ╚═════════════════════════════════════════════════════╝
echo.

:: Check for video files
set "file_found=false"
for %%X in (%formats%) do (
    for %%F in (doned/videos\*.%%X) do (
        if exist "%%F" (
            set "file_found=true"
            goto :start_conversion
        )
    )
)

echo [!] No supported video files found in doned/videos
pause
exit /b

:start_conversion
echo 📥 Starting conversion to MP3...

for %%X in (%formats%) do (
    for %%F in (doned/videos\*.%%X) do (
        if exist "%%F" (
            set "filename=%%~nxF"
            set "nameonly=%%~nF"
            echo [»] Converting: !filename! → !nameonly!.mp3

            ffmpeg -i "%%~fF" -vn -acodec libmp3lame -b:a 192k "doned/video-music\!nameonly!.mp3"

            echo [✓] Done: !nameonly!.mp3
        )
    )
)

echo.
echo ✅ All files converted. Saved to: doned/video-music
pause
exit /b
