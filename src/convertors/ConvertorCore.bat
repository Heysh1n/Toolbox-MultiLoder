@echo off
chcp 65001 >nul
setlocal EnableDelayedExpansion

call src\config\colors.bat

:menu
cls
echo %pink2% ╔═════════════════════════════════════════════════════╗
echo %pink2% ║                 %white%UNIVERSAL CONVERTER%pink2%                 ║
echo %pink2% ╚═════════════════════════════════════════════════════╝
echo.

echo %pink1%[1]%white% 🎵 Audio Converter %gray%- Convert audio → MP3, FLAC, WAV, OGG, M4A, AAC
echo %gray%    Supported input:%white% mp3, flac, wav, ogg, m4a, aac, ac3, opus, wma, amr, aiff, au
echo.

echo %pink1%[2]%white% 🎞 Video Converter %gray%- Convert MP4 ⇄ MKV ⇄ AVI ⇄ WEBM ⇄ GIF ⇄ MOV
echo %gray%    Supported input:%white% mp4, mkv, avi, mov, webm, flv, mpg, wmv, m4v, ts, 3gp, vob, ogv, m2ts, f4v, rmvb, asf
echo.

echo %pink1%[3]%white% 🖼 Image Converter %gray%- Convert PNG ⇄ JPG ⇄ BMP ⇄ WEBP ⇄ ICO ⇄ TIFF
echo %gray%    Supported input:%white% png, jpg, jpeg, bmp, tiff, gif, webp, heic
echo.

echo %pink1%[0]%white% ❌ Back
echo.

set /p choice=%gray%Choice [0-4]: %reset%

if "%choice%"=="1" goto audio
if "%choice%"=="2" goto video
if "%choice%"=="3" goto image
if "%choice%"=="0" exit /b
goto menu

:audio
cls
echo %pink2%[Audio Converter]%reset%
echo %white%Converts audio into:%gray% MP3, FLAC, WAV, OGG, M4A, AAC
echo %white%Supported input:%gray% mp3, flac, wav, ogg, m4a, aac, ac3, opus, wma, amr, aiff, au
echo.
call "src\convertors\modules\AudioConvertor.bat"
goto menu

:video
cls
echo %pink2%[Video Converter]%reset%
echo %white%Converts video between formats:%gray% MP4, MKV, AVI, WEBM, GIF, MOV
echo %white%Supported input:%gray% mp4, mkv, avi, mov, webm, flv, mpg, wmv, m4v, ts, 3gp, vob, ogv, m2ts, f4v, rmvb, asf
echo.
call "src\convertors\modules\VideoConvertor.bat"
goto menu

:image
cls
echo %pink2%[Image Converter]%reset%
echo %white%Converts images into:%gray% PNG, JPG, BMP, WEBP, ICO, TIFF
echo %white%Supported input:%gray% png, jpg, jpeg, bmp, tiff, gif, webp, heic
echo.
call "src\convertors\modules\ImageConvertor.bat"
goto menu
