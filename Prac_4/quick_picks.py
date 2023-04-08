import random
MINIMUM_NUMBER = 1
MAXIMUM_NUMBER = 45
NUMBERS_IN_LINE = 6
def main():
    lines = int(input("How many quick picks: "))
    for line in range(lines):
        numbers = []
        while len(numbers) < NUMBERS_IN_LINE:
            number = random.randint(MINIMUM_NUMBER,MAXIMUM_NUMBER)
            if number not in numbers:
                numbers.append(number)

        numbers.sort()
        print (" ".join(str(number)for number in numbers))

main()