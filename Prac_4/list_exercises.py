def main():
    numbers = []
    for i in range(5):
        number = int(input("Number: "))
        numbers.append(number)
    print(numbers)

    first_number = numbers [0]
    last_number = numbers [-1]
    smallest_number = min(numbers)
    largest_number = max(numbers)
    average_number = sum(numbers) / len(numbers)

    print(f"The first_number is {first_number}\n"
        f"The last number is {last_number}\n"
        f"The smallest number is {smallest_number}\n"
        f"The largest number is {largest_number}\n"
        f"The average of the number is {average_number}")

    usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface',
                 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer',
                 'bob']
    user_name = input("Please Enter Username: ")
    if user_name in usernames:
        print("Access granted")
    else:
        print("Access denied")

main()