import os
import sys
from pathlib import Path

# Add src to path
sys.path.append(str(Path(__file__).parent / "src"))

from config.colors import Colors as C
from config.banners import Banners as B
from config.ui_helper import UI
from config.animation import Loader

from downloaders.video_downloader import Downloader
from convertors.convertor_core import ConvertorCore
from downloaders.music_dowloader import SpotifyDownloader
from setup.setup import setup_environment


def check_first_run():
    """Check if setup has been completed"""
    setup_flag = Path("./src/setup/.setup_done")
    
    if not setup_flag.exists():
        UI.clear()
        print(B.setup_banner())
        print()
        UI.info("Running setup for the first time...")
        print()
        # os.makedirs("src/setup", exist_ok=True)
        # with open(setup_flag, 'w') as f:
        #     f.write("Setup completed")
        setup_environment()
        UI.wait()


def show_main_menu():
    UI.print_banner("main")
    UI.menu_item("1", "Video downloader [Any platform]", "📥")
    UI.menu_item("2", "All Convertors", "♻️")
    UI.menu_item("3", "All to MP3", "🎞️")
    UI.menu_item("4", "Music downloader [Spotify need VPN -- BETA]", "🎵")
    UI.menu_item("0", "Exit", "❌")
    print()


def downloader_menu():
    UI.print_banner("downloader")
    print(f"{C.PINK2}{'='*80}{C.RESET}\n")
    UI.menu_item("1", "Download Video (Best Quality)", "🎥")
    UI.menu_item("2", "Download Audio Only (MP3)", "🎵")
    UI.menu_item("3", "Download Playlist", "📋")
    UI.menu_item("0", "Back to Main Menu", "◀️")
    print()

    choice = UI.prompt("Select option [0-3]: ").strip()

    if choice == '1':
        url = UI.prompt("Enter video URL: ").strip()
        if url:
            Downloader.download_video(url)
        UI.wait()
    elif choice == '2':
        url = UI.prompt("Enter video URL: ").strip()
        if url:
            Downloader.download_audio(url)
        UI.wait()
    elif choice == '3':
        url = UI.prompt("Enter playlist URL: ").strip()
        if url:
            Downloader.download_playlist(url)
        UI.wait()


def converter_menu():
    UI.print_banner("converter")
    print(f"{C.PINK2}{'='*80}{C.RESET}\n")
    UI.menu_item("1", "Convert Audio File", "🎵")
    UI.menu_item("2", "Convert Video File", "🎥")
    UI.menu_item("3", "Convert Image File", "🖼️")
    UI.menu_item("4", "Batch Convert Directory", "📁")
    UI.menu_item("5", "Convert All to MP3", "🎞️")
    UI.menu_item("0", "Back to Main Menu", "◀️")
    print()

    choice = UI.prompt("Select option [0-5]: ").strip()
    
    if choice == '1':
        from convertors.modules.audio_convertor import AudioConvertor
        input_file = UI.prompt("Input audio file path: ").strip()
        output_format = UI.prompt("Output format (mp3/wav/flac/aac/ogg): ").strip()
        if input_file and output_format:
            AudioConvertor.convert(input_file, output_format)
        UI.wait()
    elif choice == '2':
        from convertors.modules.video_convertor import VideoConvertor
        input_file = UI.prompt("Input video file path: ").strip()
        output_format = UI.prompt("Output format (mp4/avi/mkv/mov/webm): ").strip()
        if input_file and output_format:
            VideoConvertor.convert(input_file, output_format)
        UI.wait()
    elif choice == '3':
        from convertors.modules.image_convertor import ImageConvertor
        input_file = UI.prompt("Input image file path: ").strip()
        output_format = UI.prompt("Output format (jpg/png/webp/gif): ").strip()
        if input_file and output_format:
            ImageConvertor.convert(input_file, output_format)
        UI.wait()
    elif choice == '4':
        input_dir = UI.prompt("Input directory path: ").strip()
        output_format = UI.prompt("Output format: ").strip()
        if input_dir and output_format:
            ConvertorCore.batch_convert(input_dir, output_format)
        UI.wait()
    elif choice == '5':
        from convertors.modules.toMP3 import ToMP3
        input_path = UI.prompt("Input file or directory path: ").strip()
        if input_path:
            ToMP3.convert_to_mp3(input_path)
        UI.wait()


def spotify_menu():
    UI.print_banner("spotify")
    print(f"{C.PINK2}{'='*80}{C.RESET}")
    UI.warning("VPN may be required in some regions")
    print(f"{C.PINK2}{'='*80}{C.RESET}\n")
    
    UI.menu_item("1", "Download Track", "🎵")
    UI.menu_item("2", "Download Album", "💿")
    UI.menu_item("3", "Download Playlist", "📋")
    UI.menu_item("4", "Download Artist", "👤")
    UI.menu_item("0", "Back to Main Menu", "◀️")
    print()

    choice = UI.prompt("Select option [0-5]: ").strip()

    url = None
    if choice == '1':
        url = UI.prompt("Enter track name or Spotify URL: ").strip()
    elif choice == '2':
        url = UI.prompt("Enter album URL: ").strip()
    elif choice == '3':
        url = UI.prompt("Enter playlist URL: ").strip()
    elif choice == '4':
        url = UI.prompt("Enter artist URL: ").strip()

    
    if choice in ['1','2','3','4'] and url:
        for event, msg in SpotifyDownloader.download(url):
            if event == "info":
                UI.info(msg)
            elif event == "progress":
                print(f"Progress: {msg}%")
            elif event == "success":
                UI.success(msg)
            elif event == "warn":
                UI.warning(msg)
        UI.wait()


def main():
    Path('doned/videos').mkdir(parents=True, exist_ok=True)
    Path('doned/videos-music').mkdir(parents=True, exist_ok=True)
    Path('doned/spotify-music').mkdir(parents=True, exist_ok=True)
    Path('doned/converted').mkdir(parents=True, exist_ok=True)
    Path('doned/converted/input').mkdir(parents=True, exist_ok=True)
    
    while True:
        show_main_menu()
        choice = UI.prompt("Choice from [0-4]: ").strip()
        if choice == '1':
            downloader_menu()
        elif choice == '2':
            converter_menu()
        elif choice == '3':
            from convertors.modules.toMP3 import ToMP3
            input_path = UI.prompt("Input file or directory path: ").strip()
            if input_path:
                ToMP3.convert_to_mp3(input_path)
            UI.wait()
        elif choice == '4':
            spotify_menu()
        elif choice == '0':
            UI.clear()
            print(B.main_banner())
            print(B.box_message("Thank you for using HS1N LOADER!"))
            sys.exit(0)
        else:
            UI.error("Invalid option! Please try again.")
            UI.wait()


if __name__ == "__main__":
    check_first_run()
    main()
