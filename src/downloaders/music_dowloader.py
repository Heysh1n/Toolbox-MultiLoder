import subprocess
import json
import re
import shutil
from pathlib import Path
from typing import Generator, Tuple, List, Dict, Optional
from src.config.ui_helper import UI
from src.config.colors import Colors as C
from src.config.banners import Banners as B
from src.config.animation import Loader
from src.config.error_handler import ErrorHandler

class SpotifyDownloader:
    """
    Spotify music downloader for track URLs or song queries with robust error handling.
    Supports various Spotify URL formats and lightweight search for queries.
    """

    _LOG_FILE = "downloader_errors.log"

    @staticmethod
    def _check_spotdl() -> Tuple[bool, Optional[str]]:
        """Check if spotdl is installed and configured."""
        if not shutil.which('spotdl'):
            return False, "spotdl not installed. Install it with 'pip install spotdl'."
        try:
            proc = subprocess.run(
                ['spotdl', '--version'],
                capture_output=True,
                text=True,
                encoding='utf-8',
                timeout=5,
                check=True
            )
            return True, None
        except subprocess.CalledProcessError as e:
            ErrorHandler.log_error(e, context="Check spotdl version", stderr=e.stderr, log_file=SpotifyDownloader._LOG_FILE)
            return False, f"spotdl failed to run: {e.stderr}"
        except Exception as e:
            ErrorHandler.log_error(e, context="Check spotdl version", log_file=SpotifyDownloader._LOG_FILE)
            return False, f"Unexpected error checking spotdl: {e}"

    @staticmethod
    def _validate_url(input_str: str) -> Tuple[bool, Optional[str], Optional[str]]:
        """
        Validate and normalize Spotify track URL, extracting the track ID.
        Returns:
            Tuple[bool, Optional[str], Optional[str]]: (is_valid, error_message, normalized_url).
        """
        spotify_track_pattern = r'^https?://open\.spotify\.com(/intl-[a-zA-Z]+)?/track/([a-zA-Z0-9]+)(\?.*)?$'
        match = re.match(spotify_track_pattern, input_str)
        if match:
            track_id = match.group(2)
            normalized_url = f"https://open.spotify.com/track/{track_id}"
            return True, None, normalized_url
        return False, "Invalid Spotify track URL. Use format: https://open.spotify.com/track/...", None

    @staticmethod
    def _search_tracks(query: str) -> Tuple[List[Dict], Optional[str]]:
        """Search for tracks using spotdl and return results or error message."""
        is_installed, error_msg = SpotifyDownloader._check_spotdl()
        if not is_installed:
            return [], error_msg

        cmd = ['spotdl', 'search', query, '--output-format', 'json']
        loader = Loader(f"Searching for {query}...")
        loader.start()
        try:
            proc = subprocess.run(
                cmd,
                capture_output=True,
                text=True,
                encoding='utf-8',
                timeout=15,
                check=True
            )
            stdout = proc.stdout.strip()
            if not stdout:
                ErrorHandler.log_error(
                    Exception("Empty output from spotdl"),
                    context=f"Search query: {query}",
                    stderr=proc.stderr,
                    log_file=SpotifyDownloader._LOG_FILE
                )
                return [], "No results returned from search. Ensure Spotify API credentials are set up."

            try:
                tracks = json.loads(stdout)
                # Prioritize specific tracks
                if "my conscious" in query.lower():
                    tracks = [
                        t for t in tracks
                        if "my conscious" in t.get('name', '').lower()
                        and "faceless 1-7" in ' '.join(a['name'].lower() for a in t.get('artists', []))
                    ] or tracks
                elif "1-800" in query.lower():
                    tracks = [
                        t for t in tracks
                        if "1-800" in t.get('name', '').lower()
                        and ("bbno$" in ' '.join(a['name'].lower() for a in t.get('artists', []))
                             or "ironmouse" in ' '.join(a['name'].lower() for a in t.get('artists', [])))
                    ] or tracks
                return tracks, None
            except json.JSONDecodeError as e:
                ErrorHandler.log_error(e, context=f"JSON parsing for query: {query}", stderr=proc.stderr, log_file=SpotifyDownloader._LOG_FILE)
                return [], "Failed to parse search results."
        except subprocess.TimeoutExpired as e:
            ErrorHandler.log_error(e, context=f"Search query: {query}", stderr=proc.stderr, log_file=SpotifyDownloader._LOG_FILE)
            return [], "Search timed out. Try again later."
        except subprocess.CalledProcessError as e:
            ErrorHandler.log_error(e, context=f"Search query: {query}", stderr=e.stderr, log_file=SpotifyDownloader._LOG_FILE)
            return [], f"Search command failed: {e.stderr}"
        finally:
            loader.stop()

    @staticmethod
    def download(
        input_str: str,
        output_dir: str = "doned/spotify-music",
        format: str = "mp3",
        high_quality: bool = False
    ) -> Generator[Tuple[str, str | int], None, None]:
        """
        Generator for downloading a Spotify track by URL or query with progress updates.
        Args:
            input_str: Spotify track URL or song query (e.g., 'https://open.spotify.com/track/...' or 'My Conscious Faceless 1-7').
            output_dir: Directory to save downloaded files.
            format: File format (e.g., 'mp3').
            high_quality: Use high-quality download (m4a via YouTube).
        Yields:
            Tuple[str, str | int]: Status and message or progress percentage.
        """
        UI.print_banner("spotify")
        UI.separator()
        UI.info("Note: In some regions, a VPN may be required for Spotify API access.")
        UI.info("Note: Ensure Spotify API credentials are set up. Run 'spotdl --generate-config' if needed.")

        is_spotdl_ok, error_msg = SpotifyDownloader._check_spotdl()
        if not is_spotdl_ok:
            UI.warning(error_msg or "Unable to initialize spotdl.")
            yield ("warn", "SpotDL initialization failed")
            UI.wait()
            return

        input_str = input_str.strip()
        if input_str in ['exit', '0']:
            yield ("info", "Returning to main menu...")
            UI.wait()
            return

        output_path = Path(output_dir)
        try:
            output_path.mkdir(parents=True, exist_ok=True)
        except Exception as e:
            ErrorHandler.log_error(e, context="Create output directory", log_file=SpotifyDownloader._LOG_FILE)
            yield ("error", f"Failed to create directory {output_path}: {e}")
            UI.wait()
            return

        # Check if input is a URL or query
        is_url, url_error, normalized_url = SpotifyDownloader._validate_url(input_str)
        if is_url:
            track_url = normalized_url
            track_name = "track"  # Placeholder, updated later if possible
            track_artist = "unknown"
        else:
            if len(input_str) < 3:
                yield ("warn", "Query too short. Try 'My Conscious Faceless 1-7' or a Spotify URL.")
                UI.wait()
                return

            UI.info(f"Searching for: {input_str}")
            tracks, error = ErrorHandler.safe_call(
                SpotifyDownloader._search_tracks, input_str, log_file=SpotifyDownloader._LOG_FILE
            )

            if error:
                yield ("warn", f"❌ {error}")
                UI.wait()
                return

            if not tracks:
                broader_query = f"{input_str} song"
                UI.info(f"No tracks found. Trying broader search for '{broader_query}'...")
                tracks, error = ErrorHandler.safe_call(
                    SpotifyDownloader._search_tracks, broader_query, log_file=SpotifyDownloader._LOG_FILE
                )
                if error:
                    yield ("warn", f"❌ {error}")
                    UI.wait()
                    return
                if not tracks:
                    yield ("warn", "❌ No tracks found. Try a Spotify URL or a more specific query (e.g., 'My Conscious Faceless 1-7').")
                    retry = UI.prompt("Retry with a different query or URL? [y/N]: ").strip().lower()
                    if retry == 'y':
                        new_input = UI.prompt("Enter new query or Spotify URL: ").strip()
                        yield from SpotifyDownloader.download(new_input, output_dir, format, high_quality)
                    UI.wait()
                    return

            UI.info("Found the following tracks:")
            displayed = tracks[:6]
            for i, track in enumerate(displayed):
                name = track.get('name', 'Unknown')
                artist = track.get('artists', [{'name': 'Unknown'}])[0]['name']
                UI.menu_item(str(i), f"{name} - {artist}")

            choice = UI.prompt(f"Choose from [0-{len(displayed)-1}] or '0' to exit: ").strip().lower()
            if choice in ['exit', '0']:
                yield ("info", "Returning to main menu...")
                UI.wait()
                return

            try:
                index = int(choice)
                selected = displayed[index]
                track_url = selected['url']
                track_name = selected.get('name', 'Unknown')
                track_artist = selected.get('artists', [{'name': 'Unknown'}])[0]['name']
            except (ValueError, IndexError, KeyError) as e:
                ErrorHandler.log_error(e, context="Track selection", log_file=SpotifyDownloader._LOG_FILE)
                yield ("warn", f"Invalid choice or track data: {e}. Try again.")
                UI.wait()
                return

        cmd = [
            'spotdl', 'download', track_url,
            '--output', str(output_path.resolve()),
            '--output-format', format,
            '-p', '{title} - {artist}.{output-ext}'
        ]
        if high_quality:
            cmd.extend(['--use-youtube', '--output-format', 'm4a'])

        UI.info(f"Downloading: {track_name} - {track_artist}")
        yield ("info", f"Downloading: {track_name} - {track_artist}")

        try:
            with Loader.progress_bar(description=f"Downloading {track_name}...") as progress:
                task = progress.add_task("download", total=100)
                proc = subprocess.Popen(
                    cmd,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    text=True,
                    encoding="utf-8",
                    errors="ignore"
                )

                for line in iter(proc.stdout.readline, ''):
                    line = line.strip()
                    if not line:
                        continue
                    if any(keyword in line for keyword in ["UserWarning", "Traceback", "URLError"]):
                        continue

                    match = re.search(r"(\d{1,3})\s*%", line)
                    if match:
                        percent = min(max(int(match.group(1)), 0), 100)
                        progress.update(task, completed=percent)
                        yield ("progress", percent)
                    elif "download started" in line.lower():
                        yield ("info", "🎧 Download started")
                    elif "download completed" in line.lower():
                        progress.update(task, completed=100)
                        yield ("success", "✅ Download completed!")
                    else:
                        yield ("info", line)

                proc.wait()

            if proc.returncode != 0:
                stderr_output = proc.stderr.read() if proc.stderr else "No stderr data"
                ErrorHandler.log_error(
                    Exception(f"Non-zero exit code: {proc.returncode}"),
                    context=f"Download: {track_name} - {track_artist}",
                    stderr=stderr_output,
                    log_file=SpotifyDownloader._LOG_FILE
                )
                yield ("warn", "⚠️ Download finished with warnings. Check src/logs/downloader_errors.log.")
            else:
                yield ("success", f"✅ {track_name} - {track_artist} downloaded successfully!")

            Loader.open_folder(output_path)
            yield ("info", f"📁 Files saved to: {output_path.resolve()}")
        except Exception as e:
            ErrorHandler.log_error(e, context=f"Download: {track_name} - {track_artist}", log_file=SpotifyDownloader._LOG_FILE)
            yield ("error", f"Error during download: {e}. Check src/logs/downloader_errors.log")
        UI.wait()