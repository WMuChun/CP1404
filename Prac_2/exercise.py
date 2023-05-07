"""
import random

length = int(input("Length: "))
width = random.randint(1,length)
print(f"Width: {width}")
area = length * width
print(f"Area: {area}")

"""

valid_input = False
while not valid_input:
    try:
        age = int(input("Age: "))
        valid_input = True
    except ValueError:
        print("Invalid (not an integer)")
print("Next year you will be", age + 1)
# x = 5
# y = 10
# if x <10:
#     if y > 10 and x > 5:
#         print("A")
# else:
#     print("B")
# def main():
#     print_line(20)
#     print("Welcome!")
#     print_line(8)
#
# def print_line(length):
#     print("*" * length)
#
# main()

# print_grid(3,7)
# def print_grid(number_of_rows, number_of_columns):
#     for i in range(number_of_columns):
#         print("*", end=' ')
#