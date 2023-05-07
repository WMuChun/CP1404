"""
Word Occurrences
Estimate: 60 minutes
Actual:   42 minutes
"""

name_to_emails={}

while True:
    email = input("Email: ")
    if email =="":
        break

    name = email.split('@')[0].title()
    confirm_name = input(f"Is your name {name}? (Y/n)")

    if confirm_name !="y":
        name = input("Name: ")
    name_to_emails[email] = name

print("User:")
for email, name in name_to_emails.items():
    print(f"{name} ({email})")