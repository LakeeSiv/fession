# import csv
from facebook_scraper import get_posts

"""
currently login does not work

with open("logindetails.csv","r") as file:
    details = csv.reader(file)
    for detail in details:

        email = detail[0]
        password = detail[1]

print(email,password)
"""

GROUP = "realoxfess"


all_posts = get_posts(GROUP, pages=2)
next(all_posts)  # ignore the page description

def post_number(hashtags,index):
    try:
        num = int(hashtags[index][11:])
        return num
    except ValueError:
        raise Exception("The string could not be converted into an integer")


for post in (all_posts):
    text = post["text"]
    # print(text,"\n","--------------------------------------------------------------------")

    hashtags = text.split("\n", 2)

    # if GROUP in hashtags[1]:
    post_num = post_number(hashtags,0)
    print(post_num)