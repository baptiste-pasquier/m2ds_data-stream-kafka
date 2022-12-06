import json
import os
import time

import tweepy
from colorama import Style
from kafka import KafkaProducer

from m2ds_data_stream_kafka.config import KEYWORD, MAX_RESULTS, TIME_SLEEP, TOPICS_COLOR

# Define Kafka producer
producer = KafkaProducer(
    bootstrap_servers="localhost:9092",
    value_serializer=lambda m: json.dumps(m).encode("utf8"),
)

# Define Tweepy client
client = tweepy.Client(bearer_token=os.getenv("TWITTER_BEARER_TOKEN"))

# Loop
i = 0
while True:
    for tweet in tweepy.Paginator(
        client.search_recent_tweets,
        query=KEYWORD,
        tweet_fields=["created_at", "lang"],
        max_results=MAX_RESULTS,
    ).flatten():
        message = {
            "created_at": tweet["created_at"].strftime("%Y-%m-%d %H:%M:%S"),
            "lang": tweet["lang"],
            "text": str(tweet),
        }

        topic = "raw-tweets"
        print(
            f"Sending message to topic: {TOPICS_COLOR[topic] + topic + Style.RESET_ALL}\n{message}\n"
        )
        producer.send(topic, message)
        i += 1
        time.sleep(TIME_SLEEP)
