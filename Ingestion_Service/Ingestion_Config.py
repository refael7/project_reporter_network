import os


class IngestionConfig:
    def __init__(self):
        self.bootstrap_servers = os.getenv("KAFKA_BOOTSTRAP_SERVERS", "localhost:9092")
        self.raw_topic = os.getenv("RAW_TOPIC", "raw")
        self.mongo_loader_url = os.getenv("MONGO_LOADER_URL", "http://localhost:8001")

    def validate(self):
        if not self.mongo_loader_url:
            raise ValueError("MONGO_LOADER_URL is required")
        if not self.raw_topic:
            raise ValueError("RAW_TOPIC is required")
        if not self.bootstrap_servers:
            raise ValueError("KAFKA_BOOTSTRAP_SERVERS is required")
