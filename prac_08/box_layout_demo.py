"""
CP1404 Practical 8,
Modify Existing GUI Program exercise.
"""

from kivy.app import App
from kivy.lang import Builder


class BoxLayoutDemo(App):
    def build(self):
        """Build Kivy App GUI."""
        self.title = "Box Layout Demo"
        self.root = Builder.load_file('box_layout.kv')
        return self.root

    def handle_greet(self):
        """Display a greeting to the user when the 'Greet' button is pressed."""
        print('test')
        self.root.ids.output_label.text = f"Hello {self.root.ids.input_name.text}"

    def clear_all(self):
        """Clear all text boxes of their values."""
        print('cleared!')
        self.root.ids.output_label.text = "Enter your name"
        self.root.ids.input_name.text = ""

BoxLayoutDemo().run()
