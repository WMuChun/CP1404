"""
CP1404/CP5632 - Practical 2 - password_stars
Name: Muchun Wan
ID: 14309726
"""

MINIMUM_PASSWORD_LENGTH = 6

def main():
    password = get_password()
    if len(password) >= MINIMUM_PASSWORD_LENGTH:
        print_stars(password)
    else:
        print("Please try again.")


def print_stars(password):
    print("*" * len(password))


def get_password():
    password = input(f"Enter a password with at least {MINIMUM_PASSWORD_LENGTH} characters: ")
    return password


main()