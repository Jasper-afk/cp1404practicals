"""CP1404 practical 2 password validation program."""

MINIMUM_PASSWORD_LENGTH = 10


def main():
    """Get a password from the user and print it masked."""
    password = get_password()
    print_password_mask(password)


def print_password_mask(password: str) -> None:
    """Print a password mask multiplied by password length."""
    print("*" * len(password))


def get_password() -> str:
    """Get a valid password from the user."""
    password = input('Enter password: ')
    while len(password) < MINIMUM_PASSWORD_LENGTH:
        print(f"Password must be at least {MINIMUM_PASSWORD_LENGTH} characters long.")
        password = input('Enter password: ')
    return password


main()
