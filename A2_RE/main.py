"""
Name:Muchun Wan
Date: 06/10/2023

Brief Project Description:The "Travel Tracker" is a simple console-based Python application designed to help users keep
track of their travel goals. The application manages a list of travel destinations, with each destination characterized
by its name, country, priority (a number representing the place's importance), and a visited status flag indicating
whether the user has visited the place or not.

GitHub URL: https://github.com/JCUS-CP1404/cp1404---travel-tracker---assignment-2-WMuChun
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from place import Place
from placecollection import PlaceCollection

# Definitions for visited and unvisited status
UNVISITED = "n"
VISITED = "v"


class TravelTrackerApp(App):

    def build(self):
        # Setting the title of the app and loading the UI file
        self.title = "Travel Tracker"
        self.root = Builder.load_file('app.kv')

        # Creating a place collection and loading places from the csv
        self.place_collection = PlaceCollection()
        self.place_collection.load_places('places.csv')

        # Sorting the places by name and binding the text change of the sort spinner
        self.place_collection.sort('name')
        self.root.ids.sort_spinner.bind(text=self.sort_text_change)

        # Updating the grid with the current places
        self.update_grid()

        return self.root

    def clear_fields(self):
        # Clearing all the fields
        self.root.ids.name_input.text = ''
        self.root.ids.country_input.text = ''
        self.root.ids.priority_input.text = ''

    def sort_text_change(self, spinner, text):
        # Sorting the places when the sort spinner text changes and updating the grid
        self.place_collection.sort(text.lower())
        self.update_grid()

    def update_grid(self):
        # Clearing the grid and adding buttons for each place, changing the status bar
        self.root.ids.places_grid.clear_widgets()
        i = 0
        for place in self.place_collection.places:
            status = " (Visited)" if place.visited == VISITED else ""
            if status == "":
                i = i+1
            btn = Button(text=f"{place.name} in {place.country}, priority {place.priority}{status}",background_color=(0.2, 0.2, 0.2, 1) if status==" (Visited)" else (0,1,1, 1))
            btn.bind(on_release=self.change_place_status)
            self.root.ids.places_grid.add_widget(btn)
        self.root.ids.top_status_label.text = f'Places to visit: {i}'

    def change_place_status(self, instance):
        # Changing the visited status of a place and updating the grid and saving the places
        name, remainder = instance.text.split(" in ")
        country, remainder = remainder.split(", priority ")
        data = remainder.split(" (")
        if len(data)>1:
            priority, status = data
        else:
            priority, status = data[0],"Unvisited)"
        status = status[:-1]
        for place in self.place_collection.places:
            if place.name == name and place.country == country:
                place.visited = VISITED if status == "Unvisited" else UNVISITED
                if place.visited == VISITED:
                    self.root.ids.bottom_status_label.text=f'You visited {place.name}.Great travelling'
                break
        self.place_collection.sort(self.root.ids.sort_spinner.text.lower())
        self.update_grid()
        self.place_collection.save_places()

    def add_place(self):
        # Adding a place, updating the grid and saving the places, validating the inputs
        name = self.root.ids.name_input.text
        country = self.root.ids.country_input.text
        priority = self.root.ids.priority_input.text
        if name is None or len(name.strip())==0 or country is None or len(country.strip()) == 0 \
            or priority is None or len(priority.strip())==0:
            self.root.ids.bottom_status_label.text = 'all column must be not none'
            return
        if not priority.isnumeric():
            self.root.ids.bottom_status_label.text='please input a number'
            return
        if int(priority)<1:
            self.root.ids.bottom_status_label.text='priority must greater than zero'
            return
        self.place_collection.add_place(Place(name,country,int(priority),'n'))
        self.place_collection.sort(self.root.ids.sort_spinner.text.lower())
        self.update_grid()
        self.place_collection.save_places()
        self.clear_fields()
        self.root.ids.bottom_status_label.text = 'Welcome to Travel Tracker'


if __name__ == '__main__':
    # Running the app
    TravelTrackerApp().run()


