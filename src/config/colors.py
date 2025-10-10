
class Colors:
    """Terminal color codes with gradient pink/magenta theme"""
    
    # Reset
    RESET = '\033[0m'
    
    # Basic colors
    WHITE = '\033[97m'
    GRAY = '\033[90m'
    BLACK = '\033[30m'
    
    # Pink/Magenta gradient (main theme)
    PINK1 = '\033[38;5;213m'  # Light pink
    PINK2 = '\033[38;5;219m'  # Lighter pink
    MAGENTA = '\033[35m'      # Magenta
    MAGENTA_BRIGHT = '\033[95m'  # Bright magenta
    PURPLE = '\033[38;5;141m'  # Purple
    
    # Additional colors
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    
    # Styles
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    
    @staticmethod
    def gradient_text(text: str, start_color: str, end_color: str) -> str:
        """Create gradient effect on text"""
        return f"{start_color}{text}{end_color}"