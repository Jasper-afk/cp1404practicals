"""
CP1404 Practical 5 emails exercise.
estimated: 25 minutes
actual: 28 minutes
"""


def main():
    """Create a dictionary of emails to names."""
    email_to_name = {}
    email = input("Email: ")
    while email != "":
        name = extract_name(email)
        confirmation = input(f"Is your name {name}? (Y/n) ").upper()
        if confirmation != "Y" and confirmation != "":
            name = input("Name: ")
        email_to_name[email] = name
        email = input("Email: ")

    for email, name in email_to_name.items():
        print(f"{name} ({email})")


def extract_name(email: str) -> str:
    """Extract name from given email."""
    name = email.split("@")[0]
    parts = name.split(".")
    return " ".join(parts).title()


main()
