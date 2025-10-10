import os
import traceback
import datetime
from threading import Lock
from pathlib import Path
from typing import Optional, Callable, TypeVar, Any
from src.config.ui_helper import UI

T = TypeVar('T')

class ErrorHandler:
    """Reusable error handler for logging errors to dynamic log files with user-friendly suggestions."""

    _LOG_DIR = Path("src/logs")
    _DEFAULT_LOG_FILE = "type_errors.log"
    _lock = Lock()

    @classmethod
    def _ensure_log_dir(cls) -> None:
        """Ensure the log directory exists."""
        cls._LOG_DIR.mkdir(parents=True, exist_ok=True)

    @classmethod
    def log_error(
        cls,
        error: Exception,
        context: Optional[str] = None,
        stderr: Optional[str] = None,
        log_file: str = _DEFAULT_LOG_FILE
    ) -> bool:
        """
        Log an error to a specified file and display a user-friendly message.
        Args:
            error: The exception to log.
            context: Optional context for the error (e.g., function or task name).
            stderr: Optional stderr output from subprocess commands.
            log_file: Name of the log file (e.g., 'downloader_errors.log').
        Returns:
            bool: True if logging was successful, False otherwise.
        """
        try:
            cls._ensure_log_dir()
            log_path = cls._LOG_DIR / log_file
            error_type = type(error).__name__
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            tb = traceback.format_exc()
            log_entry = (
                f"\n[{timestamp}] {error_type}: {error}\n"
                f"Context: {context or 'No context'}\n"
                f"Stderr: {stderr or 'No stderr'}\n{tb}\n{'-'*80}\n"
            )

            with cls._lock:
                with open(log_path, "a", encoding="utf-8") as f:
                    f.write(log_entry)

            UI.error(f"❌ Error: {error_type} — {error}")
            UI.info(f"🔍 Details written to {log_path}")

            suggestion = cls.suggest_fix(error, stderr)
            if suggestion:
                UI.warning(f"🛠 Possible fix: {suggestion}")

            return True
        except Exception as e:
            UI.error(f"Failed to log error: {e}")
            return False

    @classmethod
    def suggest_fix(cls, error: Exception, stderr: Optional[str] = None) -> Optional[str]:
        """
        Provide a suggested fix based on the error type and message.
        Args:
            error: The exception to analyze.
            stderr: Optional stderr output for additional context.
        Returns:
            Optional[str]: A suggested fix or None if no suggestion applies.
        """
        msg = str(error).lower()
        stderr_lower = stderr.lower() if stderr else ""

        if "file not found" in msg or "no such file" in msg:
            return "Check the file path or ensure dependencies are installed."
        if "yt-dlp" in msg or "yt-dlp" in stderr_lower:
            return "Ensure yt-dlp is installed: pip install yt-dlp"
        if "spotdl" in msg or "spotdl" in stderr_lower:
            return "Ensure spotdl is installed: pip install spotdl. Run 'spotdl --generate-config' to set up Spotify API credentials."
        if "client id" in stderr_lower or "client secret" in stderr_lower:
            return (
                "Missing Spotify API credentials. Run 'spotdl --generate-config' to create a config file, "
                "then add your client ID and secret from https://developer.spotify.com/dashboard."
            )
        if "connection" in msg or "network" in msg or "connection" in stderr_lower:
            return "Check your internet connection or try using a VPN (e.g., set to US or EU region)."
        if "permission" in msg:
            return "Run the program as an administrator."
        if "json" in msg:
            return "Invalid data format — check input files or API response."
        if "none" in msg:
            return "Function returned None — verify the return value."
        if "timeout" in msg:
            return "Operation timed out — check network stability or increase timeout."
        return None

    @classmethod
    def safe_call(cls, func: Callable[..., T], *args: Any, **kwargs: Any) -> Optional[T]:
        """
        Safely call a function with error handling.
        Args:
            func: The function to call.
            *args: Positional arguments for the function.
            **kwargs: Keyword arguments for the function (may include log_file).
        Returns:
            Optional[T]: The function's result or None if an error occurs.
        """
        try:
            return func(*args, **kwargs)
        except Exception as e:
            cls.log_error(e, context=func.__name__, stderr=kwargs.get('stderr'), log_file=kwargs.get('log_file', cls._DEFAULT_LOG_FILE))
            return None