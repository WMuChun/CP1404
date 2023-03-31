"""
Question 1
"""

name = input("You Name Is: ")

in_file = open("name.txt",'w')
print(name, file=in_file)
in_file.close()
print("Name saved to file.")

"""
Question 2
"""
out_file = open("name.txt", 'r')
read_name = out_file.readline()
out_file.close()
print(f"You Name is {read_name}")

"""
Question 3
"""
number_file = open("numbers.txt", 'r')
numbers = number_file.readlines()
number_file.close()
first_number = int(numbers[0].strip())
second_number = int(numbers[1].strip())
total_number = first_number + second_number
print(f"Result: {total_number}")

"""
Question 4
"""

numbers_file = open("numbers.txt", 'r')
lines = numbers_file.readlines()
numbers_file.close()
total = 0
for block in lines:
    number = int(block.strip())
    total += number
print(f"The total is: {total}")