from m2ds_data_stream_kafka.sentiment_analysis import (
    positive_negative_words,
    text_preprocessing,
    classify_sentiment,
)


def test_positive_negative_words():
    positive_words, negative_words = positive_negative_words("data/")
    assert positive_words["french"][:5] == [
        "plus",
        "comme",
        "premier",
        "bien",
        "groupe",
    ]
    assert positive_words["english"][:5] == [
        "a+",
        "abound",
        "abounds",
        "abundance",
        "abundant",
    ]
    assert negative_words["french"][:5] == ["sur", "tres", "tout", "contre", "faire"]
    assert negative_words["english"][:5] == [
        "2-faced",
        "2-faces",
        "abnormal",
        "abolish",
        "abominable",
    ]


def test_text_preprocessing():
    english_string = "RT @joaquinlife: 36% positivity rate in the United States this week for COVID — more than 1/3 of every test is positive. Utterly mind-blowing. #covid https://www.google.com/"
    assert (
        text_preprocessing(english_string, "english")
        == "rt positivity rate united states week covid every test positive utterly mind blowing covid"
    )

    french_string = "RT @joaquinlife : 36 % de taux de positivité aux États-Unis cette semaine pour le COVID — plus d'1/3 des tests sont positifs. Complètement époustouflant. #covid https://www.google.com/"
    assert (
        text_preprocessing(french_string, "french")
        == "rt taux positivite etats unis cette semaine covid plus tests positifs completement epoustouflant covid"
    )


def test_classify_sentiment():
    positive_words, negative_words = positive_negative_words("data/")
    assert (
        classify_sentiment(
            "appreciates solidarity boring",
            "english",
            positive_words,
            negative_words,
        )
        == "Positive"
    )
    assert (
        classify_sentiment(
            "appreciates bad boring",
            "english",
            positive_words,
            negative_words,
        )
        == "Negative"
    )
    assert (
        classify_sentiment(
            "apprecie solidarite ennuyeux",
            "french",
            positive_words,
            negative_words,
        )
        == "Positive"
    )
    assert (
        classify_sentiment(
            "apprecie mal ennuyeux",
            "french",
            positive_words,
            negative_words,
        )
        == "Negative"
    )
