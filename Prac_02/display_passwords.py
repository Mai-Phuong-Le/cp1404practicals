
PASSWORD_LENGTH = 10

def main():
    """Display the password in *"""
    password = validate_password()
    print(len(password) * '*')

def validate_password() -> str:
    """Check the password length"""
    password = input("Enter password: ")
    while len(password) < PASSWORD_LENGTH:
        print("Invalid Password")
        password = input("Enter password: ")
    return password

main()