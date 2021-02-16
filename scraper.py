from facebook_scraper import get_posts
from PostClass import PostClass

GROUP = "realoxfess"


all_posts = get_posts(GROUP, pages=20)
next(all_posts)  # ignore the page description


for post in (all_posts):
    Post = PostClass(post, GROUP)
    print(post["text"],"\n","--------------------------------------------------------------------")

    print(Post.get_post_number(),"\n","--------------------------------------------------------------------")
    print(Post.get_setiment())
