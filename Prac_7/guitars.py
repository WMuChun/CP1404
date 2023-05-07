
from guitar import Guitar
def main():
    file_name = 'guitars.csv'
    guitars = read_guitars(file_name)

    print("Guitars:")
    for guitar in guitars:
        print(guitar)

    print("\nEnter your new guitars:")
    while True:
        name = input("Name: ")
        if not name:
            break

        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        guitar = Guitar(name, year, cost)
        guitars.append(guitar)

    guitars.sort()
    write_guitars(file_name, guitars)

    print("\nGuitars sorted by year:")
    for guitar in guitars:
        print(guitar)


def read_guitars(file_name):
    guitars = []
    with open(file_name, 'r') as file:
        for line in file:
            name, year, cost = line.strip().split(',')
            guitar = Guitar(name, int(year), float(cost))
            guitars.append(guitar)
    return guitars


def write_guitars(file_name, guitars):
    with open(file_name, 'w') as file:
        for guitar in guitars:
            file.write(f"{guitar.name},{guitar.year},{guitar.cost}\n")

main()