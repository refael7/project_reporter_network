from kafka import KafkaProducer
import json


class KafkaPublisher:
    def __init__(self, bootstrap_servers, topic_name, logger):
        self.topic_name = topic_name
        self.logger = logger
        self.producer = KafkaProducer(
            bootstrap_servers= bootstrap_servers,
            value_serializer= lambda v: json.dumps(v).encode("utf-8")
        )

    def publish(self,event):
        try:
            self.producer.send(self.topic_name,event)
            self.producer.flush()
            self.logger.info(f"the {event} send to {self.topic_name}")
        except Exception as e:
            self.logger.error(f"failed to publish event {e}")
            raise


