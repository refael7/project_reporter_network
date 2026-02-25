import hashlib

from PIL import Image


class MetadataExtractor:
    def __init__(self,logger):
        self.logger = logger


    def extract_metadata(self,image_path):
        try:
            img = Image.open(image_path)
            width, height = img.size
            file_format =img.format

            metadata = {
                'width':width,
                'height':height,
                'format':file_format
            }
            self.logger.info(f"Metadata extracted for {image_path}")
            return metadata


        except Exception as e:
            self.logger.error(f"Metadata extraction failed for {image_path}: {e}")
            raise

    def generate_image_id(self, image_path):
        with open(image_path,'rb') as f:
            conn = f.read()
        return hashlib.sha256(conn).hexdigest()