import csv


def post_number(words: list, GROUP: str) -> int:
    """
    finds the postnumber by searching for the largest number
    in the GROUP hashtag, which normally looks like
    f"#{GROUP}{post_num}"

    Args:
        words: list of words in a post
        GROUP: unifession group name

    Returns:
        post_num: post number
    """
    post_num = 0
    for word in words:
        word = word.lower()
        if GROUP in word:
            number = int(word[1 + len(GROUP):])
            post_num = max(post_num, number)

    return post_num


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
