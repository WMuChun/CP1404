"""
CP1404/CP5632 - Practical 2 - score menu
Name: Muchun Wan
ID: 14309726
"""


MENU= """(G)et a valid score
(P)rint result
(S)how stars
(Q)uit
"""

def main():
    print(MENU)
    choice = input(">>> ").upper()
    while choice !="Q":
        if choice =="G":
            score = get_valid_score()
        elif choice == "P":
            score_result = print_result(score)
            print(f"The {score} is {score_result}")
        elif choice =="S":
            show_stars(score)
        else:
            print("Invalid Choice")
        print(MENU)
        choice = input(">>> ").upper()
    print("Bye Bye")


def get_valid_score():
    score = int(input("Enter a score between 0 and 100: "))
    if score < 0 or score > 100:
        print("Invalid score")
    else:
        return score

def print_result(score):
    if score >= 90:
        message ="Excellent"
    elif score >= 50:
        message = "Pass"
    else:
        message = "Bad"
    return message

def show_stars(score):
    print("*" * score)

main()