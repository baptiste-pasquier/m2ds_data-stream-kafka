from datetime import datetime

from colorama import Style
from kafka import KafkaConsumer

from m2ds_data_stream_kafka.config import TOPICS_COLOR

TOPIC_LIST = [
    "raw-tweets",
    "en-tweets",
    "fr-tweets",
    "positive-tweets",
    "negative-tweets",
]

# Define Kafka consumer
consumer = KafkaConsumer(
    bootstrap_servers="localhost:9092",
    value_deserializer=lambda m: m.decode("utf8"),
)
consumer.subscribe(TOPIC_LIST)

# Loop
for message in consumer:
    topic = message.topic
    print(
        f"{TOPICS_COLOR[topic] + topic + Style.RESET_ALL}, {message.partition}, {message.offset}, {datetime.now()}"
    )
