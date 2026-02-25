import easyocr
import logging

class OcrEngine:
    def __init__(self,logger:logging.Logger):
        self.logger=logger
    def  extract_text(self,image_path):
        try:

            reader = easyocr.Reader(['en'], gpu=False)
            result = reader.readtext(image_path, detail=0)
            return " ".join(result)

        except Exception as e:
            self.logger.error(f"ocr failed for {image_path}: {e}")
            raise

