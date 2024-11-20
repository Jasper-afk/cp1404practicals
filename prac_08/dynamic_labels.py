"""
CP1404 Practical 8,
Dynamic Kivy Widgets exercise.
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.uix.label import Label


class DynamicLabels(App):
    """Main Kivy App - create Labels from data."""
    output_label = StringProperty()

    def __init__(self):
        """Initialise main app data."""
        super().__init__()
        self.names = {"John", "Bob", "Mary", "Alice", "Bartunia", "James"}

    def build(self):
        """Build Kivy GUI."""
        self.title = "Dynamic Labels"
        self.root = Builder.load_file("dynamic_labels.kv")
        self.create_labels()

    def create_labels(self):
        """Create Labels from data and add them to GUI."""
        for name in self.names:
            label = Label(text=name)
            self.root.ids.main.add_widget(label)


DynamicLabels().run()
