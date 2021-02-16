
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
