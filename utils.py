import csv


def post_number(hashtags, index):
    try:
        num = int(hashtags[index][11:])
        return num
    except ValueError:
        raise Exception("The string could not be converted into an integer")


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
