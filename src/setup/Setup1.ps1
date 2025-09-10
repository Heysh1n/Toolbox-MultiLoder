# ===== HS1N SYSTEM SETUP =====
Write-Host "=============================" -ForegroundColor Cyan
Write-Host "     🔧 HS1N SYSTEM SETUP     " -ForegroundColor Cyan
Write-Host "=============================`n" -ForegroundColor Cyan

# --- Проверка Python ---
Write-Host "[🔍] Checking Python..."
$python = Get-Command python -ErrorAction SilentlyContinue
$missingPython = $false

if (-not $python) {
    Write-Host "[✘] Python not found." -ForegroundColor Red
    $choice = Read-Host "Would you like to install Python? (y/n)"
    if ($choice -eq "y") {
        Start-Process "https://www.python.org/downloads/"
        Write-Host "Opened Python download page. Install manually and restart this script." -ForegroundColor Yellow
        exit
    } else {
        Write-Host "Skipping Python installation." -ForegroundColor DarkYellow
        $missingPython = $true
    }
} else {
    $version = python --version
    Write-Host "[✓] Python found: $version" -ForegroundColor Green
}

# --- Проверка pip ---
if (-not $missingPython) {
    Write-Host "`n[🔍] Checking pip..."
    $pip = Get-Command pip -ErrorAction SilentlyContinue
    if (-not $pip) {
        Write-Host "[✘] pip not found." -ForegroundColor Red
        $choice = Read-Host "Install pip automatically? (y/n)"
        if ($choice -eq "y") {
            try {
                Invoke-WebRequest -Uri https://bootstrap.pypa.io/get-pip.py -OutFile "get-pip.py"
                python get-pip.py
                Remove-Item "get-pip.py"
                Write-Host "[✓] pip installed successfully." -ForegroundColor Green
            } catch {
                Write-Host "[!] Failed to install pip automatically." -ForegroundColor Red
            }
        } else {
            Write-Host "Skipping pip installation." -ForegroundColor DarkYellow
        }
    } else {
        Write-Host "[✓] pip found." -ForegroundColor Green
    }

    # --- Проверка spotDL ---
    Write-Host "`n[🔍] Checking spotDL..."
    $spotdl = Get-Command spotdl -ErrorAction SilentlyContinue
    if (-not $spotdl) {
        $choice = Read-Host "spotDL not found. Install using pip? (y/n)"
        if ($choice -eq "y") {
            pip install spotdl
        } else {
            Write-Host "Skipping spotDL installation." -ForegroundColor DarkYellow
        }
    } else {
        Write-Host "[✓] spotDL found." -ForegroundColor Green
    }
}

# --- Проверка FFmpeg ---
Write-Host "`n[🔍] Checking FFmpeg..."
$ffmpeg = Get-Command ffmpeg -ErrorAction SilentlyContinue
if (-not $ffmpeg) {
    Write-Host "[✘] FFmpeg not found." -ForegroundColor Red
    $choice = Read-Host "Would you like to auto-install FFmpeg? (y/n)"
    if ($choice -eq "y") {
        $temp = "$env:TEMP\ffmpeg"
        $ffmpegZip = "$temp\ffmpeg.zip"
        $ffmpegURL = "https://www.gyan.dev/ffmpeg/builds/ffmpeg-release-essentials.zip"

        try {
            Write-Host "[⏬] Downloading FFmpeg..."
            Invoke-WebRequest -Uri $ffmpegURL -OutFile $ffmpegZip

            Write-Host "[📦] Extracting FFmpeg..."
            Expand-Archive -Path $ffmpegZip -DestinationPath $temp -Force

            $ffmpegPath = Get-ChildItem -Path "$temp" -Directory | Where-Object { $_.Name -like "ffmpeg-*" } | Select-Object -First 1
            $binPath = "$($ffmpegPath.FullName)\bin"
            $env:Path += ";$binPath"

            Write-Host "[✓] FFmpeg installed and temporarily added to PATH." -ForegroundColor Green
        } catch {
            Write-Host "[!] FFmpeg installation failed: $_" -ForegroundColor Red
        }
    } else {
        Write-Host "Skipping FFmpeg installation." -ForegroundColor DarkYellow
    }
} else {
    $ffmpegVersion = ffmpeg -version | Select-String "ffmpeg version" | Select-Object -First 1
    Write-Host "[✓] FFmpeg found: $ffmpegVersion" -ForegroundColor Green
}

Write-Host "`n[✓] Setup check completed." -ForegroundColor Cyan
pause
