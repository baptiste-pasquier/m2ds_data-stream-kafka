

# m2ds_data_stream_kafka

[![Build & Test](https://github.com/baptiste-pasquier/m2ds_data-stream-kafka/actions/workflows/main.yml/badge.svg)](https://github.com/baptiste-pasquier/m2ds_data-stream-kafka/actions/workflows/main.yml)

## Prerequities

- Sign-up for a Twitter developer account on this [link](https://developer.twitter.com/en/apply-for-access)
- Create a Bearer Token ([documentation](https://developer.twitter.com/en/docs/authentication/oauth-2-0/bearer-tokens))
- Set the environment variable `TWITTER_BEARER_TOKEN` with your Bearer Token
- Install and run Kafka ([documentation](https://kafka.apache.org/quickstart))

## Installation

Clone the repository and run inside :

- With `poetry` ([installation](https://python-poetry.org/docs/#installation)) :
```bash
poetry install
```

- With `pip` :
```bash
pip install -e .
```

## Usage

> **Warning**
> Each script must be run in a separate console

Stream tweets based on a keyword (defined [here](src\m2ds_data_stream_kafka\config.py)):
```bash
python script/ingest_tweets.py
```

Filter english and french tweets:
```bash
python script/filter_tweets.py
```

Classify tweet sentiment:
```bash
python script/sentiment_tweets.py
```

Archive all topics data:
```bash
python script/archives_tweets.py
```

Monitor all the Kafka topics:
```bash
python script/monitor-kafka.py
```