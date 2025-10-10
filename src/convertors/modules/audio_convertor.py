import subprocess
from pathlib import Path
from src.config.ui_helper import UI


class AudioConvertor:
    """Convert audio files between different formats"""
    
    SUPPORTED_FORMATS = ['mp3', 'wav', 'flac', 'aac', 'ogg', 'm4a', 'wma', 'opus']
    
    @staticmethod
    def convert(input_file: str, output_format: str, output_dir: str = "doned/converted"):
        """Convert audio file to specified format"""
        try:
            input_path = Path(input_file)
            
            if not input_path.exists():
                UI.error(f"File not found: {input_file}")
                return False
            
            if output_format.lower() not in AudioConvertor.SUPPORTED_FORMATS:
                UI.error(f"Unsupported format: {output_format}")
                UI.info(f"Supported formats: {', '.join(AudioConvertor.SUPPORTED_FORMATS)}")
                return False
            
            Path(output_dir).mkdir(parents=True, exist_ok=True)
            output_file = Path(output_dir) / f"{input_path.stem}.{output_format}"
            
            UI.info(f"Converting: {input_path.name}")
            UI.info(f"Format: {output_format.upper()}")
            UI.processing("Converting...")
            
            cmd = [
                'ffmpeg',
                '-i', str(input_path),
                '-vn',
                '-acodec', 'libmp3lame' if output_format == 'mp3' else output_format,
                '-y',
                str(output_file)
            ]
            
            result = subprocess.run(cmd, capture_output=True, text=True)
            
            if result.returncode == 0:
                UI.success(f"Saved to: {output_file}")
                return True
            else:
                UI.error("Conversion failed")
                return False
                
        except FileNotFoundError:
            UI.error("ffmpeg not found! Please install ffmpeg")
            return False
        except Exception as e:
            UI.error(f"Unexpected error: {e}")
            return False
