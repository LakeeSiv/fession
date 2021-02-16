import csv
import re
from textblob import TextBlob
from textblob.sentiments import NaiveBayesAnalyzer, PatternAnalyzer
from sentiment_model.model import predict


class PostClass:

    def __init__(self, post, GROUP):

        self.post_text = post["text"]
        self.GROUP = GROUP

    def get_post_number(self) -> int:
        """
        finds the postnumber by searching for the largest number
        in the GROUP hashtag, which normally looks like
        f"#{GROUP}{post_num}"

        Returns:
            post_num: post number
        """
        words = re.split("\n| ", self.post_text)
        post_num = 0
        for word in words:
            word = word.lower()
            if self.GROUP in word and any(c.isdigit() for c in word):

                number = int(word[1 + len(self.GROUP):])
                post_num = max(post_num, number)

        return post_num

    def get_post_text(self) -> str:
        """
        Removes the hastags from the post and returns
        all the text as a string

        Returns:
            text: text w/o hashtags
        """

        words = re.split("\n| ", self.post_text)
        post_text_list = [
            word for word in words if f"#{self.GROUP}" not in word.lower()]

        text = " ".join(post_text_list)

        return text

    def get_setiment(self):
        """
        Calcultes the sentiment of a text using the avergae of
        2 different methods of sentiment analysis (TextBlob Libary, Twitter Sentiment Analysis model from Kaggle).

        Returns:
            score: float in range (-1,1), where 1 is postive and -1 is negative

        """
        sentiment_model = predict(self.get_post_text())
        sentiment_textblob = (
            TextBlob(
                self.get_post_text(),
                analyzer=PatternAnalyzer())).sentiment

        return (sentiment_model + sentiment_textblob[0]) / 2
