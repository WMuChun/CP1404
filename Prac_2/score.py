"""
CP1404/CP5632 - Practical 2 -score
Name: Muchun Wan
ID: 14309726
"""

import random

def main():
    score = float(input("Enter score: "))
    users_level = score_level(score)
    print(f"The {score} is {users_level}")
    random_score = random.randint(1, 100)
    print(f"The Random score is {random_score}")
    random_level = score_level(random_score)
    print(f"The Random Score {random_score} is {random_level}")

def score_level(score):
    if score < 0 or score > 100:
        message = "Invalid score"
    elif score >= 90:
        message ="Excellent"
    elif score >= 50:
        message = "Pass"
    else:
        message = "Bad"
    return message

main()