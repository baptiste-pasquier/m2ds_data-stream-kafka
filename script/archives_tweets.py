import os

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

# Create archives folder if it does not exist
if not os.path.isdir("archives"):
    os.makedirs("archives")
for topic in TOPIC_LIST:
    with open(f"archives/{topic}.txt", "w") as _:
        pass

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
        f"Saving message from topic: {TOPICS_COLOR[topic] + topic + Style.RESET_ALL}\n{message.value}\n"
    )
    with open(f"archives/{message.topic}.txt", "a") as f:
        f.write(message.value)
        f.write("\n")
