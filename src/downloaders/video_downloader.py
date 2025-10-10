import subprocess
from pathlib import Path
from rich.progress import Progress, BarColumn, TextColumn, TimeRemainingColumn
from src.config.ui_helper import UI

class Downloader:
    """Download videos and audio from various platforms with rich progress bar"""

    @staticmethod
    def _run_yt_dlp(cmd, task_name: str):
        """Run yt-dlp command and parse progress"""
        with Progress(
            TextColumn(f"[bold white]{task_name}[/bold white]"),
            BarColumn(bar_width=None),
            TextColumn("[green]{task.percentage:>3.0f}%"),
            TimeRemainingColumn(),
            transient=True
        ) as progress:

            task = progress.add_task("download", total=100)

            try:
                proc = subprocess.Popen(
                    cmd,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.STDOUT,
                    text=True,
                    encoding="utf-8",
                    errors="ignore"
                )

                for line in proc.stdout:
                    line = line.strip()
                    if not line:
                        continue

                    # Ищем проценты
                    import re
                    match = re.search(r"(\d{1,3}\.\d{1,2}|\d{1,3})%", line)
                    if match:
                        percent = float(match.group(1))
                        progress.update(task, completed=percent)

                    # Дополнительные уведомления
                    elif "Destination" in line:
                        UI.info(line)
                    elif "Downloading" in line:
                        UI.processing(line)

                proc.wait()

                if proc.returncode != 0:
                    UI.error("Download failed!")
                    return False

                return True

            except FileNotFoundError:
                UI.error("yt-dlp not found!")
                UI.info("Please install: pip install yt-dlp")
                return False

    @staticmethod
    def download_video(url: str, output_path: str = "doned/videos"):
        """Download video with best quality"""
        UI.info(f"Downloading video from: {url}")
        Path(output_path).mkdir(parents=True, exist_ok=True)

        cmd = [
            'yt-dlp',
            '-f', 'bestvideo+bestaudio/best',
            '--merge-output-format', 'mp4',
            '-o', f'{output_path}/%(title)s.%(ext)s',
            '--no-playlist',
            url
        ]

        success = Downloader._run_yt_dlp(cmd, "Video Download")
        if success:
            UI.success("Video downloaded successfully!")
        return success

    @staticmethod
    def download_audio(url: str, output_path: str = "doned/videos-music"):
        """Download audio only in MP3 format"""
        UI.info(f"Downloading audio from: {url}")
        Path(output_path).mkdir(parents=True, exist_ok=True)

        cmd = [
            'yt-dlp',
            '-x',
            '--audio-format', 'mp3',
            '--audio-quality', '192',
            '-o', f'{output_path}/%(title)s.%(ext)s',
            '--no-playlist',
            url
        ]

        success = Downloader._run_yt_dlp(cmd, "Audio Download")
        if success:
            UI.success("Audio downloaded successfully!")
        return success

    @staticmethod
    def download_playlist(url: str, output_path: str = "doned/videos"):
        """Download entire playlist"""
        UI.info(f"Downloading playlist from: {url}")
        Path(output_path).mkdir(parents=True, exist_ok=True)

        cmd = [
            'yt-dlp',
            '-f', 'bestvideo+bestaudio/best',
            '--merge-output-format', 'mp4',
            '-o', f'{output_path}/%(playlist_index)s - %(title)s.%(ext)s',
            '--yes-playlist',
            url
        ]

        success = Downloader._run_yt_dlp(cmd, "Playlist Download")
        if success:
            UI.success("Playlist downloaded successfully!")
        return success
