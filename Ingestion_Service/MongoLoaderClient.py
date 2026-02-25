import requests


class MongoLoaderClient:
    def __init__(self, mongo_loader_url, logger):
        self.mongo_loader_url = mongo_loader_url
        self.logger = logger

    def send(self, file_path, image_id):
        try:
            self.logger.info(f"{file_path}->send to mongo")
            with open(file_path, 'rb') as f:
                response = requests.post(
                    f"{file_path}/upload",
                    files={'file': file_path},
                    data={'image_id': image_id}, )
                response.raise_for_status()
                self.logger.info(f"the sending successfully")
                return response.json()
        except Exception as e:
            self.logger.error(f"Metadata extraction failed for {file_path}: {e}")
            raise


