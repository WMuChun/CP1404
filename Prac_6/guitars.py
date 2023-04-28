from Prac_6.guitar import Guitar

def main():
    guitars = []

    print("My Guitars!")
    guitar_name = input("Name: ")

    while guitar_name != "":
        guitar_year = int(input("Year: "))
        guitar_cost = float(input("Cost: $"))

        guitar = Guitar(guitar_name, guitar_year, guitar_cost)
        guitars.append(guitar)
        guitar_name = input("Name: ")

    print("These are my guitars:")
    for i, guitar in enumerate(guitars, 1):
        vintage_string = "(vintage)" if guitar.is_vintage() else ""
        print(f"Guitar {i}:{guitar.name} ({guitar.year}), worth ${guitar.cost:10,.2f}{vintage_string}")

main()