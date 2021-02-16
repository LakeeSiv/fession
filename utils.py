import csv


def post_number(words, GROUP):
    """
    Args:
    words: list of words
    GROUP: group name

    Returns:
    post_num: post number

    finds the postnumber by searching for the largest number
    in the GROUP hashtag, which normally looks like
    f"#{GROUP}{post_num}"
    """
    post_num = 0
    for word in words:
        word = word.lower()
        if GROUP in word:
            number = int(word[1 + len(GROUP):])
            post_num = max(post_num, number)

    return post_num


def get_credentials():
    """
    currently login does not work
    """

    with open("logindetails.csv", "r") as file:
        details = csv.reader(file)
        for detail in details:

            email = detail[0]
            password = detail[1]

        return (email, password)
