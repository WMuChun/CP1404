"""
import random

length = int(input("Length: "))
width = random.randint(1,length)
print(f"Width: {width}")
area = length * width
print(f"Area: {area}")

"""

# def main():
#     print_line(20)
#     print("Welcome!")
#     print_line(8)
#
# def print_line(length):
#     print("*" * length)
#
# main()

print_grid(3,7)
def print_grid(number_of_rows, number_of_columns):
    for i in range(number_of_columns):
        print("*", end=' ')
    