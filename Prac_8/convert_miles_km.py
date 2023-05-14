from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty

MILES_TO_KM = 1.60934
class MainApp(App):
    converted_miles = StringProperty()
    def build(self):
        self.title = "Convert Miles to KM"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root
    def convert_miles_to_km(self):
        try:
            miles = float(self.root.ids.input_miles.text)
        except ValueError:
            miles = 0.0
        km = miles * MILES_TO_KM
        self.converted_miles = str(km)

    def increment_miles(self, value):
        try:
            miles = float(self.root.ids.input_miles.text)
        except ValueError:
            miles = 0.0
        miles += value
        self.root.ids.input_miles.text = str(miles)

MainApp().run()