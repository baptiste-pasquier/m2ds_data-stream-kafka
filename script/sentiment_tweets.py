import json

from colorama import Style
from kafka import KafkaConsumer, KafkaProducer

from m2ds_data_stream_kafka.config import TOPICS_COLOR
from m2ds_data_stream_kafka.sentiment_analysis import (
    classify_sentiment,
    positive_negative_words,
    text_preprocessing,
)

POSITIVE_WORDS, NEGATIVE_WORDS = positive_negative_words("data/")

consumer = KafkaConsumer(
    "en-tweets",
    "fr-tweets",
    bootstrap_servers="localhost:9092",
    value_deserializer=lambda m: json.loads(m.decode("utf8")),
)

producer = KafkaProducer(
    bootstrap_servers="localhost:9092",
    value_serializer=lambda m: json.dumps(m).encode("utf8"),
)

for message in consumer:
    tweet = message.value

    if tweet["lang"] == "fr":
        language = "french"
    elif tweet["lang"] == "en":
        language = "english"
    else:
        raise ValueError(tweet["lang"])

    string = tweet["text"]
    string_preprocessed = text_preprocessing(string, language)

    sentiment = classify_sentiment(
        string_preprocessed, language, POSITIVE_WORDS, NEGATIVE_WORDS
    )

    if sentiment == "Positive":
        topic = "positive-tweets"
    elif sentiment == "Negative":
        topic = "negative-tweets"
    else:
        raise ValueError(sentiment)
    print(
        f"Sending message to topic: {TOPICS_COLOR[topic] + topic + Style.RESET_ALL}\n{tweet}\n"
    )
    producer.send(topic, tweet)
