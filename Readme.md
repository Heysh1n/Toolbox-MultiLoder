
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
HS1N LOADER/
├── src/
│   ├── config/                      # Configuration and utility modules
│   │   ├── animation.py             # Loading animations and spinners
│   │   ├── banners.py               # ASCII banners for CLI
│   │   ├── colors.py                # Terminal color codes and gradient styles
│   │   ├── error_handler.py         # Centralized error logging and handling
│   │   └── ui_helper.py             # CLI UI helpers, prompts, menus, messages
│   │
│   ├── convertors/                  # Conversion logic
│   │   ├── convertor_core.py        # Main conversion engine
│   │   └── modules/                 # Specific converters
│   │       ├── audio_convertor.py
│   │       ├── image_convertor.py
│   │       ├── toMP3.py
│   │       └── video_convertor.py
│   │
│   ├── downloaders/                 # Download managers
│   │   ├── music_dowloader.py       # Spotify/music downloader
│   │   └── video_downloader.py      # Video downloader (YouTube etc.)
│   │
│   ├── logs/                        # Log files for errors and actions
│   │   └── spotify_errors.log       # Example: Spotify downloader logs
│   │
│   └── setup/                       # Setup scripts and main entry point
│       ├── setup.py                 # Initial setup / installation
│
├── main.py                          # Main executable file
│
└── readme.md                        # Project documentation

```

---

## 🚀 Roadmap

* [x] Core functionality: download videos & music
* [x] Add universal audio/video/image converters
* [x] Organized folder structure (`inputs`, `outputs`, `logs`)
* [x] Auto-update for `yt-dlp`
* [x] Optional `.exe` build (standalone, no Python required)
* [x] Add batch-conversion with progress display
* [x] Multi-platform support (Linux, macOS)
* [x] Automatic dependency installer with GUI dialog

**Planned features:**



* [ ] Optianal `.apk` build (portable for Android)
* [ ] Fix Spotify Downloader (spotdl was update and old functionality don't work)
* [ ] Compilate to `.exe` and publicate to `Releases`

---

## ⚠️ Disclaimer

This application was created solely for **educational purposes** as part of my personal learning process in developing console-based programs.

It is not intended for public/commercial use.
You are not permitted to download, distribute, or use this software outside of its educational demonstration.

The author assumes no responsibility or liability for any consequences, direct or indirect, resulting from the use, distribution, or modification of this program.

---

## 📜 License & Usage

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



