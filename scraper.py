from facebook_scraper import get_posts
from utils import post_number
import re

GROUP = "realoxfess"


all_posts = get_posts(GROUP, pages=20)
next(all_posts)  # ignore the page description


for post in (all_posts):
    text = post["text"]
    # print(text,"\n","--------------------------------------------------------------------")

    words = re.split("\n| ", text)

    print(post_number(words, GROUP))

    # print(words,"\n","--------------------------------------------------------------------")
