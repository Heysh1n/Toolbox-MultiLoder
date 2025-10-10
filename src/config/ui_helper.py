import os
import sys
from src.config.colors import Colors as C
from src.config.banners import Banners as B


def safe_print(text: str):
    """Safe print with encoding fallback"""
    try:
        print(text)
    except UnicodeEncodeError:
        # Fallback: remove non-ASCII characters
        print(text.encode('ascii', 'ignore').decode('ascii'))


class UI:
    """UI Helper class for consistent terminal output"""
    
    @staticmethod
    def clear():
        """Clear terminal screen"""
        os.system('cls' if os.name == 'nt' else 'clear')
    
    @staticmethod
    def print_banner(banner_type="main"):
        """Print specific banner"""
        UI.clear()
        print()
        try:
            if banner_type == "main":
                print(B.main_banner())
            elif banner_type == "downloader":
                print(B.downloader_banner())
            elif banner_type == "converter":
                print(B.converter_banner())
            elif banner_type == "spotify":
                print(B.spotify_banner())
            elif banner_type == "setup":
                print(B.setup_banner())
        except UnicodeEncodeError:
            # Fallback banner
            print("="*60)
            print(f"    HS1N-ToolBox - {banner_type.upper()}")
            print("="*60)
        print()
    
    @staticmethod
    def success(message: str):
        """Print success message"""
        try:
            print(f"{C.GREEN}[OK] {message}{C.RESET}")
        except UnicodeEncodeError:
            print(f"{C.GREEN}[OK] {message}{C.RESET}")
    
    @staticmethod
    def error(message: str):
        """Print error message"""
        try:
            print(f"{C.RED}[ERROR] {message}{C.RESET}")
        except UnicodeEncodeError:
            print(f"{C.RED}[ERROR] {message}{C.RESET}")
    
    @staticmethod
    def info(message: str):
        """Print info message"""
        try:
            print(f"{C.CYAN}[INFO] {message}{C.RESET}")
        except UnicodeEncodeError:
            print(f"{C.CYAN}[INFO] {message}{C.RESET}")
    
    @staticmethod
    def warning(message: str):
        """Print warning message"""
        try:
            print(f"{C.YELLOW}[WARNING] {message}{C.RESET}")
        except UnicodeEncodeError:
            print(f"{C.YELLOW}[WARNING] {message}{C.RESET}")
    
    @staticmethod
    def processing(message: str):
        """Print processing message"""
        try:
            print(f"{C.MAGENTA}[PROCESSING] {message}{C.RESET}")
        except UnicodeEncodeError:
            print(f"{C.MAGENTA}[PROCESSING] {message}{C.RESET}")
    
    @staticmethod
    def menu_item(number: str, text: str, icon: str = ""):
        """Print styled menu item"""
        try:
            print(f"{C.PINK1}[{number}]{C.WHITE} {icon} {text}{C.RESET}")
        except UnicodeEncodeError:
            print(f"{C.PINK1}[{number}]{C.WHITE} {text}{C.RESET}")
    
    @staticmethod
    def prompt(text: str) -> str:
        """Styled input prompt"""
        try:
            return input(f"{C.GRAY}{text}{C.RESET}")
        except UnicodeEncodeError:
            return input(f"{text}")
    
    @staticmethod
    def separator(char="="):
        """Print separator"""
        print(B.separator(char))
    
    @staticmethod
    def wait():
        """Wait for user input"""
        try:
            input(f"\n{C.GRAY}Press Enter to continue...{C.RESET}")
        except UnicodeEncodeError:
            input("\nPress Enter to continue...")