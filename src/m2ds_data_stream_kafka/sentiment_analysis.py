import re
from pathlib import Path

import nltk
import unidecode
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

nltk.download("punkt")
nltk.download("stopwords")


def positive_negative_words(data_path):

    positive_words = {"english": [], "french": []}
    negative_words = {"english": [], "french": []}

    for language in ["french", "english"]:
        if language == "french":
            encoding = "utf8"
        else:
            encoding = "windows-1252"
        with open(
            Path(data_path, f"positive-words-{language}.txt"), "r", encoding=encoding
        ) as f:
            for line in f:
                if not line.startswith(";"):
                    word = line.strip()
                    word = unidecode.unidecode(word)
                    if len(word) > 0:
                        positive_words[language].append(word)
        with open(
            Path(data_path, f"negative-words-{language}.txt"), "r", encoding=encoding
        ) as f:
            for line in f:
                if not line.startswith(";"):
                    word = line.strip()
                    word = unidecode.unidecode(word)
                    if len(word) > 0:
                        negative_words[language].append(word)

    return positive_words, negative_words


def text_preprocessing(string, language):
    # remove accent
    string = unidecode.unidecode(string)

    # lowercase
    string = string.lower()

    # remove extra newlines
    string = re.sub(r"[\r|\n|\r\n]+", " ", string)

    # remove @tag
    string = re.sub(r"@[\S]+", "", string)

    # remove URL
    string = re.sub("https?://[\S]+", "", string)

    # remove hashtag and numbers
    string = re.sub("[^a-zA-Z]", " ", string)

    # tokenization
    string = word_tokenize(string)

    # remove stop words
    string = [word for word in string if word not in stopwords.words(language)]

    string = " ".join(word for word in string)

    return string


def classify_sentiment(string, language, positive_words, negative_words):
    words = string.split()
    n_positive = 0
    n_negative = 0
    for word in words:
        if word in positive_words[language]:
            n_positive += 1
        if word in negative_words[language]:
            n_negative += 1

    if n_positive >= n_negative:
        return "Positive"
    else:
        return "Negative"
