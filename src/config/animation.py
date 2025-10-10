import sys
import threading
import itertools
import time
from rich.progress import Progress, BarColumn, TextColumn, TimeRemainingColumn
from pathlib import Path
from src.config.ui_helper import UI
from src.config.colors import Colors as C
from src.config.error_handler import ErrorHandler

class Loader:
    """Loader animation with spinner and optional progress bar"""

    def __init__(self, description="Loading..."):
        self.description = description
        self._stop_spinner = False
        self.spinner_thread = None

    def _spinner_task(self):
        spinner = itertools.cycle(["|", "/", "-", "\\"])
        while not self._stop_spinner:
            sys.stdout.write(f"\r{C.MAGENTA}[{next(spinner)}] {self.description}{C.RESET}")
            sys.stdout.flush()
            time.sleep(0.1)
        sys.stdout.write("\r" + " " * (len(self.description) + 5) + "\r")
        sys.stdout.flush()

    def start(self):
        """Start spinner in separate thread"""
        self._stop_spinner = False
        self.spinner_thread = threading.Thread(target=self._spinner_task)
        self.spinner_thread.start()

    def stop(self):
        """Stop spinner"""
        self._stop_spinner = True
        if self.spinner_thread:
            self.spinner_thread.join()

    @staticmethod
    def progress_bar(total=100, description="Downloading..."):
        """Context manager for rich progress bar"""
        return Progress(
            TextColumn(f"[bold white]{description}"),
            BarColumn(bar_width=None),
            TextColumn("[green]{task.percentage:>3.0f}%"),
            TimeRemainingColumn(),
            transient=True,
        )

    @staticmethod
    def open_folder(path: Path):
        """Открывает папку с файлами"""
        try:
            folder = path.resolve()
            if sys.platform.startswith('win'):
                import os
                os.startfile(folder)
            elif sys.platform.startswith('darwin'):
                import subprocess
                subprocess.run(['open', folder])
            else:
                import subprocess
                subprocess.run(['xdg-open', folder])
        except Exception as e:
            ErrorHandler.log(f"Failed to open folder {path}: {e}")
            UI.warning(f"Не удалось открыть папку {path}")
