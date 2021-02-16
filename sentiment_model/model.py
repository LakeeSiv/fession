"""
All credit for the model goes to paoloripamonti's kaggle notebook on
Twitter Sentiment Analysis

Link to notebook:
https://www.kaggle.com/paoloripamonti/twitter-sentiment-analysis
"""


from keras.preprocessing.sequence import pad_sequences
from keras.models import load_model
import pickle
import os
import tensorflow as tf
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'


SEQUENCE_LENGTH = 300

# SENTIMENT
POSITIVE = "POSITIVE"
NEGATIVE = "NEGATIVE"
NEUTRAL = "NEUTRAL"
SENTIMENT_THRESHOLDS = (0.4, 0.7)


model = load_model("sentiment_model/model.h5")


with open('sentiment_model/tokenizer.pkl', 'rb') as handle:
    tokenizer = pickle.load(handle)


def decode_sentiment(score, include_neutral=True):
    if include_neutral:
        label = NEUTRAL
        if score <= SENTIMENT_THRESHOLDS[0]:
            label = NEGATIVE
        elif score >= SENTIMENT_THRESHOLDS[1]:
            label = POSITIVE

        return label
    else:
        return NEGATIVE if score < 0.5 else POSITIVE


def predict(text, include_neutral=True):

    # Tokenize text
    x_test = pad_sequences(
        tokenizer.texts_to_sequences(
            [text]), maxlen=SEQUENCE_LENGTH)
    # Predict
    score = model.predict([x_test])[0]
    # Decode sentiment
    label = decode_sentiment(score, include_neutral=include_neutral)

    return {"label": label, "score": float(score)}
