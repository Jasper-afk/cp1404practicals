"""CP1404 practical 2 password validation program."""

MINIMUM_PASSWORD_LENGTH = 10


def main():
    """Get a password from the user and print it masked."""
    password = get_valid_password(MINIMUM_PASSWORD_LENGTH)
    print_password_mask(password)


def print_password_mask(password: str) -> None:
    """Print a password mask multiplied by password length."""
    print("*" * len(password))


def get_valid_password(minimum_password_length) -> str:
    """Get a valid password from the user."""
    password = input('Enter password: ')
    while len(password) < minimum_password_length:
        print(f"Password must be at least {minimum_password_length} characters long.")
        password = input('Enter password: ')
    return password


main()
