"""Passwprd check with Functions"""
# imports
MINIMUM_LENGTH = 6

def main():
    """Check passwords stars"""
    print_asterisks()


def print_asterisks():
    password = input("Password: ")
    while len(password) < MINIMUM_LENGTH:
        print("Password is too short")
        password = input("Password: ")


main()