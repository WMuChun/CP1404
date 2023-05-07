
from guitar import Guitar
def main():
    file_name = 'guitars.csv'
    guitars = read_guitars(file_name)

    guitars.sort()
    print("Guitars sorted by year:")
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

main()