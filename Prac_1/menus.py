"""
CP1404/CP5632 - Practical 1 - menus
Name: Muchun Wan
ID: 14309726
"""

menu = """(H)ello
(G)oodbye
(Q)uit
"""
name = input("Enter name: ")
print(menu)

choice = input(">>> ").upper()

while choice != "Q":
    if choice == "H":
        print(f"Hello {name}")
    elif choice == "G":
        print(f"Goodbye {name}")
    else:
        print("Invalid choice")
    print(menu)
    choice = input(">>> ").upper()
print("Finished")