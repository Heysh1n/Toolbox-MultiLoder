
# 🎬🎵 Universal Downloader & Converter CLI

A powerful command-line application for:

* 📥 Downloading videos from various platforms (YouTube, Pinterest, Instagram, TikTok, etc.)
* 🎧 Downloading music from Spotify and other supported services
* 🔄 Converting media files (video, audio, images)

---

## 📦 Features

* ✅ Download videos via URL
* ✅ Convert video/audio/images to multiple formats
* ✅ Download tracks, albums, and playlists from Spotify
* ✅ Simple and intuitive CLI interface
* ✅ Organized input/output folder structure
* ✅ **Supported only on Windows platforms** (or its analogs like Wine)

---

## 🛠 Installation || Full guide

```bash
1. Download the latest Python version → [click*](https://www.python.org/downloads/)
   1.1 Check "Add to PATH" during installation  
   1.2 Click "Install NOW" and wait until the process finishes  

2. Download FFmpeg dependency from the official website → [click*](https://ffmpeg.org/download.html)  
   2.1 Extract all files from the archive and place them on Disk "C:\"  
   2.2 Add FFmpeg to PATH in Windows system settings  

3. Run the `main.bat` file — it will check for dependencies  
   3.1 If some dependencies are missing, the checker will ask you to auto-install — type "Y" and press Enter  
   3.2 If the checker fails to resolve something — contact me  

4. Delete the `.setup.done` file from `\src\setup\`  

5. Run `main.bat` again and enjoy 🚀  
```

> *Dependencies may include: `ffmpeg`, `yt-dlp`, `spotdl`, `python`, `pip` packages.*

---

## 📁 Project Structure

```
/HS1N-ToolBox
   /doned
      /videos
      /videos-music
      /spotify-music
      /converter
         /inputs
         /outputs
   /src
      /convertors
         /modules
            /2mp3.bat
            /AudioConvertor.bat
            /VideoConvertor.bat
            /ImageConvertor.bat
         /ConvertorCore.bat
      /downloader
         /Downloader.bat
         /yt-dlp.exe
      /music
         /SpotifyDownloader.bat
      /setup
         /Setup1.ps1
   main.bat
   readme.md
```

---

## 🚀 Roadmap

* [x] Core functionality: download videos & music
* [x] Add Spotify music downloader (via `spotdl`)
* [x] Add universal audio/video/image converters
* [x] Organized folder structure (`inputs`, `outputs`, `logs`)
* [x] Auto-update for `yt-dlp`

**Planned features:**

* [ ] Add support for more image formats (JPG ⇄ PNG ⇄ WebP ⇄ ICO ⇄ BMP)
* [ ] Add support for more video formats (AVI ⇄ MOV ⇄ MKV ⇄ WebM ⇄ FLV)
* [ ] Add playlist & channel downloader for YouTube
* [ ] Add batch-conversion with progress display
* [ ] Multi-platform support (Linux, macOS via Wine/Mono wrappers)
* [ ] Automatic dependency installer with GUI dialog
* [ ] Optional `.exe` build (standalone, no Python required)

---

## ⚠️ Disclaimer

This application was created solely for **educational purposes** as part of my personal learning process in developing console-based programs.

It is not intended for public/commercial use.
You are not permitted to download, distribute, or use this software outside of its educational demonstration.

The author assumes no responsibility or liability for any consequences, direct or indirect, resulting from the use, distribution, or modification of this program.

Use of this tool may violate the Terms of Service of platforms like Spotify, YouTube, or others. Any misuse is strictly prohibited.

---

## 📜 License & Usage

This project is **UNLICENSED**.
It may only be used as a **fork** on GitHub for educational and non-commercial purposes.

You may:
✔ Fork the repository
✔ Study the code
✔ Modify it locally for learning purposes

You may **NOT**:
❌ Redistribute binaries or modified versions
❌ Use the tool for public distribution or commercial purposes

All rights reserved.

---

## 👤 Author

**[Heysh1n aka hs1n](https://github.com/Heysh1n)**
Feel free to open issues or submit pull requests (educational contributions only)!

