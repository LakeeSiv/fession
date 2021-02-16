import csv
import re


class PostClass:

    def __init__(self, post, GROUP):

        self.posttext = post["text"]
        self.GROUP = GROUP

    def get_post_number(self) -> int:
        """
        finds the postnumber by searching for the largest number
        in the GROUP hashtag, which normally looks like
        f"#{GROUP}{post_num}"

        Returns:
            post_num: post number
        """
        words = re.split("\n| ", self.posttext)
        post_num = 0
        for word in words:
            word = word.lower()
            if self.GROUP in word:
                number = int(word[1 + len(self.GROUP):])
                post_num = max(post_num, number)

        return post_num

    def get_post_text(self) -> str:
        """
        Removes the hastags from the post and returns
        all the text as a string

        Returns:
            text
        """
        words = re.split("\n| ", self.posttext)
        post_text_list = [
            word for word in words if f"#{self.GROUP}" not in word.lower()]

        text = " ".join(post_text_list)

        return text


def get_credentials() -> tuple:
    """
    !Note: the login feature in the facebook_scraper library
    is currently broken!

    Returns:
        (email,password): tuples contaning email and password as strings
    """

    with open("logindetails.csv", "r") as file:
        details = csv.reader(file)
        for detail in details:

            email = detail[0]
            password = detail[1]

        return (email, password)
