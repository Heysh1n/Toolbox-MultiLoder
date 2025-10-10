import subprocess
from pathlib import Path
from src.config.ui_helper import UI


class ConvertorCore:
    """Core conversion logic and batch processing"""
    
    AUDIO_FORMATS = ['mp3', 'wav', 'flac', 'aac', 'ogg', 'm4a', 'wma', 'opus']
    VIDEO_FORMATS = ['mp4', 'avi', 'mkv', 'mov', 'wmv', 'flv', 'webm', 'mpeg']
    IMAGE_FORMATS = ['jpg', 'jpeg', 'png', 'gif', 'bmp', 'webp', 'tiff', 'ico']
    
    @staticmethod
    def detect_file_type(file_path: str) -> str:
        """Detect file type based on extension"""
        ext = Path(file_path).suffix[1:].lower()
        
        if ext in ConvertorCore.AUDIO_FORMATS:
            return 'audio'
        elif ext in ConvertorCore.VIDEO_FORMATS:
            return 'video'
        elif ext in ConvertorCore.IMAGE_FORMATS:
            return 'image'
        else:
            return 'unknown'
    
    @staticmethod
    def batch_convert(input_dir: str, output_format: str, output_dir: str = "doned/converted"): 
        """Batch convert all compatible files"""
        input_path = Path(input_dir)
        
        if not input_path.exists():
            UI.error(f"Directory not found: {input_dir}")
            return
        
        if not input_path.is_dir():
            UI.error(f"Not a directory: {input_dir}")
            return
        
        Path(output_dir).mkdir(parents=True, exist_ok=True)
        
        files = [f for f in input_path.iterdir() if f.is_file()]
        
        if not files:
            UI.warning("No files found in directory")
            return
        
        UI.info(f"Found {len(files)} files")
        UI.info(f"Converting to: {output_format}")
        UI.info(f"Output directory: {output_dir}")
        print()
        
        success_count = 0
        fail_count = 0
        
        for file in files:
            file_type = ConvertorCore.detect_file_type(str(file))
            
            if file_type == 'unknown':
                UI.warning(f"Skipped: {file.name} - Unknown format")
                continue
            
            UI.processing(f"Processing: {file.name}")
            
            try:
                from src.convertors.modules.audio_convertor import AudioConvertor
                from src.convertors.modules.video_convertor import VideoConvertor
                from src.convertors.modules.image_convertor import ImageConvertor
                
                if file_type == 'audio':
                    result = AudioConvertor.convert(str(file), output_format, output_dir)
                elif file_type == 'video':
                    result = VideoConvertor.convert(str(file), output_format, output_dir)
                elif file_type == 'image':
                    result = ImageConvertor.convert(str(file), output_format, output_dir)
                
                if result:
                    success_count += 1
                else:
                    fail_count += 1
                    
            except Exception as e:
                UI.error(f"Failed to convert {file.name}: {e}")
                fail_count += 1
        
        print()
        UI.info(f"Conversion complete! Success: {success_count} | Failed: {fail_count}")

