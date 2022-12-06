import json

from colorama import Style
from kafka import KafkaConsumer, KafkaProducer

from m2ds_data_stream_kafka.config import TOPICS_COLOR

# Define Kafka consumer
consumer = KafkaConsumer(
    "raw-tweets",
    bootstrap_servers="localhost:9092",
    value_deserializer=lambda m: json.loads(m.decode("utf8")),
)

# Define Kafka producer
producer = KafkaProducer(
    bootstrap_servers="localhost:9092",
    value_serializer=lambda m: json.dumps(m).encode("utf8"),
)

# Loop
for message in consumer:
    tweet = message.value
    if tweet["lang"] in ["fr", "en"]:
        topic = "en-tweets" if tweet["lang"] == "en" else "fr-tweets"
        print(
            f"Sending message to topic: {TOPICS_COLOR[topic] + topic + Style.RESET_ALL}\n{tweet}\n"
        )
        producer.send(topic, tweet)
