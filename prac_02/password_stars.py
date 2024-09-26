minimum_password_length = 10
password = input('Enter password: ')
while len(password) < minimum_password_length:
    print(f"Password must be at least {minimum_password_length} characters long.")
    password = input('Enter password: ')
print("*" * len(password))