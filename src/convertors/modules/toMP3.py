import subprocess
from pathlib import Path
from src.config.ui_helper import UI


class ToMP3:
    """Convert any media to MP3 format"""
    
    @staticmethod
    def convert_to_mp3(input_path: str, output_dir: str = "doned/converted"):  # ← ЗДЕСЬ
        """Convert file or directory to MP3"""
        path = Path(input_path)
        
        if not path.exists():
            UI.error(f"Path not found: {input_path}")
            return False
        
        Path(output_dir).mkdir(parents=True, exist_ok=True)
        
        if path.is_file():
            return ToMP3._convert_single_file(path, output_dir)
        elif path.is_dir():
            return ToMP3._convert_directory(path, output_dir)
    
    @staticmethod
    def _convert_single_file(input_file: Path, output_dir: str):
        """Convert single file to MP3"""
        try:
            output_file = Path(output_dir) / f"{input_file.stem}.mp3"
            
            UI.info(f"Converting: {input_file.name}")
            UI.processing("Converting to MP3...")
            
            cmd = [
                'ffmpeg',
                '-i', str(input_file),
                '-vn',
                '-acodec', 'libmp3lame',
                '-q:a', '0',
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
    
    @staticmethod
    def _convert_directory(input_dir: Path, output_dir: str):
        """Convert all files in directory to MP3"""
        files = [f for f in input_dir.iterdir() if f.is_file()]
        
        if not files:
            UI.warning("No files found in directory")
            return False
        
        UI.info(f"Found {len(files)} files to convert")
        print()
        
        success_count = 0
        fail_count = 0
        
        for file in files:
            if ToMP3._convert_single_file(file, output_dir):
                success_count += 1
            else:
                fail_count += 1
            print()
        
        UI.info(f"Batch conversion complete! Success: {success_count} | Failed: {fail_count}")
        return success_count > 0