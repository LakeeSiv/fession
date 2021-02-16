from facebook_scraper import get_posts
from PostClass import PostClass
import sqlite3

GROUP = "realoxfess"
# GROUP = "leedsfess"

conn = sqlite3.connect(f"{GROUP}.db")
c = conn.cursor()
# c.execute("""CREATE TABLE posts(postnum INT, text TEXT, sentiment FLOAT)""")


c.execute("""SELECT postnum FROM posts""")
post_num_list = c.fetchall()
post_num_list = [tuple[0] for tuple in post_num_list]
max_post_num = max(post_num_list)


all_posts = get_posts(GROUP, pages=100)
next(all_posts)  # ignore the page description


for post in (all_posts):
    Post = PostClass(post, GROUP)
    try:
        postnum = Post.get_post_number()
        print(postnum, "\n")

        if postnum <= max_post_num:
            print("Added all the new posts to the database")
            break

        text = Post.get_post_text()
        sentiment = Post.get_setiment()

        c.execute("""INSERT INTO posts VALUES(?,?,?)""",
                  (postnum, text, sentiment))
    except BaseException:
        pass

    # print(Post.get_setiment(),Post.get_post_number(),"\n")
    # print(Post.get_post_text(),"\n","--------------------------------------------------------------------")

conn.commit()
