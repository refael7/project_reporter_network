from Ingestion_Service.Kafka_Publisher import KafkaPublisher

from Ingestion_Service import Ingestion_Config, OCR_Engine, Metadata_Extractor,MongoLoaderClient
import logging
IMAGE_DIRECTORY=r'C:\Users\refae\Downloads\messaging_images\tweet_images'
class IngestionOrchestrator:
    def __init__(
            self,
            config: Ingestion_Config,
            ocr_engine: OCR_Engine,
            metadata_extractor: Metadata_Extractor,
            mongo_client: MongoLoaderClient,
            publisher: KafkaPublisher,
            logger: logging.Logger,
    ):
        self.config = config
        self.ocr_engine = ocr_engine
        self.metadata_extractor = metadata_extractor
        self.mongo_client = mongo_client
        self.publisher = publisher
        self.logger = logger

    def process_image(self, image_path: str):
        self.logger.info(f"Processing image: {image_path}")
        image_id = self.metadata_extractor.generate_image_id(image_path)
        metadata = self.metadata_extractor.extract_metadata(image_path)
        raw_text = self.ocr_engine.extract_text(image_path)
        self.mongo_client.send(image_path, image_id)
        event = {
            "image_id": image_id,
            "raw_text": raw_text,
            "metadata": metadata,
        }
        self.publisher.publish(event)
        self.logger.info(f"Finished processing image_id={image_id}")


    def run(self):
        import os
        files = [
            f for f in os.listdir(IMAGE_DIRECTORY)
        ]
        for filename in files:
            full_path = os.path.join(IMAGE_DIRECTORY, filename)
            self.process_image(full_path)
        self.logger.info("Ingestion run complete")



