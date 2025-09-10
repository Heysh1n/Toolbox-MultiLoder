@echo off
chcp 65001 >nul
setlocal EnableDelayedExpansion
call src\config\colors.bat

:: Paths
set "inputDir=doned\convertor\inputs\image"
set "outputDir=doned\convertor\outputs\image"
set "logDir=src\convertor\logs"

:: Supported formats
set "image_ext=png jpg jpeg bmp gif ico tiff webp heic"

:: Create folders
if not exist "%inputDir%" mkdir "%inputDir%"
if not exist "%outputDir%" mkdir "%outputDir%"
if not exist "%logDir%" mkdir "%logDir%"

:menu
cls
echo %pink2% ╔═════════════════════════════════════════════════════╗
echo %pink2% ║                   %white%IMAGE CONVERTER%pink2%                   ║
echo %pink2% ╚═════════════════════════════════════════════════════╝
echo.

set /a i=1
for %%e in (%image_ext%) do (
    echo %pink1%[!i!]%white% Convert all → %%e
    set "opt[!i!]=%%e"
    set /a i+=1
)
echo %pink1%[S]%white% 🎯 Single file convert
echo %pink1%[0]%white% ⬅ Back
echo.

set /p choice=%gray%Select option: %reset%
if "%choice%"=="0" exit /b
if /i "%choice%"=="S" goto single

set "target=!opt[%choice%]!"
if not defined target goto menu

echo %pink2%[🔄] Converting all files in "%inputDir%" to %target%...%reset%
for %%f in ("%inputDir%\*") do (
    set "filename=%%~nf"
    ffmpeg -i "%%f" "%outputDir%\!filename!.%target%" -y 2>> "%logDir%\ffmpeg_image.log"
)
echo %pink2%[✓] Done! Saved in "%outputDir%"%reset%
pause
goto menu

:single
echo %white%Drag & drop a file here, or type path:%reset%
set /p "file=> "
if not exist "%file%" (
    echo %red%[!] File not found!%reset%
    pause
    goto menu
)
echo Choose format: %image_ext%
set /p "target=Format: "
set "filename=%~nfile%"
ffmpeg -i "%file%" "%outputDir%\%filename%.%target%" -y 2>> "%logDir%\ffmpeg_image.log"
echo %pink2%[✓] Done!%reset%
pause
goto menu
