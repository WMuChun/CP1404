"""
Name:Muchun Wan
Date: 06/07/2023
GitHub URL: https://github.com/JCUS-CP1404/cp1404---travel-tracker---assignment-2-WMuChun
AND
https://github.com/WMuChun/cp1404practicals/tree/master/A2_RE
"""

import random


class Place:
    """Class representing a single travel destination."""

    UNVISITED = "n"
    VISITED = "v"

    def __init__(self, name, country, priority, visited=UNVISITED):
        """
        Constructor for Place class.
        Takes name, country and priority of the place, and its visited status.
        """
        self.name = name
        self.country = country
        self.priority = priority
        self.visited = visited

    def mark_as_visited(self):
        """Method to mark the place as visited."""
        self.visited = self.VISITED

    def mark_as_unvisited(self):
        """Method to mark the place as not visited."""
        self.visited = self.UNVISITED

    def is_visited(self):
        """Method to check if the place is visited."""
        return self.visited == self.VISITED

    def __str__(self):
        """Returns a string representation of the place object."""
        return f"{self.name},{self.country},{self.priority},{self.visited}"


class PlaceCollection:
    """Class representing a collection of travel destinations."""

    def __init__(self):
        """Constructor for PlaceCollection class."""
        self.places = []

    def load_places(self, filename):
        """
        Method to load places from a file.
        Takes the filename to load the places from.
        """
        with open(filename, 'r') as file:
            for line in file:
                name, country, priority, visited = line.strip().split(',')
                self.places.append(Place(name, country, int(priority), visited))

    def save_places(self, filename):
        """
        Method to save places to a file.
        Takes the filename to save the places to.
        """
        with open(filename, 'w') as file:
            for place in self.places:
                file.write(str(place) + '\n')

    def add_place(self, name, country, priority):
        """
        Method to add a place to the collection.
        Takes the name, country and priority of the place to be added.
        """
        place = Place(name, country, priority)
        self.places.append(place)
        print(f"{place.name} in {place.country} (priority {place.priority}) added to Travel Tracker")

    def mark_place_visited(self, place_number):
        """
        Method to mark a place as visited.
        Takes the number of the place to be marked.
        """
        place = self.places[place_number - 1]
        if not place.is_visited():
            place.mark_as_visited()
            print(f"{place.name} in {place.country} visited!")
        else:
            print(f"You have already visited {place.name}")

    def recommend_random_place(self):
        """
        Method to recommend a random unvisited place.
        """
        unvisited_places = [place for place in self.places if not place.is_visited()]
        if unvisited_places:
            random_place = random.choice(unvisited_places)
            print(f"Not sure where to visit next? \nHow about... {random_place.name} in {random_place.country}")
        else:
            print("No places left to visit!")

    def list_places(self):
        """
        Method to list all the places.
        """
        for i, place in enumerate(self.places, start=1):
            visited_status = '*' if not place.is_visited() else ''
            print(f"{visited_status:2}{i}. {place.name} in {place.country} {place.priority}")


def get_valid_number(prompt):
    """
    Helper function to get a valid number from the user.
    Takes the prompt string to display to the user.
    """
    while True:
        try:
            number = int(input(prompt))
            if number > 0:
                return number
            else:
                print("Number must be > 0")
        except ValueError:
            print("Invalid input; enter a valid number")


def print_menu():
    """
    Helper function to print the main menu for the application.
    """
    print("Menu:")
    print("L - List places")
    print("R - Recommend random place")
    print("A - Add new place")
    print("M - Mark a place as visited")
    print("Q - Quit")


def main():
    """
    Main function to run the application.
    """
    FILENAME = "places.csv"

    print("Travel Tracker 1.0 - by Muchun Wan")

    place_collection = PlaceCollection()
    place_collection.load_places(FILENAME)
    print(f"{len(place_collection.places)} places loaded from {FILENAME}")

    print_menu()
    menu_choice = input(">>> ").upper()

    while menu_choice != 'Q':
        if menu_choice == 'L':
            place_collection.list_places()
        elif menu_choice == 'R':
            place_collection.recommend_random_place()
        elif menu_choice == 'A':
            place_name = input("Name: ").strip()
            while not place_name:
                print("Input can not be blank")
                place_name = input("Name: ").strip()

            country_name = input("Country: ").strip()
            while not country_name:
                print("Input can not be blank")
                country_name = input("Country: ").strip()

            place_priority = get_valid_number("Priority: ")
            place_collection.add_place(place_name, country_name, place_priority)
        elif menu_choice == 'M':
            unvisited_places = [place for place in place_collection.places if not place.is_visited()]
            if not unvisited_places:
                print("No unvisited places")
            else:
                place_collection.list_places()
                place_number = get_valid_number("Enter the number of a place to mark as visited\n>>>")
                place_collection.mark_place_visited(place_number)
        else:
            print("Invalid menu choice")

        print_menu()
        menu_choice = input(">>> ").upper()

    place_collection.save_places(FILENAME)
    print(f"{len(place_collection.places)} places saved to {FILENAME}")
    print("Have a nice day :)")


if __name__ == '__main__':
    main()

