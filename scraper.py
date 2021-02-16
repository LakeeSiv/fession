from facebook_scraper import get_posts
from PostClass import PostClass
import sqlite3

GROUP = "realoxfess"
# GROUP = "leedsfess"

conn = sqlite3.connect(f"{GROUP}.db")
c = conn.cursor()
# c.execute("""CREATE TABLE posts(postnum INT, text TEXT, sentiment FLOAT)""")

all_posts = get_posts(GROUP, pages=1000)
next(all_posts)  # ignore the page description


for post in (all_posts):
    Post = PostClass(post, GROUP)
    try:
        postnum = Post.get_post_number()
        text = Post.get_post_text()
        sentiment = Post.get_setiment()

        c.execute("""INSERT INTO posts VALUES(?,?,?)""",(postnum,text,sentiment))
    except:
        pass

    # print(Post.get_setiment(),Post.get_post_number(),"\n")
    # print(Post.get_post_text(),"\n","--------------------------------------------------------------------")

conn.commit()

c.execute("""SELECT postnum FROM posts""")
print(c.fetchall())