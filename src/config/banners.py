from src.config.colors import Colors as C


class Banners:
    """Collection of ASCII art banners"""
    
    @staticmethod
    def main_banner():
        """Main HS1N LOADER banner with gradient"""
        banner = f"""
{C.WHITE}   ██╗  ██╗███████╗ ██╗███╗   ██╗    ██╗      ██████╗  █████╗ ██████╗ ███████╗██████╗   
{C.GRAY}   ██║  ██║██╔════╝███║████╗  ██║    ██║     ██╔═══██╗██╔══██╗██╔══██╗██╔════╝██╔══██╗ 
{C.MAGENTA}   ███████║███████╗╚██║██╔██╗ ██║    ██║     ██║   ██║███████║██║  ██║█████╗  ██████╔╝ 
{C.MAGENTA_BRIGHT}   ██╔══██║╚════██║ ██║██║╚██╗██║    ██║     ██║   ██║██╔══██║██║  ██║██╔══╝  ██╔══██╗  
{C.PINK1}   ██║  ██║███████║ ██║██║ ╚████║    ███████╗╚██████╔╝██║  ██║██████╔╝███████╗██║  ██║ 
{C.PINK2}{C.BOLD}   ╚═╝  ╚═╝╚══════╝ ╚═╝╚═╝  ╚═══╝    ╚══════╝ ╚═════╝ ╚═╝  ╚═╝╚═════╝ ╚══════╝╚═╝  ╚═╝ {C.RESET}

{C.PINK2}==  ==  ==  ==  ==  ==  ==  ==  ==   {C.WHITE}HS1N LOADER{C.PINK2}   ==  ==  ==  ==  ==  ==  ==  ==  ==  =={C.RESET}
"""
        return banner
    
    @staticmethod
    def downloader_banner():
        """Video/Audio downloader banner"""
        banner = f"""
{C.PINK1}   ██████╗  ██████╗ ██╗    ██╗███╗   ██╗██╗      ██████╗  █████╗ ██████╗ ███████╗██████╗ 
{C.PINK2}   ██╔══██╗██╔═══██╗██║    ██║████╗  ██║██║     ██╔═══██╗██╔══██╗██╔══██╗██╔════╝██╔══██╗
{C.MAGENTA_BRIGHT}   ██║  ██║██║   ██║██║ █╗ ██║██╔██╗ ██║██║     ██║   ██║███████║██║  ██║█████╗  ██████╔╝
{C.MAGENTA}   ██║  ██║██║   ██║██║███╗██║██║╚██╗██║██║     ██║   ██║██╔══██║██║  ██║██╔══╝  ██╔══██╗
{C.PINK2}   ██████╔╝╚██████╔╝╚███╔███╔╝██║ ╚████║███████╗╚██████╔╝██║  ██║██████╔╝███████╗██║  ██║
{C.PINK1}   ╚═════╝  ╚═════╝  ╚══╝╚══╝ ╚═╝  ╚═══╝╚══════╝ ╚═════╝ ╚═╝  ╚═╝╚═════╝ ╚══════╝╚═╝  ╚═╝{C.RESET}
"""
        return banner
    
    @staticmethod
    def converter_banner():
        """Converter banner"""
        banner = f"""
{C.PINK1}    ██████╗ ██████╗ ███╗   ██╗██╗   ██╗███████╗██████╗ ████████╗███████╗██████╗ 
{C.PINK2}   ██╔════╝██╔═══██╗████╗  ██║██║   ██║██╔════╝██╔══██╗╚══██╔══╝██╔════╝██╔══██╗
{C.MAGENTA_BRIGHT}   ██║     ██║   ██║██╔██╗ ██║██║   ██║█████╗  ██████╔╝   ██║   █████╗  ██████╔╝
{C.MAGENTA}   ██║     ██║   ██║██║╚██╗██║╚██╗ ██╔╝██╔══╝  ██╔══██╗   ██║   ██╔══╝  ██╔══██╗
{C.PINK2}   ╚██████╗╚██████╔╝██║ ╚████║ ╚████╔╝ ███████╗██║  ██║   ██║   ███████╗██║  ██║
{C.PINK1}    ╚═════╝ ╚═════╝ ╚═╝  ╚═══╝  ╚═══╝  ╚══════╝╚═╝  ╚═╝   ╚═╝   ╚══════╝╚═╝  ╚═╝{C.RESET}
"""
        return banner
    
    @staticmethod
    def spotify_banner():
        """Spotify downloader banner"""
        banner = f"""
{C.PINK1}   ███████╗██████╗  ██████╗ ████████╗██╗███████╗██╗   ██╗
{C.PINK2}   ██╔════╝██╔══██╗██╔═══██╗╚══██╔══╝██║██╔════╝╚██╗ ██╔╝
{C.MAGENTA_BRIGHT}   ███████╗██████╔╝██║   ██║   ██║   ██║█████╗   ╚████╔╝ 
{C.MAGENTA}   ╚════██║██╔═══╝ ██║   ██║   ██║   ██║██╔══╝    ╚██╔╝  
{C.PINK2}   ███████║██║     ╚██████╔╝   ██║   ██║██║        ██║   
{C.PINK1}   ╚══════╝╚═╝      ╚═════╝    ╚═╝   ╚═╝╚═╝        ╚═╝   {C.RESET}
"""
        return banner
    
    @staticmethod
    def setup_banner():
        """Setup banner"""
        banner = f"""
{C.PINK1}   ███████╗███████╗████████╗██╗   ██╗██████╗ 
{C.PINK2}   ██╔════╝██╔════╝╚══██╔══╝██║   ██║██╔══██╗
{C.MAGENTA_BRIGHT}   ███████╗█████╗     ██║   ██║   ██║██████╔╝
{C.MAGENTA}   ╚════██║██╔══╝     ██║   ██║   ██║██╔═══╝ 
{C.PINK2}   ███████║███████╗   ██║   ╚██████╔╝██║     
{C.PINK1}   ╚══════╝╚══════╝   ╚═╝    ╚═════╝ ╚═╝     {C.RESET}
"""
        return banner
    
    @staticmethod
    def separator(char="=", length=80, color=None):
        """Create colored separator line"""
        if color is None:
            color = C.PINK2
        return f"{color}{char * length}{C.RESET}"
    
    @staticmethod
    def box_message(message: str, color=None):
        """Create boxed message"""
        if color is None:
            color = C.PINK1
        length = len(message) + 4
        top = f"{color}╔{'═' * length}╗{C.RESET}"
        mid = f"{color}║  {C.WHITE}{message}{color}  ║{C.RESET}"
        bot = f"{color}╚{'═' * length}╝{C.RESET}"
        return f"{top}\n{mid}\n{bot}"
