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

# load model
model = load_model("sentiment_model/model.h5")

# load tokenizer
with open('sentiment_model/tokenizer.pkl', 'rb') as handle:
    tokenizer = pickle.load(handle)


def predict(text, include_neutral=True):

    # Tokenize text
    x_test = pad_sequences(
        tokenizer.texts_to_sequences(
            [text]), maxlen=SEQUENCE_LENGTH)

    score = model.predict([x_test])[0]
    score = 2 * score - 1  # map score between [-1,1]

    return score[0]
