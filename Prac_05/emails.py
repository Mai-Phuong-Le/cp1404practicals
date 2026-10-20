
SPECIAL_CHARACTER = "@"

def main():
    """Create dictionary of emails-to-names."""
    email_to_name = {}

    email = input("Enter email (Email must contain @): ")
    while email != "":
        while SPECIAL_CHARACTER not in email:
            print("Error")
            email = input("Enter email (Email must contain @): ")

        name = get_name(email)
        confirmation = input(f"Is your name {name}? (Y/n) ").upper()
        if confirmation.upper() != "Y" and confirmation != "":
            name = input("Name: ")
        email_to_name[email] = name
        email = input("Enter email (Email must contain @): ")

def print_email(email_to_name):
    for email, name in email_to_name.items():
        print(f"{name} ({email})")

def get_name(email):
    """Extract expected name from email address."""
    print(email)
    prefix = email.split(SPECIAL_CHARACTER)[0]
    print(prefix)
    parts = prefix.split('.')
    print(parts)
    name = " ".join(parts).title()
    return name

