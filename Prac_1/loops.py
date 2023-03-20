"""
CP1404/CP5632 - Practical 1 - loops
Name: Muchun Wan
ID: 14309726
"""

for i in range(1, 21, 2):
    print(i, end=' ')
print()

"""
A. Count in 10s from 0 to 100
"""

for i in range (0, 101, 10):
    print(i, end=' ')
print()

"""
B. Count down from 20 to 1
"""

for i in range (20, 0, -1):
    print(i, end=' ')
print()

"""
C. Print n stars.
"""
numbers_of_stars = int(input("Number of stars: "))
for i in range (numbers_of_stars):
    print("*", end=' ')
print()

"""
D. Print n lines of increasing stars.
"""
numbers_of_stars = int(input("Number of stars: "))
for i in range(1, numbers_of_stars+1):
    print("*" * i)
print()
