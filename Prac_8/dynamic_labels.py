from kivy.app import App
from kivy.uix.label import Label
from kivy.lang import Builder


class MainApp(App):
    def build(self):
        self.title = "Dynamic Labels"
        self.root = Builder.load_file('dynamic_labels.kv')

        names = ["Muchun", "David", "Lewis", "Bob", "Alice"]

        for name in names:
            label = Label(text=name)
            self.root.ids.main.add_widget(label)
        return self.root


MainApp().run()
